# VPC Service Controls in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/vpc-service-controls/docs/tpc-differences
Last updated: 2026-07-29

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

VPC Service Controls

](https://documentation.s3ns.fr/vpc-service-controls/docs)






- 








[

Guides

](https://documentation.s3ns.fr/vpc-service-controls/docs/overview)












# VPC Service Controls in Cloud de Confiance versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Availability and disaster recovery ](#availability-differences)
- [ Security and access control ](#security-differences)
- [ Integrations ](#integrations-differences)
- [ Other differences ](#availability-differences)

- [ Related guides ](#related-guides)
- 










VPC Service Controls secures Cloud de Confiance services and resources by
defining a security perimeter around your resources. VPC Service Controls
lets you define security policies that prevent access to Google-managed services
outside of a trusted perimeter, block access to data from untrusted locations,
and mitigate data exfiltration risks.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of VPC Service Controls.



For more detailed information about VPC Service Controls, see the
[VPC Service Controls overview](/vpc-service-controls/docs/overview) and the rest of the
VPC Service Controls documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of VPC Service Controls and
the Google Cloud version.
Some notable differences include the following:






- Standalone access levels are unavailable in Cloud de Confiance by S3NS.

- Perimeter bridges are unavailable in Cloud de Confiance by S3NS.

- Support for configuring VPC networks and identity groups
in the ingress and egress rules are unavailable.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular VPC Service Controls feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Availability and disaster recovery



| 
**Regions and zones**
| 
Cloud de Confiance by S3NS has only a single region, though with multiple zones.
Multi-region features and cross-region failover are not supported. Deployment
across multiple zones for resiliency is supported.
| 
|


### Security and access control



| 
**Access levels**
| 




- Standalone access levels are unavailable. Use access levels in ingress and egress
rules instead.

- Custom access levels are unavailable.


| 
|

| 
**Perimeter bridges**
| 




- Perimeter bridges are unavailable. Use ingress and egress rules instead.


| 
|

| 
Ingress and egress rules** | 

The following features are unavailable when configuring ingress and egress rules:



- Using service methods.

- Configuring identities such as service accounts, identity groups,
and third-party identities.

- Configuring VPC networks.

- Configuring access levels with internal IP addresses.


| 
|


### Integrations



| 
**Supported services** | 

Only the following services are available for configuring with
VPC Service Controls in Cloud de Confiance by S3NS:



- Access Approval

- Artifact Registry

- BigQuery

- BigQuery Reservation API

- Cloud DNS

- Cloud KMS

- Cloud Logging

- Cloud Monitoring

- Cloud Storage

- Cloud SQL

- Compute Engine

- Essential Contacts

- GKE

- Identity and Access Management (IAM)

- Organization Policy Service

- Pub/Sub

- Resource Manager

- Security Token Service

- Service Account Credentials

- Service Directory


| 
|


### Other differences



| 
**Troubleshooting**
| 




- VPC Service Controls violation analyzer is unavailable.


| 
|





## Related guides



The following information might also affect how you use and design for VPC Service Controls
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products



- [Access Context Manager in
Cloud de Confiance by S3NS](/access-context-manager/docs/tpc-differences)


### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)