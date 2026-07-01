# Artifact Registry in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/artifact-registry/docs/tpc-differences
Last updated: 2026-06-29

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

Application development

](https://berlin.devsitetest.how/docs/application-development)






- 








[

Artifact Registry

](https://berlin.devsitetest.how/artifact-registry/docs)






- 








[

Guides

](https://berlin.devsitetest.how/artifact-registry/docs/overview)












# Artifact Registry in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Workflows and tools ](#workflows-tools)
- [ Integrations ](#integrations-differences)
- [ Security and access control ](#security-differences)

- [ Related guides ](#related-guides)
- 










Artifact Registry lets you centrally store artifacts and build
dependencies as part of an integrated Google Cloud Dedicated in Germany experience.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Artifact Registry.



For more detailed information about Artifact Registry, see the
[Artifact Registry overview](/artifact-registry/docs/overview) and the rest of the
Artifact Registry documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Artifact Registry and
the Google Cloud version.
Some notable differences include the following:






- 
The following Artifact Registry repository artifact formats are
available in Google Cloud Dedicated in Germany:



- Docker

- Apt

- Yum




- 
Only standard mode repositories are available in Google Cloud Dedicated in Germany.


- 
[GPG Keys](https://gnupg.org/) aren't available for Apt and
Yum repositories in Google Cloud Dedicated in Germany.


- 
Cleanup policies aren't available in Google Cloud Dedicated in Germany.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Artifact Registry feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Workflows and tools



| 
**Repository formats** | 


The following Artifact Registry repository formats are
available:




- Docker

- Apt

- Yum


| 
|

| 
**Repository modes** | 
Only standard mode Artifact Registry repositories are available. | 
|

| 
**GPG Keys** | 
[GPG Keys](https://gnupg.org/) aren't available for Apt and
Yum repositories. | 
|

| 
**Artifact Registry domain** | 
Use `pkg-berlin-build0.goog` instead of `pkg.dev` when using Artifact Registry in Google Cloud Dedicated in Germany. | 
|


### Integrations



| 
**Client tools**
| 



Pushing or pulling artifacts is only available with the following
client tools:




- Docker CLI

- `critcl`

- Apt client

- Yum client


| 
|

| 
**Cleanup policies ** | 
Cleanup policies aren't available. | 
|


### Security and access control



| 
**Vulnerability Scanning**
| 
Vulnerability scanning with Artifact Analysis isn't available.
| 
|





## Related guides



The following information might also affect how you use and design for Artifact Registry
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)