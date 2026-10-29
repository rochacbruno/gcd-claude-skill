# Google Cloud release notes

Source: https://berlin.devsitetest.how/release-notes
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/tpc-differences) for more details.














- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Documentation

](https://berlin.devsitetest.how/docs)












# Google Cloud release notes 



















The following release notes cover the most recent changes over the last 60 days.
For a comprehensive list of product-specific release notes, see the
[individual product release note pages](/release-notes/all).

You can also see and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes) or you
can programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).















To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/gcp-release-notes.xml) directly.











## October 27, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R46) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.4162000+preview is now available for GKE alpha clusters in the Rapid channel.

- Alpha version 1.38.0-gke.2743000+preview is no longer available in the Rapid channel.




### Regular channel




- The following versions are now available in the Regular channel:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- Version 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.




### Stable channel




- The following versions are now available in the Stable channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




### Extended channel




- The following versions are now available in the Extended channel:

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.32.13-gke.2906000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2906000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.33.13-gke.2207000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2207000)

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2759000

- 1.31.14-gke.2825000

- 1.31.14-gke.3042000

- 1.32.13-gke.2504000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2567000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2788000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1721000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1815000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.2074000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.31 to [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.32 to [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- 1.33 to [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)




### No channel (deprecated)




- The following versions are now available:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- The following node versions are now available:

- [1.32.13-gke.2906000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2906000)

- [1.33.13-gke.2207000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2207000)

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- Version 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.






Change 

#### (2026-R46) Version updates

- The following versions are now available in the Stable channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




Change 

#### (2026-R46) Version updates

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- Version 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R46) Version updates

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.4162000+preview is now available for GKE alpha clusters in the Rapid channel.

- Alpha version 1.38.0-gke.2743000+preview is no longer available in the Rapid channel.




Change 

#### (2026-R46) Version updates

- The following versions are now available:

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- The following node versions are now available:

- [1.32.13-gke.2906000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2906000)

- [1.33.13-gke.2207000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2207000)

- [1.34.12-gke.1539000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1539000)

- [1.35.9-gke.1505000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-9-gke-1505000)

- [1.36.5-gke.1982000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1982000)

- [1.37.1-gke.3020000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-3020000)

- Version 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R46) Version updates

- The following versions are now available in the Extended channel:

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.32.13-gke.2906000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2906000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.33.13-gke.2207000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2207000)

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2759000

- 1.31.14-gke.2825000

- 1.31.14-gke.3042000

- 1.32.13-gke.2504000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2567000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2788000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1721000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1815000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.2074000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1919000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.31 to [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.32 to [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- 1.33 to [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)




## October 26, 2026

**Compute Engine**

Security 


A vulnerability (CVE-2026-85299) about incorrect authorization in
Compute Engine was discovered and has been addressed. For more information,
see the
[GCP-2026-073 security bulletin](/compute/docs/security-bulletins#gcp-2026-073). 

**Google Kubernetes Engine**

Change 

#### (2026-R45) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.3229000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1153000

- 1.35.8-gke.1919000

- 1.36.4-gke.2326000

- 1.37.1-gke.1552000

- Alpha version 1.38.0-gke.2240000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.34 to [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- 1.35 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.35 to [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- 1.37 to [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)




### Regular channel




- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495002

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




### Stable channel




- Version [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001) is now the default version for cluster creation in the Stable channel.

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- The following versions are no longer available in the Stable channel:

- 1.34.11-gke.1056000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250001

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)




### Extended channel




- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.3042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-3042000)

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2963000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2701000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1952000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495002

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




### No channel (deprecated)




- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- The following node versions are now available:

- [1.31.14-gke.3042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-3042000)

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- The following versions are no longer available:

- 1.34.11-gke.1056000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)






Change 

#### (2026-R45) Version updates

- Version [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001) is now the default version for cluster creation in the Stable channel.

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- The following versions are no longer available in the Stable channel:

- 1.34.11-gke.1056000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250001

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)




Change 

#### (2026-R45) Version updates

- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495002

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




Change 

#### (2026-R45) Version updates

- Version [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.3229000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1153000

- 1.35.8-gke.1919000

- 1.36.4-gke.2326000

- 1.37.1-gke.1552000

- Alpha version 1.38.0-gke.2240000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.34 to [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- 1.35 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- 1.35 to [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- 1.36 to [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- 1.37 to [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)




Change 

#### (2026-R45) Version updates

- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- The following node versions are now available:

- [1.31.14-gke.3042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-3042000)

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.34.12-gke.1363000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1363000)

- [1.35.8-gke.2308000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-2308000)

- [1.36.5-gke.1259000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-5-gke-1259000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [1.37.1-gke.2097000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-2097000)

- The following versions are no longer available:

- 1.34.11-gke.1056000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




Change 

#### (2026-R45) Version updates

- Version [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.3042000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-3042000)

- [1.32.13-gke.2788000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2788000)

- [1.33.13-gke.2074000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-2074000)

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2963000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2701000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1952000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495002

- 1.36.4-gke.1495003 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




## October 21, 2026

**Bigtable**

Feature 


Bigtable is now available in Google Cloud. For more information, see
[Bigtable in Google Cloud versus Google Cloud](/bigtable/docs/tpc-differences).



## October 20, 2026

**Filestore**

Feature 


Filestore is available in Google Cloud. For more information, see [Filestore differences in Google Cloud versus Google Cloud](/filestore/docs/tpc-differences).



## October 19, 2026

**Google Cloud Armor**

Security 


Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-stable`
rulesets. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning).

The following rulesets have been updated:

- `sqli-v33-stable`

- `xss-v33-stable`

- `lfi-v33-stable`

- `rfi-v33-stable`

- `rce-v33-stable`

- `methodenforcement-v33-stable`

- `scannerdetection-v33-stable`

- `protocolattack-v33-stable`

- `php-v33-stable`

- `sessionfixation-v33-stable`

- `java-v33-stable`

- `nodejs-v33-stable`




Security 


Security fixes and enhancements to Cloud Armor preconfigured WAF `stable`
rulesets for v3.0. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning).

The following rulesets have been updated:

- `sqli-stable`

- `xss-stable`

- `lfi-stable`

- `rfi-stable`

- `rce-stable`

- `methodenforcement-stable`

- `scannerdetection-stable`

- `protocolattack-stable`

- `php-stable`

- `sessionfixation-stable`



**Virtual Private Cloud**

Feature 


**General Availability**: VPC Flow Logs adds the following metadata annotations
and packet drop reasons for Cloud NAT:

- Metadata annotations: `connection.nat_ip`, `connection.nat_port`, and
`nat_gateway_details`

- Drop reasons: `NAT_ENDPOINT_INDEPENDENT_CONFLICT`, `NAT_OUT_OF_CONNECTIONS`,
and `NAT_OUT_OF_PORTS`

For more information, see
[Record format](/vpc/docs/about-flow-logs-records#record_format) and
[Packet drop reasons](/vpc/docs/about-flow-logs-records#drop-reason).



## October 14, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R44) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2884000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1011000

- 1.35.8-gke.1796000

- 1.36.4-gke.2046002

- 1.36.4-gke.2202002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2304000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.37.0-gke.3503000

- Alpha version 1.38.0-gke.1002000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- 1.34 to [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- 1.35 to [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- 1.35 to [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- 1.36 to [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




### Regular channel




- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1102000

- 1.35.8-gke.1439001

- 1.36.4-gke.1391002

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.34 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)




### Stable channel




- The following versions are now available in the Stable channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- Version 1.34.9-gke.1655001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)




### Extended channel




- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.31.14-gke.2963000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2963000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2704000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2925000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2427000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2662000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1647000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1915000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1102000

- 1.35.8-gke.1439001

- 1.36.4-gke.1391002

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- 1.31 to [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- 1.32 to [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- 1.33 to [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)




### No channel (deprecated)




- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following node versions are now available:

- [1.31.14-gke.2963000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2963000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following versions are no longer available:

- 1.34.9-gke.1655001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1225000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2202002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2304000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.36 to [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)






Change 

#### (2026-R44) Version updates

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- Version 1.34.9-gke.1655001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)




Change 

#### (2026-R44) Version updates

- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1102000

- 1.35.8-gke.1439001

- 1.36.4-gke.1391002

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.34 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)




Change 

#### (2026-R44) Version updates

- Version [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- [1.37.1-gke.1697000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2884000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.12-gke.1011000

- 1.35.8-gke.1796000

- 1.36.4-gke.2046002

- 1.36.4-gke.2202002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2304000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.37.0-gke.3503000

- Alpha version 1.38.0-gke.1002000+preview is no longer available in the Rapid channel.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- 1.34 to [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- 1.35 to [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- 1.35 to [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- 1.36 to [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- 1.37 to [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)




Change 

#### (2026-R44) Version updates

- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following node versions are now available:

- [1.31.14-gke.2963000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2963000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.34.12-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)

- [1.35.8-gke.1975000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- [1.36.4-gke.2377000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)

- The following versions are no longer available:

- 1.34.9-gke.1655001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1225000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1495000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2202002 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2304000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.36 to [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)




Change 

#### (2026-R44) Version updates

- Version [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.31.14-gke.2963000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2963000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.32.13-gke.2701000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2701000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.33.13-gke.1952000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1952000)

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2046003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2704000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2925000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2427000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2662000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1647000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1915000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1102000

- 1.35.8-gke.1439001

- 1.36.4-gke.1391002

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- 1.31 to [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- 1.32 to [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- 1.33 to [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495003](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)




## October 10, 2026

**Cloud SQL for MySQL**

Change 


MySQL 8.0.46 is now the
[default minor version](/sql/docs/mysql/db-versions#database-version-support)
for Cloud SQL for MySQL 8.0.

For more information about minor version support in Cloud SQL for MySQL,
see [MySQL 8.0](/sql/docs/mysql/db-versions#mysql-8.0).



## October 08, 2026

**Cloud SQL for MySQL**

Feature 


Cloud SQL for MySQL now supports the
`innodb_cloudsql_managed_buffer_pool_tuneup_pct` database flag.

Managed buffer pool automatically adjusts the InnoDB buffer pool size to reduce
out-of-memory events. When instance memory usage remains at or below 70% for 10
minutes or longer after prior reductions, Cloud SQL increases the buffer pool
size. You can now use the `innodb_cloudsql_managed_buffer_pool_tuneup_pct` flag
to change this 70% threshold to a different percentage. Increase the threshold
to restore the InnoDB buffer pool size when baseline usage exceeds 70%, or
decrease it to preserve additional RAM allocation for memory spikes.

This flag requires the Cloud SQL maintenance version
[*MYSQL_VERSION*.R20260726.00_05](/sql/docs/mysql/maintenance-changelog)
or later. For more information, see [Enable managed buffer
pool](/sql/docs/mysql/optimize-high-memory-usage#enable-managed-buffer-pool).


**Google Kubernetes Engine**

Change 

#### (2026-R43) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2743000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495000

- 1.36.4-gke.2046000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.35 to [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)




### Regular channel




- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1056000

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1225000

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




### Stable channel




- Version [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000) is now available in the Stable channel.

- Version 1.34.11-gke.1044000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




### Extended channel




- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.31.14-gke.2925000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2689000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2825000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2411000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2567000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1636000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1815000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1056000

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- 1.31 to [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- 1.32 to [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- 1.33 to [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




### No channel (deprecated)




- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- The following node versions are now available:

- [1.31.14-gke.2925000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- The following versions are no longer available:

- 1.34.11-gke.1044000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1036000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)






Change 

#### (2026-R43) Version updates

- Version [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000) is now available in the Stable channel.

- Version 1.34.11-gke.1044000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R43) Version updates

- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1056000

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1225000

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




Change 

#### (2026-R43) Version updates

- Version [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- [1.37.1-gke.1552000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2743000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1209000

- 1.35.8-gke.1626001

- 1.36.4-gke.1495000

- 1.36.4-gke.2046000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.34 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.35 to [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- 1.35 to [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- 1.36 to [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)




Change 

#### (2026-R43) Version updates

- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- The following node versions are now available:

- [1.31.14-gke.2925000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.34.12-gke.1153000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)

- [1.35.8-gke.1919000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- [1.36.4-gke.2046002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)

- [1.36.4-gke.2202002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)

- [1.36.4-gke.2304000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)

- [1.36.4-gke.2326000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)

- The following versions are no longer available:

- 1.34.11-gke.1044000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1036000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.2046000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




Change 

#### (2026-R43) Version updates

- Version [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.31.14-gke.2925000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.32.13-gke.2662000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.33.13-gke.1915000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)

- [1.36.4-gke.1495002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2689000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2825000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2411000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2567000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1636000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1815000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1056000

- 1.35.8-gke.1380001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1247000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- 1.31 to [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- 1.32 to [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- 1.33 to [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- 1.36 to [1.36.4-gke.1391002](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)




## October 07, 2026

**Google Kubernetes Engine**

Feature 


The microVM sandbox type is now Generally Available (GA) with GKE Sandbox in
clusters that run version 1.37.0-gke.4713000 and later. MicroVM sandboxes
provide hardware virtualization and isolation for untrusted workloads, AI agent
runtimes, and multi-tenant environments. GKE microVM sandboxes use Kata
Containers and Cloud Hypervisor to provide this isolation while maintaining a
full Linux kernel that includes standard Linux features

For more information, see the
[GKE Sandbox](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/sandbox-pods)
documentation.


**Virtual Private Cloud**

Feature 


Service producers can let service consumers establish more connections to a
Private Service Connect endpoint or backend by
[configuring the target published service (service attachment) to use an additional NAT
IP address](/vpc/docs/manage-private-service-connect-services#update-nat-ips-per-endpoint).
For more information, see
[Maximum connections](/vpc/docs/about-vpc-hosted-services#max-connections).



## October 06, 2026

**Google Kubernetes Engine**

Issue 


Starting with GKE version 1.36, the default engine for kube-dns is [CoreDNS](https://coredns.io/). For
Pod IP DNS queries in the ` . .pod.cluster.local` format,
CoreDNS returns NXDOMAIN if the specified ` ` does not exist. The
legacy `kubernetes/dns` implementation skipped checking the existence of the
namespace provided in the ` ` segment in these queries.

Queries in the ` . .pod.cluster.local` format are not part of
the
[Kubernetes DNS specification](https://github.com/kubernetes/dns/blob/master/docs/specification.md).
We can't guarantee that uses outside of those specified in the DNS spec will
remain consistent across releases.

Mitigation:

- **Recommended**: Migrate to supported headless Service DNS records
(` . . .svc.cluster.local`).

- **Workaround**: Ensure the ` ` specified in the DNS query exists in
the cluster.




## October 05, 2026

**Google Kubernetes Engine**

Feature 


GKE support for using the `c4-standard-*` machine types (up to 192 vCPUs) as
Confidential GKE Nodes with Intel TDX is generally available. For more
information, see the following pages:

- To use this feature with GKE , see [Encrypt workload data in-use with
Confidential GKE
Nodes](https://berlin.devsitetest.how/kubernetes-engine/docs/how-to/confidential-gke-nodes).

- To learn more about the feature from Compute Engine, see [Confidential VM
overview](https://berlin.devsitetest.how/confidential-computing/confidential-vm/docs/confidential-vm-overview).

- To see supported configurations, including machine support, see [Supported
configurations](https://berlin.devsitetest.how/confidential-computing/confidential-vm/docs/supported-configurations)
and its "Machine types, CPUs, and zones" section.




## October 02, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R42) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2240000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1102000

- 1.35.8-gke.1439000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.34 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.35 to [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)




### Regular channel




- The following versions are now available in the Regular channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1044000

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




### Stable channel




- Version [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001) is now the default version for cluster creation in the Stable channel.

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- The following versions are no longer available in the Stable channel:

- 1.34.10-gke.1328000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.34 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.35 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)




### Extended channel




- Version [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2667000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2759000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2393000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2504000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1613000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1721000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1044000

- 1.35.8-gke.1225000

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- 1.31 to [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- 1.32 to [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- 1.33 to [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




### No channel (deprecated)




- The following versions are now available:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- The following node versions are now available:

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- The following versions are no longer available:

- 1.34.9-gke.1065000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1328000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1439000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)






Change 

#### (2026-R42) Version updates

- Version [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001) is now the default version for cluster creation in the Stable channel.

- The following versions are now available in the Stable channel:

- [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- The following versions are no longer available in the Stable channel:

- 1.34.10-gke.1328000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1250000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.34 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.35 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)




Change 

#### (2026-R42) Version updates

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available in the Regular channel:

- 1.34.11-gke.1044000

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




Change 

#### (2026-R42) Version updates

- Version [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2240000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1102000

- 1.35.8-gke.1439000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1391000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.34 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.35 to [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- 1.35 to [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- 1.36 to [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)




Change 

#### (2026-R42) Version updates

- The following versions are now available:

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- The following node versions are now available:

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.34.12-gke.1011000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)

- [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.35.8-gke.1626001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)

- [1.35.8-gke.1796000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)

- [1.36.4-gke.2046000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)

- The following versions are no longer available:

- 1.34.9-gke.1065000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1328000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1439000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1626000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.6-gke.1250001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




Change 

#### (2026-R42) Version updates

- Version [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- [1.31.14-gke.2825000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)

- [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- [1.32.13-gke.2567000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)

- [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- [1.33.13-gke.1815000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- [1.35.8-gke.1439001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2667000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2759000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2393000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2504000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1613000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1721000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.11-gke.1044000

- 1.35.8-gke.1225000

- 1.35.8-gke.1380000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1767000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- 1.31 to [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- 1.32 to [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- 1.33 to [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380001](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)




## September 30, 2026

**Cloud Storage**

Feature 


Cloud Storage client libraries now provide automated, end-to-end checksumming by
default for object read and write operations to help maintain data integrity
from client to storage. For more information, see
[data validation](/storage/docs/data-validation#client-validation-writes).


**Managed Service for Apache Spark**

Announcement 


Managed Service for Apache Spark is now available in Google Cloud. For more information, see [Managed Service for Apache Spark differences in Google Cloud versus Google Cloud](https://documentation.s3ns.fr/managed-spark/docs/tpc-differences).



## September 29, 2026

**Compute Engine**

Feature 


**Generally available**: You can create a standard or archive snapshot of a
disk and protect the snapshot with a customer-managed encryption key
(CMEK), even if the source disk isn't protected with a CMEK. If the source disk
is protected with a CMEK, then you can use a different CMEK to encrypt the new
snapshot.

For more information, see [Create a CMEK-encrypted snapshot](/compute/docs/disks/customer-managed-encryption#create_snapshot).



## September 28, 2026

**Cloud Logging**

Breaking 


Only platform services can write log entries to billing accounts.
These logs have names with the format
`billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`.
For more information, see
[`entries.write`](/logging/docs/reference/v2/rest/v2/entries/write).



## September 23, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R40) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.1002000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1056000

- 1.35.8-gke.1380000

- 1.36.4-gke.1247000

- 1.37.0-gke.3165000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- 1.35 to [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- 1.36 to [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- 1.37 to [1.37.0-gke.3503000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3503000)




### Regular channel




- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.34 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)




### Stable channel




- Version [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000) is now available in the Stable channel.

- Version 1.34.10-gke.1236000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




### Extended channel




- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2630000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2704000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2337000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2427000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1547000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1647000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- 1.31 to [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- 1.32 to [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- 1.33 to [1.33.13-gke.1613000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1613000)

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)




### No channel (deprecated)




- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- The following node versions are now available:

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- The following versions are no longer available:

- 1.34.10-gke.1236000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.7-gke.1222000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)






Change 

#### (2026-R40) Version updates

- Version [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000) is now available in the Stable channel.

- Version 1.34.10-gke.1236000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R40) Version updates

- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.34 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)




Change 

#### (2026-R40) Version updates

- Version [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- [Alpha version](https://berlin.devsitetest.how/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.1002000+preview is now available for GKE alpha clusters in the Rapid channel.

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1056000

- 1.35.8-gke.1380000

- 1.36.4-gke.1247000

- 1.37.0-gke.3165000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.34 to [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- 1.35 to [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- 1.35 to [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- 1.36 to [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- 1.37 to [1.37.0-gke.3503000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3503000)




Change 

#### (2026-R40) Version updates

- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- The following node versions are now available:

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.34.11-gke.1209000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)

- [1.35.8-gke.1626000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)

- [1.36.4-gke.1495000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)

- The following versions are no longer available:

- 1.34.10-gke.1236000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.7-gke.1222000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)




Change 

#### (2026-R40) Version updates

- Version [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- [1.31.14-gke.2759000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)

- [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- [1.32.13-gke.2504000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)

- [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- [1.33.13-gke.1721000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2630000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2704000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2337000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2427000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1547000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1647000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.4-gke.1082000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- 1.31 to [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- 1.32 to [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- 1.33 to [1.33.13-gke.1613000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1613000)

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)




## September 17, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R39) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- [1.37.0-gke.3503000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3503000)

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1044000

- 1.35.8-gke.1225000

- 1.36.4-gke.1082000

- 1.37.0-gke.2941000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- 1.35 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- 1.37 to [1.37.0-gke.3165000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3165000)




### Regular channel




- Version [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1236000

- 1.35.7-gke.1222000

- 1.36.3-gke.1640000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.34 to [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.35 to [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- 1.36 to [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)




### Stable channel




- Version [1.34.10-gke.1236000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000) is now available in the Stable channel.

- Version 1.34.10-gke.1106000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.34 to [1.35.6-gke.1250000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)




### Extended channel




- Version [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2630000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2630000)

- [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- [1.32.13-gke.2337000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2337000)

- [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- [1.33.13-gke.1547000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1547000)

- [1.33.13-gke.1613000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1613000)

- [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2579000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2613000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2689000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2268000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2314000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2411000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1329000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1499000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1636000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1236000

- 1.35.7-gke.1222000

- 1.36.3-gke.1640000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2630000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2630000)

- 1.31 to [1.32.13-gke.2337000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2337000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2630000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2630000)

- 1.32 to [1.32.13-gke.2337000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2337000)

- 1.33 to [1.33.13-gke.1547000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1547000)

- 1.34 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.35 to [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- 1.36 to [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)




### No channel (deprecated)




- Version [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following node versions are now available:

- [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available:

- 1.34.10-gke.1106000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.7-gke.1150000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1640000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.34 to [1.35.6-gke.1250000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.35 to [1.35.6-gke.1250000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)

- 1.36 to [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)






Change 

#### (2026-R39) Version updates

- Version [1.34.10-gke.1236000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000) is now available in the Stable channel.

- Version 1.34.10-gke.1106000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.34 to [1.35.6-gke.1250000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)




Change 

#### (2026-R39) Version updates

- Version [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1236000

- 1.35.7-gke.1222000

- 1.36.3-gke.1640000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.34 to [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.35 to [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- 1.36 to [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)




Change 

#### (2026-R39) Version updates

- Version [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- [1.37.0-gke.3503000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3503000)

- The following versions are no longer available in the Rapid channel:

- 1.34.11-gke.1044000

- 1.35.8-gke.1225000

- 1.36.4-gke.1082000

- 1.37.0-gke.2941000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.34 to [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- 1.35 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- 1.35 to [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- 1.36 to [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- 1.37 to [1.37.0-gke.3165000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3165000)




Change 

#### (2026-R39) Version updates

- Version [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following node versions are now available:

- [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- [1.34.11-gke.1102000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)

- [1.35.8-gke.1439000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)

- [1.36.4-gke.1391000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)

- The following versions are no longer available:

- 1.34.10-gke.1106000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.7-gke.1150000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1640000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.34 to [1.35.6-gke.1250000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.35 to [1.35.6-gke.1250000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)

- 1.36 to [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)




Change 

#### (2026-R39) Version updates

- Version [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2630000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2630000)

- [1.31.14-gke.2667000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2667000)

- [1.31.14-gke.2704000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)

- [1.32.13-gke.2337000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2337000)

- [1.32.13-gke.2393000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2393000)

- [1.32.13-gke.2427000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)

- [1.33.13-gke.1547000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1547000)

- [1.33.13-gke.1613000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1613000)

- [1.33.13-gke.1647000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)

- [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2579000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2613000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2689000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2268000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2314000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2411000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1329000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1499000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1636000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1236000

- 1.35.7-gke.1222000

- 1.36.3-gke.1640000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2630000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2630000)

- 1.31 to [1.32.13-gke.2337000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2337000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2630000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2630000)

- 1.32 to [1.32.13-gke.2337000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2337000)

- 1.33 to [1.33.13-gke.1547000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1547000)

- 1.34 to [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- 1.35 to [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- 1.36 to [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)




## September 16, 2026

**Virtual Private Cloud**

Feature 


**General Availability**: You can add Dynamic NICs to the same VPC network used
by other network interfaces of a Compute Engine instance. For more information,
see [Multiple network interfaces](/vpc/docs/multiple-interfaces-concepts#specifications).



Feature 


**General Availability**: VPC Flow Logs supports logging for
App Engine resources that are configured with
[Direct VPC egress](/appengine/docs/standard/vpc-direct-vpc).
For more information, see
[Serverless flows](/vpc/docs/about-traffic-flows#serverless-flows) and
[ServerlessDetails field format](/vpc/docs/about-flow-logs-records#serverless-details).



Feature 


**General Availability**: VPC Flow Logs adds the following metadata annotations
for Private Service Connect:

- `src_psc_interface` and `dest_psc_interface`

- `psc.consumer_connection`

- `psc.psc_endpoint.name`

- `psc.psc_attachment.name`

For more information, see
[Record format](/vpc/docs/about-flow-logs-records#record_format).



## September 08, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R38) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- [1.37.0-gke.3165000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3165000)

- The following versions are no longer available in the Rapid channel:

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.3-gke.1767000

- 1.37.0-gke.2155000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.34 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- 1.35 to [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- 1.36 to [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)

- 1.37 to [1.37.0-gke.2941000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-2941000)




### Regular channel




- Version [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1106000

- 1.35.7-gke.1150000

- 1.36.3-gke.1537000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1236000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000)

- 1.34 to [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1236000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000)

- 1.35 to [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)

- 1.36 to [1.36.3-gke.1640000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1640000)




### Stable channel




- Version [1.34.10-gke.1106000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1106000) is now available in the Stable channel.

- Version 1.34.10-gke.1079000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




### Extended channel




- Version [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2667000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2393000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1613000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1106000

- 1.35.7-gke.1150000

- 1.36.3-gke.1537000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1236000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000)

- 1.35 to [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)

- 1.36 to [1.36.3-gke.1640000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1640000)




### No channel (deprecated)




- Version [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following node versions are now available:

- [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available:

- 1.34.10-gke.1079000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.7-gke.1027000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1537000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.35 to [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)

- 1.36 to [1.36.3-gke.1640000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1640000)






Change 

#### (2026-R38) Version updates

- Version [1.34.10-gke.1106000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1106000) is now available in the Stable channel.

- Version 1.34.10-gke.1079000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.




Change 

#### (2026-R38) Version updates

- Version [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1106000

- 1.35.7-gke.1150000

- 1.36.3-gke.1537000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1236000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000)

- 1.34 to [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1236000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000)

- 1.35 to [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)

- 1.36 to [1.36.3-gke.1640000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1640000)




Change 

#### (2026-R38) Version updates

- Version [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- [1.37.0-gke.3165000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3165000)

- The following versions are no longer available in the Rapid channel:

- 1.34.10-gke.1328000

- 1.35.8-gke.1036000

- 1.36.3-gke.1767000

- 1.37.0-gke.2155000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.34 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- 1.35 to [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.11-gke.1044000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)

- 1.35 to [1.35.8-gke.1225000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)

- 1.36 to [1.36.4-gke.1082000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)

- 1.37 to [1.37.0-gke.2941000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-2941000)




Change 

#### (2026-R38) Version updates

- Version [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following node versions are now available:

- [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- [1.34.11-gke.1056000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)

- [1.35.8-gke.1380000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)

- [1.36.4-gke.1247000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)

- The following versions are no longer available:

- 1.34.10-gke.1079000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.7-gke.1027000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1537000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.35 to [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)

- 1.36 to [1.36.3-gke.1640000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1640000)




Change 

#### (2026-R38) Version updates

- Version [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2689000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)

- [1.32.13-gke.2411000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)

- [1.33.13-gke.1636000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)

- [1.34.10-gke.1328000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)

- [1.35.8-gke.1036000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)

- [1.36.3-gke.1767000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2667000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2393000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1613000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1106000

- 1.35.7-gke.1150000

- 1.36.3-gke.1537000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1236000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000)

- 1.35 to [1.35.7-gke.1222000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)

- 1.36 to [1.36.3-gke.1640000](https://berlin.devsitetest.how/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1640000)




## September 02, 2026

**Google Kubernetes Engine**

Change 

#### (2026-R37) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://berlin.devsitetest.how/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://berlin.devsitetest.how/kubernetes-engine/upgrades).





### Rapid channel




- Version [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)

- [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)

- [1.37.0-gke.2155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)

- [1.37.0-gke.2941000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)

- The following versions are no longer available in the Rapid channel:

- 1.34.10-gke.1236000

- 1.35.7-gke.1222000

- 1.35.8-gke.1026000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1640000

- The following alpha versions are no longer available in the Rapid channel:

- 1.37.0-gke.2034000+preview

- 1.37.0-gke.2048000+preview

- 1.37.0-gke.2074000+preview

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.34 to [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- 1.35 to [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.35 to [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- 1.36 to [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)

- 1.37 to [1.37.0-gke.2155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)




### Regular channel




- Version [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1079000

- 1.35.7-gke.1027000

- 1.36.2-gke.2064000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.34 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)




### Stable channel




- Version [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410) is now available in the Stable channel.

- Version 1.34.9-gke.1610001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)




### Extended channel




- Version [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- [1.31.14-gke.2667000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- [1.32.13-gke.2314000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- [1.32.13-gke.2393000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- [1.33.13-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)

- [1.33.13-gke.1613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)

- [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2543000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2630000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2231000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2337000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1269000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1547000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1079000

- 1.35.7-gke.1027000

- 1.36.2-gke.2064000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2579000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- 1.31 to [1.32.13-gke.2268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2579000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- 1.32 to [1.32.13-gke.2268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- 1.33 to [1.33.13-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)

- 1.34 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)




### No channel (deprecated)




- Version [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)

- [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)

- The following node versions are now available:

- [1.31.14-gke.2667000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- [1.32.13-gke.2393000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- [1.33.13-gke.1613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)

- [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)

- [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)

- The following versions are no longer available:

- 1.34.9-gke.1610001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1710000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1026000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.2-gke.2064000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)

- 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)






Change 

#### (2026-R37) Version updates

- Version [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410) is now available in the Stable channel.

- Version 1.34.9-gke.1610001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)




Change 

#### (2026-R37) Version updates

- Version [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation in the Regular channel.

- The following versions are now available in the Regular channel:

- [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1079000

- 1.35.7-gke.1027000

- 1.36.2-gke.2064000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.34 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)




Change 

#### (2026-R37) Version updates

- Version [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363) is now the default version for cluster creation in the Rapid channel.

- The following versions are now available in the Rapid channel:

- [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)

- [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)

- [1.37.0-gke.2155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)

- [1.37.0-gke.2941000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)

- The following versions are no longer available in the Rapid channel:

- 1.34.10-gke.1236000

- 1.35.7-gke.1222000

- 1.35.8-gke.1026000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.3-gke.1640000

- The following alpha versions are no longer available in the Rapid channel:

- 1.37.0-gke.2034000+preview

- 1.37.0-gke.2048000+preview

- 1.37.0-gke.2074000+preview

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.34 to [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- 1.35 to [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.35 to [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- 1.36 to [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)

- 1.37 to [1.37.0-gke.2155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)




Change 

#### (2026-R37) Version updates

- Version [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation.

- The following versions are now available:

- [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)

- [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)

- The following node versions are now available:

- [1.31.14-gke.2667000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- [1.32.13-gke.2393000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- [1.33.13-gke.1613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)

- [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)

- [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)

- [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)

- The following versions are no longer available:

- 1.34.9-gke.1610001 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.6-gke.1710000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.35.8-gke.1026000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- 1.36.2-gke.2064000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.33 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.34 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)

- 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)




Change 

#### (2026-R37) Version updates

- Version [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation in the Extended channel.

- The following versions are now available in the Extended channel:

- [1.31.14-gke.2613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- [1.31.14-gke.2667000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- [1.32.13-gke.2314000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- [1.32.13-gke.2393000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- [1.33.13-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)

- [1.33.13-gke.1613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)

- [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)

- The following versions are no longer available in the Extended channel:

- 1.31.14-gke.2543000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.31.14-gke.2630000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2231000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.32.13-gke.2337000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1269000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.33.13-gke.1547000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- 1.34.10-gke.1079000

- 1.35.7-gke.1027000

- 1.36.2-gke.2064000 is [deprecated](https://berlin.devsitetest.how/kubernetes-engine/versioning#patch-version-support) in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:

- 1.30 to [1.31.14-gke.2579000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- 1.31 to [1.32.13-gke.2268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:

- 1.31 to [1.31.14-gke.2579000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)

- 1.32 to [1.32.13-gke.2268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)

- 1.33 to [1.33.13-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)

- 1.34 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)

- 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)

- 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)




## August 31, 2026

**Google Kubernetes Engine**

Feature 


Session affinity support using GCPTrafficDistributionPolicy for GKE Gateway is
generally available. This release currently supports single-cluster GKE Gateway
load balancers using the following GatewayClasses:

- `gke-l7-rilb`

- `gke-l7-regional-external-managed`

- `gke-l7-global-external-managed`

In addition to the session affinity types available in Preview, you can now use
the `STRONG_COOKIE_AFFINITY` type, which provides the most persistent session
stickiness among the session affinity types available in Google Cloud
Application Load Balancers.

The session affinity types require the following minimum GKE versions:

- `CLIENT_IP`, `HEADER_FIELD`, `GENERATED_COOKIE`, and `HTTP_COOKIE`:
version 1.35.2-gke.1269001 or later

- `STRONG_COOKIE_AFFINITY`: version 1.36.3-gke.1767000 or later

For more information, see [Configure session affinity using GCPTrafficDistributionPolicy](https://berlin.devsitetest.how/kubernetes-engine/docs/how-to/configure-gateway-resources#expanded-session-affinity).


**Virtual Private Cloud**

Feature 


**General Availability**: You can create Compute Engine instances that have
multiple virtual network interfaces (vNICs) in the same VPC network.
For more information, see
[Multiple network interfaces in the same VPC network](/vpc/docs/multiple-interfaces-concepts#same-vpc).