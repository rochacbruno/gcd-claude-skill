# Cloud VPN in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/network-connectivity/docs/vpn/concepts/tpc-differences
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

Network Connectivity

](https://berlin.devsitetest.how/network-connectivity/docs)






- 








[

Cloud VPN

](https://berlin.devsitetest.how/network-connectivity/docs/vpn)






- 








[

Guides

](https://berlin.devsitetest.how/network-connectivity/docs/vpn/concepts/overview)












# Cloud VPN in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Availability and disaster recovery ](#availability-differences)

- [ Related guides ](#related-guides)
- 










Cloud VPN provides secure communication between private networks in
Google Cloud Dedicated. You can use it to connect a peer network to your
Virtual Private Cloud (VPC) network through a [IPsec](https://wikipedia.org/wiki/IPsec)
[VPN](https://wikipedia.org/wiki/Virtual_private_network) connection, or to
connect two VPC networks.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Cloud VPN.



For more detailed information about Cloud VPN, see the
[Cloud VPN overview](/network-connectivity/docs/vpn/concepts/overview) and the rest of the
Cloud VPN documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Cloud VPN and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud VPN feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Availability and disaster recovery



| 
**Regions and zones** | 
Google Cloud Dedicated in Germany has only a single region, though with multiple zones.
Multi-region features and cross-region failover are not supported. | 
|





## Related guides



The following information might also affect how you use and design for Cloud VPN
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products





- 
[VPC in Google Cloud Dedicated](/vpc/docs/tpc-differences)


- 
[Compute Engine in Google Cloud Dedicated](/compute/docs/tpc-differences)


- 
[Logging in Google Cloud Dedicated](/logging/docs/tpc-differences)


- 
[Monitoring in Google Cloud Dedicated](/monitoring/docs/tpc-differences)




### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)