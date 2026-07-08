# Cloud DNS overview

Source: https://berlin.devsitetest.how/dns/docs/overview
Last updated: 2026-07-07

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

Cloud DNS

](https://berlin.devsitetest.how/dns/docs)






- 








[

Guides

](https://berlin.devsitetest.how/dns/docs/set-up-dns-records-domain-name)












# Cloud DNS overview 






- On this page 
- [ Shared VPC considerations ](#shared-vpc)
- [ DNS forwarding methods ](#dns-forwarding-methods)
- [ DNS64 ](#dns64-overview)
- [ Access control ](#access_control)

- [ Access control for managed zones ](#access_control_for_managed_zones)

- [ Performance and timing ](#performance_and_timing)

- [ Propagation of changes ](#propagation_of_changes)

- [ What's next ](#whats_next)
- 










This page provides an overview of Cloud DNS features and capabilities.
Cloud DNS is a high-performance, resilient, global Domain Name System
(DNS) service that publishes your domain names to the global
DNS.

DNS is a hierarchical distributed database that lets you store IP addresses and
other data and look them up by name. Cloud DNS lets you publish your
zones and records in DNS without the burden of managing your own DNS servers
and software.

Cloud DNS offers private managed DNS zones. A private zone is visible
only from one or more Virtual Private Cloud (VPC) networks that you specify. For
detailed information about zones, see
[DNS zones overview](/dns/docs/zones/zones-overview).

Cloud DNS supports Identity and Access Management (IAM) permissions at the
project level and individual DNS zone level. For information about how to
set individual resource IAM permissions, see [Create a zone
with specific IAM
permissions](/dns/docs/zones/iam-per-resource-zones).

For a list of general DNS terminology, see the
[General DNS overview](/dns/docs/dns-overview).

For a list of key terminology on which Cloud DNS is built, see
[Key terms](/dns/docs/key-terms).

To get started using Cloud DNS, see the
[Quickstart](/dns/docs/set-up-dns-records-domain-name).

## Shared VPC considerations

To use a Cloud DNS managed private zone, Cloud DNS forwarding
zone, or Cloud DNS peering zone with Shared VPC, you must
create the zone in the
[host project](/vpc/docs/shared-vpc#concepts_and_terminology), and then add one
or more Shared VPC networks to the list of authorized networks
for that zone. Alternatively, you can set up the zone in a service project using
[cross-project binding](/dns/docs/zones/cross-project-binding).

For more information, see
[Best practices for Cloud DNS private zones](/dns/docs/best-practices-dns#best_practices_for_private_zones).

## DNS forwarding methods

Google Cloud Dedicated offers inbound and outbound DNS forwarding for private zones.
You can configure DNS forwarding by creating a forwarding zone or a
Cloud DNS server policy. The two methods are summarized in the
following table.



| 
DNS forwarding | 
Cloud DNS methods | 
|

| 
Inbound | 


Create an [*inbound server policy*](/dns/docs/server-policies-overview#dns-server-policy-in)
to enable an on-premises DNS client or server to send DNS requests to
Cloud DNS. The DNS client or server can then resolve records
according to a VPC network's name resolution order.



On-premises clients can resolve records in private zones, forwarding
zones, and peering zones for which the VPC network has been
authorized. On-premises clients use Cloud VPN or Cloud Interconnect
to connect to the VPC network.

| 
|

| 
Outbound | 



You can configure VMs in a VPC network to do the following:




- Send DNS requests to DNS name servers of your choosing. The name
servers can be located in the same VPC network, in an
on-premises network, or on the internet.

- Resolve records hosted on name servers configured as forwarding
targets of a forwarding zone authorized for use by your
VPC network. For information about how Google Cloud Dedicated
routes traffic to a forwarding target, see
[Forwarding targets
and routing methods](/dns/docs/zones/zones-overview#fz-targets).

- Create an
[*outbound server policy*](/dns/docs/server-policies-overview#dns-server-policy-out)
for the VPC network
to send all DNS requests to an alternative name server. When using an
alternative name server, VMs in your VPC network are no
longer able to resolve records in Cloud DNS private zones,
forwarding zones, peering zones, or Compute Engine internal DNS
zones. For additional details, see
[Name resolution order](/dns/docs/vpc-name-res-order).


| 
|


You can simultaneously configure inbound and outbound DNS forwarding for a
VPC network. Bi-directional forwarding lets VMs in your
VPC network resolve records in an on-premises network or in a
network hosted by a different cloud provider. This type of forwarding also
enables hosts in the on-premises network to resolve records for your
Google Cloud Dedicated resources.

The Cloud DNS control plane uses the [forwarding target selection
order](/dns/docs/zones/zones-overview#fz-target-selection) to select a forwarding target. Outbound forwarded
queries might sometimes result in `SERVFAIL` errors if the forwarding targets
are not reachable or if they don't respond quickly enough. For troubleshooting
instructions, see [Outbound forwarded queries receive SERVFAIL
errors](/dns/docs/troubleshooting#outbound-forwarded-queries-receive-servfail-errors).

For information about how to apply server policies, see [Create DNS
server policies](/dns/docs/policies#creating). To learn how to create a
forwarding zone, see [Create a forwarding
zone](/dns/docs/zones/forwarding-zones).

## DNS64

You can connect your IPv6-only Compute Engine virtual machine (VM)
instances to IPv4 destinations by
using Cloud DNS DNS64. DNS64 provides a synthesized IPv6 address for
each IPv4 destination. Cloud DNS creates a synthesized address by
combining the [Well-Known Prefix
(WKP)](https://www.rfc-editor.org/rfc/rfc6052#page-5) `64:ff9b::/96` with the 32
bits of the destination IPv4 address.

The following example shows how an IPv6-only VM instance
named `vmipv6` resolves the name of an IPv4-only destination.

- 

The `vmipv6` VM instance initiates a DNS request to resolve the destination name to an
IPv6 address.

- 

If a `AAAA` record (IPv6 address) exists, Cloud DNS returns the IPv6
address, and the `vmipv6` VM instance uses it to connect to the destination.

- 

If no `AAAA` record exists, but you configured DNS64, Cloud DNS
searches for an `A` record (IPv4 address). If Cloud DNS finds an `A`
record, it synthesizes a `AAAA` record by prefixing the IPv4 address with
`64:ff9b::/96`.

For example, if the IPv4 address is `32.34.50.60`, the resulting synthesized
IPv6 address is `64:ff9b::2022:323c`, where `2022:323c` is the hexadecimal
equivalent of the IPv4 address. The `64:ff9b::/96` prefix is defined in [RFC
6052](https://datatracker.ietf.org/doc/html/rfc6052). Cloud DNS
synthesizes these IPv6 addresses even when you host the DNS records on-premises,
as long as you enable DNS forwarding in Cloud DNS.

You can use DNS64 in the following scenarios:

- Adhere to mandates requiring a shift to IPv6 addresses without
allocating IPv4 addresses.

- Transition to IPv6-only address infrastructure in stages while maintaining
access to existing IPv4 infrastructure.

- Avoid disruptions to critical services by
ensuring continued access to environments with legacy IPv4 addresses
during your transition to IPv6 addresses.

To configure DNS64 for a VPC network, follow the instructions in
[Configure DNS64](/dns/docs/configure-dns64).

## Access control

You can manage the users who are allowed to make changes to your DNS records
on the [**IAM & Admin** page in the
Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/iam-admin).
For users to be authorized to make changes, they must have the
DNS Administrator role (`roles/dns.admin`) in the Permissions
section of the Google Cloud Dedicated console. The DNS Reader role (`roles/dns.reader`)
grants read-only access to the Cloud DNS records.

These permissions also apply to service accounts that you might use to manage
your DNS services.

To view the permissions assigned to these roles, see [Roles](/dns/docs/access-control#roles).

### Access control for managed zones

Users with the project [Owner role or Editor role](/iam/docs/roles-overview#basic)
(`roles/owner` or `roles/editor`) can manage or view the managed zones in the specific
project that they are managing.

Users with the DNS Administrator role or DNS Reader role can manage or view the
managed zones across all the projects that they have access to.

Project Owners, Editors, DNS Administrators, and DNS Readers can view the list
of private zones applied to any VPC network in the current project.

#### Per resource permission access

To configure a policy on a DNS resource such as a managed zone, you must have
Owner access to the project that owns that resource. The DNS Administrator
role does not have the `setIamPolicy` permission. As a project owner, you can
also create custom IAM roles for your specific needs. For
detailed information, see [Understanding IAM custom
roles](/iam/docs/understanding-custom-roles).

## Performance and timing

Cloud DNS uses [anycast](http://wikipedia.org/wiki/Anycast) to serve
your managed zones.

### Propagation of changes

Changes are propagated in two parts. First, the change that you send through
the API or command-line tool must be pushed to Cloud DNS's
authoritative DNS servers. Second, DNS resolvers must pick up this change when
their cache of the records expires.

The time to live (TTL) value that you set for your records, which is specified
in seconds, controls the DNS resolver's cache. For example, if you set a TTL
value of 86400 (the number of seconds in 24 hours), the DNS resolvers are
instructed to cache the records for 24 hours. Some DNS resolvers ignore the
TTL value or use their own values, which can delay the full propagation of
records.

If you are planning for a change to services that requires a narrow window, you
might want to change the TTL to a shorter value before making
your change—the new shorter TTL value is applied after the previous TTL value expires
in the resolver cache. This approach can help reduce the caching window and ensure a
quicker change to your new record settings. After the change, you can change the
value back to its previous TTL value to reduce load on the DNS resolvers.

## What's next

- Learn about [Cloud DNS differences in Google Cloud Dedicated versus Google Cloud](/dns/docs/tpc-differences).

- 

To get started using Cloud DNS, see
[Quickstart: Set up DNS records for a domain name with Cloud DNS](/dns/docs/set-up-dns-records-domain-name).

- 

To learn about API client libraries, see
[Samples and libraries](/dns/docs/reference/libraries).

- 

To find solutions for common issues that you might encounter when using
Cloud DNS, see [Troubleshooting](/dns/docs/troubleshooting).