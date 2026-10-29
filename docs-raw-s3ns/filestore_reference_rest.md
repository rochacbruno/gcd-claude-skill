# Cloud Filestore API

Source: https://documentation.s3ns.fr/filestore/docs/reference/rest
Last updated: 2025-12-02

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/filestore/docs/tpc-differences) for more details.














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

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Filestore

](https://documentation.s3ns.fr/filestore/docs)






- 








[

Reference

](https://documentation.s3ns.fr/filestore/docs/apis)












# Cloud Filestore API 


















The Cloud Filestore API is used for creating and managing cloud file servers.




- [REST Resource: v1.projects.locations](#v1.projects.locations)

- [REST Resource: v1.projects.locations.backups](#v1.projects.locations.backups)

- [REST Resource: v1.projects.locations.instances](#v1.projects.locations.instances)

- [REST Resource: v1.projects.locations.instances.snapshots](#v1.projects.locations.instances.snapshots)

- [REST Resource: v1.projects.locations.operations](#v1.projects.locations.operations)





## Service: file.googleapis.com



To call this service, we recommend that you use the Google-provided [client libraries](https://documentation.s3ns.fr/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document



A [Discovery Document](https://s3nsapis.fr/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://file.s3nsapis.fr/$discovery/rest?version=v1](https://file.s3nsapis.fr/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://documentation.s3ns.fr/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://file.s3nsapis.fr`






## REST Resource: [v1.projects.locations](/filestore/docs/reference/rest/v1/projects.locations)









| 
Methods | 
|



| 

`[get](/filestore/docs/reference/rest/v1/projects.locations/get)` | 

The method `google.cloud.location.Locations.GetLocation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/filestore/docs/reference/rest/v1/projects.locations/list)` | 

The method `google.cloud.location.Locations.ListLocations` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.projects.locations.backups](/filestore/docs/reference/rest/v1/projects.locations.backups)









| 
Methods | 
|



| 

`[create](/filestore/docs/reference/rest/v1/projects.locations.backups/create)` | 

`POST /v1/{parent=projects/*/locations/*}/backups` 

Creates a backup. | 
|

| 

`[delete](/filestore/docs/reference/rest/v1/projects.locations.backups/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/backups/*}` 

Deletes a backup. | 
|

| 

`[get](/filestore/docs/reference/rest/v1/projects.locations.backups/get)` | 

`GET /v1/{name=projects/*/locations/*/backups/*}` 

Gets the details of a specific backup. | 
|

| 

`[list](/filestore/docs/reference/rest/v1/projects.locations.backups/list)` | 

`GET /v1/{parent=projects/*/locations/*}/backups` 

Lists all backups in a project for either a specified location or for all locations. | 
|

| 

`[patch](/filestore/docs/reference/rest/v1/projects.locations.backups/patch)` | 

`PATCH /v1/{backup.name=projects/*/locations/*/backups/*}` 

Updates the settings of a specific backup. | 
|






## REST Resource: [v1.projects.locations.instances](/filestore/docs/reference/rest/v1/projects.locations.instances)









| 
Methods | 
|



| 

`[create](/filestore/docs/reference/rest/v1/projects.locations.instances/create)` | 

`POST /v1/{parent=projects/*/locations/*}/instances` 

Zonal instances, Managed AD integration, Private Service Access and Private Service Connect are not supported.
Creates an instance. | 
|

| 

`[delete](/filestore/docs/reference/rest/v1/projects.locations.instances/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/instances/*}` 

Deletes an instance. | 
|

| 

`[get](/filestore/docs/reference/rest/v1/projects.locations.instances/get)` | 

`GET /v1/{name=projects/*/locations/*/instances/*}` 

Gets the details of a specific instance. | 
|

| 

`[list](/filestore/docs/reference/rest/v1/projects.locations.instances/list)` | 

`GET /v1/{parent=projects/*/locations/*}/instances` 

Lists all instances in a project for either a specified location or for all locations. | 
|

| 

`[patch](/filestore/docs/reference/rest/v1/projects.locations.instances/patch)` | 

`PATCH /v1/{instance.name=projects/*/locations/*/instances/*}` 

Updates the settings of a specific instance. | 
|

| 

`[promoteReplica](/filestore/docs/reference/rest/v1/projects.locations.instances/promoteReplica)` | 

`POST /v1/{name=projects/*/locations/*/instances/*}:promoteReplica` 

Promote the standby instance (replica). | 
|

| 

`[restore](/filestore/docs/reference/rest/v1/projects.locations.instances/restore)` | 

`POST /v1/{name=projects/*/locations/*/instances/*}:restore` 

Restores an existing instance's file share from a backup. | 
|

| 

`[revert](/filestore/docs/reference/rest/v1/projects.locations.instances/revert)` | 

`POST /v1/{name=projects/*/locations/*/instances/*}:revert` 

Revert an existing instance's file system to a specified snapshot. | 
|

| 

`[pauseReplica](/filestore/docs/reference/rest/v1/projects.locations.instances/pauseReplica)` | 

The method `google.cloud.filestore.v1.CloudFilestoreManager.PauseReplica` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resumeReplica](/filestore/docs/reference/rest/v1/projects.locations.instances/resumeReplica)` | 

The method `google.cloud.filestore.v1.CloudFilestoreManager.ResumeReplica` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.projects.locations.instances.snapshots](/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots)









| 
Methods | 
|



| 

`[create](/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/create)` | 

`POST /v1/{parent=projects/*/locations/*/instances/*}/snapshots` 

Creates a snapshot. | 
|

| 

`[delete](/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/instances/*/snapshots/*}` 

Deletes a snapshot. | 
|

| 

`[get](/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/get)` | 

`GET /v1/{name=projects/*/locations/*/instances/*/snapshots/*}` 

Gets the details of a specific snapshot. | 
|

| 

`[list](/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/list)` | 

`GET /v1/{parent=projects/*/locations/*/instances/*}/snapshots` 

Lists all snapshots in a project for either a specified location or for all locations. | 
|

| 

`[patch](/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/patch)` | 

`PATCH /v1/{snapshot.name=projects/*/locations/*/instances/*/snapshots/*}` 

Updates the settings of a specific snapshot. | 
|






## REST Resource: [v1.projects.locations.operations](/filestore/docs/reference/rest/v1/projects.locations.operations)









| 
Methods | 
|



| 

`[cancel](/filestore/docs/reference/rest/v1/projects.locations.operations/cancel)` | 

`POST /v1/{name=projects/*/locations/*/operations/*}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[delete](/filestore/docs/reference/rest/v1/projects.locations.operations/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/operations/*}` 

Deletes a long-running operation. | 
|

| 

`[get](/filestore/docs/reference/rest/v1/projects.locations.operations/get)` | 

`GET /v1/{name=projects/*/locations/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/filestore/docs/reference/rest/v1/projects.locations.operations/list)` | 

`GET /v1/{name=projects/*/locations/*}/operations` 

Lists operations that match the specified filter in the request. | 
|