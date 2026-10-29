# Cloud NGFW release notes

Source: https://documentation.s3ns.fr/firewall/docs/release-notes
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/firewall/docs/tpc-differences) for more details.














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

Cloud NGFW

](https://documentation.s3ns.fr/firewall/docs)






- 








[

Resources

](https://documentation.s3ns.fr/firewall/docs/resources)












# Cloud NGFW release notes 



















This page contains release notes for features and updates to Cloud Next Generation Firewall (Cloud NGFW).

To view Cloud NGFW announcements prior to April 2023, see the
[Virtual Private Cloud (VPC) release notes](/vpc/docs/release-notes).







You can see the latest product updates for all of Cloud de Confiance by S3NS on the
[
Cloud de Confiance](/release-notes) page, browse and filter all release notes in the
[Cloud de Confiance console](https://console.cloud.s3nscloud.fr/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.s3nscloud.fr/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://documentation.s3ns.fr/feeds/cloud-firewall-release-notes.xml) directly.









## June 30, 2026

v1 


Feature 


You can now create and configure project-level resources for application layer
inspection in Cloud NGFW, including project-level firewall endpoints, security
profile groups, and security profiles. For more information, see
[Organization-level and project-level
resources](/firewall/docs/about-app-layer-inspection#org-project-resources),
[Firewall endpoints overview](/firewall/docs/about-firewall-endpoints),
[Security profile groups overview](/firewall/docs/about-security-profile-groups),
and [Security profiles overview](/firewall/docs/about-security-profiles). This
feature is available in **General Availability**.


v1 


Feature 


To restrict traffic to the managed Envoy proxies in a
[proxy-only subnet](/load-balancing/docs/proxy-only-subnets), you can configure
global network firewall policies and regional network firewall policies to
protect internal Application Load Balancers and internal proxy Network Load
Balancers. For more information, see [Use global network firewall policies to
protect Envoy-based load balancers](/firewall/docs/global-network-app-lb) and
[Use regional network firewall policies to protect internal Application Load
Balancers and internal proxy Network Load
Balancers](/firewall/docs/regional-network-app-lb). This feature is available in
**General Availability**.



## May 15, 2026

v1 


Issue 


Due to a known issue, the limit of firewall endpoint associations per
organization-level firewall endpoint is restricted to 15. To track the planned
increase of the limit to 50 or to request a limit increase, contact
[Support](/firewall/docs/getting-support).



## May 04, 2026

v1 


Feature 


You can now create and configure the following organization-level Cloud NGFW
resources within a Google Cloud project:

- Security profiles

- Security profile groups

- Firewall endpoints

- Firewall endpoint associations

For more information, see [Security profile
overview](/firewall/docs/about-security-profiles), [Security profile group
overview](/firewall/docs/about-security-profile-groups), and [Firewall endpoint
overview](/firewall/docs/about-firewall-endpoints). This feature is available in **Public preview**.



## March 23, 2026

v1 


Feature 


Secure tags with a `purpose-data` attribute specifying a VPC network or an
organization now support VPC networks that are connected using VPC Network
Peering. For more information, see
[Secure tags for firewalls](/firewall/docs/tags-firewalls-overview).
This feature is available in **General Availability**. 


## February 25, 2026

v1 


Feature 


You can use network contexts to meet your security goals by using fewer
firewall policy rules more efficiently. For more information, see
[Network contexts](/firewall/docs/understand-network-contexts). This feature
is available in **General Availability**.



## February 19, 2026

v1 


Feature 


Cloud NGFW now supports regional system firewall policies. Regional system
firewall policies are read-only policies that internal Google services, such as
Google Kubernetes Engine, use to secure their operations within a VPC network.
For more information, see [Regional system firewall
policies](/firewall/docs/firewall-policies-overview#regional-system-firewall-policies).
This feature is available in **General Availability**.



## November 17, 2025

v1 


Feature 


You can create a Remote Direct Memory Access (RDMA) over converged ethernet (RoCE) Virtual Private Cloud (VPC) network and configure firewall rules that apply to the network. For more information, see [Cloud NGFW for RoCE VPC networks](/firewall/docs/firewall-for-roce). This feature is available in **General Availability**.



## November 13, 2025

v1 


Feature 


You can create a firewall endpoint that supports jumbo frames up to 8,500 bytes in size. For more information, see [Supported packet size](/firewall/docs/about-firewall-endpoints#supported-packet-size). This feature is available in **General Availability**.



## July 25, 2025

v1 


Feature 


You can create a Remote Direct Memory Access (RDMA) over converged ethernet (RoCE) Virtual Private Cloud (VPC) network and configure firewall rules that apply to the network. For more information, see [Cloud NGFW for RoCE VPC networks](/firewall/docs/firewall-for-roce). This feature is available in **Preview**.



## June 23, 2025

v1 


Feature 


You can create a secure tag at the organization level and bind its value to all virtual machine (VM) instances across that organization, instead of applying tags to instances within a specific network. For more information, see [Secure tags for firewalls](/firewall/docs/tags-firewalls-overview). This feature is available in **Preview**.



## April 24, 2025

v1 


Feature 


You can use a single request to batch update all the firewall policy rules for hierarchical and network firewall policies. For more information, see [Overview of batch update to firewall policy rules](/firewall/docs/batch-update-overview). This feature is available in **General Availability**.



## December 13, 2024

v1 


Feature 


You can use network contexts to meet your security goals by using fewer firewall policy rules more efficiently. This feature is available in **Preview**. For more information, see [Network contexts](/firewall/docs/understand-network-contexts).