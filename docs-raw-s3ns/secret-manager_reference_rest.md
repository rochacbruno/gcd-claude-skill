# Secret Manager API

Source: https://documentation.s3ns.fr/secret-manager/docs/reference/rest
Last updated: 2025-11-04

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/secret-manager/docs/tpc-differences) for more details.














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

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Secret Manager

](https://documentation.s3ns.fr/secret-manager/docs)






- 








[

Reference

](https://documentation.s3ns.fr/secret-manager/docs/apis)












# Secret Manager API 


















Stores sensitive data such as API keys, passwords, and certificates. Provides convenience while improving security.




- [REST Resource: v1.projects.locations](#v1.projects.locations)

- [REST Resource: v1.projects.locations.secrets](#v1.projects.locations.secrets)

- [REST Resource: v1.projects.locations.secrets.versions](#v1.projects.locations.secrets.versions)

- [REST Resource: v1.projects.secrets](#v1.projects.secrets)

- [REST Resource: v1.projects.secrets.versions](#v1.projects.secrets.versions)





## Service: secretmanager.googleapis.com



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://secretmanager.googleapis.com/$discovery/rest?version=v1](https://secretmanager.googleapis.com/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://secretmanager.googleapis.com`





### Regional service endpoint



A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 






## REST Resource: [v1.projects.locations](/secret-manager/docs/reference/rest/v1/projects.locations)









| 
Methods | 
|



| 

`[get](/secret-manager/docs/reference/rest/v1/projects.locations/get)` | 

The method `google.cloud.location.Locations.GetLocation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.locations/list)` | 

The method `google.cloud.location.Locations.ListLocations` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.projects.locations.secrets](/secret-manager/docs/reference/rest/v1/projects.locations.secrets)









| 
Methods | 
|



| 

`[addVersion](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/addVersion)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.AddSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[create](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/create)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.CreateSecret` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/delete)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.DeleteSecret` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/get)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.GetSecret` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/getIamPolicy)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.GetIamPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/list)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.ListSecrets` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/patch)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.UpdateSecret` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/setIamPolicy)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.SetIamPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/secret-manager/docs/reference/rest/v1/projects.locations.secrets/testIamPermissions)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.TestIamPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.projects.locations.secrets.versions](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions)









| 
Methods | 
|



| 

`[access](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/access)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.AccessSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[destroy](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/destroy)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.DestroySecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[disable](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/disable)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.DisableSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[enable](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/enable)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.EnableSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/get)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.GetSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions/list)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.ListSecretVersions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.projects.secrets](/secret-manager/docs/reference/rest/v1/projects.secrets)









| 
Methods | 
|



| 

`[addVersion](/secret-manager/docs/reference/rest/v1/projects.secrets/addVersion)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.AddSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[create](/secret-manager/docs/reference/rest/v1/projects.secrets/create)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.CreateSecret` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/secret-manager/docs/reference/rest/v1/projects.secrets/delete)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.DeleteSecret` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/secret-manager/docs/reference/rest/v1/projects.secrets/get)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.GetSecret` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/secret-manager/docs/reference/rest/v1/projects.secrets/getIamPolicy)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.GetIamPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.secrets/list)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.ListSecrets` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/secret-manager/docs/reference/rest/v1/projects.secrets/patch)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.UpdateSecret` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/secret-manager/docs/reference/rest/v1/projects.secrets/setIamPolicy)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.SetIamPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/secret-manager/docs/reference/rest/v1/projects.secrets/testIamPermissions)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.TestIamPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.projects.secrets.versions](/secret-manager/docs/reference/rest/v1/projects.secrets.versions)









| 
Methods | 
|



| 

`[access](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/access)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.AccessSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[destroy](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/destroy)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.DestroySecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[disable](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/disable)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.DisableSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[enable](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/enable)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.EnableSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/get)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.GetSecretVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/secret-manager/docs/reference/rest/v1/projects.secrets.versions/list)` | 

The method `google.cloud.secretmanager.v1.SecretManagerService.ListSecretVersions` is not available in Cloud de Confiance by S3NS. | 
|