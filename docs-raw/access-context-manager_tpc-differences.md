# Access Context Manager in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/access-context-manager/docs/tpc-differences
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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

Access Context Manager

](https://berlin.devsitetest.how/access-context-manager/docs)






- 








[

Guides

](https://berlin.devsitetest.how/access-context-manager/docs/create-access-level)












# Access Context Manager in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Security and access control ](#security-differences)

- [ Related guides ](#related-guides)
- 










Access Context Manager helps you secure access to your Google Cloud Dedicated in Germany resources based on the
context of the request. You can define access levels based on attributes like
user location and device to control who can access your resources.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Access Context Manager.



For more detailed information about Access Context Manager, see the
[Access Context Manager overview](/access-context-manager/docs/overview) and the rest of the
Access Context Manager documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Access Context Manager and
the Google Cloud version.
Some notable differences include the following:






- 


Only basic access levels are available in Google Cloud Dedicated.




- 


Only IP subnetworks and geographic location conditions are available for
access levels in Google Cloud Dedicated.






A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Access Context Manager feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Security and access control



| 
**Access levels**
| 
Google Cloud Dedicated supports basic access levels. Advanced and custom access levels are unavailable.
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
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products



- [VPC Service Controls in
Google Cloud Dedicated in Germany](/vpc-service-controls/docs/tpc-differences)


### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)