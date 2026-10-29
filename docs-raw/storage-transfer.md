# Storage Transfer Service

Source: https://berlin.devsitetest.how/storage-transfer/docs
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/storage-transfer/docs/overview/tpc-differences) for more details.














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

Storage

](https://berlin.devsitetest.how/docs/storage)






- 








[

Storage Transfer Service

](https://berlin.devsitetest.how/storage-transfer/docs/overview)












# Storage Transfer Service 




















Storage Transfer Service enables seamless data movement across object and file
storage systems, including:

- Amazon S3 to Cloud Storage (requires agents), or Cloud Storage to Cloud Storage

- On-premises storage to Cloud Storage, or Cloud Storage to on-premises

- Between on-premises storage systems

- From HDFS to Cloud Storage

Storage Transfer Service is optimized for transfers involving more than 1TiB of data.
For smaller transfers, see our
[recommendations](/storage-transfer/docs/transfer-options).

With Storage Transfer Service, you can:

- **Automate data transfers**: Eliminate the need for manual processes and custom scripts.

- **Transfer data at scale**: Move petabytes of data quickly and reliably.

- **Optimize network performance**: Choose between Google-managed transfers for simplicity or self-hosted agents for granular control over network routing and bandwidth consumption.

- **Support diverse storage systems**: Transfer data seamlessly between cloud providers and on-premises environments.

## Use cases

**Migrating data to Cloud Storage**: Storage Transfer Service can be used to migrate
data from other cloud storage providers or on-premises data centers to
Cloud Storage.

**Backup**: Replicate your data to Google Cloud, or create a copy of a
Cloud Storage bucket in another region

**Data processing pipelines**: Move data generated on other clouds, your data
center, and the edge to Google Cloud for analytics using
[BigQuery](/bigquery).

**Archival**: Move cold data from costly on-premises storage systems to
Cloud Storage to reduce storage cost.

## Benefits

**Secure**

- End-to-end encryption protects your data in transit. Storage Transfer Service
supports TLS 1.3 for all HTTPS communication.

- Data integrity validation ensures that your data is not corrupted during
transfer.

**Performant**

- Highly-parallelized architecture accelerates transfer speeds.

- Automatic retries and load balancing ensure reliable transfers.

**Fully managed**

- No need to manage infrastructure or write code.

- Focus on your applications, not data transfer.

## Get started

Check to see if your
[source and sink combination is supported](/storage-transfer/docs/sources-and-sinks).

There are a number of ways that you can work with Storage Transfer Service:

- The Google Cloud Dedicated console

- REST APIs

- The `gcloud` command-line tool

- Java and Python client libraries

See [Create transfers](/storage-transfer/docs/create-transfers) to get started.

## What's next

- Learn about [Storage Transfer Service differences in Google Cloud versus Google Cloud](/storage-transfer/docs/tpc-differences).