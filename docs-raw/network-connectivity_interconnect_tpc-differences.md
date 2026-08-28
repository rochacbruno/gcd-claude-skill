# Cloud Interconnect in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/network-connectivity/docs/interconnect/tpc-differences
Last updated: 2026-08-26

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

Cloud Interconnect

](https://berlin.devsitetest.how/network-connectivity/docs/interconnect)






- 








[

Guides

](https://berlin.devsitetest.how/network-connectivity/docs/interconnect/concepts/overview)












# Cloud Interconnect in Google Cloud Dedicated versus Google Cloud 






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
Google Cloud Dedicated and Google Cloud versions of Cloud Interconnect.



For more detailed information about Cloud Interconnect, see the
[Cloud Interconnect overview](/network-connectivity/docs/interconnect/concepts/overview) and the rest of the
Cloud Interconnect documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Cloud Interconnect and
the Google Cloud version.
Some notable differences include the following:






- Only Dedicated Interconnect and Partner Interconnect
are available.


Cross-Cloud Interconnect isn't available.



- Multi-region features and cross-region failover aren't available.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Interconnect feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Network



| 
**Cloud Interconnect types** | 

Only Dedicated Interconnect and Partner Interconnect
are available. Cross-Cloud Interconnect isn't available.
| 
|

| 
**Regions and zones** | 

Google Cloud Dedicated has only a single region, though with multiple zones.
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
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products




- 
[Virtual Private Cloud
in Google Cloud Dedicated in Germany](/vpc/docs/tpc-differences)




### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)