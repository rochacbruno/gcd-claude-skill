# Quotas and system limits

Source: https://documentation.s3ns.fr/service-usage/docs/quotas
Last updated: 2026-08-07

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/service-usage/docs/tpc-differences) for more details.














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

Access and resource management

](https://documentation.s3ns.fr/docs/access-resources)






- 








[

Service Usage

](https://documentation.s3ns.fr/service-usage/docs)






- 








[

Resources

](https://documentation.s3ns.fr/service-usage/docs/resources)

















- On this page 
- [ Rate quotas ](#rate_quotas)
- [ Get quota and system limit metric names ](#get-metric-names)
- [ Request a quota adjustment ](#request_a_quota_adjustment)
- 









# Quotas and system limits 



This document lists the quotas and system limits that apply to
Service Usage.


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

Rate quotas restrict the rate at which you can consume a resource. Per-minute
rate quotas reset every minute. The following table lists the rate quotas that
apply to Service Usage and the default value for each quota.



| 
Quota | 
Value | 
|



| 
List available/disabled services requests per minute | 
60 | 
|

| 
List enabled services requests per minute | 
600 | 
|

| 
List public services requests per minute | 
60 | 
|

| 
Default requests per minute

(all other read-only operations that don't modify the state of your
project)
| 
600 | 
|

| 
Mutate requests per minute

(state-changing operations that actively change your project's
configuration)
| 
120 | 
|



## Get quota and system limit metric names

Quotas and system limits have two types of names: display names and metric
names. Display names have spaces and capitalization that make them easier for
humans to read. Metric names are more likely to be lowercase and delimited by
underscores instead of spaces; the exact format depends on the service.

The following instructions show how to get metric names for quotas and system
limits by using either the Cloud de Confiance console or the
gcloud CLI.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

In the Cloud de Confiance console, go to the
**IAM & Admin  > 
Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.s3nscloud.fr/iam-admin/quotas)

The table on this page displays quotas and system limits that have usage or
have adjusted values, and a reference entry for other quotas. The reference
entry has the word "default" in parentheses at the end of the listing in
the **Name** column.

- 

If you don't see the **Metric** column, take the following steps.

- Click view_column 
**Column display options**.

- Select **Metric**.

- Click **OK**. The **Metric** column appears in the table.

The **Metric** column shows the metric names. To filter the results, enter a
property name or value in the field next to
filter_list **Filter**—for example, **Service Usage API**.



To get the metric names for a Cloud de Confiance by S3NS service by
using the gcloud CLI, run the
[`quotas info list`](/sdk/gcloud/reference/beta/quotas/info/list)
command. To skip lines that don't list metric names, pass the output to a
command such as `grep` with `metric:` as the search term, or use the
gcloud CLI [`--format`](/sdk/gcloud/reference#--format) flag:


```
gcloud beta quotas info list --project= PROJECT_ID_OR_NUMBER \
--service=serviceusage.googleapis.com --format="value(metric)"
```


Replace the ` PROJECT_ID_OR_NUMBER ` with your project ID
or project number.

If you receive an an error message about no quota project being set, see
[User credentials not working](/docs/authentication/troubleshoot-adc#user-creds-client-based).



## Request a quota adjustment

To adjust most quotas, use the Cloud de Confiance console.
For more information, see
[Request a quota adjustment](/docs/quotas/help/request_increase).