# Service Usage in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/service-usage/docs/tpc-differences
Last updated: 2026-07-29

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

Access and resource management

](https://documentation.s3ns.fr/docs/access-resources)






- 








[

Service Usage

](https://documentation.s3ns.fr/service-usage/docs)






- 








[

Guides

](https://documentation.s3ns.fr/service-usage/docs/overview)












# Service Usage in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Workflows and tools ](#workflow-differences)

- [ Related guides ](#related-guides)
- 










Service Usage lets you list, enable, and disable APIs and services in your Cloud de Confiance by S3NS projects.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Service Usage.



For more detailed information about Service Usage, see the
[Service Usage overview](/service-usage/docs/overview) and the rest of the
Service Usage documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Service Usage and
the Google Cloud version.
Some notable differences include the following:






- 
Enabling private, user-created services is unavailable.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Service Usage feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Workflows and tools



| 
**Private APIs**
| 
Enabling private (third party) APIs created using Cloud Endpoints is unavailable. You can only enable Cloud de Confiance by S3NS APIs and services with Service Usage.
| 
|

| 
**Default enabled APIs**
| 
The APIs enabled by default for a project only include services that are available in Cloud de Confiance by S3NS.
| 
|





## Related guides



The following information might also affect how you use and design for Service Usage
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)