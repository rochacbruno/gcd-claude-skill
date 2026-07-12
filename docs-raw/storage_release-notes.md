# Cloud Storage release notes

Source: https://berlin.devsitetest.how/storage/docs/release-notes
Last updated: 2026-07-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/storage/docs/tpc-differences) for more details.














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

Cloud Storage

](https://berlin.devsitetest.how/storage/docs)






- 








[

Resources

](https://berlin.devsitetest.how/storage/docs/resources)












# Cloud Storage release notes 






- On this page 
- [ June 17, 2026 ](#June_17_2026)
- [ May 28, 2026 ](#May_28_2026)
- [ April 20, 2026 ](#April_20_2026)
- [ April 08, 2026 ](#April_08_2026)
- [ April 06, 2026 ](#April_06_2026)
- [ April 02, 2026 ](#April_02_2026)
- [ March 12, 2026 ](#March_12_2026)
- [ January 30, 2026 ](#January_30_2026)
- [ January 28, 2026 ](#January_28_2026)
- [ January 21, 2026 ](#January_21_2026)
- [ January 16, 2026 ](#January_16_2026)
- [ January 15, 2026 ](#January_15_2026)
- [ April 17, 2025 ](#April_17_2025)
- [ February 05, 2025 ](#February_05_2025)
- [ November 15, 2024 ](#November_15_2024)
- [ November 07, 2024 ](#November_07_2024)
- [ October 29, 2024 ](#October_29_2024)
- [ October 28, 2024 ](#October_28_2024)
- [ October 22, 2024 ](#October_22_2024)
- [ September 23, 2024 ](#September_23_2024)
- [ August 05, 2024 ](#August_05_2024)
- [ July 31, 2024 ](#July_31_2024)
- [ July 23, 2024 ](#July_23_2024)
- [ July 11, 2024 ](#July_11_2024)
- [ July 08, 2024 ](#July_08_2024)
- [ July 02, 2024 ](#July_02_2024)
- [ June 28, 2024 ](#June_28_2024)
- [ June 18, 2024 ](#June_18_2024)
- [ June 06, 2024 ](#June_06_2024)
- 













This page documents production updates to Cloud Storage. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.







You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/storage-release-notes.xml) directly.









## June 17, 2026 


Feature 


When you [create composite objects](/storage/docs/composing-objects), you can
delete the temporary source objects as part of the composition process.



## May 28, 2026


Breaking 


As of August 26, 2026, in buckets with hierarchical namespace enabled,
the [Object Lifecycle Management](/storage/docs/lifecycle) `Delete` action will
delete empty folders when the empty folder meets all of the conditions in the
lifecycle rule.



## April 20, 2026


Feature 


Cloud Storage Model Context Protocol (MCP) server is [generally
available](https://berlin.devsitetest.how/products#product-launch-stages). You can
connect to Cloud Storage from AI applications using the server. It lets AI
applications and agents create buckets, retrieve object metadata, read and write
object data, and list buckets and objects. For more information, see [Use the
Cloud Storage MCP server](/storage/docs/use-cloud-storage-mcp) and [Cloud
Storage MCP reference](/storage/docs/reference/mcp).



## April 08, 2026


Feature 


You can delete up to 1,000 objects in a single request by using the
Cloud Storage multi-object delete XML API. If you use Amazon S3-compatible tools or
libraries, you can point your request to the Cloud Storage endpoint to use this
feature with your existing workflows. For more information, see
[Delete objects](/storage/docs/deleting-objects) and
[Delete multiple objects](/storage/docs/xml-api/post-bucket).



## April 06, 2026


Feature 


You can now use [Storage batch operations](/storage/docs/batch-operations/overview)
to update [object contexts](/storage/docs/object-contexts) for multiple objects
in a single job. You can clear all existing contexts from the specified objects,
remove contexts with specific keys, or update and insert new context key-value
pairs. For more information, see
[Create and manage batch operation jobs](/storage/docs/batch-operations/create-manage-batch-operation-jobs).



Feature 


[Object contexts](/storage/docs/object-contexts) are now
[generally available](https://berlin.devsitetest.how/products#product-launch-stages).
You can attach key-value pairs to your objects to categorize, track, and search
your data. Object contexts are preserved by default during copy, rewrite, and
compose operations. You can help control this behavior by using the
[`dropContextGroups`](/storage/docs/json_api/v1/objects/copy#dropContextGroups)
JSON API parameter or by providing new contexts in the request.



## April 02, 2026


Feature 


You can configure which encryption types are allowed or prohibited for
creating new objects in a bucket. For more information, see
[Enforce or restrict the encryption types for a bucket](/storage/docs/encryption/enforce-encryption-types).



## March 12, 2026


Change 


Object uploads that use customer-managed encryption keys (CMEK) now fail if the
Cloud Storage service agent lacks the necessary IAM
role to decrypt the object. For steps to grant the required role, see
[Assign a Cloud KMS key to a service agent](/storage/docs/encryption/using-customer-managed-keys#service-agent-access).



## January 30, 2026


Announcement 


Object change notification is deprecated on January 30, 2026. To generate
notifications for changes to objects, use
[Pub/Sub notifications for Cloud Storage](https://berlin.devsitetest.how/storage/docs/migrate-to-pub-sub-notifications) instead.



## January 28, 2026


Feature 


Previously, when [listing buckets](/storage/docs/listing-buckets) by using the
client libraries, JSON API, or RPC API, the request returned an error if some
buckets couldn't be reached because a location was temporarily unavailable. You
can now use a partial success option to return a list of buckets that are
available, as well as the names of any buckets that can't be reached.



## January 21, 2026


Feature 


Bucket relocation with write downtime now supports completed multipart uploads.
If a multipart upload is started before relocation begins and is completed
before the final synchronization step, the objects are successfully relocated.
In-progress multipart uploads continue to block the final synchronization
step until they are either completed or cancelled. For more information, see
[Bucket relocation overview](/storage/docs/bucket-relocation/overview).



## January 16, 2026


Feature 


You can now use [dry run](/storage/docs/batch-operations/overview#dry-run) mode
to simulate storage batch operations jobs without modifying or deleting data.
Dry run helps you to validate your job configuration before running the actual
operation.

To learn how to configure a dry run job, see [Create and manage batch operations
jobs](/storage/docs/batch-operations/create-manage-batch-operation-jobs).



## January 15, 2026


Feature 


When you
[bulk restore soft-deleted objects](/storage/docs/use-soft-deleted-objects#bulk-restore),
you can restore objects that were live at a specific time. You can also choose
the objects to restore based on the object creation time.



## April 17, 2025


Change 


[Best practices for using Cloud Storage with media workloads](/storage/docs/best-practices-media-workload) are now available.



## February 05, 2025


Announcement 


[Announced billing changes](/resources/storage/billing-fix-bigquery) for accessing Cloud Storage through BigQuery take effect Feb 21, 2025. These changes were originally set to take effect on February 01, 2025.



## November 15, 2024


Change 


You can now use the [`x-amz-decoded-content-length` header](/storage/docs/xml-api/reference-headers#xamzdecodedcontentlength) to allow an XML API upload that uses chunked transfer encoding to include a [signature](/storage/docs/authentication/signatures) in its `Authorization` header.



## November 07, 2024


Feature 


You can now restore soft-deleted buckets. If you delete a bucket with an active soft delete policy, Cloud Storage retains the bucket for the specified soft delete retention duration, during which the bucket can be restored to a live state. To learn more about the bucket restore feature, see [Use soft-deleted buckets](/storage/docs/use-soft-deleted-buckets).



## October 29, 2024


Change 


[Data Access logs](/storage/docs/audit-logging#available-logs) are now compatible with all [authenticated browser downloads](/storage/docs/request-endpoints#cookieauth).

- When an authenticated browser download occurs outside of the Google Cloud console, a resulting Data Access log has its `principalEmail` and `callerIp` fields redacted.




## October 28, 2024


Change 


Additional functionality is now available for the [Object Retention Lock](/storage/docs/object-lock) and [Bucket Lock](/storage/docs/bucket-lock) features:

- 

You can now [enable Object Retention Lock on existing buckets using the Console](/storage/docs/using-object-lock#enable-retentions).

- 

Enabling Object Retention Lock on a bucket will cause a [lien](/resource-manager/docs/project-liens) to be placed, at best effort, on the project containing the bucket.

- 

Buckets can now have Bucket Lock and [Object Versioning](/storage/docs/object-versioning) enabled at the same time.




## October 22, 2024


Feature 


You can now emit client-side metrics for gRPC. To learn which metrics are supported and how to emit them, see [Use gRPC client-side metrics](/storage/docs/client-side-metrics).



## September 23, 2024


Feature 


You can now use [hierarchical namespace](/storage/docs/hns-overview) with Cloud Storage FUSE. To learn more about how mounting buckets with hierarchical namespace enabled can help improve performance, see [Mount buckets with hierarchical namespace enabled](/storage/docs/gcsfuse-performance#hierarchical-namespace).



## August 05, 2024


Feature 


You can now use parallel downloads with Cloud Storage FUSE to accelerate read performance of large files over 1 GB in size. When enabled, parallel downloads use multiple workers to download a file in parallel, accelerating file reads. For more information, see [Improve read performance using parallel downloads](/storage/docs/gcsfuse-performance-and-best-practices#parallel-downloads).



## July 31, 2024


Feature 


You can now use the Google Cloud console to set a default soft delete retention duration. For more information, see [Use tags to set a default soft delete retention duration for new buckets](/storage/docs/use-tags-for-soft-delete#overview).



Feature 


You can now use list caching with Cloud Storage FUSE, which is a cache for directory and file list, or `ls`, responses that improves list operation speeds. To learn more about list caching and how to enable it, see the [Cloud Storage FUSE caching overview page](/storage/docs/gcsfuse-cache#list-cache-overview).



## July 23, 2024


Feature 


You can now use tags to set a default soft delete retention duration on newly created buckets in your organization. To learn how to customize a default soft delete retention duration, see [Set a default soft delete retention duration](/storage/docs/use-tags-for-soft-delete).



## July 11, 2024


Feature 


You can now specify Frankfurt (europe-west3) and Zürich (europe-west6) as a predefined dual-region pairing. For more information, see [Predefined dual-regions](/storage/docs/locations#predefined).



## July 08, 2024


Feature 


You can now specify London (`europe-west2`) and Frankfurt (`europe-west3`) as a predefined dual-region pairing. For more information, see [Predefined dual-regions](/storage/docs/locations#predefined).



## July 02, 2024


Feature 


You can now disable soft delete for multiple buckets at a time or for all buckets in a project. To learn more, see [Bulk disable soft delete](/storage/docs/use-soft-delete#bulk-turn-off-soft-delete-policy).



## June 28, 2024


Feature 


You can now specify the Frankfurt, Germany (`europe-west3`) and Paris, France (`europe-west9`) regions when using [regional endpoints](/storage/docs/regional-endpoints).



## June 18, 2024


Feature 


Hierarchical namespace for Cloud Storage buckets is now available in [Preview](https://developers.google.com/maps/launch-stages#preview). With hierarchical namespace, you can store your data in a logical file system structure.



Issue 


[Renaming a folder](/storage/docs/rename-hns-folders) in a bucket with hierarchical namespace enabled using command line is not supported.



## June 06, 2024


Feature 


Cloud Storage now offers a new pre-defined dual region, `EUROPE-WEST2` (London) and `EUROPE-WEST1` (Belgium). To learn more about Cloud Storage pre-defined dual regions, see the [Bucket locations page](/storage/docs/locations#predefined).