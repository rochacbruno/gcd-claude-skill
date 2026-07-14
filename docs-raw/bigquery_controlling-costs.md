# Estimate and control costs

Source: https://berlin.devsitetest.how/bigquery/docs/controlling-costs
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

Guides

](https://berlin.devsitetest.how/bigquery/docs/introduction)

















- On this page 
- [ Understand compute pricing for BigQuery ](#understand-compute-pricing)

- [ Pricing models ](#compute-pricing-models)
- [ Restrict costs for each model ](#restrict-compute-costs)

- [ Control query costs ](#control-query-cost)

- [ Create custom query quotas ](#create-custom-cost-controls)
- [ Check the estimated cost before running a query ](#check-query-cost)
- [ Estimate query costs ](#estimate-query-costs)
- [ Avoid running queries to explore table data ](#preview-data)
- [ Restrict the number of bytes billed per query ](#restrict-bytes-billed)
- [ Avoid using LIMIT in non-clustered tables ](#avoid-limit-non-clustered-table)
- [ Materialize query results in stages ](#materialize_query_results_in_stages)
- [ Use Rapid Cache to query Cloud Storage with external tables ](#use-rapid-cache)

- [ Control workload costs ](#control-workload-costs)

- [ Use the Google Cloud Dedicated in Germany pricing calculator ](#use-pricing-calculator)
- [ Use reservations and commitments ](#use-reservations-commitments)
- [ Use the slot estimator ](#use-slot-estimator)
- [ Cancel unnecessary long-running jobs ](#cancel-lr-jobs)
- [ View costs using a dashboard ](#view-costs-using-dashboards)
- [ Use billing budgets and alerts ](#use-billing-budgets)

- [ Control storage costs ](#control-storage-cost)

- [ Use long-term storage ](#store-data-bigquery)
- [ Configure the storage billing model ](#storage-billing-model)
- [ Avoid overwriting tables ](#avoid-overwriting-tables)
- [ Reduce the time travel window ](#reduce-time-travel-window)
- [ Use table expiration for destination tables ](#use_table_expiration_for_destination_tables)
- [ Archive data to Cloud Storage ](#archival-data-cloud-storage)

- [ Troubleshooting BigQuery cost discrepancies and unexpected charges ](#troubleshooting-bigquery-cost-discrepancies-and-unexpected-charges)

- [ Unexpected charges related to queries, reservations and commitments ](#unexpected_charges_related_to_queries_reservations_and_commitments)
- [ Unexpected storage charges ](#unexpected_storage_charges)

- [ What's next ](#whats_next)
- 









# Estimate and control costs 



This page describes best practices for estimating and controlling costs in BigQuery.

The primary costs in BigQuery are compute, used for query processing,
and storage, for data that is stored in BigQuery.
BigQuery offers two types of pricing models for query processing,
[on-demand](https://berlin.devsitetest.how/bigquery/pricing#on_demand_pricing) and [capacity-based](https://berlin.devsitetest.how/bigquery/pricing#capacity_compute_analysis_pricing) pricing. Each model offers different
best practices for cost control. For
[data stored in BigQuery](https://berlin.devsitetest.how/bigquery/pricing#storage), costs
depend on the [storage billing model](/bigquery/docs/datasets-intro#dataset_storage_billing_models)
configured for each dataset.

## Understand compute pricing for Big Query

There are subtle differences in compute pricing for BigQuery that
affect capacity planning and cost control.

### Pricing models

For on-demand compute in BigQuery, you incur charges per TiB for
BigQuery queries.

Alternatively, for capacity compute in BigQuery, you incur
charges for the compute resources (*[slots](/bigquery/docs/slots)*) that are
used to process the query. To use this model, you configure
*[reservations](/bigquery/docs/reservations-workload-management)* for slots.

Reservations have the following features:

- They are allocated in pools of slots, and they let you manage capacity and
isolate workloads in ways that make sense for your organization.

- They must reside in one administration project and are subject to
[quotas and limits](/bigquery/quotas#reservations).

The capacity pricing model offers several [*editions*](/bigquery/docs/editions-intro),
which all offer a pay-as-you-go option that's charged in slot hours.
Enterprise and Enterprise Plus editions also provide optional
one- or three-year slot commitments that can save money over the pay-as-you-go rate.

You can also set [autoscaling reservations](/bigquery/docs/slots-autoscaling-intro)
using the pay-as-you-go option. For more
information, see the following:

- To compare pricing models, see
[Choosing a model](/bigquery/docs/reservations-intro#choosing_a_model).

- For pricing details, see [On-demand compute pricing](https://berlin.devsitetest.how/bigquery/pricing#on_demand_pricing)
and [Capacity compute pricing](https://berlin.devsitetest.how/bigquery/pricing#capacity_compute_analysis_pricing).

### Restrict costs for each model

When you use the on-demand pricing model, the only way to restrict costs is to
configure project-level or user-level daily quotas. However, these quotas
enforce a hard cap that prevents users from running queries beyond the quota
limit. To set quotas, see [Create custom query quotas](/bigquery/docs/best-practices-costs#create-custom-cost-controls).

When you use the capacity pricing model using slot reservations, you specify the
maximum number of slots that are available to a reservation. You can also
purchase slot commitments that provide discounted prices for a committed period
of time.

You can use editions fully on demand by setting the baseline of the reservation
to 0 and the maximum to a setting that meets your workload needs.
BigQuery automatically scales up to the number of slots
needed for your workload, never exceeding the maximum that you set. For more
information, see [Workload management using reservations](/bigquery/docs/reservations-workload-management).

## Control query costs

To control the costs of individual queries, we recommend that you first follow
best practices for [optimizing query computation](/bigquery/docs/best-practices-performance-compute)
and [optimizing storage](/bigquery/docs/best-practices-storage).

The following sections outline additional best practices that you can use
to further control your query costs.

### Create custom query quotas

**Best practice:** Use custom daily query quotas to limit the amount of data
processed per day.

You can manage costs by setting a [custom quota](/bigquery/docs/custom-quotas)
that specifies a limit on the amount of data processed per day per project
or per user. Users are not able to run queries once the quota is reached.

To set a custom quota, you need [specific roles or permissions](/bigquery/docs/custom-quotas#required_role).
For quotas to set, see [Quotas and limits](/bigquery/quotas).

For more information, see [Restrict costs for each pricing model](#restrict-compute-costs).

### Check the estimated cost before running a query

**Best practice:** Before running queries, preview them to estimate costs.

When using the on-demand pricing model, queries are billed according to the
number of bytes read. To estimate costs before running a query:

- [Use the query validator](#use-query-validator) in the Google Cloud Dedicated console.

- [Perform a dry run](#perform-dry-run) for queries.

#### Use the query validator

When you enter a query in the Google Cloud Dedicated console, the query validator
verifies the query syntax and provides an estimate of the number of bytes read.
You can use this estimate to calculate query cost in the pricing calculator.

- 

If your query is not valid, then the query validator displays an error
message. For example:

`Not found: Table myProject:myDataset.myTable was not found in location US`

- 

If your query is valid, then the query validator provides an estimate of the
number of bytes required to process the query. For example:

`This query will process 623.1 KiB when run.`

#### Perform a dry run

To perform a dry run, do the following:


[ Console ](#console) [ bq ](#bq) [ API ](#api) [ Go](#go) [ Java](#java) [ Node. js ](#node.js) [ PHP ](#php) [ Python ](#python) 
More 




- 

Go to the BigQuery page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

Enter your query in the query editor.

If the query is valid, then a check mark automatically appears along with the amount of data that the query will process. If the query is invalid, then an exclamation point appears along with an error message.




Enter a query like the following using the `--dry_run` flag.


```
bq query \ 
--use_legacy_sql = false \ 
--dry_run \ 
'SELECT 
COUNTRY, 
AIRPORT, 
IATA 
FROM 
` project_id `. dataset .airports 
LIMIT 
1000' 

```


For a valid query, the command produces the following response:


```
Query successfully validated. Assuming the tables are not modified,
running this query will process 10918 bytes of data.
```




To perform a dry run by using the API, submit a query job with
`dryRun` set to `true` in the
[JobConfiguration](/bigquery/docs/reference/rest/v2/Job#jobconfiguration)
type.
































Before trying this sample, follow the Go setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Go API
reference documentation](https://godoc.org/cloud.google.com/go/bigquery).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import ( 
"context" 
"fmt" 
"io" 

"cloud.google.com/go/bigquery" 
) 

// queryDryRun demonstrates issuing a dry run query to validate query structure and 
// provide an estimate of the bytes scanned. 
func queryDryRun ( w io . Writer , projectID string ) error { 
// projectID := "my-project-id" 
ctx := context . Background () 
client , err := bigquery . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "bigquery.NewClient: %v" , err ) 
} 
defer client . Close () 

q := client . Query ( ` 
SELECT 
name, 
COUNT(*) as name_count 
FROM ` + "`bigquery-public-data.usa_names.usa_1910_2013`" + ` 
WHERE state = 'WA' 
GROUP BY name` ) 
q . DryRun = true 
// Location must match that of the dataset(s) referenced in the query. 
q . [ Location ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Job_Location) = "US" 

job , err := q . Run ( ctx ) 
if err != nil { 
return err 
} 
// Dry run is not asynchronous, so get the latest status and statistics. 
status := job . [ LastStatus ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Job_LastStatus) () 
if err := status . [ Err ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_JobStatus_Err) (); err != nil { 
return err 
} 
fmt . Fprintf ( w , "This query will process %d bytes\n" , status . [ Statistics ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Statistics) . TotalBytesProcessed ) 
return nil 
} 
```


















































Before trying this sample, follow the Java setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Java API
reference documentation](/java/docs/reference/google-cloud-bigquery/latest/overview).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import com.google.cloud.bigquery.[BigQuery](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) ; 
import com.google.cloud.bigquery.[BigQueryException](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) ; 
import com.google.cloud.bigquery.[BigQueryOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) ; 
import com.google.cloud.bigquery.[Job](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) ; 
import com.google.cloud.bigquery.[JobInfo](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html) ; 
import com.google.cloud.bigquery.[JobStatistics](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobStatistics.html) ; 
import com.google.cloud.bigquery.[QueryJobConfiguration](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) ; 

// Sample to run dry query on the table 
public class QueryDryRun { 

public static void runQueryDryRun () { 
String query = 
"SELECT name, COUNT(*) as name_count " 
+ "FROM `bigquery-public-data.usa_names.usa_1910_2013` " 
+ "WHERE state = 'WA' " 
+ "GROUP BY name" ; 
queryDryRun ( query ); 
} 

public static void queryDryRun ( String query ) { 
try { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
[ BigQuery ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [ BigQueryOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) . getDefaultInstance (). getService (); 

[ QueryJobConfiguration ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig = 
[ QueryJobConfiguration ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) . newBuilder ( query ). [ setDryRun ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.Builder.html#com_google_cloud_bigquery_QueryJobConfiguration_Builder_setDryRun_java_lang_Boolean_) ( true ). setUseQueryCache ( false ). build (); 

[ Job ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) job = bigquery . [ create ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____) ( JobInfo . of ( queryConfig )); 
[ JobStatistics ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobStatistics.html) . [ QueryStatistics ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobStatistics.QueryStatistics.html) statistics = job . getStatistics (); 

System . out . println ( 
"Query dry run performed successfully." + statistics . [ getTotalBytesProcessed ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobStatistics.QueryStatistics.html#com_google_cloud_bigquery_JobStatistics_QueryStatistics_getTotalBytesProcessed__) ()); 
} catch ( [ BigQueryException ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e ) { 
System . out . println ( "Query not performed \n" + e . toString ()); 
} 
} 
} 
```


















































Before trying this sample, follow the Node.js setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Node.js API
reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
// Import the Google Cloud client library 
const { BigQuery } = require ( '[@google-cloud/bigquery](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/overview.html)' ); 
const bigquery = new [ BigQuery ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html) (); 

async function queryDryRun () { 
// Runs a dry query of the U.S. given names dataset for the state of Texas. 

const query = `SELECT name 
FROM \`bigquery-public-data.usa_names.usa_1910_2013\` 
WHERE state = 'TX' 
LIMIT 100` ; 

// For all options, see https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query 
const options = { 
query : query , 
// Location must match that of the dataset(s) referenced in the query. 
location : 'US' , 
dryRun : true , 
}; 

// Run the query as a job 
const [ job ] = await bigquery . createQueryJob ( options ); 

// Print the status and statistics 
console . log ( 'Status:' ); 
console . log ( [ job ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html) . metadata . status ); 
console . log ( '\nJob Statistics:' ); 
console . log ( [ job ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html) . metadata . statistics ); 
} 
```


















































Before trying this sample, follow the PHP setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery PHP API
reference documentation](/php/docs/reference/cloud-bigquery/latest/BigQueryClient).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
use Google\Cloud\BigQuery\BigQueryClient; 

/** Uncomment and populate these variables in your code */ 
// $projectId = 'The Google project ID'; 
// $query = 'SELECT id, view_count FROM `bigquery-public-data.stackoverflow.posts_questions`'; 

// Construct a BigQuery client object. 
$bigQuery = new BigQueryClient([ 
'projectId' => $projectId, 
]); 

// Set job configs 
$jobConfig = $bigQuery->query($query); 
$jobConfig->useQueryCache(false); 
$jobConfig->dryRun(true); 

// Extract query results 
$queryJob = $bigQuery->startJob($jobConfig); 
$info = $queryJob->info(); 

printf('This query will process %s bytes' . PHP_EOL, $info['statistics']['totalBytesProcessed']); 
```





















Set the
[QueryJobConfig.dry_run](/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJob#google_cloud_bigquery_job_QueryJob_dry_run)
property to `True`.
[Client.query()](/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client#google_cloud_bigquery_client_Client_query)
always returns a completed
[QueryJob](/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJob#google_cloud_bigquery_job_QueryJob)
when provided a dry run query configuration.































Before trying this sample, follow the Python setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Python API
reference documentation](/python/docs/reference/bigquery/latest).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
from google.cloud import [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest)

# Construct a BigQuery client object. 
client = [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html) () 

job_config = [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ QueryJobConfig ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig.html) ( dry_run = True , use_query_cache = False ) 

# Start the query, passing in the extra configuration. 
query_job = client . [ query ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html) ( 
( 
"SELECT name, COUNT(*) as name_count " 
"FROM `bigquery-public-data.usa_names.usa_1910_2013` " 
"WHERE state = 'WA' " 
"GROUP BY name" 
), 
job_config = job_config , 
) # Make an API request. 

# A dry run query completes immediately. 
print ( "This query will process {} bytes." . format ( [ query_job ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job) . total_bytes_processed )) 
```




















### Estimate query costs 

When using the [on-demand pricing model](https://berlin.devsitetest.how/bigquery/pricing#on_demand_pricing),
you can estimate the cost of running a
query by calculating the number of bytes processed.

#### On-demand query size calculation 

To calculate the number of bytes processed by the various types of queries,
see the following sections:

- [DML statements](/bigquery/docs/reference/standard-sql/dml-syntax#on-demand-query-size-calculation)

- [DDL statements](/bigquery/docs/reference/standard-sql/data-definition-language#on-demand-query-size-calculation)

- [Clustered tables](/bigquery/docs/clustered-tables#block-pruning)

### Avoid running queries to explore table data

**Best practice:** Don't run queries to explore or preview table data.

If you are experimenting with or exploring your data, you can use table preview
options to view data at no charge and without affecting quotas.

BigQuery supports the following data preview options:

- In the Google Cloud Dedicated console, on the table details page, click the
**Preview** tab to sample the data.

- In the bq command-line tool, use the [`bq head`](/bigquery/docs/managing-table-data#browse-table)
command and specify the number of rows to preview.

- In the API, use [`tabledata.list`](/bigquery/docs/reference/rest/v2/tabledata/list)
to retrieve table data from a specified set of rows.

- Avoid using `LIMIT` in non-clustered tables. For non-clustered tables, a
`LIMIT` clause won't reduce compute costs.

### Restrict the number of bytes billed per query

**Best practice:** Use the maximum bytes billed setting to limit query costs
when using the on-demand pricing model.

You can limit the number of bytes billed for a query using the maximum bytes
billed setting. When you set maximum bytes billed, the number of bytes that the
query reads is estimated before the query execution. If the number of
estimated bytes is beyond the limit, then the query fails without incurring a
charge.

For clustered tables, the estimation of the number of bytes billed for a query
is an upper bound, and can be higher than the actual number of bytes billed
after running the query. So in some cases, if you set the maximum bytes billed,
a query on a clustered table can fail, even though the actual bytes billed
wouldn't exceed the maximum bytes billed setting.

If a query fails because of the maximum bytes billed setting, an error similar
to following is returned:

`Error: Query exceeded limit for bytes billed: 1000000. 10485760 or higher
required.`

To set the maximum bytes billed:


[ Console ](#console) [ bq ](#bq) [ API](#api) 
More 




- In the **Query editor**, click **Edit** > **Query settings**
> **Advanced options**.

- In the **Maximum bytes billed** field, enter an integer.

- Click **Save**.




Use the `bq query` command with the `--maximum_bytes_billed` flag.


```
bq query --maximum_bytes_billed = 1000000 \ 
--use_legacy_sql = false \ 
'SELECT 
word 
FROM 
`bigquery-public-data`.samples.shakespeare' 
```



Set the `maximumBytesBilled` property in [`JobConfigurationQuery`](/bigquery/docs/reference/rest/v2/Job#jobconfigurationquery) or
[`QueryRequest`](/bigquery/docs/reference/rest/v2/jobs/query#queryrequest).



### Avoid using `LIMIT` in non-clustered tables

**Best practice:** For non-clustered tables, don't use a `LIMIT` clause as a
method of cost control.

For non-clustered tables, applying a `LIMIT` clause to a query doesn't affect
the amount of data that is read. You are billed for reading all bytes in the
entire table as indicated by the query, even though the query returns only a
subset. With a clustered table, a `LIMIT` clause can reduce the number of bytes
scanned, because scanning stops when enough blocks are scanned to get the
result. You are billed for only the bytes that are scanned.

### Materialize query results in stages

**Best practice:** If possible, materialize your query results in stages.

If you create a large, multi-stage query, each time you run it,
BigQuery reads all the data that is required by the query. You are
billed for all the data that is read each time the query is run.

Instead, break your query into stages where each stage materializes the query
results by writing them to a [destination table](/bigquery/querying-data#permanent-table).
Querying the smaller destination table reduces the amount of data that is read
and lowers costs. The cost of storing the materialized results is much less than
the cost of processing large amounts of data.

### Use Rapid Cache to query Cloud Storage with external tables

**Best practice:** Consider enabling Rapid Cache when querying Cloud Storage data with external tables.

Rapid Cache provides an SSD-backed zonal read cache for your
Cloud Storage buckets, which can potentially improve query performance
and reduce query costs when querying external tables. For more information, see
[Optimize Cloud Storage external table queries](/bigquery/docs/external-tables#cloud-storage-query-optimization).

## Control workload costs

This section describes best practices for controlling costs within a workload.
**A workload is a set of related queries**. For example, a workload can be a data
transformation pipeline that runs daily, a set of dashboards run by a group of
business analysts, or several ad-hoc queries run by a set of data scientists.

### Use the Google Cloud Dedicated in Germany pricing calculator

**Best practice:** Use the [Google Cloud Dedicated in Germany pricing calculator](https://berlin.devsitetest.how/products/calculator)
to create an overall monthly cost estimate for BigQuery
based on projected usage. You can then compare this estimate to your actual
costs to identify areas for optimization.


[ On-demand ](#on-demand) [ Editions ](#editions) 
More 




To estimate costs in the [Google Cloud Dedicated in Germany pricing calculator](https://berlin.devsitetest.how/products/calculator)
when using the on-demand pricing model, follow these steps:

- Open the [Google Cloud Dedicated in Germany pricing calculator](https://berlin.devsitetest.how/products/calculator).

- Click **Add to estimate**.

- Select BigQuery.

- Select "On-demand" for **Service type**.

- Choose the location where your queries will run.

- For **Amount of data queried**, enter the estimated bytes read from your dry run or
the query validator.

- Enter your estimations of storage usage for **Active storage**, **Long-term storage**, **Streaming inserts**, and **Streaming reads**.
You only need to estimate either physical storage or logical storage, depending on the [dataset storage billing model](/bigquery/docs/datasets-intro#dataset_storage_billing_models).

- The estimate appears in the **Cost details** panel. For more information about the estimated cost, click **Open detailed view**. You can also download and share the cost estimate.

For more information, see [On-demand pricing](https://berlin.devsitetest.how/bigquery/pricing#on_demand_pricing).



To estimate costs in the [Google Cloud Dedicated in Germany pricing calculator](https://berlin.devsitetest.how/products/calculator)
when using the capacity-based pricing model with [BigQuery editions](/bigquery/docs/editions-intro), follow these steps:

- Open the [Google Cloud Dedicated in Germany pricing calculator](https://berlin.devsitetest.how/products/calculator).

- Click **Add to estimate**.

- Select BigQuery.

- Select "Editions" for **Service type**.

- Choose the location where the slots are used.

- Choose your **Edition**.

- Choose the **Maximum slots**, **Baseline slots**, optional **Commitment**, and **Estimated utilization of autoscaling**.

- Choose the location where the data is stored.

- Enter your estimations of storage usage for **Active storage**, **Long-term storage**, **Streaming inserts**, and **Streaming reads**.
You only need to estimate either physical storage or logical storage, depending on the [dataset storage billing model](/bigquery/docs/datasets-intro#dataset_storage_billing_models).

- The estimate appears in the **Cost details** panel. For more information about the estimated cost, click **Open detailed view**. You can also download and share the cost estimate.

For more information, see [Capacity-based pricing](https://berlin.devsitetest.how/bigquery/pricing#capacity_compute_analysis_pricing).



### Use reservations and commitments

**Best practice:** Use BigQuery reservations and commitments to control costs.

For more information, see [Restrict costs for each pricing model](#restrict-compute-costs).

### Use the slot estimator

**Best practice:** Use slot estimator to estimate the number of slots required for your workloads.

The [BigQuery slot estimator](/bigquery/docs/slot-estimator)
helps you to manage slot capacity based on historical performance metrics.

In addition, customers using the on-demand pricing model can view sizing
recommendations for commitments and autoscaling reservations with similar performance
when moving to capacity-based pricing.

### Cancel unnecessary long-running jobs

To free capacity, check on long-running jobs to make sure that they should
continue running. If not, [cancel](/bigquery/docs/managing-jobs#cancel_jobs)
them.

### View costs using a dashboard

**Best practice:** Create a dashboard to analyze your Cloud Billing data so you can
monitor and make adjustments to your BigQuery usage.

You can [export your billing data](/billing/docs/how-to/export-data-bigquery) to
BigQuery and visualize it in a tool such as Data Studio.

### Use billing budgets and alerts

**Best practice:** Use [Cloud Billing budgets](/billing/docs/how-to/budgets)
to monitor your BigQuery charges in one place.

Cloud Billing budgets let you track your actual costs against your planned
costs. After you've set a budget amount, you set budget alert threshold rules
that are used to trigger email notifications. Budget alert emails help you stay
informed about how your BigQuery spend is tracking against your
budget.

## Control storage costs

Use these best practices for optimizing the cost of BigQuery
storage. You can also [optimize storage for query performance](/bigquery/docs/best-practices-storage).

### Use long-term storage

**Best practice:** Use [long-term storage pricing](https://berlin.devsitetest.how/bigquery/pricing#storage)
to reduce cost of older data.

When you load data into BigQuery storage, the data is subject to
BigQuery [storage pricing](https://berlin.devsitetest.how/bigquery/pricing#storage).
For older data, you can automatically take advantage of BigQuery
long-term storage pricing.

If you have a table that is not modified for 90 consecutive days, the price of
storage for that table automatically drops by 50 percent. If you have a
partitioned table, each partition is considered separately for eligibility for
long-term pricing, subject to the same rules as non-partitioned tables.

Be aware that, once tables and table partitions are in long-term storage, any
modifications to data, metadata, or partitioning, can cause these resources to
move back to active BigQuery storage. The following are examples
of actions that might result in this move:

- 

Insert, update, truncate, merge, or delete statements that change table data

- 

Loading, streaming, or appending data to the table

- 

`ALTER` statements that change the table schema

- 

Adding or modifying table properties like description, labels, or expiration

- 

Modifying table metadata

### Configure the storage billing model

**Best practice:** Optimize the storage billing model based on your usage
patterns.

BigQuery supports storage billing using logical (uncompressed)
or physical (compressed) bytes, or a combination of both. The
[storage billing model](/bigquery/docs/datasets-intro#dataset_storage_billing_models)
configured for each dataset determines your storage pricing, but it does not
impact query performance.

You can use the `INFORMATION_SCHEMA` views to determine the storage billing model
that works best [based on your usage patterns](/bigquery/docs/information-schema-table-storage#forecast_storage_billing).

### Avoid overwriting tables

**Best practice:** When you are using the physical storage billing model, avoid
repeatedly overwriting tables.

When you overwrite a table, for example by using the `--replace` parameter
in [batch load jobs](/bigquery/docs/batch-loading-data#appending_to_or_overwriting_a_table)
or using the [`TRUNCATE TABLE`](/bigquery/docs/reference/standard-sql/dml-syntax#truncate_table_statement)
SQL statement, the replaced data is kept for the duration of the time travel and failsafe windows.
If you overwrite a table frequently, you will incur additional storage charges.

Instead, you can incrementally load data into a table by using the `WRITE_APPEND`
parameter in load jobs, the `MERGE` SQL statement, or using the
[storage write API](/bigquery/docs/write-api).

### Reduce the time travel window

**Best practice:** Based on your requirements, you can lower the time travel window.

Reducing the [time travel](/bigquery/docs/time-travel) window from the default
value of seven days reduces the retention period for data deleted from or changed in a
table. You are billed for time travel storage only when using the physical (compressed)
[storage billing model](/bigquery/docs/datasets-intro#dataset_storage_billing_models).

The time travel window is set at the dataset level. You can also set the
default time travel window for new datasets using [configuration settings](/bigquery/docs/default-configuration).

### Use table expiration for destination tables

**Best practice:** If you are writing large query results to a destination
table, use the default table expiration time to remove the data when it's no
longer needed.

Keeping large result sets in BigQuery storage has a cost. If you
don't need permanent access to the results, use the
[default table expiration](/bigquery/docs/updating-datasets#table-expiration)
to automatically delete the data for you.

### Archive data to Cloud Storage

**Best practice:** Consider archiving data in Cloud Storage.

You can move data from BigQuery to Cloud Storage
based on the business need for archival. As a best practice, consider
[long-term storage pricing](#store-data-bigquery) and
the [physical storage billing model](#storage-billing-model)
before [exporting data out of BigQuery](/bigquery/docs/exporting-data).

## Troubleshooting Big Query cost discrepancies and unexpected charges

Follow these steps to troubleshoot unexpected BigQuery charges or cost discrepancies:

- 

To understand where the charges for BigQuery are coming from when looking at the Cloud Billing report, the first recommendation is grouping charges by SKU so that it is easier to observe the usage and charges for the corresponding BigQuery services.

- 

After that, study the pricing for the corresponding SKUs in the `Pricing` page in the Cloud Billing UI to understand which feature it is, for example, BigQuery Storage Read API, long-term storage, on-demand pricing, Standard edition.

- 

After identifying the corresponding SKUs, use the `INFORMATION_SCHEMA` views to identify the specific resources associated with these charges, for example:

- If you are charged for on-demand analysis, look into the [`INFORMATION_SCHEMA.JOBS` view examples](/bigquery/docs/information-schema-jobs#examples) to determine jobs driving costs and users who launched them.

- If you are charged for reservation or commitment SKUs, look into the corresponding [`INFORMATION_SCHEMA.RESERVATIONS`](/bigquery/docs/information-schema-reservations) and [`INFORMATION_SCHEMA.CAPACITY_COMMITMENTS`](/bigquery/docs/information-schema-capacity-commitments#example) views to identify the reservations and commitments that are being charged.

- If the charges come from storage SKUs, look at the [`INFORMATION_SCHEMA.TABLE_STORAGE` view examples](/bigquery/docs/information-schema-table-storage#example_2) to understand which datasets and tables are driving more costs.

Important troubleshooting considerations:

- 

Take into account that a *Daily* time period in the Cloud Billing report starts at midnight US and Canadian Pacific Time (UTC-8), and observes daylight saving time shifts in the United States—adjust your calculations and data aggregations to match the same timeframes.

- 

When you compare the Cloud Billing UI to the
[Cloud Billing data export](/billing/docs/how-to/export-data-bigquery),
to BigQuery, make sure that you aggregate based on
`usage_start_time` and `usage_end_time`, not the `export_time`.

- 

Filter by project if there are multiple projects attached to the billing account and you want to review charges coming from a specific project.

- 

Make sure to select the correct region when performing investigations.

### Unexpected charges related to queries, reservations and commitments

Troubleshooting unexpected charges related to job execution depends on the origin of these charges:

- If you see an increase in on-demand analysis costs, this can be related to an increase in the number of jobs that were launched or the change in the amount of data that needs to be processed by jobs. Investigate this using the [`INFORMATION_SCHEMA.JOBS`](/bigquery/docs/information-schema-jobs) view.

- If there is an increase in charges for committed slots, investigate this by querying [`INFORMATION_SCHEMA.CAPACITY_COMMITMENT_CHANGES`](/bigquery/docs/information-schema-capacity-commitment-changes) to see if new commitments have been purchased or modified.

- For increases in charges originating from reservation usage look into changes to reservations that are recorded in [`INFORMATION_SCHEMA.RESERVATION_CHANGES`](/bigquery/docs/information-schema-reservation-changes). To match autoscaling reservation usage with billing data follow [the autoscaling example](/bigquery/docs/slots-autoscaling-intro#monitor_autoscaling_with_information_schema).

#### Slot-hours billed larger than INFORMATION_ SCHEMA. JOBS view calculated slot-hours

When using an autoscaling reservation, billing is calculated according to the number of scaled slots, not the number of slots used. BigQuery autoscales in multiples of 50 slots, which leads to billing for the nearest multiple even if less than the autoscaled amount is actually used.
Autoscaler has a 1 minute minimum period before scaling down by default, which translates into at least 1 minute being charged even if the query used the slots for less time, for example, for only 10 seconds out of the minute. To avoid these charges, you can opt in to BigQuery fluid scaling at the reservation level for per-second billing with no minimum duration. The correct way to estimate charges for an autoscaling reservation is documented in the [Slots Autoscaling page](/bigquery/docs/slots-autoscaling-intro#monitor_autoscaling_with_information_schema). For more information about using autoscaling efficiently, see [autoscaling best practices](/bigquery/docs/slots-autoscaling-intro#autoscaling_best_practices) to use autoscaling efficiently.

A similar scenario will be observed for non-autoscaling reservations—billing is calculated according to the number of slots provisioned, not the number of slots used. If you want to estimate charges for a non-autoscaling reservation, you can query the [`RESERVATIONS_TIMELINE` view](/bigquery/docs/information-schema-reservation-timeline#examples) directly.

#### Billing is less than the total bytes billed calculated through INFORMATION_ SCHEMA. JOBS for project running on-demand queries

There can be multiple reasons for the actual billing to be less than the calculated bytes processed:

- Each project is provided with 1 TB of free tier querying per month for no extra charge.

- `SCRIPT` type jobs were not excluded from the calculation, which could lead to some values being counted twice.

- Different types of savings applied to your Cloud Billing account, such as negotiated discounts, promotional credits and others. 

#### Billing is larger than the bytes processed calculated through INFORMATION_ SCHEMA. JOBS for project running on-demand queries

If the billing amount is larger than the value you calculated by querying the `INFORMATION_SCHEMA.JOBS` view, there might be certain conditions that caused this:

- 

Queries over row-level security tables

- Queries over tables with row-level security don't produce a value for `total_bytes_billed` in the `INFORMATION_SCHEMA.JOBS` view, therefore, the billing calculated using `total_bytes_billed` from `INFORMATION_SCHEMA.JOBS` view will be less than the billed value. See the [Row Level Security best practices](/bigquery/docs/best-practices-row-level-security#limit-side-channel-attacks) page for more details about why this information is not visible.

- 

Performing ML operations in BigQuery

- BigQuery ML pricing for on-demand queries depends on the type of model being created. Some of these model operations are charged at a higher rate than non-ML queries. Therefore, if you just add up all of the `total_billed_bytes` for the project and use the standard on-demand pricing per-TB rate, this won't be a correct pricing aggregation—you need to account for the pricing difference per-TB.

- 

Incorrect pricing amounts

- Confirm that the correct per-TB pricing values are used in the calculations - make sure to choose the correct region as prices are location-dependent. See the [Pricing documentation](https://berlin.devsitetest.how/bigquery/pricing?e=48754805#bigquery-pricing).

The general advice is following the recommended way of calculating the on-demand job usage for billing in our [public documentation](/bigquery/docs/information-schema-jobs#compare_on-demand_job_usage_to_billing_data).

#### Billed for Big Query Reservations API usage even though the API is disabled and not reservations or commitments used

Inspect the SKU to better understand what services are charged. If the SKU billed is `BigQuery Governance SKU`—these are charges coming from Knowledge Catalog.
Some Knowledge Catalog functionalities trigger job execution using BigQuery. These charges are now processed under the corresponding BigQuery Reservations API SKU. 

#### Project is assigned to a reservation, but still seeing Big Query Analysis on-demand costs

Read through the [Troubleshooting issues with reservations](/bigquery/docs/reservations-workload-management#troubleshoot_issues_with_reservations) section to identify where the `Analysis` charges might be coming from.

#### Unexpected charges for pay-as-you go (PAYG) slots for the Big Query Standard edition

In the Cloud Billing report, apply a filter with the label `goog-bq-feature-type` with the value `BQ_STUDIO_NOTEBOOK`. The usage you will see is metered as pay-as-you go slots under the [BigQuery Standard edition](/bigquery/docs/editions-intro). These are charges for using the [BigQuery Studio notebook](/bigquery/docs/notebooks-introduction#monitor_slot_usage). Read more about the [BigQuery Studio notebook pricing](https://berlin.devsitetest.how/bigquery/pricing?e=48754805#notebook-runtime-pricing).

#### Unexpected charges for pay-as-you go (PAYG) slots for the Big Query Enterprise edition

In the Cloud Billing report, apply a filter with the label `goog-bq-feature-type` with the value `SPARK_PROCEDURE`. The usage you will see is metered as pay-as-you go slots under the [BigQuery Enterprise edition](/bigquery/docs/editions-intro). These are charges for using the [BigQuery Apache Spark procedures](/bigquery/docs/spark-procedures#pricing), which are charged this way regardless of the computing model used by the project.

#### Big Query Reservations API charges appearing after the Reservation API is disabled

Disabling the BigQuery won't stop commitment charges. In order to stop commitment charges, you will need to delete a commitment. Set the renewal plan to `NONE`, and the commitment will be automatically deleted when it expires.

#### Querying very small tables results in disproportionately large cost for on-demand

The minimum "processed data per referenced table" billed for a BigQuery query is 10 MiB, regardless of the actual size of the table. Likewise, the minimum billed "processed data per query" is 10 MiB. When you query small tables, even a KB-sized table, you are charged for at least 10 MiB for each query. This can result in much higher charges than your on-demand billing estimates and is particularly expensive for on-demand compute pricing.

### Unexpected storage charges

Scenarios that could lead to storage charge increases:

- Increases in the amount of data that is stored in your tables—use the [`INFORMATION_SCHEMA.TABLE_STORAGE_USAGE_TIMELINE`](/bigquery/docs/information-schema-table-storage-usage) view to monitor the change in bytes for your tables

- Changing [dataset billing models](/bigquery/docs/datasets-intro#dataset_storage_billing_models)

- Increasing the [time-travel window](/bigquery/docs/time-travel) for physical billing model datasets

- Modification of tables that have data in [long-term storage](https://berlin.devsitetest.how/bigquery/pricing?e=48754805#storage-pricing), causing them to become [active storage](https://berlin.devsitetest.how/bigquery/pricing?e=48754805#storage-pricing)

#### Deletion of table( s) or dataset( s) resulted in higher Big Query storage costs

The [BigQuery time travel feature](/bigquery/docs/time-travel) retains deleted data for duration of the configured time-travel window and an additional 7 days for fail-safe recovery. During this retention window, the deleted data in physical storage billing model datasets contributes to the active physical storage cost, even though the tables will no longer appear in `INFORMATION_SCHEMA.TABLE_STORAGE` or in the console. If the table data was in long-term storage, deletion causes this data to be moved to active physical storage. This causes the corresponding cost to rise, because active physical bytes are charged approximately 2 times more than long-term physical bytes according to the [BigQuery storage pricing page](https://berlin.devsitetest.how/bigquery/pricing?e=48754805#storage-pricing). The recommended approach to minimize costs caused by data deletion for physical storage billing model datasets is to reduce the time-travel window to 2 days.

#### Storage costs reduced with no modifications to the data

In BigQuery users pay for active and long-term storage. Active storage charges include any table or table partition that has not been modified for 90 consecutive days, whereas long-term storage charges include tables and partitions that haven't been modified for 90 consecutive days. Overall storage cost reduction can be observed when data transitions to long-term storage, which is around 50% cheaper than active storage. Read about [storage pricing](https://berlin.devsitetest.how/bigquery/pricing?e=48754805#storage-pricing) for more details.

#### Storage cost increased with no significant data increase

Storage costs can increase if data in long-term storage moves to active
BigQuery storage as a result of certain actions on table data,
metadata, or partitions. For more details, see
[Use long-term storage](/bigquery/docs/best-practices-costs#store-data-bigquery).

#### INFORMATION_ SCHEMA storage calculations don't match billing

- Use the [`INFORMATION_SCHEMA.TABLE_STORAGE_USAGE_TIMELINE` view](/bigquery/docs/information-schema-table-storage-usage) instead of `INFORMATION_SCHEMA.TABLE_STORAGE` - `TABLE_STORAGE_USAGE_TIMELINE` provides more accurate and granular data to correctly calculate storage costs

- The queries run on `INFORMATION_SCHEMA` views don't include taxes, adjustments, and rounding errors—take these into account when comparing the data. Read more about Reports in Cloud Billing [on this page](/billing/docs/how-to/reports).

- Data presented in the `INFORMATION_SCHEMA` views is in UTC, whereas billing report data is reported in the US and Canadian Pacific Time (UTC-8).

## What's next

- Learn about [BigQuery pricing](https://berlin.devsitetest.how/bigquery/pricing).

- Learn how to [optimize queries](/bigquery/docs/best-practices-performance-compute).

- Learn how to [optimize storage](/bigquery/docs/best-practices-storage).

- 

To learn about billing, alerts, and visualizing data, see the following topics:

- [Create, edit, or delete budgets and budget alerts](/billing/docs/how-to/budgets)

- [Export Cloud Billing data to BigQuery](/billing/docs/how-to/export-data-bigquery)