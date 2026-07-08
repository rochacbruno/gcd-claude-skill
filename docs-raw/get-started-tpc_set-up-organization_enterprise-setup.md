# Enterprise setup with the Fabric FAST toolkit

Source: https://berlin.devsitetest.how/docs/get-started-tpc/set-up-organization/enterprise-setup
Last updated: 2026-07-07

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












# Enterprise setup with the Fabric FAST toolkit 






- On this page 
- [ What should I know first? ](#what_should_i_know_first)
- [ About Fabric FAST stages ](#about_fabric_fast_stages)
- [ Before you begin ](#before_you_begin)

- [ Grant required permissions ](#grant_required_permissions)
- [ Create a temporary project ](#create_a_temporary_project)
- [ Get the Terraform ](#get_the_terraform)

- [ Apply the Organization setup Terraform ](#apply_the_organization_setup_terraform)
- [ Apply additional stages ](#apply_additional_stages)
- [ What's next ](#whats_next)
- 









This page introduces you to Fabric FAST and how to use it to configure a
production-ready organization in
Google Cloud Dedicated. Fabric FAST is a highly
configurable Terraform toolkit for setting up an organization. It reflects many
best practices around scalability, security, and maintainability, using patterns
that have worked well for many Google Cloud customers. Fabric
FAST was developed for Google Cloud but is fully supported for
Google Cloud Dedicated.

This page is for experienced administrators who need to configure a new
organization in Google Cloud Dedicated. It focuses on
initial resource setup, but provides links to Fabric FAST's extensive
documentation for further details.

If you have a smaller organization, or are developing a proof-of-concept, or if
you are less familiar with Terraform, consider our [Basic
setup](/docs/get-started-tpc/set-up-organization/basic-setup), which provides
you with a relatively simple organization that's ready to deploy workloads in a
single step. For more details, see [Which Fabric FAST setup is for
me?](/docs/get-started-tpc/set-up-organization#which-setup).

## What should I know first? 

Before you read this guide, you should:

- 

Understand the basic Google Cloud Dedicated
concepts described in the [Google Cloud Dedicated
overview](/docs/overview/tpc-overview).

- 

Understand the Google Cloud Dedicated [resource
hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy),
including organizations, folders, and projects.

- 

Understand [organization policies](/organization-policy/overview).

- 

Be familiar with using
[Terraform](https://developer.hashicorp.com/terraform/intro).

- 

If you are already familiar with setting up resources for
Google Cloud, we recommend that you review the key
[differences between Google Cloud Dedicated and
Google Cloud](/docs/get-started-tpc/differences).

If you have used Fabric FAST on Google Cloud, you can skip ahead
to [Before you begin](#before_you_begin).

## About Fabric FAST stages

Fabric FAST uses the concept of *stages* to iteratively build your organization.
For example, you first set up basic resources, then can add security,
networking, and so on. Each stage includes one or more pre-configured YAML
*datasets* that specify the type and number of resources you want to create,
letting you select between best practices for different types of organization
and different technical needs. For example, you can choose between different
network datasets depending on your networking and security needs. You can deploy
these configurations "as is" (other than providing your own details such as your
billing account) or edit them to meet your specific needs. The provided datasets
are verified to work on Google Cloud Dedicated, and
can be used to bootstrap a complete landing zone.

Each stage also aligns with typical organizational boundaries, which lets you
delegate ownership of each stage to the team responsible for the types of
resources it manages. For example, as its name suggests, the networking stage
sets up all the networking elements and is usually the responsibility of a
dedicated networking team within the organization. Depending on your
organization's size and complexity, as you go through this guide and the Fabric
FAST documentation you might delegate responsibility to different team
administrators as you add new stages.

The Fabric FAST stages are:

- **Organization setup**: Combines the organization-level bootstrap together
with the initial configuration of the resource hierarchy. This stage
configures high level Identity and Access Management (IAM) and organization policies,
and the initial layers of the resource hierarchy that partitions the org
into different environments and scopes. Fabric FAST provides a special
`classic-gcd` dataset for this stage for use with your universe.

- **VPC-SC**: Implements a VPC Service Controls configuration, and includes resource
auto-discovery.

- **Networking**: Manages centralized network resources, and provides a way to
share them to application and service teams. This stage provides several
different design as YAML datasets, including hub-and-spoke with VPC
peerings, VPNs, NVAs and NCC.

- **Project factory**: Allows simplified management of folder hierarchies and
projects using YAML-based configuration files, helping you set up groups of
projects for management by different application teams or business units.

- **Security**: Manages centralized security configurations and resources like
Cloud KMS, and provides a space for additional security-related
resources. Typically this stage is owned by a central security team.

All of these stages except organization setup are optional, and their use depends on
actual requirements. This guide focuses on the **Organization setup** stage. You
can read more about the resources created in this stage in the [Fabric FAST
documentation](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/blob/master/fast/stages/0-org-setup/README.md#classic-fast-dataset).

## Before you begin

Ensure the following:

- You have [an identity provider (IdP) configured for your organization](/docs/get-started-tpc/set-up-identity-provider) and
that you are signed in to Google Cloud Dedicated with your administrator ID.

- You have [set up the Google Cloud CLI](/docs/get-started-tpc/setup-gcloud) for use with Google Cloud Dedicated.

- You have the `git` and `terraform` tools installed on your local machine:

- [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- [Install Terraform](/docs/terraform/install-configure-terraform) (minimum version 1.12)

- 

You have the following information ready:

- Your chosen [principal](/iam/docs/principals-overview#workforce) who should be granted administrator permissions for your organization. This can either be your own ID or (recommended) an administrator user group of which you are a member.

- Your chosen [essential contact](/resource-manager/docs/manage-essential-contacts) email address for core projects

- 

Your [organization resource](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) ID. You can find this in the Google Cloud Dedicated console, or by running the following Google Cloud CLI command:


```
gcloud organizations list
```


This lists all the organizations to which you belong (there should only be one!) and their corresponding IDs.

### Grant required permissions

Run the following commands to grant the principal running the deployment the required IAM permissions:


```
export FAST_PRINCIPAL = " PRINCIPAL_ID " 

export FAST_ORG_ID = " ORG_ID " 

# set needed roles (billing role only needed for organization-owned account) 
export FAST_ROLES = "\ 
roles/billing.admin \ 
roles/logging.admin \ 
roles/iam.organizationRoleAdmin \ 
roles/orgpolicy.policyAdmin \ 
roles/resourcemanager.folderAdmin \ 
roles/resourcemanager.organizationAdmin \ 
roles/resourcemanager.projectCreator \ 
roles/resourcemanager.tagAdmin \ 
roles/owner" 

for role in $FAST_ROLES ; do 
gcloud organizations add-iam-policy-binding $FAST_ORG_ID \ 
--member $FAST_PRINCIPAL --role $role --condition None
done 
```


Replace the following:

- ` PRINCIPAL_ID `: An identifier for the relevant principal. You can learn more about how to specify identities and groups from Workforce Identity Federation in [Principal identifiers](/iam/docs/principal-identifiers).

- ` ORG_ID `: Your organization resource ID.

### Create a temporary project

Fabric FAST Terraform requires at least one existing project to run, because organization policy services are not automatically available at the organization root during initial setup. If this is your first time applying the Terraform in an empty organization, create a temporary project at the root of your new organization with the following steps:

- [Create a project](/resource-manager/docs/creating-managing-projects) in
your organization and make a note of its project ID.

- 

Set the project as your current project for the Google Cloud CLI:


```
gcloud config set project PROJECT_ID 
```


- 

Enable the required services in your project by running the following command:


```
gcloud services enable \ 
bigquery.googleapis.com \ 
cloudbilling.googleapis.com \ 
cloudresourcemanager.googleapis.com \ 
essentialcontacts.googleapis.com \ 
iam.googleapis.com \ 
logging.googleapis.com \ 
orgpolicy.googleapis.com \ 
serviceusage.googleapis.com
```


You can delete this project if you like once you have finished your setup.

### Get the Terraform

Clone the Fabric FAST repository to your local machine by running the following command:


```
git clone https://github.com/GoogleCloudPlatform/cloud-foundation-fabric.git
```


After the files are copied to your machine, change to the Fabric FAST organization setup stage root directory as your working directory to get started.


```
cd cloud-foundation-fabric/fast/stages/0-org-setup
```


## Apply the Organization setup Terraform

By default, Fabric FAST uses the `classic` dataset for this stage. However,
because Google Cloud Dedicated has significant
differences from Google Cloud at this level, including billing
and endpoints, we provide a special `classic-gcd` dataset, adapting the `classic`
dataset for your universe. You must use this dataset rather than the default version.

Follow the instructions in
[README-GCD](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/blob/master/fast/stages/0-org-setup/README-GCD.md)
to switch to `classic-gcd` and update any relevant configuration files with the
information you gathered in [Before you begin](#before_you_begin) before
applying the Terraform. You might also need to refer to the stage's
[README](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/blob/master/fast/stages/0-org-setup/README.md)
for additional information.

## Apply additional stages

Follow the instructions in the [Fabric FAST documentation](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/fast) to apply any
additional stages that you require. Additional stages don't require any special
customization to work with Google Cloud Dedicated.

## What's next

- Explore your organization and verify your setup by trying a [suggested
tutorial](/docs/get-started-tpc/suggested-tutorials)