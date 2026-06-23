# Overview of Terraform on Google Cloud Dedicated

Source: https://berlin.devsitetest.how/docs/terraform/terraform-overview
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












# Overview of Terraform on Google Cloud Dedicated 






- On this page 
- [ Benefits of using Terraform ](#benefits)
- [ Using Terraform ](#using)
- [ Google Cloud providers ](#providers)
- [ What's next ](#whats-next)
- 










Hashicorp Terraform is an Infrastructure as code (IaC) tool that lets you
provision and manage cloud infrastructure. Terraform provides plugins called
*providers* that lets you interact with cloud providers and other
APIs. You can use the *Terraform provider for Google Cloud* to
provision and manage Google Cloud Dedicated infrastructure.

## Benefits of using Terraform 

This section explains some of the benefits of using Terraform to provision and
manage Google Cloud Dedicated infrastructure:

- Terraform is the most commonly used tool to provision and automate
Google Cloud Dedicated infrastructure. You can use the
[Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
to configure and manage all Google Cloud Dedicated resources using the same
declarative syntax and tooling.

- Terraform lets you specify your preferred end state for your infrastructure.
You can then deploy the same configuration multiple times to create
reproducible development, test, and production environments.

- Terraform lets you generate an execution plan that shows what Terraform will
do when you apply your configuration. This lets you avoid any surprises when
you modify your infrastructure through Terraform.

- Terraform lets you package and reuse common code in the form of
[modules](https://registry.terraform.io/namespaces/terraform-google-modules).
Modules present standard interfaces for creating cloud resources. They
simplify projects by increasing readability and allow teams to organize
infrastructure in readable blocks. 

- Terraform records the current state of your infrastructure and lets you
manage state effectively. The Terraform state file keeps track of all
resources in a deployment.

## Using Terraform

Terraform has a declarative and configuration-oriented syntax, which you can use
to [author the infrastructure](https://developer.hashicorp.com/terraform/language)
that you want to provision. Using this syntax, you'll define your preferred
end-state for your infrastructure in a *Terraform configuration file*. You'll then
use the [Terraform CLI](/docs/terraform/basic-commands) to provision
infrastructure based on the configuration file.

The following steps explain how Terraform works:

- You describe the Google Cloud Dedicated infrastructure you want to provision
in a Terraform configuration file. You don't need to author code
describing *how* to provision this configuration.

- You run the `terraform plan` command, which evaluates your configuration
and generates an execution plan. You can review the plan and make changes as
needed.

- Then, you run the `terraform apply` command, which performs the following
actions:

- It provisions your infrastructure based on your execution plan by invoking
the corresponding Google Cloud APIs in the background.

- It creates a *Terraform state file*, which is a JSON formatted mapping of
resources in your configuration file to the resources in the
real world infrastructure. Terraform uses this file to know the latest
state of your infrastructure, and to determine when to create, update, and
destroy resources.

- Subsequently, when you run `terraform apply`, Terraform uses the mapping in
the state file to compare the existing infrastructure to the code, and make
updates as necessary:

- If a resource object defined in the configuration file does not exist in
the state file, Terraform creates it.

- If a resource object exists in the state file, but has a different
configuration from your configuration file, Terraform updates the
resource to match your configuration file.

- If a resource object in the state file matches your configuration
file, Terraform leaves the resource unchanged.

## Google Cloud providers

There are two providers that let you provision and manage Google Cloud Dedicated
infrastructure:

- `google`: Use this provider to provision and manage
Google Cloud APIs.

- `google-beta`: Use this provider to provision and manage
Google Cloud beta APIs.

For instructions on using these providers, see the
[Google Cloud provider configuration reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference).

`google` and `google-beta` providers are developed using a tool called
*Magic Modules*. Magic Modules allows contributors to make changes against a
single codebase and develop both `google` and `google-beta` providers
simultaneously.

You can contribute to the Google Cloud providers using Magic
Modules by following the instructions in the
[Magic Modules contribution guide](https://googlecloudplatform.github.io/magic-modules/get-started/generate-providers/).

## What's next

- Learn about [Terraform differences in Google Cloud Dedicated versus Google Cloud](/docs/terraform/tpc-differences)

- Learn how to
[create a basic web server on Compute Engine using Terraform](/docs/terraform/get-started-with-terraform)

- Learn how to
[store Terraform state in a Cloud Storage bucket](/docs/terraform/resource-management/store-state)