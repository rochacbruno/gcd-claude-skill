# Quotas and system limits

Source: https://documentation.s3ns.fr/docs/quotas/quotas
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Resources

](https://documentation.s3ns.fr/docs/quotas/quotas)












# Quotas and system limits 






- On this page 
- [ Rate quotas ](#rate_quotas)
- [ Request a quota adjustment ](#request_a_quota_adjustment)
- [ What's next ](#whats_next)
- 










This document lists the quotas and system limits that apply to
Cloud Quotas.


- *Quotas* have default values, but you can typically request
adjustments.

- *System limits* are fixed values that can't be changed.

Cloud de Confiance by S3NS uses quotas to help ensure fairness and reduce
spikes in resource use and availability. A quota restricts how much of a
Cloud de Confiance resource your Cloud de Confiance project can use. Quotas
apply to a range of resource types, including hardware, software, and network
components. For example, quotas can restrict the number of API calls to a
service, the number of load balancers used concurrently by your project, or the
number of projects that you can create. Quotas protect the community of
Cloud de Confiance users by preventing the overloading of services. Quotas also
help you to manage your own Cloud de Confiance resources.

The Cloud Quotas system does the following:


- Monitors your consumption of Cloud de Confiance products and services

- Restricts your consumption of those resources

- Provides a way to
[request changes to the quota value](/docs/quotas/help/request_increase)
and [automate quota adjustments](/docs/quotas/quota-adjuster)

In most cases, when you attempt to consume more of a resource than its quota
allows, the system blocks access to the resource, and the task that
you're trying to perform fails.

Quotas generally apply at the Cloud de Confiance project
level. Your use of a resource in one project doesn't affect
your available quota in another project. Within a Cloud de Confiance project, quotas
are shared across all applications and IP addresses. 

For more information, see the
[Cloud Quotas overview](/docs/quotas/overview).

## Rate quotas

The following quotas apply to Cloud Quotas API requests:



| 
Quota | 
Value | 
|



| 
Read requests per minute, per project | 
1200 | 
|

| 
Update requests per minute, per project | 
60 | 
|

| 
Quota increase requests per day, per project | 
300 | 
|



## Request a quota adjustment

To adjust most quotas, use the Cloud de Confiance console.
For more information, see
[Request a quota adjustment](/docs/quotas/help/request_increase).

## What's next

- [View and manage quotas](/docs/quotas/view-manage)

- [Quota and system limit terminology](/docs/quotas/terminology)

- [Release notes](/docs/quotas/release-notes)