# Sources and sinks

Source: https://berlin.devsitetest.how/storage-transfer/docs/sources-and-sinks
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












# Sources and sinks 















Storage Transfer Service can transfer data from a number of sources to a number of
destinations. The table below details the supported sources and destinations.



| 
Storage system | 
Source | 
Destination | 
Notes | 
|




| 
Cloud Storage | 
check_circle | 
check_circle | 


Cloud Storage is a valid sink for transfers from all sources.



Transfers from Cloud Storage, Amazon S3, and Azure to
Cloud Storage do not require agents or agent
pools; they are managed entirely by Storage Transfer Service.



To configure Cloud Storage as a source and/or sink, refer to the
following pages:




- [Configure
access to a source: Cloud Storage](/storage-transfer/docs/source-cloud-storage)

- [Configure
access to a sink: Cloud Storage](/storage-transfer/docs/sink-cloud-storage)


| 
|

| 
Amazon Simple Storage Service (Amazon S3) | 
check_circle | 
| 


Transfers to Cloud Storage only. Does not require agents or
agent pools.



To configure Amazon S3, refer to
[Configure access to
a source: Amazon S3](/storage-transfer/docs/source-amazon-s3).

| 
|

| 
S3-compatible storage | 
check_circle | 
| 


Transfers to Cloud Storage only. Requires agents and
agent pools.



To configure S3-compatible storage, refer to
[Configure access to
a source: S3-compatible storage](/storage-transfer/docs/source-s3-compatible).

| 
|

| 
Azure Blob Storage, including Azure Data Lake Storage Gen2 | 
check_circle | 
| 


Transfers to Cloud Storage only. Does not require agents or
agent pools.



To configure Azure storage options, refer to
[Configure access
to a source: Microsoft Azure Storage](/storage-transfer/docs/source-microsoft-azure).
| 
|

| 
Publicly accessible or signed HTTP and HTTPs URLs | 
check_circle | 
| 


Storage Transfer Service accepts a TSV file specifying a list of URLs to
transfer.



Transfers to Cloud Storage only. Does not require agents or
agent pools.



See [Create a URL
list](/storage-transfer/docs/create-url-list) for details.

| 
|

| 
File system | 
check_circle | 
check_circle | 


Storage Transfer Service supports transfers:




- From file systems to Cloud Storage

- From Cloud Storage to file systems

- Between two file systems




Transfers involving file systems require agents and agent pools. See
[Manage agent
pools](/storage-transfer/docs/on-prem-agent-pools) to get started.
| 
|

| 
Hadoop distributed file system (HDFS) | 
check_circle | 
| 


Transfers to Cloud Storage only. Requires agents and agent pools.




To configure a transfer from an HDFS source, refer to
[Transfer from HDFS to
Cloud Storage](/storage-transfer/docs/hdfs).

| 
|