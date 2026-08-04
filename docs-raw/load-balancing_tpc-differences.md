# Cloud Load Balancing in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/load-balancing/docs/tpc-differences
Last updated: 2026-07-29

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

Load Balancing

](https://berlin.devsitetest.how/load-balancing/docs)






- 








[

Guides

](https://berlin.devsitetest.how/load-balancing/docs/load-balancing-overview)












# Cloud Load Balancing in Google Cloud Dedicated versus Google Cloud 






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
Google Cloud Dedicated and Google Cloud versions of Cloud Load Balancing.



For more detailed information about Cloud Load Balancing, see the
[Cloud Load Balancing overview](/load-balancing/docs/load-balancing-overview) and the rest of the
Cloud Load Balancing documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Cloud Load Balancing and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Load Balancing feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Load balancers



| 
Load balancers** | 


Google Cloud Dedicated in Germany has a single region, so only the following
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
load balancers are available in Google Cloud Dedicated in Germany. For example,
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
App Engine aren't available in Google Cloud Dedicated in Germany)

- Global internet NEGs


| 
|


### Availability and disaster recovery



| 
**Regions and zones** | 
Google Cloud Dedicated in Germany has only a single region, though with multiple zones.
Multi-region features and cross-region failover aren't available.
Load balancers with backends deployed across multiple zones for resiliency
are available. | 
|


### Networking features



| 
**Network Service Tiers** | 


Standard Tier isn't available in Google Cloud Dedicated in Germany. All load balancers
and their resources use Premium Tier.

| |

| 
**VPC networks** | 




- Because there's only one region in Google Cloud Dedicated in Germany, auto mode
networks contain only one subnet.

- There is no default network created when you create a project. Some
guides assume that you have a default network. If you
need a default network you can [
manually create an equivalent auto mode network called
`default`](/vpc/docs/create-modify-vpc-networks#create-default-network).




See the [VPC
documentation](/vpc/docs/tpc-differences) to learn more about which VPC features are
available in Google Cloud Dedicated in Germany.

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
available in Google Cloud Dedicated in Germany. | 
|

| 
**TLS/SSL certificates** | 


The following types of SSL certificates aren't available in
Google Cloud Dedicated in Germany:




- Certificate Manager certificates and certificate maps

- Compute Engine Google-managed certificates (global and regional)

- Compute Engine self-managed certificates (global only)


| 
|

| 
**Other security features** | 


The following security features aren't available in
Google Cloud Dedicated in Germany:




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
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products





- 
[Compute Engine documentation](/compute/docs/tpc-differences)


- 
[Logging documentation](/logging/docs/tpc-differences)


- 
[Monitoring documentation](/monitoring/docs/tpc-differences)




### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)