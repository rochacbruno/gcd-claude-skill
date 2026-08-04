# Cloud Quotas in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/docs/quotas/tpc-differences
Last updated: 2026-07-17

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

Cloud Quotas

](https://documentation.s3ns.fr/docs/quotas)






- 








[

Guides

](https://documentation.s3ns.fr/docs/quotas/overview)












# Cloud Quotas in Cloud de Confiance versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Workflows and tools ](#workflow-differences)

- [ Related guides ](#related-guides)
- 










Cloud Quotas provides tools so you can view your usage of cloud
resources, create usage alerts, and even
[automate quota adjustments](/docs/quotas/quota-adjuster).
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Quotas.



For more detailed information about Cloud Quotas, see the
[Cloud Quotas overview](/docs/quotas/overview) and the rest of the
Cloud Quotas documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Cloud Quotas and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Quotas feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Workflows and tools



| 
**Quota increase adjustments**
| 



To request a quota increase adjustment, you must contact
[Cloud de Confiance support](https://support.s3ns.fr).



Follow the steps to
[request a quota adjustment](/docs/quotas/help/request_increase),
and provide the following information about the quota
value that you would like to increase:




- Project name or number**: for example, `my-project`

- **Service name**: for example, `compute.googleapis.com`

- **Quota name**: for example, `CPUS-per-project-region`

- **Dimensions**: for example, `region=europe-west9-a, vm_family=C3`

- **Desired quota value**: for example, `2000`

- **Justification**: explain why the increase is needed—for example, `I'm
deploying a new app and the estimated CPU requirement is 1800`

- **Email address**: provide a way to contact you


| 
|





## Related guides



The following information might also affect how you use and design for Cloud Quotas
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)