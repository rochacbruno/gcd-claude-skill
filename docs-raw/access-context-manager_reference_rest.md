# Access Context Manager API

Source: https://berlin.devsitetest.how/access-context-manager/docs/reference/rest
Last updated: 2026-04-21

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/access-context-manager/docs/tpc-differences) for more details.














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

Access Context Manager

](https://berlin.devsitetest.how/access-context-manager/docs)






- 








[

Reference

](https://berlin.devsitetest.how/access-context-manager/docs/apis)












# Access Context Manager API 






- On this page 
- [ Service: accesscontextmanager.googleapis.com ](#service:-accesscontextmanager.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)

- [ REST Resource: v1.accessPolicies ](#rest-resource:-v1.accesspolicies)
- [ REST Resource: v1.accessPolicies.accessLevels ](#rest-resource:-v1.accesspolicies.accesslevels)
- [ REST Resource: v1.accessPolicies.authorizedOrgsDescs ](#rest-resource:-v1.accesspolicies.authorizedorgsdescs)
- [ REST Resource: v1.accessPolicies.servicePerimeters ](#rest-resource:-v1.accesspolicies.serviceperimeters)
- [ REST Resource: v1.operations ](#rest-resource:-v1.operations)
- [ REST Resource: v1.organizations.gcpUserAccessBindings ](#rest-resource:-v1.organizations.gcpuseraccessbindings)
- [ REST Resource: v1.permissions ](#rest-resource:-v1.permissions)
- [ REST Resource: v1.services ](#rest-resource:-v1.services)
- 













An API for setting attribute based access control to requests to Google Cloud Dedicated services. 




- [REST Resource: v1.accessPolicies](#v1.accessPolicies)

- [REST Resource: v1.accessPolicies.accessLevels](#v1.accessPolicies.accessLevels)

- [REST Resource: v1.accessPolicies.authorizedOrgsDescs](#v1.accessPolicies.authorizedOrgsDescs)

- [REST Resource: v1.accessPolicies.servicePerimeters](#v1.accessPolicies.servicePerimeters)

- [REST Resource: v1.operations](#v1.operations)

- [REST Resource: v1.organizations.gcpUserAccessBindings](#v1.organizations.gcpUserAccessBindings)

- [REST Resource: v1.permissions](#v1.permissions)

- [REST Resource: v1.services](#v1.services)





## Service: accesscontextmanager. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://accesscontextmanager.apis-berlin-build0.goog/$discovery/rest?version=v1](https://accesscontextmanager.apis-berlin-build0.goog/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://accesscontextmanager.apis-berlin-build0.goog`






## REST Resource: [v1. access Policies](/access-context-manager/docs/reference/rest/v1/accessPolicies)









| 
Methods | 
|



| 

`[create](/access-context-manager/docs/reference/rest/v1/accessPolicies/create)` | 

`POST / v1/ access Policies` 

Creates an access policy. | 
|

| 

`[delete](/access-context-manager/docs/reference/rest/v1/accessPolicies/delete)` | 

`DELETE /v1/{name=accessPolicies/*}` 

Deletes an `[access policy](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)` based on the resource name. | 
|

| 

`[get](/access-context-manager/docs/reference/rest/v1/accessPolicies/get)` | 

`GET /v1/{name=accessPolicies/*}` 

Returns an `[access policy](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)` based on the name. | 
|

| 

`[getIamPolicy](/access-context-manager/docs/reference/rest/v1/accessPolicies/getIamPolicy)` | 

`POST /v1/{resource=accessPolicies/*}:getIamPolicy` 

Gets the IAM policy for the specified Access Context Manager `[access policy](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)`. | 
|

| 

`[list](/access-context-manager/docs/reference/rest/v1/accessPolicies/list)` | 

`GET /v1/accessPolicies` 

Lists all `[access policies](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)` in an organization. | 
|

| 

`[patch](/access-context-manager/docs/reference/rest/v1/accessPolicies/patch)` | 

`PATCH /v1/{policy.name=accessPolicies/*}` 

Updates an `[access policy](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)`. | 
|

| 

`[setIamPolicy](/access-context-manager/docs/reference/rest/v1/accessPolicies/setIamPolicy)` | 

`POST /v1/{resource=accessPolicies/*}:setIamPolicy` 

Sets the IAM policy for the specified Access Context Manager `[access policy](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)`. | 
|

| 

`[testIamPermissions](/access-context-manager/docs/reference/rest/v1/accessPolicies/testIamPermissions)` | 

`POST /v1/{resource=accessPolicies/*}:testIamPermissions` 

Returns the IAM permissions that the caller has on the specified Access Context Manager resource. | 
|






## REST Resource: [v1.accessPolicies.accessLevels](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)









| 
Methods | 
|



| 

`[create](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create)` | 

`POST /v1/{parent=accessPolicies/*}/accessLevels` 

Creates an `[access level](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)`. | 
|

| 

`[delete](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/delete)` | 

`DELETE /v1/{name=accessPolicies/*/accessLevels/*}` 

Deletes an `[access level](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` based on the resource name. | 
|

| 

`[get](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/get)` | 

`GET /v1/{name=accessPolicies/*/accessLevels/*}` 

Gets an `[access level](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` based on the resource name. | 
|

| 

`[list](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/list)` | 

`GET /v1/{parent=accessPolicies/*}/accessLevels` 

Lists all `[access levels](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` for an access policy. | 
|

| 

`[patch](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/patch)` | 

`PATCH /v1/{accessLevel.name=accessPolicies/*/accessLevels/*}` 

Updates an `[access level](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)`. | 
|

| 

`[replaceAll](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/replaceAll)` | 

`POST /v1/{parent=accessPolicies/*}/accessLevels:replaceAll` 

Replaces all existing `[access levels](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` in an `[access policy](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)` with the `[access levels](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)` provided. | 
|

| 

`[testIamPermissions](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/testIamPermissions)` | 

`POST /v1/{resource=accessPolicies/*/accessLevels/*}:testIamPermissions` 

Returns the IAM permissions that the caller has on the specified Access Context Manager resource. | 
|






## REST Resource: [v1.accessPolicies.authorizedOrgsDescs](/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs)









| 
Methods | 
|



| 

`[create](/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs/create)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.CreateAuthorizedOrgsDesc` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs/delete)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAuthorizedOrgsDesc` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs/get)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.GetAuthorizedOrgsDesc` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs/list)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.ListAuthorizedOrgsDescs` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs/patch)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAuthorizedOrgsDesc` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.accessPolicies.servicePerimeters](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)









| 
Methods | 
|



| 

`[commit](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/commit)` | 

`POST /v1/{parent=accessPolicies/*}/servicePerimeters:commit` 

Commits the dry-run specification for all the `[service perimeters](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` in an `[access policy](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)`. | 
|

| 

`[create](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/create)` | 

`POST /v1/{parent=accessPolicies/*}/servicePerimeters` 

Creates a `[service perimeter](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`. | 
|

| 

`[delete](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/delete)` | 

`DELETE /v1/{name=accessPolicies/*/servicePerimeters/*}` 

Deletes a `[service perimeter](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` based on the resource name. | 
|

| 

`[get](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/get)` | 

`GET /v1/{name=accessPolicies/*/servicePerimeters/*}` 

Gets a `[service perimeter](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` based on the resource name. | 
|

| 

`[list](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/list)` | 

`GET /v1/{parent=accessPolicies/*}/servicePerimeters` 

Lists all `[service perimeters](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` for an access policy. | 
|

| 

`[patch](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/patch)` | 

`PATCH /v1/{servicePerimeter.name=accessPolicies/*/servicePerimeters/*}` 

Updates a `[service perimeter](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)`. | 
|

| 

`[replaceAll](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/replaceAll)` | 

`POST /v1/{parent=accessPolicies/*}/servicePerimeters:replaceAll` 

Replace all existing `[service perimeters](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` in an `[access policy](/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy)` with the `[service perimeters](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter)` provided. | 
|

| 

`[testIamPermissions](/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/testIamPermissions)` | 

`POST /v1/{resource=accessPolicies/*/servicePerimeters/*}:testIamPermissions` 

Returns the IAM permissions that the caller has on the specified Access Context Manager resource. | 
|






## REST Resource: [v1.operations](/access-context-manager/docs/reference/rest/v1/operations)









| 
Methods | 
|



| 

`[cancel](/access-context-manager/docs/reference/rest/v1/operations/cancel)` | 

`POST /v1/{name=operations/**}:cancel` 

Starts asynchronous cancellation on a long-running operation. | 
|

| 

`[delete](/access-context-manager/docs/reference/rest/v1/operations/delete)` | 

`DELETE /v1/{name=operations/**}` 

Deletes a long-running operation. | 
|

| 

`[get](/access-context-manager/docs/reference/rest/v1/operations/get)` | 

`GET /v1/{name=operations/**}` 

Gets the latest state of a long-running operation. | 
|

| 

`[list](/access-context-manager/docs/reference/rest/v1/operations/list)` | 

`GET /v1/{name=operations}` 

Lists operations that match the specified filter in the request. | 
|






## REST Resource: [v1.organizations.gcpUserAccessBindings](/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings)









| 
Methods | 
|



| 

`[create](/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings/create)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.CreateGcpUserAccessBinding` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings/delete)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.DeleteGcpUserAccessBinding` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings/get)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.GetGcpUserAccessBinding` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings/list)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.ListGcpUserAccessBindings` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings/patch)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.UpdateGcpUserAccessBinding` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.permissions](/access-context-manager/docs/reference/rest/v1/permissions)









| 
Methods | 
|



| 

`[list](/access-context-manager/docs/reference/rest/v1/permissions/list)` | 

The method `google.identity.accesscontextmanager.v1.AccessContextManager.ListSupportedPermissions` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.services](/access-context-manager/docs/reference/rest/v1/services)









| 
Methods | 
|



| 

`[get](/access-context-manager/docs/reference/rest/v1/services/get)` | 

`GET /v1/services/{name}` 

Returns a `[VPC-SC supported service](/access-context-manager/docs/reference/rest/v1/services#SupportedService)` based on the service name. | 
|

| 

`[list](/access-context-manager/docs/reference/rest/v1/services/list)` | 

`GET /v1/services` 

Lists all `[VPC-SC supported services](/access-context-manager/docs/reference/rest/v1/services#SupportedService)`. | 
|