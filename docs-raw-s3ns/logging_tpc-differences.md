# Logging in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/logging/docs/tpc-differences
Last updated: 2026-08-31

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

Observability

](https://documentation.s3ns.fr/docs/observability)






- 








[

Cloud Logging

](https://documentation.s3ns.fr/logging/docs)






- 








[

Guides

](https://documentation.s3ns.fr/logging/docs/overview)












# Logging in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Workflows and tools ](#workflow-differences)

- [ Related guides ](#related-guides)
- 










Cloud Logging is a real-time log-management system with storage, search,
and analysis. Cloud Logging automatically collects log data from
Cloud de Confiance by S3NS resources.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Logging.



For more detailed information about Logging, see the
[Logging overview](/logging/docs/overview) and the rest of the
Logging documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Logging and
the Google Cloud version.
Some notable differences include the following:





- Observability Analytics is unavailable.

- Visualizing and monitoring log data is unavailable.



A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Logging feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Workflows and tools



| 
**[Cloud Audit Logs](/logging/docs/audit)**
| 
Available. | 
|

| 
**[Collection of logs](/logging/docs/structured-logging)**
| 


Log data is collected from the following:




- Cloud de Confiance by S3NS resources.

- Applications instrumented to send logs to your Cloud de Confiance project by
using
[client libraries](/logging/docs/reference/libraries)
or the
[Cloud Logging API](/logging/docs/reference/api-overview).




The following are unavailable:




- Collecting log data by using the Ops Agent or the
legacy Logging agent.

- Collecting log data by using an open-source framework.


| 

|

| 
**[Configuration of default settings](/logging/docs/default-settings)**

( Applies only to organizations and folders ) | 
Available. | 
|

| 
**[Creation of log buckets](/logging/docs/buckets)**
| 


The following features are available:




- Creating, listing, modifying, and deleting log buckets.

- Create a [log bucket with CMEK enabled](/logging/docs/routing/managed-encryption-storage).

- Custom retention.




The following features are unavailable:




- Creating a log bucket that is upgraded to use Observability Analytics.

- Upgrading a log bucket to use Observability Analytics.

- Creating a linked BigQuery dataset.


| 
|

| 
**[Creation of log sinks](/logging/docs/export/configure_export_v2)**
| 


Project-level log sinks and [aggregated log sinks](/logging/docs/export/aggregated_sinks) are available.
The following sink destinations are available:




- Cloud de Confiance by S3NS project.

- Log bucket.

- Pub/Sub topic.




The following sink destinations are unavailable:




- BigQuery datasets.

- Cloud Storage buckets.


| 
|

| 
**[Creation of log scopes](/logging/docs/log-scope/create-and-manage)**
| 


The following features are unavailable:




- Configuring a log scope by using the Cloud de Confiance console.

- Setting the default log scope is unavailable.


| 
|

| 
**[Creation of log views](/logging/docs/logs-views)**
| 
Available. | 
|

| 
**Custom indexing** | 
Unavailable. | 
|

| 
**Observability Analytics** | 
Unavailable. | 
|

| 
**[Logs Explorer](/logging/docs/view/logs-explorer-interface)**
| 


Available.



When Logs Explorer is integrated with a feature that is
unavailable, the integration is disabled.

| 
|

| 
**[Log regionalization](/logging/docs/regionalized-logs)**
| 
Available. | 
|

| 
**Retroactive log export** | 
Unavailable. | 
|

| 
**Visualization and monitoring of logs** | 


The following features are unavailable:




- Displaying log entries or a summary of log data on a dashboard.

- Creating or visualizing log-based metrics.

- Creating alerting policies that monitor a log-based metric or
individual log entries.

- Streaming and tailing log entries.


| 
|





## Related guides



The following information might also affect how you use and design for Logging
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)