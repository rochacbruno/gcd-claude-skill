# Set up quota alerts and monitoring

Source: https://berlin.devsitetest.how/docs/quotas/set-up-quota-alerts
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












# Set up quota alerts and monitoring 






- On this page ** 
- [ Set up basic quota usage alerts ](#basic)
- [ Create charts ](#charts)
- [ Check quota metric support ](#checking_metric_support)
- [ Get metric names ](#get-metric-names)
- [ Do more with Cloud Monitoring ](#do-more)
- [ What's next ](#whats_next)
- 










You can set up usage alerts and monitoring for your quotas. The
Cloud Quotas dashboard is integrated with
[Cloud Monitoring](/monitoring/docs/monitoring-overview) for convenience.
This document describes how to set up alerts, create charts, and find more
information about using Cloud Monitoring for Cloud Quotas.

## Set up basic quota usage alerts 

You can set up quota alerts from the
**IAM & Admin  > Quotas & System Limits** page to get
notifications of quota events. For example, you can set up an alert to notify
you when your quota usage reaches a percentage of the maximum value. This
feature is only supported for project-level quotas.

To set up an alert for a specific quota or system limit, do the following:

- 

Make sure that you have
[permissions to create alerts](/docs/quotas/permissions#permissions_create_alert) 

- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

In the right-most column of the table, click more_vert **More
actions**, and then select **Create usage alert**. The **Alert policy
templates** pane opens.

- 

Under **Configure notifications**, select your notification channel. The
notification channel is how you receive the alert—for example email,
SMS, or Pub/Sub.

- 

Click **Create**.

## Create charts

The Cloud Monitoring metrics explorer lets you create charts to view metrics.
You can use it to view metrics related to Cloud Quotas.

To view the metrics for a monitored resource by using the
Metrics Explorer, do the following:


- 

In the Google Cloud Dedicated console, go to the
*leaderboard*  Metrics explorer** page:


[Go to **Metrics explorer**](https://console.cloud.berlin-build0.goog/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is
**Monitoring**.


- In the toolbar of the Google Cloud Dedicated console, select your Google Cloud Dedicated project.
For [App Hub](/app-hub/docs/overview) configurations, select the
App Hub host project or the app-enabled folder's management project.

- In the **Metric** element, expand the **Select a metric** menu,
enter `quota usage`
in the filter bar, and then use the submenus to select a specific resource type and metric:




- In the **Active resources** menu, select **Consumer Quota**.

- In the **Active metric categories** menu, select **Quota**.

- In the **Active metrics** menu, select a metric from the list. To display both active and inactive
metrics, click **Active** to clear the filter in the **Select a metric**
menu.



- Click **Apply**.







- 

To add filters, which remove time series from the query results, use the
[**Filter** element](/monitoring/charts/metrics-selector#filter-option).





- 

To combine time series, use the menus on the
[**Aggregation** element](/monitoring/charts/metrics-selector#select_display).
For example, to display the CPU utilization for your VMs, based on their zone, set the
first menu to **Mean** and the second menu to **zone**.



All time series are displayed when the first menu of the **Aggregation** element is set
to **Unaggregated**. The default settings for the **Aggregation** element
are determined by the metric type you selected.



- For quota and other metrics that report one sample per day, do the following:



- In the **Display** pane,
set the **Widget type** to **Stacked bar chart**.

- Set the time period to at least one week.





After you've found the quota usage information you want, you can use
Cloud Monitoring to create custom dashboards and alerts. For more
information, see [Do more with Cloud Monitoring](#do-more).

## Check quota metric support

Not all services support quota metrics in Cloud Monitoring. To see
applicable quota metrics for supported services, select **Consumer Quota** as
the resource type when building a chart or creating an alerting policy. Services
that don't support quota metrics aren't displayed.

- 

Common services that support quota metrics include Compute Engine,
Dataflow, Spanner, Pub/Sub, Cloud Vision,
Speech-to-Text, Cloud Monitoring, and Cloud Logging.

- 

Common services that don't support quota metrics include App Engine and
Cloud SQL.

## Get metric names

Quotas and system limits have two types of names: display names and metric
names. Display names have spaces and capitalization that make them easier for
humans to read. Metric names are more likely to be lowercase and delimited by
underscores instead of spaces; the exact format depends on the service.

The following instructions show how to get quota and system limit metric names
using either the Google Cloud Dedicated console or gcloud CLI.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

The table on this page displays quotas and system limits that have usage or
have adjusted values, and a reference entry for other quotas. The reference
entry has the word "default" in parentheses at the end of the listing in
the **Name** column. For
example, `SetIAMPolicy requests per minute per region (default)` is the
reference entry for the quota
`SetIamPolicyRequestsPerMinutePerProject`.

- 

If you don't see the **Metric** column, take the following steps.

- Click view_column **Column display options**.

- Select **Metric**.

- Click **OK**. The **Metric** column appears in the table.

The **Metric** column shows the metric names. To filter the results, enter a
property name or value in the field next to
filter_list **Filter**.



To get the metric names for a Google Cloud Dedicated in Germany service by
using the gcloud CLI, run the `quotas info list`
command. To skip lines that don't list metric names, pass the output to a
command such as `grep` with `metric:` as the search term, or use the
gcloud CLI
[`--format`](/sdk/gcloud/reference#--format) flag:


```
gcloud beta quotas info list --project= PROJECT_ID_OR_NUMBER \
--service= SERVICE_NAME --format="value(metric)"
```


Replace the following:

- ` PROJECT_ID_OR_NUMBER `: the project ID or project
number.

- ` SERVICE_NAME `: the name of the service whose quota
metrics you want to see—for example, the service name for
Compute Engine is `compute.googleapis.com`. Include the
`googleapis.com` portion of the service name.




## Do more with Cloud Monitoring

The [Cloud Monitoring](/monitoring/docs/monitoring-overview) tools let you
monitor quota usage, values, and errors in depth. You can use these metrics to
create custom dashboards and alerts. For example, you can view quota usage over
time or receive an alert when you're approaching your quota value.

Cloud Monitoring supports a wide variety of metrics that you can combine
with filters and aggregations for new and insightful views into your quota
usage. For example, you can combine a metric for allocation quota usage with a
`quota_metric` filter on Cloud TPU names.

Pricing for Cloud Monitoring is described in the
[Google Cloud Observability pricing](https://berlin.devsitetest.how/stackdriver/pricing)
document.

The [Cloud Monitoring documentation](/monitoring/docs/monitoring-overview)
is extensive, so here are a few documents to get you started:

- [Building charts](/monitoring/charts):
A comprehensive guide to creating charts and tables, and adding them to a
custom dashboard.

- [Introduction to alerting](/monitoring/alerts):
An overview covering how alerting works and what your options are for creating
an alert policy.

- [Managing alerting policies](/monitoring/alerts/manage-alerts):
A guide to various management tasks for your existing alerting policies—for
example, view a policy, edit a policy, delete a policy, or add a policy to a
dashboard.

- [Using quota metrics](/monitoring/alerts/using-quota-metrics):
A detailed document dedicated to quotas use cases, with examples covering topics
such as how to create alerts for `quota/exceeded` errors.

- [Google Cloud Dedicated in Germany metrics guide](/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime):
A metrics reference document. The `serviceruntime` section lists the quotas
metrics used for monitoring.

## What's next

- [View and manage quotas](/docs/quotas/view-manage)

- [Cloud Quotas audit logging](/docs/quotas/audit-logging)

- [Troubleshoot quota errors](/docs/quotas/troubleshoot)