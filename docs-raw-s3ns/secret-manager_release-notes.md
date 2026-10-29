# Secret Manager release notes

Source: https://documentation.s3ns.fr/secret-manager/docs/release-notes
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/secret-manager/docs/tpc-differences) for more details.














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

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Secret Manager

](https://documentation.s3ns.fr/secret-manager/docs)






- 








[

Resources

](https://documentation.s3ns.fr/secret-manager/docs/resources)












# Secret Manager release notes 



















This page documents production updates to Secret Manager. Check this page for
announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

For updates to the Secret Manager integration with
Google Kubernetes Engine (GKE), including the Secret Manager add-on and
secret synchronization, see
[GKE integration release notes](/secret-manager/docs/gke-release-notes).







You can see the latest product updates for all of Cloud de Confiance by S3NS on the
[
Cloud de Confiance](/release-notes) page, browse and filter all release notes in the
[Cloud de Confiance console](https://console.cloud.s3nscloud.fr/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.s3nscloud.fr/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://documentation.s3ns.fr/feeds/secretmanager-release-notes.xml) directly.









## August 07, 2026


Feature 


Secret Manager is generally available in your Google Cloud Dedicated universe.



## April 04, 2025


Feature 


The Secret Manager add-on for Google Kubernetes Engine (GKE) now supports the automatic rotation of secrets. You can configure the Secret Manager add-on to automatically rotate secrets so that secrets updated in Secret Manager after initial pod deployment are automatically and periodically pushed to the pod. This feature is available in [Preview](https://documentation.s3ns.fr/products#product-launch-stages). 

For more information, see [Configure automatic rotation of secrets](/secret-manager/docs/secret-manager-managed-csi-component#configure_automatic_rotation_of_secrets).



## March 03, 2025


Feature 


Secret Manager is now available in the following region:

- europe-north2 (Stockholm)

For more information, see [Secret Manager locations](/secret-manager/docs/locations).



## February 28, 2025


Feature 


Parameter Manager, currently in [Preview](https://documentation.s3ns.fr/products#product-launch-stages), now offers a console for storing, accessing, and managing the lifecycle of your workload parameters. For more information, see the [Parameter Manager documentation](/secret-manager/parameter-manager/docs/create-parameter).



## December 06, 2024


Feature 


Parameter Manager, an extension to the Secret Manager service, is available in [Preview](https://documentation.s3ns.fr/products#product-launch-stages). You can use Parameter Manager to store, access, and manage the lifecycle of your workload parameters. For more information, see [Parameter Manager overview](/secret-manager/parameter-manager/docs/overview).



## November 19, 2024


Feature 


Creating [custom organization policies](/resource-manager/docs/organization-policy/overview#custom-organization-policies) with Secret Manager resources is now in General Availability ([GA](https://documentation.s3ns.fr/products#product-launch-stages)). You can use custom organization policies to enhance secret security by enforcing rotation schedules, annotations, and expirations for secrets. You can also use custom organization policies to restrict secret types to manage costs. To learn more about using custom organization policies in Secret Manager, see [Use custom organization policies](/secret-manager/docs/secret-manager-custom-constraints).



## November 17, 2024


Feature 


Secret Manager is now available in the following region:

- northamerica-south1

For more information, see [Secret Manager locations](/secret-manager/docs/locations).



## October 14, 2024


Feature 


Creating regional secrets using Secret Manager is now in Generally Availability ([GA](https://documentation.s3ns.fr/products#product-launch-stages)). Regional secrets let you store your sensitive data within a specific geographic location, ensuring it remains in that region at all times – whether at rest, in use, or in transit. Regional secrets are crucial for meeting data residency requirements and complying with regulatory mandates.

For information about all tasks related to creating and managing regional secrets, see the [Regional service documentation](/secret-manager/regional-secrets/global-regionalized-service-comparison).



## September 10, 2024


Feature 


Secret Manager is now enabled for use with Cloud KMS Autokey.

Using keys generated by Autokey can help you consistently align with industry
standards and recommended practices for data security, including the HSM
protection level, separation of duties, key rotation, location, and key
specificity. Keys requested using Autokey function identically to other
Cloud HSM keys with the same settings.

For more information, see [Enable customer-managed encryption keys for Secret Manager](/secret-manager/docs/cmek). To learn more
about Cloud KMS Autokey, see
[Autokey overview](/kms/docs/autokey-overview).



## August 23, 2024


Feature 


You can now create regional secrets using Secret Manager. When you create a regional secret, you specify the location where you want it to be stored. Your secret data remains within the chosen location at all times, whether it's at rest, in use, or in transit. This capability allows you to meet data residency requirements, which mandate that data remains within specified geographic boundaries, often due to regulatory or compliance reasons. The feature is in [Preview](https://documentation.s3ns.fr/products#product-launch-stages). 

For more information, see [Data residency and regional secrets](/secret-manager/docs/regional-secrets-overview).



## August 21, 2024


Feature 


You can attach tags to secrets to conditionally grant or deny access to Secret Manager resources. For example, you can conditionally grant Identity and Access Management (IAM) roles based on whether a secret has a specific tag. This feature is in [Preview](http://documentation.s3ns.fr/products#product-launch-stages). For more information, see [Create and manage tags](/secret-manager/docs/create-and-manage-tags).



## August 20, 2024


Feature 


Secret Manager add-on for Google Kubernetes Engine (GKE) is now generally available ([GA](https://documentation.s3ns.fr/products#product-launch-stages)). With the add-on, you can access the secrets stored in Secret Manager as volumes mounted in Kubernetes Pods. You can install the Secret Manager add-on on both Standard clusters and Autopilot clusters. The Secret Manager add-on is a Google managed and officially supported version of the open source Kubernetes Secrets Store CSI driver. 

For more information, see [Use Secret Manager add-on with Google Kubernetes Engine](/secret-manager/docs/secret-manager-managed-csi-component).



## June 12, 2024


Feature 


Delayed destruction of secret versions is now [generally available (GA)](https://documentation.s3ns.fr/products#product-launch-stages). You can [set up a duration for delayed destruction](/secret-manager/docs/delay-destruction-of-secret-versions#set-up-delay-duration) at the time of creating or updating a secret. When a destruction delay duration is configured for a secret, destroying a version of that secret will disable the version and prevent its use. However, it won't be immediately destroyed. Instead, it will remain scheduled for destruction for the specified delay duration. After that duration expires, the version will be permanently destroyed. Secret Manager administrators can restore a secret version that is scheduled for destruction by either enabling or disabling it during the delay period.