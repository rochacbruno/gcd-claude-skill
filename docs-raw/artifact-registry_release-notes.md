# Artifact Registry release notes

Source: https://berlin.devsitetest.how/artifact-registry/docs/release-notes
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/artifact-registry/docs/tpc-differences) for more details.














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

Application development

](https://berlin.devsitetest.how/docs/application-development)






- 








[

Artifact Registry

](https://berlin.devsitetest.how/artifact-registry/docs)






- 








[

Resources

](https://berlin.devsitetest.how/artifact-registry/docs/resources)












# Artifact Registry release notes 






- On this page 
- [ March 04, 2025 ](#March_04_2025)
- [ February 19, 2025 ](#February_19_2025)
- [ October 15, 2024 ](#October_15_2024)
- [ October 03, 2024 ](#October_03_2024)
- [ August 30, 2024 ](#August_30_2024)
- [ August 21, 2024 ](#August_21_2024)
- 













This page documents production updates to Artifact Registry. Check this page for
announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.







You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/artifactregistry-release-notes.xml) directly.









## March 04, 2025 

v1 


Feature 


Artifact Registry is available in the `europe-north2` region (Stockholm). For more information, see [Global locations](https://berlin.devsitetest.how/about/locations).



## February 19, 2025

v1 


Issue 


Artifact Registry might give a 400 error on pushes or pulls for Workforce Identity Federation users. This issue is caused by Workforce Identity Federation [attribute mappings](/iam/docs/workforce-identity-federation#attribute-mappings) in the Artifact Registry URL causing problems on the backend.

To mitigate this issue, you can push or pull from Artifact Registry without attribute mappings, or reduce the length of your attribute mappings.



## October 15, 2024

v1 


Feature 


Organization policy constraints for Artifact Registry is available in **General Availability**.

For more information, see [Use custom organization policies](/artifact-registry/docs/custom-constraints).



## October 03, 2024

v1 


Feature 


Artifact Registry support for [OCI specifications v1.1](https://github.com/opencontainers/image-spec) is [generally available](https://berlin.devsitetest.how/products/#product-launch-stages) in Docker format repositories.

You can upload containerized metadata about another container image to Artifact Registry as an attachment. To learn more, see [Manage container metadata](/artifact-registry/docs/docker/manage-metadata).



## August 30, 2024

v1 


Change 


Updates to the Artifact Registry API are as follows:

- Add or update file annotations with 
[`UpdateFile()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateFile).

- Add or update package version annotations with 
[`UpdateVersion()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateVersion).

- Filter by annotation or name with
[`ListFiles()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListFiles),
[`ListPackages()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListPackages), 
and
[`ListVersions()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListVersions).

- Filter by name with [`ListTags()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListTags),
[`ListRepositories()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListRepositories)
and [`ListDockerImages()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListDockerImages).

- Order by `name`, `createTime`, or `updateTime` for
[`ListFiles()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListFiles),
[`ListVersions()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListVersions),
[`ListRepositories()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListRepositories),
and 
[`ListPackages()`](/artifact-registry/docs/reference/rpc/google.devtools.artifactregistry.v1#google.devtools.artifactregistry.v1.ArtifactRegistry.ListPackages).




## August 21, 2024

v1 


Change 


The following Artifact Registry Cloud Audit Log method names have changed:

- `Docker-EmptyTarBlob` is renamed `Docker-ServeBlob`

- `Docker-GetEmptyTags` is renamed `Docker-GetTags`

- `Docker-HeadEmptyTarBlob` is renamed `Docker-HeadBlob`

- `Kfp-UploadPackage-Redirect` is renamed `Kfp-UploadPackage`

- `Apt-ViewRemoteIndexFile` is renamed to indicate the type of file requested:

- `Apt-ViewIndexFile`: when a repository metadata file is requested

- `Apt-Contents`: when the Contents index file for a specific repository component and architecture 
type is requested

- `Apt-ViewArchIndexFile`: when the Packages index file for a specific repository component and 
architecture type is requested

- `Apt-ViewRemotePackageFile` is renamed `Apt-ViewPackageFile`

- `Yum-ViewUpstreamFile` is renamed to indicate the type of file requested:

- `Yum-ViewIndexKey`: when the public key for signing Yum packages is requested

- `Yum-ViewIndexFile`: when one of a repository's index files is requested

- `Yum-ViewPackageFile`: when a Yum package file is requested

For more information on Artifact Registry logs, see [Audit Logging](/artifact-registry/docs/audit-logging).