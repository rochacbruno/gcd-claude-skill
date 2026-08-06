# Compute Engine in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/compute/docs/tpc-differences
Last updated: 2026-08-05

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

Compute

](https://documentation.s3ns.fr/docs/compute-area)






- 








[

Compute Engine

](https://documentation.s3ns.fr/compute/docs)






- 








[

Guides

](https://documentation.s3ns.fr/compute/docs/overview)












# Compute Engine in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Hardware and OS ](#hardware-and-os-differences)
- [ Networking ](#network-differences)
- [ Availability and Disaster Recovery ](#availability-differences)
- [ Cost management ](#cost-management-differences)
- [ Security and access control ](#security-differences)
- [ Workflows and tools ](#workflow-differences)

- [ Recommendations ](#recommendations)
- [ Related guides ](#related-guides)
- 










Compute Engine is a customizable compute service for creating and running
virtual machines. Compute Engine offers scale, performance, and value that
lets you easily move from single virtual machines for experimentation and
development to large compute clusters for production workloads. Because
Cloud de Confiance is optimized for general
purpose compute infrastructure and modest-scale AI/ML workloads, there are some
differences between Compute Engine in
Cloud de Confiance by S3NS and Google Cloud.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Compute Engine.



For more detailed information about Compute Engine, see the
[Compute Engine overview](/compute/docs/overview) and the rest of the
Compute Engine documentation.




You can find recommendations and best practices for using Compute Engine in
Cloud de Confiance, including recommended alternatives where features differ from
Google Cloud, in the [Recommendations](#recommendations) section.




## Key differences



There are some differences between the Cloud de Confiance version of Compute Engine and
the Google Cloud version.
Some notable differences include the following:






- 

Only four machine series are available in
Cloud de Confiance


- 

Hyperdisk Balanced is the only disk type available in
Cloud de Confiance


- 

Image adaptation is the only supported migration path into
Cloud de Confiance





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Compute Engine feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Hardware and OS



| 
**Machine types** | 



Only the following machine series and machine types are available in
Cloud de Confiance:




- [C3](/compute/docs/general-purpose-machines#c3_series)
machine types with up to 176 vCPUs. C3 Bare metal instances aren't
available.

- [M3](/compute/docs/memory-optimized-machines#m3_series)
machine types with up to 128 vCPUs.

- [A3](/compute/docs/accelerator-optimized-machines#a3-vms)
Edge machine type: `a3-edgegpu-8g-nolssd`

- 

[A3](/compute/docs/accelerator-optimized-machines#a3-vms)
High machine types:




- `a3-highgpu-1g-nolssd`

- `a3-highgpu-2g-nolssd`

- `a3-highgpu-4g-nolssd`

- `a3-highgpu-8g-nolssd`







All other machine series, including AMD and Arm-based machine types are
unavailable. For recommendations about how to adapt your machine usage in
Cloud de Confiance, see the
[recommendations section](#recommendations).



The following instance types are available in
Cloud de Confiance:




- [Virtual machine (VM) instances](/compute/docs/instances)


- [Managed and unmanaged
instance groups](/compute/docs/instance-groups)

- [Sole tenant nodes](/compute/docs/nodes/sole-tenant-nodes)





All other instance types are unavailable, including the following:




- Bare metal instances

- Confidential VM instances


| 
|

| 
**GPUs and TPUs** | 



Only the following GPUs are available in
Cloud de Confiance:




- NVIDIA H100 GPUs (`nvidia-h100-80gb`) are available with
the [A3 Edge machine type](/compute/docs/gpus#h100-gpus),
with the following differences:



- Supported machine type: `a3-edgegpu-8g-nolssd`

- Attached Local SSD (Gib): 0. Local SSD isn't supported in
Cloud de Confiance

- Maximum network bandwidth (Gbps): 800




- NVIDIA H100 GPUs (`nvidia-h100-80gb`) are available with
the [A3 High machine type](/compute/docs/gpus#h100-gpus),
with the following differences:



- 

Supported machine types:




- `a3-highgpu-1g-nolssd`

- `a3-highgpu-2g-nolssd`

- `a3-highgpu-4g-nolssd`

- `a3-highgpu-8g-nolssd`




- Attached Local SSD (Gib): 0. Local SSD isn't supported in
Cloud de Confiance








All other GPU machine types are unavailable. TPUs are unavailable.

| 
|

| 
**Disks and encryption** | 



The following disk types are available in
Cloud de Confiance:




- [Hyperdisk Balanced](/compute/docs/disks#hyperdisks)




All other disk types are unavailable. For recommendations about how to
adapt your disk usage in Cloud de Confiance,
see the [recommendations section](#recommendations).




[
Compute Engine automatically encrypts customer content at rest](/compute/docs/disks/disk-encryption). The
following key encryption key (KEK) methods are additionally available in
Cloud de Confiance:




- [Customer-managed
encryption keys (CMEK)](/compute/docs/disks/customer-managed-encryption)




All other KEK encryption methods are unavailable.

| 
|

| 
**Operating system images** | 



The following Linux operating systems are available in
Cloud de Confiance:




- [Debian](/compute/docs/images/os-details#debian)

- [Ubuntu LTS](/compute/docs/images/os-details#ubuntu_lts)

- [Rocky Linux](/compute/docs/images/os-details#rocky_linux)

- [Container-Optimized
OS](/compute/docs/images/os-details#container-optimized_os_cos)




Arm image families are unavailable in
Cloud de Confiance.



If you want to use enterprise operating systems, you must bring your
own licenses (BYOL). You can import BYOL images for Windows, Red Hat
Enterprise Linux (RHEL), and SUSE Linux Enterprise Server (SLES) into
Compute Engine by
[adapting operating systems for
Cloud de Confiance](/compute/docs/import/image-import).
This import process isn't supported for other operating systems.

| 
|

| 
**Operating system details** | 



The following differences apply to
[OS images](/compute/docs/images/os-details) in
Cloud de Confiance:





- Image project:



- Debian: `s3ns-system:debian-cloud`

- Ubuntu LTS: `s3ns-system:ubuntu-os-cloud`

- Rocky Linux: `s3ns-system:rocky-linux-cloud`

- Container-Optimized OS: `s3ns-system:cos-cloud`




- Arm image family: Not supported

- SCSI interfaces: Not supported

- IDPF interfaces: Not supported

- Guest environment: Supported. You are responsible for installation and updates.

- gcloud CLI: Supported. You are responsible for installing and updating.

- OS Login: Not supported

- VM Manager: Not supported

- Import: [Adapting operating
systems for Cloud de Confiance](/compute/docs/import/image-import) is supported

- License: No licenses are required


| 
|


### Networking



| 
**VM networking**
| 


[Zonal DNS names](/compute/docs/networking/zonal-dns) are
available in Cloud de Confiance.



Global DNS names are unavailable.



There is no default network created when you create a project. Some
examples assume that you have a default network. If you need a default
network you can
[manually
create an equivalent auto mode network called `default`](/vpc/docs/create-modify-vpc-networks#create-default-network).



For detailed information about networking differences in
Cloud de Confiance, see the following
documents:




- [VPC in
Cloud de Confiance](/vpc/docs/tpc-differences)

- [Cloud NAT in
Cloud de Confiance](/nat/docs/tpc-differences)

- [Cloud Load Balancing
in Cloud de Confiance](/load-balancing/docs/tpc-differences)

- [Cloud NGFW in
Cloud de Confiance](/firewall/docs/tpc-differences)

- [Network Service Tiers in
Cloud de Confiance](/network-tiers/docs/tpc-differences)

- [Cloud VPN
in Cloud de Confiance](/network-connectivity/docs/vpn/concepts/tpc-differences)


| 
|


### Availability and Disaster Recovery



| 
**Regions and zones** | 



Cloud de Confiance has multiple zones in a
single region. Multi-region features and cross-region failover are not
supported. Deployment across multiple zones for resiliency is supported. We
recommend that you use off-cloud data replication to ensure business continuity
in case of an outage.

| 
|

| 
**Reservations** | 



[On-demand
reservations](/compute/docs/instances/reservations-single-project) are available in
Cloud de Confiance.



Future reservations are not available.

| 
|


### Cost management



| 
**Cost saving features**
| 



[Spot VMs](/compute/docs/instances/spot) are available
for all machine series (C3, M3, and A3) in
Cloud de Confiance at discounts up to 60%
off the on-demand price. Spot VMs pricing is updated
quarterly. For the latest prices, see the
[pricing page](https://documentation.s3ns.fr/spot-vms/pricing).




Preemptible VMs, which are the legacy version of Spot VMs,
aren't available in Cloud de Confiance.




Cloud de Confiance by S3NS offers compute flexible
committed use discounts (CUDs) for eligible spend across
Compute Engine, GKE, and Cloud Run.
To purchase spend-based commitments, contact
[
Cloud de Confiance by S3NS billing support](https://support.s3ns.fr/).
For more information, see the
[billing differences page](/billing/docs/tpc-differences).




All other cost-savings features aren't available in
Cloud de Confiance, including
resource-based CUDs and sustained use discounts (SUDs).


| 
|


### Security and access control



| 
**VM security features**
| 


The following VM security features are available in
Cloud de Confiance:




- [VPC Service Controls](/compute/docs/instances/protecting-resources-vpc-service-controls)

- [Shielded VMs](/compute/docs/about-shielded-vm)




All other security features are unavailable, including the following:



- Confidential VMs

| 
|


### Workflows and tools



| 
**VM creation** | 



The following VM creation options are unavailable in
Cloud de Confiance:




- Bulk VM creation


| 
|

| 
**Migration** | 


[Image adaptation](/compute/docs/import/image-import) is
available in Cloud de Confiance.



All other migration options are unavailable.

| 
|

| 
**Backup and restoration** | 



The following backup options are available in
Cloud de Confiance:




- [Snapshots](/compute/docs/disks/snapshots)

- [Clones](/compute/docs/disks/clone-duplicate-disks)




All other backup and restoration options are unavailable.

| 
|

| 
**VM and user management** | 



The following VM and user management options are unavailable in
Cloud de Confiance:




- VM Manager

- OS Login

- Interactive serial console access

- Identity-Aware Proxy (IAP) TCP forwarding


| 
|




## Recommendations




- Machine type recommendations:



- 


If you need small machine types like N2, we recommend that you use C3
in Cloud de Confiance. C3 instances have
more powerful CPUs than N2 instances, so you might be able to use fewer
instances to achieve equivalent or better performance.



- 


If you need large amounts of memory, we recommend that you use M3.



- 


If you need to use GPUs to accelerate your computations, we
recommend that you use A3 High or A3 Edge. Consider doing CPU
inferencing if A3 High or A3 Edge is too large for your workload.






- Disk recommendations:



- 


Hyperdisk Balanced is the recommended block storage option for
Compute Engine and the only block storage option in
Cloud de Confiance by S3NS. If you use balanced
Persistent Disk in Google Cloud, we recommend that you use
Google Cloud Hyperdisk in Cloud de Confiance by S3NS and
Google Cloud alike.










## Related guides



The following information might also affect how you use and design for Compute Engine
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products





- 
[VPC documentation](/vpc/docs)


- 
[Logging documentation](/logging/docs)


- 
[Monitoring documentation](/monitoring/docs)




### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)