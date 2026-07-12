# BigQuery in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/bigquery/docs/tpc-differences
Last updated: 2026-07-10

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

Data analytics

](https://berlin.devsitetest.how/docs/data)






- 








[

BigQuery

](https://berlin.devsitetest.how/bigquery/docs)






- 








[

Guides

](https://berlin.devsitetest.how/bigquery/docs/introduction)












# Big Query in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ API and service availability ](#security-differences)
- [ Regions and zones ](#security-differences)
- [ Cost management ](#cost-management-differences)
- [ Security and access control ](#security-differences)
- [ Integrations ](#integrations-differences)
- [ Workflows and tools ](#workflow-differences)
- [ BigQuery Data Transfer Service ](#data-transfer-service)

- [ Related guides ](#related-guides)
- 










BigQuery is a fully managed, serverless data warehouse that enables scalable analysis over petabytes of data. BigQuery provides features such as built-in machine learning, geospatial analysis, and business intelligence.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of BigQuery.



For more detailed information about BigQuery, see the
[BigQuery overview](/bigquery/docs/overview) and the rest of the
BigQuery documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of BigQuery and
the Google Cloud version.
Some notable differences include the following:





- Many external connections to data sources are unavailable. These include
services such as BigQuery Migration Service,
BigQuery sharing (formerly known as Analytics Hub),
BigQuery Connection API and BigQuery Omni
(AWS and Azure connections), and BigLake APIs.

- Certain advanced query features are unavailable. These include saved
queries and notebooks, Gemini in BigQuery features,
and BigQuery ML external models.



A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular BigQuery feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### API and service availability

The following BigQuery APIs and services are unavailable in Google Cloud Dedicated in Germany:


- Dataform API

- Migration API

- Analytics Hub API

- Data Transfer API

### Regions and zones



| 
**Regions and zones**
| 
Trusted Cloud has only a single region, though with multiple zones.
Multi-region features and cross-region failover are not supported.
| 
|

| 
**Cross region replication & failover**
| 
Cross region replication and failover are not available in Trusted Cloud.
| 
|


### Cost management



| 
**Cost saving features**
| 
Committed use discounts (CUDs) are unavailable in
Google Cloud Dedicated. | 
|


### Security and access control



| 
**Data masking** | 
Data masking is unavailable. | 
|

| 
**Column level access control** | 
Column level access control is unavailable. | 
|

| 
**Customer-managed encryption keys** | 
Customer-managed encryption key (CMEK) provisioning requires manual
provisioning. | 
|


### Integrations



| 
**Cloud Asset Inventory** | 
Cloud Asset Inventory is unavailable. | 
|


### Workflows and tools



| 
**Client libraries** | 
Most client libraries are available for supported APIs.
| 
|

| 
**Terraform support** | 
Terraform support is unavailable. | 
|

| 
**BigQuery ML** | 
BigQuery ML supports only [internal models.](/bigquery/docs/bqml-introduction#internally_trained_models) | 
|

| 
**Gemini in BigQuery** | 
Gemini in BigQuery is unavailable. | 
|

| 
**Public datasets** | 
BigQuery public datasets are not available in Google Cloud Dedicated. You must import your own data to try BigQuery, including following our tutorials. | 
|

| 
**Scheduled queries** | 
BigQuery scheduled queries are unavailable. | 
|


### BigQuery Data Transfer Service



| 
**Transfer run notifications** | 
[Email notifications](/bigquery/docs/transfer-run-notifications#email_notifications) are unavailable.
| 
|





## Related guides



The following information might also affect how you use and design for BigQuery
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)