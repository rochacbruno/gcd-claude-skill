# Organization Policy in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/organization-policy/tpc-differences
Last updated: 2026-10-22

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

Organization Policy

](https://berlin.devsitetest.how/organization-policy)






- 








[

Guides

](https://berlin.devsitetest.how/organization-policy/overview)












# Organization Policy in Google Cloud Dedicated versus Google Cloud 















The Organization Policy Service gives you centralized and programmatic control over your
organization's cloud resources. As the organization policy administrator, you
can configure constraints across your entire resource hierarchy.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Organization Policy.



For more detailed information about Organization Policy, see the
[Organization Policy overview](/organization-policy/overview) and the rest of the
Organization Policy documentation.




## Key differences



There are some differences between the Google Cloud Dedicated version of Organization Policy and
the Google Cloud version.
Some notable differences include the following:






- 
Organization Policy Service dry-run policies are unavailable


- 
Only a subset of managed constraints and custom constraints is
available. See
[
Organization policy constraints](/organization-policy/reference/org-policy-constraints) and [
Services that support custom constraints](/organization-policy/reference/custom-constraint-supported-services).


- 
Policy Intelligence for Organization Policy Service features such as
Analyzer, Simulator, and Recommender are unavailable.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Organization Policy feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Integrations



| 
**Policy Intelligence**
| 
Policy Intelligence tools for Organization Policy Service, including
Recommender, Simulator, and Analyzer, are not available in
Google Cloud Dedicated in Germany.
| 
|


### Security and access control



| 
**Organization policy managed constraints**
| 
A subset of managed constraints is unavailable in
Google Cloud Dedicated in Germany. All
[
legacy managed constraints](/organization-policy/overview#legacy-constraints) are available. For a list of available
constraints, see
[
Organization policy constraints](/organization-policy/reference/org-policy-constraints).
| 
**Organization policy custom constraints**
| 
A subset of custom constraints are unavailable in
Google Cloud Dedicated in Germany. For a list of services with
available custom constraints, see
[
Services that support custom constraints](/organization-policy/reference/custom-constraint-supported-services).
| 
|

| 
**Dry-run organization policies**
| 
Dry-run organization policies are unavailable in
Google Cloud Dedicated in Germany.
| 
|





## Related guides



The following information might also affect how you use and design for Organization Policy
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)


Related products 




- 
[Resource Manager](/resource-manager/docs/tpc-differences)



Google Cloud Dedicated guides 




- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)