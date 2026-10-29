# Schedule and trigger Airflow DAGs

Source: https://documentation.s3ns.fr/composer/docs/latest/schedule-and-trigger-dags
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/composer/docs/tpc-differences) for more details.














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

Data analytics

](https://documentation.s3ns.fr/docs/data)






- 








[

Managed Service for Apache Airflow

](https://documentation.s3ns.fr/composer/docs)






- 








[

Gen 3 Guides

](https://documentation.s3ns.fr/composer/docs/composer-3/composer-overview)












# Schedule and trigger Airflow DAGs 





















This page explains how scheduling and DAG triggering works in Airflow, how to
define a schedule for a DAG, and how to trigger a DAG manually or pause it.

## About Airflow DAGs in Managed Airflow

Airflow DAGs in Managed Airflow are executed in
one or more [Managed Airflow environments](/composer/docs/composer-3/create-environments) in your
project. You [upload source files](/composer/docs/composer-3/manage-dags#add) of your Airflow DAGs to
a Cloud Storage bucket associated with an environment. The environment's
instance of Airflow then parses these files and schedules DAG runs, as defined
by each DAG's schedule. During a DAG run, Airflow schedules and executes
individual tasks that make up a DAG in a sequence defined by the DAG.

To learn more about Airflow's core concepts such as Airflow DAGs, DAG runs,
tasks, or operators, see the [Core Concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html) page in the
Airflow documentation.

## About DAG scheduling in Airflow

Airflow provides the following concepts for its scheduling mechanism:


Logical date 


Represents a date *for which a particular DAG run is executed*.

This is not the actual date when Airflow runs a DAG, but a period of time
that a particular DAG run must process. For example, for a DAG that is
scheduled to run every day at 12:00, the logical date would also be 12:00
on a specific day. Since it runs twice per day, the period of time it must
process is the past 12 hours. At the same time, the logic defined in the
DAG itself might not use the logical date or the time interval at all.
For example, a DAG might run the same script once per day without using the
value of the logical date.

In Airflow versions earlier than 2.2, this date is called *execution date*.

Run date 


Represents a date *when a particular DAG run is executed*.

For example, for a DAG that is scheduled to run every day at 12:00 the
actual execution of the DAG might happen on 12:05, some time after the
logical date passes.

Schedule interval 


Represents when and how often a DAG must be executed, in terms of logical
dates.

For example, a daily schedule means that a DAG is executed once per day,
and the logical dates for its DAG runs have 24 hour intervals.

Start date 


Specifies when you want Airflow to start scheduling your DAG.

Tasks in your DAG can have individual start dates, or you can specify a
single start date for all tasks. Based on the minimum start date for tasks
in your DAG and on the schedule interval, Airflow schedules DAG runs.

Catchup, backfill, and retries 


Mechanisms for executing DAG runs for past dates.

Catchup executes DAG runs that didn't run yet, for example,
if the DAG was paused for a long period of time and then unpaused. You can
use backfill to execute DAG runs for a certain range of dates. Retries
specify how many attempts Airflow must make when executing tasks from a DAG.



Scheduling works in the following way:

- 

After the start date passes, Airflow waits for the next occurrence of the
schedule interval.

- 

Airflow schedules the first DAG run to happen at the end of this schedule
interval.

For example, if a DAG is scheduled to run every hour and the start date is
at 12:00 today, then the first DAG run happens at 13:00 today.

The [Schedule an Airflow DAG](#schedule-dag) section in this document describes
how to set up scheduling for your DAGs using these concepts. For more
information about DAG runs and scheduling, see
[DAG Runs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html) in the Airflow documentation.

## About ways to trigger a DAG

Airflow provides the following ways to trigger a DAG:

- 

[Trigger on a schedule](#schedule-dag). Airflow triggers the DAG
automatically based on the schedule specified for it in the DAG file.

- 

[Trigger manually](#manually). You can trigger a DAG manually from
Cloud de Confiance console, Airflow UI, or by running an Airflow CLI command
from Google Cloud CLI.

- 

Trigger in response to events. The standard way to trigger a DAG in
response to events is to [use a sensor](http://airflow.apache.org/docs/apache-airflow/stable/concepts/sensors.html).

Other ways to trigger DAGs:

- 

Trigger programmatically. You can
[trigger a DAG using the Airflow REST API](/composer/docs/composer-3/access-airflow-api).
For example, from a Python script.

- 

Trigger programmatically in response to events. You can trigger DAGs in
response to events by using
[Cloud Run functions and the Airflow REST API](/composer/docs/composer-3/triggering-with-gcf).

## Before you begin

- Make sure that your account has a role that can manage objects in the
environment buckets and view and trigger DAGs.
For more information, see [Access control](/composer/docs/composer-3/access-control#user-account).

## Schedule an Airflow DAG

You define a schedule for a DAG in the DAG file. Edit the DAG's definition in
the following way:

- 

Locate and edit the DAG file on your computer. If you don't have the DAG
file, you can download its copy
[from the environment's bucket](/composer/docs/composer-3/manage-dags#bucket). For a new DAG, you
can define all parameters when you create the DAG file.

- 

In the `schedule` parameter, define the schedule. You can use a
Cron expression, such as `0 0 * * *`, or a preset, such as `@daily`. For
more information, see [Cron and Time Intervals](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html)
in the Airflow documentation.

Airflow determines logical dates for DAG runs based on the schedule that
you set.

- 

In the `start_date` parameter, define the start date.

Airflow determines the logical date of the first DAG run using this
parameter.

- 

(Optional) In the `catchup` parameter, define if Airflow must execute
all previous runs of this DAG from the start date to the current date that
weren't executed yet.

DAG runs executed during the catchup will have their logical date in the
past and their run date will reflect the time when the DAG run was actually
executed.

- 

(Optional) In the `retries` parameter, define how many times Airflow
must retry tasks that failed (each DAG consists of one or more individual
tasks). By default, tasks in Managed Airflow are retried two
times.

- 

[Upload the new version of the DAG](/composer/docs/composer-3/manage-dags#add) to the environment's
bucket.

- 

Wait until Airflow successfully parses the DAG. For example, you can check
the [list of DAGs in your environment](/composer/docs/composer-3/view-dags) in the
Cloud de Confiance console or in the [Airflow UI](/composer/docs/composer-3/access-airflow-web-interface).

The following example DAG definition runs twice a day at 00:00 and 12:00. Its
start date is set to January 1, 2024, but Airflow does not run it for past dates
after you upload or pause it because the catchup is disabled.

The DAG contains one task named `insert_query_job`, which inserts a row into a
table with the `BigQueryInsertJobOperator` operator. This operator is one of
[Cloud de Confiance by S3NS BigQuery Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/bigquery.html),
which you can use to manage datasets and tables, run queries, and validate data.
If a particular execution of this task fails, Airflow retries it four more
times with the default retry interval. The logical date for these retries
remains the same.

The SQL query for this row uses
[Airflow templates](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html) to write DAG's logical date
and name to the row.


```
import datetime 

from airflow.models.dag import DAG 
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator 

with DAG ( 
"bq_example_scheduling_dag" , 
start_date = datetime . datetime ( 2024 , 1 , 1 ), 
schedule = '0 */12 * * *' , 
catchup = False 
) as dag : 

insert_query_job = BigQueryInsertJobOperator ( 
task_id = "insert_query_job" , 
retries = 4 , 
configuration = { 
"query" : { 
# schema: date (string), description (string) 
# example row: "20240101T120000", "DAG run: " 
"query" : "INSERT example_dataset.example_table VALUES ('{{ ts_nodash }}', 'DAG run: {{ dag }}' )" , 
"useLegacySql" : False , 
"priority" : "BATCH" , 
} 
}, 
location = "us-central1" 
) 

insert_query_job 
```


To test this DAG, you can [trigger it manually](#manually) and
then [view the task execution logs](/composer/docs/composer-3/view-dags).

### More scheduling parameter examples

The following scheduling parameter examples illustrate how scheduling works with
different combinations of parameters:

- 

If `start_date` is `datetime(2024, 4, 4, 16, 25)` and `schedule` is
`30 16 * * *`, then the first DAG run happens at 16:30 on 5 April, 2024.

- 

If `start_date` is `datetime(2024, 4, 4, 16, 35)` and `schedule` is
`30 16 * * *`, then the first DAG run happens at 16:30 on 6 April, 2024.
Because the start date is after the schedule interval on 4 April, 2024,
the DAG run does not happen on 5 April, 2024. Instead, the schedule
interval ends at 16:35 on 5 April, 2024, so the next DAG run is scheduled
for 16:30 on the following day.

- 

If `start_date` is `datetime(2024, 4, 4)`, and the `schedule` is
`@daily`, then the first DAG run is scheduled for 00:00 on April 5, 2024.

- 

If `start_date` is `datetime(2024, 4, 4, 16, 30)`, and
the `schedule` is `0 * * * *`, then the first DAG run is
scheduled for 18:00 on April 4, 2024. After the specified date and time
passes, Airflow schedules a DAG run to happen at the minute 0 of every
hour. The nearest point in time when this happens is 17:00. At this time,
Airflow schedules a DAG run to happen at the end of the schedule interval,
that is, at 18:00.

## Trigger a DAG manually

When you manually trigger an Airflow DAG, Airflow runs
the DAG once, independently from the schedule specified in the DAG file.



### Console

To trigger a DAG from Cloud de Confiance console:

- 

In the Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

Select an environment to view its details.

- 

On the **Environment details** page, go to the **DAGs** tab.

- 

Click the name of a DAG.

- 

On the **DAG details** page, click **Trigger DAG**. A new DAG run is
created.



### Airflow UI

To trigger a DAG from the Airflow UI:

- 

In the Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

In the **Airflow webserver** column, follow the **Airflow** link for your
environment.

- 

Sign in with the Google Account that has the appropriate permissions.

- 

In the Airflow UI, on the **DAGs** page, click the **Trigger DAG** button
for your DAG.



### gcloud

Run the `dags trigger` Airflow CLI command:


```
gcloud composer environments run ENVIRONMENT_NAME \ 
--location LOCATION \ 
dags trigger -- DAG_ID 
```


Replace the following:

- `ENVIRONMENT_NAME`: the name of your environment.

- `LOCATION`: the region where the environment is located.

- `DAG_ID`: the name of the DAG.

For more information about running Airflow CLI commands in
Managed Airflow environments, see
[Running Airflow CLI commands](/composer/docs/composer-3/access-airflow-cli).

For more information about the available Airflow CLI commands, see
the [`gcloud composer environments run` command reference](/sdk/gcloud/reference/composer/environments/run).



## View DAG run logs and details

In the Cloud de Confiance console, you can:

- [View statuses of past DAG runs and DAG details](/composer/docs/composer-3/view-dags).

- [Explore detailed logs](/composer/docs/composer-3/view-logs#streaming) of all DAG runs and all tasks
from these DAG.

- View [DAG statistics](/composer/docs/composer-3/use-monitoring-dashboard#dag-statistics).

In addition, Managed Airflow provides access to the
[Airflow UI](/composer/docs/composer-3/access-airflow-web-interface), which is Airflow's own web interface.

## Pause a DAG



### Console

To pause a DAG from Cloud de Confiance console:

- 

In the Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

Select an environment to view its details.

- 

On the **Environment details** page, go to the **DAGs** tab.

- 

Click the name of a DAG.

- 

On the **DAG details** page, click **Pause DAG**.



### Airflow UI

To pause a DAG from the Airflow UI:

- In the Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

In the **Airflow webserver** column, follow the **Airflow** link for your
environment.

- 

Sign in with the Google Account that has the appropriate permissions.

- 

In the Airflow web interface, on the **DAGs** page, click
the toggle next to the DAG's name.



### gcloud

Run the `dags pause` Airflow CLI command:


```
gcloud composer environments run ENVIRONMENT_NAME \ 
--location LOCATION \ 
dags pause -- DAG_ID 
```


Replace the following:

- `ENVIRONMENT_NAME`: the name of your environment.

- `LOCATION`: the region where the environment is located.

- `DAG_ID`: the name of the DAG.

For more information about running Airflow CLI commands in
Managed Airflow environments, see
[Running Airflow CLI commands](/composer/docs/composer-3/access-airflow-cli).

For more information about the available Airflow CLI commands, see
the [`gcloud composer environments run` command reference](/sdk/gcloud/reference/composer/environments/run).



## What's next

- [Write Airflow DAGs](/composer/docs/composer-3/write-dags)

- [Test Airflow DAGs](/composer/docs/composer-3/test-dags)

- [Troubleshoot Airflow DAGs](/composer/docs/composer-3/troubleshooting-dags)