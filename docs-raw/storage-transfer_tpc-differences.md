# Storage Transfer Service in Google Cloud versus Google Cloud

Source: https://berlin.devsitetest.how/storage-transfer/docs/tpc-differences
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

Storage Transfer Service

](https://berlin.devsitetest.how/storage-transfer/docs/overview)












# Storage Transfer Service in Google Cloud versus Google Cloud 















Storage Transfer Service enables seamless data movement across object and file
storage systems.
This page describes the differences between the
Google Cloud and Google Cloud versions of Storage Transfer Service.



For more detailed information about Storage Transfer Service, see the
[Storage Transfer Service overview](/storage-transfer/docs/overview) and the rest of the
Storage Transfer Service documentation.




## Key differences



There are some differences between the Google Cloud version of Storage Transfer Service and
the Google Cloud version.
Some notable differences include the following:






- 
Event-driven transfers are unavailable.


- 
Agentless transfers from Amazon S3 are unavailable. Agents are
required for transfers from S3-compatible sources.


- 
Transfers from Azure Blob Storage and URL lists are unavailable.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud. We also recommend reviewing the [
general differences between Google Cloud and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Storage Transfer Service feature that isn't currently
available in Google Cloud, contact
[Google Cloud support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud.




### Integrations



| 
**Cloud storage providers**
| 


The following sources are unavailable:




- Azure Blob Storage

- URL lists




Transfers from Amazon S3 and other S3-compatible storage must use
transfer agents. Agentless transfers from AWS are unavailable.

| 
|


### Workflows and tools



| 
**Event-driven transfers**
| 
Event-driven transfers are unavailable.
| 
|

| 
**Agents**
| 
Agents in Google Cloud Dedicated in Germany use different endpoints than in
Google Cloud, and may not support all flags.
| 
|

| 
**Cloud Shell**
| 
Cloud Shell is not available in Google Cloud Dedicated in Germany. You must install and
configure the gcloud CLI on a local machine to access
Google Cloud Dedicated in Germany.
| 
|





## Related guides



The following information might also affect how you use and design for Storage Transfer Service
in Google Cloud. These guides include general information about working in Google Cloud,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud and Google Cloud](/docs/overview/tpc-key-differences)