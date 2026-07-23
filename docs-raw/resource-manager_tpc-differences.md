# Resource Manager in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/resource-manager/docs/tpc-differences
Last updated: 2026-07-22

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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

Resource Manager

](https://berlin.devsitetest.how/resource-manager/docs)






- 








[

Guides

](https://berlin.devsitetest.how/resource-manager/docs/resource-manager-overview)












# Resource Manager in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Projects ](#naming-differences)
- [ Organizations ](#organization-differences)
- [ Availability and disaster recovery ](#availability-differences)

- [ Related guides ](#related-guides)
- 










Resource Manager provides a hierarchical way to organize Google Cloud Dedicated in Germany
resources, such as projects, folders, and organizations. Resource Manager
helps you manage access control, billing,
[organization policies](/organization-policy/overview),
and other settings for your resources.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Resource Manager.



For more detailed information about Resource Manager, see the
[Resource Manager overview](/resource-manager/docs/overview) and the rest of the
Resource Manager documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Resource Manager and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Resource Manager feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Projects



| 
**Project ID format** | 
In Google Cloud Dedicated in Germany, all project IDs are
automatically prefixed with
`eu0:` | 
|


### Organizations



| 
**Organization resource** | 
Organizations associated with Google Workspace and
Cloud Identity accounts are not available in
Google Cloud Dedicated in Germany. Instead, a new empty organization resource is
provided by your platform operator when your organization [onboards to Google Cloud Dedicated in Germany](/docs/get-started-tpc#set_up_a_new_organization). | 
|


### Availability and disaster recovery



| 
**Regions and zones** | 
Google Cloud Dedicated in Germany has only a single region,
though with multiple zones.
Multi-region features and cross-region failover are not supported.
Deployment across multiple zones for resiliency is supported. | 
|





## Related guides



The following information might also affect how you use and design for Resource Manager
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products





- 
[Organization Policy Service](/organization-policy/tpc-differences)




### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)