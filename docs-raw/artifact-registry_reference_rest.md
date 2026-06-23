# Artifact Registry API

Source: https://berlin.devsitetest.how/artifact-registry/docs/reference/rest
Last updated: 2025-11-14

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/artifact-registry/docs/tpc-differences) for more details.














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

Application development

](https://berlin.devsitetest.how/docs/application-development)






- 








[

Artifact Registry

](https://berlin.devsitetest.how/artifact-registry/docs)






- 








[

Reference

](https://berlin.devsitetest.how/artifact-registry/docs/apis)












# Artifact Registry API 






- On this page 
- [ Service: artifactregistry.googleapis.com ](#service:-artifactregistry.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)
- [ Regional service endpoint ](#regional-service-endpoint)

- [ REST Resource: v1.projects ](#rest-resource:-v1.projects)
- [ REST Resource: v1.projects.locations ](#rest-resource:-v1.projects.locations)
- [ REST Resource: v1.projects.locations.operations ](#rest-resource:-v1.projects.locations.operations)
- [ REST Resource: v1.projects.locations.repositories ](#rest-resource:-v1.projects.locations.repositories)
- [ REST Resource: v1.projects.locations.repositories.aptArtifacts ](#rest-resource:-v1.projects.locations.repositories.aptartifacts)
- [ REST Resource: v1.projects.locations.repositories.attachments ](#rest-resource:-v1.projects.locations.repositories.attachments)
- [ REST Resource: v1.projects.locations.repositories.dockerImages ](#rest-resource:-v1.projects.locations.repositories.dockerimages)
- [ REST Resource: v1.projects.locations.repositories.files ](#rest-resource:-v1.projects.locations.repositories.files)
- [ REST Resource: v1.projects.locations.repositories.genericArtifacts ](#rest-resource:-v1.projects.locations.repositories.genericartifacts)
- [ REST Resource: v1.projects.locations.repositories.goModules ](#rest-resource:-v1.projects.locations.repositories.gomodules)
- [ REST Resource: v1.projects.locations.repositories.googetArtifacts ](#rest-resource:-v1.projects.locations.repositories.googetartifacts)
- [ REST Resource: v1.projects.locations.repositories.kfpArtifacts ](#rest-resource:-v1.projects.locations.repositories.kfpartifacts)
- [ REST Resource: v1.projects.locations.repositories.mavenArtifacts ](#rest-resource:-v1.projects.locations.repositories.mavenartifacts)
- [ REST Resource: v1.projects.locations.repositories.npmPackages ](#rest-resource:-v1.projects.locations.repositories.npmpackages)
- [ REST Resource: v1.projects.locations.repositories.packages ](#rest-resource:-v1.projects.locations.repositories.packages)
- [ REST Resource: v1.projects.locations.repositories.packages.tags ](#rest-resource:-v1.projects.locations.repositories.packages.tags)
- [ REST Resource: v1.projects.locations.repositories.packages.versions ](#rest-resource:-v1.projects.locations.repositories.packages.versions)
- [ REST Resource: v1.projects.locations.repositories.pythonPackages ](#rest-resource:-v1.projects.locations.repositories.pythonpackages)
- [ REST Resource: v1.projects.locations.repositories.rules ](#rest-resource:-v1.projects.locations.repositories.rules)
- [ REST Resource: v1.projects.locations.repositories.yumArtifacts ](#rest-resource:-v1.projects.locations.repositories.yumartifacts)
- 













Store and manage build artifacts in a scalable and integrated service built on Sovereign Cloud infrastructure.




- [REST Resource: v1.projects](#v1.projects)

- [REST Resource: v1.projects.locations](#v1.projects.locations)

- [REST Resource: v1.projects.locations.operations](#v1.projects.locations.operations)

- [REST Resource: v1.projects.locations.repositories](#v1.projects.locations.repositories)

- [REST Resource: v1.projects.locations.repositories.aptArtifacts](#v1.projects.locations.repositories.aptArtifacts)

- [REST Resource: v1.projects.locations.repositories.attachments](#v1.projects.locations.repositories.attachments)

- [REST Resource: v1.projects.locations.repositories.dockerImages](#v1.projects.locations.repositories.dockerImages)

- [REST Resource: v1.projects.locations.repositories.files](#v1.projects.locations.repositories.files)

- [REST Resource: v1.projects.locations.repositories.genericArtifacts](#v1.projects.locations.repositories.genericArtifacts)

- [REST Resource: v1.projects.locations.repositories.goModules](#v1.projects.locations.repositories.goModules)

- [REST Resource: v1.projects.locations.repositories.googetArtifacts](#v1.projects.locations.repositories.googetArtifacts)

- [REST Resource: v1.projects.locations.repositories.kfpArtifacts](#v1.projects.locations.repositories.kfpArtifacts)

- [REST Resource: v1.projects.locations.repositories.mavenArtifacts](#v1.projects.locations.repositories.mavenArtifacts)

- [REST Resource: v1.projects.locations.repositories.npmPackages](#v1.projects.locations.repositories.npmPackages)

- [REST Resource: v1.projects.locations.repositories.packages](#v1.projects.locations.repositories.packages)

- [REST Resource: v1.projects.locations.repositories.packages.tags](#v1.projects.locations.repositories.packages.tags)

- [REST Resource: v1.projects.locations.repositories.packages.versions](#v1.projects.locations.repositories.packages.versions)

- [REST Resource: v1.projects.locations.repositories.pythonPackages](#v1.projects.locations.repositories.pythonPackages)

- [REST Resource: v1.projects.locations.repositories.rules](#v1.projects.locations.repositories.rules)

- [REST Resource: v1.projects.locations.repositories.yumArtifacts](#v1.projects.locations.repositories.yumArtifacts)





## Service: artifactregistry. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://artifactregistry.apis-berlin-build0.goog/$discovery/rest?version=v1](https://artifactregistry.apis-berlin-build0.goog/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://artifactregistry.apis-berlin-build0.goog`





### Regional service endpoint



A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 
global 

- `https://artifactregistry.apis-berlin-build0.goog` 





## REST Resource: [v1. projects](/artifact-registry/docs/reference/rest/v1/projects)









| 
Methods | 
|



| 

`[get Project Settings](/artifact-registry/docs/reference/rest/v1/projects/getProjectSettings)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetProjectSettings` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateProjectSettings](/artifact-registry/docs/reference/rest/v1/projects/updateProjectSettings)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateProjectSettings` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations](/artifact-registry/docs/reference/rest/v1/projects.locations)









| 
Methods | 
|



| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations/get)` | 

The method `google.cloud.location.Locations.GetLocation` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[getVpcscConfig](/artifact-registry/docs/reference/rest/v1/projects.locations/getVpcscConfig)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetVPCSCConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations/list)` | 

The method `google.cloud.location.Locations.ListLocations` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateVpcscConfig](/artifact-registry/docs/reference/rest/v1/projects.locations/updateVpcscConfig)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateVPCSCConfig` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.operations](/artifact-registry/docs/reference/rest/v1/projects.locations.operations)









| 
Methods | 
|



| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.operations/get)` | 

`GET /v1/{name=projects/*/locations/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v1.projects.locations.repositories](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories)









| 
Methods | 
|



| 

`[create](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/create)` | 

`POST /v1/{parent=projects/*/locations/*}/repositories` 

Creates a repository. | 
|

| 

`[delete](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/repositories/*}` 

Deletes a repository and all of its contents. | 
|

| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/get)` | 

`GET /v1/{name=projects/*/locations/*/repositories/*}` 

Gets a repository. | 
|

| 

`[getIamPolicy](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/getIamPolicy)` | 

`GET /v1/{resource=projects/*/locations/*/repositories/*}:getIamPolicy` 

Gets the IAM policy for a given resource. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/list)` | 

`GET /v1/{parent=projects/*/locations/*}/repositories` 

Lists repositories. | 
|

| 

`[patch](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/patch)` | 

`PATCH /v1/{repository.name=projects/*/locations/*/repositories/*}` 

Updates a repository. | 
|

| 

`[setIamPolicy](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/setIamPolicy)` | 

`POST /v1/{resource=projects/*/locations/*/repositories/*}:setIamPolicy` 

Updates the IAM policy for a given resource. | 
|

| 

`[testIamPermissions](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/testIamPermissions)` | 

`POST /v1/{resource=projects/*/locations/*/repositories/*}:testIamPermissions` 

Tests if the caller has a list of permissions on a resource. | 
|

| 

`[exportArtifact](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/exportArtifact)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ExportArtifact` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.aptArtifacts](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.aptArtifacts)









| 
Methods | 
|



| 

`[import](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.aptArtifacts/import)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ImportAptArtifacts` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[upload](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.aptArtifacts/upload)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UploadAptArtifact` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.attachments](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.attachments)









| 
Methods | 
|



| 

`[create](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.attachments/create)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.CreateAttachment` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.attachments/delete)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.DeleteAttachment` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.attachments/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetAttachment` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.attachments/list)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ListAttachments` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.dockerImages](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.dockerImages)









| 
Methods | 
|



| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.dockerImages/get)` | 

`GET /v1/{name=projects/*/locations/*/repositories/*/dockerImages/*}` 

Gets a docker image. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.dockerImages/list)` | 

`GET /v1/{parent=projects/*/locations/*/repositories/*}/dockerImages` 

Lists docker images. | 
|






## REST Resource: [v1.projects.locations.repositories.files](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.files)









| 
Methods | 
|



| 

`[delete](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.files/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/repositories/*/files/*}` 

Deletes a file and all of its content. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.files/list)` | 

`GET /v1/{parent=projects/*/locations/*/repositories/*}/files` 

Lists files. | 
|

| 

`[patch](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.files/patch)` | 

`PATCH /v1/{file.name=projects/*/locations/*/repositories/*/files/*}` 

Updates a file. | 
|

| 

`[upload](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.files/upload)` | 

`POST /v1/{parent=projects/*/locations/*/repositories/*}/files:upload` 

`POST /upload/v1/{parent=projects/*/locations/*/repositories/*}/files:upload` 

Directly uploads a file to a repository. | 
|

| 

`[download](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.files/download)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.DownloadFile` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.files/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetFile` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.genericArtifacts](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.genericArtifacts)









| 
Methods | 
|



| 

`[upload](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.genericArtifacts/upload)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UploadGenericArtifact` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.goModules](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.goModules)









| 
Methods | 
|



| 

`[upload](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.goModules/upload)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UploadGoModule` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.googetArtifacts](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.googetArtifacts)









| 
Methods | 
|



| 

`[import](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.googetArtifacts/import)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ImportGoogetArtifacts` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[upload](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.googetArtifacts/upload)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UploadGoogetArtifact` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.kfpArtifacts](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.kfpArtifacts)









| 
Methods | 
|



| 

`[upload](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.kfpArtifacts/upload)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UploadKfpArtifact` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.mavenArtifacts](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts)









| 
Methods | 
|



| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetMavenArtifact` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts/list)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ListMavenArtifacts` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.npmPackages](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.npmPackages)









| 
Methods | 
|



| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.npmPackages/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetNpmPackage` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.npmPackages/list)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ListNpmPackages` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.packages](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages)









| 
Methods | 
|



| 

`[delete](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/repositories/*/packages/*}` 

Deletes a package and all of its versions and tags. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages/list)` | 

`GET /v1/{parent=projects/*/locations/*/repositories/*}/packages` 

Lists packages. | 
|

| 

`[patch](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages/patch)` | 

`PATCH /v1/{package.name=projects/*/locations/*/repositories/*/packages/*}` 

Updates a package. | 
|

| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetPackage` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.packages.tags](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.tags)









| 
Methods | 
|



| 

`[create](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.tags/create)` | 

`POST /v1/{parent=projects/*/locations/*/repositories/*/packages/*}/tags` 

Creates a tag. | 
|

| 

`[delete](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.tags/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/repositories/*/packages/*/tags/*}` 

Deletes a tag. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.tags/list)` | 

`GET /v1/{parent=projects/*/locations/*/repositories/*/packages/*}/tags` 

Lists tags. | 
|

| 

`[patch](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.tags/patch)` | 

`PATCH /v1/{tag.name=projects/*/locations/*/repositories/*/packages/*/tags/*}` 

Updates a tag. | 
|

| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.tags/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetTag` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.packages.versions](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.versions)









| 
Methods | 
|



| 

`[delete](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.versions/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/repositories/*/packages/*/versions/*}` 

Deletes a version and all of its content. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.versions/list)` | 

`GET /v1/{parent=projects/*/locations/*/repositories/*/packages/*}/versions` 

Lists versions. | 
|

| 

`[patch](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.versions/patch)` | 

`PATCH /v1/{version.name=projects/*/locations/*/repositories/*/packages/*/versions/*}` 

Updates a version. | 
|

| 

`[batchDelete](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.versions/batchDelete)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.BatchDeleteVersions` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.packages.versions/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetVersion` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.pythonPackages](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.pythonPackages)









| 
Methods | 
|



| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.pythonPackages/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetPythonPackage` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.pythonPackages/list)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ListPythonPackages` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.rules](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules)









| 
Methods | 
|



| 

`[create](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/create)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.CreateRule` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/delete)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.DeleteRule` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/get)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.GetRule` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/list)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ListRules` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/patch)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UpdateRule` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.repositories.yumArtifacts](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.yumArtifacts)









| 
Methods | 
|



| 

`[import](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.yumArtifacts/import)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.ImportYumArtifacts` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[upload](/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.yumArtifacts/upload)` | 

The method `google.devtools.artifactregistry.v1.ArtifactRegistry.UploadYumArtifact` is not available in Google Cloud Dedicated in Germany. | 
|