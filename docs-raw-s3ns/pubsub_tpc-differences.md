# Pub/Sub in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/pubsub/docs/tpc-differences
Last updated: 2026-08-11

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

Data analytics

](https://documentation.s3ns.fr/docs/data)






- 








[

Pub/Sub

](https://documentation.s3ns.fr/pubsub/docs)






- 








[

Guides

](https://documentation.s3ns.fr/pubsub/docs/overview)












# Pub/ Sub in Cloud de Confiance versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Features ](#features-differences)
- [ Availability and disaster recovery ](#availability-differences)
- [ Architecture ](#integrations-differences)
- [ Integrations ](#integrations-differences)

- [ Related guides ](#related-guides)
- 










Pub/Sub is an asynchronous and scalable messaging service that
decouples services that produce messages from services that process those
messages. Pub/Sub lets services communicate asynchronously,
often to stream analytics and empower data integration pipelines to ingest and
distribute data.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Pub/Sub.



For more detailed information about Pub/Sub, see the
[Pub/Sub overview](/pubsub/docs/overview) and the rest of the
Pub/Sub documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Pub/Sub and
the Google Cloud version.
Some notable differences include the following:






- 
Some types of subscriptions are unavailable in Cloud de Confiance.


- 
Some types of import topics are unavailable in Cloud de Confiance.


- 
Pub/Sub Lite is unavailable in Cloud de Confiance.


- 
Some features, like ordering keys or dead-letter queues are unavailable
in Cloud de Confiance.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Pub/Sub feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Features



| 
Authentication for push subscriptions**
| 
Authentication for push subscriptions is unavailable.
| 
|

| 
**Dead-letter queues**
| 
Dead-letter queues are unavailable.
| 
|

| 
**Exactly-once delivery**
| 
Exactly-once delivery is unavailable.
| 
|

| 
**Filtering**
| 
Filtering is unavailable.
| 
|

| 
**Import topics**
| 
Import topics are not available for use. Including Amazon Kinesis
Data Streams import topics, Cloud Storage import topics, Azure Event
Hubs import topics, MSK import topics, and Confluent Cloud import topics.
| 
|

| 
**Ordering keys**
| 
Ordering keys are unavailable.
| 
|

| 
**Payload unwrapping for push subscriptions**
| 
Payload unwrapping for push subscriptions is unavailable.
| 
|

| 
**Schemas**
| 
Schemas are unavailable.
| 
|

| 
**Snapshots and seek**
| 
Snapshots and seek are unavailable.
| 
|

| 
**Subscriptions**
| 
BigQuery subscriptions and Cloud Storage subscriptions
are unavailable. Ingesting data from sources like
Amazon Web Services (AWS) or Cloud Storage is also unavailable.
| 
|


### Availability and disaster recovery



| 
**Regions and zones**
| 
Cloud de Confiance is only supported in a
single region and can be used in both regional and zonal configuration
deployments. Zone separation in a single region is supported. Multi-regional
functionality and features that rely on multi-regions are not supported.
| 
|

| 
**Disaster recovery**
| 
Cross-region failover is unavailable for customers operating in universes
with a single region. Zone separation within a region is supported.
| 
|


### Architecture



| 
**Global availability of data**
| 
Data in Cloud de Confiance is not globally
available. It is only available in a single region, specific to your universe.
| 
|

| 
**Resource location and IAM controls**
| 
Resource location restrictions are not supported.
| 
|


### Integrations



| 
**Core integrations**
| 
The following core integrations aren't supported in
Cloud de Confiance: Dataflow,
BigQuery subscriptions, Cloud Functions, App Engine,
and Cloud Run.
| 
|

| **Third-party integrations**
| 
Third-party integrations might not be supported. To determine if a
third-party integration is supported in Cloud de Confiance,
check with the respective vendor you are working with. | 
|





## Related guides



The following information might also affect how you use and design for Pub/Sub
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)