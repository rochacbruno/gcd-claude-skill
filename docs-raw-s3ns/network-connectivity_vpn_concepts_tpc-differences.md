# Cloud VPN in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/network-connectivity/docs/vpn/concepts/tpc-differences
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

Network Connectivity

](https://documentation.s3ns.fr/network-connectivity/docs)






- 








[

Cloud VPN

](https://documentation.s3ns.fr/network-connectivity/docs/vpn)






- 








[

Guides

](https://documentation.s3ns.fr/network-connectivity/docs/vpn/concepts/overview)












# Cloud VPN in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Availability and disaster recovery ](#availability-differences)

- [ Related guides ](#related-guides)
- 










Cloud VPN provides secure communication between private networks in
Cloud de Confiance. You can use it to connect a peer network to your
Virtual Private Cloud (VPC) network through a [IPsec](https://wikipedia.org/wiki/IPsec)
[VPN](https://wikipedia.org/wiki/Virtual_private_network) connection, or to
connect two VPC networks.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud VPN.



For more detailed information about Cloud VPN, see the
[Cloud VPN overview](/network-connectivity/docs/vpn/concepts/overview) and the rest of the
Cloud VPN documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud VPN and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud VPN feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Availability and disaster recovery



| 
**Regions and zones** | 
Cloud de Confiance by S3NS has only a single region, though with multiple zones.
Multi-region features and cross-region failover are not supported. | 
|





## Related guides



The following information might also affect how you use and design for Cloud VPN
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products





- 
[VPC in Cloud de Confiance](/vpc/docs/tpc-differences)


- 
[Compute Engine in Cloud de Confiance](/compute/docs/tpc-differences)


- 
[Logging in Cloud de Confiance](/logging/docs/tpc-differences)


- 
[Monitoring in Cloud de Confiance](/monitoring/docs/tpc-differences)




### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)