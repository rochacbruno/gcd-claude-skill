# Regions and zones in Google Cloud Dedicated

Source: https://berlin.devsitetest.how/docs/get-started-tpc/regions-and-zones
Last updated: 2026-07-17

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

Get started

](https://berlin.devsitetest.how/docs/get-started)












# Regions and zones in Google Cloud Dedicated 






- On this page 
- [ Regions ](#regions_and_zones)
- [ Zones ](#zones)
- [ Regional and zonal resources ](#regional_resources)
- [ Handling failures ](#application_deployment_considerations)
- [ What's next ](#whats_next)
- 









In both Google Cloud and
Google Cloud Dedicated in Germany, regions and zones are logical
abstractions of the underlying physical machines that power each cloud.
*Regions* are independent geographic areas that consist of *zones*, a
deployment area for cloud resources.
Google Cloud Dedicated in Germany has a single region, with multiple
zones into which you can deploy your resources.

This page provides a brief overview of region and zone considerations when
designing and running applications in
Google Cloud Dedicated in Germany.

## Regions 

Google Cloud Dedicated helps ensure data sovereignty
by operating as a single, completely standalone *region*,
`u-germany-northeast1`.

Features that rely on the existence of multiple regions—such as load
balancing across regions, or multi-region storage—are unavailable
Google Cloud Dedicated.

## Zones

A region is logically divided into *zones*. Zones have high-bandwidth,
low-latency network connections to other zones in the same region. The
`u-germany-northeast1` region has three
zones:
`u-germany-northeast1-a`,
`u-germany-northeast1-b`, and
`u-germany-northeast1-c`.

Each zone should be considered a single failure domain. To deploy fault-tolerant
applications with high availability and help protect against unexpected
infrastructure, hardware, and software failures in
Google Cloud Dedicated, deploy your applications
across multiple zones.

## Regional and zonal resources

Resources that live in a zone, such as Compute Engine virtual machine (VM)
instances or zonal disks, are referred to as *zonal resources*. Other resources,
like static external IP addresses, are *regional resources*.

Regional resources can be used by any resource in
Google Cloud Dedicated, regardless of zone, while
zonal resources can only be used by other resources in the same zone. For
example, to attach a zonal persistent disk to a VM instance, both resources must
be in the same zone. If you want to assign a static IP address to a VM, the VM
can run in any zone.

## Handling failures

Zones are designed to minimize the risk of correlated failures caused by
physical infrastructure outages in physical infrastructure like power, cooling,
or networking. At some point, however, your instances might experience an
unexpected failure.

To help ensure your applications can tolerate outages, distribute your resources
across multiple zones. Thus, if a zone becomes unavailable, you can transfer
traffic to another zone to keep your services running. Managed services in
Google Cloud Dedicated typically monitor and manage
resource distribution across zones for you.

## What's next

- [Get started with Google Cloud Dedicated](/docs/get-started-tpc).