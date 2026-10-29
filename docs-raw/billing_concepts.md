# Cloud Billing overview

Source: https://berlin.devsitetest.how/billing/docs/concepts
Last updated: 2026-10-26

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

Costs and usage management

](https://berlin.devsitetest.how/docs/costs-usage)






- 








[

Cloud Billing

](https://berlin.devsitetest.how/billing/docs)






- 








[

Guides

](https://berlin.devsitetest.how/billing/docs/concepts)












# Cloud Billing overview 















Cloud Billing is a collection of tools that help you track and
understand your Google Cloud Dedicated spending, pay your bill, and optimize
your costs.

This document covers the following topics:

- An [introduction to Cloud Billing accounts](#account).
Your Cloud Billing account pays for your
usage of Google Cloud Dedicated resources and services.

- An [overview of resource management in Google Cloud Dedicated](#about_resource_management_for_billing).
The way you organize your Google Cloud Dedicated resources depends on your
organization's structure and affects how you analyze your costs in the
Cloud Billing reports.

Not all Cloud Billing features
that are available in Google Cloud can be used in
Google Cloud Dedicated. See our [differences guide](/billing/docs/tpc-differences) for more details.

Pricing and invoicing in Google Cloud Dedicated are handled by . If you have any questions about pricing or invoicing, contact [Google Cloud Dedicated in Germany billing support]().

## About Cloud Billing accounts

A *Cloud Billing account* is set up in Google Cloud Dedicated and defines
who pays for a given set of Google Cloud Dedicated resources.

This account is used to track all of the costs (charges and savings) incurred by
your Google Cloud Dedicated usage in all projects linked to the Cloud Billing account.

[Access control to a Cloud Billing account](/billing/docs/how-to/billing-access) 
is established by IAM roles.



## About resource management for billing

You can configure billing on Google Cloud Dedicated in Germany in a variety of
ways to meet different needs. This section introduces the core concepts for your
organization and for billing, and discusses how to use them effectively.

### About resources

In the context of Google Cloud Dedicated, a resource can refer to service-level
resources that are used to process your workloads, such as virtual machines and
databases, or to account-level resources that sit above the services, such as
projects, folders, and the organization.

### Resource management

Resource management focuses on how you should configure and grant access to
the various cloud resources for your company/team, specifically the setup and
organization of the account-level resources that sit above the service-level
resources. Account-level resources are the resources involved in setting
up and administering your Google Cloud Dedicated account.

### Resource hierarchy

Google Cloud Dedicated resources are organized hierarchically. This hierarchy lets
you map your organization's operational structure to Google Cloud Dedicated, and
to manage access control and permissions for groups of related resources. The
[resource hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy) 
provides logical attachment points for access management policies
([Identity and Access Management](/iam/docs/overview)) and
[Organization policies](/resource-manager/docs/organization-policy/overview).

Both IAM and Organization policies are inherited through the
hierarchy, and the effective policy at each node of the hierarchy is the result
of policies directly applied at the node and policies inherited from its
ancestors.

For more information on the hierarchy of resources, see the
[Resource Manager documentation](/resource-manager/docs/cloud-platform-resource-hierarchy).

### Organization

- An organization is the root node of the Google Cloud Dedicated hierarchy of
resources.

- All Google Cloud Dedicated resources that belong to an organization are grouped
under the organization node, allowing you to define settings, permissions,
and policies for all projects, folders, resources, and
Cloud Billing accounts it parents.

- A new organization is created for you when you onboard to Google Cloud Dedicated.

- Using an organization, you can centrally manage your Google Cloud Dedicated
resources and your users' access to those resources. This includes:

- Proactive management: reorganize resources as needed (for example,
restructuring or spinning up a new division may require new
projects and folders).

- Reactive management: an organization resource provides a safety net
to regain access to lost resources (for example, if one of your team members
loses their access or leaves the company).

- The various roles and resources that are related to Google Cloud Dedicated
(including the organization, projects, folders, resources, and
Cloud Billing accounts) are managed within the Google Cloud Dedicated console.

For more information on organizations, see the following documentation:

- [Creating and managing organizations](/resource-manager/docs/creating-managing-organization) 

- [Viewing and managing organization resources](/resource-manager/docs/organization-resource-management) 

- [Managing multiple organizations](/resource-manager/docs/managing-multiple-orgs) 

### Folders

- Folders are a grouping mechanism and can contain projects,
other folders, or a combination of both.

- To use folders, you must have an
[organization node](/resource-manager/docs/cloud-platform-resource-hierarchy).

- Folders and projects are all mapped under the organization node.

- Folders can be used to group resources that share common IAM
policies.

- While a folder can contain multiple folders or resources, a given folder or
resource can have exactly one parent.

For more details about using folders, see
[Creating and managing folders](/resource-manager/docs/creating-managing-folders).

### Projects

- All service-level resources are parented by projects, the
base-level organizing entity in Google Cloud Dedicated.

- Projects are *required* to use service-level resources (such as
Compute Engine virtual machines, Pub/Sub topics, and
Cloud Storage buckets).

- You can use projects to represent logical projects, teams,
environments, or other collections that map to a business function or
structure.

- Projects form the basis for enabling services, APIs, and
IAM permissions.

- Any given resource can only exist in one project.

For more details about projects, see the following documentation:

- [Creating and managing projects](/resource-manager/docs/creating-managing-projects) 

- [Moving a project](/resource-manager/docs/moving-projects-folders) 

- [Migrating projects](/resource-manager/docs/project-migration) 

### Resources

- Google Cloud Dedicated service-level resources are the fundamental components
that make up all Google Cloud Dedicated services, such as Compute Engine virtual
machines, Pub/Sub topics, and Cloud Storage buckets.

- For billing and access control purposes, resources exist at the lowest level
of a hierarchy that also includes projects and an organization.

### Labels

- Labels help you categorize your Google Cloud Dedicated resources (such as
Compute Engine instances).

- A label is a key-value pair.

- You can attach labels to each resource, then filter the resources based on
their labels.

- Labels are great for cost tracking at a granular level. Information about
labels is forwarded to the billing system, so you can
[analyze your charges](/billing/docs/how-to/bq-examples) 
by label.

For more details about using labels, see
[Creating and managing labels](/resource-manager/docs/creating-managing-labels).

## Relationships between resources and Cloud Billing accounts

Two types of relationships govern the interactions between organizations,
Cloud Billing accounts, and projects: ownership and
payment linkage.

- **Ownership** refers to IAM permission inheritance.

- **Payment linkages** define which Cloud Billing account pays for a
given project.

*Ownership* of a Cloud Billing account is limited to a single
organization. *Payment linkage* of a project linked to a Cloud Billing
account is not limited by organization ownership. It is possible for a
Cloud Billing account to pay for projects that belong to an
organization that is different than the organization that owns the
Cloud Billing account. For more information on managing the
Cloud Billing account for your projects, see
[Enable, disable, or change billing for a project](/billing/docs/how-to/modify-project).

For information about granting IAM billing roles, see
[Overview of Cloud Billing access control](/billing/docs/how-to/billing-access).