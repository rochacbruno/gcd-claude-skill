# Artifact Registry in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/artifact-registry/docs/tpc-differences
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

Application development

](https://documentation.s3ns.fr/docs/application-development)






- 








[

Artifact Registry

](https://documentation.s3ns.fr/artifact-registry/docs)






- 








[

Guides

](https://documentation.s3ns.fr/artifact-registry/docs/overview)












# Artifact Registry in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Workflows and tools ](#workflows-tools)
- [ Integrations ](#integrations-differences)
- [ Security and access control ](#security-differences)

- [ Related guides ](#related-guides)
- 










Artifact Registry lets you centrally store artifacts and build
dependencies as part of an integrated Cloud de Confiance by S3NS experience.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Artifact Registry.



For more detailed information about Artifact Registry, see the
[Artifact Registry overview](/artifact-registry/docs/overview) and the rest of the
Artifact Registry documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Artifact Registry and
the Google Cloud version.
Some notable differences include the following:






- 
The following Artifact Registry repository artifact formats are
available in Cloud de Confiance by S3NS:



- Docker

- Apt

- Yum




- 
Only standard mode repositories are available in Cloud de Confiance by S3NS.


- 
[GPG Keys](https://gnupg.org/) aren't available for Apt and
Yum repositories in Cloud de Confiance by S3NS.


- 
Cleanup policies aren't available in Cloud de Confiance by S3NS.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Artifact Registry feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




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
Use `s3nsregistry.fr` instead of `pkg.dev` when using Artifact Registry in Cloud de Confiance by S3NS. | 
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
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)