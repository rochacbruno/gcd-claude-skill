# Cloud Quotas API

Source: https://documentation.s3ns.fr/docs/quotas/reference/rest
Last updated: 2025-12-10

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://documentation.s3ns.fr/docs/quotas)






- 








[

Reference

](https://documentation.s3ns.fr/docs/quotas/apis)












# Cloud Quotas API 


















Cloud Quotas API provides GCP service consumers with management and observability for resource usage, quotas, and restrictions of the services they consume.




- [REST Resource: v1.folders.locations.quotaPreferences](#v1.folders.locations.quotaPreferences)

- [REST Resource: v1.folders.locations.services.quotaInfos](#v1.folders.locations.services.quotaInfos)

- [REST Resource: v1.organizations.locations.quotaPreferences](#v1.organizations.locations.quotaPreferences)

- [REST Resource: v1.organizations.locations.services.quotaInfos](#v1.organizations.locations.services.quotaInfos)

- [REST Resource: v1.projects.locations.quotaPreferences](#v1.projects.locations.quotaPreferences)

- [REST Resource: v1.projects.locations.services.quotaInfos](#v1.projects.locations.services.quotaInfos)





## Service: cloudquotas.googleapis.com



To call this service, we recommend that you use the Google-provided [client libraries](https://documentation.s3ns.fr/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document



A [Discovery Document](https://s3nsapis.fr/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://cloudquotas.s3nsapis.fr/$discovery/rest?version=v1](https://cloudquotas.s3nsapis.fr/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://documentation.s3ns.fr/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://cloudquotas.s3nsapis.fr`






## REST Resource: [v1.folders.locations.quotaPreferences](/docs/quotas/reference/rest/v1/folders.locations.quotaPreferences)









| 
Methods | 
|



| 

`[create](/docs/quotas/reference/rest/v1/folders.locations.quotaPreferences/create)` | 

`POST /v1/{parent=folders/*/locations/*}/quotaPreferences` 

Creates a new QuotaPreference that declares the desired value for a quota. | 
|

| 

`[get](/docs/quotas/reference/rest/v1/folders.locations.quotaPreferences/get)` | 

`GET /v1/{name=folders/*/locations/*/quotaPreferences/*}` 

Gets details of a single QuotaPreference. | 
|

| 

`[list](/docs/quotas/reference/rest/v1/folders.locations.quotaPreferences/list)` | 

`GET /v1/{parent=folders/*/locations/*}/quotaPreferences` 

Lists QuotaPreferences in a given project, folder or organization. | 
|

| 

`[patch](/docs/quotas/reference/rest/v1/folders.locations.quotaPreferences/patch)` | 

`PATCH /v1/{quotaPreference.name=folders/*/locations/*/quotaPreferences/*}` 

Updates the parameters of a single QuotaPreference. | 
|






## REST Resource: [v1.folders.locations.services.quotaInfos](/docs/quotas/reference/rest/v1/folders.locations.services.quotaInfos)









| 
Methods | 
|



| 

`[get](/docs/quotas/reference/rest/v1/folders.locations.services.quotaInfos/get)` | 

`GET /v1/{name=folders/*/locations/*/services/*/quotaInfos/*}` 

Retrieve the QuotaInfo of a quota for a project, folder or organization. | 
|

| 

`[list](/docs/quotas/reference/rest/v1/folders.locations.services.quotaInfos/list)` | 

`GET /v1/{parent=folders/*/locations/*/services/*}/quotaInfos` 

Lists QuotaInfos of all quotas for a given project, folder or organization. | 
|






## REST Resource: [v1.organizations.locations.quotaPreferences](/docs/quotas/reference/rest/v1/organizations.locations.quotaPreferences)









| 
Methods | 
|



| 

`[create](/docs/quotas/reference/rest/v1/organizations.locations.quotaPreferences/create)` | 

`POST /v1/{parent=organizations/*/locations/*}/quotaPreferences` 

Creates a new QuotaPreference that declares the desired value for a quota. | 
|

| 

`[get](/docs/quotas/reference/rest/v1/organizations.locations.quotaPreferences/get)` | 

`GET /v1/{name=organizations/*/locations/*/quotaPreferences/*}` 

Gets details of a single QuotaPreference. | 
|

| 

`[list](/docs/quotas/reference/rest/v1/organizations.locations.quotaPreferences/list)` | 

`GET /v1/{parent=organizations/*/locations/*}/quotaPreferences` 

Lists QuotaPreferences in a given project, folder or organization. | 
|

| 

`[patch](/docs/quotas/reference/rest/v1/organizations.locations.quotaPreferences/patch)` | 

`PATCH /v1/{quotaPreference.name=organizations/*/locations/*/quotaPreferences/*}` 

Updates the parameters of a single QuotaPreference. | 
|






## REST Resource: [v1.organizations.locations.services.quotaInfos](/docs/quotas/reference/rest/v1/organizations.locations.services.quotaInfos)









| 
Methods | 
|



| 

`[get](/docs/quotas/reference/rest/v1/organizations.locations.services.quotaInfos/get)` | 

`GET /v1/{name=organizations/*/locations/*/services/*/quotaInfos/*}` 

Retrieve the QuotaInfo of a quota for a project, folder or organization. | 
|

| 

`[list](/docs/quotas/reference/rest/v1/organizations.locations.services.quotaInfos/list)` | 

`GET /v1/{parent=organizations/*/locations/*/services/*}/quotaInfos` 

Lists QuotaInfos of all quotas for a given project, folder or organization. | 
|






## REST Resource: [v1.projects.locations.quotaPreferences](/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences)









| 
Methods | 
|



| 

`[create](/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/create)` | 

`POST /v1/{parent=projects/*/locations/*}/quotaPreferences` 

Creates a new QuotaPreference that declares the desired value for a quota. | 
|

| 

`[get](/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/get)` | 

`GET /v1/{name=projects/*/locations/*/quotaPreferences/*}` 

Gets details of a single QuotaPreference. | 
|

| 

`[list](/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/list)` | 

`GET /v1/{parent=projects/*/locations/*}/quotaPreferences` 

Lists QuotaPreferences in a given project, folder or organization. | 
|

| 

`[patch](/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/patch)` | 

`PATCH /v1/{quotaPreference.name=projects/*/locations/*/quotaPreferences/*}` 

Updates the parameters of a single QuotaPreference. | 
|






## REST Resource: [v1.projects.locations.services.quotaInfos](/docs/quotas/reference/rest/v1/projects.locations.services.quotaInfos)









| 
Methods | 
|



| 

`[get](/docs/quotas/reference/rest/v1/projects.locations.services.quotaInfos/get)` | 

`GET /v1/{name=projects/*/locations/*/services/*/quotaInfos/*}` 

Retrieve the QuotaInfo of a quota for a project, folder or organization. | 
|

| 

`[list](/docs/quotas/reference/rest/v1/projects.locations.services.quotaInfos/list)` | 

`GET /v1/{parent=projects/*/locations/*/services/*}/quotaInfos` 

Lists QuotaInfos of all quotas for a given project, folder or organization. | 
|