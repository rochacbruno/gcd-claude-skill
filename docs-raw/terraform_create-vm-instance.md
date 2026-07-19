# Quickstart: Create a Compute Engine VM instance using Terraform

Source: https://berlin.devsitetest.how/docs/terraform/create-vm-instance
Last updated: 2026-07-17

- 





[

Technology areas

](https://berlin.devsitetest.how/docs)






- 








[

Guides

](https://berlin.devsitetest.how/docs/terraform/terraform-overview)

















- On this page ** 
- [ Before you begin ](#before-you-begin)
- [ Prepare the environment ](#prepare-environment)
- [ Review the Terraform files ](#review-files)
- [ Create the Compute Engine VM instance ](#create-instance)
- [ Connect to the VM instance ](#connect-instance)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Quickstart: Create a VM instance using Terraform 




In this quickstart, you learn how to use Terraform to create a Compute Engine
Virtual Machine (VM) instance and connect to that VM instance.

Hashicorp Terraform is an Infrastructure as code (IaC) tool that lets you
provision and manage cloud infrastructure. *Terraform provider for
Google Cloud Dedicated* (*Google Cloud Dedicated provider*) lets you provision and
manage Google Cloud Dedicated infrastructure.





## Before you begin 



- 

To use an online terminal with the gcloud CLI and Terraform
already set up, activate Cloud Shell:











Activate Cloud Shell on this page 

At the bottom of this page, a Cloud Shell session starts and
displays a command-line prompt. It can take a few seconds for the session to
initialize.

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



Enable the Compute Engine API:





Roles required to enable APIs**


To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).


```
gcloud services enable compute.googleapis.com
```


- 







Grant roles to your user account. Run the following command once for each of the following
IAM roles:
`roles/compute.instanceAdmin.v1`




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












## Prepare the environment

- 

Clone the GitHub repository containing Terraform samples:


```
git clone https://github.com/terraform-google-modules/terraform-docs-samples.git --single-branch
```


- 

Go to the directory that contains the quickstart sample:


```
cd terraform-docs-samples/compute/quickstart/create_vm
```


## Review the Terraform files

Review the `main.tf` file. This file defines the Google Cloud Dedicated
resources that you want to create.


```
cat main.tf
```


The output is similar to the following




















```
resource "google_compute_instance" "default" {
name = "my-vm"
machine_type = "n1-standard-1"
zone = "us-central1-a"

boot_disk {
initialize_params {
image = "ubuntu-minimal-2210-kinetic-amd64-v20230126"
}
}

network_interface {
network = "default"
access_config {}
}
}
```



This file describes the
[`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance), which is the Terraform resource for the
Compute Engine VM instance. `google_compute_instance` is configured to
have the following properties:

- `name` is set to `my-vm`.

- `machine_type` is set to `n1-standard-1`.

- `zone` is set to `us-central1-a`.

- `boot_disk` sets the boot disk for the instance.

- `network_interface` is set to use the default network in your
Google Cloud Dedicated project.

## Create the Compute Engine VM instance

- 

In Cloud Shell, run the following command to verify that Terraform
is available:


```
terraform
```


The output should be similar to the following:


```
Usage: terraform [ global options ] [ args ] 

The available commands for execution are listed below.
The primary workflow commands are given first, followed by
less common or more advanced commands.

Main commands:
init Prepare your working directory for other commands
validate Check whether the configuration is valid
plan Show changes required by the current configuration
apply Create or update infrastructure
destroy Destroy previously-created infrastructure
```


- 

Initialize Terraform by running the following command. This command prepares
your workspace so Terraform can apply your configuration.


```
terraform init
```


The output should be similar to the following:


```
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/google...
- Installing hashicorp/google v5.35.0...
- Installed hashicorp/google v5.35.0 ( signed by HashiCorp ) 

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!
```


- 

Validate the Terraform configuration by running the following command.
This command takes the following actions:

- Verifies that the syntax of `main.tf` is correct.

- Shows a preview of the resources that will be created.


```
terraform plan
```


The output should be similar to the following:


```
Plan: 1 to add, 0 to change, 0 to destroy.

Note: You didn 't use the -out option to save this plan, so Terraform can' t
guarantee to take exactly these actions if you run "terraform apply" now.
```


- 

Apply the configuration to provision resources described in the `main.tf`
file:


```
terraform apply
```


When prompted, enter `yes`.

Terraform calls Google Cloud Dedicated APIs to create the VM instance defined in
the `main.tf` file.

The output should be similar to the following:


```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed
```


## Connect to the VM instance

Connect to the VM instance you just created by running the following command:


```
gcloud compute ssh --zone = us-central1-a my-vm
```







## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, delete the Google Cloud Dedicated project with the
resources.






In Cloud Shell, run the following command to delete the Terraform
resources:


```
terraform destroy
```


When prompted, enter `yes`.

The output should be similar to the following:


```
Destroy complete! Resources: 1 destroyed.
```







## What's next



- Learn how to [deploy a basic Flask web server using Terraform](/docs/terraform/deploy-flask-web-server).

- Learn how to [store Terraform state in a Cloud Storage bucket](/docs/terraform/resource-management/store-state).