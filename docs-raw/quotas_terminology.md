# Quota and system limit terminology

Source: https://berlin.devsitetest.how/docs/quotas/terminology
Last updated: 2026-07-07

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://berlin.devsitetest.how/docs/quotas)






- 








[

Guides

](https://berlin.devsitetest.how/docs/quotas/overview)












# Quota and system limit terminology 






- On this page 
- [ What's next ](#whats_next)
- 









Quotas and system limits restrict your use of Google Cloud Dedicated in Germany resources to
support resource availability for all Google Cloud Dedicated in Germany users. Quotas have default
values, and can typically be adjusted. System limits are fixed values that
cannot be changed.

The following table lists additional quota terminology and definitions.



| 


Term
| 


Description
| 
|

| 


Dimension
| 


A dimension is an attribute that represents a region or a zone, or a service-specific dimension, such as `gpu_family` or `network_id`.



The Cloud Quotas API represents dimensions as key-value pairs, where the key is the dimension name, and the value is the value of the named dimension—for example, {"`key" : "region", "value" : "us-central1`"}.
| 
|

| 


Quota
| 


Usually, *quota* refers to a Google Cloud Dedicated in Germany resource and its
unit of measurement. For example, the quota
`CPUS-PER-VM-FAMILY-per-project-region` defines the
number of Compute Engine virtual CPUs (vCPUs) available to your
project for a specific VM family in a particular region. Occasionally,
Google Cloud Dedicated in Germany documentation uses the word *quota* in its more
general sense, meaning a limited allowance.
| 
|

| 


Quota adjustment
| 


A request to increase or decrease a quota value. Quota adjustment
requests are subject to review by Google Cloud Dedicated in Germany.

| 
|

| 


Quota adjuster settings ([Preview](https://berlin.devsitetest.how/products#product-launch-stages))
| 


This resource represents your quota adjuster settings for a particular
project. When enabled, the quota adjuster monitors your usage for the
specified resources and issues quota adjustment requests when resource
usage approaches its quota value.
| 
|

| 


Quota info
| 


`QuotaInfo` is a read-only resource that provides metadata and quota value information about a particular quota for a given project, folder or organization. The `QuotaInfo` resource contains:


- Metadata such as name and dimension.

- Quota values for different quota dimensions.


Cloud Quotas obtains information from the quotas defined by Google Cloud Dedicated services and any fulfilled quota adjustments that you initiate.



**Note**: Because `QuotaInfo` is constructed by incorporating information from different sources, a default quota configuration exists even if you have not created a `QuotaPreference` resource. Until you express a preferred state through `quotaPreference.create` or `quotaPreference.update`, `QuotaInfo` relies on the default quota information available to determine what quota value to enforce.
| 
|

| 


Quota preference
| 


A `QuotaPreference` resource represents your quota
preferences for a particular dimension combination. You can use this
resource to make quota adjustments requests and specify behavior for
adjustment requests. You can set quota preferences by using the
Google Cloud Dedicated in Germany console, the Cloud Quotas API, or the
Google Cloud CLI.
| 
|

| 


Quota value
| 


The maximum for a given quota. This value can be adjusted for most
quotas.
| 
|

| 


System limit
| 


A fixed value; typically, an architectural constraint. System limits cannot be adjusted.
| 
|


## What's next

- [Cloud Quotas overview](/docs/quotas/overview)

- [View and manage quotas](/docs/quotas/view-manage)

- [Cloud Quotas API overview](/docs/quotas/api-overview)