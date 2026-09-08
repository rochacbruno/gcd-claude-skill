# Quickstart: Create your Cloud de Confiance by S3NS resource hierarchy

Source: https://documentation.s3ns.fr/resource-manager/docs/manage-google-cloud-resources
Last updated: 2026-09-07

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/resource-manager/docs/tpc-differences) for more details.














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

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Resource Manager

](https://documentation.s3ns.fr/resource-manager/docs)






- 








[

Guides

](https://documentation.s3ns.fr/resource-manager/docs/resource-manager-overview)

















- On this page ** 
- [ Before you begin ](#before-you-begin)
- [ View your resources ](#view_your_resources)
- [ Create a project resource ](#create_a_project_resource)
- [ Create a folder resource ](#create_a_folder_resource)
- [ Grant IAM roles at the organization level ](#grant-iam-roles-org)
- [ Create a billing account ](#create_a_billing_account)
- [ Migrate existing billing accounts ](#migrate_existing_billing_accounts)
- [ View billing accounts under the organization resource ](#view_billing_accounts_under_the_organization_resource)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Manage your Cloud de Confiance by S3NS resources 




This page explains how to view and manage your Cloud de Confiance by S3NS
resources, grant Identity and Access Management (IAM) roles at the organization
level, and manage organization resource billing accounts using the
[Cloud de Confiance console](https://console.cloud.s3nscloud.fr/).





## Before you begin 



- 

Make sure that you have an
[organization resource](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

An organization resource is available for Google Workspace customers:


- 
**Google Workspace:** Sign up for [Google Workspace](https://support.google.com/a/answer/53926).


Once you have created your Google Workspace or Cloud Identity account and associated it with a
domain, your organization resource will be automatically created for you. The resource will be
provisioned at different times depending on your account status:


- 
If you are new to Cloud de Confiance and have not created a project yet, the
organization resource will be created for you when you log in to the
Cloud de Confiance console and accept the terms and conditions.


- 


If you are an existing Cloud de Confiance user, the organization
resource will be created for you when you create a new project or
billing account (if one doesn't already exist). Any projects you
created previously will be listed under "No organization", and this
is normal. The organization resource will appear and the new project
you created will be linked to it automatically.




You will need to move any projects you created under "No organization" into your new
organization resource. For instructions on how to move your projects, see
[Migrating projects into an organization resource](/resource-manager/docs/migrating-projects-billing).




The organization resource that is created will be linked to your Google Workspace or
Cloud Identity account with the project or billing account you created set as a child resource.
All projects and billing accounts created under your Google Workspace or Cloud Identity domain
will be children of this organization resource.


- 
For information about how to migrate pre-existing projects, see
[Migrating existing projects](/resource-manager/docs/migrating-projects-billing).


Each Google Workspace or Cloud Identity account is associated with exactly
one organization resource. An organization resource is associated with exactly
one domain, which is set when the organization resource is created.

**Note:** Trying to register an organization with a domain that
already exists will result in a "This domain is already in use" error. To
resolve this, follow the steps in
[Resolve "This domain is already in use"](https://support.google.com/a/answer/80610#zippy=%2Cthis-domain-is-already-in-use%2Cthis-domain-has-been-registered-and-is-in-the-process-of-ownership-verification).

- 

Make sure that you have the Organization Administrator role on the
organization resource.

- 















Make sure that you have the following role or roles on the organization:

Billing Account Creator, Folder Creator, Project Creator



#### Check for the roles





- 


In the Cloud de Confiance console, go to the IAM** page.


[Go to IAM](https://console.cloud.s3nscloud.fr/projectselector/iam-admin/iam?supportedpurview=organizationId)


- 

Select the organization.



- 


In the **Principal** column, find all rows that identify you or a group that
you're included in. To learn which groups you're included in, contact your
administrator.




- 
For all rows that specify or include you, check the **Role** column to see whether
the list of roles includes the required roles.





#### Grant the roles





- 


In the Cloud de Confiance console, go to the **IAM** page.





[Go to IAM](https://console.cloud.s3nscloud.fr/projectselector/iam-admin/iam?supportedpurview=organizationId)


- 

Select the organization.



- 
Click person_add **Grant access**.


- 


In the **New principals** field, enter your user identifier.

This is typically the identifier for a user in a workforce identity pool. For details,
see [
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users), or contact your administrator.





- 
Click **Select a role**, then search for the role.

- 
To grant additional roles, click add **Add
another role** and add each additional role.


- 
Click **Save**.












## View your resources

To view your Cloud de Confiance resources, follow these steps:

- Go to the Cloud de Confiance console
[Manage resources](https://console.cloud.s3nscloud.fr/cloud-resource-manager)
page.


[Go to Manage resources](https://console.cloud.s3nscloud.fr/cloud-resource-manager)

- All projects and folders in the organization resource are listed on the
page.

## Create a project resource

To create a new project, do the following:


- 
Go to the **Manage resources** page in the Cloud de Confiance console.







[Go to Manage Resources](https://console.cloud.s3nscloud.fr/cloud-resource-manager?walkthrough_id=resource-manager--create-project&start_index=1#step_index=1)

The remaining steps appear in the Cloud de Confiance console.





- Click **Create project**.


- 
In the **New project** window that appears, enter a project
name and select a billing account as applicable. A project name can contain
only letters, numbers, single quotes, hyphens, spaces, or exclamation
points, and must be between 4 and 30 characters.



- 
Enter the parent organization or folder resource in the **Parent
resource** box. That resource will be the hierarchical parent of
the new project.



- When you're finished entering new project details, click
**Create**.

Once you have created your first project, your organization resource will be
provisioned automatically.

## Create a folder resource

Once you have an organization resource, you can create folder resources and
begin to organize your resource hierarchy. To create a folder in your
organization resource, follow these steps:

- Go to the
Cloud de Confiance console
[Manage resources](https://console.cloud.s3nscloud.fr/cloud-resource-manager)
page.


[Go to Manage resources](https://console.cloud.s3nscloud.fr/cloud-resource-manager)

- Click **Create folder**, and select one of the following options:

- **Standard Google Cloud folder**: A standard
[folder resource](/resource-manager/docs/cloud-platform-resource-hierarchy#folders).

- **Compliant folder**: An
[Assured Workloads folder](/assured-workloads/docs/key-concepts#folders),
which provides additional regulatory, regional, or sovereign controls
for Cloud de Confiance by S3NS resources. Selecting this option will take you to
Assured Workloads to
[create a folder](/assured-workloads/docs/create-folder).

- In the **Folder name** box, enter your new folder's name.

- Under **Parent resource**, click **Browse**, then select the organization
resource or folder under which you want to create your new folder.

- When you're finished entering new folder details, click **Create**.

## Grant IAM roles at the organization level

To grant organization-level roles, follow these steps:

- Go to the Cloud de Confiance console
[IAM & admin](https://console.cloud.s3nscloud.fr/iam-admin/iam/)
page:


[Go to IAM & Admin](https://console.cloud.s3nscloud.fr/iam-admin/iam/)

- The **IAM** page that appears shows the following details:

- The **Principals** column shows the accounts that have roles in the
organization resource, including your account and domain.

- The **Role(s)** column shows the roles that each principal has.

- Next to your account, you should see **Organization Administrator**
under **Role(s)**.

- Next to the domain account, you should see **Project Creator** under
**Role(s)**.

- If you see **Multiple** under **Role(s)**, the account has more than
one role. Click the drop-down to see what roles a principal has.

- To grant roles to an existing principal, click the drop-down under
**Role(s)** and then select each role you want the principal to have.

- When you're finished selecting roles, click **Save**.

- To add a new principal, click **Add** at the top of the page. In the **Add
principals** dialog that appears:

- Enter an email address in the **Principals** field.

- Under **Roles**, select each role you want the principal to have.

- When you're finished selecting roles, click **Add**.

The principals you added now have the organization-level permissions you
selected.

## Create a billing account

- Go to the Cloud de Confiance console [Billing](https://console.cloud.s3nscloud.fr/billing) page:


[Go to the Billing page](https://console.cloud.s3nscloud.fr/billing)

- Click **Create account**.

- In the **Create a new billing account** dialog that appears, enter the
appropriate details, including a billing account name and your billing
information.

- The options you see depend on the country of your billing address.

- For United States accounts, you can't change tax status after you create
the billing account.

- When you're finished entering details, click **Submit and enable billing**.

You've now created a new billing account for your organization resource.

## Migrate existing billing accounts

If you are a Google Workspace or Cloud Identity customer with existing Cloud Billing
accounts, you can migrate them to your organization resource. Migrating a Cloud Billing account
into an organization resource doesn't affect project services.

You must have these roles to migrate billing accounts:


- 
You must be a **Billing Account Administrator** for the Cloud Billing
account that you want to migrate.


- 
You must be a **Billing Account Creator** on the organization resource to which you
want to migrate your Cloud Billing account.


- 
If you want to migrate a Cloud Billing account from an existing organization resource,
you must be a **Billing Account Administrator** for the organization resource that
you are migrating the Cloud Billing account from.


To learn about granting these roles, see the
[Overview of Cloud Billing access control](/billing/docs/how-to/billing-access).

To migrate your existing billing accounts into an organization resource, follow the steps below:


- 
Go to the Cloud de Confiance console [Billing](https://console.cloud.s3nscloud.fr/billing) page:


[Go to the Billing page](https://console.cloud.s3nscloud.fr/billing)


- 
From the **Select an organization** menu, select an organization resource to see the
Cloud Billing accounts associated with it, or select **No organization**
to see billing accounts that aren't associated with an organization resource.


- 
Under **Billing account name**, click the name of the Cloud Billing
account that you want to migrate. The billing account overview page opens.


- 
In the Billing navigation menu, click **Account management**.


- 
At the top of the Account management page, click business 
**Change Organization**, then select the organization resource to which you want to
migrate the Cloud Billing account.


## View billing accounts under the organization resource

To view billing accounts under an organization resource, follow these steps:

- Go to the Cloud de Confiance console [Billing](https://console.cloud.s3nscloud.fr/billing) page:


[Go to the Billing page](https://console.cloud.s3nscloud.fr/billing)

All billing accounts for the organization resource are listed on the page.






## Clean up




To delete the project you created for this quickstart:

- 

Go to the Cloud de Confiance console
[Manage resources](https://console.cloud.s3nscloud.fr/cloud-resource-manager)
page.

[Go to Manage resources](https://console.cloud.s3nscloud.fr/cloud-resource-manager)

- 

In the list of resources, select the project that you want to delete.

- 

Click **Delete**.

- 

In the **Shut down project** dialog that appears, enter the project ID,
and then click **Shut down**.

The project resources you selected are deleted and all billing and traffic
serving stops.






## What's next



- Try
[Migrating existing projects into the organization resource](/resource-manager/docs/migrating-projects-billing).

- You don't have to move all your project resources at the same time.

- It's best to start by moving a test project first, and then move the rest
of the projects later.