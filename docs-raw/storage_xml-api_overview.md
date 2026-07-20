# XML API overview

Source: https://berlin.devsitetest.how/storage/docs/xml-api/overview
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/storage/docs/tpc-differences) for more details.














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

Storage

](https://berlin.devsitetest.how/docs/storage)






- 








[

Cloud Storage

](https://berlin.devsitetest.how/storage/docs)






- 








[

Reference

](https://berlin.devsitetest.how/storage/docs/apis)












# XML API overview 






- On this page 
- [ Overview ](#overview)
- [ Requests ](#requests)

- [ Authentication ](#authentication)
- [ Endpoints ](#endpoints)
- [ Headers and query string parameters ](#headers_and_query_string_parameters)
- [ Example request ](#example_request)

- [ Responses ](#responses)
- 


















This document gives an overview of the Cloud Storage XML API and is intended
for software developers. It assumes that you are familiar with RESTful services
and web programming and that you are comfortable creating applications that
operate through HTTP requests. If you are just starting out with
Cloud Storage, you should first try either the
[Google Cloud Dedicated console Quickstart](https://firebase.google.com/docs/storage/) or the [Google Cloud CLI Quickstart](/storage/docs/xml-api/get-bucket-list).
These tutorials demonstrate the basics of using Cloud Storage without
the need to use the API directly.

## Overview 

The Cloud Storage XML API is a RESTful interface that lets you manage
Cloud Storage data in a programmatic way. As a RESTful API, it relies on
*method information* and *scoping information* to define the operations to
perform:

- 

**Method information**

You specify the method information with standard HTTP methods, such as
`DELETE`, `GET`, `HEAD`, `POST`, and `PUT`.

- 

**Scoping information**

You specify the scoping information with a [publicly-accessible endpoint](/storage/docs/request-endpoints)
(URI) and various scoping parameters. For the XML API, the primary scoping
parameters are the bucket and object names. You can further scope
your operations by using [HTTP headers and query string parameters](/storage/docs/reference-headers).

You use HTTP methods to perform operations on the resource you specify in the
scope. For a list of operations available in the XML API, see
[XML API Request Methods](/storage/docs/xml-api/reference-methods). Key capabilities include:

- Standard object operations such as `PUT`, `GET`, `HEAD`, `POST`, and `DELETE`.

- Bucket management.

- Access Control List (ACL) management.

Access to Cloud Storage through the XML API is useful when you are using
tools and libraries that must work across different storage providers, or
when you are migrating from another storage provider to Cloud Storage. In the
latter case, you only need to make a few simple changes to your existing tools
and libraries to begin sending requests to Cloud Storage. For more
information about migrating to Cloud Storage, see
[Simple migration from Amazon S3 to Cloud Storage](/storage/docs/aws-simple-migration).

## Requests

The Cloud Storage XML API provides a web interface for making HTTP
requests and handling HTTP responses. The API is compatible with HTTP/1.1,
HTTP/2, and HTTP/3 protocols. Each request implements a standard HTTP method.
Along with these methods, you can use various HTTP request headers.

### Authentication

All requests to Cloud Storage must be authenticated, with the exception
of requests made to anonymously accessible objects or buckets. Requests are
typically authenticated using the [`Authorization` header](/storage/docs/xml-api/reference-headers#authorization).

### Endpoints

Most Cloud Storage XML API requests use the following URI for accessing
buckets and objects:


```
storage.apis-berlin-build0.goog
```


You can scope this further by adding a bucket and object to the URI. The
resulting URL can take two forms:


```
BUCKET_NAME .storage.apis-berlin-build0.goog/ OBJECT_NAME 
storage.apis-berlin-build0.goog/ BUCKET_NAME / OBJECT_NAME 
```


You can use the Cloud Storage URI with unsecured requests (HTTP) and secured
requests (HTTPS) that use secure sockets layer (SSL) encryption.

For additional endpoints, such as dedicated upload and download endpoints
for the XML API, see [Request Endpoints](/storage/docs/request-endpoints).

### Headers and query string parameters

The Cloud Storage XML API supports HTTP request headers. It also
supports several extension (custom) request headers, which have an `x-goog-`
prefix. Request header requirements vary depending on the kind of request you're
making. Some frequently used request headers include:



| 
Request Header | 
Description | 
Usage | 
|




| 
`Authorization` | 
The authentication string for requests. | 
Required for all authenticated requests. | 
|

| 
`Content-Length` | 
The size of the request body (excluding headers) in bytes. | 
Required for all PUT and POST requests, except chunked transfers. | 
|

| 
`Content-Type` | 
The MIME type of the request body, such as `application/xml` or `text/html`. | 
Recommended for requests that contain an entity body. | 
|

| 
`Date` | 
The date and time of the request. | 
Required for all requests, except for [signed URLs](/storage/docs/access-control/signed-urls), which can use `x-goog-date` instead. | 
|

| 
`Host` | 
The URI for the request. | 
Required for all requests. | 
|

| 
`x-goog-project-id` | 
The ID of the project you want to use. | 
Required for creating buckets or listing buckets except when you are using the XML API for interoperability, such as for compatibility with Amazon S3. For more information, see [Simple migration from Amazon S3 to Cloud Storage](/storage/docs/aws-simple-migration). | 
|



The Cloud Storage XML API also supports a variety of query string parameters,
which you can use to scope your requests. Append query string parameters to the
HTTP path portion of the request with the following syntax:


```
PATH_TO_OBJECT /? PARAMETER = VALUE & PARAMETER = VALUE ...
```


For a complete list of XML API headers and query string parameters, see
[HTTP headers and query string parameters](/storage/docs/reference-headers).

### Example request

A typical authenticated Cloud Storage request is shown in the following
example. This request [retrieves a list of objects](/storage/docs/xml-api/get-bucket-list) that are stored in a
bucket named `travel-maps`. The request limits the list of objects to only those
objects that have the prefix `/europe/france`.


```
GET /?list-type=2&prefix=/europe/france/ HTTP/1.1
Host: travel-maps.storage.apis-berlin-build0.goog
Date: Wed, 17 Feb 2010 15:31:56 -0800
Content-Length: 0
Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
```


## Responses

The Cloud Storage XML API returns standard HTTP response headers and
several extension (custom) response headers. The response headers vary according
to the operation you perform. Some frequently used response headers include:



| 
Response Header | 
Description | 
|




| 
`Cache-Control` | 
The cache control setting for the response. | 
|

| 
`Content-Length` | 
The size of the response body (excluding headers) in bytes. | 
|

| 
`Content-Type` | 
The MIME type of the response body, such as `application/xml` or `text/html`. | 
|

| 
`Date` | 
The date and time of the response. | 
|

| 
`ETag` | 
An [HTTP 1.1 entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3), which you can use to determine whether an object has changed. | 
|



Responses can also include a status code. Cloud Storage uses standard
HTTP status codes. An error response includes an XML document in the
response body, which contains information about the error conditions. For a
list of status codes used by the XML API, see [HTTP Status and Error Codes](/storage/docs/reference-status).

A typical Cloud Storage response is shown in the following example. This
example is a response to a request for [listing a bucket's contents](/storage/docs/xml-api/get-bucket-list). The
bucket name is `travel-maps` and the request is scoped so that only objects
with the prefix `/europe/france/` are returned in the list.


```
HTTP/1.1 200 OK
Content-Length: 4061
Content-Type: application/xml
Date: Wed, 17 Feb 2010 23:31:57 GMT
Cache-Control: private, max-age=0



travel-maps 
/europe/france/ 

false 

europe/france/cannes.jpg 
2010-02-17T22:11:12.487Z 
"53fc311c15eda0a031809982ccf92aac" 
5061631 
STANDARD 


europe/france/paris.jpg 
2010-02-17T22:09:57.457Z 
"53fc311c15eda0a031809982ccf92aac" 
5061631 
STANDARD 


```