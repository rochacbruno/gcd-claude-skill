# Set up your organization

Source: https://berlin.devsitetest.how/docs/get-started-tpc/set-up-organization
Last updated: 2026-07-17

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

Get started

](https://berlin.devsitetest.how/docs/get-started)












# Set up your organization 






- On this page 
- [ Configuration options ](#configuration_options)
- [ About Fabric FAST ](#about_fabric_fast)

- [ Which Fabric FAST setup is for me? ](#which-setup)

- [ What's next ](#whats_next)
- 









When you first onboard to Google Cloud Dedicated, you
are provided with a new empty
[organization](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).
To use this organization, you need to configure it with projects, a network, and
other resources. Google Cloud Dedicated provides
multiple options for configuring your organization, including [Fabric
FAST](#about_fabric_fast): a Terraform framework that helps you quickly set up
the resources you and your users need to get started.

This page is for administrators who need to configure a new organization in
Google Cloud Dedicated.

Before you read this guide, you should:

- 

Understand the basic Google Cloud Dedicated
concepts described in the [Google Cloud Dedicated
overview](/docs/overview/tpc-overview)

- 

If you are already familiar with setting up an organization in
Google Cloud, review the [key
differences](/docs/overview/tpc-key-differences) between
Google Cloud and your universe. The resource hierarchy
is the same in both universes and our recommended organization structures
follow the same patterns. However, there are some differences you should be aware of,
particularly if you choose to adapt your own landing zone Terraform.

## Configuration options

There are several possible options for configuring a new organization in
Google Cloud Dedicated.

- **Minimal setup**: If you just want to try out
Google Cloud Dedicated features in a new
organization before doing a full setup, you can follow our [minimal
setup](/docs/get-started-tpc/set-up-organization/minimal-setup) to get
started.

For production setup, you can choose from the following:

- 

**Basic setup with Fabric FAST**: If you have a smaller organization or
developing a proof-of-concept, possibly limited experience with cloud
configuration, and don't expect to (or immediately expect to) manage all
your infrastructure by using Terraform, we provide a [*starter* Fabric FAST
Terraform option](/docs/get-started-tpc/set-up-organization/basic-setup).
This option provides you with a single-step configuration that meets best
practices in terms of basic resource and network setup.

After you have performed this setup, you can continue to manage your
organization using the Google Cloud CLI or the Google Cloud Dedicated console, or
incrementally grow the starter stage by adding resources and features while
still using Terraform.

- 

**Enterprise setup with Fabric FAST**: (Recommended for most enterprise
users) Use our [*classic* Fabric FAST Terraform
option](/docs/get-started-tpc/set-up-organization/enterprise-setup). This
option provides greater flexibility and choices for multiple types of
organization and their business needs, and lets your teams continue to
manage their projects, networks, policies, and more by using Terraform in
source control (["infrastructure as code"](/docs/terraform/iac-overview)).

- 

**Reuse existing Terraform**: (Advanced users only) If you have existing
Terraform "landing zone" modules that you have used in
Google Cloud, you can adapt and reuse them to configure your
organization in Google Cloud Dedicated. If you
choose this option, you should carefully review the [differences between the
two universes](/docs/overview/tpc-key-differences), both at a high level and
for any services you want to use.

- 

**Manual configuration**: You can manually create projects, networks,
policies, and other resources by using the Google Cloud CLI or the
Google Cloud Dedicated console, following the instructions in the relevant documentation.

Configuration from the Google Cloud Dedicated console is not available in
Google Cloud Dedicated.

## About Fabric FAST

Setting up a production-ready cloud organization is often a time-consuming
process. Fabric FAST is an opinionated toolkit that helps you do this by
providing:

- A robust organization design that includes the typical elements required by
enterprise customers, including projects, folders, networks, and security
policies.

- A reference implementation of the FAST design using Terraform that you can
apply quickly to create the resources your organization needs.

You can learn more about Fabric FAST in its
[documentation](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/fast).

Fabric FAST is currently the only supported landing zone Terraform for
Google Cloud Dedicated.

### Which Fabric FAST setup is for me?

If you want to use Fabric FAST but are still not sure which option to use, the
following compares our starter and classic configurations:



| 
Feature | 
Classic | 
Starter | 
|




| 
**Execution** | 
Requires running Terraform in strict sequential stages (Stage 0 for bootstrap, Stage 1 for folders/security, Stage 2 for networks, Stage 3 for apps). | 
Flattens the workflow. You define your folders, networks, and application projects all at once in Stage 0. | 
|

| 
**Organization structure** | 
Uses a deep, enterprise-grade folder tree: for example, separating Common, Networking, and Security at the top level, then branching into Tenants containing Environments. | 
Uses a flat, pragmatic structure. Everything simply lives inside either Dev or Prod. | 
|

| 
**Separation of duties** | 
Designed for large enterprises where different teams manage different layers (a Network team manages VPCs, a Security team manages firewalls, App teams manage workloads). | 
Designed for smaller organizations, startups, or proof-of-concepts where a single team (or even a single engineer) manages the entire stack end-to-end. | 
|

| 
**Networking complexity** | 
Often implements complex hub-and-spoke topologies, cross-region routing, and dedicated security perimeters (VPC-SC). | 
Provides simple, isolated Shared VPCs per environment with basic, sensible firewall rules to get workloads communicating immediately. | 
|



We also recommend visiting the [Fabric FAST
documentation](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/fast)
to see the full range of networking, security, and other options offered by
Fabric FAST: depending on your organization's technical needs you might prefer
to go straight to the "classic" FAST configuration.

Fabric FAST also provides a third "hardened" organization option with additional
security controls. While this has not yet been customized for
Google Cloud Dedicated, you can use it as a source if
you want to copy specific controls and security configuration into one of the
other provided options.

## What's next

- Try out Google Cloud Dedicated with a [minimal
setup](/docs/get-started-tpc/set-up-organization/minimal-setup).

- Learn about our "starter" Fabric FAST setup and how to use it in [Basic
setup with Fabric
FAST](/docs/get-started-tpc/set-up-organization/basic-setup).

- Learn more about Fabric FAST and how to use it to set up and manage an
enterprise organization in [Enterprise setup with Fabric
FAST](/docs/get-started-tpc/set-up-organization/enterprise-setup).