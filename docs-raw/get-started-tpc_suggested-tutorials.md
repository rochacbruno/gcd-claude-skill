# Suggested tutorials

Source: https://berlin.devsitetest.how/docs/get-started-tpc/suggested-tutorials
Last updated: 2026-07-17

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

Get started

](https://berlin.devsitetest.how/docs/get-started)












# Suggested tutorials 






- On this page 
- [ Differences from Google Cloud ](#differences-from-google-cloud)
- [ Simplest quickstart (Compute Engine) ](#simplest-quickstart-compute-engine)
- [ Simple application (Cloud SQL and Compute Engine) ](#simple-application-cloud-sql-and-compute-engine)
- [ Containerized application (Cloud SQL and GKE): ](#containerized-application-cloud-sql-and-google-kubernetes-engine)
- [ Data analytics workload (BigQuery) ](#data-analytics-workload-bigquery)
- [ Resilient application (Compute Engine) ](#resilient-application-compute-engine)
- 









The following are some suggestions for first quickstarts (basic tutorials) and
tutorials to follow when getting started with
Google Cloud Dedicated in Germany. Or go exploring!

## Differences from Google Cloud 

Note the following important differences from Google Cloud when
following tutorials:

- Cloud Build is not yet available in
Google Cloud Dedicated in Germany.

- BigQuery public datasets are not available in
Google Cloud Dedicated in Germany.

- Cloud Shell is not yet available in
Google Cloud Dedicated in Germany. Instead, set up your development
environment locally or on a Google Cloud Dedicated in Germany VM
with the following software:

- [Install Go](https://go.dev/doc/install)

- [Install Docker](https://www.docker.com/get-started/)

- Install and set up the gcloud CLI following the instructions
in [Set up the Google Cloud CLI](/docs/get-started-tpc/setup-gcloud)

- 

Default networks are not automatically created in new projects by design.
Use these commands for manual setup before following the tutorials if you
have not already followed our [minimal
setup](/docs/get-started-tpc/set-up-organization/minimal-setup):


```
gcloud compute networks create default
gcloud compute firewall-rules create default-allow-internal --allow = tcp:1-65535,udp:1-65535,icmp --source-ranges 10 .128.0.0/9
gcloud compute firewall-rules create default-allow-ssh --allow = tcp:22
gcloud compute firewall-rules create default-allow-rdp --allow = tcp:3389
gcloud compute firewall-rules create default-allow-icmp --allow = icmp
```


Particularly if you choose to explore beyond this recommended list of tutorials,
be aware that additional differences from Google Cloud may apply
to them. If in doubt, consult the [differences
page](/docs/overview/gcd-documentation#differences) for the relevant service.

## Simplest quickstart (Compute Engine)

Create a Compute Engine VM and connect to it using the Google Cloud Dedicated console:

- [Create a Linux VM instance](/compute/docs/create-linux-vm-instance)

- [Create a Windows VM instance](/compute/docs/create-windows-server-vm-instance)

## Simple application (Cloud SQL and Compute Engine)

Deploy a sample app on a Compute Engine VM connected to a SQL instance.
Choose between the MySQL and PostgreSQL versions of this tutorial (SQL Server is
not available in Google Cloud Dedicated in Germany).

- [Connect to Cloud SQL for MySQL from Compute Engine](/sql/docs/mysql/connect-instance-compute-engine)

- [Connect to Cloud SQL for PostgreSQL from Compute Engine](/sql/docs/postgres/connect-instance-compute-engine)

## Containerized application (Cloud SQL and GKE):

Deploy a sample app in a Google Kubernetes Engine (GKE) cluster connected to a SQL
instance. Choose between the MySQL and PostgreSQL versions of this tutorial (SQL
Server is not available in Google Cloud Dedicated in Germany).

- [Connect to Cloud SQL for MySQL from GKE](/sql/docs/mysql/connect-instance-kubernetes)

- [Connect to Cloud SQL for PostgreSQL from GKE](/sql/docs/postgres/connect-instance-kubernetes)

Because **Cloud Build is not yet available**, in both tutorials you'll need
to build the sample app with Docker (rather than `gcloud builds`) before
[pushing to Artifact Registry](/artifact-registry/docs/docker/pushing-and-pulling).

## Data analytics workload (BigQuery)

Test loading, analysing and exporting data with BigQuery. **Note
that BigQuery public datasets are not currently available in
Google Cloud Dedicated in Germany.** To follow tutorials that use them,
we suggest that you export the sample tables from Google Cloud and
import the tables locally in your own Google Cloud Dedicated in Germany
datasets.

- [Google Cloud Dedicated console quickstart](/bigquery/docs/sandbox).

- [Command line quickstart](/bigquery/docs/quickstarts/query-public-dataset-bq)

- [Client libraries quickstart](/bigquery/docs/quickstarts/quickstart-client-libraries)

## Resilient application (Compute Engine)

Use autohealing to build a highly available application.

- [Use autohealing for highly available applications](/compute/docs/tutorials/high-availability-autohealing)