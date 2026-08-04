# Cloud Interconnect in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/network-connectivity/docs/interconnect/tpc-differences
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

Cloud Interconnect

](https://documentation.s3ns.fr/network-connectivity/docs/interconnect)






- 








[

Guides

](https://documentation.s3ns.fr/network-connectivity/docs/interconnect/concepts/overview)












# Cloud Interconnect in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Network ](#network-differences)

- [ Related guides ](#related-guides)
- 










Cloud Interconnect provides low-latency, high-availability connections that
enable you to reliably transfer data between your Virtual Private Cloud (VPC)
networks and your other networks. Also, Cloud Interconnect connections
provide internal IP address communication, which means internal IP addresses are
directly accessible from both networks.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Interconnect.



For more detailed information about Cloud Interconnect, see the
[Cloud Interconnect overview](/network-connectivity/docs/interconnect/concepts/overview) and the rest of the
Cloud Interconnect documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud Interconnect and
the Google Cloud version.
Some notable differences include the following:






- Only Dedicated Interconnect and Partner Interconnect
are available.


Cross-Cloud Interconnect isn't available.



- Multi-region features and cross-region failover aren't available.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Interconnect feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Network



| 
**Cloud Interconnect types** | 

Only Dedicated Interconnect and Partner Interconnect
are available. Cross-Cloud Interconnect isn't available.
| 
|

| 
**Regions and zones** | 

Cloud de Confiance has only a single region, though with multiple zones.
Multi-region features and cross-region failover are not available.
Deployment across multiple zones for resiliency is available.
| 
|

| 
**Critical production / 99.99% availability** | 
Critical production / 99.99% availability connectivity isn't
available.
| 
|





## Related guides



The following information might also affect how you use and design for Cloud Interconnect
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products




- 
[Virtual Private Cloud
in Cloud de Confiance by S3NS](/vpc/docs/tpc-differences)




### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)