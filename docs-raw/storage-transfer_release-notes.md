# Storage Transfer Service release notes

Source: https://berlin.devsitetest.how/storage-transfer/docs/release-notes
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






- 








[

Resources

](https://berlin.devsitetest.how/storage-transfer/docs/resources)












# Storage Transfer Service release notes 



















This page documents production updates to Storage Transfer Service. We recommend
that Storage Transfer Service developers periodically check this list for any
new announcements.







You can see the latest product updates for all of Google Cloud on the
[
Google Cloud](/release-notes) page, browse and filter all release notes in the
[Google Cloud console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/storagetransfer-release-notes.xml) directly.









## December 19, 2024


Feature 


When providing a URL list to transfer files, you can now host the list itself in an access-controlled Cloud Storage bucket. See [Transfer from public URLs](/storage-transfer/docs/create-url-list) for full details.



## July 23, 2024


Security 


We've released a lighter weight (~50% reduction in image size) and more secure version of the transfer agent container image. If you're running agents that were installed on or before June 17th, 2024, we highly recommend that you delete those agents and [install new agents](/storage-transfer/docs/managing-on-prem-agents#install-agent) into your agent pool. Any existing transfers using that pool will resume once the new agents are installed.