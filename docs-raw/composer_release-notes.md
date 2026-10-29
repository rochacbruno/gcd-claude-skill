# Managed Service for Apache Airflow release notes

Source: https://berlin.devsitetest.how/composer/docs/release-notes
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/composer/docs/tpc-differences) for more details.














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

Managed Service for Apache Airflow

](https://berlin.devsitetest.how/composer/docs)






- 








[

Resources

](https://berlin.devsitetest.how/composer/docs/resources)












# Managed Service for Apache Airflow release notes 























These release notes apply to the Managed Service for Apache Airflow service. Announcements
and information about new or updated features, bug fixes and deprecated
functionality is published on this page.

You can also:

- Follow Managed Airflow release notes in the
[Apache Airflow Community workspace](https://apache-airflow-slack.herokuapp.com/) 
on Slack.

- See
[Cloud Composer version list](/composer/docs/composer-versions)
for more information about Managed Airflow images and support
dates.

- Check the [Cloud Composer known issues](/composer/docs/latest/known-issues)
page to learn more about known issues and possible workarounds.







You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/composer-release-notes.xml) directly.









## March 11, 2025


Fixed 


*(Cloud Composer 3)* Validation error messages now use the correct format for image versions.



Change 


New [images](https://berlin.devsitetest.how/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.11.5-airflow-2.10.2 (default)

- composer-2.11.5-airflow-2.9.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.11 (default)

- composer-3-airflow-2.9.3-build.18




## March 05, 2025


Feature 


You can now specify an [order in which Airflow searches for secrets](https://berlin.devsitetest.how/composer/docs/composer-3/configure-secret-manager#configure-backend) by overriding the
`[secrets]backends_order` Airflow configuration option.



Fixed 


Fixed an issue in Cloud Composer REST API that allowed some `environment.patch` operations to succeed when multiple update masks that aren't related to each other were passed in a request. Now operations with such masks fail with an error.



Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.10 (default)

- composer-3-airflow-2.9.3-build.17




Deprecated 


Cloud Composer versions 2.6.2 and 2.6.3 have reached their [end of support period](https://berlin.devsitetest.how/composer/docs/composer-versioning-overview#version-deprecation-and-support).



Change 


New [images](https://berlin.devsitetest.how/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.11.4-airflow-2.10.2 (default)

- composer-2.11.4-airflow-2.9.3




## March 04, 2025


Feature 


Cloud Composer 3 supports [Customer Managed Encryption Keys (CMEK)](https://berlin.devsitetest.how/composer/docs/composer-3/configure-cmek-encryption).



## February 27, 2025


Feature 


[Database retention policy](https://berlin.devsitetest.how/composer/docs/composer-3/configure-db-retention) is available in Cloud Composer 3. You can use this feature to automatically delete older records from the Airflow database, which helps to maintain the Airflow database's size.



## February 25, 2025


Feature 


**Cloud Composer 3** is now available in Stockholm (europe-north2). The change is gradually rolling out.



## February 21, 2025


Announcement 


Starting April 14, 2025, **the Deployment Manager API won't be automatically enabled** when you enable Cloud Composer API because this API isn't used by the Cloud Composer service.



## February 20, 2025


Fixed 


*(Cloud Composer 3)* Fixed a problem with configuring access to SMTP servers that don't support user and password authentication. The `[smtp]smtp_user` and `[smtp]smtp_password` Airflow configuration options are no longer preconfigured with placeholder values.



Change 


Improved the forbidden APIs check. When a new environment is created, Cloud Composer now checks for forbidden APIs that are required by a specific major version of Cloud Composer.



Change 


*(Airflow 2.10.2 and 2.9.3)* Preinstalled packages were changed:

- `virtualenv` was downgraded from 20.29.1 to 20.28.1




Deprecated 


Cloud Composer version 2.6.1 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/composer-versioning-overview#version-deprecation-and-support).



Change 


New [images](https://berlin.devsitetest.how/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.11.3-airflow-2.10.2 (default)

- composer-2.11.3-airflow-2.9.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.9 (default)

- composer-3-airflow-2.9.3-build.16




## February 13, 2025


Fixed 


*(Cloud Composer 3)* The `GOOGLE_CLOUD_PROJECT` environment variable is changed to reserved for Cloud Composer 3. This fixes an issue where creating an environment with this variable failed with a non-specific error.



Change 


*(Cloud Composer 2)* The list of permissions reported by `dependency_permissions_check_count` metric was updated. Now the metric reports more permissions that are required for a functioning environment. Permissions that weren't necessary were replaced or removed.



Fixed 


*(Cloud Composer 2)* The `dependency_permissions_check_count` metric now correctly reports the number of missing permissions.



Fixed 


*(Available without upgrading)* Fixed a problem that caused Terraform to unnecessarily force the replacement of `cloud_composer_network_ipv4_cidr_block`, `web_server_ipv4_cidr_block`, and `cloud_sql_ipv4_cidr_block` fields in some configurations of Cloud Composer 2 and Cloud Composer 1 environments.



Change 


*(New Cloud Composer environments only)* Cloud Composer now enforces SSL connections to Cloud SQL instances.

This change implements a security compliance standard in Cloud Composer and enforces SSL usage. You can adopt other security standards by following recommendations listed in [Vulnerability findings](https://berlin.devsitetest.how/security-command-center/docs/concepts-vulnerabilities-findings#supported-security-standards).
Previously, it was possible to create a non-SSL connection to the Airflow database. After the change, the connection will be refused.



Change 


*(Airflow 2.10.2 and 2.9.3)* Preinstalled packages were changed:

- `logbook` was removed from preinstalled packages

- `minimal-snowplow-tracker` was removed from preinstalled packages

- `mashumaro` was downgraded from 3.15 to 3.14




Change 


New [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.11.2-airflow-2.10.2 (default)

- composer-2.11.2-airflow-2.9.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.8 (default)

- composer-3-airflow-2.9.3-build.15




Deprecated 


Cloud Composer versions 2.6.0 and 2.6.1 have reached their [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



## February 07, 2025


Announcement 


Starting March 2025, the **default version for new Cloud Composer environments** changes from Cloud Composer 2 to Cloud Composer 3.

New environments that are created without a specified version will use the default Airflow build of Cloud Composer 3, `composer-3-airflow-2`. Currently, the default version is `composer-2-airflow-2`.



## February 06, 2025


Change 


Cloud Composer 2 is **no longer available in Mexico (northamerica-south1)**. It is not possible to select this region when creating a new Cloud Composer 2 environment. Existing Cloud Composer 2 environments and both new and existing Cloud Composer 3 environments are not affected by this change.



## February 04, 2025


Announcement 


All Cloud Composer environment's GKE clusters are set up with maintenance exclusions from January 21, 2025 to February 10, 2025. For more information, see [Maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).



## January 31, 2025


Issue 


*(Cloud Composer 3)* The [issue with upgrading Airflow builds](#January_27_2025) **is now resolved**. You can now upgrade Airflow builds for Cloud Composer 3 in the asia-south1, asia-northeast2, europe-west1, europe-west3, and europe-north1 regions.



## January 30, 2025


Announcement 


At the beginning of February 2025, we will **delete inactive environments that are non-recoverable** in Cloud Composer 1, Cloud Composer 2, and Cloud Composer 3. After this change, non-recoverable environments that have listed problems will be deleted automatically.

**Cloud Composer 1 and Cloud Composer 2** environments that have both of the following problems present at the same time will be deleted:

- The environment's underlying GKE cluster is deleted.

- The environment is in the ERROR state for at least 60 days because of a disabled billing account or because the Cloud Composer API service was deactivated in its project.

**Cloud Composer 3** environments that have the following problem will be deleted:

- The environment is in the ERROR state for at least 60 days because of a disabled billing account or because the Cloud Composer API service was deactivated in its project.

This change doesn't affect buckets of these environments. You can still recover your DAGs and other data from the environment's bucket and then delete the bucket manually. See [Delete environments](https://berlin.devsitetest.how/composer/docs/composer-3/delete-environments#about-not-deleted) for information about data that is not deleted automatically together with the environment.



## January 28, 2025


Feature 


Java Runtime in Airflow workers and schedulers is updated from [version 17](https://openjdk.org/projects/jdk/17/) to [version 21](https://openjdk.org/projects/jdk/17/).



Fixed 


*(Cloud Composer 3)* Fixed an issue with KubernetesPodOperator failing to run properly when `do_xcom_push` was set to `True`.



Fixed 


Fixed a problem where synchronization between the environment's bucket and Airflow components failed because incorrect objects in the bucket were not ignored.



Change 


*(Available without upgrading)* In Cloud Composer 2 and Cloud Composer 1, a more meaningful error message is produced when the Composer Service Agent account doesn't have necessary permissions to access the network during the environment creation.



Fixed 


Fixed an issue where log messages were incorrectly formatted for non-string content, such as dictionaries and numbers.



Fixed 


*(Available without upgrading)* In Cloud Composer 3, fixed an issue where deleting an environment with an attached VPC network failed if the project accept list of the network attachment was cleared manually.



Fixed 


Terminating Airflow workers now generate log messages with information about still running tasks.



Change 


*(Cloud Composer 3)* The zone in the [`Environment.config.node_config.location`](https://berlin.devsitetest.how/composer/docs/reference/rest/v1/projects.locations.environments#nodeconfig) field is no longer populated in the Cloud Composer API.



Change 


*(Available without upgrading)* Starting from Cloud Composer version 2.11.0 with Airflow 2.10.2 and 2.9.3, the `enable_task_context_logger` Airflow configuration option is no longer blocked.



Change 


*(Airflow 2.10.2 and 2.9.3)* The following preinstalled provider packages were upgraded to new major versions:

- `apache-airflow-providers-apache-beam` upgraded from 5.9.1 to 6.0.0

- `apache-airflow-providers-dbt-cloud` upgraded from 3.11.2 to 4.0.0

- `apache-airflow-providers-hashicorp` upgraded from 3.8.0 to 4.0.0

- `apache-airflow-providers-http` upgraded from 4.13.3 to 5.0.0

- `apache-airflow-providers-mysql` upgraded from 5.7.4 to 6.0.0

- `apache-airflow-providers-sendgrid` upgraded from 3.6.0 to 4.0.0

- `apache-airflow-providers-sqlite` upgraded from 3.9.1 to 4.0.0

- `apache-airflow-providers-ssh` upgraded from 3.14.0 to 4.0.0




Change 


*(Airflow 2.10.2 and 2.9.3)* The `apache-airflow-providers-cncf-kubernetes` package was upgraded to version 10.1.0 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-cncf-kubernetes changelog](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html) from version 10.0.1 to version 10.1.0.



Change 


*(Airflow 2.10.2 and 2.9.3)* The following preinstalled packages were downgraded:

- `certifi` downgraded from 2024.12.14 to 2024.8.30.

- `charset-normalizer` downgraded from 3.4.1 to 3.4.0.

- `cryptography` downgraded from 44.0.0 to 43.0.3.

- `filelock` downgraded from 3.16.1 to 3.15.4.

- `google-auth` downgraded from 2.37.0 to 2.35.0.

- `keyring` downgraded from 25.6.0 to 25.5.0.

- `urllib3` downgraded from 2.3.0 to 2.2.3.

- `zipp` downgraded from 3.21.0 to 3.20.2.




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.7 (default)

- composer-3-airflow-2.9.3-build.14




Change 


New [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.11.1-airflow-2.10.2 (default)

- composer-2.11.1-airflow-2.9.3




Deprecated 


Cloud Composer version 2.5.5 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



## January 27, 2025


Issue 


**January 31, 2025 update**: The issue [is resolved](#January_31_2025).

*(Cloud Composer 3 only)* We are currently experiencing an issue with upgrading Airflow builds for Cloud Composer 3 in asia-south1, asia-northeast2, europe-west1, europe-west3, europe-north1 regions.

The upgrades are temporarily disabled as we continue our work to restore the listed functionalities. We will release an additional announcement after the issue is resolved.



## January 24, 2025


Deprecated 


The following recently released Cloud Composer 3 Airflow builds and Cloud Composer 2 versions are **rolled back and aren't available** for creating and upgrading existing environments. We will roll out new builds in the next release.

- composer-2.11.0-airflow-2.10.2

- composer-2.11.0-airflow-2.9.3

- composer-3-airflow-2.10.2-build.6

- composer-3-airflow-2.9.3-build.13




## January 15, 2025


Announcement 


In April 2025, Cloud Composer 2 environments will always **use the environment's service account for performing PyPI packages installations**:

- The environment's service account will be used instead.

- Existing Cloud Composer 2 environments that previously used the default Cloud Build service account will change to using the environment's service account instead.

- Cloud Composer 2 environments created in versions 2.10.2 and later already have this change.

- Cloud Composer 3 environments already use the environment's service account, and are not impacted by this change.




Announcement 


Starting April 13, 2025, we are **removing the default environment's service account setting**. This change enhances security and provides greater control over your Cloud Composer environments.

- Previously, the default Compute Engine service account was used by default when a user didn't specify a service account during Cloud Composer creation.

- After the change, you'll need to explicitly specify a service account when you create a new Cloud Composer environment.

- Existing Cloud Composer environments will not be affected by this change.

To address this change:

- We recommend to **create one or more user-managed service accounts** for Cloud Composer environments in your project and grant them the minimum of required permissions. For more information and instructions, see [Grant roles to an environment's service account](https://berlin.devsitetest.how/composer/docs/composer-3/access-control#service-account).

- If you use **Terraform, scripts or other automation and configuration management tools**, then make sure to update them, so that an environment's service account [is specified when you create an environment](https://berlin.devsitetest.how/composer/docs/composer-2/create-environments#basic-setup).




## January 12, 2025


Announcement 


**April 3, 2025 update**: This change [is postponed](https://berlin.devsitetest.how/composer/docs/release-notes#April_03_2025).

Starting after **April 13, 2025**, Cloud Composer 3 will **unify its billing with BigQuery**. The Cloud Composer 3 standard milli DCU-hours SKU will be replaced with the new BigQuery Engine for Apache Airflow SKU, which will be calculated based on the number of BigQuery slot hours that your Cloud Composer 3 environments consume. Other SKUs will be renamed and moved under the BigQuery hierarchy. The change will be rolled out gradually to all regions supported by Cloud Composer 3. For more information about the change, see [Transition to BigQuery slot-hour-based pricing](https://berlin.devsitetest.how/composer/pricing#composer-3-bq-sku).



## January 10, 2025


Feature 


*(Cloud Composer 3)* You can now use custom certificates when [installing packages from your private repository](https://berlin.devsitetest.how/composer/docs/composer-3/install-python-dependencies#install-private-repo). This change is gradually rolled out to all Cloud Composer 3 environments. To obtain this change earlier, upgrade the Airflow build of your environment.



Feature 


*(Cloud Composer 3)* [New metrics](https://berlin.devsitetest.how/composer/docs/composer-3/monitor-environments#services-quotas) are available for Cloud Composer 3 environments:

- CPU quota limit for Cloud Composer workloads

- CPU quota usage for Cloud Composer workloads




Change 


*(Available without upgrading)* Improved the error message generated when the Cloud Composer Service Agent service account is missing permissions on the project or on the environment's service account.



Fixed 


Fixed an issue where the user-defined Cloud DNS configuration for Google API domains would break Cloud Composer 3 environment creation and attachment of VPC networks.



Change 


*(Cloud Composer 3 only)* The `/data` folder is now synchronized with Airflow triggerers.



Fixed 


*(Cloud Composer 2)* Cloud Composer 2 environments that use PSC interfaces will no longer try to allocate IP ranges for VPC peerings in the tenant project. Environments that use PSC instead of VPC peerings do not use these ranges. This fixes a problem where these ranges overlapped with ranges used for the PSC subnetwork.



Change 


*(New Cloud Composer 2 environments only)* Cloud Composer 2 environments in versions 2.10.2 and later **always use the environment's service account** for performing PyPI packages installations. This change applies **only to newly created environments**, existing environments that are upgraded to 2.10.2 and later versions will not get this change.



Issue 


The issue with automatic environment upgrades and upgrading Airflow builds in Cloud Composer 3 **is resolved** and these operations are working. If you think that your environment is still impacted by this issue, please reach out to the Cloud Support team.



Change 


The Redis persistent disk is now automatically deleted together with the environment. This persistent disk is used by the Redis queue and stores only technical data.



Change 


The `importlib-resources` package was removed from preinstalled packages.



Fixed 


Removed the warning log message about in-memory storage because it doesn't apply to Cloud Composer.



Change 


The `worker_autoscale` Airflow configuration option is blocked in Cloud Composer 2. Previously, it was blocked only in Cloud Composer 3.



Fixed 


Fixed a problem with the interpolation of pip.conf file. Now the pip.conf file is not interpolated and can contain unescaped % characters.



Deprecated 


Cloud Composer version 2.5.4 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


New [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.10.2-airflow-2.10.2 (default)

- composer-2.10.2-airflow-2.9.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.5 (default)

- composer-3-airflow-2.9.3-build.12




Change 


Cloud Composer 2.10.1 is a version with an extended upgrade timeline.



## January 09, 2025


Issue 


**January 10, 2025 update**: The issue is resolved.

*(Cloud Composer 3 only)* We are currently experiencing an issue with automatic environment upgrades and upgrading Airflow builds for Cloud Composer 3 in asia-south1, europe-west1, and asia-northeast2 regions.

The upgrades are temporarily disabled as we continue our work to restore the listed functionalities. We will release an additional announcement after the issue is resolved.



Announcement 


In January 2025, we will **delete inactive Cloud Composer 1 environments that are non-recoverable**. Environments that have both of the following problems present at the same time will be deleted:

- The environment's underlying GKE cluster is deleted.

- The environment is in the ERROR state for at least 60 days because of a disabled billing account or because the Cloud Composer API service was deactivated in its project.

This change doesn't affect buckets of these environments. You can still recover your DAGs and other data from the environment's bucket and then delete the bucket manually. See [Delete environments](https://berlin.devsitetest.how/composer/docs/delete-environments#about-not-deleted) for information about data that is not deleted automatically together with the environment.



## December 20, 2024


Feature 


**Cloud Composer 3** is now available in Mexico (northamerica-south1).



## December 16, 2024


Feature 


**[Cloud Composer 3](https://berlin.devsitetest.how/composer/docs/composer-versioning-overview#comparison) is now generally available (GA)**:

- All [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) starting from airflow-2.9.3-build.11 and airflow-2.10.2-build.4 are supported at the GA level.

- If your environment uses an earlier Airflow build, then upgrade it to airflow-2.9.3-build.11, airflow-2.10.2-build.4, or a later build to use Cloud Composer 3 on the GA level.




## December 15, 2024


Change 


When creating new environments in Google Cloud console, it's now required to explicitly select a service account for the environment. We recommend to [create a user-managed service account](https://berlin.devsitetest.how/composer/docs/composer-3/access-control#custom-service-account) and use it for Cloud Composer environments.



## December 11, 2024


Announcement 


In January 2025, we plan to release Cloud Composer 2 versions that will always use the environment's service account for performing PyPI packages installations:

- New Cloud Composer 2 environments created in versions 2.10.2 and later will have this change. This change applies only to newly created environments, existing environments that are upgraded to 2.10.2 and later versions will not get this change.

- Currently, Cloud Composer 2 environments use the default Cloud Build service account if it exists (and the environment's service account if it doesn't). Depending on the way Cloud Build is configured in your project, this might mean that the default Cloud Compute service account or the legacy Cloud Build service account might be used by your environment. We recommend to configure Cloud Build to [adhere to the principle of least privilege](https://berlin.devsitetest.how/build/docs/securing-builds/configure-user-specified-service-accounts).

- Make sure to check the [Cloud Build default service account change](https://berlin.devsitetest.how/build/docs/cloud-build-service-account-updates) page for information about changes to the default Cloud Build service account.

- Cloud Composer 3 environments already use the environment's service account, and are not impacted by this change.




Fixed 


*(Cloud Composer 3)* It is now possible to upgrade an environment if the `[sentry]sentry_on` Airflow configuration option is set to `true`.



Change 


The `COMPOSER_AGENT_BUILD_SERVICE_ACCOUNT` environment variable is changed to reserved. This change improves the security of Cloud Composer environments.



Change 


*(Cloud Composer 2)* Airflow worker liveness check configuration was changed to be consistent with the configuration used in Cloud Composer 3. In particular, this change increases the timeout, giving the liveness check more time to detect unhealthy Airflow workers. This change is gradually rolled out to all regions supported by Cloud Composer.



Fixed 


Cloud Composer no longer adds any missing IAM permissions to the Cloud Storage bucket when it is used to create an environment with a custom environment's bucket. Make sure that the environment's service account has permissions from the Composer Worker role [on the bucket](https://berlin.devsitetest.how/storage/docs/access-control/using-iam-permissions).



Change 


Increased allowed timeouts when detecting tasks stuck in the "queued" state during the Airflow worker liveness check. This change makes it less likely that checks will incorrectly fail in specific scenarios. This change is gradually rolled out to all regions supported by Cloud Composer.



Deprecated 


Cloud Composer version 2.5.3 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


New [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.10.1-airflow-2.10.2 (default)

- composer-2.10.1-airflow-2.9.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.4 (default)

- composer-3-airflow-2.9.3-build.11




## December 05, 2024


Feature 


New Cloud Composer 3 environments can now be [created in VPC SC](https://berlin.devsitetest.how/composer/docs/composer-3/configure-vpc-sc). This feature is gradually rolled out to all regions supported by Cloud Composer.



Feature 


Improved Airflow worker liveness checks to detect workers with unexpected idle task slots. This feature improves the stability of Airflow by better detection of unhealthy Airflow workers. This feature is gradually rolled out to all regions supported by Cloud Composer.



Fixed 


Fixed the issue in the environment's component responsible for uploading the logs of Airflow components to Cloud Logging. This bug sometimes lead to a situation where Cloud Composer-level log might be missing for an Airflow component. The same log was still available on the Kubernetes-component level.



Fixed 


*(Cloud Composer 3)* KubernetesPodOperator now works when the `do_xcom_push` parameter is set to `True`.



Fixed 


*(Cloud Composer 2)* If an upgrade operation fails, Cloud Composer 2 now restores the environment with the correct number of triggers.



Fixed 


*(Cloud Composer 2 only)* It is now possible to upgrade an environment if the `[sentry]sentry_on` Airflow configuration option is set to `true`.



Fixed 


Long log entries now have proper task instance annotations.



Fixed 


*(New Cloud Composer 3 environments)* Increased the maximum number of internet connections that each Airflow worker can support at the same time.



Fixed 


The maximum limit on the database size during upgrades in Cloud Composer 3 is now the same as the limit for snapshots (20 GB).



Change 


The `aiohttp` package was downgraded from 3.11.0 to 3.10.11.



Change 


*(Airflow 2.10.2 and 2.9.3)* The `apache-airflow-providers-google` package was upgraded to version 10.26.0 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/10.26.0/commits.html) from version 10.25.0 to version 10.26.0.



Change 


*(Available without upgrading)* Fixed an issue where Airflow workers sometimes generated incomplete or unreadable output.



Change 


*(Airflow 2.10.2 and 2.9.3)* The `apache-airflow-providers-cncf-kubernetes` package was upgraded to version 10.0.1 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-cncf-kubernetes changelog](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html) from version 9.0.1 to version 10.0.1.



Change 


The default version of Airflow is changed to 2.10.2.



Deprecated 


Airflow 2.7.3 is no longer included in Cloud Composer images and builds.



Change 


New [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.10.0-airflow-2.10.2 (default)

- composer-2.10.0-airflow-2.9.3




Deprecated 


Cloud Composer version 2.5.2 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.3 (default)

- composer-3-airflow-2.9.3-build.10




## December 04, 2024


Feature 


[Scheduled snapshots](https://berlin.devsitetest.how/composer/docs/composer-3/configure-scheduled-snapshots) are available in Cloud Composer 3. This feature will be gradually rolled out to all regions supported by Cloud Composer 3.



Feature 


**Cloud Composer 2** is now available in Mexico (northamerica-south1).



## December 03, 2024


Announcement 


All Cloud Composer environment's GKE clusters are set up with maintenance exclusions from December 20, 2024 to January 2, 2025. For more information, see [Maintenance exclusions](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).



## November 27, 2024


Announcement 


In December 2024, Google will **remove the following previously deprecated Airflow operators** from the `apache-airflow-providers-google` package.

The new version of this package will be included in one of the future releases of Cloud Composer and the change will be announced in the Release Notes. After this change, it will not be possible to use these operators in your DAGs.

Make sure that you use up-to-date alternatives of the removed operators instead. For more information about removed and deprecated Airflow operators and their up-to-date alternatives, see [Deprecated and removed Airflow operators](https://berlin.devsitetest.how/composer/docs/composer-2/write-dags#deprecated-operators).

**Operators that will be removed in December 2024**: DataPipelineHook, CreateDataPipelineOperator, RunDataPipelineOperator, AutoMLDatasetLink, AutoMLDatasetListLink, AutoMLModelLink, AutoMLModelTrainLink, AutoMLModelPredictLink.



## November 13, 2024


Feature 


**Airflow 2.10.2** is available in Cloud Composer.



Fixed 


*(Airflow 2.7.3)* Backported [#35887](https://github.com/apache/airflow/pull/35887) to fix an issue that occurred during the DST transition. The issue affected DAGs with timezone-aware cron schedule and caused infinite loops in the Airflow scheduler.



Change 


Improved the error message generated when a Cloud Composer 3 environment creation fails because of missing permissions.



Change 


*(Airflow 2.10.2 and 2.9.3)* The `apache-airflow-providers-cncf-kubernetes` package was upgraded to version 9.0.1 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-cncf-kubernetes changelog](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html) from version 9.0.0 to version 9.0.1.



Change 


*(Airflow 2.10.2 and 2.9.3)* The `apache-airflow-providers-google` package was upgraded to version 10.25.0 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/10.25.0/commits.html) from version 10.24.0 to version 10.25.0.



Change 


New [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.9.11-airflow-2.10.2

- composer-2.9.11-airflow-2.9.3 (default)

- composer-2.9.11-airflow-2.7.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.10.2-build.0

- composer-3-airflow-2.9.3-build.7 (default)

- composer-3-airflow-2.7.3-build.23




Change 


Support dates for previous Cloud Composer 3 builds are available. All Cloud Composer 3 builds with Airflow 2.9.3 are supported until November 13, 2025.



## November 06, 2024


Change 


*(Airflow 2.9.3 and 2.7.3)* The `docutils` package was removed from preinstalled packages.



Fixed 


*(Cloud Composer 3)* Fixed an issue that affected the speed of PyPI package installation. PyPI packages are now installed slightly faster.



Change 


New [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available in Cloud Composer 2:

- composer-2.9.10-airflow-2.9.3 (default)

- composer-2.9.10-airflow-2.7.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.3-build.6 (default)

- composer-3-airflow-2.7.3-build.22




Change 


Cloud Composer 2.9.7 is a version with an extended upgrade timeline.



Deprecated 


Cloud Composer version 2.5.1 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



## October 30, 2024


Fixed 


*(Cloud Composer 3)* Airflow workers now generate a proper OpenID Connect (OIDC) token.



Change 


*(Airflow 2.9.3 and 2.7.3)* The `dbt-common` package was downgraded from 1.11.0 to 1.10.0.



Deprecated 


Cloud Composer version 2.5.0 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.3-build.5 (default)

- composer-3-airflow-2.7.3-build.21




Change 


Cloud Composer 2.9.9 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.9-airflow-2.9.3 (default)

- composer-2.9.9-airflow-2.7.3




## October 22, 2024


Change 


*(Only new Cloud Composer 2 environments, all versions)* If a GKE Control Plane IP range is specified for an environment, GKE creates a new subnetwork in this range to provision the IP address for communication with the GKE Control Plane. Otherwise, the subnetwork specified in the Cloud Composer connection subnetwork range is used (this range defaults to the environment's subnetwork). For more information about IP ranges used by Cloud Composer environments, see [Configure private IP networking](https://berlin.devsitetest.how/composer/docs/composer-2/configure-private-ip).



Change 


*(Airflow 2.9.3)* The `apache-airflow-providers-google` package was upgraded to version 10.24.0 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/10.24.0/commits.html) from version 10.23.0 to version 10.24.0.



Change 


*(Airflow 2.9.3)* The `apache-airflow-providers-cncf-kubernetes` package was upgraded to version 9.0.0 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-cncf-kubernetes changelog](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html) from version 8.4.2 to version 9.0.0.



Change 


*(Airflow 2.9.3 and 2.7.3)* Changes in preinstalled packages:

- The `grpcio` package was downgraded from 1.66.2 to 1.65.5.

- The `js2py` package was removed from dependencies.

- The `pyjsparser` package was removed from dependencies.

- The `tzlocal` package was removed from dependencies.




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.3-build.4 (default)

- composer-3-airflow-2.7.3-build.20




Change 


Cloud Composer 2.9.8 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.8-airflow-2.9.3 (default)

- composer-2.9.8-airflow-2.7.3




Deprecated 


Cloud Composer version 2.4.6 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



## October 16, 2024


Fixed 


Fixed a bug where upgrading a private IP environment could fail because of an invalid CIDR range.



Change 


The default version of Airflow is changed to 2.9.3.



Change 


Airflow 2.9.1 is no longer included in Cloud Composer images and builds.



Change 


Cloud Composer 2.9.7 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.7-airflow-2.9.3 (default)

- composer-2.9.7-airflow-2.7.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.3-build.3 (default)

- composer-3-airflow-2.7.3-build.19




## October 08, 2024


Change 


Cloud Composer 2.9.6 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.6-airflow-2.9.3

- composer-2.9.6-airflow-2.9.1 (default)

- composer-2.9.6-airflow-2.7.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.3-build.2

- composer-3-airflow-2.9.1-build.9 (default)

- composer-3-airflow-2.7.3-build.18




Deprecated 


Cloud Composer version 2.4.5 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



## October 01, 2024


Fixed 


*(Available without upgrading)* Fixed the cause of DAG run failures for runs created from the Cloud Console when the `[scheduler]allowed_run_id_pattern` Airflow configuration option is set to a custom value.



Change 


*(Airflow 2.9.3 and 2.9.1)* The `apache-airflow-providers-cncf-kubernetes` package was upgraded to version 8.4.2 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-cncf-kubernetes changelog](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html) from version 8.4.1 to version 8.4.2.



Change 


*(Airflow 2.9.3 and 2.9.1)* The `apache-airflow-providers-google` package was upgraded to version 10.23.0 in Cloud Composer 2 images and Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/10.23.0/commits.html) from version 10.22.0 to version 10.23.0.



Deprecated 


Cloud Composer version 2.4.4 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


Cloud Composer 2.9.5 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.5-airflow-2.9.3

- composer-2.9.5-airflow-2.9.1 (default)

- composer-2.9.5-airflow-2.7.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.3-build.1

- composer-3-airflow-2.9.1-build.8 (default)

- composer-3-airflow-2.7.3-build.17




## September 18, 2024


Fixed 


*(Cloud Composer 3)* Fixed the issue that caused KubernetesPodOperator tasks to fail if they ran for longer than 15 minutes.



Feature 


**Airflow 2.9.3** is available in Cloud Composer images.



Fixed 


*(Cloud Composer 2)* Fixed the issue where environment create and update operations could fail in rare cases because of the scheduler probe timeouts.



Deprecated 


Cloud Composer versions 2.4.2 and 2.4.3 have reached their [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


Cloud Composer 2.9.4 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.4-airflow-2.9.3

- composer-2.9.4-airflow-2.9.1 (default)

- composer-2.9.4-airflow-2.7.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.3-build.0

- composer-3-airflow-2.9.1-build.7 (default)

- composer-3-airflow-2.7.3-build.16




Change 


Support dates for previous Cloud Composer 3 builds are available. All Cloud Composer 3 builds with Airflow 2.9.1 are supported until September 18, 2025.



## September 02, 2024


Feature 


Added a new metric: `composer.googleapis.com/workflow/task_instance/queued_duration`. This metric is based on the `dag. . .queued_duration` [Airflow metric](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/metrics.html).



Fixed 


*(Cloud Composer 3)* Fixed the cause of false-positive failures of Airflow Celery workers reported by the liveness health check.



Fixed 


Fixed an issue where an upgrade of a PSC-based private IP environment failed leaving the environment in an inconsistent state.



Change 


The `apache-airflow-providers-cncf-kubernetes` package was upgraded to version 8.4.1 in Cloud Composer 2 images and Cloud Composer 3 builds with Airflow 2.9.1. For more information about changes, see the [apache-airflow-providers-cncf-kubernetes changelog](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html) from version 8.3.4 to version 8.4.1.



Change 


The `apache-airflow-providers-google` package was upgraded to version 10.22.0 in Cloud Composer 2 images and Cloud Composer 3 builds with Airflow 2.9.1. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/10.22.0/commits.html) from version 10.21.0 to version 10.22.0.



Change 


Cloud Composer 2.9.3 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.3-airflow-2.9.1 (default)

- composer-2.9.3-airflow-2.7.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.1-build.6 (default)

- composer-3-airflow-2.7.3-build.15




## August 27, 2024


Announcement 


*(Cloud Composer 2)* Starting on September 26, 2024, all Cloud Composer environments within a VPC SC perimeter will have **no access to public PyPI repositories by default**. For details about installing PyPI packages in the VPC SC mode, see [Installing PyPI packages](https://berlin.devsitetest.how/composer/docs/composer-2/configure-vpc-sc#pypi-packages).



## August 22, 2024


Fixed 


Fixed a bug where executing Airflow CLI commands produced output that was not human-readable.



Fixed 


*(Cloud Composer 3)* Fixed the `dags backfill` Airflow CLI command that was failing with a connection error.



Change 


The `apache-airflow-providers-google` package was upgraded to version 10.21.1 in Cloud Composer 2 images with Airflow 2.7.3 and 2.9.1, and in all latest Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/10.21.1/commits.html) from version 10.21.0 to version 10.21.1.



Deprecated 


Cloud Composer version 2.4.1 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.1-build.5

- composer-3-airflow-2.7.3-build.14




Change 


Cloud Composer 2.9.2 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.2-airflow-2.9.1 (default)

- composer-2.9.2-airflow-2.7.3




## August 13, 2024


Change 


*(Airflow 2.7.3)* Improved the reliability of connections between Airflow components and the Redis component.



Change 


Cloud Composer 2.9.1 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.1-airflow-2.9.1 (default)

- composer-2.9.1-airflow-2.7.3




Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.1-build.4

- composer-3-airflow-2.7.3-build.13




## August 08, 2024


Announcement 


The [kubelet read-only port in GKE clusters](https://berlin.devsitetest.how/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port) (TCP port 10255) is not used by Cloud Composer. You can define appropriate firewall rules to block external traffic over TCP 10255 in your customer project as described in [Modify VPC firewall rules](https://berlin.devsitetest.how/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port#modify-firewalls).



Change 


*(Airflow 2.9.1)* Improved the reliability of connections between Airflow components and the Redis component.



Fixed 


Fixed a problem that caused file synchronization between the bucket and Airflow components to be stuck or progress very slowly.



Change 


The default version of Airflow is changed to 2.9.1.



Deprecated 


Cloud Composer version 2.4.0 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.1-build.3

- composer-3-airflow-2.7.3-build.12




Change 


Cloud Composer 2.9.0 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.9.0-airflow-2.9.1 (default)

- composer-2.9.0-airflow-2.7.3




## August 01, 2024


Announcement 


*(Cloud Composer 3 only)* The [July 24th issue with Airflow upgrade operations for Cloud Composer 3 environments](https://berlin.devsitetest.how/composer/docs/release-notes#July_24_2024) is now fixed. Airflow upgrade operations are now being re-enabled, and should reach all Cloud Composer 3 environments within the next couple of days.



Announcement 


In July and August 2024, **new Cloud Composer 2 environments** keep switching to using GKE 1.29 and PSC as a connectivity channel to the GKE control plane. Creating new Cloud Composer 2 private IP environments will require using PSC `SERVICE_PRODUCER` endpoints, which might be blocked by the **Disable Private Service Connect for Consumers** organization policy constraint. Previously, this org policy limitation could be addressed by using VPC peerings instead of PSC, but starting from GKE 1.29, this workaround is no longer available.



Feature 


The initial synchronization of DAGs and plugins in Airflow workloads is performed in a separate container and utilizes full resources of the Pod.



Fixed 


*(Cloud Composer 3)* Fixed an error that happened when values in certain formats were used for Airflow configuration options.



Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.1-build.2

- composer-3-airflow-2.7.3-build.11




Deprecated 


Airflow 2.6.3 is no longer included in Cloud Composer 2 images.



Change 


Cloud Composer 2.8.8 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.8.8-airflow-2.9.1

- composer-2.8.8-airflow-2.7.3 (default)




## July 25, 2024


Fixed 


Cloud Composer now verifies that the environment's service account is enabled before starting an environment creation operation. As a result, this type of error is reported sooner and the operation does not start.



Deprecated 


Cloud Composer version 2.3.5 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.1-build.1

- composer-3-airflow-2.7.3-build.10




Change 


Cloud Composer 2.8.7 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.8.7-airflow-2.9.1

- composer-2.8.7-airflow-2.7.3 (default)

- composer-2.8.7-airflow-2.6.3




## July 24, 2024


Issue 


**2024-08-01 Update**: This issue has been resolved. For more information, see the [release note from August 1st 2024](https://berlin.devsitetest.how/composer/docs/release-notes#August_01_2024).

*(Cloud Composer 3 only)* We are currently experiencing an issue with the Airflow upgrade operations for Cloud Composer 3 environments. [Upgrading Airflow builds for Cloud Composer 3](https://berlin.devsitetest.how/composer/docs/composer-3/upgrade-environments#about-airflow-upgrades) is temporarily disabled as we continue our work to restore Airflow upgrade functionalities.



## July 18, 2024


Change 


Information about **excluded Cloud Storage objects in the environment's bucket** is no longer logged. This change reduces the usage of the Storage API during the synchronization of DAG files, which improves the performance of Airflow components and results in fewer Airflow component restarts. The change will gradually become available in all Cloud Composer environments.



## July 17, 2024


Change 


*(Airflow 2.9.1)* Task context logging is disabled, and it is not possible to enable it.



Change 


*(Airflow 2.9.1)* Raw HTML code in DAG docs and DAG parameter descriptions is disabled by default.



Change 


*(Airflow 2.9.1)* Audit log permissions are revoked from all roles except `Admin`.



Feature 


**Airflow 2.9.1** is available in Cloud Composer images and builds. We recommend checking the list of changes in [Apache Airflow release notes](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html) before upgrading to this version.



Change 


The upgraded `apache-airflow-providers-google` package provides new operators and sensors for triggering DAGs across Cloud Composer environments:

- **CloudComposerRunAirflowCLICommandOperator** makes a call to the Airflow REST API of a Cloud Composer environment.

- **CloudComposerDAGRunSensor** checks if a DAG Run is completed.




Change 


The `apache-airflow-providers-google` package was upgraded to version 10.21.0 in Cloud Composer 2 images with Airflow 2.7.3 and 2.9.1, and in all latest Cloud Composer 3 builds. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/10.21.0/commits.html) from version 10.18.0 to version 10.21.0.



Change 


When installing PyPI packages, if you want your builds to run with a custom service account, you can override the
`COMPOSER_AGENT_BUILD_SERVICE_ACCOUNT` environment variable with the chosen service account. For more information, see [Install Python dependencies](https://berlin.devsitetest.how/composer/docs/composer-2/install-python-dependencies).



Change 


New [Airflow builds](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) are available in Cloud Composer 3:

- composer-3-airflow-2.9.1-build.0

- composer-3-airflow-2.7.3-build.9




Deprecated 


Cloud Composer version 2.3.4 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



Change 


Cloud Composer 2.8.6 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.8.6-airflow-2.9.1

- composer-2.8.6-airflow-2.7.3 (default)

- composer-2.8.6-airflow-2.6.3




Change 


Support dates for previous Cloud Composer 3 builds are available. All Cloud Composer 3 builds with Airflow 2.7.3 are supported until July 17, 2025.



## July 15, 2024


Deprecated 


It is no longer possible to **create Cloud Composer 1 environments in Google Cloud console**. It's still possible to create Cloud Composer 1 environments through Google Cloud SDK, Terraform, and API in projects that support creating new Cloud Composer 1 environments.



## July 09, 2024


Change 


A new [Airflow build](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) is available in Cloud Composer 3:

- composer-3-airflow-2.7.3-build.8




Change 


Cloud Composer 2.8.5 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.8.5-airflow-2.7.3 (default)

- composer-2.8.5-airflow-2.6.3




## July 03, 2024


Change 


**New Cloud Composer 2 environments** are gradually switched to using GKE 1.29 and PSC as a connectivity channel to the GKE control plane. The IP address for the PSC endpoint will be taken from the nodes IP range. This change might require using a larger IP range for the nodes when you create an environment.



## July 02, 2024


Change 


Cloud Composer 2.8.4 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.8.4-airflow-2.7.3 (default)

- composer-2.8.4-airflow-2.6.3




Change 


A new [Airflow build](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) is available in Cloud Composer 3:

- composer-3-airflow-2.7.3-build.7




Issue 


**2024-07-03 Update**: Resolution status updated.

The [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387) vulnerability in the OpenSSH package issue was discovered recently. GKE clusters used by Cloud Composer environments are impacted by this vulnerability, and Cloud Composer 1 and 2 environments that use Public IP networking are especially vulnerable to the described issue. For more information about CVE-2024-6387, see [Google GKE Security bulletins](https://berlin.devsitetest.how/anthos/clusters/docs/security-bulletins#gcp-2024-040-gke).

- 

**Newly created** Composer environments should not be impacted by this issue any more

- 

Composer-owned GKE clusters will be auto-upgraded to newer GKE versions including the fix for [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387). Other components of Composer environments using older versions of [COS](https://berlin.devsitetest.how/compute/docs/security-bulletins#gcp-2024-040) images will also be upgraded. These operations will be done in an expedited manner so some of the update operations might be done outside environment's regular maintenance windows. 

While Google works on resolving this issue so Composer environments are immune to [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), you can disallow SSH to the Cloud Composer's cluster nodes through establishing proper firewall rules on the environment's cluster as described in the Google GKE Security bulletins. Follow the [steps outlined for GKE](https://berlin.devsitetest.how/anthos/clusters/docs/security-bulletins#gcp-2024-040-gke).



Deprecated 


Cloud Composer version 2.3.3 has reached its [end of support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



## June 25, 2024


Feature 


Cloud Composer is now available in Johannesburg (africa-south1).



## June 20, 2024


Feature 


​​We are thrilled to announce the Public Preview launch of the new generation of Cloud Composer, **Cloud Composer 3**. The new version is now publicly available in all regions supported by Cloud Composer. It comes with a number of new features and characteristics:

- All infrastructure hidden in a tenant project

- Evergreen versioning

- Simplified networking configuration

- Improved performance

- More reliable DAG parsing and scheduling as DAG Processor and Schedulers are now separate components

- 10 times bigger storage for Airflow workers

As well as most functionalities already known from the previous Composer versions. To see the list of features already supported by Composer 3, see [Comparison of Cloud Composer versions](https://berlin.devsitetest.how/composer/docs/composer-versioning-overview#comparison).



Feature 


*(Airflow 2.7.3)* New operators for executing jobs in Google Kubernetes Engine and Kubernetes are available. For example, you can use these operators [with Kueue](https://kueue.sigs.k8s.io/).

Operators for Google Kubernetes Engine:

- GKEStartJobOperator

- GKEStartKueueInsideClusterOperator

- GKEDescribeJobOperator

- GKEListJobsOperator

- GKECreateCustomResourceOperator

- GKEDeleteCustomResourceOperator

- GKEStartKueueJobOperator

- GKEDeleteJobOperator

- GKESuspendJobOperator

- GKEResumeJobOperator

Operators for Kubernetes:

- KubernetesJobOperator

- KubernetesPatchJobOperator

- KubernetesDeleteJobOperator




Change 


*(Airflow 2.7.3)* The `apache-airflow-providers-cncf-kubernetes` package was upgraded to version 8.3.1.



Change 


*(Airflow 2.7.3)* The `apache-beam` package was upgraded to version 2.56.0.



Change 


*(Airflow 2.7.3)* The `apache-airflow-providers-google` package was upgraded to version 10.18.0. For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/10.18.0/commits.html) from version 10.17.0 to version 10.18.0.



Change 


Cloud Composer 2.8.3 [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-2) are available:

- composer-2.8.3-airflow-2.7.3 (default)

- composer-2.8.3-airflow-2.6.3




Change 


A new [Airflow build](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions#images-composer-3) is available in Cloud Composer 3:

- composer-3-airflow-2.7.3-build.6




Change 


Cloud Composer 2.8.3 is a version with an extended upgrade timeline.



Deprecated 


Cloud Composer versions 2.3.2, 2.3.1, and 2.3.0 have reached their [end of full support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



## June 14, 2024


Feature 


[Environment upgrading](https://berlin.devsitetest.how/composer/docs/composer-2/upgrade-environments) is now generally available (GA)



## June 05, 2024


Change 


The `dbt-core` and `dbt-bigquery` packages were upgraded to version 1.8.1.



Change 


The `google-cloud-bigquery` package version was downgraded from 3.23.1 to 3.20.1 because of the [#39541](https://github.com/apache/airflow/issues/39541) issue in the public version of Airflow.



Change 


**Cloud Composer 2.8.2** [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions) are available:

- composer-2.8.2-airflow-2.7.3 (default)

- composer-2.8.2-airflow-2.6.3




Deprecated 


Cloud Composer versions 2.2.1, 2.2.0, and 2.1.15 have reached their [end of full support period](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versioning-overview#version-deprecation-and-support).



## May 27, 2024


Feature 


Cloud Composer 2 now supports [data lineage](https://berlin.devsitetest.how/composer/docs/composer-2/lineage-integration) for environments that have CMEK enabled.



Change 


**Cloud Composer 2.8.1** [images](https://berlin.devsitetest.how/composer/docs/concepts/versioning/composer-versions) are available:

- composer-2.8.1-airflow-2.7.3 (default)

- composer-2.8.1-airflow-2.6.3




## November 26, 2023


Feature 


Cloud Composer is now available in Dammam (me-central2).