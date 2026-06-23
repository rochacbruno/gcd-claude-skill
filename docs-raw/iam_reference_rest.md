# Identity and Access Management (IAM) API

Source: https://berlin.devsitetest.how/iam/docs/reference/rest
Last updated: 2026-01-15

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

IAM

](https://berlin.devsitetest.how/iam/docs)






- 








[

Reference

](https://berlin.devsitetest.how/iam/docs/apis)












# Identity and Access Management (IAM) API 






- On this page ** 
- [ Service: iam.googleapis.com ](#service:-iam.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)

- [ REST Resource: v2beta.policies ](#rest-resource:-v2beta.policies)
- [ REST Resource: v2beta.policies.operations ](#rest-resource:-v2beta.policies.operations)
- [ REST Resource: v2.policies ](#rest-resource:-v2.policies)
- [ REST Resource: v2.policies.operations ](#rest-resource:-v2.policies.operations)
- [ REST Resource: v1beta.projects.locations.workloadIdentityPools ](#rest-resource:-v1beta.projects.locations.workloadidentitypools)
- [ REST Resource: v1beta.projects.locations.workloadIdentityPools.operations ](#rest-resource:-v1beta.projects.locations.workloadidentitypools.operations)
- [ REST Resource: v1beta.projects.locations.workloadIdentityPools.providers ](#rest-resource:-v1beta.projects.locations.workloadidentitypools.providers)
- [ REST Resource: v1beta.projects.locations.workloadIdentityPools.providers.operations ](#rest-resource:-v1beta.projects.locations.workloadidentitypools.providers.operations)
- [ REST Resource: v1.iamPolicies ](#rest-resource:-v1.iampolicies)
- [ REST Resource: v1.locations.workforcePools ](#rest-resource:-v1.locations.workforcepools)
- [ REST Resource: v1.locations.workforcePools.operations ](#rest-resource:-v1.locations.workforcepools.operations)
- [ REST Resource: v1.locations.workforcePools.providers ](#rest-resource:-v1.locations.workforcepools.providers)
- [ REST Resource: v1.locations.workforcePools.providers.keys ](#rest-resource:-v1.locations.workforcepools.providers.keys)
- [ REST Resource: v1.locations.workforcePools.providers.operations ](#rest-resource:-v1.locations.workforcepools.providers.operations)
- [ REST Resource: v1.locations.workforcePools.providers.scimTenants ](#rest-resource:-v1.locations.workforcepools.providers.scimtenants)
- [ REST Resource: v1.locations.workforcePools.providers.scimTenants.tokens ](#rest-resource:-v1.locations.workforcepools.providers.scimtenants.tokens)
- [ REST Resource: v1.locations.workforcePools.subjects ](#rest-resource:-v1.locations.workforcepools.subjects)
- [ REST Resource: v1.organizations.roles ](#rest-resource:-v1.organizations.roles)
- [ REST Resource: v1.permissions ](#rest-resource:-v1.permissions)
- [ REST Resource: v1.projects.locations.oauthClients ](#rest-resource:-v1.projects.locations.oauthclients)
- [ REST Resource: v1.projects.locations.oauthClients.credentials ](#rest-resource:-v1.projects.locations.oauthclients.credentials)
- [ REST Resource: v1.projects.locations.workloadIdentityPools ](#rest-resource:-v1.projects.locations.workloadidentitypools)
- [ REST Resource: v1.projects.locations.workloadIdentityPools.namespaces ](#rest-resource:-v1.projects.locations.workloadidentitypools.namespaces)
- [ REST Resource: v1.projects.locations.workloadIdentityPools.namespaces.managedIdentities ](#rest-resource:-v1.projects.locations.workloadidentitypools.namespaces.managedidentities)
- [ REST Resource: v1.projects.locations.workloadIdentityPools.operations ](#rest-resource:-v1.projects.locations.workloadidentitypools.operations)
- [ REST Resource: v1.projects.locations.workloadIdentityPools.providers ](#rest-resource:-v1.projects.locations.workloadidentitypools.providers)
- [ REST Resource: v1.projects.locations.workloadIdentityPools.providers.keys ](#rest-resource:-v1.projects.locations.workloadidentitypools.providers.keys)
- [ REST Resource: v1.projects.locations.workloadIdentityPools.providers.operations ](#rest-resource:-v1.projects.locations.workloadidentitypools.providers.operations)
- [ REST Resource: v1.projects.roles ](#rest-resource:-v1.projects.roles)
- [ REST Resource: v1.projects.serviceAccounts ](#rest-resource:-v1.projects.serviceaccounts)
- [ REST Resource: v1.projects.serviceAccounts.keys ](#rest-resource:-v1.projects.serviceaccounts.keys)
- [ REST Resource: v1.roles ](#rest-resource:-v1.roles)
- 













Manages identity and access control for Sovereign Cloud Platform resources, including the creation of service accounts, which you can use to authenticate to Sovereign Cloud and make API calls.




- [REST Resource: v2beta.policies](#v2beta.policies)

- [REST Resource: v2beta.policies.operations](#v2beta.policies.operations)

- [REST Resource: v2.policies](#v2.policies)

- [REST Resource: v2.policies.operations](#v2.policies.operations)

- [REST Resource: v1beta.projects.locations.workloadIdentityPools](#v1beta.projects.locations.workloadIdentityPools)

- [REST Resource: v1beta.projects.locations.workloadIdentityPools.operations](#v1beta.projects.locations.workloadIdentityPools.operations)

- [REST Resource: v1beta.projects.locations.workloadIdentityPools.providers](#v1beta.projects.locations.workloadIdentityPools.providers)

- [REST Resource: 
v1beta.projects.locations.workloadIdentityPools.providers.operations](#v1beta.projects.locations.workloadIdentityPools.providers.operations)

- [REST Resource: v1.iamPolicies](#v1.iamPolicies)

- [REST Resource: v1.locations.workforcePools](#v1.locations.workforcePools)

- [REST Resource: v1.locations.workforcePools.operations](#v1.locations.workforcePools.operations)

- [REST Resource: v1.locations.workforcePools.providers](#v1.locations.workforcePools.providers)

- [REST Resource: v1.locations.workforcePools.providers.keys](#v1.locations.workforcePools.providers.keys)

- [REST Resource: v1.locations.workforcePools.providers.operations](#v1.locations.workforcePools.providers.operations)

- [REST Resource: v1.locations.workforcePools.providers.scimTenants](#v1.locations.workforcePools.providers.scimTenants)

- [REST Resource: v1.locations.workforcePools.providers.scimTenants.tokens](#v1.locations.workforcePools.providers.scimTenants.tokens)

- [REST Resource: v1.locations.workforcePools.subjects](#v1.locations.workforcePools.subjects)

- [REST Resource: v1.organizations.roles](#v1.organizations.roles)

- [REST Resource: v1.permissions](#v1.permissions)

- [REST Resource: v1.projects.locations.oauthClients](#v1.projects.locations.oauthClients)

- [REST Resource: v1.projects.locations.oauthClients.credentials](#v1.projects.locations.oauthClients.credentials)

- [REST Resource: v1.projects.locations.workloadIdentityPools](#v1.projects.locations.workloadIdentityPools)

- [REST Resource: v1.projects.locations.workloadIdentityPools.namespaces](#v1.projects.locations.workloadIdentityPools.namespaces)

- [REST Resource: 
v1.projects.locations.workloadIdentityPools.namespaces.managedIdentities](#v1.projects.locations.workloadIdentityPools.namespaces.managedIdentities)

- [REST Resource: v1.projects.locations.workloadIdentityPools.operations](#v1.projects.locations.workloadIdentityPools.operations)

- [REST Resource: v1.projects.locations.workloadIdentityPools.providers](#v1.projects.locations.workloadIdentityPools.providers)

- [REST Resource: v1.projects.locations.workloadIdentityPools.providers.keys](#v1.projects.locations.workloadIdentityPools.providers.keys)

- [REST Resource: 
v1.projects.locations.workloadIdentityPools.providers.operations](#v1.projects.locations.workloadIdentityPools.providers.operations)

- [REST Resource: v1.projects.roles](#v1.projects.roles)

- [REST Resource: v1.projects.serviceAccounts](#v1.projects.serviceAccounts)

- [REST Resource: v1.projects.serviceAccounts.keys](#v1.projects.serviceAccounts.keys)

- [REST Resource: v1.roles](#v1.roles)





## Service: iam. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:




- [https://iam.apis-berlin-build0.goog/$discovery/rest?version=v2](https://iam.apis-berlin-build0.goog/$discovery/rest?version=v2)

- [https://iam.apis-berlin-build0.goog/$discovery/rest?version=v2beta](https://iam.apis-berlin-build0.goog/$discovery/rest?version=v2beta)

- [https://iam.apis-berlin-build0.goog/$discovery/rest?version=v1](https://iam.apis-berlin-build0.goog/$discovery/rest?version=v1)

- [https://iam.apis-berlin-build0.goog/$discovery/rest?version=v1beta](https://iam.apis-berlin-build0.goog/$discovery/rest?version=v1beta)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://iam.apis-berlin-build0.goog`






## REST Resource: [v2beta. policies](/iam/docs/reference/rest/v2beta/policies)









| 
Methods | 
|



| 

`[create Policy](/iam/docs/reference/rest/v2beta/policies/createPolicy)` | 

`POST / v2beta/ {parent=policies/ */ *}` 

Creates a policy. | 
|

| 

`[delete](/iam/docs/reference/rest/v2beta/policies/delete)` | 

`DELETE / v2beta/ {name=policies/ */ */ *}` 

Deletes a policy. | 
|

| 

`[get](/iam/docs/reference/rest/v2beta/policies/get)` | 

`GET /v2beta/{name=policies/*/*/*}` 

Gets a policy. | 
|

| 

`[listPolicies](/iam/docs/reference/rest/v2beta/policies/listPolicies)` | 

`GET /v2beta/{parent=policies/*/*}` 

Retrieves the policies of the specified kind that are attached to a resource. | 
|

| 

`[update](/iam/docs/reference/rest/v2beta/policies/update)` | 

`PUT /v2beta/{policy.name=policies/*/*/*}` 

Updates the specified policy. | 
|






## REST Resource: [v2beta.policies.operations](/iam/docs/reference/rest/v2beta/policies.operations)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v2beta/policies.operations/get)` | 

`GET /v2beta/{name=policies/*/*/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v2.policies](/iam/docs/reference/rest/v2/policies)









| 
Methods | 
|



| 

`[createPolicy](/iam/docs/reference/rest/v2/policies/createPolicy)` | 

`POST /v2/{parent=policies/*/*}` 

Creates a policy. | 
|

| 

`[delete](/iam/docs/reference/rest/v2/policies/delete)` | 

`DELETE /v2/{name=policies/*/*/*}` 

Deletes a policy. | 
|

| 

`[get](/iam/docs/reference/rest/v2/policies/get)` | 

`GET /v2/{name=policies/*/*/*}` 

Gets a policy. | 
|

| 

`[listPolicies](/iam/docs/reference/rest/v2/policies/listPolicies)` | 

`GET /v2/{parent=policies/*/*}` 

Retrieves the policies of the specified kind that are attached to a resource. | 
|

| 

`[update](/iam/docs/reference/rest/v2/policies/update)` | 

`PUT /v2/{policy.name=policies/*/*/*}` 

Updates the specified policy. | 
|






## REST Resource: [v2.policies.operations](/iam/docs/reference/rest/v2/policies.operations)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v2/policies.operations/get)` | 

`GET /v2/{name=policies/*/*/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v1beta.projects.locations.workloadIdentityPools](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/create)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/delete)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/get)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/list)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPools` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/patch)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools/undelete)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1beta.projects.locations.workloadIdentityPools.operations](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.operations)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.operations/get)` | 

`GET /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v1beta.projects.locations.workloadIdentityPools.providers](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/create)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/delete)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/get)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/list)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/patch)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers/undelete)` | 

The method `google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1beta.projects.locations.workloadIdentityPools.providers.operations](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers.operations)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v1beta/projects.locations.workloadIdentityPools.providers.operations/get)` | 

`GET /v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v1.iamPolicies](/iam/docs/reference/rest/v1/iamPolicies)









| 
Methods | 
|



| 

`[lintPolicy](/iam/docs/reference/rest/v1/iamPolicies/lintPolicy)` | 

`POST /v1/iamPolicies:lintPolicy` 

Lints, or validates, an IAM policy. | 
|

| 

`[queryAuditableServices](/iam/docs/reference/rest/v1/iamPolicies/queryAuditableServices)` | 

`POST /v1/iamPolicies:queryAuditableServices` 

Returns a list of services that allow you to opt into audit logs that are not generated by default. | 
|






## REST Resource: [v1.locations.workforcePools](/iam/docs/reference/rest/v1/locations.workforcePools)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/locations.workforcePools/create)` | 

The method `google.iam.admin.v1.WorkforcePools.CreateWorkforcePool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/locations.workforcePools/delete)` | 

The method `google.iam.admin.v1.WorkforcePools.DeleteWorkforcePool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/locations.workforcePools/get)` | 

The method `google.iam.admin.v1.WorkforcePools.GetWorkforcePool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[getIamPolicy](/iam/docs/reference/rest/v1/locations.workforcePools/getIamPolicy)` | 

The method `google.iam.admin.v1.WorkforcePools.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/locations.workforcePools/list)` | 

The method `google.iam.admin.v1.WorkforcePools.ListWorkforcePools` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/locations.workforcePools/patch)` | 

The method `google.iam.admin.v1.WorkforcePools.UpdateWorkforcePool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/iam/docs/reference/rest/v1/locations.workforcePools/setIamPolicy)` | 

The method `google.iam.admin.v1.WorkforcePools.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/iam/docs/reference/rest/v1/locations.workforcePools/testIamPermissions)` | 

The method `google.iam.admin.v1.WorkforcePools.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/locations.workforcePools/undelete)` | 

The method `google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.locations.workforcePools.operations](/iam/docs/reference/rest/v1/locations.workforcePools.operations)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v1/locations.workforcePools.operations/get)` | 

`GET /v1/{name=locations/*/workforcePools/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v1.locations.workforcePools.providers](/iam/docs/reference/rest/v1/locations.workforcePools.providers)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/locations.workforcePools.providers/create)` | 

The method `google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/locations.workforcePools.providers/delete)` | 

The method `google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/locations.workforcePools.providers/get)` | 

The method `google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/locations.workforcePools.providers/list)` | 

The method `google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviders` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/locations.workforcePools.providers/patch)` | 

The method `google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/locations.workforcePools.providers/undelete)` | 

The method `google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.locations.workforcePools.providers.keys](/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/create)` | 

The method `google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderKey` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/delete)` | 

The method `google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderKey` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/get)` | 

The method `google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderKey` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/list)` | 

The method `google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderKeys` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys/undelete)` | 

The method `google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderKey` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.locations.workforcePools.providers.operations](/iam/docs/reference/rest/v1/locations.workforcePools.providers.operations)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v1/locations.workforcePools.providers.operations/get)` | 

`GET /v1/{name=locations/*/workforcePools/*/providers/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v1.locations.workforcePools.providers.scimTenants](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/create)` | 

The method `google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimTenant` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/delete)` | 

The method `google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimTenant` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/get)` | 

The method `google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimTenant` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/list)` | 

The method `google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTenants` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/patch)` | 

The method `google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimTenant` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants/undelete)` | 

The method `google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderScimTenant` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.locations.workforcePools.providers.scimTenants.tokens](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/create)` | 

The method `google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimToken` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/delete)` | 

The method `google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimToken` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/get)` | 

The method `google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimToken` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/list)` | 

The method `google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTokens` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/patch)` | 

The method `google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimToken` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/undelete)` | 

The method `google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderScimToken` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.locations.workforcePools.subjects](/iam/docs/reference/rest/v1/locations.workforcePools.subjects)









| 
Methods | 
|



| 

`[delete](/iam/docs/reference/rest/v1/locations.workforcePools.subjects/delete)` | 

The method `google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolSubject` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/locations.workforcePools.subjects/undelete)` | 

The method `google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolSubject` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.organizations.roles](/iam/docs/reference/rest/v1/organizations.roles)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/organizations.roles/create)` | 

`POST /v1/{parent=organizations/*}/roles` 

Creates a new custom `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/organizations.roles/delete)` | 

`DELETE /v1/{name=organizations/*/roles/*}` 

Deletes a custom `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[get](/iam/docs/reference/rest/v1/organizations.roles/get)` | 

`GET /v1/{name=organizations/*/roles/*}` 

Gets the definition of a `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[list](/iam/docs/reference/rest/v1/organizations.roles/list)` | 

`GET /v1/{parent=organizations/*}/roles` 

Lists every predefined `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)` that IAM supports, or every custom role that is defined for an organization or project. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/organizations.roles/patch)` | 

`PATCH /v1/{name=organizations/*/roles/*}` 

Updates the definition of a custom `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/organizations.roles/undelete)` | 

`POST /v1/{name=organizations/*/roles/*}:undelete` 

Undeletes a custom `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|






## REST Resource: [v1.permissions](/iam/docs/reference/rest/v1/permissions)









| 
Methods | 
|



| 

`[queryTestablePermissions](/iam/docs/reference/rest/v1/permissions/queryTestablePermissions)` | 

`POST /v1/permissions:queryTestablePermissions` 

Lists every permission that you can test on a resource. | 
|






## REST Resource: [v1.projects.locations.oauthClients](/iam/docs/reference/rest/v1/projects.locations.oauthClients)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.locations.oauthClients/create)` | 

The method `google.iam.admin.v1.OauthClients.CreateOauthClient` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.locations.oauthClients/delete)` | 

The method `google.iam.admin.v1.OauthClients.DeleteOauthClient` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.locations.oauthClients/get)` | 

The method `google.iam.admin.v1.OauthClients.GetOauthClient` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.locations.oauthClients/list)` | 

The method `google.iam.admin.v1.OauthClients.ListOauthClients` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/projects.locations.oauthClients/patch)` | 

The method `google.iam.admin.v1.OauthClients.UpdateOauthClient` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/projects.locations.oauthClients/undelete)` | 

The method `google.iam.admin.v1.OauthClients.UndeleteOauthClient` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.oauthClients.credentials](/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/create)` | 

The method `google.iam.admin.v1.OauthClients.CreateOauthClientCredential` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/delete)` | 

The method `google.iam.admin.v1.OauthClients.DeleteOauthClientCredential` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/get)` | 

The method `google.iam.admin.v1.OauthClients.GetOauthClientCredential` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/list)` | 

The method `google.iam.admin.v1.OauthClients.ListOauthClientCredentials` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials/patch)` | 

The method `google.iam.admin.v1.OauthClients.UpdateOauthClientCredential` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.workloadIdentityPools](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/create)` | 

The method `google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/delete)` | 

The method `google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/get)` | 

The method `google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[getIamPolicy](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/getIamPolicy)` | 

The method `google.iam.v1.WorkloadIdentityPools.GetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/list)` | 

The method `google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPools` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/patch)` | 

The method `google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setIamPolicy](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/setIamPolicy)` | 

The method `google.iam.v1.WorkloadIdentityPools.SetIamPolicy` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[testIamPermissions](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/testIamPermissions)` | 

The method `google.iam.v1.WorkloadIdentityPools.TestIamPermissions` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools/undelete)` | 

The method `google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPool` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.workloadIdentityPools.namespaces](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/create)` | 

The method `google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolNamespace` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/delete)` | 

The method `google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolNamespace` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/get)` | 

The method `google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolNamespace` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/list)` | 

The method `google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolNamespaces` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/patch)` | 

The method `google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolNamespace` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/undelete)` | 

The method `google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolNamespace` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.workloadIdentityPools.namespaces.managedIdentities](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities)









| 
Methods | 
|



| 

`[addAttestationRule](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/addAttestationRule)` | 

The method `google.iam.v1.WorkloadIdentityPools.AddAttestationRule` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[create](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/create)` | 

The method `google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolManagedIdentity` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/delete)` | 

The method `google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolManagedIdentity` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/get)` | 

The method `google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolManagedIdentity` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/list)` | 

The method `google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolManagedIdentities` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[listAttestationRules](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/listAttestationRules)` | 

The method `google.iam.v1.WorkloadIdentityPools.ListAttestationRules` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/patch)` | 

The method `google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolManagedIdentity` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[removeAttestationRule](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/removeAttestationRule)` | 

The method `google.iam.v1.WorkloadIdentityPools.RemoveAttestationRule` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[setAttestationRules](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/setAttestationRules)` | 

The method `google.iam.v1.WorkloadIdentityPools.SetAttestationRules` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities/undelete)` | 

The method `google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolManagedIdentity` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.workloadIdentityPools.operations](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.operations)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.operations/get)` | 

`GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v1.projects.locations.workloadIdentityPools.providers](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/create)` | 

The method `google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/delete)` | 

The method `google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/get)` | 

The method `google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/list)` | 

The method `google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/patch)` | 

The method `google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers/undelete)` | 

The method `google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.workloadIdentityPools.providers.keys](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/create)` | 

The method `google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProviderKey` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/delete)` | 

The method `google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProviderKey` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/get)` | 

The method `google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProviderKey` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/list)` | 

The method `google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviderKeys` is not available in Google Cloud Dedicated in Germany. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys/undelete)` | 

The method `google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProviderKey` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.workloadIdentityPools.providers.operations](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.operations)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.operations/get)` | 

`GET /v1/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*/operations/*}` 

Gets the latest state of a long-running operation. | 
|






## REST Resource: [v1.projects.roles](/iam/docs/reference/rest/v1/projects.roles)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.roles/create)` | 

`POST /v1/{parent=projects/*}/roles` 

Creates a new custom `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.roles/delete)` | 

`DELETE /v1/{name=projects/*/roles/*}` 

Deletes a custom `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.roles/get)` | 

`GET /v1/{name=projects/*/roles/*}` 

Gets the definition of a `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.roles/list)` | 

`GET /v1/{parent=projects/*}/roles` 

Lists every predefined `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)` that IAM supports, or every custom role that is defined for an organization or project. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/projects.roles/patch)` | 

`PATCH /v1/{name=projects/*/roles/*}` 

Updates the definition of a custom `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/projects.roles/undelete)` | 

`POST /v1/{name=projects/*/roles/*}:undelete` 

Undeletes a custom `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|






## REST Resource: [v1.projects.serviceAccounts](/iam/docs/reference/rest/v1/projects.serviceAccounts)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.serviceAccounts/create)` | 

`POST /v1/{name=projects/*}/serviceAccounts` 

Creates a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.serviceAccounts/delete)` | 

`DELETE /v1/{name=projects/*/serviceAccounts/*}` 

Deletes a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[disable](/iam/docs/reference/rest/v1/projects.serviceAccounts/disable)` | 

`POST /v1/{name=projects/*/serviceAccounts/*}:disable` 

Disables a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` immediately. | 
|

| 

`[enable](/iam/docs/reference/rest/v1/projects.serviceAccounts/enable)` | 

`POST /v1/{name=projects/*/serviceAccounts/*}:enable` 

Enables a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` that was disabled by `[DisableServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts/disable#google.iam.admin.v1.IAM.DisableServiceAccount)`. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.serviceAccounts/get)` | 

`GET /v1/{name=projects/*/serviceAccounts/*}` 

Gets a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[getIamPolicy](/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)` | 

`POST /v1/{resource=projects/*/serviceAccounts/*}:getIamPolicy` 

Gets the IAM policy that is attached to a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.serviceAccounts/list)` | 

`GET /v1/{name=projects/*}/serviceAccounts` 

Lists every `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` that belongs to a specific project. | 
|

| 

`[patch](/iam/docs/reference/rest/v1/projects.serviceAccounts/patch)` | 

`PATCH /v1/{serviceAccount.name=projects/*/serviceAccounts/*}` 

Patches a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[setIamPolicy](/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy)` | 

`POST /v1/{resource=projects/*/serviceAccounts/*}:setIamPolicy` 

Sets the IAM policy that is attached to a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[signBlob](/iam/docs/reference/rest/v1/projects.serviceAccounts/signBlob) 
(deprecated)**` | 

`POST /v1/{name=projects/*/serviceAccounts/*}:signBlob` 

Signs a blob using the system-managed private key for a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[signJwt](/iam/docs/reference/rest/v1/projects.serviceAccounts/signJwt) 
**(deprecated)**` | 

`POST /v1/{name=projects/*/serviceAccounts/*}:signJwt` 

Signs a JSON Web Token (JWT) using the system-managed private key for a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[testIamPermissions](/iam/docs/reference/rest/v1/projects.serviceAccounts/testIamPermissions)` | 

`POST /v1/{resource=projects/*/serviceAccounts/*}:testIamPermissions` 

Tests whether the caller has the specified permissions on a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[undelete](/iam/docs/reference/rest/v1/projects.serviceAccounts/undelete)` | 

`POST /v1/{name=projects/*/serviceAccounts/*}:undelete` 

Restores a deleted `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|

| 

`[update](/iam/docs/reference/rest/v1/projects.serviceAccounts/update)` | 

`PUT /v1/{name=projects/*/serviceAccounts/*}` 

**Note:** We are in the process of deprecating this method. | 
|






## REST Resource: [v1.projects.serviceAccounts.keys](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys)









| 
Methods | 
|



| 

`[create](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/create)` | 

`POST /v1/{name=projects/*/serviceAccounts/*}/keys` 

Creates a `[ServiceAccountKey](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`. | 
|

| 

`[delete](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/delete)` | 

`DELETE /v1/{name=projects/*/serviceAccounts/*/keys/*}` 

Deletes a `[ServiceAccountKey](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`. | 
|

| 

`[disable](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/disable)` | 

`POST /v1/{name=projects/*/serviceAccounts/*/keys/*}:disable` 

Disable a `[ServiceAccountKey](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`. | 
|

| 

`[enable](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/enable)` | 

`POST /v1/{name=projects/*/serviceAccounts/*/keys/*}:enable` 

Enable a `[ServiceAccountKey](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`. | 
|

| 

`[get](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/get)` | 

`GET /v1/{name=projects/*/serviceAccounts/*/keys/*}` 

Gets a `[ServiceAccountKey](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)`. | 
|

| 

`[list](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/list)` | 

`GET /v1/{name=projects/*/serviceAccounts/*}/keys` 

Lists every `[ServiceAccountKey](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKey)` for a service account. | 
|

| 

`[upload](/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/upload)` | 

`POST /v1/{name=projects/*/serviceAccounts/*}/keys:upload` 

Uploads the public key portion of a key pair that you manage, and associates the public key with a `[ServiceAccount](/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`. | 
|






## REST Resource: [v1.roles](/iam/docs/reference/rest/v1/roles)









| 
Methods | 
|



| 

`[get](/iam/docs/reference/rest/v1/roles/get)` | 

`GET /v1/{name=roles/*}` 

Gets the definition of a `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)`. | 
|

| 

`[list](/iam/docs/reference/rest/v1/roles/list)` | 

`GET /v1/roles` 

Lists every predefined `[Role](/iam/docs/reference/rest/v1/organizations.roles#Role)` that IAM supports, or every custom role that is defined for an organization or project. | 
|

| 

`[queryGrantableRoles](/iam/docs/reference/rest/v1/roles/queryGrantableRoles)` | 

`POST /v1/roles:queryGrantableRoles` 

Lists roles that can be granted on a Sovereign Cloud resource. | 
|