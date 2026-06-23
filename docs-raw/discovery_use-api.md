# Use the Discovery API

Source: https://berlin.devsitetest.how/docs/discovery/use-api
Last updated: 2025-06-16

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/discovery/tpc-differences) for more details.














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

Google APIs Discovery Service

](https://berlin.devsitetest.how/docs/discovery)












# Use the Discovery API 






- On this page 
- [ Discovery document format ](#discovery-document-format)

- [ Basic API Description ](#basic-api-description)
- [ Authentication ](#authentication)
- [ Resources and schemas ](#resources-and-schemas)
- [ Methods ](#methods)
- [ Common parameters ](#common-parameters)
- [ Inline documentation ](#inline-documentation)

- 










This document is intended for developers who want to write client libraries, IDE plugins, and
other tools for interacting with Google APIs. The Google APIs Discovery Service allows you to do all of the
above by exposing machine readable metadata about other Google APIs through a simple API. This
guide provides an overview of each section of the Discovery document, as well as helpful tips
on how to use the document.




All calls to the API are unauthenticated, JSON-based, [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer) requests that use
SSL—in other words, URLs begin with `https`.



## Discovery document format 



This section gives an overview of the Discovery document.



All the examples below use the Discovery document from the
[Service Usage API](https://berlin.devsitetest.how/service-usage/docs/reference/rest).
You can load the
[Discovery document](https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1)
for the Service Usage API by executing this `GET` request:



```
GET https://**serviceusage**.apis-berlin-build0.goog/$discovery/rest?version=**v1**
```



The format of a Discovery document includes information that falls into six main categories:





- [Basic description](#discovery-doc-apiproperties) of the API.

- [Authentication](#discovery-doc-auth) information for the API.

- 
[Resource and schema details](#discovery-doc-resources) describing the API's
data.


- Details about the [API's methods](#discovery-doc-methods).

- 
Information about any custom [features](#discovery-features) supported by the
API.


- 
[Inline documentation](#discovery-doc-documentation) that describes key elements
of the API.





Each of these Discovery document sections is described below.



### Basic API Description



The Discovery document contains a set of API-specific properties. These properties don't necessarily
appear in this order, or in the same section of the discovery doc:


```
"id" : "serviceusage:v1" , 
"canonicalName" : "Service Usage" , 
"revision" : "20240331" , 
"servicePath" : "" , 
"baseUrl" : "https://serviceusage.apis-berlin-build0.goog/" , 
"kind" : "discovery#restDescription" , 
"description" : "Enables services that service consumers want to use on Google Cloud Platform, lists the available or enabled services, or disables services that service consumers no longer use." , 
"ownerDomain" : "google.com" , 
"version_module" : true , 
"version" : "v1" , 
"fullyEncodeReservedExpansion" : true , 
"name" : "serviceusage" , 
"title" : "Service Usage API" , 
"discoveryVersion" : "v1" , 
"rootUrl" : "https://serviceusage.apis-berlin-build0.goog/" , 
"protocol" : "rest" 
```



These API-level properties include details about a particular version of an API, including
the `name`, `version`, `title` and
`description`. The `protocol` always has a fixed value of
`rest`, as the APIs Discovery Service only supports RESTful methods of accessing the
APIs.




The `servicePath` field indicates the path prefix for this particular API
version.



### Authentication



The `auth` section contains details about the OAuth 2.0 auth scopes for the API. To
learn more about how to use scopes with OAuth 2.0, visit [Using
OAuth 2.0 to Access Google APIs](/accounts/docs/OAuth2).




The `auth` section contains a nested `oauth2` and `scopes`
section. The `scopes` section is a key/value mapping from the scope value to more
details about the scope:



```
"**auth**" : { 
"**oauth2**" : { 
"**scopes**" : { 
"https://www.googleapis.com/auth/cloud-platform" : { 
"description" : "See, edit, configure, and delete your Google Cloud data and see the email address for your Google Account." 
}, 
"https://www.googleapis.com/auth/cloud-platform.read-only" : { 
"description" : "View your data across Google Cloud services and see the email address of your Google Account" 
}, 
"https://www.googleapis.com/auth/service.management" : { 
"description" : "Manage your Google API service configuration" 
} 
} 
} 
} 
```



The `auth` section only defines the scopes for a particular API. To learn how these
scopes are associated with an API method, consult the [Methods](#discovery-doc-methods) section below.



### Resources and schemas



An API's operations act on data objects called `resources`. The Discovery document
is built around the concept of resources. Each Discovery document has a top-level
`resources` section that groups all the resources associated with the API. For
example, the Service Usage API has a `services` resource and an
`operations` resource under top-level `resources`:



```
"**resources**" : { 
"services" : { 
// Methods associated with the services resource 
} 
"operations" : { 
// Methods associated with the operations resource 
} 
} 
```



Inside each resource section are the methods associated with that resource. For example, the
Service Usage API has six methods associated with the `services`
resource: `get`, `enable`, `disable`, `batchGet`,
`batchEnable`, and `list`.




Schemas tell you what the resources in an API look like. Each Discovery document has a
top-level `schemas` section, which contains a name/value pair of schema ID to
object. Schema IDs are unique per API, and are used to uniquely identify the schema in the
`methods` section of the Discovery document. For example, here are a few of the
schemas in the Service Usage API Discovery document:



```
"**schemas**" : { 
"Method" : { 
// JSON schema of the Method resource 
}, 
"Authentication" : { 
// JSON schema of the Authentication resource 
}, 
"RubySettings" : { 
// JSON schema of the RubySettings resource 
}, 
"EnableServiceResponse" : { 
// JSON schema of the EnableServiceResponse resource 
} 
} 
```



APIs Discovery Service uses [JSON
Schema draft-03](https://tools.ietf.org/html/draft-zyp-json-schema-03) for its schema representations. The following is a snippet of the JSON
Schema for the `EnableServiceResponse` resource, along with the
`GoogleApiServiceusagev1Service` that it references. Alongside these schemas is a
portion of an actual response for a request to enable the Pub/Sub API
(`pubsub.googleapis.com`).





| 
**`EnableServiceResponse` Resource JSON Schema:** | 
**Actual response for enabling a service:** | 
|

| 


```
"EnableServiceResponse" : { 
"id" : "EnableServiceResponse" , 
"description" : "Response message for the `EnableService` method. This response message is assigned to the `response` field of the returned Operation when that operation is done." , 
"properties" : { 
"**service**" : { 
"description" : "The new state of the service after enabling." , 
"$ref" : "GoogleApiServiceusageV1Service" 
} 
}, 
"type" : "object" 
}, 
"GoogleApiServiceusageV1Service" : { 
"description" : "A service that is available for use by the consumer." , 
"properties" : { 
"**config**" : { 
"$ref" : "GoogleApiServiceusageV1ServiceConfig" , 
"description" : "The service configuration of the available service. Some fields may be filtered out of the configuration in responses to the `ListServices` method. These fields are present only in responses to the `GetService` method." 
}, 
"**name**" : { 
"type" : "string" , 
"description" : "The resource name of the consumer and service. A valid name would be: - projects/123/services/serviceusage.googleapis.com" 
}, 
"`state`" : { 
"enumDescriptions" : [ 
"The default value, which indicates that the enabled state of the service is unspecified or not meaningful. Currently, all consumers other than projects (such as folders and organizations) are always in this state." , 
"The service cannot be used by this consumer. It has either been explicitly disabled, or has never been enabled." , 
"The service has been explicitly enabled for use by this consumer." 
], 
"description" : "Whether or not the service has been enabled for use by the consumer." , 
"type" : "string" , 
"enum" : [ 
"STATE_UNSPECIFIED" , 
"DISABLED" , 
"ENABLED" 
] 
}, 
"`parent`" : { 
"type" : "string" , 
"description" : "The resource name of the consumer. A valid name would be: - projects/123" 
} 
}, 
"id" : "GoogleApiServiceusageV1Service" , 
"type" : "object" 
} 
```

| 


```
"response" : { 
"@type" : "type.googleapis.com/google.api.serviceusage.v1.EnableServiceResponse" , 
"**service**" : { 
"**name "** ** : "projects/232342569935/services/pubsub.googleapis.com" , 
" config**" : { 
"name" : "pubsub.googleapis.com" , 
"title" : "Cloud Pub/Sub API" , 
"documentation" : { 
"summary" : "Provides reliable, many-to-many, asynchronous messaging between applications.\n" 
}, 
"quota" : {}, 
"authentication" : {}, 
"usage" : { 
"requirements" : [ 
"serviceusage.googleapis.com/tos/cloud" 
] 
}, 
"monitoring" : {} 
}, 
"`state`" : "ENABLED" , 
"`parent`" : "projects/232342569935" 
} 
} 
```
** 
** | 
|




The fields in bold show the mapping between the JSON Schema and the actual response.



As shown in this example, schemas can contain references to other schemas. If you are building
a client library, this can help you effectively model the objects of an API in your data model
classes. In the `EnableServiceResponse` example above, the `service`
property is a reference to a schema with ID `GoogleApiServiceusageV1Service`,
another schema in the Service Usage API Discovery document. You can substitute the
`GoogleApiServiceusageV1Service` property in the `EnableServiceResponse`
resource with the value of the `GoogleApiServiceusageV1Service` schema
(note that the `$ref` syntax comes from the [JSON Schema
spec](https://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.28)).




Methods may also reference schemas when indicating their request and response bodies. Refer to
the [Methods](#discovery-doc-methods) section for more details.



### Methods



The core of the Discovery document is built around methods. Methods are the operations that
can be performed on an API. You will find the `methods` section in various areas of
the Discovery document, including at the top level (which we call API-level methods) or at
the `resources` level.



```
"**methods**" : { 
// API-level methods 
} 
"**resources**" : { 
" resource1 " : { 
" methods " : { 
// resource-level methods 
} 
"**resources**" : { 
" nestedResource " : { 
" methods " : { 
// methods can even be found in nested-resources 
} 
} 
} 
} 
} 
```



While an API *can* have API-level methods, a resource *must* have a
`methods` section.




Each `methods` section is a key-value map from method name to other details about
that method. The example below documents three methods, `get`, `enable`
and `disable`:



```
"methods" : { 
"get" : { //details about the "get" method }, 
"enable" : { //details about the "enable" method }, 
"disable" : { //details about the "disable" method } 
} 
```



Finally, each method's section details various properties about that method. Here is an
example of the `enable` method:



```
"enable" : { 
"path" : "v1/{+name}:enable" , 
"request" : { 
"$ref" : "EnableServiceRequest" 
}, 
"parameterOrder" : [ 
"name" 
], 
"id" : "serviceusage.services.enable" , 
"response" : { 
"$ref" : "Operation" 
}, 
"description" : "Enable a service so that it can be used with a project." , 
"httpMethod" : "POST" , 
"flatPath" : "v1/{v1Id}/{v1Id1}/services/{servicesId}:enable" , 
"scopes" : [ 
"https://www.googleapis.com/auth/cloud-platform" , 
"https://www.googleapis.com/auth/service.management" 
], 
"parameters" : { 
"name" : { 
"location" : "path" , 
"description" : "Name of the consumer and service to enable the service on. The `EnableService` and `DisableService` methods currently only support projects. Enabling a service requires that the service is public or is shared with the user enabling the service. An example name would be: `projects/123/services/serviceusage.googleapis.com` where `123` is the project number." , 
"required" : true , 
"type" : "string" , 
"pattern" : "^[^/]+/[^/]+/services/[^/]+$" 
} 
} 
}, 
```



This section contains general method details such as a unique `ID` to identify the
method, the `httpMethod` to use, and the `path` of the method (for
details on how to use the `path` property to calculate the full method url, see the
[Compose a request](#build-compose) section). In addition to these general method
properties, there are a few properties that connect the method with other sections in the Discovery document:



#### Scopes



The `auth` section defined earlier in this documentation contains information about
all the scopes supported by a particular API. If a method supports one of these scopes, it will
have a scopes array. There is one entry in this array for each scope supported by the method.


Note that choosing an auth scope to use in your application depends on various factors such as
which methods are being called and what parameters are sent along with the method. Therefore,
the decision of which scope to use is left to the developer. Discovery only documents which
scopes are valid for a method.



#### Request and response



If the method has a request or response body, these are documented in the `request`
or `response` sections, respectively. For example, for the `enable`
method, the content of the `request` section indicates that the method's request is
defined by a JSON schema with an ID of `EnableServiceRequest`. This schema can be
found in the top-level schemas section.



#### Parameters



If a method has parameters that should be specified by the user, these parameters are
documented in the method-level `parameters` section. This section contains a
key/value mapping of the parameter name to more details about that parameter.




For example, there's one parameter for the `enable` method: `name`.
Parameters can either go in the `path` or the URL `query`; the
`location` property indicates where the client library should put the parameter.




There are many other properties describing the parameter, including the parameter data
`type` (useful for strongly-typed languages), whether the parameter is
`required`, and whether the parameter is an enum. See the reference documentation
for this API for more details about these properties.




**Parameter order**



There are many ways for client libraries to structure their interfaces. One way is to have a
method with each API parameter in the method signature. However, since JSON is an unordered
format, it's difficult to know programmatically how to order the parameters in the method
signature. The `parameterOrder` array provides a fixed parameter ordering for
making requests. The array lists the name of each parameter in order of significance; it can
contain either path or query parameters, but every parameter in the array is required.



#### Media upload



If a method supports uploading media, such as images, audio, or video, then the location and
protocols supported for uploading that media are documented in the `mediaUpload`
section. This section contains details about which upload protocols are supported, and
information about what kinds of media can be uploaded.




The `enable` method doesn't contain a `mediaUpload` section. However, a
typical `mediaUpload` section might look like the following:


```
"**supportsMediaUpload**" : true , 
"**mediaUpload**" : { 
"**accept**" : [ 
"image/*" 
], 
"**maxSize**" : "10MB" , 
"**protocols**" : { 
"**simple**" : { 
"**multipart**" : true , 
"**path**" : "/upload/storage/v1beta1/b/{bucket}/o" 
}, 
"**resumable**" : { 
"**multipart**" : true , 
"**path**" : "/resumable/upload/storage/v1beta1/b/{bucket}/o" 
} 
} 
} 
```



In the example above, the `supportsMediaUpload` property is a boolean value that
determines if the method supports uploading media. If the value is true then the
`mediaUpload` section documents the kinds of media that can be uploaded.




The `accept` property is a list of [media-ranges](https://tools.ietf.org/html/rfc2616#section-14.1) that determine which
mime-types are acceptable to upload. The endpoint shown in the example above will accept any
image format.




The `maxSize` property has the maximum size of an upload. The value is a string in
units of MB, GB or TB. In the example above, uploads are limited to a maximum size of 10 MB.
Note that this value doesn't reflect an individual user's remaining storage quota for that
API, so even if the upload is less than `maxSize` the client library should still
be prepared to handle an upload that fails because of insufficient space.




The `protocols` section lists the upload protocols that a method supports. The
`simple` protocol is simply POSTing the media to the given endpoint in a single
HTTP request. The `resumable` protocol implies that the endpoint given in the
`path` URI supports the [resumable upload
protocol](/drive/manage-uploads#resumable). If the `multipart` property is `true` then the endpoint
accepts multipart uploads, which means both the JSON request and the media can be wrapped
together in a [mutlipart/related](https://tools.ietf.org/html/rfc2387) body and sent
together. Note that both `simple` and `resumable` protocols may support
multipart uploads.




The `path` property is a URI Template and should be expanded just like the
`path` property for the method, as outlined in the [Compose
a request](#build-compose) section.



#### Media download



If a method supports downloading media, such as images, audio, or video, then that is indicated
by the `supportsMediaDownload` parameter:



```
"supportsMediaDownload" : true , 
```



When downloading media you must set the `alt` query parameter to `media`
in the request URL.




If the `useMediaDownloadService` property of the API method is `true`,
insert `/download` before `servicePath` to avoid a redirect. For example,
the download path is `/download/youtube/v3/captions/{id}` if the concatenation of
`servicePath` and `path` is `/youtube/v3/captions/{id}`. It is
recommended to construct media download URL with `/download` even when
`useMediaDownloadService` is false.





### Common parameters



The top-level Discovery document contains a `parameters` property. This section is
similar to the [parameters section for each
method](#discovery-doc-methods-parameters), however these parameters can be applied to any method in the API.




For example, the `get` and `list` methods of the Service Usage API can
have a `prettyPrint` parameter in the request parameters, which will format the
response for all those methods in a human-readable format. Here's a list of common parameters:




| 
Parameter | 
Meaning | 
Notes | 
Applicability | 
|

| 
`access_token` | 
OAuth 2.0 token for the current user. | 



- 
[One possible way](/identity/protocols/OAuth2) to provide an OAuth 2.0
token.


| 
|

| 
`alt` | 


Data format for the response.
| 



- Valid values: `json`, `atom`, `csv`. 

- Default value: varies per API.

- Not all values are available for every API.

| 



- Applies to all operations for all resources.

| 
|

| 
`callback` | 
Callback function. | 



- Name of the JavaScript callback function that handles the response.

- 
Used in JavaScript [JSON-P](https://en.wikipedia.org/wiki/JSONP)
requests.



| 
|

| 
`fields` | 
Selector specifying a subset of fields to include in the response. | 




- Use for better performance.


| 
|

| 
`key` | 

API key. (REQUIRED) [](https://code.google.com/apis/console/)
| 




- Required unless you provide an OAuth 2.0 token.

- 
Your [API key](/console-help#WhatIsKey) identifies your project and
provides you with API access, quota, and reports.


- 
Obtain your project's API key from the [APIs console](https://code.google.com/apis/console/).



| 
|

| 
`prettyPrint` | 
Returns response with identations and line breaks. | 




- Returns the response in a human-readable format if `true`. 

- Default value: varies per API.

- 
When this is `false`, it can reduce the response payload size, which might
lead to better performance in some environments.



| 
|

| 
`quotaUser` | 
Alternative to `userIp`. | 




- 
Lets you enforce per-user quotas from a server-side application even in cases when the
user's IP address is unknown. This can occur, for example, with applications that run
cron jobs on App Engine on a user's behalf.


- 
You can choose any arbitrary string that uniquely identifies a user, but it is limited
to 40 characters.


- Overrides `userIp` if both are provided.

- Learn more about [capping usage](/console-help#cappingusage).


| 
|

| 
`userIp` | 
IP address of the end user for whom the API call is being made. | 




- 
Lets you enforce per-user quotas when calling the API from a server-side
application.


- Learn more about [capping usage](/console-help#cappingusage).


| 
|



### Inline documentation



Each Discovery document is annotated with a number of `description` fields that
provide inline documentation for the API. The `description` fields can be found for
the following API elements:





- API itself

- OAuth scopes

- Resource schemas

- API Methods

- Method parameters

- Acceptable values for certain parameters




These fields are especially useful if you wish to use the Google APIs Discovery Service to generate human
readable documentation for a client library—for example, JavaDoc.