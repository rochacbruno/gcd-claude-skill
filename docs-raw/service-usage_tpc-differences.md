# Service Usage in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/service-usage/docs/tpc-differences
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

Access and resource management

](https://berlin.devsitetest.how/docs/access-resources)






- 








[

Service Usage

](https://berlin.devsitetest.how/service-usage/docs)






- 








[

Guides

](https://berlin.devsitetest.how/service-usage/docs/overview)












# Service Usage in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Workflows and tools ](#workflow-differences)

- [ Related guides ](#related-guides)
- 










Service Usage lets you list, enable, and disable APIs and services in your Google Cloud Dedicated in Germany projects.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Service Usage.



For more detailed information about Service Usage, see the
[Service Usage overview](/service-usage/docs/overview) and the rest of the
Service Usage documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Service Usage and
the Google Cloud version.
Some notable differences include the following:






- 
Enabling private, user-created services is unavailable.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Service Usage feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Workflows and tools



| 
**Private APIs**
| 
Enabling private (third party) APIs created using Cloud Endpoints is unavailable. You can only enable Google Cloud Dedicated in Germany APIs and services with Service Usage.
| 
|

| 
**Default enabled APIs**
| 
The APIs enabled by default for a project only include services that are available in Google Cloud Dedicated in Germany.
| 
|





## Related guides



The following information might also affect how you use and design for Service Usage
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)