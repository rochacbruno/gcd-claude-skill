# Save and load environment snapshots

Source: https://documentation.s3ns.fr/composer/docs/latest/save-load-snapshots
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












# Save and load environment snapshots 





















This page explains how to save and load the state of your environment using
environment snapshots.

You can configure your environment to automatically save snapshots. For more
information, see [Configure scheduled snapshots](/composer/docs/composer-3/configure-scheduled-snapshots).

## About environment snapshots

Environment snapshots store the state of your environment. You can save and
load environment snapshots on demand.

You can use snapshots to:

- 

Restore your environment to an earlier state. Create backups of your
environment using snapshots, then load one of the snapshots to restore your
environment. For example, you can roll back an update operation that
installs PyPI packages or overrides Airflow configuration options, even
after your environment is successfully updated.

- 

Perform side-by-side upgrades and copy environments. Create a snapshot of an
existing environment, create a new environment that uses the same or later
version of Managed Airflow, then apply the snapshot to this new
environment. This procedure is similar to
[migrating](/composer/docs/composer-1/migrate-composer-2-snapshots-af-2). Make sure to pause DAGs before
you make the snapshot, to avoid duplicate DAG runs.

### How snapshots are stored

An environment snapshot is a set of files that describe the state of your
environment and store the backup of the environment data.

You can create multiple snapshots of your environment. Environment snapshots
are non-incremental. You can use any snapshot independently of other snapshots.

Managed Airflow does not delete snapshots when you delete your
environment.

By default, Managed Airflow stores snapshots in the `snapshots/`
folder in your environment's bucket. You can also specify a custom location
when you create a snapshot.

While the Cloud Storage UI displays data as folders for convenience,
buckets work in a flat-file structure. This doesn't change how you work with
saving and loading snapshots in the Cloud de Confiance console, but keep this in
mind when you perform operations directly on the files in your bucket. For more
information, see [Object namespace](/storage/docs/objects#namespace).

### Security considerations for snapshots

To mitigate this security risk, you can store sensitive information
that is used by Airflow DAGs, such as keys or passwords, in
Secret Manager. For more information, see
[Configure Secret Manager for your environment](/composer/docs/composer-3/configure-secret-manager).

Make sure to check security permissions for your environment's bucket. If you
store environment snapshots in a custom bucket, make sure that
[access permissions](/storage/docs/access-control/iam-roles) for it are configured properly in your
project. When assigning permissions, make sure that environment's service
account [has enough permissions](#before) to save and load snapshots from the
bucket.

### What data is saved in snapshots

Managed Airflow saves the following data in snapshots:

- Airflow configuration overrides.

- Environment variables.

- List of custom PyPI packages, as requirements.

- A backup of the Airflow database, including states of executed tasks, and DAG
runs history.

- A backup of the `/dags`, `/data`, and `/plugins` folders from the
environment's bucket.

- Environment's [fernet key](/composer/docs/composer-3/manage-airflow-connections).

- Other information about the environment's configuration, such as
environment's scale and performance parameters.
Managed Airflow does not use this information when it loads
snapshots. 

### What data is loaded from snapshots

Managed Airflow loads the following data from snapshots:

- Airflow configuration overrides.

- Environment variables.

- 

Custom PyPI packages (unless you choose to skip installing them).

- 

The contents of the Airflow database, including states of executed tasks, and
DAG runs history.

- 

Contents of the `/dags`, `/data`, and `/plugins` folders from the snapshot
are loaded into the environment's bucket.

- 

The fernet key from the snapshot is used to re-encrypt the data from the
snapshot with the environment's own fernet key. The fernet key of the
environment remains unchanged.

Although Managed Airflow stores some information about the
environment's configuration in snapshots, it is not used when loading
snapshots. The following parameters of your environment do not change when you
load a snapshot:

- Environment configuration, such as environment scale and performance
parameters.

- Environment's networking configuration.

- Contents of the environment's bucket outside of the `/dags`, `/data`, and
`/plugins` folders.

- Environment labels.

Any settings that you applied in Managed Airflow infrastructure
without using Cloud Composer API might be lost when you load a
snapshot.

### About partially completed operations

When you load a snapshot, the operation can be successful, failed, or partially
completed:

- Successful operations load all data from the snapshot.

- Failed operations do not introduce any changes.

- Partially completed operations load a subset of data from the snapshot. Such
operations are reported as failed, but the error message indicates what
data was successfully loaded. For example, if PyPI packages are installed,
but Airflow configuration option overrides did not succeed, the error
message indicates this.

For a partially completed operation, you can try to load the same snapshot
again. Managed Airflow skips steps that were successful on the
previous attempt. For example, if an operation failed on a timeout, but the
database was successfully loaded, then the next attempt does not load the
database again.

## Before you begin

- 

Snapshots are supported in Managed Airflow (Gen 2) version 2.0.9 and later.
Managed Airflow (Legacy Gen 1) supports saving environment snapshots in 1.18.5 and later
versions. 

- 

Snapshots do not create an environment. If you want to load a snapshot from
an environment to a different environment, you first need to create a new
environment and then load the snapshot to it.

- 

You cannot load snapshots to environments that are in the error state. It is
not possible to fix such environments by loading a snapshot. You can still
load an existing snapshot to a new environment.

- 

You can only load snapshots to the same or later version of Airflow. For
example, you cannot load a snapshot from Airflow 2.9.3 to Airflow 2.7.3.

- 

It is possible to load a snapshot from a later Airflow build of the same
Airflow version to an environment with an earlier build. For example, you
can load `airflow-2.9.3-build.6` to `airflow-2.9.3-build.5`. We recommend
to load snapshots to earlier builds only if it's necessary to do so.

- 

The maximum size of the Airflow database that supports snapshots is
20 GB. If your environment's database takes
more than 20 GB,
[reduce the size of the Airflow database](/composer/docs/composer-3/cleanup-airflow-database) before saving a
snapshot.

- 

The total number of objects in the `/dags`, `/plugins` and `/data` folders in
the environment's bucket must be less than 100,000 to
create snapshots.

- 

If you use the XCom mechanism to transfer files, make sure that you
[use it according to Airflow's guidelines](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html#object-storage-xcom-backend).
Transferring big files or a large number of files using XCom impacts
Airflow database's performance and can lead to failures when loading
snapshots or upgrading your environment. Consider using alternatives such
as Cloud Storage to transfer large volumes of data.

- 

The maximum length of an object's name in the environment's bucket must be no
longer that 1024 symbols. Otherwise, snapshots cannot be created.

- 

If you save snapshots in a location outside your environment's
bucket, the [service account of your environment](/composer/docs/composer-3/access-control#service-account) must have
read and write permissions for the specified location. For example, the
[**Storage Object Admin** role](/storage/docs/access-control/iam-roles) has such permissions. You
can apply it to a project or to a specific bucket.

- 

Creating and storing snapshots produces additional costs, which are related
to Cloud Storage. For more information, see [Pricing](/composer/pricing).

## Save an environment snapshot

Managed Airflow saves environment snapshots in a
[subfolder](/storage/docs/objects#namespace), relative to the folder that you specify.
The folder name contains the project ID, the environment's location, the
environment's name, and the timestamp when the snapshot was saved. For example:
`/snapshots/example-project_us-central1_example-environment_2022-01-05T18-59-00`.



### Console

To create a snapshot of your environment:

- 

In Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

In the list of environments, click the name of your environment.
The **Environment details** page opens.

- 

Click **Save snapshot**.

- 

In the **Save snapshot** dialog, select where to store the snapshot:

- 

To store the snapshot in the `/snapshots` folder in the environment's
bucket, select **Use snapshot folder in environment bucket
(default)**.

- 

To store the snapshot in the custom folder, select
**Use custom folder in another bucket**, then specify a location.

- 

Click **Save**.



### gcloud

The `gcloud composer environments snapshots save` command saves a
snapshot of your environment.

- The `snapshot-location` argument specifies a folder where the snapshot is
saved. By default, snapshots are saved in the `/snapshots` folder in your
environment's bucket. For example,
`gs://us-central1-example-916807e1-bucket/snapshots`. You can also specify
any other folder.

To save a snapshot of your environment, run:


```
gcloud composer environments snapshots save \ 
ENVIRONMENT_NAME \ 
--location LOCATION \ 
--snapshot-location " SNAPSHOTS_FOLDER " 
```


Replace:

- `ENVIRONMENT_NAME` with the name of the environment.

- `LOCATION` with the region where the environment is located.

- (Optional) `SNAPSHOTS_FOLDER` with the URI of a bucket folder where to store
the snapshot. If you omit this argument, Managed Airflow saves
the snapshot in the `/snapshots` folder in your environment's bucket.

The following example uses the default location:


```
gcloud composer environments snapshots save \ 
example-environment \ 
--location us-central1
```


The following example saves to a custom folder:


```
gcloud composer environments snapshots save \ 
example-environment \ 
--location us-central1 \ 
--snapshot-location "gs://example-bucket/environment_snapshots" 
```


### API

- 

Construct an
[`environments.saveSnapshot`](/composer/docs/reference/rest/v1/projects.locations.environments/saveSnapshot)
API request.

- 

In the request body, in the `snapshotLocation` field, specify
the folder where you want to save the snapshot.


```
{ 
"snapshotLocation" : " SNAPSHOTS_FOLDER " 
} 
```


Replace:

- `SNAPSHOTS_FOLDER` with the URI of a bucket folder where to
save the snapshot.

Example:


```
// POST https://composer.googleapis.com/v1/projects/example-project/ 
// locations/us-central1/environments/example-environment:saveSnapshot 

{ 
"snapshotLocation" : "gs://us-central1-example-916807e1-bucket/snapshots" 
} 
```


### Terraform

It is not possible to save and load environment snapshots from Terraform.

Saving and loading snapshots are actions performed on an environment, and the
resulting snapshots are not a part of an environment's definition. Since
Terraform manages only Managed Airflow environment's configuration,
you cannot save or load environment snapshots from it.



## Load an environment snapshot

Consider the following situation. For example,
[catch-up](https://airflow.apache.org/docs/apache-airflow/stable/dag-run.html#catchup) is enabled and Airflow executes a DAG
on a schedule between the time when the snapshot was created and when it was
loaded. In this case, after you load the snapshot, Airflow has no information
about the DAG run that happened, so Airflow runs the DAG again for the
same time and data.

As another example, consider a DAG that runs on a daily schedule. You take a
snapshot, then Airflow executes this DAG, and after that you load the snapshot
on the same day. In this case, Airflow runs the DAG again, even if catch-up
is disabled.



### Console

To load a snapshot to your environment:

- 

In Cloud de Confiance console, go to the **Environments** page.

[Go to Environments](https://console.cloud.s3nscloud.fr/composer/environments) 

- 

In the list of environments, click the name of your
environment. The **Environment details** page opens.

- 

Click **Load snapshot**.

- 

In the **Load snapshot** dialog, click **Browse**.

- 

Select a folder that stores the snapshot. The name of the folder lists the
ID of your project, environment's location and the timestamp when the
snapshot was saved. For example,
`/snapshots/example-project_us-central1_example-environment_2022-01-05T18-59-00`.

- 

(Optional) To skip the installation of custom PyPI packages from the
snapshot, select **Skip PyPI packages installation**. If you load a
snapshot of an environment with installed
[custom PyPI packages](/composer/docs/composer-3/install-python-dependencies),
then Managed Airflow does not install these custom packages.

- 

Click **Load** and wait until Managed Airflow loads the snapshot.



### gcloud

The `gcloud composer environments snapshots load` command loads a
snapshot to your environment.

- 

The `--snapshot-path` argument specifies a folder where the snapshot is
located.

The name of the folder lists the ID of your project, environment's
location and the timestamp when the snapshot was saved. For example,
`gs://us-central1-example-916807e1-bucket/snapshots/example-project_us-central1_example-environment_2022-01-05T18-59-00`.

- 

(Optional) The `--skip-pypi-packages-installation` argument skips the
installation of custom PyPI packages from the snapshot. If you load a
snapshot of an environment with installed
[custom PyPI packages](/composer/docs/composer-3/install-python-dependencies),
then Managed Airflow does not install these custom packages.


```
gcloud composer environments snapshots load \ 
DESTINATION_ENVIRONMENT_NAME \ 
--location LOCATION \ 
--snapshot-path " SNAPSHOT_PATH " 
```


Replace:

- `DESTINATION_ENVIRONMENT_NAME` with the name of the environment where you
want to load the snapshot.

- `LOCATION` with the region where the environment is located.

- `SNAPSHOT_PATH` with the URI of a bucket, followed by the path to the
snapshot.

Example:


```
gcloud composer environments snapshots load \ 
example-environment \ 
--location us-central1 \ 
--snapshot-path "gs://us-central1-example-916807e1-bucket/snapshots/example-project_us-central1_example-environment_2022-01-05T18-59-00" 
```


### API

- 

Construct an
[`environments.loadSnapshot`](/composer/docs/reference/rest/v1/projects.locations.environments/loadSnapshot)
API request.

- 

In the request body, in the `snapshotPath` field, specify
the URI of a bucket, followed by the path to the snapshot. The name of
the folder lists the ID of your project, environment's location and the
timestamp when the snapshot was saved. For example,
`gs://us-central1-example-916807e1-bucket/snapshots/example-project_us-central1_example-environment_2022-01-05T18-59-00`.

- 

(Optional) In the request body, in the `skipPypiPackagesInstallation` field
specify if Managed Airflow must skip the
installation of custom PyPI packages from the snapshot. If you load a
snapshot of an environment with installed
[custom PyPI packages](/composer/docs/composer-3/install-python-dependencies),
then Managed Airflow does not install these custom packages.

This field is optional. If you omit this field, Managed Airflow
installs PyPI packages from the snapshot.


```
{ 
"snapshotPath" : " SNAPSHOT_PATH " 
} 
```


Replace:

- `SNAPSHOT_PATH` with the URI of a bucket folder where to
store the snapshot.

Example:


```
// POST https://composer.googleapis.com/v1/projects/example-project/ 
// locations/us-central1/environments/example-environment:loadSnapshot 

{ 
"snapshotPath" : "gs://us-central1-example-916807e1-bucket/snapshots/example-project_us-central1_example-environment_2022-01-05T18-59-00" , 
"skipPypiPackagesInstallation" : "False" 
} 
```


### Terraform

It is not possible to save and load environment snapshots using Terraform.

Saving and loading snapshots are actions performed on an environment, and the
resulting snapshots are not a part of an environment's definition. Since
Terraform manages only Managed Airflow environment's configuration,
you cannot save or load environment snapshots from it.



## What's next

- [Configure scheduled snapshots](/composer/docs/composer-3/configure-scheduled-snapshots)

- [Create environments](/composer/docs/composer-3/create-environments)

- [Access control](/composer/docs/composer-3/access-control)