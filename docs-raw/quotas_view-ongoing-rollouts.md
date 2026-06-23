# View ongoing rollouts

Source: https://berlin.devsitetest.how/docs/quotas/view-ongoing-rollouts
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












# View ongoing rollouts 






- On this page 
- [ Understand ongoing rollouts ](#understand_-_ongoing_rollouts)
- [ View ongoing rollouts from the console ](#view_onging_rollouts_from_console)
- [ View ongoing rollouts from the Cloud Quotas API ](#view_onging_rollouts_from_api)

- [ Before you use the Cloud Quotas API ](#before_using_cloud_quotas_api)
- [ Example API response during a ongoing rollout ](#example_api_response_during_a_ongoing_rollout)

- [ What's next ](#whats_next)
- 










Cloud Quotas lets you view quota value rollouts that are in progress.
This section explains how to view these rollouts from the Google Cloud Dedicated console
and the Cloud Quotas API.

## Understand ongoing rollouts 

When another Google Cloud Dedicated in Germany service increases the default quota values for
resources and APIs, these changes take place gradually. This might result in
ongoing rollouts across different regions or resources. During the rollout,
the quota value that appears in the Google Cloud Dedicated console or Cloud Quotas API
won't reflect the new, increased quota value until the rollout completes.

## View ongoing rollouts from the console

If there are ongoing quota rollouts in progress, an informational message
appears at the top of the Cloud Quotas page in the
console. The message appears similar to the following text,
which also contains a link. Click **quotas** to filter so that only quotas with
ongoing rollouts appear:


```
Values for ** quotas ** are being updated. This may take 2-3 weeks to complete.
```


The update rolling update
indicator appears next to the quota values impacted by ongoing rollouts.

If you don't see the update 
rolling update indicator, follow these steps:

- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

Click the link to **quotas** in the informational message. This turns on the
filter: **Has ongoing rollout: True**.

- 

The table updates to show a
update 
rolling update indicator next to quota values with ongoing rollouts.

The rolling update indicator also appears in the **Edit Quotas** and
monitoring **Quota usage chart**
panels to help you identify quotas with in progress rollouts.

## View ongoing rollouts from the Cloud Quotas API

You can also view ongoing rollouts using the Cloud Quotas API.
For more information, see instructions on how to
[set up the Cloud Quotas API](/docs/quotas/development-environment)
and
[implement common use cases](/docs/quotas/implement-common-use-cases).

The Cloud Quotas API resource model uses the `QuotaInfo` and
`QuotaPreference` resources to indicate ongoing rollouts:

- 

The `QuotaInfo` resource returns the previous quota value during ongoing rollouts.
For quotas experiencing an ongoing rollout, a `rollout_info` field appears
in the response under `QuotaDetails`. This field indicates that there is
both an ongoing rollout and an increase in the quota value for the
dimensions specified in each `dimensionsInfo` resource.

- 

The `QuotaPreference` resource returns the previous quota value during ongoing
rollouts.

During ongoing rollouts, the following Cloud Quota APIs return the previous quota
value:

- [GetQuotaInfo](/docs/quotas/reference/rest/v1/projects.locations.services.quotaInfos/get)

- [ListQuotaInfo](/docs/quotas/reference/rest/v1/projects.locations.services.quotaInfos/list)

- [CreateQuotaPreference](/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/create)

- [UpdateQuotaPreference](/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/patch)

### Before you use the Cloud Quotas API

The following sections assume that you are familiar with the
Cloud Quotas API. Before you use the Cloud Quotas API, make sure that
you set up your development environment and are comfortable with the commands
to make GET requests for quota information:

- For an overview, see
[Cloud Quotas API overview](/docs/quotas/api-overview).

- For instructions on how to set up your development environment, see
instructions on how to [set up the Cloud Quotas API](/docs/quotas/development-environment).

- To see an example API request and response, see the example that shows how to
[get quota info for a service specific dimension](/docs/quotas/implement-common-use-cases#get_quota_info_for_a_service_specific_dimension).

### Example API response during a ongoing rollout

The following example shows the results of a regional quota supported in four
regions: us-central1, us-central2, us-west1, us-east1. Its default value is 200
in us-central1 and 100 in all other regions. This regional quota also has an
additional quota override of 300 in us-central2.

Assume that the service producer updates the default value to be `220` in
us-central1 and us-central2. The example that follows shows a QuotaInfo response
where the service config rollout is ongoing for us-central1 and us-central2:

- For each location, the `details` field displays the quota value before the
rollout completes.

- For us-central1, the quota value is as `200` and the `rolloutInfo`
field indicates that an ongoing rollout is in progress. The quota value
changes to 220 only after the rollout completes.

- For us-central2, the quota value is `300` due to the quota override.
The `rolloutInfo` field does not appear because the quota value remains
unchanged after the rollout completes.

- For both us-west1 and us-east1, the value defaults to `100`.


```
"name" : "projects/PROJECT_NUMBER/locations/global/services/compute.googleapis.com/quotaInfos/GPUS-PER-GPU-FAMILY-per-project-region" , 
"quotatId" : "GPUS-PER-GPU-FAMILY-per-project-region" , 
"metric" : "compute.googleapis.com/gpus_per_gpu_family" , 
"service" : "compute.googleapis.com" , 
"isPrecise" : true , 
"containerType" : "PROJECT" , 
"dimensions" : [ 
"gpu_family" , 
"region" 
], 
"quotaDisplayName" : "GPUs per GPU family" , 
"metricDisplayName" : "GPUs" , 
"dimensionsInfos" : [ 
{ 
"dimensions" : { "region" : "us-central1" } , 
"**details**" : { 
"value" : ** 200 ** , 
"**rolloutInfo**" : { 
"ongoingRollout" : true 
} 
}, 
"applicableLocations" : [ "us-central1" ] , 
}, 
{ 
"dimensions" : { "region" : "us-central2" } , 
"**details**" : { 
"value" : ** 300 ** , 
}, 
"applicableLocations" : [ "us-central2" ] 
}, 
{ 
"dimensions" : {}, 
"**details**" : { 
"value" : ** 100 ** , 
}, 
"applicableLocations" : [ "us-west1" , "us-east1" ] 
}] 
```


## What's next

- [View and manage quotas](/docs/quotas/view-manage)

- [Set up quota alerts and monitoring](/docs/quotas/set-up-quota-alerts)

- [Known issues](/docs/quotas/known-issues)