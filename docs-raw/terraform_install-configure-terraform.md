# Install Terraform

Source: https://berlin.devsitetest.how/docs/terraform/install-configure-terraform
Last updated: 2026-07-10

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












# Install Terraform 






- On this page 
- [ What's next ](#whats_next)
- 










This page describes the steps to install Terraform for
Google Cloud Dedicated in [Cloud Shell](/shell/docs) and in a local shell.
Cloud Shell is an interactive shell environment for Google Cloud Dedicated
that lets you learn and experiment with Google Cloud Dedicated and manage your
projects and resources from your web browser.

For a introductory guide to using Terraform with Google Cloud Dedicated, see the
[Terraform for Google Cloud Dedicated Quickstart](/docs/terraform/create-vm-instance).


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

To use Terraform with Google Cloud Dedicated, you should ensure the
following tasks are completed within Google Cloud Dedicated:

- [Create or have a Google Cloud Dedicated project](/resource-manager/docs/creating-managing-projects).

- [Enable billing](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project)
for the Google Cloud Dedicated project.

- [Enable APIs](/apis/docs/getting-started#enabling_apis) for the
Google Cloud Dedicated services you intend to work with.

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

To use Terraform with Google Cloud Dedicated, you should ensure the
following tasks are completed within Google Cloud Dedicated:

- [Create or have a Google Cloud Dedicated project](/resource-manager/docs/creating-managing-projects).

- [Enable billing](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project)
for the Google Cloud Dedicated project.

- [Enable APIs](/apis/docs/getting-started#enabling_apis) for the
Google Cloud Dedicated services you intend to work with.

- [Set up authentication](/docs/terraform/authentication) for
Terraform.




## What's next 

- Work through the
[Terraform for Google Cloud Dedicated quickstart](/docs/terraform/create-vm-instance)

- Learn about the [basic Terraform commands](/docs/terraform/basic-commands).