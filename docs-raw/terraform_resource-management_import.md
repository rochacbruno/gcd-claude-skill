# Import your Google Cloud Dedicated in Germany resources into Terraform state

Source: https://berlin.devsitetest.how/docs/terraform/resource-management/import
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












# Import your Google Cloud Dedicated in Germany resources into Terraform state 






- On this page 
- [ Import resources one at a time ](#import-resources-one-at-a-time)

- [ Import resources within modules ](#import-resources-within-modules)

- [ Import resources in bulk with a configuration-driven import block ](#import-resources-in-bulk-in-code)
- [ Import resources created after doing a bulk export ](#import-resources-after-doing-a-bulk-export)

- [ Before you begin ](#before_you_begin)
- [ Generate Terraform code for your resources ](#generate_terraform_code_for_your_resources)
- [ Create Terraform modules from the generated code ](#create_terraform_modules_from_the_generated_code)
- [ Import the modules into the Terraform state ](#import_the_modules_into_the_terraform_state)

- [ Next steps ](#next_steps)
- 










Terraform can import existing infrastructure. This allows you to take resources
you've created by some other means and bring them under Terraform management.

You can import the state for any Google Cloud Dedicated in Germany resource.

Terraform supports multiple ways to import resources:

- [One at a time](#import-resources-one-at-a-time) by using the [`terraform import`](https://developer.hashicorp.com/terraform/cli/commands/import) subcommand.

- [In bulk](#import-resources-in-bulk-in-code) by including an [`import` block in the
configuration](https://developer.hashicorp.com/terraform/tutorials/state/state-import) (requires Terraform version 1.5 or later).

- In bulk by using a Google Cloud Dedicated feature that lets you [import
resources after doing a bulk export](#import-resources-after-doing-a-bulk-export).

## Import resources one at a time

The `import` command takes two arguments—the resource address and ID.
The [resource address](https://developer.hashicorp.com/terraform/cli/state/resource-addressing) 
is an identifier that points to a resource instance within a configuration.
The ID is an identifier that identifies a resource in Google Cloud Dedicated in Germany
that is being imported. Format for the ID differs based on resource type and
[is documented](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#import) 
for each resource supported by the provider. We recommend using the full
identifier, which includes the project ID when supported.

- 

Identify the resource address to be imported.


```
resource "google_storage_bucket" "sample" {
name = "my-bucket"
project = "sample-project"
location = "US"
force_destroy = true
}
```


For a sample resource such as Cloud Storage bucket defined earlier,
this is `google_storage_bucket.sample`.

- 

To identify the resource ID format, see the [provider import
documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#import) for the `google_storage_bucket` resource. In this case, it is of the
form `project/name`, so the resource ID for the preceding sample is
`sample-project/my-bucket`.

- 

Construct the `import` statement by using the resource address and ID, as
follows:


```
terraform import google_storage_bucket.sample sample-project/my-bucket
```


Output:


```
terraform import google_storage_bucket.sample sample-project/my-bucket
google_storage_bucket.sample: Importing from ID "sample-project/my-bucket"...
google_storage_bucket.sample: Import prepared!
Prepared google_storage_bucket for import
google_storage_bucket.sample: Refreshing state... [id=sample-project/my-bucket]
Import successful!
The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```


### Import resources within modules

Modules encapsulate one or more resources within a Terraform configuration.
Because importing requires a resource address, each resource within a module has to
be imported individually.

- 

Identify the resources within a module to be imported.


```
module "gcs_bucket" {
source = "terraform-google-modules/cloud-storage/google//modules/simple_bucket"
version = "~> 3.4"

name = "my-bucket"
project_id = "sample-project"
location = "us-east1"
}
```


To identify resource addresses, you can inspect [module contents](https://github.com/terraform-google-modules/terraform-google-cloud-storage/blob/v3.4.0/modules/simple_bucket/main.tf).
Alternatively, apply the configuration and use the errors surfaced by the
provider. For example:


```
terraform apply
module.gcs_bucket.google_storage_bucket.bucket: Creating...
╷
│ Error: googleapi: Error 409: Your previous request to create the named bucket succeeded and you already own it., conflict
│
│ with module.gcs_bucket.google_storage_bucket.bucket,
```


By using the preceding log, you can identify the resource address that needs to be
imported as `module.gcs_bucket.google_storage_bucket.bucket`.

- 

To identify the resource ID format, see the [provider import
documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#import) for the `google_storage_bucket` resource. In this case, it is of
the form `project/name`. The name can be identified from the plan output.

Output:


```
module.gcs_bucket.google_storage_bucket.bucket will be created
+ resource "google_storage_bucket" "bucket" {
+ name = "my-bucket"
+ project = "sample-project"
...
}
```


For the preceding sample, the resource ID is `sample-project/my-bucket`.

- 

Construct the `import` statement by using the resource address and ID, as
follows:


```
terraform import module.gcs_bucket.google_storage_bucket.bucket sample-project/my-bucket
```


Output:


```
terraform import module.gcs_bucket.google_storage_bucket.bucket sample-project/my-bucket
module.gcs_bucket.google_storage_bucket.bucket: Importing from ID "sample-project/my-bucket"...
module.gcs_bucket.google_storage_bucket.bucket: Import prepared!
Prepared google_storage_bucket for import
module.gcs_bucket.google_storage_bucket.bucket: Refreshing state... [id=sample-project/my-bucket]
Import successful!
The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```


## Import resources in bulk with a configuration-driven `import` block

Terraform version 1.5 lets you add an `import` block to your Terraform
configuration. This allows import operations to be previewed during the `plan`
operation and executed using the `apply` operation.

You can also do automatic code generation for imported resources instead of
writing the code manually.

The `import` block takes two parameters:

- 

`id`: The provider-defined resource ID of the cloud resource to be imported.

For the accepted provider-defined resource ID, see the **Import** section for
the resource in Hashicorp's Google provider documentation. For example,
`projects/{project}/global/networks/{name}` is a resource ID for a
VPC network, as shown on the
[`google_compute_network` reference page](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network#import).

- 

`to`: The Terraform [resource
address](https://developer.hashicorp.com/terraform/cli/state/resource-addressing)
to be created. Usually in the form
RESOURCE TYPE . NAME .

Here’s an example of an `import` block for a Virtual Private Cloud network:


```
import {
# Provider-defined resource ID of the cloud resource to be imported
id = "projects/ PROJECT_ID /global/networks/my-network"

# Terraform resource address to be created
to = google_compute_network.my_network
}
```


If you have manually created your resource block, execute `terraform plan` to
preview the import operation.

If you want Terraform to generate the resource blocks for you, use the
`-generate-config-out` flag to specify the file to generate configuration.

For example:


```
terraform plan -generate-config-out = generated_resources.tf 
```


After reviewing the generated code, run the `terraform apply` operation to
import the configuration to the Terraform state.

## Import resources created after doing a bulk export



Bulk export lets you export Google Cloud Dedicated resources
as Terraform configurations and import Terraform state for those resources
so that you can manage your deployment in Terraform.

### Before you begin

- 

Prepare Cloud Shell.

Launch [Cloud Shell](https://shell.cloud.google.com/), and set
the default Google Cloud Dedicated project where you want to generate Terraform code for the
deployed resources.

You only need to run this command once per project, and you can run it in any
directory.


```
export GOOGLE_CLOUD_PROJECT= PROJECT_ID 
```


Environment variables are overridden if you set explicit values in a
Terraform configuration file.

- 

In Cloud Shell, install the command-line interface (CLI) for Config Connector.


```
gcloud components install config-connector
```


Config Connector lets you use Google Cloud Dedicated's Terraform bulk-export tool.

If you see `ERROR: (gcloud.components.install) You cannot perform this action
because the Google Cloud CLI component manager is disabled for this
installation`, run the following command instead:


```
sudo apt-get install google-cloud-sdk-config-connector
```


- 

Enable the Cloud Asset API.


```
gcloud services enable cloudasset.googleapis.com
```


### Generate Terraform code for your resources

- 

If you haven't done so already, create the directory where you want to
output the project's configuration.


```
mkdir OUTPUT_DIRECTORY 
```


- 

Run the [`gcloud beta resource-config bulk-export`](/sdk/gcloud/reference/beta/resource-config/bulk-export)
command to output the project's entire configuration to the
` OUTPUT_DIRECTORY ` path:


```
gcloud beta resource-config bulk-export \
--path= OUTPUT_DIRECTORY \
--project= PROJECT_ID \
--resource-format=terraform
```


### Create Terraform modules from the generated code

Run the [`gcloud beta resource-config terraform
generate-import`](/sdk/gcloud/reference/beta/resource-config/terraform/generate-import)
command, pointing to the content in the output directory:


```
gcloud beta resource-config terraform generate-import OUTPUT_DIRECTORY 
```


This command generates Terraform modules and an import script:

- 

The `gcloud-export-modules.tf` file. This file points to all of
the modules from the sub-resources. The content of this file looks like this:


```
provider "google" {
project = " PROJECT_ID "
}

module " OUTPUT_DIRECTORY -projects- PROJECT_ID -ComputeFirewall" {
source = "./ OUTPUT_DIRECTORY /projects/ PROJECT_ID /ComputeFirewall"
}

module " OUTPUT_DIRECTORY -projects- PROJECT_ID -ComputeBackendService-global" {
source = "./ OUTPUT_DIRECTORY /projects/ PROJECT_ID /ComputeBackendService/global"
}
```


...and so on.

- 

An executable shell script called something like
`terraform_import_20220331-19-12-33.sh`.
The shell script contains a list of `terraform import` commands:


```
#!/bin/sh
# Terraform Import Script generated by gcloud cli

terraform import module. OUTPUT_DIRECTORY -projects- PROJECT_ID -ComputeFirewall.google_compute_firewall.allow_ssh projects/ PROJECT_ID /global/firewalls/allow-ssh
```


...and so on.

The `terraform import` commands are for importing the modules created by the
`generate-import` command into the Terraform state.

### Import the modules into the Terraform state

- 

Initialize it:


```
terraform init
```


- 

Run the script:


```
./terraform_import_20220331-19-12-33.sh
```


Output:


```
module.examples-projects- PROJECT_ID -ComputeInstance-us-central1-a.google_compute_instance.instance_1:
Importing from ID
"projects/ PROJECT_ID /zones/us-central1-a/instances/instance-1"...
module.examples-projects- PROJECT_ID -ComputeInstance-us-central1-a.google_compute_instance.instance_1:
Import prepared!
Prepared google_compute_instance for import
module.examples-projects- PROJECT_ID -ComputeInstance-us-central1-a.google_compute_instance.instance_1:
Refreshing state...
[id=projects/ PROJECT_ID /zones/us-central1-a/instances/instance-1]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```


## Next steps

- [Store state in a Cloud Storage
bucket](/docs/terraform/resource-management/store-state).