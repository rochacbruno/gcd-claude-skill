# Introduction to workload management

Source: https://documentation.s3ns.fr/bigquery/docs/reservations-intro
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/bigquery/docs/tpc-differences) for more details.














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

BigQuery

](https://documentation.s3ns.fr/bigquery/docs)






- 








[

Guides

](https://documentation.s3ns.fr/bigquery/docs/introduction)

























# Introduction to workload management



BigQuery workload management lets you allocate and manage compute
resources available for data analysis and processing, and also lets you specify how
you are charged for those resources.

## Workload management models

BigQuery offers two models of workload management.
With *on-demand* billing, you pay for the number of bytes processed
when you query or process your data. With *capacity-based* billing, you
allocate processing capacity for workloads with the option of automatically
scaling capacity up and down when needed.



You can switch between on-demand and capacity-based billing models at any time.
You can also use a [combination of the two models](/bigquery/docs/reservations-workload-management#combine_reservations_with_on-demand_billing).

## Choosing a model

Consider the following when choosing a workload management model:




| 
| 
**On-demand** | 
**Capacity-based** | 
|



| 
**Usage model** | 
Data scanned or processed by your queries | 
Dedicated slots or autoscaling slots | 
|

| 
**Unit of metering** | 
TiB | 
slot-hours | 
|

| 
**Minimum capacity** | 
Up to 2,000 slots per project | 
50 slots per reservation | 
|

| 
**Maximum capacity** | 
Up to 2,000 slots per project | 
Configurable per reservation up to regional quota | 
|

| 
**Cost control** | 
Optionally configure project-level or user-level quotas (hard cap) | 
Configure a budget expressed in slots for each reservation | 
|

| 
**Configuration** | 
No configuration required | 
Create slot reservations and assign to projects | 
|

| 
**Editions support** | 
Fixed feature set | 
Available in 3 editions | 
|

| 
**Capacity discounts** | 
Pay-as-you-go only | 
Optional slot commitments for steady-state workloads | 
|

| 
**Predictability** | 
Variable usage and billing | 
Predictable billing through baselines and commitments | 
|

| 
**Centralized purchasing** | 
Per project billing | 
Allocate and bill slots centrally rather than for each project | 
|

| 
**Flexibility** | 
Capacity on-demand (minimum 10 MiB per query) | 
Baseline or autoscaled slots (1-minute minimum by default; opt in to
BigQuery fluid scaling for no minimum duration) | 
|



## Jobs

Every time you [load](/bigquery/docs/loading-data),
[export](/bigquery/exporting-data-from-bigquery),
[query](/bigquery/docs/running-queries), or
[copy data](/bigquery/docs/managing-tables#copy-table),
BigQuery automatically creates, schedules, and runs a job
that tracks the progress of the task.

Because jobs can potentially take a long time to complete, they run asynchronously and can be
polled for their status. Shorter actions, such as listing resources or getting metadata, are not
managed as jobs.

For more information about jobs, see [Manage jobs](/bigquery/docs/managing-jobs).

## Slots

A BigQuery slot is a *virtual compute unit* used by BigQuery
to execute SQL queries or other [job types](/bigquery/docs/managing-jobs).
During the execution of a query, BigQuery automatically determines
how many slots are used by the query. The number of slots used depends on the
amount of data being processed, the complexity of the query, and the number of
slots available.

To learn more about slots and how they are used, see [understand slots](/bigquery/docs/slots).

## Reservations

In the capacity-based pricing model, slots are allocated in pools
called *reservations*. Reservations let you assign slots in ways that make sense
for your organization. For example, you might create a reservation named `prod`
for production workloads, and a separate reservation named `test` for testing,
so that test jobs don't compete for capacity with production workloads. Or, you
might create reservations for different departments in your organization.

For more information about reservations, see [workload management using reservations](/bigquery/docs/reservations-workload-management).

## BI Engine

BI Engine is a fast, in-memory analysis service that accelerates many
SQL queries in BigQuery by intelligently caching the data you use most
frequently. BI Engine can accelerate SQL queries from any source,
including those written by data visualization tools, and can manage cached
tables for ongoing optimization.

[BI Engine reservations](/bigquery/docs/bi-engine-reserve-capacity)
are allocated in GiB of memory and managed separately from slot reservations.

For more information about BI Engine, see [Introduction to BI Engine](/bigquery/docs/bi-engine-intro).

## What's next

- [Understand slots](/bigquery/docs/slots)

- [Understand reservations](/bigquery/docs/reservations-workload-management)

- Learn about [on-demand pricing](https://documentation.s3ns.fr/bigquery/pricing#on_demand_pricing)

- Learn about [capacity-based
pricing](https://documentation.s3ns.fr/bigquery/pricing#capacity_compute_analysis_pricing)

- [Estimate and control costs](/bigquery/docs/best-practices-costs)

- [Create custom cost controls](/bigquery/docs/custom-quotas)