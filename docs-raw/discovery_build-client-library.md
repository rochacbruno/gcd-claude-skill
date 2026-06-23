# Build a client library

Source: https://berlin.devsitetest.how/docs/discovery/build-client-library
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












# Build a client library 






- On this page ** 
- [ Fetch the Discovery document ](#fetch-the-discovery-document)
- [ Compose a request ](#compose-a-request)
- [ Make a call and handle the response ](#make-a-call-and-handle-the-response)
- [ Examples ](#examples)

- [ Simple APIs client ](#simple-apis-client)

- 











You can use the Google APIs Discovery Service for building a variety of different tools to use with Google APIs.
However, the primary purpose of the Discovery document is to allow Google to create client
libraries in various programming languages. This document describes how you could go about
building a custom client library for Google APIs.




A stable and feature-complete client library is a complicated tool that can take months to
develop. However, the general instructions for building a simple client library for Google
APIs can be broken down to three simple steps:





- Fetching the Discovery document and constructing API surface

- Composing a request

- Making a call and fetching the response




These steps are described in more detail in the following sections. You can also have a look
at the [Simple APIs client](#simple_apis_client) sample in the Examples section to see how
these instructions map to the code.



## Fetch the Discovery document



Before you begin implementing a client library, there are some basic requirements that impact
how you will proceed down your development path. For example, your programming language of
choice may be either typed or untyped; if it is typed it could be either statically or
dynamically typed. It may be compiled or interpreted. These requirements will guide your
approach to consuming and using the Discovery document.




The first development task is to fetch the Discovery document. Your strategy for exactly when
the document is to be fetched is determined by the requirements you identified. For example,
in a statically-typed language, you might fetch the Discovery document early in the process
and then generate code to handle the specific API described by the Discovery document. For a
strongly-typed language, you might generate some code and build a compiled library. For a
dynamically typed language, you can lazily construct the programming structures to interface
to the API on the fly as the programming surface is used.



## Compose a request



Composing a requests involves two separate steps:




- Composing the request body.

- Constructing the request URL.




You need to convert the request body, if any, from a language-appropriate
representation into the correct wire format. For example, in a Java client
library, there may be a class for each request type that allows type-safe
manipulation of the request data and is serializable into JSON.




The construction of the request URL is a slightly more complicated process.




The `path` property of each method in the API uses [URI Template v04](https://code.google.com/p/uri-templates/) syntax. This property may
contain variables, which are surrounded by curly braces. Here is an example of a
`path` property with variables:



```
/example/path/var
```



In the path above, `var` is a variable. The value for this variable comes from the
Discovery document's `parameters` section for that method. Each variable name has
a corresponding value in the `parameters` object. In the example above, there is a
parameter named `var` in the `parameters` section (and its
`location` property is `path`, to indicate that it is a path
variable).




When making a request, you should substitute the value for `var` into the URL.
For example, if the user of the library makes a choice that sets `var` to the
value `foo`, the new URL will be `/example/path/foo`.




Also note that the `path` property is a relative URI. In order to calculate the
absolute URI, follow these steps:





- 
If you know your location (region), and the Discovery document has the
`endpoints` property, check if your location is present in the
`endpoints` list. If so, grab the `endpointUrl` from the
`endpoints` list whose `location` matches yours.


- 


If there is no `endpoints` property in the Discovery document or your location
is not present in the `endpoints` list or you want to target the global
endpoint, grab the `rootUrl` property from the top level of the
Discovery document.




For example, the `rootUrl` property in the
[
Discovery document](https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1) for
[
the Service Usage API](https://berlin.devsitetest.how/service-usage/docs/reference/rest) is:



```
https://serviceusage.apis-berlin-build0.goog/
```



- 
Grab the `servicePath` from the top level of the Discovery document. For
example, the `servicePath` property in the Discovery document for the Service Usage
API is empty.


- 


Concatenate them together to get:


```
https://serviceusage.apis-berlin-build0.goog/
```



- 


Grab the `path` property, expand it as a URI Template, and combine the results
of that expansion with the URI from the previous step. For example, in the v1 Service
Usage API's `serviceusage.services.enable` method, the value of the
`path` property is `v1/{+name}:enable`. So, the full URI for the
method is:



```
https://serviceusage.apis-berlin-build0.goog/v1/{+name}:enable
```






You don't need an [API key](https://berlin.devsitetest.how/docs/authentication/api-keys)
to call the Service Usage API. However, if the API you're calling requires an API key, you can
add the API key to the URI's query string:



```
REQUEST_URI ?key= API_KEY 
```


## Make a call and handle the response



After you send the request, the you need to deserialize the response into the appropriate
language representation, taking care to handle error conditions that could occur—both in the
underlying HTTP transport and error messages generated from the API service. The format of the
errors is documented as part of the [Google JSON Style
Guide](https://google.github.io/styleguide/jsoncstyleguide.xml#error).



## Examples



The following section gives a simple example of an APIs client library.



### Simple APIs client



Below is an example of a very simple client library written in Python3. The client builds an
interface for interacting with the [Service Usage API](https://berlin.devsitetest.how/service-usage/docs/reference/rest), then
uses that interface to enable the Compute Engine API (`compute.googleapis.com`) in
the project `my-project`.




```
import httplib2 
import json 
import uritemplate 
import urllib 

# Step 1: Fetch Discovery document **
DISCOVERY_URI = "https://serviceusage.apis-berlin-build0.goog/$discovery/rest?version=v1" 
h = httplib2 . Http () 
resp , content = h . request ( DISCOVERY_URI ) 
discovery = json . loads ( content ) 
location = None # Set this to your location if appropriate 
use_global_endpoint = True # Set this to False if you want to target the endpoint for your location 

** # Step 2.a: Construct base URI **
BASE_URL = None 
if not use_global_endpoint and location : 
if discovery [ 'endpoints' ]: 
BASE_URL = next (( item [ 'endpointUrl' ] for item in discovery [ 'endpoints' ] if item [ 'location' ] == location ), None ) 
if not BASE_URL : 
BASE_URL = discovery [ 'rootUrl' ] 
BASE_URL += discovery [ 'servicePath' ] 

class Collection ( object ): pass 

def createNewMethod ( name , method ): 
** # Step 2.b Compose request **
def newMethod ( ** kwargs ): 
body = kwargs . pop ( 'body' , None ) 
url = urllib . parse . urljoin ( BASE_URL , uritemplate . expand ( method [ 'path' ], kwargs )) 
for pname , pconfig in method . get ( 'parameters' , {}) . items (): 
if pconfig [ 'location' ] == 'path' and pname in kwargs : 
del kwargs [ pname ] 
if kwargs : 
url = url + '?' + urllib . parse . urlencode ( kwargs ) 
return h . request ( url , method = method [ 'httpMethod' ], body = body , 
headers = { 'content-type' : 'application/json' }) 

return newMethod 

** # Step 3.a: Build client surface **
def build ( discovery , collection ): 
for name , resource in discovery . get ( 'resources' , {}) . items (): 
setattr ( collection , name , build ( resource , Collection ())) 
for name , method in discovery . get ( 'methods' , {}) . items (): 
setattr ( collection , name , createNewMethod ( name , method )) 
return collection 

** # Step 3.b: Use the client **
service = build ( discovery , Collection ()) 
print ( serviceusage . services . enable ( name = 'projects/my-project/services/compute.googleapis.com' )) 
```



The critical components of the client are:




- 
**Step 1: Fetch the Discovery document**. The
Discovery document for the Service Usage API is retrieved and parsed into a data
structure. Since Python is a dynamically typed language, the Discovery document can be
fetched at runtime.


- 
**Step 2.a: Construct the base URI**.
The base URI is calculated.


- 
**Step 2.b: Compose the request**. When a method
is called on a collection the URI Template is expanded with the parameters passed into the
method, and parameters with a location of `query` are put into the query
parameters of the URL. Finally a request is sent to the composed URL using the HTTP method
specified in the Discovery document.


- 
**Step 3.a: Build the client surface**. The client
surface is built by recursively descending over the parsed Discovery document. For each
method in the `methods` section a new method is attached to the
`Collection` object. Because collections can be nested we look for
`resources` and recursively build a `Collection` object for all of its
members if one is found. Each nested collection is also attached as an attribute to the
`Collection` object.


- 
**Step 3.b: Use the client**. This demonstrates how the built API surface is
used. First a service object is built from the Discovery document, then the Service Usage
API is used to enable the Compute Engine API in the project `my-project`.