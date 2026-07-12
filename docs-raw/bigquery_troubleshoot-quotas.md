# Troubleshoot quota and limit errors

Source: https://berlin.devsitetest.how/bigquery/docs/troubleshoot-quotas
Last updated: 2026-07-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/bigquery/docs/tpc-differences) for more details.














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

Data analytics

](https://berlin.devsitetest.how/docs/data)






- 








[

BigQuery

](https://berlin.devsitetest.how/bigquery/docs)






- 








[

Reference

](https://berlin.devsitetest.how/bigquery/quotas)

















- On this page 
- [ Overview ](#overview)
- [ Diagnosis ](#diagnosis)
- [ Troubleshoot quotas or limits that can be increased ](#troubleshoot_quotas_or_limits_that_can_be_increased)

- [ Your project exceeded quota for free query bytes scanned ](#your_project_exceeded_quota_for_free_query_bytes_scanned)
- [ Streaming insert quota errors ](#ts-streaming-insert-quota)
- [ Maximum number of concurrent queries that contain remote functions ](#ts-maximum-number-of-concurrent-remote-functions)
- [ Maximum number of CREATE MODEL statements ](#maximum_number_of_create_model_statements)
- [ Maximum number of copy jobs per day per project quota errors ](#ts-maximum-number-of-copy-jobs-per-day-per-project-quota)
- [ Exceeded extract bytes per day quota error ](#ts-exceeded-extract-bytes-per-day-quota)
- [ Maximum tabledata.list bytes per second per project quota errors ](#ts-maximum-tabledata-list-bytes-per-second-per-project-quota)
- [ Maximum number of API requests limit errors ](#ts-maximum-api-request-limit)
- [ Maximum Python UDF image storage bytes per project per region ](#ts-maximum-python-udf-storage)
- [ Maximum concurrent Python UDFs ](#ts-max-concurrent-python-udfs)

- [ Troubleshoot quotas or limits that can't be increased ](#troubleshoot_quotas_or_limits_that_cant_be_increased)

- [ Maximum number of pending jobs errors ](#ts-max-pending-jobs)
- [ Query queue limit errors ](#ts-query-queue-limit)
- [ Shuffle size limit errors ](#ts-shuffle-limit-errors)
- [ Number of partition modifications for column-partitioned tables quota errors ](#ts-number-column-partition-quota)
- [ Maximum rate of table metadata update operations limit errors ](#ts-maximum-update-table-metadata-limit)
- [ Table imports or query appends quota errors ](#ts-table-import-quota)
- [ Quota exceeded for quota metric 'Authorized Views per dataset' and limit '2500'. ](#quota_exceeded_for_quota_metric_authorized_views_per_dataset_and_limit_2500)
- [ Too many DML statements outstanding against table ](#ts-too-many-dml-statements-against-table-quota)
- [ Loading CSV files quota errors ](#ts-load-csv-files-quota)
- [ Your user exceeded quota for concurrent project.lists requests ](#your_user_exceeded_quota_for_concurrent_projectlists_requests)

- 









# Troubleshoot quota and limit errors 



BigQuery has various [quotas and limits](/bigquery/quotas)
that limit the rate and volume of different requests and operations. They exist
both to protect the infrastructure and to help guard against unexpected
customer usage. This document describes how to diagnose and mitigate
specific errors resulting from quotas and limits.

Some error messages specify quotas or limits that you can increase, while other
error messages specify quotas or limits that you can't increase. Reaching a hard
limit means that you need to implement temporary or permanent workarounds or
best practices for your workload. Doing so is a best practice, even for quotas
or limits that can be increased.

This document organizes error messages and their solutions according to these
categories, and the "Overview" section later in this document explains how to
read an error message and apply the correct solution for your issue.

If your error message is not listed in this document, then refer to
[the list of error messages](/bigquery/docs/error-messages), which has more
generic error information.

## Overview

If a BigQuery operation fails because of exceeding a quota, the API
returns the HTTP `403 Forbidden` status code. The response body contains more
information about the quota that was reached. The response body looks similar to
the following:


```
{ 
"code" : 403 , 
"errors" : [ { 
"domain" : "global" , 
"message" : "Quota exceeded: ..." , 
"reason" : "quotaExceeded" 
} ], 
"message" : "Quota exceeded: ..." 
} 
```


The `message` field in the payload describes which limit was exceeded. For
example, the `message` field might say `Exceeded rate limits: too many table
update operations for this table`.

In general, quota limits fall into two categories, indicated by the `reason`
field in the response payload.

- 

**`rateLimitExceeded`.** This value indicates a short-term
limit. To resolve these limit issues, retry the operation after a few seconds.
Use *exponential backoff* between retry attempts. That is, exponentially
increase the delay between each retry.

- 

**`quotaExceeded`.** This value indicates a longer-term limit. If you reach a
longer-term quota limit, you should wait 10 minutes or longer before trying
the operation again. If you consistently reach one of these longer-term
quota limits, you should analyze your workload for ways to mitigate the
issue. Mitigations can include optimizing your workload or requesting a
quota increase.

For `quotaExceeded` errors, examine the error message to understand which quota
limit was exceeded. Then, analyze your workload to see if you can avoid reaching
the quota.

In some cases, the quota can be raised by
[contacting BigQuery support](/bigquery/docs/getting-support) or
[contacting Google Cloud Dedicated in Germany sales](https://berlin.devsitetest.how/contact),
but we recommend trying the suggestions in this document first.

## Diagnosis

To diagnose issues, do the following:

- 

Use [`INFORMATION_SCHEMA` views](/bigquery/docs/information-schema-tables) along with a
[region qualifier](/bigquery/docs/information-schema-intro#region_qualifier) to analyze the underlying issue. These views contain metadata about your BigQuery
resources, including jobs, reservations, and streaming inserts.

For example, the following query uses the
[`INFORMATION_SCHEMA.JOBS`](/bigquery/docs/information-schema-jobs) view to list all
quota-related errors within the past day:


```
SELECT 
job_id , 
creation_time , 
error_result 
FROM `region- REGION_NAME ` . INFORMATION_SCHEMA . JOBS 
WHERE creation_time > TIMESTAMP_SUB ( CURRENT_TIMESTAMP , INTERVAL 1 DAY ) AND 
error_result . reason IN ( 'rateLimitExceeded' , 'quotaExceeded' ) 
```


Replace ` REGION_NAME ` with the region of the
project. It must be preceded by `region-`. For example, for the `US`
multi-region, use `region-us`.

- 

View errors in Cloud Audit Logs.

For example, using
[Logs Explorer](/logging/docs/view/logs-explorer-summary), the following query
returns errors with either `Quota exceeded` or `limit` in the message string:


```
resource.type = ("bigquery_project" OR "bigquery_dataset")
protoPayload.status.code ="7"
protoPayload.status.message: ("Quota exceeded" OR "limit")
```


In this example, the status code `7` indicates
[`PERMISSION_DENIED`](/tasks/docs/reference/rpc/google.rpc#code), which
corresponds to the HTTP `403` status code.

For additional Cloud Audit Logs query samples, see [BigQuery
queries](/logging/docs/view/query-library-preview#bigquery-filters).

## Troubleshoot quotas or limits that can be increased

You can increase the following quotas and limits; however, it's best to first
try any suggested workarounds or best practices.

### Your project exceeded quota for free query bytes scanned

BigQuery returns this error when you run a query in the free
usage tier and the account reaches the monthly query limit. For more information about query pricing, see [Free
usage tier](https://berlin.devsitetest.how/bigquery/pricing#free-usage-tier).

**Error message**


```
Your project exceeded quota for free query bytes scanned
```


#### Resolution

To continue using BigQuery, you need to [upgrade the account to a
paid Cloud Billing account](/free/docs/gcp-free-tier#how-to-upgrade).

### Streaming insert quota errors

This section provides tips for troubleshooting quota errors related to
streaming data into BigQuery.

In certain regions, streaming inserts have a higher quota if you don't populate
the `insertId` field for each row. For more information about quotas for
streaming inserts, see [Streaming inserts](/bigquery/quotas#streaming_inserts).
The quota-related errors for BigQuery streaming depend on the
presence or absence of `insertId`.

**Error message**

If the `insertId` field is empty, the following quota error is possible:



| 
Quota limit | 
Error message | 
|




| 
Bytes per second per
project

| 
Your entity with gaia_id: GAIA_ID ,
project: PROJECT_ID in region:
REGION exceeded quota for insert bytes
per second. | 
|



If the `insertId` field is populated, the following quota errors are possible:



| 
Quota limit | 
Error message | 
|




| 
Rows per second per
project
| 
Your project: PROJECT_ID in
REGION exceeded quota for streaming
insert rows per second. | 
|

| 
Rows per second per
table | 
Your table: TABLE_ID exceeded quota for
streaming insert rows per second. | 
|

| 
Bytes per second per
table | 
Your table: TABLE_ID exceeded quota for
streaming insert bytes per second. | 
|



The purpose of the `insertId` field is to deduplicate inserted rows. If multiple
inserts with the same `insertId` arrive within a few minutes' window,
BigQuery writes a single version of the record. However, this
automatic deduplication is not guaranteed. For maximum streaming throughput, we
recommend that you don't include `insertId` and instead use
[manual deduplication](/bigquery/docs/streaming-data-into-bigquery#manually_removing_duplicates).
For more information, see
[Ensuring data consistency](/bigquery/docs/streaming-data-into-bigquery#dataconsistency).

When you encounter this error, [diagnose the issue](#ts-streaming-insert-quota-diagnose)
the issue and then [follow the recommended steps](#ts-streaming-insert-quota-resolution) to resolve it.

#### Diagnosis

Use the [`STREAMING_TIMELINE_BY_*`](/bigquery/docs/information-schema-streaming)
views to analyze the streaming traffic. These views aggregate streaming
statistics over one-minute intervals, grouped by `error_code`. Quota errors appear
in the results with `error_code` equal to `RATE_LIMIT_EXCEEDED` or
`QUOTA_EXCEEDED`.

Depending on the specific quota limit that was reached, look at `total_rows` or
`total_input_bytes`. If the error is a table-level quota, filter by `table_id`.

For example, the following query shows total bytes ingested per minute, and the
total number of quota errors:


```
SELECT 
start_timestamp , 
error_code , 
SUM ( total_input_bytes ) as sum_input_bytes , 
SUM ( IF ( error_code IN ( 'QUOTA_EXCEEDED' , 'RATE_LIMIT_EXCEEDED' ), 
total_requests , 0 )) AS quota_error 
FROM 
`region- REGION_NAME ` . INFORMATION_SCHEMA . STREAMING_TIMELINE_BY_PROJECT 
WHERE 
start_timestamp > TIMESTAMP_SUB ( CURRENT_TIMESTAMP , INTERVAL 1 DAY ) 
GROUP BY 
start_timestamp , 
error_code 
ORDER BY 1 DESC 
```


#### Resolution

To resolve this quota error, do the following:

- 

If you are using the `insertId` field for deduplication, and your project is
in a region that supports the higher streaming quota, we recommend removing the
`insertId` field. This solution might require some additional steps to manually
deduplicate the data. For more information, see
[Manually removing duplicates](/bigquery/docs/streaming-data-into-bigquery#manually_removing_duplicates).

- 

If you are not using `insertId`, or if it's not feasible to remove it, monitor
your streaming traffic over a 24-hour period and analyze the quota errors:

- 

If you see mostly `RATE_LIMIT_EXCEEDED` errors rather than `QUOTA_EXCEEDED`
errors, and your overall traffic is less than 80% of quota, the errors probably
indicate temporary spikes. You can address these errors by retrying the
operation using exponential backoff between retries.

- 

If you are using a Dataflow job to insert data, consider using
load jobs instead of streaming
inserts. For more information, see [Setting the insertion
method](https://beam.apache.org/documentation/io/built-in/google-bigquery/#setting-the-insertion-method).
If you are using Dataflow with a custom I/O connector, consider
using a built-in I/O connector instead. For more information, see [Custom
I/O patterns](https://beam.apache.org/documentation/patterns/custom-io/).

- 

If you see `QUOTA_EXCEEDED` errors or the overall traffic consistently
exceeds 80% of the quota, submit a request for a quota increase. For more
information, see
[Request a quota adjustment](/docs/quotas/help/request_increase).

- 

You might also want to consider replacing streaming inserts with the newer
[Storage Write API](/bigquery/docs/write-api), which has higher throughput,
lower price, and many useful features.

For more information about streaming inserts, see [streaming data into BigQuery](/bigquery/docs/streaming-data-into-bigquery).

### Maximum number of concurrent queries that contain remote functions

BigQuery returns this error when the number of concurrent
queries that contain remote functions exceeds the limit.

To learn more about remote functions limits, see
[Remote functions](/bigquery/quotas#remote_function_limits).

**Error message**


```
Exceeded rate limits: too many concurrent queries with remote functions for
this project
```


This limit can be increased. Try the workarounds and best practices first.

#### Diagnosis

To see limits for concurrent queries that contain [remote
functions](/bigquery/docs/remote-functions), see
[Remote function limits](/bigquery/quotas#remote_function_limits).

#### Resolution

- When using remote functions, adhere to [best practices for remote
functions](/bigquery/docs/remote-functions#best_practices_for_remote_functions).

- You can request a quota increase by contacting
[support](/bigquery/docs/getting-support) or
[sales](https://berlin.devsitetest.how/contact). It might take several days to review and
process the request. We recommend stating the priority, use case, and the
project ID in the request.

### Maximum number of `CREATE MODEL` statements

This error means that you have exceeded the quota for `CREATE MODEL` statements.

**Error message**


```
Quota exceeded: Your project exceeded quota for CREATE MODEL queries per
project.
```


#### Resolution

If you exceed the [quota](/bigquery/quotas#create_model_statements)
for `CREATE MODEL` statements, send an email to
[bqml-feedback@google.com](mailto:bqml-feedback@google.com)
and request a quota increase.

### Maximum number of copy jobs per day per project quota errors

BigQuery returns this error when the number of copy jobs running
in a project has exceeded the daily limit.
To learn more about the limit for copy jobs per day, see
[Copy jobs](/bigquery/quotas#copy_jobs).

**Error message**


```
Your project exceeded quota for copies per project
```


#### Diagnosis

If you'd like to gather more data about where the copy jobs are coming from,
you can try the following:

- 

If your copy jobs are located in a single or only a few regions, you can try
querying the [`INFORMATION_SCHEMA.JOBS`](/bigquery/docs/information-schema-jobs)
table for specific regions. For example:


```
SELECT 
creation_time , job_id , user_email , destination_table . project_id , destination_table . dataset_id , destination_table . table_id 
FROM ` PROJECT_ID ` . `region- REGION_NAME ` . INFORMATION_SCHEMA . JOBS 
WHERE 
creation_time BETWEEN TIMESTAMP_SUB ( CURRENT_TIMESTAMP (), INTERVAL 2 DAY ) AND CURRENT_TIMESTAMP () 
AND job_type = "COPY" 
order by creation_time DESC 
```


You can also adjust the time interval depending on the time range you're interested in.

- 

To see all copy jobs in all regions, you can use the following filter in
Cloud Logging:


```
resource.type="bigquery_resource"
protoPayload.methodName="jobservice.insert"
protoPayload.serviceData.jobInsertRequest.resource.jobConfiguration.tableCopy:*
```


#### Resolution

- If the goal of the frequent copy operations is to create a snapshot of data,
consider using [table snapshots](/bigquery/docs/table-snapshots-intro)
instead. Table snapshots are a cheaper and faster alternative to copying full tables.

- You can request a quota increase by contacting
[support](/bigquery/docs/getting-support) or
[sales](https://berlin.devsitetest.how/contact). It might take several days to review and
process the request. We recommend stating the priority, use case, and the
project ID in the request.

### Exceeded extract bytes per day quota error

BigQuery returns this error when the extraction exceeds the
default 50 TiB daily limit in a project.
For more information about extract job limits, see [Extract jobs](/bigquery/quotas#export_jobs).

**Error message**


```
Your usage exceeded quota for ExtractBytesPerDay
```


#### Diagnosis

If you are exporting a table that is larger than 50 TiB, the export fails because
it [exceeds the extraction limit](/bigquery/quotas#export_jobs).
If you want to
[export table data](/bigquery/docs/partitioned-tables#export_table_data)
for specific table partitions, you can use a
[partition decorator](/bigquery/docs/partitioned-tables#partition_decorators) to
identify the partitions to export.

If you would like to gather usages of exports data over recent days, you can
try the following:

- 

[View the quotas for your project](/docs/quotas/view-manage#view_project_quotas)
with filter criteria such as `Name: Extract bytes per day` or
`Metric: bigquery.googleapis.com/quota/extract/bytes` along with the Show usage
chart to see your usage trend over a few days.

- 

Alternatively you can query [`INFORMATION_SCHEMA.JOBS_BY_PROJECT`](/bigquery/docs/information-schema-jobs)
to see your total extract bytes over a few days. For example, the following
query returns the daily total bytes processed by `EXTRACT` jobs in the past
seven days.


```
SELECT 
TIMESTAMP_TRUNC ( creation_time , DAY ) AS day , 
SUM ( total_bytes_processed ) / POW ( 1024 , 3 ) AS total_gibibytes_processed 
FROM 
`region- REGION_NAME ` . INFORMATION_SCHEMA . JOBS_BY_PROJECT 
WHERE 
creation_time BETWEEN TIMESTAMP_SUB ( CURRENT_TIMESTAMP (), INTERVAL 7 DAY ) AND CURRENT_TIMESTAMP () 
AND job_type = "EXTRACT" 
GROUP BY 1 
ORDER BY 2 DESC 
```


- 

You can then further refine the results by identifying the specific jobs that
are consuming more bytes than expected. The following example returns the top
100 `EXTRACT` jobs which are consuming more than 100 GB processed over the
past seven days.


```
SELECT 
creation_time , 
job_id , 
total_bytes_processed / POW ( 1024 , 3 ) AS total_gigabytes_processed 
FROM 
`region- REGION_NAME ` . INFORMATION_SCHEMA . JOBS_BY_PROJECT 
WHERE 
creation_time BETWEEN TIMESTAMP_SUB ( CURRENT_TIMESTAMP (), INTERVAL 7 DAY ) AND CURRENT_TIMESTAMP () 
AND job_type = "EXTRACT" 
AND total_bytes_processed > ( POW ( 1024 , 3 ) * 100 ) 
ORDER BY 
total_bytes_processed DESC 
LIMIT 100 
```


You can alternatively use the [jobs explorer](/bigquery/docs/admin-jobs-explorer)
with filters like `Bytes processed more than` to filter for high processing jobs
for a specified period of time.

#### Resolution

One method of resolving this quota error is to create a slot
[reservation](/bigquery/docs/reservations-intro#reservations) and
[assign](/bigquery/docs/reservations-workload-management#assignments) your
project into the reservation with the `PIPELINE` job type. This method can
bypass the limit check since it uses your dedicated reservations rather than
a free shared slot pool. If needed, the reservation can be deleted if you want
to use a shared slot pool later on.

For alternative approaches that allow exporting more *than* 50 TiB,
see the notes section in [Extract jobs](/bigquery/quotas#export_jobs).

### Maximum `tabledata.list` bytes per second per project quota errors

BigQuery returns this error when the project number mentioned
in the error message reaches the maximum size of data that can be read through
the `tabledata.list` API call in a project per second. For more information, see
[Maximum `tabledata.list` bytes per minute](/bigquery/quotas#tabledata_list_bytes_per_minute).

**Error message**


```
Your project:[project number] exceeded quota for tabledata.list bytes per second per project
```


#### Resolution

To resolve this error, do the following:

- In general, we recommend trying to stay under this limit. For example, by
spacing out requests over a longer period with delays. If the error doesn't
happen frequently, implementing retries with exponential backoff
solves this issue.

- If the use case expects fast and frequent reading of a large amount of data
from a table, we recommend using [BigQuery Storage Read API](/bigquery/docs/reference/storage)
instead of the `tabledata.list` API.

- 

If the preceding suggestions don't work, you can request a quota increase from
Google Cloud Dedicated console API dashboard by doing the following:

- Go to the [Google Cloud Dedicated console API dashboard](https://console.cloud.berlin-build0.goog/apis/dashboard).

- In the dashboard, filter for Quota: `Tabledata list bytes per minute (default quota)`.

- Select the quota and follow the instructions in [Request a quota adjustment](/docs/quotas/help/request_increase).

It might take several days to review and process the request.

### Maximum number of API requests limit errors

BigQuery returns this error when you reach the rate limit for the
number of API requests to a BigQuery API per user per method—for
example, the [`tables.get` method](/bigquery/docs/reference/rest/v2/tables/get)
calls from a service account, or the
[`jobs.insert` method](/bigquery/docs/reference/rest/v2/jobs/insert) calls from
a different user email.

Most BigQuery API core methods have a maximum of 100 API requests per user
per method; however, some of these core methods can have different rate limits;
for example:

- The [`jobs.get` method](/bigquery/docs/reference/rest/v2/jobs/get)
has a limit of 1000 API requests per user per second.

- The [`projects.list` method](/bigquery/docs/reference/rest/v2/projects/list)
and the [`tables.insert` method](/bigquery/docs/reference/rest/v2/tables/insert)
both have a limit of 10 requests per user per second.

In addition, BigQuery API rate limits [don't apply](/bigquery/quotas#streaming_inserts)
to streaming inserts.

For more information on individual rate limits, see the
[**Maximum number of API requests per second per user per method** rate limit](/bigquery/quotas#api_request_quotas).

**Error message**


```
Quota exceeded: Your user_method exceeded quota for concurrent api requests
per user per method.
```


When you encounter this error, [diagnose](#ts-maximum-api-request-limit-diagnose) the
issue and then [follow the recommended steps](#ts-maximum-api-request-limit-resolution)
to resolve it.

#### Diagnosis

If you have not identified the method that has reached this rate limit, do the
following:

**For service account**

- 

[Go to the project](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)
that hosts the service account.

- 

In the Google Cloud Dedicated console, go to the [API Dashboard](https://console.cloud.berlin-build0.goog/apis/dashboard).

For instructions on how to view the detailed usage information of an API,
see [Using the API Dashboard](/apis/docs/monitoring#using_the_api_dashboard).

- 

In the API Dashboard, select **BigQuery API**.

- 

To view more detailed usage information, select **Metrics**, and then do
the following:

- 

For **Select Graphs**, select **Traffic by API method**.

- 

Filter the chart by the service account's credentials. You might see
spikes for a method in the time range where you noticed the error.

**For API calls**

Some API calls log errors in BigQuery audit
logs in Cloud Logging. To identify the method that reached the limit, do the
following:

- 

In the Google Cloud Dedicated console, go to the Google Cloud Dedicated navigation
menu menu and then
select **Logging** > **Logs Explorer** for your project:

[Go to the Logs Explorer](https://console.cloud.berlin-build0.goog/logs/query) 

- 

Filter logs by running the following query:


```
resource.type="bigquery_resource"
protoPayload.authenticationInfo.principalEmail=" "
"Too many API requests per user per method for this user_method"
In the log entry, you can find the method name under the property protoPayload.method_name.
```


For more information, see [BigQuery audit logs
overview](/bigquery/docs/reference/auditlogs).

#### Resolution

To resolve this quota error, do the following:

- 

Reduce the number of API requests or add a delay between multiple API requests
so that the number of requests stays under this limit.

- 

If the limit is only exceeded occasionally, you can implement retries on this
specific error with exponential backoff.

- 

If you frequently insert data, consider using the
[BigQuery Storage Write API](/bigquery/docs/write-api-streaming). Streaming
data with this API isn't affected by the BigQuery API quota.

- 

While loading data to BigQuery using Dataflow
with the [BigQuery I/O connector](https://beam.apache.org/documentation/io/built-in/google-bigquery/), you
might encounter this error for the [`tables.get` method](/bigquery/docs/reference/rest/v2/tables/get). To resolve this issue, do the following:

- 

Set the destination table's create disposition to `CREATE_NEVER`. For more
information, see [Create disposition](https://beam.apache.org/documentation/io/built-in/google-bigquery/#create-disposition).

- 

Use the Apache Beam SDK version 2.24.0 or higher. In the
previous versions of the SDK, the `CREATE_IF_NEEDED` disposition
calls the `tables.get` method to check if the table exists.

- 

For additional quota, see [Request a quota increase](/bigquery/quotas#requesting_a_quota_increase).
Requesting a quota increase might take several days to process. To provide more
information for your request, we recommend that
your request includes the priority of the job, the user running the query, and
the affected method.

### Maximum Python UDF image storage bytes per project per region

The total size of all stored container images used by active Python UDFs can't
exceed `10 GiB` per project per region. This limit is enforced when you create
or update a Python UDF. If the total size exceeds the regional limit, the
request fails immediately, and the following error is returned.

**Error message**

`Resources exceeded during query execution: Quota exceeded: Your project:
PROJECT_ID exceeded quota for Python UDF image storage usage per
region per project.`

#### Resolution

To resolve this error, do the following:

- 

Request an increase: go to the [**Quotas & System Limits** page](/docs/quotas/view-manage#viewing_your_quota_console),
search for the `Python UDF image storage bytes per project per region`
limit, and then request an increase.

- 

Optimize storage: delete unused Python UDFs using the `DROP FUNCTION`
statement to free space. After a UDF is deleted, its image size no longer
counts towards the quota. You can find the image size by using the API's
[`RoutineBuildStatus`](/bigquery/docs/reference/rest/v2/routines#routinebuildstatus).
For more information on viewing build status, see
[Container build status](/bigquery/docs/user-defined-functions-python#container_build_status).

### Maximum concurrent Python UDFs

You are limited to 10 concurrent Python UDFs per project. If you run more than
10, you receive the following error.

**Error message**

`Exceeded rate limits: too many concurrent queries with Python UDFs in this
project. Your project:
PROJECT_ID exceeded quota for maximum concurrent Python UDFs per
project.`

To view all Python UDF quotas, see [Routines](/bigquery/quotas#udf_limits) in
the Quotas and limits reference.

#### Resolution

To resolve this error, you can request a quota increase by contacting
[support](/bigquery/docs/getting-support) or
[sales](https://berlin.devsitetest.how/contact). It might take several days to review
and process the request. We recommend stating the priority, use case, and the
project ID in the request.

## Troubleshoot quotas or limits that can't be increased

You can't increase the following quotas or limits, but you can apply the
suggested workarounds or best practices to mitigate them.

### Maximum number of pending jobs errors

This limit [can't be increased](/bigquery/quotas#pending_jobs).

**Error message**


```
Quota exceeded: concurrent number of jobs that can be in the pending state
```


#### Resolution

This quota cannot be increased.

To resolve this error, do the following:

- **Reduce submission rate:** reduce the rate at which you submit jobs to BigQuery.

- **Limit concurrency:** avoid submitting a large number of jobs in parallel that might get stuck in the pending state.

### Query queue limit errors

You might encounter this error if a project queues more interactive or batch
queries than its [queue limit](/bigquery/quotas#queued_interactive_queries)
permits.

**Error message**


```
Quota exceeded: Your project and region exceeded quota for max number of jobs
that can be queued per project.
```


#### Resolution

This limit [can't be increased](/bigquery/quotas#jobs). To resolve this error,
see the following general guidance. For high-volume interactive queries, see
[Avoid limits for high-volume interactive queries](#interactive-query-queue-resolution).

- **Pause the job.** If you identify a process or pipeline responsible for an
increase in queries, then pause that process or pipeline.

- **Distribute run times.** Distribute the load across a larger timeframe.
If your reporting solution needs to run many queries, try to introduce some
randomness for when queries start. For example, don't start all reports at the
same time.

- 

**Optimize queries and the data model.** Often, a query can be rewritten
so that it runs more efficiently.

For example, if your query contains a *Common table expression (CTE)*–a `WITH`
clause–which is referenced in more than one place in the query, then this
computation is done multiple times. It is better to persist calculations done
by the CTE in a temporary table,
and then reference it in the query.

Multiple joins can also be the source of lack of efficiency. In this case, you
might want to consider using [
nested and repeated columns](/bigquery/docs/nested-repeated). Using this often improves locality of the
data, eliminates the need for some joins, and overall reduces resource
consumption and the query runtime.

Optimizing queries makes them cheaper, so when you use capacity-based pricing,
you can run more queries with your slots. For more information, see
[Introduction to optimizing query
performance](/bigquery/docs/best-practices-performance-overview).

- 

**Optimize the query model.** BigQuery is not a relational
database. It is not optimized for an infinite number of small queries. Running a
large number of small queries quickly depletes your quotas. Such queries don't
run as efficiently as they do with the smaller database products.
BigQuery is a large data warehouse and this is its primary use
case. It performs best with analytical queries over large amounts of data.

Use the recommendations in the following list to optimize the query model to
avoid reaching the query queue limit.

- **Persist data (saved tables).** Pre-process the data in
BigQuery and store that data in additional tables. For
example, if you execute many similar, computationally intensive queries
using different `WHERE` conditions, then their results are not cached. Such
queries also consume resources each time they run. You can improve the
performance of such queries and decrease their processing time by
pre-computing the data and storing it in a table. This pre-computed data in
the table can be queried by `SELECT` queries. It can often be done during
ingestion within the ETL process, or by using [scheduled queries](/bigquery/docs/scheduling-queries)
or [materialized views](/bigquery/docs/materialized-views-intro).

- **Use dry run mode.** Run queries in [dry run mode](/bigquery/docs/running-queries#dry-run),
which estimates the number of bytes read but does not actually process the
query.

- **Preview table data.** To experiment with or explore data rather than
running queries, preview table data with the
[table preview capability](/bigquery/docs/best-practices-costs#preview-data) 
in BigQuery.

- **Use [cached query results](/bigquery/docs/cached-results).**
All query results, including both interactive and batch queries, are cached
in temporary tables for approximately 24 hours with some
[exceptions](/bigquery/docs/cached-results#cache-exceptions).
While running a cached query does still count against your concurrent query
limit, queries that use cached results are significantly faster than queries
that don't use cached results because BigQuery does not need
to compute the result set.

- **Use BigQuery BI Engine.** If you have encountered this error while using a
business intelligence (BI) tool
to create dashboards that query data in BigQuery, then we
recommend that you use [BigQuery BI Engine](/bigquery/docs/bi-engine-intro).
Using BigQuery BI Engine is optimal for this use case.

- 

**Use jobs with batch priority.** You can queue more
[batch queries](/bigquery/docs/running-queries#batch) than interactive
queries.

- 

**Distribute queries.** Organize and distribute the load across different
projects as informed by the nature of your queries and your business needs.

- 

**Increase slots in your reservation.** [Increase slots](/bigquery/docs/reservations-workload-management#estimate-slots) or, if you have a
high-demand workload, [switch](/bigquery/docs/reservations-intro#choosing_a_model)
to reservations (capacity-based model) from on-demand (pay-per query model).

##### Avoid limits for high-volume interactive queries

Running high-volume interactive queries can cause those queries to reach
the [limit](/bigquery/quotas#query_jobs) for the maximum number of queued
interactive queries. This limit can't be increased.

If you run high-volume interactive queries, especially in scenarios
that involve automated triggers like Cloud Run functions, first
[monitor](/bigquery/docs/admin-jobs-explorer)
the behavior of, and stop, the Cloud Run function causing the
error, and then use one of the following recommended strategies for avoiding
this limit:


- [Increase slots
in your reservation](/bigquery/docs/reservations-workload-management#estimate-slots). If you have a high-demand workload,
[switch](/bigquery/docs/reservations-intro#choosing_a_model)
to reservations (capacity-based model) from on-demand (pay per query model).

- Spread the workload across interactive queries.

- Because you can queue more batch queries than interactive queries, use
[batch
priority jobs](/bigquery/docs/running-queries#batch) instead of interactive queries.

### Shuffle size limit errors

BigQuery returns this error when your project exceeds the maximum
disk and memory size limit available for shuffle operations.

This quota is computed per-reservation and sliced across projects for the
reservations. The quota cannot be modified by Cloud Customer Care. You can learn
more about your usage by querying the [`INFORMATION_SCHEMA.JOBS_TIMELINE` view](/bigquery/docs/information-schema-jobs-timeline#schema).

If you are using the [on-demand](https://berlin.devsitetest.how/bigquery/pricing#on_demand_pricing)
pricing model, you are limited to a [maximum of 2,000 slots](/bigquery/quotas#query_jobs). To increase the
number of slots, you must change to a [capacity-based](https://berlin.devsitetest.how/bigquery/pricing#capacity_compute_analysis_pricing)
pricing model.

**Error message**

You receive one of the following error messages:


```
Quota exceeded: Your project exceeded quota for total shuffle size limit.
```



```
Resources exceeded: Your project or organization exceeded the maximum
disk and memory limit available for shuffle operations. Consider provisioning
more slots, reducing query concurrency, or using more efficient logic in this
job.
```


#### Resolution

To resolve this error, do the following:

- [Increase your reservation](/bigquery/docs/reservations-tasks#update_reservations).

- [Optimize queries](/bigquery/docs/best-practices-performance-overview).

- Reduce concurrency of queries or materializing intermediate results to reduce
dependence on resources. For more information, see [Query queues](/bigquery/docs/query-queues) and [Create materialized views](/bigquery/docs/materialized-views-create).

- [Review detailed steps](/bigquery/docs/query-insights#insufficient_shuffle_quota)
for mitigating insufficient shuffle quota.

### Number of partition modifications for column-partitioned tables quota errors

BigQuery returns this error when your column-partitioned table
reaches the
quota of the number of partition modifications permitted per day.
Partition modifications include the total of all [load jobs](/bigquery/quotas#load_jobs),
[copy jobs](/bigquery/quotas#copy_jobs), and [query jobs](/bigquery/quotas#query_jobs)
that append or overwrite a destination partition.

To see the value of the **Number of partition
modifications per column-partitioned table per day** limit, see [Partitioned
tables](/bigquery/quotas#partitioned_tables).

**Error message**


```
Quota exceeded: Your table exceeded quota for
Number of partition modifications to a column partitioned table
```


#### Resolution

This quota cannot be increased. To resolve this quota error, do the following:

- Change the partitioning on the table to have more data in each partition, in
order to decrease the total number of partitions. For example, change from
[partitioning by day to partitioning by month](/bigquery/docs/partitioned-tables#select_daily_hourly_monthly_or_yearly_partitioning)
or change [how you partition the table](/bigquery/docs/partitioned-tables).

- Use [clustering](/bigquery/docs/clustered-tables#when_to_use_clustering)
instead of partitioning.

- 
If you frequently load data from multiple small files stored in Cloud Storage that uses a
job per file, then combine multiple load jobs into a single job. You can load from multiple
Cloud Storage URIs with a comma-separated list (for example,
`gs://my_path/file_1,gs://my_path/file_2`), or by using wildcards (for example,
`gs://my_path/*`).


For more information, see
[Batch loading data](/bigquery/docs/batch-loading-data#permissions-load-data-from-cloud-storage).


- 
If you use load, select or copy jobs to append single rows of data to a table, for example, then you
should consider batching multiple jobs into one job. BigQuery doesn't perform well
when used as a relational database. As a best practice, avoid running frequent, single-row append
actions.

- 
To append data at a high rate, consider using
[BigQuery Storage Write API](/bigquery/docs/write-api). It is a recommended solution for
high-performance data ingestion. The BigQuery Storage Write API has robust features, including
exactly-once delivery semantics. To learn about limits and quotas, see
[Storage Write API](https://berlin.devsitetest.how/bigquery/quotas#write-api-limits) and to
see costs of using this API, see
[BigQuery data ingestion pricing](https://berlin.devsitetest.how/bigquery/pricing#data_ingestion_pricing).

- 
To monitor the number of modified partitions on a table, use the
[`INFORMATION_SCHEMA` view](https://berlin.devsitetest.how/bigquery/docs/information-schema-jobs#partitions-modified-by).

- For information about optimizing table load jobs to avoid reaching quota limits, see
[Optimize load jobs](/bigquery/docs/optimize-load-jobs).

### Maximum rate of table metadata update operations limit errors

BigQuery returns this error when your table reaches the limit for
maximum rate of table metadata update operations per table for standard tables.
Table operations include the combined total of all [load jobs](/bigquery/quotas#load_jobs),
[copy jobs](/bigquery/quotas#copy_jobs), and [query jobs](/bigquery/quotas#query_jobs)
that append to or overwrite a destination table or that use
a [DML](/bigquery/docs/reference/standard-sql/dml-syntax) `DELETE`, `INSERT`,
`MERGE`, `TRUNCATE TABLE`, or `UPDATE` to write data to a table.

To see the value of the **Maximum rate of table metadata update
operations per table** limit, see [Standard tables](/bigquery/quotas#standard_tables).

**Error message**


```
Exceeded rate limits: too many table update operations for this table
```


When you encounter this error, [diagnose](#ts-maximum-update-table-metadata-limit-diagnose) the
issue, and then [follow the recommended steps](#ts-maximum-update-table-metadata-limit-resolution)
to resolve it.

#### Diagnosis

Metadata table updates can originate from *API calls* that modify a table's
metadata or from *jobs* that modify a table's content. If you have not
identified the source from where most update operations to a table's metadata
are originating, do the following:

- [Identify API calls](#identify-api-calls).

- [Identify jobs](#identify-jobs).

##### Identify API calls

- 

Go to the Google Cloud Dedicated navigation
menu menu, and then
select **Logging > Logs Explorer**:

[Go to the Logs Explorer](https://console.cloud.berlin-build0.goog/logs/query) 

- 

Filter logs to view table operations by running the following query:


```
resource.type="bigquery_dataset"
protoPayload.resourceName="projects/my-project-id/datasets/my_dataset/tables/my_table"
(protoPayload.methodName="google.cloud.bigquery.v2.TableService.PatchTable" OR
protoPayload.methodName="google.cloud.bigquery.v2.TableService.UpdateTable" OR
protoPayload.methodName="google.cloud.bigquery.v2.TableService.InsertTable")
```


##### Identify jobs

The following query returns a list of jobs that modify the affected table in
the project within the past day. If you expect multiple projects in an organization
to write to the table, replace `JOBS_BY_PROJECT` with `JOBS_BY_ORGANIZATION`.


```
SELECT 
job_id , 
user_email , 
query 
FROM `region- REGION_NAME ` . INFORMATION_SCHEMA . JOBS_BY_PROJECT 
WHERE creation_time > TIMESTAMP_SUB ( CURRENT_TIMESTAMP , INTERVAL 1 DAY ) 
AND destination_table . project_id = "my-project-id" 
AND destination_table . dataset_id = "my_dataset" 
AND destination_table . table_id = "my_table" 
```


For more information, see [BigQuery audit logs
overview](/bigquery/docs/reference/auditlogs).

#### Resolution

This quota cannot be increased. To resolve this quota error, do the following:

- Reduce the update rate for the table metadata.

- Add a delay between jobs or table operations to make sure that the update rate
is within the limit.

- 

For data inserts or modification, consider using DML operations. DML
operations are not affected by the **Maximum rate of table metadata update
operations per table** rate limit.

DML operations have other [limits](/bigquery/quotas#data-manipulation-language-statements)
and quotas. For more information, see [Using
data manipulation language (DML)](/bigquery/docs/reference/standard-sql/data-manipulation-language).

- 
If you frequently load data from multiple small files stored in Cloud Storage that uses a
job per file, then combine multiple load jobs into a single job. You can load from multiple
Cloud Storage URIs with a comma-separated list (for example,
`gs://my_path/file_1,gs://my_path/file_2`), or by using wildcards (for example,
`gs://my_path/*`).


For more information, see
[Batch loading data](/bigquery/docs/batch-loading-data#permissions-load-data-from-cloud-storage).


- 
If you use load, select or copy jobs to append single rows of data to a table, for example, then you
should consider batching multiple jobs into one job. BigQuery doesn't perform well
when used as a relational database. As a best practice, avoid running frequent, single-row append
actions.

- 
To append data at a high rate, consider using
[BigQuery Storage Write API](/bigquery/docs/write-api). It is a recommended solution for
high-performance data ingestion. The BigQuery Storage Write API has robust features, including
exactly-once delivery semantics. To learn about limits and quotas, see
[Storage Write API](https://berlin.devsitetest.how/bigquery/quotas#write-api-limits) and to
see costs of using this API, see
[BigQuery data ingestion pricing](https://berlin.devsitetest.how/bigquery/pricing#data_ingestion_pricing).

- 
To monitor the number of modified partitions on a table, use the
[`INFORMATION_SCHEMA` view](https://berlin.devsitetest.how/bigquery/docs/information-schema-jobs#partitions-modified-by).

- For information about optimizing table load jobs to avoid reaching quota limits, see
[Optimize load jobs](/bigquery/docs/optimize-load-jobs).

### Table imports or query appends quota errors

BigQuery returns this error message when your table reaches the
limit for
table operations per day for standard tables. Table operations include the
combined total of all [load jobs](/bigquery/quotas#load_jobs),
[copy jobs](/bigquery/quotas#copy_jobs), and [query jobs](/bigquery/quotas#query_jobs)
that append or overwrite a destination table.

To see the value of the **Table operations per day** limit, see [Standard
tables](/bigquery/quotas#standard_tables).

**Error message**


```
Your table exceeded quota for imports or query appends per table
```


When you encounter this error, [diagnose](#ts-table-import-quota-diagnose) the
issue, and then [follow the recommended steps](#ts-table-import-quota-resolution)
to resolve it.

#### Diagnosis

If you have not identified the source from where most table operations are
originating, do the following:

- 

Make a note of the project, dataset, and table that the failed query, load,
or the copy job is writing to.

- 

Use `INFORMATION_SCHEMA.JOBS_BY_*` tables to learn more about jobs
that modify the table.

The following example finds the hourly count of jobs grouped by job type for
the last 24-hour period using `JOBS_BY_PROJECT`. If you expect multiple
projects to write to the table, replace `JOBS_BY_PROJECT` with
`JOBS_BY_ORGANIZATION`.


```
SELECT 
TIMESTAMP_TRUNC ( creation_time , HOUR ), 
job_type , 
count ( 1 ) 
FROM `region- REGION_NAME ` . INFORMATION_SCHEMA . JOBS_BY_PROJECT 
WHERE creation_time > TIMESTAMP_SUB ( CURRENT_TIMESTAMP , INTERVAL 1 DAY ) 
AND destination_table . project_id = "my-project-id" 
AND destination_table . dataset_id = "my_dataset" 
AND destination_table . table_id = "my_table" 
GROUP BY 1 , 2 
ORDER BY 1 DESC 
```


#### Resolution

This quota cannot be increased. To resolve this quota error, do the following:


- 
If you frequently load data from multiple small files stored in Cloud Storage that uses a
job per file, then combine multiple load jobs into a single job. You can load from multiple
Cloud Storage URIs with a comma-separated list (for example,
`gs://my_path/file_1,gs://my_path/file_2`), or by using wildcards (for example,
`gs://my_path/*`).


For more information, see
[Batch loading data](/bigquery/docs/batch-loading-data#permissions-load-data-from-cloud-storage).


- 
If you use load, select or copy jobs to append single rows of data to a table, for example, then you
should consider batching multiple jobs into one job. BigQuery doesn't perform well
when used as a relational database. As a best practice, avoid running frequent, single-row append
actions.

- 
To append data at a high rate, consider using
[BigQuery Storage Write API](/bigquery/docs/write-api). It is a recommended solution for
high-performance data ingestion. The BigQuery Storage Write API has robust features, including
exactly-once delivery semantics. To learn about limits and quotas, see
[Storage Write API](https://berlin.devsitetest.how/bigquery/quotas#write-api-limits) and to
see costs of using this API, see
[BigQuery data ingestion pricing](https://berlin.devsitetest.how/bigquery/pricing#data_ingestion_pricing).

- 
To monitor the number of modified partitions on a table, use the
[`INFORMATION_SCHEMA` view](https://berlin.devsitetest.how/bigquery/docs/information-schema-jobs#partitions-modified-by).

- For information about optimizing table load jobs to avoid reaching quota limits, see
[Optimize load jobs](/bigquery/docs/optimize-load-jobs).

### Quota exceeded for quota metric 'Authorized Views per dataset' and limit '2500'.

If a dataset's access control list exceeds the combined limit for authorized
resources, BigQuery returns this error message.

**Error message**


```
Quota exceeded for quota metric 'Authorized Views per dataset' and limit '2500'.
```


#### Resolution

A dataset's access control list can have up to 2,500 total authorized
resources, including
[authorized views](/bigquery/docs/authorized-views),
[authorized datasets](/bigquery/docs/authorized-datasets),
and
[authorized functions](/bigquery/docs/authorized-functions).

If you exceed this limit due to a large number of authorized views, consider grouping the
views into authorized datasets.

As a best practice, group related views into authorized datasets when you design new
BigQuery architectures, especially multi-tenant architectures.

### Too many DML statements outstanding against table

This error means that the number of [concurrent mutating DML statements](/bigquery/docs/data-manipulation-language#update_delete_merge_dml_concurrency)
(`UPDATE`, `DELETE`, `MERGE`) running against the same table has exceeded
the [data manipulation language (DML) quota limit](/bigquery/quotas#data-manipulation-language-statements).
This quota limit is per table,
and applies to mutating DML statements only, which does not include `INSERT`.

#### Resolution

Batch the DML jobs by following [Best practices for DML statements](/bigquery/docs/data-manipulation-language#best_practices).

### Loading CSV files quota errors

If you load a large CSV file using the `bq load` command with the
[`--allow_quoted_newlines` flag](/bigquery/docs/reference/bq-cli-reference#flags_and_arguments_9),
you might encounter this error.

**Error message**


```
Input CSV files are not splittable and at least one of the files is larger than
the maximum allowed size. Size is: ...
```


#### Resolution

To resolve this quota error, do the following:

- Set the `--allow_quoted_newlines` flag to `false`.

- Split the CSV file into smaller chunks that are each less than 4 GB.

For more information about limits that apply when you load data into
BigQuery, see [Load jobs](/bigquery/quotas#load_jobs).

### Your user exceeded quota for concurrent `project.lists` requests

This error occurs when Microsoft Power BI jobs that communicate with
BigQuery through a Simba ODBC driver or DataHub fail because they
exceed the `project.list` API limit. To resolve this issue, use the short-term
or long-term workarounds described in this section.

**Error message**


```
Your user exceeded quota for concurrent project.lists requests
```


#### Diagnosis

This error occurs during the connection and discovery phase for Power BI when
a Power BI report refreshes and the Simba driver establishes a connection to a
specific BigQuery project.

#### Short-term resolution

To address this issue in the short term, use the following workarounds, which
are ordered from most to least effective. Implement fixes three or four,
depending on whether you connect to BigQuery using the Simba
driver or using DataHub.

For long-term fixes, see [Long-term resolution](#long-term-resolution).

- 

**Stagger report refreshes**. If you can't modify the DSN, mitigate the quota
issue by reducing the number of simultaneous requests. Instead of having all
reports refresh simultaneously (for example, at
9:00 AM), stagger their schedules by a few minutes (for example, at 9:01 AM,
9:03 AM, and 9:05 AM). This practice spreads out API calls over time, making
it less likely that you reach the concurrent limit.

- 

**Implement retries in Power BI**. This reactive strategy helps a report recover
from a temporary failure. Power BI has built-in retry logic for data refresh
failures. While this practice doesn't prevent the quota error, it makes your
pipeline more resilient by allowing a report to succeed on a subsequent
attempt after the initial spike in API calls subsides. To implement this
fix, do the following:

- In the Power BI service, go to **Settings** for your dataset.

- Expand the **Scheduled refresh** section. Under **Retry**, configure
Power BI to automatically rerun a failed refresh.

- 

**For earlier versions of the Simba driver, specify the project ID in the ODBC
connection**. This action prevents the driver from performing the
`projects.list` discovery call. Instead, the driver connects directly to the
specified project, which prevents unnecessary API calls and resolves the
quota issue.

Newer drivers fail immediately if the project isn't specified with a message
similar to `Unable to establish connection with data source. Missing settings: {[Catalog]}`.

To make this fix, do the following:

- On the machine running the Power BI Gateway or Power BI Desktop, open
the
**ODBC Data Sources (64-bit)** application.

- On the main setup screen for the Simba ODBC driver for
BigQuery, fill the **Catalog (Project)** field with your
specific Google Cloud Dedicated project ID—for example, `my-gcp-project-id`.

- 

**For earlier versions of DataHub, specify the project ID in the
DataHub ingestion configuration**. Make this fix if you are using DataHub
instead of the Simba driver. Similar to Simba, later versions of DataHub
require you to specify the project ID or they won't connect to
BigQuery.

To avoid exceeding DataHub limits, modify your DataHub ingestion configuration
to provide an explicit list of project IDs to scan. This prevents the DataHub
configuration from finding all projects that the service account can see.

In your BigQuery source recipe file (typically a YAML
file), use the `project_ids` configuration to enumerate the projects that you
want to ingest. Then, redeploy the DataHub ingestion recipe with the new
configuration. See the following example and [this longer example](https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/recipes/bigquery_to_datahub.dhub.yaml)
provided by DataHub.

The following is an example of a DataHub configuration snippet:


```
source : 
type : "bigquery" 
config : 
# Instead of relying on discovery, explicitly list the projects. 
# This avoids the problematic projects.list() API call. 
project_ids : 
- " YOUR_PRODUCTION_PROJECT_ID " 
- " YOUR_ANALYTICS_PROJECT_ID " 
- " ANOTHER_BQ_PROJECT " 
```


#### Long-term resolution

The best long-term fix for this error message is to create separate, dedicated
Google Cloud Dedicated service accounts for each function. For example, create a
service account for all Power BI reports and a service account for DataHub
ingestion.

This best practice isolates API usage into separate quota buckets and
prevents a high-load job in DataHub from causing critical business reports in
Power BI to fail.

Use the action plan in the following sections to resolve long-term quota errors
across Power BI and DataHub.

##### Phase 1: Preparation

- Inform owners of the Power BI gateways and DataHub configuration that you
will make coordinated changes to resolve ongoing job failures.

- In the Google Cloud Dedicated console, [create](/iam/docs/service-accounts-create)
two new service accounts—for example, `sa-powerbi-gateway@...`
and `sa-datahub-ingestion@...`.

- [Create](/iam/docs/keys-create-delete) service account keys for the Power BI
and DataHub service accounts.

- [Grant](/iam/docs/manage-access-service-accounts) each new service account
least-privilege permissions by assigning the following Identity and Access Management roles
that enable it to perform its tasks in relevant Identity and Access Management (IAM). Avoid assigning
overly broad roles—for example, **ProjectEditor**.

###### Required roles

The service account for Power BI runs queries and reads data from tables. Grant
the following roles to service accounts in each Google Cloud Dedicated project that
contains data that Power BI must access. To learn more about these roles, see
[BigQuery roles](/bigquery/docs/access-control#bigquery-roles).

- [**BigQuery Data Viewer**](/bigquery/docs/access-control#bigquery.dataViewer):
provides read-only access to datasets, tables, and views.

- [**BigQuery Job User**](/bigquery/docs/access-control#bigquery.jobUser):
provides permissions to run jobs,
including queries, which is essential for Power BI to execute its requests.

The service account for DataHub ingestion only needs to read metadata, such as
table names, schemas, and descriptions, not the data within the tables. Grant
the following role at the project level for each project that DataHub scans.
To learn more about these roles, see
[IAM roles for BigQuery](/iam/docs/roles-permissions/bigquery).

[**BigQuery Metadata Viewer**](/bigquery/docs/access-control#bigquery.metadataViewer): this role is designed specifically to read metadata. It grants permissions to
list datasets and tables and view their metadata without granting access to the
underlying data.

##### Phase 2: Coordinated rollout

During a low-usage period, the Power BI administrator updates the ODBC DSN
configurations on the gateway machines by performing the following steps:

- Changes the authentication method to use the new `sa-powerbi-gateway@...`
service account key created in a previous step.

- If not already performed as a short-term fix, enters the Google Cloud Dedicated
project ID in the **Catalog (Project)** field of the ODBC driver.

- Has the DataHub owner update the BigQuery source
configuration YAML file.

- Points to the new `sa-datahub-ingestion@...` service account key created
in a previous step.

- If not already performed as a short-term fix, uses the `project_ids`
parameter to explicitly list the projects to be scanned.

- Redeploys the DataHub ingestion recipe with the new configuration.

##### Phase 3: Verification and monitoring

To verify and monitor the effects of the fixes, the Power BI and DataHub
administrators perform the following steps:

- Manually trigger a refresh for a few key Power BI reports and a new
ingestion run in DataHub. Confirm that these jobs complete successfully
without incurring quota errors.

- To ensure the `Quota exceeded: Your user exceeded quota for concurrent
project.lists requests` error no longer occurs, monitor your application
logs or business intelligence tool run histories.

- 

Optional: verify that the overall volume of `projects.list` API calls or
related `403` errors has decreased for the associated service accounts:

- 

In the Google Cloud Dedicated console, go to the BigQuery API **API/Service
Details** page

[Go to APIs & services](https://console.cloud.berlin-build0.goog/apis/api/bigquery.googleapis.com/metrics) 

- 

View the dashboards on the **Metrics** tab to verify the decrease in call
volume and related 403 errors.

Administrators should see a dramatic and permanent drop in the usage of this
specific API call, confirming that the fix was successful.