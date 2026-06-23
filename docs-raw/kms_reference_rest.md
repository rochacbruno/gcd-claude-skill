# Cloud Key Management Service (KMS) API

Source: https://berlin.devsitetest.how/kms/docs/reference/rest
Last updated: 2025-09-25

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/kms/docs/tpc-differences) for more details.














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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

Cloud KMS

](https://berlin.devsitetest.how/kms/docs)






- 








[

Reference

](https://berlin.devsitetest.how/kms/docs/apis)












# Cloud Key Management Service (KMS) API 






- On this page 
- [ Service: cloudkms.googleapis.com ](#service:-cloudkms.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)
- [ Regional service endpoint ](#regional-service-endpoint)

- [ REST Resource: v1.folders ](#rest-resource:-v1.folders)
- [ REST Resource: v1.organizations ](#rest-resource:-v1.organizations)
- [ REST Resource: v1.projects ](#rest-resource:-v1.projects)
- [ REST Resource: v1.projects.locations ](#rest-resource:-v1.projects.locations)
- [ REST Resource: v1.projects.locations.ekmConfig ](#rest-resource:-v1.projects.locations.ekmconfig)
- [ REST Resource: v1.projects.locations.ekmConnections ](#rest-resource:-v1.projects.locations.ekmconnections)
- [ REST Resource: v1.projects.locations.keyHandles ](#rest-resource:-v1.projects.locations.keyhandles)
- [ REST Resource: v1.projects.locations.keyRings ](#rest-resource:-v1.projects.locations.keyrings)
- [ REST Resource: v1.projects.locations.keyRings.cryptoKeys ](#rest-resource:-v1.projects.locations.keyrings.cryptokeys)
- [ REST Resource: v1.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions ](#rest-resource:-v1.projects.locations.keyrings.cryptokeys.cryptokeyversions)
- [ REST Resource: v1.projects.locations.keyRings.importJobs ](#rest-resource:-v1.projects.locations.keyrings.importjobs)
- [ REST Resource: v1.projects.locations.operations ](#rest-resource:-v1.projects.locations.operations)
- 













Manages keys and performs cryptographic operations in a central cloud service, for direct use by other cloud resources and applications.




- [REST Resource: v1.folders](#v1.folders)

- [REST Resource: v1.organizations](#v1.organizations)

- [REST Resource: v1.projects](#v1.projects)

- [REST Resource: v1.projects.locations](#v1.projects.locations)

- [REST Resource: v1.projects.locations.ekmConfig](#v1.projects.locations.ekmConfig)

- [REST Resource: v1.projects.locations.ekmConnections](#v1.projects.locations.ekmConnections)

- [REST Resource: v1.projects.locations.keyHandles](#v1.projects.locations.keyHandles)

- [REST Resource: v1.projects.locations.keyRings](#v1.projects.locations.keyRings)

- [REST Resource: v1.projects.locations.keyRings.cryptoKeys](#v1.projects.locations.keyRings.cryptoKeys)

- [REST Resource: v1.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions](#v1.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions)

- [REST Resource: v1.projects.locations.keyRings.importJobs](#v1.projects.locations.keyRings.importJobs)

- [REST Resource: v1.projects.locations.operations](#v1.projects.locations.operations)





## Service: cloudkms. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://cloudkms.apis-berlin-build0.goog/$discovery/rest?version=v1](https://cloudkms.apis-berlin-build0.goog/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://cloudkms.apis-berlin-build0.goog`





### Regional service endpoint



A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 
global 






## REST Resource: [v1. folders](/kms/docs/reference/rest/v1/folders)









| 
Methods | 
|



| 

`[get Autokey Config](/kms/docs/reference/rest/v1/folders/getAutokeyConfig)` | 

The method `google. cloud. kms. v1. Autokey Admin. Get Autokey Config` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[getKajPolicyConfig](/kms/docs/reference/rest/v1/folders/getKajPolicyConfig)` | 

The method `google.cloud.kms.v1.KeyAccessJustificationsConfig.GetKeyAccessJustificationsPolicyConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateAutokeyConfig](/kms/docs/reference/rest/v1/folders/updateAutokeyConfig)` | 

The method `google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateKajPolicyConfig](/kms/docs/reference/rest/v1/folders/updateKajPolicyConfig)` | 

The method `google.cloud.kms.v1.KeyAccessJustificationsConfig.UpdateKeyAccessJustificationsPolicyConfig` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.organizations](/kms/docs/reference/rest/v1/organizations)









| 
Methods | 
|



| 

`[getKajPolicyConfig](/kms/docs/reference/rest/v1/organizations/getKajPolicyConfig)` | 

The method `google.cloud.kms.v1.KeyAccessJustificationsConfig.GetKeyAccessJustificationsPolicyConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateKajPolicyConfig](/kms/docs/reference/rest/v1/organizations/updateKajPolicyConfig)` | 

The method `google.cloud.kms.v1.KeyAccessJustificationsConfig.UpdateKeyAccessJustificationsPolicyConfig` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects](/kms/docs/reference/rest/v1/projects)









| 
Methods | 
|



| 

`[getAutokeyConfig](/kms/docs/reference/rest/v1/projects/getAutokeyConfig)` | 

The method `google.cloud.kms.v1.AutokeyAdmin.GetAutokeyConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[getKajPolicyConfig](/kms/docs/reference/rest/v1/projects/getKajPolicyConfig)` | 

The method `google.cloud.kms.v1.KeyAccessJustificationsConfig.GetKeyAccessJustificationsPolicyConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[showEffectiveAutokeyConfig](/kms/docs/reference/rest/v1/projects/showEffectiveAutokeyConfig)` | 

The method `google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[showEffectiveKeyAccessJustificationsEnrollmentConfig](/kms/docs/reference/rest/v1/projects/showEffectiveKeyAccessJustificationsEnrollmentConfig)` | 

The method `google.cloud.kms.v1.KeyAccessJustificationsConfig.ShowEffectiveKeyAccessJustificationsEnrollmentConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[showEffectiveKeyAccessJustificationsPolicyConfig](/kms/docs/reference/rest/v1/projects/showEffectiveKeyAccessJustificationsPolicyConfig)` | 

The method `google.cloud.kms.v1.KeyAccessJustificationsConfig.ShowEffectiveKeyAccessJustificationsPolicyConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateAutokeyConfig](/kms/docs/reference/rest/v1/projects/updateAutokeyConfig)` | 

The method `google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[updateKajPolicyConfig](/kms/docs/reference/rest/v1/projects/updateKajPolicyConfig)` | 

The method `google.cloud.kms.v1.KeyAccessJustificationsConfig.UpdateKeyAccessJustificationsPolicyConfig` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations](/kms/docs/reference/rest/v1/projects.locations)









| 
Methods | 
|



| 

`[generateRandomBytes](/kms/docs/reference/rest/v1/projects.locations/generateRandomBytes)` | 

`POST /v1/{location=projects/*/locations/*}:generateRandomBytes` 

Generate random bytes using the Cloud KMS randomness source in the provided location. | 
|

| 

`[getEkmConfig](/kms/docs/reference/rest/v1/projects.locations/getEkmConfig)` | 

`GET /v1/{name=projects/*/locations/*/ekmConfig}` 

Returns the `[EkmConfig](/kms/docs/reference/rest/v1/EkmConfig)` singleton resource for a given project and location. | 
|

| 

`[updateEkmConfig](/kms/docs/reference/rest/v1/projects.locations/updateEkmConfig)` | 

`PATCH /v1/{ekmConfig.name=projects/*/locations/*/ekmConfig}` 

Updates the `[EkmConfig](/kms/docs/reference/rest/v1/EkmConfig)` singleton resource for a given project and location. | 
|

| 

`[get](/kms/docs/reference/rest/v1/projects.locations/get)` | 

The method `google.cloud.location.Locations.GetLocation` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/kms/docs/reference/rest/v1/projects.locations/list)` | 

The method `google.cloud.location.Locations.ListLocations` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.ekmConfig](/kms/docs/reference/rest/v1/projects.locations.ekmConfig)









| 
Methods | 
|



| 

`[getIamPolicy](/kms/docs/reference/rest/v1/projects.locations.ekmConfig/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/kms/docs/reference/rest/v1/projects.locations.ekmConfig/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/kms/docs/reference/rest/v1/projects.locations.ekmConfig/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.ekmConnections](/kms/docs/reference/rest/v1/projects.locations.ekmConnections)









| 
Methods | 
|



| 

`[create](/kms/docs/reference/rest/v1/projects.locations.ekmConnections/create)` | 

`POST /v1/{parent=projects/*/locations/*}/ekmConnections` 

Only EXTERNAL_VPC connections are supported.
Creates a new `[EkmConnection](/kms/docs/reference/rest/v1/projects.locations.ekmConnections#EkmConnection)` in a given Project and Location. | 
|

| 

`[get](/kms/docs/reference/rest/v1/projects.locations.ekmConnections/get)` | 

`GET /v1/{name=projects/*/locations/*/ekmConnections/*}` 

Only EXTERNAL_VPC connections are supported.
Returns metadata for a given `[EkmConnection](/kms/docs/reference/rest/v1/projects.locations.ekmConnections#EkmConnection)`. | 
|

| 

`[list](/kms/docs/reference/rest/v1/projects.locations.ekmConnections/list)` | 

`GET /v1/{parent=projects/*/locations/*}/ekmConnections` 

Only EXTERNAL_VPC connections are supported.
Lists `[EkmConnections](/kms/docs/reference/rest/v1/projects.locations.ekmConnections#EkmConnection)`. | 
|

| 

`[patch](/kms/docs/reference/rest/v1/projects.locations.ekmConnections/patch)` | 

`PATCH /v1/{ekmConnection.name=projects/*/locations/*/ekmConnections/*}` 

Only EXTERNAL_VPC connections are supported.
Updates an `[EkmConnection](/kms/docs/reference/rest/v1/projects.locations.ekmConnections#EkmConnection)`'s metadata. | 
|

| 

`[verifyConnectivity](/kms/docs/reference/rest/v1/projects.locations.ekmConnections/verifyConnectivity)` | 

`GET /v1/{name=projects/*/locations/*/ekmConnections/*}:verifyConnectivity` 

Only EXTERNAL_VPC connections are supported.
Verifies that Cloud KMS can successfully connect to the external key manager specified by an `[EkmConnection](/kms/docs/reference/rest/v1/projects.locations.ekmConnections#EkmConnection)`. | 
|

| 

`[getIamPolicy](/kms/docs/reference/rest/v1/projects.locations.ekmConnections/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/kms/docs/reference/rest/v1/projects.locations.ekmConnections/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/kms/docs/reference/rest/v1/projects.locations.ekmConnections/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.keyHandles](/kms/docs/reference/rest/v1/projects.locations.keyHandles)









| 
Methods | 
|



| 

`[create](/kms/docs/reference/rest/v1/projects.locations.keyHandles/create)` | 

The method `google.cloud.kms.v1.Autokey.CreateKeyHandle` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/kms/docs/reference/rest/v1/projects.locations.keyHandles/get)` | 

The method `google.cloud.kms.v1.Autokey.GetKeyHandle` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/kms/docs/reference/rest/v1/projects.locations.keyHandles/list)` | 

The method `google.cloud.kms.v1.Autokey.ListKeyHandles` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.keyRings](/kms/docs/reference/rest/v1/projects.locations.keyRings)









| 
Methods | 
|



| 

`[create](/kms/docs/reference/rest/v1/projects.locations.keyRings/create)` | 

`POST /v1/{parent=projects/*/locations/*}/keyRings` 

Create a new `[KeyRing](/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing)` in a given Project and Location. | 
|

| 

`[get](/kms/docs/reference/rest/v1/projects.locations.keyRings/get)` | 

`GET /v1/{name=projects/*/locations/*/keyRings/*}` 

Returns metadata for a given `[KeyRing](/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing)`. | 
|

| 

`[list](/kms/docs/reference/rest/v1/projects.locations.keyRings/list)` | 

`GET /v1/{parent=projects/*/locations/*}/keyRings` 

Lists `[KeyRings](/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing)`. | 
|

| 

`[getIamPolicy](/kms/docs/reference/rest/v1/projects.locations.keyRings/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/kms/docs/reference/rest/v1/projects.locations.keyRings/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/kms/docs/reference/rest/v1/projects.locations.keyRings/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.keyRings.cryptoKeys](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys)









| 
Methods | 
|



| 

`[create](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create)` | 

`POST /v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` 

Create a new `[CryptoKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)` within a `[KeyRing](/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing)`. | 
|

| 

`[decrypt](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` 

Decrypts data that was protected by `[Encrypt](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt#google.cloud.kms.v1.KeyManagementService.Encrypt)`. | 
|

| 

`[encrypt](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` 

Encrypts data, so that it can only be recovered by a call to `[Decrypt](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt#google.cloud.kms.v1.KeyManagementService.Decrypt)`. | 
|

| 

`[get](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/get)` | 

`GET /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}` 

Returns metadata for a given `[CryptoKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)`, as well as its `[primary](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.primary)` `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)`. | 
|

| 

`[list](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list)` | 

`GET /v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` 

Lists `[CryptoKeys](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)`. | 
|

| 

`[patch](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/patch)` | 

`PATCH /v1/{cryptoKey.name=projects/*/locations/*/keyRings/*/cryptoKeys/*}` 

Update a `[CryptoKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)`. | 
|

| 

`[updatePrimaryVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/updatePrimaryVersion)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:updatePrimaryVersion` 

Update the version of a `[CryptoKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)` that will be used in `[Encrypt](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt#google.cloud.kms.v1.KeyManagementService.Encrypt)`. | 
|

| 

`[getIamPolicy](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions)









| 
Methods | 
|



| 

`[asymmetricDecrypt](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` 

Decrypts data that was encrypted with a public key retrieved from `[GetPublicKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey#google.cloud.kms.v1.KeyManagementService.GetPublicKey)` corresponding to a `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` with `[CryptoKey.purpose](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.purpose)` ASYMMETRIC_DECRYPT. | 
|

| 

`[asymmetricSign](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` 

Signs data using a `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` with `[CryptoKey.purpose](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.purpose)` ASYMMETRIC_SIGN, producing a signature that can be verified with the public key retrieved from `[GetPublicKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey#google.cloud.kms.v1.KeyManagementService.GetPublicKey)`. | 
|

| 

`[create](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/create)` | 

`POST /v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` 

Create a new `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` in a `[CryptoKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)`. | 
|

| 

`[destroy](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/destroy)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:destroy` 

Schedule a `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` for destruction. | 
|

| 

`[get](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/get)` | 

`GET /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}` 

Returns metadata for a given `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)`. | 
|

| 

`[getPublicKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey)` | 

`GET /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` 

Returns the public key for the given `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)`. | 
|

| 

`[import](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import)` | 

`POST /v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions:import` 

Import wrapped key material into a `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)`. | 
|

| 

`[list](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list)` | 

`GET /v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` 

Lists `[CryptoKeyVersions](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)`. | 
|

| 

`[macSign](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macSign)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` 

Signs data using a `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` with `[CryptoKey.purpose](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.purpose)` MAC, producing a tag that can be verified by another source with the same key. | 
|

| 

`[macVerify](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macVerify)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` 

Verifies MAC tag using a `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` with `[CryptoKey.purpose](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.purpose)` MAC, and returns a response that indicates whether or not the verification was successful. | 
|

| 

`[patch](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/patch)` | 

`PATCH /v1/{cryptoKeyVersion.name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}` 

Update a `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)`'s metadata. | 
|

| 

`[rawDecrypt](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawDecrypt)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` 

Decrypts data that was originally encrypted using a raw cryptographic mechanism. | 
|

| 

`[rawEncrypt](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawEncrypt)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` 

Encrypts data using portable cryptographic primitives. | 
|

| 

`[restore](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/restore)` | 

`POST /v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:restore` 

Restore a `[CryptoKeyVersion](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` in the `[DESTROY_SCHEDULED](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.DESTROY_SCHEDULED)` state. | 
|

| 

`[decapsulate](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/decapsulate)` | 

The method `google.cloud.kms.v1.KeyManagementService.Decapsulate` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.keyRings.importJobs](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs)









| 
Methods | 
|



| 

`[create](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create)` | 

`POST /v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` 

Create a new `[ImportJob](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob)` within a `[KeyRing](/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing)`. | 
|

| 

`[get](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get)` | 

`GET /v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` 

Returns metadata for a given `[ImportJob](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob)`. | 
|

| 

`[list](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/list)` | 

`GET /v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` 

Lists `[ImportJobs](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob)`. | 
|

| 

`[getIamPolicy](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/getIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/setIamPolicy)` | 

The method `google.iam.v1.IAMPolicy.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/testIamPermissions)` | 

The method `google.iam.v1.IAMPolicy.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.operations](/kms/docs/reference/rest/v1/projects.locations.operations)









| 
Methods | 
|



| 

`[get](/kms/docs/reference/rest/v1/projects.locations.operations/get)` | 

The method `google.longrunning.Operations.GetOperation` is not available in Google Cloud Dedicated in Germany. | 
|