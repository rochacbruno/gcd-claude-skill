# Cloud Logging API

Source: https://berlin.devsitetest.how/logging/docs/reference/v2/rest
Last updated: 2025-11-13

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/logging/docs/tpc-differences) for more details.














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

Observability

](https://berlin.devsitetest.how/docs/observability)






- 








[

Cloud Logging

](https://berlin.devsitetest.how/logging/docs)






- 








[

Reference

](https://berlin.devsitetest.how/logging/docs/apis)












# Cloud Logging API 






- On this page 
- [ Service: logging.googleapis.com ](#service:-logging.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)

- [ REST Resource: v2 ](#rest-resource:-v2)
- [ REST Resource: v2.billingAccounts ](#rest-resource:-v2.billingaccounts)
- [ REST Resource: v2.billingAccounts.exclusions ](#rest-resource:-v2.billingaccounts.exclusions)
- [ REST Resource: v2.billingAccounts.locations.buckets ](#rest-resource:-v2.billingaccounts.locations.buckets)
- [ REST Resource: v2.billingAccounts.locations.buckets.links ](#rest-resource:-v2.billingaccounts.locations.buckets.links)
- [ REST Resource: v2.billingAccounts.locations.buckets.views ](#rest-resource:-v2.billingaccounts.locations.buckets.views)
- [ REST Resource: v2.billingAccounts.locations.buckets.views.logs ](#rest-resource:-v2.billingaccounts.locations.buckets.views.logs)
- [ REST Resource: v2.billingAccounts.locations.operations ](#rest-resource:-v2.billingaccounts.locations.operations)
- [ REST Resource: v2.billingAccounts.locations.recentQueries ](#rest-resource:-v2.billingaccounts.locations.recentqueries)
- [ REST Resource: v2.billingAccounts.locations.savedQueries ](#rest-resource:-v2.billingaccounts.locations.savedqueries)
- [ REST Resource: v2.billingAccounts.logs ](#rest-resource:-v2.billingaccounts.logs)
- [ REST Resource: v2.billingAccounts.sinks ](#rest-resource:-v2.billingaccounts.sinks)
- [ REST Resource: v2.entries ](#rest-resource:-v2.entries)
- [ REST Resource: v2.exclusions ](#rest-resource:-v2.exclusions)
- [ REST Resource: v2.folders ](#rest-resource:-v2.folders)
- [ REST Resource: v2.folders.exclusions ](#rest-resource:-v2.folders.exclusions)
- [ REST Resource: v2.folders.locations.buckets ](#rest-resource:-v2.folders.locations.buckets)
- [ REST Resource: v2.folders.locations.buckets.links ](#rest-resource:-v2.folders.locations.buckets.links)
- [ REST Resource: v2.folders.locations.buckets.views ](#rest-resource:-v2.folders.locations.buckets.views)
- [ REST Resource: v2.folders.locations.buckets.views.logs ](#rest-resource:-v2.folders.locations.buckets.views.logs)
- [ REST Resource: v2.folders.locations.logScopes ](#rest-resource:-v2.folders.locations.logscopes)
- [ REST Resource: v2.folders.locations.operations ](#rest-resource:-v2.folders.locations.operations)
- [ REST Resource: v2.folders.locations.recentQueries ](#rest-resource:-v2.folders.locations.recentqueries)
- [ REST Resource: v2.folders.locations.savedQueries ](#rest-resource:-v2.folders.locations.savedqueries)
- [ REST Resource: v2.folders.logs ](#rest-resource:-v2.folders.logs)
- [ REST Resource: v2.folders.sinks ](#rest-resource:-v2.folders.sinks)
- [ REST Resource: v2.locations.buckets ](#rest-resource:-v2.locations.buckets)
- [ REST Resource: v2.locations.buckets.links ](#rest-resource:-v2.locations.buckets.links)
- [ REST Resource: v2.locations.buckets.views ](#rest-resource:-v2.locations.buckets.views)
- [ REST Resource: v2.locations.operations ](#rest-resource:-v2.locations.operations)
- [ REST Resource: v2.logs ](#rest-resource:-v2.logs)
- [ REST Resource: v2.monitoredResourceDescriptors ](#rest-resource:-v2.monitoredresourcedescriptors)
- [ REST Resource: v2.organizations ](#rest-resource:-v2.organizations)
- [ REST Resource: v2.organizations.exclusions ](#rest-resource:-v2.organizations.exclusions)
- [ REST Resource: v2.organizations.locations.buckets ](#rest-resource:-v2.organizations.locations.buckets)
- [ REST Resource: v2.organizations.locations.buckets.links ](#rest-resource:-v2.organizations.locations.buckets.links)
- [ REST Resource: v2.organizations.locations.buckets.views ](#rest-resource:-v2.organizations.locations.buckets.views)
- [ REST Resource: v2.organizations.locations.buckets.views.logs ](#rest-resource:-v2.organizations.locations.buckets.views.logs)
- [ REST Resource: v2.organizations.locations.logScopes ](#rest-resource:-v2.organizations.locations.logscopes)
- [ REST Resource: v2.organizations.locations.operations ](#rest-resource:-v2.organizations.locations.operations)
- [ REST Resource: v2.organizations.locations.recentQueries ](#rest-resource:-v2.organizations.locations.recentqueries)
- [ REST Resource: v2.organizations.locations.savedQueries ](#rest-resource:-v2.organizations.locations.savedqueries)
- [ REST Resource: v2.organizations.logs ](#rest-resource:-v2.organizations.logs)
- [ REST Resource: v2.organizations.sinks ](#rest-resource:-v2.organizations.sinks)
- [ REST Resource: v2.projects ](#rest-resource:-v2.projects)
- [ REST Resource: v2.projects.exclusions ](#rest-resource:-v2.projects.exclusions)
- [ REST Resource: v2.projects.locations.buckets ](#rest-resource:-v2.projects.locations.buckets)
- [ REST Resource: v2.projects.locations.buckets.links ](#rest-resource:-v2.projects.locations.buckets.links)
- [ REST Resource: v2.projects.locations.buckets.views ](#rest-resource:-v2.projects.locations.buckets.views)
- [ REST Resource: v2.projects.locations.buckets.views.logs ](#rest-resource:-v2.projects.locations.buckets.views.logs)
- [ REST Resource: v2.projects.locations.logScopes ](#rest-resource:-v2.projects.locations.logscopes)
- [ REST Resource: v2.projects.locations.operations ](#rest-resource:-v2.projects.locations.operations)
- [ REST Resource: v2.projects.locations.recentQueries ](#rest-resource:-v2.projects.locations.recentqueries)
- [ REST Resource: v2.projects.locations.savedQueries ](#rest-resource:-v2.projects.locations.savedqueries)
- [ REST Resource: v2.projects.logs ](#rest-resource:-v2.projects.logs)
- [ REST Resource: v2.projects.sinks ](#rest-resource:-v2.projects.sinks)
- [ REST Resource: v2.sinks ](#rest-resource:-v2.sinks)
- 













Writes log entries and manages your Cloud Logging configuration.




- [REST Resource: v2](#v2)

- [REST Resource: v2.billingAccounts](#v2.billingAccounts)

- [REST Resource: v2.billingAccounts.exclusions](#v2.billingAccounts.exclusions)

- [REST Resource: v2.billingAccounts.locations.buckets](#v2.billingAccounts.locations.buckets)

- [REST Resource: v2.billingAccounts.locations.buckets.links](#v2.billingAccounts.locations.buckets.links)

- [REST Resource: v2.billingAccounts.locations.buckets.views](#v2.billingAccounts.locations.buckets.views)

- [REST Resource: v2.billingAccounts.locations.buckets.views.logs](#v2.billingAccounts.locations.buckets.views.logs)

- [REST Resource: v2.billingAccounts.locations.operations](#v2.billingAccounts.locations.operations)

- [REST Resource: v2.billingAccounts.locations.recentQueries](#v2.billingAccounts.locations.recentQueries)

- [REST Resource: v2.billingAccounts.locations.savedQueries](#v2.billingAccounts.locations.savedQueries)

- [REST Resource: v2.billingAccounts.logs](#v2.billingAccounts.logs)

- [REST Resource: v2.billingAccounts.sinks](#v2.billingAccounts.sinks)

- [REST Resource: v2.entries](#v2.entries)

- [REST Resource: v2.exclusions](#v2.exclusions)

- [REST Resource: v2.folders](#v2.folders)

- [REST Resource: v2.folders.exclusions](#v2.folders.exclusions)

- [REST Resource: v2.folders.locations.buckets](#v2.folders.locations.buckets)

- [REST Resource: v2.folders.locations.buckets.links](#v2.folders.locations.buckets.links)

- [REST Resource: v2.folders.locations.buckets.views](#v2.folders.locations.buckets.views)

- [REST Resource: v2.folders.locations.buckets.views.logs](#v2.folders.locations.buckets.views.logs)

- [REST Resource: v2.folders.locations.logScopes](#v2.folders.locations.logScopes)

- [REST Resource: v2.folders.locations.operations](#v2.folders.locations.operations)

- [REST Resource: v2.folders.locations.recentQueries](#v2.folders.locations.recentQueries)

- [REST Resource: v2.folders.locations.savedQueries](#v2.folders.locations.savedQueries)

- [REST Resource: v2.folders.logs](#v2.folders.logs)

- [REST Resource: v2.folders.sinks](#v2.folders.sinks)

- [REST Resource: v2.locations.buckets](#v2.locations.buckets)

- [REST Resource: v2.locations.buckets.links](#v2.locations.buckets.links)

- [REST Resource: v2.locations.buckets.views](#v2.locations.buckets.views)

- [REST Resource: v2.locations.operations](#v2.locations.operations)

- [REST Resource: v2.logs](#v2.logs)

- [REST Resource: v2.monitoredResourceDescriptors](#v2.monitoredResourceDescriptors)

- [REST Resource: v2.organizations](#v2.organizations)

- [REST Resource: v2.organizations.exclusions](#v2.organizations.exclusions)

- [REST Resource: v2.organizations.locations.buckets](#v2.organizations.locations.buckets)

- [REST Resource: v2.organizations.locations.buckets.links](#v2.organizations.locations.buckets.links)

- [REST Resource: v2.organizations.locations.buckets.views](#v2.organizations.locations.buckets.views)

- [REST Resource: v2.organizations.locations.buckets.views.logs](#v2.organizations.locations.buckets.views.logs)

- [REST Resource: v2.organizations.locations.logScopes](#v2.organizations.locations.logScopes)

- [REST Resource: v2.organizations.locations.operations](#v2.organizations.locations.operations)

- [REST Resource: v2.organizations.locations.recentQueries](#v2.organizations.locations.recentQueries)

- [REST Resource: v2.organizations.locations.savedQueries](#v2.organizations.locations.savedQueries)

- [REST Resource: v2.organizations.logs](#v2.organizations.logs)

- [REST Resource: v2.organizations.sinks](#v2.organizations.sinks)

- [REST Resource: v2.projects](#v2.projects)

- [REST Resource: v2.projects.exclusions](#v2.projects.exclusions)

- [REST Resource: v2.projects.locations.buckets](#v2.projects.locations.buckets)

- [REST Resource: v2.projects.locations.buckets.links](#v2.projects.locations.buckets.links)

- [REST Resource: v2.projects.locations.buckets.views](#v2.projects.locations.buckets.views)

- [REST Resource: v2.projects.locations.buckets.views.logs](#v2.projects.locations.buckets.views.logs)

- [REST Resource: v2.projects.locations.logScopes](#v2.projects.locations.logScopes)

- [REST Resource: v2.projects.locations.operations](#v2.projects.locations.operations)

- [REST Resource: v2.projects.locations.recentQueries](#v2.projects.locations.recentQueries)

- [REST Resource: v2.projects.locations.savedQueries](#v2.projects.locations.savedQueries)

- [REST Resource: v2.projects.logs](#v2.projects.logs)

- [REST Resource: v2.projects.sinks](#v2.projects.sinks)

- [REST Resource: v2.sinks](#v2.sinks)





## Service: logging. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://logging.apis-berlin-build0.goog/$discovery/rest?version=v2](https://logging.apis-berlin-build0.goog/$discovery/rest?version=v2)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://logging.apis-berlin-build0.goog`






## REST Resource: [v2](/logging/docs/reference/v2/rest/v2/TopLevel)









| 
Methods | 
|



| 

`[get Settings](/logging/docs/reference/v2/rest/v2/TopLevel/getSettings)` | 

`GET / v2/ {name=*/ *}/ settings` 

Gets the settings for the given resource. | 
|

| 

`[update Settings](/logging/docs/reference/v2/rest/v2/TopLevel/updateSettings)` | 

`PATCH / v2/ {name=*/ *}/ settings` 

Updates the settings for the given resource. | 
|

| 

`[get Cmek Settings](/logging/docs/reference/v2/rest/v2/TopLevel/getCmekSettings)` | 

The method `google. logging. v2. Config Service V2. Get Cmek Settings` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[update Cmek Settings](/logging/docs/reference/v2/rest/v2/TopLevel/updateCmekSettings)` | 

The method `google. logging. v2. Config Service V2. Update Cmek Settings` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2. billing Accounts](/logging/docs/reference/v2/rest/v2/billingAccounts)









| 
Methods | 
|



| 

`[getSettings](/logging/docs/reference/v2/rest/v2/billingAccounts/getSettings)` | 

`GET /v2/{name=billingAccounts/*}/settings` 

Gets the settings for the given resource. | 
|

| 

`[getCmekSettings](/logging/docs/reference/v2/rest/v2/billingAccounts/getCmekSettings)` | 

The method `google.logging.v2.ConfigServiceV2.GetCmekSettings` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.billingAccounts.exclusions](/logging/docs/reference/v2/rest/v2/billingAccounts.exclusions)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/billingAccounts.exclusions/create)` | 

`POST /v2/{parent=billingAccounts/*}/exclusions` 

Creates a new exclusion in the _Default sink in a specified parent resource. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/billingAccounts.exclusions/delete)` | 

`DELETE /v2/{name=billingAccounts/*/exclusions/*}` 

Deletes an exclusion in the _Default sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/billingAccounts.exclusions/get)` | 

`GET /v2/{name=billingAccounts/*/exclusions/*}` 

Gets the description of an exclusion in the _Default sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.exclusions/list)` | 

`GET /v2/{parent=billingAccounts/*}/exclusions` 

Lists all the exclusions on the _Default sink in a parent resource. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/billingAccounts.exclusions/patch)` | 

`PATCH /v2/{name=billingAccounts/*/exclusions/*}` 

Changes one or more properties of an existing exclusion in the _Default sink. | 
|






## REST Resource: [v2.billingAccounts.locations.buckets](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/create)` | 

`POST /v2/{parent=billingAccounts/*/locations/*}/buckets` 

Creates a log bucket that can be used to store log entries. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/delete)` | 

`DELETE /v2/{name=billingAccounts/*/locations/*/buckets/*}` 

Deletes a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/get)` | 

`GET /v2/{name=billingAccounts/*/locations/*/buckets/*}` 

Gets a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/list)` | 

`GET /v2/{parent=billingAccounts/*/locations/*}/buckets` 

Lists log buckets. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/patch)` | 

`PATCH /v2/{name=billingAccounts/*/locations/*/buckets/*}` 

Updates a log bucket. | 
|

| 

`[undelete](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/undelete)` | 

`POST /v2/{name=billingAccounts/*/locations/*/buckets/*}:undelete` 

Undeletes a log bucket. | 
|

| 

`[createAsync](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/createAsync)` | 

The method `google.logging.v2.ConfigServiceV2.CreateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateAsync](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/updateAsync)` | 

The method `google.logging.v2.ConfigServiceV2.UpdateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.billingAccounts.locations.buckets.links](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.links)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.links/create)` | 

The method `google.logging.v2.ConfigServiceV2.CreateLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.links/delete)` | 

The method `google.logging.v2.ConfigServiceV2.DeleteLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.links/get)` | 

The method `google.logging.v2.ConfigServiceV2.GetLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.links/list)` | 

The method `google.logging.v2.ConfigServiceV2.ListLinks` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.billingAccounts.locations.buckets.views](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.views)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.views/create)` | 

`POST /v2/{parent=billingAccounts/*/locations/*/buckets/*}/views` 

Creates a view over log entries in a log bucket. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.views/delete)` | 

`DELETE /v2/{name=billingAccounts/*/locations/*/buckets/*/views/*}` 

Deletes a view on a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.views/get)` | 

`GET /v2/{name=billingAccounts/*/locations/*/buckets/*/views/*}` 

Gets a view on a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.views/list)` | 

`GET /v2/{parent=billingAccounts/*/locations/*/buckets/*}/views` 

Lists views on a log bucket. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.views/patch)` | 

`PATCH /v2/{name=billingAccounts/*/locations/*/buckets/*/views/*}` 

Updates a view on a log bucket. | 
|






## REST Resource: [v2.billingAccounts.locations.buckets.views.logs](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.views.logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.views.logs/list)` | 

`GET /v2/{parent=billingAccounts/*/locations/*/buckets/*/views/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|






## REST Resource: [v2.billingAccounts.locations.operations](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations)









| 
Methods | 
|



| 

`[cancel](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations/cancel)` | 

`POST /v2/{name=billingAccounts/*/locations/*/operations/*}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations/get)` | 

`GET /v2/{name=billingAccounts/*/locations/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations/list)` | 

`GET /v2/{name=billingAccounts/*/locations/*}/operations` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v2.billingAccounts.locations.recentQueries](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.recentQueries)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.recentQueries/list)` | 

`GET /v2/{parent=billingAccounts/*/locations/*}/recentQueries` 

Lists the RecentQueries that were created by the user making the request. | 
|






## REST Resource: [v2.billingAccounts.locations.savedQueries](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.savedQueries)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.savedQueries/create)` | 

`POST /v2/{parent=billingAccounts/*/locations/*}/savedQueries` 

Creates a new SavedQuery for the user making the request. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.savedQueries/delete)` | 

`DELETE /v2/{name=billingAccounts/*/locations/*/savedQueries/*}` 

Deletes an existing SavedQuery that was created by the user making the request. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.savedQueries/get)` | 

`GET /v2/{name=billingAccounts/*/locations/*/savedQueries/*}` 

Returns all data associated with the requested query. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.savedQueries/list)` | 

`GET /v2/{parent=billingAccounts/*/locations/*}/savedQueries` 

Lists the SavedQueries that were created by the user making the request. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/billingAccounts.locations.savedQueries/patch)` | 

`PATCH /v2/{savedQuery.name=billingAccounts/*/locations/*/savedQueries/*}` 

Updates an existing SavedQuery. | 
|






## REST Resource: [v2.billingAccounts.logs](/logging/docs/reference/v2/rest/v2/billingAccounts.logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.logs/list)` | 

`GET /v2/{parent=billingAccounts/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/billingAccounts.logs/delete)` | 

The method `google.logging.v2.LoggingServiceV2.DeleteLog` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.billingAccounts.sinks](/logging/docs/reference/v2/rest/v2/billingAccounts.sinks)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/billingAccounts.sinks/create)` | 

`POST /v2/{parent=billingAccounts/*}/sinks` 

BigQuery and GCS exports are not supported.
Creates a sink that exports specified log entries to a destination. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/billingAccounts.sinks/delete)` | 

`DELETE /v2/{sinkName=billingAccounts/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Deletes a sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/billingAccounts.sinks/get)` | 

`GET /v2/{sinkName=billingAccounts/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Gets a sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/billingAccounts.sinks/list)` | 

`GET /v2/{parent=billingAccounts/*}/sinks` 

BigQuery and GCS exports are not supported.
Lists sinks. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/billingAccounts.sinks/patch)` | 

`PATCH /v2/{sinkName=billingAccounts/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|

| 

`[update](/logging/docs/reference/v2/rest/v2/billingAccounts.sinks/update)` | 

`PUT /v2/{sinkName=billingAccounts/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|






## REST Resource: [v2.entries](/logging/docs/reference/v2/rest/v2/entries)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/entries/list)` | 

`POST /v2/entries:list` 

Lists log entries. | 
|

| 

`[write](/logging/docs/reference/v2/rest/v2/entries/write)` | 

`POST /v2/entries:write` 

Writes log entries to Logging. | 
|

| 

`[copy](/logging/docs/reference/v2/rest/v2/entries/copy)` | 

The method `google.logging.v2.ConfigServiceV2.CopyLogEntries` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[tail](/logging/docs/reference/v2/rest/v2/entries/tail)` | 

The method `google.logging.v2.LoggingServiceV2.TailLogEntries` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.exclusions](/logging/docs/reference/v2/rest/v2/exclusions)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/exclusions/create)` | 

`POST /v2/{parent=*/*}/exclusions` 

Creates a new exclusion in the _Default sink in a specified parent resource. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/exclusions/delete)` | 

`DELETE /v2/{name=*/*/exclusions/*}` 

Deletes an exclusion in the _Default sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/exclusions/get)` | 

`GET /v2/{name=*/*/exclusions/*}` 

Gets the description of an exclusion in the _Default sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/exclusions/list)` | 

`GET /v2/{parent=*/*}/exclusions` 

Lists all the exclusions on the _Default sink in a parent resource. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/exclusions/patch)` | 

`PATCH /v2/{name=*/*/exclusions/*}` 

Changes one or more properties of an existing exclusion in the _Default sink. | 
|






## REST Resource: [v2.folders](/logging/docs/reference/v2/rest/v2/folders)









| 
Methods | 
|



| 

`[getSettings](/logging/docs/reference/v2/rest/v2/folders/getSettings)` | 

`GET /v2/{name=folders/*}/settings` 

Gets the settings for the given resource. | 
|

| 

`[updateSettings](/logging/docs/reference/v2/rest/v2/folders/updateSettings)` | 

`PATCH /v2/{name=folders/*}/settings` 

Updates the settings for the given resource. | 
|

| 

`[getCmekSettings](/logging/docs/reference/v2/rest/v2/folders/getCmekSettings)` | 

The method `google.logging.v2.ConfigServiceV2.GetCmekSettings` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.folders.exclusions](/logging/docs/reference/v2/rest/v2/folders.exclusions)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/folders.exclusions/create)` | 

`POST /v2/{parent=folders/*}/exclusions` 

Creates a new exclusion in the _Default sink in a specified parent resource. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/folders.exclusions/delete)` | 

`DELETE /v2/{name=folders/*/exclusions/*}` 

Deletes an exclusion in the _Default sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/folders.exclusions/get)` | 

`GET /v2/{name=folders/*/exclusions/*}` 

Gets the description of an exclusion in the _Default sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/folders.exclusions/list)` | 

`GET /v2/{parent=folders/*}/exclusions` 

Lists all the exclusions on the _Default sink in a parent resource. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/folders.exclusions/patch)` | 

`PATCH /v2/{name=folders/*/exclusions/*}` 

Changes one or more properties of an existing exclusion in the _Default sink. | 
|






## REST Resource: [v2.folders.locations.buckets](/logging/docs/reference/v2/rest/v2/folders.locations.buckets)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/folders.locations.buckets/create)` | 

`POST /v2/{parent=folders/*/locations/*}/buckets` 

Creates a log bucket that can be used to store log entries. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/folders.locations.buckets/delete)` | 

`DELETE /v2/{name=folders/*/locations/*/buckets/*}` 

Deletes a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/folders.locations.buckets/get)` | 

`GET /v2/{name=folders/*/locations/*/buckets/*}` 

Gets a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/folders.locations.buckets/list)` | 

`GET /v2/{parent=folders/*/locations/*}/buckets` 

Lists log buckets. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/folders.locations.buckets/patch)` | 

`PATCH /v2/{name=folders/*/locations/*/buckets/*}` 

Updates a log bucket. | 
|

| 

`[undelete](/logging/docs/reference/v2/rest/v2/folders.locations.buckets/undelete)` | 

`POST /v2/{name=folders/*/locations/*/buckets/*}:undelete` 

Undeletes a log bucket. | 
|

| 

`[createAsync](/logging/docs/reference/v2/rest/v2/folders.locations.buckets/createAsync)` | 

The method `google.logging.v2.ConfigServiceV2.CreateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateAsync](/logging/docs/reference/v2/rest/v2/folders.locations.buckets/updateAsync)` | 

The method `google.logging.v2.ConfigServiceV2.UpdateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.folders.locations.buckets.links](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.links)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.links/create)` | 

The method `google.logging.v2.ConfigServiceV2.CreateLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.links/delete)` | 

The method `google.logging.v2.ConfigServiceV2.DeleteLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.links/get)` | 

The method `google.logging.v2.ConfigServiceV2.GetLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.links/list)` | 

The method `google.logging.v2.ConfigServiceV2.ListLinks` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.folders.locations.buckets.views](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views/create)` | 

`POST /v2/{parent=folders/*/locations/*/buckets/*}/views` 

Creates a view over log entries in a log bucket. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views/delete)` | 

`DELETE /v2/{name=folders/*/locations/*/buckets/*/views/*}` 

Deletes a view on a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views/get)` | 

`GET /v2/{name=folders/*/locations/*/buckets/*/views/*}` 

Gets a view on a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views/list)` | 

`GET /v2/{parent=folders/*/locations/*/buckets/*}/views` 

Lists views on a log bucket. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views/patch)` | 

`PATCH /v2/{name=folders/*/locations/*/buckets/*/views/*}` 

Updates a view on a log bucket. | 
|

| 

`[getIamPolicy](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.folders.locations.buckets.views.logs](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views.logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/folders.locations.buckets.views.logs/list)` | 

`GET /v2/{parent=folders/*/locations/*/buckets/*/views/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|






## REST Resource: [v2.folders.locations.logScopes](/logging/docs/reference/v2/rest/v2/folders.locations.logScopes)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/folders.locations.logScopes/create)` | 

`POST /v2/{parent=folders/*/locations/*}/logScopes` 

Creates a log scope. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/folders.locations.logScopes/delete)` | 

`DELETE /v2/{name=folders/*/locations/*/logScopes/*}` 

Deletes a log scope. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/folders.locations.logScopes/get)` | 

`GET /v2/{name=folders/*/locations/*/logScopes/*}` 

Gets a log scope. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/folders.locations.logScopes/list)` | 

`GET /v2/{parent=folders/*/locations/*}/logScopes` 

Lists log scopes. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/folders.locations.logScopes/patch)` | 

`PATCH /v2/{logScope.name=folders/*/locations/*/logScopes/*}` 

Updates a log scope. | 
|






## REST Resource: [v2.folders.locations.operations](/logging/docs/reference/v2/rest/v2/folders.locations.operations)









| 
Methods | 
|



| 

`[cancel](/logging/docs/reference/v2/rest/v2/folders.locations.operations/cancel)` | 

`POST /v2/{name=folders/*/locations/*/operations/*}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/folders.locations.operations/get)` | 

`GET /v2/{name=folders/*/locations/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/folders.locations.operations/list)` | 

`GET /v2/{name=folders/*/locations/*}/operations` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v2.folders.locations.recentQueries](/logging/docs/reference/v2/rest/v2/folders.locations.recentQueries)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/folders.locations.recentQueries/list)` | 

`GET /v2/{parent=folders/*/locations/*}/recentQueries` 

Lists the RecentQueries that were created by the user making the request. | 
|






## REST Resource: [v2.folders.locations.savedQueries](/logging/docs/reference/v2/rest/v2/folders.locations.savedQueries)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/folders.locations.savedQueries/create)` | 

`POST /v2/{parent=folders/*/locations/*}/savedQueries` 

Creates a new SavedQuery for the user making the request. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/folders.locations.savedQueries/delete)` | 

`DELETE /v2/{name=folders/*/locations/*/savedQueries/*}` 

Deletes an existing SavedQuery that was created by the user making the request. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/folders.locations.savedQueries/get)` | 

`GET /v2/{name=folders/*/locations/*/savedQueries/*}` 

Returns all data associated with the requested query. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/folders.locations.savedQueries/list)` | 

`GET /v2/{parent=folders/*/locations/*}/savedQueries` 

Lists the SavedQueries that were created by the user making the request. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/folders.locations.savedQueries/patch)` | 

`PATCH /v2/{savedQuery.name=folders/*/locations/*/savedQueries/*}` 

Updates an existing SavedQuery. | 
|






## REST Resource: [v2.folders.logs](/logging/docs/reference/v2/rest/v2/folders.logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/folders.logs/list)` | 

`GET /v2/{parent=folders/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/folders.logs/delete)` | 

The method `google.logging.v2.LoggingServiceV2.DeleteLog` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.folders.sinks](/logging/docs/reference/v2/rest/v2/folders.sinks)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/folders.sinks/create)` | 

`POST /v2/{parent=folders/*}/sinks` 

BigQuery and GCS exports are not supported.
Creates a sink that exports specified log entries to a destination. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/folders.sinks/delete)` | 

`DELETE /v2/{sinkName=folders/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Deletes a sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/folders.sinks/get)` | 

`GET /v2/{sinkName=folders/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Gets a sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/folders.sinks/list)` | 

`GET /v2/{parent=folders/*}/sinks` 

BigQuery and GCS exports are not supported.
Lists sinks. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/folders.sinks/patch)` | 

`PATCH /v2/{sinkName=folders/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|

| 

`[update](/logging/docs/reference/v2/rest/v2/folders.sinks/update)` | 

`PUT /v2/{sinkName=folders/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|






## REST Resource: [v2.locations.buckets](/logging/docs/reference/v2/rest/v2/locations.buckets)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/locations.buckets/create)` | 

`POST /v2/{parent=*/*/locations/*}/buckets` 

Creates a log bucket that can be used to store log entries. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/locations.buckets/delete)` | 

`DELETE /v2/{name=*/*/locations/*/buckets/*}` 

Deletes a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/locations.buckets/get)` | 

`GET /v2/{name=*/*/locations/*/buckets/*}` 

Gets a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/locations.buckets/list)` | 

`GET /v2/{parent=*/*/locations/*}/buckets` 

Lists log buckets. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/locations.buckets/patch)` | 

`PATCH /v2/{name=*/*/locations/*/buckets/*}` 

Updates a log bucket. | 
|

| 

`[undelete](/logging/docs/reference/v2/rest/v2/locations.buckets/undelete)` | 

`POST /v2/{name=*/*/locations/*/buckets/*}:undelete` 

Undeletes a log bucket. | 
|

| 

`[createAsync](/logging/docs/reference/v2/rest/v2/locations.buckets/createAsync)` | 

The method `google.logging.v2.ConfigServiceV2.CreateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateAsync](/logging/docs/reference/v2/rest/v2/locations.buckets/updateAsync)` | 

The method `google.logging.v2.ConfigServiceV2.UpdateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.locations.buckets.links](/logging/docs/reference/v2/rest/v2/locations.buckets.links)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/locations.buckets.links/create)` | 

The method `google.logging.v2.ConfigServiceV2.CreateLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/locations.buckets.links/delete)` | 

The method `google.logging.v2.ConfigServiceV2.DeleteLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/locations.buckets.links/get)` | 

The method `google.logging.v2.ConfigServiceV2.GetLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/locations.buckets.links/list)` | 

The method `google.logging.v2.ConfigServiceV2.ListLinks` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.locations.buckets.views](/logging/docs/reference/v2/rest/v2/locations.buckets.views)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/locations.buckets.views/create)` | 

`POST /v2/{parent=*/*/locations/*/buckets/*}/views` 

Creates a view over log entries in a log bucket. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/locations.buckets.views/delete)` | 

`DELETE /v2/{name=*/*/locations/*/buckets/*/views/*}` 

Deletes a view on a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/locations.buckets.views/get)` | 

`GET /v2/{name=*/*/locations/*/buckets/*/views/*}` 

Gets a view on a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/locations.buckets.views/list)` | 

`GET /v2/{parent=*/*/locations/*/buckets/*}/views` 

Lists views on a log bucket. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/locations.buckets.views/patch)` | 

`PATCH /v2/{name=*/*/locations/*/buckets/*/views/*}` 

Updates a view on a log bucket. | 
|

| 

`[getIamPolicy](/logging/docs/reference/v2/rest/v2/locations.buckets.views/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/logging/docs/reference/v2/rest/v2/locations.buckets.views/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/logging/docs/reference/v2/rest/v2/locations.buckets.views/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.locations.operations](/logging/docs/reference/v2/rest/v2/locations.operations)









| 
Methods | 
|



| 

`[cancel](/logging/docs/reference/v2/rest/v2/locations.operations/cancel)` | 

`POST /v2/{name=*/*/locations/*/operations/*}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/locations.operations/get)` | 

`GET /v2/{name=*/*/locations/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/locations.operations/list)` | 

`GET /v2/{name=*/*/locations/*}/operations` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v2.logs](/logging/docs/reference/v2/rest/v2/logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/logs/list)` | 

`GET /v2/{parent=*/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/logs/delete)` | 

The method `google.logging.v2.LoggingServiceV2.DeleteLog` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.monitoredResourceDescriptors](/logging/docs/reference/v2/rest/v2/monitoredResourceDescriptors)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/monitoredResourceDescriptors/list)` | 

`GET /v2/monitoredResourceDescriptors` 

Lists the descriptors for monitored resource types used by Logging. | 
|






## REST Resource: [v2.organizations](/logging/docs/reference/v2/rest/v2/organizations)









| 
Methods | 
|



| 

`[getSettings](/logging/docs/reference/v2/rest/v2/organizations/getSettings)` | 

`GET /v2/{name=organizations/*}/settings` 

Gets the settings for the given resource. | 
|

| 

`[updateSettings](/logging/docs/reference/v2/rest/v2/organizations/updateSettings)` | 

`PATCH /v2/{name=organizations/*}/settings` 

Updates the settings for the given resource. | 
|

| 

`[getCmekSettings](/logging/docs/reference/v2/rest/v2/organizations/getCmekSettings)` | 

The method `google.logging.v2.ConfigServiceV2.GetCmekSettings` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateCmekSettings](/logging/docs/reference/v2/rest/v2/organizations/updateCmekSettings)` | 

The method `google.logging.v2.ConfigServiceV2.UpdateCmekSettings` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.organizations.exclusions](/logging/docs/reference/v2/rest/v2/organizations.exclusions)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/organizations.exclusions/create)` | 

`POST /v2/{parent=organizations/*}/exclusions` 

Creates a new exclusion in the _Default sink in a specified parent resource. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/organizations.exclusions/delete)` | 

`DELETE /v2/{name=organizations/*/exclusions/*}` 

Deletes an exclusion in the _Default sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/organizations.exclusions/get)` | 

`GET /v2/{name=organizations/*/exclusions/*}` 

Gets the description of an exclusion in the _Default sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.exclusions/list)` | 

`GET /v2/{parent=organizations/*}/exclusions` 

Lists all the exclusions on the _Default sink in a parent resource. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/organizations.exclusions/patch)` | 

`PATCH /v2/{name=organizations/*/exclusions/*}` 

Changes one or more properties of an existing exclusion in the _Default sink. | 
|






## REST Resource: [v2.organizations.locations.buckets](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets/create)` | 

`POST /v2/{parent=organizations/*/locations/*}/buckets` 

Creates a log bucket that can be used to store log entries. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets/delete)` | 

`DELETE /v2/{name=organizations/*/locations/*/buckets/*}` 

Deletes a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets/get)` | 

`GET /v2/{name=organizations/*/locations/*/buckets/*}` 

Gets a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets/list)` | 

`GET /v2/{parent=organizations/*/locations/*}/buckets` 

Lists log buckets. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets/patch)` | 

`PATCH /v2/{name=organizations/*/locations/*/buckets/*}` 

Updates a log bucket. | 
|

| 

`[undelete](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets/undelete)` | 

`POST /v2/{name=organizations/*/locations/*/buckets/*}:undelete` 

Undeletes a log bucket. | 
|

| 

`[createAsync](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets/createAsync)` | 

The method `google.logging.v2.ConfigServiceV2.CreateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateAsync](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets/updateAsync)` | 

The method `google.logging.v2.ConfigServiceV2.UpdateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.organizations.locations.buckets.links](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.links)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.links/create)` | 

The method `google.logging.v2.ConfigServiceV2.CreateLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.links/delete)` | 

The method `google.logging.v2.ConfigServiceV2.DeleteLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.links/get)` | 

The method `google.logging.v2.ConfigServiceV2.GetLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.links/list)` | 

The method `google.logging.v2.ConfigServiceV2.ListLinks` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.organizations.locations.buckets.views](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views/create)` | 

`POST /v2/{parent=organizations/*/locations/*/buckets/*}/views` 

Creates a view over log entries in a log bucket. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views/delete)` | 

`DELETE /v2/{name=organizations/*/locations/*/buckets/*/views/*}` 

Deletes a view on a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views/get)` | 

`GET /v2/{name=organizations/*/locations/*/buckets/*/views/*}` 

Gets a view on a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views/list)` | 

`GET /v2/{parent=organizations/*/locations/*/buckets/*}/views` 

Lists views on a log bucket. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views/patch)` | 

`PATCH /v2/{name=organizations/*/locations/*/buckets/*/views/*}` 

Updates a view on a log bucket. | 
|

| 

`[getIamPolicy](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.organizations.locations.buckets.views.logs](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views.logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.locations.buckets.views.logs/list)` | 

`GET /v2/{parent=organizations/*/locations/*/buckets/*/views/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|






## REST Resource: [v2.organizations.locations.logScopes](/logging/docs/reference/v2/rest/v2/organizations.locations.logScopes)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/organizations.locations.logScopes/create)` | 

`POST /v2/{parent=organizations/*/locations/*}/logScopes` 

Creates a log scope. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/organizations.locations.logScopes/delete)` | 

`DELETE /v2/{name=organizations/*/locations/*/logScopes/*}` 

Deletes a log scope. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/organizations.locations.logScopes/get)` | 

`GET /v2/{name=organizations/*/locations/*/logScopes/*}` 

Gets a log scope. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.locations.logScopes/list)` | 

`GET /v2/{parent=organizations/*/locations/*}/logScopes` 

Lists log scopes. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/organizations.locations.logScopes/patch)` | 

`PATCH /v2/{logScope.name=organizations/*/locations/*/logScopes/*}` 

Updates a log scope. | 
|






## REST Resource: [v2.organizations.locations.operations](/logging/docs/reference/v2/rest/v2/organizations.locations.operations)









| 
Methods | 
|



| 

`[cancel](/logging/docs/reference/v2/rest/v2/organizations.locations.operations/cancel)` | 

`POST /v2/{name=organizations/*/locations/*/operations/*}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/organizations.locations.operations/get)` | 

`GET /v2/{name=organizations/*/locations/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.locations.operations/list)` | 

`GET /v2/{name=organizations/*/locations/*}/operations` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v2.organizations.locations.recentQueries](/logging/docs/reference/v2/rest/v2/organizations.locations.recentQueries)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.locations.recentQueries/list)` | 

`GET /v2/{parent=organizations/*/locations/*}/recentQueries` 

Lists the RecentQueries that were created by the user making the request. | 
|






## REST Resource: [v2.organizations.locations.savedQueries](/logging/docs/reference/v2/rest/v2/organizations.locations.savedQueries)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/organizations.locations.savedQueries/create)` | 

`POST /v2/{parent=organizations/*/locations/*}/savedQueries` 

Creates a new SavedQuery for the user making the request. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/organizations.locations.savedQueries/delete)` | 

`DELETE /v2/{name=organizations/*/locations/*/savedQueries/*}` 

Deletes an existing SavedQuery that was created by the user making the request. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/organizations.locations.savedQueries/get)` | 

`GET /v2/{name=organizations/*/locations/*/savedQueries/*}` 

Returns all data associated with the requested query. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.locations.savedQueries/list)` | 

`GET /v2/{parent=organizations/*/locations/*}/savedQueries` 

Lists the SavedQueries that were created by the user making the request. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/organizations.locations.savedQueries/patch)` | 

`PATCH /v2/{savedQuery.name=organizations/*/locations/*/savedQueries/*}` 

Updates an existing SavedQuery. | 
|






## REST Resource: [v2.organizations.logs](/logging/docs/reference/v2/rest/v2/organizations.logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.logs/list)` | 

`GET /v2/{parent=organizations/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/organizations.logs/delete)` | 

The method `google.logging.v2.LoggingServiceV2.DeleteLog` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.organizations.sinks](/logging/docs/reference/v2/rest/v2/organizations.sinks)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/organizations.sinks/create)` | 

`POST /v2/{parent=organizations/*}/sinks` 

BigQuery and GCS exports are not supported.
Creates a sink that exports specified log entries to a destination. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/organizations.sinks/delete)` | 

`DELETE /v2/{sinkName=organizations/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Deletes a sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/organizations.sinks/get)` | 

`GET /v2/{sinkName=organizations/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Gets a sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/organizations.sinks/list)` | 

`GET /v2/{parent=organizations/*}/sinks` 

BigQuery and GCS exports are not supported.
Lists sinks. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/organizations.sinks/patch)` | 

`PATCH /v2/{sinkName=organizations/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|

| 

`[update](/logging/docs/reference/v2/rest/v2/organizations.sinks/update)` | 

`PUT /v2/{sinkName=organizations/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|






## REST Resource: [v2.projects](/logging/docs/reference/v2/rest/v2/projects)









| 
Methods | 
|



| 

`[getSettings](/logging/docs/reference/v2/rest/v2/projects/getSettings)` | 

`GET /v2/{name=projects/*}/settings` 

Gets the settings for the given resource. | 
|

| 

`[getCmekSettings](/logging/docs/reference/v2/rest/v2/projects/getCmekSettings)` | 

The method `google.logging.v2.ConfigServiceV2.GetCmekSettings` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.projects.exclusions](/logging/docs/reference/v2/rest/v2/projects.exclusions)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/projects.exclusions/create)` | 

`POST /v2/{parent=projects/*}/exclusions` 

Creates a new exclusion in the _Default sink in a specified parent resource. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/projects.exclusions/delete)` | 

`DELETE /v2/{name=projects/*/exclusions/*}` 

Deletes an exclusion in the _Default sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/projects.exclusions/get)` | 

`GET /v2/{name=projects/*/exclusions/*}` 

Gets the description of an exclusion in the _Default sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/projects.exclusions/list)` | 

`GET /v2/{parent=projects/*}/exclusions` 

Lists all the exclusions on the _Default sink in a parent resource. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/projects.exclusions/patch)` | 

`PATCH /v2/{name=projects/*/exclusions/*}` 

Changes one or more properties of an existing exclusion in the _Default sink. | 
|






## REST Resource: [v2.projects.locations.buckets](/logging/docs/reference/v2/rest/v2/projects.locations.buckets)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/create)` | 

`POST /v2/{parent=projects/*/locations/*}/buckets` 

Creates a log bucket that can be used to store log entries. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/delete)` | 

`DELETE /v2/{name=projects/*/locations/*/buckets/*}` 

Deletes a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/get)` | 

`GET /v2/{name=projects/*/locations/*/buckets/*}` 

Gets a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/list)` | 

`GET /v2/{parent=projects/*/locations/*}/buckets` 

Lists log buckets. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch)` | 

`PATCH /v2/{name=projects/*/locations/*/buckets/*}` 

Updates a log bucket. | 
|

| 

`[undelete](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/undelete)` | 

`POST /v2/{name=projects/*/locations/*/buckets/*}:undelete` 

Undeletes a log bucket. | 
|

| 

`[createAsync](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/createAsync)` | 

The method `google.logging.v2.ConfigServiceV2.CreateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateAsync](/logging/docs/reference/v2/rest/v2/projects.locations.buckets/updateAsync)` | 

The method `google.logging.v2.ConfigServiceV2.UpdateBucketAsync` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.projects.locations.buckets.links](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/create)` | 

The method `google.logging.v2.ConfigServiceV2.CreateLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/delete)` | 

The method `google.logging.v2.ConfigServiceV2.DeleteLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/get)` | 

The method `google.logging.v2.ConfigServiceV2.GetLink` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/list)` | 

The method `google.logging.v2.ConfigServiceV2.ListLinks` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.projects.locations.buckets.views](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views/create)` | 

`POST /v2/{parent=projects/*/locations/*/buckets/*}/views` 

Creates a view over log entries in a log bucket. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views/delete)` | 

`DELETE /v2/{name=projects/*/locations/*/buckets/*/views/*}` 

Deletes a view on a log bucket. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views/get)` | 

`GET /v2/{name=projects/*/locations/*/buckets/*/views/*}` 

Gets a view on a log bucket. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views/list)` | 

`GET /v2/{parent=projects/*/locations/*/buckets/*}/views` 

Lists views on a log bucket. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views/patch)` | 

`PATCH /v2/{name=projects/*/locations/*/buckets/*/views/*}` 

Updates a view on a log bucket. | 
|

| 

`[getIamPolicy](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.projects.locations.buckets.views.logs](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views.logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views.logs/list)` | 

`GET /v2/{parent=projects/*/locations/*/buckets/*/views/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|






## REST Resource: [v2.projects.locations.logScopes](/logging/docs/reference/v2/rest/v2/projects.locations.logScopes)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/create)` | 

`POST /v2/{parent=projects/*/locations/*}/logScopes` 

Creates a log scope. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/delete)` | 

`DELETE /v2/{name=projects/*/locations/*/logScopes/*}` 

Deletes a log scope. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/get)` | 

`GET /v2/{name=projects/*/locations/*/logScopes/*}` 

Gets a log scope. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/list)` | 

`GET /v2/{parent=projects/*/locations/*}/logScopes` 

Lists log scopes. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/patch)` | 

`PATCH /v2/{logScope.name=projects/*/locations/*/logScopes/*}` 

Updates a log scope. | 
|






## REST Resource: [v2.projects.locations.operations](/logging/docs/reference/v2/rest/v2/projects.locations.operations)









| 
Methods | 
|



| 

`[cancel](/logging/docs/reference/v2/rest/v2/projects.locations.operations/cancel)` | 

`POST /v2/{name=projects/*/locations/*/operations/*}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/projects.locations.operations/get)` | 

`GET /v2/{name=projects/*/locations/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/projects.locations.operations/list)` | 

`GET /v2/{name=projects/*/locations/*}/operations` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v2.projects.locations.recentQueries](/logging/docs/reference/v2/rest/v2/projects.locations.recentQueries)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/projects.locations.recentQueries/list)` | 

`GET /v2/{parent=projects/*/locations/*}/recentQueries` 

Lists the RecentQueries that were created by the user making the request. | 
|






## REST Resource: [v2.projects.locations.savedQueries](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create)` | 

`POST /v2/{parent=projects/*/locations/*}/savedQueries` 

Creates a new SavedQuery for the user making the request. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/delete)` | 

`DELETE /v2/{name=projects/*/locations/*/savedQueries/*}` 

Deletes an existing SavedQuery that was created by the user making the request. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/get)` | 

`GET /v2/{name=projects/*/locations/*/savedQueries/*}` 

Returns all data associated with the requested query. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/list)` | 

`GET /v2/{parent=projects/*/locations/*}/savedQueries` 

Lists the SavedQueries that were created by the user making the request. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/patch)` | 

`PATCH /v2/{savedQuery.name=projects/*/locations/*/savedQueries/*}` 

Updates an existing SavedQuery. | 
|






## REST Resource: [v2.projects.logs](/logging/docs/reference/v2/rest/v2/projects.logs)









| 
Methods | 
|



| 

`[list](/logging/docs/reference/v2/rest/v2/projects.logs/list)` | 

`GET /v2/{parent=projects/*}/logs` 

Lists the logs in projects, organizations, folders, or billing accounts. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/projects.logs/delete)` | 

The method `google.logging.v2.LoggingServiceV2.DeleteLog` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v2.projects.sinks](/logging/docs/reference/v2/rest/v2/projects.sinks)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/projects.sinks/create)` | 

`POST /v2/{parent=projects/*}/sinks` 

BigQuery and GCS exports are not supported.
Creates a sink that exports specified log entries to a destination. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/projects.sinks/delete)` | 

`DELETE /v2/{sinkName=projects/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Deletes a sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/projects.sinks/get)` | 

`GET /v2/{sinkName=projects/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Gets a sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/projects.sinks/list)` | 

`GET /v2/{parent=projects/*}/sinks` 

BigQuery and GCS exports are not supported.
Lists sinks. | 
|

| 

`[patch](/logging/docs/reference/v2/rest/v2/projects.sinks/patch)` | 

`PATCH /v2/{sinkName=projects/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|

| 

`[update](/logging/docs/reference/v2/rest/v2/projects.sinks/update)` | 

`PUT /v2/{sinkName=projects/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|






## REST Resource: [v2.sinks](/logging/docs/reference/v2/rest/v2/sinks)









| 
Methods | 
|



| 

`[create](/logging/docs/reference/v2/rest/v2/sinks/create)` | 

`POST /v2/{parent=*/*}/sinks` 

BigQuery and GCS exports are not supported.
Creates a sink that exports specified log entries to a destination. | 
|

| 

`[delete](/logging/docs/reference/v2/rest/v2/sinks/delete)` | 

`DELETE /v2/{sinkName=*/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Deletes a sink. | 
|

| 

`[get](/logging/docs/reference/v2/rest/v2/sinks/get)` | 

`GET /v2/{sinkName=*/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Gets a sink. | 
|

| 

`[list](/logging/docs/reference/v2/rest/v2/sinks/list)` | 

`GET /v2/{parent=*/*}/sinks` 

BigQuery and GCS exports are not supported.
Lists sinks. | 
|

| 

`[update](/logging/docs/reference/v2/rest/v2/sinks/update)` | 

`PUT /v2/{sinkName=*/*/sinks/*}` 

BigQuery and GCS exports are not supported.
Updates a sink. | 
|