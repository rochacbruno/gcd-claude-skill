# Service Usage API

Source: https://berlin.devsitetest.how/service-usage/docs/reference/rest
Last updated: 2025-12-10

- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Technology areas

](https://berlin.devsitetest.how/docs)






- 








[

Service Usage

](https://berlin.devsitetest.how/service-usage)






- 








[

Reference

](https://berlin.devsitetest.how/service-usage/docs/apis)












# Service Usage API 






- On this page ** 
- [ Service: serviceusage.googleapis.com ](#service:-serviceusage.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)

- [ REST Resource: v2beta.operations ](#rest-resource:-v2beta.operations)
- [ REST Resource: v1beta1.operations ](#rest-resource:-v1beta1.operations)
- [ REST Resource: v1beta1.services ](#rest-resource:-v1beta1.services)
- [ REST Resource: v1beta1.services.consumerQuotaMetrics ](#rest-resource:-v1beta1.services.consumerquotametrics)
- [ REST Resource: v1beta1.services.consumerQuotaMetrics.limits ](#rest-resource:-v1beta1.services.consumerquotametrics.limits)
- [ REST Resource: v1beta1.services.consumerQuotaMetrics.limits.adminOverrides ](#rest-resource:-v1beta1.services.consumerquotametrics.limits.adminoverrides)
- [ REST Resource: v1beta1.services.consumerQuotaMetrics.limits.consumerOverrides ](#rest-resource:-v1beta1.services.consumerquotametrics.limits.consumeroverrides)
- [ REST Resource: v1.operations ](#rest-resource:-v1.operations)
- [ REST Resource: v1.services ](#rest-resource:-v1.services)
- 













Enables services that service consumers want to use on Sovereign Cloud Platform, lists the available or enabled services, or disables services that service consumers no longer use.




- [REST Resource: v2beta.operations](#v2beta.operations)

- [REST Resource: v1beta1.operations](#v1beta1.operations)

- [REST Resource: v1beta1.services](#v1beta1.services)

- [REST Resource: v1beta1.services.consumerQuotaMetrics](#v1beta1.services.consumerQuotaMetrics)

- [REST Resource: v1beta1.services.consumerQuotaMetrics.limits](#v1beta1.services.consumerQuotaMetrics.limits)

- [REST Resource: v1beta1.services.consumerQuotaMetrics.limits.adminOverrides](#v1beta1.services.consumerQuotaMetrics.limits.adminOverrides)

- [REST Resource: 
v1beta1.services.consumerQuotaMetrics.limits.consumerOverrides](#v1beta1.services.consumerQuotaMetrics.limits.consumerOverrides)

- [REST Resource: v1.operations](#v1.operations)

- [REST Resource: v1.services](#v1.services)





## Service: serviceusage. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:




- [https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v2beta](https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v2beta)

- [https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1](https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1)

- [https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1beta1](https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1beta1)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://serviceusage.apis-berlin-build0.goog`






## REST Resource: [v2beta. operations](/service-usage/docs/reference/rest/v2beta/operations)









| 
Methods | 
|



| 

`[get](/service-usage/docs/reference/rest/v2beta/operations/get)` | 

`GET / v2beta/ {name=operations/ *}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/service-usage/docs/reference/rest/v2beta/operations/list)` | 

`GET / v2beta/ operations` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v1beta1. operations](/service-usage/docs/reference/rest/v1beta1/operations)









| 
Methods | 
|



| 

`[get](/service-usage/docs/reference/rest/v1beta1/operations/get)` | 

`GET /v1beta1/{name=operations/*}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/service-usage/docs/reference/rest/v1beta1/operations/list)` | 

`GET /v1beta1/operations` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v1beta1.services](/service-usage/docs/reference/rest/v1beta1/services)









| 
Methods | 
|



| 

`[batchEnable](/service-usage/docs/reference/rest/v1beta1/services/batchEnable) 
(deprecated)**` | 

`POST /v1beta1/{parent=*/*}/services:batchEnable` 

Enables multiple services on a project. | 
|

| 

`[disable](/service-usage/docs/reference/rest/v1beta1/services/disable) 
**(deprecated)**` | 

`POST /v1beta1/{name=*/*/services/*}:disable` 

Disables a service so that it can no longer be used with a project. | 
|

| 

`[enable](/service-usage/docs/reference/rest/v1beta1/services/enable) 
**(deprecated)**` | 

`POST /v1beta1/{name=*/*/services/*}:enable` 

Enables a service so that it can be used with a project. | 
|

| 

`[generateServiceIdentity](/service-usage/docs/reference/rest/v1beta1/services/generateServiceIdentity)` | 

`POST /v1beta1/{parent=*/*/services/*}:generateServiceIdentity` 

Generates service identity for service. | 
|

| 

`[get](/service-usage/docs/reference/rest/v1beta1/services/get) 
**(deprecated)**` | 

`GET /v1beta1/{name=*/*/services/*}` 

Returns the service configuration and enabled state for a given service. | 
|

| 

`[list](/service-usage/docs/reference/rest/v1beta1/services/list) 
**(deprecated)**` | 

`GET /v1beta1/{parent=*/*}/services` 

Lists all services available to the specified project, and the current state of those services with respect to the project. | 
|






## REST Resource: [v1beta1.services.consumerQuotaMetrics](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics)









| 
Methods | 
|



| 

`[get](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/get)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.GetConsumerQuotaMetric` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[importAdminOverrides](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/importAdminOverrides)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.ImportAdminOverrides` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[importConsumerOverrides](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/importConsumerOverrides)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.ImportConsumerOverrides` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/list)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.ListConsumerQuotaMetrics` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1beta1.services.consumerQuotaMetrics.limits](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits)









| 
Methods | 
|



| 

`[get](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits/get)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.GetConsumerQuotaLimit` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1beta1.services.consumerQuotaMetrics.limits.adminOverrides](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides)









| 
Methods | 
|



| 

`[create](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides/create)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.CreateAdminOverride` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides/delete)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.DeleteAdminOverride` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides/list)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.ListAdminOverrides` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides/patch)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.UpdateAdminOverride` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1beta1.services.consumerQuotaMetrics.limits.consumerOverrides](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides)









| 
Methods | 
|



| 

`[create](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides/create)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.CreateConsumerOverride` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides/delete)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.DeleteConsumerOverride` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides/list)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.ListConsumerOverrides` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides/patch)` | 

The method `google.api.serviceusage.v1beta1.ServiceUsage.UpdateConsumerOverride` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.operations](/service-usage/docs/reference/rest/v1/operations)









| 
Methods | 
|



| 

`[cancel](/service-usage/docs/reference/rest/v1/operations/cancel)` | 

`POST /v1/{name=operations/**}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[delete](/service-usage/docs/reference/rest/v1/operations/delete)` | 

`DELETE /v1/{name=operations/**}` 

Deletes a long-running operation. | 
|

| 

`[get](/service-usage/docs/reference/rest/v1/operations/get)` | 

`GET /v1/{name=operations/*}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/service-usage/docs/reference/rest/v1/operations/list)` | 

`GET /v1/operations` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v1.services](/service-usage/docs/reference/rest/v1/services)









| 
Methods | 
|



| 

`[batchEnable](/service-usage/docs/reference/rest/v1/services/batchEnable)` | 

`POST /v1/{parent=*/*}/services:batchEnable` 

Enable multiple services on a project. | 
|

| 

`[batchGet](/service-usage/docs/reference/rest/v1/services/batchGet)` | 

`GET /v1/{parent=*/*}/services:batchGet` 

Returns the service configurations and enabled states for a given list of services. | 
|

| 

`[disable](/service-usage/docs/reference/rest/v1/services/disable)` | 

`POST /v1/{name=*/*/services/*}:disable` 

Disable a service so that it can no longer be used with a project. | 
|

| 

`[enable](/service-usage/docs/reference/rest/v1/services/enable)` | 

`POST /v1/{name=*/*/services/*}:enable` 

Enable a service so that it can be used with a project. | 
|

| 

`[get](/service-usage/docs/reference/rest/v1/services/get)` | 

`GET /v1/{name=*/*/services/*}` 

Returns the service configuration and enabled state for a given service. | 
|

| 

`[list](/service-usage/docs/reference/rest/v1/services/list)` | 

`GET /v1/{parent=*/*}/services` 

List all services available to the specified project, and the current state of those services with respect to the project. | 
|