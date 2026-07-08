# IAM in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/iam/docs/tpc-differences
Last updated: 2026-07-08

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

IAM

](https://berlin.devsitetest.how/iam/docs)






- 








[

Guides

](https://berlin.devsitetest.how/iam/docs/overview)












# IAM in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Integrations ](#integrations-differences)
- [ Security and access control ](#security-differences)
- [ Workflows and tools ](#Workflows and tools)
- [ Insights and observability ](#observability-differences)

- [ Related guides ](#related-guides)
- 










Identity and Access Management (IAM) is a tool to manage fine-grained authorization for Google Cloud Dedicated in Germany.
It lets you control *who* can do *what* on *which resources*.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of IAM.



For more detailed information about IAM, see the
[IAM overview](/iam/docs/overview) and the rest of the
IAM documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of IAM and
the Google Cloud version.
Some notable differences include the following:






- 
Only Workforce Identity Federation and Workload Identity Federation identities
can be used as [principal
identifiers](/iam/docs/principal-identifiers).


- 
Policy Intelligence capabilities are unavailable.


- 
Principal access boundary (PAB) policies are unavailable.


- 
Privileged Access Manager (PAM) is unavailable.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular IAM feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Integrations



| 
**Organization Policy Service** | 


Organization Policy gives you
centralized, programmatic control over your organization's resources. In Google Cloud Dedicated, predefined organization
policies are provided and can be used; however, you can't do the following:




- You can't create and use your own custom constraints.

- You can't use managed constraints.


| 
|


### Security and access control



| 
**Supported principal types** | 



Only the following types of [principal types](/iam/docs/principals-overview) are
supported when creating policies in Google Cloud Dedicated:





- Individual service accounts

- Workforce Identity Federation identities

- Workload Identity Federation identities

- GKE service accounts

| 
|

| 
**Principal access boundary policies** | 
Principal access boundary policies let you define the resources that
principals can access. These policies are unavailable in Google Cloud Dedicated. | 
|

| 
**Privileged Access Manager** | 
You can use
Privileged Access Manager to control just-in-time temporary privilege elevation for
select principals, and to view audit logs afterwards to find out who had
access to what and when. This feature is unavailable in Google Cloud Dedicated. | 
|


### Workflows and tools



| 
**Gemini assistance in the IAM role picker** | 


The IAM role picker lets you ask Gemini which
roles to grant to your principals. In Google Cloud Dedicated,
role suggestions from Gemini are unavailable.
| 
|

| 
**Permission error messages** | 


In the Google Cloud Dedicated console, permission error messages provide basic remediation
guidance. They don't provide the option to resolve permission errors directly from the
error message.
| 
|


### Insights and observability



| 
**Policy Intelligence** | 


Policy Intelligence tools help you understand and
manage your policies to proactively improve your security configuration.
Policy Intelligence tools are unavailable in Google Cloud Dedicated. As a result, the following features are
unavailable:




- Activity Analyzer

- Policy Analyzer

- Policy Simulator

- Policy Troubleshooter

- Role recommendations

- Service account insights


| 
|





## Related guides



The following information might also affect how you use and design for IAM
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)