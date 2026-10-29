# View projects linked to Cloud Billing accounts

Source: https://documentation.s3ns.fr/billing/docs/how-to/view-linked
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/billing/docs/tpc-differences) for more details.














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

Costs and usage management

](https://documentation.s3ns.fr/docs/costs-usage)






- 








[

Cloud Billing

](https://documentation.s3ns.fr/billing/docs)






- 








[

Guides

](https://documentation.s3ns.fr/billing/docs/concepts)












# View projects linked to Cloud Billing accounts 


















































A Cloud Billing account defines who pays for a given set of
resources, and it can be linked to one or more projects. Project usage is
charged to the linked Cloud Billing account. In most cases, you
configure billing when you create a project.

If you're managing billing for projects under a cost center or
if you need to close your Cloud Billing account, you'll need to know
which projects are linked to your Cloud Billing account.

## View the projects linked to a billing account

### Permissions required to complete this task

To view the list of projects linked to a Cloud Billing account, you
need a role that includes the following
[permission](/iam/docs/roles-permissions/billing) 
on your Cloud Billing account:

- [`billing.resourceAssociations.list`](/billing/docs/how-to/custom-roles#resource_associations) 
to view project associations for the billing account.

To gain this permission using a predefined role, ask your administrator to
grant you one of the following
[Cloud Billing IAM](/billing/docs/how-to/billing-access) 
roles on your Cloud Billing account:

- Billing Account Viewer

- Billing Account Costs Manager

- Billing Account Administrator

### How to view the projects linked to a billing account

Follow these steps to open a billing account and then view a list of projects
linked to that billing account.

- 

In the Cloud de Confiance console, go to the **Account management** page for
the Cloud Billing account.

[Go to Account Management page](https://console.cloud.s3nscloud.fr/billing/manage) 

- 

At the prompt, choose the Cloud Billing account that you want to
view.

- 

On the **Account management** page, linked projects are listed under
**Projects linked to this billing account**.

A padlock icon lock 
displays next to each project that's locked to its linked
Cloud Billing account. For information about unlocking or locking this
link, see
[Secure the link between a project and its billing account](/billing/docs/how-to/secure-project-billing-account-link).

For information about changing the billing account for a project, see
[Enable, disable, or change billing for a project](/billing/docs/how-to/modify-project).

## View the billing account linked to each of your projects

### Permissions required to complete this task

To view a tabular list of all your projects and their linked
Cloud Billing, you need a role that includes the following
[permission](/iam/docs/roles-permissions/billing) 
on each of your projects:

- [`resourcemanager.projects.get`](/billing/docs/how-to/custom-roles#resource_associations) 
to view projects.

To gain this permission using a predefined role, ask your administrator to
grant you one of the following roles on your projects:

- Project Browser

- Project Viewer

- Project Editor

- Project Owner

### How to view a list of projects and their linked billing account

Follow these steps to view a list of all your projects and the billing account
linked to each project.

- 

In the Cloud de Confiance console, go to the **Manage Billing Accounts** page.

[Go to Manage Billing Accounts page](https://console.cloud.s3nscloud.fr/billing) 

- 

Select the **My projects** tab.

You'll see a table that lists all of your projects, and the associated
billing account name and billing account ID. If a billing account isn't
linked to a project, in the **Billing account** column, you see
*Billing is disabled*.

A padlock icon lock 
displays next to each project that's locked to its linked
Cloud Billing account. For information about unlocking or locking this
link, see
[Secure the link between a project and its billing account](/billing/docs/how-to/secure-project-billing-account-link).

For information about enabling billing on a project, see
[Enable billing for an existing project](/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project).

For information about changing the billing account for a project, see
[Enable, disable, or change billing for a project](/billing/docs/how-to/modify-project).

## Verify the status of the linked billing account

A Cloud Billing account can be closed or suspended at any time, causing
billing to become disabled on all projects that remain linked to that account.
[Learn how to confirm the status of the linked Cloud Billing account](/billing/docs/how-to/verify-billing-enabled#billing_account_status).