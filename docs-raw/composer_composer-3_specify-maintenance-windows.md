# Specify maintenance windows

Source: https://berlin.devsitetest.how/composer/docs/composer-3/specify-maintenance-windows
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/composer/docs/tpc-differences) for more details.














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

Managed Service for Apache Airflow

](https://berlin.devsitetest.how/composer/docs)






- 








[

Gen 3 Guides

](https://berlin.devsitetest.how/composer/docs/composer-3/composer-overview)












# Specify maintenance windows 





















This page explains how to define maintenance windows for your environments.

## About maintenance windows

A maintenance window is a time period where you permit
Managed Airflow to perform maintenance operations. For example, you
can make sure that your critical task executions are not interrupted by
specifying maintenance windows outside of the DAG schedule times.

With maintenance windows, you have control over the time periods where
maintenance can happen for your environment:

- 

If you define custom maintenance windows for your environment,
Managed Airflow performs maintenance during these defined periods.

- 

If you do not define custom maintenance windows for your environment or
specify an empty value, then Managed Airflow performs maintenance
during the default maintenance windows.

## How maintenance windows work

Maintenance windows work in the following way:

- 

Maintenance operations require at least 12 hours of time allocated in a
single week.

- 

You can use several time slots, but each slot duration must be at least 4
hours.

- 

Your environment stays available during maintenance windows. Some components
of your environment might become temporarily unavailable when maintenance
operations are ongoing.

- 

The 12 hours are required so that Managed Airflow has enough time
to schedule and perform all maintenance operations. This does not mean that
maintenance operations take full 12 hours or even happen every week.

You can still run your DAGs during maintenance windows, as long as it is
acceptable that some tasks can be interrupted and retried. If you run DAGs
during maintenance windows, make sure that you enable task retries. You can
configure task retries at the Airflow configuration, DAG, or task level.

Tasks that take less than
24 hours
to execute are generally not impacted by maintenance operations, but they still
need to have retries enabled to withstand scheduler restarts. Scheduler might
restart during standard Managed Airflow operations, outside
maintenance windows.

Managed Airflow informs Airflow workers that a maintenance operation
is about to happen. An Airflow worker finishes already started tasks and does
not pick new tasks. These new tasks are executed by Airflow workers that do not
undergo maintenance operations.

If you use a [highly resilient environment](/composer/docs/composer-3/set-up-highly-resilient-environments),
then Airflow components of your environment are likely to be restarted at
different times during a maintenance operation (this depends on the type of
maintenance operation). Overall, using a highly resilient environment reduces
the downtime of your environment during maintenance operations.

Maintenance operations have the following effects on your environment:

- 

Airflow UI might be temporarily not available.

- 

Managed Airflow might perform an
[automatic infrastructure upgrade operation](/composer/docs/composer-3/upgrade-environments#about-infrastructure-upgrades)
if upgrades are available.

- 

Changing some parameters of your environment or might not be possible
temporarily.

- 

Some Airflow tasks that take longer than
24 hours
to execute can be interrupted. After the maintenance operation completes,
Airflow schedules retries for these tasks (if not configured otherwise).

## Default maintenance windows

Default maintenance windows in Managed Airflow (Gen 3) are defined in the following
way:

- All times are in the local time zone of the region where your environment is
located, but with daylight saving time ignored.

- On Tuesday, Wednesday, Thursday, and Friday maintenance windows are from
00:00:00 to 02:00:00.

- On Saturday, Sunday, and Monday maintenance windows are from 00:00:00
to 04:00:00.

## Maintenance outside of maintenance windows

Managed Airflow might perform maintenance outside of configured
maintenance windows in the following cases:

- 

In emergency situations, for example, when fixing a critical security
vulnerability, some maintenance operations might be performed outside of
regular maintenance windows.

- 

If Managed Airflow couldn't perform regular maintenance operations
during maintenance windows for 30 days, it performs critical maintenance
operations outside of the specified maintenance windows. This is a fallback
mechanism for cases when maintenance windows are misconfigured
and Managed Airflow repeatedly can't perform maintenance on an
environment.

## How to use maintenance windows

Maintenance operations might impact the execution of your DAGs and Airflow
tasks, so we recommend you to do the following:

- 

Define maintenance windows for your Managed Airflow environments.

- 

Schedule DAG runs outside of specified maintenance windows by using
[`start_date` and `schedule`](https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html) parameters in
your DAGs.

## Specify maintenance windows for new environments

You can specify maintenance windows when you create an environment. For more
information, see [Create environments](/composer/docs/composer-3/create-environments#maintenance-windows).

## Specify maintenance windows for existing environments



### Console

To define or change maintenance windows for an existing environment,
[update the environment](/composer/docs/composer-3/update-environments):

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

Select your environment.

- 

Go to the **Environment configuration** tab.

- 

Next to the **Maintenance windows** entry, click **Edit**.

- 

In the **Maintenance windows** dialog, select the
**Set custom time for maintenance windows** checkbox.

- 

Set **Start time**, **Timezone**, **Days**, and **Length**, so that
combined time for the specified schedule is at least 12 hours in a 7-day
rolling window. For example, a period of 4 hours every Monday,
Wednesday, and Friday provides the required amount of time.

- 

Click **Save** and wait until your environment updates.



### gcloud

When you update an environment, the following arguments define
maintenance windows parameters:

- `--maintenance-window-start` sets the start time of a maintenance
window.

- `--maintenance-window-end` sets the end time of a maintenance window.

- `--maintenance-window-recurrence` sets the
[maintenance window recurrence](/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window).


```
gcloud composer environments update ENVIRONMENT_NAME \ 
--location LOCATION \ 
--maintenance-window-start ' DATETIME_START ' \ 
--maintenance-window-end ' DATETIME_END ' \ 
--maintenance-window-recurrence ' MAINTENANCE_RECURRENCE ' 
```


Replace:

- `ENVIRONMENT_NAME` with the name of the environment.

- `DATETIME_START` with the start date and time in the
[date/time input format](/sdk/gcloud/reference/topic/datetimes). Only the
specified time of the day is used, the specified date is ignored.

- `DATETIME_END` with the end date and time in the
[date/time input format](/sdk/gcloud/reference/topic/datetimes). Only the
specified time of the day is used, the specified date is ignored. The
specified date and time must be after the start date.

- 

`MAINTENANCE_RECURRENCE` with an RFC 5545 RRULE for maintenance windows
recurrence. Managed Airflow supports two formats:

- 

The `FREQ=DAILY` format specifies a daily recurrence.

- 

The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a
recurrence on selected days of the week.

The following example specifies a 6-hour maintenance window between 01:00 and
07:00 (UTC) on Wednesdays, Saturdays, and Sundays. The 1 January, 2023
date is ignored.


```
gcloud composer environments update example-environment \ 
--location us-central1 \ 
--maintenance-window-start '2023-01-01T01:00:00Z' \ 
--maintenance-window-end '2023-01-01T07:00:00Z' \ 
--maintenance-window-recurrence 'FREQ=WEEKLY;BYDAY=SU,WE,SA' 
```


### API

- 

Construct an [`environments.patch`](/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

- 

In this request:

- 

In the `updateMask` parameter, specify
the `config.maintenanceWindow` mask.

- 

In the request body, specify the parameters for maintenance windows.


```
{ 
"config" : { 
"maintenanceWindow" : { 
"startTime" : " DATETIME_START " , 
"endTime" : " DATETIME_END " , 
"recurrence" : " MAINTENANCE_RECURRENCE " 
} 
} 
} 
```


Replace:

- `DATETIME_START` with the start date and time in the
[date/time input format](/sdk/gcloud/reference/topic/datetimes). Only the specified time of
the day is used, the specified date is ignored.

- `DATETIME_END` with the end date and time in the
[date/time input format](/sdk/gcloud/reference/topic/datetimes). Only the specified time of
the day is used, the specified date is ignored. The specified date and
time must be after the start date.

- 

`MAINTENANCE_RECURRENCE` with an RFC 5545 RRULE for maintenance windows
recurrence. Managed Airflow supports two formats:

- The `FREQ=DAILY` format specifies a daily recurrence.

- The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a
recurrence on selected days of the week.

The following example specifies a 6-hour maintenance window between 01:00 and
07:00 (UTC) on Wednesdays, Saturdays, Sundays. The 1 January, 2023
date is ignored.


```
// PATCH https://composer.googleapis.com/v1/projects/example-project/ 
// locations/us-central1/environments/example-environment?updateMask= 
// config.maintenanceWindow 

{ 
"config" : { 
"maintenanceWindow" : { 
"startTime" : "2023-01-01T01:00:00Z" , 
"endTime" : "2023-01-01T07:00:00Z" , 
"recurrence" : "FREQ=WEEKLY;BYDAY=SU,WE,SA" 
} 
} 
} 
```


### Terraform

The `maintenance_window` block specifies the maintenance windows for your
environment:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 
maintenance_window { 
start_time = " DATETIME_START " 
end_time = " DATETIME_END " 
recurrence = " MAINTENANCE_RECURRENCE " 
} 
} 
} 
```


Replace:

- `ENVIRONMENT_NAME` with the name of the environment.

- `LOCATION` with the region where the environment is located.

- `DATETIME_START` with the start date and time in the
[date/time input format](/sdk/gcloud/reference/topic/datetimes). Only the specified time of
the day is used, the specified date is ignored.

- `DATETIME_END` with the end date and time in the
[date/time input format](/sdk/gcloud/reference/topic/datetimes). Only the specified time of
the day is used, the specified date is ignored. The specified date and
time must be after the start date.

- 

`MAINTENANCE_RECURRENCE` with an RFC 5545 RRULE for maintenance windows
recurrence. Managed Airflow supports two formats:

- The `FREQ=DAILY` format specifies a daily recurrence.

- The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a
recurrence on selected days of the week.

The following example specifies a 6-hour maintenance window between 01:00 and
07:00 (UTC) on Wednesdays, Saturdays, and Sundays. The 1 January, 2023
date is ignored.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 
maintenance_window { 
start_time = "2023-01-01T01:00:00Z" 
end_time = "2023-01-01T07:00:00Z" 
recurrence = "FREQ=WEEKLY;BYDAY=SU,WE,SA" 
} 
} 
} 
```



## What's next

- [Creating environments](/composer/docs/composer-3/create-environments)

- [Updating environments](/composer/docs/composer-3/update-environments)

- [Clean up the Airflow database](/composer/docs/composer-3/cleanup-airflow-database)