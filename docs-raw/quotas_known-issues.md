# Known issues

Source: https://berlin.devsitetest.how/docs/quotas/known-issues
Last updated: 2026-06-18

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

The Google Cloud Dedicated console doesn't display per-user quota usage.

## What's next

- [Troubleshoot quota errors](/docs/quotas/troubleshoot)

- [Billing questions](/docs/quotas/billing-questions)

- [View and manage quotas](/docs/quotas/view-manage)