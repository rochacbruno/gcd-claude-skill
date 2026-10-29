# Filestore in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/filestore/docs/tpc-differences
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












# Filestore in Cloud de Confiance versus Google Cloud 















Filestore is a scalable, high-performance file storage service for Cloud de Confiance by S3NS. Filestore instances are fully managed NFS file servers on Cloud de Confiance by S3NS for use with applications running on Compute Engine virtual machine (VM) instances, Google Kubernetes Engine clusters, external datastores such as Google Cloud VMware Engine, or on-premises machines.

This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Filestore.



For more detailed information about Filestore, see the
[Filestore overview](/filestore/docs/overview) and the rest of the
Filestore documentation.




## Key differences



There are some differences between the Cloud de Confiance version of Filestore and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Filestore feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Availability and disaster recovery



| 
**Service tiers**
| 
Filestore regional service tier with the capacity range of 1 TiB to 9.75 TiB is available in Cloud de Confiance.
Filestore basic SSD, basic HDD, zonal, and enterprise service tiers are not available in Cloud de Confiance.
|

| 
**Regions and zones**
| 
Cloud de Confiance uses a single region with multiple zones.
| 
|


### Integrations



| 
**Product integrations**
| 
Filestore CSI driver for Google Kubernetes Engine is the only product integration available in Cloud de Confiance.
| 
|


### Network


| **File system protocols**
| 
While NFSv4.1 file system protocol is available in Cloud de Confiance, the integration with Microsoft Managed Active Directory is not available.
| 
|

| 
| **Connectivity**
| 
Direct Peering is the only option available in Cloud de Confiance to establish connectivity between the Virtual Private Cloud network and a Filestore instance. Private services access and Private Service Connect capabilities are not available in Cloud de Confiance. 
| 
|





## Related guides



The following information might also affect how you use and design for Filestore
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)