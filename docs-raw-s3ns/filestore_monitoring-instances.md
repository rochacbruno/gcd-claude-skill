# Monitoring instances and quota

Source: https://documentation.s3ns.fr/filestore/docs/monitoring-instances
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/filestore/docs/tpc-differences) for more details.














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

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Filestore

](https://documentation.s3ns.fr/filestore/docs)






- 








[

Guides

](https://documentation.s3ns.fr/filestore/docs/overview)












# Monitoring instances and quota 














This page shows you how to monitor your Filestore instances and set up
alerts for low disk space and low backups quota.

You can monitor Filestore instances using
[Cloud Monitoring](/monitoring).

## Before you begin

Before you begin, make sure you have access to the following roles:

- Monitoring Viewer

- Monitoring Editor

To see how to grant access to these roles, see [Grant access to Cloud Monitoring](/monitoring/access-control#grant-monitoring-access).

## Add a Filestore metric chart to a Cloud Monitoring dashboard

To see Filestore performance metrics in a Cloud Monitoring
dashboard, follow these steps:

- 

In the Cloud de Confiance console, go to the
*leaderboard* **Metrics explorer** page:


[Go to **Metrics explorer**](https://console.cloud.s3nscloud.fr/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is
**Monitoring**.

- Click the **Select a metric** expandable section.

- In the **Filter by resource or metric name** field, type `filestore` and
select the **Filestore Instance** expandable section.

- Select an available metric to view:




| 
Metric | 
Description | 
Basic tiers | 
Regional, zonal, and enterprise tiers | 
|



| 
**Average read latency** | 
The average time a read operation takes (in milliseconds). | 
| 
✓ | 
|

| 
**Average write latency** | 
The average time a write operation takes (in milliseconds). | 
| 
✓ | 
|

| 
**Bytes written** | 
Number of bytes written. | 
✓ | 
✓ | 
|

| 
**Bytes read** | 
Number of bytes read from persistent storage. This can be less than the
number of bytes read by clients, as some reads might be served from a memory
cache. * | 
✓ | 
✓ | 
|

| 
**Disk read operation count** | 
Number of disk read operations. If the Filestore instance
caches the data, some read operations are not reflected as disk reads.
* | 
✓ | 
✓ | 
|

| 
**Disk write operation count** | 
Number of disk write operations. If the Filestore instance
caches the data, some write operations are not reflected as disk writes.
* | 
✓ | 
✓ | 
|

| 
**Metadata operations count** | 
Number of disk metadata operations. | 
| 
✓ | 
|

| 
**Free bytes** | 
Number of free disk bytes. | 
✓ | 
✓ | 
|

| 
**Free disk space percent** | 
Percentage of free disk bytes. | 
✓ | 
✓ | 
|

| 
**[Free raw capacity percent](#free-raw-capacity-percent)** | 
Free raw capacity as a percentage of total space. | 
| 
✓ | 
|

| 
**Procedure call count** | 
Returns the same information as the [nfsstat -s](https://linux.die.net/man/8/nfsstat) command. | 
✓ | 
| 
|

| 
**[Snapshots used bytes](#snapshots-used-bytes)** | 
The amount of space used for storing snapshots, measured in bytes. | 
| 
✓ | 
|

| 
**Time (in milliseconds) spent on read operations** | 
Time spent on disk reads. | 
✓ | 
| 
|

| 
**Time (in milliseconds) spent on write operations** | 
Time spent on disk writes. | 
✓ | 
| 
|

| 
**Used bytes** | 
Number of used disk bytes. | 
✓ | 
✓ | 
|

| 
**Used space percent** | 
Percentage of used disk bytes. | 
✓ | 
✓ | 
|



* Memory-cached operations only occur in basic tier instances.

- 

Optional configurations:



| 
Field | 
Description | 
|




| 
[**Filter**](/monitoring/charts/metrics-selector#filter-option) | 
Filter to the Filestore instances that you want to monitor. | 
|

| 
[**Group by**](/monitoring/charts/metrics-selector#groupby-option) | 
Combining data from similar time series. | 
|

| 
[**Aggregator**](/monitoring/charts/metrics-selector#groupby-option) | 
Combine time series using common functions. | 
|

| 
[**Minimum alignment period**](/monitoring/charts/metrics-selector#alignment) | 
The time interval for which aggregation takes place. | 
|



- 

If you want to add more metrics to the chart, click **Add another metric**.

- 

Click **Save Chart** to create a dashboard. Alternatively, you can add the
chart to an existing dashboard.

## Metric definitions

The following sections describe certain Filestore-specific metrics
in detail.

### Free raw capacity percent

The [free raw capacity percent](/monitoring/api/metrics_gcp_d_h#gcp-file)
metric represents capacity available to users, not necessarily the available
raw disk space.

Your instance replicates data to provide durability and to help support
performance, resulting in a total storage capacity greater than the
user-specified capacity of the instance.

The free raw capacity percent metric represents the percentage of free raw
capacity available to users after any replication performed as a function of
instance durability or performance.

If this metric reaches 0%, new data cannot be written to the cluster until more
free space becomes available.

For more information on how to scale instance capacity up or down, see
[Scale capacity](/filestore/docs/scale).

### Snapshots used bytes

The [snapshots used bytes](/monitoring/api/metrics_gcp_d_h#gcp-file) metric
represents the number of bytes in use by all snapshots, whether internal or
external. This metric is allocated and indexed by share, not instance.

### Used bytes

The [used bytes](/monitoring/api/metrics_gcp_d_h#gcp-file) metric represents the
raw data written by the user. It doesn't take into account the space required
for [inodes](/filestore/docs/scale#inode-usage) and metadata.



### Anticipating capacity

For a better understanding of an instance's available capacity, we recommend
monitoring the available space as well as the written space.

To see the free space on an instance, use the [free raw capacity percent](#free-raw-capacity-percent)
metric.

Each file stored on the file share consumes one inode. If the file system runs
out of inodes, you won't be able to store more files on the file share even
if you haven't reached the maximum allocated capacity.

To see the number of inodes in use, use the `df` command. For more information,
see [Scale capacity](/filestore/docs/scale) and [Troubleshoot capacity issues](/filestore/docs/capacity-issues).

## Set up alerts



### Low disk space

To ensure that your Filestore instances don't run out of free
space, we recommend setting up low disk space alerts.
This guide uses the **free disk space percent** metric to measure the free disc space for basic instances.

If you want to measure low disk space for zonal, regional, or enterprise instances, use the following steps to set up two separate alerts using **free disk space percent** and **free raw capacity percent** metrics.

- 

In the Cloud de Confiance console, go to the
*notifications* **Alerting** page:


[Go to **Alerting**](https://console.cloud.s3nscloud.fr/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is
**Monitoring**.

- Click **Create Policy**.

- Click the **Select a metric** expandable section.

- In the **Filter by resource or metric name** field, type `filestore` and
select the **Filestore Instance** expandable section.

- Select the **Nfs** active metric category.

- Select the metric **Free disk space percent**.

- Click **Apply**.

- In the **Add filters** section, click **Add a filter**.

- Click the **Filter** expandable section and select **instance_name**.

- In the **Value** field, enter the Filestore instance name
for which you want to receive alerts.

- 

Click **Done**.

For more information about filtering Cloud Monitoring metrics, see
[Filtering](/monitoring/charts/metrics-selector#filter-option).

- 

In the **Transform data** section, specify the **Rolling window** and
**Rolling window function**. Indicate whether you want to include a
secondary data transformation and click **Next**.

- 

In the **Configure alert trigger** window, choose a condition type.

- 

Set the following specifications:



| 
Field | 
Configuration | 
|




| 
**Alert trigger** | 
**Any time series violates** | 
|

| 
**Threshold position** | 
**Below threshold** | 
|

| 
**Threshold value** | 
Enter the lowest acceptable free disk space percentage for each of your Filestore instances. | 
|



You can test the alert by setting a low limit and seeing whether the alert
gets triggered.

For more information, see [Default create alerting policy flow](/monitoring/alerts/using-alerting-ui#default).

- 

Enter any advanced options.

- 

In the **Condition name** field, enter a name for the condition.

- 

Click **Next**.

- 

In the **Configure notifications and finalize alert** window, indicate
which notification channels you want to use.

For information on how to create new channels, see [Manage notification
channels](/monitoring/support/notification-options).

- 

In the **Incident autoclose duration** menu, select the duration you want
to use.

- 

In the **Policy user labels** section, indicate the labels you want to use.

- 

In the **Documentation** section, add any documentation you want to include 
such as instructions on how to address the issue.

- 

In the **Alert policy name** field, enter an alert policy name and click
**Next**.

- 

Click **Create policy**.



### Low backups quota

If you are scheduling or automating backups creation for your
Filestore instances, you should set up alerts for when you're
running low on backups quota.

- 

In the Cloud de Confiance console, go to the
*notifications* **Alerting** page:


[Go to **Alerting**](https://console.cloud.s3nscloud.fr/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is
**Monitoring**.

- Click **Create Policy**.

- Click the **Select a metric** expandable section.

- In the **Filter by resource or metric name** field, type `quota` and
select the **Consumer quota** expandable section.

- Select the **Quota** active metric category.

- Select the metric **Allocation quota usage**.

- Click **Apply**.

- In the **Add filters** section, click **Add Filter**.

- Click the **Filter** expandable section and select **quota_metric**.

- In the **Value** field, enter `file.googleapis.com/backups-per-region`.

- Click **Done**.

- 

Optional: To add another filter, click **Add filter** and repeat the
process.

For more information about filtering Cloud Monitoring metrics, see
[Filtering](/monitoring/charts/metrics-selector#filter-option).

- 

In the **Transform data** section, specify the **Rolling window** and
**Rolling window function**. Indicate whether you want to include a
secondary data transformation and click **Next**.

- 

In the **Configure alert trigger** window, choose a condition type.

- 

Set the following specifications:



| 
Field | 
Configuration | 
|




| 
**Alert trigger** | 
**Any time series violates** | 
|

| 
**Threshold position** | 
**Below threshold** | 
|

| 
**Threshold value** | 
Enter the lowest acceptable backups quota remaining. | 
|



You can test the alert by setting a low limit and seeing whether the alert
gets triggered.

For more information, see [Default create alerting policy flow](/monitoring/alerts/using-alerting-ui#default).

- 

Enter any advanced options.

- 

In the **Condition name** field, enter a name for the condition.

- 

Click **Next**.

- 

In the **Configure notifications and finalize alert** window, indicate
which notification channels you want to use.

For information on how to create new channels, see [Manage notification
channels](/monitoring/support/notification-options).

- 

In the **Incident autoclose duration** menu, select the duration you want
to use.

- 

In the **Policy user labels** section, indicate the labels you want to use.

- 

In the **Documentation** section, add any documentation you want to include
such as instructions on how to address the issue, for example, "Delete older
backups" or "Request additional quota".

- 

In the **Alert policy name** field, enter an alert policy name and click
**Next**.

- 

Click **Create policy**.




## What's next

- [Request a quota increase](/filestore/docs/requesting-quota-increases).

- [Understand capacity errors](/filestore/docs/known-issues#capacity_errors_before_reaching_full_provisioned_capacity).

- [Optimize and test instance performance](/filestore/docs/performance).

- [Scale capacity](/filestore/docs/scale).