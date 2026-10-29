# Copy data to or from instances

Source: https://documentation.s3ns.fr/filestore/docs/copying-data
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/filestore/docs/tpc-differences) for more details.














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

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Filestore

](https://documentation.s3ns.fr/filestore/docs)






- 








[

Guides

](https://documentation.s3ns.fr/filestore/docs/overview)












# Copy data to or from instances 














This page shows you how to copy data from:

- Cloud Storage buckets to Filestore file shares

- Computers in your environment to Filestore file shares

- Filestore file shares to Cloud Storage buckets

We recommend the following options for transferring large volumes of data:

- [Transfer Appliance](/transfer-appliance): If you're looking to
transfer data to Cloud de Confiance by S3NS offline or from an area with poor internet
connectivity.

- [Storage Transfer Service](/storage-transfer/docs/overview): If you want to transfer
data to Cloud de Confiance from an online data source, such as another cloud
product.

- [Transfer service for on-premises data](/storage-transfer/docs/on-prem-overview): If you want to transfer
data from on-premises to Cloud de Confiance.

## Before you begin

To follow these instructions, you must [install](/sdk/docs/install) the
[gcloud CLI](/sdk/gcloud).

## Copy data from a Cloud Storage bucket to a Filestore file share

To copy data from a Cloud Storage bucket to a Filestore file share
that's mounted on a Compute Engine VM instance, use the
[`gcloud storage rsync`](/sdk/gcloud/reference/storage/rsync) command. This
command works on both Linux and Windows VMs. To copy data on Linux VM instances,
you can also use standard commands like
[`rsync`](https://linux.die.net/man/1/rsync).



### Linux

- 

In the Cloud de Confiance console, go to the VM Instances page.

[Go to the Compute Engine instances page](https://console.cloud.s3nscloud.fr/compute/instances) 

- 

Choose a Compute Engine VM instance that has the target Filestore
file share mounted and click **SSH** to open a terminal on that VM instance.

- 

Copy data to the mounted Filestore file share by running the
following command. To recursively synchronize subdirectories of the
location you specify, use the `--recursive` option with the
`gcloud storage rsync` command.


```
gcloud storage rsync gs:// bucket mount-directory 
```


where:

- bucket is the Cloud Storage bucket, directory, or
subdirectory to copy data from.

- mount-directory is the directory on the client where
the Filestore file share is mounted.

#### Example

The following command copies data from the `data` bucket and all
subdirectories to the `/mnt/filer` directory.


```
gcloud storage rsync gs://data /mnt/filer --recursive
```


### Windows

- 

In the Cloud de Confiance console, go to the VM Instances page.

[Go to the Compute Engine instances page](https://console.cloud.s3nscloud.fr/compute/instances) 

- 

Choose a Compute Engine VM instance that has the target Filestore
file share mapped to a drive and click **RDP** to open a
remote desktop connection to that VM.

- 

Copy data to the mapped Filestore file share by running the
following command. To recursively synchronize subdirectories of the
location you specify, use the `--recursive` option with the
`gcloud storage rsync` command.


```
gcloud storage rsync gs:// bucket mount-directory 
```


where:

- bucket is the Cloud Storage bucket, directory, or
subdirectory to copy data from.

- mount-directory is the directory on the client where
the Filestore file share is mounted.

#### Example

The following command copies data from the `data` bucket and all subdirectories
to the `Z:` drive that is mapped to the Filestore file share.


```
gcloud storage rsync gs://data Z:\ --recursive
```



## Copy data from a computer in your environment to a Filestore file share

To copy data from a computer in your environment to a Filestore
file share that is mounted on a Compute Engine Linux VM instance, use
the [`gcloud compute scp`](/sdk/gcloud/reference/compute/scp) command . The
`gcloud compute scp` command doesn't work on Windows VM instances.

- Use SSH to connect to the computer that contains the data you want to copy.

- 

Check whether you have the gcloud CLI installed by running the following
command:


```
which gcloud
```


If the gcloud CLI is installed, the command returns the installation path.
If no installation path is returned, follow the instructions at
[Installing gcloud CLI](/sdk/downloads) to install it.

- 

Copy data to the mounted Filestore file share:


```
gcloud compute scp local-data-path client-name :/ mount-directory --project= project-id --zone= zone 
```


where:

- local-data-path is the path of a local file or directory that
contains the data you want to copy to the instance. If you want to copy
data from other subdirectories, use the `--recurse` flag after
local-data-path .

- client-name is the name of the Compute Engine VM instance that the
Filestore file share is mounted on.

- mount-directory is the directory on the client where
the Filestore file share is mounted.

- project-id is the ID of the project that contains the client
VM instance.
If you have set the `gcloud` default project by using
[`gcloud config set project project-id `](/sdk/gcloud/reference/config/set),
you can skip this flag and use the default project instead.

- zone is the zone in which the Compute Engine VM instance resides.
If you have set the `gcloud` default zone by using
[`gcloud config set compute/zone zone `](/sdk/gcloud/reference/config/set),
you can skip this flag and use default zone instead.

#### Example

The following command copies data from the local `/etc/acme/data` directory
and its subdirectories to the `/mnt/filer` directory on the `nfs-client` VM
instance, in the `myproject` project, in zone `us-central1-c`:


```
gcloud compute scp /etc/acme/data --recurse nfs-client:/mnt/filer --project myproject --zone us-central1-c
```


## Copy data from a Filestore file share to a Cloud Storage bucket

You can copy data from a Filestore file share that is mounted on a
Compute Engine VM instance to a Cloud Storage bucket by using the
[`gcloud storage rsync`](/sdk/gcloud/reference/storage/rsync) command.

Before proceeding, first make sure that the Compute Engine VM can write to
Cloud Storage:

- 

In the Cloud de Confiance console, go to the VM Instances page.

[Go to the Compute Engine instances page](https://console.cloud.s3nscloud.fr/compute/instances) 

- 

Choose a Compute Engine VM instance that has the source Filestore
file share mounted.

- 

Check whether the instance has **Read Write** scope:

- Click the instance name to open the instance details page.

- Expand **Cloud API access scopes** and see if **Storage** has **Read
Write** scope.

If the Compute Engine VM doesn't have **Read Write** scope, perform the following steps:

- Stop the Compute Engine instance by clicking **Stop**.

- When the instance has stopped, click **Edit** at the top of the page.

- Under **Access scopes**, select **Set access for each API**.

- Under **Storage**, select **Read Write**, and click **Save**.

- When the instance finishes updating, click **Start** at the top of the page.

To copy data from a Filestore file share to a Cloud Storage
bucket, perform the following:



### Linux

- 

In the Cloud de Confiance console, go to the VM Instances page.

[Go to the Compute Engine instances page](https://console.cloud.s3nscloud.fr/compute/instances) 

- 

Choose a Compute Engine VM instance that has the source Filestore
file share mounted, and then click **SSH** to open a terminal on that
VM instance.

- 

Copy data from the mounted Filestore file share by running
the following command. To recursively synchronize subdirectories of the
location you specify, use the `--recursive` option with the
`gcloud storage rsync` command.


```
gcloud storage rsync mount-directory gs:// bucket 
```


where:

- mount-directory is the directory on the client where
the Filestore file share is mounted.

- bucket is the Cloud Storage bucket, directory, or
subdirectory to copy data to.

#### Example

The following command copies data from the `/mnt/filer` directory and all
subdirectories to the `archive` bucket.


```
gcloud storage rsync /mnt/filer gs://archive --recursive
```


### Windows

- 

In the Cloud de Confiance console, go to the VM Instances page.

[Go to the Compute Engine instances page](https://console.cloud.s3nscloud.fr/compute/instances) 

- 

Choose a Compute Engine VM instance that has the source Filestore
file share mounted, and then click **RDP** to open a
remote desktop connection to that VM.

- 

Copy data from the mapped Filestore file share by running
the following command. To recursively synchronize subdirectories of the
location you specify, use the `--recursive` option with the
`gcloud storage rsync` command.


```
gcloud storage rsync mapped-drive gs:// bucket 
```


where:

- mapped-drive is the drive on the client to which
the Filestore file share is mapped.

- bucket is the Cloud Storage bucket, directory, or
subdirectory to copy data to.

#### Example

The following command copies data from the mapped drive `Z:` and all
subdirectories to the `archive` bucket.


```
gcloud storage rsync Z:\ gs://archive --recursive
```



## Troubleshooting

Copying data from Cloud Storage to a Filestore instance using the
gcloud CLI can be slow. For detailed information on how to improve
performance, see [Improve performance across Cloud de Confiance resources](/filestore/docs/performance#across-resources).