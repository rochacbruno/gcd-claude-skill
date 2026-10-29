# Bigtable in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/bigtable/docs/tpc-differences
Last updated: 2026-10-28

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

Databases

](https://berlin.devsitetest.how/docs/databases)






- 








[

Bigtable

](https://berlin.devsitetest.how/bigtable/docs)






- 








[

Guides

](https://berlin.devsitetest.how/bigtable/docs/overview)












# Bigtable in Google Cloud Dedicated versus Google Cloud 















Bigtable is a fully managed, NoSQL wide-column database service
for large analytical and operational workloads. It offers high throughput and
low latency for massive datasets.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Bigtable.



For more detailed information about Bigtable, see the
[Bigtable overview](/bigtable/docs/overview) and the rest of the
Bigtable documentation.




## Key differences



There are some differences between the Google Cloud Dedicated version of Bigtable and
the Google Cloud version.
Some notable differences include the following:






- 
Multi-region replication is unavailable.


- 
Cross-region backup and restore is unavailable.


- 
Knowledge Catalog is unavailable.


- Querying data with Google SQL is unavailable.


- Querying data that resides in Bigtable through
BigQuery federation is unavailable.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Bigtable feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Compute and storage



| 
**Instance**
| 
Large nodes that use the 2x nodes scaling factor are unavailable.
| 
|

| 
**Storage type**
| 


The following storage types are available:




- Solid-state drives (SSD)

- Hard disk drives (HDD)




The choice between SSD and HDD is permanent, and every cluster in your
instance must use the same type of storage.



Tiered storage is unavailable.

| 
|

| 
**Backups**
| 


The following types of backups are available:




- Automated backups that let Bigtable create daily backups
for you.

- Hot backups that let you restore to production faster.

- Backup copy that lets you copy a backup to a different instance is available.


| 
|


### Availability and disaster recovery



| 
**Regions and zones**
| 
Bigtable clusters deploy in a single region. Multi-region
features and cross-region failover are unavailable. Deployment across
multiple zones for resiliency is available.
| 
|

| 
**Replication**
| 


Cross-region replication for Bigtable instances is
unavailable. You can configure replication within the single available region
across multiple zones.



For disaster recovery, multi-cluster application profiles are available to
enable automatic failover.

| 
|


### Data management



| 
**Google SQL**
| 
Querying Bigtable data with Google SQL is unavailable,
including the k-nearest neighbor method.
| 
|

| 
**Views**
| 


Authorized views are available.



Logical views and continuous materialized views are
unavailable.

| 
|

| 
**Change streams**
| 
Change streams that capture data changes to a Bigtable
table as they happen are available.
| 
|

| 
**Data Boost**
| 
Data Boost that lets you send large read jobs and queries using
serverless compute is unavailable.
| 
|


### Integrations



| 
**Integrations**
| 
Bigtable integrates with a more limited set of services
than in Google Cloud: Managed Service for Apache Spark, Compute Engine, and
Google Kubernetes Engine (GKE). BigQuery federation
is unavailable.
| 
|

| 
**Third-party integrations**
| 
Terraform and the `BigtableVectorStore` integration for
LangChain are unavailable.
| 
|


### Security and compliance



| 
**Key management**
| 
Customer-Managed Encryption Keys (CMEK) for Bigtable is
available.
| 
|

| 
**VPC Service Controls**
| 
VPC Service Controls is available to create security perimeters around
Bigtable resources.
| 
|

| 
**Custom organization policies**
| 
Custom organization policies that restrict specific
operations on selected Google Cloud resources are
unavailable.
| 
|

| 
**Tags**
| 
Tags that conditionally allow or deny policies based on whether a
Bigtable resource has a specific tag are unavailable.
| 
|


### Observability



| 
**Key Visualizer**
| 
The Key Visualizer tool that helps you analyze your
Bigtable usage is unavailable. Consequently, hot tablets are
unavailable.
| 
|

| 
**Client-side metrics**
| 
Client-side metrics are unavailable.
| 
|


### Interfaces



| 
**Bigtable Studio**
| 
The query builder and editor interfaces that let you build, edit, and run
queries in the console are unavailable.
| 
|

| 
**API**
| 
The `ListHotTablets` method of the Bigtable
Admin API is unavailable.
| 
|





## Related guides



The following information might also affect how you use and design for Bigtable
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)