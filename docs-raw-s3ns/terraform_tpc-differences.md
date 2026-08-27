# Terraform in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/docs/terraform/tpc-differences
Last updated: 2026-08-26

- 





[

Technology areas

](https://documentation.s3ns.fr/docs)






- 








[

Guides

](https://documentation.s3ns.fr/docs/terraform/terraform-overview)












# Terraform in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Security and access control ](#security-differences)
- [ Workflows and tools ](#workflow-differences)

- [ Related guides ](#related-guides)
- 










HashiCorp Terraform is an Infrastructure as code (IaC) tool that lets you
provision and manage cloud infrastructure.

You can use the *Terraform provider for Google Cloud* with
Cloud de Confiance by S3NS.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Terraform.



For more detailed information about Terraform, see the
[Terraform overview](/docs/terraform/terraform-overview) and the rest of the
Terraform documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Terraform and
the Google Cloud version.
Some notable differences include the following:






- 
Policy validation for Terraform with `gcloud terraform vet` isn't supported in Cloud de Confiance.


- 
[
Exporting your Cloud de Confiance resources to Terraform format
using `gcloud beta resource-config bulk-export`](https://documentation.s3ns.fr/docs/terraform/resource-management/export) isn't
supported in Cloud de Confiance.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Terraform feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support]().
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Security and access control



| 
**Policy validation**
| 


Policy validation using `gcloud beta terraform vet` isn't
supported in Cloud de Confiance.



However, you can use [Terraform checks](https://developer.hashicorp.com/terraform/language/checks)
to validate your Terraform configuration in Cloud de Confiance. There may
be other Terraform policy tools that aren't managed by Google Cloud
that work in Cloud de Confiance.


| 
|


### Workflows and tools



| 
**Export to Terraform format**
| 


Exporting your resources to Terraform format
using `gcloud beta resource-config bulk-export` isn't
supported in Cloud de Confiance.




Alternately, you can use HashiCorp's [Generating Configuration](https://developer.hashicorp.com/terraform/language/import/generating-configuration)
export method in Cloud de Confiance. You may be able to export your
Terraform configurations using other Terraform-supported tools that
are not managed by Google Cloud.


| 
|





## Related guides



The following information might also affect how you use and design for Terraform
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)