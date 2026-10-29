# Bigtable release notes

Source: https://documentation.s3ns.fr/bigtable/docs/release-notes
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/bigtable/docs/tpc-differences) for more details.














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

Databases

](https://documentation.s3ns.fr/docs/databases)






- 








[

Bigtable

](https://documentation.s3ns.fr/bigtable/docs)






- 








[

Resources

](https://documentation.s3ns.fr/bigtable/docs/resources)












# Bigtable release notes 


















This page documents production updates to Bigtable. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

Note: To view release notes for the Bigtable HBase client for
Java, see the client library's
[GitHub releases page](https://github.com/googleapis/java-bigtable-hbase/releases).







You can see the latest product updates for all of Cloud de Confiance by S3NS on the
[
Cloud de Confiance](/release-notes) page, browse and filter all release notes in the
[Cloud de Confiance console](https://console.cloud.s3nscloud.fr/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.s3nscloud.fr/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://documentation.s3ns.fr/feeds/bigtable-release-notes.xml) directly.









## October 21, 2026


Feature 


Bigtable is now available in Cloud de Confiance. For more information, see
[Bigtable in Cloud de Confiance versus Google Cloud](/bigtable/docs/tpc-differences).



## December 12, 2025


Feature 


In the Google Cloud console, you can import data into Bigtable using the
[Dataflow job builder](/dataflow/docs/guides/job-builder),
a web interface for building and running Dataflow pipelines. This integration
provides a pre-populated template to import data from Pub/Sub to Bigtable. You
can also create a custom job to import data from other sources. For more
information, see [Import and export data](/bigtable/docs/import-export).



## March 11, 2025


Feature 


You can use Cloud KMS Autokey to automate the creation and use of [customer-managed encryption keys (CMEK)](/bigtable/docs/cmek) in Bigtable clusters. This feature is generally available [(GA)](https://documentation.s3ns.fr/products#product-launch-stages).



Feature 


[Data lineage](/dataplex/docs/about-data-lineage) for Dataflow jobs is generally available [(GA)](https://documentation.s3ns.fr/products#product-launch-stages) in the Bigtable Beam connector (`BigtableIO`) and the Bigtable HBase Beam connector (`CloudBigtableIO`). For more information, see [Tracking lineage](https://github.com/googleapis/java-bigtable-hbase/tree/v2.15.0/bigtable-dataflow-parent/bigtable-beam-import#tracking-lineage).



## March 04, 2025


Feature 


Bigtable is available in the `europe-north2` (Stockholm) region. For more information, see [Bigtable locations](/bigtable/docs/locations).



## February 24, 2025


Feature 


[Bigtable Data Boost](/bigtable/docs/data-boost-overview), a serverless compute service designed for high-throughput read jobs and queries, is [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages).



Feature 


Automated backup for Bigtable is [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages). For more information, see the [Backups overview](/bigtable/docs/backups).



## February 03, 2025


Feature 


Tags data for Bigtable instances is now included in Cloud Billing data, letting you use tagged Bigtable instances to gain visibility into your resource usage and spending. For more information, see [Understand standard and detailed usage cost data](/billing/docs/how-to/export-data-bigquery-tables/standard-usage#usage-cost-export-more-info).



## December 18, 2024


Feature 


You can now enable [2x node scaling](/bigtable/docs/scaling#node-scaling) when you create a new Bigtable cluster. This cluster configuration lets Bigtable treat two standard nodes as a larger, single compute node, and the cluster is always scaled in increments of two nodes. This feature is [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages).



Change 


The [Preview](https://documentation.s3ns.fr/products#product-launch-stages) of Bigtable automated backup has been expanded to let you configure the backup retention period in automated backup policies, and the default is now seven days. For more information, see [Update an automated backup policy](/bigtable/docs/managing-backups#update-automated-backup).



## December 17, 2024


Feature 


You can use Organization Policy Service custom constraints to manage specific operations on Bigtable resources. For more information, see [Use custom organization policies](/bigtable/docs/custom-constraints). This feature is [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages).



## December 12, 2024


Feature 


Bigtable is now supported by Database Center, which is in [Preview](https://documentation.s3ns.fr/products#product-launch-stages). Database Center is an AI-assisted dashboard that gives you one centralized view across your entire database fleet. With this release, Database Center displays health issues for Bigtable availability and data protection. For more information, see [Database health issues](/database-center/docs/database-health-issues).



## December 11, 2024


Feature 


You can now enable [row-affinity routing](/bigtable/docs/routing#row-affinity) to let Bigtable automatically ensure that single-row requests for a given row are routed to the same cluster. This feature is [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages).



Feature 


You can now use the Google Cloud console to [create and manage authorized views](/bigtable/docs/authorized-views-create-manage) of your Bigtable tables.



Announcement 


You can now select a row in a Bigtable Studio query results table to view formatted row data. For more information, see [Query your data with SQL in the query editor](/bigtable/docs/manage-data-using-console#query-editor).



## December 02, 2024


Change 


To create a Bigtable instance, a user or account must be a principal in a role with the permission `bigtable.clusters.create`. For more information, see [Bigtable access control with IAM](/bigtable/docs/access-control).



## November 18, 2024


Feature 


You can now create a Data Boost app profile and view Data Boost metrics in the Google Cloud console. Data Boost for Bigtable is in [Preview](https://documentation.s3ns.fr/products#product-launch-stages). For more information, see [Create and configure app profiles](/bigtable/docs/configuring-app-profiles).



Feature 


Bigtable is now available in the `northamerica-south1` (Mexico) region. For more information, see [Bigtable locations](/bigtable/docs/locations).



## October 08, 2024


Feature 


Hot backups, optimized backups to restore your data to production performance availability more efficiently, are now [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages). For more information, see [Backups overview](/bigtable/docs/backups).



## September 25, 2024


Announcement 


You can perform [similarity vector search in Bigtable](/bigtable/docs/find-k-nearest-neighbors) by finding the K-nearest neighbors. This feature is available as part of the [GoogleSQL for Bigtable Preview](/bigtable/docs/googlesql-overview).



## August 28, 2024


Feature 


The [Preview](https://documentation.s3ns.fr/products#product-launch-stages) of Data Boost for Bigtable has been expanded to let you use Data Boost compute resources when you read Bigtable data using a Spark application. For more information, see [Use the Bigtable Spark connector](/bigtable/docs/use-bigtable-spark-connector#compute).



## August 26, 2024


Feature 


You can use `EXPORT DATA` statements to [directly export BigQuery data to Bigtable (reverse ETL)](/bigquery/docs/export-to-bigtable). This feature is [generally available](https://documentation.s3ns.fr/products#product-launch-stages) (GA).



## August 13, 2024


Announcement 


You can now enable client-side metrics with the Bigtable client library for Go. Used in conjunction with server-side monitoring metrics, client-side metrics can provide a complete, actionable view of Bigtable performance. For more information, see [Set up client-side metrics](/bigtable/docs/client-side-metrics-setup).



## August 01, 2024


Feature 


Bigtable supports querying in **SQL**. This feature is available in [Preview](https://documentation.s3ns.fr/products#product-launch-stages). For more information, see [Introduction to SQL for Bigtable](/bigtable/docs/introduction-sql).



Feature 


The Bigtable Studio **query editor** is available in [Preview](https://documentation.s3ns.fr/products#product-launch-stages). For more information, see [Manage your data using Bigtable Studio](/bigtable/docs/manage-data-using-console).



Feature 


Bigtable aggregates let you build **distributed counters** and aggregate your Bigtable data at write time using min, max, sum, or HLL. This feature is [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages). For more information, see [Aggregate values at write time](/bigtable/docs/aggregates).



## July 25, 2024


Feature 


The [Preview](https://documentation.s3ns.fr/products#product-launch-stages) of automated backup has been expanded to let you enable and disable automated backup in the Google Cloud console. For more information, see the [automated backup](/bigtable/docs/managing-backups#use-automated-backup) documentation.



## June 17, 2024


Feature 


The Python client library for Bigtable now offers an asynchronous API for use with asynchronous applications. The async API is [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages). To get started, see the [Python hello world](/bigtable/docs/samples-python-hello).