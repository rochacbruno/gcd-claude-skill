# Managed Service for Apache Spark in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/managed-spark/docs/tpc-differences
Last updated: 2026-10-26

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












# Managed Service for Apache Spark in Google Cloud Dedicated versus Google Cloud 















Managed Service for Apache Spark cluster deployment is a managed Spark and Hadoop service that lets you take advantage of open 
source data tools for batch processing, querying, streaming, and machine learning.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Managed Service for Apache Spark.



For more detailed information about Managed Service for Apache Spark, see the
[Managed Service for Apache Spark overview](/managed-spark/docs/concepts/overview) and the rest of the
Managed Service for Apache Spark documentation.




## Key differences



There are some differences between the Google Cloud Dedicated version of Managed Service for Apache Spark and
the Google Cloud version.
Some notable differences include the following:






- 
Managed Service for Apache Spark serverless (formerly known as Google Cloud Dedicated in Germany for Serverless for Apache Spark) is unavailable in
Google Cloud Dedicated.


- 
Managed Service for Apache Spark cluster optional OSS components are unavailable in Google Cloud Dedicated.


- 
Managed Service for Apache Spark cluster autoscaling is unavailable in Google Cloud Dedicated.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Managed Service for Apache Spark feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Hardware and OS



| 
**Machine types**
| 
Only `m3`, `c3-highcpu`, `c3-highmem`, `c3-standard`, and `a3` machine types
are supported.
| 
|

| 
**GPUs**
| 
Only NVIDIA H100 SXM GPUs are supported.
| 
|

| 
**Secondary workers**
| 
Preemptible and spot VMs are not supported.
| 
|

| 
**Flexible VMs**
| 
Flexible VMs are not supported.
| 
|

| 
**Local solid state drives**
| 
Local SSDs are not supported.
| 
|

| 
**Persistent boot disks**
| 
Only hyperdisk boot disks are supported.
| 
|

| 
**Cluster image versions**
| 
Only [2.3+ image versions](/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions) are supported.
| 
|

| 
**Kubernetes clusters**
| 
Kubernetes clusters are not supported.
| 
|


### Integrations



| 
**Optional OSS components**
| 
Managed Service for Apache Spark cluster optional OSS components, and cluster properties related to these components, are not supported.
| 
|

| 
**Notebooks**
| 
Notebooks, such as Jupyter, are not supported.
| 
|

| 
**Knowledge Catalog**
| 
Knowledge Catalog, including data lineage, is not supported.
| 
|

| 
**Pub/Sub Lite Lite**
| 
Pub/Sub Lite Lite is not supported.
| 
|


### Security and access control



| 
CMEK 
| 
CMEK (customer-managed encryption keys) is supported, however you can't
use CMEK with workflow template data, since workflow templates are not
supported.
| 
|

| 
Memory encryption 
| 
Memory encryption is not supported.
| 
|

| 
**Personal cluster authentication**
| 
Personal cluster authentication is not supported.
| 
|

| 
**Granular IAM**
| 
Granular IAM is not supported.
| 
|

| 
**Secure multi-tenancy clusters**
| 
Secure multi-tenancy clusters using service accounts or Kerberos is not
supported.
| 
|


### Network



| 
**Default network**
| 
A default network is not automatically created in a project.
[Users must create a VPC network in a project](/managed-spark/docs/tpc-differences#network-differences).
| 
|


### Workflows and tools



| 
**Initialization actions**
| 
Initialization actions are not supported.
| 
|

| 
**Autoscaling**
| 
Autoscaling is not supported.
| 
|

| 
**Component Gateway**
| 
The Managed Service for Apache Spark Component Gateway is not supported.
| 
Connecting through the Managed Service for Apache Spark Component Gateway to
cluster web interfaces is not supported.
| 
Workforce access to the Managed Service for Apache Spark Component Gateway is
not supported.
| 
|

| 
**Workflow orchestration**
| 
Managed Service for Apache Airflow is supported without workflow templates, and other workflow tools, such as Managed Service for Apache Spark workflow templates, Cloud Scheduler, and Cloud Functions, are not supported.
| 
|

| 
**Custom constraints**
| 
Custom constraints in organization policies are not supported.
| 
Fleet management with custom organization policies with
custom constraints is not supported.
| 
|

| 
**Persistent History Server**
| 
Persistent History Server (PHS) is not supported.
| 
|

| 
**Enhanced Flexibility Mode**
| 
Enhanced Flexibility Mode (EFM) is not supported.
| 
|

| 
**MCP server**
| 
The MCP server is not supported.
| 
|


### Insights and observability



| 
**Managed Service for Apache Spark cluster metrics**
| 
`dataproc.googleapis` metrics are available, but Managed Service for Apache Spark serverless and custom metrics are not available. 
| 
|

| 
**Metric dashboards and alerts**
| 
Managed Service for Apache Spark metric dashboards and metric alerts are not available.
| 
|





## Related guides



The following information might also affect how you use and design for Managed Service for Apache Spark
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)