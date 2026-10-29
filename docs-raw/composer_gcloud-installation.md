# Using Google Cloud CLI with Managed Airflow

Source: https://berlin.devsitetest.how/composer/docs/gcloud-installation
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

Reference

](https://berlin.devsitetest.how/composer/docs/apis)












# Using Google Cloud CLI with Managed Airflow 


















This page describes how to get started using Google Cloud CLI with
Managed Service for Apache Airflow environments.

## Before you begin

- Google Cloud CLI uses Cloud Composer API to run
`gcloud composer` commands, so you must
[enable the API](/composer/docs/latest/enable-composer-service).

- Install [Google Cloud CLI](/sdk/docs/install) on your local client.

## Getting started with the gcloud command-line tool

You can manage and access Managed Airflow environments
with `gcloud composer` commands provided by
[Google Cloud CLI](/sdk/docs).

To start with the `gcloud` tool, review
the [Google Cloud CLI documentation](/sdk/docs).
You can get help for the tool, resources, and commands by using the `--help`
flag:


```
gcloud composer environments --help
```


The help displayed with the `--help` flag is also available in the
[Google Cloud CLI reference](/sdk/gcloud/reference/composer) for `gcloud composer`.

## Setting the default project and location in your local client

Most `gcloud composer` commands require a location. You can specify the
location by using the `--location` flag or by setting the default location.

To set the default project and location for Managed Airflow:

- 

Set the default project by running the following command:


```
gcloud config set project PROJECT_ID 
```


Replace the following:

- `PROJECT_ID`: the [Project ID](/resource-manager/docs/creating-managing-projects) of the
project where your Managed Airflow environment is located.

- 

Configure the Managed Airflow location by running the following
command:


```
gcloud config set composer/location LOCATION 
```


Replace the following:

- `LOCATION`: the region where the environment is located, such as
`us-central1` or `europe-west1`.

- 

(Optional) To list the configuration for Google Cloud CLI, you can run the
following command:


```
gcloud config list
```


## What's next

- [Add and update Airflow DAGs](/composer/docs/latest/manage-dags)

- [`gcloud composer` reference](/sdk/gcloud/reference/composer)

- [`gcloud beta composer` reference](/sdk/gcloud/reference/beta/composer)