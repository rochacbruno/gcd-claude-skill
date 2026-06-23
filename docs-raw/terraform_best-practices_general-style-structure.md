# Best practices for general style and structure

Source: https://berlin.devsitetest.how/docs/terraform/best-practices/general-style-structure
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/terraform/tpc-differences) for more details.














- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Documentation

](https://berlin.devsitetest.how/docs)






- 








[

Developer tools

](https://berlin.devsitetest.how/docs/costs-usage)






- 








[

Terraform on Google Cloud

](https://berlin.devsitetest.how/docs/terraform)






- 








[

Guides

](https://berlin.devsitetest.how/docs/terraform/terraform-overview)












# Best practices for general style and structure 






- On this page ** 
- [ Follow a standard module structure ](#module-structure)
- [ Adopt a naming convention ](#naming-convention)
- [ Use variables carefully ](#variables)
- [ Expose outputs ](#outputs)
- [ Use data sources ](#data-sources)
- [ Limit the use of custom scripts ](#custom-scripts)
- [ Include helper scripts in a separate directory ](#helper-scripts)
- [ Put static files in a separate directory ](#static-files)
- [ Protect stateful resources ](#stateful-resources)
- [ Use built-in formatting ](#built-in-formatting)

- [ Limit the complexity of expressions ](#expressions)

- [ Use count for conditional values ](#count)
- [ Use for_each for iterated resources ](#for_each)
- [ Publish modules to a registry ](#publish)
- [ What's next ](#whats-next)
- 










This document provides basic style and structure recommendations for your
Terraform configurations. These recommendations apply to reusable Terraform
modules and to root configurations.

This guide is not an introduction to Terraform. For an introduction to using
Terraform with Google Cloud Dedicated in Germany, see
[Get started with Terraform](/docs/terraform/get-started-with-terraform).

## Follow a standard module structure 

- Terraform modules must follow the
[standard module structure](https://www.terraform.io/docs/modules/create.html).

- Start every module with a `main.tf` file, where resources are located by
default.

- In every module, include a `README.md` file in Markdown format. In the
`README.md` file, include basic documentation about the module.

- Place examples in an `examples/` folder, with a separate subdirectory for
each example. For each example, include a detailed `README.md` file.

- Create logical groupings of resources with their own files and
descriptive names, such as `network.tf`, `instances.tf`, or `loadbalancer.tf`.

- Avoid giving every resource its own file. Group resources by
their shared purpose. For example, combine `google_dns_managed_zone`
and `google_dns_record_set` in `dns.tf`.

- In the module's root directory, include only Terraform
(`*.tf`) and repository metadata files (such as `README.md` and
`CHANGELOG.md`).

- Place any additional documentation in a `docs/` subdirectory.

## Adopt a naming convention

- 

Name all configuration objects using underscores to delimit multiple
words. This practice ensures consistency with the naming convention for
resource types, data source types, and other predefined values. This
convention does not apply to name
[arguments](https://www.terraform.io/docs/glossary#argument).

Recommended: 


```
resource "google_compute_instance" "web_server"** {
name = "web-server"
}
```


Not recommended: 


```
resource "google_compute_instance" **"web-server"** {
name = "web-server"
}
```


- 

To simplify references to a resource that is the only one of its type
(for example, a single load balancer for an entire module), name the
resource `main`.

- It takes extra mental work to remember
`some_google_resource.my_special_resource.id` versus
`some_google_resource.main.id`.

- 

To differentiate resources of the same type from each other (for example,
`primary` and `secondary`), provide meaningful resource names.

- 

Make resource names singular.

- 

In the resource name, don't repeat the resource type.
For example:

Recommended: 


```
resource "google_compute_global_address" "main" { ... }
```


Not recommended: 


```
resource "google_compute_global_address" "main_global_address" { … }
```


## Use variables carefully

- Declare all variables in `variables.tf`.

- Give variables descriptive names that are relevant to their usage or
purpose:

- Inputs, local variables, and outputs representing numeric
values—such as disk sizes or RAM size—*must* be named with
units (such as `ram_size_gb`). Google Cloud Dedicated APIs don't have standard
units, so naming variables with units makes the expected
input unit clear for configuration maintainers.

- For units of storage, use binary unit prefixes (powers of 1024)—`kibi`,
`mebi`, `gibi`. For all other units of measurement, use decimal
unit prefixes (powers of 1000)—`kilo`, `mega`, `giga`. This usage
matches the usage within Google Cloud Dedicated.

- To simplify conditional logic, give boolean variables positive names—for
example, `enable_external_access`.

- Variables must have descriptions. Descriptions are automatically
included in a published module's auto-generated documentation.
Descriptions add additional context for new developers that descriptive
names cannot provide.

- Give variables defined types.

- When appropriate, provide default values:

- For variables that have environment-independent values (such as disk
size), provide default values.

- For variables that have environment-specific values (such as
`project_id`), don't provide default values. This way, the calling module
must provide meaningful values.

- Use empty defaults for variables (like empty strings or lists) only when
leaving the variable empty is a valid preference that the underlying APIs
don't reject.

- Be judicious in your use of variables. Only parameterize values that
must vary for each instance or environment. When deciding whether to expose
a variable, ensure that you have a concrete use case for changing that
variable. If there's only a small chance that a variable might be needed,
don't expose it.

- Adding a variable with a default value is backwards-compatible.

- Removing a variable is backwards-incompatible.

- In cases where a literal is reused in multiple places, you can use a
[local value](https://www.terraform.io/docs/configuration/locals.html)
without exposing it as a variable.

## Expose outputs

- Organize all outputs in an `outputs.tf` file.

- Provide meaningful descriptions for all outputs.

- Document output descriptions in the `README.md` file. Auto-generate
descriptions on commit with tools like
[terraform-docs](https://github.com/terraform-docs/terraform-docs).

- Output all useful values that root modules might need to refer to or share.
Especially for open source or heavily used modules, expose all outputs that
have potential for consumption.

- 

Don't pass outputs directly through input variables, because doing so
prevents them from being properly added to the dependency graph. To ensure
that
[implicit dependencies](https://learn.hashicorp.com/terraform/getting-started/dependencies.html)
are created, make sure that outputs reference attributes from resources.
Instead of referencing an input variable for an instance directly, pass
the attribute through as shown here:

Recommended: 


```
output "name" {
description = "Name of instance"
value = google_compute_instance.main.name
}
```


Not recommended: 


```
output "name" {
description = "Name of instance"
value = var.name
}
```


## Use data sources

- Put
[data sources](https://www.terraform.io/docs/configuration/data-sources.html)
next to the resources that reference them. For example, if you are fetching
an image to be used in launching an instance, place it alongside the
instance instead of collecting data resources in their own file.

- If the number of data sources becomes large, consider moving them to a
dedicated `data.tf` file.

- To fetch data relative to the current environment, use variable or resource
[interpolation](https://www.terraform.io/language/expressions/strings#interpolation).

## Limit the use of custom scripts

- Use scripts only when necessary. The state of resources created
through scripts is not accounted for or managed by Terraform.

- Avoid custom scripts, if possible. Use them only when Terraform
resources don't support the desired behavior.

- Any custom scripts used must have a clearly documented reason for
existing and ideally a deprecation plan.

- Terraform can call custom scripts through provisioners, including the
local-exec provisioner.

- Put custom scripts called by Terraform in a `scripts/` directory.

## Include helper scripts in a separate directory

- Organize helper scripts that aren't called by Terraform in a
`helpers/` directory.

- Document helper scripts in the `README.md` file with explanations and
example invocations.

- If helper scripts accept arguments, provide argument-checking and
`--help` output.

## Put static files in a separate directory

- Static files that Terraform references but doesn't execute (such as
startup scripts loaded onto Compute Engine instances) must be organized
into a `files/` directory.

- Place lengthy HereDocs in external files, separate from their HCL.
Reference them with the
[`file()` function](https://www.terraform.io/language/functions/file).

- For files that are read in by using the Terraform
[`templatefile` function](https://www.terraform.io/docs/configuration/functions/templatefile.html),
use the file extension `.tftpl`.

- Templates must be placed in a `templates/` directory.

## Protect stateful resources

For stateful resources, such as databases, ensure that
[deletion protection](https://www.terraform.io/language/meta-arguments/lifecycle)
is enabled. For example:


```
resource "google_sql_database_instance" "main" { 
name = "primary-instance" 
settings { 
tier = "D0" 
} 

lifecycle { 
prevent_destroy = true 
} 
} 
```


## Use built-in formatting

All Terraform files must conform to the standards of `terraform fmt`.

### Limit the complexity of expressions

- Limit the complexity of any individual interpolated expressions. If
many functions are needed in a single expression, consider splitting it out
into multiple expressions by using
[local values](https://www.terraform.io/docs/configuration/locals.html).

- Never have more than one ternary operation in a single line. Instead,
use multiple local values to build up the logic.

## Use `count` for conditional values

To instantiate a resource conditionally, use the
[`count`](https://www.terraform.io/language/meta-arguments/count) meta-argument.
For example:


```
variable "readers" { 
description = "..." 
type = list
default = [] 
} 

resource "resource_type" "reference_name" { 
// Do not create this resource if the list of readers is empty.
count = length ( var.readers ) == 0 ? 0 : 1 
...
} 
```


Be sparing when using user-specified variables to set the `count` variable for
resources. If a resource attribute is provided for such a variable (like
`project_id`) and that resource does not yet exist, Terraform can't
generate a plan. Instead, Terraform reports the error
[`value of count cannot be computed`](https://github.com/hashicorp/terraform/issues/17421).
In such cases, use a separate `enable_x` variable to compute the
conditional logic.

## Use `for_each` for iterated resources

If you want to create multiple copies of a resource based on an input resource,
use the
[`for_each`](https://www.terraform.io/language/meta-arguments/for_each)
meta-argument.

## Publish modules to a registry

- 

**Reusable modules**: Publish reusable modules to a
[module registry](https://www.terraform.io/internals/module-registry-protocol).

- 

**Open source modules**: Publish open source modules to the
[Terraform Registry](https://registry.terraform.io/).

- 

**Private modules**: Publish private modules to a
[private registry](https://www.terraform.io/cloud-docs/registry).

## What's next

- Learn about [best practices when using reusable modules](/docs/terraform/best-practices/reusable-modules).

- Learn about [best practices when using Terraform root modules](/docs/terraform/best-practices/root-modules).