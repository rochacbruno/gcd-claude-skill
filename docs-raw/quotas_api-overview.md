# Cloud Quotas API overview

Source: https://berlin.devsitetest.how/docs/quotas/api-overview
Last updated: 2026-07-10

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












# Cloud Quotas API overview 






- On this page 
- [ Limitations ](#limitations)
- [ Service endpoint ](#service_endpoint)
- [ Required roles ](#required_roles)
- [ API resource model ](#api_resource_model)

- [ Quota preference ](#quota_preference)
- [ Quota info ](#quota_info)
- [ Quota adjuster settings ](#quota_adjuster_settings)

- [ Resource names ](#resource_names)

- [ Quota preference resource ](#quota_preference_resource)
- [ Quota info resource ](#quota_info_resource)
- [ Quota adjuster settings resource ](#quota_adjuster_settings_resource)

- [ What's next? ](#whats_next)
- 










The Cloud Quotas API lets you programmatically adjust project-level
[quotas](/docs/quotas/overview) 
and automate project-level quota [adjustment requests](/docs/quotas/overview#about_increase_requests). For
example, you can use the Cloud Quotas API to:

- 

**Automate quota adjustments**: You can use the Cloud Quotas API to request quota
adjustments based on your own criteria. For example, to avoid quota
exceeded errors, you can use the API to programmatically request a quota
adjustment when Compute Engine resources reach 80% of the available quota.

- 

**Reuse quota configurations across projects**: The Cloud Quotas API can clone
your quota configurations from project to project. If there is a known set of
quotas that need to be increased for every new Google Cloud Dedicated in Germany project, you can
use the Cloud Quotas API to automate this in the creation logic of your project.
Quota adjustment requests are subject to Google Cloud Dedicated in Germany approval.

- 

**Serve customer quota requests**: If you are a SaaS provider integrated with
Google Cloud Dedicated in Germany, you might receive quota increase requests through a
customer-facing portal other than the Google Cloud Dedicated console. These requests must be
forwarded to Google Cloud Dedicated in Germany for processing. The Cloud Quotas API can automatically
forward customer requests.

- 

**Enable client configuration version control**: The Cloud Quotas API is
declarative. You can treat quota configurations as code and store
configurations in your own version controlled system for history and rollback.

## Limitations

Cloud Quotas has the following limitations:

- 

In most cases, quota *increase* adjustments must be made at the
[project-level](/resource-manager/docs/creating-managing-projects).
A limited number of products support
[organization-level](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations)
quota increase adjustments. To see if a Google Cloud Dedicated in Germany product supports
organization-level quota increase adjustments, refer to the documentation
for that product.

- 

You can request quota *decrease* adjustments for
project-, organization-, and
[folder-level](/resource-manager/docs/cloud-platform-resource-hierarchy#folders)
quotas.

## Service endpoint

The service endpoint is a base URL that specifies the network address of an API
service. One service might have multiple endpoints. The Cloud Quotas API
service has the following endpoint and all URIs are relative to it:

`https://cloudquotas.googleapis.com`

## Required roles











































































































To get the permissions that
you need to access the `cloudquotas_quotaPreferences`, `cloudquotas_quotaInfos`, and `cloudquotas_quotaAdjusterSettings` resources,

ask your administrator to grant you the
Cloud Quotas Admin (`cloudquotas.admin`)
IAM role on the project.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).








This predefined role contains

the permissions required to access the `cloudquotas_quotaPreferences`, `cloudquotas_quotaInfos`, and `cloudquotas_quotaAdjusterSettings` resources. To see the exact permissions that are
required, expand the **Required permissions** section:





#### Required permissions




The following permissions are required to access the `cloudquotas_quotaPreferences`, `cloudquotas_quotaInfos`, and `cloudquotas_quotaAdjusterSettings` resources:






- 
`cloudquotas.quotas.update`



- 
`cloudquotas.quotas.get`



- 
`monitoring.timeSeries.list`



- 
`resourcemanager.projects.get`



- 
`resourcemanager.projects.list`














You might also be able to get
these permissions
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









## API resource model

The Cloud Quotas API resource model consists of two resources:
`QuotaPreference` and `QuotaInfo`.

### Quota preference

The `QuotaPreference` resource represents your quota preference for a particular
[dimension combination](/docs/quotas/configure-dimensions#dimension_precedence). Use
this resource to adjust the quotas in your projects, folders, or organizations.

#### Set a preferred value for a region

The following example shows a `QuotaPreference` resource in a
`CreateQuotaPreference` method.


```
{ 
"service" : "compute.googleapis.com" , 
"quotaId" : "GPUS-PER-GPU-FAMILY-per-project-region" , 
"quotaConfig" : { 
"preferredValue" : 100 
}, 
"dimensions" : { 
"region" : "us-central1" 
} 
} 
```


The `preferredValue` of 100 indicates that the
requester wants the `GPUS-PER-GPU-FAMILY-per-project-region` quota to be set to
that value. The dimensions field indicates the preference only applies to region
`us-central1`.

#### Verify the granted value

View your quota preference and look at the `grantedValue` field to verify the
granted value.

To view your quota preference using the Google Cloud CLI, run the following in
your terminal:


```
gcloud alpha quotas preferences describe QUOTA_PREFERENCE_ID --project = PROJECT 
```


Replace the following:

- ` QUOTA_PREFERENCE_ID `: the ID of your quota preference.
This is the value that was specified when the quota preference was created.

- ` PROJECT `: the ID or number of your Google Cloud Dedicated in Germany
project.

If you made a quota adjustment request and the request is partially approved,
a `stateDetail` field appears after the `grantedValue` field. The
`grantedValue` shows the adjustment that was made, and the `stateDetail` field
describes the partially approved state.

To see if the granted value is the final value approved, look at the
`reconciling` field. If your request is still undergoing evaluation, the
`reconciling` field is set to `true`. If the `reconciling` field is set to
`false` or is omitted, the granted value is the final value approved.

The following code snippets show examples of the quota preference object. They
use a demo quota preference with the ID
`compute_googleapis_com-gpus-us-central1`.


[gcloud](#gcloud) [REST](#rest) 
More 




If you view your quota preference using the gcloud CLI, the
output looks similar to the following:


```
createTime: '2023-01-15T01:30:15.01Z'
dimensions:
region: us-central1
name: projects/ PROJECT_NUMBER /locations/global/quotaPreferences/compute_googleapis_com-gpus-us-central1
quotaConfig:
grantedValue: '100'
preferredValue: '100'
traceId: 123acd-345df23
requestOrigin: ORIGIN_UNSPECIFIED
service: compute.googleapis.com
quotaId: GPUS-PER-GPU-FAMILY-per-project-region
updateTime: '2023-01-16T02:35:16.01Z'
```



If you view your quota preference using the Cloud Quotas API, the
output looks similar to the following:


```
{ 
"name" : "projects/ PROJECT_NUMBER /locations/global/quotaPreferences/compute_googleapis_com-gpus-us-central1" , 
"service" : "compute.googleapis.com" , 
"quotaId" : "GPUS-PER-GPU-FAMILY-per-project-region" , 
"quotaConfig" : { 
"preferredValue" : 100 , 
"grantedValue" : 100 , 
"traceId" : "123acd-345df23" , 
"requestOrigin" : "ORIGIN_UNSPECIFIED" 
}, 
"dimensions" : { 
"region" : "us-central1" 
}, 
"createTime" : "2023-01-15T01:30:15.01Z" , 
"updateTime" : "2023-01-16T02:35:16.01Z" 
} 
```



This output includes the following values:

- ` PROJECT_NUMBER `: an automatically generated
unique identifier for your project.

The response shows a `grantedValue` of 100, meaning
the `preferredValue` from the previous example has been approved and fulfilled.
Preferences for different dimensions are different `QuotaPreference`
resources. For example, `QuotaPreference` for CPU in regions `us-central1` and
`us-east1` are two distinct resources.

#### Quota preference is required

`QuotaPreference` resources are used to indicate your preferred value for a
particular quota. The current value for a particular quota is based on:

- 

`QuotaPreference` requests made by you.

- 

Approved quota increase requests by Google Cloud Dedicated in Germany.

- 

Changes to quotas initiated by Google Cloud Dedicated in Germany.

The ability to delete a `QuotaPreference` is not supported. However, you can set
a preferred quota value lower than the Google Cloud Dedicated in Germany approved value to add further guardrails.

For more information on the `QuotaPreference` resource, see the [Cloud Quotas API Reference](/docs/quotas/reference/rest).

For more information on the `QuotaPreference` queries, see
[Implement common use cases](/docs/quotas/implement-common-use-cases).

### Quota info

`QuotaInfo` is a read-only resource that provides information about a particular
quota for a given project, folder, or organization. It displays information from
the quotas defined by Google Cloud Dedicated in Germany services and any fulfilled quota
adjustments initiated by customers. The `QuotaInfo` resource contains
information such as the metadata, container type, and dimensions.

#### Set different quota values by region

The following `QuotaInfo` resource example shows that the CPU quota for the
project is 200 for region `us-central1` and 100 for all other regions.


```
{ 
"name" : "projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos/CPUS-per-project-region" , 
"quotaId" : "CPUS-per-project-region" , 
"metric" : "compute.googleapis.com/cpus" , 
"containerType" : "PROJECT" , 
"dimensions" : [ 
"region" 
], 
"isPrecise" : true , 
"quotaDisplayName" : "CPUs per project per region" , 
"metricDisplayName" : "CPUs" , 
"dimensionsInfo" : [ 
{ 
"dimensions" : { 
"region" : "us-central1" 
}, 
"details" : { 
"quotaValue" : 200 , 
"resetValue" : 200 
}, 
"applicableLocations" : [ 
"us-central1" , 
] 
}, 
{ 
"details" : { 
"quotaValue" : 100 , 
"resetValue" : 100 
}, 
"applicableLocations" : [ 
"us-central2" , 
"us-west1" , 
"us-east1" 
] 
} 
] 
} 
```


This output includes the following values:

- ` PROJECT_NUMBER `: an automatically generated
unique identifier for your project.

#### Set a global quota

The following `QuotaInfo` resource example shows a rate quota with a per minute
refresh interval. The dimensions are blank, which indicates that this is a
global quota. All quotas without a region or zone dimension are global.


```
{ 
"name" : "projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos/ReadRequestsPerMinutePerProject" , 
"quotaId" : "ReadRequestsPerMinutePerProject" , 
"metric" : "compute.googleapis.com/read_requests" , 
"refreshInterval" : "minute" , 
"containerType" : "PROJECT" , 
"dimensions" : [], 
"isPrecise" : false , 
"quotaDisplayName" : "Read Requests per Minute" , 
"metricDisplayName" : "Read Requests" , 
"dimensionsInfo" : [ 
{ 
"details" : { 
"quotaValue" : 100 , 
"resetValue" : 200 
}, 
"applicableLocations" : [ 
"global" 
] 
} 
] 
} 
```


This output includes the following values:

- ` PROJECT_NUMBER `: an automatically generated
unique identifier for your project.

For more details on the `QuotaInfo` resource, see the [Cloud Quotas API Reference](/docs/quotas/reference/rest).

For more details on the `QuotaPreference` queries, see
[Implement common use cases](/docs/quotas/implement-common-use-cases).

### Quota adjuster settings

The `QuotaAdjusterSettings` resource ([Preview](https://berlin.devsitetest.how/products#product-launch-stages))
represents your quota adjuster settings for a particular project. When enabled,
the quota adjuster monitors your usage of the specified resources and issues
quota adjustment requests when resource use approaches its quota value.

- 

To view the current quota adjuster settings for a project, use a
[GET](/docs/quotas/reference/rest/v1beta/projects.locations.quotaAdjusterSettings/getQuotaAdjusterSettings)
operation to retrieve the `QuotaAdjusterSettings` resource.

- 

To enable quota adjuster for a project, use an
[PATCH](/docs/quotas/reference/rest/v1beta/projects.locations.quotaAdjusterSettings/updateQuotaAdjusterSettings)
operation to set the following `QuotaAdjusterSettings` resource options:


```
"quota_adjuster_settings" :{ 
"name" : "projects/ PROJECT_NUMBER /locations/global/quotaAdjusterSettings" , 
"enablement" : ENABLED , 
} 
```


Replace ` PROJECT_NUMBER ` with the unique identifier for
your project.

For details,
see [Enable the quota adjuster](/docs/quotas/quota-adjuster#enable)
and [Disable the quota adjuster](/docs/quotas/quota-adjuster#disable).

## Resource names

Resources are named entities and are identified by resource names. Resource
names are used in all requests and responses, and each resource must have
its own unique resource name. Each resource name is encoded by a set of fields.

### Quota preference resource

The naming convention for a `QuotaPreference` resource uses the following pattern:


```
projects/ PROJECT_NUMBER /locations/global/quotaPreferences/ QUOTA_PREFERENCE_ID 
```


You can set the `quotaPreferenceId` when creating a quota preference, otherwise
an ID is generated. It is recommended that a `quotaPreferenceId` naming scheme
encodes the service name, quota ID, location and other dimensions. The
`quotaPreferenceId` must be unique for the project, folder, or organization.

As an example `quotaPreference`
One pattern to encode your quota preference ID is the following:


```
SERVICE _ LOCATION _ DIMENSION1-VALUES-IN-ORDER 
```


The following example demonstrates this pattern:


```
compute_us-central1_nvidia-200
```


With a resource name, you should use the
[`GET`](/docs/quotas/reference/rest/v1beta/organizations.locations.quotaPreferences/get)
method to retrieve a `QuotaPreference`. You can also call the
[`PATCH`](/docs/quotas/reference/rest/v1beta/organizations.locations.quotaPreferences/patch)
method with the `allow_missing` option enabled to create or update a
`QuotaPreference`.

### Quota info resource

The naming convention for a `QuotaInfo` resource uses the following pattern:


```
projects/ PROJECT_NUMBER /locations/global/services/ SERVICE_NAME /quotaInfos/ QUOTA_ID 
```


### Quota adjuster settings resource

The naming convention for a `QuotaAdjusterSettings` resource uses the following pattern:


```
projects/ PROJECT_NUMBER /locations/global/quotaAdjusterSettings
```


## What's next?

- 

[Implement common use cases](/docs/quotas/implement-common-use-cases) 

- 

Cloud Quotas API [reference](/docs/quotas/reference/rest) 

- 

Understand [quotas](/docs/quotas/overview)