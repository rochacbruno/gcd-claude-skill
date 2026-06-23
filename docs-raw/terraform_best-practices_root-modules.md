# Best practices for root modules

Source: https://berlin.devsitetest.how/docs/terraform/best-practices/root-modules
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












# Best practices for root modules 






- On this page 
- [ Minimize the number of resources in each root module ](#minimize-resources)
- [ Use separate directories for each application ](#separate-directories)
- [ Split applications into environment-specific subdirectories ](#subdirectories)
- [ Use environment directories ](#environment-directories)
- [ Expose outputs through remote state ](#outputs-remote-state)
- [ Pin to minor provider versions ](#minor-provider-versions)
- [ Store variables in a tfvars file ](#tfvars)
- [ Check in .terraform.lock.hcl file ](#lockfile)
- [ What's next ](#whats-next)
- 










This document provides guidelines and recommendations to consider
when using root modules.

Root configurations or root modules are the working directories from which you
run the Terraform CLI. Make sure that root configurations adhere to the
following standards (and to the previous Terraform guidelines where applicable).
Explicit recommendations for root modules supersede the general guidelines.

This guide is not an introduction to Terraform. For an introduction to using
Terraform with Google Cloud Dedicated in Germany, see [Get started with
Terraform](/docs/terraform/get-started-with-terraform).

## Minimize the number of resources in each root module 

It is important to keep a single root configuration from growing too large, with
too many resources stored in the same directory and state. *All* resources in a
particular root configuration are refreshed every time Terraform is run. This
can cause slow execution if too many resources are included in a single state. A
general rule: Don't include more than 100 resources (and ideally only a few
dozen) in a single state.

## Use separate directories for each application

To manage applications and projects independently of each other, put resources
for each application and project in their own Terraform directories. A service
might represent a particular application or a common service such as shared
networking. Nest all Terraform code for a particular service under *one*
directory (including subdirectories).

## Split applications into environment-specific subdirectories

When deploying services in Google Cloud Dedicated, split the Terraform
configuration for the service into two top-level directories: a `modules`
directory that contains the actual configuration for the service, and an
`environments` directory that contains the root configurations for each
environment.


```
-- SERVICE-DIRECTORY/ 
-- OWNERS 
-- modules/ 
-- service-name>/ 
-- main.tf 
-- variables.tf 
-- outputs.tf 
-- provider.tf 
-- README 
-- ... other… 
-- environments/ 
-- dev/ 
-- backend.tf 
-- main.tf 

-- qa/ 
-- backend.tf 
-- main.tf 

-- prod/ 
-- backend.tf 
-- main.tf 
```


## Use environment directories

To share code across environments, reference modules. Typically, this might be a
service module that includes the base shared Terraform configuration for the
service. In service modules, hard-code common inputs and only require
environment-specific inputs as variables.

Each environment directory must contain the following files:

- A `backend.tf` file, declaring the Terraform
[backend](https://www.terraform.io/docs/backends/) 
state location (typically, [Cloud Storage](/storage))

- A `main.tf` file that instantiates the service module

Each environment directory (`dev`, `qa`, `prod`) corresponds to a default
[Terraform workspace](https://www.terraform.io/docs/state/workspaces) 
and deploys a version of the service to that environment. These workspaces
isolate environment-specific resources into their own contexts. *Use only the
default workspace*.

Having multiple
[CLI workspaces](https://developer.hashicorp.com/terraform/language/state/workspaces) 
within an environment isn't recommended for the following reasons:

- It can be difficult to inspect the configuration in each workspace.

- Having a single shared backend for multiple workspaces isn't recommended
because the shared backend becomes a single point of failure if it is used for
environment separation.

- While code reuse is possible, code becomes harder to read having to switch
based on the current workspace variable (for example,
`terraform.workspace == "foo" ? this : that`).

For more information, see the following:

- [Workspaces](https://www.terraform.io/language/state/workspaces#when-to-use-multiple-workspaces) 

- [When Not to Use Multiple Workspaces](https://developer.hashicorp.com/terraform/cli/workspaces#when-not-to-use-multiple-workspaces) 

## Expose outputs through remote state

Make sure you're exposing useful outputs of module instances from a root module.

For example, the following code snippet passes through the project ID output
from the project factory module instance as an output of the root module.


```
# Project root module 
terraform { 
backend "gcs" { 
bucket = "BUCKET" 
} 
} 

module "project" { 
source = "terraform-google-modules/project-factory/google" 
... 
} 

output "project_id" { 
value = module.project.project_id 
description = "The ID of the created project" 
} 
```


Other Terraform environments and applications can reference root module-level
outputs only.

By using
[remote state](https://www.terraform.io/language/state/remote-state-data),
you can reference root module outputs. To allow use by other dependent apps for
configuration, make sure you're exporting information that's related to a
service's endpoints, to remote state.


```
# Networks root module 
data "terraform_remote_state" "network_project" { 
backend = "gcs" 

config = { 
bucket = "BUCKET" 
} 
} 

module "vpc" { 
source = "terraform-google-modules/network/google" 
version = "~> 9.0" 

project_id = data.terraform_remote_state.network_project.outputs.project_id 
network_name = "vpc-1" 
... 
} 
```


Sometimes, such as when invoking a shared service module from environment
directories, it is appropriate to re-export the entire child module, as follows:


```
output "service" { 
value = module.service
description = "The service module outputs" 
} 
```


## Pin to minor provider versions

In root modules, declare each provider and pin to a *minor* version. This
allows automatic upgrade to new patch releases while still keeping a solid
target. For consistency, name the versions file `versions.tf`.


```
terraform { 
required_providers { 
google = { 
source = "hashicorp/google" 
version = "~> 4.0.0" 
} 
} 
} 
```


## Store variables in a `tfvars` file

For root modules, provide variables by using a `.tfvars` variables file. For
consistency, name variable files `terraform.tfvars`.

Don't specify variables by using alternative
[`var-files`](https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files) 
or `var='key=val'` command-line options. Command-line options are ephemeral and
easy to forget. Using a default variables file is more predictable.

## Check in `.terraform.lock.hcl` file

For root modules, the `.terraform.lock.hcl` [dependency lock](https://www.terraform.io/language/files/dependency-lock) 
file should be checked into source control. This allows for tracking and
reviewing changes in provider selections for a given configuration.

## What's next

- Learn about [general style and structure best practices for Terraform on Google Cloud Dedicated](/docs/terraform/best-practices/general-style-structure).

- Learn about [best practices when using reusable modules](/docs/terraform/best-practices/reusable-modules).