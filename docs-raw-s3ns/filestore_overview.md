# Filestore overview

Source: https://documentation.s3ns.fr/filestore/docs/overview
Last updated: 2026-10-26

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

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Filestore

](https://documentation.s3ns.fr/filestore/docs)






- 








[

Guides

](https://documentation.s3ns.fr/filestore/docs/overview)












# Filestore overview 














Filestore instances are fully managed file servers on Cloud de Confiance by S3NS that
can be connected to a number of client types:

- [Compute Engine VMs](/filestore/docs/mounting-fileshares)

- [Google Kubernetes Engine (GKE) clusters](/filestore/docs/filestore-for-gke)

- [On-premises machines](/filestore/docs/remote-mounting)

- [Cloud Run services](/filestore/docs/mount-filestore-cloud-run)

- [AI agent fleets and sandboxes](/filestore/docs/agent-volumes-overview)

Once provisioned, you can scale the capacity of your instances according to need
without any downtime.

## Why Filestore?

Cloud de Confiance by S3NS offers three main types of data storage: block, file, and object
storage.

As a type of persistent file storage, Filestore supports multiple
concurrent application instances accessing the same file system simultaneously.

For Google Kubernetes Engine users, for example, Filestore provides multiple reader,
multiple writer access, letting you mount your GKE
PersistentVolumes as read-write by many nodes.

When compared to object storage, such as Cloud Storage FUSE, while that product does
offer some file system [semantics](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md),
it [lacks some of the more robust characteristics of file storage](/storage/docs/gcs-fuse#expandable-1)
provided by Filestore. Some examples of capabilities supported by
Filestore and not Cloud Storage FUSE include the following:

- POSIX compliance

- Hard links and file locking

- Concurrency control for multiple writes on the same object

For more information, see the following resources:

- [Compare the relative advantages of block, file, and object storage](/architecture/storage-advisor#review_the_storage_options).

- [Review the storage options for HPC workloads in Cloud de Confiance by S3NS](/architecture/parallel-file-systems-for-hpc#storage-options-for-hpc-workloads-in-google-cloud).

- [Learn more about Filestore support for GKE](/filestore/docs/filestore-for-gke).

- [Learn more about using Custom performance with GKE](/filestore/docs/csi-driver#custom-performance) to scale IOPS independently of capacity.

- [Learn more about the limitations of Cloud Storage FUSE](/storage/docs/gcs-fuse#expandable-1).

- [Learn about storage options and access modes for GKE clusters](/kubernetes-engine/docs/concepts/storage-overview).

## Service tiers

Filestore offers multiple service tiers that vary in capacity,
performance, and features. Each service tier is tailored for specific use cases:


- **Regional tier:** The only service tier available in Cloud de Confiance,
with capacity from 1 TiB to 9.75 TiB. Recommended for
mission-critical workloads requiring high availability.

For details, see [Service tiers](/filestore/docs/service-tiers).

## Protocol support

Filestore supports the following file system protocols:




| 
Protocol | 
Supported service tiers | 
Highlights | 
|



| 
NFSv3 | 
All service tiers | 




- Supports bidirectional communication between the client and server.


- Supports [VPC Network Peering](/vpc/docs/vpc-peering).



| 
|

| 
NFSv4.1 | 
[zonal, regional, and enterprise service tiers](/filestore/docs/service-tiers) | 




- Supports client and server authentication, message integrity checks, and in-transit data encryption.


- Supports [VPC Network Peering](/vpc/docs/vpc-peering).



| 
|



For help understanding which protocol may be right for you, see
[About supported protocols](/filestore/docs/about-supported-protocols).

## Connectivity

Filestore instances can connect to any clients that are on the same VPC
network, including [Shared VPC networks](/vpc/docs/shared-vpc). You can
also connect to clients on remote networks, such as an on-premises machine,
using
[Cloud VPN](/network-connectivity/docs/vpn/concepts/overview) or
[Cloud Interconnect](/network-connectivity/docs/interconnect/concepts/overview).

## Networking

For information related to Filestore networking requirements, see the
following resources:

- [Filestore networking and IP resource requirements](/filestore/docs/network-ip-requirements)

- [Configure NFS ports on client VMs](/filestore/docs/setting-nfs-ports)

- [Configure firewall rules](/filestore/docs/configuring-firewall)

- [Create an instance on a Shared VPC network in service projects](/filestore/docs/shared-vpc)

- [Supported file system protocols](/filestore/docs/about-supported-protocols)

## Performance

[Custom performance](/filestore/docs/custom-performance) lets you define the performance settings for
your Filestore instances independently of the specified capacity. 
This means you can optimize your Filestore instances for your workload
requirements and scale your file shares to meet the demands of your applications
without resizing the capacity.

Note: Custom performance is available for the regional [service tier](/filestore/docs/service-tiers). In addition, GKE workloads can dynamically adjust performance for zonal and regional tiers without downtime.

For details on performance settings, limits, and testing see [performance](/filestore/docs/performance).

## Data protection

The following sections discuss Filestore instance data protection.

### Encryption at rest

By default, Filestore automatically encrypts your data at rest. The
durable storage behind each Filestore instance is encrypted with
system-defined keys that are managed by Google.

When you delete a Filestore instance, Google discards the encryption
information used by the instance, rendering the data irretrievable as per the
description in [Data deletion on Cloud de Confiance by S3NS](/docs/security/deletion).

If you need more control over the keys that protect your data, you can also use
[customer-managed encryption keys (CMEK)](/filestore/docs/cmek) with Filestore.

For details, see
[Encryption at rest in Cloud de Confiance by S3NS](/docs/security/encryption/default-encryption).

### Encryption in transit

While NFSv3 does not encrypt data in transit, the NFSv4.1 protocol supports
in-transit data encryption using Kerberos (`krb5p`). Additionally, all
in-transit data to and within Cloud de Confiance by S3NS is encrypted.

For details, see the following resources:

- [Benefits of NFSv4.1](/filestore/docs/about-supported-protocols#benefits-of-nfsv41)

- [Encryption in Transit in Cloud de Confiance by S3NS](/docs/security/encryption-in-transit)

### Access control

You can control the level of access that a client has on Filestore
instance data based on the client's IP address.
[IP-based access control](/filestore/docs/access-control#ip-based_access_control)
rules for an instance can be created or modified during and after instance
creation.

You can also control which Cloud de Confiance by S3NS users can create, edit, and view
Filestore resources by using [IAM permissions and roles](/filestore/docs/iam).

## Data recovery options

The following sections discuss Filestore instance data recovery options.

### Backups

[Filestore backups](/filestore/docs/backups) are point-in-time copies of
a Filestore instance that includes all user data and some instance
metadata. You can create a backup of an instance and then use it
to restore the instance to an existing Filestore instance or a new instance.

### Snapshots

A [Filestore snapshot](/filestore/docs/snapshots) preserves the state of
your Filestore instance data at the time that the snapshot is created.
You can use snapshots to restore individual files or directories or completely
revert your instance to the state of a snapshot.

## Reliability

Filestore offers several features to ensure the reliability and availability of your data.

### Regional reliability

Regional tier instances are regional resources.

They provide transparent failover during zone failures, continuing to serve data and accept writes. Filestore uses a strict consistency policy, acknowledging writes only after they are persisted to ensure data integrity during zone failures.

While NFS data access continues without interruption, operations through the Cloud de Confiance console or the Filestore API might be unavailable for several hours during a zone failure. You might also experience some performance degradation until the zone recovers. Note that you cannot create new regional or enterprise instances in a region while it is experiencing a zone failure.

## What's next

- Learn about [Filestore differences in Cloud de Confiance versus Google Cloud](/filestore/docs/tpc-differences).

- Learn more about Filestore's
[service tiers](/filestore/docs/service-tiers)
to decide which service tier is right for you.

- [Compare the relative advantages of block, file, and object
storage](/architecture/storage-advisor#review_the_storage_options).

- [Review the storage options for HPC workloads in
Cloud de Confiance by S3NS](/architecture/parallel-file-systems-for-hpc#storage-options-for-hpc-workloads-in-google-cloud).