# Cloud DNS in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/dns/docs/tpc-differences
Last updated: 2026-07-17

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

Cloud DNS

](https://berlin.devsitetest.how/dns/docs)






- 








[

Guides

](https://berlin.devsitetest.how/dns/docs/set-up-dns-records-domain-name)












# Cloud DNS in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Network ](#networks)
- [ Regions and zones ](#regions-zones)

- [ Related guides ](#related-guides)
- 










Cloud DNS is a high-performance, resilient, global Domain Name System (DNS) service that publishes your domain names to the global DNS in a cost-effective way.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Cloud DNS.



For more detailed information about Cloud DNS, see the
[Cloud DNS overview](/dns/docs/overview) and the rest of the
Cloud DNS documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Cloud DNS and
the Google Cloud version.
Some notable differences include the following:






- Only private DNS zones are available in Google Cloud Dedicated in Germany. Public DNS zones aren't supported.

- Reverse DNS lookup of public IPv4 and IPv6 addresses isn't supported.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud DNS feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Network



| 
**Private DNS zones**
| 


The following types are available:




- DNS forwarding zones

- DNS peering zones

- Managed reverse lookup zones

- Service Directory zones


| 
|

| 
**Public DNS zones**
| 
Not available
| 
|

| 
**DNS server policies**
| 
All configurations are available
| 
|

| 
**Response policy zones**
| 
All configurations are supported
| 
|



### Regions and zones



| 
**Regions and zones**
| 
Google Cloud Dedicated has only a single region, though with multiple zones.
Multi-region features are not supported.
| 
|





## Related guides



The following information might also affect how you use and design for Cloud DNS
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products




- 
[
Cloud Load Balancing documentation](/load-balancing/docs/tpc-differences)


- 
[
Cloud VPN documentation](/network-connectivity/docs/vpn/concepts/tpc-differences)


- 
[Virtual Private Cloud documentation](/vpc/docs/tpc-differences)


- 
[
Cloud Interconnect documentation](/network-connectivity/docs/interconnect/tpc-differences)


- 
[Cloud NAT documentation](/nat/docs/tpc-differences)




### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)