# Cloud Storage in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/storage/docs/tpc-differences
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

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Cloud Storage

](https://documentation.s3ns.fr/storage/docs)






- 








[

Guides

](https://documentation.s3ns.fr/storage/docs/discover-object-storage-console)












# Cloud Storage in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Locations, availability, and disaster recovery ](#availability-differences)
- [ Integrations ](#integrations-differences)
- [ Security and access control ](#security-differences)
- [ Network ](#network-differences)
- [ Workflows and tools ](#workflow-differences)
- [ Insights and observability ](#observability-differences)
- [ Other differences ](#other-differences)

- [ Related guides ](#related-guides)
- 










Cloud Storage is a managed service for storing unstructured data.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Storage.



For more detailed information about Cloud Storage, see the
[Cloud Storage overview](/storage/docs/introduction) and the rest of the
Cloud Storage documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud Storage and
the Google Cloud version.
Some notable differences include the following:






- 
Cloud de Confiance does not support features that use multiple locations,
such as dual-regions, bucket relocation, and turbo replication.


- 
Cloud de Confiance does not support Storage Insights.


- 
Cloud de Confiance does not support domain-named buckets.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Storage feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Locations, availability, and disaster recovery



| 
**Locations**
| 
Cloud de Confiance has only a
[single region](/storage/docs/locations) as an available bucket
location. Features that use more than one region are not
supported, such as dual-regions, multi-regions, and bucket
relocation. Rapid Bucket, which places buckets in zones, is also not
supported.
| 
|

| 
**Default location**
| 
When creating a bucket in Cloud de Confiance, you must include a location
parameter as part of the process. Cloud de Confiance does not support creating
buckets in a default location.
| 
|


### Integrations



| 
**Storage Transfer Service**
| 
The Storage Transfer Service is not available in Cloud de Confiance.
| 
|

| 
**Storage Insights**
| 
The Storage Insights feature is not available in Cloud de Confiance.
| 
|

| 
**Default projects**
| 
You can't set a default project in Cloud de Confiance for interoperability
access.
| 
|


### Security and access control



| 
**User account HMAC keys**
| 
User account HMAC keys are not available in Cloud de Confiance.
Use service account HMAC keys instead.
| 
|


### Network



| 
**Rapid Cache**
| 
The Rapid Cache feature is not available in Cloud de Confiance.
| 
|

| 
**Regional and locational endpoints**
| 
Regional and locational endpoints are not available in Cloud de Confiance.
| 
|

| 
**Custom domains**
| 
Using buckets as backends for content serving to custom domains through
`A` and `CNAME` redirects are not available in Cloud de Confiance. Additionlly, creating buckets with domain names is not supported.
| 
|


### Workflows and tools



| 
**Cloud Storage FUSE**
| 




- The Cloud Storage FUSE CSI driver for Google Kubernetes Engine (GKE) is
not available in Cloud de Confiance.

- When using [Cloud Storage FUSE](/storage/docs/cloud-storage-fuse/overview),
the authentication for the Cloud de Confiance
bucket must be done either by using Cloud Storage FUSE in a Compute Engine
virtual machine that's contained in the same project as the bucket or
by specifying a service account key file for a service account that has
permission to read and write data within the bucket. The service account
key file can be specified either in the
[configuration file](/storage/docs/cloud-storage-fuse/config-file)
or by using the `--key-file` flag in individual commands.


| 
|


### Insights and observability



| 
**Cloud Storage usage logs and storage logs**
| 
Usage logs and storage logs, which are legacy logging features specific
to Cloud Storage, are not supported in Cloud de Confiance.
| 
|


### Other differences



| 
**Legacy storage classes**
| 
The legacy storage classes Multi-Regional storage, Regional storage,
and Durable Reduced Availability (DRA) storage are not available in Cloud de Confiance.
| 
|





## Related guides



The following information might also affect how you use and design for Cloud Storage
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)