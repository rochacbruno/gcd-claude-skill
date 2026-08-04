# Quickstart: Create and manage VPC networks

Source: https://documentation.s3ns.fr/vpc/docs/create-modify-vpc-networks
Last updated: 2026-08-03

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/vpc/docs/tpc-differences) for more details.














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

Virtual Private Cloud

](https://documentation.s3ns.fr/vpc/docs)






- 








[

Guides

](https://documentation.s3ns.fr/vpc/docs/overview)

















- On this page 
- [ Create networks ](#creating_networks)

- [ Create an auto mode VPC network ](#create-auto-network)
- [ Create a custom mode VPC network with IPv4-only subnets ](#create-custom-network)
- [ Create a custom mode VPC network with a dual-stack subnet ](#create-network-dual)
- [ Create a custom mode VPC network with IPv6-only subnets ](#create-network-ipv6-only)
- [ Create a default network ](#create-default-network)
- [ About firewall rules ](#about_firewall_rules)

- [ View networks ](#viewing-networks)
- [ Work with subnets ](#subnet-rules)

- [ List subnets ](#listing_existing_subnets)
- [ Describe a subnet ](#describing_an_existing_subnet)
- [ Add an IPv4-only subnet ](#add-subnets)
- [ Add a dual-stack subnet ](#add-subnet-ipv6)
- [ Add an IPv6-only subnet ](#add-subnet-ipv6-only)
- [ Change an IPv4-only subnet to dual-stack ](#subnet-enable-ipv6)
- [ Change a dual-stack subnet to IPv4 only ](#subnet-change-stacktype)
- [ Add a subnet that uses an IPv6 BYOIP address range ](#byoip)
- [ Add a subnet that uses a reserved IPv4 internal range ](#subnet-internal-range)
- [ Delete a subnet ](#deleting_subnets)
- [ Expand a primary IPv4 range ](#expand-subnet)
- [ Edit secondary IPv4 ranges ](#edit-secondary)

- [ Modify networks ](#modifying_a_vpc_network)

- [ Convert an auto mode VPC network to custom mode ](#switch-network-mode)
- [ Assign an internal IPv6 ULA range to a network ](#enable-internal-ipv6-network)
- [ Change the dynamic routing mode ](#switch-dynamic-routing)
- [ Change the MTU of a network ](#change-mtu)
- [ Delete a network ](#deleting_a_network)

- [ Monitor your VPC network ](#monitoring_your_vpc_network)
- [ Migrate VMs ](#migrating_vms)
- [ Troubleshooting ](#troubleshooting)

- [ Can't delete a VPC network that was used with Serverless VPC Access ](#network-deletion-serverless-error)
- [ Error: Constraint constraints/compute.requireVpcFlowLogs violated ](#constraint-flow-logs)
- [ Resource not found error ](#resource-not-found)
- [ Resource already exists ](#resource-already-exists)

- [ What's next ](#whats_next)
- 









# Create and manage VPC networks 



This document describes how to create, modify, and delete Virtual Private Cloud (VPC)
networks and subnetworks. Before reading this document,
ensure that you are familiar with the characteristics of
VPC networks as described in [VPC networks](/vpc/docs/vpc).
Networks and subnets are [different
resources](/vpc/docs/subnets#vpc_networks_and_subnets) in Cloud de Confiance.

If you plan to enable IPv6 ranges on subnets, see [IPv6
subnet ranges](/vpc/docs/subnets#ipv6-ranges).

## Create networks 

You can choose to create an auto mode or custom mode VPC network.
Each new network that you create must have a unique name within the same
project.

You can optionally create your network using a network profile provided by
Cloud de Confiance for a specific use case. You only need to configure a network
profile if you want to run
[AI Hypercomputer](/ai-hypercomputer/docs/overview) workloads
that require RDMA NICs. For more information, see
[RDMA network profiles](/vpc/docs/rdma-network-profiles).

### Create an auto mode VPC network

When you create an [auto mode](/vpc/docs/vpc#subnet-ranges) VPC
network, one [subnet](/vpc/docs/subnets) is created in each Cloud de Confiance
region. As new regions become available, new subnets in those regions are
automatically added to the auto mode VPC network. IPv4 ranges for
the automatically created subnets come from a [predetermined set of
ranges](/vpc/docs/subnets#ip-ranges). All auto mode VPC networks
use the same set of IPv4 ranges.

Subnets with IPv6 address ranges are not supported on auto mode VPC
networks. Create a [custom mode VPC network](#create-network-dual)
if you want to create subnets with IPv6 address ranges.

To create an auto mode VPC network, follow these steps.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click **Create VPC network**.

- 

Enter a **Name** for the network.

- 

To configure the maximum transmission unit (MTU) of the network, do
the following:

- To use the default value of `1460`, keep the **Set MTU automatically**
checkbox selected.

- To set a custom value, do the following:

- Review the information in [Maximum transmission unit](/vpc/docs/mtu).

- Clear the **Set MTU automatically** checkbox.

- In the **Maximum transmission unit (MTU)** field, choose an MTU
value.

- 

Choose **Automatic** for the **Subnet creation mode**.

- 

In the **Firewall rules** section, select zero or more predefined
[firewall rules](/vpc/docs/firewalls). The rules address common use cases
for connectivity to instances.

Whether or not you select pre-defined rules, you can [create your own
firewall rules](/vpc/docs/using-firewalls) after you create the
network.

Each predefined rule name starts with the name of the
VPC network that you are creating,
` NETWORK `. In the **IPv4 firewall rules** tab, the
predefined ingress firewall rule named
**` NETWORK -allow-custom`** is editable. By default
it specifies the source range `10.128.0.0/9`, which contains current
and future IPv4 ranges for subnets in an auto mode network. The
right side of the row that contains the rule, click **Edit** to
select subnets, add additional IPv4 ranges, and specify protocols and
ports.

- 

Choose the **Dynamic routing mode** for the VPC network.

For more information, see [dynamic routing
mode](/vpc/docs/vpc#routing_for_hybrid_networks). You can [change the
dynamic routing mode](#switch-dynamic-routing) later.

- 

Click **Create**.




Use the
[`networks create` command](/sdk/gcloud/reference/compute/networks/create).


```
gcloud compute networks create NETWORK \
--subnet-mode=auto \
--bgp-routing-mode= DYNAMIC_ROUTING_MODE \
--mtu= MTU 
```


Replace the following:

- ` NETWORK `: a name for the VPC network.

- ` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `global` or
`regional`. The default is `regional`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).

- ` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).




Use
the [`google_compute_network` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).

` MTU ` is the maximum transmission unit, or largest packet
size, of the network. MTU can be set to any value from `1300` to `8896`.
The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).




















```
resource "google_compute_network" "vpc_network" {
project = var.project_id # Replace this with your project ID in quotes
name = "my-auto-mode-network"
auto_create_subnetworks = true
mtu = 1460
}
```



To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).




Make a `POST` request to
the [`networks.insert` method](/compute/docs/reference/rest/v1/networks/insert).


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks
{
"autoCreateSubnetworks": true,
"name": "auto-network1",
"mtu": MTU 
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project where the VPC
network is created.

- ` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).

To specify the [dynamic routing
mode](/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes)
of the VPC network, include the `routingConfig` field:


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks
{
"routingConfig": {
"routingMode": " DYNAMIC_ROUTING_MODE "
},
"autoCreateSubnetworks": true,
"name": " NETWORK ",
"mtu": MTU 
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project where the VPC
network is created.

- ` NETWORK `: a name for the VPC network.

- ` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `GLOBAL` or
`REGIONAL`. The default is `REGIONAL`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).

- ` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).




### Create a custom mode VPC network with IPv4-only subnets

For custom mode VPC networks, create a network, then create the subnets that you
want within a region. You do not have to specify subnets for all regions right
away, or even at all, but you cannot create instances in a region that has no
subnet defined. Finally, define the firewall rules for your network.

Each subnet in a VPC network can have a different configuration;
you don't need to configure them all as IPv4-only, for example. You can also
[change an IPv4-only only subnet to dual-stack](#subnet-enable-ipv6) later.

To create a custom mode VPC network with IPv4-only subnets,
follow these steps.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click **Create VPC network**.

- 

Enter a **Name** for the network.

- 

To configure the MTU of the network, do
the following:

- To use the default value of `1460`, keep the **Set MTU automatically**
checkbox selected.

- To set a custom value, do the following:

- Review the information in [Maximum transmission unit](/vpc/docs/mtu).

- Clear the **Set MTU automatically** checkbox.

- In the **Maximum transmission unit (MTU)** field, choose an MTU
value.

- 

Choose **Custom** for the **Subnet creation mode**.

- 

In the **New subnet** section, specify the following configuration
parameters for a subnet:

- Provide a **Name** for the subnet.

- Select a **Region**.

- 

Enter an **IP address range**. This is the [primary IPv4
range](/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that
the range doesn't conflict with an existing configuration. For more
information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- 

To define a secondary range for the subnet, click **Create secondary
IP range**.

If you select a range that is not an RFC 1918 address, confirm that
the range doesn't conflict with an existing configuration. For more
information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- 

**Private Google Access**: Choose whether to enable
[Private Google Access](/vpc/docs/private-access-options) for the
subnet when you create it or later by editing it.

- 

**Flow logs**: Choose whether to enable [VPC flow
logs](/vpc/docs/using-flow-logs) for the subnet when you create it
or later by editing it.

- 

Click **Done**.

- 

To add more subnets, click **Add subnet** and repeat the previous steps.
You can also [add more subnets](#add-subnets) to the network after you
have created the network.

- 

In the **Firewall rules** section, select zero or more predefined
[firewall rules](/vpc/docs/firewalls) in the **IPv4 firewall rules**.
The rules address common use cases for connectivity to instances.

If you don't select any predefined rules, you can [create your own
firewall rules](/vpc/docs/using-firewalls) after you create the
network.

Each predefined rule name starts with the name of the
VPC network that you are creating,
` NETWORK `. In the **IPv4 firewall rules** tab, the
predefined ingress firewall rule named
**` NETWORK -allow-custom`** is editable. On the
right side of the row that contains the rule, click **Edit** to
select subnets, add additional IPv4 ranges, and specify protocols and
ports.

The **` NETWORK -allow-custom`** firewall rule is not
automatically updated if you later add additional subnets. If you need
firewall rules for the new subnets, you must update the firewall
configuration to add the rules.

- 

Choose the **Dynamic routing mode** for the VPC network.

For more information, see [dynamic routing
mode](/vpc/docs/vpc#routing_for_hybrid_networks). You can [change the
dynamic routing mode](#switch-dynamic-routing) later.

- 

Click **Create**.




Use the [`networks create` command](/sdk/gcloud/reference/compute/networks/create).


```
gcloud compute networks create NETWORK \
--subnet-mode=custom \
--bgp-routing-mode= DYNAMIC_ROUTING_MODE \
--mtu= MTU 
```


Replace the following:

- ` NETWORK `: a name for the VPC network.

- ` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `global` or
`regional`. The default is `regional`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).

- ` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).

Next, [add subnets](#add-subnets) to your network.



Use the [`google_compute_network` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).

` MTU ` is the maximum transmission unit, or largest packet
size, of the network. MTU can be set to any value from `1300` to `8896`.
The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).




















```
resource "google_compute_network" "vpc_network" {
project = var.project_id # Replace this with your project ID in quotes
name = "my-custom-mode-network"
auto_create_subnetworks = false
mtu = 1460
}
```



Next, [add subnets](#add-subnets) to your network.

To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).




Make a `POST` request to the
[`networks.insert` method](/compute/docs/reference/rest/v1/networks/insert).


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks
{
"autoCreateSubnetworks": false,
"name": " NETWORK ",
"mtu": MTU ,
"routingConfig": {
"routingMode": " DYNAMIC_ROUTING_MODE "
}
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project where the VPC
network is created.

- ` NETWORK `: a name for the VPC network.

- ` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `GLOBAL` or
`REGIONAL`. The default is `REGIONAL`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).

- ` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).

Next, [add subnets](#add-subnets) to your network.



### Create a custom mode VPC network with a dual-stack subnet

You can create subnets when you create the network, or you can add them later.

A dual-stack subnet can have one of the following configurations for its primary
IP address ranges:

- Internal IPv4 range and *internal* IPv6 range

- Internal IPv4 range and *external* IPv6 range

Each subnet in a VPC network can have a different configuration;
you don't need to configure them all as dual-stack, for example.

By default, the addresses for a subnet's IPv6 range are provided by
Google. If you want to use BYOIP to bring your own IPv6 addresses,
see [Assign subnet ranges](/vpc/docs/create-ipv6-sub-prefixes#create-subnets)
instead.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click **Create VPC network**.

- 

Enter a **Name** for the network.

- 

To configure the MTU of the network, do
the following:

- To use the default value of `1460`, keep the **Set MTU automatically**
checkbox selected.

- To set a custom value:

- Review the information in [Maximum transmission unit](/vpc/docs/mtu).

- Clear the **Set MTU automatically** checkbox.

- In the **Maximum transmission unit (MTU)** field, choose an MTU
value.

- 

For **Subnet creation mode**, choose **Custom**.

- 

If you want to configure internal IPv6 address ranges on subnets in this
network, complete these steps:

- In the **Private IPv6 address settings** section, select
**Configure a ULA internal IPv6 range for this VPC Network**.

- 

For **Allocate internal IPv6 range**, select **Automatically** or
**Manually**.

If you select **Manually**, enter a `/48` range from within the
`fd20::/20` range. If the range is in use, you are prompted to provide
a different range.

- 

In the **New subnet** section, specify the following configuration
parameters for a subnet:

- Provide a **Name** for the subnet.

- Select a **Region**.

- To create a dual-stack subnet, for **IP stack type**, select
**IPv4 and IPv6 (dual-stack)**.

- 

Enter an **IPv4 range**. This is the [primary IPv4
range](/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that
the range doesn't conflict with an existing configuration. For more
information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- 

Select an **IPv6 access type**: **External** or **Internal**.

- 

Click **Done**.

- 

To add more subnets, click **Add subnet** and repeat the previous steps.

Each subnet in a VPC network can have different stack type
and IPv6 access type configurations. You do not need to configure all
subnets in a given network as dual-stack subnets.

You can also [add more subnets](#subnet-rules) of any stack type to the
network after you create the network.

- 

In the **Firewall rules** section, select zero or more predefined
[firewall rules](/vpc/docs/firewalls) in the **IPv4 firewall rules** and
**IPv6 firewall rules** tabs. The rules address common use cases for
connectivity to instances.

If you don't select any predefined rules, you can [create your own
firewall rules](/vpc/docs/using-firewalls) after you create the
network.

Each predefined rule name starts with the name of the
VPC network that you are creating,
` NETWORK `. In both the **IPv4 firewall rules** tab and
the **IPv6 firewall rules** tab, there is an editable predefined
ingress firewall rule; the IPv4 rule is named
**` NETWORK -allow-custom`** and the IPv6 rule is named
**` NETWORK -allow-ipv6-custom`**. On the right side of
the row that contains the rule, click **Edit** to select subnets, add
additional IP ranges, and specify protocols and ports.

The **` NETWORK -allow-custom`** and
**` NETWORK -allow-ipv6-custom`** firewall rule are not
automatically updated if you later add additional subnets. If you need
firewall rules for the new subnets, you must update the firewall
configuration to add the rules.

- 

Choose the **Dynamic routing mode** for the VPC network.

For more information, see [dynamic routing
mode](/vpc/docs/vpc#routing_for_hybrid_networks). You can [change the
dynamic routing mode](#switch-dynamic-routing) later.

- 

Click **Create**.




Use the [`networks create` command](/sdk/gcloud/reference/compute/networks/create).
After you have created the network, you can add [subnets](#subnet-rules)
to it.

If you want to configure *internal* IPv6 ranges on any subnets in this
network, use the `--enable-ula-internal-ipv6` flag. This option assigns a
`/48` ULA prefix from within the `fd20::/20` range used by Google for internal
IPv6 subnet ranges. If you want to select the `/48` IPv6 range that is
assigned, use the `--internal-ipv6-range` flag to specify a range.

You can omit both flags if you want to configure only *external* IPv6 on
subnets in this VPC network.


```
gcloud compute networks create NETWORK \
--subnet-mode=custom \
[ --enable-ula-internal-ipv6 [ --internal-ipv6-range= ULA_IPV6_RANGE ]] \
--bgp-routing-mode= DYNAMIC_ROUTING_MODE \
--mtu= MTU 
```


Replace the following:

- 

` NETWORK `: a name for the VPC network.

- 

` ULA_IPV6_RANGE `: a `/48` prefix from within the
`fd20::/20` range used by Google for internal IPv6 subnet ranges. If you
don't use the `--internal-ipv6-range` flag, Google selects a `/48` prefix
for the network.

- 

` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `global` or
`regional`. The default is `regional`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).

- 

` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).




Use the [`google_compute_network` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).

If you want to configure internal IPv6 ranges on any subnets in this network,
use the `enable_ula_internal_ipv6` argument.

See the following example:




















```
resource "google_compute_network" "default" {
name = "vpc-network-ipv6"
auto_create_subnetworks = false
enable_ula_internal_ipv6 = true
}
```



Next, [add subnets](#add-subnet-ipv6) to your network.

To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).




Make a `POST` request to the
[`networks.insert` method](/compute/docs/reference/rest/v1/networks/insert).
After you have created the network, you can add [subnets](#subnet-rules)
to it.

If you want to configure *internal* IPv6 ranges on any subnets in this
network, set `enableUlaInternalIpv6` to true. This option assigns a `/48`
range from within the `fd20::/20` range used by Google for internal IPv6
subnet ranges. If you want to select which `/48` IPv6 range is assigned,
also use the `internalIpv6Range` field when you specify a range.

To configure only *external* IPv6 on subnets in this VPC network,
omit both fields.


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks
{
"autoCreateSubnetworks": false,
"name": " NETWORK ",
"mtu": MTU ,
"enableUlaInternalIpv6": true,
"internalIpv6Range": " ULA_IPV6_RANGE ",
"routingConfig": {
"routingMode": " DYNAMIC_ROUTING_MODE "
}
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project where the VPC
network is created.

- ` NETWORK `: a name for the VPC network.

- ` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).

- ` ULA_IPV6_RANGE `: a `/48` prefix from within the
`fd20::/20` range used by Google for internal IPv6 subnet ranges. If you
don't provide a value for `internalIpv6Range`, Google selects a `/48` prefix
for the network.

- ` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `GLOBAL` or
`REGIONAL`. The default is `REGIONAL`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).




### Create a custom mode VPC network with IPv6-only subnets

You can create subnets when you create the network, or you can add them later.

An IPv6-only subnet can have an *internal* IPv6 range or an *external* IPv6
range.

Each subnet in a VPC network can have a different configuration;
you don't need to configure them all as IPv6-only, for example.

You can't change a dual-stack or IPv4-only subnet to IPv6-only.
Conversely, you can't change an IPv6-only subnet to IPv4-only or dual-stack.

By default, the IPv6 addresses for a subnet are provided by Google.
If you want to use BYOIP to bring your own IPv6 addresses,
see [Assign subnet ranges](/vpc/docs/create-ipv6-sub-prefixes#create-subnets)
instead.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click **Create VPC network**.

- 

Enter a **Name** for the network.

- 

To configure the MTU of the network, do
the following:

- To use the default value of `1460`, keep the **Set MTU automatically**
checkbox selected.

- To set a custom value, do the following:

- Review the information in [Maximum transmission unit](/vpc/docs/mtu).

- Clear the **Set MTU automatically** checkbox.

- In the **Maximum transmission unit (MTU)** field, choose an MTU
value.

- 

For **Subnet creation mode**, choose **Custom**.

- 

To configure internal IPv6 address ranges on subnets in this
network, complete these steps:

- In the **Private IPv6 address settings** section, select
**Configure a ULA internal IPv6 range for this VPC Network**.

- 

For **Allocate internal IPv6 range**, select **Automatically** or
**Manually**.

If you select **Manually**, enter a `/48` range from within the
`fd20::/20` range. If the range is in use, you are prompted to provide
a different range.

- 

In the **New subnet** section, specify the following configuration
parameters for a subnet:

- Provide a **Name** for the subnet.

- Select a **Region**.

- To create an IPv6-only subnet, for **IP stack type**, select
**IPv6 (single-stack)**.

- Select an IPv6 access type: **External** or **Internal**.

- Click **Done**.

- 

To add more subnets, click **Add subnet** and repeat the previous steps.

Each subnet in a VPC network can have different stack type
and IPv6 access type configurations. You don't need to configure all
subnets in a given network as IPv6-only subnets.

You can also [add more subnets](#subnet-rules) of any stack type to the
network after you create the network.

- 

In the **Firewall rules** section, select zero or more predefined
[firewall rules](/vpc/docs/firewalls) in the **IPv6 firewall rules**
tab. The rules address common use cases for connectivity to instances.

If you don't select any predefined rules, you can [create your own
firewall rules](/vpc/docs/using-firewalls) after you create the
network.

Each predefined rule name starts with the name of the
VPC network that you are creating,
` NETWORK `. In the **IPv6 firewall rules** tab, there
is an editable predefined ingress firewall rule named
**` NETWORK -allow-ipv6-custom`**. On the row that
contains the rule, click **Edit** to select subnets, add
additional IP ranges, and specify protocols and ports.

The **` NETWORK -allow-ipv6-custom`** firewall rule
isn't automatically updated if you later add additional subnets. If you
need firewall rules for the new subnets, you must update the firewall
configuration to add the rules.

- 

Choose the **Dynamic routing mode** for the VPC network.

For more information, see [Dynamic routing
mode](/vpc/docs/vpc#routing_for_hybrid_networks). You can [change the
dynamic routing mode](#switch-dynamic-routing) later.

- 

Click **Create**.




Use the [`networks create` command](/sdk/gcloud/reference/compute/networks/create).
After you have created the network, you can add [subnets](#subnet-rules)
to it.

If you want to configure *internal* IPv6 ranges on any subnets in this
network, use the `--enable-ula-internal-ipv6` flag. This option assigns a
`/48` ULA prefix from within the `fd20::/20` range used by Google for internal
IPv6 subnet ranges. If you want to select the `/48` IPv6 range that is
assigned, use the `--internal-ipv6-range` flag to specify a range.

You can omit both flags if you want to configure only *external* IPv6 on
subnets in this VPC network.


```
gcloud compute networks create NETWORK \
--subnet-mode=custom \
[ --enable-ula-internal-ipv6 [ --internal-ipv6-range= ULA_IPV6_RANGE ]] \
--bgp-routing-mode= DYNAMIC_ROUTING_MODE \
--mtu= MTU 
```


Replace the following:

- 

` NETWORK `: a name for the VPC network.

- 

` ULA_IPV6_RANGE `: a `/48` prefix from within the
`fd20::/20` range used by Google for internal IPv6 subnet ranges. If you
don't use the `--internal-ipv6-range` flag, Google selects a `/48` prefix
for the network.

- 

` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `global` or
`regional`. The default is `regional`. For more information, see
[Dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).

- 

` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).




Use the [`google_compute_network` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).

If you want to configure internal IPv6 ranges on any subnets in this network,
use the `enable_ula_internal_ipv6` argument.

See the following example:




















```
resource "google_compute_network" "default" {
name = "vpc-network-ipv6"
auto_create_subnetworks = false
enable_ula_internal_ipv6 = true
}
```



Next, [add subnets](#add-subnet-ipv6-only) to your network.

To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).




Make a `POST` request to the
[`networks.insert` method](/compute/docs/reference/rest/v1/networks/insert).
After you have created the network, you can add [subnets](#subnet-rules)
to it.

If you want to configure *internal* IPv6 ranges on any subnets in this
network, set `enableUlaInternalIpv6` to true. This option assigns a `/48`
range from within the `fd20::/20` range used by Google for internal IPv6
subnet ranges. If you want to select which `/48` IPv6 range that is assigned,
also use the `internalIpv6Range` field to specify a range.

You can omit both fields if you want to configure only *external* IPv6 on
subnets in this VPC network.


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks
{
"autoCreateSubnetworks": false,
"name": " NETWORK ",
"mtu": MTU ,
"enableUlaInternalIpv6": true,
"internalIpv6Range": " ULA_IPV6_RANGE ",
"routingConfig": {
"routingMode": " DYNAMIC_ROUTING_MODE "
}
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project where the VPC
network is created.

- ` NETWORK `: a name for the VPC network.

- ` MTU `: the maximum transmission unit (MTU), which is the
largest packet size of the network. MTU can be set to any value from
`1300` to `8896`. The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).

- ` ULA_IPV6_RANGE `: a `/48` prefix from within the
`fd20::/20` range used by Google for internal IPv6 subnet ranges. If you
don't provide a value for `internalIpv6Range`, Google selects a `/48` prefix
for the network.

- ` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `GLOBAL` or
`REGIONAL`. The default is `REGIONAL`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).




### Create a default network

Some tasks assume that you have an auto mode VPC
network that is called `default`. To create this configuration, do the
following.


[ gcloud ](#gcloud) 
More 




- 

Create an auto mode VPC network called `default` by using the
[`networks create` command](/sdk/gcloud/reference/compute/networks/create).


```
gcloud compute networks create default \
--subnet-mode=auto
```


- 

Configure firewall rules by using the [`firewall-rules create`
command](/sdk/gcloud/reference/compute/firewall-rules/create).


```
gcloud compute firewall-rules create default-allow-internal \
--allow=tcp:1-65535,udp:1-65535,icmp \
--direction=INGRESS \
--network=default \
--priority=1000 \
--source-ranges=10.128.0.0/9
```



```
gcloud compute firewall-rules create default-allow-ssh \
--allow=tcp:22 \
--direction=INGRESS \
--network=default \
--priority=1000 \
--source-ranges=0.0.0.0/0
```



```
gcloud compute firewall-rules create default-allow-rdp \
--allow=tcp:3389 \
--direction=INGRESS \
--network=default \
--priority=1000 \
--source-ranges=0.0.0.0/0
```



```
gcloud compute firewall-rules create default-allow-icmp \
--allow=icmp \
--direction=INGRESS \
--network=default \
--priority=1000 \
--source-ranges=0.0.0.0/0
```





### About firewall rules

After you create a network, [create firewall rules](/vpc/docs/using-firewalls)
to allow or deny traffic between resources in the network, such as communication
between VM instances. You also use firewall rules to control what traffic leaves
or enters the VPC network to or from the internet.

## View networks

View the VPC and legacy networks in your project. For
VPC networks, you can view information about their subnets and
their subnet creation mode.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

The console lists all of your VPC and legacy networks.

- 

Select a VPC network to view its details, such as its
peering connections and subnets.




- 

To list the networks in your project, use the
[`networks list` command](/sdk/gcloud/reference/compute/networks/list).


```
gcloud compute networks list
```


The command lists all of your VPC and legacy networks.
Legacy networks show a subnet creation mode of `LEGACY`, while
VPC networks show either `AUTO` or `CUSTOM`.


```
NAME SUBNET_MODE BGP_ROUTING_MODE IPV4_RANGE GATEWAY_IPV4
custom-network CUSTOM REGIONAL
default AUTO REGIONAL
legacy-network1 LEGACY REGIONAL 10.240.0.0/16 10.240.0.1
```


- 

To describe a network and view its details, such as peering connections
and subnets, use the
[`networks describe` command](/sdk/gcloud/reference/compute/networks/describe).


```
gcloud compute networks describe NETWORK 
```


Replace ` NETWORK ` with the name of the network.




- 

To list all networks in your project, make a `GET` request to the
[`networks.list` method](/compute/docs/reference/rest/v1/networks/list).


```
GET https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks
```


Replace ` PROJECT_ID ` with the ID of the project that contains
the VPC networks to list.

- 

To describe a network and view its details, make a `GET` request to the
[`networks.get` method](/compute/docs/reference/rest/v1/networks/get).


```
GET https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks/ NETWORK 
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network.

- ` NETWORK `: the name of the VPC network
to describe.




## Work with subnets

The following sections describe how to create and manage subnets.

### List subnets

You can see all the subnets that exist for a project or VPC
network, including details about IP address utilization.

IP address utilization shows the number of free and allocated IP addresses
that exist in a subnet. The allocated total includes IP addresses that are
managed by Compute Engine, such as VMs and internal forwarding rules.
However, this total doesn't include some IP addresses the are managed outside of
Compute Engine, such as the stable IP addresses used by `ClusterIP`
Kubernetes Services.

The allocated IP address total also includes the unusable
[IPv4](/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet) and
[IPv6](/vpc/docs/subnets#unusable-ip-addresses-in-every-ipv6-subnet)
addresses that are reserved for internal use.

To view utilization details for IPv6 addresses, use the
gcloud CLI or send an API request. For IPv6 utilization, the
total values are calculated by the following equation:
(`high` * 2^64) + `low` = total value.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

To view subnets, do one of the following:

- 

Click the name of a network, and then click the **Subnets** tab on
the **VPC network details** page.

This view lets you add new subnets and modify other configurations
for a single selected network.

- 

Click the **Subnets in current project** tab and select one or more
networks from the **VPC networks** list.

This view lets you list the subnets in more than one network.

The percentage of available IP addresses that are assigned to resources is
displayed in the **Primary IPv4 range availability** column.
To see the specific number of free and allocated IP addresses,
hold the pointer over this column in the row where you want to
view details.




You can list all subnets in all networks in your project, or you can show
only the subnets for a particular network or region. The following examples
demonstrate how to use the
[`subnets list` command](/sdk/gcloud/reference/compute/networks/subnets/list).

- 

To list all subnets in all VPC networks, use the following
command:


```
gcloud compute networks subnets list
```


- 

To list all subnets in a particular VPC network, use
the following command:


```
gcloud compute networks subnets list \
--network= NETWORK 
```


Replace ` NETWORK ` with the name of the network.

- 

To list all subnets in a particular region, use the following command:


```
gcloud compute networks subnets list \
--filter="region:( REGION … )"
```


Replace ` REGION ` with the name of the region.

- 

To list all subnets in your project and include their IP address
utilization, use the following command:


```
gcloud compute networks subnets list \
--view=WITH_UTILIZATION
```





- 

To list all subnets in your project, make a `GET` request to the
[`subnetworks.aggregatedList` method](/compute/docs/reference/rest/v1/subnetworks/aggregatedList).


```
GET https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /aggregated/subnetworks
```


Replace ` PROJECT_ID ` with the ID of the project that contains the
subnets to list.

- 

To list all subnets in a region and include their IP address
utilization, make the following `GET` request:


```
GET https://compute.googleapis.com/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks?views=WITH_UTILIZATION
```





### Describe a subnet

You can view the details of an existing subnet—such as its primary IPv4
ranges, secondary IP ranges, IPv6 ranges, IP address
utilization, and region—by following the steps in this section.

IP address utilization shows the number of free and allocated IP addresses
that exist in a subnet. The allocated total includes IP addresses that are
managed by Compute Engine, such as VMs and internal forwarding rules.
However, this total doesn't include some IP addresses the are managed outside of
Compute Engine, such as the stable IP addresses used by `ClusterIP`
Kubernetes Services.

The allocated IP address total also
includes the unusable [IPv4](/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet) and
[IPv6](/vpc/docs/subnets#unusable-ip-addresses-in-every-ipv6-subnet)
addresses that are reserved for internal use.

To view utilization details for IPv6 addresses, use the
gcloud CLI or send an API request. For IPv6 utilization, the
total values are calculated by the following equation:
(`high` * 2^64) + `low` = total value.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

All networks and subnets in your project are presented in a hierarchical
view, where subnets are shown as entries within networks.

- 

To focus on subnets for a particular network, click the name of a
network. On its *VPC network details* page, click the name of a subnet in
the **Subnets** tab to view its *Subnet details* page.




- 

[List subnets](#listing_existing_subnets) to determine the names
and regions of existing subnets in your project.

- 

Use the
[`subnets describe` command](/sdk/gcloud/reference/compute/networks/subnets/describe).

- 

To describe the subnet, use the following command:


```
gcloud compute networks subnets describe SUBNET \
--region= REGION 
```


Replace the following:

- ` SUBNET `: the subnet to describe

- ` REGION `: the region of the subnet to describe

- 

To describe the subnet and view its IP address utilization, use the
following command:


```
gcloud compute networks subnets describe SUBNET \
--region= REGION \
--view=WITH_UTILIZATION
```





- 

To list subnets in a particular region and find a subnet's name,
make a `GET` request to the
[`subnetworks.list` method](/compute/docs/reference/rest/v1/subnetworks/list).


```
GET https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
subnets to list.

- ` REGION `: the name of the Cloud de Confiance region
that contains the subnets to list.

- 

Make a `GET` request to the [`subnetworks.get` method](/compute/docs/reference/rest/v1/subnetworks/get).

- 

To describe the subnet, send the following request:


```
GET https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks/ SUBNET 
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that
contains the subnet to describe.

- ` REGION `: the name of the Cloud de Confiance
region that contains the subnet to describe.

- ` SUBNET `: the name of the subnet to describe.

- 

To describe the subnet and view its IP address utilization,
send the following request:


```
GET https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks/ SUBNET ?views=WITH_UTILIZATION
```





### Add an IPv4-only subnet

When you create a subnet, you set a name, a region, and at least a primary IPv4
address range according to the [name](/vpc/docs/subnets#subnet-name-limitations) and
[IPv4 subnet range](/vpc/docs/subnets#ipv4-range-limitations) limitations.

To create an IPv4-only subnet, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click the name of a VPC network to show its *VPC network
details* page.

- 

Click **Add subnet**. In the panel that appears:

- Provide a **Name**.

- Select a **Region**.

- 

Enter an **IP address range**. This is the [primary IPv4
range](/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that
the range doesn't conflict with an existing configuration. For more
information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- 

To define a secondary range for the subnet, click **Create secondary
IP range**.

If you select a range that is not an RFC 1918 address, confirm that
the range doesn't conflict with an existing configuration. For more
information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- 

**Private Google access**: You can enable
[Private Google Access](/vpc/docs/private-access-options) for the
subnet when you create it or later by editing it.

- 

**Flow logs**: You can enable [VPC flow
logs](/vpc/docs/using-flow-logs) for the subnet when you create it
or later by editing it.

- 

Click **Add**.




Use the [`subnets create`
command](/sdk/gcloud/reference/compute/networks/subnets/create).


```
gcloud compute networks subnets create SUBNET \
--network= NETWORK \
--range= PRIMARY_RANGE \
--region= REGION 
```


Replace the following:

- ` SUBNET `: a name for the new subnet.

- ` NETWORK `: the name of the VPC network
that contains the new subnet.

- ` PRIMARY_RANGE `: the primary IPv4 range for the new
subnet, in CIDR notation. For more information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- ` REGION `: the Cloud de Confiance region in which the
new subnet is created.

You can modify the preceding command with the following optional flags:

- `--secondary-range= SECONDARY_RANGE_NAME = SECONDARY_RANGE `:
Replace ` SECONDARY_RANGE_NAME ` with a name for the
secondary range. Replace ` SECONDARY_RANGE ` with a
secondary range in CIDR notation. The [per network
limits](/vpc/docs/quota#per_network) describe the maximum number of
secondary ranges that you can define for each subnet.

- `--enable-flow-logs`: Enables [VPC Flow Logs](/vpc/docs/using-flow-logs) in
the subnet at creation time.

- `--enable-private-ip-google-access`: Enables
[Private Google Access](/vpc/docs/private-access-options) in the
subnet at creation time.

- `--purpose`: Enables you to specify the [purpose of the
subnet](/vpc/docs/subnets#purpose).

- `--role`: Enables you to specify a role (active or backup) for a
[proxy-only subnet](/load-balancing/docs/proxy-only-subnets).

Next, create [firewall
rules](/firewall/docs/using-firewalls#creating_firewall_rules).



Use a
[Terraform module](https://github.com/terraform-google-modules/terraform-google-network).

` MTU ` is the maximum transmission unit, or largest packet
size, of the network. MTU can be set to any value from `1300` to `8896`.
The default is `1460`. Before setting the MTU to a
value higher than `1460`, review [Maximum transmission unit](/vpc/docs/mtu).




















```
module "test-vpc-module" {
source = "terraform-google-modules/network/google"
version = "~> 16.0"
project_id = var.project_id # Replace this with your project ID in quotes
network_name = "my-custom-mode-network"
mtu = 1460

subnets = [
{
subnet_name = "subnet-01"
subnet_ip = "10.10.10.0/24"
subnet_region = "us-west1"
},
{
subnet_name = "subnet-02"
subnet_ip = "10.10.20.0/24"
subnet_region = "us-west1"
subnet_private_access = "true"
subnet_flow_logs = "true"
},
{
subnet_name = "subnet-03"
subnet_ip = "10.10.30.0/24"
subnet_region = "us-west1"
subnet_flow_logs = "true"
subnet_flow_logs_interval = "INTERVAL_10_MIN"
subnet_flow_logs_sampling = 0.7
subnet_flow_logs_metadata = "INCLUDE_ALL_METADATA"
subnet_flow_logs_filter = "false"
}
]
}
```



Next, create [firewall rules](/vpc/docs/using-firewalls#creating_firewall_rules).



Make a `POST` request to the
[`subnetworks.insert` method](/compute/docs/reference/rest/v1/subnetworks/insert).


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks
{
"ipCidrRange": " IP_RANGE ",
"network": " NETWORK_URL ",
"name": " SUBNET "
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network to modify.

- ` REGION `: the name of the Cloud de Confiance region where
the subnet is added.

- ` IP_RANGE `: the primary IPv4 address range for the subnet.
For more information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- ` NETWORK_URL `: the URL of the VPC network
where you're adding the subnet.

- ` SUBNET `: a name for the subnet.

Next, create [firewall rules](/vpc/docs/using-firewalls#creating_firewall_rules).



### Add a dual-stack subnet

Dual-stack subnets have both IPv4 and IPv6 address ranges. You can create a
subnet with
[external or internal IPv6 addresses](/vpc/docs/subnets#ipv6-ranges).

By default, the addresses for a subnet's IPv6 range are provided by
Google. If you want to use BYOIP to bring your own IPv6 addresses,
see [Assign subnet ranges](/vpc/docs/create-ipv6-sub-prefixes#create-subnets)
instead.

To create a dual-stack subnet, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click the name of a VPC network to show its *VPC network
details* page.

- 

Click **Add subnet**. In the panel that appears:

- Provide a **Name**.

- Select a **Region**.

- For **IP stack type**, select **IPv4 and IPv6 (dual-stack)**.

- 

Enter an **IPv4 range**. This is the [primary IPv4
range](/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that
the range doesn't conflict with an existing configuration. For more
information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- 

Select an **IPv6 access type**: **Internal** or **External**.

If you want to set the access type to **Internal**, but the
**Internal** option is not available, check that [an internal IPv6
range is assigned](#enable-internal-ipv6-network) on the network.

- 

Click **Add**.




Use the
[`subnets create` command](/sdk/gcloud/reference/compute/networks/subnets/create).
If you're creating an internal IPv6 subnet range, make sure that the network
has an assigned [internal IPv6 ULA range](#enable-internal-ipv6-network).


```
gcloud compute networks subnets create SUBNET \
--network= NETWORK \
--range= PRIMARY_IPv4_RANGE \
--stack-type=IPV4_IPV6 \
--ipv6-access-type= IPv6_ACCESS_TYPE \
--region= REGION 
```


Replace the following:

- ` SUBNET `: a name for the new subnet.

- ` NETWORK `: the name of the VPC network
that will contain the new subnet.

- ` PRIMARY_IPv4_RANGE `: the primary IPv4 range for the new
subnet, in CIDR notation. For more information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- ` IPv6_ACCESS_TYPE `: the IPv6 access type.
It can be `EXTERNAL` or `INTERNAL`.

- ` REGION `: the Cloud de Confiance region in which the new
subnet will be created.




Use the [`google_compute_subnetwork` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork).

See the following example:




















```
resource "google_compute_subnetwork" "subnet_dual_stack" {
name = "subnet-dual-stack"
ip_cidr_range = "10.0.0.0/22"
region = "us-west2"
stack_type = "IPV4_IPV6"
ipv6_access_type = "INTERNAL"
network = google_compute_network.default.id
}
```



To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).




Make a `POST` request to the
[`subnetworks.insert` method](/compute/docs/reference/rest/v1/subnetworks/insert).
If you're creating an internal IPv6 subnet range, make sure that the network
has an assigned [internal IPv6 ULA range](#enable-internal-ipv6-network).


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks
{
"ipCidrRange": " IP_RANGE ",
"network": " NETWORK_URL ",
"name": " SUBNET "
"stackType": IPV4_IPV6,
"ipv6AccessType": IPv6_ACCESS_TYPE 
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network to modify.

- ` REGION `: the name of the Cloud de Confiance region
where the subnet is added.

- ` IP_RANGE `: the primary IPv4 address range for the subnet.
For more information, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- ` NETWORK_URL `: the URL of the VPC network
where you're adding the subnet.

- ` SUBNET `: a name for the subnet.

- ` IPv6_ACCESS_TYPE `: the IPv6 access type. It can be
`EXTERNAL` or `INTERNAL`.




### Add an IPv6-only subnet

You can create an IPv6-only subnet with [external or internal IPv6
addresses](/vpc/docs/subnets#ipv6-ranges) enabled.

By default, the addresses for a subnet's IPv6 range are provided by
Google. If you want to use BYOIP to bring your own IPv6 addresses,
see [Assign subnet ranges](/vpc/docs/create-ipv6-sub-prefixes#create-subnets)
instead.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

To view the **VPC network details** page, click the name of a VPC network.

- 

On the **Subnets** tab, click add_box **Add subnet**.
In the panel that appears:

- Provide a **Name**.

- Select a **Region**.

- For **IP stack type**, select **IPv6 (single-stack)**.

- 

Select an IPv6 access type: **Internal** or **External**.

If you want to set the access type to **Internal**, but the
**Internal** option is not available, check that [an internal IPv6
range is assigned](#enable-internal-ipv6-network) on the network.

- 

Click **Add**.




Use the
[`gcloud compute networks subnets create` command](/sdk/gcloud/reference/compute/networks/subnets/create).


```
gcloud compute networks subnets create SUBNET \
--network= NETWORK \
--stack-type=IPV6_ONLY \
--ipv6-access-type= IPv6_ACCESS_TYPE \
--region= REGION 
```


Replace the following:

- ` SUBNET `: a name for the new subnet.

- ` NETWORK `: the name of the VPC network
to contain the new subnet.

- ` IPv6_ACCESS_TYPE `: the IPv6 access type.
The access type can be either `EXTERNAL` or `INTERNAL`.

- ` REGION `: the Cloud de Confiance region in which the new
subnet is to be created.




Use the [`google_compute_subnetwork` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork).

See the following example:




















```
resource "google_compute_subnetwork" "subnet_ipv6_only" {
name = "subnet-ipv6-only"
region = "us-central1"
network = google_compute_network.default.id
stack_type = "IPV6_ONLY"
ipv6_access_type = "INTERNAL"
}
```



To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).




Make a `POST` request to the
[`subnetworks.insert` method](/compute/docs/reference/rest/v1/subnetworks/insert).


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks
{
"network": " NETWORK_URL ",
"name": " SUBNET "
"stackType": IPV6_ONLY,
"ipv6AccessType": IPv6_ACCESS_TYPE 
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network to modify.

- ` REGION `: the name of the Cloud de Confiance region
where the subnet is added.

- ` NETWORK_URL `: the URL of the VPC network
where you are adding the subnet.

- ` SUBNET `: a name for the subnet.

- ` IPv6_ACCESS_TYPE `: the IPv6 access type. The
access type can be either `EXTERNAL` or `INTERNAL`.




### Change an IPv4-only subnet to dual-stack

Dual-stack subnets have both IPv4 and IPv6 subnet ranges. You can add either [an
internal or an external IPv6 subnet range](/vpc/docs/subnets#ipv6-ranges) to an
existing IPv4-only subnet in a custom mode VPC network. For more
information, see [IPv6 subnet ranges](/vpc/docs/subnets#ipv6-ranges).

By default, the addresses for a subnet's IPv6 range are provided by
Google. If you want to use BYOIP to bring your own IPv6 addresses,
see [Assign subnet ranges](/vpc/docs/create-ipv6-sub-prefixes#create-subnets)
instead.

To change a subnet's stack type to dual-stack, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click the name of a network to view the **VPC network details** page.

- 

In the **Subnets** tab, click the name of the subnet that you want to
modify.

- 

In the **Subnet details** page, click **Edit**.

- 

For **IP stack type**, select **IPv4 and IPv6 (dual-stack)**.

- 

Select an **IPv6 access type**: **Internal** or **External**.

If you want to set the access type to **Internal**, but the
**Internal** option is not available, check that [an internal IPv6
range is assigned](#enable-internal-ipv6-network) for the network.

- 

Click **Save**.




Use the
[`subnets update` command](/sdk/gcloud/reference/compute/networks/subnets/update).


```
gcloud compute networks subnets update SUBNET \
--stack-type=IPV4_IPV6 \
--ipv6-access-type= IPv6_ACCESS_TYPE \
--region= REGION 
```


Replace the following:

- ` SUBNET `: the name of the subnet.

- ` REGION `: the region of the subnet.

- ` IPv6_ACCESS_TYPE `: the IPv6 access type of the subnet.
It can be `EXTERNAL` or `INTERNAL`.




Make a `PATCH` request to
the [`subnetworks.patch` method](/compute/docs/reference/rest/v1/subnetworks/patch).


```
PATCH https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks/ SUBNET 
{
"stackType": IPV4_IPV6,
"ipv6AccessType": IPv6_ACCESS_TYPE 
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network to modify.

- ` REGION `: the subnet's region.

- ` SUBNET `: the name of the subnet.

- ` IPv6_ACCESS_TYPE `: the IPv6 access type. It can be
`EXTERNAL` or `INTERNAL`.






### Change a dual-stack subnet to IPv4 only

You can change a subnet's stack type from IPv4 and IPv6 (dual-stack) to IPv4
only (single-stack) if the IPv6 access type is *external*.

If you make this change, you cannot create new dual-stack VMs that are connected
to that subnet. However, existing dual-stack VMs are not affected. If you need
to change a VM's stack type to be IPv4 only, see [Change the stack type of a
VM](/compute/docs/ip-addresses/configure-ipv6-address#update-vm-stacktype).

This change is supported in Google Cloud CLI and the API only.

Changing the stack type from IPv4 and IPv6 (dual-stack) to IPv4 only
(single-stack) is not supported if the IPv6 access type is *internal*.

To change a subnet's stack type to IPv4 only, do the following.


[ gcloud ](#gcloud) [ API ](#api) 
More 




Use the
[`subnets update` command](/sdk/gcloud/reference/compute/networks/subnets/update).


```
gcloud compute networks subnets update SUBNET \
--stack-type=IPV4_ONLY \
--region= REGION 
```


Replace the following:

- ` SUBNET `: the name of the subnet.

- ` REGION `: the subnet's Cloud de Confiance region




Make a `PATCH` request to the
[`subnetworks.patch` method](/compute/docs/reference/rest/v1/subnetworks/patch).


```
PATCH https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks/ SUBNET 
{
"stackType": IPV4_ONLY,
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network to modify.

- ` REGION `: the subnet's Cloud de Confiance region.

- ` SUBNET `: the name of the subnet.




### Add a subnet that uses an IPv6 BYOIP address range

Bring your own IP addresses (BYOIP) lets you import global unicast address
(GUA) ranges that you can assign to a subnet's internal or external IPv6 address
range. When you assign a subnet an internal GUA range, the addresses
are configured as privately used GUAs that aren't publicly routable.

For more information, see
[Assign subnet ranges](/vpc/docs/create-ipv6-sub-prefixes#create-subnets).

### Add a subnet that uses a reserved IPv4 internal range

If you have a reserved internal range with usage type set to `FOR_VPC`, and
peering type set to `FOR_SELF`, you can create a subnet that uses all or part of
that range. For more information, see [Create subnetworks with IPv4 internal
ranges](/vpc/docs/create-use-internal-ranges#create-subnets-with-ranges).

### Delete a subnet

Use the following directions to delete a manually created subnet. Before you can
delete a subnet, you must delete all resources that use it. For example, you
need to [delete
VMs](/compute/docs/instances/deleting-instance),
reserved internal IP addresses, internal forwarding rules, and
Cloud NAT gateways that use the subnet.

To delete a subnet, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

All networks and subnets in your project are presented in a hierarchical
view, where subnets are shown as entries within networks.

- 

To view a particular network, click the name of a
network. On its **VPC network details** page, click the name of a subnet
in the **Subnets** tab to view its **Subnet details** page.

- 

Click **Delete subnet**.

- 

In the message that appears, click **Delete** to confirm.




Use the [`subnets delete` command](/sdk/gcloud/reference/compute/networks/subnets/delete).


```
gcloud compute networks subnets delete SUBNET \
--region= REGION 
```


Replace the following:

- ` SUBNET `: the name of the subnet to delete.

- ` REGION `: the region of the subnet to delete.




Make a `DELETE` request to the
[`subnetworks.delete` method](/compute/docs/reference/rest/v1/subnetworks/delete).


```
DELETE https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks/ SUBNET 
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
subnet to delete.

- ` REGION `: the name of the Cloud de Confiance region that
contains the subnet to delete.

- ` SUBNET `: the name of the subnet to delete.




### Expand a primary IPv4 range

You can expand the primary IPv4 range of an existing subnet by modifying its
subnet mask, setting the prefix length to a *smaller* number. The proposed
new primary IPv4 range of the subnet must follow the rules listed in the
[IPv4 subnet range limitations](/vpc/docs/subnets#ipv4-range-limitations).

When expanding the IPv4 range of an automatically created subnet in an auto mode
VPC network (or in a custom mode VPC network that
was previously an auto mode VPC network),
the broadest prefix (subnet mask) you can use is `/16`. Any prefix broader than
`/16` would conflict with [the primary IPv4 ranges of the other automatically
created subnets](/vpc/docs/subnets#ip-ranges).

You can't expand subnets that are used exclusively for load
balancer proxies. For more information, see [Proxy-only subnets for load
balancers](/load-balancing/docs/proxy-only-subnets).

Expanding the primary IPv4 range of a subnet can take several
minutes to complete. During expansion, traffic within the subnet is *not*
interrupted.

If you expand the primary IPv4 range of a subnet, you might need to modify
other configurations that are assuming this IP address range.

- If you have [VPC firewall rules](/vpc/docs/firewalls) or
[firewall policy rules](/vpc/docs/firewall-policies-rule-details) that use the
original IPv4 address range as a source or destination, add additional firewall
rules to apply the same rules to the extended range.

- If a Google Kubernetes Engine (GKE) cluster uses the subnet whose primary
IPv4 address range you expand, you must
[add the expanded IP range to the control plane authorized networks
list](/kubernetes-engine/docs/how-to/authorized-networks#add).

To expand a subnet's primary IPv4 range, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

All networks and subnets in your project are presented in a hierarchical
view, where subnets are shown as entries within networks.

- 

To focus on subnets for a particular network, click the name of a
network. On its **VPC network details** page, click the name of a subnet
in the **Subnets** tab to view its **Subnet details** page.

- 

Click **Edit**.

- 

Enter a new, broader CIDR block in the **IP address range** field.

For valid ranges, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- 

Click **Save**.




Use the
[`subnets expand-ip-range` command](/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range).


```
gcloud compute networks subnets expand-ip-range SUBNET \
--region= REGION \
--prefix-length= PREFIX_LENGTH 
```


Replace the following:

- ` SUBNET `: the name of the subnet.

- ` REGION `: the region in which the subnet is located.

- ` PREFIX_LENGTH `: a subnet mask size in bits. If the primary IPv4
range is `10.1.2.0/24`, you can supply `20` to reduce the subnet mask to
20 bits, which changes the primary IPv4 range to `10.1.2.0/20`. For valid
ranges, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).




Make a `POST` request to the
[`subnetworks.expandIpCidrRange` method](/compute/docs/reference/rest/v1/subnetworks/expandIpCidrRange).


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks/ SUBNET /expandIpCidrRange
{
"ipCidrRange": " IP_RANGE "
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the subnet to
modify.

- ` REGION `: the name of the Cloud de Confiance region that contains the
subnet to modify.

- ` SUBNET `: the name of the subnet to modify.

- ` IP_RANGE `: the expanded IPv4 address range for the subnet. For
valid ranges, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).




### Edit secondary IPv4 ranges

You can add secondary IPv4 ranges to subnets, or you can remove any
secondary IPv4 range as long as no resources are using IP addresses in it.


[ gcloud ](#gcloud) [ API ](#api) 
More 




To add a new secondary IPv4 range to a subnet, use the
[`subnets update` command](/sdk/gcloud/reference/compute/networks/subnets/update).


```
gcloud compute networks subnets update SUBNET \
--region= REGION \
--add-secondary-ranges= SECONDARY_RANGE_NAME = SECONDARY_RANGE 
```


Replace the following:

- ` SUBNET `: the name of the subnet.

- ` REGION `: the region in which the subnet is located.

- ` SECONDARY_RANGE_NAME `: a name for the secondary range.

- ` SECONDARY_RANGE `: the secondary IPv4 range in CIDR notation. For
valid ranges, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

To remove a secondary IPv4 range from a subnet, use the
[`subnets update` command](/sdk/gcloud/reference/compute/networks/subnets/update).


```
gcloud compute networks subnets update SUBNET \
--region= REGION \
--remove-secondary-ranges= SECONDARY_RANGE_NAME 
```


Replace the following:

- ` SUBNET `: the name of the subnet.

- ` REGION `: the region in which the subnet is located.

- ` SECONDARY_RANGE_NAME `: the name of the secondary range to
remove.




To modify secondary IPv4 address ranges for an existing subnet, make a
`PATCH` request to the
[`subnetworks.patch` method](/compute/docs/reference/rest/v1/subnetworks/patch).


```
PATCH https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /regions/ REGION /subnetworks/ SUBNET 
{
"secondaryIpRanges": [
{
"rangeName": " SECONDARY_RANGE_NAME ",
"ipCidrRange": " IP_RANGE "
},
{
"rangeName": " SECONDARY_RANGE_NAME ",
"ipCidrRange": " IP_RANGE "
}],
"fingerprint": " SUBNETWORK_FINGERPRINT "
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the subnet to
modify.

- ` REGION `: the name of the Cloud de Confiance region that
contains the subnet to modify.

- ` SUBNET `: the name of the subnet to modify.

- ` SECONDARY_RANGE_NAME `: a name for the secondary IPv4 address
range.

- ` IP_RANGE `: the expanded IPv4 address range for the subnet. For
valid ranges, see [IPv4 subnet
ranges](/vpc/docs/subnets#manually_created_subnet_ip_ranges).

- ` SUBNET_FINGERPRINT `: the fingerprint ID for the existing
subnet, which is provided when you [describe a
subnet](#describing_an_existing_subnet).




## Modify networks

### Convert an auto mode VPC network to custom mode

You can convert an auto mode VPC network to a custom mode
VPC network using this procedure. Review the [considerations for
auto mode VPC networks](/vpc/docs/vpc#auto-mode-considerations)
for background information about reasons why you might want to do this.

Converting an auto mode VPC network to a custom mode
VPC network **preserves** all of its automatically created
subnets and any subnets you have added. Subnet names and IP ranges are not
changed.

After you convert an auto mode VPC network to custom mode, you
must review all API calls and gcloud CLI commands that implicitly
reference any subnet that was automatically created while the network was in
auto mode. API calls and commands will need to be modified so that they
reference the subnet explicitly. For gcloud CLI commands that have a
subnet specification flag (`--subnet`), that flag is required to reference
subnets in a custom mode VPC network.

To convert an auto mode VPC network to a custom mode
VPC network, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click the name of a VPC network to show its **VPC network
details** page.

- 

Click **Edit**.

- 

In the **Subnet creation mode** section, choose **Custom**.

- 

Click **Save**.




Use the
[`networks update` command](/sdk/gcloud/reference/compute/networks/update).


```
gcloud compute networks update NETWORK \
--switch-to-custom-subnet-mode
```


Replace ` NETWORK ` with the name of the network to
update.



Make a `POST` request to the
[`networks.switchToCustomMode` method](/compute/docs/reference/rest/v1/networks/switchToCustomMode).


```
POST https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks/ NETWORK /switchToCustomMode
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network to convert.

- ` NETWORK `: the name of the VPC network to
convert.




### Assign an internal IPv6 ULA range to a network

If you want to configure internal IPv6 unique local addresses (ULAs) on a
subnet, you must first enable ULA addresses on the VPC network.
When you enable ULAs, a `/48` ULA range is assigned to the network. Addresses
are allocated from this range when you assign a ULA range to a subnet.

This step isn't required if you're assigning an internal IPv6 subnet range from
a BYOIP sub-prefix.

After you have enabled a ULA range for your VPC network,
you can do the following:

- [Add dual-stack subnets](#add-subnet-ipv6)

- [Change an IPv4-only subnet to dual-stack](#subnet-enable-ipv6)

- [Add IPv6-only subnets](#add-subnet-ipv6-only)

To assign an internal ULA range to a network, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click the name of a VPC network to show its *VPC network
details* page.

- 

Click **Edit**.

- 

In the **Private IPv6 address settings** section, select
**Configure a ULA internal IPv6 range for this VPC Network**.

- 

Optional: You can provide the prefix to use for the internal IPv6 range.

- For **Allocate ULA internal IPv6 range**, click **Manually**.

- 

Enter a `/48` range from within the `fd20::/20` range.

If the range is in use, you are prompted to enter a different range.

- 

Click **Save**.




Use the
[`networks update` command](/sdk/gcloud/reference/compute/networks/update).

The `--enable-ula-internal-ipv6` flag assigns a `/48` prefix from within the
`fd20::/20` range used by Google for internal IPv6 subnet ranges. If you
want to select the `/48` IPv6 range that is assigned, use the
`--internal-ipv6-range` flag to specify a range.


```
gcloud compute networks update NAME \
--enable-ula-internal-ipv6 \
[ --internal-ipv6-range= ULA_IPV6_RANGE ]
```


Replace the following:

- ` NAME `: the name of the VPC network.

- ` ULA_IPV6_RANGE `: the range of IPv6 addresses to which you need
to allocate a ULA prefix.




Make a `PATCH` request to the
[`networks.insert` method](/compute/docs/reference/rest/v1/networks/insert).

Setting `enableUlaInternalIpv6` to true assigns a `/48` range from within
the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you
want to select which `/48` IPv6 range is assigned, also use the
`internalIpv6Range` field to specify a range.


```
PATCH https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networksa/ NETWORK 
{
"enableUlaInternalIpv6": true,
"internalIpv6Range": " ULA_IPV6_RANGE ",
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project where the VPC
network is created.

- ` NETWORK `: a name for the VPC network.

- ` ULA_IPV6_RANGE `: a `/48` prefix from within the
`fd20::/20` range used by Google for internal IPv6 subnet ranges. If you
don't provide a value for `internalIpv6Range`, Google selects a `/48` prefix
for the network.




### Change the dynamic routing mode

Each VPC network has an associated dynamic routing mode that
controls the behavior of Cloud Routers in the network. Refer to the
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks) section in
*VPC networks* to understand how each mode affects
how Cloud Routers share routes and apply learned routes.

To change a VPC network's dynamic routing mode, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click the name of a VPC network to show its **VPC network
details** page.

- 

Click **Edit**.

- 

In the **Dynamic routing mode** section, choose either **Global** or
**Regional**.

- 

Click **Save**.




Use the
[`networks update` command](/sdk/gcloud/reference/compute/networks/update).


```
gcloud compute networks update NETWORK \
--bgp-routing-mode= DYNAMIC_ROUTING_MODE 
```


Replace the following:

- ` NETWORK `: the name of the VPC network
to update.

- ` DYNAMIC_ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `global` or
`regional`. The default is `regional`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).




Make a
`PATCH` request to the
[`subnetworks.patch` method](/compute/docs/reference/rest/v1/subnetworks/patch).


```
PATCH https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks/ NETWORK 
{
"routingConfig": {
"routingMode": " ROUTING_MODE "
}
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network to modify.

- ` NETWORK `: the name of the VPC network to
modify.

- ` ROUTING_MODE `: controls the behavior of
Cloud Routers in the network. Can be either `GLOBAL` or
`REGIONAL`. The default is `REGIONAL`. For more information, see
[dynamic routing mode](/vpc/docs/vpc#routing_for_hybrid_networks).




### Change the MTU of a network

For information about changing the MTU of a VPC network, see
[Change the MTU setting of a VPC
network](/vpc/docs/change-mtu-vpc-network).

### Delete a network

If a network is not being used, you can delete it. Before you can delete
a network, you must delete all resources in all of its subnets, and all
resources that reference the network. Resources that reference the network
include [VPC Network Peering connections](/vpc/docs/using-vpc-peering#deleting-peer), [Cloud VPN gateways](/network-connectivity/docs/vpn/how-to/deleting-a-gateway), [Cloud Routers](/network-connectivity/docs/router/how-to/managing-routers#deletes),
[Serverless VPC Access connectors](/vpc/docs/configure-serverless-vpc-access#delete-connector) and their connected services,
[firewall rules](/firewall/docs/using-firewalls#deleting_firewall_rules), and [custom static routes](/vpc/docs/using-routes#deletingaroute).

To delete a VPC network, do the following.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Cloud de Confiance console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.s3nscloud.fr/networking/networks/list) 

- 

Click the name of a VPC network to show its **VPC network
details** page.

- 

Click **Delete VPC network**.

- 

In the message that appears, click **Delete** to confirm.




Use the
[`networks delete` command](/sdk/gcloud/reference/compute/networks/delete).


```
gcloud compute networks delete NETWORK 
```


Replace ` NETWORK ` with the name of the network to delete.



Make a `DELETE` request to the
[`networks.delete` method](/sdk/gcloud/reference/compute/networks/delete).


```
DELETE https://compute.s3nsapis.fr/compute/v1/projects/ PROJECT_ID /global/networks/ NETWORK 
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the
VPC network to delete.

- ` NETWORK `: the name of the VPC network to
delete.




## Monitor your VPC network

You can enable logging of network flows to and from VMs. See
[Using VPC Flow Logs](/vpc/docs/using-flow-logs) for instructions.

You can enable logging for firewall rules to see which rules allowed or
blocked which traffic. See
[Using Firewall Rules Logging](/vpc/docs/using-firewall-rules-logging) for instructions.

## Migrate VMs

You can migrate your virtual machine (VM) instances from one network to
another within a given project. For instructions, see [Migrating a VM between
networks](/compute/docs/instances/migrating-interfaces-between-networks).

## Troubleshooting

### Can't delete a VPC network that was used with Serverless VPC Access

You might receive an error when attempting to delete a VPC
network for which Serverless VPC Access was
configured even if you have deleted the
associated Serverless VPC Access connector. The error message
is similar to the following: `The network resource ' RESOURCE ' cannot be deleted because it is being used by a Serverless resource.` This error occurs because
there is still an association between one or more serverless resources and the VPC network.

To resolve this issue, remove any associations to the
Serverless VPC Access connector from the serverless resources:

- 

If any Cloud Run services or functions used the connector, then
for each service or function, follow the steps to
[Disconnect a Cloud Run service from a VPC network](/run/docs/configuring/vpc-connectors#disconnect-service).

- 

If any Cloud Run jobs used the connector, then for each job,
follow the steps to [Disconnect a Cloud Run job from a VPC network](/run/docs/configuring/vpc-connectors#disconnect-job)

- 

If any App Engine services used the connector, then
for each service, follow the steps to
[Disconnect an App Engine service from a VPC network](/appengine/docs/standard/connecting-vpc#disconnect).

- 

After you disconnect all serverless resources from the VPC
network,
[delete the VPC network](#deleting_a_network).

To prevent this issue from happening again, ensure that you disconnect any
serverless resources before deleting a connector as described in
[Delete a connector](/run/docs/configuring/vpc-connectors#delete).

In rare cases, you might still receive an error after completing the steps
in this section. If you still can't delete the VPC network,
contact [Cloud Customer Care](https://documentation.s3ns.fr/support).

### Error: `Constraint constraints/compute.requireVpcFlowLogs violated`

This error occurs if both of these conditions apply:

- 

An organization policy constraint has been set that requires that
VPC Flow Logs is configured.

- 

You create a subnet, or update the VPC Flow Logs configuration of an
existing subnet, and the configuration does not meet the requirements of the
policy.

For more information about this constraint and its effects on subnet creation
and updates, see [Organization policy constraints for
VPC Flow Logs](/vpc/docs/org-policy-flow-logs).

### Resource not found error

When deleting a VPC network, you might see a message that is
similar to the following: `The resource "aet-uscentral1-subnet--1-egrfw" was not
found.`

For information about this error and its solution, see
[Resource not found error](/vpc/docs/using-firewalls#resource-not-found) in the
VPC firewall rules documentation.

### Resource already exists

When you create a subnet, you see a message that is similar to the following:
`The resource ' SUBNET_URI ' already exists`. You see this error
if there's already a subnet with the same name and region as the subnet that
you're trying to create. For more information about subnet names, see
[Limitations for naming subnets](/vpc/docs/subnets#subnet-name-limitations).

## What's next

- For information about routes, see [Routes](/vpc/docs/routes).

- For information about firewall rules, see [Firewall rules](/vpc/docs/firewalls).

- For more details about VPC networking, see [Advanced VPC concepts](/vpc/docs/advanced-vpc).

- Learn about [using a hybrid subnet to migrate workloads to a VPC network without changing IP addresses](/vpc/docs/hybrid-subnets).