# Method: organizations.locations.quotaPreferences.list

Source: https://documentation.s3ns.fr/docs/quotas/reference/rest/v1/organizations.locations.quotaPreferences/list
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












# Method: organizations. locations. quota Preferences. list 






- On this page 
- [ HTTP request ](#http-request)
- [ Path parameters ](#path-parameters)
- [ Query parameters ](#query-parameters)
- [ Request body ](#request-body)
- [ Response body ](#response-body)
- [ Authorization scopes ](#authorization-scopes)
- [ IAM Permissions ](#iam-permissions)
- 















- [HTTP request](#body.HTTP_TEMPLATE)

- [Path parameters](#body.PATH_PARAMETERS)

- [Query parameters](#body.QUERY_PARAMETERS)

- [Request body](#body.request_body)

- [Response body](#body.response_body)

- [Authorization scopes](#body.aspect)

- [IAM Permissions](#body.aspect_1)

- [Try it!](#try-it)






Lists QuotaPreferences in a given project, folder or organization.






### HTTP request 



`GET https://cloudquotas.s3nsapis.fr/v1/{parent=organizations/*/locations/*}/quotaPreferences`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.




### Path parameters 








| 
Parameters | 
|



| 
`parent` | 



`string`



Required. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed.

When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container.

Example parents: `projects/123/locations/global`

| 
|





### Query parameters








| 
Parameters | 
|



| 
`page Size` | 



`integer`



Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

| 
|

| 
`page Token` | 



`string`



Optional. A token identifying a page of results the server should return.

| 
|

| 
`filter` | 



`string`



Optional. Filter result QuotaPreferences by their state, type, create/update time range.

Example filters: `reconciling=true AND request_type=CLOUD_CONSOLE`, `reconciling=true OR creation_time>2022-12-03T10:30:00`

| 
|

| 
`order By` | 



`string`



Optional. How to order of the results. By default, the results are ordered by create time.

Example orders: `quotaId`, `service, createTime`

| 
|





### Request body



The request body must be empty.




### Response body



If successful, the response body contains an instance of `[ListQuotaPreferencesResponse](/docs/quotas/reference/rest/v1/ListQuotaPreferencesResponse)`.




### Authorization scopes



Requires the following OAuth scope:




- `https://www.googleapis.com/auth/cloud-platform`


For more information, see the [Authentication Overview](/docs/authentication#authorization-gcp).




### IAM Permissions



Requires the following [IAM](https://documentation.s3ns.fr/iam/docs) permission on the `parent` resource:




- `cloudquotas.quotas.get`


For more information, see the [IAM documentation](https://documentation.s3ns.fr/iam/docs).