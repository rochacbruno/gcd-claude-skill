# Access Context Manager in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/access-context-manager/docs/tpc-differences
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

Access Context Manager

](https://documentation.s3ns.fr/access-context-manager/docs)






- 








[

Guides

](https://documentation.s3ns.fr/access-context-manager/docs/create-access-level)












# Access Context Manager in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Security and access control ](#security-differences)

- [ Related guides ](#related-guides)
- 










Access Context Manager helps you secure access to your Cloud de Confiance by S3NS resources based on the
context of the request. You can define access levels based on attributes like
user location and device to control who can access your resources.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Access Context Manager.



For more detailed information about Access Context Manager, see the
[Access Context Manager overview](/access-context-manager/docs/overview) and the rest of the
Access Context Manager documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Access Context Manager and
the Google Cloud version.
Some notable differences include the following:






- 


Only basic access levels are available in Cloud de Confiance.




- 


Only IP subnetworks and geographic location conditions are available for
access levels in Cloud de Confiance.






A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Access Context Manager feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Security and access control



| 
**Access levels**
| 
Cloud de Confiance supports basic access levels. Advanced and custom access levels are unavailable.
| 
|

| 
**Conditions**
| 
Only IP subnetworks, IP addresses, and geographic location conditions
are available for access levels. Other conditions, such as device
attributes and request time, are unavailable.
| 
|





## Related guides



The following information might also affect how you use and design for Access Context Manager
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)



### Related products



- [VPC Service Controls in
Cloud de Confiance by S3NS](/vpc-service-controls/docs/tpc-differences)


### Cloud de Confiance guides





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)