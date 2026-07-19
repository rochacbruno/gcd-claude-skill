# Export your Google Cloud Dedicated in Germany resources to Terraform format

Source: https://berlin.devsitetest.how/docs/terraform/resource-management/export
Last updated: 2026-07-17

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












# Export your Google Cloud Dedicated in Germany resources to Terraform format 






- On this page 
- [ Roles ](#roles)
- [ Before you begin ](#before-you-begin)
- [ Limitations ](#limitations)
- [ Export the entire project configuration to Terraform HCL code ](#export_the_entire_project_configuration_to_terraform_hcl_code)

- [ Write the output to a directory structure ](#write_the_output_to_a_directory_structure)
- [ Write the output to a single file ](#write_the_output_to_a_single_file)

- [ Filter the output ](#filter_the_output)

- [ List the supported resource types to filter on ](#list_the_supported_resource_types_to_filter_on)
- [ Export a single resource type ](#export_a_single_resource_type)
- [ Export multiple resource types ](#export_multiple_resource_types)
- [ Use a file to specify the resource types to export ](#use_a_file_to_specify_the_resource_types_to_export)

- [ Troubleshooting ](#troubleshooting)
- [ Next steps ](#next_steps)
- 












You've deployed resources in Google Cloud Dedicated, and now need to manage your
infrastructure as code (IaC) with Terraform. Google provides a tool that you
can use to generate Terraform code for resources in a project, folder, or
organization.

## Roles






































































































To get the permissions that
you need to export assets to Terraform,

ask your administrator to grant you the
following IAM roles on the organization, folder, or project:













- [Service Usage Consumer ](/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)




- 
If writing state to an existing bucket (`--storage-path=BUCKET`):




- [Storage Object Creator ](/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)


- [Storage Object Viewer ](/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)







- 
If writing state to a new bucket:
[Storage Object Viewer ](/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









## Before you begin

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


- 

Create a service account to use for this export:


```
gcloud beta services identity create --service=cloudasset.googleapis.com
```


- 

Ensure that the [Cloud Asset Service
Agent](/iam/docs/service-agents)
(`gcp-sa-cloudasset.eu0-system.iam.gserviceaccount.com`) has the
`roles/servicenetworking.serviceAgent` role:


```
gcloud projects add-iam-policy-binding PROJECT_ID \
--member=serviceAccount:service- PROJECT_NUMBER @gcp-sa-cloudasset.eu0-system.iam.gserviceaccount.com \
--role=roles/servicenetworking.serviceAgent
```


- 

Ensure that the [Cloud Asset Service
Agent](/iam/docs/service-agents)
(`gcp-sa-cloudasset.eu0-system.iam.gserviceaccount.com`) has the
`roles/storage.objectAdmin` role:


```
gcloud projects add-iam-policy-binding PROJECT_ID \
--member=serviceAccount:service- PROJECT_NUMBER @gcp-sa-cloudasset.eu0-system.iam.gserviceaccount.com \
--role=roles/storage.objectAdmin
```


## Limitations

Some resource types aren't supported for export to Terraform format
even though they are supported by the Terraform Google provider. For a
list of resource types that are supported for export to Terraform format, run
the [`gcloud beta resource-config list-resource-types`](/sdk/gcloud/reference/beta/resource-config/list-resource-types) command.

## Export the entire project configuration to Terraform HCL code

The [`gcloud beta resource-config bulk-export --resource-format=terraform`](/sdk/gcloud/reference/beta/resource-config/bulk-export) command exports
resources configured in the project, folder, or
organization and prints them to the screen in [HCL code format](https://www.terraform.io/language/configuration-0-11/syntax).


```
gcloud beta resource-config bulk-export \
--project= PROJECT_ID \
--resource-format=terraform
```


### Write the output to a directory structure

- 

If you haven't done so already, create the directory where you want to
output the project's configuration:


```
mkdir OUTPUT_DIRECTORY 
```


- 

Export the project's entire configuration to the directory:


```
gcloud beta resource-config bulk-export \
--path= OUTPUT_DIRECTORY \
--project= PROJECT_ID \
--resource-format=terraform
```


The `--path` flag specifies the location to output the HCL code.

After running the command, the HCL code for each resource is output to a
separate `.tf` file in the following directory structure:


```
OUTPUT_DIRECTORY /projects/ PROJECT_ID / RESOURCE_TYPE 
```


### Write the output to a single file

If you don't want to print the output to the screen or create separate `.tf`
files, you can write all of the output to a single file, as shown in this
example:


```
gcloud beta resource-config bulk-export \
--resource-format=terraform \
--project= PROJECT_ID \
>> gcp_resources.tf
```


## Filter the output

Filter the output of the bulk export command by specifying resource types.

### List the supported resource types to filter on

For a list of resource types that are supported for export to Terraform format,
run the [`gcloud beta resource-config list-resource-types`](/sdk/gcloud/reference/beta/resource-config/list-resource-types) command:


```
gcloud beta resource-config list-resource-types
```


Optionally, write the output to a file:


```
gcloud beta resource-config list-resource-types >> strings.txt
```


In the output, the resource type for Compute Engine VMs is listed as:


```
KRM KIND: **ComputeInstance**
```


You can ignore the `KRM KIND:` prefix.

### Export a single resource type

Use a string, such as `ComputeInstance`, to export specific resource types for
your project in HCL code format:


```
gcloud beta resource-config bulk-export \
--resource-types= RESOURCE_TYPE \
--project= PROJECT_ID \
--resource-format=terraform
```


The `--resource-types` flag specifies the resource type to output.

### Export multiple resource types

Export VM instances and firewall rules in HCL code format:


```
gcloud beta resource-config bulk-export \
--resource-types=ComputeFirewall,ComputeInstance \
--project= PROJECT_ID \
--resource-format=terraform
```


### Use a file to specify the resource types to export

- 

Create a directory called `tf-output`.


```
cd && mkdir tf-output && cd tf-output
```


- 

Create a file called `types.txt`, and add a list of resource types. For
example:


```
ComputeBackendBucket
ComputeBackendService
ComputeForwardingRule
```


- 

Run the `gcloud beta resource-config bulk-export` command with the
`--resource-types-file` flag:


```
gcloud beta resource-config bulk-export \
--resource-types-file=types.txt \
--path=tf-output \
--project= PROJECT_ID \
--resource-format=terraform
```


If the project doesn't contain any of a particular resource type, the command
succeeds but nothing is output for that resource type.

## Troubleshooting

If you see the following error:

"Permission denied during export. Please ensure the Cloud Asset Inventory API is
enabled."

Make sure that you have followed the instructions in the
[Before you begin](#before-you-begin) section.

## Next steps

- [Import your Google Cloud Dedicated in Germany resources into Terraform
state](/docs/terraform/resource-management/import).