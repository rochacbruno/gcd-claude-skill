# Cloud KMS in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/kms/docs/tpc-differences
Last updated: 2026-09-01

- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Cloud Key Management Service

](https://documentation.s3ns.fr/kms)






- 








[

Guides

](https://documentation.s3ns.fr/kms/docs/key-management-service)












# Cloud KMS in Cloud de Confiance versus Google Cloud 






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
in compatible Cloud de Confiance services and in your own applications.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud KMS.



For more detailed information about Cloud KMS, see the
[Cloud KMS overview](/kms/docs/key-management-service) and the rest of the
Cloud KMS documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud KMS and
the Google Cloud version.
Some notable differences include the following:






- 
Key tracking and key usage details are not supported in
Cloud de Confiance by S3NS.


- 
Multi-tenant Cloud HSM keys are not supported in
Cloud de Confiance by S3NS.


- 
Single-tenant Cloud HSM instances and keys are not supported in
Cloud de Confiance by S3NS.


- 
The EKM over internet protection level is not supported in
Cloud de Confiance by S3NS.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud KMS feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Hardware and OS



| 
**Multi-tenant hardware keys**
| 
The `HSM` protection level (Multi-tenant Cloud HSM keys) is
not available for Cloud de Confiance.
| 
|

| 
**Single-tenant hardware keys**
| 
Single-tenant Cloud HSM instances and the
`HSM_ SINGLE_ TENANT` protection level (Single-tenant Cloud HSM
keys) are not available for Cloud de Confiance.
| 
|


### Availability and disaster recovery



| 
**Regional locations**
| 
Only the `u-france-east1` regional
location is supported for Cloud de Confiance.
| 
|

| **Multi-regions**
| 
Multi-regions other than `global` are not supported for
Cloud de Confiance.
| 
|

| 
**`global` location** | 


The `global` location exists for
Cloud de Confiance but contains only a
single region, `u-france-east1`.
Resources stored in the `global` region satisfy the same
residency requirements as those stored in
`u-france-east1`. Choose the
`global` location for your Cloud KMS resources if
you want to use CMEK to protect resources in the `global`
location. Otherwise, you should create your Cloud KMS resources
in the `u-france-east1` region.

| |


### Integrations



| 
**CMEK integrations**
| 
A subset of CMEK-integrated services are available for
Cloud de Confiance. To learn whether a
service is available, see the [list of supported services](https://documentation.s3ns.fr/products).
| 
|


### Network



| 
**EKM over internet**
| 
The EKM over internet (`EXTERNAL`) protection level is not
available for Cloud de Confiance.
| 
|


### Workflows and tools



| 
**Cloud KMS Autokey**
| 
Cloud KMS Autokey is not available for
Cloud de Confiance because it requires
Cloud HSM keys.
| 
|


### Insights and observability



| 
**Key tracking and key usage tracking**
| 
Key tracking and key usage tracking, including the key tracking dashboard
and Cloud KMS Inventory API, are not available for
Cloud de Confiance.
| 
|


### Other differences



| 
**`generateRandomBytes`**
| 
The `generateRandomBytes` method isn't available for
Cloud de Confiance.
| 
|





## Related guides



The following information might also affect how you use and design for Cloud KMS
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)