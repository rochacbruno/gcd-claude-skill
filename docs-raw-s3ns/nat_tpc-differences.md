# Cloud NAT in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/nat/docs/tpc-differences
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

Networking

](https://documentation.s3ns.fr/docs/networking)






- 








[

Cloud NAT

](https://documentation.s3ns.fr/nat/docs)






- 








[

Guides

](https://documentation.s3ns.fr/nat/docs/overview)












# Cloud NAT in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Security and access control ](#security-differences)
- [ Network ](#network-differences)
- [ Workflows ](#workflow-differences)
- [ Insights and observability ](#observability-differences)

- [ Related guides ](#related-guides)
- 










Cloud NAT provides network address translation (NAT) for outbound traffic
to the internet, Virtual Private Cloud (VPC) networks, on-premises networks,
and other cloud provider networks.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud NAT.



For more detailed information about Cloud NAT, see the
[Cloud NAT overview](/nat/docs/overview) and the rest of the
Cloud NAT documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud NAT and
the Google Cloud version.
Some notable differences include the following:





- Only NAT for traffic to the internet is available (Public NAT).
NAT for traffic to VPC, on-premises, and other cloud
provider networks is unavailable (Private NAT).

- Only IPv4 to IPv4 address translation is available.

- Cloud NAT allocates external IP addresses from Premium
Tier.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud NAT feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Security and access control



| 
**Organization Policy Service** | 
Custom constraints are unavailable. | 
|


### Network



| 
**Cloud NAT types** | 
Only Public NAT is available.
Private NAT is unavailable. | 
|

| 
**IPv6** | 
Only IPv4 to IPv4 address translation is available.
IPv6 to IPv4 address translation is unavailable. | 
|

| 
**Network Service Tiers** | 
Cloud NAT allocates external IP addresses from Premium Tier.
Standard Tier is unavailable. | 
|


### Workflows



| 
**Google Kubernetes Engine** | 
Some GKE features are unavailable. For more information,
see
[GKE
in Cloud de Confiance by S3NS](/kubernetes-engine/docs/tpc-differences). | 
|

| 
**Serverless environments** | 
Cloud Run, Cloud Run functions, and App Engine are
unavailable. | 
|


### Insights and observability



| 
**Cloud Logging** | 
Some Logging features are unavailable. For more
information, see
[Logging
in Cloud de Confiance by S3NS](/logging/docs/tpc-differences). | 
|

| 
**Cloud Monitoring** | 
Some Monitoring features are unavailable.
For more information, see
[Monitoring
in Cloud de Confiance by S3NS](/monitoring/docs/tpc-differences). | 
|

| 
**Network Intelligence Center** | 
Network Intelligence Center is unavailable. | 
|





## Related guides



The following information might also affect how you use and design for Cloud NAT
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products




- 
[VPC
in Cloud de Confiance by S3NS](/vpc/docs/tpc-differences)


- 
[Compute Engine
in Cloud de Confiance by S3NS](/compute/docs/tpc-differences)


- 
[GKE
in Cloud de Confiance by S3NS](/kubernetes-engine/docs/tpc-differences)


- 
[Cloud Load Balancing
in Cloud de Confiance by S3NS](/load-balancing/docs/tpc-differences)


- 
[Logging
in Cloud de Confiance by S3NS](/logging/docs/tpc-differences)


- 
[Monitoring
in Cloud de Confiance by S3NS](/monitoring/docs/tpc-differences)




### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)