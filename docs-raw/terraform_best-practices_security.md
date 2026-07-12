# Best practices for security

Source: https://berlin.devsitetest.how/docs/terraform/best-practices/security
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












# Best practices for security 






- On this page 
- [ Use remote state ](#use-remote-state)
- [ Encrypt state ](#encrypt-state)
- [ Don't store secrets in state ](#storing-secrets)
- [ Mark sensitive outputs ](#sensitive-outputs)
- [ Ensure separation of duties ](#separation-of-duties)
- [ Run continuous audits ](#continuous-audits)
- [ What's next ](#whats-next)
- 










This document provides guidelines and recommendations for securely using
Terraform for Google Cloud Dedicated. Terraform requires sensitive access to your
cloud infrastructure to operate. Following security best practices can help to
minimize the associated risks and improve your overall cloud security.

This guide is not an introduction to Terraform. For an introduction to using
Terraform with Google Cloud Dedicated in Germany, see
[Get started with Terraform](/docs/terraform/get-started-with-terraform).

## Use remote state 

For Google Cloud Dedicated customers, we recommend using the
[Cloud Storage state backend](https://www.terraform.io/docs/backends/types/gcs.html).
This approach locks the state to allow for collaboration as a team. It also
separates the state and all the potentially sensitive information from version
control.

Make sure that only the build system and highly privileged administrators can
access the bucket that is used for remote state.

To prevent accidentally committing development state to source control, use
[gitignore](https://github.com/github/gitignore/blob/master/Terraform.gitignore) 
for Terraform state files.

## Encrypt state

Though Google Cloud Dedicated buckets are encrypted at rest, you can use
[customer-supplied encryption keys](/storage/docs/encryption#customer-supplied)
to provide an added layer of protection. Do this by using the
`GOOGLE_ENCRYPTION_KEY` environment variable. Even though no secrets should be
in the state file, always encrypt the state as an additional measure of defense.

## Don't store secrets in state

There are many resources and data providers in Terraform that store secret
values in plaintext in the state file. Where possible, avoid
storing secrets in state. Following are some examples of providers that store
secrets in plaintext:

- [`vault_generic_secret`](https://registry.terraform.io/providers/hashicorp/vault/latest/docs/resources/generic_secret) 

- [`tls_private_key`](https://registry.terraform.io/providers/hashicorp/tls/latest/docs/resources/private_key) 

- [`google_service_account_key`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account_key) 

- [`google_client_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/client_config) 

## Mark sensitive outputs

Instead of attempting to manually
[encrypt sensitive values](https://www.terraform.io/docs/extend/best-practices/sensitive-state.html),
rely on Terraform's built-in support for sensitive state management. When
exporting sensitive values to output, make sure that the values are marked as
[sensitive](https://www.terraform.io/docs/configuration/outputs.html#sensitive-suppressing-values-in-cli-output).

## Ensure separation of duties

If you can't run Terraform from an automated system where no users have access,
adhere to a separation of duties by separating permissions and directories. For
example, a network project would correspond with a network Terraform service
account or user whose access is limited to this project.

## Run continuous audits

After the `terraform apply` command has executed, run automated security checks.
These checks can help to ensure that infrastructure doesn't drift into an
insecure state. The following tools are valid choices for this type of check:

- [Security Health Analytics](/security-command-center/docs/how-to-use-security-health-analytics)

- [InSpec](https://inspec.io) 

- [Serverspec](https://serverspec.org/) 

## What's next

- Learn about [general style and structure best practices for Terraform on Google Cloud Dedicated](/docs/terraform/best-practices/general-style-structure).

- Learn about [best practices when using Terraform root modules](/docs/terraform/best-practices/root-modules).