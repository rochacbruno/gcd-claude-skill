# View and manage quotas

Source: https://berlin.devsitetest.how/docs/quotas/help/request_increase
Last updated: 2026-07-10

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












# View and manage quotas 






- On this page 
- [ Limitations ](#limitations)
- [ Before you begin ](#before_you_begin)

- [ Required roles ](#required_roles)

- [ View quotas in the Google Cloud Dedicated console ](#viewing_your_quota_console)

- [ View the quotas for your project ](#view_project_quotas)
- [ View and export quota usage over time ](#charts)
- [ View API-specific quotas ](#api_specific_quota)
- [ Filter quotas ](#filtering_quotas)

- [ Manage your quotas using the console ](#managing_your_quota_console)

- [ Request a quota adjustment ](#requesting_higher_quota)
- [ View quota increase requests ](#viewing_quota_increase_requests)
- [ Create a quota override ](#create_override)
- [ Reset a quota value ](#reset_quota)

- [ Manage quotas using the Cloud Quotas API ](#managing_your_quota_api)
- [ Manage quotas using the gcloud CLI ](#managing_your_quota_gcloud)
- [ Request project quota ](#request_project_quota)
- [ What's next ](#whats_next)
- 










This document describes how you can view quota values in the
Google Cloud Dedicated console. You can also manage quotas from the
Google Cloud Dedicated console, Cloud Quotas API, and Google Cloud CLI
(gcloud CLI).

## Limitations

Cloud Quotas has the following limitations:

- 

In most cases, quota *increase* adjustments must be made at the
[project-level](/resource-manager/docs/creating-managing-projects).
A limited number of products support
[organization-level](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations)
quota increase adjustments. To see if a Google Cloud Dedicated in Germany product supports
organization-level quota increase adjustments, refer to the documentation
for that product.

- 

You can request quota *decrease* adjustments for
project-, organization-, and
[folder-level](/resource-manager/docs/cloud-platform-resource-hierarchy#folders)
quotas.

## Before you begin

The tasks in this document require Identity and Access Management (IAM) roles.

### Required roles







































































































To get the permissions that
you need to request quota adjustments,

ask your administrator to grant you the
following IAM roles on the project, folder, or organization:












- 
To view quotas:
[Quota Viewer ](/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaViewer) (`roles/servicemanagement.quotaViewer`)





- 
To request quota adjustments:
[Quota Administrator ](/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaAdmin) (`roles/servicemanagement.quotaAdmin`)










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).








These predefined roles contain

the permissions required to request quota adjustments. To see the exact permissions that are
required, expand the **Required permissions** section:





#### Required permissions




The following permissions are required to request quota adjustments:






- 
`serviceusage.quotas.update`



- 
`cloudquotas.quotas.update`














You might also be able to get
these permissions
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









## View quotas in the Google Cloud Dedicated console

You can view your current quota values in two different areas of the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/):

- 

The [**Quotas & System Limits**](https://console.cloud.berlin-build0.goog/quotas?project=_) page, which lists
all quota usage and values for your project.

- 

The [**Google Cloud Dedicated console API dashboard**](https://console.cloud.berlin-build0.goog/apis/dashboard),
which lists quota information for a particular API, including resource
usage over time.



### View the quotas for your project

The **IAM & Admin  > Quotas & System Limits** page displays a table
with configurable columns. The **Service** and **Quota** columns provide general
information about which quota is being described.
For example, the **Service** might be **Cloud Logging API** and the **Quota**
might be **Log ingestion requests per minute**. The **Quota** field also
describes how the quota is evaluated. Rate quotas are evaluated per minute, per
100 seconds, or per day. Quotas without any of these statements are allocation
quotas.

To view quota usage and values for all resources in your project, follow these
steps:


[Console](#console) 
More 




- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

To focus on the information that you need, filter and sort the list as
follows:

- 

To filter the list, enter the properties and values in the field. For
example, to view the BigQuery API quotas, select
**Service**, and then select **BigQuery API**.

- 

To sort the list, click the heading of the column you want to sort by. For
example, to sort alphabetically by the quota name, click the
**Quota** column heading.

By default, the list is sorted to show your most used quotas first, which
helps you see quotas that are at risk of being exceeded.

- 

Optional: To inspect the aggregate quota usage at the folder and
organization levels, select the organization or folder from the resource
selector.

You can find additional information about the quota by using the
**Metric**, **Limit name**, and **Monitored resource** columns. These
columns provide the detailed information needed to chart a quota.

For information about your quota usage, view the
**Current usage percentage** and **Current usage** columns.
Current usage is calculated according to the following criteria:

- 

For per-minute rate quotas:

- The *average* per minute usage in the past 10 minutes.

- 

For per-day rate quotas:

- The *total* usage so far in the current day, according to Pacific
Standard Time.

- 

For allocation quotas:

- The most recent value. For example, this number
might show the number of load balancers in use by your project.

- 

For concurrent quotas:

- The most recent value. For example, this number
might show the number of in-flight insert_operations for a given service.




You can learn more about quotas for a specific service by reading the
documentation for that service. For example, Compute Engine users can read the
[Compute Engine quota and limits overview](/compute/quotas-limits).

### View and export quota usage over time 

You can view quota usage over time with charts. The Quotas & System Limits page
of the console provides charts for each individual quota or system limit that's
in the Quotas & System Limits table. After you view a chart, you can export it.
To view and export a chart, follow these steps:


[Console](#console) 
More 




- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

Find the quota or system limit that you're interested in. In the entry
for this quota or system limit, click
monitoring **Show usage chart**. The chart view opens.

- 

In the chart view, set the time period. The default is 7 days. To change
this, click the time period menu and select your time period.

- 

To export the chart, click more_vert 
**More chart options**, and then select **Download**  > 
**Download PNG**. The chart downloads as a PNG file.




To do more with charts, see
[Set up quota alerts and monitoring](/docs/quotas/set-up-quota-alerts).

### View API-specific quotas 

To view detailed quota information for a particular API, including usage
over time, visit the quota page for the API in the Google Cloud Dedicated console.
Depending on the API, these limits can include *requests per day*,
*requests per minute*, and *requests per minute per user*.
Some APIs set very low limits until you
[enable billing on your project](/billing/docs/how-to/modify-project#enable_billing_for_a_project).

If there is no value for a given quota, the value appears as `Unlimited`.

You can view the current limits for a particular API in two different areas of
the Google Cloud Dedicated console:
on the Google Cloud Dedicated console **Quotas & System Limits** page
or **APIs & Services** page. Use the console view that you prefer:


[Console](#console) 
More 




- 

To view API-specific quotas from the **Quotas & System Limits** page using
a filter:

- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

Click filter_list **Filter** and select **Service** from
the menu that appears.

- 

Select or enter the service name that you want to view.

The page displays quotas and system limit information for the
specified API. The numbers that appear in the `Value` column are the
default quota values, unless you made a quota adjustment.

- 

To view API-specific quotas from the **APIs & Services** page:

- 

Go to the **APIs & Services** page:

[Go to APIs & Services](https://console.cloud.berlin-build0.goog/apis/dashboard?project=_)

- 

Select your project.

- 

Click the API name for the service you want to view.

- 

Click the **Quotas & System Limits** tab.

The page displays quotas and system limit information for the
specified API. The numbers that appear in the `Value` column are the
default quota values, unless you made a quota adjustment.

To see usage over time, click legend_toggle **Show usage chart**.



### Filter quotas

To filter the list of quotas by specific properties:


[Console](#console) 
More 




- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

Click filter_list **Filter** to
query your quotas by a specific property name or value.




## Manage your quotas using the console 

Depending on your resource usage, you might want to adjust the quota
values of your project up or down. This section describes how to change the provided quota
values. To see the values, in the **Details** column, click **All Quotas**.

### Request a quota adjustment 

Cloud Quotas adjustment requests are subject to review.


[Console](#console) 
More 




To adjust a quota value, follow these steps:

- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:




[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

If prompted to select a project, select the project that you want to
adjust.

- 

Find the quota value that you want to update in the **Quota** column and
select the checkbox next to the quota that you want to update.

If needed, use the **Filter** search box to search for your quota.

- 

Enter the quota value that you want in the **New value** field.
Some quota values have a unit of measurement; if this applies, select the
unit that you want in the adjacent list. Click **Done**.

Optional: If you see a checkbox with the text `I understand that this
request will remove any overrides`, it means that adjusting the quota value
to a number equal to or greater than the default will remove the previous
[quota override](/docs/quotas/view-manage#create_override). If this is what
you want, select the checkbox and proceed.

- 

To request a quota increase adjustment higher than the default, gather the
following information about the quota value that you would like to update:

- **Project name or number**: for example, `my-project`

- **Service name**: for example, `compute.googleapis.com`

- **Quota name**: for example, `CPUS-per-project-region`

- **Dimensions**: for example, `region=europe-west9-a, vm_family=C3`

- **Desired quota value**: for example, `2000`

- **Justification**: explain why the increase is needed—for example, `I'm
deploying a new app and the estimated CPU requirement is 1800`

- **Email address**: provide a way to contact you

- 

File a [Google Cloud Dedicated support request](/docs/overview/gcd-support) with the information that you gathered in
the previous step and
note that quota increase adjustment requests are subject to review.

To learn more about how the quota increase process works, see
[About quota increase requests](/docs/quotas/overview#about_increase_requests).

#### Batching requests for higher quota values

You can batch requests for higher quota by selecting the checkbox next to each
quota that you want to include. However, batching requests can increase the
amount of time it takes for Google Cloud Dedicated in Germany to review your request.

To reduce review time, group quota adjustment requests by product and area. For
example, if you want to request adjustments to networking and Compute Engine
VM quotas, create one request for the networking quotas and another request for
the Compute Engine VM quotas.



### View quota increase requests 

You can see pending and past quota increase requests in the
Google Cloud Dedicated console.

To see pending quota increase requests:


[Console](#console) 
More 




- 

Ensure that you have [permission to view quota increase requests.](/docs/quotas/permissions#permissions_increase) 

- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

A pending 
**Pending** icon appears next to the quota values that are pending a
decision on previously submitted increase requests. Click
pending **Pending** to view details of
the pending requests.

Pending requests are also shown in the **Quota changes** form when a
quota adjustment is about to be submitted.



To view all quota increase requests, which includes pending and past requests:


[Console](#console) 
More 




- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

Click the **Increase Requests** tab.

- 

Click filter_list **Filter** to
query your quota increase requests by a specific property.

When an organization or folder is selected, the page shows all quota increase
requests for all projects within the organization or folder.





### Create a quota override 

To restrict usage of a particular resource, create a *quota override* by
changing the quota value to a value less than the default quota value.
Creating a quota override is sometimes referred to as *capping usage*.

To create a quota override, follow the steps to
[update a quota value](#requesting_higher_quota).

Quota overrides are not available to all services. For service-specific
information, check the quota and system limits documentation for your service.

### Reset a quota value 

To reset the quota value after an override has been applied, follow these steps:


[Console](#console) 
More 




- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

Enter text in the filter_list **Filter**
search box to search for your quota. Set **Has override: True** to
show only quotas that have an override.

- 

On the Quotas page, info 
**Override** appears next to the quota limits that have an override.
Click info **Override** to view
details of this quota and an option to reset the value.

- 

To acknowledge that a reset removes your overrides, click the checkbox
preceding **Reset value** and then click **Reset value** to reset the quota.




To reset a quota manually, follow the same steps as for
[requesting a higher quota limit](#requesting_higher_quota). Make sure that you
set the **New value** equal to the **Default value** displayed below the quota
name in the **Quota changes** form.

## Manage quotas using the Cloud Quotas API

You can use the Cloud Quotas API to get current quota information and
set quota preferences for Google Cloud Dedicated in Germany APIs and services. For more information,
see the following:

- For an overview, see
[Cloud Quotas API overview](/docs/quotas/api-overview).

- For instructions on how to set up your development environment, see
[Set up the Cloud Quotas API](/docs/quotas/development-environment).

- For examples that show how to use the Cloud Quotas API to adjust quotas and
automate quota adjustments in your Google Cloud Dedicated projects, folders, or
organization, see [Implement common use cases](/docs/quotas/implement-common-use-cases).

## Manage quotas using the gcloud CLI

To use the gcloud CLI, make sure you have
[installed](/sdk/docs/install)
and [initialized](/sdk/docs/initialize) the latest version of the
gcloud CLI, including the [beta commands](/sdk/docs/components#alpha_and_beta_components)
component. If you're using Cloud Shell to interact with Google Cloud Dedicated in Germany, the
gcloud CLI is installed for you.

See the following sections for more information:

- 

For example `gcloud beta quotas info` and `gcloud beta quotas preferences`
commands, see
[Use the gcloud CLI to view and manage quotas](/docs/quotas/gcloud-cli-examples).

- 

For a complete list of `gcloud beta quotas` commands and flags, see the
[gcloud beta quotas](/sdk/gcloud/reference/beta/quotas) 
section of the Google Cloud CLI reference.

- [gcloud beta quotas info](/sdk/gcloud/reference/beta/quotas/info)

- [gcloud beta quotas preferences](/sdk/gcloud/reference/beta/quotas/preferences)

## Request project quota

For more information about requesting additional *project quotas*, refer to the
[Project quota requests](https://support.google.com/cloud/answer/6330231)
support article.

## What's next

- Set up the [quota adjuster](/docs/quotas/quota-adjuster) to monitor and
submit quota adjustment requests for you.

- Use the [Cloud Quotas API](/docs/quotas/api-overview) to manage your quotas at
the project level.

- Control access using [IAM](/docs/quotas/permissions) or
[VPC Service Controls](/docs/quotas/configure-vpc-service-controls).

- Configure your [quota project](/docs/quotas/quota-project).

- [Monitor](/docs/quotas/monitor) and
[troubleshoot](/docs/quotas/troubleshoot) quotas.