# Managed Airflow overview

Source: https://documentation.s3ns.fr/composer/docs/latest/composer-overview
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












# Managed Airflow overview 





















This page provides a brief introduction to Airflow and DAGs, and describes the
features and capabilities of Managed Airflow.

For more information about new features in Managed Airflow releases,
see [Release notes](/composer/docs/release-notes).

## About Managed Airflow

Managed Airflow is a fully managed workflow orchestration service,
enabling you to create, schedule, monitor, and manage workflow pipelines
that span across clouds and on-premises data centers.

Managed Airflow is built on the popular
[Apache Airflow](https://airflow.apache.org) open source project and
operates using the Python programming language.

By using Managed Airflow instead of a local instance of Apache
Airflow, you can benefit from the best of Airflow with no installation or
management overhead. Managed Airflow helps you create managed Airflow
environments quickly and use Airflow-native tools, such as the powerful
Airflow web interface and command-line tools, so you can focus on your
workflows and not your infrastructure.

## Differences between Managed Airflow versions

For more information about differences between major versions of
Managed Airflow, see
[Managed Service for Apache Airflow versioning overview](/composer/docs/composer-versioning-overview).

## Airflow and Airflow DAGs (workflows)

In data analytics, a *workflow* represents a series of tasks for ingesting,
transforming, analyzing, or utilizing data. In Airflow, workflows are created
using DAGs, or "Directed Acyclic Graphs".




**Figure 1.** Relationship between DAGs and tasks



A *DAG* is a collection of tasks that you want to schedule and run, organized
in a way that reflects their relationships and dependencies. DAGs are created
in Python files, which define the DAG structure using code. The DAG's
purpose is to ensure that each task is executed at the right time
and in the right order.

Each *task* in a DAG can represent almost anything—for example, one task
might perform any of the following functions:

- Preparing data for ingestion

- Monitoring an API

- Sending an email

- Running a pipeline

In addition to running a DAG on a schedule, you can trigger DAGs manually or
in response to events, such as changes in a Cloud Storage
bucket. For more information, see [Schedule and trigger DAGs](/composer/docs/composer-3/schedule-and-trigger-dags).

For more information about DAGs and
tasks, see the
[Apache Airflow documentation](https://airflow.apache.org/docs/stable/concepts.html).

## Managed Airflow environments

*Managed Airflow environments* are self-contained Airflow
deployments based on Google Kubernetes Engine. They work with other Cloud de Confiance
services using connectors built into Airflow. You can
[create one or more environments](/composer/docs/composer-3/create-environments) in a single Cloud de Confiance
project, in any [supported region](/about/locations).

Managed Airflow provisions Cloud de Confiance services that run
your workflows and all Airflow components. The main components of an
environment are:

- 

*GKE cluster*: Airflow components such as Airflow
schedulers, triggerers, and workers run as GKE workloads
in a single cluster created for your environment, and are responsible for
processing and executing DAGs.

The cluster also hosts
[other Managed Airflow components](/composer/docs/composer-3/environment-architecture) like Composer Agent
and Airflow Monitoring, which help manage the Managed Airflow
environment, gather logs to store in Cloud Logging, and gather
metrics to upload to Cloud Monitoring.

- 

*Airflow web server*: The web server runs the Apache Airflow UI.

- 

*Airflow database*: The database holds the Apache Airflow metadata.

- 

*Cloud Storage bucket*: Managed Airflow associates
a Cloud Storage bucket with your environment.
This bucket, also called *environment's bucket*, stores the
[DAGs](/composer/docs/composer-3/manage-dags), [logs](/composer/docs/composer-3/view-logs), custom
[plugins](/composer/docs/composer-3/install-plugins),
and data for the environment. For more information about the environment's
bucket see
[Data stored in Cloud Storage](/composer/docs/composer-3/cloud-storage).

For an in-depth look at the components of an environment, see
[Environment architecture](/composer/docs/composer-3/environment-architecture).

## Managed Airflow interfaces

Managed Airflow provides interfaces for managing environments,
Airflow instances that run within environments, and individual DAGs.

For example, you can [create](/composer/docs/composer-3/create-environments) and configure
Managed Airflow environments in Cloud de Confiance console,
Google Cloud CLI, [Cloud Composer API](/composer/docs/apis), or Terraform.

As another example, you can [manage DAGs](/composer/docs/composer-3/manage-dags) from
Cloud de Confiance console, [native Airflow UI](/composer/docs/composer-3/access-airflow-web-interface), or by running
Google Cloud CLI and [Airflow CLI commands](/composer/docs/composer-3/access-airflow-cli).

## Airflow features in Managed Airflow

When using Managed Airflow, you can manage and use Airflow features
such as:

- 

[Airflow DAGs](/composer/docs/composer-3/manage-dags): You can add, update, remove, or trigger
Airflow DAGs in Cloud de Confiance console or using the native Airflow UI.

- 

[Airflow configuration options](/composer/docs/composer-3/override-airflow-configurations): You can change Airflow
configuration options from default values used by
Managed Airflow to custom values. In
Managed Airflow, some of the configuration options are
[blocked](/composer/docs/airflow-configurations), and you cannot change their values.

- 

[Airflow connections](/composer/docs/composer-3/manage-airflow-connections).

- 

[Airflow UI](/composer/docs/composer-3/access-airflow-web-interface).

- 

[Airflow CLI](/composer/docs/composer-3/access-airflow-cli).

- 

[Custom plugins](/composer/docs/composer-3/install-plugins): You can install
[custom Airflow plugins](https://airflow.apache.org/docs/apache-airflow/stable/plugins.html), such as
custom, in-house Apache Airflow operators, hooks,
sensors, or interfaces, into your Managed Airflow environment.

- 

[Python dependencies](/composer/docs/composer-3/install-python-dependencies): You can install Python
dependencies from the [Python Package Index](https://pypi.org) 
in your environment or from a private package repository, including
Artifact Registry repositories. If the
dependencies are not in the package index, you can also use plugins.

- 

Logging and monitoring for DAGs, Airflow components, and
Managed Airflow environments:

- 

You can view Airflow logs that are associated with single DAG tasks
in the [Airflow web interface](/composer/docs/composer-3/access-airflow-web-interface)
and the `logs` folder in the [environment's bucket](/composer/docs/composer-3/cloud-storage).

- 

[Cloud Monitoring logs and environment metrics](/composer/docs/composer-3/monitor-environments)
for Managed Airflow environments.

## Access control in Managed Airflow

You manage security at the Cloud de Confiance project level and can
[assign IAM roles](/composer/docs/composer-3/access-control) that allow individual
users to modify or create environments. If someone does not have access
to your project or does not have an appropriate Managed Airflow
IAM role, that person cannot access any of your environments.

In addition to IAM, you can use
[Airflow UI access control](/composer/docs/composer-3/airflow-rbac), which is based on the Apache
Airflow Access Control model.

For more information about security features in Managed Airflow, see
[Managed Airflow security overview](/composer/docs/composer-3/composer-security-overview).

## Environment networking

Managed Airflow supports several networking configurations for
environments, with many configuration options. For example, in a Private IP
environment, DAGs and Airflow components are fully isolated from the public
internet.

For more information about networking in Managed Airflow, see pages
for individual networking features:

- [Public IP and Private IP environments](/composer/docs/composer-3/change-networking-type)

- [Connecting an environment to your VPC network](/composer/docs/composer-3/connect-vpc-network)

- [Shared VPC environments](/composer/docs/composer-3/configure-shared-vpc)

- [Configuring VPC Service Controls](/composer/docs/composer-3/configure-vpc-sc)

## Other features of Managed Airflow

Other Managed Airflow features include:

- [Autoscaling environments](/composer/docs/composer-3/scale-environments)

- [Development with local Airflow environments](/composer/docs/composer-3/run-local-airflow-environments)

- [Highly resilient environments](/composer/docs/composer-3/set-up-highly-resilient-environments)

- [Environment snapshots](/composer/docs/composer-3/save-load-snapshots)

- [Encryption with customer-managed encryption keys (CMEK)](/composer/docs/composer-3/configure-cmek-encryption)

## Frequently Asked Questions

### What version of Apache Airflow does Managed Airflow use?

Managed Airflow environments are based on
[Managed Airflow images](/composer/docs/composer-versions#images). When you create an
environment, you can select an image with a specific Airflow version:

- Managed Airflow (Gen 3) supports Airflow 2 and Airflow 3.

You have control over the Apache Airflow version of your environment. You can
decide to [upgrade your environment](/composer/docs/composer-3/upgrade-environments) to a later version of
Managed Airflow image. Each
[Managed Airflow release](/composer/docs/release-notes) supports several Apache
Airflow versions.

### Can I use native Airflow UI and CLI?

You can access the Apache Airflow web interface of your environment. Each of
your environments has its own Airflow UI. For more information about accessing
the Airflow UI, see [Airflow web interface](/composer/docs/composer-3/access-airflow-web-interface).

To run Airflow CLI commands in your environments, use `gcloud` commands.
For more information about running Airflow CLI commands in
Managed Airflow environments, see
[Airflow command-line interface](/composer/docs/composer-3/access-airflow-cli).

### Can I use my own database as the Airflow database?

Managed Airflow uses a managed database service for the Airflow
database. It is not possible to use a user-provided database
as the Airflow database.

### Can I use my own cluster as a Managed Airflow cluster?

Managed Airflow uses Google Kubernetes Engine service to create, manage and
delete environment clusters where Airflow components run. These clusters are
fully managed by Managed Airflow.

It is not possible to build a Managed Airflow environment based on a
self-managed Google Kubernetes Engine cluster.

### Can I use my own container registry?

Managed Airflow uses Artifact Registry service to manage container
image repositories used by Managed Airflow environments.
It is not possible to replace it with a user-provided container registry.

### Are Managed Airflow environments zonal or regional?

When you create an environment, you specify a region for it:

- Highly resilient (Highly Available)
Managed Airflow environments
have a multi-zonal Airflow database and a multi-zonal Airflow execution
layer. A highly resilient environment runs across at least two zones of the
selected region. Managed Airflow automatically distributes the
components of your environment between zones. The Cloud SQL
component that stores the Airflow database has a primary instance and a
standby instance distributed between zones in the selected region.

## What's next

- Learn about [Managed Airflow differences in Cloud de Confiance versus Google Cloud](/composer/docs/tpc-differences).

- [Security overview](/composer/docs/composer-3/composer-security-overview)

- [Create environments](/composer/docs/composer-3/create-environments)

- [Environment architecture](/composer/docs/composer-3/environment-architecture)