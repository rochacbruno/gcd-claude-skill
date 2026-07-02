# Cloud KMS release notes

Source: https://berlin.devsitetest.how/kms/docs/release-notes
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/kms/docs/tpc-differences) for more details.














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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

Cloud KMS

](https://berlin.devsitetest.how/kms/docs)






- 








[

Resources

](https://berlin.devsitetest.how/kms/docs/resources)












# Cloud KMS release notes 






- On this page 
- [ February 21, 2025 ](#February_21_2025)
- [ October 18, 2024 ](#October_18_2024)
- [ June 14, 2024 ](#June_14_2024)
- 














This page documents production updates to Cloud Key Management Service. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

**Current version: v1**







You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/kms-release-notes.xml) directly.









## February 21, 2025 


Feature 


Cloud KMS now supports the following post-quantum computing (PQC) algorithms for digital signatures in Public Preview:

- `PQ_SIGN_ML_DSA_65`: Module-lattice-based digital signature algorithm

- `PQ_SIGN_SLH_DSA_SHA2_128S`: Stateless hash-based digital signature algorithm

To [Retrieve a public key](/kms/docs/retrieve-public-key) for a PQC key, you must use the `gcloud` CLI or the Cloud KMS REST API.

- For the `gcloud` CLI, use the `--public-key-format nist-pqc` flag.

- For the REST API, use the `public_key_format=NIST_PQC` header parameter.

For more information about PQC algorithms, see [PQC signing algorithms](/kms/docs/algorithms#pqc_signing_algorithms). For more information about PQC digital signatures, see [Post-quantum cryptography (PQC) digital signature](/kms/docs/digital-signatures#pqc).



## October 18, 2024


Feature 


You can now use custom constraints with Organization Policy to provide more granular control over specific fields for some Cloud KMS resources. For more information, see [Create custom organization policy constraints for Cloud KMS](/kms/docs/custom-org-policies).



## June 14, 2024


Change 


As previously announced, Cloud KMS has changed the default duration of the scheduled for destruction period from 24 hours to 30 days.

As of February 1, 2024, newly created CryptoKeys use the new default duration of 30 days, unless a different duration is specified during key creation. For more information about key destruction, see [Destroy and restore key versions](/kms/docs/destroy-restore).

Owners of existing CryptoKeys that had used the default duration were given until May 1, 2024 to opt out from automatically updating those keys to use the new default duration. Existing CryptoKeys that were not opted out have been updated to use the new default duration of 30 days. No further action is required from you.