# Get support

Source: https://berlin.devsitetest.how/docs/overview/gcd-support
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












# Get support 






- On this page 
- [ Before you begin ](#before-you-begin)
- [ Create a support case ](#create-case)
- [ Prerequisites ](#prerequisites)

- [ Set up a Google Cloud organization ](#organization)
- [ Configure an Assured Workloads folder ](#aw-folder)
- [ Create an empty Google Cloud project ](#create-project)
- [ Submit your information to Google ](#submit-info)

- 










Learn how to create support cases for
Google Cloud Dedicated in Germany during the private preview. For the
preview, support is provided by Google.

## Before you begin 

Before you create your first support case, you must complete the
[prerequisites](#prerequisites), including creating a dedicated
Google Cloud project for support requests. You need this project
in addition to any projects that you create in
Google Cloud Dedicated in Germany. This process ensures that your
support case is routed correctly and that you receive support at no additional
cost.

## Create a support case 

Follow these steps to create a technical support case.

Make sure you file the support case against the dedicated project that you
created for support cases. This ensures that your request is routed to the
Google Cloud Dedicated in Germany support team in the EU. If you
haven't created this project yet, see the [prerequisites](#prerequisites).

- In the Google Cloud console, on the
[project selector page](https://developers.google.com/google-cloud-console/projectselector2/home/dashboard),
select your dedicated support project.

- Go to the [**Support Cases** page](https://developers.google.com/google-cloud-console/support/cases).

- Click **Get help**.

- 

In **Quick details**, fill out the following information:

- 

In **Select your product**, choose the product that you want support for,
such as Compute Engine or Cloud Storage.

- 

In **How would you describe your issue?**, enter a brief summary of the
issue.

- 

In **Observed error message**, include any relevant error messages.

- 

In **Priority**, select a priority based on the business impact of this
issue.

- 

Click **Next**. The form displays a resources page with suggested
documentation. After reviewing the information, click **Next** again.

- 

In the **Detailed description** form, enter more specific information
about the issue.

- 

The fields on this page are dynamic and change based on the product that
you select. For example, for a Compute Engine issue, you might be asked
for the VM instance name and zone.

- 

In the text area, provide a complete description of the issue, including
error messages, logs, and steps to reproduce the issue.

- 

To create the case, click **Submit**.

## Prerequisites

Before you create your first support case, follow the steps in this section to
ensure that your case is handled by the correct team and that you receive
support at no additional cost. You only need to complete the steps in this
section one time.

This setup process uses the Google Cloud console, not the
Google Cloud Dedicated in Germany console.

As part of this process, you will create:

- A Google Workspace or Cloud Identity account

- A Google Cloud organization

- An Assured Workloads folder dedicated to your support cases

- An empty Google Cloud project to use to file support cases

### Set up a Google Cloud organization

A Google Cloud organization is the root node of the Google Cloud resource
hierarchy and a prerequisite for using Assured Workloads. For more
information, see
[Creating and managing organization resources](https://developers.google.com/google-cloud-docs/resource-manager/docs/creating-managing-organization).

- 

If you already have a Google Cloud organization, skip this section, and
[configure an Assured Workloads folder](#aw-folder).

- 

If you don't have a Google Cloud organization, you need either a
Google Workspace or a Cloud Identity account associated with your domain.

#### Create a Cloud Identity account

This section explains how to create a Cloud Identity account.
If you already have a Google Workspace account, skip this section, and
[create a Google Cloud organization](#create-organization).

- Go to the following sign-up page: 
[https://workspace.google.com/gcpidentity/signup?sku=identitypremium](https://workspace.google.com/gcpidentity/signup?sku=identitypremium).

- Follow the guided instructions.

- When prompted, provide your business information and domain name.

- Choose **Free edition**.

During setup, you need to verify ownership of your domain. After your
Google Cloud account is active and your domain is verified, you can create a
Google Cloud organization.

#### Create a Google Cloud organization

After you set up a Google Workspace account or Cloud Identity account, the first
project that you create triggers the creation of the organization resource for
your domain. The organization resource is created automatically.

- Sign in to the Google Cloud console using your Google Workspace or
Cloud Identity super administrator account.

- Go to the
[project creation page](https://developers.google.com/google-cloud-console/projectcreate).

- Fill out the form to create a new Google Cloud project.

To verify that the organization exists, in the console, navigate to the
[**Identity & Organization** page](https://developers.google.com/google-cloud-console/iam-admin/org-onboarding).

For more information, see
[Set up Cloud Identity as a Google Cloud admin](https://developers.google.com/google-cloud-docs/identity/docs/set-up-cloud-identity-admin).

### Configure an Assured Workloads folder

To configure an Assured Workloads folder, follow these steps. An
Assured Workloads folder provides a regulatory boundary for any
projects, resources, and workloads within it, ensuring that they are compliant
with a specific control package. In this case, Assured Workloads folder
ensures EU data residency. For more information about
Assured Workloads, see the
[Assured Workloads overview](https://developers.google.com/google-cloud-docs/assured-workloads/docs/overview).

Your dedicated support project must be created in this folder.

#### Grant permissions for Assured Workloads

To create an Assured Workloads folder, you must be granted the
**Assured Workloads Administrator** (`roles/assuredworkloads.admin`) role, which
contains the minimum IAM permissions to create and manage
Assured Workloads folders.

- In the console, go to the [**IAM** page](https://developers.google.com/google-cloud-console/iam-admin/iam).

- In the resource selector, select your organization.

- Click person_add **Grant access**.

- For **New principals**, enter the email address of the user or group that is
creating the Assured Workloads folder.

- From the **Select a role** menu, search for
**Assured Workloads Administrator**, then click
**Assured Workloads Administrator**.

- Click **Save**.

- Verify that the principal and the corresponding role are listed in the
IAM page.

#### Create an Assured Workloads folder

You need a dedicated Assured Workloads folder to ensure that support
is provided by personnel in the EU.

- In the console, go to the
[**Manage resources** page](https://developers.google.com/google-cloud-console/cloud-resource-manager).

- Click **Create Folder**, and select **Compliant folder**. You are redirected
to the Assured Workloads creation flow.

- 

In the step to **Add folder details**:

- 

In **Folder name**, enter a descriptive name for the folder, such as
`GCD-EU-Support-Folder`. The folder name must be a minimum of 4 characters
in length and a maximum of 30, and can only contain letters, numbers,
spaces, and hyphens.

- 

In **Organization**, select the organization to create your folder in, or
select an appropriate folder location within your organizations structure.
You can't change this location later.

- 

In **Folder location**, select the location in the resource hierarchy
where the folder will be created. An Assured Workloads folder can
be created as a child of an organization or of another folder.

- 

Click **Next**.

- 

In the step to **Choose a control package option**, select
**Regional Controls**.

- 

Select **EU Data Boundary and Support** from the drop-down menu. This option
enforces the EU Data Boundary and support restrictions.

- 

In **Select resource location**, choose the location where resource creation
and usage will be enforced by the folder's organization policy.

- 

Click **Next**.

- 

In the step to **Review and create folder**, review the details about your
folder and ensure that they are correct. Then, click **Create**.

### Create an empty Google Cloud project

Use this project to file all of your Google Cloud Dedicated in Germany support cases. This project
ensures that all Google Cloud Dedicated in Germany cases are routed to the appropriate support team.
The project must be in the Assured Workloads folder that you created in
the previous step.

Keep this project empty. Its sole purpose is to establish a designated node for
your Google Cloud Dedicated in Germany support cases.

- In the console, go to the
[**Manage resources** page](https://developers.google.com/google-cloud-console/cloud-resource-manager).

- In the **Resources** list, select the Assured Workloads folder that
you created for support cases.

- Click **Create project**.

- Name your project. Use a descriptive project name, like
`GCD-Support-Project`. Make a note of your generated project ID and project
number. You need them when you submit your information to Google.

- Click **Create**.

### Submit your information to Google

To complete the setup, provide the following details to the
Google Cloud Dedicated in Germany team. We use this information to
enable the support routing for your account.

- Google Cloud organization ID

- The project number of the project that you created for your support cases

Send this information to your Google contact, or reply directly to your
Google Cloud Dedicated in Germany Preview welcome email.

- Our team will apply the configurations needed to route your cases and enable
Standard Support for this project at no cost.

- The provisioning can take up to 48 business hours. Don't submit any cases
until provisioning completes.