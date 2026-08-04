# Key differences between Cloud de Confiance and Google Cloud

Source: https://documentation.s3ns.fr/code/docs
Last updated: 2026-07-17

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

Get started

](https://documentation.s3ns.fr/docs/get-started)












# Key differences between Cloud de Confiance and Google Cloud 






- On this page 
- [ Service and feature availability ](#service_and_feature_availability)
- [ Service and platform management ](#service_and_platform_management)

- [ Service level agreements ](#sla)

- [ Key differences for developers ](#key_differences_for_developers)
- [ Key differences for architects and operators ](#key_differences_for_architects_and_operators)
- [ Redirected links ](#redirect)
- [ General differences ](#general_differences)

- [ Hardware and OS ](#hardware_and_os)
- [ Availability and disaster recovery ](#availability_and_disaster_recovery)
- [ Cost management ](#cost_management)
- [ Integrations ](#integrations)
- [ Security and access control ](#security_and_access_control)
- [ Network ](#network)
- [ Workflows and tools ](#workflows_and_tools)
- [ Organization setup ](#organization_setup)
- [ Project identifiers ](#project_identifiers)
- [ Service names, endpoints, and resources ](#service_names_endpoints_and_resources)
- [ Service accounts ](#service_accounts)
- [ Documentation ](#documentation)

- [ What's next ](#whats_next)
- 









Cloud de Confiance by S3NS is a local, isolated cloud based on
Google Cloud, with its own subset of Google Cloud
products, features, and workflows. This page explains the key
differences between Google Cloud and
Cloud de Confiance. You can learn more about
Cloud de Confiance and its use cases in the
[Cloud de Confiance overview page](/docs/overview/tpc-overview).

If you're already familiar with Google Cloud, you should read and
understand the differences in this guide carefully. We also recommend that you
review the detailed differences guide for each
Cloud de Confiance product you want to use:
these guides appear in each individual product's documentation set. How you
design, run, and manage your applications might require some changes from what
you're used to in Google Cloud.

Because of these differences between Google Cloud and
Cloud de Confiance, the documentation might also
seem different from Google Cloud documentation. For more
information, see
[About Cloud de Confiance by S3NS documentation](/docs/overview/gcd-documentation).

## Service and feature availability

Not all Google Cloud products and services are available (or available yet) in
Cloud de Confiance. You can see a list of currently available
services in our [product list](/products).

Products and services that *are* available in Cloud de Confiance have
the same names as their Google Cloud counterparts and use the
same Google-developed code and infrastructure. However, they don't always
provide exactly the same capabilities. For example, only Autopilot mode
is available in Google Kubernetes Engine (GKE), older VM types for
Compute Engine are unavailable, and you can't use certain
Identity and Access Management (IAM) policies.

Additional differences include the following:

- New features that launch in Google Cloud might not launch at
the same time in Cloud de Confiance.

- Preview releases of features are generally not available in Cloud de Confiance.

To be notified when new services and features deploy in
Cloud de Confiance, subscribe to the
[release notes](/release-notes).
If there's a particular service or feature you want,
[contact support](https://support.s3ns.fr).

## Service and platform management

Some product or feature names in
Cloud de Confiance might include "Google-managed",
but that doesn't mean that Google actually manages your data. Your
Cloud de Confiance operator always manages
products, services, and your data.

Instead, think of products or features as being "Google-powered". Some product
or feature names have changed for
Cloud de Confiance to make this clearer. For
example, "Google-managed encryption keys" have been renamed to make it clear
that they're *not* managed or accessible by Google. Instead, keys are named
"Google Cloud-powered encryption keys / Managed in
Cloud de Confiance by S3NS". The feature
uses the same technology as in Google Cloud, but your
Cloud de Confiance operator implements and manages
it.

Cloud de Confiance has its own Site Reliability
Engineering (SRE) team that monitors and manages the environment. The SRE team
uses independent monitoring and alerting stacks that are separate from
Google Cloud.

Billing is handled by your Cloud de Confiance
operator, not Google. For more information, see
[Cloud de Confiance billing](/billing) or
[contact your Cloud de Confiance operator](https://support.s3ns.fr).

### Service level agreements

All service level agreements (SLAs) are with your universe's operator. Google Cloud
SLAs don't apply to Cloud de Confiance. For details about SLAs contact [your operator](https://support.s3ns.fr).

## Key differences for developers

As a developer, the following high-level differences can help you build
applications that run in Cloud de Confiance:

- Default API service *names* are the same as in Google Cloud,
such as `bigquery.googleapis.com`.
These service names are visible when you enable or disable APIs, for
example. The service *endpoint* FQDN is different, based on the
Cloud de Confiance hostname. For example,
`bigquery.googleapis.com` becomes
`bigquery.s3nsapis.fr`.

- OAuth scope names are consistent between Google Cloud and
Cloud de Confiance. If an OAuth scope includes
`googleapis` in Google Cloud, it also does so in
Cloud de Confiance.

- Unlike in Google Cloud, you need to specify your target
universe (in this case, Cloud de Confiance)
when setting up and using developer tools like the Google Cloud CLI and
client libraries. For example, you must set a
`GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable before running any code
samples that use our client libraries. For more information, see
[Set up the gcloud CLI for Cloud de Confiance](/docs/get-started-tpc/setup-gcloud)
and [Use client libraries in Cloud de Confiance](/docs/get-started-tpc/use-client-libraries).

- You must provide the appropriate
Cloud de Confiance prefix, such as
`s3ns:`, to identify
projects. This prefix is automatically prepended to the IDs of any
projects you create in Cloud de Confiance. For
example, the ID `example-project` must be referenced as
`s3ns:example-project`.

- Because there's no Cloud Shell in
Cloud de Confiance, you must install command
line tools locally or on a VM that runs in
Cloud de Confiance. If you have workflows or
tools that expect access to Cloud Shell, update them for
locally-installed access using client libraries or the Google Cloud CLI.

To learn more about additional differences between Google Cloud
and Cloud de Confiance, review the
product-specific differences page for each product.

## Key differences for architects and operators

Carefully review existing architecture practices and designs that you use in
Google Cloud. The same design might not work appropriately in
Cloud de Confiance. The following differences are
important for admins, architects, and operators:

- Cloud de Confiance has no inter-region
redundancy, only a single region that contains multiple zones. If your
architecture and applications are built on a multi-region approach for
redundancy or load balancing, change the design to accommodate a
single-region Cloud de Confiance.

- Compute Engine provides a limited selection of VM types in
Cloud de Confiance compared to
Google Cloud. Update your applications if workloads are
designed for a particular size or family of VM that are unavailable in
Cloud de Confiance, including any
Infrastructure as Code (IaC) resources like Terraform files or scripts.

- Cloud Identity is not available in
Cloud de Confiance. This means that you can
only use external identities through
[Workforce Identity Federation](/iam/docs/workforce-identity-federation)
(including from a Google Workspace identity provider), or [service
accounts](/iam/docs/service-account-overview) for authentication and
authorization in Cloud de Confiance. Regular
Google Accounts are not supported. For more information about configuring an
identity provider, see [Set up an identity
provider](/docs/get-started-tpc/set-up-identity-provider).

- There's no Cloud Shell in
Cloud de Confiance, so you must install
command line tools locally or on a VM that runs in
Cloud de Confiance. Update workflows or tools
that expect access to Cloud Shell for locally-installed access
using client libraries or the Google Cloud CLI.

To learn more about additional differences between Google Cloud
and Cloud de Confiance, review the
product-specific differences page for each product.

## Redirected links 

If you followed a link to a product or feature that isn't available in
Cloud de Confiance, you might have been
redirected to this page.

To learn which products are available in
Cloud de Confiance, see
[Products and services](/products). To learn more about other differences
between your universe and Google Cloud, see the other sections
in this page.

## General differences 

The following sections detail some key top-level differences between
Cloud de Confiance and
Google Cloud. In addition to these differences, each supported
product has its own specific differences page in its documentation set to
provide more detail about how the product works in
Cloud de Confiance. Carefully review these pages
along with this guide if you plan to use a product or service in
Cloud de Confiance.

If you run into any issues,
[contact support](https://support.s3ns.fr).

### Hardware and OS 

- Cloud de Confiance doesn't provide the same
hardware and OS support as Google Cloud. For example,
Compute Engine doesn't support ARM-based images, and TPUs are
unavailable. Review the
[Compute Engine differences pages](/compute/docs/tpc-differences) for more
information.

- A public release of a new machine type or operating system in
Google Cloud doesn't indicate future support in
Cloud de Confiance.

### Availability and disaster recovery 

- Cloud de Confiance doesn't have multiple
regions. Instead, Cloud de Confiance runs in
one region, `u-france-east1`, that has three zones. Use multiple zones rather than multiple
regions to duplicate resources across different locations for redundancy.
Multi-region Google Cloud features are unavailable. Review
and update any existing applications or architectures that assume
multi-region redundancy or load balancing before you deploy them in
Cloud de Confiance.

- 

Even though Cloud de Confiance doesn't have
multiple regions, `global` resources (such as the `global` Cloud Key Management Service
location or the Secret Manager global `Secret` resource) are still
available. Like in Google Cloud these resources are scoped
across the entire universe. Unlike in Google Cloud, however,
the universe only has one region, and so the result is the same as using
resources scoped to `u-france-east1`.

You might want to use `global` if, for example, you want to reuse existing
Google Cloud code that addresses global endpoints, or if you are
using CMEK with Cloud KMS to protect resources created in the `global`
location.

### Cost management

- Pricing for products and features in
Cloud de Confiance might differ from that in
Google Cloud.
[Contact your Cloud de Confiance operator](https://support.s3ns.fr)
for any pricing questions.

- There's no free trial tier in
Cloud de Confiance.

- Cloud de Confiance quotas might be different
to those you are used to in Google Cloud. If you need a
quota increase adjustment, you must contact
Cloud de Confiance support.

- Committed use discounts (CUDs) are not available in
Cloud de Confiance.

### Integrations

- Some products and features might be unavailable if they interact with
other products that are unavailable in
Cloud de Confiance. Review the
product-specific differences page to understand what integrations might be
unavailable in Cloud de Confiance.

### Security and access control

- Cloud Identity is not available in
Cloud de Confiance. Use third-party identities
through Workforce Identity Federation (such as from Google Workspace,
Microsoft, or Okta), or [service
accounts](/iam/docs/service-account-overview) for authentication and
authorization in Cloud de Confiance. Regular
Google Accounts and groups are unavailable for Identity and Access Management (IAM) in
Cloud de Confiance.

- OAuth scope names are consistent between Google Cloud and
Cloud de Confiance. If an OAuth scope includes
`googleapis` in Google Cloud, it also does so in
Cloud de Confiance.

- IAM roles and permissions are consistent between
Google Cloud and
Cloud de Confiance.

### Network

- Cloud de Confiance runs a separate, distinct
network that's isolated from Google Cloud. The data center
infrastructure for Cloud de Confiance isn't
shared with Google Cloud.

- Inter-data center network traffic uses a separate WAN that isn't shared
with Google Cloud.

- There's separate connectivity to the Internet, using peering or transit.

- Create or assign a Virtual Private Cloud (VPC) for applications to use when you
create a project in Cloud de Confiance. Unlike
in Google Cloud, a default network isn't created
automatically for projects.

Learn more about key networking differences and available features in the following guides:

- [Virtual Private Cloud](/vpc/docs/tpc-differences)

- [Cloud NAT](/nat/docs/tpc-differences)

- [Network Service Tiers](/network-tiers/docs/tpc-differences)

- [Cloud VPN](/network-connectivity/docs/vpn/concepts/tpc-differences)

- [Cloud Interconnect](/network-connectivity/docs/interconnect/tpc-differences)

- [Cloud Router](/network-connectivity/docs/router/tpc-differences)

- [Cloud DNS](/dns/docs/tpc-differences)

- [Cloud Load Balancing](/load-balancing/docs/tpc-differences)

- [Cloud Next Generation Firewall](/firewall/docs/tpc-differences)

- [VPC Service Controls](/vpc-service-controls/docs/tpc-differences)

- [Google Cloud Armor](/armor/docs/tpc-differences)

### Workflows and tools

- Cloud Shell is unavailable in
Cloud de Confiance. Instead, you must install
command line tools locally. Update or adapt any workflows or tools that
expect access to Cloud Shell , including any documentation examples
that include an integrated Cloud Shell experience.

- By default, the gcloud CLI works with Google Cloud
and uses Google Accounts for authentication and authorization. Using the
gcloud CLI with Cloud de Confiance
requires some additional setup to target
Cloud de Confiance and to use an external
identity. For more information, see [Set up the gcloud CLI for
Cloud de Confiance](/docs/get-started-tpc/setup-gcloud).

- Update workflows or processes to ensure that the gcloud CLI
targets Cloud de Confiance.

- If a feature or products is unavailable in
Cloud de Confiance, the corresponding
gcloud CLI commands and parameters are also unavailable.

- Ensure that you have set your target `GOOGLE_CLOUD_UNIVERSE_DOMAIN`
environment variable when using client libraries.

- Provide the appropriate Cloud de Confiance
prefix, such as `s3ns`, to
identify projects in Cloud de Confiance. For
example, a project named `example-project` must be referenced as
`s3ns:example-project`

- When using the Cloud de Confiance console, your chosen language is selected at
sign-on and cannot be changed from within the Cloud de Confiance console.

### Organization setup

- In Cloud de Confiance, your operator creates
and provides you with an empty organization. You can't create a new
organization yourself, unlike in Google Cloud.

- The guided organization setup flow in the Cloud de Confiance console is not
available in Cloud de Confiance.

### Project identifiers

Similar to Google Cloud, projects in Cloud de Confiance
have a user-specified project name, a project ID, and a project number. *Unlike*
in Google Cloud, the project ID has a universe-specific prefix,
`s3ns:`. This prefix is
automatically added by Cloud de Confiance when you
create a project, you don't need to add it yourself when specifying a new
project name. For example, the same project might have:

- The project name `Ponycopter`

- The project ID `s3ns:ponycopter`

- The project number `123456789012`

Project IDs are always used with their universe-specific prefix, including in
the Cloud de Confiance console and when specifying the project in commands and API
calls. The exception to this is when project IDs appear in user-created service
account names. You can read more about this in [Service
accounts](#service_accounts).

### Service names, endpoints, and resources

Review these differences carefully if you plan to use Cloud de Confiance
services programmatically or from the command line, particularly if you intend
to reuse existing Google Cloud code or scripts.

- 

**Service names:** Service names such as `bigquery.googleapis.com` are the
*same* in Cloud de Confiance and
Google Cloud. These are the names that you'll see, for
example, when you enable or disable APIs for your project.

- 

**Service endpoints:** Service endpoints (also known as API endpoints) are
the URLs used to make requests to Cloud de Confiance
APIs, including the [Discovery service](/docs/discovery). Unlike service
names, these are *different* in Cloud de Confiance, with a different universe-specific domain. For example,
`bigquery.googleapis.com` becomes `bigquery.s3nsapis.fr`.

- 

**Service resources:** You can specify service resources in multiple ways.
Don't forget when specifying service resources that all Cloud de Confiance
project IDs have a [Cloud de Confiance
prefix](#workflows_and_tools) (`s3ns:`), which must be included when specifying a
project as part of a resource name or URL.

- 

If you use a unique [full resource
name](https://google.aip.dev/122#full-resource-names) (FRN) to specify a
service resource, the FRN is the *same* as the one you'd use in
Google Cloud, including `googleapis`. For example,
`//bigquery.googleapis.com/projects/my-project/datasets/my-dataset` is
the same in both universes.

- 

If you use a [resource name without its parent
API](https://google.aip.dev/122), such as
`projects/my-project/dataset/my-dataset`, the name is also the *same* as
the one you'd use in Google Cloud.

- 

If you use a URL, that URL uses the universe-specific service endpoint
domain and so is
*different* to Google Cloud. For example,
`https://bigquery.googleapis.com/bigquery/v2/projects/my-project/datasets/my-dataset`
becomes `https://bigquery.s3nsapis.fr/bigquery/v2/projects/my-project/datasets/my-dataset` in Cloud de Confiance.

### Service accounts

[Service account](/iam/docs/service-account-overview) email addresses (including universe-managed service accounts, also known as *service agents*) use universe-specific domains and so are *different* to those you'd use in Google Cloud:



| 
Google Cloud | 
Cloud de Confiance | 
Usage | 
|

| 
`developer. gserviceaccount. com` | 
`developer. s3ns-system. iam. gserviceaccount. com` | 
Used in the Compute Engine default service account. | 
|

| 
`iam. gserviceaccount. com` | 
`s3ns. iam. gserviceaccount. com` | 
Used in domains for most user-managed service accounts. | 
|

| 
`s3ns-system. iam. gserviceaccount. com` | 
Used for some service agents. | 
|

| 
`system. gserviceaccount. com` | 
`s3ns-system. system. gserviceaccount. com` | 
Used for some service agents. | 
|

| 
Other uses of `gserviceaccount. com` | 
`s3ns-system. system. gserviceaccount. com` | 
Used for some service agents. | 
|


So, for example:

- The default Compute Engine service account in your project might have the
address `1234567-compute@developer.s3ns-system.iam.gserviceaccount.com`

- A user-created service account might have the address
`my-service-account@my-project.s3ns.iam.gserviceaccount.com`

For user-created accounts, note that the **parent project's [universe-specific
prefix](#project_identifiers) is not used**. If in doubt about a particular service account, visit
the **Identity and Access Management** pages in the Cloud de Confiance console to see the full names with
domains of all your project's service accounts and service agents, including
those created by Cloud de Confiance:


[Go to IAM](https://console.cloud.s3nscloud.fr/iam-admin)

If you are using GKE, workload identity pool domains (and any Kubernetes ServiceAccounts that use them) are also
specified differently in different universes. You can read more about this in
the GKE [differences
page](/kubernetes-engine/docs/tpc-differences).

### Documentation

Documentation for Cloud de Confiance is adapted
from Google Cloud's documentation, with some differences. For
example, pages about Google Cloud services that are not available in Cloud de Confiance
are not included in this documentation site.

Learn more in [About Cloud de Confiance by S3NS documentation](/docs/overview/gcd-documentation).

## What's next

Review the product-specific [differences page for each product](/docs/overview/gcd-documentation#differences) to learn more
about additional differences between Google Cloud and
Cloud de Confiance.

To get started using Cloud de Confiance, review
the following pages:

- [Set up the gcloud CLI for Cloud de Confiance](/docs/get-started-tpc/setup-gcloud)

- [Set up an identity provider](/docs/get-started-tpc/set-up-identity-provider)