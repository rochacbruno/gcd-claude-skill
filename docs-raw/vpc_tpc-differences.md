# VPC in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/vpc/docs/tpc-differences
Last updated: 2026-08-03

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

Virtual Private Cloud

](https://berlin.devsitetest.how/vpc/docs)






- 








[

Guides

](https://berlin.devsitetest.how/vpc/docs/overview)












# VPC in Google Cloud Dedicated versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Network ](#networks)
- [ Regions and zones ](#regions-zones)
- [ Insights and observability ](#observability-differences)

- [ Related guides ](#related-guides)
- 










Virtual Private Cloud (VPC) provides networking functionality to
[Compute Engine virtual machine (VM) instances](/compute/docs/instances) and
[Google Kubernetes Engine (GKE) clusters](/kubernetes-engine/docs).
VPC includes networking features such as networks, subnets, IP
addresses, routing, and access to Google APIs and services.

This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of VPC.



For more detailed information about VPC, see the
[VPC overview](/vpc/docs/overview) and the rest of the
VPC documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of VPC and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular VPC feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Network



| 
VPC networks**
| 




- Because there's only one region in Google Cloud Dedicated, auto mode
networks contain only one subnet.


- There is no default network created when you create a project. Some
guides assume that you have a default network. If you
need a default network you can [
manually create an equivalent auto mode network called
`default`](/vpc/docs/create-modify-vpc-networks#create-default-network).



| 
|

| 
**Legacy networks**
| 
Not available
| 
|

| 
**IP addresses**
| Global external IPv4 addresses aren't available. | 
|

| 
**Network Service Tiers** | 


Only Premium Tier is available.

| |

| 
**Routing**
| 

Policy-based routes aren't available.
| 
|

| 
**Private Service Connect**
| 




- Automatic DNS configuration isn't available for endpoints that
have published service targets.



- Endpoints with global or regional Google API targets aren't available.

- Backends with global or regional Google API targets aren't available.





- Service connection policies and service connectivity automation
aren't available.

- Connection propagation for Private Service Connect
endpoints isn't available.

- Cross-regional failover for published services, including
Composite Health, is not available.


| 
|

| 
**Private Google Access** | 


The IP addresses for Private Google Access are different:




- `private.apis-berlin-build0.goog` VIP (equivalent to `private.googleapis.com`):



- IPv4: `34.3.152.0/30`

- IPv6: `2607:1c0:9302::/64`



- `restricted.apis-berlin-build0.goog` VIP (equivalent to `restricted.googleapis.com`):



- IPv4: `34.3.152.4/30`

- IPv6: `2607:1c0:9302:1::/64`






Use these IP addresses when you [configure DNS](/vpc/docs/configure-private-google-access#dns-config-other-domains).
Use the appropriate Google Cloud Dedicated domain in your DNS
configuration— for example, `apis-berlin-build0.goog`.
Don't use the `googleapis.com` domain.

| 
|

| 
**Private services access** | 
Not available | 
|

| 
**Bring your own IP address**
| 




- Only v2 prefixes are available in Google Cloud Dedicated.

- BYOIP IPv6 sub-prefixes in subnet creation mode aren't available in Google Cloud Dedicated.


| 
|

| 
**Network profiles**
| 
Not available.
| 
|


### Regions and zones



| 
**Regions and zones**
| 
Google Cloud Dedicated has only a single region, though with multiple zones.
Multi-region features and cross-region failover aren't supported.
| 
|


### Insights and observability



| 
**VPC Flow Logs**
| 




- Only flow logs for subnets through the Compute Engine API are
available. VPC Flow Logs for organizations,
VPC networks, subnets, VLAN attachments for
Cloud Interconnect, and Cloud VPN tunnels through the
Network Management API isn't available.

- The following metadata fields aren't available:



- `internet_routing_details`

- `rdma_traffic_type`

- `src_gke_details` and `dest_gke_details`

- `src_serverless_details` and `dest_serverless_details`





| 
|





## Related guides



The following information might also affect how you use and design for VPC
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products





- 
[
Cloud Next Generation Firewall documentation](/firewall/docs/tpc-differences)


- 
[
Cloud DNS documentation](/dns/docs/tpc-differences)


- 
[Compute Engine documentation](/compute/docs/tpc-differences)


- 
[
Cloud Load Balancing documentation](/load-balancing/docs/tpc-differences)


- 
[Cloud Logging documentation](/logging/docs/tpc-differences)


- 
[Cloud Monitoring documentation](/monitoring/docs/tpc-differences)


- 
[Resource Manager documentation](/resource-manager/docs/tpc-differences)




### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)