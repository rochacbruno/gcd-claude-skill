# Enabling Access Transparency

Source: https://berlin.devsitetest.how/assured-workloads/access-transparency/docs/enable
Last updated: 2026-10-26

- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Access Transparency

](https://berlin.devsitetest.how/assured-workloads/access-transparency/docs)






- 








[

Guides

](https://berlin.devsitetest.how/assured-workloads/access-transparency/docs/overview)

























# Enabling Access Transparency



## Requirements for enabling Access Transparency

## Configuring Access Transparency using the Google Cloud Dedicated console

To verify that Access Transparency is enabled for audit purposes on any resource level within your organization:

- 1. Verify that you have the IAM role Access Approval Viewer
(`roles/accessapproval.viewer`) or **Access Transparency Admin** (`roles/axt.admin`). 

- Go to **Security** > **Access Approval** in the Google Cloud Dedicated console.

- Confirm that Access Transparency is enabled on the **Home** tab.

or

- 

Check the Organization-Level Access Transparency IAM Settings Page. 

- 

Go to the **Identity and Access Management** page on the
Google Cloud Dedicated console.

- 

Verify that you have the IAM role
**Access Transparency Admin** (`roles/axt.admin`) listed in the **Role**
column for your **Principal** listing under the organization.

- 

Select any Google Cloud Dedicated organization or project within the organization using the
selector menu.

- 

Go to the **IAM** > **Settings** page.

- Verify that Access Transparency is enabled.