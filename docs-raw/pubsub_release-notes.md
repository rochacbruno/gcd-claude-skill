# Pub/Sub release notes

Source: https://berlin.devsitetest.how/pubsub/docs/release-notes
Last updated: 2026-07-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/pubsub/docs/tpc-differences) for more details.














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

Pub/Sub

](https://berlin.devsitetest.how/pubsub/docs)






- 








[

Resources

](https://berlin.devsitetest.how/pubsub/docs/resources)












# Pub/ Sub release notes 






- On this page 
- [ November 18, 2024 ](#November_18_2024)
- [ November 06, 2024 ](#November_06_2024)
- [ August 20, 2024 ](#August_20_2024)
- 













This page contains production updates and feature announcements for the
Pub/Sub service. For language-specific
updates about Pub/Sub
[ Client Library](/pubsub/docs/reference/libraries) releases,
use the following links:
[C#](https://github.com/googleapis/google-cloud-dotnet/releases),
[Go](https://github.com/googleapis/google-cloud-go/releases),
[Java](https://github.com/googleapis/java-pubsub/releases),
[Node.js](https://github.com/googleapis/nodejs-pubsub/releases),
[PHP](https://github.com/googleapis/google-cloud-php/releases),
[Python](https://github.com/googleapis/python-pubsub/releases),
and
[Ruby](https://github.com/googleapis/google-cloud-ruby/releases).







You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/pubsub-release-notes.xml) directly.









## November 18, 2024 


Feature 


Pub/Sub is now available in the `northamerica-south1` region (Querétaro, Mexico, North America). For more information, see [Cloud locations](https://berlin.devsitetest.how/about/locations).



## November 06, 2024


Feature 


General availability: You can now create Cloud Storage import topics in Pub/Sub that lets you ingest data from Cloud Storage into Pub/Sub. The change is being rolled out in a phased manner over the rest of the week. For more information about Cloud Storage import topics, see [Create a Cloud Storage import topic ](/pubsub/docs/create-cloud-storage-import-topic).



## August 20, 2024


Feature 


BigQuery subscriptions with `use table schema` enabled now support type conversions for `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `NUMERIC`, and `BIGNUMERIC` data types. For more information about these conversions, see the [Use table schema documentation](/pubsub/docs/subscription-properties#use-table-schema).



Feature 


Pub/Sub has increased the limit on schema definition size to 300 KB. For more information, see [Resource limits](/pubsub/quotas#resource_limits).