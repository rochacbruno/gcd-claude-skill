# Roles and permissions

Source: https://berlin.devsitetest.how/iam/docs/roles-overview
Last updated: 2026-06-25

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

IAM

](https://berlin.devsitetest.how/iam/docs)






- 








[

Guides

](https://berlin.devsitetest.how/iam/docs/overview)












# Roles and permissions 






- On this page 
- [ Before you begin ](#before-you-begin)
- [ Role types ](#role-types)
- [ Role components ](#components)
- [ Basic roles ](#basic)

- [ Legacy basic roles ](#legacy-basic)

- [ Predefined roles ](#predefined)
- [ Custom roles ](#custom)

- [ Supported permissions ](#custom-role-supported-permissions)
- [ Permission dependencies ](#custom-role-permission-dependencies)
- [ Custom roles lifecycle ](#custom-role-lifecycle)

- [ What's next ](#whats_next)
- 










This page describes Identity and Access Management (IAM) roles, which are collections of
IAM permissions.

A role contains a set of permissions that allows you to perform specific actions on
Google Cloud Dedicated resources.
To make permissions available to principals, including
users, groups, and service accounts, you grant roles to the principals.

## Before you begin 

- Understand the [basic concepts](/iam/docs/overview) of IAM.

## Role types 

There are three types of roles in IAM:

- **Basic roles**, which provide broad access to Google Cloud Dedicated resources.

- **Predefined roles**, which provide granular access for a specific service and
are managed by Google Cloud Dedicated.

- **Custom roles**, which provide granular access according to a user-specified
list of permissions.

To determine if a permission is included in a basic, predefined, or custom role,
you can use one of the following methods:

- 

View the role in the Google Cloud Dedicated console.

[Go to Roles](https://console.cloud.berlin-build0.goog/iam-admin/roles) 

- 

Run the [`gcloud iam roles describe`](/sdk/gcloud/reference/iam/roles/describe)
command.

- 

Get the role using the appropriate REST API method:

- For predefined roles, use [`roles.get()`](/iam/reference/rest/v1/roles/get).

- For project-level custom roles, use
[`projects.roles.get()`](/iam/docs/reference/rest/v1/projects.roles/get).

- For organization-level custom roles, use
[`organizations.roles.get()`](/iam/docs/reference/rest/v1/organizations.roles/get).

- 

For basic and predefined roles only: Search the [permissions
reference](/iam/docs/permissions-reference) to see if the permission is granted by the role.

- 

For predefined roles only: Search the [predefined role
descriptions](/iam/docs/roles-permissions) to see which
permissions the role includes.

For guidance on when to use specific role types, see [Choose which type of role
to use](/iam/docs/choose-role-type).

## Role components

Each role has the following components:

- **Title**: A human-readable name for the role. The role
title is used to identify the role in the Google Cloud Dedicated console.

- 

**Name**: An identifier for the role in one of the following
formats:

- Predefined roles: `roles/ SERVICE . IDENTIFIER `

- Project-level custom roles: `projects/ PROJECT_ID /roles/ IDENTIFIER `

- Organization-level custom roles: `organizations/ ORG_ID /roles/ IDENTIFIER `

The role name is used to identify the role in [allow policies](/iam/docs/allow-policies).

- 

**ID**: A unique identifier for the role. For basic and
predefined roles, the ID is the same as the role name. For custom roles, the
ID is everything after `roles/` in the role name.

- 

**Description**: A human-readable description of the role.

- 

**Stage**: The stage of the role in the launch lifecycle, such as
`ALPHA`, `BETA`, or `GA`. To learn more about launch stages, see
[Testing and deploying](#custom-role-testing-deploying).

- 

**Permissions**: The permissions included in the role. Permissions allow
principals to perform specific actions on Google Cloud Dedicated in Germany resources. When you
grant a role to a principal, the principal gets all of the permissions in the
role.

Permissions have the following format:


```
SERVICE . RESOURCE . VERB 
```


For example, the `compute.instances.list` permission allows a user to list
the Compute Engine instances they own, and `compute.instances.stop` allows
a user to stop a VM.

Permissions usually, but not always, correspond 1:1 with REST methods. That
is, each Google Cloud Dedicated service has an associated permission for each
REST method that it has. To call a method, the caller needs the associated
permission. For example, to call the Pub/Sub API's
`projects.topics.publish` method, you need the `pubsub.topics.publish`
permission.

- 

**ETag**: An identifier for the version of the role to help
prevent concurrent updates from overwriting each other. Basic and predefined
roles always have the ETag `AA==`. ETags for custom roles change each time you
modify the roles.

## Basic roles



Basic roles are highly permissive roles that give broad access to
Google Cloud Dedicated resources.

The basic roles in IAM are Admin (`roles/admin`), Writer
(`roles/writer`), and Reader (`roles/reader`). IAM also has three
legacy basic roles that existed prior to the introduction of IAM:
Owner (`roles/owner`), Editor (`roles/editor`), and Viewer
(`roles/viewer`). To learn more about these roles, see [Legacy basic
roles](#legacy-basic) on this page.

The following table summarizes the permissions that the Admin, Writer, and
Reader give principals across all Google Cloud Dedicated services:




| 
Basic role | 
Permissions | 
|



| 
**Reader** (`roles/reader`) | 



Permissions for read-only actions that don't affect state, such as
viewing (but not modifying) existing resources or data.




For a list of permissions in the Reader role, see the role details in
the Google Cloud Dedicated console:




[Go to Reader
role](https://console.cloud.berlin-build0.goog/iam-admin/roles/details/roles%3Creader)


| 
|

| 
**Writer** (`roles/writer`) | 



All of the permissions in the Reader role, *plus* permissions
for actions that modify state, such as changing existing resources.




The permissions in the Writer role let you create and delete resources
for most Google Cloud Dedicated services. However, the Writer role doesn't
contain permissions to perform all actions for all services. For more
information about how to check whether a role has the permissions that
you need, see [Role types](#role-types) on this page.




For a list of permissions in the Writer role, see the role details in
the Google Cloud Dedicated console:




[Go to Writer
role](https://console.cloud.berlin-build0.goog/iam-admin/roles/details/roles%3Cwriter)


| 
|

| 
**Admin** (`roles/admin`) | 



All of the permissions in the Writer role, *plus* permissions
for actions like the following:





- 
Completing sensitive tasks, like managing tag bindings for
Compute Engine resources


- 
Managing roles and permissions for a project and all resources
within the project


- 
Setting up billing for a project





The Admin role *doesn't* contain all permissions for all
Google Cloud Dedicated resources. For example, it doesn't contain
permissions to modify your Cloud Billing payment information or
create IAM deny policies.




For a list of permissions in the Admin role, see the role details in
the Google Cloud Dedicated console:




[Go to Admin
role](https://console.cloud.berlin-build0.goog/iam-admin/roles/details/roles%3Cadmin)


| 
|



You can't use the Google Cloud Dedicated console to grant the Reader, Writer, or Admin
roles. Instead, use the API or the gcloud CLI. You can also create
entitlements for these roles using [Privileged Access Manager](/iam/docs/pam-overview).

For instructions, see [Granting, changing, and revoking
access](/iam/docs/granting-changing-revoking-access).

### Legacy basic roles

Legacy basic roles existed prior to the introduction of IAM.
They were originally known as *primitive roles*. Unlike with other basic
roles, you can't add [conditions](/iam/docs/conditions-overview) to role bindings for legacy
basic roles.

The legacy basic roles are Owner (`roles/owner`), Editor (`roles/editor`), and
Viewer (`roles/viewer`).

When you grant a legacy basic role to a principal, the principal gets all of the
permissions in the role. The principal also gets any permissions that
services provide to principals with legacy basic roles—for example,
permissions gained through [Cloud Storage
convenience values](/storage/docs/access-control/iam#convenience-values) and [BigQuery special
group membership](/bigquery/docs/access-control-basic-roles).

The following table summarizes the permissions that the legacy basic roles give
principals across all Google Cloud Dedicated services:




| 
Legacy basic role | 
Permissions | 
|



| 
**Viewer** (`roles/viewer`) | 



Permissions for read-only actions that don't affect state, such as
viewing (but not modifying) existing resources or data.




For a list of permissions in the Viewer role, see the role details in
the Google Cloud Dedicated console:




[Go to Viewer
role](https://console.cloud.berlin-build0.goog/iam-admin/roles/details/roles%3Cviewer)


| 
|

| 
**Editor** (`roles/editor`) | 



All viewer permissions, *plus* permissions for actions that
modify state, such as changing existing resources.




The permissions in the Editor role let you create and delete resources
for most Google Cloud Dedicated services. However, the Editor role doesn't
contain permissions to perform all actions for all services. For more
information about how to check whether a role has the permissions that
you need, see [Role types](#role-types) on this page.




For a list of permissions in the Editor role, see the role details in
the Google Cloud Dedicated console:




[Go to Editor
role](https://console.cloud.berlin-build0.goog/iam-admin/roles/details/roles%3Ceditor)


| 
|

| 
**Owner** (`roles/owner`) | 



All Editor permissions, *plus* permissions for actions like the
following:





- 
Completing sensitive tasks, like managing tag bindings for
Compute Engine resources


- 
Managing roles and permissions for a project and all resources
within the project


- 
Setting up billing for a project





The Owner role *doesn't* contain all permissions for all
Google Cloud Dedicated resources. For example, it doesn't contain
permissions to modify your Cloud Billing payment information or
create IAM deny policies.




For a list of permissions in
the Owner role, see the role details in the Google Cloud Dedicated console:




[Go to Owner
role](https://console.cloud.berlin-build0.goog/iam-admin/roles/details/roles%3Cowner)


| 
|



Generally, you can grant legacy basic roles using the Google Cloud Dedicated console,
the API, or the gcloud CLI. However, you must use the
Google Cloud Dedicated console to grant the Owner role in the following situations:

- The user that you're granting the Owner role to isn't part of your
organization.

- The project that you're granting the Owner role on isn't part of any
organization.

Additionally, you can only grant the Owner role to the following types of
principals:

- Google Accounts

- Service accounts in your organization

- Google groups in your organization

To learn how to grant roles, see [Granting, changing, and revoking
access](/iam/docs/granting-changing-revoking-access).

## Predefined roles

In addition to the basic roles, IAM provides additional
predefined roles that give granular access to specific Google Cloud Dedicated
resources. These roles are created and maintained by Google. Google
automatically updates their permissions as necessary, such as when
Google Cloud Dedicated adds new features or services.

You can grant multiple roles to the same user, at any level of the resource
hierarchy. For example, the same user can have the Compute Network Admin and
Logs Viewer roles on a project, and also have the Pub/Sub Publisher role on a
Pub/Sub topic within that project. To list the permissions contained in
a role, see
[Getting the role metadata](/iam/docs/creating-custom-roles#getting_the_role_metadata).

For help choosing the most appropriate predefined roles, see
[Find the right predefined roles](/iam/docs/choose-predefined-roles).

For a list of predefined roles, see the [roles
reference](/iam/docs/understanding-roles).

## Custom roles

IAM also lets you create *custom IAM roles*.
Custom roles help you enforce the principle of least privilege, because they
help to ensure that the principals in your organization have only the
permissions that they need.

Custom roles are user-defined, and allow you to bundle one or more supported
permissions to meet your specific needs. When you create a custom role, you must
choose an organization or project to create it in. You can then grant the custom
role on the organization or project, as well as any resources within that
organization or project. You can only create 300
per organization and 300 per project.

You can only grant a custom role within the project or organization in which you
created it. You cannot grant custom roles on other projects or organizations,
or on resources within other projects or organizations.

You create a custom role by combining one or more of the supported
IAM permissions. To learn how to create a custom role,
see [Create and manage custom roles](/iam/docs/creating-custom-roles).

### Supported permissions

You can include many, but not all, IAM permissions in custom roles. Each permission
has one of the following support levels for use in custom roles:




| 
Support level | 
Description | 
|



| 
`SUPPORTED` | 
The permission is fully supported in custom roles. | 
|

| 
`TESTING` | 

Google is testing the permission to check its compatibility with custom roles. You can
include the permission in custom roles, but you might see unexpected behavior. Not
recommended for production use.
| 
|

| 
`NOT_SUPPORTED` | 
The permission is not supported in custom roles. | 
|



To see a full list of the permissions that are supported in custom roles, see
[Support levels for permissions in custom
roles](/iam/docs/custom-roles-permissions-support).

An organization-level custom role can include any of the IAM
permissions that are supported in custom roles. A project-level custom role can
contain any supported permission *except for* permissions that can only be used
at the organization or folder level.

The reason that you can't include folder-specific and organization-specific
permissions in project-level roles is that they don't do anything when granted
at the project level. This is because resources in Google Cloud Dedicated are
organized hierarchically. Permissions are inherited through the resource
hierarchy, meaning that they are effective for the resource and all of that
resource's descendants. However, organizations and folders are always above
projects in the
Google Cloud Dedicated resource hierarchy. As a result, you'll never be able to use
a permission that you were given at the project level to access folders or
organizations. As a result, folder-specific and organization-specific
permissions—for example, `resourcemanager.folders.list`—are
ineffective for project-level custom roles.

### Permission dependencies

Some permissions are effective only when given together. For example, to
update an allow policy, you must read the policy before you can modify
and write it. As a result, to update an allow policy, you almost always need the
`getIamPolicy` permission for that service and resource type, in addition to the
`setIamPolicy` permission.

To make sure your custom roles are effective, you can create custom roles based
on predefined roles with similar permissions. Predefined roles are designed with
specific tasks in mind and contain all of the permissions you need to accomplish
those tasks. Reviewing these roles can help you see which permissions are
usually granted together. Then, you can use that information to design effective
custom roles.

To learn how to create a custom role based on a predefined role, see
[Creating and managing custom roles](/iam/docs/creating-custom-roles).

### Custom roles lifecycle

The following sections describe key considerations at each phase of a custom
role's lifecycle. You can use this information to inform how you create and
manage your custom roles.

#### Creation

When you're creating a custom role, choose an ID, title, and description that
help you identify the role:

- 

**Role ID**: The role ID is a unique identifier for the role. It can be up to
64 bytes long and can contain uppercase and
lowercase alphanumeric characters, underscores, and periods. You can't reuse a
role ID within an organization or project.

You can't change role IDs, so choose them carefully. You can delete a custom
role, but you can't create a new custom role with the same ID in the same
organization or project until after the 44-day
deletion process has completed. For more information about the deletion
process, see [Deleting a custom role](/iam/docs/creating-custom-roles#deleting_a_custom_role).

- 

**Role title**: The role title appears in the list of roles in the
Google Cloud Dedicated console. The title doesn't have to be unique, but we recommend
using unique and descriptive titles to better distinguish your roles. Also,
consider indicating in the role title if the role was created at the
organization level or the project level.

Role titles can be up to 100 bytes long and
can contain uppercase and lowercase alphanumeric characters and symbols. You
can change role titles at any time.

- 

**Role description**: The role description is an optional field where you can
provide additional information about a role. For example, you could include
the role's intended purpose, the date a role was created or modified, and any
predefined roles that the custom role is based on. Descriptions can be up to
300 bytes long and can contain
uppercase and lowercase alphanumeric characters and symbols.

Also keep [permission dependencies](#custom-role-permission-dependencies) in
mind when creating custom roles.

To learn how to create a custom role based on a predefined role, see [Creating
and managing custom roles](/iam/docs/creating-custom-roles).

#### Launch

Custom roles include a launch stage as part of the role's metadata. The most
common launch stages for custom roles are `ALPHA`, `BETA`, and `GA`. These
launch stages are informational; they help you keep track of whether each role
is ready for widespread use. Another common launch stage is `DISABLED`. This
launch stage lets you [disable a custom role](#custom-role-disable).

We recommend that you use launch stages to convey the following information
about the role:

- `EAP` or `ALPHA`: The role is still being developed or tested, or it includes
permissions for Google Cloud Dedicated services or features that are not yet
public. It is not ready for widespread use.

- `BETA`: The role has been tested on a limited basis, or it includes
permissions for Google Cloud Dedicated services or features that are not generally
available.

- `GA`: The role has been widely tested, and all of its permissions are for
Google Cloud Dedicated services or features that are generally available.

- `DEPRECATED`: The role is no longer in use.

To learn how to change a role's launch stage, see
[Editing an existing custom role](/iam/docs/creating-custom-roles#editing_an_existing_custom_role).

#### Maintenance

You are responsible for maintaining custom roles. This includes updating roles
as your users' responsibilities change, as well as updating roles to let users
access new features that require additional permissions.

If you base your custom role on predefined roles, we recommend routinely
checking those predefined roles for permission changes. Tracking these changes
can help you decide when and how to update your custom role. For example, you
might notice that a predefined role was updated with permissions to use a new
Preview feature, and might decide to add those permissions to your custom role
as well.

To make it easier to see which predefined roles to monitor, we recommend listing
any predefined roles that your custom role is based on in the custom role's
description field. The Google Cloud Dedicated console does this automatically when you
use the Google Cloud Dedicated console to create a custom role based on predefined
roles.

To learn how to update a custom role's permissions and description, see [Editing
an existing custom role](/iam/docs/creating-custom-roles#editing_an_existing_custom_role).

Refer to the [permissions change log](/iam/docs/permissions-change-log) to
determine what roles and permissions have changed recently.

#### Disabling

If you no longer want any principals in your organization to use a custom role,
you can disable the role. To disable the role, change its launch stage to
`DISABLED`.

Disabled roles still appear in your IAM policies and can be
granted to principals, but they don't have any effect.

To learn how to disable a custom role, see
[disabling a custom role](/iam/docs/creating-custom-roles#disabling-custom-role).

## What's next

- Learn how to [grant IAM roles](/iam/docs/granting-changing-revoking-access)
to principals.

- Find out how to
[choose the most appropriate predefined roles](/iam/docs/choose-predefined-roles).

- Learn how to [create custom roles](/iam/docs/creating-custom-roles).

- Learn about the [use cases for specific role types](/iam/docs/choose-role-type).