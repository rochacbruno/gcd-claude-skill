# Cloud Billing in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/billing/docs/tpc-differences
Last updated: 2026-08-26

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












# Cloud Billing in Cloud de Confiance versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Billing and cost management differences ](#billing-differences)
- [ Other differences ](#other-differences)

- [ Related guides ](#related-guides)
- 










Cloud Billing is a collection of tools that help you track and understand
your Cloud de Confiance by S3NS spending, pay your bill, and optimize your costs.

This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Billing.



For more detailed information about Cloud Billing, see the
[Cloud Billing overview](/billing/docs/concepts) and the rest of the
Cloud Billing documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud Billing and
the Google Cloud version.
Some notable differences include the following:




- Cloud de Confiance by S3NS does not support self-serve (or online) accounts. If you
are interested in purchasing Cloud de Confiance by S3NS services, you must work with
your operator for Cloud Billing account creation.

- You cannot create, modify, close, or reopen billing accounts from within
Cloud de Confiance by S3NS.

- Customer invoicing is managed by your universe operator. If you require
invoicing or billing support, contact
[Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/).



A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Billing feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Billing and cost management differences



| 

Cost management**
| 



Cost management self-service features, including
**Reports**, **Cost Table**, and
**Cost Breakdown**, are available in Cloud de Confiance by S3NS.




Budgets, alerts, and anomalies are unavailable.




If you need to export billing cost data, contact
[
Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/).


| 
|

| 

**Cost optimization**
| 



Cloud de Confiance by S3NS offers committed use discounts (CUDs). To purchase
spend-based CUDs, contact
[
Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/).




The following products and services are eligible for spend-based
CUDs in Cloud de Confiance by S3NS:





- Cloud SQL

- 
Compute Engine
(including Cloud Run and GKE)


- BigQuery reservations

- Bigtable 1 

- Spanner 1 




Other cost optimization features, such as FinOps Hub, pricing,
cost estimation, and credits, are unavailable in Cloud de Confiance by S3NS.




1 These services are not immediately available for
spend-based CUDs but will be supported in the near future.


| 
|

| 

**Payments**
| 

Payments are managed by your universe operator. For assistance with account payment
management, contact
[Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/).
| 
|

| 

**Billing management **
| 

**Billing account creation**
To create, close or reopen a
Cloud Billing Account, contact
[Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/).

**Managing existing Cloud Billing accounts**
To find your Cloud
Billing Accounts, go to the [Account management page](https://console.cloud.s3nscloud.fr/billing") in the Cloud Billing console.


The Lock Billing Account function is not available. Other
account management features are available.
| 
|


### Other differences



| 

**Invoice management**
| 

To manage and access your Cloud Billing documents such as an invoice,
statement, or receipt, contact
[Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/).
| 
|

| 

**Cloud Billing APIs**
| 

You can programmatically manage billing for your Cloud de Confiance by S3NS projects
using the Cloud Billing API. Not all methods from the Google Cloud
version of this API are available. See the
[API reference guide ](/billing/docs/reference/rest/v1/billingAccounts)
for details.
| 
|

| 

**Cloud Billing Support**
| 

For all Cloud Billing inquiries, support, and issue resolution, please
contact
[Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/).
| 
|





## Related guides



The following information might also affect how you use and design for Cloud Billing
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)