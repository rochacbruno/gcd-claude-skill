# Cloud Quotas overview

Source: https://berlin.devsitetest.how/docs/quotas/overview
Last updated: 2026-06-18

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












# Cloud Quotas overview 






- On this page 
- [ Types of quotas ](#types-of-quota)
- [ Quotas and the Google Cloud Dedicated hierarchy ](#gcp-hierarchy)
- [ Regions and zones ](#regions_and_zones)
- [ Manage quota values ](#manage_quota_values)

- [ When you run out of quota ](#running_out)
- [ About quota adjustments ](#about_increase_requests)

- [ What's next ](#whats_next)
- 










Google Cloud Dedicated in Germany uses quotas to help ensure fairness and reduce
spikes in resource use and availability. A quota restricts how much of a
Google Cloud Dedicated resource your Google Cloud Dedicated project can use. Quotas
apply to a range of resource types, including hardware, software, and network
components. For example, quotas can restrict the number of API calls to a
service, the number of load balancers used concurrently by your project, or the
number of projects that you can create. Quotas protect the community of
Google Cloud Dedicated users by preventing the overloading of services. Quotas also
help you to manage your own Google Cloud Dedicated resources.

The Cloud Quotas system does the following:


- Monitors your consumption of Google Cloud Dedicated products and services

- Restricts your consumption of those resources

- Provides a way to
[request changes to the quota value](/docs/quotas/help/request_increase)
and [automate quota adjustments](/docs/quotas/quota-adjuster)

In most cases, when you attempt to consume more of a resource than its quota
allows, the system blocks access to the resource, and the task that
you're trying to perform fails.

Quotas generally apply at the Google Cloud Dedicated project
level. Your use of a resource in one project doesn't affect
your available quota in another project. Within a Google Cloud Dedicated project, quotas
are shared across all applications and IP addresses. 

Many services also have system limits. System limits are fixed constraints,
such as maximum file sizes or database schema limitations, which cannot be
increased or decreased.

To learn about the quotas and system limits for a product, see the product's
quotas and limits page—for example,
[Cloud Storage quotas and limits](/storage/quotas).

The following links provide additional information related to resource usage:





- For other API usage metrics, see
[Monitoring API usage](/apis/docs/monitoring)




## Types of quotas

Google Cloud Dedicated in Germany has three types of quotas:

- 

**Allocation quotas**: Allocation quotas restrict how much of a resource
Google Cloud Dedicated allocates to you. For example, Compute Engine applies an
allocation quota to the number of VMs allocated for a Google Cloud Dedicated
project.

- 

**Rate quotas**: Rate quotas restrict the rate at which you can consume a
resource. Rate quotas specify a time period, and the amount of the resource
that you are permitted to consume over that time period.

- 

**Concurrent quotas**: Concurrent quotas restrict the number of operations that run
concurrently. Concurrent quotas usually apply to long-running operations. For
example, some Compute Engine `insert` operations can run for as long as one
hour and are limited by a concurrent quota.

## Quotas and the Google Cloud Dedicated hierarchy

Most quotas apply to one of the following levels of the Google Cloud Dedicated
[hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy):

- 

**Project-level quotas**: Project-level quotas restrict your resource usage
within a Google Cloud Dedicated project. Using the resource in one project
doesn't affect your available quota in another project.

- 

**Folder-level quotas**: Folder-level quotas restrict your resource usage
within a Google Cloud Dedicated folder. Child folders and projects contribute to
your quota usage. Folders and projects outside of your folder don't affect
your available quota.

- 

**Organization-level quotas**: Organization-level quotas restrict your
resource usage within a Google Cloud Dedicated organization. Child folders and
projects contribute to your quota usage. Resource usage outside of your
organization doesn't affect your available quota.

For example, the Compute Engine API has a project-level quota for the number of
queries you can make per minute. If one project reaches the quota value in less
than a minute, the project cannot make any more queries. Other projects can
continue to make queries.

Some quotas apply at the user level. For example, the number of
Google Cloud Dedicated projects you can create is limited by a quota applied at the
level of the user or service account.

To identify the Google Cloud Dedicated hierarchy level of the quotas for your
product, see the product's quotas and limits page—for example,
[Cloud Storage quotas and limits](/storage/quotas).

## Regions and zones

Quotas are regional or zonal:




- 
**Regional**: Regional quotas restrict resource usage in a
Google Cloud Dedicated region. Resource use in any zone in the region
contributes to regional quota use.




- 
**Zonal**: Zonal quotas restrict resource usage in a
Google Cloud Dedicated zone. Resource usage in one zone doesn't affect available
zonal quota in another zone. If the resource is also subject to a regional
quota, usage in one zone affects available quota in other zones by reducing
the regional quota shared across zones, even though the zonal quota for
other zones is unaffected.


Some resources have multiple location-based quotas. For example, a resource
might have both a regional quota and a zonal quota. The zonal quota restricts
the amount of use in each zone. The regional quota restricts the total use
across all zones in a given region.
To find out whether a quota is regional, zonal, or global, follow the
instructions to
[view dimensions](/docs/quotas/configure-dimensions#view_dimensions).

Regions and zones are examples of quota dimensions. For more information about
working with dimensions, see
[Configure dimensions](/docs/quotas/configure-dimensions).

## Manage quota values

Managing quota values and planning your resource use accordingly helps prevent
errors. Quota values are specific to your project, folder, and organization. For
example, you might request an adjustment to the value of a quota in one project,
but continue to use the default value in another project.

To get alerts
when you're approaching a quota value or system limit,
[Set up quota alerts](/docs/quotas/set-up-quota-alerts). To learn what to do if
you run out of quota or reach a system limit, see
[When you run out of quota](#running_out).

### When you run out of quota

Usually, if you run out of quota the task that you're trying to perform fails
and you get a [quota error](/docs/quotas/troubleshoot). For example, creating a
new project or calling an API throws a quota error if the task requires more
quota than you have. When this happens, the task continues to fail until you
have enough quota to accomplish the task.

If you want to keep your quota value, you can work within its constraints to
make your request:

- 

**Allocation quotas**: For allocation quotas, you can free up quota by deleting unused resources that
count towards the quota or system limit that you want to consume. For example,
you could have a quota value of 100 for a certain Compute Engine virtual
machine. If you already have 99 of that virtual machine but you want to create
ten more, your request will fail because adding ten more exceeds your quota
value (you can still provision one more virtual machine). To free up resources,
delete nine of the machines.

- 

**Rate quotas**: For rate quotas, your available quota resets automatically
when the time period resets. For example, you could have a quota value of 1000
requests per day for an API. If you already made 1000 requests to that API and
you want to make 1000 more, wait until the next day. For per-day quotas, the
time period resets at midnight Pacific Time. For per-minute quotas, the time
period resets one minute after your first request in a rolling window.

If you want to change your quota value to accommodate more resource use, you can
request a quota adjustment. Using more resources can incur more costs. To learn
about quota adjustments, see
[About quota adjustments](#about_increase_requests).

### About quota adjustments

To request a quota increase adjustment, you must contact
[Google Cloud Dedicated](https:///docs/overview/gcd-support)
support.

Evaluation criteria for automated reviews is not disclosed to ensure
fairness for all customers and prevent attempts to manipulate the process.
Sometimes quota adjustment requests are escalated to human reviewers, who also
follow criteria, but can consider your unique circumstances.

For more information, see the [Cloud Quotas differences page](/docs/quotas/tpc-differences).

## What's next

- Learn about [Cloud Quotas differences in Google Cloud Dedicated versus Google Cloud](/docs/quotas/tpc-differences)

- [Understand quota and system limit terminology](/docs/quotas/terminology) 

- [Quota permissions](/docs/quotas/permissions) 

- [View and manage quotas](/docs/quotas/view-manage) 

- [Monitor and alert](/docs/quotas/set-up-quota-alerts) 

- [Troubleshoot](/docs/quotas/troubleshoot)