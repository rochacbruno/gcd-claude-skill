# Cloud NAT in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/nat/docs/tpc-differences
Last updated: 2026-08-11

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

Cloud NAT

](https://berlin.devsitetest.how/nat/docs)






- 








[

Guides

](https://berlin.devsitetest.how/nat/docs/overview)












# Cloud NAT in Google Cloud Dedicated versus Google Cloud 






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
Google Cloud Dedicated and Google Cloud versions of Cloud NAT.



For more detailed information about Cloud NAT, see the
[Cloud NAT overview](/nat/docs/overview) and the rest of the
Cloud NAT documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Cloud NAT and
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
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud NAT feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




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
in Google Cloud Dedicated in Germany](/kubernetes-engine/docs/tpc-differences). | 
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
in Google Cloud Dedicated in Germany](/logging/docs/tpc-differences). | 
|

| 
**Cloud Monitoring** | 
Some Monitoring features are unavailable.
For more information, see
[Monitoring
in Google Cloud Dedicated in Germany](/monitoring/docs/tpc-differences). | 
|

| 
**Network Intelligence Center** | 
Network Intelligence Center is unavailable. | 
|





## Related guides



The following information might also affect how you use and design for Cloud NAT
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products




- 
[VPC
in Google Cloud Dedicated in Germany](/vpc/docs/tpc-differences)


- 
[Compute Engine
in Google Cloud Dedicated in Germany](/compute/docs/tpc-differences)


- 
[GKE
in Google Cloud Dedicated in Germany](/kubernetes-engine/docs/tpc-differences)


- 
[Cloud Load Balancing
in Google Cloud Dedicated in Germany](/load-balancing/docs/tpc-differences)


- 
[Logging
in Google Cloud Dedicated in Germany](/logging/docs/tpc-differences)


- 
[Monitoring
in Google Cloud Dedicated in Germany](/monitoring/docs/tpc-differences)




### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)