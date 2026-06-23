# Terraform support for Cloud Quotas

Source: https://berlin.devsitetest.how/docs/quotas/terraform-support-for-cloud-quotas
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://berlin.devsitetest.how/docs/quotas)






- 








[

Guides

](https://berlin.devsitetest.how/docs/quotas/overview)












# Terraform support for Cloud Quotas 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Terraform resources and data sources ](#terraform-resources-and-data-sources)

- [ Resources ](#resources)
- [ Data sources ](#data_sources)

- [ What's next ](#whats_next)
- 










[Terraform](https://www.terraform.io/)
is an Infrastructure as code (IaC) tool that you can use to provision resources
and permissions for Cloud Quotas. To learn how to use Terraform
to provision infrastructure on Google Cloud Dedicated in Germany, refer to the
[Terraform on Google Cloud Dedicated in Germany documentation](/docs/terraform).

You can use Terraform to do the following with Cloud Quotas:

- Retrieve the `QuotaInfo` data source of a quota for a project, folder or
organization.

- List `QuotaInfos` data source of all quotas for a given project, folder or
organization.

- Create a new, or update an existing, `QuotaPreference` quota configuration
that specifies the preferred value for a quota.

## Before you begin

Before you begin, you need access to Terraform:

- 

If you're getting started, note that [Cloud Shell](/shell/docs) has
Terraform already integrated, and you can follow this step by step
tutorial,
[Deploy a basic Flask web server](/docs/terraform/get-started-with-terraform)
using Terraform and Cloud Shell.

- 

If you'd prefer to install Terraform yourself, see HashiCorp's
[Terraform installation instructions](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).

To use Terraform with Cloud Quotas,
[create a configuration file](https://developer.hashicorp.com/terraform/language)
to describe your infrastructure, and then
[apply the configuration file](https://developer.hashicorp.com/terraform/cli/commands/apply)
to create an execution plan and perform operations to provision your
infrastructure.

## Terraform resources and data sources

The following lists contain links to Cloud Quotas Terraform
resources and data source samples that appear in the
[Terraform registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/).

### Resources

Cloud Quotas provides the following Terraform resources:

- [google_cloud_quotas_quota_preference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_quotas_quota_preference)

- [google_cloud_quotas_quota_adjuster_settings](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_quotas_quota_adjuster_settings) ([Preview](https://berlin.devsitetest.how/products#product-launch-stages))

### Data sources

Cloud Quotas provides the following Terraform data sources:

- [google_cloud_quotas_quota_info](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloud_quotas_quota_info)

- [google_cloud_quotas_quota_infos](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloud_quotas_quota_infos)

## What's next

Learn more about Terraform:

- 

[What is Terraform?](https://developer.hashicorp.com/terraform/intro)

- 

[Terraform Developer website](https://developer.hashicorp.com/terraform/)

- 

[Terraform Language Documentation](https://developer.hashicorp.com/terraform/language)

- 

[Terraform CLI Documentation](https://developer.hashicorp.com/terraform/cli)