# Overview of the Discovery API

Source: https://berlin.devsitetest.how/docs/discovery
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












# Overview of the Discovery API 






- On this page 
- [ Discovery Service Background ](#discovery-service-background)

- [ Concepts ](#concepts)
- [ Data model ](#data-model)
- [ Operations ](#operations)

- [ Calling style ](#calling-style)

- [ REST ](#rest)

- 











The Discovery API provides a list of Google APIs for retrieving a machine-readable "Discovery
document" metadata for each API.




This document is intended for developers who want to write client libraries, IDE plugins, and
other tools for interacting with Google APIs.



## Discovery Service Background 


### Concepts 



The Google APIs Discovery Service is built upon two basic concepts:




- 
**APIs Directory**: A list of all APIs that are supported by the
APIs Discovery Service. Each directory entry shows details about a supported API, including its
*name*, a brief *description* of what it does, and a *documentation
link*. An API can have multiple Directory entries, one for each of its supported
versions.


- 
**Discovery document**: A machine-readable description of a particular API.
The Discovery document describes the surface for a particular version of an API. The
document provides details on how to access the various methods of each API via RESTful HTTP
calls. A Discovery document includes descriptions of the data and methods associated with
the API, as well as information about available OAuth scopes, and descriptions of schemas,
methods, parameters and available parameter values.




### Data model



A resource is an individual data entity with a unique identifier. The Google APIs Discovery Service operates on
two types of resources, based on the above concepts.



#### APIs Directory List: A list of APIs



Each directory entry contains an API **name**/**version** pair with the
following information:





- 
**Identification and description information,**: name, version, title, and
description.


- **Documentation information**: icons and a documentation link.

- 
**Status information**, including status labels, and an indication as to
whether or not this is the preferred version of the API.


- 
**Discovery document link**, the URI of the discovery document for this API
(given as a full URL—for example,
`https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1`).




#### Discovery Document resource: A machine-readable description of a particular API



In addition to the information provided in the APIs Directory, a Discovery document also
includes:





- 
**Schemas**, which is a list of API resource schemas that describe the data you
have access to in each API; the Google APIs Discovery Service schemas are based on [JSON Schema](https://json-schema.org/).


- 
**Methods**, including a list of API methods and available parameters for each
method.


- 
**OAuth scopes**, which identifies the list of OAuth scopes available for this
API.


- 
**Inline documentation**, which provides brief descriptions of schemas,
methods, parameters and available parameter values.





The single Directory Collection is the conceptual container of the single APIs Directory
resource, and the Discovery Document resources for each supported API.



### Operations



You can invoke two different methods on collections and resources in the Google APIs Discovery Service, as
described in the following table.




| 
Operation | 
Description | 
REST HTTP mappings | 
|

| 
list | 
Lists all supported APIs. | 
`GET` on the Directory resource URI. | 
|



## Calling style




### REST



The supported Google APIs Discovery Service operations map directly to the [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer) HTTP
`GET` verb, as described in [Operations](#background-operations).




The specific format for Google APIs Discovery Service URIs are:


```
https:// API /$discovery/rest?version= VERSION 
```



where API is the identifier for a Discovery Document resource, and
VERSION is the identifier of the particular version of the API.




Here are a couple of examples of how this works in the Google APIs Discovery Service.



List all the Google APIs Discovery Service supported APIs:


```
GET https://discovery.apis-berlin-build0.goog/discovery/v1/apis
```



[
Try it now in APIs Explorer!](//developers.google.com/apis-explorer/#p/discovery/v1/discovery.apis.list)




Get the Discovery document for Service Usage API, version 1:


```
GET https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1
```