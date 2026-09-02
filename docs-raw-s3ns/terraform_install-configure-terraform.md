# Install Terraform

Source: https://documentation.s3ns.fr/docs/terraform/install-configure-terraform
Last updated: 2026-08-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/terraform/tpc-differences) for more details.














- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Documentation

](https://documentation.s3ns.fr/docs)






- 








[

Developer tools

](https://documentation.s3ns.fr/docs/costs-usage)






- 








[

Terraform on Google Cloud

](https://documentation.s3ns.fr/docs/terraform)






- 








[

Guides

](https://documentation.s3ns.fr/docs/terraform/terraform-overview)












# Install Terraform 






- On this page 
- [ What's next ](#whats_next)
- 










This page describes the steps to install Terraform for
Cloud de Confiance in [Cloud Shell](/shell/docs) and in a local shell.
Cloud Shell is an interactive shell environment for Cloud de Confiance
that lets you learn and experiment with Cloud de Confiance and manage your
projects and resources from your web browser.

For a introductory guide to using Terraform with Cloud de Confiance, see the
[Terraform for Cloud de Confiance Quickstart](/docs/terraform/create-vm-instance).


[ Cloud Shell ](#cloud-shell) [ Local shell ](#local-shell) 
More 




- 

To use an online terminal with the gcloud CLI and Terraform
already set up, activate Cloud Shell:











Activate Cloud Shell on this page 

At the bottom of this page, a Cloud Shell session starts and
displays a command-line prompt. It can take a few seconds for the session
to initialize.

- 

Run the following command to verify that Terraform is available:


```
terraform
```


The output should be similar to the following:


```
Usage : terraform [ global options ] subcommand > [ args ] 

The available commands for execution are listed below . 
The primary workflow commands are given first , followed by 
less common or more advanced commands . 

Main commands : 
init Prepare your working directory for other commands 
validate Check whether the configuration is valid 
plan Show changes required by the current configuration 
apply Create or update infrastructure 
destroy Destroy previously-created infrastructure 
```


- 

To use Terraform with Cloud de Confiance, you should ensure the
following tasks are completed within Cloud de Confiance:

- [Create or have a Cloud de Confiance project](/resource-manager/docs/creating-managing-projects).

- [Enable billing](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project)
for the Cloud de Confiance project.

- [Enable APIs](/apis/docs/getting-started#enabling_apis) for the
Cloud de Confiance services you intend to work with.

- [Set up authentication](/docs/terraform/authentication) for
Terraform.




- 

Use the [installation instructions](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli)
provided by Terraform.

- 

Run the following command to verify that Terraform is available:


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

To use Terraform with Cloud de Confiance, you should ensure the
following tasks are completed within Cloud de Confiance:

- [Create or have a Cloud de Confiance project](/resource-manager/docs/creating-managing-projects).

- [Enable billing](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project)
for the Cloud de Confiance project.

- [Enable APIs](/apis/docs/getting-started#enabling_apis) for the
Cloud de Confiance services you intend to work with.

- [Set up authentication](/docs/terraform/authentication) for
Terraform.




## What's next 

- Work through the
[Terraform for Cloud de Confiance quickstart](/docs/terraform/create-vm-instance)

- Learn about the [basic Terraform commands](/docs/terraform/basic-commands).