# Cloud SQL in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/sql/docs/tpc-differences
Last updated: 2026-07-16

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

Guides

](https://berlin.devsitetest.how/sql/docs/introduction)












# Cloud SQL in Google Cloud Dedicated versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Databases and editions ](#databases-and-editions)
- [ Hardware and OS ](#hardware-and-os-differences)
- [ Availability and disaster recovery ](#availability-differences)
- [ Security and access control ](#security-differences)
- [ Network ](#network-differences)
- [ Workflows and tools ](#workflow-differences)
- [ Insights and observability ](#observability-differences)

- [ Related guides ](#related-guides)
- 










Cloud SQL is a fully managed relational database service for MySQL, PostgreSQL,
and SQL Server. This frees you from database administration tasks so that you
have more time to manage your data.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Cloud SQL.



For more detailed information about Cloud SQL, see the
[Cloud SQL overview](/sql/docs/introduction) and the rest of the
Cloud SQL documentation.




## Key differences 



There are some differences between the Google Cloud Dedicated version of Cloud SQL and
the Google Cloud version.
Some notable differences include the following:






- Cloud SQL for SQL Server isn't available in Google Cloud Dedicated.

- Only Cloud SQL Enterprise Plus edition is available in Google Cloud Dedicated.

- Only C3 series machine types are available in Google Cloud Dedicated.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud SQL feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Databases and editions




| 
**Databases engines**
| 
Cloud SQL for SQL Server is unavailable.
| 
|

| 
**Product editions**
| 
Only Cloud SQL Enterprise Plus edition is available. Cloud SQL Enterprise edition is unavailable.
| 
|


### Hardware and OS




| 
**Machine types**
| 

Only C3 series machine types are available. You can choose from the
following machine types:



- db-perf-optimized-C-4

- db-perf-optimized-C-8

- db-perf-optimized-C-22

- db-perf-optimized-C-44

- db-perf-optimized-C-88

- db-perf-optimized-C-176


| 
|

| 
**Storage**
| 




- Google Cloud Dedicated VMs are available with
[Hyperdisk Balanced](/compute/docs/disks/hd-types/hyperdisk-balanced)
and [Hyperdisk Balanced High Availability](/compute/docs/disks/hd-types/hyperdisk-balanced-ha)
storage only.

- [Data cache](/sql/docs/mysql/data-cache) is unavailable.


| 
|


### Availability and disaster recovery




| 
**Regions and zones**
| 
Google Cloud Dedicated has only a single region,
with three zones. Multi-region features and cross-region failover are
not available. Deployment across multiple zones for resiliency is available.
| 
|


### Security and access control




| 
**IAM and permissions**
| 
Database IAM authentication is available with limitations in Google Cloud Dedicated.
Only service account IAM authentication is available in Google Cloud Dedicated.
User account and group IAM authentication is unavailable in Google Cloud Dedicated.
| 
|

| 
**Domain controllers**
| 
Managed Service for Microsoft Active Directory is unavailable in Google Cloud Dedicated.
| 
|


### Network




| 
**Connectivity**
| 




- Private Service Connect is available in Google Cloud Dedicated.

- Private Service Connect with service automation isn't available in Google Cloud Dedicated.

- Private services access is unavailable in Google Cloud Dedicated.


| 
|


### Workflows and tools




| 
**Data migration**
| 
Database Migration Service is unavailable in Google Cloud Dedicated.
Administrators should plan to manage data migrations accordingly.
| 
|

| 
**Data import and export**
| 
Serverless export operations are unavailable in Google Cloud Dedicated.
| 
|


### Insights and observability




| 
**Monitoring**
| 
Query insights for Cloud SQL Enterprise Plus edition is unavailable in Google Cloud Dedicated.
| 
|

| 
**Maintenance**
| 




- Instances that are configured with [maintenance windows](/sql/docs/mysql/set-maintenance-window)
don't receive any automatic maintenance updates in Google Cloud Dedicated.


Only instances that aren't configured with a maintenance window receive automatic maintenance updates. Without a scheduled maintenance window, this means that the automatic maintenance update can occur at any time, even during business hours.



To work around these issues, you can apply the maintenance updates manually to an instance. Use one of the following workarounds:




- [Stop and restart the instance](/sql/docs/mysql/start-stop-restart-instance).
The maintenance update is applied when the instance restarts.

- [Perform self-service maintenance](/sql/docs/mysql/self-service-maintenance)
to apply the maintenance update.



- Maintenance notifications are unavailable in Google Cloud Dedicated.

- Cloud SQL Studio is available without Gemini Code Assist in Google Cloud Dedicated.


| 
|





## Related guides



The following information might also affect how you use and design for Cloud SQL
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)