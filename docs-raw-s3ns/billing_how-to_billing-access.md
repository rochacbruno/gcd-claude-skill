# Cloud Billing access control and permissions

Source: https://documentation.s3ns.fr/billing/docs/how-to/billing-access
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












# Cloud Billing access control and permissions 


















































This document describes roles and access permissions for Cloud Billing
accounts.

A Cloud Billing account is set up in Cloud de Confiance and accrues
and calculates costs for your usage of resources and services in
Cloud de Confiance. Cloud Billing lets you control which users have
administrative and cost viewing permissions for specific resources by setting
[Identity and Access Management (IAM)](/iam/docs/overview) 
policies on the resources.

## Cloud Billing access

To grant or limit access to Cloud Billing, you can set an
IAM policy at the
[organization level](/resource-manager/docs/access-control-org),
the Cloud Billing account level, or the project
level. Cloud de Confiance resources inherit
the IAM policies of their parent node, which means you can
set a policy at the organization level to apply it to all the
Cloud Billing accounts, projects, and resources in the
organization.

You can control viewing permissions at different levels for different users or
roles by setting access permissions at the Cloud Billing account or
project level.

To grant permission to a user to view the costs of *all* projects under a
Cloud Billing account, give the user permission to view the costs for
a Cloud Billing account (`billing.accounts.getSpendingInformation`). To
grant permission to a user to view the costs for a *specific*
project, give the user view permissions for individual
projects (`billing.resourceCosts.get`).

## Overview of Cloud Billing roles in IAM

You don't directly give users permissions; instead, you grant them *roles*,
which have one or more permissions bundled within them.

You can grant one or more roles to the same user or on the same resource.

The following predefined Cloud Billing IAM roles let you
use access control to enforce separation of duties:



| 
Role | 
Purpose | 
Level | 
Use Case | 
|

| 
[
**Billing Account Creator**](/billing/docs/how-to/billing-access#billing.creator)

(`roles/billing.creator`) | 
Create new self-serve (online) billing accounts. | 
Organization | 
Use this role for initial billing setup or to allow creation of additional
billing accounts.

Users must have this role to sign up for Cloud de Confiance with a credit card
using their corporate identity.

**Tip**: Minimize the number of users who have this role to help
prevent proliferation of untracked cloud spend in your organization.
| 
|

| 
[
**Billing Account Administrator**](/billing/docs/how-to/billing-access#billing.admin)

(`roles/billing.admin`)
| 
Manage billing accounts (but not create them). | 
Organization or billing account. | 
This role is an owner role for a billing account. Admins can add and edit
payment methods, update payments profile info including
mailing addresses, configure billing exports, view cost information, make
a manual payment, link and unlink projects, and manage other user roles on the billing account. By default, the person who creates the Cloud Billing account is a Billing Account Administrator for the Cloud Billing
account.
| 
|

| 
[
**Billing Account Costs Manager**](/billing/docs/how-to/billing-access#billing.costsManager)

(`roles/billing.costsManager`) | 
Manage budgets and view and export cost information of billing accounts
(but not pricing information). | 
Organization or billing account. | 
Create, edit, and delete budgets, view billing account cost information
and transactions, and manage the export of billing cost data to
BigQuery. Doesn't confer the right to export *pricing* data
or view *custom pricing* in the **Pricing** page. Doesn't allow the
linking or unlinking of projects or otherwise managing the properties of the
billing account.
| 
|

| 
[
**Billing Account Viewer**](/billing/docs/how-to/billing-access#billing.viewer)

(`roles/billing.viewer`) | 
View billing account cost information and transactions. | 
Organization or billing account. | 
Billing Account Viewer access is usually granted to finance teams. It
provides read access to cost and payment information, but doesn't confer the
right to link or unlink projects or otherwise manage the properties of the
billing account. | 
|

| 
[
**Project Billing Costs Manager**](/billing/docs/how-to/billing-access#billing.projectCostsManager)

(`roles/billing.projectCostsManager`) | 
View billing account cost information scoped to projects. | 
Organization or billing account. | 
When granted in conjunction with
[
cost view permissions on *projects*](/billing/docs/how-to/custom-roles#cost_information),
Project Billing Costs Manager provides access to billing information scoped to
the projects to which the user has cost access. Billing information scoped
to projects includes access to Reports, FinOps hub, Budgets and alerts, and
Anomalies.
| 
|

| 
[
**Billing Account User**](/billing/docs/how-to/billing-access#billing.user)

(`roles/billing.user`) | 
Link projects to billing accounts. | 
Organization or billing account. | 
This role has very restricted permissions, so you can grant it broadly.
When granted in combination with Project Creator, the two roles let users
create new projects linked to the billing account on which the Billing
Account User role is granted. Or, when granted in combination with the
Project Billing Manager role, the two roles let users link and unlink
projects on the billing account on which the Billing Account User role is
granted.
| 
|

| 
[
**Project Billing Manager**](/billing/docs/how-to/billing-access#billing.projectManager)

(`roles/billing.projectManager`)
| 
Link and unlink the project to and from a billing account. | 
Organization, folder, or project. | 
When granted in combination with the Billing Account User role, the
Project Billing Manager role lets users attach the project to the
billing account, but doesn't grant any rights over resources. Project Owners
can use this role to let someone else manage the billing for the
project without granting them resource access.
| 
|


The following table lists the details of the predefined IAM
Billing roles, including the permissions bundled within each role.






| 
Role | 
Permissions | 
|



| 

#### Billing Account Administrator

(`roles/ billing.admin`)



Provides access to see and manage all aspects of billing accounts.



Lowest-level resources where you can grant this role:

- 
Billing Account

| 



`billing.accounts.close`



`billing.accounts.get`



`billing. accounts. getCarbonInformation`



`billing.accounts.getIamPolicy`



`billing. accounts. getPaymentInfo`



`billing.accounts.getPricing`



`billing. accounts. getSpendingInformation`



`billing. accounts. getUsageExportSpec`



`billing.accounts.list`



`billing.accounts.move`



`billing. accounts. redeemPromotion`



`billing. accounts. removeFromOrganization`



`billing.accounts.reopen`



`billing.accounts.setIamPolicy`



`billing.accounts.update`



`billing. accounts. updatePaymentInfo`



`billing. accounts. updateUsageExportSpec`




`billing.anomalies.*` 





- `billing.anomalies.get`

- `billing.anomalies.list`

- `billing. anomalies. submitFeedback`






`billing.anomaliesConfigs.*` 





- `billing.anomaliesConfigs.get`

- `billing. anomaliesConfigs. update`





`billing. billingAccountPrice. get`



`billing. billingAccountPrices. list`




`billing. billingAccountServices.*` 





- `billing. billingAccountServices. get`

- `billing. billingAccountServices. list`






`billing. billingAccountSkuGroupSkus.*` 





- `billing. billingAccountSkuGroupSkus. get`

- `billing. billingAccountSkuGroupSkus. list`






`billing. billingAccountSkuGroups.*` 





- `billing. billingAccountSkuGroups. get`

- `billing. billingAccountSkuGroups. list`






`billing.billingAccountSkus.*` 





- `billing.billingAccountSkus.get`

- `billing. billingAccountSkus. list`






`billing.budgets.*` 





- `billing. budgets. configureSpendCap`

- `billing.budgets.create`

- `billing.budgets.delete`

- `billing.budgets.get`

- `billing.budgets.list`

- `billing.budgets.update`





`billing.credits.list`



`billing. finOpsBenchmarkInformation. get`



`billing. finOpsHealthInformation. get`




`billing.resourceAssociations.*` 





- `billing. resourceAssociations. create`

- `billing. resourceAssociations. delete`

- `billing. resourceAssociations. list`






`billing.subscriptions.*` 





- `billing.subscriptions.create`

- `billing.subscriptions.get`

- `billing.subscriptions.list`

- `billing.subscriptions.update`






`chroniclesm.contracts.*` 





- `chroniclesm.contracts.get`

- `chroniclesm.contracts.update`





`cloudasset. assets. searchAllResources`



`cloudnotifications. activities. list`



`cloudsupport.properties.get`




`cloudsupport.techCases.*` 





- `cloudsupport.techCases.create`

- `cloudsupport. techCases. escalate`

- `cloudsupport.techCases.get`

- `cloudsupport.techCases.list`

- `cloudsupport.techCases.update`






`commerceoffercatalog.*` 





- `commerceoffercatalog. agreements. get`

- `commerceoffercatalog. agreements. list`

- `commerceoffercatalog. documents. get`

- `commerceoffercatalog. documents. list`

- `commerceoffercatalog. offers. get`





`compute.commitments.create`



`compute.commitments.get`



`compute.commitments.list`



`compute.commitments.update`



`compute. commitments. updateReservations`




`consumerprocurement.accounts.*` 





- `consumerprocurement. accounts. create`

- `consumerprocurement. accounts. delete`

- `consumerprocurement. accounts. get`

- `consumerprocurement. accounts. list`





`consumerprocurement. consents. check`



`consumerprocurement. consents. grant`



`consumerprocurement. consents. list`



`consumerprocurement. consents. revoke`




`consumerprocurement.events.*` 





- `consumerprocurement.events.get`

- `consumerprocurement. events. list`






`consumerprocurement. licensePools.*` 





- `consumerprocurement. licensePools. assign`

- `consumerprocurement. licensePools. enumerateLicensedUsers`

- `consumerprocurement. licensePools. get`

- `consumerprocurement. licensePools. unassign`

- `consumerprocurement. licensePools. update`






`consumerprocurement. orderAttributions.*` 





- `consumerprocurement. orderAttributions. get`

- `consumerprocurement. orderAttributions. list`

- `consumerprocurement. orderAttributions. update`






`consumerprocurement.orders.*` 





- `consumerprocurement. orders. cancel`

- `consumerprocurement.orders.get`

- `consumerprocurement. orders. list`

- `consumerprocurement. orders. modify`

- `consumerprocurement. orders. place`





`dataprocessing.datasources.get`



`dataprocessing. datasources. list`



`dataprocessing. groupcontrols. get`



`dataprocessing. groupcontrols. list`




`discoveryengine. billingAccountLicenseConfigs.*` 





- `discoveryengine. billingAccountLicenseConfigs. distribute`

- `discoveryengine. billingAccountLicenseConfigs. get`

- `discoveryengine. billingAccountLicenseConfigs. list`

- `discoveryengine. billingAccountLicenseConfigs. retract`





`logging.logEntries.list`



`logging.logServiceIndexes.list`



`logging.logServices.list`



`logging.logs.list`



`logging.privateLogEntries.list`



`recommender. cloudsqlIdleInstanceRecommendations. get`



`recommender. cloudsqlIdleInstanceRecommendations. list`



`recommender. cloudsqlOverprovisionedInstanceRecommendations. get`



`recommender. cloudsqlOverprovisionedInstanceRecommendations. list`




`recommender. commitmentUtilizationInsights.*` 





- `recommender. commitmentUtilizationInsights. get`

- `recommender. commitmentUtilizationInsights. list`

- `recommender. commitmentUtilizationInsights. update`





`recommender. computeAddressIdleResourceRecommendations. get`



`recommender. computeAddressIdleResourceRecommendations. list`



`recommender. computeDiskIdleResourceRecommendations. get`



`recommender. computeDiskIdleResourceRecommendations. list`



`recommender. computeImageIdleResourceRecommendations. get`



`recommender. computeImageIdleResourceRecommendations. list`



`recommender. computeInstanceGroupManagerMachineTypeRecommendations. get`



`recommender. computeInstanceGroupManagerMachineTypeRecommendations. list`



`recommender. computeInstanceIdleResourceRecommendations. get`



`recommender. computeInstanceIdleResourceRecommendations. list`



`recommender. computeInstanceMachineTypeRecommendations. get`



`recommender. computeInstanceMachineTypeRecommendations. list`




`recommender.costInsights.*` 





- `recommender.costInsights.get`

- `recommender.costInsights.list`

- `recommender. costInsights. update`






`recommender. costRecommendations.*` 





- `recommender. costRecommendations. listAll`

- `recommender. costRecommendations. summarizeAll`





`recommender. resourcemanagerProjectUtilizationRecommendations. get`



`recommender. resourcemanagerProjectUtilizationRecommendations. list`




`recommender. spendBasedCommitmentInsights.*` 





- `recommender. spendBasedCommitmentInsights. get`

- `recommender. spendBasedCommitmentInsights. list`

- `recommender. spendBasedCommitmentInsights. update`






`recommender. spendBasedCommitmentRecommendations.*` 





- `recommender. spendBasedCommitmentRecommendations. get`

- `recommender. spendBasedCommitmentRecommendations. list`

- `recommender. spendBasedCommitmentRecommendations. update`






`recommender. spendBasedCommitmentRecommenderConfig.*` 





- `recommender. spendBasedCommitmentRecommenderConfig. get`

- `recommender. spendBasedCommitmentRecommenderConfig. update`






`recommender. usageCommitmentRecommendations.*` 





- `recommender. usageCommitmentRecommendations. get`

- `recommender. usageCommitmentRecommendations. list`

- `recommender. usageCommitmentRecommendations. update`





`resourcemanager. projects. createBillingAssignment`



`resourcemanager. projects. deleteBillingAssignment`



`resourcemanager.projects.get`



`resourcemanager.projects.list`

| 
|

| 

#### Project Billing Manager

(`roles/ billing.projectManager`)



When granted in conjunction with the Billing Account User role, provides access to assign a
project's billing account or disable its billing.



Lowest-level resources where you can grant this role:

- 
Project

| 



`resourcemanager. projects. createBillingAssignment`



`resourcemanager. projects. deleteBillingAssignment`

| 
|

| 

#### Billing Account Viewer

(`roles/ billing.viewer`)



View billing account cost and pricing information, transactions, and billing and commitment
recommendations.



Lowest-level resources where you can grant this role:

- 
Billing Account

| 



`billing.accounts.get`



`billing. accounts. getCarbonInformation`



`billing.accounts.getIamPolicy`



`billing. accounts. getPaymentInfo`



`billing.accounts.getPricing`



`billing. accounts. getSpendingInformation`



`billing. accounts. getUsageExportSpec`



`billing.accounts.list`



`billing.anomalies.get`



`billing.anomalies.list`



`billing.anomaliesConfigs.get`



`billing. billingAccountPrice. get`



`billing. billingAccountPrices. list`




`billing. billingAccountServices.*` 





- `billing. billingAccountServices. get`

- `billing. billingAccountServices. list`






`billing. billingAccountSkuGroupSkus.*` 





- `billing. billingAccountSkuGroupSkus. get`

- `billing. billingAccountSkuGroupSkus. list`






`billing. billingAccountSkuGroups.*` 





- `billing. billingAccountSkuGroups. get`

- `billing. billingAccountSkuGroups. list`






`billing.billingAccountSkus.*` 





- `billing.billingAccountSkus.get`

- `billing. billingAccountSkus. list`





`billing.budgets.get`



`billing.budgets.list`



`billing.credits.list`



`billing. finOpsBenchmarkInformation. get`



`billing. finOpsHealthInformation. get`



`billing. resourceAssociations. list`



`billing.subscriptions.get`



`billing.subscriptions.list`



`chroniclesm.contracts.get`




`commerceoffercatalog.*` 





- `commerceoffercatalog. agreements. get`

- `commerceoffercatalog. agreements. list`

- `commerceoffercatalog. documents. get`

- `commerceoffercatalog. documents. list`

- `commerceoffercatalog. offers. get`





`consumerprocurement. accounts. get`



`consumerprocurement. accounts. list`



`consumerprocurement. consents. check`



`consumerprocurement. consents. list`



`consumerprocurement. orderAttributions. get`



`consumerprocurement. orderAttributions. list`



`consumerprocurement.orders.get`



`consumerprocurement. orders. list`



`dataprocessing.datasources.get`



`dataprocessing. datasources. list`



`dataprocessing. groupcontrols. get`



`dataprocessing. groupcontrols. list`



`discoveryengine. billingAccountLicenseConfigs. get`



`discoveryengine. billingAccountLicenseConfigs. list`



`recommender. commitmentUtilizationInsights. get`



`recommender. commitmentUtilizationInsights. list`



`recommender.costInsights.get`



`recommender.costInsights.list`




`recommender. costRecommendations.*` 





- `recommender. costRecommendations. listAll`

- `recommender. costRecommendations. summarizeAll`





`recommender. spendBasedCommitmentInsights. get`



`recommender. spendBasedCommitmentInsights. list`



`recommender. spendBasedCommitmentRecommendations. get`



`recommender. spendBasedCommitmentRecommendations. list`



`recommender. spendBasedCommitmentRecommenderConfig. get`



`recommender. usageCommitmentRecommendations. get`



`recommender. usageCommitmentRecommendations. list`

| 
|

| 

#### Carbon Footprint Viewer

(`roles/ billing.carbonViewer`)




| 



`billing.accounts.get`



`billing. accounts. getCarbonInformation`



`billing.accounts.list`

| 
|

| 

#### Billing Account Costs Manager

(`roles/ billing.costsManager`)



Manage budgets for a billing account, and view, analyze, and export cost information of a billing
account.



Lowest-level resources where you can grant this role:

- 
Billing Account

| 



`billing.accounts.get`



`billing.accounts.getIamPolicy`



`billing. accounts. getSpendingInformation`



`billing. accounts. getUsageExportSpec`



`billing.accounts.list`



`billing. accounts. updateUsageExportSpec`



`billing.anomalies.get`



`billing.anomalies.list`




`billing.anomaliesConfigs.*` 





- `billing.anomaliesConfigs.get`

- `billing. anomaliesConfigs. update`





`billing.budgets.create`



`billing.budgets.delete`



`billing.budgets.get`



`billing.budgets.list`



`billing.budgets.update`



`billing. resourceAssociations. list`




`recommender.costInsights.*` 





- `recommender.costInsights.get`

- `recommender.costInsights.list`

- `recommender. costInsights. update`



| 
|

| 

#### Billing Account Creator

(`roles/ billing.creator`)



Provides access to create billing accounts.



Lowest-level resources where you can grant this role:

- 
Organization

| 



`billing.accounts.create`



`resourcemanager. organizations. get`

| 
|

| 

#### Account Hierarchy Manager

(`roles/ billing.linkAdmin`)



Authorized to manage billing account hierarchy


| 



`billing.accounts.create`



`billing.accounts.get`



`billing. accounts. getCarbonInformation`



`billing.accounts.getIamPolicy`



`billing. accounts. getPaymentInfo`



`billing.accounts.getPricing`



`billing. accounts. getSpendingInformation`



`billing. accounts. getUsageExportSpec`



`billing.accounts.list`



`billing.accounts.move`



`billing. accounts. removeFromOrganization`



`billing.anomalies.get`



`billing.anomalies.list`



`billing.anomaliesConfigs.get`



`billing. billingAccountPrice. get`



`billing. billingAccountPrices. list`




`billing. billingAccountServices.*` 





- `billing. billingAccountServices. get`

- `billing. billingAccountServices. list`






`billing. billingAccountSkuGroupSkus.*` 





- `billing. billingAccountSkuGroupSkus. get`

- `billing. billingAccountSkuGroupSkus. list`






`billing. billingAccountSkuGroups.*` 





- `billing. billingAccountSkuGroups. get`

- `billing. billingAccountSkuGroups. list`






`billing.billingAccountSkus.*` 





- `billing.billingAccountSkus.get`

- `billing. billingAccountSkus. list`





`billing.budgets.get`



`billing.budgets.list`



`billing.credits.list`



`billing. finOpsBenchmarkInformation. get`



`billing. finOpsHealthInformation. get`



`billing. resourceAssociations. list`



`billing.subscriptions.get`



`billing.subscriptions.list`




`commerceoffercatalog.*` 





- `commerceoffercatalog. agreements. get`

- `commerceoffercatalog. agreements. list`

- `commerceoffercatalog. documents. get`

- `commerceoffercatalog. documents. list`

- `commerceoffercatalog. offers. get`





`consumerprocurement. accounts. get`



`consumerprocurement. accounts. list`



`consumerprocurement. consents. check`



`consumerprocurement. consents. list`



`consumerprocurement. orderAttributions. get`



`consumerprocurement. orderAttributions. list`



`consumerprocurement.orders.get`



`consumerprocurement. orders. list`



`dataprocessing.datasources.get`



`dataprocessing. datasources. list`



`dataprocessing. groupcontrols. get`



`dataprocessing. groupcontrols. list`



`recommender. commitmentUtilizationInsights. get`



`recommender. commitmentUtilizationInsights. list`



`recommender.costInsights.get`



`recommender.costInsights.list`




`recommender. costRecommendations.*` 





- `recommender. costRecommendations. listAll`

- `recommender. costRecommendations. summarizeAll`





`recommender. spendBasedCommitmentInsights. get`



`recommender. spendBasedCommitmentInsights. list`



`recommender. spendBasedCommitmentRecommendations. get`



`recommender. spendBasedCommitmentRecommendations. list`



`recommender. spendBasedCommitmentRecommenderConfig. get`



`recommender. usageCommitmentRecommendations. get`



`recommender. usageCommitmentRecommendations. list`

| 
|

| 

#### Project Billing Costs Manager

(`roles/ billing.projectCostsManager`)



When granted in conjunction with
[
cost view permissions on projects](/billing/docs/how-to/custom-roles#cost_information), provides access to billing
information scoped to the projects to which the user has cost access.



Lowest-level resources where you can grant this role:

- 
Billing Account

| 



`billing.accounts.get`



`billing.accounts.getIamPolicy`



`billing. accounts. getSpendingInformationScoped`



`billing. costRecommendations. listScoped`

| 
|

| 

#### Billing Account User

(`roles/ billing.user`)



When granted in conjunction with the Project Owner role or Project Billing Manager role, provides
access to associate projects with billing accounts.



Lowest-level resources where you can grant this role:

- 
Billing Account

| 



`billing.accounts.get`



`billing.accounts.getIamPolicy`



`billing.accounts.list`



`billing. accounts. redeemPromotion`



`billing.credits.list`



`billing. resourceAssociations. create`

| 
|




## IAM relationships between organizations, projects, and Cloud Billing accounts

Two types of relationships govern the interactions between organizations,
Cloud Billing accounts, and projects: ownership and
payment linkage.

- **Ownership** refers to IAM permission inheritance.

- **Payment linkages** define which Cloud Billing account pays for a
given project.

The following diagram shows the relationship of ownership and payment linkages
for a sample organization.



In the diagram, the Organization node has ownership over Projects 1, 2, and 3,
meaning that it's the IAM permissions parent of the three
projects.

The Cloud Billing account is linked to Projects 1, 2, and 3, meaning
that it pays for costs incurred by the three projects. The
Cloud Billing account can also pay for projects in other organizations,
but the billing account inherits IAM permissions from its parent
organization.

Although Cloud Billing accounts are linked to projects,
Cloud Billing accounts *aren't* parents of projects in an
IAM sense, and therefore projects don't inherit permissions
from the Cloud Billing account they're linked to.

In this example, any users who are granted IAM billing
roles on the organization also have those roles on the Cloud Billing
account or the projects.

## Cloud Billing access control examples

Combine IAM roles as follows to meet the needs of a variety
of scenarios.



| 
Scenario: Small-to-medium enterprise with a preference
for centralized control. | 
|

| 
**User type** | 
**Billing IAM roles** | 
**Billing activities** | 
|

| 
**CEO** | 
Billing Account Administrator | 
Manage payment instrument.

View and approve invoices. | 
|

| 
**CTO** | 
Billing Account Administrator

Project Creator | 
Set budget alerts.

View spend.

Create new billable projects. | 
|

| 
**Development teams** | 
None | 
None | 
|




| 
Scenario: Small-to-medium enterprise with a preference for
delegated authority. | 
|

| 
**User type** | 
**Billing IAM roles** | 
**Billing activities** | 
|

| 
**CEO** | 
Billing Account Administrator | 
Manage payment instrument.

Delegate authority. | 
|

| 
**CFO** | 
Billing Account Administrator | 
Set budget alerts.

View spend. | 
|

| 
**Accounts payable** | 
Billing Account Viewer | 
View and approve invoices. | 
|

| 
**Development teams** | 
Billing Account User

Project Creator | 
Create new billable projects. | 
|




| 
Scenario: Separate financial planning and procurement
functions | 
|

| 
**User type** | 
**Billing IAM roles** | 
**Billing activities** | 
|

| 
**Procurement or Central IT** | 
Billing Account Administrator | 
Manage payment instrument.

Set budget alerts.

Communicate spend to development teams. | 
|

| 
**Financial planning** | 
Billing Account Viewer | 
View billing reports.

Process exports.

Communicate with CxO. | 
|

| 
**Accounts payable** | 
Billing Account Viewer | 
Approve invoices. | 
|

| 
**Development teams** | 
Billing Account User

Project Creator | 
Create new billable projects. | 
|




| 
Scenario: Development agency | 
|

| 
**User type** | 
**Billing IAM roles** | 
**Billing activities** | 
|

| 
**CEO** | 
Billing Account Administrator | 
Manage payment instrument.

Delegate authority. | 
|

| 
**CFO** | 
Billing Account Administrator | 
Set budget alerts.

View spend.

Approve invoices. | 
|

| 
**Project lead** | 
Billing Account User

Project Creator | 
Create new billable projects. | 
|

| 
**Project development team** | 
None | 
Develop within existing projects. | 
|

| 
**Client** | 
Project Billing Manager | 
Take payment ownership of the project when it's completed. | 
|


## How to update Cloud Billing permissions

To learn how to review, add, or remove Cloud Billing permissions,
follow the guidance on
[Manage access to Cloud Billing accounts](/billing/docs/how-to/grant-access-to-billing) 

## Related topics

- [Manage access to Cloud Billing accounts](/billing/docs/how-to/grant-access-to-billing) 

- [Cloud Billing API access control](/billing/v1/how-tos/access-control) 

- [Granting, changing, and revoking Access](/iam/docs/granting-changing-revoking-access) 
in the IAM documentation

- [Create custom roles for Cloud Billing](/billing/docs/how-to/custom-roles)