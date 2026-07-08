# Best practices when working with Google Cloud Dedicated resources

Source: https://berlin.devsitetest.how/docs/terraform/best-practices/working-with-resources
Last updated: 2026-07-07

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












# Best practices when working with Google Cloud Dedicated resources 






- On this page 
- [ Bake virtual machine images ](#vm-instances)
- [ Manage Identity and Access Management ](#iam)
- [ What's next ](#whats-next)
- 










Best practices for provisioning Google Cloud Dedicated resources with Terraform, are
integrated into the [Cloud Foundation Toolkit](/foundation-toolkit) modules that
Google maintains. This document reiterates some of these best practices.

This guide is not an introduction to Terraform. For an introduction to using
Terraform with Google Cloud Dedicated in Germany, see
[Get started with Terraform](/docs/terraform/get-started-with-terraform).

## Bake virtual machine images 

In general, we recommend that you *bake* virtual machine images
[using a tool like Packer](/compute/docs/images/image-management-best-practices#automated_baking).
Terraform then only needs to launch machines using the pre-baked images.

If pre-baked images are not available, Terraform can hand off new virtual
machines to a configuration management tool with a `provisioner` block. We
recommend that you avoid this method and only use it as a
[last resort](https://www.terraform.io/language/resources/provisioners/syntax#provisioners-are-a-last-resort).
To clean up old state associated with the instance, provisioners that require
teardown logic should use a `provisioner` block with `when = destroy`.

Terraform should provide VM configuration information to configuration
management with
[instance metadata](/compute/docs/metadata/overview).

## Manage Identity and Access Management

When provisioning IAM associations with Terraform, several
different resources are available:

- `google_*_iam_policy` (for example, `google_project_iam_policy`)

- `google_*_iam_binding` (for example, `google_project_iam_binding`)

- `google_*_iam_member` (for example, `google_project_iam_member`)

`google_*_iam_policy` and `google_*_iam_binding` create *authoritative*
IAM associations, where the Terraform resources serve as the only
source of truth for what permissions can be assigned to the relevant resource.

If the permissions change outside of Terraform, Terraform on its next
execution overwrites all permissions to represent the policy as defined in your
configuration. This might make sense for resources that are wholly managed by a
particular Terraform configuration, but it means that roles that are
automatically managed by Google Cloud Dedicated are removed—potentially disrupting
the functionality of some services.

To prevent this, we recommend using either `google_*_iam_member` resources
directly or the
[IAM module from Google](https://github.com/terraform-google-modules/terraform-google-iam).

## What's next

- Learn about [best practices for version control](/docs/terraform/best-practices/version-control).

- Learn about [best practices for Terraform operations](/docs/terraform/best-practices/operations).