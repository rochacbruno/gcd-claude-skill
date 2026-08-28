# Resource Manager in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/resource-manager/docs/tpc-differences
Last updated: 2026-08-26

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

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Resource Manager

](https://documentation.s3ns.fr/resource-manager/docs)






- 








[

Guides

](https://documentation.s3ns.fr/resource-manager/docs/resource-manager-overview)












# Resource Manager in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Projects ](#naming-differences)
- [ Organizations ](#organization-differences)
- [ Availability and disaster recovery ](#availability-differences)

- [ Related guides ](#related-guides)
- 










Resource Manager provides a hierarchical way to organize Cloud de Confiance by S3NS
resources, such as projects, folders, and organizations. Resource Manager
helps you manage access control, billing,
[organization policies](/organization-policy/overview),
and other settings for your resources.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Resource Manager.



For more detailed information about Resource Manager, see the
[Resource Manager overview](/resource-manager/docs/overview) and the rest of the
Resource Manager documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Resource Manager and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Resource Manager feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Projects



| 
**Project ID format** | 
In Cloud de Confiance by S3NS, all project IDs are
automatically prefixed with
`s3ns:` | 
|


### Organizations



| 
**Organization resource** | 
Organizations associated with Google Workspace and
Cloud Identity accounts are not available in
Cloud de Confiance by S3NS. Instead, a new empty organization resource is
provided by your platform operator when your organization [onboards to Cloud de Confiance by S3NS](/docs/get-started-tpc#set_up_a_new_organization). | 
|


### Availability and disaster recovery



| 
**Regions and zones** | 
Cloud de Confiance by S3NS has only a single region,
though with multiple zones.
Multi-region features and cross-region failover are not supported.
Deployment across multiple zones for resiliency is supported. | 
|





## Related guides



The following information might also affect how you use and design for Resource Manager
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products





- 
[Organization Policy Service](/organization-policy/tpc-differences)




### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)