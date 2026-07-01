# Best practices on dependency management

Source: https://berlin.devsitetest.how/docs/terraform/best-practices/dependency-management
Last updated: 2026-06-29

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












# Best practices on dependency management 






- On this page 
- [ Favor implicit dependencies over explicit dependencies ](#favor-implicit-dependencies)
- [ Reference output attributes from dependent resources ](#reference-output-attributes)
- [ What's next ](#whats-next)
- 










This document provides recommendations for expressing dependencies between
resources in your Terraform configuration.

## Favor implicit dependencies over explicit dependencies 

Resource dependencies arise when one resource depends on the existence of other
resources. Terraform must be able to understand these dependencies to ensure
that resources are created in the correct order. For example, if resource A has
a dependency on resource B, resource B is created before resource A.

Terraform configuration dependencies can be established through
[implicit and explicit dependency declarations](https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies).
Implicit dependencies are declared through
[expression references](https://developer.hashicorp.com/terraform/language/expressions/references),
while explicit dependencies are specified by using the
[`depends_on`](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on)
meta argument. The `depends_on` argument specifies that Terraform must complete
all the actions on the object(s) that a resource or a module depends on, before
proceeding with the dependent object.

While both approaches ensure a correct order of operations, implicit
dependencies often lead to more efficiency in planning for [updates and
replacement of resources](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on#processing-and-planning-consequences). This is because Terraform can
intelligently track the specific fields involved in an implicit dependency,
potentially avoiding changes to the dependent resource if those specific fields
remain unaltered within the dependency.

In comparison to implicit dependencies, explicit dependencies convey less
specific information. This means that Terraform can only formulate more
conservative plans for resource creation, updates, and replacement in the
absence of knowledge of the particular attributes that constitute the dependency.
In practice, this impacts the sequence in which resources are created by
Terraform and how Terraform determines whether resources require updates or
replacements.

We recommended using explicit dependencies with the `depends_on` meta argument
only as the last resort when a dependency between two resources is hidden and
can't be expressed through implicit dependencies.

In the following example, the required project services must be enabled before
creating a BigQuery dataset. This dependency is declared
explicitly:

Not recommended: 


```
module "project_services" { 
source = "terraform-google-modules/project-factory/google//modules/project_services" 
version = "~> 14.4" 

project_id = var.project_id 
activate_apis = [ 
"bigquery.googleapis.com" , 
"bigquerystorage.googleapis.com" , 
] 
} 

module "bigquery" { 
source = "terraform-google-modules/bigquery/google" 
version = "~> 5.4" 

dataset_id = "demo_dataset" 
dataset_name = "demo_dataset" 
project_id = var.project_id 
depends_on = [ module.project_services ] # 
} 
```


The following example replaces the explicit dependency with an implicit
dependency by referencing the `project_id` argument as the `project_id` output
attribute of the `project_services` resource:

Recommended: 


```
module "bigquery" { 
source = "terraform-google-modules/bigquery/google" 
version = "~> 5.4" 

dataset_id = "demo_dataset" 
dataset_name = "demo_dataset" 
project_id = module.project_services.project_id # 
} 
```


The use of implicit dependencies allows for precise declarations of
dependencies, such as specifying the exact information that needs to be
collected from an upstream object. This also reduces the need for making changes
in multiple places, which in turn reduces the risk of errors.

## Reference output attributes from dependent resources

When you create implicit dependencies by referencing values from upstream
resources, make sure to only reference output attributes, specifically
[values that are not yet known](https://developer.hashicorp.com/terraform/language/expressions/references#values-not-yet-known).
This will ensure that Terraform waits for the upstream resources to be created
before provisioning the current resource.

In the following example, the `google_storage_bucket_object` resource references
the name argument of the `google_storage_bucket` resource. Arguments have known
values during the Terraform plan phase. This means that when Terraform creates
the `google_storage_bucket_object` resource, it doesn't wait for the
`google_storage_bucket` resource to be created because referencing a known
argument (the bucket name) doesn't create an implicit dependency between the
`google_storage_bucket_object` and the `google_storage_bucket`. This defeats the
purpose of the implicit dependency declaration between the two resources.

Not recommended: 


```
# Cloud Storage bucket 
resource "google_storage_bucket" "bucket" { 
name = "demo-bucket" 
location = "US" 
} 

resource "google_storage_bucket_object" "bucket_object" { 
name = "demo-object" 
source = "./test.txt" 
bucket = google_storage_bucket.bucket.name # name is an input argument 
} 
```


Instead, `google_storage_bucket_object` resource must reference the `id`
output attribute of the `google_storage_bucket_object` resource. Since the `id`
field is an output attribute, its value is only set after the creation of its
resource has been executed. Therefore, Terraform will wait for the creation of
the `google_storage_bucket_object` resource to complete before beginning the
creation of the `google_storage_bucket_object` resource.

Recommended: 


```
resource "google_storage_bucket_object" "bucket_object" { 
name = "demo-object" 
source = "./test.txt" 
bucket = google_storage_bucket.bucket.id # id is an output attribute 
} 
```


Sometimes there is no obvious output attribute to reference. For example,
consider the following example where `module_a` takes the name of the generated
file as input. Inside `module_a`, the filename is used to read the file. If
you run this code as-is, you'll get a `no such file or directory` exception,
which is caused by Terraform attempting to read the file during its planning
phase, at which time the file hasn't been created yet. In this case, an
examination of the output attribute of the `local_file` resource reveals that
there are no obvious fields that you can use in place of the filename input
argument.

Not recommended: 


```
resource "local_file" "generated_file" { 
filename = "./generated_file.text" 
content = templatefile ( "./template.tftpl" , { 
project_id = var.project_id 
}) 
} 

module "module_a" { 
source = "./modules/module-a" 
root_config_file_path = local_file.generated_file.filename 
} 
```


You can solve this problem by introducing an explicit dependency. As a best
practice, make sure add a comment on why the explicit dependency is needed:

Recommended: 


```
module "module_a" { 
source = "./modules/module-a" 
root_config_file_path = local_file.generated_file.filename 
depends_on = [ local_file.generated_file ] # waiting for generated_file to be created 
} 
```


## What's next

- Learn about [best practices for cross-configuration communication](/docs/terraform/best-practices/cross-config-communication).

- Learn about [best practices when working with Google Cloud Dedicated resources](/docs/terraform/best-practices/working-with-resources).