# API Keys API Documentation

Source: https://documentation.s3ns.fr/api-keys/docs/reference/rest
Last updated: 2025-08-06

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/api-keys/docs/tpc-differences) for more details.














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

Access and resource management

](https://documentation.s3ns.fr/docs/access-resources)






- 








[

Service Usage

](https://documentation.s3ns.fr/service-usage/docs)






- 








[

API Keys API Documentation

](https://documentation.s3ns.fr/api-keys/docs)






- 








[

Reference

](https://documentation.s3ns.fr/api-keys/docs/apis)












# API Keys API 






- On this page 
- [ Service: apikeys.googleapis.com ](#service:-apikeys.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)

- [ REST Resource: v2.keys ](#rest-resource:-v2.keys)
- [ REST Resource: v2.operations ](#rest-resource:-v2.operations)
- [ REST Resource: v2.projects.locations.keys ](#rest-resource:-v2.projects.locations.keys)
- 













Manages the API keys associated with developer projects.




- [REST Resource: v2.keys](#v2.keys)

- [REST Resource: v2.operations](#v2.operations)

- [REST Resource: v2.projects.locations.keys](#v2.projects.locations.keys)





## Service: apikeys. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://documentation.s3ns.fr/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://apikeys.s3nsapis.fr/$discovery/rest?version=v2](https://apikeys.s3nsapis.fr/$discovery/rest?version=v2)





### Service endpoint



A [service endpoint](https://documentation.s3ns.fr/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://apikeys.s3nsapis.fr`






## REST Resource: [v2. keys](/api-keys/docs/reference/rest/v2/keys)









| 
Methods | 
|



| 

`[lookup Key](/api-keys/docs/reference/rest/v2/keys/lookupKey)` | 

`GET / v2/ keys:lookup Key` 

Find the parent project and resource name of the API key that matches the key string in the request. | 
|






## REST Resource: [v2. operations](/api-keys/docs/reference/rest/v2/operations)









| 
Methods | 
|



| 

`[get](/api-keys/docs/reference/rest/v2/operations/get)` | 

The method `google. longrunning. Operations. Get Operation` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v2.projects.locations.keys](/api-keys/docs/reference/rest/v2/projects.locations.keys)









| 
Methods | 
|



| 

`[create](/api-keys/docs/reference/rest/v2/projects.locations.keys/create)` | 

`POST /v2/{parent=projects/*/locations/*}/keys` 

Creates a new API key. | 
|

| 

`[delete](/api-keys/docs/reference/rest/v2/projects.locations.keys/delete)` | 

`DELETE /v2/{name=projects/*/locations/*/keys/*}` 

Deletes an API key. | 
|

| 

`[get](/api-keys/docs/reference/rest/v2/projects.locations.keys/get)` | 

`GET /v2/{name=projects/*/locations/*/keys/*}` 

Gets the metadata for an API key. | 
|

| 

`[getKeyString](/api-keys/docs/reference/rest/v2/projects.locations.keys/getKeyString)` | 

`GET /v2/{name=projects/*/locations/*/keys/*}/keyString` 

Get the key string for an API key. | 
|

| 

`[list](/api-keys/docs/reference/rest/v2/projects.locations.keys/list)` | 

`GET /v2/{parent=projects/*/locations/*}/keys` 

Lists the API keys owned by a project. | 
|

| 

`[patch](/api-keys/docs/reference/rest/v2/projects.locations.keys/patch)` | 

`PATCH /v2/{key.name=projects/*/locations/*/keys/*}` 

Patches the modifiable fields of an API key. | 
|

| 

`[undelete](/api-keys/docs/reference/rest/v2/projects.locations.keys/undelete)` | 

`POST /v2/{name=projects/*/locations/*/keys/*}:undelete` 

Undeletes an API key which was deleted within 30 days. | 
|