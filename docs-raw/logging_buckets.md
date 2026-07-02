# Configure log buckets

Source: https://berlin.devsitetest.how/logging/docs/buckets
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/logging/docs/tpc-differences) for more details.














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

Observability

](https://berlin.devsitetest.how/docs/observability)






- 








[

Cloud Logging

](https://berlin.devsitetest.how/logging/docs)






- 








[

Guides

](https://berlin.devsitetest.how/logging/docs/overview)












# Configure log buckets 






- On this page ** 
- [ Before you begin ](#before-you-begin)
- [ Create a bucket ](#create_bucket)
- [ Manage buckets ](#manage_buckets)

- [ Update a bucket ](#update_bucket)
- [ Lock a bucket ](#locking-logs-buckets)
- [ List buckets ](#listing-log-buckets)
- [ View a bucket's details ](#viewing-logs-buckets)
- [ Delete a bucket ](#deleting-logs-bucket)
- [ Restore a deleted bucket ](#restore-logs-bucket)

- [ Write to a bucket ](#writing)
- [ Read from a bucket ](#reading)
- [ Configure custom retention ](#custom-retention)
- [ Troubleshoot common issues ](#troubleshooting)
- [ What's next ](#whats_next)
- 









This document describes how to create and manage Cloud Logging buckets using
the Google Cloud Dedicated console, the [Google Cloud CLI](/sdk/docs), and the
[Logging API](/logging/docs/reference/v2/rest/v2/projects.locations.buckets).
It also provides instructions for creating and managing log buckets at the
Google Cloud Dedicated project level. You can't create log buckets at the folder
or organization level; however, Cloud Logging automatically creates
`_Default` and `_Required` log buckets at the folder and organization level for
you.

For a conceptual overview of buckets, see
[Routing and storage overview: Log buckets](/logging/docs/store-log-entries).

This document doesn't describe how to create a log bucket that uses a
customer-managed encryption key (CMEK). If you are interested in that topic,
then see
[Configure CMEK for logs storage](/logging/docs/routing/managed-encryption-storage).

## Before you begin 

To get started with buckets, do the following:


- Configure your Google Cloud Dedicated project:



- 




[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).





- 


































To get the permissions that
you need to create, upgrade, and link a log bucket,

ask your administrator to grant you the
[Logs Configuration Writer ](/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) IAM role on your project.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).











For the full list of permissions and roles, see
[Access control with IAM](/logging/docs/access-control).








- Understand the [supported regions](/logging/docs/region-support#bucket-regions)
in which you can store your logs.


- 















Select the tab for how you plan to use the samples on this page:











[Console](#console) [gcloud](#gcloud) [REST](#rest) 
More 







When you use the Google Cloud Dedicated console to access Google Cloud Dedicated in Germany services and
APIs, you don't need to set up authentication.

































[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).

After signing in,
[initialize](/sdk/docs/initializing) the Google Cloud CLI by running the following command:





```
gcloud init
```



































































To use the REST API samples on this page in a local development environment, you use the
credentials you provide to the gcloud CLI.












[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


















For more information, see
[Authenticate for using REST](/docs/authentication/rest)
in the Google Cloud Dedicated authentication documentation.


















- If you plan to use the Google Cloud CLI or Cloud Logging API to
create or manage your log buckets, then understand the
[`LogBucket`](/logging/docs/reference/v2/rest/v2/locations.buckets) formatting requirements.


## Create a bucket

You can create a maximum of 100 buckets per
Google Cloud Dedicated project. You can't create log buckets in folders or
organizations.

To create a user-defined log bucket for your Google Cloud Dedicated project, do the
following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) [ REST ](#rest) 
More 




To create a log bucket in your Google Cloud Dedicated project, do the following:

- 

In the Google Cloud Dedicated console, go to the Logs Storage** page:


[Go to **Logs Storage**](https://console.cloud.berlin-build0.goog/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

Click **Create log bucket**.

- 

Enter a **Name** and **Description** for your bucket.

- 

To select the storage [region](/logging/docs/region-support#bucket-regions)
for your logs, click the **Select log bucket region** menu and select a
region.

- 

Optional: To set a [custom retention](#custom-retention) period for the
logs in the bucket, click **Next**.

In the **Retention period** field, enter the number of days, between
1 day and
400 days, that you want Cloud Logging to
retain your logs. If you don't customize the retention period, the default
is `30 days`.

You can also update the retention period for your log bucket
after you create it.

- 

Click **Create bucket**.

It might take a moment for these steps to complete.




To create a log bucket,
run the [`gcloud logging buckets create`](/sdk/gcloud/reference/logging/buckets/create) command:


```
gcloud logging buckets create ** BUCKET_ID --location= LOCATION 
```


For example, if you want to create a bucket with the BUCKET_ID 
`my-bucket` in the `global` region, your command would look like the
following:


```
gcloud logging buckets create my-bucket --location global --description "My first bucket"
```





To create a bucket, use the
[`projects.locations.buckets.create`](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/create)
method. Prepare the arguments to the method as follows:

- 

Set the `parent` parameter to be the resource in which
to create the bucket:
`projects/ PROJECT_ID /locations/ LOCATION `

The variable LOCATION refers to the
[region](/logging/docs/region-support#bucket-regions) in which you
want your logs to be stored.

For example, if you want to create a bucket for project `my-project` in
the in the `global` region, your `parent` parameter would look like
this: `projects/my-project/locations/global`

- 

Set the `bucketId` parameter; for example, `my-bucket`.

- 

Call the synchronous method
[`projects.locations.buckets.create`](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/create)
to create the bucket.




After creating a bucket, create a sink to route log entries to your bucket and
[configure log views](/logging/docs/logs-views) to control who can access the logs in
your bucket and which logs they can view. You can also update the bucket to
configure [custom retention](#custom-retention).

## Manage buckets

This section describes how to manage your log buckets using the Google Cloud CLI
or the Google Cloud Dedicated console.

### Update a bucket

To update the properties of your bucket, such as the
description or retention period, do the following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) [ REST ](#rest) 
More 




To update your bucket's properties, do the following:

- 

In the Google Cloud Dedicated console, go to the Logs Storage** page:


[Go to **Logs Storage**](https://console.cloud.berlin-build0.goog/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

For the bucket you want to update, click *more_vert* **More**.

- 

Select **Edit bucket**.

- 

Edit your bucket as needed.

- 

Click **Update bucket**.




To update your bucket's properties, run the
[`gcloud logging buckets update`](/sdk/gcloud/reference/logging/buckets/update) command:


```
gcloud logging buckets update ** BUCKET_ID --location= LOCATION UPDATED_ATTRIBUTES 
```


For example:


```
gcloud logging buckets update my-bucket --location=global --description "Updated description"
```



To update your bucket's properties, use
[`projects.locations.buckets.patch`](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch)
in the Logging API.



### Lock a bucket

When you lock a bucket against updates, you also lock the bucket's
retention policy. After a retention policy is locked, you can't delete the
bucket until every log entry in the bucket has fulfilled the bucket's retention
period. If you want to prevent the accidental deletion of a project that
contains a locked log bucket, then add a lien to the project.
To learn more, see [Protecting projects with liens](/resource-manager/docs/project-liens).

To prevent anyone from updating or deleting a log bucket, lock the bucket. To
lock the bucket, do the following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) [ REST ](#rest) 
More 




The Google Cloud Dedicated console doesn't support locking a log bucket.



To lock your bucket, run the [`gcloud logging buckets update`](/sdk/gcloud/reference/logging/buckets/update)
command with the `--locked` flag:


```
gcloud logging buckets update BUCKET_ID --location= LOCATION --locked
```


For example:


```
gcloud logging buckets update my-bucket --location=global --locked
```



To lock your bucket's attributes, use
[`projects.locations.buckets.patch`](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch)
in the Logging API. Set the `locked` parameter to `true`.



### List buckets

To list the log buckets associated with a Google Cloud Dedicated project, and to see
details such as retention settings, do the following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) [ REST ](#rest) 
More 




In the Google Cloud Dedicated console, go to the Logs Storage** page:


[Go to **Logs Storage**](https://console.cloud.berlin-build0.goog/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

A table named **Log buckets** lists the buckets associated with the current
Google Cloud Dedicated project.

The table lists the following attributes for each log bucket:

- **Name**: The name of the log bucket.

- **Description**: The description of the bucket.

- **Retention period**: The number of days that the bucket's data will
be stored by Cloud Logging.

- **Region**: The geographic location in which the bucket's data is stored.

- **Status**: Whether the bucket is [locked](#locking-logs-buckets) or
unlocked.

If a bucket is pending [deletion](#deleting-logs-bucket) by Cloud Logging,
then its table entry is annotated with a *warning* **warning**
symbol.



Run the [`gcloud logging buckets list`](/sdk/gcloud/reference/logging/buckets/list) command:


```
gcloud logging buckets list
```


You see the following attributes for the log buckets:

- `LOCATION`: The [region](/logging/docs/region-support#bucket-regions)
in which the bucket's data is stored.

- `BUCKET_ID`: The name of the log bucket.

- `RETENTION_DAYS`: The number of days that the bucket's data will be
stored by Cloud Logging.

- `LIFECYCLE_STATE`: Indicates whether the bucket is pending
[deletion](#deleting-logs-bucket) by Cloud Logging.

- `LOCKED`: Whether the bucket is [locked](#locking-logs-buckets) or
unlocked.

- `CREATE_TIME`: A timestamp that indicates when the bucket was created.

- `UPDATE_TIME`: A timestamp that indicates when the bucket was last
modified.

You can also view the attributes for just one bucket. For example, to view
the details for the `_Default` log bucket in the `global` region, run the
[`gcloud logging buckets describe`](/sdk/gcloud/reference/logging/buckets/describe) command:


```
gcloud logging buckets describe _Default --location=global
```



To list the log buckets associated with a Google Cloud Dedicated project, use
[`projects.locations.buckets.list`](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/list)
in the Logging API.



### View a bucket's details

To view the details of a single log bucket, do the following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) [ REST ](#rest) 
**More 




In the Google Cloud Dedicated console, go to the Logs Storage** page:


[Go to **Logs Storage**](https://console.cloud.berlin-build0.goog/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

On the log bucket, click *more_vert* **More** and then
select **View bucket details**.

The dialog lists the following attributes for the log bucket:

- **Name**: The name of the log bucket.

- **Description**: The description of the log bucket.

- **Retention period**: The number of days that the bucket's data will
be stored by Cloud Logging.

- **Region**: The geographic location in which the bucket's data is stored.




Run the [`gcloud logging buckets describe`](/sdk/gcloud/reference/logging/buckets/describe) command.

For example, the following command reports the details of the `_Default`
bucket:


```
gcloud logging buckets describe _Default --location=global
```


You see the following attributes for the log bucket:

- `createTime`: A timestamp that indicates when the bucket was created.

- `description`: The description of the log bucket.

- `lifecycleState`: Indicates whether the bucket is pending
[deletion](#deleting-logs-bucket) by Cloud Logging.

- `name`: The name of the log bucket.

- `retentionDays`: The number of days that the bucket's data will be
stored by Cloud Logging.

- `updateTime`: A timestamp that indicates when the bucket was last
modified.




To view the details of a single log bucket, use
[`projects.locations.buckets.get`](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/get)
in the Logging API.



### Delete a bucket

You can delete log buckets that satisfy one of the following:

- The log bucket is [unlocked](#locking-logs-buckets).

- The log bucket is [locked](#locking-logs-buckets) and all log entries in
the log bucket have fulfilled the bucket's retention period.

You can't delete a log bucket that is locked against updates
when that log bucket stores log entries that haven't fulfilled the bucket's
retention period.

After you issue the delete command, the log bucket transitions to the
[`DELETE_REQUESTED` state](/logging/docs/reference/v2/rest/v2/LifecycleState), and it stays in that state
for 7 days. During this time period, Logging continues to
route logs to the log bucket. You can stop routing logs to the log bucket
by deleting or modifying the log sinks that route log entries to the bucket.

You can't create a new log bucket that uses the same name as a log bucket
that is in the `DELETE_REQUESTED` state.

To delete a log bucket, do the following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) [ REST ](#rest) 
**More 




To delete a log bucket, do the following:

- 

In the Google Cloud Dedicated console, go to the Logs Storage** page:


[Go to **Logs Storage**](https://console.cloud.berlin-build0.goog/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

Locate the bucket that you want to delete, and click
*more_vert***More**.

- 

Select **Delete bucket**.

- 

On the confirmation panel, click **Delete**.

- 

On the **Logs Storage** page, your bucket has an indicator that it's
pending deletion. The bucket, including all the logs in it, is deleted
after 7 days.




To delete a log bucket, run the
[`gcloud logging buckets delete`](/sdk/gcloud/reference/logging/buckets/delete) command:


```
gcloud logging buckets delete ** BUCKET_ID --location= LOCATION 
```


You can't delete a log bucket when that bucket has a linked
BigQuery dataset:

- To list the links associated with a log bucket, run the
[`gcloud logging links list`](/sdk/gcloud/reference/logging/links/list) command.

- To delete a linked dataset, run the
[`gcloud logging links delete`](/sdk/gcloud/reference/logging/links/delete) command.




To delete a bucket, use
[`projects.locations.buckets.delete`](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/delete)
in the Logging API.




### Restore a deleted bucket

You can restore, or undelete, a log bucket that's in the pending deletion state.
To restore a log bucket, do the following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) [ REST ](#rest) 
More 




To restore a log bucket that is pending deletion, do the following:

- 

In the Google Cloud Dedicated console, go to the Logs Storage** page:


[Go to **Logs Storage**](https://console.cloud.berlin-build0.goog/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

For the bucket you want to restore,
click *more_vert* **More**, and then select
**Restore deleted bucket**.

- 

On the confirmation panel, click **Restore**.

- 

On the **Logs Storage** page, the pending-deletion indicator is removed
from your log bucket.




To restore a log bucket that is pending deletion, run the
[`gcloud logging buckets undelete`](/sdk/gcloud/reference/logging/buckets/undelete) command:


```
gcloud logging buckets undelete ** BUCKET_ID --location= LOCATION 
```



To restore a bucket that is pending deletion, use
[`projects.locations.buckets.undelete`](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/undelete)
in the Logging API.



## Write to a bucket

You don't directly write logs to a log bucket. Rather, you write logs to
Google Cloud Dedicated resource: a Google Cloud Dedicated project, folder, or organization.
The sinks in the parent resource then route the logs to destinations, including
log buckets. A sink routes logs to a log bucket destination when the logs match
the sink's filter and the sink has permission to route the logs to the log
bucket.

## Read from a bucket

Each log bucket has a set of log views. To read logs from a log bucket, you
need access to a log view on the log bucket. Log views let you grant a user
access to only a subset of the logs stored in a log bucket. For information
about how to configure log views, and how to grant access to specific log views,
see [Configure log views on a log bucket](/logging/docs/logs-views).

To read logs from a log bucket, do the following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) [ REST ](#rest) 
More 




- 

In the Google Cloud Dedicated console, go to the
segment 
Logs Explorer** page:


[Go to **Logs Explorer**](https://console.cloud.berlin-build0.goog/logs/query)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

To customize which logs are displayed in the Logs Explorer,
click **Refine scope**, and then select an option. For example,
you can view logs stored in a project or by log view.

- 

Click **Apply**. The **Query results** pane reloads with logs that match
the option you selected.

For more information, see
[Logs Explorer overview: Refine scope](/logging/docs/view/logs-explorer-interface#refine_scope).



To read logs from a log bucket, use the
[`gcloud logging read`](/sdk/gcloud/reference/logging/read) command and add
a [`LOG_FILTER`](/sdk/gcloud/reference/logging/read#LOG_FILTER) to select
data:


```
gcloud logging read ** LOG_FILTER --bucket= BUCKET_ID --location= LOCATION --view= LOG_VIEW_ID 
```



To read logs from a log bucket, use the
[entries.list](/logging/docs/reference/v2/rest/v2/entries/list) method. Set
`resourceNames` to specify the appropriate bucket and log view, and set
`filter` to select data.



For detailed information about the filtering syntax, see
[Logging query language](/logging/docs/view/logging-query-language).

## Configure custom retention

When you [create a log bucket](#create_bucket), you can customize the period
that Cloud Logging stores logs in the bucket. You can also configure the
retention period for the `_Default` log bucket when that log bucket is in a
project.

You can't change the retention period of the `_Required` log bucket. You also
can't extend the retention period of a log bucket that is in a folder or
organization. However, you can create a log sink to route
folder- or organization-level log entries to a log bucket that is in a project,
and then configure the retention period of that log bucket.

If you shorten the retention period of a log bucket, then there is a 7-day grace
period in which expired logs aren't deleted. You can't query or view the expired
logs. However, during this 7-day period, you can restore full access by
extending the bucket's retention period. Logs stored during the grace period
count toward your retention costs.

Retention enforcement is an eventually-consistent process. If you write
log entries to a log bucket when the log entries are older than the bucket's
retention period, then you might be able to briefly see these log entries.
For example, if you send log entries that are 10 days old to a log bucket
with a retention period of 7 days, then those log entries are stored and then
eventually purged. These log entries don't contribute to your retention
costs. They do contribute to your storage costs. To minimize your storage
costs, don't write log entries that are older than your bucket's
retention period.

To update the retention period for a custom log bucket or for the
`_Default` log bucket that is in a project, do the following:


[ Google Cloud Dedicated console ](#google-cloud-dedicated-console) [ gcloud ](#gcloud) 
More 




To update a log bucket's retention period, do the following:

- 

In the Google Cloud Dedicated console, go to the Logs Storage** page:


[Go to **Logs Storage**](https://console.cloud.berlin-build0.goog/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

For the bucket you want to update,
click *more_vert* **More**, and then select
**Edit bucket**.

- 

In the **Retention** field, enter the number of days, between
1 day and
400 days, that you want Cloud Logging to
retain your logs.

- 

Click **Update bucket**. Your new retention period appears in the
**Logs bucket** list.




To update the retention period for a user-defined log bucket or for the
`_Default` log bucket that is in a project, run the
[`gcloud logging buckets update`](/sdk/gcloud/reference/logging/buckets/update) command, after setting a value for
RETENTION_DAYS :


```
gcloud logging buckets update ** BUCKET_ID --location= LOCATION --retention-days= RETENTION_DAYS 
```


For example, to retain the logs in the `_Default` bucket in the
`global` location for a year, your command would look like the following:


```
gcloud logging buckets update _Default --location=global --retention-days=365
```



If you extend a bucket's retention period, then the retention rules apply going
forward and not retroactively. Logs can't be recovered after the applicable
retention period ends.

## Troubleshoot common issues

If you encounter problems when using log buckets, refer to the following
troubleshooting steps and answers to common questions.

### Why can't I delete this bucket?

If you're trying to delete a bucket, do the following:

- 

Verify that you have the correct permissions to delete the bucket. For the
list of the permissions that you need, see
[Access control with IAM](/logging/docs/access-control).

- 

Determine whether the bucket is locked by
[listing the bucket's attributes](#listing-log-buckets). If the bucket is
locked, check the bucket's
[retention period](#custom-retention). You can't delete a locked bucket until
all of the logs in the bucket have fulfilled the bucket's retention period.

### Which service accounts are routing logs to my bucket?

To determine if any service accounts have IAM permissions to
route logs to your bucket, do the following:

- 

In the Google Cloud Dedicated console, go to the IAM** page:


[Go to **IAM**](https://console.cloud.berlin-build0.goog/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is
**IAM & Admin**.

- 

From the **Permissions** tab, view by **Roles**. You see a table with all
the IAM roles and principals associated with your
Google Cloud Dedicated project.

- 

In the table's **Filter**
**text box*** filter_list*,
enter **Logs Bucket Writer**.

You see any principals with the **Logs Bucket Writer** role. If a principal
is a service account, its ID contains the string `eu0-system.iam.gserviceaccount.com`.

- 

Optional: If you want to remove a service account from being able to route
logs to your Google Cloud Dedicated project, select the
**check box*** check_box_outline_blank*
for the service account and click **Remove**.

### Why do I see logs for a Google Cloud Dedicated project even though I excluded them from my `_Default` sink?

You might be viewing logs in a log bucket in a
[centralized Google Cloud Dedicated project](/logging/docs/central-log-storage), which
aggregates logs from across your organization.

If you're using the Logs Explorer to access these logs and see logs that you
excluded from the `_Default` sink, then your view might be set to the
Google Cloud Dedicated project level.

To fix this issue, select **Log view** in the
[Refine scope](/logging/docs/view/logs-explorer-interface#refine_scope) menu
and then select the log view associated with the `_Default` bucket in your
Google Cloud Dedicated project. You shouldn't see the excluded logs anymore.

## What's next

For information on the log bucket API methods, refer to the
[`LogBucket`](/logging/docs/reference/v2/rest/v2/locations.buckets) reference documentation.

If you manage an organization or a folder, then you can specify the location of
the `_Default` and `_Required` log buckets of child resources. You can also
configure whether log buckets use CMEK and the behavior of the
`_Default` log sink. For more information, see
[Configure default settings for organizations and folders](/logging/docs/default-settings).

For information on addressing common use cases with log buckets, see the
following topics:

- [Aggregate and store your organization's logs](/logging/docs/central-log-storage).

- [Regionalize your logs](/logging/docs/regionalized-logs).