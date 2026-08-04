# Cloud Billing in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/billing/docs/tpc-differences
Last updated: 2026-07-29

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












# Cloud Billing in Google Cloud Dedicated versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Billing and cost management differences ](#billing-differences)
- [ Other differences ](#other-differences)

- [ Related guides ](#related-guides)
- 










Cloud Billing is a collection of tools that help you track and understand
your Google Cloud Dedicated in Germany spending, pay your bill, and optimize your costs.

This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Cloud Billing.



For more detailed information about Cloud Billing, see the
[Cloud Billing overview](/billing/docs/concepts) and the rest of the
Cloud Billing documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Cloud Billing and
the Google Cloud version.
Some notable differences include the following:




- Google Cloud Dedicated in Germany does not support self-serve (or online) accounts. If you
are interested in purchasing Google Cloud Dedicated in Germany services, you must work with
your operator for Cloud Billing account creation.

- You cannot create, modify, close, or reopen billing accounts from within
Google Cloud Dedicated in Germany.

- Customer invoicing is managed by your universe operator. If you require
invoicing or billing support, contact
[Google Cloud Dedicated in Germany billing support]().



A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Billing feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Billing and cost management differences



| 

Cost management**
| 



Cost management self-service features, including
**Reports**, **Cost Table**, and
**Cost Breakdown**, are available in Google Cloud Dedicated in Germany.




Budgets, alerts, and anomalies are unavailable.




If you need to export billing cost data, contact
[
Google Cloud Dedicated in Germany billing support]().


| 
|

| 

**Cost optimization**
| 



Google Cloud Dedicated in Germany offers committed use discounts (CUDs). To purchase
spend-based CUDs, contact
[
Google Cloud Dedicated in Germany billing support]().




The following products and services are eligible for spend-based
CUDs in Google Cloud Dedicated in Germany:





- Cloud SQL

- 
Compute Engine
(including Cloud Run and GKE)


- BigQuery reservations

- Bigtable 1 

- Spanner 1 




Other cost optimization features, such as FinOps Hub, pricing,
cost estimation, and credits, are unavailable in Google Cloud Dedicated in Germany.




1 These services are not immediately available for
spend-based CUDs but will be supported in the near future.


| 
|

| 

**Payments**
| 

Payments are managed by your universe operator. For assistance with account payment
management, contact
[Google Cloud Dedicated in Germany billing support]().
| 
|

| 

**Billing management **
| 

**Billing account creation**
To create, close or reopen a
Cloud Billing Account, contact
[Google Cloud Dedicated in Germany billing support]().

**Managing existing Cloud Billing accounts**
To find your Cloud
Billing Accounts, go to the [Account management page](https://console.cloud.berlin-build0.goog/billing") in the Cloud Billing console.


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
[Google Cloud Dedicated in Germany billing support]().
| 
|

| 

**Cloud Billing APIs**
| 

You can programmatically manage billing for your Google Cloud Dedicated in Germany projects
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
[Google Cloud Dedicated in Germany billing support]().
| 
|





## Related guides



The following information might also affect how you use and design for Cloud Billing
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)