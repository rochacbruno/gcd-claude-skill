# Shared VPC

Source: https://documentation.s3ns.fr/vpc/docs/shared-vpc
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

















- On this page ** 
- [ Concepts ](#concepts_and_terminology)

- [ Organizations, folders, and projects ](#shared_vpc_host_project_and_service_project_associations)
- [ Networks ](#shared_vpc_networks)
- [ Organization policy constraints ](#organization_policy_constraints)

- [ Administrators and IAM ](#iam_in_shared_vpc)

- [ Required administrative roles ](#iam_roles_required_for_shared_vpc)
- [ Service Project Admins ](#svc_proj_admins)
- [ Network and Security Admins ](#net_and_security_admins)

- [ Specifications ](#specifications)

- [ Quotas and limits ](#quota)

- [ Resources ](#resources)

- [ Eligible resources ](#eligible-resources)
- [ IP addresses ](#ip_addresses)
- [ Internal DNS ](#shared_vpc_and_internal_dns)
- [ Cloud DNS private zones ](#shared_vpc_and_cloud_dns_private_zones)
- [ Load balancing ](#shared_vpc_with_load_balancing)

- [ Examples and use cases ](#use_cases)

- [ Basic concepts ](#shared_vpc_overview)
- [ Multiple host projects ](#example_multiple_host_projects)
- [ Hybrid cloud scenario ](#hybrid_cloud_scenario)
- [ Two-tier web service ](#two-tier_web_service)

- [ What's next ](#whats_next)
- 









# Shared VPC 



This page provides an overview of Shared VPC in Cloud de Confiance by S3NS.
Shared VPC allows an
[organization](/resource-manager/docs/cloud-platform-resource-hierarchy) to
connect resources from multiple projects to a common
[Virtual Private Cloud (VPC) network](/vpc/docs/vpc) so that they can
communicate with each other securely and efficiently by using internal IP
addresses from that network.

When you use Shared VPC,
you designate a project as a *host project* and attach one or more other
*service projects* to it. The VPC networks in the host project are called
*Shared VPC networks*. [Eligible resources](#eligible-resources)
from service projects can use subnets in the Shared VPC network.

Shared VPC lets [organization
administrators](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations)
delegate administrative responsibilities, such as creating and managing
instances, to [Service Project Admins](#iam_in_shared_vpc) while maintaining
centralized control over network resources like subnets, routes, and firewalls.
This model allows organizations to do the following:

- Implement a security best practice of least privilege for network
administration, auditing, and access control. Shared VPC Admins can delegate
network administration tasks to Network and Security Admins in the Shared VPC
network without allowing Service Project Admins to make network-impacting
changes. Service Project Admins are only given the ability to create and
manage instances that make use of the Shared VPC network. Refer to the
[administrators and IAM](#iam_in_shared_vpc) section for more details.

- Apply and enforce consistent access control policies at the network level for
multiple service projects in the organization while delegating administrative
responsibilities. For example, Service Project Admins can
be Compute Instance Admins in their project, creating and deleting instances
that use approved subnets in the Shared VPC host project.

- Use service projects to separate budgeting or internal cost centers.

## Concepts

### Organizations, folders, and projects



Shared VPC connects projects within the same
[organization](/resource-manager/docs/creating-managing-organization).
Linked projects can be in the same or different
[folders](/resource-manager/docs/creating-managing-folders), but
if they are in different folders the admin must have
[Shared VPC Admin](#iam_in_shared_vpc) rights to both folders. Refer
to the Cloud de Confiance by S3NS [resource
hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy) for
more information about organizations, folders, and projects.

Participating host and service projects cannot belong to different
organizations. The only exception is during a migration of your projects
from one organization to another. During the migration, service projects can
be in a different organization than the host project temporarily. For more
information about migrating projects, see [Migrating
projects](/resource-manager/docs/project-migration#shared_vpc).

A project that participates in Shared VPC is either a *host project* or a
*service project*:

- 

A host project contains one or more [Shared VPC
networks](#shared_vpc_networks). A [Shared VPC Admin](#iam_in_shared_vpc) must
first [enable](/vpc/docs/provisioning-shared-vpc#enable-shared-vpc-host) a project as a
host project. After that, a Shared VPC Admin can attach one or more
service projects to it.

- 

A service project is any project that has been
[attached](/vpc/docs/provisioning-shared-vpc#create-shared) to a host project by a
Shared VPC Admin. This attachment allows it to participate in Shared VPC. It's
a common practice to have multiple service projects operated and administered
by different departments or teams in your organization.

- 

A project cannot be both a host project and a service project simultaneously. Thus, a
service project cannot be a host project to further service projects.

- 

You can create and use multiple host projects; however, each service project
can only be attached to a single host project. For an illustration, see the
[multiple host projects example](#example_multiple_host_projects).

- 

You can create networks, subnets, secondary address ranges, firewall rules,
and other network resources in the host project. The host project can then
share selected subnets, including secondary ranges, with the
service projects. Services running in a service project can use
Shared VPC to communicate with resources running in the other
service projects.

For clarity, a project that does not participate in Shared VPC is called
a *standalone project*. This emphasizes that it is neither a host project nor
a service project.

A *standalone VPC network* is an unshared VPC
network that exists in either a standalone project or a service project.

### Networks

A **Shared VPC network** is a [VPC
network](/vpc/docs/vpc) defined in a host project and made available as a
centrally shared network for [eligible resources](#eligible-resources) in
service projects. Shared VPC networks can be either [auto or custom
mode](/vpc/docs/vpc#subnet-ranges), but [legacy
networks](/compute/docs/vpc/legacy) are not supported.

When a host project is enabled, you have two options for sharing networks:

- You can share all host project subnets. If you select this option, then
any new subnets created in the host project, including subnets in new
networks, will also be shared.

- You can specify individual subnets to share. If you share subnets
individually, then only those subnets are shared unless you manually change
the list.

Host and service projects are connected by attachments **at the project level**.
Subnets of the Shared VPC networks in the host project are accessible by Service
Project Admins as described in the next section, [administrators and
IAM](#iam_in_shared_vpc).

### Organization policy constraints

Organization policies and IAM permissions [work together](/organization-policy/overview#differences_from_iam) to provide different levels
of access control. Organization policies enable you to set controls at the
organization, folder, or project level.

If you are an [organization policy
administrator](/organization-policy/apply-policies),
you can specify the following Shared VPC constraints in an organization policy:

- 

You can limit the set of host projects to which a non-host project or non-host
projects in a folder or organization can be attached. The constraint applies
when a Shared VPC Admin attaches a service project with a host project.
The constraint doesn't affect [existing attachments](/organization-policy/overview#violations).
Existing attachments remain intact even if a policy denies new ones. For more
information, see the
[`constraints/compute.restrictSharedVpcHostProjects`](/organization-policy/reference/org-policy-constraints#constraints/compute.restrictSharedVpcHostProjects)
constraint.

- 

You can specify the Shared VPC subnets that a service project can
access at the project, folder, or organization level. The constraint applies
when you create new VMs and load balancers in the specified subnets and
doesn't affect [existing resources](/organization-policy/overview#violations).
Existing VMs and load balancers continue to operate normally in their subnets
even if a policy prevents new resources from being added. This constraint only
restricts the subnets from being used for VMs and load balancers. Forwarding
rules that are used for Private Service Connect endpoints aren't
restricted by this constraint. For more information, see the
[`constraints/compute.restrictSharedVpcSubnetworks`](/organization-policy/reference/org-policy-constraints#constraints/compute.restrictSharedVpcSubnetworks)
constraint.

## Administrators and IAM

Shared VPC makes use of [Identity and Access Management
(IAM)](/iam/docs/overview) roles for delegated administration. The following
roles can be granted to [IAM
principals](/iam/docs/overview#concepts_related_identity), such as users, Google
groups, Google domains, or Cloud de Confiance service accounts. If you need
to contact any of these admins, you can look them up in your organization's or
project's [IAM policy](/iam/docs/overview#iam_policy). If you don't have the
required permissions, you must contact a network or project administrator in
your organization.

### Required administrative roles



| 
Administrator (IAM role) | 
Purpose | 
|

| 
[
Organization Admin](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) (`resourcemanager.organizationAdmin`)

  • IAM principal in the organization | 
Organization Admins have the
`resourcemanager.organizationAdmin` role for your organization.
They nominate Shared VPC Admins by granting them
[appropriate
project creation and deletion roles](/iam/docs/roles-permissions/resourcemanager), and the *Shared VPC Admin*
role for the organization. These admins can define organization-level
policies, but specific folder and project actions require additional
folder and project roles. | 
|

| 
Shared VPC Admin 
(`compute.xpnAdmin` and 

`resourcemanager.projectIamAdmin`)

  • IAM principal in the organization, or

  • IAM principal in a folder | 
Shared VPC Admins have the
[
*Compute Shared VPC Admin* (`compute.xpnAdmin`)](/iam/docs/roles-permissions/compute#compute.xpnAdmin)
and [
*Project IAM Admin*
(`resourcemanager.projectIamAdmin`)](/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) roles for
the organization or one or more folders. They perform various tasks
necessary to
[set up Shared VPC](/vpc/docs/provisioning-shared-vpc#setting_up_shared_vpc),
such as enabling host projects, attaching service
projects to host projects, and delegating access to some or all of the
subnets in Shared VPC networks to Service Project Admins. A Shared VPC
Admin for a given host project is typically its project owner as well. 

A user assigned the Compute Shared VPC Admin role for the organization has
that role for all folders in the organization. A user assigned the role
for a folder has that role for the given folder and any folders nested
underneath it. A Shared VPC Admin can link projects in two different
folders only if the admin has the role for both folders. | 
|

| 
Service Project Admin 
(`compute.networkUser`)

  • IAM principal in the organization, or

  • IAM principal in a host project, or

  • IAM principal in some subnets in the host project | 
A Shared VPC Admin defines a Service Project Admin by granting an IAM
principal the [
*Network User* (`compute.networkUser`) role](/compute/docs/access/iam#compute.networkUser) to
[either the whole host project or select subnets
of its Shared VPC networks](#svc_proj_admins). Service Project Admins also maintain
ownership and control over resources defined in the service projects, so
they should have the [
*Instance Admin* (`compute.instanceAdmin`) role](/compute/docs/access/iam#compute.instanceAdmin) to
the corresponding service projects. They may have additional IAM roles to
the service projects, such as project owner.
| 
|


### Service Project Admins

When defining each Service Project Admin, a Shared VPC Admin can grant
permission to use the whole host project or just some subnets:

- 

**Project-level permissions**: A Service Project Admin can be defined to have
[permission to use all
subnets](/vpc/docs/provisioning-shared-vpc#networkuseratproject) in the host
project if the Shared VPC Admin grants the role of `compute.networkUser` for
the whole host project to the Service Project Admin. The result is that the
Service Project Admin has permission to use all subnets in all VPC networks of
the host project, including subnets and VPC networks added to the host project
in the future.

- 

**Subnet-level permissions**: Alternatively, a Service Project Admin can be
granted a more restrictive set of [permissions to use only some
subnets](/vpc/docs/provisioning-shared-vpc#networkuseratsubnet) if the Shared VPC Admin
grants the role of `compute.networkUser` for those selected subnets to the
Service Project Admin. A Service Project Admin who only has subnet-level
permissions is restricted to using only those subnets. After new Shared VPC
networks or new subnets are added to the host project, a Shared VPC Admin
should review the permission bindings for the `compute.networkUser` role to
ensure that the subnet-level permissions for all Service Project Admins match
the intended configuration.

### Network and Security Admins

Shared VPC Admins have full control over the resources in the host project,
including administration of the Shared VPC network. They can optionally delegate
certain network administrative tasks to other IAM principals:



| 
Administrator | 
Purpose | 
|

| 
Network Admin

  • IAM principal in the host project, or

  • IAM principal in the organization | 
Shared VPC Admin defines a Network Admin by granting an IAM
principal the [
*Network Admin* (`compute.networkAdmin`) role](/compute/docs/access/iam#compute.networkAdmin) to the
host project. Network Admins have full control over all network resources
except for firewall rules and SSL certificates.
| 
|

| 
Security Admin

  • IAM principal in the host project, or

  • IAM principal in the organization | 
A Shared VPC Admin can define a Security Admin by granting an IAM
principal the [
*Security Admin* (`compute.securityAdmin`) role](/compute/docs/access/iam#compute.securityAdmin) to
the host project. Security Admins manage firewall rules and SSL
certificates.
| 
|


## Specifications

### Quotas and limits

Shared VPC host projects are subject to standard [per-project
VPC quotas](/vpc/docs/quota#per_project). Shared VPC networks
are subject to the [per-network limits](/vpc/docs/quota#per_network) and
[per-instance limits](/vpc/docs/quota#per_instance) for VPC
networks. Additionally, the relationships between host and service projects are
governed by [limits specific to Shared VPC](/vpc/docs/quota#shared-vpc).

## Resources




### Eligible resources

You can use most Cloud de Confiance products and features in Shared VPC
service projects.

The following limitations apply to resources that are eligible for participation
in a Shared VPC scenario:

- 

*Use of a Shared VPC network is not mandatory.* For example, instance admins
can create instances in the service project that use a VPC network in that
project. Networks defined in service projects are not shared.

- 

*Some resources must be re-created in order to use a Shared VPC network.* When
a Shared VPC Admin [attaches an existing project to a host
project](/vpc/docs/provisioning-shared-vpc#create-shared), that project becomes a
service project, but its existing resources do not automatically use shared
network resources. To use a Shared VPC network, a Service Project Admin has to
create an eligible resource and configure it to use a subnet of a Shared VPC
network. For example, an existing instance in a service project cannot be
reconfigured to use a Shared VPC network, but a new instance can be created to
use available subnets in a Shared VPC network. This limitation applies to
private zones.

### IP addresses

When you create an instance in a service project, the IP versions that you
can configure depend on the host project's subnet configuration.
For more information, see
[Create an instance](/vpc/docs/provisioning-shared-vpc#creating_an_instance_in_a_shared_subnet).

Instances in service projects attached to a host project that uses the same
Shared VPC network can communicate internally with one another by using either their
internal IPv4 addresses or their internal or external IPv6 addresses, subject
to applicable [firewall rules](/vpc/docs/firewalls).

Service Project Admins can assign any of the following IP address types to
resources in a service project:

- 

**Ephemeral IPv4 and IPv6 addresses:** An ephemeral IP address can be
automatically assigned to an instance in a
service project. For example, when Service Project Admins [create
instances](/vpc/docs/provisioning-shared-vpc#creating_an_instance_in_a_shared_subnet),
they select the Shared VPC network and an [available shared
subnet](/vpc/docs/provisioning-shared-vpc#discovering_subnets_that_can_be_used).
For instances with IPv4 addresses, the primary internal IPv4 address comes
from the range of available IP addresses in the selected shared subnet's
primary IPv4 address range. For instances with IPv6 addresses, the IPv6
address comes from the range of available IP addresses in the selected
shared subnet's IPv6 subnet range.

Ephemeral IPv4 addresses can also be automatically assigned to internal load
balancers. For more information, see [create an
internal passthrough Network Load Balancer](/vpc/docs/provisioning-shared-vpc#creating_an_internal_load_balancer_forwarding_rule)
or [create an internal Application Load Balancer](/vpc/docs/provisioning-shared-vpc#creating_an_internal_HTTPS_load_balancer).

- 

**Static internal IPv4 and IPv6 addresses:** A static internal IPv4 or IPv6 address
can be reserved in a service project. The internal IPv4 or IPv6 address *object*
must be created in the same service project as the resource that uses it, even
though the value of the IP address comes from the available IP addresses of
the selected shared subnet in a Shared VPC network. For more information,
see [Reserve static internal IP4 and IPv6 addresses](/vpc/docs/provisioning-shared-vpc#reserve_internal_ip)
on the "Provision Shared VPC" page.

- 

**Static external IPv4 addresses:** External IPv4 address objects defined in
the host project can be used by resources in *either* that host project or
any attached service project. Service projects can also use their own external
IPv4 address objects. For example, an instance in a service project can use
a regional external IPv4 address defined in either its service project or in
the host project.

- 

**Static external IPv6 addresses:** A Service Project Admin can also choose
to reserve a static external IPv6 address. The external IPv6 address
*object* must be created in the same service project as the resource that uses
it, even though the value of the IP address comes from the available IPv6
addresses of the selected shared subnet in a Shared VPC network.
For more information, see
[Reserve a static external IPv6 address](/vpc/docs/provisioning-shared-vpc#reserve_external_ipv6)
on the *Provision Shared VPC* page.

### Internal DNS

VMs in the same service project can reach each other using the internal DNS
names that Cloud de Confiance creates automatically. These DNS names use the
project ID of the *service project* where the VMs are created, even though the
names point to internal IP addresses in the host project. For a complete
explanation, see [Internal DNS names and Shared VPC](/compute/docs/internal-dns#shared-vpc)
in the *Internal DNS* documentation.

### Cloud DNS private zones

You can use Cloud DNS private zones in a Shared VPC network.
You can create your private zone in the host project and authorize access to
the zone for the Shared VPC network or set up the zone in a service
project using [cross-project binding](/dns/docs/zones/cross-project-binding).

### Load balancing

Shared VPC can be used in conjunction with
[Cloud Load Balancing](/load-balancing/docs/load-balancing-overview). In most
cases, you create the backend instances in a service project. In that case, all
load balancer components are created in that project. While it's possible to
create backend instances in the host project, such a setup is not well suited
for typical Shared VPC deployments since it does not separate network
administration and service development responsibilities.

Use the links in the following table to learn more about supported
Shared VPC architectures for each type of load balancer.




| 
Load balancer type | 
Links | 
|



| 
[External Application Load Balancer](/load-balancing/docs/https) | 
[
Shared VPC architecture](/load-balancing/docs/https#shared-vpc)
| 
|
| 
[Internal Application Load Balancer](/load-balancing/docs/l7-internal#shared_vpc) | 
[Shared VPC
architecture](/load-balancing/docs/l7-internal#shared_vpc) | 
|

| 
[External proxy Network Load Balancer](/load-balancing/docs/tcp) | 
[Shared VPC
architecture](/load-balancing/docs/tcp#shared-vpc) | 
|

| 
[Internal proxy Network Load Balancer](/load-balancing/docs/tcp/internal-proxy) | 
[Shared VPC
architecture](/load-balancing/docs/tcp/internal-proxy#shared-vpc) | 
|

| 
[Internal passthrough Network Load Balancer](/load-balancing/docs/internal) | 
[
Shared VPC architecture](/load-balancing/docs/internal#shared-vpc)
| 
|

| 
[Regional external passthrough Network Load Balancer](/load-balancing/docs/network) | 
[
Shared VPC architecture](/load-balancing/docs/network/networklb-backend-service#shared-vpc)
| 
|




## Examples and use cases

### Basic concepts

Figure 1 shows a simple Shared VPC scenario:


[

](/static/vpc/images/shared-vpc/shared-vpc-example-concepts.png)



Figure 1.** A host project with a
Shared VPC network provides internal connectivity for two
service projects, while a standalone project doesn't use
Shared VPC (click to enlarge).




- 

A Shared VPC Admin for the organization has created a host project and
attached two service projects to it:

- 

Service Project Admins in `Service project A` can be configured to access
all or some of the subnets in the Shared VPC network. A Service Project
Admin with at least subnet-level permissions to the `10.0.1.0/24 subnet`
has created `Instance A` in a zone of the `us-west1` region. This instance
receives its internal IP address, `10.0.1.3`, from the `10.0.1.0/24` CIDR
block.

- 

Service Project Admins in `Service project B` can be configured to access
all or some of the subnets in the Shared VPC network. A Service Project
Admin with at least subnet-level permissions to the `10.15.2.0/24 subnet`
has created `Instance B` in a zone of the `us-east1` region. This instance
receives its internal IP address, `10.15.2.4`, from the `10.15.2.0/24`
CIDR block.

- 

The *Standalone Project* does not participate in the Shared VPC at all; it is
neither a host nor a service project. Standalone instances are created by
IAM principals who have at least the `compute.InstanceAdmin` role for the project.

### Multiple host projects

Figure 2 shows how Shared VPC can be used to build separate
testing and production environments. For this case, an organization has decided
to use two separate host projects, a *Test Environment* and a *Production
Environment*.


[
](/static/vpc/images/shared-vpc/shared-vpc-example-multiple-host-projects.png)



**Figure 2.** A Test environment host project and a Production
environment host project use Shared VPC to create distinct
production and test environments (click to enlarge).




- 

A Shared VPC Admin for the organization has created two host projects and
attached two service projects to them as follows:

- 

The `Apps testing` and `Mobile testing` service projects are attached to
the `Test environment` host project. Service Project Admins in each
project can be configured to access all or some of the subnets in the
`Testing network`.

- 

The `Apps production` and `Mobile production` service projects are
attached to the `Production environment` host project. Service Project
Admins in each project can be configured to access all or some of the
subnets in the `Production network`.

- 

Both host projects have one Shared VPC network with subnets configured
to use the same CIDR ranges. In both the `Testing network` and `Production
network`, the two subnets are:

- 

`10.0.1.0/24 subnet` in the `us-west1` region

- 

`10.15.2.0/24 subnet` in the `us-east1` region

- 

Consider `Instance AT` in the `Apps testing` service project and `Instance AP`
in the `Apps production` service project:

- 

Service Project Admins can create instances like them provided they have
at least subnet-level permissions to the `10.0.1.0/24 subnet`.

- 

Notice that both instances use the IP address `10.0.1.3`. This is
acceptable because each instance exists in a service project attached to
a unique host project containing its own Shared VPC network. Both the
testing and production networks have been purposefully configured in
the same way.

- 

Instances using the `10.0.1.0/24 subnet` must be located in a zone in the
same region as the subnet, even though the subnet and instances are
defined in separate projects. Because the `10.0.1.0/24 subnet` is located
in the `us-west1` region, Service Project Admins who create instances
using that subnet must choose a zone in the same region, such as
`us-west1-a`.

### Hybrid cloud scenario

Figure 3 shows how Shared VPC can be used in a hybrid
environment.


[
](/static/vpc/images/shared-vpc/shared-vpc-example-hybrid-cloud.png)



**Figure 3.** A Shared VPC network is connected to
an on-premises network and three service projects (click to enlarge).




For this example, an organization has a created a single host
project with a single Shared VPC network. The Shared VPC network is connected
by using [Cloud VPN](/network-connectivity/docs/vpn/concepts/overview) to an on-premises network. Some
services and applications are hosted in Cloud de Confiance while others are
kept on-premises:

- 

A Shared VPC Admin enabled the host project and connected three service
projects to it: `Service project A`, `Service project B`, and `Service project
C`.

- 

Separate teams can manage each of the service projects. IAM permissions
have been configured such that a Service Project Admin for one project has
no permissions to the other service projects.

- 

The Shared VPC Admin has granted subnet-level or project-level permissions
to the necessary Service Project Admins so they can [create
instances](/vpc/docs/provisioning-shared-vpc#creating_an_instance_in_a_shared_subnet)
that use the Shared VPC network:

- 

A Service Project Admin for `Service project A` who has subnet-level
permissions to the `10.0.1.0/24 subnet` can create `Instance A` in it.
The Service Project Admin has to choose a zone in the `us-west1`
region for the instance, because that is the region that contains the
`10.0.1.0/24 subnet`. `Instance A` receives its IP address,
`10.0.1.3`, from the range of free IP addresses in the `10.0.1.0/24
subnet`.

- 

A Service Project Admin for `Service project B` who has subnet-level
permissions to the `10.15.2.0/24 subnet` can create `Instance B` in
it. The Service Project Admin has to choose a zone in the `us-east1`
region for the instance, because that is the region that contains the
`10.15.2.0/24 subnet`. `Instance B` receives its IP address,
`10.15.2.4`, from the range of free IP addresses in `10.15.2.0/24
subnet`.

- 

A Service Project Admin for `Service project C` who has project-level
permissions to the whole host project can create instances in any of
the subnets in any of the VPC networks in the host project. For
example, the Service Project Admin can create `Instance C` in the
`10.7.1.0/24 subnet`, choosing a zone in the `us-east1` region to
match the region for the subnet. `Instance C` receives its IP address,
`10.7.1.50`, from the range of free IP addresses in the `10.7.1.0/24
Subnet`.

- 

The Service Project Admins in each project are responsible for [creating
and managing resources](/vpc/docs/provisioning-shared-vpc#create-resources).

- 

A Shared VPC Admin has delegated network administration tasks to other IAM
principals who are [Network and Security Admins](#net_and_security_admins) for
the Shared VPC network.

- 

A Network Admin has created a Cloud VPN gateway and configured a VPN
tunnel through the internet to an on-premises gateway. The Cloud VPN
exchanges and receives routes with its on-premises counterpart because a
corresponding Cloud Router in the same `us-east1` region [has been
configured](/network-connectivity/docs/vpn/how-to/creating-ha-vpn).

- 

If the [dynamic
routing mode](/vpc/docs/vpc#routing_for_hybrid_networks) of the VPC is
global, the Cloud Router applies the learned routes to the on-premises
network in all subnets in the VPC network, and it shares routes to all of
the VPC subnets with its on-premises counterpart.

- 

Security Admins create and manage firewall rules in the Shared VPC network
to control traffic among instances in Cloud de Confiance and the
on-premises network.

- 

Subject to applicable firewall rules, instances in the service projects
can be configured to communicate with internal services, such as database
or directory servers located on-premises.

### Two-tier web service

Figure 4 demonstrates how Shared VPC can be employed to delegate
administrative responsibilities and maintain the principle of least privilege.
For this case, an organization has a web service that is separated into two
tiers, and different teams manage each tier. Tier 1 represents the
externally facing component, behind an [HTTP(S) load
balancer](/load-balancing/docs/https). Tier 2 represents an internal
service upon which Tier 1 relies, and it is balanced using an [internal TCP/UDP
load balancer](/load-balancing/docs/internal).


[
](/static/vpc/images/shared-vpc/shared-vpc-example-two-tier.png)


**Figure 4.** In this two-tier web service, an externally
facing component and an internal service are connected to a common
Shared VPC network and managed by different teams (click to
enlarge).




Shared VPC lets you map each tier of the web service to different projects
so that they can be managed by different teams while sharing a common VPC
network:

- 

Resources, such as instances and load balancer components, for each tier are
placed in individual service projects managed by different teams.

- 

Each tier service project has been attached to the host project by a
Shared VPC Admin. The Shared VPC Admin also enabled the host project.

- 

Separate teams can manage each tier of the web service by virtue of being
a Service Project Admin in the appropriate service project.

- 

The Service Project Admins in each project are responsible for [creating
and managing resources](/vpc/docs/provisioning-shared-vpc#create-resources).

- 

Network access control is delineated as follows:

- 

IAM principals who only work on Tier 1 are Service Project Admins for the
`Tier 1 service project` and are granted subnet-level permissions for only
the `10.0.1.0/24 subnet`. In this example, one such Service Project Admin
has created three `Tier 1 instances` in that subnet.

- 

IAM principals who only work on Tier 2 are Service Project Admins for the
`Tier 2 service project` and are granted subnet-level permissions for just
the `10.0.2.0/24 subnet`. In this example, another Service Project Admin
has created three `Tier 2 instances` in that subnet along with an internal
load balancer whose forwarding rule uses an IP address from the range
available in that subnet.

- 

IAM principals who oversee the whole web service are Service Project Admins
in both service projects, and they have project-level permissions to the
host project so they can use any subnet defined in it.

- 

Optionally, a Shared VPC Admin can delegate network administration tasks
to [Network and Security Admins](#net_and_security_admins).

## What's next

- To set up Shared VPC, see [Provisioning Shared VPC](/vpc/docs/provisioning-shared-vpc).

- To set up Kubernetes Engine clusters with Shared VPC, see [Setting up clusters with Shared VPC](/kubernetes-engine/docs/how-to/cluster-shared-vpc).

- To delete a Shared VPC setup, see [Deprovisioning Shared VPC](/vpc/docs/deprovisioning-shared-vpc).