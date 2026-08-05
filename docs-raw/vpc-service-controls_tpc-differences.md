# VPC Service Controls in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/vpc-service-controls/docs/tpc-differences
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

Networking

](https://berlin.devsitetest.how/docs/networking)






- 








[

VPC Service Controls

](https://berlin.devsitetest.how/vpc-service-controls/docs)






- 








[

Guides

](https://berlin.devsitetest.how/vpc-service-controls/docs/overview)












# VPC Service Controls in Google Cloud Dedicated versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Availability and disaster recovery ](#availability-differences)
- [ Security and access control ](#security-differences)
- [ Integrations ](#integrations-differences)
- [ Other differences ](#availability-differences)

- [ Related guides ](#related-guides)
- 










VPC Service Controls secures Google Cloud Dedicated services and resources by
defining a security perimeter around your resources. VPC Service Controls
lets you define security policies that prevent access to Google-managed services
outside of a trusted perimeter, block access to data from untrusted locations,
and mitigate data exfiltration risks.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of VPC Service Controls.



For more detailed information about VPC Service Controls, see the
[VPC Service Controls overview](/vpc-service-controls/docs/overview) and the rest of the
VPC Service Controls documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of VPC Service Controls and
the Google Cloud version.
Some notable differences include the following:






- Standalone access levels are unavailable in Google Cloud Dedicated in Germany.

- Perimeter bridges are unavailable in Google Cloud Dedicated in Germany.

- Support for configuring VPC networks and identity groups
in the ingress and egress rules are unavailable.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular VPC Service Controls feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Availability and disaster recovery



| 
**Regions and zones**
| 
Google Cloud Dedicated in Germany has only a single region, though with multiple zones.
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
VPC Service Controls in Google Cloud Dedicated in Germany:



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
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products



- [Access Context Manager in
Google Cloud Dedicated in Germany](/access-context-manager/docs/tpc-differences)


### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)