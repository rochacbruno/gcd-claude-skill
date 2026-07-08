# Quota permissions

Source: https://berlin.devsitetest.how/docs/quotas/permissions
Last updated: 2026-07-07

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












# Quota permissions 






- On this page 
- [ Permissions for viewing quota ](#permissions_viewing)
- [ Permissions for changing quota ](#permissions_changing)
- [ Permissions for viewing quota increase requests ](#permissions_increase)
- [ Permissions for creating an alert policy for a quota ](#permissions_create_alert)
- [ What's next ](#whats_next)
- 










The predefined
[Identity and Access Management (IAM)](/iam/docs/overview) 
role for permissions is named Quota Administrator. This role can be assigned at
the project, folder, and organization levels.

- If granted at the project level, the user will have permission to perform
project-level operations.

- If granted at the folder level, the user will have permission to perform
project-level operations for all projects in that folder.

- If granted at the organization level, the user will have permission to
perform organization level operations. Because IAM permissions
are inherited from the top level, this user will also be granted project and
folder level permissions.

Users who are part of the Project Owners role can assign the Quota Administrator
role to other users at the project level. Users in the Organization Owner role
can assign the Quota Administrator role at the organization level.

## Permissions for viewing quota

To view your project quota in the Google Cloud Dedicated console or to access your project
quota programmatically using the Cloud Quotas API, you must have the
following IAM permissions:

- `resourcemanager.projects.get`

- `resourcemanager.folders.get` if you want to view quota for an entire
[Folder.](/resource-manager/docs/cloud-platform-resource-hierarchy#folders) 

- `resourcemanager.organizations.get` if you want to view quota for an entire
[Organization.](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) 

- [`monitoring.timeSeries.list`](/iam/docs/roles-permissions/monitoring#monitoring.timeSeries.list) 

- [`serviceusage.services.list`](/iam/docs/roles-permissions/serviceusage#serviceusage.services.list) 

- [`cloudquotas.quotas.get`](/iam/docs/roles-permissions/cloudquotas#cloudquotas.quotas.get) 

To learn which [roles](/iam/docs/roles-overview) include
these permissions by default, see the
[IAM permissions reference](/iam/docs/roles-permissions).

Cloud Quotas can also be viewed programmatically by using the
[Service Usage API](/service-usage/docs/reference/rest). To learn about the
IAM roles and permissions required for this approach, see
[Access control with IAM](/service-usage/docs/access-control) in the
Service Usage documentation.

## Permissions for changing quota

To change your quota at the project level, folder level, or organization level,
you must have the following IAM permissions:

- [`serviceusage.quotas.update`](/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.update) 

- [`cloudquotas.quotas.update`](/iam/docs/roles-permissions/cloudquotas#cloudquotas.quotas.update) 

These permissions are included by default for the following
[roles](/iam/docs/roles-overview): Owner, Editor, Quota
Administrator, and Service Usage Admin.

## Permissions for viewing quota increase requests

To view quota increase requests in the Google Cloud Dedicated console, you must have the
following [IAM permissions](/iam/docs/roles-permissions):

- `resourcemanager.projects.get`

- [`serviceusage.services.list`](/iam/docs/roles-permissions/serviceusage#serviceusage.services.list) 

- [`serviceusage.quotas.get`](/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.get) 

## Permissions for creating an alert policy for a quota

To [set up quota alerts](/docs/quotas/set-up-quota-alerts), you must have the
following permission:

- `monitoring.alertPolicies.create`

## What's next

- [Configure VPC Service Controls](/docs/quotas/configure-vpc-service-controls)

- [Use custom organization policies](/docs/quotas/custom-constraints)

- [View and manage quotas](/docs/quotas/view-manage)