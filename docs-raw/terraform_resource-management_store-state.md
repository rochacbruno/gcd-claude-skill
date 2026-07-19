# Store Terraform state in a Cloud Storage bucket

Source: https://berlin.devsitetest.how/docs/terraform/resource-management/store-state
Last updated: 2026-07-17

- 





[

Technology areas

](https://berlin.devsitetest.how/docs)






- 








[

Guides

](https://berlin.devsitetest.how/docs/terraform/terraform-overview)












# Store Terraform state in a Cloud Storage bucket 






- On this page ** 
- [ Objectives ](#objectives)
- [ Costs ](#costs)
- [ Before you begin ](#before-you-begin)
- [ Prepare the environment ](#prepare-environment)
- [ Review the Terraform files ](#review-files)
- [ Update the backend configuration ](#update-backend)
- [ Provision the Cloud Storage bucket ](#provision-bucket)
- [ Migrate state to Cloud Storage bucket ](#migrate-state)
- [ Clean up ](#clean-up)

- [ Delete the project ](#delete_the_project)

- [ What's next ](#whats-next)
- 













In this tutorial, you learn how to store Terraform state in a Cloud Storage
bucket.

By default, Terraform stores [state](https://www.terraform.io/docs/state/)
locally in a file named `terraform.tfstate`. This default configuration can
make Terraform usage difficult for teams when multiple users run Terraform at
the same time and each machine has its own understanding of the current
infrastructure.

To help you avoid such issues, this page shows you how to configure a
[remote state](https://www.terraform.io/docs/state/remote.html) that points to a
Cloud Storage bucket. Remote state is a feature of
[Terraform backends](https://www.terraform.io/docs/backends).








## Objectives 



This tutorial shows you how to do the following:

- Use Terraform to provision a Cloud Storage bucket to store
Terraform state.

- Add templating in the Terraform configuration file to migrate the state from
the local backend to the Cloud Storage bucket.








## Costs








In this document, you use the following billable components of Google Cloud Dedicated in Germany:








- [
Cloud Storage](/storage/all-pricing)














When you finish the tasks that are described in this document, you can avoid
continued billing by deleting the resources that you created. For more information, see
[Clean up](#clean-up).

Cloud Storage incurs costs for storage, read and write operations,
network egress, and replication.

The Cloud Storage bucket in this tutorial has [Object
Versioning](/storage/docs/object-versioning) enabled to keep the history of your
deployments. Enabling Object Versioning increases storage costs, which you can
mitigate by configuring [Object Lifecycle Management](/storage/docs/lifecycle)
to delete old state versions.






## Before you begin



- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)






Cloud Shell is preinstalled with Terraform.

- 

If you're using a local shell, perform the following steps:

- [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).

- 









Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).





- 






[Create or select a Google Cloud Dedicated project](https://berlin.devsitetest.how/resource-manager/docs/creating-managing-projects).




Roles required to select or create a project**





- 
**Select a project**: Selecting a project doesn't require a specific
IAM role—you can select any project that you've been
granted a role on.


- 
**Create a project**: To create a project, you need the Project Creator role
(`roles/resourcemanager.projectCreator`), which contains the
`resourcemanager.projects.create` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).













- 


Create a Google Cloud Dedicated project:


```
gcloud projects create ** PROJECT_ID 
```



Replace ` PROJECT_ID ` with a name for the Google Cloud Dedicated project you are creating.



- 


Select the Google Cloud Dedicated project that you created:


```
gcloud config set project PROJECT_ID 
```



Replace ` PROJECT_ID ` with your Google Cloud Dedicated project name.







- 




[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).




- 



Enable the Cloud Storage API:





Roles required to enable APIs**


To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).


```
gcloud services enable storage.googleapis.com
```


- 







Grant roles to your user account. Run the following command once for each of the following
IAM roles:
`roles/storage.admin`




```
gcloud projects add-iam-policy-binding PROJECT_ID --member = "user: USER_IDENTIFIER " --role = ROLE 
```



Replace the following:




- ` PROJECT_ID `: Your project ID.


- ` USER_IDENTIFIER `: The identifier for your user

account. For examples, see
[
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users).



- ` ROLE `: The IAM role that you grant to your user account.







Alternately, you can create a
[custom IAM role](/iam/docs/roles-overview#custom) that contains
the following permissions:

- `storage.buckets.create`

- `storage.buckets.list`

- `storage.objects.get`

- `storage.objects.create`

- `storage.objects.delete`

- `storage.objects.update`

As a best practice, we recommend that access to the bucket and the state
files stored there is controlled. Only a small set of users (for example,
the main cloud administrator and the person acting as the alternative or
backup administrator) should have admin permissions for the bucket. The
other developers should have permissions to only write and read objects in
the bucket.







## Prepare the environment

- 

Clone the GitHub repository containing Terraform samples:


```
git clone https://github.com/terraform-google-modules/terraform-docs-samples.git --single-branch
```


- 

Change to the working directory:


```
cd terraform-docs-samples/storage/remote_terraform_backend_template
```


## Review the Terraform files

- 

Review the `main.tf` file:


```
cat main.tf
```


The output is similar to the following




















```
resource "random_id" "default" {
byte_length = 8
}

resource "google_storage_bucket" "default" {
name = "${random_id.default.hex}-terraform-remote-backend"
location = "US"

force_destroy = false
public_access_prevention = "enforced"
uniform_bucket_level_access = true

versioning {
enabled = true
}
}

resource "local_file" "default" {
file_permission = "0644"
filename = "${path.module}/backend.tf"

# You can store the template in a file and use the templatefile function for
# more modularity, if you prefer, instead of storing the template inline as
# we do here.
content = 


This file describes the following resources:

- `random_id`: This is appended to the Cloud Storage bucket name to
ensure a unique name for the Cloud Storage bucket.

- `google_storage_bucket`: The Cloud Storage bucket to store
the state file. This bucket is configured to have the following
properties:

- `force_destroy` is set to `false` to ensure that the bucket is not
deleted if there are objects in it. This ensures that the state
information in the bucket isn't accidentally deleted.

- `public_access_prevention` is set to `enforced` to make sure the
bucket contents aren't accidentally exposed to the public.

- `uniform_bucket_level_access` is set to `true` to allow controlling
access to the bucket and its contents using
[IAM permissions instead of access control lists](/storage/docs/uniform-bucket-level-access).

- `versioning` is enabled to ensure that earlier versions of the state
are preserved in the bucket.

- `local_file`: A local file. The contents of this file instructs Terraform
to use Cloud Storage bucket as the remote backend once the
bucket is created.

## Update the backend configuration

When using Google Cloud Dedicated in Germany, you must update the cloned `main.tf` file for your sovereign environment before provisioning the resources to make sure the storage_custom_endpoint is redirected to the one of the universe you are using.

## Provision the Cloud Storage bucket

- 

Initialize Terraform:


```
terraform init 
```


When you run `terraform init` for the first time, the Cloud Storage
bucket that you specified in the `main.tf` file doesn't exist yet, so
Terraform initializes a local backend to store state in the local
file system.

- 

Apply the configuration to provision resources described in the `main.tf`
file:


```
terraform apply 
```


When prompted, enter `yes`.

When you run `terraform apply` for the first time, Terraform provisions the
Cloud Storage bucket for storing the state. It also creates a local
file; the contents of this file instruct Terraform to use the
Cloud Storage bucket as the remote backend to store state.

## Migrate state to Cloud Storage bucket

- 

Migrate Terraform state to the remote Cloud Storage backend:


```
terraform init -migrate-state 
```


Terraform detects that you already have a state file locally and prompts you
to migrate the state to the new Cloud Storage bucket. When prompted,
enter `yes`.

After running this command, your Terraform state is stored in the
Cloud Storage bucket. Terraform pulls the latest state from this bucket
before running a command, and pushes the latest state to the bucket after
running a command.








## Clean up




To avoid incurring charges to your Google Cloud account for the resources used in this
tutorial, either delete the project that contains the resources, or keep the project and
delete the individual resources.





### Delete the project

To avoid incurring charges to your Google Cloud Dedicated account for the resources
used on this page, follow these steps.

- 

Open the `main.tf` file.

- 

In the `google_storage_bucket.default` resource, update the value of
`force_destroy` to `true`.

- 

Apply the updated configuration:


```
terraform apply 
```


When prompted, enter `yes`.

- 

Delete the state file:


```
rm backend.tf
```


- 

Reconfigure the backend to be local:


```
terraform init -migrate-state 
```


When prompted, enter `yes`.

- 

Run the following command to delete the Terraform resources:


```
terraform destroy 
```


When prompted, enter `yes`.







## What's next



- Learn how to [manage infrastructure as code with Terraform, Cloud Build, and GitOps](/docs/terraform/resource-management/managing-infrastructure-as-code)

- [Learn about policy validation](/docs/terraform/policy-validation).