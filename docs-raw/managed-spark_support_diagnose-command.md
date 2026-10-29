# View cluster diagnostic data

Source: https://berlin.devsitetest.how/managed-spark/docs/support/diagnose-command
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/managed-spark/docs/tpc-differences) for more details.














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

Managed Service for Apache Spark

](https://berlin.devsitetest.how/managed-spark/docs)






- 








[

Guides

](https://berlin.devsitetest.how/managed-spark/docs/overview/key-concepts)












# View cluster diagnostic data 


















"View Managed Service for Apache Spark cluster diagnostic data" 


You can take advantage of the following Managed Service for Apache Spark diagnostic data
collection features to troubleshoot cluster and job issues:

- [**Checkpoint diagnostic data**](#checkpoint_diagnostic_data_collection):
By default, Managed Service for Apache Spark collects checkpoint
diagnostic data during the cluster lifecycle.

- [**Snapshot diagnostic data**](#snapshot_diagnostic_data_collection):
You can collect a one-time snapshot of cluster diagnostic data when needed.

## Checkpoint diagnostic data collection

By default, Managed Service for Apache Spark collects
[checkpoint diagnostic data](#checkpoint_diagnostic_data)
during [cluster creation](/managed-spark/docs/guides/create-cluster),
[cluster update](/managed-spark/docs/guides/manage-cluster#update_a_cluster), and
[Managed Service for Apache Spark job](/managed-spark/docs/guides/submit-job) operations.

### Checkpoint data location

Managed Service for Apache Spark saves [checkpoint diagnostic data](#checkpoint_diagnostic_data)
in the cluster [temp bucket](/managed-spark/docs/concepts/configuring-clusters/staging-bucket)
in Cloud Storage in the following folder (the `checkpoint diagnostic data folder`):


```
gs:// TEMP_BUCKET /google-cloud-dataproc-diagnostic/ CLUSTER_UUID 
```


The default cluster temp bucket has a TTL retention period of 90 days. The data
is deleted at the end of the retention period. You can
[specify your own cluster temp bucket](/managed-spark/docs/concepts/configuring-clusters/staging-bucket#create_your_own_staging_and_temp_buckets)
with a different [TTL period](/storage/docs/managing-lifecycles) when you
create a cluster.

### Checkpoint diagnostic data

- 

**Cluster node detail logs:** Managed Service for Apache Spark runs the following commands
to collect and write YARN and HDFS information to the following
locations in the checkpoint diagnostic data folder in Cloud Storage. 


| 
**Command executed** | 
**Location in diagnostic folder** | 
|



| 
`yarn node -list -all` | 
`.../nodes/ timestamp /yarn-nodes.log` | 
|

| 
`hdfs dfsadmin -report -live -decommissioning` | 
`.../nodes/ timestamp /hdfs-nodes.log` | 
|

| 
`cp gs:// STAGING_BUCKET /google-cloud-dataproc-metainfo/ CLUSTER_UUID /nodes_exclude.xml` | 
`.../nodes/ timestamp /nodes_exclude.xml` | 
|



- 

**Job Details:** Managed Service for Apache Spark saves MapReduce job information and
Spark job logs for jobs using the Managed Service for Apache Spark Jobs API. This
job data is collected for each MapReduce and spark job submitted.

- MapReduce `job.xml`: A file containing job configuration settings,
saved at `.../jobs/ JOB_UUID /mapreduce/job.xml`.

- Spark event logs: Job execution details useful for debugging,
saved at `.../jobs/ JOB_UUID /spark/application-id`.

- 

**Linux system information:** Managed Service for Apache Spark runs the following
commands to collect and save system information in the following locations
in the checkpoint diagnostic data folder in Cloud Storage.



| 
**Command** | 
**Location in diagnostics folder** | 
|




| 
`sysctl -a` | 
`.../system/sysctl.log` | 
|

| 
`cat /proc/sys/fs/file-nr` | 
`.../system/fs-file-nr.log` | 
|

| 
`ping -c 1` | 
`.../system/cluster-ping.log` | 
|

| 
`cp /etc/hosts` | 
`.../system/hosts_entries.log` | 
|

| 
`cp /etc/resolv.conf` | 
`.../system/resolv.conf` | 
|



- 

**Configuration files:** Managed Service for Apache Spark saves the following
configuration files in the following locations
in the checkpoint diagnostic data folder in Cloud Storage.



| 
**Item(s) included** | 
**Location in diagnostics folder** | 
|



| 
Managed Service for Apache Spark properties | 
`.../configs/dataproc/dataproc.properties` | 
|

| 
All files in 
`/etc/google-dataproc/` | 
`.../configs/dataproc/` | 
|

| 
All files in 
`/etc/hadoop/conf/` | 
`.../configs/hadoop/` | 
|

| 
All files in `/etc/hive/conf/` | 
`.../configs/hive/` | 
|

| 
All files in 
`/etc/hive-hcatalog/conf/` | 
`.../configs/hive-hcatalog/` | 
|

| 
All files in `/etc/knox/conf/` | 
`.../configs/knox/` | 
|

| 
All files in `/etc/pig/conf/` | 
`.../configs/pig/` | 
|

| 
All files in 
`/etc/presto/conf/` | 
`.../configs/presto/` | 
|

| 
All files in 
`/etc/spark/conf/` | 
`.../configs/spark/` | 
|

| 
All files in `/etc/tez/conf/` | 
`.../configs/tez/` | 
|

| 
All files in 
`/etc/zookeeper/conf/` | 
`.../configs/zookeeper/` | 
|



### Share checkpoint diagnostic data with support

You can enable sharing checkpoint diagnostic data with
[Google Cloud Dedicated in Germany support](/managed-spark/docs/support/getting-support) in the
following ways:

- 

**Enable sharing at cluster creation**: Add the following
[optional cluster property](/managed-spark/docs/concepts/configuring-clusters/cluster-properties#examples)
when you [create a cluster](/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster):


```
dataproc:diagnostic.capture.access=GOOGLE_DATAPROC_DIAGNOSE
```


This property automatically shares collected checkpoint diagnostic data with
[Google Cloud Dedicated in Germany support](/managed-spark/docs/support/getting-support) so that you
don't have to manually share after cluster creation each time.

- 

**Enable sharing after cluster creation**: You can enable sharing checkpoint data
with [Google Cloud Dedicated in Germany support](/managed-spark/docs/support/getting-support)
after cluster creation by providing read access to checkpoint data to the
service account used by the Google Cloud Dedicated in Germany support, as follows:

- 

If uniform bucket-level access is enabled on the temp bucket,
add IAM policy binding:

```
gcloud storage buckets add-iam-policy-binding gs:// TEMP_BUCKET \
    --member=serviceAccount:cloud-diagnose@cloud-dataproc.eu0.iam.gserviceaccount.com \
    --role=roles/storage.objectViewer
```


- 

If object-level access control is enabled on the temp bucket,
run the following command to share checkpoint diagnostic data:

```
gcloud storage objects update \
    gs:// TEMP_BUCKET /google-cloud-dataproc-diagnostic/ CLUSTER_UUID \
    --add-acl-grant=entity=user-cloud-diagnose@cloud-dataproc.eu0.iam.gserviceaccount.com,role=READER --recursive
```


### Disable checkpoint diagnostic data collection

To disable the collection of checkpoint diagnostic data on a cluster, set
[`dataproc:diagnostic.capture.enabled=false`](/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc_service_properties_table)
when you create the cluster.

## Snapshot diagnostic data collection

You can run the following
[`gcloud dataproc clusters diagnose`](/sdk/gcloud/reference/dataproc/clusters/diagnose)
command to collect a [snapshot of diagnostic data](#diagnostic_snapshot_data) from a
running cluster. The data is written as an archive (tar) file to the Managed Service for Apache Spark
[staging bucket](/managed-spark/docs/concepts/configuring-clusters/staging-bucket) in
Cloud Storage.


```
gcloud dataproc clusters diagnose CLUSTER_NAME \
    --region= REGION \
    --tarball-access=GOOGLE_DATAPROC_DIAGNOSE \
    --tarball-gcs-dir= TARBALL_DIR 
```


Notes:

- CLUSTER_NAME : The name of the cluster to diagnose.

- REGION : The cluster's region, for example, `us-central1`.

- 

`--tarball-access`=`GOOGLE_DATAPROC_DIAGNOSE` This flag
provides access to the diagnostic tar file to
[Google Cloud Dedicated in Germany support](/managed-spark/docs/support/getting-support).
Provide Google Cloud Dedicated in Germany support with the Cloud Storage path of the
diagnostic tar file.

As an alternative to providing the tar file to support, you can
provide the cluster UUID, operation ID of the diagnose command,
and the Cloud Storage location of the cluster configuration bucket.

If you choose to write diagnostic tar file to a specific directory,
provide Google Cloud Dedicated in Germany support with the full Cloud Storage path
of the tar file which is printed by the diagnose command.

**Bucket access and scope of shared content**: The access setting
on the Cloud Storage bucket that contains the diagnostic
tar file determines the scope of the content shared with Google Cloud Dedicated in Germany support:

- 

**Uniform bucket-level access**: If
[uniform bucket-level access](/storage/docs/uniform-bucket-level-access)
is enabled on the Managed Service for Apache Spark staging bucket or,
if a TARBALL_DIR is specified, on the bucket that contains the
TARBALL_DIR , all of the bucket contents are shared with
Google Cloud Dedicated in Germany support.

- 

**Object-level access**: If object-level access
is enabled on the Managed Service for Apache Spark staging bucket or,
if a TARBALL_DIR is specified, on the bucket that contains the
TARBALL_DIR , only the diagnostic tar file is shared with
Google Cloud Dedicated in Germany support.

- 

TARBALL_DIR : Optional. You can use this flag to specify
a Cloud Storage directory where the diagnostic tar file will
be written. If this flag is omitted, the diagnostic tar file will be
written to the
[Managed Service for Apache Spark staging bucket](/managed-spark/docs/concepts/configuring-clusters/staging-bucket).

- 

Additional flags :

- 

`--start-time` with `--end-time`: Use both flags to specify a time
range in `%Y-%m-%dT%H:%M:%S.%fZ` format for the collection of
diagnostic data. Specifying a time range also enables the collection of
Managed Service for Apache Spark autoscaling logs during the time range (by
default, Managed Service for Apache Spark autoscaling logs are not collected in
the diagnostic snapshot data).

- 

You can use either of both of the following flags to collect specific
job driver, Spark event, YARN application, and
[Sparklens](https://spark-packages.org/package/qubole/sparklens) output
logs:

- `--job-ids`: A comma-separated list of job IDs

- 

`--yarn-application-ids`: A comma-separated list of YARN application IDs 

- YARN log aggregation must be enabled (`yarn.log-aggregation-enable=true`)
for the collection of YARN
application logs.

- For MapReduce jobs, YARN application logs only are collected.

### Optional: Run the diagnostic script

The `gcloud dataproc clusters diagnose` command can fail or time-out if a
cluster is in an error state and cannot accept diagnose tasks from the
Managed Service for Apache Spark server. As an alternative to running the diagnose command, you
can [use SSH](/managed-spark/docs/concepts/accessing/ssh) to connect to the cluster
then run the script locally on the master node.


```
gcloud compute ssh HOSTNAME 
`gcloud storage cp gs://dataproc-diagnostic-scripts/diagnostic-script.sh .`
`sudo bash diagnostic-script.sh
```


The diagnostic archive tar file is saved in a local directory. The command
output lists the location of the tar file with instructions on how to upload the
tar file to a Cloud Storage bucket.

### Diagnostic snapshot data

Cluster snapshot data includes a diagnostic summary and several archive sections. 

**Diagnostic summary:** The archive file includes summary.txt` that is
at the root of the archive. It provides an overview of cluster status,
including YARN, HDFS, disk, and networking status, and includes warnings to
alert you to potential problems.

**Archive sections:** The archive file includes the following information
that is written to the following archive file locations.

- 

**Daemons and services information**



| 
Command executed | 
Location in archive | 
|



| 
`yarn node -list -all` | 
`/system/yarn-nodes.log` | 
|

| 
`hdfs dfsadmin -report -live -decommissioning` | 
`/system/hdfs-nodes.log` | 
|

| 
`hdfs dfs -du -h` | 
`/system/hdfs-du.log` | 
|

| 
`service --status-all` | 
`/system/service.log` | 
|

| 
`systemctl --type service` | 
`/system/systemd-services.log` | 
|

| 
`curl "http://${HOSTNAME}:8088/jmx"` | 
`/metrics/resource_manager_jmx` | 
|

| 
`curl "http://${HOSTNAME}:8088/ws/v1/cluster/apps"` | 
`/metrics/yarn_app_info` | 
|

| 
`curl "http://${HOSTNAME}:8088/ws/v1/cluster/nodes"` | 
`/metrics/yarn_node_info` | 
|

| 
`curl "http://${HOSTNAME}:9870/jmx"` | 
`/metrics/namenode_jmx` | 
|



- 

**JVM information**



| 
Command executed | 
Location in archive | 
|



| 
`jstack -l "${DATAPROC_AGENT*PID}"`
| 
`jstack/agent*${DATAPROC_AGENT_PID}.jstack` | 
|

| 
`jstack -l "${PRESTO*PID}"` | 
`jstack/agent*${PRESTO_PID}.jstack` | 
|

| 
`jstack -l "${JOB_DRIVER*PID}"`
| 
`jstack/driver*${JOB_DRIVER_PID}.jstack` | 
|

| 
`jinfo "${DATAPROC_AGENT*PID}"`
| 
`jinfo/agent*${DATAPROC_AGENT_PID}.jstack` | 
|

| 
`jinfo "${PRESTO*PID}"` | 
`jinfo/agent*${PRESTO_PID}.jstack` | 
|

| 
`jinfo "${JOB_DRIVER*PID}"` | 
`jinfo/agent*${JOB_DRIVER_PID}.jstack` | 
|



- 

**Linux system information**


| 
Command executed | 
Location in archive | 
|



| 
`df -h` | 
`/system/df.log` | 
|

| 
`ps aux` | 
`/system/ps.log` | 
|

| 
`free -m` | 
`/system/free.log` | 
|

| 
`netstat -anp` | 
`/system/netstat.log` | 
|

| 
`sysctl -a` | 
`/system/sysctl.log` | 
|

| 
`uptime` | 
`/system/uptime.log` | 
|

| 
`cat /proc/sys/fs/file-nr` | 
`/system/fs-file-nr.log` | 
|

| 
`ping -c 1` | 
`/system/cluster-ping.log` | 
|



- 

**Log files** 


| 
Item included | 
Location in archive | 
|



| 

All logs in `/var/log` with the following prefixes in their filename:


`cloud-sql-proxy`

`dataproc`

`druid`

`gcdp`

`google`

`hadoop`

`hdfs`

`hive`

`knox`

`presto`

`spark`

`syslog`

`yarn`

`zookeeper`
| 
Files are placed in the archive `logs` folder, and keep their original filenames. | 
|

| 
Managed Service for Apache Spark node startup logs for each node (master and worker) in your cluster. | 
Files are placed in the archive `node_startup` folder, which contains separate subfolders for each machine in the cluster. | 
|

| 
Component gateway logs from `journalctl -u google-dataproc-component-gateway` | 
`/logs/google-dataproc-component-gateway.log` | 
|



- 

**Configuration files**


| 
Item(s) included | 
Location in archive | 
|



| 
VM metadata | 
`/conf/dataproc/metadata` | 
|

| 
Environment variables in `/etc/environment` | 
`/conf/dataproc/environment` | 
|

| 
Managed Service for Apache Spark properties | 
`/conf/dataproc/dataproc.properties` | 
|

| 
All files in `/etc/google-dataproc/` | 
`/conf/dataproc/` | 
|

| 
All files in `/etc/hadoop/conf/` | 
`/conf/hadoop/` | 
|

| 
All files in `/etc/hive/conf/` | 
`/conf/hive/` | 
|

| 

All files in `/etc/hive-hcatalog/conf/`
| 
`/conf/hive-hcatalog/` | 
|

| 
All files in `/etc/knox/conf/` | 
`/conf/knox/` | 
|

| 
All files in `/etc/pig/conf/` | 
`/conf/pig/` | 
|

| 
All files in `/etc/presto/conf/` | 
`/conf/presto/` | 
|

| 
All files in `/etc/spark/conf/` | 
`/conf/spark/` | 
|

| 
All files in `/etc/tez/conf/` | 
`/conf/tez/` | 
|

| 
All files in `/etc/zookeeper/conf/` | 
`/conf/zookeeper/` | 
|



### Share the archive file

You can share the archive file with Google Cloud Dedicated in Germany support or users to
obtain help to troubleshoot cluster or job issues.

To share the archive file:

- [Copy the archive file](/sdk/gcloud/reference/storage/cp)
from Cloud Storage, and then share the downloaded archive, or

- 

[Change the permissions](/sdk/gcloud/reference/storage/objects/update)
on the archive to allow other Google Cloud Dedicated in Germany users or projects to access the
file.

Example: The following command gives read permissions to the archive to
owners of the project `test-project`:


```
gcloud storage objects update PATH_TO_ARCHIVE --add-acl-grant=entity=project-owners-test-project,role=READER
```