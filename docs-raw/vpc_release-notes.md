# VPC release notes

Source: https://berlin.devsitetest.how/vpc/docs/release-notes
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/vpc/docs/tpc-differences) for more details.














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

Resources

](https://berlin.devsitetest.how/vpc/docs/resources)












# VPC release notes 


















This page contains release notes for features and updates to
Virtual Private Cloud (VPC) networking in Google Cloud Dedicated in Germany.







You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/vpc-release-notes.xml) directly.









## October 19, 2026


Feature 


**General Availability**: VPC Flow Logs adds the following metadata annotations
and packet drop reasons for Cloud NAT:

- Metadata annotations: `connection.nat_ip`, `connection.nat_port`, and
`nat_gateway_details`

- Drop reasons: `NAT_ENDPOINT_INDEPENDENT_CONFLICT`, `NAT_OUT_OF_CONNECTIONS`,
and `NAT_OUT_OF_PORTS`

For more information, see
[Record format](/vpc/docs/about-flow-logs-records#record_format) and
[Packet drop reasons](/vpc/docs/about-flow-logs-records#drop-reason).



## October 07, 2026


Feature 


Service producers can let service consumers establish more connections to a
Private Service Connect endpoint or backend by
[configuring the target published service (service attachment) to use an additional NAT
IP address](/vpc/docs/manage-private-service-connect-services#update-nat-ips-per-endpoint).
For more information, see
[Maximum connections](/vpc/docs/about-vpc-hosted-services#max-connections).



## September 16, 2026


Feature 


**General Availability**: You can add Dynamic NICs to the same VPC network used
by other network interfaces of a Compute Engine instance. For more information,
see [Multiple network interfaces](/vpc/docs/multiple-interfaces-concepts#specifications).



Feature 


**General Availability**: VPC Flow Logs supports logging for
App Engine resources that are configured with
[Direct VPC egress](/appengine/docs/standard/vpc-direct-vpc).
For more information, see
[Serverless flows](/vpc/docs/about-traffic-flows#serverless-flows) and
[ServerlessDetails field format](/vpc/docs/about-flow-logs-records#serverless-details).



Feature 


**General Availability**: VPC Flow Logs adds the following metadata annotations
for Private Service Connect:

- `src_psc_interface` and `dest_psc_interface`

- `psc.consumer_connection`

- `psc.psc_endpoint.name`

- `psc.psc_attachment.name`

For more information, see
[Record format](/vpc/docs/about-flow-logs-records#record_format).



## August 31, 2026


Feature 


**General Availability**: You can create Compute Engine instances that have
multiple virtual network interfaces (vNICs) in the same VPC network.
For more information, see
[Multiple network interfaces in the same VPC network](/vpc/docs/multiple-interfaces-concepts#same-vpc).



## August 27, 2026


Feature 


**General Availability**: VPC Flow Logs generates log records for dropped
traffic. For more information, see
[Records for dropped traffic](/vpc/docs/about-flow-logs-records#packet-drops).



Feature 


**General Availability**: You can reserve static external IPv6 addresses from
bring your own IP addresses (BYOIP) sub-prefixes that are in
`EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.

You can assign these addresses to forwarding rules for external passthrough
Network Load Balancers and external protocol forwarding. You can also promote
ephemeral IPv6 BYOIP addresses that are used by external forwarding rules
to reserved static IP addresses.

For more information, see
[Create external forwarding rules](/vpc/docs/create-ipv6-sub-prefixes#create-subprefix-use).



## August 07, 2026


Feature 


**General Availability**: You can use Private Service Connect endpoints
to access global Google APIs. For more information, see
[About accessing Google APIs through endpoints](/vpc/docs/about-accessing-google-apis-endpoints).



## July 30, 2026


Feature 


**General Availability**: You can use the **Resolve subnet mask** setting on a
subnet to configure all attached Compute Engine instances with the same netmask
as the subnet (instead of `/32`). Configuring larger instance netmasks lets
compute instances discover the MAC addresses of other machines within the same
subnet and directly communicate with them by using destination MAC addresses.

For more information, see
[Compute instance netmasks](/vpc/docs/compute-instance-netmasks).



## July 20, 2026


Feature 


**Preview**: You can reserve static external IPv6 addresses from
bring your own IP addresses (BYOIP) sub-prefixes that are in
`EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.

You can assign these addresses to forwarding rules for external passthrough
Network Load Balancers and external protocol forwarding. You can also promote
ephemeral IPv6 BYOIP addresses that are used by external forwarding rules
to reserved static IP addresses.

For more information, see
[Create external forwarding rules](/vpc/docs/create-ipv6-sub-prefixes#create-subprefix-use).



## June 24, 2026


Feature 


**General Availability**: You can cancel pending deletion requests for VPC
Network Peering connections that are in consensus mode.
For more information, see
[Cancel a deletion request](/vpc/docs/using-vpc-peering#cancel-delete).



## April 10, 2026


Feature 


Private Service Connect consumers can configure supported load
balancers or regional Cloud Service Mesh to access published services through
Private Service Connect endpoints. This feature is available in **Preview**.

For more information, see
[Published service backends](https://berlin.devsitetest.how/vpc/docs/about-accessing-vpc-hosted-services-endpoints#published-service-backends).



## April 03, 2026


Feature 


[Hybrid Subnets](/vpc/docs/hybrid-subnets) is available in
**General Availability**. Hybrid subnet routing
lets a VPC network share a CIDR block with a connected on-premises network.
This configuration helps you migrate workloads to Google Cloud without needing
to change any IP addresses. During migration, workloads that have migrated
to your VPC network can communicate with those remaining in the on-premises
network by using internal IP addresses. After all workloads have migrated,
you can disable hybrid subnet routing to restore normal routing behavior.

For information about pricing for Hybrid Subnets, see
[Virtual Private Cloud pricing](/vpc/pricing?e=0#hybrid-subnets).



## March 30, 2026


Feature 


Service producers can
[accept or reject connections from individual Private Service Connect endpoints](/vpc/docs/about-controlling-access-published-services#accept-endpoint).
This feature is available in **General Availability**.



## March 18, 2026


Feature 


You can
[update a service attachment's target service without recreating the service attachment](https://berlin.devsitetest.how/vpc/docs/manage-private-service-connect-services#change-service).
Consumer connections are preserved during the update, but traffic is briefly
disrupted. This feature is available in **General Availability**.

For more information, including a list of supported configurations, see
[Service mutability](https://berlin.devsitetest.how/vpc/docs/about-vpc-hosted-services#service-mutability).



## February 09, 2026


Feature 


You can bring your own IPv6 global unicast addresses (GUAs)
to assign to a
[subnet's internal IPv6 address range](https://berlin.devsitetest.how/vpc/docs/create-ipv6-sub-prefixes).
Although GUAs are typically public addresses, in this configuration they are
used privately and function in the same way as Google Cloud-provisioned ULAs.

For more information, see [Bring your own IP addresses](https://berlin.devsitetest.how/vpc/docs/bring-your-own-ip).



## February 04, 2026


Feature 


You can create individual static external IPv4 addresses from
bring your own IP addresses (BYOIP) prefixes. This feature is
available in **General Availability** and only applies to IPv4
regional v2 prefixes that are created after
December 13, 2025.

For more information, see [Enhanced IP address allocation](https://berlin.devsitetest.how/vpc/docs/bring-your-own-ip#enhanced-allocation).



## November 14, 2025


Feature 


Dynamic Private Service Connect interfaces are available in
**General Availability**. Private Service Connect interfaces let service
producers initiate connections to service consumers. You can update a VM
instance to add or remove dynamic Private Service Connect interfaces without needing to restart or recreate the instance.

For more information, see
[Private Service Connect interface types](/vpc/docs/about-private-service-connect-interfaces#types).



## November 03, 2025


Feature 


VPC Network Peering supports peering connections in consensus mode. This feature
is available in **General Availability**. For more information, see
[Connection mode](/vpc/docs/about-peering-connections#connection-mode).



## October 30, 2025


Feature 


Dynamic Network Interfaces (NICs) are available in **General Availability**.

Dynamic NICs let you update an instance to add or remove network interfaces without having to restart or recreate the instance.

You can also use Dynamic NICs when you need more network interfaces. The maximum number of vNICs for most machine types in Google Cloud is 10; however, you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

- [Dynamic NICs](/vpc/docs/multiple-interfaces-concepts#dynamic-nics)

- [Create a VM instance with Dynamic NICs](/vpc/docs/create-use-multiple-interfaces)

- [Add Dynamic NICs to an existing instance](/vpc/docs/add-dynamic-nics)




## October 29, 2025


Feature 


You can specify a `/96` IPv6 address range when reserving static regional IPv6
addresses. For more information, see the following:

- [Reserve a static internal IP address](/vpc/docs/reserve-static-internal-ip-address)

- [Reserve a static external IP address](/vpc/docs/reserve-static-external-ip-address)

This feature is available in **General Availability**.



## October 24, 2025


Feature 


You can view IP address utilization when you
[list](https://berlin.devsitetest.how/vpc/docs/create-modify-vpc-networks#listing_existing_subnets)
or
[describe](https://berlin.devsitetest.how/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet)
subnets. IP address utilization displays the number of free
and allocated IP addresses in a subnet. This feature is available in
**General Availability**.



## August 26, 2025


Feature 


IPv6-only subnets and instances are available in **General Availability**. For more information, see the following:

- [Add an IPv6-only subnet](/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only)

- [Create an IPv6-only instance](/compute/docs/instances/create-ipv6-instance#create-vm-ipv6-only)

- [Configure IPv6-only subnets and instances with DNS64 and NAT64](/vpc/docs/connect-ipv6-to-ipv4)

You can also use an IPv6-only NAT subnet to [publish a service with Private Service Connect](/vpc/docs/configure-private-service-connect-producer#publish-service).

For information about which services support IPv6-only configurations, see [IPv6 support in Google Cloud](/vpc/docs/ipv6-support).



## August 04, 2025


Feature 


When you reserve an internal range with an automatically allocated IPv4 CIDR block, you can specify the [allocation strategy](/vpc/docs/internal-ranges#allocation-strategies) that is used to select a free block. This feature is available in **General Availability**.



## July 09, 2025


Feature 


VPC Network Peering supports peering connections in consensus mode. This
feature is available in **Preview**. For more information, see
[Connection mode](/vpc/docs/about-peering-connections#connection-mode).



## May 12, 2025


Feature 


You can exclude IP address ranges from being used for automatic IP address allocation for internal ranges. This feature is available in **General Availability**. For more information, see [Reserve internal ranges](/vpc/docs/create-use-internal-ranges#create-internal-ranges).



## May 07, 2025


Feature 


The following features of internal ranges are available in **General Availability**:

- Reserving internal ranges with IPv6 addresses

- Creating immutable ranges (ranges that can't be edited, except for the description)

- Editable descriptions

For more information, see [Internal ranges overview](/vpc/docs/internal-ranges).



Feature 


When you reserve an internal range with an automatically allocated IPv4 CIDR block, you can specify the [allocation strategy](/vpc/docs/internal-ranges#allocation-strategies) that is used to select a free block. This feature is available in **Preview**.



## April 30, 2025


Feature 


If you're a service producer that makes a service available through VPC Network Peering, you can [migrate your service to Private Service Connect](/vpc/docs/about-migrating-peering-services-private-service-connect) without changing the IPv4 address that consumers use to access the service. This feature is available in **General Availability**.



## March 26, 2025


Feature 


Support for the following is available in **General availability** for dual-stack configurations:

- IPv6 static routes with a next hop internal passthrough Network Load Balancer (`next-hop-ilb`) 

- IPv6 static routes with a next hop instance identified by address (`next-hop-address`) 

For more information, see [Next hops and features](/vpc/docs/static-routes#static-route-next-hops) in the static routes overview.



## March 07, 2025


Feature 


The following features of internal ranges are available in **Preview**:

- Reserving internal ranges with IPv6 addresses

- Creating immutable internal ranges (ranges that can't be updated, except for the description)

- Editable descriptions

For more information, see [Internal ranges overview](/vpc/docs/internal-ranges).



Feature 


You can exclude IP address ranges from internal range automatic IP address allocation. This feature is available in **Preview**. For more information, see [Reserve internal ranges](/vpc/docs/create-use-internal-ranges#create-internal-ranges).



Feature 


You can create internal ranges that overlap with routes and subnets. This feature is available in **General Availability**. For more information, see [Internal ranges overview](/vpc/docs/internal-ranges).



## February 27, 2025


Feature 


The following Private Service Connect monitoring metrics are available for both producers and consumers in **General Availability**:

- Closed connections count

- Received packets dropped count

- Sent packets dropped count

- New connections count

- Open connections

- Received bytes count

- Received packets count

- Sent bytes count

- Sent packets count

Additionally, the NAT IP address capacity metric is available for producers in **General Availability**.

You can use these metrics to help monitor and troubleshoot [published services](/vpc/docs/configure-private-service-connect-producer#dropped-packets), [endpoints that connect to published services](/vpc/docs/configure-private-service-connect-services#dropped-packets), and [backends that connect to published services](/vpc/docs/configure-private-service-connect-services-controls#dropped-packets). For more information, see [Monitor Private Service Connect connections](/vpc/docs/monitor-private-service-connect-connections).



## January 27, 2025


Issue 


There is a known issue with global access endpoints that access services that are published by using internal passthrough Network Load Balancers or internal protocol forwarding (target instances). Private Service Connect doesn't validate that the global access setting on the endpoint matches the setting on the producer's load balancer. We recommend the following:

- 

If you're a service consumer, only enable global access on an endpoint if you know that the producer's load balancer is configured for global access. For more information, see endpoint [Known issues](/vpc/docs/configure-private-service-connect-services#global-access).

- 

If you're a service producer whose services are hosted on internal passthrough Network Load Balancers or internal protocol forwarding (target instances), and those services are accessed through global access endpoints, ensure that global access is enabled on your services' load balancers. For more information, see published services [Known issues](/vpc/docs/configure-private-service-connect-producer#global-access-service-attachments).




Feature 


VPC Flow Logs metadata annotations include [InstanceGroupDetails](/vpc/docs/about-flow-logs-records#instance-group-details). This feature is available in **General Availability**.



## January 15, 2025


Feature 


You can create an internal range with the usage type `FOR_MIGRATION` to migrate a CIDR range from one subnet to another. For more information, see [Migrating subnet ranges](/vpc/docs/internal-ranges#for-migration). This feature is available in **General Availability**.



## December 17, 2024


Feature 


IPv6-only subnets and instances are available in **Preview**. For more information, see the following:

- [Add an IPv6-only subnet](/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only)

- [Create an IPv6-only instance](/compute/docs/ip-addresses/configure-ipv6-address#create-vm-ipv6-only)

- [Types of subnets](/vpc/docs/subnets#subnet-types)

For information about which services support IPv6-only configurations, see [IPv6 support in Google Cloud](/vpc/docs/ipv6-support).



## December 11, 2024


Feature 


[Private Service Connect port mapping](/vpc/docs/about-private-service-connect-port-mapping) is available in **General Availability**. Port mapping lets consumer virtual machine (VM) instances privately communicate with specific service ports on specific producer VMs through a single Private Service Connect endpoint.



## October 31, 2024


Feature 


Support for [IPv6 static routes](/vpc/docs/static-routes#static-route-next-hops) with a next hop internal passthrough Network Load Balancer (`next-hop-ilb`) is available in **Preview**.



## August 12, 2024


Feature 


VPC Flow Logs includes the following metadata annotations in **General Availability**:

- `src_gateway` and `dest_gateway`

- `src_google_service` and `dest_google_service`

- `load_balancing`

- `network_service`

- `psc`

For more information, see [Record Format](/vpc/docs/about-flow-logs-records#record_format).



## July 24, 2024


Feature 


The following producer load balancers now support all [Private Service Connect monitoring metrics](/vpc/docs/monitor-private-service-connect-connections):

- Regional internal Application Load Balancer

- Regional internal proxy Network Load Balancer




## July 22, 2024


Feature 


In the Google Cloud Console, the **Effective routes** tab on the **Routes** page shows only routes that are effective. You can optionally show suppressed routes by using the **Show suppressed routes** toggle. You can also view the reason why a given route is suppressed. For more information, see [List routes for a VPC network](/vpc/docs/using-routes#listingroutes).



## June 28, 2024


Breaking 


Bring your own IP [does not support creating BYOIP addresses in Shared VPC service projects](/vpc/docs/bring-your-own-ip#support). This limitation is documented, but was previously not enforced. Enforcement has been added to prevent the creation of BYOIP addresses in service projects. If you're using bring your own IP with Shared VPC, use the project architecture described in [BYOIP addresses administration with Shared VPC](/vpc/docs/byoip-planning#byoip-shared-vpc).



## June 17, 2024


Feature 


[Private Service Connect backends](/vpc/docs/private-service-connect-backends) support using a [cross-regional internal Application Load Balancer](/load-balancing/docs/l7-internal) to access [global Google API targets](/vpc/docs/private-service-connect-backends#global-google-apis). This feature is available in **Preview**.



## June 14, 2024


Feature 


[Private Service Connect port mapping](/vpc/docs/about-private-service-connect-port-mapping) is available in **Preview**. Port mapping lets consumer virtual machine (VM) instances privately communicate with specific service ports on specific producer VMs through a single Private Service Connect endpoint.



Feature 


[Private Service Connect propagated connections](/vpc/docs/about-propagated-connections) are available in **Preview**. With propagated connections, services that are accessible in one consumer VPC spoke through Private Service Connect endpoints can be privately accessed by other consumer VPC spokes that are connected to the same Network Connectivity Center hub.



## June 10, 2024


Feature 


VPC Flow Logs includes internet routing details for egress flows. For more information, see [InternetRoutingDetails field format](/vpc/docs/flow-logs#InternetRoutingDetails). This field is available in **General Availability**.



Feature 


The following features of policy-based routes are available in **Preview**:

- Applying policy-based routes to IPv6 traffic

- Using a next hop that is in a peered VPC network

For more information, see [Create policy-based routes](/vpc/docs/use-policy-based-routes#create).



## June 03, 2024


Feature 


Bring your own IP lets you [bring your own public IPv6 addresses](/vpc/docs/bring-your-own-ip#comparison) to Google Cloud. IPv6 BYOIP addresses can be used with [external passthrough Network Load Balancers](/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6). Bring your own IP for IPv6 addresses is available in **General Availability**.