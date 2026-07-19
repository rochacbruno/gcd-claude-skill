# Best practices for Terraform operations

Source: https://berlin.devsitetest.how/docs/terraform/best-practices/operations
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












# Best practices for Terraform operations 






- On this page 
- [ Always plan first ](#plan)
- [ Implement an automated pipeline ](#pipeline)
- [ Use service account credentials for continuous integration ](#credentials)
- [ Avoid importing existing resources ](#importing)
- [ Don't modify Terraform state manually ](#manual-state-modification)
- [ Regularly review version pins ](#version-pins)
- [ Use application default credentials when running locally ](#default-credentials)
- [ Set aliases to Terraform ](#aliases)
- [ What's next ](#whats-next)
- 










This document provides guidelines and recommendations for Terraform operations.

This guide is not an introduction to Terraform. For an introduction to using
Terraform with Google Cloud Dedicated in Germany, see
[Get started with Terraform](/docs/terraform/get-started-with-terraform).

## Always plan first 

Always generate a plan first for Terraform executions.
[Save the plan to an output file](https://learn.hashicorp.com/tutorials/terraform/automate-terraform).
After an infrastructure owner approves it, execute the plan. Even when
developers are locally prototyping changes, they should generate a plan and
review the resources to be added, modified, and destroyed before applying the
plan.

## Implement an automated pipeline

To ensure consistent execution context, execute Terraform through automated
tooling. If a build system (like Jenkins) is already in use and widely adopted,
use it to run the `terraform plan` and `terraform apply` commands automatically.
If no existing system is available, adopt either
[Cloud Build](/docs/terraform/resource-management/managing-infrastructure-as-code)
or
[Terraform Cloud](https://cloud.hashicorp.com/products/terraform).

## Use service account credentials for continuous integration

When Terraform is executed from a machine in a CI/CD pipeline, it should
inherit the service account credentials from the service executing the pipeline.
Wherever possible, run CI pipelines on Google Cloud Dedicated because
Cloud Build, Google Kubernetes Engine, or Compute Engine inject credentials
without downloading service account keys.

For pipelines that run outside of Google Cloud Dedicated, prefer
[workload identity federation](/iam/docs/using-workload-identity-federation)
to obtain credentials without downloading service account keys.

## Avoid importing existing resources

Where possible, avoid importing existing resources
(using [`terraform import`](https://www.terraform.io/cli/import)), because doing
so can make it challenging to fully understand the provenance and configuration
of manually created resources. Instead, create new resources through Terraform
and delete the old resources.

In cases where deleting old resources would create significant toil,
use the `terraform import` command with explicit approval. After a resource is
imported into Terraform, manage it exclusively with Terraform.

## Don't modify Terraform state manually

The Terraform state file is critical for maintaining the mapping between
Terraform configuration and Google Cloud Dedicated resources. Corruption can lead
to major infrastructure problems. When modifications to the Terraform state are
necessary, use the [`terraform state`](https://www.terraform.io/cli/state) 
command.

## Regularly review version pins

Pinning versions ensures stability but prevents bug fixes and other
improvements from being incorporated into your configuration. Therefore,
regularly review version pins for Terraform, Terraform providers, and modules.

To automate this process, use a tool such as
[Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates#supported-repositories-and-ecosystems).

## Use application default credentials when running locally

When developers are locally iterating on Terraform configuration, they should
authenticate by running
[`gcloud auth application-default login`](https://berlin.devsitetest.how/sdk/gcloud/reference/auth/application-default/login)
to generate application default credentials. Don't download service account
keys, because downloaded keys are harder to manage and secure.

## Set aliases to Terraform

To make local development easier, you can add aliases to your command shell
profile:

- `alias tf="terraform"`

- `alias terrafrom="terraform"`

## What's next

- Learn about [best practices to securely use Terraform](/docs/terraform/best-practices/security).

- Learn about [best practices for testing Terraform modules and configurations](/docs/terraform/best-practices/testing).