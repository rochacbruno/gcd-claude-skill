# Create Managed Service for Apache Airflow environments

Source: https://documentation.s3ns.fr/composer/docs/latest/create-environments
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












# Create Managed Service for Apache Airflow environments 






















This page explains how to create a Managed Airflow environment.

- For more information about environments, see [Environment architecture](/composer/docs/composer-3/environment-architecture).

- For more information about creating an environment with Terraform, see [Create environments (Terraform)](/composer/docs/composer-2/terraform-create-environments).

## Before you begin

- 

[Enable the Cloud Composer API](/composer/docs/composer-3/enable-composer-service). For the full list
of services used by Managed Airflow, see
[Services required by Managed Airflow](/composer/docs/composer-3/enable-composer-service#required-services).

- 

The approximate time to create an environment is
25 minutes.

- 

If you create an environment with Terraform, the service account used by
Terraform must [have a role](/composer/docs/composer-3/access-control#service-account) with
the `composer.environments.create` permission enabled.

For more information about the service account for Terraform, see
[Google Provider Configuration Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#credentials).

For more information about using Terraform to create a
Managed Airflow environment, see
[Terraform documentation](https://www.terraform.io/docs/providers/google/r/composer_environment).

For more information about additional parameters, see
[Terraform Argument Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/composer_environment#argument-reference---cloud-composer-2).

- 

**VPC SC**: To deploy Managed Airflow environments inside a security
perimeter, see [Configuring VPC SC](/composer/docs/composer-3/configure-vpc-sc). When used with
Managed Airflow, VPC Service Controls have several
[known limitations](/vpc-service-controls/docs/supported-products#composer).

## Step 1. Create or choose an environment's service account

When you create an environment, you specify a service account. This service
account is called *environment's service account*. Your environment uses this
service account to perform most of the operations.

The service account for your environment is not a user account. A
service account is a special kind of account used by an application or a
virtual machine (VM) instance, not a person.

You can't change the service account of your environment later.

If you don't have a service account for Managed Airflow
environments in your project yet, create it.

See [Create environments (Terraform)](/composer/docs/composer-2/terraform-create-environments) for an
extended example of creating a service account for your environment in
Terraform.

To create a new service account for your environment:

- 

[Create a new service account](/iam/docs/service-accounts-create#creating) as described in
the Identity and Access Management documentation.

- 

[Grant a role to it](/iam/docs/granting-changing-revoking-access#grant-single-role), as described in the Identity and Access Management
documentation. The required role is **Composer Worker** (`composer.worker`).

- 

To access other resources in your Cloud de Confiance project, grant
extra permissions to access those resources to this service account.
The **Composer Worker** (`composer.worker`) role provides this required
set of permissions in most cases. Add extra permissions to this service
account only when it's necessary for the operation of your DAGs.

## Step 2. Basic setup

This step creates a Managed Airflow environment with default
parameters in the specified location.

All other steps in this guide explain how to customize and configure
different aspects of your environment. All of the remaining steps are optional.



### Console

- 

In the Cloud de Confiance console, go to the **Create environment** page.

[Go to Create environment](https://console.cloud.s3nscloud.fr/composer/environments/create-composer-3) 

- 

In the **Name** field, enter a name for your environment.

The name must start with a lowercase letter followed by up to 62 lowercase
letters, numbers, or hyphens, and can't end with a hyphen. The environment
name is used to create subcomponents for the environment, so you must provide
a name that is also valid as a Cloud Storage
bucket name. See [Bucket naming guidelines](/storage/docs/buckets#naming) for a list
of restrictions.

- 

In the **Location** drop-down list, choose a location
for your environment.

A location is the region where the environment is located.

- 

In the **Image version** drop-down list, select
a [Managed Airflow image](/composer/docs/composer-versions#images) with the required
version of Airflow.

- 

In

the **Service account** drop-down list,

select a service account for your environment.

If you don't have a service
account for your environment yet, see
[Create or choose an environment's service account](#environment-service-account).



### gcloud


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version IMAGE_VERSION \ 
--service-account " SERVICE_ACCOUNT " 
```


Replace:

- 

`ENVIRONMENT_NAME` with the name of the environment.

The name must start with a lowercase letter followed by up to 62 lowercase
letters, numbers, or hyphens, and can't end with a hyphen. The environment
name is used to create subcomponents for the environment, so you must provide
a name that is also valid as a Cloud Storage
bucket name. See [Bucket naming guidelines](/storage/docs/buckets#naming) for a list
of restrictions.

- 

`LOCATION` with the region for the environment.

A location is the region where the environment is located.

- 

`SERVICE_ACCOUNT` with the service account for your environment.

- 

`IMAGE_VERSION` with the name of a Managed Airflow image.

Example:


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" 
```


### API

Construct an [`environments.create`](/composer/docs/reference/rest/v1/projects.locations.environments/create) API request. Specify the
configuration in the [`Environment`](/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource.


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"config" : { 
"softwareConfig" : { 
"imageVersion" : " IMAGE_VERSION " 
}, 
"nodeConfig" : { 
"serviceAccount" : " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- 

`PROJECT_ID` with the [Project ID](/resource-manager/docs/creating-managing-projects).

- 

`LOCATION` with the region for the environment.

A location is the region where the environment is located.

- 

`ENVIRONMENT_NAME` with the environment name.

The name must start with a lowercase letter followed by up to 62 lowercase
letters, numbers, or hyphens, and can't end with a hyphen. The environment
name is used to create subcomponents for the environment, so you must provide
a name that is also valid as a Cloud Storage
bucket name. See [Bucket naming guidelines](/storage/docs/buckets#naming) for a list
of restrictions.

- 

`IMAGE_VERSION` with the name of a Managed Airflow image.

- 

`SERVICE_ACCOUNT` with the service account for your environment.

Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"config" : { 
"softwareConfig" : { 
"imageVersion" : "composer-3-airflow-2.11.1-build.21" 
}, 
"nodeConfig" : { 
"serviceAccount" : " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```


### Terraform

To create an environment with default parameters is a specified location,
add the following resource block to your Terraform configuration and run
`terraform apply`.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 
software_config { 
image_version = " IMAGE_VERSION " 
} 
node_config { 
service_account = " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- 

`ENVIRONMENT_NAME` with the name of the environment.

The name must start with a lowercase letter followed by up to 62 lowercase
letters, numbers, or hyphens, and can't end with a hyphen. The environment
name is used to create subcomponents for the environment, so you must provide
a name that is also valid as a Cloud Storage
bucket name. See [Bucket naming guidelines](/storage/docs/buckets#naming) for a list
of restrictions.

- 

`LOCATION` with the region for the environment.

A location is the region where the environment is located.

- 

`IMAGE_VERSION` with the name of a Managed Airflow image.

- 

`SERVICE_ACCOUNT` with the service account for your environment.

Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 
software_config { 
image_version = "composer-3-airflow-2.11.1-build.21" 
} 
node_config { 
service_account = " 
example-account@example-project . s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```



## Step 3. (Optional) Enable development mode

Development mode environments can be used to test and develop DAGs before they
are published to production. You can [hibernate](/composer/docs/composer-3/hibernate-environments) a development
mode environment when you're not using it.

Development mode environments have the following constraints:

- Only Managed Airflow (Gen 3) with Airflow 3.

- Only [standard resilience mode](#enable-high-resilience).

- 

Small environment size and default resource limits provided by the
[Small environment preset](/composer/docs/composer-3/scale-environments#presets). It's not possible to
change the number of Airflow components or resource limits of a development
mode environment.



### Console

On the **Create environment** page:

- In **Image version**, select a version with Airflow 3.

- Select **Development mode**.



### gcloud

When you create an environment, the `--enable-development-mode` argument
enables the development mode:


```
gcloud beta composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-3 \ 
--service-account " SERVICE_ACCOUNT " \ 
--enable-development-mode
```


### API

When you create an environment, in the [Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment)
resource, set the `mode` field to `DEVELOPMENT`:


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"mode" : "DEVELOPMENT" 
} 
```


Example:


```
// POST https://composer.googleapis.com/v1beta1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"mode" : "DEVELOPMENT" 
} 
```


### Terraform

Terraform support for this feature isn't available yet.



After your development mode environment is created, it will be in the running
state. You can [hibernate or resume](/composer/docs/composer-3/hibernate-environments) it at any time.

## Step 4. (Optional) Configure environment scale and performance parameters

To specify the scale and performance configuration for your environment,
select the environment size and workloads configuration.

You can change all performance and scale parameters
after you create an environment.

Following parameters control the scale and performance:

- 

**Environment size**. Controls the performance parameters of the managed
Managed Airflow infrastructure that includes the Airflow
database. Consider selecting a larger environment size if you want to run a
large number of DAGs and tasks with higher infrastructure performance. For
example, larger environment's size increases the amount of Airflow task log
entries that your environment can process with minimal delay.

- 

**Workloads configuration**. Controls the scale and performance of Airflow
components that run in a GKE cluster of your environment.

- 

**Airflow scheduler**. Parses DAG definition files, schedules DAG runs
based on the schedule interval, and queues tasks for execution by
Airflow workers.

Your environment can run more than one Airflow scheduler at the same
time. Use multiple schedulers to distribute load between several
scheduler instances for better performance and reliability.

Increasing the number of schedulers does not always improve Airflow
performance. For example, having only one scheduler might provide better
performance than having two. This might happen when the extra scheduler is not
utilized, and thus consumes resources of your environment without contributing
to overall performance. The actual scheduler performance depends on the
number of Airflow workers, the number of DAGs and tasks that run in your
environment, and the configuration of both Airflow and the environment.

We recommend starting with two schedulers and then monitoring the performance
of your environment. If you change the number of schedulers, you can always
scale your environment back to the original number of schedulers.

For more information about configuring multiple schedulers, see
[Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html#fine-tuning-your-scheduler-performance).

- 

**Airflow triggerer**. Asynchronously monitors all deferred tasks in your
environment. If you have at least one triggerer instance in your
environment (or at least two in highly resilient environments), you can
use [deferrable operators in your DAGs](/composer/docs/composer-3/use-deferrable-operators).

In Managed Airflow (Gen 3), the Airflow triggerer is enabled by default. If you
want to create an environment without a triggerer, set the number of
triggerers to zero.

- 

**Airflow DAG processor**. Processes DAG files and turns them into
DAG objects. In Managed Airflow (Gen 3), this part of the scheduler runs as a
separate environment component.

- 

**Airflow web server**. Runs the Airflow web interface where you can
monitor, manage, and visualize your DAGs.

- 

**Airflow workers**. Execute tasks that are scheduled by Airflow
schedulers. The minimum and maximum number of workers in your
environment changes dynamically depending on the number of tasks in the
queue.



### Console

You can select a preset for your environment. When you select a preset, the
scale and performance parameters for that preset are automatically selected.
You also have an option to select a custom preset and specify all scale and
performance parameters for your environment.

To select the scale and performance configuration for your environment, on
the **Create environment** page:

- 

To use predefined values, in the **Environment resources** section, click
**Small**, **Medium**, **Large**, or
**Extra Large**.

- 

To specify custom values for the scale and performance parameters:

- 

In the **Environment resources** section, click **Custom**.

- 

In the **Scheduler** section, set the number of schedulers you want to
use, and the resource allocation for their CPU, memory, and storage.

- 

In the **Triggerer** section, use the **Number of triggerers** field
to enter the number of triggerers in your environment.

If you don't want to
[use deferrable operators in your DAGs](/composer/docs/composer-3/use-deferrable-operators),
set the number of triggerers to zero.

If you set at least one triggerer for your environment, use the
the **CPU**, and **Memory** fields to configure resource allocation
for your triggerers.

- 

In the **DAG processor** section, specify the number of DAG processors
in your environment and the amount of CPUs, memory, and storage for
each DAG processor.

Highly resilient environments require at least two DAG processors.

- 

In the **Web server** section, specify the amount of CPUs, memory, and
storage for the web server.

- 

In the **Worker** section, specify:

- The minimum and maximum number of workers for autoscaling limits in
your environment.

- The CPU, memory, and storage allocation for your workers

- 

In the **Core infrastructure** section, in the **Environment size**
drop-down list, select the environment size.



### gcloud

When you create an environment, the following arguments control the
scale and performance parameters of your environment.

- `--environment-size` specifies the environment size.

- `--scheduler-count` specifies the number of schedulers.

- `--scheduler-cpu` specifies the number of CPUs for an Airflow scheduler.

- `--scheduler-memory` specifies the amount of memory for an Airflow
scheduler.

- 

`--scheduler-storage` specifies the amount of disk space for an Airflow
scheduler.

- 

`--triggerer-count` specifies the number of Airflow triggerers in your
environment. The default value for this flag is `0`.
You need triggerers if you want to
[use deferrable operators in your DAGs](/composer/docs/composer-3/use-deferrable-operators).

- For standard resilience environments, use a value between `0` and
`10`.

- For highly resilient environments, use `0` or a value between
`2` and `10`.

- 

`--triggerer-cpu` specifies the number of CPUs for an Airflow
triggerer, in vCPU units. Allowed values: `0.5`, `0.75`, `1`. The default
value is `0.5`.

- 

`--triggerer-memory` specifies the amount of memory for an
Airflow triggerer, in GB. The default value is `0.5`.

The minimum required memory is equal to the number of CPUs allocated for
the triggerers. The maximum allowed value is equal to the number of
triggerer CPUs multiplied by 6.5.

For example, if you set the `--triggerer-cpu` flag to `1`, the
**minimum value** for `--triggerer-memory` is `1` and the
**maximum value** is `6.5`.

- 

`--dag-processor-count` specifies the number of DAG processors in your
environment.

Highly resilient environments require at least two DAG processors.

- 

`--dag-processor-cpu` specifies the number of CPUs for the DAG processor.

- 

`--dag-processor-memory` specifies the amount of memory for the DAG
processor.

- 

`--dag-processor-storage` specifies the amount of disk space for the DAG
processor.

- 

`--web-server-cpu` specifies the number of CPUs for the Airflow web server.

- 

`--web-server-memory` specifies the amount of memory for the Airflow web
server.

- 

`--web-server-storage` specifies the amount of disk space for the Airflow
web server.

- 

`--worker-cpu` specifies the number of CPUs for an Airflow worker.

- 

`--worker-memory` specifies the amount of memory for an Airflow worker.

- 

`--worker-storage` specifies the amount of disk space for an Airflow
worker.

- 

`--min-workers` specifies the minimum number of Airflow workers. Your
environment's cluster runs at least this number of workers.

- 

`--max-workers` specifies the maximum number of Airflow workers. Your
environment's cluster runs at most this number of workers.


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--environment-size ENVIRONMENT_SIZE \ 
--scheduler-count SCHEDULER_COUNT \ 
--scheduler-cpu SCHEDULER_CPU \ 
--scheduler-memory SCHEDULER_MEMORY \ 
--scheduler-storage SCHEDULER_STORAGE \ 
--triggerer-count TRIGGERER_COUNT \ 
--triggerer-cpu TRIGGERER_CPU \ 
--triggerer-memory TRIGGERER_MEMORY \ 
--dag-processor-count DAG_PROCESSOR_COUNT \ 
--dag-processor-cpu DAG_PROCESSOR_CPU \ 
--dag-processor-memory DAG_PROCESSOR_MEMORY \ 
--dag-processor-storage DAG_PROCESSOR_STORAGE \ 
--web-server-cpu WEB_SERVER_CPU \ 
--web-server-memory WEB_SERVER_MEMORY \ 
--web-server-storage WEB_SERVER_STORAGE \ 
--worker-cpu WORKER_CPU \ 
--worker-memory WORKER_MEMORY \ 
--worker-storage WORKER_STORAGE \ 
--min-workers WORKERS_MIN \ 
--max-workers WORKERS_MAX 
```


Replace:

- `ENVIRONMENT_SIZE` with `small`, `medium`, `large`,
`extra-large`.

- `SCHEDULER_COUNT` with the number of schedulers.

- `SCHEDULER_CPU` with the number of CPUs for a scheduler, in vCPU units.

- `SCHEDULER_MEMORY` with the amount of memory for a scheduler.

- `SCHEDULER_STORAGE` with the disk size for a scheduler.

- `TRIGGERER_COUNT` with the number of triggerers.

- `TRIGGERER_CPU` with the number of CPUs for a triggerer, in vCPU units.

- 

`TRIGGERER_MEMORY` with the amount of memory for a triggerer, in GB.

- 

`DAG_PROCESSOR_COUNT` with the number of DAG processors.

- 

`DAG_PROCESSOR_CPU` with the number of CPUs for the DAG processor.

- 

`DAG_PROCESSOR_MEMORY` with the amount of memory for the DAG
processor.

- 

`DAG_PROCESSOR_STORAGE` with the amount of disk space for the DAG
processor.

- 

`WEB_SERVER_CPU` with the number of CPUs for the web server, in vCPU units.

- 

`WEB_SERVER_MEMORY` with the amount of memory for the web server.

- 

`WEB_SERVER_STORAGE` with the amount of memory for the web server.

- 

`WORKER_CPU` with the number of CPUs for a worker, in vCPU units.

- 

`WORKER_MEMORY` with the amount of memory for a worker.

- 

`WORKER_STORAGE` with the disk size for a worker.

- 

`WORKERS_MIN` with the minimum number of Airflow workers that your
environment can run. The number of workers in your environment does not
go above this number, even if a lower number of workers can handle
the load.

- 

`WORKERS_MAX` with the maximum number of Airflow workers that your
environment can run. The number of workers in your environment does not
go above this number, even if a higher number of workers is required to
handle the load.

Example:


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" \ 
--environment-size small \ 
--scheduler-count 1 \ 
--scheduler-cpu 0 .5 \ 
--scheduler-memory 2 .5GB \ 
--scheduler-storage 2GB \ 
--triggerer-count 1 \ 
--triggerer-cpu 0 .5 \ 
--triggerer-memory 0 .5GB \ 
--dag-processor-count 1 \ 
--dag-processor-cpu 0 .5 \ 
--dag-processor-memory 2GB \ 
--dag-processor-storage 1GB \ 
--web-server-cpu 1 \ 
--web-server-memory 2 .5GB \ 
--web-server-storage 2GB \ 
--worker-cpu 1 \ 
--worker-memory 2GB \ 
--worker-storage 2GB \ 
--min-workers 2 \ 
--max-workers 4 
```


### API

When you create an environment, in the [Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > 
[EnvironmentConfig](/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) > 
[WorkloadsConfig](/composer/docs/reference/rest/v1/projects.locations.environments#WorkloadsConfig) resource, specify environment
scale and performance parameters.


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"config" : { 
"workloadsConfig" : { 
"scheduler" : { 
"cpu" : SCHEDULER_CPU , 
"memoryGb" : SCHEDULER_MEMORY , 
"storageGb" : SCHEDULER_STORAGE , 
"count" : SCHEDULER_COUNT 
}, 
"triggerer" : { 
"count" : TRIGGERER_COUNT , 
"cpu" : TRIGGERER_CPU , 
"memoryGb" : TRIGGERER_MEMORY 
}, 
"dagProcessor" : { 
"count" : DAG_PROCESSOR_COUNT , 
"cpu" : DAG_PROCESSOR_CPU , 
"memoryGb" : DAG_PROCESSOR_MEMORY , 
"storageGb" : DAG_PROCESSOR_STORAGE 
}, 
"webServer" : { 
"cpu" : WEB_SERVER_CPU , 
"memoryGb" : WEB_SERVER_MEMORY , 
"storageGb" : WEB_SERVER_STORAGE 
}, 
"worker" : { 
"cpu" : WORKER_CPU , 
"memoryGb" : WORKER_MEMORY , 
"storageGb" : WORKER_STORAGE , 
"minCount" : WORKERS_MIN , 
"maxCount" : WORKERS_MAX 
} 
}, 
"environmentSize" : " ENVIRONMENT_SIZE " , 
"nodeConfig" : { 
"serviceAccount" : " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- `SCHEDULER_CPU` with the number of CPUs for a scheduler, in vCPU units.

- `SCHEDULER_MEMORY` with the amount of memory for a scheduler, in GB.

- `SCHEDULER_STORAGE` with the disk size for a scheduler, in GB.

- 

`SCHEDULER_COUNT` with the number of schedulers.

- 

`TRIGGERER_COUNT` with the number of triggerers. The default value is `0`.
You need triggerers if you want to
[use deferrable operators in your DAGs](/composer/docs/composer-3/use-deferrable-operators).

- For standard resilience environments, use a value between `0` and
`10`.

- For highly resilient environments, use `0` or a value between
`2` and `10`.

If you use at least one triggerer, you must also specify the
`TRIGGERER_CPU`, and `TRIGGERER_MEMORY` parameters:

- 

`TRIGGERER_CPU` specifies the number of CPUs for a triggerer,
in vCPU units. Allowed values: `0.5`, `0.75`, `1`.

- 

`TRIGGERER_MEMORY` configures the amount of memory for a
triggerer. The minimum required memory is equal to the number of
CPUs allocated for the triggerers. The maximum allowed value is
equal to the number of triggerer CPUs multiplied by 6.5.

For example, if you set the `TRIGGERER_CPU` to `1`, the
**minimum value** for `TRIGGERER_MEMORY` is `1` and the
**maximum value** is `6.5`.

- 

`DAG_PROCESSOR_COUNT` with the number of DAG processors.

Highly resilient environments require at least two DAG processors.

- 

`DAG_PROCESSOR_CPU` with the number of CPUs for the DAG processor, in vCPU
units.

- 

`DAG_PROCESSOR_MEMORY` with the amount of memory for the DAG
processor, in GB.

- 

`DAG_PROCESSOR_STORAGE` with the amount of disk space for the DAG
processor, in GB.

- 

`WEB_SERVER_CPU` with the number of CPUs for the web server, in vCPU units.

- 

`WEB_SERVER_MEMORY` with the amount of memory for the web server, in GB.

- 

`WEB_SERVER_STORAGE` with the disk size for the web server, in GB.

- 

`WORKER_CPU` with the number of CPUs for a worker, in vCPU units.

- 

`WORKER_MEMORY` with the amount of memory for a worker, in GB.

- 

`WORKER_STORAGE` with the disk size for a worker, in GB.

- 

`WORKERS_MIN` with the minimum number of Airflow workers that your
environment can run. The number of workers in your environment does not
go above this number, even if a lower number of workers can handle
the load.

- 

`WORKERS_MAX` with the maximum number of Airflow workers that your
environment can run. The number of workers in your environment does not
go above this number, even if a higher number of workers is required to
handle the load.

- 

`ENVIRONMENT_SIZE` with the environment size:
`ENVIRONMENT_SIZE_SMALL`, `ENVIRONMENT_SIZE_MEDIUM`,
`ENVIRONMENT_SIZE_LARGE`,
`ENVIRONMENT_SIZE_EXTRA_LARGE`.

Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"config" : { 
"workloadsConfig" : { 
"scheduler" : { 
"cpu" : 2.5 , 
"memoryGb" : 2.5 , 
"storageGb" : 2 , 
"count" : 1 
}, 
"triggerer" : { 
"cpu" : 0.5 , 
"memoryGb" : 0.5 , 
"count" : 1 
}, 
"dagProcessor" : { 
"count" : 1 , 
"cpu" : 0.5 , 
"memoryGb" : 2 , 
"storageGb" : 1 
}, 
"webServer" : { 
"cpu" : 1 , 
"memoryGb" : 2.5 , 
"storageGb" : 2 
}, 
"worker" : { 
"cpu" : 1 , 
"memoryGb" : 2 , 
"storageGb" : 2 , 
"minCount" : 2 , 
"maxCount" : 4 
} 
}, 
"environmentSize" : "ENVIRONMENT_SIZE_SMALL" , 
"nodeConfig" : { 
"serviceAccount" : " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```


### Terraform

When you create an environment, following arguments control the scale and
performance parameters of your environment.

- 

In the `config` block:

- The `environment_size` field controls the environment size.

- 

In the `workloads_config` block:

- The `scheduler.cpu` field specifies the number of CPUs for an Airflow
scheduler.

- The `scheduler.memory_gb` field specifies the amount of memory for an
Airflow scheduler.

- The `scheduler.storage_gb` field specifies the amount of disk space for
a scheduler.

- The `scheduler.count` field specifies the number of schedulers in your
environment.

- The `triggerer.cpu` field specifies the number of CPUs for an Airflow
triggerer.

- The `triggerer.memory_gb` field specifies the amount of memory for an
Airflow triggerer.

- 

The `triggerer.count` field specifies the number of triggerers in your
environment.

- 

The `dag_processor.cpu` field specifies the number of CPUs for a DAG
processor.

- 

The `dag_processor.memory_gb` field specifies the amount of memory for
a DAG processor.

- 

The `dag_processor.storage_gb` field specifies the amount of disk space
for a DAG processor.

- 

The `dag_processor.count` field specifies the number of DAG processors.

Highly resilient environments require at least two DAG processors.

- 

The `web_server.cpu` field specifies the number of CPUs for the Airflow
web server.

- 

The `web_server.memory_gb` field specifies the amount of memory for the
Airflow web server.

- 

The `web_server.storage_gb` field specifies the amount of disk space
for the Airflow web server.

- 

The `worker.cpu` field specifies the number of CPUs for an Airflow
worker.

- 

The `worker.memory_gb` field specifies the amount of memory for an
Airflow worker.

- 

The `worker.storage_gb` field specifies the amount of disk space for an
Airflow worker.

- 

The `worker.min_count` field specifies the minimum number of workers in
your environment.

- 

The `worker.max_count` field specifies the maximum number of workers in
your environment.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 

workloads_config { 

scheduler { 
cpu = SCHEDULER_CPU 
memory_gb = SCHEDULER_MEMORY 
storage_gb = SCHEDULER_STORAGE 
count = SCHEDULER_COUNT 
} 
triggerer { 
count = TRIGGERER_COUNT 
cpu = TRIGGERER_CPU 
memory_gb = TRIGGERER_MEMORY 
} 
dag_processor { 
cpu = DAG_PROCESSOR_CPU 
memory_gb = DAG_PROCESSOR_MEMORY 
storage_gb = DAG_PROCESSOR_STORAGE 
count = DAG_PROCESSOR_COUNT 
} 
web_server { 
cpu = WEB_SERVER_CPU 
memory_gb = WEB_SERVER_MEMORY 
storage_gb = WEB_SERVER_STORAGE 
} 
worker { 
cpu = WORKER_CPU 
memory_gb = WORKER_MEMORY 
storage_gb = WORKER_STORAGE 
min_count = WORKERS_MIN 
max_count = WORKERS_MAX 
} 
} 

environment_size = " ENVIRONMENT_SIZE " 

node_config { 
service_account = " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- `ENVIRONMENT_NAME` with the name of the environment.

- `LOCATION` with the region where the environment is located.

- `SERVICE_ACCOUNT` with the service account for your environment.

- `SCHEDULER_CPU` with the number of CPUs for a scheduler, in vCPU units.

- `SCHEDULER_MEMORY` with the amount of memory for a scheduler, in GB.

- `SCHEDULER_STORAGE` with the disk size for a scheduler, in GB.

- `SCHEDULER_COUNT` with the number of schedulers.

- `TRIGGERER_COUNT` with the number of triggerers.

- `TRIGGERER_CPU` with the number of CPUs for a triggerer, in vCPU units.

- 

`TRIGGERER_MEMORY` with the amount of memory for a triggerer, in GB.

- 

`DAG_PROCESSOR_CPU` with the number of CPUs for the DAG processor, in vCPU
units.

- 

`DAG_PROCESSOR_MEMORY` with the amount of memory for the DAG
processor, in GB.

- 

`DAG_PROCESSOR_STORAGE` with the amount of disk space for the DAG
processor, in GB.

- 

`DAG_PROCESSOR_COUNT` with the number of DAG processors.

- 

`WEB_SERVER_CPU` with the number of CPUs for the web server, in vCPU units.

- 

`WEB_SERVER_MEMORY` with the amount of memory for the web server, in GB.

- 

`WEB_SERVER_STORAGE` with the disk size for the web server, in GB.

- 

`WORKER_CPU` with the number of CPUs for a worker, in vCPU units.

- 

`WORKER_MEMORY` with the amount of memory for a worker, in GB.

- 

`WORKER_STORAGE` with the disk size for a worker, in GB.

- 

`WORKERS_MIN` with the minimum number of Airflow workers that your
environment can run. The number of workers in your environment does not
go above this number, even if a lower number of workers can handle
the load.

- 

`WORKERS_MAX` with the maximum number of Airflow workers that your
environment can run. The number of workers in your environment does not
go above this number, even if a higher number of workers is required to
handle the load.

- 

`ENVIRONMENT_SIZE` with the environment size:
`ENVIRONMENT_SIZE_SMALL`, `ENVIRONMENT_SIZE_MEDIUM`,
`ENVIRONMENT_SIZE_LARGE`,
`ENVIRONMENT_SIZE_EXTRA_LARGE`.

Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 

workloads_config { 

scheduler { 
cpu = 2.5 
memory_gb = 2.5 
storage_gb = 2 
count = 1 
} 
triggerer { 
count = 1 
cpu = 0.5 
memory_gb = 0.5 
} 
dag_processor { 
cpu = 1 
memory_gb = 2 
storage_gb = 1 
count = 1 
} 
web_server { 
cpu = 1 
memory_gb = 2.5 
storage_gb = 2 
} 
worker { 
cpu = 1 
memory_gb = 2 
storage_gb = 2 
min_count = 2 
max_count = 4 
} 
} 

environment_size = "ENVIRONMENT_SIZE_SMALL" 

node_config { 
service_account = " 
example-account@example-project . s3ns.iam.gserviceaccount.com
" 
} 

} 
} 
```



## Step 5. (Optional) Enable high resilience mode

[Highly resilient](/composer/docs/composer-3/set-up-highly-resilient-environments) (Highly Available)
Managed Airflow environments are environments that use built-in
redundancy and failover mechanisms that reduce the environment's susceptibility
to zonal failures and single point of failure outages.

In Managed Airflow (Gen 3), highly resilient environments are available starting
from Airflow builds composer-3-airflow-2.10.2-build.13 and
composer-3-airflow-2.9.3-build.20.

A highly resilient environment is multi-zonal and runs across at
least two zones of a selected region. The following components run in separate
zones:

- 

Exactly two Airflow schedulers

- 

At least two triggerers
([if the number of triggerers isn't set to `0`](#scale-and-performance))

- 

At least two DAG processors

- 

Two web servers

The minimum number of workers is set to two, and your environment's cluster
distributes worker instances between zones. In case of a zonal outage, affected
worker instances are rescheduled in a different zone. The Cloud SQL
component of a highly resilient environment has a primary instance and a standby
instance that are distributed between zones.



### Console

On the **Create environment** page:

- 

In the **Resilience mode** section, select **High resilience**.

- 

In the **Environment resources** section, select scale parameters for a
highly resilient environment. Highly resilient environments require
exactly two schedulers, zero or between two and ten triggerers, and at least two workers:

- 

Click **Custom**.

- 

In the **Number of schedulers** drop-down list, select `2`.

- 

In the **Number of triggerers** drop-down list, select `0`,
or a value between `2` and `10`. Configure the **CPU** and **Memory**
allocation for your triggerers.

- 

In the **Minimum number of workers** drop-down list, select `2` or
more, depending on the required number of workers.

- 

In the **Network configuration** section:

- 

In the **Networking type**, select **Private IP environment**.

- 

If required, specify [other networking parameters](#networking).



### gcloud

When you create an environment, the `--enable-high-resilience` argument
enables the high resilience mode.

Set the following arguments:

- `--enable-high-resilience`

- `--enable-private-environment`, and
[other networking parameters](#networking) for a Private IP environment,
if required

- `--scheduler-count` to `2`

- 

`--triggerer-count` to `0` or a value between `2` and `10`.
If you use triggerers, the `--triggerer-cpu and`--triggerer-memory`
flags are also required for environment creation.

For more information about `--triggerer-count`, `--triggerer-cpu`, and
`--triggerer-memory` flags, see
[Configure environment scale and performance parameters](#scale-and-performance).

- 

`--min-workers` to `2` or more


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--enable-high-resilience \ 
--enable-private-environment \ 
--scheduler-count 2 \ 
--triggerer-count 2 \ 
--triggerer-cpu 0 .5 \ 
--triggerer-memory 0 .5 \ 
--min-workers 2 
```


### API

When you create an environment, in the [Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > 
[EnvironmentConfig](/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, enable the high
resilience mode.


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"config" : { 
"resilience_mode" : "HIGH_RESILIENCE" , 
"nodeConfig" : { 
"serviceAccount" : " SERVICE_ACCOUNT " 
} 

} 
} 
```


Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"config" : { 
"resilience_mode" : "HIGH_RESILIENCE" , 
"nodeConfig" : { 
"serviceAccount" : " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" 
} 

} 
} 
```


### Terraform

When you create an environment, the `resilience_mode` field in the `config`
block enables the high resilience mode.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 

resilience_mode = "HIGH_RESILIENCE" 

node_config { 
service_account = " SERVICE_ACCOUNT " 
} 

} 
} 
```


Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 

resilience_mode = "HIGH_RESILIENCE" 

node_config { 
service_account = " 
example-account@example-project . s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```



## Step 6. (Optional) Specify a zone for the environment's database

You can specify a preferred Cloud SQL zone when creating a standard
resilience environment.



### Console

On the **Create environment** page:

- 

In the **Advanced configuration** section, expand
the **Show advanced configuration** item.

- 

In the **Airflow database zone** list, select a preferred
Cloud SQL zone.



### gcloud

When you create an environment, the `--cloud-sql-preferred-zone` argument
specifies a preferred Cloud SQL zone.


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--cloud-sql-preferred-zone SQL_ZONE 
```


Replace the following:

- `SQL_ZONE`: preferred Cloud SQL zone. This zone must be located
in the region where the environment is located.

Example:


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" \ 
--cloud-sql-preferred-zone us-central1-a
```


### API

When you create an environment, in the [Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment)
> [DatabaseConfig](/composer/docs/reference/rest/v1/projects.locations.environments#DatabaseConfig) resource, specify the
preferred Cloud SQL zone.


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"config" : { 
"databaseConfig" : { 
"zone" : " SQL_ZONE " 
}, 
"nodeConfig" : { 
"serviceAccount" : " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace the following:

- `SQL_ZONE`: preferred Cloud SQL zone. This zone must be located
in the region where the environment is located.

Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"config" : { 
"databaseConfig" : { 
"zone" : "us-central1-a" 
}, 
"nodeConfig" : { 
"serviceAccount" : " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```


### Terraform

When you create an environment, the `zone` field in the `database_config`
block specifies the preferred Cloud SQL zone.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 
database_config { 
zone = " SQL_ZONE " 
} 

node_config { 
service_account = " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace the following:

- `SQL_ZONE`: preferred Cloud SQL zone. This zone must be located
in the region where the environment is located.




## Step 7. (Optional) Configure your environment's networking

You can configure Managed Airflow (Gen 3) networking in the following ways:

- In a **Public IP environment**, your environment's Airflow components can
access the internet.

- In a **Private IP environment**, your environment's Airflow components do not
have access to the internet.

- Private IP and Public IP environments can
[connect to your VPC network](/composer/docs/composer-3/connect-vpc-network) as a separate option.

- You can specify the
[internal IP range of your environment](/composer/docs/composer-3/connect-vpc-network#internal-range). This range can't be changed later.

- 

You can
[enable access to the internet when installing PyPI packages](/composer/docs/composer-3/packages-internet-access).
For example, your Private IP environment can
still install PyPI packages from
[Python Package Index](https://pypi.org) if you enable this
option.

- 

For a **Shared VPC environment**, you must do additional networking setup for
the host project, then create a Public or a Private IP environment in a
service project. Follow the instructions on the
[Configuring Shared VPC](/composer/docs/composer-3/configure-shared-vpc) page.



### Console

- 

Make sure that your networking is configured for the type of environment
that you want to create.

- 

In the **Network configuration** section, expand
the **Show network configuration** item.

- 

If you want to connect your environment to a VPC network, in the
**Network attachment** field, select a network attachment. You can also
create a new network attachment. For more information, see
[Connect an environment to a VPC network](/composer/docs/composer-3/connect-vpc-network). 

- 

If you want to create a Private IP environment, in the **Networking type**
section, select the **Private IP environment** option.

- 

If you want to add network tags, see [Add network tags](#network-tags) for
more information.



### gcloud

Make sure that your networking is configured for the type of environment that you want to create.

When you create an environment, the following arguments control
the networking parameters. If you omit a parameter, the default value is
used.

- 

`--enable-private-environment` enables a Private IP environment.

- 

`--network` specifies your VPC network ID.

- 

`--subnetwork` specifies your VPC subnetwork ID.

- `--composer-internal-ipv4-cidr-block` specifies the
[environment's internal IP range](/composer/docs/composer-3/connect-vpc-network#internal-range).
This range is used by Managed Airflow in the
[tenant project](/composer/docs/composer-3/environment-architecture) of your environment.

Example (Private IP environment
with a connected VPC network)


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--enable-private-environment \ 
--network NETWORK_ID \ 
--subnetwork SUBNETWORK_ID \ 
```


Replace:

- `NETWORK_ID` with your VPC network ID.

- 

`SUBNETWORK_ID` with your VPC subnetwork ID.




## Step 8. (Optional) Add network tags

Network [tags](/vpc/docs/add-remove-network-tags) are applied to all node VMs in your environment's
cluster. Tags are used to identify valid sources or targets for network
firewalls. Each tag within the list must comply with
[RFC 1035](https://www.ietf.org/rfc/rfc1035.txt).

For example, you might want to add network tags if you plan to restrict
traffic for a Private IP environment with firewall rules.



### Console

On the **Create environment** page:

- Locate the **Network configuration** section.

- In the **Network tags** field, enter network tags for your environment.



### gcloud

When you create an environment, following arguments control network tags:

- `--tags` specifies a comma-separated list of network tags applied to all
node VMs.


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--tags TAGS 
```


Replace:

- `TAGS` with a comma-separated list of network tags.

Example:


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--tags group1,production
```


### API

When you create an environment, in the [Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > 
[EnvironmentConfig](/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify
network tags for your environment.


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"config" : { 
"nodeConfig" : { 
"tags" : [ 
" TAG " 
], 
"serviceAccount" : " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- `TAG` with a network tag.

Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"config" : { 
"nodeConfig" : { 
"tags" : [ 
"group1" , 
"production" 
], 
"serviceAccount" : " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```


### Terraform

When you create an environment, following fields define network tags for
your environment:

- `tags` field in the `node_config` block specifies a comma-separated list
of network tags applied to all node VMs.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 

node_config { 
tags = [ " TAGS " ] 
service_account = " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- `TAGS` with a comma-separated list of network tags.

Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 
node_config { 
tags = [ "group1","production" ] 
service_account = " 
example-account@example-project . s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```



## Step 9. (Optional) Configure web server network access

The Airflow web server access parameters do not depend on the type of your
environment. Instead, you can configure web server access separately. For
example, a Private IP environment can still have the Airflow UI accessible
from the internet.

You can't configure the allowed IP ranges using private IP addresses.



### Console

On the **Create environment** page:

- 

In the **Network configuration** section, expand the **Show network
configuration** item.

- 

In the **Web server network access control** section:

- 

To provide access to the Airflow web server from all IP addresses,
select **Allow access from all IP addresses**.

- 

To restrict access only to specific IP ranges, select
**Allow access only from specific IP addresses**. In the **IP range**
field, specify an IP range in the CIDR notation. In
the **Description** field, specify an optional description for this
range. If you want to specify more than one range, click **Add IP
range**.

- 

To forbid access for all IP addresses, select **Allow access only from
specific IP addresses** and click **Delete item** next to the empty
range entry.



### gcloud

When you create an environment, following arguments control web server
access level:

- 

`--web-server-allow-all` provides access to Airflow from all IP addresses.
This is the default option.

- 

`--web-server-allow-ip` restricts access only to specific source IP
ranges. To specify several IP ranges, use this argument multiple times.

- 

`--web-server-deny-all` forbids access for all IP addresses.


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--web-server-allow-ip ip_range = WS_IP_RANGE ,description = WS_RANGE_DESCRIPTION 
```


Replace:

- `WS_IP_RANGE` with the IP range, in the CIDR notation, that can access
Airflow UI.

- `WS_RANGE_DESCRIPTION` with the description of the IP range.

Example:


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" \ 
--web-server-allow-ip ip_range = 192 .0.2.0/24,description = "office net 1" \ 
--web-server-allow-ip ip_range = 192 .0.4.0/24,description = "office net 3" 
```


### API

When you create an environment, in the [Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > 
[EnvironmentConfig](/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify web server
access parameters.

- 

To provide access to the Airflow web server from all IP addresses,
omit `webServerNetworkAccessControl`.

- 

To restrict access only to specific IP ranges, specify one or more ranges
in `allowedIpRanges`.

- 

To forbid access for all IP addresses, add `allowedIpRanges` and make it an
empty list. Do not specify IP ranges in it.


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"config" : { 
"webServerNetworkAccessControl" : { 
"allowedIpRanges" : [ 
{ 
"value" : " WS_IP_RANGE " , 
"description" : " WS_RANGE_DESCRIPTION " 
} 
] 
}, 
"nodeConfig" : { 
"serviceAccount" : " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- `WS_IP_RANGE` with the IP range, in the CIDR notation, that can access
Airflow UI.

- `WS_RANGE_DESCRIPTION` with the description of the IP range.

Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"config" : { 
"webServerNetworkAccessControl" : { 
"allowedIpRanges" : [ 
{ 
"value" : "192.0.2.0/24" , 
"description" : "office net 1" 
}, 
{ 
"value" : "192.0.4.0/24" , 
"description" : "office net 3" 
} 
] 
}, 
"nodeConfig" : { 
"serviceAccount" : " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```


### Terraform

When you create an environment, the `allowed_ip_range` block in the
`web_server_network_access_control` block contains IP ranges that can access
web server.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 

web_server_network_access_control { 

allowed_ip_range { 
value = " WS_IP_RANGE " 
description = " WS_RANGE_DESCRIPTION " 
} 
} 

node_config { 
service_account = " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- `WS_IP_RANGE` with the IP range, in the CIDR notation, that can access
Airflow UI.

- `WS_RANGE_DESCRIPTION` with the description of the IP range.

Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 

web_server_network_access_control { 
allowed_ip_range { 
value = "192.0.2.0/24" 
description = "office net 1" 
}, 
allowed_ip_range { 
value = "192.0.4.0/24" 
description = "office net 3" 
} 
} 

node_config { 
service_account = " 
example-account@example-project . s3ns.iam.gserviceaccount.com
" 
} 

} 
```



## Step 10. (Optional) Specify Airflow configuration overrides and environment variables

You can set up [Airflow configuration overrides](/composer/docs/composer-3/override-airflow-configurations) and
[environment variables](/composer/docs/composer-3/set-environment-variables) when you create an environment. As an
alternative, you can do it later, after your environment is created.

Some Airflow configuration options [are blocked](/composer/docs/airflow-configurations) and you
can't override them.

For the list of available Airflow configuration options, see
[Configuration reference for Airflow 2](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) 
and [Airflow 1.10.*](https://airflow.apache.org/docs/apache-airflow/1.10.15/configurations-ref.html) 

To specify Airflow configuration overrides and environment variables:



### Console

On the **Create environment** page:

- 

In the **Environment variables** section, click
**Add environment variable**.

- 

Enter the **Name** and **Value** for the environment variable.

- 

In the **Airflow configuration overrides** section, click
**Add Airflow configuration override**.

- 

Enter the **Section**, **Key**, and **Value** for the configuration
option override.

For example:



| 
Section | 
Key | 
Value | 
|




| 
`webserver` | 
`dag_orientation` | 
`TB` | 
|





### gcloud

When you create an environment, following arguments control environment
variables and Airflow configuration overrides:

- 

`--env-variables` specifies a comma-separated list of environment
variables.

Variable names may contain upper and lowercase letters, digits, and
underscores, but they may not begin with a digit.

- 

`--airflow-configs` specifies a comma-separated list of keys and values
for Airflow configuration overrides.


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--env-variables ENV_VARS \ 
--airflow-configs CONFIG_OVERRIDES 
```


Replace:

- `ENV_VARS` with a list of comma-separated `NAME=VALUE` pairs for
environment variables.

- `CONFIG_OVERRIDES` with a list of comma-separated `SECTION-KEY=VALUE`
pairs for configuration overrides. Separate the name of the
configuration section with a `-` symbol, followed by the key name. For
example: `core-dags_are_paused_at_creation`.

Example:


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" \ 
--env-variables SENDGRID_MAIL_FROM = user@example.com,SENDGRID_API_KEY = example-key \ 
--airflow-configs core-dags_are_paused_at_creation = True,webserver-dag_orientation = TB
```


### API

When you create an environment, in the [Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > 
[EnvironmentConfig](/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify
environment variables and Airflow configuration overrides.


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"config" : { 
"softwareConfig" : { 
"airflowConfigOverrides" : { 
" SECTION - KEY " : " OVERRIDE_VALUE " 
}, 
"envVariables" : { 
" VAR_NAME " : " VAR_VALUE " , 
} 
}, 
"nodeConfig" : { 
"serviceAccount" : " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

- `SECTION` with the section in the configuration file where the Airflow
configuration option is located.

- `KEY` with the name of the Airflow configuration option.

- `OVERRIDE_VALUE` with a value of the Airflow configuration option.

- `VAR_NAME` with the name of the environment variable.

- `VAR_VALUE` with the value of the environment variable.

Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"config" : { 
"softwareConfig" : { 
"airflowConfigOverrides" : { 
"core-dags_are_paused_at_creation" : "True" , 
"webserver-dag_orientation" : "TB" 
}, 
"envVariables" : { 
"SENDGRID_MAIL_FROM" : "user@example.com" , 
"SENDGRID_API_KEY" : "example-key" 
} 
}, 
"nodeConfig" : { 
"serviceAccount" : " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```


### Terraform

When you create an environment, following blocks control environment
variables and Airflow configuration overrides:

- 

`env_variables` block in the `software_config` block specifies
environment variables.

Variable names may contain upper and lowercase letters, digits, and
underscores, but they may not begin with a digit.

- 

`airflow_config_overrides` block in the `software_config` block specifies
Airflow configuration overrides.


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

config { 

software_config { 

airflow_config_overrides = { 
SECTION - KEY = " OVERRIDE_VALUE " 
} 

env_variables = { 
VAR_NAME = " VAR_VALUE " 
} 
} 

node_config { 
service_account = " SERVICE_ACCOUNT " 
} 

} 
} 
```


Replace:

- `SECTION` with the section in the configuration file where the Airflow
configuration option is located.

- `KEY` with the name of the Airflow configuration option.

- `OVERRIDE_VALUE` with a value of the Airflow configuration option.

- `VAR_NAME` with the name of the environment variable.

- `VAR_VALUE` with the value of the environment variable.

Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

config { 

software_config { 

airflow_config_overrides = { 
core-dags_are_paused_at_creation = "True" 
webserver-dag_orientation = "TB" 
} 

env_variables = { 
SENDGRID_MAIL_FROM = "user@example.com" 
SENDGRID_API_KEY = "example-key" 
} 
} 

node_config { 
service_account = " 
example-account@example-project . s3ns.iam.gserviceaccount.com
" 
} 
} 
} 
```



## Step 11. (Optional) Specify maintenance windows

Default [maintenance windows](/composer/docs/composer-3/specify-maintenance-windows) in Managed Airflow (Gen 3)
are defined in the following way:

- All times are in the local time zone of the region where your environment is
located, but with daylight saving time ignored.

- On Tuesday, Wednesday, Thursday, and Friday maintenance windows are from
00:00:00 to 02:00:00.

- On Saturday, Sunday, and Monday maintenance windows are from 00:00:00
to 04:00:00.

To specify custom maintenance windows for your environment:



### Console

On the **Create environment** page

- 

Locate the **Maintenance windows** section.

- 

In the **Timezone** drop-down list, choose a time zone for maintenance
windows.

- 

Set **Start time**, **Days**, and **Length**, so that:

- 

At least 12 hours of time is allocated in a single week.

- 

You can use several time slots, but each slot duration must be at least
4 hours.

For example, a period of 4 hours every Monday, Wednesday, and Friday
provides the required amount of time.



### gcloud

The following arguments define maintenance windows parameters:

- `--maintenance-window-start` sets the start time of a maintenance
window.

- `--maintenance-window-end` sets the end time of a maintenance window.

- `--maintenance-window-recurrence` sets
the [maintenance window recurrence](/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window).


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--maintenance-window-start ' DATETIME_START ' \ 
--maintenance-window-end ' DATETIME_END ' \ 
--maintenance-window-recurrence ' MAINTENANCE_RECURRENCE ' 
```


Replace:

- `ENVIRONMENT_NAME` with the name of the environment.

- `DATETIME_START` with the start date and time in the
[date/time input format](/sdk/gcloud/reference/topic/datetimes). Only the specified time of
the day is used, the specified date is ignored.

- `DATETIME_END` with the end date and time in the
[date/time input format](/sdk/gcloud/reference/topic/datetimes). Only the specified time of
the day is used, the specified date is ignored. The specified date and
time must be after the start date.

- 

`MAINTENANCE_RECURRENCE` with
an [RFC 5545](https://www.ietf.org/rfc/rfc5545.txt) RRULE for maintenance
windows recurrence. Managed Airflow supports two formats:

- 

The `FREQ=DAILY` format specifies a daily recurrence.

- 

The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a
recurrence on selected days of the week.

The following example specifies a 6-hour maintenance window between 01:00 and
07:00 (UTC) on Wednesdays, Saturdays, and Sundays. The 1 January, 2023
date is ignored.


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" \ 
--maintenance-window-start '2023-01-01T01:00:00Z' \ 
--maintenance-window-end '2023-01-01T07:00:00Z' \ 
--maintenance-window-recurrence 'FREQ=WEEKLY;BYDAY=SU,WE,SA' 
```


### API

When you create an environment, in the
[Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > 
[EnvironmentConfig](/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify
maintenance windows parameters:


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"config" : { 
"maintenanceWindow" : { 
"startTime" : " DATETIME_START " , 
"endTime" : " DATETIME_END " , 
"recurrence" : " MAINTENANCE_RECURRENCE " 
}, 
"nodeConfig" : { 
"serviceAccount" : " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

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

Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"config" : { 
"maintenanceWindow" : { 
"startTime" : "2023-01-01T01:00:00Z" , 
"endTime" : "2023-01-01T07:00:00Z" , 
"recurrence" : "FREQ=WEEKLY;BYDAY=SU,WE,SA" 
}, 
"nodeConfig" : { 
"serviceAccount" : " SERVICE_ACCOUNT " 
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

node_config { 
service_account = " SERVICE_ACCOUNT " 
} 
} 
} 
```


Replace:

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



## Step 12. (Optional) Data lineage integration

Data lineage is a Knowledge Catalog feature that lets you track data movement.

[Data lineage integration](/composer/docs/composer-3/lineage-integration) is available in all versions
of Managed Airflow (Gen 3).

Data lineage integration is **automatically enabled** in a new
Managed Airflow environment if the following conditions are met:

- 

Data Lineage API is enabled in your project. For more information, see
[Enabling Data Lineage API](/dataplex/docs/use-lineage) in
Knowledge Catalog documentation.

- 

A custom [Lineage Backend](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/lineage.html#lineage-backend) isn't configured in
Airflow.

You can disable data lineage integration when you create an environment. For
example, if you want to override the automatic behavior or choose to
[enable data lineage later](/composer/docs/composer-3/lineage-integration), after the environment is
created.



### Console

To disable data lineage integration, on the **Create environment** page, do
the following:

- 

In the **Advanced configuration** section, expand
**Show advanced configuration**.

- 

In the **Knowledge Catalog Lineage integration** menu, select
**Disable integration with Knowledge Catalog Lineage**.



### gcloud

When you create an environment, the `--disable-cloud-data-lineage-integration`
argument disables the data lineage integration.


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--disable-cloud-data-lineage-integration
```


Replace:

- `ENVIRONMENT_NAME` with the name of the environment.

- `LOCATION` with the region where the environment is located.

Example:


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" \ 
--disable-cloud-data-lineage-integration
```



## Step 13. (Optional) Configure data encryption (CMEK)

By default, data in your environment is encrypted with a key provided by
Google.

To use customer-managed encryption keys (CMEK) to encrypt data in your
environment, follow the instructions outlined in
[Using customer-managed encryption keys](/composer/docs/composer-3/configure-cmek-encryption).

## Step 14. (Optional) Use a custom environment's bucket

When you create an environment, Managed Airflow creates a bucket for
your environment automatically.

As an alternative, you can specify a custom Cloud Storage bucket from your
project. Your environment uses this bucket in the same way as the automatically
created bucket.

To use a custom environment bucket, follow the instructions outlined in
[Use a custom environment's bucket](/composer/docs/composer-3/custom-bucket).

## Step 15. (Optional) Configure database retention

If you enable database retention in your environment, then
Managed Airflow periodically removes records related to DAG
executions and user sessions older than the specified time period from the
Airflow database. The most recent DAG run information is always retained.

**By default, database retention is enabled**. To configure the retention
period for a new environment or disable database retention, follow the
instructions outlined in
[Configure database retention policy](/composer/docs/composer-3/configure-db-retention). You can also configure
database retention later.

## Step 16. (Optional) Specify environment labels

You can assign labels to your environments to
[break down billing costs based on these labels](/composer/docs/composer-3/manage-environment-labels).



### Console

On the **Create environment** page, in the **Labels** section:

- 

Click **Add label**.

- 

In **Key** and **Value** fields, specify key and value pairs for the
environment labels.



### gcloud

When you create an environment, the `--labels` argument specifies a comma-separated list of keys and values with environment labels.


```
gcloud composer environments create ENVIRONMENT_NAME \ 
--location LOCATION \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " SERVICE_ACCOUNT " \ 
--labels LABELS 
```


Replace:

- `LABELS` with a list of comma-separated `KEY=VALUE` pairs for environment
labels.

Example:


```
gcloud composer environments create example-environment \ 
--location us-central1 \ 
--image-version composer-3-airflow-2.11.1-build.21 \ 
--service-account " 
example-account@example-project. s3ns.iam.gserviceaccount.com
" \ 
--labels owner = engineering-team,env = production
```


### API

When you create an environment, in the [Environment](/composer/docs/reference/rest/v1/projects.locations.environments#Environment)
resource, specify labels for your environment.


```
{ 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /environments/ ENVIRONMENT_NAME " , 
"labels" : { 
" LABEL_KEY " : " LABEL_VALUE " 
} 
} 
```


Replace:

- `LABEL_KEY` with a key of the environment label.

- `LABEL_VALUE` with a value of the environment label.

Example:


```
// POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments 

{ 
"name" : "projects/example-project/locations/us-central1/environments/example-environment" , 
"labels" : { 
"owner" : "engineering-team" , 
"env" : "production" 
} 
} 
```


### Terraform

When you create an environment, specify labels in the `labels` block (
outside of the `config` block).


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = " ENVIRONMENT_NAME " 
region = " LOCATION " 

labels = { 
LABEL_KEY = " LABEL_VALUE " 
} 

} 
```


Replace:

- `LABEL_KEY` with a key of the environment label.

- `LABEL_VALUE` with a value of the environment label.

Example:


```
resource "google_composer_environment" "example" { 
provider = google-beta 
name = "example-environment" 
region = "us-central1" 

labels = { 
owner = "engineering-team" 
env = "production" 
} 

} 
```



## What's next

- [Troubleshooting environment creation](/composer/docs/composer-3/troubleshooting-environment-creation)

- [Configuring Shared VPC](/composer/docs/composer-3/configure-shared-vpc)

- [Configuring VPC Service Controls](/composer/docs/composer-3/configure-vpc-sc)

- [Adding and updating DAGs](/composer/docs/composer-3/manage-dags)

- [Accessing Airflow UI](/composer/docs/composer-3/access-airflow-web-interface)

- [Updating and deleting environments](/composer/docs/composer-3/update-environments)

- [About Managed Airflow versions](/composer/docs/composer-versioning-overview)