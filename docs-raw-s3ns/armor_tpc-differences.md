# Cloud Armor in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/armor/docs/tpc-differences
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

Networking

](https://documentation.s3ns.fr/docs/networking)






- 








[

Google Cloud Armor

](https://documentation.s3ns.fr/armor/docs)






- 








[

Guides

](https://documentation.s3ns.fr/armor/docs/cloud-armor-overview)












# Cloud Armor in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Cost management ](#network-differences)
- [ Integrations ](#integrations-differences)
- [ Security and access control ](#security-differences)
- [ Network ](#network-differences)

- [ Related guides ](#related-guides)
- 










Google Cloud Armor helps you protect your Cloud de Confiance by S3NS
deployments from multiple types of threats, including
distributed denial-of-service (DDoS) attacks and application attacks like
cross-site scripting (XSS) and SQL injection (SQLi).
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Armor.



For more detailed information about Cloud Armor, see the
[Cloud Armor overview](/armor/docs/cloud-armor-overview) and the rest of the
Cloud Armor documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud Armor and
the Google Cloud version.
Some notable differences include the following:






- 
Only regional external Application Load Balancers are supported in Cloud de Confiance by S3NS


- 
Google Cloud Armor Enterprise isn't available in Cloud de Confiance by S3NS. This means
that none of the features that require a Cloud Armor Enterprise
subscription are available in Cloud de Confiance by S3NS.


- 
reCAPTCHA is not supported in Cloud de Confiance by S3NS.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Armor feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Cost management



| 
**Cloud Armor Enterprise**
| 
Cloud Armor Enterprise
isn't available, which means that all resources are billed based on
Cloud Armor Standard pricing.
| 
|


### Integrations



| 
**reCAPTCHA**
| 
reCAPTCHA is not available.
| 
|


### Security and access control



| 
**Security policy types**
| 
The following security policy types are not available:



- Global backend security policies

- Global edge security policies

- Network edge security policies


| 
|

| 
**Security policy rules**
| 
Bot management rules are not available.
| 
|

| 
**Features that require Cloud Armor Enterprise**
| 
The following features that require a Cloud Armor Enterprise
subscription are not available:



- Google Cloud Armor Adaptive Protection

- Advanced network DDoS protection, including byte-offset filtering

- Address groups

- Google Threat Intelligence

- DDoS attack visibility

- DDoS response support

- DDoS bill protection


| 
|
| 
**Security Command Center**
| 
Security Command Center is not available.
| 
|


### Network



| 
**Load balancers**
| 
Only regional external Application Load Balancers are available.
| 
|





## Related guides



The following information might also affect how you use and design for Cloud Armor
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products




- 
[Cloud Load Balancing
in Cloud de Confiance by S3NS](/load-balancing/docs/tpc-differences)




### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)