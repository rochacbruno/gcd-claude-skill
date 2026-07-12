# Cloud KMS in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/kms/docs/tpc-differences
Last updated: 2026-07-10

- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Technology areas

](https://berlin.devsitetest.how/docs)






- 








[

Cloud Key Management Service

](https://berlin.devsitetest.how/kms)






- 








[

Guides

](https://berlin.devsitetest.how/kms/docs/key-management-service)












# Cloud KMS in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Hardware and OS ](#hardware-and-os-differences)
- [ Availability and disaster recovery ](#availability-differences)
- [ Integrations ](#integrations-differences)
- [ Network ](#network-differences)
- [ Workflows and tools ](#workflow-differences)
- [ Insights and observability ](#observability-differences)
- [ Other differences ](#other-differences)

- [ Related guides ](#related-guides)
- 










Cloud Key Management Service (Cloud KMS) lets you create and manage cryptographic keys for use
in compatible Google Cloud Dedicated services and in your own applications.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Cloud KMS.



For more detailed information about Cloud KMS, see the
[Cloud KMS overview](/kms/docs/key-management-service) and the rest of the
Cloud KMS documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Cloud KMS and
the Google Cloud version.
Some notable differences include the following:






- 
Key tracking and key usage details are not supported in
Google Cloud Dedicated in Germany.


- 
Multi-tenant Cloud HSM keys are not supported in
Google Cloud Dedicated in Germany.


- 
Single-tenant Cloud HSM instances and keys are not supported in
Google Cloud Dedicated in Germany.


- 
The EKM over internet protection level is not supported in
Google Cloud Dedicated in Germany.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud KMS feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Hardware and OS



| 
**Multi-tenant hardware keys**
| 
The `HSM` protection level (Multi-tenant Cloud HSM keys) is
not available for Google Cloud Dedicated.
| 
|

| 
**Single-tenant hardware keys**
| 
Single-tenant Cloud HSM instances and the
`HSM_ SINGLE_ TENANT` protection level (Single-tenant Cloud HSM
keys) are not available for Google Cloud Dedicated.
| 
|


### Availability and disaster recovery



| 
**Regional locations**
| 
Only the `u-germany-northeast1` regional
location is supported for Google Cloud Dedicated.
| 
|

| **Multi-regions**
| 
Multi-regions other than `global` are not supported for
Google Cloud Dedicated.
| 
|

| 
**`global` location** | 


The `global` location exists for
Google Cloud Dedicated but contains only a
single region, `u-germany-northeast1`.
Resources stored in the `global` region satisfy the same
residency requirements as those stored in
`u-germany-northeast1`. Choose the
`global` location for your Cloud KMS resources if
you want to use CMEK to protect resources in the `global`
location. Otherwise, you should create your Cloud KMS resources
in the `u-germany-northeast1` region.

| |


### Integrations



| 
**CMEK integrations**
| 
A subset of CMEK-integrated services are available for
Google Cloud Dedicated. To learn whether a
service is available, see the [list of supported services](https://berlin.devsitetest.how/products).
| 
|


### Network



| 
**EKM over internet**
| 
The EKM over internet (`EXTERNAL`) protection level is not
available for Google Cloud Dedicated.
| 
|


### Workflows and tools



| 
**Cloud KMS Autokey**
| 
Cloud KMS Autokey is not available for
Google Cloud Dedicated because it requires
Cloud HSM keys.
| 
|


### Insights and observability



| 
**Key tracking and key usage tracking**
| 
Key tracking and key usage tracking, including the key tracking dashboard
and Cloud KMS Inventory API, are not available for
Google Cloud Dedicated.
| 
|


### Other differences



| 
**`generateRandomBytes`**
| 
The `generateRandomBytes` method isn't available for
Google Cloud Dedicated.
| 
|





## Related guides



The following information might also affect how you use and design for Cloud KMS
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)