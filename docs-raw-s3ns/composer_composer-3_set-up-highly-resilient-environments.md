# Set up highly resilient environments

Source: https://documentation.s3ns.fr/composer/docs/composer-3/set-up-highly-resilient-environments
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












# Set up highly resilient environments 





















This page describes how to set up highly resilient (Highly Available)
Managed Airflow environments.

## About highly resilient (Highly Available) environments

A highly resilient environment is multi-zonal and runs across at least two
zones of a selected region. Managed Airflow
[automatically distributes](#about-components) the components of your
environment between zones.

For example, a zonal outage interrupts Airflow tasks that run in a specific
zone. Afterwards, a highly resilient environment recovers, restarts its
affected components in a different zone, and switches its database to a
secondary zone. Thus, the failed Airflow tasks can be rescheduled and
restarted by Airflow, while at the same time preserving the history of DAG
runs and other settings.

### About highly available database of your environment

In highly available Managed Airflow environments, the Cloud SQL
component that stores the database of your environment runs in the
[high availability mode](/sql/docs/postgres/high-availability). A primary instance and a
standby instance of Cloud SQL are distributed between zones.

In case of an outage, the Cloud SQL instance of your environment
performs the automatic database failover to the standby Cloud SQL
instance. You do not need to perform any additional actions in your
Managed Airflow environment. Once the primary zone is operational
again, the environment switches back to having two zones (primary and
secondary). Primary and secondary zones can be swapped in some cases. The
Cloud SQL instance in high availability mode uses the same IP
address after a failover.

### About highly available Airflow components

A highly resilient environment is multi-zonal and runs across at least two
zones of a selected region. The following components run in separate zones:

- 

Exactly two Airflow schedulers

- 

At least two triggerers
([if the number of triggerers isn't set to zero](#scale-and-performance))

- 

At least two DAG processors

- 

Two web servers

The minimum number of workers is set to two, and your environment's cluster distributes worker instances between zones. In case of a zonal outage, affected
worker instances are rescheduled in a different zone.

For more information about the architecture of highly resilient environments,
see [Highly resilient environment architecture](/composer/docs/composer-3/environment-architecture#private-ip-high-resilience).

## Before you begin

- 

In Managed Airflow (Gen 3), high resilience is available
both for Private IP and Public IP environments.

- 

In Managed Airflow (Gen 3), highly resilient environments are available starting
from Airflow builds composer-3-airflow-2.10.2-build.13 and
composer-3-airflow-2.9.3-build.20.

- 

Highly resilient environments run extra environment components. This results
in [increased costs](/composer/pricing#sku-composer-3) when compared to
regular environments.

- 

If you want to update a standard environment to a highly resilient one, make
sure that it meets the following configuration requirements. If
your environment doesn't meet these requirements, you can
[update its scale and performance parameters](/composer/docs/composer-3/scale-environments).

- The minimum number of Airflow workers is two or more.

- 

The number of Airflow schedulers is exactly two.

- 

At least two DAG processors.

- 

If you use [deferrable operators in your DAGs](/composer/docs/composer-3/use-deferrable-operators),
then at least two triggerers.

## Create a highly resilient environment

To create a highly resilient environment,
[enable the high resilience mode](/composer/docs/composer-3/create-environments#enable-high-resilience) when you create an
environment.

## Update a standard environment to high resilience mode



### Console

- 

In Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

In the list of environments, click the name of your environment.
The **Environment details** page opens.

- 

Select the **Environment configuration** tab.

- 

In the **Resilience mode** section, click **Edit**.

- 

Select **High resilience** and click **Save**.



### gcloud

```
gcloud composer environments update ENVIRONMENT_NAME \ 
--location LOCATION \ 
--enable-high-resilience
```


Replace the following:

- `ENVIRONMENT_NAME`: the name of your environment.

- `LOCATION`: the region where the environment is located.



### API

- 

Construct an [`environments.patch`](/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

- 

In this request:

- 

In the `updateMask` parameter, specify the
`config.resilienceMode` mask.

- 

In the request body, specify, `HIGH_RESILIENCE` to switch to the high
resilience mode.

Example:


```
// PATCH https://composer.googleapis.com/v1/projects/example-project/ 
// locations/us-central1/environments/example-environment?updateMask= 
// config.resilienceMode 

{ 
"config" : { 
"resilience_mode" : { "HIGH_RESILIENCE" } 
} 
} 
```


### Terraform

The `resilience_mode` field in the `config` block specifies the resilience
mode. To use the high resilience mode, set this value to `HIGH_RESILIENCE`.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 

resilience_mode = "HIGH_RESILIENCE" 

} 
} 
```


Replace the following:

- `ENVIRONMENT_NAME`: the name of your environment.

- `LOCATION`: the region where the environment is located.

Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 

resilience_mode = "HIGH_RESILIENCE" 

} 
```



## Change a highly resilient environment to standard resilience mode

You can change your environment to standard resilience mode at any time. This
operation:

- Reduces the number of web servers in your environment to one.

- Switches off the [high availability mode](#about-database) of your
environment's Airflow database.

- 

Doesn't change the settings for minimum number of Airflow workers,
schedulers, or triggerers.



### Console

- 

In Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

In the list of environments, click the name of your environment.
The **Environment details** page opens.

- 

Select the **Environment configuration** tab.

- 

In the **Resilience mode** section, click **Edit**.

- 

Select **Standard resilience (default)** and click **Save**.



### gcloud

```
gcloud composer environments update ENVIRONMENT_NAME \ 
--location LOCATION \ 
--disable-high-resilience
```


Replace the following:

- `ENVIRONMENT_NAME`: the name of your Cloud Composer environment

- `LOCATION`: the region where the environment is located.



### API

- 

Construct an [`environments.patch`](/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

- 

In this request:

- 

In the `updateMask` parameter, specify the
`config.resilienceMode` mask.

- 

In the request body, specify, `RESILIENCE_MODE_UNSPECIFIED` to switch
to the standard resilience mode.

Example:


```
// PATCH https://composer.googleapis.com/v1/projects/example-project/ 
// locations/us-central1/environments/example-environment?updateMask= 
// config.resilienceMode 

{ 
"config" : { 
"resilience_mode" : { "RESILIENCE_MODE_UNSPECIFIED" } 
} 
} 
```


### Terraform

The `resilience_mode` field in the `config` block specifies the resilience
mode. To use the standard resilience mode, set this value to
`STANDARD_RESILIENCE`.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 

resilience_mode = "STANDARD_RESILIENCE" 

} 
} 
```


Replace the following:

- `ENVIRONMENT_NAME`: the name of your environment.

- `LOCATION`: the region where the environment is located.

Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 

resilience_mode = "STANDARD_RESILIENCE" 

} 
```



## Check if your environment runs in the high resilience mode



### Console

- 

In Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

In the list of environments, click the name of your environment.
The **Environment details** page opens.

- 

Select the **Environment configuration** tab.

- 

In the **Resilience mode** section, view the resilience mode of your
environment.



### gcloud

To check if the high resilience mode is enabled in your environment, run the
following Google Cloud CLI command. The value of `True` means that high
resilience mode is enabled in your environment.


```
gcloud composer environments describe ENVIRONMENT_NAME \ 
--location LOCATION \ 
--format = "value(config.resilienceMode)" 
```


Replace the following:

- `ENVIRONMENT_NAME`: the name of your Cloud Composer environment

- `LOCATION`: the region where the environment is located.




## What's next

- [Perform failover tests](/composer/docs/composer-3/perform-failover-tests) for your highly
resilient environment.

- [Disaster recovery with environment snapshots](/composer/docs/composer-3/disaster-recovery-with-snapshots)