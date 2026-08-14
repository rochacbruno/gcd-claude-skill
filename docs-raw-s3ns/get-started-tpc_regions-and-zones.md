# Regions and zones in Cloud de Confiance

Source: https://documentation.s3ns.fr/docs/get-started-tpc/regions-and-zones
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

Get started

](https://documentation.s3ns.fr/docs/get-started)












# Regions and zones in Cloud de Confiance 






- On this page 
- [ Regions ](#regions_and_zones)
- [ Zones ](#zones)
- [ Regional and zonal resources ](#regional_resources)
- [ Handling failures ](#application_deployment_considerations)
- [ What's next ](#whats_next)
- 









In both Google Cloud and
Cloud de Confiance by S3NS, regions and zones are logical
abstractions of the underlying physical machines that power each cloud.
*Regions* are independent geographic areas that consist of *zones*, a
deployment area for cloud resources.
Cloud de Confiance by S3NS has a single region, with multiple
zones into which you can deploy your resources.

This page provides a brief overview of region and zone considerations when
designing and running applications in
Cloud de Confiance by S3NS.

## Regions 

Cloud de Confiance helps ensure data sovereignty
by operating as a single, completely standalone *region*,
`u-france-east1`.

Features that rely on the existence of multiple regions—such as load
balancing across regions, or multi-region storage—are unavailable
Cloud de Confiance.

## Zones

A region is logically divided into *zones*. Zones have high-bandwidth,
low-latency network connections to other zones in the same region. The
`u-france-east1` region has three
zones:
`u-france-east1-a`,
`u-france-east1-b`, and
`u-france-east1-c`.

Each zone should be considered a single failure domain. To deploy fault-tolerant
applications with high availability and help protect against unexpected
infrastructure, hardware, and software failures in
Cloud de Confiance, deploy your applications
across multiple zones.

## Regional and zonal resources

Resources that live in a zone, such as Compute Engine virtual machine (VM)
instances or zonal disks, are referred to as *zonal resources*. Other resources,
like static external IP addresses, are *regional resources*.

Regional resources can be used by any resource in
Cloud de Confiance, regardless of zone, while
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
Cloud de Confiance typically monitor and manage
resource distribution across zones for you.

## What's next

- [Get started with Cloud de Confiance](/docs/get-started-tpc).