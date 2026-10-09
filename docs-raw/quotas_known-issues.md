# Known issues

Source: https://berlin.devsitetest.how/docs/quotas/known-issues
Last updated: 2026-10-08

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://berlin.devsitetest.how/docs/quotas)






- 








[

Guides

](https://berlin.devsitetest.how/docs/quotas/overview)












# Known issues 






- On this page 
- [ Quota values during rollouts ](#quota_values_during_rollouts)
- [ Quota preference contactEmail field is required ](#quota_preference_contactemail_field_is_required)
- [ Cloud Quotas limitations in the Google Cloud Dedicated console ](#console_limitations)

- [ Requests for adjustments on quotas that have no usage ](#requests_for_adjustments_on_quotas_that_have_no_usage)
- [ Per-user quota usage doesn't appear ](#per-user_quota_usage_doesnt_appear)

- [ What's next ](#whats_next)
- 










The following are known issues within Cloud Quotas.

## Quota values during rollouts 

Google Cloud Dedicated in Germany sometimes increases the default quota values for resources and
APIs. These changes take place gradually, which means that during the rollout,
the quota value that appears in the Google Cloud Dedicated console or Cloud Quotas API
won't reflect the new, increased quota value until the rollout completes.

If a quota rollout is in progress, an informational message appears at the top
of the Cloud Quotas page and the rolling update indicator appears
next to the quota values impacted by ongoing rollouts.
For details, see
[View ongoing rollouts](/docs/quotas/view-ongoing-rollouts).

For troubleshooting steps, see
[Exceeding quota values during a service rollout](/docs/quotas/troubleshoot#exceeding_quota_values_during_a_service_rollout).

## Quota preference `contact Email` field is required

To update the `QuotaPreference` value through the Cloud Quotas API,
the `contactEmail` field is required. This email address cannot be a group
email.

For examples of using `QuotaPreference` in the API, see
[Implement common use cases](/docs/quotas/implement-common-use-cases).

## Cloud Quotas limitations in the Google Cloud Dedicated console

The following limitations apply when you use Cloud Quotas in the
Google Cloud Dedicated console.

### Requests for adjustments on quotas that have no usage

The Google Cloud Dedicated console doesn't support quota adjustment requests for quotas that
have no prior usage. However, you can still request a quota adjustment through
the REST API or Google Cloud CLI:


[gcloud](#gcloud) [REST](#rest) 
More 




Request a quota adjustment by [using the gcloud CLI](/docs/quotas/gcloud-cli-examples#request_a_quota_increase_adjustment_using_a_dimension)



Request a quota adjustment by [using the REST API](/docs/quotas/implement-common-use-cases#request_adjustments_on_quotas_that_have_no_usage)



For example, you might clone a project and know ahead of time that you need to
increase the value for
`compute.googleapis.com/local_ssd_total_storage_per_vm_family`. Although you
won't see that quota available in the Google Cloud Dedicated console, you can still
use the API or gcloud CLI to request a quota adjustment. For more information, see
[View ongoing rollouts](/docs/quotas/view-ongoing-rollouts).

### Per-user quota usage doesn't appear

The Google Cloud Dedicated console doesn't display per-user quota usage on the
Cloud Quotas page. If an application or service account exceeds
a per-user rate limit, then API requests return an HTTP
`429 Too Many Requests` status code, even when aggregate project-level metrics
on the Cloud Quotas page show that quota remains available.

To diagnose which user or service account is exhausting a per-user rate limit,
complete the following steps:

- In the Google Cloud Dedicated console, select the project that initiates the API requests,
and then go to the
[**Metrics Explorer**](https://console.cloud.berlin-build0.goog/monitoring/metrics-explorer) page.

- Click **Select a metric**, and then enter
`serviceruntime.googleapis.com/api/request_count` in the filter bar. In the
submenus, select **Consumed API  > Api  > 
Request count**, and then click **Apply**.

- In the **Filter** element, add filters for the response code and the target
service or API method:

- Click **Add filter**, and then select `response_code`. In the filter
dialog, leave **Comparator** set to **= (equals)**, enter `429` in the
**Value** field, and then click **Apply**.

- Click **Add filter** again, and then select either `service` (for
example, enter `sqladmin.googleapis.com` in the **Value** field for
Cloud SQL Admin API) or `method` (for example, enter
`google.cloud.sql.v1.SqlInstancesService.Get` in the **Value** field),
and then click **Apply**.

- In the **Aggregation** element, verify that the first menu is set to
**Sum**, and then in the second menu (next to **by**), select
`credential_id` to group requests by individual credential.

- In the results, find the credential ID (`credential_id`) with the highest
number of `429` response codes. This value is the OAuth 2.0 client ID of the
service account or user credential that is exhausting the per-user rate
limit.

- To find which service account corresponds to that client ID, go to the
[**Service accounts**](https://console.cloud.berlin-build0.goog/iam-admin/serviceaccounts) page in the
Google Cloud Dedicated console and search for the OAuth 2.0 client ID matching the
credential ID. The matching entry is the service account that is exhausting
the per-user rate limit.

To resolve the error after you identify the service account, implement
client-side caching or exponential backoff in the client application,
distribute workloads across distinct service accounts, or
[request a quota adjustment](/docs/quotas/help/request_increase).

## What's next

- [Troubleshoot quota errors](/docs/quotas/troubleshoot)

- [Billing questions](/docs/quotas/billing-questions)

- [View and manage quotas](/docs/quotas/view-manage)