# Quickstart: Create your Google Cloud Dedicated in Germany resource hierarchy

Source: https://berlin.devsitetest.how/resource-manager/docs/manage-google-cloud-resources
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/resource-manager/docs/tpc-differences) for more details.














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

Resource Manager

](https://berlin.devsitetest.how/resource-manager/docs)






- 








[

Guides

](https://berlin.devsitetest.how/resource-manager/docs/resource-manager-overview)

















- On this page ** 
- [ Before you begin ](#before-you-begin)
- [ View your resources ](#view_your_resources)
- [ Create a Project resource ](#create_a_project_resource)
- [ Create a Folder resource ](#create_a_folder_resource)
- [ Grant IAM roles at the organization level ](#grant_roles_at_the_organization_level)
- [ Create a billing account ](#create_a_billing_account)
- [ Migrate existing billing accounts ](#migrate_existing_billing_accounts)
- [ View billing accounts under the organization resource ](#view_billing_accounts_under_the_organization_resource)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Manage your Google Cloud Dedicated in Germany resources 




This page explains how to view and manage your Google Cloud Dedicated in Germany
resources, grant Identity and Access Management (IAM) roles at the organization
level, and manage organization resource billing accounts using the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/).





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
If you are new to Google Cloud Dedicated and have not created a project yet, the
organization resource will be created for you when you log in to the
Google Cloud Dedicated console and accept the terms and conditions.


- 


If you are an existing Google Cloud Dedicated user, the organization resource will
be created for you when you create a new project or billing account. Any projects you created
previously will be listed under "No organization", and this is normal. The organization
resource will appear and the new project you created will be linked to it automatically.




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

- 

Make sure that you have the Organization Administrator role on the
organization resource.

- 















Make sure that you have the following role or roles on the organization:

Billing Account Creator, Folder Creator, Project Creator



#### Check for the roles





- 


In the Google Cloud Dedicated console, go to the IAM** page.


[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=organizationId)


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


In the Google Cloud Dedicated console, go to the **IAM** page.





[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=organizationId)


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

To view your Google Cloud Dedicated resources, follow the steps below:

- Go to the Google Cloud Dedicated console
[Manage resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager)
page.


[Go to Manage Resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager)

- On the dropdown at the top of the page, select the organization resource
for which you want to manage resources.

- All Projects and Folders in the organization resource are listed on the page.

## Create a Project resource

To create a new project, do the following:


- 
Go to the **Manage resources** page in the Google Cloud Dedicated console.







[Go to Manage Resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager?walkthrough_id=resource-manager--create-project&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud Dedicated console.





- 
On the **Select organization** drop-down list at the top of the page, select the
organization resource in which you want to create a project. If you are a free trial user, skip this
step, as this list does not appear.


- Click **Create Project**.


- 
In the **New Project** window that appears, enter a project name and select a
billing account as applicable. A project name can contain only letters, numbers, single
quotes, hyphens, spaces, or exclamation points, and must be between 4 and 30 characters.


- 
Enter the parent organization or folder resource in the **Location** box. That resource
will be the hierarchical parent of the new project.



- When you're finished entering new project details, click **Create**.

Once you have created your first Project, your organization resource will be
provisioned automatically.

## Create a Folder resource

Once you have an organization resource, you can create Folder resources and
begin to organize your resource hierarchy. To create a Folder in your
organization resource, follow the steps below:

- Go to the
Google Cloud Dedicated console
[Manage resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager)
page.


[Go to Manage Resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager)

- On the dropdown at the top of the page, select the organization resource
for which you want to create a Folder resource.

- Click **Create Folder**.

- In the **Create Folder** window that appears, enter a Folder name.

- If you want to create the Folder resource inside a Folder that already
exists, enter the parent Folder name in the **Destination** box.

- When you're finished entering new Folder details, click **Create**.

## Grant IAM roles at the organization level

To grant organization-level roles, follow the steps below:

- 

Go to the Google Cloud Dedicated console
[IAM & admin](https://console.cloud.berlin-build0.goog/iam-admin/iam/)
page:


[Go to IAM & Admin](https://console.cloud.berlin-build0.goog/iam-admin/iam/)

- 

Click **Select**, then use the drop-down to select the organization resource for
which you want to manage IAM permissions.

- In the list of resources that appears, click the name of the organization resource.

- The **IAM** page that appears shows the following details:

- The **Principals** column shows the accounts that have roles in the
organization resource, including your account and domain.

- The **Role(s)** column shows the roles that each principal has.

- Next to your account, you should see **Organization Administrator**
under **Role(s)**.

- Next to the domain account, you should see **Project Creator** under
**Roles(s)**.

- If you see **Multiple** under **Role(s)**, the account has more than
one role. Click the drop-down to see what roles a principal has.

- To grant roles to an existing principal, click the drop-down under
**Role(s)** and then select each role you want the principal to have.

- When you're finished selecting roles, click **Save**.

- To add a new principal, click **Add** at the top of the page. In the **Add
principals** dialog that appears:

- Enter an email address in the **Principals** box.

- Under **Roles**, select each role you want the principal to have.

- When you're finished selecting roles, click **Add**.

The principals you added now have the organization-level permissions you
selected.

## Create a billing account

- Go to the Google Cloud Dedicated console [Billing](https://console.cloud.berlin-build0.goog/billing) page:


[GO TO THE BILLING PAGE](https://console.cloud.berlin-build0.goog/billing)

- In the drop-down at the top of the page, select the organization resource
for which you want to add a billing account.

- Click **Create account**.

- On the **Create a new billing account** window that appears, enter the
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
Go to the Google Cloud Dedicated console [Billing](https://console.cloud.berlin-build0.goog/billing) page:


[Go to the Billing page](https://console.cloud.berlin-build0.goog/billing)


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

To view billing accounts under an organization resource, follow the steps below:

- Go to the Google Cloud Dedicated console [Billing](https://console.cloud.berlin-build0.goog/billing) page:


[GO TO THE BILLING PAGE](https://console.cloud.berlin-build0.goog/billing)

- In the drop-down at the top of the page, select the organization resource
for which you want to view billing accounts.

All billing accounts for the organization resource are listed on the page.






## Clean up




To delete the Project you just created for this quickstart:

- 

Go to the Google Cloud Dedicated console
[Manage resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager)
page.

[Go to Manage Resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager)

- In the drop-down at the top of the page, select the organization resource
in which you want to delete Project resources.

- In the list of Project resources that appears, select the Project that you
want to delete, then click **Delete**.

- On the **Shut down project** dialog that appears, enter the Project ID,
then click **Shut down**.

The Project resources you selected are deleted and all billing and traffic
serving stops.






## What's next



- Try
[Migrating existing projects into the organization resource](/resource-manager/docs/migrating-projects-billing).

- You don't have to move all your Project resources at the same time.

- It's best to start by moving a test Project first, and then move the rest
of the Projects later.