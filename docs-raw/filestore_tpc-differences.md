# Filestore in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/filestore/docs/tpc-differences
Last updated: 2026-10-26

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

Storage

](https://berlin.devsitetest.how/docs/storage)






- 








[

Filestore

](https://berlin.devsitetest.how/filestore/docs)






- 








[

Guides

](https://berlin.devsitetest.how/filestore/docs/overview)












# Filestore in Google Cloud Dedicated versus Google Cloud 















Filestore is a scalable, high-performance file storage service for Google Cloud Dedicated in Germany. Filestore instances are fully managed NFS file servers on Google Cloud Dedicated in Germany for use with applications running on Compute Engine virtual machine (VM) instances, Google Kubernetes Engine clusters, external datastores such as Google Cloud VMware Engine, or on-premises machines.

This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Filestore.



For more detailed information about Filestore, see the
[Filestore overview](/filestore/docs/overview) and the rest of the
Filestore documentation.




## Key differences



There are some differences between the Google Cloud Dedicated version of Filestore and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Filestore feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Availability and disaster recovery



| 
**Service tiers**
| 
Filestore regional service tier with the capacity range of 1 TiB to 9.75 TiB is available in Google Cloud Dedicated.
Filestore basic SSD, basic HDD, zonal, and enterprise service tiers are not available in Google Cloud Dedicated.
|

| 
**Regions and zones**
| 
Google Cloud Dedicated uses a single region with multiple zones.
| 
|


### Integrations



| 
**Product integrations**
| 
Filestore CSI driver for Google Kubernetes Engine is the only product integration available in Google Cloud Dedicated.
| 
|


### Network


| **File system protocols**
| 
While NFSv4.1 file system protocol is available in Google Cloud Dedicated, the integration with Microsoft Managed Active Directory is not available.
| 
|

| 
| **Connectivity**
| 
Direct Peering is the only option available in Google Cloud Dedicated to establish connectivity between the Virtual Private Cloud network and a Filestore instance. Private services access and Private Service Connect capabilities are not available in Google Cloud Dedicated. 
| 
|





## Related guides



The following information might also affect how you use and design for Filestore
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)