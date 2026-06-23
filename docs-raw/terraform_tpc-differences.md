# Terraform in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/docs/terraform/tpc-differences
Last updated: 2026-06-18

- 





[

Technology areas

](https://berlin.devsitetest.how/docs)






- 








[

Guides

](https://berlin.devsitetest.how/docs/terraform/terraform-overview)












# Terraform in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Security and access control ](#security-differences)
- [ Workflows and tools ](#workflow-differences)

- [ Related guides ](#related-guides)
- 










HashiCorp Terraform is an Infrastructure as code (IaC) tool that lets you
provision and manage cloud infrastructure.

You can use the *Terraform provider for Google Cloud* with
Google Cloud Dedicated in Germany.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Terraform.



For more detailed information about Terraform, see the
[Terraform overview](/docs/terraform/terraform-overview) and the rest of the
Terraform documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Terraform and
the Google Cloud version.
Some notable differences include the following:






- 
Policy validation for Terraform with `gcloud terraform vet` isn't supported in Google Cloud Dedicated.


- 
[
Exporting your Google Cloud Dedicated resources to Terraform format
using `gcloud beta resource-config bulk-export`](https://berlin.devsitetest.how/docs/terraform/resource-management/export) isn't
supported in Google Cloud Dedicated.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Terraform feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support]().
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Security and access control



| 
**Policy validation**
| 


Policy validation using `gcloud beta terraform vet` isn't
supported in Google Cloud Dedicated.



However, you can use [Terraform checks](https://developer.hashicorp.com/terraform/language/checks)
to validate your Terraform configuration in Google Cloud Dedicated. There may
be other Terraform policy tools that aren't managed by Google Cloud
that work in Google Cloud Dedicated.


| 
|


### Workflows and tools



| 
**Export to Terraform format**
| 


Exporting your resources to Terraform format
using `gcloud beta resource-config bulk-export` isn't
supported in Google Cloud Dedicated.




Alternately, you can use HashiCorp's [Generating Configuration](https://developer.hashicorp.com/terraform/language/import/generating-configuration)
export method in Google Cloud Dedicated. You may be able to export your
Terraform configurations using other Terraform-supported tools that
are not managed by Google Cloud.


| 
|





## Related guides



The following information might also affect how you use and design for Terraform
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)