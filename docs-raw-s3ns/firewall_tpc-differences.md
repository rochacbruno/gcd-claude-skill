# Cloud NGFW in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/firewall/docs/tpc-differences
Last updated: 2026-08-17

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

Cloud NGFW

](https://documentation.s3ns.fr/firewall/docs)






- 








[

Guides

](https://documentation.s3ns.fr/firewall/docs/about-firewalls)












# Cloud NGFW in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Firewall tiers ](#firewall-tiers)
- [ Availability and disaster recovery ](#availability-differences)
- [ Firewall features ](#firewall-features)
- [ Security and access control ](#security-differences)
- [ Other cross-product integrations ](#integrations-differences)

- [ Related guides ](#related-guides)
- 










Cloud Next Generation Firewall is a fully distributed firewall service with
advanced protection capabilities, micro-segmentation, and pervasive coverage
to protect your workloads from internal and external attacks.
Cloud NGFW provides a stateful, fully distributed host-based
enforcement on each workload to enable zero-trust security architecture.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud NGFW.



For more detailed information about Cloud NGFW, see the
[Cloud NGFW overview](/firewall/docs/about-firewalls) and the rest of the
Cloud NGFW documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud NGFW and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud NGFW feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Firewall tiers



| 
**Firewall tiers** | 


The following tiers of Cloud NGFW are available in Cloud de Confiance by S3NS:




- Cloud Next Generation Firewall Essentials

- Cloud Next Generation Firewall Standard




Cloud NGFW Enterprise is unavailable.

| 
|


### Availability and disaster recovery



| 
**Regions and zones** | 
Cloud de Confiance by S3NS has only a single region, though with multiple zones.
Multi-region features and cross-region failover are unavailable. | 
|


### Firewall features



| 
**Security profiles** | 
Unavailable | 
|

| 
**Security profile groups** | 
Unavailable | 
|

| 
**Firewall endpoints** | 
Unavailable | 
|

| 
| 

### Security and access control



| 
**Security features** | 


The following security features are unavailable in
Cloud de Confiance by S3NS:




- Threat intelligence

- Threat signature

- Intrusion prevention

- URL filtering

- Transport Layer Security (TLS) inspection

| 
|


### Other cross-product integrations



| 
**Google Cloud Armor ** | 
Available | 
|

| 
**App Engine** | 
Available | 
|

| 
**Filestore** | 
Available | 
|





## Related guides



The following information might also affect how you use and design for Cloud NGFW
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products





- 
[VPC documentation](/vpc/docs/tpc-differences)


- 
[Logging documentation](/logging/docs/tpc-differences)


- 
[Monitoring documentation](/monitoring/docs/tpc-differences)




### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)