# Implement common use cases

Source: https://berlin.devsitetest.how/docs/quotas/implement-common-use-cases
Last updated: 2026-07-07

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












# Implement common use cases 






- On this page 
- [ Limitations ](#limitations)
- [ Track usage and request an increase when usage is over 80% ](#track_usage_and_request_an_increase_when_usage_is_over_80)
- [ Decrease a quota ](#decrease_a_quota)
- [ Copy quota preferences to another project ](#copy_quota_preferences_to_another_project)
- [ List pending quota requests ](#list_pending_quota_requests)
- [ Request group quota increases ](#request_group_quota_increases)
- [ Request adjustments on quotas that have no usage ](#request_adjustments_on_quotas_that_have_no_usage)
- [ Get quota info for a service specific dimension ](#get_quota_info_for_a_service_specific_dimension)
- [ Create a quota preference for a service specific dimension ](#create_a_quota_preference_for_a_service_specific_dimension)
- [ Update a quota preference for a service specific dimension ](#update_a_quota_preference_for_a_service_specific_dimension)
- [ What's next ](#whats_next)
- 










This document describes how to implement common use cases using the
Cloud Quotas API.
This API lets you programmatically adjust
[quotas](/docs/quotas/overview) 
and automate
[quota adjustments](/docs/quotas/overview#about_increase_requests) 
in your Google Cloud Dedicated in Germany projects, folders, or organization.

To learn more, see the Cloud Quotas API
[overview](/docs/quotas/api-overview) and
[reference](/docs/quotas/reference/rest).

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

## Track usage and request an increase when usage is over 80%

This example tracks quota usage with Cloud Monitoring and then requests
an increase when the usage is over 80%.

- 

Call the `QuotaInfo` resource for your service to determine the current
`quotaValue`. The service in this example is `compute.googleapis.com`:


```
GET projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos
```


Replace ` PROJECT_NUMBER ` with the project number for
your project.

- 

To find the CPUs per project and the applicable locations, look through the
`QuotaInfo` response for the `CPUS-per-project-region` quota ID. The
`quotaValue` is 20.


```
"quotaInfos" : [ 
... 
{ 
"name" : "projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos/CPUS-per-project-region" , 
"quotaId" : "CPUS-per-project-region" , 
"metric" : "compute.googleapis.com/cpus" , 
"containerType" : "PROJECT" , 
"dimensions" : [ 
"region" 
], 
"dimensionsInfo" : [ 
{ 
"dimensions" : [], 
"details" : { 
"quotaValue" : 20 , 
"resetValue" : 20 
}, 
"applicableLocations" : [ 
"us-central1" , 
"us-central2" , 
"us-west1" , 
"us-east1" 
] 
} 
] 
}, 
... 
] 
```


- 

Call the Cloud Monitoring API to find the quota usage. In the following
example, the region `us-central1` has been specified. Supported quota
metrics are listed under
[`serviceruntime`](/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime).


```
{ 
"name" : "projects/ PROJECT_NUMBER " 
"filter" : "metric.type=\"serviceruntime.googleapis.com/quota/allocation/usage\" AND 
metric.labels.quota_metric=\"compute.googleapis.com/cpus\" AND resource.type=\"consumer_quota\" AND 
resource.label.location=\"us-central1\" " , 
"interval" : { 
"startTime" : "2023-11-10T18:18:18.0000Z" , 
"endTime" : "2023-11-17T18:18:18.0000Z" 
}, 
"aggregation" : { 
"alignmentPeriod" : "604800s" , // 7 days 
"perSeriesAligner" : "ALIGN_MAX" , 
"crossSeriesReducer" : "REDUCE_MAX" 
} 
} 
```


- 

To determine your usage, handle the response from the Cloud Monitoring API.
Compare the value from Cloud Monitoring to the `quotaValue` in earlier
steps to determine the usage.

In the following example response the usage value in Cloud Monitoring is 19
in the `us-central1` region. The `quotaValue` for all regions is 20. The usage
is greater than 80% of the quota, and a quota preference update can be
initiated.


```
time_series { 
metric { 
labels { 
key : "quota_metric" 
value : "compute.googleapis.com/cpus" 
} 
type : "serviceruntime.googleapis.com/quota/allocation/usage" 
} 
resource { 
type : "consumer_quota" 
labels { 
key : "project_id" 
value : " PROJECT_ID " 
} 
labels { 
key : "location" 
value : "us-central1" 
} 
} 
metric_kind : GAUGE 
value_type : INT64 
points { 
interval { 
start_time { 
seconds : "2023-11-10T18:18:18.0000Z" 
} 
end_time { 
seconds : "2023-11-17T18:18:18.0000Z" 
} 
} 
value { 
int64_value : 19 
} 
} 
} 
```


- 

To avoid duplicated quota preferences, call `ListQuotaPreferences` first to
check if there are any pending requests. The `reconciling=true` flag calls
pending requests.


```
GET projects/ PROJECT_NUMBER /locations/global/quotaPreferences?filter = service = %22compute.googleapis.com%22%20AND%20quotaId = %22CPUS-per-project-region%22%20AND%20reconciling = true 
```


Replace ` PROJECT_NUMBER ` with the project number for your
project.

- 

Call `UpdateQuotaPreference` to increase the quota value for region
`us-central1`. In the following example, a new preferred value of 100 has been
specified.

The field `allow_missing` is set to `true`. This tells the system to create a
`QuotaPreference` resource where none exists with the provided name.


```
PATCH projects/ PROJECT_NUMBER /locations/global/quotaPreferences/compute_googleapis_com-cpus-us-central1?allowMissing=true { 
"service" : "compute.googleapis.com" , 
"quotaId" : "CPUS-per-project-region" , 
"quotaConfig" : { "preferredValue" : 100 } , 
"dimensions" : { "region" : "us-central1" } , 
"justification" : " JUSTIFICATION " , 
"contactEmail" : " EMAIL " 
} 
```


Replace the following:

- ` PROJECT_NUMBER `: The unique identifier for your
project.

- ` JUSTIFICATION `: An optional string that explains
your request.

- ` EMAIL `: An email address that can be used as a
contact, in case Google Cloud Dedicated in Germany needs more information before additional quota
can be granted.

- 

Call `GetQuotaPreference` to check the status of the quota preference change:


```
GET projects/ PROJECT_NUMBER /locations/global/quotaPreferences/compute_googleapis_com-cpus-us-central1
```


Replace ` PROJECT_NUMBER ` with the project number for your
project.

While Google Cloud Dedicated in Germany evaluates the requested quota value, the reconciling status
of your quota is set to `true`.

Sometimes Google Cloud Dedicated in Germany approves part of your increase request instead of
approving the full increase. If the request is partially approved, the quota
preference includes a `stateDetail` field. The `stateDetail` field describes
the partially approved state. The `grantedValue` field shows the adjustment
that was made to partially fulfill your request.

To see if the granted value is the final value approved, look at the
`reconciling` field. If your request is still undergoing evaluation, the
`reconciling` field is set to `true`. If the `reconciling` field is set to
`false` or is omitted, the granted value is the final value approved.

In the following example, the requested quota value is 100 and the
`reconciling` field indicates that the request is undergoing review.


```
"name" : "projects/ PROJECT_NUMBER /locations/global/quotaPreferences/compute_googleapis_com-cpus-us-central1" , 
"service" : "compute.googleapis.com" , 
"quotaId" : "CPUS-per-project-region" , 
"quotaConfig" : { 
"preferredValue" : 100 , 
"grantedValue" : 50 , 
"traceId" : "123acd-345df23" , 
"requestOrigin" : "ORIGIN_UNSPECIFIED" 
} , 
"dimensions" : { "region" : "us-central1" } , 
"reconciling" : true, 
"createTime" : "2023-01-15T01:30:15.01Z" , 
"updateTime" : "2023-01-16T02:35:16.01Z" 
```


After the quota preference has been processed, the `reconciling`
field is set to `false`. The `grantedValue` is the same as
the `preferredValue`. The preferred quota is fully granted.

When Google Cloud Dedicated in Germany denies or partially approves a customer request, the
granted quota value can still be less than the preferred value.

## Decrease a quota

The following example decreases the number of TPUs to 10 in each
region.

- 

Get the quota ID and the current quota value with a `ListQuotaInfos` call:


```
GET projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos
```


Replace ` PROJECT_NUMBER ` with the project number for
your project.

- 

Look through the response fields to find a `QuotaInfo` entry for
`V2-TPUS-per-project-region`.


```
"quotaInfos" : [ 
... 
{ 
"name" : "projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos/V2-TPUS-per-project-region" , 
"quotaId" : "V2-TPUS-per-project-region" , 
"metric" : "compute.googleapis.com/Tpus" , 
"containerType" : "PROJECT" , 
"dimensions" : [ 
"region" 
], 
"dimensionsInfo" : [ 
{ 
"dimensions" : [], 
"details" : { 
"quotaValue" : 20 , 
"resetValue" : 20 
}, 
"applicableLocations" : [ 
"us-central1" , 
"us-central2" , 
"us-west1" , 
"us-east1" 
] 
} 
] 
}, 
... 
] 
```


In this response the quota ID is `V2-TPUS-per-project-region`, and the current
`quotaValue` is 20.

- 

Reduce TPU quota in each region to 10 with a `CreateQuotaPreferenceRequest`.
Set the `preferredValue` to 10.


```
POST projects/ PROJECT_NUMBER /locations/global/quotaPreferences?quotaPreferenceId=compute_googleapis_com-Tpu-all-regions { 
"quotaConfig" : { 
"preferredValue" : 10 
} , 
"dimensions" : [] , 
"service" : "compute.googleapis.com" , 
"quotaId" : "V2-TPUS-per-project-region" , 
"justification" : " JUSTIFICATION " , 
"contactEmail" : " EMAIL " 
} 
```


Replace the following:

- ` PROJECT_NUMBER `: The unique identifier for your
project.

- ` JUSTIFICATION `: An optional string that explains
your request.

- ` EMAIL `: An email address that can be used as a
contact, in case Google Cloud Dedicated in Germany needs more information before additional quota
can be granted.

- 

Confirm the new quota value with a `GetQuotaInfo` call that defines the quota
ID as `V2-TPUS-per-project-region`.


```
GET projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos/V2-TPUS-per-project-region
```


Replace ` PROJECT_NUMBER ` with the project number for
your project.

The following is an example response, the `value` is 10 and it is applicable
in all regions.


```
"name" : "projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos/V2-TPUS-per-project-region" , 
"quotaId" : "V2-TPUS-per-project-region" , 
"metric" : "compute.googleapis.com/v2_tpus" , 
"containerType" : "PROJECT" , 
"dimensions" : [ 
"region" 
] , 
"dimensionsInfo" : [ 
{ 
"dimensions" : [], 
"details" : { 
"value" : 10 , 
}, 
"applicableLocations" : [ 
"us-central1" , 
"us-central2" , 
"us-west1" , 
"us-east1" 
] 
} 
] 
```


## Copy quota preferences to another project

The following example copies all quota preferences from
one project to another. It's written in Java, but you can use any programming
language.

- 

Call `ListQuotaPreferences` on the source project with no filter:


```
GET projects/ PROJECT_NUMBER1 /locations/global/quotaPreferences
```


PROJECT_NUMBER1 is the project number for the source project. The
response contains all quota preferences for the source project.

- 

For each quota preference in the response, call `UpdateQuotaPreference` and
define the following fields:

- 

`name` - The updated name field is taken from the response, and the source
project number ( PROJECT_NUMBER1 ) is replaced with the destination
project number ( PROJECT_NUMBER2 ).

- 

`service`, `quotaId`, `preferredValue`, `dimensions` - These fields can be
taken directly from the response as is.


```
for ( QuotaPreference srcPreference : listResponse . getQuotaPreferences ()) { 
QuotaPreference . Builder targetPreference = QuotaPreference . newBuilder () 
. setName ( srcPreference . getName (). replace ( " PROJECT_NUMBER1 " , " PROJECT_NUMBER2 " )) 
. setService ( srcPreference . getService ()) 
. setQuotaId ( srcPreference . getQuotaId ()) 
. setJustification ( srcPreference . getJustification ()) 
. setContactEmail ( srcPreference . getContactEmail ()) 
. setQuotaConfig ( 
QuotaConfig . newBuilder (). setPreferredValue ( srcPreference . getQuotaConfig (). getPreferredValue ())) 
. putAllDimensions ( srcPreference . getDimensionsMap ()); 
UpdateQuotaPreferenceRequest updateRequest = UpdateQuotaPreferenceRequest . newBuilder () 
. setQuotaPreference ( targetPreference ) 
. setAllowMissing ( true ) 
. build (); 
cloudQuotas . updateQuotaPreference ( updateRequest ); 
} 
```


- 

Call `ListQuotaPreferences` to verify the status of the quota preferences for
the destination project:


```
GET projects/ PROJECT_NUMBER2 /locations/global/quotaPreferences
```


Replace ` PROJECT_NUMBER2 ` with the project number for
your destination project.

## List pending quota requests

To list all pending quota preference requests for a project, call
`ListQuotaPreferences` with the filter `reconciling=true`.


```
GET projects/ PROJECT_NUMBER /locations/global/quotaPreferences?reconciling = true 
```


Replace ` PROJECT_NUMBER ` with the project number for your
project.

The response for this request returns the latest pending
quota preference. Because Cloud Quotas API is a declarative API, the
latest quota preference is what the system tries to fulfill.

An example response looks similar to the following:


```
"quotaPreferences" : [ 
{ 
"name" : "projects/ PROJECT_NUMBER /locations/global/quotaPreferences/compute_googleapis_com-cpus-us-central1" , 
"service" : "compute.googleapis.com" , 
"quotaId" : "CPUS-per-project-region" , 
"quotaConfig" : { 
"preferredValue" : 100 , 
"grantedValue" : 30 , 
"traceId" : "123acd-345df23" , 
"requestOrigin" : "ORIGIN_UNSPECIFIED" 
}, 
"dimensions" : { 
"region" : "us-central1" 
}, 
"reconciling" : true , 
"createTime" : "2023-01-15T01:30:15.01Z" , 
"updateTime" : "2023-01-16T02:35:16.01Z" 
}, 
{ 
"name" : "projects/ PROJECT_NUMBER /locations/global/quotaPreferences/compute_googleapis_com-cpus-cross-regions" , 
"service" : "compute.googleapis.com" , 
"quotaId" : "CPUS-per-project-region" , 
"quotaConfig" : { 
"preferredValue" : 10 , 
"grantedValue" : 5 , 
"traceId" : "456asd-678df43" , 
"requestOrigin" : "ORIGIN_UNSPECIFIED" 
}, 
"reconciling" : true , 
"createTime" : "2023-01-15T01:35:15.01Z" , 
"updateTime" : "2023-01-15T01:35:15.01Z" 
} 
] 
```


## Request group quota increases

To request increases for a group of quotas in a new project, store the preferred
quotas for the new project in a CSV file with the following values:
service name, quota ID, preferred quota value, dimensions.

For each row in the CSV file, read the contents into the fields `serviceName`,
`quotaId`, `preferredValue`, and `dimensionMap`.


```
CreateQuotaPreferenceRequest request = 
CreateQuotaPreferenceRequest.newBuilder() 
.setParent("projects/ PROJECT_NUMBER /locations/global") 
.setQuotaPreferenceId(buildYourOwnQuotaPreferenceId(serviceName, quotaId, dimensionMap)) 
.setQuotaPreference( 
QuotaPreference.newBuilder() 
.setService(serviceName) 
.setQuotaId(quotaId) 
.setJustification(justification) 
.setContactEmail(contactEmail) 
.setQuotaConfig(QuotaConfig.newBuilder().setPreferredValue(preferredValue)) 
.putAllDimensions(dimensionMap)) 
.build(); 
cloudQuotas.createQuotaPreference(request); 
```


Replace ` PROJECT_NUMBER ` with the project number for your
project.

Because the target project is new, it is safe to call the
`CreateQuotaPreference` method as you read and assign the fields. Alternatively,
you can call the `UpdateQuotaPreference` method with `allow_missing` set to `true`.

The method `buildYourOwnQuotaPreferenceId` builds a quota preference ID
from service name, quota ID, and a map of dimensions according to your naming
scheme. Alternatively, you can choose not to set quota preference ID. A quota
preference ID is generated for you.

## Request adjustments on quotas that have no usage

For quotas that don't already have quota usage and that have service-specific
dimensions such as `vm_family`, it is possible that those quotas might not
be visible in the Google Cloud Dedicated console. You may need to use the
Cloud Quotas API instead.

For example, you might clone a project and know ahead of time that you need to
increase the value for `compute.googleapis.com/gpus_per_gpu_family`.
This value only appears in the Google Cloud Dedicated console for GPU families that you have
already used. To use the Cloud Quotas API to request an increase to
NVIDIA_H100 GPUs in `us-central1`, you could send a request like the following:


```
POST projec ts / PROJECT_NUMBER /loca t io ns /global/quo ta Pre feren ces?quo ta Pre feren ceId=compu te _googleapis_com - gpus - us - ce ntral 1- NVIDIA_H 100 { 
"service" : "compute.googleapis.com" , 
"quotaId" : "GPUS-PER-GPU-FAMILY-per-project-region" , 
"quotaConfig" : { "preferredValue" : 100 }, 
"dimensions" : { "region" : "us-central1" , "gpu_family" : "NVIDIA_H100" }, 
"justification" : " JUSTIFICATION " , 
"contactEmail" : " EMAIL " 
} 
```


Replace the following:

- ` PROJECT_NUMBER `: The unique identifier for your
project.

- ` JUSTIFICATION `: An optional string that explains your
request.

- ` EMAIL `: An email address that can be used as a
contact, in case Google Cloud Dedicated in Germany needs more information before additional
quota can be granted.

For more information, see also the descriptions of
[Dimension precedence](/docs/quotas/configure-dimensions#dimension_precedence) and
[Combining dimensions](/docs/quotas/configure-dimensions#combining_dimensions).

## Get quota info for a service specific dimension

GPU family is a service specific dimension. The following example request uses the
`GPUS-PER-GPU-FAMILY-per-project-region` quota ID to get the `QuotaInfo` resource.


```
GET projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos/GPUS-PER-GPU-FAMILY-per-project-region
```


Replace ` PROJECT_NUMBER ` with the project number for your
project.

This is an example response. For each unique `gpu_family` key, the `quotaValue`
and `applicableLocations` is different:


```
"name" : "projects/ PROJECT_NUMBER /locations/global/services/compute.googleapis.com/quotaInfos/GpusPerProjectPerRegion" , 
"quotatName" : "CPUS-per-project-region" , 
"metric" : "compute.googleapis.com/gpus_per_gpu_family" , 
"isPrecise" : true, 
"quotaDisplayName" : "GPUs per GPU family" , 
"metricDisplayName" : "GPUs" , 
"dimensions" : [ 
"region" , 
"gpu_family" 
] , 
"dimensionsInfo" : [ 
{ 
"dimensions" : { 
"region" : "us-central1" , 
"gpu_family" : "NVIDIA_H200" 
}, 
"details" : { 
"quotaValue" : 30 , 
"resetValue" : 30 , 
}, 
"applicableLocations" : [ 
"us-central1" 
] 
}, 
{ 
"dimensions" : { 
"region" : "us-central1" 
} 
"details" : { 
"quotaValue" : 100 , 
"resetValue" : 100 , 
}, 
"applicableLocations" : [ 
"us-central1" 
] 
}, 
{ 
"dimensions" : { 
"gpu_familly" : "NVIDIA_H100" 
} 
"details" : { 
"quotaValue" : 10 , 
}, 
"applicableLocations" : [ 
"us-central2" , 
"us-west1" , 
"us-east1" 
] 
} 
{ 
"dimensions" : [], 
"details" : { 
"quotaValue" : 50 , 
"resetValue" : 50 , 
}, 
"applicableLocations" : [ 
"us-central1" , 
"us-central2" , 
"us-west1" , 
"us-east1" 
] 
} 
] 
```


## Create a quota preference for a service specific dimension

The following example demonstrates how to create a quota for a given region and
GPU family with a preferred value of 100. The target location is specified in the
map of dimensions with the key `region`, and the target GPU family with the key
`gpu_family`.

The following `CreateQuotaPreference` example specifies a GPU family of
`NVIDIA_H100` and a region of `us-central1`.


```
POST projects/ PROJECT_NUMBER /locations/global/quotaPreferences?quotaPreferenceId=compute_googleapis_com-gpus-us-central1-NVIDIA_H100 { 
"service" : "compute.googleapis.com" , 
"quotaId" : "GPUS-PER-GPU-FAMILY-per-project-region" , 
"quotaConfig" : { 
"preferredValue" : 100 
} , 
"dimensions" : { "region" : "us-central1" , "gpu_family" : "NVIDIA_H100" } , 
"justification" : " JUSTIFICATION " , 
"contactEmail" : "" EMAIL "
} 
```


Replace the following:

- ` PROJECT_NUMBER `: The unique identifier for your
project.

- ` JUSTIFICATION `: An optional string that explains your
request.

- ` EMAIL `: An email address that can be used as a
contact, in case Google Cloud Dedicated in Germany needs more information before additional
quota can be granted.

## Update a quota preference for a service specific dimension

The following sample code gets the current value for the dimension
`{"region" : "us-central1"; gpu_family:"NVIDIA_H100"},`
and then sets the preferred value to double the value. It's written in Java, but you
can use any programming language.


```
// Get the current quota value for the target dimensions 
Map , String > targetDimensions = Maps . createHashMap ( "region" , "us-central1" , "gpu_family" , "NVIDIA_H100" ); 
long currentQuotaValue = 0 ; 
QuotaInfo quotaInfo = cloudQuotas . GetQuotaInfo ( 
"projects/ PROJECT_NUMBER /locations/global/services/" + serviceName + "quotaInfos/" + quotaId ; 
for ( dimensionsInfo : quotaInfo . getDimensionsInfoList ()) { 
If ( targetDimensions . entrySet (). containsAll ( dimensionsInfo . getDimensionsMap (). entrySet ()) { 
currentQuotaValue = dimensionsInfo . getDetails (). getValue (); 
break ; 
}) 
} 

// Set the preferred quota value to double the current value for the target dimensions 
QuotaPreference . Builder targetPreference = QuotaPreference . newBuilder () 
. setName ( buildYourOwnQuotaPreferenceId ( serviceName , quotaId , targetDimensions )) 
. setService ( serviceName ) 
. setQuotaId ( quotaId ) 
. setJustification ( justification ) 
. setContactEmail ( contactEmail ) 
. setQuotaConfig ( QuotaConfig . newBuilder (). setPreferredValue ( currentQuotaValue * 2 )) 
. putAllDimensions ( targetDimensions )); 
UpdateQuotaPreferenceRequest updateRequest = UpdateQuotaPreferenceRequest . newBuilder () 
. setQuotaPreference ( targetPreference ) 
. setAllowMissing ( true ) 
. build (); 
cloudQuotas . updateQuotaPreference ( updateRequest ); 
```


Replace ` PROJECT_NUMBER ` with the unique identifier for
your project.

## What's next

- 

About the [Cloud Quotas API](/docs/quotas/api-overview) 

- 

Cloud Quotas API [reference](/docs/quotas/reference/rest) 

- 

Understand [quotas](/docs/quotas/overview)