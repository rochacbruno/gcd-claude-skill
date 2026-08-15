# Cloud Load Balancing in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/load-balancing/docs/tpc-differences
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

Load Balancing

](https://documentation.s3ns.fr/load-balancing/docs)






- 








[

Guides

](https://documentation.s3ns.fr/load-balancing/docs/load-balancing-overview)












# Cloud Load Balancing in Cloud de Confiance versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Load balancers ](#load-balancer-components)
- [ Load balancer resources ](#load-balancer-resources)
- [ Availability and disaster recovery ](#availability-differences)
- [ Networking features ](#networking-features)
- [ Security and access control ](#security-differences)
- [ Other cross-product integrations ](#integrations-differences)

- [ Related guides ](#related-guides)
- 










Cloud Load Balancing offers a comprehensive portfolio of
application and network load balancers that let you distribute user traffic
across multiple instances of your applications. By spreading the load, load
balancing reduces the risk that your applications experience performance issues.
Google's Cloud Load Balancing is built on reliable, high-performing
technologies such as Maglev, Andromeda, Google Front Ends, and Envoy—the
same technologies that power Google's own products.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Load Balancing.



For more detailed information about Cloud Load Balancing, see the
[Cloud Load Balancing overview](/load-balancing/docs/load-balancing-overview) and the rest of the
Cloud Load Balancing documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud Load Balancing and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Load Balancing feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Load balancers



| 
Load balancers** | 


Cloud de Confiance by S3NS has a single region, so only the following
regional load balancers are available:




- Regional internal Application Load Balancer

- Regional external Application Load Balancer

- Regional internal proxy Network Load Balancer

- Regional external proxy Network Load Balancer

- Internal passthrough Network Load Balancer

- External passthrough Network Load Balancer




Global and classic load balancers aren't available.

| 
|


### Load balancer resources



| 
**Load balancer components** | 


Only regional resources that are used by regional
load balancers are available in Cloud de Confiance by S3NS. For example,
regional IP addresses, regional backend services, regional forwarding rules,
regional target proxies, and regional URL maps are available. The global
versions of these resources aren't available.



Exceptions to this are the legacy global HTTP health checks which are
required for target pool-based external passthrough Network Load Balancers, and firewall rules which are
always global.

| 
|

| 
**Backends** | 


The following backend types aren't available:




- Backend buckets that reference Cloud Storage buckets

- Serverless NEGs (Cloud Run, Cloud Run functions, and
App Engine aren't available in Cloud de Confiance by S3NS)

- Global internet NEGs


| 
|


### Availability and disaster recovery



| 
**Regions and zones** | 
Cloud de Confiance by S3NS has only a single region, though with multiple zones.
Multi-region features and cross-region failover aren't available.
Load balancers with backends deployed across multiple zones for resiliency
are available. | 
|


### Networking features



| 
**Network Service Tiers** | 


Standard Tier isn't available in Cloud de Confiance by S3NS. All load balancers
and their resources use Premium Tier.

| |

| 
**VPC networks** | 




- Because there's only one region in Cloud de Confiance by S3NS, auto mode
networks contain only one subnet.

- There is no default network created when you create a project. Some
guides assume that you have a default network. If you
need a default network you can [
manually create an equivalent auto mode network called
`default`](/vpc/docs/create-modify-vpc-networks#create-default-network).




See the [VPC
documentation](/vpc/docs/tpc-differences) to learn more about which VPC features are
available in Cloud de Confiance by S3NS.

| |

| 
**Routing and traffic management** | 



The following features are not available:




- Service load balancing policies

- In-flight balancing mode

- Custom metrics balancing mode


| 
|

| 
**Cloud Interconnect** | 
Partner Interconnect and Cross-Cloud Interconnect aren't
available. See the
[Cloud Interconnect
documentation](/network-connectivity/docs/interconnect/concepts/overview) to learn more. | 
|


### Security and access control



| 
**Cloud Armor** | 
See the [Cloud Armor
documentation](/armor/docs/tpc-differences) to learn which Cloud Armor features are
available in Cloud de Confiance by S3NS. | 
|

| 
**TLS/SSL certificates** | 


The following types of SSL certificates aren't available in
Cloud de Confiance by S3NS:




- Certificate Manager certificates and certificate maps

- Compute Engine Google-managed certificates (global and regional)

- Compute Engine self-managed certificates (global only)


| 
|

| 
**Other security features** | 


The following security features aren't available in
Cloud de Confiance by S3NS:




- Authorization policies

- Frontend and backend mTLS

- Global SSL policies

| 
|


### Other cross-product integrations



| 
**Cloud CDN** | 
Not available | 
|

| 
**Media CDN** | 
Not available | 
|

| 
**Certificate Manager** | 
Not available | 
|

| 
**Service Extensions** | 
Not available | 
|

| 
**Network Intelligence Center** | 
Not available | 
|

| 
**Cloud Service Mesh** | 
Not available | 
|





## Related guides



The following information might also affect how you use and design for Cloud Load Balancing
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products





- 
[Compute Engine documentation](/compute/docs/tpc-differences)


- 
[Logging documentation](/logging/docs/tpc-differences)


- 
[Monitoring documentation](/monitoring/docs/tpc-differences)




### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)