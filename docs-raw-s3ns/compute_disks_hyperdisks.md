# Google Cloud Hyperdisk overview

Source: https://documentation.s3ns.fr/compute/docs/disks/hyperdisks
Last updated: 2026-08-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/compute/docs/tpc-differences) for more details.














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












# Google Cloud Hyperdisk overview 






- On this page ** 
- [ Hyperdisk features ](#hyperdisk-features)
- [ Choose a Hyperdisk type for your workload ](#when-to-use)
- [ Hyperdisk size limits ](#size-limits)
- [ Hyperdisk performance ](#hd-performance-limits)

- [ Latency ](#latency)

- [ Torn write protection ](#torn-write-protection)

- [ Benefits of torn write protection ](#torn-write-benefits)

- [ Machine series support for Hyperdisk ](#machine-type-support)

- [ Design for flexibility on older machine series ](#gen2-hyperdisk_name_short)
- [ Restrictions for machine series support ](#machine_type_restrictions)

- [ Regional availability for Hyperdisk ](#hyperdisk_regions)
- [ When to use Hyperdisk pools with your workload ](#storage_pools)
- [ Share Hyperdisk volumes between instances ](#share-disks)
- [ High availability and disaster recovery protection for Hyperdisk volumes ](#hd-dr)

- [ Cross-zonal synchronous replication ](#hd-sync-rep)
- [ Cross-regional asynchronous replication ](#hd-async-rep)

- [ Encryption for Hyperdisk volumes ](#hd-encryption)

- [ Confidential Computing with Hyperdisk volumes ](#confidential-hd)

- [ Durability of Hyperdisk ](#durability_hyperdisks)
- [ Supported disk interfaces ](#supported_disk_interfaces)
- [ Pricing ](#pricing)

- [ Hyperdisk and committed use discounts ](#hyperdisk_cud)
- [ Hyperdisk and preemptible VM instances ](#hyperdisk_preemptible_instances)

- [ Limitations for Hyperdisk ](#limitations)
- [ What's next? ](#whats_next)
- 






















This document describes the features of Google Cloud Hyperdisk.
Hyperdisk is the fastest and most efficient durable disk for
Compute Engine. If you need boot or data disks for your compute
instances—virtual machine (VM) instances, containers, and bare metal
instances—then Google recommends using Hyperdisk.

For information about the other block storage options in
Compute Engine, see [Choose a disk type](/compute/docs/disks).

To create a new Hyperdisk volume, see
[Create a Hyperdisk volume](/compute/docs/disks/add-hyperdisk).

## Hyperdisk features 

With Hyperdisk you can provision, manage, and scale your
Compute Engine workloads without the cost and complexity of a typical
on-premises storage area network (SAN).

Hyperdisk volumes have the following features:

- 

**Function as physical disks**: you can use a Hyperdisk
volume with a compute instance as if it were a physical disk attached to the
instance. When you read to or write from a Hyperdisk volume,
data is transmitted over the network.

- 

**Higher performance**: Hyperdisk offers higher IOPS and
throughput than Persistent Disk by leveraging Google's Titanium
storage offload technology.

- 

**Customizable performance**: you can choose the performance—IOPS or
throughput—of each Hyperdisk volume. You can also
increase or decrease a Hyperdisk volume's performance while
it's in use.

- 

**Support for high availability**: in the unlikely event of a zonal or
regional outage, you can ensure high availability for your data by enabling
one or both of the following features:

- 

To protect your data in case of a zonal outage, use
[Hyperdisk Balanced High Availability](/compute/docs/disks/about-regional-persistent-disk).
Data on Hyperdisk Balanced High Availability volumes is synchronously replicated across two zones
within the same region to protect against up to one zonal outage.

- 

To protect your data from a regional outage, maintain a replica of your
data in another region by using
[Asynchronous Replication](/compute/docs/disks/async-pd/about).
When you enable Asynchronous Replication for a disk, data in one region is
continuously copied to a replica in a secondary region. If a regional
outage occurs, you can [failover](/compute/docs/disks/async-pd/failover-failback)
your data to a secondary region. Asynchronous Replication is available for
Hyperdisk Balanced, Hyperdisk Balanced High Availability, and Hyperdisk Extreme volumes.

- 

**Portability**: you can change the compute instance that a
Hyperdisk volume is attached to.

- 

**Shareable between VMs**: for high availability workloads, certain
Hyperdisk types can be shared by multiple VMs. Each VM has
simultaneous read-write or read-only access to the volume.

- 

**Support for pooled capacity and performance**: to simplify planning,
avoid overprovisioning storage, and reduce costs, you can purchase
Hyperdisk storage and performance in bulk by using
Hyperdisk Storage Pools.

- 

**Torn write protection**: Hyperdisk offers built-in protection
against torn writes, which prevents data corruption if a write operation is
interrupted by events like a power failure or system crash.
For more information, see [Torn write protection](#torn-write-protection).





## Choose a Hyperdisk type for your workload

To add Hyperdisk volumes to your workloads, you must choose a
Hyperdisk type. Each Hyperdisk type is designed
and optimized for a specific type of workload.
The following is a list of the available Hyperdisk types.

- Hyperdisk Balanced

- Hyperdisk Balanced High Availability

- Hyperdisk Extreme

- Hyperdisk Throughput

- Hyperdisk ML

For most workloads, we recommend Hyperdisk Balanced.

To select a Hyperdisk type, compare your workload's type and its
performance requirements with the information in the following table. For
detailed information about a specific Hyperdisk type, see the
linked page in the **Recommended Hyperdisk type** column.

In the following table, **IOPS** (input/output operations per second)
indicates the number of read and write operations that the volume can
perform per second. **Throughput** indicates the amount of data that
can be read from or written to the volume per second.




| 
Workload type | 
Recommended
Hyperdisk type | 
Unique features | 
Max IOPS and throughput per volume | 
|



| 




- Most enterprise applications

- Boot disks

- Virtual desktops

- Postgres, MySQL


| 
[Hyperdisk Balanced](/compute/docs/disks/hd-types/hyperdisk-balanced) | 




- Designed to be the best fit for the majority of workloads

- Best combination of price and performance

- Supports simultaneous read-write access to the same volume from up to
8 instances


| 

**IOPS**: 160,000

**Throughput**: 2,400 MiB/s
| 
|

| 




- Highly-available, mission-critical applications that require a
[recovery
point objective](/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) of 0


| 
[Hyperdisk Balanced High Availability](/compute/docs/disks/hd-types/hyperdisk-balanced-ha) | 




- Offers data replication in two zones within the same region for
quick failover

- Supports simultaneous read-write access to the same volume from up to
8 instances


| 

**IOPS**: 100,000

**Throughput**: 2,400 MiB/s
| 
|

| 




- SAP HANA

- High-end SQL Server, Oracle, and in-memory RDBMS


| 
[Hyperdisk Extreme](/compute/docs/disks/hd-types/hyperdisk-extreme) | 


- Offers the highest IOPS
| 

**IOPS**: 350,000

**Throughput**: 5,000 MiB/s 1 
| 
|

| 




- High-performance computing (HPC)

- Machine learning, AI inference or training

- Accelerator-optimized workloads


| 
[Hyperdisk ML](/compute/docs/disks/hd-types/hyperdisk-ml) | 




- Supports attaching a single volume in read-only mode to up to
2,500 instances.

- Offers the highest read-only throughput


| 

**IOPS**: 33,554,432 2 

**Throughput**: 2,097,152 MiB/s
| 
|

| 




- Scale out analytics workloads like Hadoop, Spark, and Kafka

- Cold disks


| 
[Hyperdisk Throughput](/compute/docs/disks/hd-types/hyperdisk-throughput) | 




- High throughput for bandwidth and capacity-intensive applications that
don't need high IOPS

- Cost-effective data disks for cost-sensitive applications


| 
**IOPS**: 9,600 2 

**Throughput**: 2,400 MiB/s | 
|




1 You can't specify a throughput level for Hyperdisk Extreme
volumes. The provisioned throughput is based on the IOPS level you specify.

2 You can't specify an IOPS level for Hyperdisk Throughput and
Hyperdisk ML volumes. The provisioned IOPS is based on the throughput level you
specify.


## Hyperdisk size limits

The following table lists the size limits for each Hyperdisk
type.





| 
Disk type | 


Minimum size | 
Maximum size | 
Default size | 

|





| 
Hyperdisk Balanced | 


4 GiB | 
64 TiB 1 | 
100 GiB | 

|


| 
Hyperdisk Balanced High Availability | 


4 GiB | 
64 TiB | 
100 GiB | 

|


| 
Hyperdisk Extreme | 


64 GiB | 
64 TiB | 
1 TiB | 

|

| 
Hyperdisk Throughput | 


2 TiB | 
32 TiB | 
2 TiB | 

|

| 
Hyperdisk ML | 


4 GiB | 
64 TiB | 
100 GiB | 

|







1 
[Preview](https://documentation.s3ns.fr/products#product-launch-stages)**:
C4 supports a maximum disk size of 128 TiB. For access to
this feature, contact
[hyperdisk-questions@google.com](https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=hyperdisk-questions@google.com).


## Hyperdisk performance

The following is a summary of key Hyperdisk performance concepts:

- You can configure the performance (IOPS and/or throughput) limit and size of
each Hyperdisk volume. You can also increase or decrease a
Hyperdisk volume's performance without changing its size.

- The performance limit you specify is referred to as the
*provisioned performance*. The provisioned performance isn't the expected
performance, rather, it's the maximum performance the disk can achieve.

- The actual performance for a Hyperdisk volume is the observed
performance while the volume is in use.

- For a Hyperdisk volume to reach its provisioned performance,
you must attach it to a compute instance that supports the same level
of performance or higher.





For a discussion of how Hyperdisk performance works, see
[About Hyperdisk performance](/compute/docs/disks/hyperdisk-performance).


For performance limits for each Hyperdisk type, see
[Hyperdisk performance limits](/compute/docs/disks/hyperdisk-perf-limits).

### Latency

Each Hyperdisk type has different latency profiles. Google
recommends comparing Hyperdisk Throughput to the latency of a hard disk drive. You can
compare the latency for Hyperdisk Balanced, Hyperdisk Balanced High Availability, Hyperdisk Extreme, and Hyperdisk ML to the
latency of enterprise SSDs.

Hyperdisk Balanced and Hyperdisk Extreme offer sub-millisecond latency.

## Torn write protection

A *torn write* is a type of corruption that occurs when a single write operation
that covers multiple blocks is interrupted. These interruptions often happen
due to events like a system crash or power failure. When write operations cover
multiple blocks, physical disks typically process these writes in a non-atomic
fashion. An interruption means that only a subset of the data blocks are
written to the disk. The resulting mix of old and new data can compromise data
integrity.

Google Cloud Hyperdisk offers built-in *torn write protection*. All
Hyperdisk types support an atomic write unit of 128 KB and
an atomic write boundary of 1 MB. When you write to a
Hyperdisk volume, writes up to 128 KB are atomic as long as
they don't cross any offset on the disk that is a multiple of 1 MB.
This atomicity ensures that multi-block write operations result in one of the
following outcomes:

- **No interruption**: All blocks are successfully written to the disk.

- **Interruption**: No changes are made and your existing data is preserved.

### Benefits of torn write protection

Some relational databases protect against torn writes by using a doublewrite
buffer. Examples of doublewrite buffers include the InnoDB and XtraDB storage
engines of MySQL and MariaDB. However, the use of a doublewrite buffer
causes these workloads to issue more I/O operations to the disk, which reduces
database write performance. Other storage workloads also use similar mechanisms
to protect themselves against torn writes.

Because Google Cloud Hyperdisk provides built-in torn write protection, you can
disable database-level protection features to reduce I/O overhead. As a result,
you can increase database write throughput by up to 25%.

To use built-in torn write protection, you must configure your operating
system, file system, and databases correctly. For more information, see
[Environment configuration requirements](/compute/docs/disks/optimize-hyperdisk#torn-write-requirements).

## Machine series support for Hyperdisk

This section lists the [machine series](/compute/docs/machine-resource#vm_terminology)
that each Hyperdisk type supports.
If a machine series doesn't support Hyperdisk, use Persistent Disk.

Select one or more machine series to see the supported Hyperdisk types.








[A2](/compute/docs/accelerator-optimized-machines#a2-vms) 
[A3 (H100)](/compute/docs/gpus#h100-gpus) 
[A3 (H200)](/compute/docs/gpus#h200-gpus) 
[A4](/compute/docs/accelerator-optimized-machines#a4-vms) 
[A4X](/compute/docs/accelerator-optimized-machines#a4x-vms) 
[A4X Max](/compute/docs/accelerator-optimized-machines#a4x-vms) 
[C2](/compute/docs/compute-optimized-machines#c2_machine_types) 
[C2D](/compute/docs/compute-optimized-machines#c2d_machine_types) 
[C3](/compute/docs/general-purpose-machines#c3_series) 
[C3D](/compute/docs/general-purpose-machines#c3d_machine_types) 
[C4](/compute/docs/general-purpose-machines#c4_series) 
[C4A](/compute/docs/general-purpose-machines#c4a_series) 
[C4D](/compute/docs/general-purpose-machines#c4d_series) 
[C4N](/compute/docs/network-optimized-machines#c4n_series) 
[E2](/compute/docs/general-purpose-machines#e2_machine_types) 
[G2](/compute/docs/accelerator-optimized-machines#g2-vms) 
[G4](/compute/docs/accelerator-optimized-machines#g4-series) 
[H3](/compute/docs/compute-optimized-machines#h3_series) 
[H4D](/compute/docs/compute-optimized-machines#h4d_series) 
[M1](/compute/docs/memory-optimized-machines#m1_machine_types) 
[M2](/compute/docs/memory-optimized-machines#m2_machine_types) 
[M3](/compute/docs/memory-optimized-machines#m3_machine_types) 
[M4](/compute/docs/memory-optimized-machines#m4_machine_types) 
[M4N](/compute/docs/network-optimized-machines#m4n_series) 
[N1](/compute/docs/general-purpose-machines#n1_machines) 
[N1+GPU](/compute/docs/gpus) 
[N2](/compute/docs/general-purpose-machines#n2_series) 
[N2D](/compute/docs/general-purpose-machines#n2d_machines) 
[N4](/compute/docs/general-purpose-machines#n4_series) 
[N4A](/compute/docs/general-purpose-machines#n4a_series) 
[N4D](/compute/docs/general-purpose-machines#n4d_series) 
[T2A](/compute/docs/general-purpose-machines#t2a_machines) 
[T2D](/compute/docs/general-purpose-machines#t2d_machines) 
[TPU v2](/tpu/docs/v2) 
[TPU v3](/tpu/docs/v3) 
[TPU v4](/tpu/docs/v4) 
[TPU v5e](/tpu/docs/v5e) 
[TPU v5p](/tpu/docs/v5p) 
[TPU v6e](/tpu/docs/v6e) 
[TPU7x](/tpu/docs/tpu7x) 
[X4](/compute/docs/memory-optimized-machines#x4_series) 
[Z3](/compute/docs/storage-optimized-machines#z3_series) 
Select one or more options ** Choose a machine series 

- A2
- A3 (H100)
- A3 (H200)
- A4
- A4X
- A4X Max
- C2
- C2D
- C3
- C3D
- C4
- C4A
- C4D
- C4N
- E2
- G2
- G4
- H3
- H4D
- M1
- M2
- M3
- M4
- M4N
- N1
- N1+GPU
- N2
- N2D
- N4
- N4A
- N4D
- T2A
- T2D
- TPU v2
- TPU v3
- TPU v4
- TPU v5e
- TPU v5p
- TPU v6e
- TPU7x
- X4
- Z3





Clear all 









| 
Machine series | 
Hyperdisk Balanced | 
Hyperdisk Balanced HA | 
Hyperdisk Extreme | 
Hyperdisk Throughput | 
Hyperdisk ML | 
|










| 
[A2](/compute/docs/accelerator-optimized-machines#a2-vms) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 


| 
|
| 
[A3 (H100)](/compute/docs/gpus#h100-gpus) | 


| 


| 


| 


| 


| 
|
| 
[A3 (H200)](/compute/docs/gpus#h200-gpus) | 


| 


| 


| 

**—** 
| 


| 
|
| 
[A4](/compute/docs/accelerator-optimized-machines#a4-vms) | 


| 

**—** 
| 


| 

**—** 
| 


| 
|
| 
[A4X](/compute/docs/accelerator-optimized-machines#a4x-vms) | 


| 

**—** 
| 


| 

**—** 
| 


| 
|
| 
[A4X Max](/compute/docs/accelerator-optimized-machines#a4x-vms) | 


| 

**—** 
| 


| 


| 


| 
|
| 
[C2](/compute/docs/compute-optimized-machines#c2_machine_types) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[C2D](/compute/docs/compute-optimized-machines#c2d_machine_types) | 

** 1 **
| 

** 1 **
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[C3](/compute/docs/general-purpose-machines#c3_series) | 


| 


| 


| 


| 


| 
|
| 
[C3D](/compute/docs/general-purpose-machines#c3d_machine_types) | 


| 


| 


| 


| 


| 
|
| 
[C4](/compute/docs/general-purpose-machines#c4_series) | 


| 


| 


| 


| 


| 
|
| 
[C4A](/compute/docs/general-purpose-machines#c4a_series) | 


| 


| 


| 


| 


| 
|
| 
[C4D](/compute/docs/general-purpose-machines#c4d_series) | 


| 


| 


| 

**—** 
| 


| 
|
| 
[C4N](/compute/docs/network-optimized-machines#c4n_series) | 


| 


| 


| 


| 


| 
|
| 
[E2](/compute/docs/general-purpose-machines#e2_machine_types) | 

** 1 **
| 

** 1 **
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[G2](/compute/docs/accelerator-optimized-machines#g2-vms) | 

**—** 
| 

**—** 
| 

**—** 
| 


| 


| 
|
| 
[G4](/compute/docs/accelerator-optimized-machines#g4-series) | 


| 


| 


| 


| 


| 
|
| 
[H3](/compute/docs/compute-optimized-machines#h3_series) | 


| 

**—** 
| 

**—** 
| 


| 

**—** 
| 
|
| 
[H4D](/compute/docs/compute-optimized-machines#h4d_series) | 


| 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[M1](/compute/docs/memory-optimized-machines#m1_machine_types) | 


| 

**—** 
| 


| 

**—** 
| 

**—** 
| 
|
| 
[M2](/compute/docs/memory-optimized-machines#m2_machine_types) | 


| 

**—** 
| 


| 

**—** 
| 

**—** 
| 
|
| 
[M3](/compute/docs/memory-optimized-machines#m3_machine_types) | 


| 


| 


| 


| 

**—** 
| 
|
| 
[M4](/compute/docs/memory-optimized-machines#m4_machine_types) | 


| 

**—** 
| 


| 

**—** 
| 

**—** 
| 
|
| 
[M4N](/compute/docs/network-optimized-machines#m4n_series) | 


| 


| 


| 


| 


| 
|
| 
[N1](/compute/docs/general-purpose-machines#n1_machines) | 

** 1 **
| 

** 1 **
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[N1+GPU](/compute/docs/gpus) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[N2](/compute/docs/general-purpose-machines#n2_series) | 

** 1 **
| 

** 1 **
| 


| 


| 

**—** 
| 
|
| 
[N2D](/compute/docs/general-purpose-machines#n2d_machines) | 

** 1 **
| 

** 1 **
| 

**—** 
| 


| 

**—** 
| 
|
| 
[N4](/compute/docs/general-purpose-machines#n4_series) | 


| 


| 

**—** 
| 


| 


| 
|
| 
[N4A](/compute/docs/general-purpose-machines#n4a_series) | 


| 


| 

**—** 
| 


| 


| 
|
| 
[N4D](/compute/docs/general-purpose-machines#n4d_series) | 


| 


| 

**—** 
| 


| 


| 
|
| 
[T2A](/compute/docs/general-purpose-machines#t2a_machines) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[T2D](/compute/docs/general-purpose-machines#t2d_machines) | 

**—** 
| 

**—** 
| 

**—** 
| 


| 

**—** 
| 
|
| 
[TPU v2](/tpu/docs/v2) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[TPU v3](/tpu/docs/v3) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[TPU v4](/tpu/docs/v4) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 
|
| 
[TPU v5e](/tpu/docs/v5e) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 


| 
|
| 
[TPU v5p](/tpu/docs/v5p) | 

**—** 
| 

**—** 
| 

**—** 
| 

**—** 
| 


| 
|
| 
[TPU v6e](/tpu/docs/v6e) | 


| 

**—** 
| 

**—** 
| 

**—** 
| 


| 
|
| 
[TPU7x](/tpu/docs/tpu7x) | 


| 

**—** 
| 

**—** 
| 

**—** 
| 


| 
|
| 
[X4](/compute/docs/memory-optimized-machines#x4_series) | 


| 

**—** 
| 


| 

**—** 
| 

**—** 
| 
|
| 
[Z3](/compute/docs/storage-optimized-machines#z3_series) | 


| 


| 


| 


| 

**—** 
| 
| 


1 To design your workload for flexibility
and use Hyperdisk Balanced or Hyperdisk Balanced High Availability with this machine series,
[contact your account team](/tam).



### Design for flexibility on older machine series

Hyperdisk Balanced and Hyperdisk Balanced High Availability are also available with select previous generation
machine families to help you design for flexibility across multiple generations.

- 

Hyperdisk Balanced and Hyperdisk Balanced High Availability on previous generations are intended for long-term
disks that will survive beyond the duration of the instance.

- 

For use-cases in which the life of the disk coincides with the life of the
instance, for example a boot disk, use the block storage defaults: Persistent Disk
with 1st- and 2nd-generation machine series, and Hyperdisk with
more recent generation instances. For example, if you need a boot disk with an
N2 instance, then you should use a Balanced or SSD Persistent Disk volume instead of
a Hyperdisk volume.

To use Hyperdisk with these machine series, [contact your account team](/tam).

### Restrictions for machine series support

This section lists the restrictions that apply to the machine series
that each Hyperdisk type supports.


- For Hyperdisk Extreme, the following restrictions apply:



- A3 machine types require at least 104 vCPUs so `a3-highgpu-1g` and
`a3-highgpu-2g` aren't supported.

- C3 machine type require at least 88 vCPUs.

- C3D machine types require at least 60 vCPUs.

- C4 and G4 machine types require at least 96 vCPUs.

- M1 machine types require at least 80 vCPUs.

- C4A, C4D, M3, and M4 machine types require at least 64 vCPUs.

- N2 machine types require at least 80 vCPUs; Custom N2 machine types aren't
supported



- For Hyperdisk Throughput, the following restrictions apply:



- You can't use Hyperdisk Throughput on bare metal instances with the exception of
A4X Max bare metal instances.

- Additional limitations apply to attaching Hyperdisk Throughput volumes to certain machine series,
including C4, C4A, and N4. For more information, see
[
Limitations for attaching Hyperdisk Throughput volumes to 4th-generation instances](/compute/docs/disks/hd-types/hyperdisk-throughput#gen4-vm-issues).





- To use Hyperdisk Balanced and Hyperdisk Balanced High Availability with the following machine series, you must
[contact your account team](/tam):



- C2D

- E2

- N1

- N2

- N2D




## Regional availability for Hyperdisk

Some Hyperdisk types are available in all
[regions and zones](/docs/geography-and-regions), while
others are available only in specific locations. The following table summarizes
regional availability for each Hyperdisk type.




| 
Hyperdisk type | 
Supported regions | 
|



| 
Hyperdisk Balanced | 
Available in all zones and regions | 
|

| 
Hyperdisk Balanced High Availability | 
Available in all zones and regions except for [AI zones](/compute/docs/regions-zones/ai-zones) | 
|

| 
Hyperdisk Extreme | 
Available in all zones and regions | 
|

| 
Hyperdisk ML | 
Available in all zones and regions | 
|

| 
Hyperdisk Throughput | 
Available in all zones and regions | 
|



## When to use Hyperdisk pools with your workload

You can simplify disk management and reduce costs with
Hyperdisk pools. Hyperdisk pools let you purchase
capacity and performance in bulk instead of for individual disks. You can then
create disks in the pool to consume the purchased resources.
Disks that are in a pool can be used as boot disks and data
disks for your instances and containers.

Hyperdisk pools are designed to also provide predictable performance
for workloads that have high peak capacity and performance needs. If a project's
disks have high concurrent or provisioned capacity, IOPS, or throughput usage in
one zone, Google recommends using Hyperdisk pools to manage the
project's disks.

As a general guideline, if your workload has one or more of the following
requirements within a single project and zone, you should use
Hyperdisk pools for your workload:




| 
Workload type | 
Thresholds for using Hyperdisk pools | 
Recommended pool type | 
|



| 



Accelerator (GPU / TPU) instances with attached boot and scratch disks



Parallel file systems like HDFS or Lustre with high concurrent usage

| 




- 1 PiB or more of provisioned capacity per zone

- 1 TiB/s or more of provisioned throughput performance

- 10 million (10,000,000) or more provisioned IOPS


| 




- Hyperdisk Exapools

- Hyperdisk Storage Pools


| 
|

| 



Large enterprise workloads such as enterprise apps, DBMS, or line
of business apps



AI/ML and HPC simulation workloads

| 




- 20 TiB or more of provisioned capacity per zone


| 




- Hyperdisk Storage Pools


| 
|



The following are examples of workloads that are suitable for
Hyperdisk pools:


- 

Example workloads for Hyperdisk Exapools**:


- AI/ML workloads spanning 4,000 TPU VMs and using 2 PiB of Hyperdisk Balanced with provisioned
performance of 20,000,000 IOPS and 3 TiB/s throughput, driving concurrent aggregate
peak throughput of 500 GiB/s.

- AI/ML training workloads with 15,000 GPU instances using Hyperdisk Balanced for boot and scratch
disks with a total capacity of 8 PiB, driving a concurrent aggregate peak throughput of
1 TiB/s.

- Parallel file system with 6 PiB or more of capacity and concurrent aggregate peaks
of 800 GiB/s of read heavy throughput.


- 

Example workloads for **Hyperdisk Storage Pools**:


- AI/ML and HPC simulation workloads with 1,000 GPU instances using Hyperdisk Balanced volumes in
conjunction with Local SSD as shared cache.

- Workload spread across several databases and applications, with 100 TiB of provisioned
capacity across multiple volumes used by both databases and applications.

You can use Hyperdisk Balanced or Hyperdisk Throughput volumes with Hyperdisk pools.
For more information about pools, see
[About Hyperdisk pools](/compute/docs/disks/pools).

## Share Hyperdisk volumes between instances

You can share a Hyperdisk volume between multiple instances by
simultaneously attaching the same volume to multiple instances.

The following scenarios are supported:

- 

Concurrent read-write access to a single volume from multiple instances.
Recommended for clustered file systems and highly available workloads like
SQL Server Failover Cluster Infrastructure. Supported for the following
Hyperdisk types:

- Hyperdisk Balanced

- Hyperdisk Extreme

- Hyperdisk Balanced High Availability

- 

Concurrent read-only access to a single volume from multiple instances.
This is more cost effective than having multiple disks with the same data.
Recommended for accelerator-optimized machine learning workloads.
Supported for Hyperdisk ML volumes.

To learn about disk sharing, see
[Share a disk between instances](/compute/docs/disks/sharing-disks-between-vms).

## High availability and disaster recovery protection for Hyperdisk volumes

You can protect your data in the rare event of a zonal or regional outage by
enabling replication, that is, maintaining a copy of the data in another zone or
region.

### Cross-zonal synchronous replication

To replicate data to another zone within the same region, you must use Hyperdisk Balanced High Availability
volumes. Hyperdisk Balanced High Availability is the only supported Hyperdisk type for
zonal replication.

For more information, see
[About synchronous disk replication](/compute/docs/disks/about-regional-persistent-disk).

### Cross-regional asynchronous replication

You can protect your data in the unlikely
event of a regional outage by enabling Asynchronous Replication. Asynchronous Replication maintains a copy of
the data on your volume in another region. For example, to protect a
Hyperdisk volume in `us-west1`,
you can use Asynchronous Replication to replicate the volume to a secondary volume in
the `us-east4` region. If the volume in `us-west1`
became unavailable, then you could use the secondary volume in `us-east4`.

You can use Asynchronous Replication with the following Hyperdisk types:

- Hyperdisk Balanced

- Hyperdisk Extreme

- Hyperdisk Balanced High Availability

To learn more about cross-regional replication, see [Asynchronous Replication](/compute/docs/disks/async-pd/about).

## Encryption for Hyperdisk volumes

By default, Compute Engine protects your Hyperdisk volumes with
Google Cloud-powered encryption keys. You can also encrypt your
Hyperdisk volumes with customer-managed encryption keys (CMEK).

For more information, see [About disk encryption](/compute/docs/disks/disk-encryption).

### Confidential Computing with Hyperdisk volumes

You can add hardware-based encryption to a Hyperdisk Balanced disk by enabling
Confidential mode for the disk when you create it.
You can use Confidential mode only with Hyperdisk Balanced disks that are attached to
Confidential VMs.

For more information, see [Confidential mode for Hyperdisk Balanced volumes](/compute/docs/disks/disk-encryption#conf_hdb).

## Durability of Hyperdisk

Compute Engine distributes the data on Hyperdisk volumes
across several physical disks to ensure durability and optimize performance.

Disk durability represents the probability of data loss, by design, for a
typical disk in a typical year. Hyperdisk data loss events are
extremely rare and have historically been the result of coordinated hardware
failures, software bugs, or a combination of the two. Google takes many steps to
mitigate the industry-wide risk of silent data corruption.

Durability is calculated with a set of assumptions about hardware failures,
the likelihood of catastrophic events, isolation practices and engineering
processes in Google data centers, and the internal encodings used by each disk
type.

Human error by a Google Cloud customer, such as when a customer accidentally
deletes a disk, is outside the scope of Hyperdisk durability.

The table below shows durability for each disk type's design. 99.999% durability
means that with 1,000 Hyperdisk volumes, you would likely go a
hundred years without losing a single one.



| 
Hyperdisk Balanced | 
Hyperdisk Extreme | 
Hyperdisk ML | 
Hyperdisk Throughput | 
Hyperdisk Balanced High Availability | 
|

| 
Better than 99.999% | 
Better than 99.9999% | 
Better than 99.999% | 
Better than 99.999% | 
Better than 99.9999% | 
|


## Supported disk interfaces

Hyperdisk volumes are mounted as a disk on a VM using the NVMe or
SCSI interface, depending on the machine type of the instance.

## Pricing

You are billed for the total provisioned capacity of your
Hyperdisk volumes until you delete them. Charges incur even if
the volume isn't attached to any instances or if the instance is suspended or
stopped. You are charged per GiB per month. Additionally, you are billed for the
following:

- Hyperdisk Balanced charges a monthly rate for the provisioned IOPS and provisioned
throughput (in MiB/s) in excess of the baseline values of
3,000 IOPS and
140 MiB/s throughput.

- Hyperdisk Extreme charges a monthly rate based on the provisioned IOPS.

- Hyperdisk ML charges a monthly rate based on the provisioned throughput
(in MiB/s).
There is no additional charge for attaching multiple VMs to a single
Hyperdisk ML volume.

- Hyperdisk Throughput charges a monthly rate based on the provisioned throughput
(in MiB/s).

Because the data for regional disks is written to two locations,
the cost of Hyperdisk Balanced High Availability storage is twice the cost of Hyperdisk Balanced storage.

For more pricing information, see
[Disk pricing](/compute/disks-image-pricing#disk).

### Hyperdisk and committed use discounts

Hyperdisk volumes are not eligible for:

- Resource-based committed use discounts (CUDs)

- Sustained use discounts (SUDs)

### Hyperdisk and preemptible VM instances

Hyperdisk can be used with Spot VMs (or
preemptible VMs). However, there are no discounted spot prices for
Hyperdisk.

## Limitations for Hyperdisk

- You can't create a [machine image](/compute/docs/machine-images) from a
Hyperdisk volume.

- You can't [create an image](/compute/docs/images/create-delete-deprecate-private-images#create_image)
from a Hyperdisk Extreme, Hyperdisk Throughput, or Hyperdisk Balanced High Availability volume.

- You can't create an instant snapshot from a Hyperdisk ML or Hyperdisk Throughput volume.

- Hyperdisk Extreme, Hyperdisk ML and Hyperdisk Throughput volumes can't be used as boot disks.

- You can attach a Hyperdisk ML volume to up to 100 VMs at most once every
30 seconds.

- You can't create a Hyperdisk ML disk in read-write mode from a snapshot or a
disk image. You must create the disk in read-only mode.

- If you enable read-only mode for a Hyperdisk ML volume, you can't re-enable
read-write mode.

- If you create a volume in multi-writer mode, see
[additional limitations](/compute/docs/disks/sharing-disks-between-vms#mw-limitations).

- If you create a Hyperdisk Balanced volume in Confidential mode, see
[additional limitations](/compute/docs/disks/customer-managed-encryption#limitations).

- Confidential VMs with AMD SEV on C3D machine types don't support
Hyperdisk Balanced and Hyperdisk Throughput.

## What's next?

- Learn how to [create a Hyperdisk volume](/compute/docs/disks/add-hyperdisk).

- Learn how to [clone a Hyperdisk volume](/compute/docs/disks/clone-duplicate-disks).

- Learn about [synchronous disk replication](/compute/docs/disks/about-regional-persistent-disk)
with Hyperdisk Balanced High Availability.

- Learn about [Hyperdisk pools](/compute/docs/disks/storage-pools).

- Review [Disk pricing](/compute/disks-image-pricing#disk) information.

- Learn how to [optimize performance of Hyperdisk](/compute/docs/disks/optimize-hyperdisk).