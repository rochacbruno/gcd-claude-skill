# IAM release notes

Source: https://berlin.devsitetest.how/iam/docs/release-notes
Last updated: 2026-07-21

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

IAM

](https://berlin.devsitetest.how/iam/docs)






- 








[

Resources

](https://berlin.devsitetest.how/iam/docs/resources)












# IAM release notes 






- On this page 
- [ September 12, 2025 ](#September_12_2025)
- [ June 13, 2025 ](#June_13_2025)
- [ May 28, 2025 ](#May_28_2025)
- [ May 15, 2025 ](#May_15_2025)
- [ May 07, 2025 ](#May_07_2025)
- [ December 09, 2024 ](#December_09_2024)
- [ September 12, 2024 ](#September_12_2024)
- [ August 12, 2024 ](#August_12_2024)
- [ July 30, 2024 ](#July_30_2024)
- [ June 10, 2024 ](#June_10_2024)
- [ May 08, 2024 ](#May_08_2024)
- 














This page documents production updates to Identity and Access Management. Check this page for
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
[feed URL](https://berlin.devsitetest.how/feeds/iam-release-notes.xml) directly.









## September 12, 2025


Feature 


IAM offers predefined roles that are tailored to specific job functions. These roles cover all of the permissions that a user might need to perform their job. This feature is [generally available](https://berlin.devsitetest.how/products#product-launch-stages).

For more information, see [Predefined roles for job functions](/iam/docs/job-functions/roles-for-job-functions).



## June 13, 2025


Change 


Conditions that check the tags for a resource can also check other attributes, such as the resource name of the timestamp of the request. This feature is available in Preview. For more information, see [Resource tags](/iam/docs/conditions-attribute-reference#resource-tags).



## May 28, 2025


Feature 


Workforce Identity Federation supports [detailed audit logging](/iam/docs/workforce-identity-federation#detailed-audit-logging), which you can use to troubleshoot attribute mapping issues. This feature is [generally available](https://berlin.devsitetest.how/products#product-launch-stages).



## May 15, 2025


Change 


The predefined role reference and the permissions reference have been reorganized to improve performance and searchability. To see the new experience, visit the [IAM roles and permissions index](/iam/docs/roles-permissions).



## May 07, 2025


Feature 


[Workload Identity Federation support for X.509 certificates](/iam/docs/workload-identity-federation-with-x509-certificates) is [generally available](https://berlin.devsitetest.how/products#product-launch-stages).



## December 09, 2024


Change 


Using IAM attributes in custom organization policies is generally available. For more information, see [Use custom organization policies](/iam/docs/org-policy-custom-constraints).



Feature 


You can use the `iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts` managed organization policy constraint to prevent default service accounts from being granted the Editor (`roles/editor`) or Owner (`roles/owner`) roles. For more information, see [Prevent the Owner and Editor role from being granted to default service accounts](/resource-manager/docs/organization-policy/restricting-service-accounts#prevent-service-account-grants).



## September 12, 2024


Change 


You can manage IAM deny policies using the Google Cloud console. For more information, see [Deny access to resources](/iam/docs/deny-access).



## August 12, 2024


Feature 


You can attach tags to Identity and Access Management (IAM) service accounts to conditionally grant or deny access to specific service accounts. This feature is in [Preview](https://berlin.devsitetest.how/products#product-launch-stages). For more information, see [Creating and managing tags for service accounts](/iam/docs/service-accounts-tags).



## July 30, 2024


Feature 


You can use IAM attributes in custom organization policies to control how your allow policies can be modified. For more information, see [Use custom organization policies](/iam/docs/org-policy-custom-constraints).



## June 10, 2024


Feature 


You can use [principal access boundary policies](/iam/docs/principal-access-boundary-policies) to limit the resources that a principal is eligible to access. This feature is available in Preview.



## May 08, 2024


Feature 


[Privileged Access Manager (PAM)](/iam/docs/pam-overview) lets you manage just-in-time temporary privilege elevation for select principals, and to view audit logs afterwards to find out who had access to what and when. This feature is in Preview.