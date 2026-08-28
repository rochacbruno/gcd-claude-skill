# Cloud Router in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/network-connectivity/docs/router/tpc-differences
Last updated: 2026-08-26

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

Cloud Router

](https://documentation.s3ns.fr/network-connectivity/docs/router)






- 








[

Guides

](https://documentation.s3ns.fr/network-connectivity/docs/router/concepts/overview)












# Cloud Router in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Network ](#regions-zones)

- [ Related guides ](#related-guides)
- 










Cloud Router is a distributed and fully managed offering that provides Border
Gateway Protocol (BGP) speaker and responder capabilities. Cloud Router
works with Cloud Interconnect, Cloud VPN, and Router appliances to
create dynamic routes in Virtual Private Cloud (VPC) networks based on
BGP-received and custom learned routes. Since
Cloud de Confiance has only a single region,
it doesn't support global routing. Consequently, Cloud Router has a
smaller feature set in Cloud de Confiance than in
Google Cloud.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Router.



For more detailed information about Cloud Router, see the
[Cloud Router overview](/network-connectivity/docs/router/concepts/overview) and the rest of the
Cloud Router documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud Router and
the Google Cloud version.
Some notable differences include the following:






- 
[Subnet range
advertisement](/network-connectivity/docs/router/concepts/advertised-routes#am-subnets) works as described for regional dynamic mode only.


- 
[Learned routes](/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode)
work as described for regional dynamic mode only.


- [Classic VPN](/network-connectivity/docs/router/concepts/overview#cloud-products-that-use-cloud-router) with dynamic routes
isn't supported on Cloud de Confiance.

- 
Network Connectivity Center-imported transit dynamic routes aren't supported
on Cloud de Confiance.

- You can't create VPC spokes to connect VPC networks together for full
mesh connectivity on Cloud de Confiance.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Router feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Network



| 
**Regions and zones**
| 



Cloud de Confiance has only a single
region and Cloud Router is only
supported in a single region on the Cloud de Confiance.
Hence, multi-region features are not supported.




This difference affects the following features in Cloud Router:



- 
[Subnet range
advertisement](/network-connectivity/docs/router/concepts/advertised-routes#am-subnets) works as described for regional dynamic mode only.


- 
[Learned routes](/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode)
work as described for regional dynamic mode only.

| 
|

| 
**Classic VPN support**
| 



[Classic VPN](/network-connectivity/docs/router/concepts/overview#cloud-products-that-use-cloud-router) for dynamic routing
isn't supported on Cloud de Confiance.


| 
|





## Related guides



The following information might also affect how you use and design for Cloud Router
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)