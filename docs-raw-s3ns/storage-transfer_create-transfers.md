# Create transfers

Source: https://documentation.s3ns.fr/storage-transfer/docs/create-transfers
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/storage-transfer/docs/overview/tpc-differences) for more details.














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

Storage Transfer Service

](https://documentation.s3ns.fr/storage-transfer/docs/overview)












# Create transfers 
















This page shows you how to create and start transfer jobs.

To see if your source and destination (also known as a sink) are supported
by Storage Transfer Service, refer to
[Supported sources and sinks](/storage-transfer/docs/sources-and-sinks).

## Agents and agent pools

Depending on your source and destination, you may need to create and configure
an agent pool and install agents on a machine with access to your source or
destination.

- 

Transfers from Amazon S3, Microsoft Azure, URL lists, or Cloud Storage
to Cloud Storage **do not require agents and agent pools**.

- 

Transfers whose source and/or destination is a file system, or from
S3-compatible storage, do require agents and agent pools. See
[Manage agent pools](/storage-transfer/docs/on-prem-agent-pools) for
instructions.

## Before you begin

Before configuring your transfers, make sure you have configured access:

- For users and service accounts:

- [Agentless transfers](/storage-transfer/docs/iam-cloud)

- [Agent-based transfers](/storage-transfer/docs/file-system-permissions)

- [To your source data and to your destination](/storage-transfer/docs/sources-and-sinks).

If you're using `gcloud` commands,
[install the gcloud CLI](/sdk/docs/install).

## Create a transfer

Don't include sensitive information such as personally identifiable information
(PII) or security data in your transfer job name. Resource names may be
propagated to the names of other Google Cloud resources and may be exposed
to Google-internal systems outside of your project.



### Cloud de Confiance console

- 

Go to the **Storage Transfer Service** page in the Cloud de Confiance console.

[Go to Storage Transfer Service](https://console.cloud.s3nscloud.fr/transfer/) 

- 

Click **Create transfer job**. The **Create a transfer job** page is
displayed.

- 

Choose a source:



### Cloud Storage

Your user account must have **storage.buckets.get** permission to select
source and destination buckets. Alternatively, you can type the name of
the bucket directly. For more information, see
[Troubleshooting access](/iam/docs/troubleshooting-access).

- 

Under **Source type**, select **Cloud Storage**.

- 

Select your **Destination type**.

- 

If your destination is Cloud Storage, select your
**Scheduling mode**. *Batch transfers* execute on a
one-time or scheduled basis. *Event-driven transfers* continuously
monitor the source and transfer data when it's added or modified.

To configure an event-driven transfer, follow the instructions at
[Event-driven transfers](/storage-transfer/docs/event-driven-transfers).

- 

Click **Next step**.

- 

Select a bucket and (optionally) a folder in that bucket by doing
one of the following:

- 

Enter an existing Cloud Storage bucket name and path in
the **Bucket or folder** field without the prefix **`gs://`**.
For example, `my-test-bucket/path/to/files`.
To specify a
Cloud Storage bucket from another project, type the name
exactly into the **Bucket name** field.

- 

Select a list of existing buckets in your projects by clicking
**Browse**, then selecting a bucket.

When you click **Browse**, you can select buckets in other
projects by clicking the **Project ID**, then selecting
the new Project ID and bucket.

- 

To create a new bucket, click
**Create new bucket**.

If you specify a path within the folder, see
[Specifying source and destination paths](#source-destination-paths)
for important details.

- 

If this is an [event-driven transfer](/storage-transfer/docs/event-driven-transfers), enter the
Pub/Sub subscription name, which takes the following
format:


```
projects/ PROJECT_NAME /subscriptions/ SUBSCRIPTION_ID 
```


- Optionally, choose to
[filter objects by prefix](/storage-transfer/docs/filtering-objects-from-transfers),
by last modified date, or by
[storage class](/storage-transfer/docs/filtering-by-storage-class). If you specified a folder as your source location, prefix filters
are relative to that folder. For example, if your source is `my-test-bucket/path/`, an
include filter of `file` includes all files starting with
`my-test-bucket/path/file`.

- 

Click **Next step**.



### Amazon S3

See
[Transfer from Amazon S3 to Cloud Storage](/storage-transfer/docs/create-transfers/agentless/s3).


### S3-compatible storage

See
[Transfer from S3-compatible storage to Cloud Storage](/storage-transfer/docs/create-transfers/agent-based/s3-compatible).


### Microsoft Azure Blob Storage 

- 

Under **Source type**, select **Azure Blob Storage or Data Lake Storage Gen2**.

- 

Click **Next step**.

- 

Specify the following:

- 

**Storage account name** — the source Microsoft Azure Storage account
name.

The storage account name is displayed in the Microsoft Azure Storage
portal under **All services > Storage > Storage accounts**.

- 

**Container name** — the Microsoft Azure Storage container name.

The container name is displayed in the Microsoft Azure Storage portal
under **Storage explorer > Blob containers**. To transfer
all containers in a storage account, enter `*` as the value.
See
[Transfer all containers in an Azure Storage account](/storage-transfer/docs/create-transfers/agentless/azure-all-containers)
for more information.

- 

**Shared access signature (SAS)** — the Microsoft Azure Storage SAS
token created from a stored access policy. For more information,
see [Grant limited access to Azure Storage resources using
shared access signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview).

The default expiration time for SAS tokens is 8 hours. When you create
your SAS token, be sure to set a reasonable expiration time that enables you to
successfully complete your transfer.

- Optionally, choose to
[filter objects by prefix](/storage-transfer/docs/filtering-objects-from-transfers),
by last modified date, or by
[storage class](/storage-transfer/docs/filtering-by-storage-class). If you specified a folder as your source location, prefix filters
are relative to that folder. For example, if your source is `my-test-bucket/path/`, an
include filter of `file` includes all files starting with
`my-test-bucket/path/file`.

- 

Click **Next step**.



### File system

- 

Under **Source type**, select **POSIX file system**.

- 

Select your **Destination type** and click **Next step**.

- 

Select an existing agent pool, or select **Create agent pool** and
follow the instructions to create a new pool.

- 

Specify the fully qualified path of the file system directory.
If you specify a path other than root, see
[Specifying source and destination paths](#source-destination-paths)
for important details.

- 

Click **Next step**.



### HDFS

See
[Transfer from HDFS to Cloud Storage](/storage-transfer/docs/create-transfers/agent-based/hdfs).


### URL list

- 

Under **Source type**, select **URL list** and click **Next step**.

- 

Under **URL of TSV file**, provide the URL to a tab-separated values
(TSV) file. See [Creating a URL List](/storage-transfer/docs/create-url-list) for details
about how to create the TSV file.

- Optionally, choose to
[filter objects by prefix](/storage-transfer/docs/filtering-objects-from-transfers),
by last modified date, or by
[storage class](/storage-transfer/docs/filtering-by-storage-class). If you specified a folder as your source location, prefix filters
are relative to that folder. For example, if your source is `my-test-bucket/path/`, an
include filter of `file` includes all files starting with
`my-test-bucket/path/file`.

- 

Click **Next step**.




- 

Choose a destination:



### Cloud Storage​

- 

In the **Bucket or folder** field, enter the destination bucket
and (optionally) folder name, or click
**Browse** to select a bucket from a list of existing buckets in your
current project. To create a new bucket, click
**Create new bucket**.

If you specify a path within the bucket, see
[Specifying source and destination paths](#source-destination-paths)
for important details.

- 

Click **Next step**.

- 

Choose your scheduling options:

- 

From the **Run once** drop-down list, select one of the following:

- 

**Run once**: Runs a single transfer, starting at a time that you
select.

- 

**Run every day**: Runs a transfer daily, starting at a time that
you select.

You can enter an optional **End date**, or leave **End date**
blank to run the transfer continually.

- 

**Run every week**: Runs a transfer weekly, starting at a time
that you select.

- 

**Run with custom frequency**: Runs a transfer at a frequency that
you select. You can choose to repeat the transfer at a regular
interval of **Hours**, **Days**, or **Weeks**.

You can enter an optional **End date**, or leave **End date**
blank to run the transfer continually.

- 

From the **Starting now** drop-down list, select one of the following:

- 

**Starting now**: Starts the transfer after you click **Create**.

- 

**Starting on**: Starts the transfer on the date and time that you
select. Click **Calendar** to display a calendar to select the
start date.

- 

Click **Next step**.

- 

Choose settings for the transfer job. Some options are only
available for certain source/sink combinations.

- 

In the **Description** field, enter a description of the
transfer. As a best practice, enter a description that is meaningful and
unique so that you can tell jobs apart.

- 

Under **Metadata options**, choose to use the default options,
or click **View and select options** to specify values for all
supported metadata. See
[Metadata preservation](/storage-transfer/docs/metadata-preservation)
for details.

- 

Under **When to overwrite**, select one of the following:

- 

**If different**: Overwrites destination files if the source file
with the same name has different Etags or checksum values.

- 

**Always**: Always overwrites destination files when the source file
has the same name, even if they're identical.

- 

Under **When to delete**, select one of the following:

- 

**Never**: Never delete files from either the source or destination.

- 

**Delete file from source after they're transferred**: Delete files
from the source after they're transferred to the destination.
If a source file isn't transferred, for example because it
already exists in the destination, the source file is not
deleted.

- 

**Delete files from destination if they're not also at source**: If
files in the destination Cloud Storage bucket aren't also in
the source, then delete the files from the Cloud Storage
bucket.

This option ensures that the destination Cloud Storage bucket
exactly matches your source.

- 

For transfers between Cloud Storage buckets, choose
whether to
[transfer managed folders](/storage-transfer/docs/managed-folders).

- 

Enable or disable
[Logging for Storage Transfer Service](/storage-transfer/docs/transfer-logs).

- 

Under **Notification options**, optionally select your
Pub/Sub topic and which events to notify for. See
[Pub/Sub notifications](/storage-transfer/docs/pub-sub-transfer)
for more details.

- 

If you're
[delegating service agent permissions](/storage-transfer/docs/iam-cloud#umsa)
to a user-managed service account, select that option and enter
the service account email address in the format
` SERVICE_ACCOUNT_NAME @ PROJECT_ID .s3ns.iam.gserviceaccount.com`.

- 

Click **Create**.



### File system​

- 

Select an existing agent pool, or select **Create agent pool**
and follow the instructions to create a new pool.

- 

Specify the fully qualified destination directory path.
If you specify a path other than root, see
[Specifying source and destination paths](#source-destination-paths)
for important details. If the path you specify doesn't exist, the
transfer agent tries to create the directory structure on
the destination file system during the transfer process. The
agent must have the necessary write permissions in the parent
directory.

- 

Click **Next step**.

- 

Choose your scheduling options:

- 

From the **Run once** drop-down list, select one of the following:

- 

**Run once**: Runs a single transfer, starting at a time that you
select.

- 

**Run every day**: Runs a transfer daily, starting at a time that
you select.

You can enter an optional **End date**, or leave **End date**
blank to run the transfer continually.

- 

**Run every week**: Runs a transfer weekly, starting at a time
that you select.

- 

**Run with custom frequency**: Runs a transfer at a frequency that
you select. You can choose to repeat the transfer at a regular
interval of **Hours**, **Days**, or **Weeks**.

You can enter an optional **End date**, or leave **End date**
blank to run the transfer continually.

- 

From the **Starting now** drop-down list, select one of the following:

- 

**Starting now**: Starts the transfer after you click **Create**.

- 

**Starting on**: Starts the transfer on the date and time that you
select. Click **Calendar** to display a calendar to select the
start date.

- 

Click **Next step**.

- 

Specify whether to use a
[manifest file](/storage-transfer/docs/manifest).

- 

Select whether to preserve metadata; when to overwrite; and
when to delete files at the source or destination.

- 

Select your logging options.

- 

Under **Notification options**, optionally select your
Pub/Sub topic and which events to notify for. See
[Pub/Sub notifications](/storage-transfer/docs/pub-sub-transfer)
for more details.

- 

If you're
[delegating service agent permissions](/storage-transfer/docs/iam-cloud#umsa)
to a user-managed service account, select that option and enter
the service account email address in the format
` SERVICE_ACCOUNT_NAME @ PROJECT_ID .s3ns.iam.gserviceaccount.com`.

- 

To create your transfer job, click **Create**.






### gcloud CLI

To create a new transfer job, use the `gcloud transfer jobs create`
command. Creating a new job initiates the specified transfer, unless a
schedule or `--do-not-run` is specified.


```
gcloud transfer jobs create \ 
SOURCE DESTINATION 
```


Replace the following:

- 

SOURCE is the data source for this transfer. The format for each
source is:

- Cloud Storage: `gs:// BUCKET_NAME `.
To transfer from a specific folder, specify
`gs:// BUCKET_NAME / FOLDER_PATH /`,
including the trailing slash.

- Amazon S3: `s3:// BUCKET_NAME/FOLDER_PATH `

- S3-compatible storage: `s3:// BUCKET_NAME `. The
bucket name is relative to the endpoint. For example, if your data
resides at `https://us-east-1.example.com/folder1/bucket_a`, enter
`s3://folder1/bucket_a`.

- Microsoft Azure Storage:
`https://myaccount.blob.core.windows.net/ CONTAINER_NAME `

- URL list: `https:// PATH_TO_URL_LIST ` or
`http:// PATH_TO_URL_LIST `

- POSIX file system: `posix:// /PATH `. This must be
an absolute path from the root of the agent host machine.

- HDFS: `hdfs:// /PATH `

If you specify a path or folder value, see
[Specifying source and destination paths](#source-destination-paths)
for important details.

- 

DESTINATION is one of:

- Cloud Storage: `gs:// BUCKET_NAME `. To transfer
into a specific directory, specify
`gs:// BUCKET_NAME / FOLDER_PATH /`,
including the trailing slash.

- POSIX file system: `posix:// /PATH `. This must be
an absolute path from the root of the agent host machine.
If the path you specify doesn't exist, the
transfer agent tries to create the directory structure on
the destination file system during the transfer process. The
agent must have the necessary write permissions in the parent
directory.

If you specify a path or folder value, see
[Specifying source and destination paths](#source-destination-paths)
for important details.

If the transfer requires transfer agents, the following options are available:

- 

`--source-agent-pool` specifies the source agent pool to use for this
transfer. Required for transfers originating from a file system.

- 

`--destination-agent-pool` specifies the destination agent pool to use for
this transfer. Required for transfers to a file system.

- 

`--intermediate-storage-path` is the path to a Cloud Storage bucket, in
the form `gs://my-intermediary-bucket`. Required for transfers between two
file systems. See
[Create a Cloud Storage bucket as an intermediary](/storage-transfer/docs/file-to-file#create_a_bucket_as_an_intermediary)
for details on creating the intermediate bucket.

Additional options include:

- 

`--source-creds-file` specifies the relative path to a local file on your
machine that includes AWS or Azure credentials for the transfer source.
For credential file formatting information, see the
[TransferSpec](/storage-transfer/docs/reference/rest/v1/TransferSpec)
reference.

- 

`--do-not-run` prevents Storage Transfer Service from running the job
upon submission of the command. To run the job, [update](#update-job) it to
add a schedule, or use `jobs run` to [start it manually](#run-job).

- 

`--manifest-file` specifies the path to a CSV file in Cloud Storage
containing a list of files to transfer from your source. For manifest file
formatting, see
[Transfer specific files or objects using a manifest](/storage-transfer/docs/manifest).

- 

**Job information**: You can specify `--name`, `--description`,
and `--source-creds-file`. Note that `--name` is not supported for cross-bucket
replication jobs.

- 

**Schedule**: Specify `--schedule-starts`, `--schedule-repeats-every`, and
`--schedule-repeats-until`, or `--do-not-run`.

- 

**Object conditions**: Use conditions to determine which objects are
transferred. These include `--include-prefixes` and `--exclude-prefixes`,
and the time-based conditions in
`--include-modified-[before | after]-[absolute | relative]`. If you
specified a folder with your source, prefix filters are relative to that
folder. See [Filter source objects by prefix](/storage-transfer/docs/filtering-objects-from-transfers) for more
information.

Object conditions aren't supported for transfers involving file systems.

- 

**Transfer options**: Specify whether to overwrite destination
files (`--overwrite-when=different` or `always`) and whether to
delete certain files during or after the transfer
(`--delete-from=destination-if-unique` or `source-after-transfer`); specify
which [metadata values to preserve](/storage-transfer/docs/metadata-preservation) (`--preserve-metadata`); and
optionally set a storage class on transferred objects
(`--custom-storage-class`).

- 

**Notifications**: Configure
[Pub/Sub notifications for transfers](/storage-transfer/docs/pub-sub-transfer)
with `--notification-pubsub-topic`, `--notification-event-types`, and
`--notification-payload-format`.

- 

**Cloud Logging**: Enable Cloud Logging for agentless transfers, or
transfers from S3-compatible sources, with `--log-actions` and
`--log-action-states`. See
[Cloud Logging for Storage Transfer Service](/storage-transfer/docs/transfer-logs)
for details.

Transfers from S3-compatible sources also use the following options:

- `--source-endpoint` (required) specifies your storage system's endpoint.
For example, `s3.example.com`. Check with your provider for the
correct formatting. Do not specify the protocol (`http://` or `https://`).

- `--source-signing-region` specifies a region for signing requests.
Omit this flag if your storage provider doesn't require a signing region.

- `--source-auth-method` specifies the authentication method to use. Valid
values are `AWS_SIGNATURE_V2` or `AWS_SIGNATURE_V4`. Refer to
Amazon's [SigV4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) and [SigV2](https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html) documentation for more information.

- `--source-request-model` specifies the addressing style to use. Valid values
are `PATH_STYLE` or `VIRTUAL_HOSTED_STYLE`. Path style uses the format
`https://s3.example.com/ BUCKET_NAME / KEY_NAME `.
Virtual hosted style uses the format
`https:// BUCKET_NAME .s3.example.com/ KEY_NAME .

- `--source-network-protocol` specifies the network protocol that agents
should use for this job. Valid values are `HTTP` or `HTTPS`.

- `--source-list-api` specifies the version of the S3 listing API for
returning objects from the bucket. Valid values are `LIST_OBJECTS` or
`LIST_OBJECTS_V2`. Refer to Amazon's [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) and
[ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) documentation for more information.

To view all options, run `gcloud transfer jobs create --help` or refer to the
[`gcloud` reference documentation](/sdk/gcloud/reference/transfer/jobs/create).

### Examples

#### Amazon S3 to Cloud Storage

See [Transfer from Amazon S3 to Cloud Storage](/storage-transfer/docs/create-transfers/agentless/s3).

#### S3-compatible storage to Cloud Storage

See [Transfer from S3-compatible storage to Cloud Storage](/storage-transfer/docs/create-transfers/agent-based/s3-compatible).

#### File system to Cloud Storage

See [Transfer from a file system to Cloud Storage](/storage-transfer/docs/create-transfers/agent-based/file-system-to-cloud-storage).

#### Cloud Storage to file system

To transfer from a Cloud Storage bucket to a file system, specify the
following.


```
gcloud transfer jobs create \ 
gs://my-storage-bucket posix:///tmp/destination \ 
--destination-agent-pool = my-destination-agent-pool
```


#### File system to file system

To transfer between two file systems, you must specify a source agent pool,
a destination agent pool, and an intermediate Cloud Storage bucket through
which the data passes.

See
[Create a Cloud Storage bucket as an intermediary](/storage-transfer/docs/file-to-file#create_a_bucket_as_an_intermediary)
for details on the intermediate bucket.

Then, specify these 3 resources when calling `transfer jobs create`:


```
gcloud transfer jobs create \ 
posix:///tmp/source/on/systemA posix:///tmp/destination/on/systemB \ 
--source-agent-pool = source_agent_pool \ 
--destination-agent-pool = destination_agent_pool \ 
--intermediate-storage-path = gs://my-intermediary-bucket
```


### REST

The following samples show you how to use Storage Transfer Service through the REST
API.

When you configure or edit transfer jobs using the
Storage Transfer Service API, the time must be in UTC. For more information on
specifying the schedule of a transfer job, see
[Schedule](/storage-transfer/docs/reference/rest/v1/transferJobs#Schedule).

## Transfer between Cloud Storage buckets

In this example, you'll learn how to move files from one Cloud Storage
bucket to another. For example, you can move data to a bucket in another
[location](/storage/docs/bucket-locations).

Request using
[transferJobs create](/storage-transfer/docs/reference/rest/v1/transferJobs/create):


```
POST h tt ps : //storagetransfer.googleapis.com/v1/transferJobs 
{ 
"description" : "YOUR DESCRIPTION" , 
"status" : "ENABLED" , 
"projectId" : "PROJECT_ID" , 
"schedule" : { 
"scheduleStartDate" : { 
"day" : 1 , 
"month" : 1 , 
"year" : 2015 
}, 
"startTimeOfDay" : { 
"hours" : 1 , 
"minutes" : 1 
} 
}, 
"transferSpec" : { 
"gcsDataSource" : { 
"bucketName" : "GCS_SOURCE_NAME" 
}, 
"gcsDataSink" : { 
"bucketName" : "GCS_SINK_NAME" 
}, 
"transferOptions" : { 
"deleteObjectsFromSourceAfterTransfer" : true 
} 
} 
} 
```

Response:

```
200 OK 
{ 
"transferJob" : [ 
{ 
"creationTime" : "2015-01-01T01:01:00.000000000Z" , 
"description" : "YOUR DESCRIPTION" , 
"name" : "transferJobs/JOB_ID" , 
"status" : "ENABLED" , 
"lastModificationTime" : "2015-01-01T01:01:00.000000000Z" , 
"projectId" : "PROJECT_ID" , 
"schedule" : { 
"scheduleStartDate" : { 
"day" : 1 , 
"month" : 1 , 
"year" : 2015 
}, 
"startTimeOfDay" : { 
"hours" : 1 , 
"minutes" : 1 
} 
}, 
"transferSpec" : { 
"gcsDataSource" : { 
"bucketName" : "GCS_SOURCE_NAME" , 
}, 
"gcsDataSink" : { 
"bucketName" : "GCS_NEARLINE_SINK_NAME" 
}, 
"objectConditions" : { 
"minTimeElapsedSinceLastModification" : "2592000.000s" 
}, 
"transferOptions" : { 
"deleteObjectsFromSourceAfterTransfer" : true 
} 
} 
} 
] 
} 
```


## Transfer from Amazon S3 to Cloud Storage

See [Transfer from Amazon S3 to Cloud Storage](/storage-transfer/docs/create-transfers/agentless/s3).

## Transfer between Microsoft Azure Blob Storage and Cloud Storage

In this example, you'll learn how to move files from Microsoft Azure Storage to a
Cloud Storage bucket, using a Microsoft Azure Storage shared access
signature (SAS) token.

For more information on Microsoft Azure Storage SAS, see
[Grant limited access to Azure Storage resources using shared access signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview).

Before starting, review
[Configure access to Microsoft Azure Storage](/storage-transfer/docs/source-microsoft-azure)
and [Pricing](https://documentation.s3ns.fr/storage-transfer/pricing) to understand the implications of
moving data from Microsoft Azure Storage to Cloud Storage.

Request using [transferJobs create](/storage-transfer/docs/reference/rest/v1/transferJobs/create):

```
POST h tt ps : //storagetransfer.googleapis.com/v1/transferJobs 
{ 
"description" : "YOUR DESCRIPTION" , 
"status" : "ENABLED" , 
"projectId" : "PROJECT_ID" , 
"schedule" : { 
"scheduleStartDate" : { 
"day" : 14 , 
"month" : 2 , 
"year" : 2020 
}, 
"scheduleEndDate" : { 
"day" : 14 
"month" : 2 , 
"year" : 2020 
}, 
"startTimeOfDay" : { 
"hours" : 1 , 
"minutes" : 1 
} 
}, 
"transferSpec" : { 
"azureBlobStorageDataSource" : { 
"storageAccount" : "AZURE_SOURCE_NAME" , 
"azureCredentials" : { 
"sasToken" : "AZURE_SAS_TOKEN" , 
}, 
"container" : "AZURE_CONTAINER" , 
}, 
"gcsDataSink" : { 
"bucketName" : "GCS_SINK_NAME" 
} 
} 
} 
```

Response:

```
200 OK 
{ 
"transferJob" : [ 
{ 
"creationTime" : "2020-02-14T01:01:00.000000000Z" , 
"description" : "YOUR DESCRIPTION" , 
"name" : "transferJobs/JOB_ID" , 
"status" : "ENABLED" , 
"lastModificationTime" : "2020-02-14T01:01:00.000000000Z" , 
"projectId" : "PROJECT_ID" , 
"schedule" : { 
"scheduleStartDate" : { 
"day" : 14 
"month" : 2 , 
"year" : 2020 
}, 
"scheduleEndDate" : { 
"day" : 14 , 
"month" : 2 , 
"year" : 2020 
}, 
"startTimeOfDay" : { 
"hours" : 1 , 
"minutes" : 1 
} 
}, 
"transferSpec" : { 
"azureBlobStorageDataSource" : { 
"storageAccount" : "AZURE_SOURCE_NAME" , 
"azureCredentials" : { 
"sasToken" : "AZURE_SAS_TOKEN" , 
}, 
"container" : "AZURE_CONTAINER" , 
}, 
"objectConditions" : {}, 
"transferOptions" : {} 
} 
} 
] 
} 
```


## Transfer from a file system

See [Transfer from a file system to Cloud Storage](/storage-transfer/docs/create-transfers/agent-based/file-system-to-cloud-storage).


### Client libraries

The following samples show you how to use Storage Transfer Service programmatically
with Go, Java, Node.js, and Python.

When you configure or edit transfer jobs programmatically, the time must be
in UTC. For more information on
specifying the schedule of a transfer job, see
[Schedule](/storage-transfer/docs/reference/rest/v1/transferJobs#Schedule).

For more information about the Storage Transfer Service client libraries, see
[Getting started with Storage Transfer Service client libraries](/storage-transfer/docs/libraries).

## Transfer between Cloud Storage buckets

In this example, you'll learn how to move files from one Cloud Storage
bucket to another. For example, you can move data to a bucket in another
[location](/storage/docs/bucket-locations).




### Go

























```
import ( 
"context" 
"fmt" 
"io" 
"time" 

"google.golang.org/genproto/googleapis/type/date" 
"google.golang.org/genproto/googleapis/type/timeofday" 
"google.golang.org/protobuf/types/known/durationpb" 

storagetransfer "cloud.google.com/go/storagetransfer/apiv1" 
"cloud.google.com/go/storagetransfer/apiv1/storagetransferpb" 
) 

func transferToNearline ( w io . Writer , projectID string , gcsSourceBucket string , gcsNearlineSinkBucket string ) ( * storagetransferpb . TransferJob , error ) { 
// Your Google Cloud Project ID 
// projectID := "my-project-id" 

// The name of the GCS bucket to transfer objects from 
// gcsSourceBucket := "my-source-bucket" 

// The name of the Nearline GCS bucket to transfer objects to 
// gcsNearlineSinkBucket := "my-sink-bucket" 

ctx := context . Background () 
client , err := storagetransfer . [ NewClient ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "storagetransfer.NewClient: %w" , err ) 
} 
defer client . [ Close ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close) () 

// A description of this job 
jobDescription := "Transfers objects that haven't been modified in 30 days to a Nearline bucket" 

// The time to start the transfer 
startTime := time . Now (). UTC () 

req := & storagetransferpb . CreateTransferJobRequest { 
TransferJob : & storagetransferpb . TransferJob { 
ProjectId : projectID , 
Description : jobDescription , 
TransferSpec : & storagetransferpb . TransferSpec { 
DataSink : & storagetransferpb . TransferSpec_GcsDataSink { 
GcsDataSink : & storagetransferpb . GcsData { BucketName : gcsNearlineSinkBucket }}, 
DataSource : & storagetransferpb . TransferSpec_GcsDataSource { 
GcsDataSource : & storagetransferpb . GcsData { BucketName : gcsSourceBucket }, 
}, 
ObjectConditions : & storagetransferpb . ObjectConditions { 
MinTimeElapsedSinceLastModification : & durationpb . Duration { Seconds : 2592000 /*30 days */ }, 
}, 
TransferOptions : & storagetransferpb . TransferOptions { DeleteObjectsFromSourceAfterTransfer : true }, 
}, 
Schedule : & storagetransferpb . Schedule { 
ScheduleStartDate : & date . Date { 
Year : int32 ( startTime . Year ()), 
Month : int32 ( startTime . Month ()), 
Day : int32 ( startTime . Day ()), 
}, 
ScheduleEndDate : & date . Date { 
Year : int32 ( startTime . Year ()), 
Month : int32 ( startTime . Month ()), 
Day : int32 ( startTime . Day ()), 
}, 
StartTimeOfDay : & timeofday . TimeOfDay { 
Hours : int32 ( startTime . Hour ()), 
Minutes : int32 ( startTime . Minute ()), 
Seconds : int32 ( startTime . Second ()), 
}, 
}, 
Status : storagetransferpb . [ TransferJob_ENABLED ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb.html#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_TransferJob_STATUS_UNSPECIFIED_TransferJob_ENABLED_TransferJob_DISABLED_TransferJob_DELETED) , 
}, 
} 
resp , err := client . CreateTransferJob ( ctx , req ) 
if err != nil { 
return nil , fmt . Errorf ( "failed to create transfer job: %w" , err ) 
} 
if _ , err = client . RunTransferJob ( ctx , & storagetransferpb . RunTransferJobRequest { 
ProjectId : projectID , 
JobName : resp . [ Name ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Name) , 
}); err != nil { 
return nil , fmt . Errorf ( "failed to run transfer job: %w" , err ) 
} 
fmt . Fprintf ( w , "Created and ran transfer job from %v to %v with name %v" , gcsSourceBucket , gcsNearlineSinkBucket , resp . [ Name ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Name) ) 
return resp , nil 
} 
```






### Java



Looking for older samples? See the [Storage Transfer Service Migration Guide](/storage-transfer/docs/reference/migration-guide).























```
import com.google.protobuf.[Duration](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) ; 
import com.google.storagetransfer.v1.proto.[StorageTransferServiceClient](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) ; 
import com.google.storagetransfer.v1.proto.[TransferProto](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html).[CreateTransferJobRequest](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.CreateTransferJobRequest.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[GcsData](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[ObjectConditions](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.ObjectConditions.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[Schedule](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.Schedule.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).Status ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferOptions](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferOptions.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferSpec](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html) ; 
import com.google.type.[Date](https://documentation.s3ns.fr/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html) ; 
import com.google.type.[TimeOfDay](https://documentation.s3ns.fr/java/docs/reference/proto-google-common-protos/latest/com.google.type.TimeOfDay.html) ; 
import java.io.IOException ; 
import java.util.Calendar ; 

public class TransferToNearline { 
/** 
* Creates a one-off transfer job that transfers objects in a standard GCS bucket that are more 
* than 30 days old to a Nearline GCS bucket. 
*/ 
public static void transferToNearline ( 
String projectId , 
String jobDescription , 
String gcsSourceBucket , 
String gcsNearlineSinkBucket , 
long startDateTime ) 
throws IOException { 

// Your Google Cloud Project ID 
// String projectId = "your-project-id"; 

// A short description of this job 
// String jobDescription = "Sample transfer job of old objects to a Nearline GCS bucket."; 

// The name of the source GCS bucket to transfer data from 
// String gcsSourceBucket = "your-gcs-source-bucket"; 

// The name of the Nearline GCS bucket to transfer old objects to 
// String gcsSinkBucket = "your-nearline-gcs-bucket"; 

// What day and time in UTC to start the transfer, expressed as an epoch date timestamp. 
// If this is in the past relative to when the job is created, it will run the next day. 
// long startDateTime = 
// new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse("2000-01-01 00:00:00").getTime(); 

// Parse epoch timestamp into the model classes 
Calendar startCalendar = Calendar . getInstance (); 
startCalendar . setTimeInMillis ( startDateTime ); 
// Note that this is a Date from the model class package, not a java.util.Date 
[ Date ](https://documentation.s3ns.fr/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html) date = 
[ Date ](https://documentation.s3ns.fr/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html) . newBuilder () 
. setYear ( startCalendar . get ( Calendar . YEAR )) 
. setMonth ( startCalendar . get ( Calendar . MONTH ) + 1 ) 
. setDay ( startCalendar . get ( Calendar . DAY_OF_MONTH )) 
. build (); 
[ TimeOfDay ](https://documentation.s3ns.fr/java/docs/reference/proto-google-common-protos/latest/com.google.type.TimeOfDay.html) time = 
[ TimeOfDay ](https://documentation.s3ns.fr/java/docs/reference/proto-google-common-protos/latest/com.google.type.TimeOfDay.html) . newBuilder () 
. setHours ( startCalendar . get ( Calendar . HOUR_OF_DAY )) 
. setMinutes ( startCalendar . get ( Calendar . MINUTE )) 
. setSeconds ( startCalendar . get ( Calendar . SECOND )) 
. build (); 

[ TransferJob ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob = 
[ TransferJob ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) . newBuilder () 
. setDescription ( jobDescription ) 
. setProjectId ( projectId ) 
. setTransferSpec ( 
[ TransferSpec ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html) . newBuilder () 
. setGcsDataSource ( [ GcsData ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html) . newBuilder (). setBucketName ( gcsSourceBucket )) 
. setGcsDataSink ( [ GcsData ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html) . newBuilder (). setBucketName ( gcsNearlineSinkBucket )) 
. setObjectConditions ( 
[ ObjectConditions ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.ObjectConditions.html) . newBuilder () 
. [ setMinTimeElapsedSinceLastModification ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.ObjectConditions.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_ObjectConditions_Builder_setMinTimeElapsedSinceLastModification_com_google_protobuf_Duration_) ( 
[ Duration ](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) . newBuilder (). setSeconds ( 2592000 /* 30 days */ ))) 
. setTransferOptions ( 
[ TransferOptions ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferOptions.html) . newBuilder (). [ setDeleteObjectsFromSourceAfterTransfer ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferOptions.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferOptions_Builder_setDeleteObjectsFromSourceAfterTransfer_boolean_) ( true ))) 
. [ setSchedule ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferJob_Builder_setSchedule_com_google_storagetransfer_v1_proto_TransferTypes_Schedule_) ( [ Schedule ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.Schedule.html) . newBuilder (). [ setScheduleStartDate ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.Schedule.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_Schedule_Builder_setScheduleStartDate_com_google_type_Date_) ( date ). [ setStartTimeOfDay ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.Schedule.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_Schedule_Builder_setStartTimeOfDay_com_google_type_TimeOfDay_) ( time )) 
. setStatus ( Status . ENABLED ) 
. build (); 

// Create a Transfer Service client 
[ StorageTransferServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) storageTransfer = [ StorageTransferServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) . create (); 

// Create the transfer job 
[ TransferJob ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) response = 
storageTransfer . [ createTransferJob ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html#com_google_storagetransfer_v1_proto_StorageTransferServiceClient_createTransferJob_com_google_storagetransfer_v1_proto_TransferProto_CreateTransferJobRequest_) ( 
CreateTransferJobRequest . newBuilder (). setTransferJob ( transferJob ). build ()); 

System . out . println ( "Created transfer job from standard bucket to Nearline bucket:" ); 
System . out . println ( response . toString ()); 
} 
} 
```






### Node.js

























```
// Imports the Google Cloud client library 
const { 
StorageTransferServiceClient , 
} = require ( '[@google-cloud/storage-transfer](https://documentation.s3ns.fr/nodejs/docs/reference/storage-transfer/latest/overview.html)' ); 

/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// The ID of the Google Cloud Platform Project that owns the job 
// projectId = 'my-project-id' 

// A useful description for your transfer job 
// description = 'My transfer job' 

// Google Cloud Storage source bucket name 
// gcsSourceBucket = 'my-gcs-source-bucket' 

// Google Cloud Storage destination bucket name 
// gcsSinkBucket = 'my-gcs-destination-bucket' 

// Date to start daily migration 
// startDate = new Date() 

// Creates a client 
const client = new [ StorageTransferServiceClient ](https://documentation.s3ns.fr/nodejs/docs/reference/storage-transfer/latest/overview.html) (); 

/** 
* Create a daily migration from a GCS bucket to another GCS bucket for 
* objects untouched for 30+ days. 
*/ 
async function createDailyNearline30DayMigration () { 
// Runs the request and creates the job 
const [ transferJob ] = await client . createTransferJob ({ 
transferJob : { 
projectId , 
description , 
status : '[ENABLED](https://documentation.s3ns.fr/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.transferjob.status.html)' , 
schedule : { 
scheduleStartDate : { 
day : startDate . getDate (), 
month : startDate . getMonth () + 1 , 
year : startDate . getFullYear (), 
}, 
}, 
transferSpec : { 
gcsDataSource : { 
bucketName : gcsSourceBucket , 
}, 
gcsDataSink : { 
bucketName : gcsSinkBucket , 
}, 
objectConditions : { 
minTimeElapsedSinceLastModification : { 
seconds : 2592000 , // 30 days 
}, 
}, 
transferOptions : { 
deleteObjectsFromSourceAfterTransfer : true , 
}, 
}, 
}, 
}); 

console . log ( `Created transferJob: ${ transferJob . name } ` ); 
} 

createDailyNearline30DayMigration (); 
```






### Python



Looking for older samples? See the [Storage Transfer Service Migration Guide](/storage-transfer/docs/reference/migration-guide).























```
from datetime import datetime 

from google.cloud import storage_transfer 
from google.protobuf.duration_pb2 import Duration 

def create_daily_nearline_30_day_migration ( 
project_id : str , 
description : str , 
source_bucket : str , 
sink_bucket : str , 
start_date : datetime , 
): 
"""Create a daily migration from a GCS bucket to a Nearline GCS bucket 
for objects untouched for 30 days.""" 

client = storage_transfer . [ StorageTransferServiceClient ](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html) () 

# The ID of the Google Cloud Platform Project that owns the job 
# project_id = 'my-project-id' 

# A useful description for your transfer job 
# description = 'My transfer job' 

# Google Cloud Storage source bucket name 
# source_bucket = 'my-gcs-source-bucket' 

# Google Cloud Storage destination bucket name 
# sink_bucket = 'my-gcs-destination-bucket' 

transfer_job_request = storage_transfer . [ CreateTransferJobRequest ](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html) ( 
{ 
"transfer_job" : { 
"project_id" : project_id , 
"description" : description , 
"status" : storage_transfer . [ TransferJob ](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html) . Status . ENABLED , 
"schedule" : { 
"schedule_start_date" : { 
"day" : start_date . day , 
"month" : start_date . month , 
"year" : start_date . year , 
} 
}, 
"transfer_spec" : { 
"gcs_data_source" : { 
"bucket_name" : source_bucket , 
}, 
"gcs_data_sink" : { 
"bucket_name" : sink_bucket , 
}, 
"object_conditions" : { 
"min_time_elapsed_since_last_modification" : Duration ( 
seconds = 2592000 # 30 days 
) 
}, 
"transfer_options" : { 
"delete_objects_from_source_after_transfer" : True 
}, 
}, 
} 
} 
) 

result = client . [ create_transfer_job ](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job) ( transfer_job_request ) 
print ( f "Created transferJob: { result . name } " ) 
```






## Transfer from Amazon S3 to Cloud Storage

See [Transfer from Amazon S3 to Cloud Storage](/storage-transfer/docs/create-transfers/agentless/s3).

## Transfer between Microsoft Azure Blob Storage and Cloud Storage

In this example, you'll learn how to move files from Microsoft Azure Storage to a
Cloud Storage bucket, using a Microsoft Azure Storage shared access
signature (SAS) token.

For more information on Microsoft Azure Storage SAS, see
[Grant limited access to Azure Storage resources using shared access signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview).

Before starting, review
[Configure access to Microsoft Azure Storage](/storage-transfer/docs/source-microsoft-azure)
and [Pricing](https://documentation.s3ns.fr/storage-transfer/pricing) to understand the implications of
moving data from Microsoft Azure Storage to Cloud Storage.



























### Go 








To learn how to install and use the client library for Storage Transfer Service, see
[Storage Transfer Service client libraries](/storage-transfer/docs/reference/libraries).



For more information, see the
[Storage Transfer Service Go API
reference documentation](https://pkg.go.dev/cloud.google.com/go/storagetransfer@v1.0.0/apiv1).





To authenticate to Storage Transfer Service, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.


























```
import ( 
"context" 
"fmt" 
"io" 
"os" 

storagetransfer "cloud.google.com/go/storagetransfer/apiv1" 
"cloud.google.com/go/storagetransfer/apiv1/storagetransferpb" 
) 

func transferFromAzure ( w io . Writer , projectID string , azureStorageAccountName string , azureSourceContainer string , gcsSinkBucket string ) ( * storagetransferpb . TransferJob , error ) { 
// Your Google Cloud Project ID. 
// projectID := "my-project-id" 

// The name of your Azure Storage account. 
// azureStorageAccountName := "my-azure-storage-acc" 

// The name of the Azure container to transfer objects from. 
// azureSourceContainer := "my-source-container" 

// The name of the GCS bucket to transfer objects to. 
// gcsSinkBucket := "my-sink-bucket" 

ctx := context . Background () 
client , err := storagetransfer . [ NewClient ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "storagetransfer.NewClient: %w" , err ) 
} 
defer client . [ Close ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close) () 

// The Azure SAS token, should be accessed via environment variable for security 
azureSasToken := os . Getenv ( "AZURE_SAS_TOKEN" ) 

req := & storagetransferpb . CreateTransferJobRequest { 
TransferJob : & storagetransferpb . TransferJob { 
ProjectId : projectID , 
TransferSpec : & storagetransferpb . TransferSpec { 
DataSource : & storagetransferpb . TransferSpec_AzureBlobStorageDataSource { 
AzureBlobStorageDataSource : & storagetransferpb . AzureBlobStorageData { 
StorageAccount : azureStorageAccountName , 
AzureCredentials : & storagetransferpb . AzureCredentials { 
SasToken : azureSasToken , 
}, 
Container : azureSourceContainer , 
}, 
}, 
DataSink : & storagetransferpb . TransferSpec_GcsDataSink { 
GcsDataSink : & storagetransferpb . GcsData { BucketName : gcsSinkBucket }}, 
}, 
Status : storagetransferpb . [ TransferJob_ENABLED ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb.html#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_TransferJob_STATUS_UNSPECIFIED_TransferJob_ENABLED_TransferJob_DISABLED_TransferJob_DELETED) , 
}, 
} 
resp , err := client . CreateTransferJob ( ctx , req ) 
if err != nil { 
return nil , fmt . Errorf ( "failed to create transfer job: %w" , err ) 
} 
if _ , err = client . RunTransferJob ( ctx , & storagetransferpb . RunTransferJobRequest { 
ProjectId : projectID , 
JobName : resp . [ Name ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Name) , 
}); err != nil { 
return nil , fmt . Errorf ( "failed to run transfer job: %w" , err ) 
} 
fmt . Fprintf ( w , "Created and ran transfer job from %v to %v with name %v" , azureSourceContainer , gcsSinkBucket , resp . [ Name ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Name) ) 
return resp , nil 
} 
```











































### Java 








To learn how to install and use the client library for Storage Transfer Service, see
[Storage Transfer Service client libraries](/storage-transfer/docs/reference/libraries).



For more information, see the
[Storage Transfer Service Java API
reference documentation](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto).





To authenticate to Storage Transfer Service, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.


























```
import com.google.storagetransfer.v1.proto.[StorageTransferServiceClient](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) ; 
import com.google.storagetransfer.v1.proto.[TransferProto](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html) ; 
import com.google.storagetransfer.v1.proto.[TransferProto](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html).[RunTransferJobRequest](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.RunTransferJobRequest.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[AzureBlobStorageData](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AzureBlobStorageData.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[AzureCredentials](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AzureCredentials.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[GcsData](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferJob](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html).Status ; 
import com.google.storagetransfer.v1.proto.[TransferTypes](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.html).[TransferSpec](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html) ; 
import java.io.IOException ; 
import java.util.concurrent.ExecutionException ; 

public class TransferFromAzure { 
public static void main ( String [] args ) 
throws IOException , ExecutionException , InterruptedException { 
// TODO(developer): Replace these variables before running the sample. 
// Your Google Cloud Project ID 
String projectId = "my-project-id" ; 

// Your Azure Storage Account name 
String azureStorageAccount = "my-azure-account" ; 

// The Azure source container to transfer data from 
String azureSourceContainer = "my-source-container" ; 

// The GCS bucket to transfer data to 
String gcsSinkBucket = "my-sink-bucket" ; 

transferFromAzureBlobStorage ( 
projectId , azureStorageAccount , azureSourceContainer , gcsSinkBucket ); 
} 

/** 
* Creates and runs a transfer job to transfer all data from an Azure container to a GCS bucket. 
*/ 
public static void transferFromAzureBlobStorage ( 
String projectId , 
String azureStorageAccount , 
String azureSourceContainer , 
String gcsSinkBucket ) 
throws IOException , ExecutionException , InterruptedException { 

// Your Azure SAS token, should be accessed via environment variable 
String azureSasToken = System . getenv ( "AZURE_SAS_TOKEN" ); 

[ TransferSpec ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html) transferSpec = 
[ TransferSpec ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.html) . newBuilder () 
. [ setAzureBlobStorageDataSource ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferSpec.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_TransferSpec_Builder_setAzureBlobStorageDataSource_com_google_storagetransfer_v1_proto_TransferTypes_AzureBlobStorageData_) ( 
[ AzureBlobStorageData ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AzureBlobStorageData.html) . newBuilder () 
. [ setAzureCredentials ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AzureBlobStorageData.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AzureBlobStorageData_Builder_setAzureCredentials_com_google_storagetransfer_v1_proto_TransferTypes_AzureCredentials_) ( 
[ AzureCredentials ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AzureCredentials.html) . newBuilder (). [ setSasToken ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AzureCredentials.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AzureCredentials_Builder_setSasToken_java_lang_String_) ( azureSasToken ). build ()) 
. [ setContainer ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AzureBlobStorageData.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AzureBlobStorageData_Builder_setContainer_java_lang_String_) ( azureSourceContainer ) 
. [ setStorageAccount ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AzureBlobStorageData.Builder.html#com_google_storagetransfer_v1_proto_TransferTypes_AzureBlobStorageData_Builder_setStorageAccount_java_lang_String_) ( azureStorageAccount )) 
. setGcsDataSink ( [ GcsData ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GcsData.html) . newBuilder (). setBucketName ( gcsSinkBucket ). build ()) 
. build (); 

[ TransferJob ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) transferJob = 
[ TransferJob ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) . newBuilder () 
. setProjectId ( projectId ) 
. setStatus ( Status . ENABLED ) 
. setTransferSpec ( transferSpec ) 
. build (); 

// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the "close" method on the client to safely clean up any remaining background resources, 
// or use "try-with-close" statement to do this automatically. 
try ( [ StorageTransferServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) storageTransfer = [ StorageTransferServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html) . create ()) { 
// Create the transfer job 
[ TransferJob ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob.html) response = 
storageTransfer . createTransferJob ( 
[ TransferProto ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.html) . CreateTransferJobRequest . newBuilder () 
. setTransferJob ( transferJob ) 
. build ()); 

// Run the created job 
storageTransfer 
. [ runTransferJobAsync ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceClient.html#com_google_storagetransfer_v1_proto_StorageTransferServiceClient_runTransferJobAsync_com_google_storagetransfer_v1_proto_TransferProto_RunTransferJobRequest_) ( 
[ RunTransferJobRequest ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.RunTransferJobRequest.html) . newBuilder () 
. setProjectId ( projectId ) 
. setJobName ( response . getName ()) 
. build ()) 
. get (); 

System . out . println ( 
"Created and ran a transfer job from " 
+ azureSourceContainer 
+ " to " 
+ gcsSinkBucket 
+ " with " 
+ "name " 
+ response . getName ()); 
} 
} 
} 
```











































### Node.js 








To learn how to install and use the client library for Storage Transfer Service, see
[Storage Transfer Service client libraries](/storage-transfer/docs/reference/libraries).



For more information, see the
[Storage Transfer Service Node.js API
reference documentation](https://googleapis.dev/nodejs/storagetransfer/latest/index.html).





To authenticate to Storage Transfer Service, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.


























```
// Imports the Google Cloud client library 
const { 
StorageTransferServiceClient , 
} = require ( '[@google-cloud/storage-transfer](https://documentation.s3ns.fr/nodejs/docs/reference/storage-transfer/latest/overview.html)' ); 

/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// The ID of the Google Cloud Platform Project that owns the job 
// projectId = 'my-project-id' 

// A useful description for your transfer job 
// description = 'My transfer job' 

// Azure Storage Account name 
// azureStorageAccount = 'accountname' 

// Azure Storage Account name 
// azureSourceContainer = 'my-azure-source-bucket' 

// Azure Shared Access Signature token 
// azureSASToken = '?sv=...' 

// Google Cloud Storage destination bucket name 
// gcsSinkBucket = 'my-gcs-destination-bucket' 

// Creates a client 
const client = new [ StorageTransferServiceClient ](https://documentation.s3ns.fr/nodejs/docs/reference/storage-transfer/latest/overview.html) (); 

/** 
* Creates a one-time transfer job from Azure Blob Storage to Google Cloud Storage. 
*/ 
async function transferFromBlobStorage () { 
// Setting the start date and the end date as the same time creates a 
// one-time transfer 
const now = new [ Date ](https://documentation.s3ns.fr/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.type.date.html) (); 
const oneTimeSchedule = { 
day : now . getDate (), 
month : now . getMonth () + 1 , 
year : now . getFullYear (), 
}; 

// Runs the request and creates the job 
const [ transferJob ] = await client . createTransferJob ({ 
transferJob : { 
projectId , 
description , 
status : '[ENABLED](https://documentation.s3ns.fr/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.transferjob.status.html)' , 
schedule : { 
scheduleStartDate : oneTimeSchedule , 
scheduleEndDate : oneTimeSchedule , 
}, 
transferSpec : { 
azureBlobStorageDataSource : { 
azureCredentials : { 
sasToken : azureSASToken , 
}, 
container : azureSourceContainer , 
storageAccount : azureStorageAccount , 
}, 
gcsDataSink : { 
bucketName : gcsSinkBucket , 
}, 
}, 
}, 
}); 

console . log ( 
`Created and ran a transfer job from ' ${ azureSourceContainer } ' to ' ${ gcsSinkBucket } ' with name ${ transferJob . name } ` 
); 
} 

transferFromBlobStorage (); 
```











































### Python 








To learn how to install and use the client library for Storage Transfer Service, see
[Storage Transfer Service client libraries](/storage-transfer/docs/reference/libraries).



For more information, see the
[Storage Transfer Service Python API
reference documentation](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest).





To authenticate to Storage Transfer Service, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.


























```
from datetime import datetime 

from google.cloud import storage_transfer 

def create_one_time_azure_transfer ( 
project_id : str , 
description : str , 
azure_storage_account : str , 
azure_sas_token : str , 
source_container : str , 
sink_bucket : str , 
): 
"""Creates a one-time transfer job from Azure Blob Storage to Google Cloud 
Storage.""" 

# Initialize client that will be used to create storage transfer requests. 
# This client only needs to be created once, and can be reused for 
# multiple requests. 
client = storage_transfer . [ StorageTransferServiceClient ](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html) () 

# The ID of the Google Cloud Platform Project that owns the job 
# project_id = 'my-project-id' 

# A useful description for your transfer job 
# description = 'My transfer job' 

# Azure Storage Account name 
# azure_storage_account = 'accountname' 

# Azure Shared Access Signature token 
# azure_sas_token = '?sv=...' 

# Azure Blob source container name 
# source_container = 'my-azure-source-bucket' 

# Google Cloud Storage destination bucket name 
# sink_bucket = 'my-gcs-destination-bucket' 

now = datetime . utcnow () 
# Setting the start date and the end date as 
# the same time creates a one-time transfer 
one_time_schedule = { "day" : now . day , "month" : now . month , "year" : now . year } 

transfer_job_request = storage_transfer . [ CreateTransferJobRequest ](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html) ( 
{ 
"transfer_job" : { 
"project_id" : project_id , 
"description" : description , 
"status" : storage_transfer . [ TransferJob ](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html) . Status . ENABLED , 
"schedule" : { 
"schedule_start_date" : one_time_schedule , 
"schedule_end_date" : one_time_schedule , 
}, 
"transfer_spec" : { 
"azure_blob_storage_data_source" : { 
"storage_account" : azure_storage_account , 
"azure_credentials" : { "sas_token" : azure_sas_token }, 
"container" : source_container , 
}, 
"gcs_data_sink" : { 
"bucket_name" : sink_bucket , 
}, 
}, 
} 
} 
) 

result = client . [ create_transfer_job ](https://documentation.s3ns.fr/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job) ( transfer_job_request ) 
print ( f "Created transferJob: { result . name } " ) 
```




















## Transfer from a file system

See [Transfer from a file system to Cloud Storage](/storage-transfer/docs/create-transfers/agent-based/file-system-to-cloud-storage).



## Specifying source and destination paths

Source and destination paths allow you to transfer data located under a
specific prefix and control where that data is placed in the destination.

- **Source path**: Acts as the root directory for the transfer. Only objects
under this path are transferred, and the source path is stripped from the
start of the object names before they are copied to the destination.

- **Destination path**: Acts as a prefix that is prepended to all object names
at the destination. For file system transfers, specifies the folder into which
objects are transferred.

Source paths can be specified for all data sources.

### Examples

**Specifying a destination path only**

Consider that you have `object.txt` at the root of a
Cloud Storage bucket named `bucketA`.

If you transfer to `bucketB`
and set a destination path named `alpha/`, your file is copied to
`bucketB/alpha/object.txt`.

**Specifying both source and destination paths**

Consider a transfer between two Cloud Storage buckets:

- Source bucket: `bucketA` with path `alpha/`

- Destination bucket: `bucketB` with path `bravo/`

An object at `gs://bucketA/alpha/object` is transferred to
`gs://bucketB/bravo/object`.

The source path `alpha/` is stripped from the object name, leaving just
`object`, and the destination path `bravo/` is prepended to it.

### Specify a source path

To specify a source path when creating a transfer job:

- In the Cloud de Confiance console, enter the path in the **Bucket or folder**
field.

- When using gcloud CLI, specify the path as part of the source URI.
For example,
`gs:// SOURCE_BUCKET / SOURCE_PATH /`.

- With the REST API or client libraries, add a `path` field to your data source
specification. For example, the `gcsDataSource` field in your
[`TransferSpec`](/storage-transfer/docs/reference/rest/v1/TransferSpec)
specification. File system transfers use `rootDirectory` instead of `path`.

### Specify a destination path

To specify a destination path when creating a transfer job:

- In the Cloud de Confiance console, enter the path in the **Bucket or folder**
field.

- When using gcloud CLI, specify the path as part of the destination
URI. For example,
`gs:// DESTINATION_BUCKET / DESTINATION_PATH /`.

- With the REST API or client libraries, add a `path` field to your data source
specification. For example, the `gcsDataSource` or `gcsDataSink` field in your
[`TransferSpec`](/storage-transfer/docs/reference/rest/v1/TransferSpec)
specification. File system transfers use `rootDirectory` instead of `path`.