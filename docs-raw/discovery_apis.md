# Discovery Document

Source: https://berlin.devsitetest.how/docs/discovery/apis
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












# Discovery Document 






- On this page 
- [ Methods ](#methods)
- [ Resource Representations ](#resource-representations)
- 










Discovery documents are available for specific versions of most APIs. Each API's Discovery Document describes the surface of the API, how to access the API and how API requests and responses are structured. The information provided by the discovery document includes API-level properties such as an API description, resource schemas, authentication scopes, and methods.




## Methods 



The Discovery document focuses on the  RESTful method of invoking an API. The  [discovery.apis.list](#method_discovery_apis_list)  method returns the list of all APIs supported by the Google APIs Discovery Service including the urls for retrieving the REST-based discovery documents. 




[list](/docs/discovery/list)

Retrieve the list of APIs supported at this endpoint. 






## Resource Representations





```
{
"kind" : "discovery#restDescription" , 
"discoveryVersion" : "v1" , 
"id" : string , 
"name" : string , 
"canonicalName" : string , 
"version" : string , 
"revision" : string , 
"title" : string , 
"description" : string , 
"icons" : {
"x16" : string , 
"x32" : string 
} , 
"documentationLink" : string , 
"labels" : [ 
string 
], 
"protocol" : "rest" , 
"baseUrl" : string , 
"basePath" : string , 
"rootUrl" : string , 
"servicePath" : string , 
"batchPath" : "batch" , 
"endpoints" : [ 
{
"endpointUrl" : string , 
"location" : string , 
"deprecated" : boolean , 
"description" : string 
}
], 
"parameters" : {
(key) : {
"id" : string , 
"type" : string , 
"$ref" : string , 
"description" : string , 
"default" : string , 
"required" : boolean , 
"format" : string , 
"pattern" : string , 
"minimum" : string , 
"maximum" : string , 
"enum" : [ 
string 
], 
"enumDescriptions" : [ 
string 
], 
"repeated" : boolean , 
"location" : string , 
"properties" : {
(key) : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ) 
} , 
"additionalProperties" : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ), 
"items" : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ), 
"annotations" : {
"required" : [ 
string 
] 
}
}
} , 
"auth" : {
"oauth2" : {
"scopes" : {
(key) : {
"description" : string 
}
}
}
} , 
"features" : [ 
string 
], 
"schemas" : {
(key) : {
"id" : string , 
"type" : string , 
"$ref" : string , 
"description" : string , 
"default" : string , 
"required" : boolean , 
"deprecated" : boolean , 
"format" : string , 
"pattern" : string , 
"minimum" : string , 
"maximum" : string , 
"enum" : [ 
string 
], 
"enumDescriptions" : [ 
string 
], 
"enumDeprecated" : [ 
boolean 
], 
"repeated" : boolean , 
"location" : string , 
"properties" : {
(key) : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ) 
} , 
"additionalProperties" : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ), 
"items" : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ), 
"annotations" : {
"required" : [ 
string 
] 
}
}
} , 
"methods" : {
(key) : {
"id" : string , 
"path" : string , 
"httpMethod" : string , 
"description" : string , 
"deprecated" : boolean , 
"parameters" : {
(key) : {
"id" : string , 
"type" : string , 
"$ref" : string , 
"description" : string , 
"default" : string , 
"required" : boolean , 
"deprecated" : boolean , 
"format" : string , 
"pattern" : string , 
"minimum" : string , 
"maximum" : string , 
"enum" : [ 
string 
], 
"enumDescriptions" : [ 
string 
], 
"enumDeprecated" : [ 
boolean 
], 
"repeated" : boolean , 
"location" : string , 
"properties" : {
(key) : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ) 
} , 
"additionalProperties" : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ), 
"items" : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ), 
"annotations" : {
"required" : [ 
string 
] 
}
}
} , 
"parameterOrder" : [ 
string 
], 
"request" : {
"$ref" : string 
} , 
"response" : {
"$ref" : string 
} , 
"scopes" : [ 
(value) 
], 
"supportsMediaDownload" : boolean , 
"supportsMediaUpload" : boolean , 
"mediaUpload" : {
"accept" : [ 
string 
], 
"maxSize" : string , 
"protocols" : {
"simple" : {
"multipart" : true , 
"path" : string 
} , 
"resumable" : {
"multipart" : true , 
"path" : string 
}
}
} , 
"supportsSubscription" : boolean 
}
} , 
"resources" : {
(key) : {
"methods" : {
(key) : {
"id" : string , 
"path" : string , 
"httpMethod" : string , 
"description" : string , 
"deprecated" : boolean , 
"parameters" : {
(key) : {
"id" : string , 
"type" : string , 
"$ref" : string , 
"description" : string , 
"default" : string , 
"required" : boolean , 
"deprecated" : boolean , 
"format" : string , 
"pattern" : string , 
"minimum" : string , 
"maximum" : string , 
"enum" : [ 
string 
], 
"enumDescriptions" : [ 
string 
], 
"enumDeprecated" : [ 
boolean 
], 
"repeated" : boolean , 
"location" : string , 
"properties" : {
(key) : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ) 
} , 
"additionalProperties" : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ), 
"items" : ( [ JsonSchema ](https://tools.ietf.org/html/draft-zyp-json-schema-03) ), 
"annotations" : {
"required" : [ 
string 
] 
}
}
} , 
"parameterOrder" : [ 
string 
], 
"request" : {
"$ref" : string 
} , 
"response" : {
"$ref" : string 
} , 
"scopes" : [ 
(value) 
], 
"supportsMediaDownload" : boolean , 
"supportsMediaUpload" : boolean , 
"mediaUpload" : {
"accept" : [ 
string 
], 
"maxSize" : string , 
"protocols" : {
"simple" : {
"multipart" : true , 
"path" : string 
} , 
"resumable" : {
"multipart" : true , 
"path" : string 
}
}
} , 
"supportsSubscription" : boolean 
}
} , 
"deprecated" : boolean , 
"resources" : {
(key) : ( RestResource ) 
}
}
}
}
```




| 
Property Name | 
Value | 
Description | 
|



| 
`kind` | 
`string` | 

The kind for this response. The fixed string
`discovery#restDescription`.
| 
|

| 
`discoveryVersion` | 
`string` | 
Indicate the version of the Discovery API used to generate this doc. | 
|

| 
`id` | 
`string` | 

The ID of the Discovery document for the API. For example,
`urlshortener:v1`. 
| 
|

| 
`name` | 
`string` | 
The name of the API. For example, `urlshortener`. | 
|

| 
`canonicalName` | 
`string` | 

The canonical name of the API. For example, `Url
Shortener`. 
| 
|

| 
`version` | 
`string` | 
The version of the API. For example, `v1`. | 
|

| 
`revision` | 
`string` | 
The revision of the API. | 
|

| 
`title` | 
`string` | 

The title of the API. For example, "Google Url Shortener
API". 
| 
|

| 
`description` | 
`string` | 
The description of this API. | 
|

| 
`icons` | 
`object` | 
Links to 16x16 and 32x32 icons representing the API. | 
|

| 
` icons. x16` | 
`string` | 
The URL of the 16x16 icon. | 
|

| 
` icons. x32` | 
`string` | 
The URL of the 32x32 icon. | 
|

| 
`documentationLink` | 
`string` | 
A link to human-readable documentation for the API. | 
|

| 
`labels[]` | 
`list` | 

Labels for the status of this API. Valid values include
`limited_availability` or `deprecated`. 
| 
|

| 
`protocol` | 
`string` | 
The protocol described by the document. For example, REST. | 
|

| 
`rootUrl` | 
`string` | 
The root url under which all API services live. | 
|

| 
`endpoints[]` | 
`list` | 

A list of location-based endpoint objects for this API. Each object contains the
endpoint URL, location, description and deprecation status.
| 
|

| 
` endpoints[]. endpointUrl` | 
`string` | 
The URL of the endpoint target host. | 
|

| 
` endpoints[]. location` | 
`string` | 
The location of the endpoint. | 
|

| 
` endpoints[]. description` | 
`string` | 
A string describing the host designated by the URL. | 
|

| 
` endpoints[]. deprecated` | 
`boolean` | 
Whether this endpoint is deprecated. | 
|

| 
`parameters` | 
`object` | 
Common parameters that apply across all apis. | 
|

| 
` parameters. (key)` | 
`nested object` | 
Description of a single parameter. | 
|

| 
` parameters.(key). id` | 
`string` | 
Unique identifier for this schema. | 
|

| 
` parameters.(key). type` | 
`string` | 

The value type for this schema. A list of values can be found at the ["type"
section in the JSON Schema](https://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.1).
| 
|

| 
` parameters.(key). $ref` | 
`string` | 

A reference to another schema. The value of this property is the ID of another
schema.
| 
|

| 
` parameters.(key). description` | 
`string` | 
A description of this object. | 
|

| 
` parameters.(key). default` | 
`string` | 
The default value of this property (if one exists). | 
|

| 
` parameters.(key). required` | 
`boolean` | 
Whether the parameter is required. | 
|

| 
` parameters.(key). format` | 
`string` | 

An additional regular expression or key that helps constrain the value.
For more details, see the [type and format summary](/docs/discovery/type-format).
| 
|

| 
` parameters.(key). pattern` | 
`string` | 
The regular expression this parameter must conform to. | 
|

| 
` parameters.(key). minimum` | 
`string` | 
The minimum value of this parameter. | 
|

| 
` parameters.(key). maximum` | 
`string` | 
The maximum value of this parameter. | 
|

| 
` parameters.(key). enum[]` | 
`list` | 
Values this parameter may take (if it is an enum). | 
|

| 
` parameters.(key). enumDescriptions[]` | 
`list` | 

The descriptions for the enums. Each position maps to the corresponding value in the
enum array.
| 
|

| 
` parameters.(key). repeated` | 
`boolean` | 
Whether this parameter may appear multiple times. | 
|

| 
` parameters.(key). location` | 
`string` | 
Whether this parameter goes in the query or the path for REST requests. | 
|

| 
` parameters.(key). properties` | 
`object` | 
If this is a schema for an object, list the schema for each property of this object. | 
|

| 
` parameters.(key).properties. (key)` | 
`nested object` | 

A single property of this object. The value is itself a JSON Schema object describing
this property.
| 
|

| 
` parameters.(key). additionalProperties` | 
`nested object` | 

If this is a schema for an object, this property is the schema for any additional
properties with dynamic keys on this object.
| 
|

| 
` parameters.(key). items` | 
`nested object` | 

If this is a schema for an array, this property is the schema for each element in the
array.
| 
|

| 
` parameters.(key). annotations` | 
`object` | 
Additional information about this property. | 
|

| 
` parameters.(key).annotations. required[]` | 
`list` | 
A list of methods that require this property on requests. | 
|

| 
`auth` | 
`object` | 
Authentication information. | 
|

| 
` auth. oauth2` | 
`object` | 
OAuth 2.0 authentication information. | 
|

| 
` auth.oauth2. scopes` | 
`object` | 
Available OAuth 2.0 scopes. | 
|

| 
` auth.oauth2.scopes. (key)` | 
`object` | 
The scope value. | 
|

| 
` auth.oauth2.scopes.(key). description` | 
`string` | 
Description of scope. | 
|

| 
`features[]` | 
`list` | 
A list of supported features for this API. | 
|

| 
`schemas` | 
`object` | 
The schemas for this API. | 
|

| 
` schemas. (key)` | 
`nested object` | 
An individual schema description. | 
|

| 
` schemas.(key). id` | 
`string` | 
Unique identifier for this schema. Example: `URL` | 
|

| 
` schemas.(key). type` | 
`string` | 

The value type for this schema. A list of values can be found at
the  ["type"
section in the JSON Schema](https://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.1) . 
| 
|

| 
` schemas.(key). $ref` | 
`string` | 

A reference to another schema. The value of this property is the ID of another
schema.
| 
|

| 
` schemas.(key). description` | 
`string` | 
A description of this object. | 
|

| 
` schemas.(key). default` | 
`string` | 
The default value of this property (if one exists). | 
|

| 
` schemas.(key). required` | 
`boolean` | 
Whether the parameter is required. | 
|

| 
` schemas.(key). deprecated` | 
`boolean` | 
Whether this schema is deprecated. | 
|

| 
` schemas.(key). format` | 
`string` | 

An additional regular expression or key that helps constrain the value.
For more details, see the [type and format summary](/docs/discovery/type-format).
| 
|

| 
` schemas.(key). pattern` | 
`string` | 
The regular expression this parameter must conform to. | 
|

| 
` schemas.(key). minimum` | 
`string` | 
The minimum value of this parameter. | 
|

| 
` schemas.(key). maximum` | 
`string` | 
The maximum value of this parameter. | 
|

| 
` schemas.(key). enum[]` | 
`list` | 
Values this parameter may take (if it is an enum). | 
|

| 
` schemas.(key). enumDescriptions[]` | 
`list` | 

The descriptions for the enums. Each position maps to the corresponding value in the
`enum` array.
| 
|

| 
` schemas.(key). enumDeprecated[]` | 
`list` | 

The deprecation status for the enums. Each position maps to the corresponding value in
the `enum` array.
| 
|

| 
` schemas.(key). repeated` | 
`boolean` | 
Whether this parameter may appear multiple times. | 
|

| 
` schemas.(key). location` | 
`string` | 
Whether this parameter goes in the query or the path for REST requests. | 
|

| 
` schemas.(key). properties` | 
`object` | 

If this is a schema for an object, list the schema for each property of this
object.
| 
|

| 
` schemas.(key).properties. (key)` | 
`nested object` | 

A single property of this object. The value is itself a JSON Schema object describing
this property.
| 
|

| 
` schemas.(key). additionalProperties` | 
`nested object` | 

If this is a schema for an object, this property is the schema for any additional
properties with dynamic keys on this object.
| 
|

| 
` schemas.(key). items` | 
`nested object` | 

If this is a schema for an array, this property is the schema for each element in the
array.
| 
|

| 
` schemas.(key). annotations` | 
`object` | 
Additional information about this property. | 
|

| 
` schemas.(key).annotations. required[]` | 
`list` | 
A list of methods that require this property on requests. | 
|

| 
`methods` | 
`object` | 
API-level methods for this API. | 
|

| 
` methods. (key)` | 
`nested object` | 
An individual method description. | 
|

| 
` methods.(key). id` | 
`string` | 

A unique ID for this method. This property can be used to match methods between
different versions of Discovery.
| 
|

| 
` methods.(key). description` | 
`string` | 
Description of this method. | 
|

| 
` methods.(key). deprecated` | 
`boolean` | 
Whether this method is deprecated. | 
|

| 
` methods.(key). parameters` | 
`object` | 
Details for all parameters in this method. | 
|

| 
` methods.(key).parameters. (key)` | 
`nested object` | 
Details for a single parameter in this method. | 
|

| 
` methods.(key).parameters.(key). id` | 
`string` | 
Unique identifier for this schema. | 
|

| 
` methods.(key).parameters.(key). type` | 
`string` | 

The value type for this schema.    A list of values can be found at
the  ["type"
section in the JSON Schema](https://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.1) . 
| 
|

| 
` methods.(key).parameters.(key). $ref` | 
`string` | 

A reference to another schema. The value of this property is the ID of another
schema.
| 
|

| 
` methods.(key).parameters.(key). description` | 
`string` | 
A description of this object. | 
|

| 
` methods.(key).parameters.(key). default` | 
`string` | 
The default value of this property (if one exists). | 
|

| 
` methods.(key).parameters.(key). required` | 
`boolean` | 
Whether the parameter is required. | 
|

| 
` methods.(key).parameters.(key). deprecated` | 
`boolean` | 
Whether the parameter is deprecated. | 
|

| 
` methods.(key).parameters.(key). format` | 
`string` | 

An additional regular expression or key that helps constrain the value.
For more details, see the [type and format summary](/docs/discovery/type-format).
| 
|

| 
` methods.(key).parameters.(key). pattern` | 
`string` | 
The regular expression this parameter must conform to. | 
|

| 
` methods.(key).parameters.(key). minimum` | 
`string` | 
The minimum value of this parameter. | 
|

| 
` methods.(key).parameters.(key). maximum` | 
`string` | 
The maximum value of this parameter. | 
|

| 
` methods.(key).parameters.(key). enum[]` | 
`list` | 
Values this parameter may take (if it is an enum). | 
|

| 
` methods.(key).parameters.(key). enumDescriptions[]` | 
`list` | 

The descriptions for the enums. Each position maps to the corresponding value in the
`enum` array.
| 
|

| 
` methods.(key).parameters.(key). enumDeprecated[]` | 
`list` | 

The deprecation status for the enums. Each position maps to the corresponding value in
the `enum` array.
| 
|

| 
` methods.(key).parameters.(key). repeated` | 
`boolean` | 
Whether this parameter may appear multiple times. | 
|

| 
` methods.(key).parameters.(key). location` | 
`string` | 
Whether this parameter goes in the query or the path for REST requests. | 
|

| 
` methods.(key).parameters.(key). properties` | 
`object` | 
If this is a schema for an object, list the schema for each property of this object. | 
|

| 
` methods.(key).parameters.(key).properties. (key)` | 
`nested object` | 

A single property of this object. The value is itself a JSON Schema object describing
this property.
| 
|

| 
` methods.(key).parameters.(key). additionalProperties` | 
`nested object` | 

If this is a schema for an object, this property is the schema for any additional
properties with dynamic keys on this object.
| 
|

| 
` methods.(key).parameters.(key). items` | 
`nested object` | 

If this is a schema for an array, this property is the schema for each element in the
array.
| 
|

| 
` methods.(key).parameters.(key). annotations` | 
`object` | 
Additional information about this property. | 
|

| 
` methods.(key).parameters.(key).annotations. required[]` | 
`list` | 
A list of methods for which this property is required on requests. | 
|

| 
` methods.(key). parameterOrder[]` | 
`list` | 

Ordered list of required parameters. This serves as a hint to clients on how to
structure their method signatures. The array is ordered such that the most significant
parameter appears first.
| 
|

| 
` methods.(key). scopes[]` | 
`list` | 
OAuth 2.0 scopes applicable to this method. | 
|

| 
` methods.(key). supportsMediaDownload` | 
`boolean` | 
Whether this method supports media downloads. | 
|

| 
` methods.(key). supportsMediaUpload` | 
`boolean` | 
Whether this method supports media uploads. | 
|

| 
` methods.(key). mediaUpload` | 
`object` | 
Media upload parameters. | 
|

| 
` methods.(key).mediaUpload. accept[]` | 
`list` | 
MIME Media Ranges for acceptable media uploads to this method. | 
|

| 
` methods.(key).mediaUpload. maxSize` | 
`string` | 
Maximum size of a media upload, such as "1MB", "2GB" or "3TB". | 
|

| 
` methods.(key). supportsSubscription` | 
`boolean` | 
Whether this method supports subscriptions. | 
|

| 
`baseUrl` | 
`string` | 
[DEPRECATED] The base URL for REST requests. | 
|

| 
`basePath` | 
`string` | 
[DEPRECATED] The base path for REST requests. | 
|

| 
`servicePath` | 
`string` | 
The base path for all REST requests. | 
|

| 
`batchPath` | 
`string` | 
The path for REST batch requests. | 
|

| 
` methods.(key). path` | 
`string` | 

The URI path of this REST method. Should be used in conjunction with the
`servicePath` property at the API-level.
| 
|

| 
` methods.(key). httpMethod` | 
`string` | 
HTTP method used by this method. | 
|

| 
` methods.(key). request` | 
`object` | 
The schema for the request. | 
|

| 
` methods.(key).request. $ref` | 
`string` | 
Schema ID for the request schema. | 
|

| 
` methods.(key).request. parameterName` | 
`string` | 

[DEPRECATED] Some APIs have this field for backward-compatibility reasons. It can be
safely ignored.
| 
|

| 
` methods.(key). response` | 
`object` | 
The schema for the response. | 
|

| 
` methods.(key).response. $ref` | 
`string` | 
Schema ID for the response schema. | 
|

| 
` methods.(key).mediaUpload. protocols` | 
`object` | 
Supported upload protocols. | 
|

| 
` methods.(key).mediaUpload.protocols. simple` | 
`object` | 
Supports uploading as a single HTTP request. | 
|

| 
` methods.(key).mediaUpload.protocols.simple. multipart` | 
`boolean` | 
True if this endpoint supports upload multipart media. | 
|

| 
` methods.(key).mediaUpload.protocols.simple. path` | 
`string` | 

The URI path to be used for upload. Should be used in conjunction with the
`rootURL` property at the api-level.
| 
|

| 
` methods.(key).mediaUpload.protocols. resumable` | 
`object` | 
Supports the Resumable Media Upload protocol. | 
|

| 
` methods.(key).mediaUpload.protocols.resumable. multipart` | 
`boolean` | 
`true` if this endpoint supports uploading multipart media. | 
|

| 
` methods.(key).mediaUpload.protocols.resumable. path` | 
`string` | 

The URI path to be used for upload. Should be used in conjunction with the
`rootURL` property at the API-level.
| 
|

| 
`resources` | 
`object` | 
The resources in this API. | 
|

| 
` resources. (key)` | 
`nested object` | 

An individual resource description. Contains methods and sub-resources related to this
resource.
| 
|

| 
` resources.(key). methods` | 
`object` | 
Methods on this resource. | 
|

| 
` resources.(key).methods. (key)` | 
`nested object` | 
Description for any methods on this resource. | 
|

| 
` resources.(key).methods.(key). id` | 
`string` | 

A unique ID for this method. This property can be used to match methods between
different versions of Discovery.
| 
|

| 
` resources.(key).methods.(key). path` | 
`string` | 

The URI path of this REST method. Should be used in conjunction with the
`servicePath` property at the API-level.
| 
|

| 
` resources.(key).methods.(key). flatPath` | 
`string` | 

The URI path of this REST method in (RFC 6570) format without level 2 features
({+var}). Supplementary to the `path` property.
| 
|

| 
` resources.(key).methods.(key). httpMethod` | 
`string` | 
HTTP method used by this method. | 
|

| 
` resources.(key).methods.(key). description` | 
`string` | 
Description of this method. | 
|

| 
` resources.(key).methods.(key). deprecated` | 
`boolean` | 
Whether this method is deprecated. | 
|

| 
` resources.(key).methods.(key). parameters` | 
`object` | 
Details for all parameters in this method. | 
|

| 
` resources.(key).methods.(key).parameters. (key)` | 
`nested object` | 
Details for a single parameter in this method. | 
|

| 
` resources.(key).methods.(key).parameters.(key). id` | 
`string` | 
Unique identifier for this schema. | 
|

| 
` resources.(key).methods.(key).parameters.(key). type` | 
`string` | 

The value type for this schema.   A list of values can be found at
the  ["type"
section in the JSON Schema](https://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.1) . 
| 
|

| 
` resources.(key).methods.(key).parameters.(key). $ref` | 
`string` | 

A reference to another schema. The value of this property is the "ID" of
another schema.
| 
|

| 
` resources.(key).methods.(key).parameters.(key). description` | 
`string` | 
A description of this object. | 
|

| 
` resources.(key).methods.(key).parameters.(key). default` | 
`string` | 
The default value of this property (if one exists). | 
|

| 
` resources.(key).methods.(key).parameters.(key). required` | 
`boolean` | 
Whether the parameter is required. | 
|

| 
` resources.(key).methods.(key).parameters.(key). deprecated` | 
`boolean` | 
Whether the parameter is deprecated. | 
|

| 
` resources.(key).methods.(key).parameters.(key). format` | 
`string` | 

An additional regular expression or key that helps constrain the value.
For more details, see the [type and format summary](/docs/discovery/type-format).
| 
|

| 
` resources.(key).methods.(key).parameters.(key). pattern` | 
`string` | 
The regular expression this parameter must conform to. | 
|

| 
` resources.(key).methods.(key).parameters.(key). minimum` | 
`string` | 
The minimum value of this parameter. | 
|

| 
` resources.(key).methods.(key).parameters.(key). maximum` | 
`string` | 
The maximum value of this parameter. | 
|

| 
` resources.(key).methods.(key).parameters.(key). enum[]` | 
`list` | 
Values this parameter may take (if it is an enum). | 
|

| 
` resources.(key).methods.(key).parameters.(key). enumDescriptions[]` | 
`list` | 

The descriptions for the enums. Each position maps to the corresponding value in the
`enum` array.
| 
|

| 
` resources.(key).methods.(key).parameters.(key). enumDeprecated[]` | 
`list` | 

The deprecation status for the enums. Each position maps to the corresponding value in
the `enum` array.
| 
|

| 
` resources.(key).methods.(key).parameters.(key). repeated` | 
`boolean` | 
Whether this parameter may appear multiple times. | 
|

| 
` resources.(key).methods.(key).parameters.(key). location` | 
`string` | 
Whether this parameter goes in the query or the path for REST requests. | 
|

| 
` resources.(key).methods.(key).parameters.(key). properties` | 
`object` | 

If this is a schema for an object, list the schema for each property of this
object.
| 
|

| 
` resources.(key).methods.(key).parameters.(key).properties. (key)` | 
`nested object` | 

A single property of this object. The value is itself a JSON Schema object describing
this property.
| 
|

| 
` resources.(key).methods.(key).parameters.(key). additionalProperties` | 
`nested object` | 

If this is a schema for an object, this property is the schema for any additional
properties with dynamic keys on this object.
| 
|

| 
` resources.(key).methods.(key).parameters.(key). items` | 
`nested object` | 

If this is a schema for an array, this property is the schema for each element in the
array.
| 
|

| 
` resources.(key).methods.(key).parameters.(key). annotations` | 
`object` | 
Additional information about this property. | 
|

| 
` resources.(key).methods.(key).parameters.(key).annotations. required[]` | 
`list` | 
A list of methods that require this property on requests. | 
|

| 
` resources.(key).methods.(key). parameterOrder[]` | 
`list` | 

Ordered list of required parameters. This serves as a hint to clients on how to
structure their method signatures. The array is ordered such that the most significant
parameter appears first.
| 
|

| 
` resources.(key).methods.(key). request` | 
`object` | 
The schema for the request. | 
|

| 
` resources.(key).methods.(key).request. $ref` | 
`string` | 
Schema ID for the request schema. | 
|

| 
` resources.(key).methods.(key). response` | 
`object` | 
The schema for the response. | 
|

| 
` resources.(key).methods.(key).response. $ref` | 
`string` | 
Schema ID for the response schema. | 
|

| 
` resources.(key).methods.(key). scopes[]` | 
`list` | 
OAuth 2.0 scopes applicable to this method. | 
|

| 
` resources.(key).methods.(key). supportsMediaDownload` | 
`boolean` | 
Whether this method supports media downloads. | 
|

| 
` resources.(key).methods.(key). supportsMediaUpload` | 
`boolean` | 
Whether this method supports media uploads. | 
|

| 
` resources.(key).methods.(key). mediaUpload` | 
`object` | 
Media upload parameters. | 
|

| 
` resources.(key).methods.(key).mediaUpload. accept[]` | 
`list` | 
MIME Media Ranges for acceptable media uploads to this method. | 
|

| 
` resources.(key).methods.(key).mediaUpload. maxSize` | 
`string` | 
Maximum size of a media upload, such as "1MB", "2GB" or "3TB". | 
|

| 
` resources.(key).methods.(key).mediaUpload. protocols` | 
`object` | 
Supported upload protocols. | 
|

| 
` resources.(key).methods.(key).mediaUpload.protocols. simple` | 
`object` | 
Supports uploading as a single HTTP request. | 
|

| 
` resources.(key).methods.(key).mediaUpload.protocols.simple. multipart` | 
`boolean` | 
`true` if this endpoint supports upload multipart media. | 
|

| 
` resources.(key).methods.(key).mediaUpload.protocols.simple. path` | 
`string` | 

The URI path to be used for upload. Should be used in conjunction with the
`rootURL` property at the API-level.
| 
|

| 
` resources.(key).methods.(key).mediaUpload.protocols. resumable` | 
`object` | 
Supports the Resumable Media Upload protocol. | 
|

| 
` resources.(key).methods.(key).mediaUpload.protocols.resumable. multipart` | 
`boolean` | 
`true` if this endpoint supports uploading multipart media. | 
|

| 
` resources.(key).methods.(key).mediaUpload.protocols.resumable. path` | 
`string` | 

The URI path to be used for upload. Should be used in conjunction with the
`rootURL` property at the API-level.
| 
|

| 
` resources.(key).methods.(key). supportsSubscription` | 
`boolean` | 
Whether this method supports subscriptions. | 
|

| 
` resources.(key). deprecated` | 
`boolean` | 
Whether this resource is deprecated. | 
|

| 
` resources.(key). resources` | 
`object` | 
Sub-resources on this resource. | 
|

| 
` resources.(key).resources. (key)` | 
`nested object` | 
Description for any sub-resources on this resource. | 
|