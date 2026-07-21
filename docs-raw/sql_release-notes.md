# Cloud SQL release notes

Source: https://berlin.devsitetest.how/sql/docs/release-notes
Last updated: 2026-07-21

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/sql/docs/tpc-differences) for more details.














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

Databases

](https://berlin.devsitetest.how/docs/databases)






- 








[

Cloud SQL

](https://berlin.devsitetest.how/sql/docs)






- 








[

Resources

](https://berlin.devsitetest.how/sql/docs/resources)












# Cloud SQL release notes 






- On this page 
- [ June 29, 2026 ](#June_29_2026)
- [ June 24, 2026 ](#June_24_2026)
- [ June 22, 2026 ](#June_22_2026)
- [ June 18, 2026 ](#June_18_2026)
- [ June 08, 2026 ](#June_08_2026)
- [ March 30, 2026 ](#March_30_2026)
- [ March 26, 2026 ](#March_26_2026)
- [ March 20, 2026 ](#March_20_2026)
- [ March 09, 2026 ](#March_09_2026)
- [ November 18, 2025 ](#November_18_2025)
- [ November 13, 2025 ](#November_13_2025)
- [ November 12, 2025 ](#November_12_2025)
- [ March 03, 2025 ](#March_03_2025)
- [ February 26, 2025 ](#February_26_2025)
- [ February 11, 2025 ](#February_11_2025)
- [ January 14, 2025 ](#January_14_2025)
- [ January 13, 2025 ](#January_13_2025)
- [ December 23, 2024 ](#December_23_2024)
- [ December 20, 2024 ](#December_20_2024)
- [ December 10, 2024 ](#December_10_2024)
- [ December 05, 2024 ](#December_05_2024)
- [ December 04, 2024 ](#December_04_2024)
- [ December 03, 2024 ](#December_03_2024)
- [ November 27, 2024 ](#November_27_2024)
- [ November 21, 2024 ](#November_21_2024)
- [ November 20, 2024 ](#November_20_2024)
- [ November 19, 2024 ](#November_19_2024)
- [ November 18, 2024 ](#November_18_2024)
- [ November 15, 2024 ](#November_15_2024)
- [ November 14, 2024 ](#November_14_2024)
- [ November 12, 2024 ](#November_12_2024)
- [ November 04, 2024 ](#November_04_2024)
- [ October 25, 2024 ](#October_25_2024)
- [ October 23, 2024 ](#October_23_2024)
- [ October 21, 2024 ](#October_21_2024)
- [ October 16, 2024 ](#October_16_2024)
- [ October 09, 2024 ](#October_09_2024)
- [ October 03, 2024 ](#October_03_2024)
- [ October 01, 2024 ](#October_01_2024)
- [ September 25, 2024 ](#September_25_2024)
- [ September 19, 2024 ](#September_19_2024)
- [ September 16, 2024 ](#September_16_2024)
- [ September 13, 2024 ](#September_13_2024)
- [ September 12, 2024 ](#September_12_2024)
- [ September 03, 2024 ](#September_03_2024)
- [ August 15, 2024 ](#August_15_2024)
- [ August 01, 2024 ](#August_01_2024)
- [ July 31, 2024 ](#July_31_2024)
- [ July 30, 2024 ](#July_30_2024)
- [ July 29, 2024 ](#July_29_2024)
- [ July 26, 2024 ](#July_26_2024)
- [ July 25, 2024 ](#July_25_2024)
- [ July 19, 2024 ](#July_19_2024)
- [ July 18, 2024 ](#July_18_2024)
- [ July 17, 2024 ](#July_17_2024)
- [ July 16, 2024 ](#July_16_2024)
- [ July 02, 2024 ](#July_02_2024)
- 




















You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/cloud-sql-release-notes.xml) directly.











## June 29, 2026 

**Cloud SQL for MySQL**

Feature 


MySQL 8.0.45 is now the [default minor version](/sql/docs/mysql/db-versions#database-version-support) for Cloud SQL for MySQL 8.0.

For more information about minor version support in Cloud SQL for MySQL,
see [MySQL 8.0](/sql/docs/mysql/db-versions#mysql-8.0).



## June 24, 2026

**Cloud SQL for MySQL**

Change 


Cloud SQL now supports Private Service Connect outbound connectivity on the
following additional types of instances:

- 

Read replica instances.

- 

Instances that use advanced disaster recovery features such as switchover and
failover operations.

For more information about Private Service Connect outbound connectivity see
[About Private Service Connect](https://berlin.devsitetest.how/sql/docs/mysql/about-private-service-connect#psc-outbound).


**Cloud SQL for PostgreSQL**

Change 


Cloud SQL now supports Private Service Connect outbound connectivity on the
following additional types of instances:

- 

Read replica instances.

- 

Instances that use advanced disaster recovery features such as switchover and
failover operations.

For more information about Private Service Connect outbound connectivity see
[About Private Service Connect](https://berlin.devsitetest.how/sql/docs/postgres/about-private-service-connect#psc-outbound).



## June 22, 2026

**Cloud SQL for PostgreSQL**

Feature 


Customer-managed encryption key (CMEK) support for Cloud SQL enhanced backups is
generally available. You can protect your CMEK-enabled Cloud SQL instances
using Google Cloud Backup and DR Service.

For more information, see [Choose your backup
option](https://berlin.devsitetest.how/sql/docs/postgres/backup-recovery/backup-options).



## June 18, 2026

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL now supports minor version
[8.0.46](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-46.html).
To upgrade your existing instance to the new minor version, see
[Upgrade the database minor version](/sql/docs/mysql/upgrade-minor-db-version#manual-upgrade).



## June 08, 2026

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL [managed buffer pool](/sql/docs/mysql/optimize-high-memory-usage#enable-managed-buffer-pool)
is now generally available ([GA](https://berlin.devsitetest.how/products/#product-launch-stages)).
Managed buffer pool helps you avoid out-of-memory events (OOMs) on your
Cloud SQL instance by reducing `innodb_buffer_pool_size` when memory usage is high.



## March 30, 2026

**Cloud SQL for PostgreSQL**

Feature 


Cloud SQL for PostgreSQL now offers conversational analytics, which lets users query
their operational data using natural language. This feature is powered by the
[Conversational Analytics API](/gemini/data-agents/conversational-analytics-api/overview),
which can help you translate complex human dialog into precise database queries
to provide actionable insights. This feature is in
[Preview](/products#product-launch-stages).
For more information, see [Conversational analytics for Cloud SQL for PostgreSQL overview](/gemini/data-agents/conversational-analytics/sql-postgres).



## March 26, 2026

**Cloud SQL for MySQL**

Feature 


MySQL 8.0.44 is now the [default minor version](https://berlin.devsitetest.how/sql/docs/mysql/db-versions#database-version-support) for Cloud SQL for MySQL 8.0.

For more information about minor version support in Cloud SQL for MySQL, see
[MySQL 8.0](https://berlin.devsitetest.how/sql/docs/mysql/db-versions#mysql-8.0).



## March 20, 2026

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL now supports minor version
[8.0.45](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-45.html).
To upgrade your existing instance to the new minor version, see
[Upgrade the database minor version](https://berlin.devsitetest.how/sql/docs/mysql/upgrade-minor-db-version#manual-upgrade).



## March 09, 2026

**Cloud SQL for MySQL**

Feature 


You can now execute SQL statements using the [Cloud SQL Data API](https://berlin.devsitetest.how/sql/docs/mysql/executesql-instance) for
administrative queries.


**Cloud SQL for PostgreSQL**

Feature 


You can now execute SQL statements using the [Cloud SQL Data API](https://berlin.devsitetest.how/sql/docs/postgres/executesql-instance) for
administrative queries.



## November 18, 2025

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL 8.4.6 is upgraded to MySQL 8.4.7.
For more information, see the [MySQL 8.4.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-7.html).



## November 13, 2025

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL now lets you have more control over the number of results
that are returned when you perform an ANN vector search with filters.
You can use iterative filtering when the selective filters of the
`WHERE` clause in your ANN search query produce fewer results
than the number of results specified in your `LIMIT` clause.

To enable iterative filtering for your ANN search query, set the
`cloudsql_vector_iterative_filtering` flag to `ON`.
You can set the flag at a session or global level.

To enable and use iterative filtering for your ANN search query, you must have
[`[MYSQL_$VERSION].R20251004.01_07`](https://berlin.devsitetest.how/sql/docs/mysql/maintenance-changelog/)
or later installed on your MySQL instance.

For more information, see [Search approximate nearest neighbors (ANN)](https://berlin.devsitetest.how/sql/docs/mysql/search-filter-vector-embeddings#ann).



## November 12, 2025

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL now supports minor version
[8.0.44](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-44.html).
To upgrade your existing
instance to the new version, see
[Upgrade the database minor version](https://berlin.devsitetest.how/sql/docs/mysql/upgrade-minor-db-version#manual-upgrade).



## March 03, 2025

**Cloud SQL for PostgreSQL**

Feature 


The rollout of the following minor versions, extension versions, and plugin versions is complete:

**Minor versions**

- 12.21 is upgraded to 12.22.

- 13.18 is upgraded to 13.20.

- 14.15 is upgraded to 14.17.

- 15.10 is upgraded to 15.12

- 16.6 is upgraded to 16.8.

- 17.2 is upgraded to 17.4.

**Extensions and plugins**

- PostGIS is upgraded from 3.4.3 to 3.4.4.

To use these versions of the extensions, update your instance to `[PostgreSQL version].R20250112.01_14`. 

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](/sql/docs/postgres/set-maintenance-window).



## February 26, 2025

**Cloud SQL for PostgreSQL**

Feature 


You can now include replicas when you perform an in-place major version upgrade using gcloud or the Cloud SQL Admin API. For more information, see [Upgrade the database major version in-place](/sql/docs/postgres/upgrade-major-db-version-inplace#include-replicas).



## February 11, 2025

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL vector search is now generally available. After you store vector embeddings in a table, you can perform K-nearest neighbor (KNN) searches against your vector dataset. You can also add a vector search index to perform approximate nearest neighbor (ANN) searches.

For more information, see [Vector search](/sql/docs/mysql/vector-search).



## January 14, 2025

**Cloud SQL for MySQL**

Feature 


You can now migrate data from Microsoft Azure to Cloud SQL. For more information, see [Configure Cloud SQL and the external server for replication](/sql/docs/mysql/replication/configure-replication-from-external).


**Cloud SQL for PostgreSQL**

Feature 


You can now migrate data from Microsoft Azure to Cloud SQL. For more information, see [Configure Cloud SQL and the external server for replication](/sql/docs/postgres/replication/configure-replication-from-external).



## January 13, 2025

**Cloud SQL for MySQL**

Deprecated 


As of January 13, 2025, the legacy configuration for high availability (HA) is deprecated for all Cloud SQL for MySQL instances. You can no longer create instances with the legacy HA configuration, and you can no longer enable the legacy HA configuration on existing instances. In addition, after January 13, 2025, legacy HA instances are no longer covered by the [Cloud SQL SLA](https://berlin.devsitetest.how/sql/sla).

We recommend that you update your remaining legacy HA instances as soon as possible to the current HA configuration. You can do so by following the instructions in [Update an instance from legacy to current high availability](/sql/docs/mysql/configure-legacy-ha#update-from-legacy).

Starting on May 1, 2025, Cloud SQL will begin updating any instances that use the legacy high availability configuration to use the current regional persistent disk-based high availability configuration automatically.



## December 23, 2024

**Cloud SQL for PostgreSQL**

Feature 


The rollout of the following minor versions, extension versions, and plugin versions is **complete**:

**Minor versions**

- 12.20 is upgraded to 12.21. This version restores functionality of the `ALTER {ROLE|DATABASE} SET role` command that's present in PostgreSQL version 12.22. For more information, see the [PostgreSQL 12.22 release notes](https://www.postgresql.org/docs/release/12.22/).

- 13.16 is upgraded to 13.18.

- 14.13 is upgraded to 14.15.

- 15.8 is upgraded to 15.10.

- 16.4 is upgraded to 16.6.

- 17.0 is upgraded to 17.2.

**Extension and plugin versions**

- orafce is upgraded from 4.7 to 4.73 (for PostgreSQL instances, versions 11-16).

- pgAudit is upgraded from 17beta to 17.1 (for PostgreSQL instances, version 17).

To use these versions of the extensions, update your instance to one of the following:

- `POSTGRES_17_0.R20241011.00_11` (for PostgreSQL instances, version 17)

- `[PostgreSQL version].R20240910.01_31` (for PostgreSQL instances, versions 12 to 16)

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](/sql/docs/postgres/set-maintenance-window).



## December 20, 2024

**Cloud SQL for MySQL**

Feature 


You can now enable query insights for Cloud SQL Enterprise Plus edition. When you enable query insights for Enterprise Plus, you can access additional features in query insights such as 30 days of metrics retention, granular query plan details, and a higher query length limit. 

For more information, see [Use query insights to improve query performance](/sql/docs/mysql/using-query-insights#query-insights-for-enterprise-plus). Query insights for Cloud SQL Cloud SQL Enterprise Plus edition is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).


**Cloud SQL for PostgreSQL**

Feature 


You can now enable query insights for Cloud SQL Enterprise Plus edition. When you enable query insights for Enterprise Plus, you can access additional features in query insights such as 30 days of metrics retention, granular query plan details, and a higher query length limit. 

For more information, see [Use query insights to improve query performance](/sql/docs/postgres/using-query-insights#query-insights-for-enterprise-plus). Query insights for Cloud SQL Cloud SQL Enterprise Plus edition is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).


**Cloud SQL for SQL Server**

Feature 


You can use the following observability dashboards in Cloud SQL for SQL Server to monitor, analyze, and diagnose issues with your instances, databases, and queries:

- System insights

- Query insights

Both of these dashboards are available to you in the Google Cloud Console. 
The System insights dashboard displays the metrics for the resources that your instance is using and can help you analyze the performance of your instance. For more information, see [Use system insights to improve system performance](/sql/docs/sqlserver/use-system-insights). System insights is [generally available](https://berlin.devsitetest.how/products#product-launch-stages) (GA).

The Query insights dashboard helps you detect problems with queries in your Cloud SQL databases. The dashboard also provides you with the ability to [monitor active queries](/sql/docs/sqlserver/monitor-active-queries) and view [index advisor](/sql/docs/sqlserver/index-advisor-overview) recommendations. For more information, see [Use query insights to improve query performance](/sql/docs/sqlserver/using-query-insights). Query insights for Cloud SQL for SQL Server is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).

You can enable [query insights for Cloud SQL Enterprise Plus edition](/sql/docs/sqlserver/using-query-insights#query-insights-for-enterprise-plus). When you enable query insights for Enterprise Plus, you can access additional features in query insights such as 30 days of metrics retention, granular query plan details, and a higher query length limit. The query insights for Cloud SQL Enterprise Plus edition, index advisor, and active queries features are also in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).



## December 10, 2024

**Cloud SQL for MySQL**

Change 


Cloud SQL now offers notifications for maintenance that's either started or completed. See the [Overview of maintenance on Cloud SQL instances](/sql/docs/mysql/maintenance#notifications). To find out how to sign up for notifications and check your instances for upcoming maintenance, see [Find and set maintenance windows](/sql/docs/mysql/set-maintenance-window).


**Cloud SQL for PostgreSQL**

Change 


Cloud SQL now offers notifications for maintenance that's either started or completed. See the [Overview of maintenance on Cloud SQL](/sql/docs/postgres/maintenance#notifications) instances. To find out how to sign up for notifications and check your instances for upcoming maintenance, see [Find and set maintenance windows](/sql/docs/postgres/set-maintenance-window).


**Cloud SQL for SQL Server**

Change 


Cloud SQL now offers notifications for maintenance that's either started or completed. See the [Overview of maintenance on Cloud SQL](/sql/docs/sqlserver/maintenance#notifications) instances. To find out how to sign up for notifications and check your instances for upcoming maintenance, see [Find and set maintenance windows](/sql/docs/sqlserver/set-maintenance-window).



## December 05, 2024

**Cloud SQL for MySQL**

Feature 


[Cloud SQL Enterprise Plus edition](/sql/docs/editions-intro) now supports the following regions:

- `africa-south1` (Johannesburg)

- `asia-east2` (Hong Kong)

- `europe-west10` (Berlin)



**Cloud SQL for PostgreSQL**

Feature 


[Cloud SQL Enterprise Plus edition](/sql/docs/editions-intro) now supports the following regions:

- `africa-south1` (Johannesburg)

- `asia-east2` (Hong Kong)

- `europe-west10` (Berlin)



**Cloud SQL for SQL Server**

Feature 


[Cloud SQL Enterprise Plus edition](/sql/docs/editions-intro) now supports the following regions:

- `africa-south1` (Johannesburg)

- `asia-east2` (Hong Kong)

- `europe-west10` (Berlin)




## December 04, 2024

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL now supports minor version 8.0.40. To upgrade your existing instance to the new version, see [Upgrade the database minor version](/sql/docs/mysql/upgrade-minor-db-version).



## December 03, 2024

**Cloud SQL for MySQL**

Feature 


You can now use the Network Connectivity Center hub to [propagate Private Service Connect endpoints](/sql/docs/mysql/about-private-service-connect#psc-endpoint-propagation) of Cloud SQL instances in a VPC network. All endpoints in this network become accessible transitively to other spoke VPC networks through the hub. This feature is available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).


**Cloud SQL for PostgreSQL**

Feature 


You can now use the Network Connectivity Center hub to [propagate Private Service Connect endpoints](/sql/docs/postgres/about-private-service-connect#psc-endpoint-propagation) of Cloud SQL instances in a VPC network. All endpoints in this network become accessible transitively to other spoke VPC networks through the hub. This feature is available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).


**Cloud SQL for SQL Server**

Feature 


You can now use the Network Connectivity Center hub to [propagate Private Service Connect endpoints](/sql/docs/sqlserver/about-private-service-connect#psc-endpoint-propagation) of Cloud SQL instances in a VPC network. All endpoints in this network become accessible transitively to other spoke VPC networks through the hub. This feature is available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).



## November 27, 2024

**Cloud SQL for MySQL**

Feature 


You can now create instances with both private services access and Private Service Connect enabled for them. You can also enable Private Service Connect for existing private services access instances. This feature is available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Configure both private services access and Private Service Connect](/sql/docs/mysql/configure-private-services-access-and-private-service-connect).


**Cloud SQL for PostgreSQL**

Feature 


You can now create instances with both private services access and Private Service Connect enabled for them. You can also enable Private Service Connect for existing private services access instances. This feature is available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Configure both private services access and Private Service Connect](/sql/docs/postgres/configure-private-services-access-and-private-service-connect).


**Cloud SQL for SQL Server**

Feature 


You can now create instances with both private services access and Private Service Connect enabled for them. You can also enable Private Service Connect for existing private services access instances. This feature is available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Configure both private services access and Private Service Connect](/sql/docs/sqlserver/configure-private-services-access-and-private-service-connect).



## November 21, 2024

**Cloud SQL for PostgreSQL**

Feature 


You can now set up AlloyDB clusters using a copy of your Cloud SQL for PostgreSQL backup. This feature is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Migrate from Cloud SQL for PostgreSQL to AlloyDB](/sql/docs/postgres/backup-recovery/migrate-cloud-sql-to-alloydb).



## November 20, 2024

**Cloud SQL for MySQL**

Feature 


You can now authenticate to Cloud SQL Studio by using [IAM database authentication](/sql/docs/mysql/iam-authentication#iam-db-auth).

For more information about authentication in Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](/sql/docs/mysql/manage-data-using-studio#authentication).


**Cloud SQL for PostgreSQL**

Feature 


You can now authenticate to Cloud SQL Studio by using [IAM database authentication](/sql/docs/postgres/iam-authentication#iam-db-auth).

For more information about authentication in Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](/sql/docs/postgres/manage-data-using-studio#authentication).



## November 19, 2024

**Cloud SQL for MySQL**

Feature 


For [Cloud SQL Enterprise Plus edition](/sql/docs/mysql/editions-intro) instances, advanced disaster recovery (DR) is now [generally available (GA)](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Advanced disaster recovery (DR)](/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery#advanced-dr) and [Use advanced disaster recovery (DR)](/sql/docs/mysql/use-advanced-disaster-recovery).



Feature 


The write endpoint feature is now available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages). This endpoint is a global domain name service (DNS) name. This name resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a regional failure. For more information, see [Configure private IP](/sql/docs/mysql/configure-private-ip#connect-write-endpoint).


**Cloud SQL for PostgreSQL**

Feature 


The write endpoint feature is now available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages). This endpoint is a global domain name service (DNS) name. This name resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access. 

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a regional failure. For more information, see [Configure private IP](/sql/docs/postgres/configure-private-ip#connect-write-endpoint).



Feature 


For [Cloud SQL Enterprise Plus edition](/sql/docs/postgres/editions-intro) instances, you can now use advanced disaster recovery (DR) to simplify recovery and fallback processes after you perform a cross-regional failover. With advanced DR, you can: 

- Designate a cross-region disaster recovery (DR) replica

- Perform a cross-region replica failover for disaster recovery

- Restore your original deployment by using zero-data loss switchover

You can also use switchover to simulate disaster recovery without data loss. You can use advanced DR on Cloud SQL for PostgreSQL version 12, 13, 14, 15, or 16.

For more information, see [Advanced disaster recovery (DR)](/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery#advanced-dr) and [Use advanced disaster recovery (DR)](/sql/docs/postgres/use-advanced-disaster-recovery). This feature is [generally available](https://berlin.devsitetest.how/products#product-launch-stages) (GA).



## November 18, 2024

**Cloud SQL for MySQL**

Feature 


Cloud SQL now supports near-zero downtime for infrequent scale downs (once every three hours) of the compute size (vCPU, memory) of your Cloud SQL Enterprise Plus edition primary instance.

For more information, see [Availability in Cloud SQL](/sql/docs/mysql/availability#planned_operations_with_near-zero_downtime).



Feature 


Cloud SQL now supports near-zero downtime when you enable or disable [data cache](/sql/docs/mysql/data-cache) for Cloud SQL Enterprise Plus edition primary instances. For more information, see [Availability in Cloud SQL](/sql/docs/mysql/availability#planned_operations_with_near-zero_downtime).



Feature 


Support for the [`northamerica-south1`](/sql/docs/mysql/locations) (Mexico) region.


**Cloud SQL for PostgreSQL**

Feature 


The `pgvector` extension is now upgraded from version 0.7.4 to version 0.8.0. Use this extension to store and search for vector embeddings in PostgreSQL databases. For more information, see [Configure PostgreSQL extensions](https://berlin.devsitetest.how/sql/docs/postgres/extensions). 

To use this version of the extension, update your instance to one of the following:

- `POSTGRES_17_0.R20241011.00_03` (for PostgreSQL instances, version 17)

- `[PostgreSQL version].R20240910.01_17` (for PostgreSQL instances, versions 13 to 16)

For more information, see [Self-service maintenance](/sql/docs/postgres/self-service-maintenance).



Feature 


Cloud SQL now supports near-zero downtime for infrequent scale downs (once every three hours) of the compute size (vCPU, memory) of your Cloud SQL Enterprise Plus edition primary instance.

For more information, see [Availability in Cloud SQL](/sql/docs/postgres/availability#planned_operations_with_near-zero_downtime).



Feature 


Cloud SQL now supports near-zero downtime when you enable or disable [data cache](/sql/docs/postgres/data-cache) for Cloud SQL Enterprise Plus edition primary instances. For more information, see [Availability in Cloud SQL](/sql/docs/postgres/availability#planned_operations_with_near-zero_downtime).



Feature 


Support for the [northamerica-south1](/sql/docs/postgres/locations) (Mexico) region.


**Cloud SQL for SQL Server**

Feature 


Support for the [`northamerica-south1`](/sql/docs/sqlserver/locations) (Mexico) region.



## November 15, 2024

**Cloud SQL for PostgreSQL**

Feature 


You can now register an AI model endpoint, generate vector embeddings, and invoke predictions by using model endpoint management in Cloud SQL. For more information, see [Register and call remote AI models in Cloud SQL overview](/sql/docs/postgres/model-endpoint-overview).



## November 14, 2024

**Cloud SQL for MySQL**

Feature 


You can now create custom organization policies for the [`BackupRun`](/sql/docs/mysql/admin-api/rest/v1/backupRuns) resource in Cloud SQL instances. In addition, more fields in the [`Instances`](/sql/docs/mysql/admin-api/rest/v1/instances) resource are available to create custom organization policies. For more information, see [Add custom organization policies](/sql/docs/mysql/org-policy/custom-org-policy).


**Cloud SQL for PostgreSQL**

Feature 


You can now create custom organization policies for the [`BackupRun`](/sql/docs/postgres/admin-api/rest/v1/backupRuns) resource in Cloud SQL instances. In addition, more fields in the [`Instances`](/sql/docs/postgres/admin-api/rest/v1/instances) resource are available to create custom organization policies. For more information, see [Add custom organization policies](/sql/docs/postgres/org-policy/custom-org-policy).


**Cloud SQL for SQL Server**

Feature 


You can now create custom organization policies for the [`BackupRun`](/sql/docs/sqlserver/admin-api/rest/v1/backupRuns) resource in Cloud SQL instances. In addition, more fields in the [`Instances`](/sql/docs/sqlserver/admin-api/rest/v1/instances) resource are available to create custom organization policies. For more information, see [Add custom organization policies](/sql/docs/sqlserver/org-policy/custom-org-policy).



## November 12, 2024

**Cloud SQL for MySQL**

Feature 


You can now have Cloud SQL create a Private Service Connect endpoint automatically instead of creating the endpoint manually after the instance is created. You use this endpoint to access a Cloud SQL instance through a VPC network. For more information, see [Connect to an instance using Private Service Connect](/sql/docs/mysql/configure-private-service-connect#create-endpoint-automatically). This feature is available in [Preview](https://berlin.devsitetest.how/products?e=48754805#product-launch-stages).


**Cloud SQL for PostgreSQL**

Feature 


You can now have Cloud SQL create a Private Service Connect endpoint automatically instead of creating the endpoint manually after the instance is created. You use this endpoint to access a Cloud SQL instance through a VPC network. For more information, see [Connect to an instance using Private Service Connect](/sql/docs/postgres/configure-private-service-connect#create-endpoint-automatically). This feature is available in [Preview](https://berlin.devsitetest.how/products?e=48754805#product-launch-stages).


**Cloud SQL for SQL Server**

Feature 


You can now have Cloud SQL create a Private Service Connect endpoint automatically instead of creating the endpoint manually after the instance is created. You use this endpoint to access a Cloud SQL instance through a VPC network. For more information, see [Connect to an instance using Private Service Connect](/sql/docs/sqlserver/configure-private-service-connect#create-endpoint-automatically). This feature is available in [Preview](https://berlin.devsitetest.how/products?e=48754805#product-launch-stages).



## November 04, 2024

**Cloud SQL for MySQL**

Feature 


You can now [view the size of a backup](/sql/docs/mysql/backup-recovery/backing-up#view-backup-size) for a Cloud SQL instance.


**Cloud SQL for PostgreSQL**

Feature 


You can now [view the size of a backup](/sql/docs/postgres/backup-recovery/backing-up#view-backup-size) for a Cloud SQL instance.


**Cloud SQL for SQL Server**

Feature 


You can now [view the size of a backup](/sql/docs/sqlserver/backup-recovery/backing-up#view-backup-size) for a Cloud SQL instance.



## October 25, 2024

**Cloud SQL for MySQL**

Feature 


When you run the [`backupRuns.GET` API](/sql/docs/mysql/admin-api/rest/v1/backupRuns/get) or the [`gcloud sql backups describe`](/sdk/gcloud/reference/sql/backups/describe) command, the `maxChargeableBytes` parameter now appears in the response. This parameter contains the maximum number of bytes that you can be charged for a backup.


**Cloud SQL for PostgreSQL**

Feature 


When you run the [`backupRuns.GET` API](/sql/docs/postgres/admin-api/rest/v1/backupRuns/get) or the [`gcloud sql backups describe`](/sdk/gcloud/reference/sql/backups/describe) command, the `maxChargeableBytes` parameter now appears in the response. This parameter contains the maximum number of bytes that you can be charged for a backup.


**Cloud SQL for SQL Server**

Feature 


When you run the [`backupRuns.GET` API](/sql/docs/sqlserver/admin-api/rest/v1/backupRuns/get) or the [`gcloud sql backups describe`](/sdk/gcloud/reference/sql/backups/describe) command, the `maxChargeableBytes` parameter now appears in the response. This parameter contains the maximum number of bytes that you can be charged for a backup.



## October 23, 2024

**Cloud SQL for PostgreSQL**

Feature 


PostgreSQL version 17 is now [generally available](https://berlin.devsitetest.how/products#product-launch-stages).

When using the CLI/API to create an instance, if the database version for the instance or replica that you're creating is PostgreSQL 16 and later, then the default Cloud SQL edition is Enterprise Plus.

When using the CLI/API to create an instance, If you either don't specify a database version or you specify a version other than PostgreSQL 16 and later, then the default Cloud SQL edition is Enterprise.

The following information applies to **flags** and **extensions** for PostgreSQL 17:

**Flags**

These flags are deprecated for PostgreSQL 17:

- old_snapshot_threshold

- trace_recovery_messages

For more information, see [Configure database flags](/sql/docs/postgres/flags).

**Extensions**

Cloud SQL for PostgreSQL version 17 doesn't support these extensions:

- ip4r 

- oracle_fdw 

- orafce

- pg_background 

- pg_bigm 

- pgfincore 

- pg_hint_plan 

- pg_partman 

- pg_proctab

- pgrouting 

- pg_similarity 

- pg_squeeze

- pgtap 

- pgtt 

- pg_wait_sampling

- PL/Proxy 

- plv8 

- postgresql_anonymizer 

- postgresql_hll

- prefix

- rdkit 

- temporal_tables

To start using PostgreSQL 17, see [Create instances](/sql/docs/postgres/create-instance).



## October 21, 2024

**Cloud SQL for MySQL**

Feature 


You can now create a read replica for an instance that has [private services access](/sql/docs/mysql/configure-private-services-access#configure-access) configured for it and [connector enforcement](/sql/docs/mysql/admin-api/rest/v1/instances#ConnectorEnforcement) enabled for it. For more information, see [Connect using Cloud SQL Language Connectors](/sql/docs/mysql/connect-connectors#enforce).


**Cloud SQL for PostgreSQL**

Feature 


You can now create a read replica for an instance that has [private services access](/sql/docs/postgres/configure-private-services-access#configure-access) configured for it and [connector enforcement](/sql/docs/postgres/admin-api/rest/v1/instances#ConnectorEnforcement) enabled for it. For more information, see [Connect using Cloud SQL Language Connectors](/sql/docs/postgres/connect-connectors#enforce).


**Cloud SQL for SQL Server**

Feature 


You can now create a read replica for an instance that has [private services access](/sql/docs/sqlserver/configure-private-services-access#configure-access) configured for it and [connector enforcement](/sql/docs/sqlserver/admin-api/rest/v1/instances#ConnectorEnforcement) enabled for it. For more information, see [Connect using Cloud SQL Language Connectors](/sql/docs/sqlserver/connect-connectors#enforce).



## October 16, 2024

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL now supports minor version 8.0.39. To upgrade your existing MySQL 8.0 instance to the new version, see [Upgrade the database minor version](/sql/docs/mysql/upgrade-minor-db-version).



## October 09, 2024

**Cloud SQL for SQL Server**

Feature 


You can [export the transaction logs](/sql/docs/sqlserver/import-export/import-export-bak) for point-in-time recovery (PITR) that Cloud SQL stores in Cloud Storage. This feature is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).



Feature 


Cloud SQL configures the `max server memory (mb)` flag based on the instance size automatically by limiting the amount of memory that SQL Server can allocate for its internal pools. For more information, see [Configure database flags](/sql/docs/sqlserver/flags).



## October 03, 2024

**Cloud SQL for MySQL**

Feature 


You can now configure server certificate authority (CA) mode when you create a Cloud SQL instance. With server CA mode, you have two options:

- **Per-instance CA**: this is the default configuration. With this option, an internal CA dedicated to each Cloud SQL instance signs the 
server certificate for that instance.

- **Shared CA**: with this option, the Cloud SQL instance uses a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service). The subordinate server CAs in a region sign the server certificates and are shared across instances in the region. This option can be used only with MySQL 8.0.30 and later.

For more information about each option, see [Certificate authority (CA) hierarchies](/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies). This feature is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).


**Cloud SQL for PostgreSQL**

Feature 


You can now configure server certificate authority (CA) mode when you create a Cloud SQL instance. With server CA mode, you have two options:

- **Per-instance CA**: this is the default configuration. With this option, an internal CA dedicated to each Cloud SQL instance signs the 
server certificate for that instance.

- **Shared CA**: with this option, the Cloud SQL instance uses a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service). The subordinate server CAs in a region sign the server certificates and are shared across instances in the region. 

For more information about each option, see [Certificate authority (CA) hierarchies](/sql/docs/postgres/authorize-ssl#certificate_authority_ca_hierarchies). This feature is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).



Feature 


The `pg_ivm` extension, version 1.9, is generally available. This extension enables you to make materialized views up-to-date in which only incremental changes are computed and applied on views rather than recomputing the contents from scratch. 

Cloud SQL for PostgreSQL, version 16, now supports the `pgRouting` extension. This extension extends PostGIS and enhances geospatial processing through network routing and analysis.

For more information on these extensions, see [Configure PostgreSQL extensions](/sql/docs/postgres/extensions).

The rollout of the following minor versions, extension versions, and plugin versions is **underway**:

**Minor versions**

- 12.19 is upgraded to 12.20.

- 13.15 is upgraded to 13.16.

- 14.12 is upgraded to 14.13.

- 15.7 is upgraded to 15.8.

- 16.3 is upgraded to 16.4.

**Extension and plugin versions**

- google_ml_integration is upgraded from 1.2 to 1.4.2.

- pgvector is upgraded from 0.7.0 to 0.7.4.

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

The new maintenance version is `[PostgreSQL version].R20240910.01.00_02`. To learn how to check your maintenance version, see [Self service maintenance](/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](/sql/docs/postgres/set-maintenance-window).


**Cloud SQL for SQL Server**

Feature 


You can now configure server certificate authority (CA) mode when you create a Cloud SQL instance. With server CA mode, you have two options:

- **Per-instance CA**: this is the default configuration. With this option, an internal CA dedicated to each Cloud SQL instance signs the 
server certificate for that instance.

- **Shared CA**: with this option, the Cloud SQL instance uses a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service). The subordinate server CAs in a region sign the server certificates and are shared across instances in the region.

For more information about each option, see [Certificate authority (CA) hierarchies](/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies). This feature is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages).



## October 01, 2024

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL 8.4 is now generally available. For more information about the differences between MySQL 8.4 and MySQL 8.0, review [What Is New in MySQL 8.4 since MySQL 8.0](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html).

By default, if you specify MySQL 8.4 as the version when you create a Cloud SQL instance (either primary or replica) using the gcloud CLI or the REST API, then the Cloud SQL edition is Enterprise Plus.

If you specify a version other than MySQL 8.4 or don't specify a version, then the default Cloud SQL edition of the instance is Enterprise.

For more information about the implementation of MySQL 8.4 in Cloud SQL, see the following topics:

- [MySQL 8.4 authentication plugin default](/sql/docs/mysql/features#mysql84-auth-plugin-default)

- [MySQL features unsupported for Cloud SQL](/sql/docs/mysql/features#unsupported-mysql-features)

- [MySQL 8.4 user privileges (cloudsqlsuperuser)](/sql/docs/mysql/users#cloudsqlsuperuser-84)

To create a MySQL 8.4 instance in Cloud SQL, see [Create instances](/sql/docs/mysql/create-instance). 
Before you upgrade to MySQL 8.4, you must first upgrade to MySQL 8.0.37 or later. To perform a major version upgrade, see [Upgrade the database major version in-place](/sql/docs/mysql/upgrade-major-db-version-inplace). To perform a minor version upgrade of Cloud SQL for MySQL 8.0, see [Upgrade the database minor version](/sql/docs/mysql/upgrade-minor-db-version).


**Cloud SQL for SQL Server**

Feature 


You can now use the `gcloud sql instances patch` command to update the time zone of your Cloud SQL for SQL Server instance after you create the instance. Previously, you could only set a custom time zone for a SQL Server instance when you first created the instance. For more information about setting the time zone for a Cloud SQL for SQL Server instance, see [About instance settings](/sql/docs/sqlserver/instance-settings#timezone).



## September 25, 2024

**Cloud SQL for PostgreSQL**

Feature 


You can now set up AlloyDB free trial clusters using a copy of your Cloud SQL for PostgreSQL backup. For more information, see [Migrate from Cloud SQL for PostgreSQL to AlloyDB](/sql/docs/postgres/backup-recovery/migrate-cloud-sql-to-alloydb).



## September 19, 2024

**Cloud SQL for PostgreSQL**

Feature 


You can now use gcloud or the Cloud SQL Admin API to switch the storage location of the transaction logs used for point-in-time recovery on your instance without downtime to Cloud Storage. For more information, see [Use point-in-time recovery](/sql/docs/postgres/backup-recovery/pitr) and [Switch transaction log storage to Cloud Storage](/sql/docs/postgres/backup-recovery/pitr#switch-to-gcs).



## September 16, 2024

**Cloud SQL for MySQL**

Deprecated 


Cloud SQL is discontinuing support for [legacy high availability (HA)](https://berlin.devsitetest.how/sql/docs/mysql/configure-legacy-ha) instance configuration on January 6, 2025. After this date, you can't create Cloud SQL for MySQL instances with the legacy configuration for high availability. You also can't enable the legacy configuration for high availability on existing instances. Until January 6, 2025, legacy HA instances are still covered by the [Cloud SQL SLA](https://berlin.devsitetest.how/sql/sla). We recommend that you [upgrade your existing legacy HA instances](/sql/docs/mysql/configure-legacy-ha#update-from-legacy) to regional persistent disk HA instances as soon as possible and create new HA instances using regional persistent disk instead.

Starting on May 1, 2025, Cloud SQL will migrate any remaining instances that use the legacy HA configuration to the current HA configuration automatically.



## September 13, 2024

**Cloud SQL for SQL Server**

Feature 


For Cloud SQL Enterprise Plus edition, you can set the number of days of retained transaction logs from 1 to 35. For more information, see [Use point-in-time recovery (PITR)](/sql/docs/sqlserver/backup-recovery/pitr).



## September 12, 2024

**Cloud SQL for MySQL**

Feature 


Cloud SQL now supports near-zero downtime planned maintenance on standalone Cloud SQL Enterprise Plus edition primary instances. In addition, you can also simulate near-zero downtime for planned maintenance events on standalone Cloud SQL Enterprise Plus edition primary instances.

For more information, see [About maintenance on Cloud SQL instances](/sql/docs/mysql/maintenance).



Feature 


You can now upgrade the minor version of a Cloud SQL for MySQL Enterprise Plus edition instance with near-zero downtime. To upgrade the minor version of your Cloud SQL for MySQL 8.0 instance, see [Upgrade the minor version](/sql/docs/mysql/upgrade-minor-db-version).



Feature 


You can now provide access to Cloud SQL Studio by granting a new IAM role, Cloud SQL Studio User (`roles/cloudsql.studioUser`), instead of using the Cloud SQL Admin IAM role.

For more information about using Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](/sql/docs/mysql/manage-data-using-studio).



Feature 


You can now upgrade your instances to Cloud SQL Enterprise Plus edition with near-zero downtime. To upgrade your instance, see [Upgrade an instance to Cloud SQL Enterprise Plus edition using in-place upgrade](/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).


**Cloud SQL for PostgreSQL**

Feature 


You can now upgrade your instances to Cloud SQL Enterprise Plus edition with near-zero downtime. To upgrade your instance, see [Upgrade an instance to Cloud SQL Enterprise Plus edition using in-place upgrade](/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).



Feature 


You can now provide access to Cloud SQL Studio by granting a new IAM role, Cloud SQL Studio User (`roles/cloudsql.studioUser`), instead of using the Cloud SQL Admin IAM role.

For more information about using Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](/sql/docs/postgres/manage-data-using-studio).



Feature 


Cloud SQL now supports near-zero downtime planned maintenance on standalone Cloud SQL Enterprise Plus edition primary instances. In addition, you can also simulate near-zero downtime for planned maintenance events on standalone Cloud SQL Enterprise Plus edition primary instances.

For more information, see [About maintenance on Cloud SQL instances](/sql/docs/postgres/maintenance).


**Cloud SQL for SQL Server**

Feature 


You can now provide access to Cloud SQL Studio by granting a new IAM role, Cloud SQL Studio User (`roles/cloudsql.studioUser`), instead of using the Cloud SQL Admin IAM role.

For more information about using Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](/sql/docs/sqlserver/manage-data-using-studio).



## September 03, 2024

**Cloud SQL for MySQL**

Feature 


When you clone your zonal instance, you can now specify a preferred zone for the instance. You can also specify preferred primary and secondary zones for your regional instance. If the zones for your instance go down in the future, then Cloud SQL can assign the preferred zones to the instance, and you don't experience downtime. For more information, see [Clone instances](/sql/docs/mysql/clone-instance).


**Cloud SQL for PostgreSQL**

Feature 


You can now use point-in-time recovery to restore your zonal instance to a preferred primary zone and your regional instance to both a preferred primary zone and a preferred secondary zone. For more information, see [Use point-in-time recovery (PITR)](/sql/docs/postgres/backup-recovery/pitr).

When you clone your zonal instance, you can now specify a preferred zone for the instance. You can also specify preferred primary and secondary zones for your regional instance. If the zones for your instance go down in the future, then Cloud SQL can assign the preferred zones to the instance, and you don't experience downtime. For more information, see [Clone instances](/sql/docs/postgres/clone-instance).


**Cloud SQL for SQL Server**

Feature 


When you clone your zonal instance, you can now specify a preferred zone for the instance. You can also specify preferred primary and secondary zones for your regional instance. If the zones for your instance go down in the future, then Cloud SQL can assign the preferred zones to the instance, and you don't experience downtime. For more information, see [Clone instances](/sql/docs/sqlserver/clone-instance).



## August 15, 2024

**Cloud SQL for MySQL**

Announcement 


Extended support pricing is now available for Cloud SQL for MySQL. To view pricing details, see [Cloud SQL pricing](https://berlin.devsitetest.how/sql/pricing#extended-support-pricing).

For more information about extended support, see [Extended support for Cloud SQL](/sql/docs/mysql/extended-support). 

For more information about extended support timelines, see [Database versions and version policies](/sql/docs/mysql/db-versions).


**Cloud SQL for PostgreSQL**

Announcement 


Extended support pricing is now available for Cloud SQL for PostgreSQL. To view pricing details, see [Cloud SQL pricing](https://berlin.devsitetest.how/sql/pricing#extended-support-pricing).

For more information about extended support, see [Extended support for Cloud SQL](/sql/docs/postgres/extended-support).

For more information about extended support timelines, see [Database versions and version policies](/sql/docs/postgres/db-versions).



Change 


If your Cloud SQL Enterprise edition instance stores the transaction logs used for point-in-time recovery (PITR) on disk, then when you do an in-place upgrade to Cloud SQL Enterprise Plus edition the storage location for the transaction logs is switched to Cloud Storage. For more information, see [Upgrade an instance to Cloud SQL Enterprise Plus edition by using in-place upgrade](/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

To check where your instance stores the transaction logs used for PITR, see [Use point-in-time recovery (PITR)](/sql/docs/postgres/backup-recovery/pitr#check-log-storage-location).



## August 01, 2024

**Cloud SQL for SQL Server**

Feature 


Cloud SQL for SQL Server now offers two editions of Cloud SQL to support your various business and application needs: **Cloud SQL Enterprise Plus edition** and **Cloud SQL Enterprise edition**. Each edition provides different performance and availability characteristics to meet the needs of your applications.

Cloud SQL Enterprise Plus edition has new machines for better performance, higher availability, and advanced disaster recovery. Existing instances become Cloud SQL Enterprise edition for SQL Server instances with no changes to pricing or features. You can upgrade existing instances to the Cloud SQL Enterprise Plus edition in-place using the Google Cloud Console, the gcloud CLI, or the API with minimal downtime.

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](/sql/docs/editions-intro).



## July 31, 2024

**Cloud SQL for MySQL**

Feature 


Gemini in Databases assistance in Cloud SQL for MySQL is now available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages) for query insights, system insights, index advisor, and active queries. You can use Gemini assistance to help you observe and troubleshoot your Cloud SQL resources. For more information, see [Observe and troubleshoot with Gemini assistance](/sql/docs/mysql/observe-troubleshoot-with-gemini).


**Cloud SQL for PostgreSQL**

Feature 


Gemini in Databases assistance in Cloud SQL for PostgreSQL is now available in [Preview](https://berlin.devsitetest.how/products#product-launch-stages) for query insights, system insights, index advisor, and active queries. You can use Gemini assistance to help you observe and troubleshoot your Cloud SQL resources. For more information, see [Observe and troubleshoot with Gemini assistance](/sql/docs/postgres/observe-troubleshoot-with-gemini).



## July 30, 2024

**Cloud SQL for MySQL**

Feature 


You can now use the gcloud CLI or the Cloud SQL Admin API to switch the storage location of transaction logs used for point-in-time recovery (PITR) on your instance from disk to Cloud Storage. For more information, see [Use point-in-time recovery](/sql/docs/mysql/backup-recovery/pitr) and [Switch transaction log storage to Cloud Storage](/sql/docs/mysql/backup-recovery/pitr#switch-to-gcs).



## July 29, 2024

**Cloud SQL for MySQL**

Feature 


Migrating your external MySQL 5.7 and 8.0 databases into Cloud SQL for MySQL by using Percona XtraBackup physical files is now [generally available](https://berlin.devsitetest.how/products#product-launch-stages) (GA).

For more information, see [Migrate to Cloud SQL from an XtraBackup physical file](/sql/docs/mysql/migrate-xtrabackup-physical-file).



## July 26, 2024

**Cloud SQL for MySQL**

Feature 


[IAM group authentication](/sql/docs/mysql/iam-authentication#iam-group-auth) is now generally available (GA) for Cloud SQL for MySQL. You can [add IAM groups to Cloud SQL instances](/sql/docs/mysql/add-manage-iam-users#add-iam-group-db) and manage database access at the group level. To use IAM group authentication, you must have `[MySQL version].R20230909.02_00` or later installed on your instance.


**Cloud SQL for PostgreSQL**

Feature 


[IAM group authentication](/sql/docs/postgres/iam-authentication#iam-group-auth) is now generally available (GA) for Cloud SQL for PostgreSQL. You can [add IAM groups to Cloud SQL instances](/sql/docs/postgres/add-manage-iam-users#add-iam-group-db) and manage database access at the group level. To use IAM group authentication, you must have `[PostgreSQL version].R20240514.00_04` or later installed on your instance.



## July 25, 2024

**Cloud SQL for MySQL**

Change 


You can now upgrade the network architecture of a Cloud SQL instance that isn't enabled with [high-availability](/sql/docs/mysql/high-availability). The previous limitation on upgrading the network architecture of these instances is removed. To check whether your Cloud SQL instance has high availability enabled, see [Verify an instance's high availability configuration](/sql/docs/mysql/configure-ha#verify-ha).

For more information about upgrading your network architecture, see [Upgrade an instance to the new network architecture](/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture).


**Cloud SQL for PostgreSQL**

Change 


You can now upgrade the network architecture of a Cloud SQL instance that isn't enabled with [high-availability](/sql/docs/postgres/high-availability). The previous limitation on upgrading the network architecture of these instances is removed. To check whether your Cloud SQL instance has high availability enabled, see [Verify an instance's high availability configuration](/sql/docs/postgres/configure-ha#verify-ha).

For more information about upgrading your network architecture, see [Upgrade an instance to the new network architecture](/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture).


**Cloud SQL for SQL Server**

Change 


You can now upgrade the network architecture of a Cloud SQL instance that isn't enabled with [high-availability](/sql/docs/sqlserver/high-availability). The previous limitation on upgrading the network architecture of these instances is removed. To check whether your Cloud SQL instance has high availability enabled, see [Verify an instance's high availability configuration](/sql/docs/sqlserver/configure-ha#verify-ha).

For more information about upgrading your network architecture, see [Upgrade an instance to the new network architecture](/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture).



## July 19, 2024

**Cloud SQL for SQL Server**

Feature 


You can now use [Extended Events (XEvents)](/sql/docs/sqlserver/extended-events) on your Cloud SQL for SQL Server instance to monitor, identify, and troubleshoot the performance of the databases on your instance.



## July 18, 2024

**Cloud SQL for MySQL**

Feature 


You can now create custom organization policies for Cloud SQL instances. For more information, see [Add custom organization policies](/sql/docs/mysql/org-policy/custom-org-policy).


**Cloud SQL for PostgreSQL**

Feature 


You can now create custom organization policies for Cloud SQL instances. For more information, see [Add custom organization policies](/sql/docs/postgres/org-policy/custom-org-policy).


**Cloud SQL for SQL Server**

Feature 


You can now create custom organization policies for Cloud SQL instances. For more information, see [Add custom organization policies](/sql/docs/sqlserver/org-policy/custom-org-policy).



## July 17, 2024

**Cloud SQL for PostgreSQL**

Feature 


You can now use the following optional flags when you export and import files into Cloud SQL instances:

- `--clean`: if you export files, then this flag enables you to include the `DROP ` SQL statement that's required to drop (clean) database objects before you import them. If you import files, then this flag enables you to clean database objects before you recreate them. 

- `--if-exists`: this flag enables you to include the `IF EXISTS` SQL statement with each `DROP` statement that's produced by the `clean` flag.

If you import files, then these flags apply only if you use the `--parallel` flag. If you export files, then use these flags only if you're not [exporting files in parallel](/sql/docs/postgres/import-export/import-export-parallel).



## July 16, 2024

**Cloud SQL for MySQL**

Feature 


Cloud SQL Studio is now [generally available](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Manage your data using Cloud SQL Studio](/sql/docs/mysql/manage-data-using-studio).



Feature 


You can now search for and manage your Cloud SQL resources by using [Dataplex Catalog](/dataplex/docs/catalog-overview). For more information about the integration of Cloud SQL and Dataplex Catalog, see [Manage your Cloud SQL resources using Dataplex Catalog](/sql/docs/mysql/dataplex-catalog-integration).


**Cloud SQL for PostgreSQL**

Feature 


Cloud SQL Studio is now [generally available](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Manage your data using Cloud SQL Studio](/sql/docs/postgres/manage-data-using-studio).



Feature 


You can now search for and manage your Cloud SQL resources by using [Dataplex Catalog](/dataplex/docs/catalog-overview). For more information about the integration of Cloud SQL and Dataplex Catalog, see [Manage your Cloud SQL resources using Dataplex Catalog](/sql/docs/postgres/dataplex-catalog-integration).


**Cloud SQL for SQL Server**

Feature 


Cloud SQL Studio is now [generally available](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Manage your data using Cloud SQL Studio](/sql/docs/sqlserver/manage-data-using-studio).



Feature 


You can now search for and manage your Cloud SQL resources by using [Dataplex Catalog](/dataplex/docs/catalog-overview). For more information about the integration of Cloud SQL and Dataplex Catalog, see [Manage your Cloud SQL resources using Dataplex Catalog](/sql/docs/sqlserver/dataplex-catalog-integration).



## July 02, 2024

**Cloud SQL for MySQL**

Feature 


[Cloud SQL Enterprise Plus edition](/sql/docs/editions-intro) now supports the southamerica-west1 (Santiago) region.


**Cloud SQL for PostgreSQL**

Feature 


[Cloud SQL Enterprise Plus edition](/sql/docs/editions-intro) now supports the southamerica-west1 (Santiago) region.