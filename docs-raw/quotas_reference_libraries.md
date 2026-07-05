# Cloud Quotas client libraries

Source: https://berlin.devsitetest.how/docs/quotas/reference/libraries
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://berlin.devsitetest.how/docs/quotas)






- 








[

Reference

](https://berlin.devsitetest.how/docs/quotas/apis)












# Cloud Quotas client libraries 






- On this page 
- [ Install the client library ](#install)
- [ Set up authentication ](#authentication)
- [ Use the client library ](#use)
- [ Additional resources ](#resources)
- 












This page shows how to get started with the Cloud Client Libraries for the
Cloud Quotas API. Client libraries make it easier to access
Google Cloud Dedicated in Germany APIs from a supported language. Although you can use
Google Cloud Dedicated in Germany APIs directly by making raw requests to the server, client
libraries provide simplifications that significantly reduce the amount of code
you need to write.

Read more about the Cloud Client Libraries
and the older Google API Client Libraries in
[Client libraries explained](/apis/docs/client-libraries-explained).



## Install the client library 















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 








For information about this client library's requirements and install
dependencies, see [Setting up a C++ development environment](/cpp/docs/setup).





































Install the `Google.Cloud.CloudQuotas.V1` package
from NuGet. Add it to your project in the normal way (for example by right-clicking
on the project in Visual Studio and choosing "Manage NuGet Packages...").
Ensure you enable pre-release packages (for example, in the Visual Studio NuGet
user interface, check the "Include prerelease" box). Some of the following samples
might only work with the latest pre-release version (`1.0.0-beta01`) of
`Google.Cloud.CloudQuotas.V1`.





For more information, see [Setting Up a C# Development Environment](/dotnet/docs/setup).






































```
go get cloud.google.com/go/cloudquotas
```





For more information, see [Setting Up a Go Development Environment](/go/docs/setup).








































If you are using [Maven](https://maven.apache.org/), add
the following to your `pom.xml` file. For more information about
BOMs, see [The Google Cloud Platform Libraries BOM](https://berlin.devsitetest.how/java/docs/bom).
























```
dependencyManagement >
dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>libraries - bom / artifactId >
version>26 .83.0 / version >
type>pom / type >
scope>import / scope >
/ dependency >
/ dependencies >
/ dependencyManagement >

dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>google - cloud - cloudquotas / artifactId >
/ dependency >
/ dependencies >
```



If you are using [Gradle](https://gradle.org/),
add the following to your dependencies:
























```
implementation ' com . google . cloud : google - cloud - cloudquotas : 0.61.0 ' 
```



If you are using [sbt](https://www.scala-sbt.org/), add
the following to your dependencies:
























```
libraryDependencies += "com.google.cloud" % "google-cloud-cloudquotas" % "0.61.0" 
```







For more information, see [Setting Up a Java Development Environment](/java/docs/setup).







































```
npm install @google-cloud/cloudquotas
```





For more information, see [Setting Up a Node.js Development Environment](/nodejs/docs/setup).







































```
composer require google/cloud
```






For more information, see [Using PHP on Google Cloud](/php/docs).







































```
pip install google-cloud-quotas
```





For more information, see [Setting Up a Python Development Environment](/python/docs/setup).







































```
gem install google-cloud-cloud_quotas
```





For more information, see [Setting Up a Ruby Development Environment](/ruby/docs/setup).
























## Set up authentication

To authenticate calls to Google Cloud Dedicated in Germany APIs, client libraries support
[Application Default Credentials (ADC)](/docs/authentication/application-default-credentials);
the libraries look for credentials in a set of defined locations and use those credentials
to authenticate requests to the API. With ADC, you can make
credentials available to your application in a variety of environments, such as local
development or production, without needing to modify your application code.

For production environments, the way you set up ADC depends on the service
and context. For more information, see [Set up Application Default Credentials](/docs/authentication/provide-credentials-adc).

For a local development environment, you can set up ADC with the credentials
that are associated with your Google Account:











- 









[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).

After signing in,
[initialize](/sdk/docs/initializing) the Google Cloud CLI by running the following command:





```
gcloud init
```




















- 









Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








A sign-in screen appears. After you sign in, your credentials are stored in the
[
local credential file used by ADC](/docs/authentication/application-default-credentials#personal).















## Use the client library

The following example shows how to use the client library.

















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 

































```
// Copyright 2024 Google LLC 
// 
// Licensed under the Apache License, Version 2.0 (the "License"); 
// you may not use this file except in compliance with the License. 
// You may obtain a copy of the License at 
// 
// https://www.apache.org/licenses/LICENSE-2.0 
// 
// Unless required by applicable law or agreed to in writing, software 
// distributed under the License is distributed on an "AS IS" BASIS, 
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and 
// limitations under the License. 

//! [all] 
#include "google/cloud/cloudquotas/v1/cloud_quotas_client.h" 
#include "google/cloud/location.h" 
#include 
#include 

int main ( int argc , char * argv []) try { 
if ( argc != 2 ) { 
std :: cerr "Usage: " argv [ 0 ] " project-id \n " ; 
return 1 ; 
} 

namespace cloudquotas = :: google :: cloud :: cloudquotas_v1 ; 
auto client = 
cloudquotas :: CloudQuotasClient ( cloudquotas :: MakeCloudQuotasConnection ()); 

auto const parent = google :: cloud :: Location ( argv [ 1 ], "global" ). FullName (); 
for ( auto r : client . ListQuotaPreferences ( parent )) { 
if ( ! r ) throw std :: move ( r ). status (); 
std :: cout r - > DebugString () " \n " ; 
} 

return 0 ; 
} catch ( google :: cloud :: Status const & status ) { 
std :: cerr "google::cloud::Status thrown: " status " \n " ; 
return 1 ; 
} 
//! [all] 
```



































































```
// Copyright 2026 Google LLC 
// 
// Licensed under the Apache License, Version 2.0 (the "License"); 
// you may not use this file except in compliance with the License. 
// You may obtain a copy of the License at 
// 
// https://www.apache.org/licenses/LICENSE-2.0 
// 
// Unless required by applicable law or agreed to in writing, software 
// distributed under the License is distributed on an "AS IS" BASIS, 
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and 
// limitations under the License. 

// Generated code. DO NOT EDIT! 

namespace GoogleCSharpSnippets 
{ 
using [ Google.Api.Gax ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html) ; 
using [ Google.Cloud.CloudQuotas.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.html) ; 
using [ Google.Protobuf.WellKnownTypes ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html) ; 
using System ; 
using System.Threading.Tasks ; 

/// Generated snippets. 
public sealed class AllGeneratedCloudQuotasClientSnippets 
{ 
/// Snippet for ListQuotaInfos 
public void ListQuotaInfosRequestObject () 
{ 
// Snippet: ListQuotaInfos(ListQuotaInfosRequest, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ ListQuotaInfosRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest.html) request = new [ ListQuotaInfosRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest.html)
{ 
ParentAsServiceName = [ ServiceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html) . [ FromProjectLocationService ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html#Google_Cloud_CloudQuotas_V1_ServiceName_FromProjectLocationService_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[SERVICE]" ), 
}; 
// Make the request 
PagedEnumerable , QuotaInfo > response = cloudQuotasClient . [ ListQuotaInfos ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfos_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 

// Iterate over all response items, lazily performing RPCs as required 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
foreach ( [ ListQuotaInfosResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = response . ReadPage ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaInfosAsync 
public async Task ListQuotaInfosRequestObjectAsync () 
{ 
// Snippet: ListQuotaInfosAsync(ListQuotaInfosRequest, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ ListQuotaInfosRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest.html) request = new [ ListQuotaInfosRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest.html)
{ 
ParentAsServiceName = [ ServiceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html) . [ FromProjectLocationService ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html#Google_Cloud_CloudQuotas_V1_ServiceName_FromProjectLocationService_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[SERVICE]" ), 
}; 
// Make the request 
PagedAsyncEnumerable , QuotaInfo > response = cloudQuotasClient . [ ListQuotaInfosAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfosAsync_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 

// Iterate over all response items, lazily performing RPCs as required 
await foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
await foreach ( [ ListQuotaInfosResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = await response . ReadPageAsync ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaInfos 
public void ListQuotaInfos () 
{ 
// Snippet: ListQuotaInfos(string, string, int?, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]" ; 
// Make the request 
PagedEnumerable , QuotaInfo > response = cloudQuotasClient . [ ListQuotaInfos ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfos_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent ); 

// Iterate over all response items, lazily performing RPCs as required 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
foreach ( [ ListQuotaInfosResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = response . ReadPage ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaInfosAsync 
public async Task ListQuotaInfosAsync () 
{ 
// Snippet: ListQuotaInfosAsync(string, string, int?, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]" ; 
// Make the request 
PagedAsyncEnumerable , QuotaInfo > response = cloudQuotasClient . [ ListQuotaInfosAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfosAsync_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent ); 

// Iterate over all response items, lazily performing RPCs as required 
await foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
await foreach ( [ ListQuotaInfosResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = await response . ReadPageAsync ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaInfos 
public void ListQuotaInfosResourceNames () 
{ 
// Snippet: ListQuotaInfos(ServiceName, string, int?, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ ServiceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html) parent = [ ServiceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html) . [ FromProjectLocationService ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html#Google_Cloud_CloudQuotas_V1_ServiceName_FromProjectLocationService_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[SERVICE]" ); 
// Make the request 
PagedEnumerable , QuotaInfo > response = cloudQuotasClient . [ ListQuotaInfos ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfos_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent ); 

// Iterate over all response items, lazily performing RPCs as required 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
foreach ( [ ListQuotaInfosResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = response . ReadPage ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaInfosAsync 
public async Task ListQuotaInfosResourceNamesAsync () 
{ 
// Snippet: ListQuotaInfosAsync(ServiceName, string, int?, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ ServiceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html) parent = [ ServiceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html) . [ FromProjectLocationService ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html#Google_Cloud_CloudQuotas_V1_ServiceName_FromProjectLocationService_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[SERVICE]" ); 
// Make the request 
PagedAsyncEnumerable , QuotaInfo > response = cloudQuotasClient . [ ListQuotaInfosAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfosAsync_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent ); 

// Iterate over all response items, lazily performing RPCs as required 
await foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
await foreach ( [ ListQuotaInfosResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = await response . ReadPageAsync ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for GetQuotaInfo 
public void GetQuotaInfoRequestObject () 
{ 
// Snippet: GetQuotaInfo(GetQuotaInfoRequest, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ GetQuotaInfoRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest.html) request = new [ GetQuotaInfoRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest.html)
{ 
QuotaInfoName = [ QuotaInfoName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html) . [ FromProjectLocationServiceQuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html#Google_Cloud_CloudQuotas_V1_QuotaInfoName_FromProjectLocationServiceQuotaInfo_System_String_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[SERVICE]" , "[QUOTA_INFO]" ), 
}; 
// Make the request 
[ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = cloudQuotasClient . [ GetQuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfo_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// End snippet 
} 

/// Snippet for GetQuotaInfoAsync 
public async Task GetQuotaInfoRequestObjectAsync () 
{ 
// Snippet: GetQuotaInfoAsync(GetQuotaInfoRequest, CallSettings) 
// Additional: GetQuotaInfoAsync(GetQuotaInfoRequest, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ GetQuotaInfoRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest.html) request = new [ GetQuotaInfoRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest.html)
{ 
QuotaInfoName = [ QuotaInfoName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html) . [ FromProjectLocationServiceQuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html#Google_Cloud_CloudQuotas_V1_QuotaInfoName_FromProjectLocationServiceQuotaInfo_System_String_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[SERVICE]" , "[QUOTA_INFO]" ), 
}; 
// Make the request 
[ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = await cloudQuotasClient . [ GetQuotaInfoAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfoAsync_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// End snippet 
} 

/// Snippet for GetQuotaInfo 
public void GetQuotaInfo () 
{ 
// Snippet: GetQuotaInfo(string, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/quotaInfos/[QUOTA_INFO]" ; 
// Make the request 
[ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = cloudQuotasClient . [ GetQuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfo_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_) ( name ); 
// End snippet 
} 

/// Snippet for GetQuotaInfoAsync 
public async Task GetQuotaInfoAsync () 
{ 
// Snippet: GetQuotaInfoAsync(string, CallSettings) 
// Additional: GetQuotaInfoAsync(string, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/quotaInfos/[QUOTA_INFO]" ; 
// Make the request 
[ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = await cloudQuotasClient . [ GetQuotaInfoAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfoAsync_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_) ( name ); 
// End snippet 
} 

/// Snippet for GetQuotaInfo 
public void GetQuotaInfoResourceNames () 
{ 
// Snippet: GetQuotaInfo(QuotaInfoName, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ QuotaInfoName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html) name = [ QuotaInfoName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html) . [ FromProjectLocationServiceQuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html#Google_Cloud_CloudQuotas_V1_QuotaInfoName_FromProjectLocationServiceQuotaInfo_System_String_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[SERVICE]" , "[QUOTA_INFO]" ); 
// Make the request 
[ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = cloudQuotasClient . [ GetQuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfo_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_) ( name ); 
// End snippet 
} 

/// Snippet for GetQuotaInfoAsync 
public async Task GetQuotaInfoResourceNamesAsync () 
{ 
// Snippet: GetQuotaInfoAsync(QuotaInfoName, CallSettings) 
// Additional: GetQuotaInfoAsync(QuotaInfoName, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ QuotaInfoName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html) name = [ QuotaInfoName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html) . [ FromProjectLocationServiceQuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html#Google_Cloud_CloudQuotas_V1_QuotaInfoName_FromProjectLocationServiceQuotaInfo_System_String_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[SERVICE]" , "[QUOTA_INFO]" ); 
// Make the request 
[ QuotaInfo ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = await cloudQuotasClient . [ GetQuotaInfoAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfoAsync_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_) ( name ); 
// End snippet 
} 

/// Snippet for ListQuotaPreferences 
public void ListQuotaPreferencesRequestObject () 
{ 
// Snippet: ListQuotaPreferences(ListQuotaPreferencesRequest, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ ListQuotaPreferencesRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest.html) request = new [ ListQuotaPreferencesRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest.html)
{ 
ParentAsLocationName = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ), 
Filter = "" , 
OrderBy = "" , 
}; 
// Make the request 
PagedEnumerable , QuotaPreference > response = cloudQuotasClient . [ ListQuotaPreferences ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferences_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 

// Iterate over all response items, lazily performing RPCs as required 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
foreach ( [ ListQuotaPreferencesResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = response . ReadPage ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaPreferencesAsync 
public async Task ListQuotaPreferencesRequestObjectAsync () 
{ 
// Snippet: ListQuotaPreferencesAsync(ListQuotaPreferencesRequest, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ ListQuotaPreferencesRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest.html) request = new [ ListQuotaPreferencesRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest.html)
{ 
ParentAsLocationName = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ), 
Filter = "" , 
OrderBy = "" , 
}; 
// Make the request 
PagedAsyncEnumerable , QuotaPreference > response = cloudQuotasClient . [ ListQuotaPreferencesAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferencesAsync_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 

// Iterate over all response items, lazily performing RPCs as required 
await foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
await foreach ( [ ListQuotaPreferencesResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = await response . ReadPageAsync ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaPreferences 
public void ListQuotaPreferences () 
{ 
// Snippet: ListQuotaPreferences(string, string, int?, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
string parent = "projects/[PROJECT]/locations/[LOCATION]" ; 
// Make the request 
PagedEnumerable , QuotaPreference > response = cloudQuotasClient . [ ListQuotaPreferences ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferences_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent ); 

// Iterate over all response items, lazily performing RPCs as required 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
foreach ( [ ListQuotaPreferencesResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = response . ReadPage ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaPreferencesAsync 
public async Task ListQuotaPreferencesAsync () 
{ 
// Snippet: ListQuotaPreferencesAsync(string, string, int?, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
string parent = "projects/[PROJECT]/locations/[LOCATION]" ; 
// Make the request 
PagedAsyncEnumerable , QuotaPreference > response = cloudQuotasClient . [ ListQuotaPreferencesAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferencesAsync_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent ); 

// Iterate over all response items, lazily performing RPCs as required 
await foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
await foreach ( [ ListQuotaPreferencesResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = await response . ReadPageAsync ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaPreferences 
public void ListQuotaPreferencesResourceNames () 
{ 
// Snippet: ListQuotaPreferences(LocationName, string, int?, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ); 
// Make the request 
PagedEnumerable , QuotaPreference > response = cloudQuotasClient . [ ListQuotaPreferences ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferences_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent ); 

// Iterate over all response items, lazily performing RPCs as required 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
foreach ( [ ListQuotaPreferencesResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = response . ReadPage ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for ListQuotaPreferencesAsync 
public async Task ListQuotaPreferencesResourceNamesAsync () 
{ 
// Snippet: ListQuotaPreferencesAsync(LocationName, string, int?, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ); 
// Make the request 
PagedAsyncEnumerable , QuotaPreference > response = cloudQuotasClient . [ ListQuotaPreferencesAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferencesAsync_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent ); 

// Iterate over all response items, lazily performing RPCs as required 
await foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 

// Or iterate over pages (of server-defined size), performing one RPC per page 
await foreach ( [ ListQuotaPreferencesResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response . AsRawResponses ()) 
{ 
// Do something with each page of items 
Console . WriteLine ( "A page of results:" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
} 

// Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required 
int pageSize = 10 ; 
Page singlePage = await response . ReadPageAsync ( pageSize ); 
// Do something with the page of items 
Console . WriteLine ( $"A page of {pageSize} results (unless it's the final page):" ); 
foreach ( [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage ) 
{ 
// Do something with each item 
Console . WriteLine ( item ); 
} 
// Store the pageToken, for when the next page is required. 
string nextPageToken = singlePage . NextPageToken ; 
// End snippet 
} 

/// Snippet for GetQuotaPreference 
public void GetQuotaPreferenceRequestObject () 
{ 
// Snippet: GetQuotaPreference(GetQuotaPreferenceRequest, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ GetQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest.html) request = new [ GetQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest.html)
{ 
QuotaPreferenceName = [ QuotaPreferenceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html) . [ FromProjectLocationQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html#Google_Cloud_CloudQuotas_V1_QuotaPreferenceName_FromProjectLocationQuotaPreference_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[QUOTA_PREFERENCE]" ), 
}; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ GetQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreference_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// End snippet 
} 

/// Snippet for GetQuotaPreferenceAsync 
public async Task GetQuotaPreferenceRequestObjectAsync () 
{ 
// Snippet: GetQuotaPreferenceAsync(GetQuotaPreferenceRequest, CallSettings) 
// Additional: GetQuotaPreferenceAsync(GetQuotaPreferenceRequest, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ GetQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest.html) request = new [ GetQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest.html)
{ 
QuotaPreferenceName = [ QuotaPreferenceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html) . [ FromProjectLocationQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html#Google_Cloud_CloudQuotas_V1_QuotaPreferenceName_FromProjectLocationQuotaPreference_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[QUOTA_PREFERENCE]" ), 
}; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ GetQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// End snippet 
} 

/// Snippet for GetQuotaPreference 
public void GetQuotaPreference () 
{ 
// Snippet: GetQuotaPreference(string, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
string name = "projects/[PROJECT]/locations/[LOCATION]/quotaPreferences/[QUOTA_PREFERENCE]" ; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ GetQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreference_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( name ); 
// End snippet 
} 

/// Snippet for GetQuotaPreferenceAsync 
public async Task GetQuotaPreferenceAsync () 
{ 
// Snippet: GetQuotaPreferenceAsync(string, CallSettings) 
// Additional: GetQuotaPreferenceAsync(string, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
string name = "projects/[PROJECT]/locations/[LOCATION]/quotaPreferences/[QUOTA_PREFERENCE]" ; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ GetQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( name ); 
// End snippet 
} 

/// Snippet for GetQuotaPreference 
public void GetQuotaPreferenceResourceNames () 
{ 
// Snippet: GetQuotaPreference(QuotaPreferenceName, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ QuotaPreferenceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html) name = [ QuotaPreferenceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html) . [ FromProjectLocationQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html#Google_Cloud_CloudQuotas_V1_QuotaPreferenceName_FromProjectLocationQuotaPreference_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[QUOTA_PREFERENCE]" ); 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ GetQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreference_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( name ); 
// End snippet 
} 

/// Snippet for GetQuotaPreferenceAsync 
public async Task GetQuotaPreferenceResourceNamesAsync () 
{ 
// Snippet: GetQuotaPreferenceAsync(QuotaPreferenceName, CallSettings) 
// Additional: GetQuotaPreferenceAsync(QuotaPreferenceName, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ QuotaPreferenceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html) name = [ QuotaPreferenceName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html) . [ FromProjectLocationQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html#Google_Cloud_CloudQuotas_V1_QuotaPreferenceName_FromProjectLocationQuotaPreference_System_String_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" , "[QUOTA_PREFERENCE]" ); 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ GetQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( name ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreference 
public void CreateQuotaPreferenceRequestObject () 
{ 
// Snippet: CreateQuotaPreference(CreateQuotaPreferenceRequest, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ CreateQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest.html) request = new [ CreateQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest.html)
{ 
ParentAsLocationName = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ), 
QuotaPreferenceId = "" , 
QuotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (), 
IgnoreSafetyChecks = 
{ 
[ QuotaSafetyCheck ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html) . [ Unspecified ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html#Google_Cloud_CloudQuotas_V1_QuotaSafetyCheck_Unspecified) , 
}, 
}; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ CreateQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreferenceAsync 
public async Task CreateQuotaPreferenceRequestObjectAsync () 
{ 
// Snippet: CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest, CallSettings) 
// Additional: CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ CreateQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest.html) request = new [ CreateQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest.html)
{ 
ParentAsLocationName = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ), 
QuotaPreferenceId = "" , 
QuotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (), 
IgnoreSafetyChecks = 
{ 
[ QuotaSafetyCheck ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html) . [ Unspecified ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html#Google_Cloud_CloudQuotas_V1_QuotaSafetyCheck_Unspecified) , 
}, 
}; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ CreateQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreference 
public void CreateQuotaPreference1 () 
{ 
// Snippet: CreateQuotaPreference(string, QuotaPreference, string, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
string parent = "projects/[PROJECT]/locations/[LOCATION]" ; 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
string quotaPreferenceId = "" ; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ CreateQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent , quotaPreference , quotaPreferenceId ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreferenceAsync 
public async Task CreateQuotaPreference1Async () 
{ 
// Snippet: CreateQuotaPreferenceAsync(string, QuotaPreference, string, CallSettings) 
// Additional: CreateQuotaPreferenceAsync(string, QuotaPreference, string, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
string parent = "projects/[PROJECT]/locations/[LOCATION]" ; 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
string quotaPreferenceId = "" ; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ CreateQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent , quotaPreference , quotaPreferenceId ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreference 
public void CreateQuotaPreference1ResourceNames () 
{ 
// Snippet: CreateQuotaPreference(LocationName, QuotaPreference, string, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ); 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
string quotaPreferenceId = "" ; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ CreateQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent , quotaPreference , quotaPreferenceId ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreferenceAsync 
public async Task CreateQuotaPreference1ResourceNamesAsync () 
{ 
// Snippet: CreateQuotaPreferenceAsync(LocationName, QuotaPreference, string, CallSettings) 
// Additional: CreateQuotaPreferenceAsync(LocationName, QuotaPreference, string, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ); 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
string quotaPreferenceId = "" ; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ CreateQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent , quotaPreference , quotaPreferenceId ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreference 
public void CreateQuotaPreference2 () 
{ 
// Snippet: CreateQuotaPreference(string, QuotaPreference, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
string parent = "projects/[PROJECT]/locations/[LOCATION]" ; 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ CreateQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent , quotaPreference ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreferenceAsync 
public async Task CreateQuotaPreference2Async () 
{ 
// Snippet: CreateQuotaPreferenceAsync(string, QuotaPreference, CallSettings) 
// Additional: CreateQuotaPreferenceAsync(string, QuotaPreference, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
string parent = "projects/[PROJECT]/locations/[LOCATION]" ; 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ CreateQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent , quotaPreference ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreference 
public void CreateQuotaPreference2ResourceNames () 
{ 
// Snippet: CreateQuotaPreference(LocationName, QuotaPreference, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ); 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ CreateQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent , quotaPreference ); 
// End snippet 
} 

/// Snippet for CreateQuotaPreferenceAsync 
public async Task CreateQuotaPreference2ResourceNamesAsync () 
{ 
// Snippet: CreateQuotaPreferenceAsync(LocationName, QuotaPreference, CallSettings) 
// Additional: CreateQuotaPreferenceAsync(LocationName, QuotaPreference, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [ LocationName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) . [ FromProjectLocation ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_) ( "[PROJECT]" , "[LOCATION]" ); 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ CreateQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_) ( parent , quotaPreference ); 
// End snippet 
} 

/// Snippet for UpdateQuotaPreference 
public void UpdateQuotaPreferenceRequestObject () 
{ 
// Snippet: UpdateQuotaPreference(UpdateQuotaPreferenceRequest, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ UpdateQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest.html) request = new [ UpdateQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest.html)
{ 
UpdateMask = new [ FieldMask ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) (), 
QuotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (), 
AllowMissing = false , 
ValidateOnly = false , 
IgnoreSafetyChecks = 
{ 
[ QuotaSafetyCheck ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html) . [ Unspecified ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html#Google_Cloud_CloudQuotas_V1_QuotaSafetyCheck_Unspecified) , 
}, 
}; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ UpdateQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_UpdateQuotaPreference_Google_Cloud_CloudQuotas_V1_QuotaPreference_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// End snippet 
} 

/// Snippet for UpdateQuotaPreferenceAsync 
public async Task UpdateQuotaPreferenceRequestObjectAsync () 
{ 
// Snippet: UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest, CallSettings) 
// Additional: UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ UpdateQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest.html) request = new [ UpdateQuotaPreferenceRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest.html)
{ 
UpdateMask = new [ FieldMask ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) (), 
QuotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (), 
AllowMissing = false , 
ValidateOnly = false , 
IgnoreSafetyChecks = 
{ 
[ QuotaSafetyCheck ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html) . [ Unspecified ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html#Google_Cloud_CloudQuotas_V1_QuotaSafetyCheck_Unspecified) , 
}, 
}; 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ UpdateQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_UpdateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_QuotaPreference_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_) ( request ); 
// End snippet 
} 

/// Snippet for UpdateQuotaPreference 
public void UpdateQuotaPreference () 
{ 
// Snippet: UpdateQuotaPreference(QuotaPreference, FieldMask, CallSettings) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create) (); 
// Initialize request argument(s) 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
[ FieldMask ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) updateMask = new [ FieldMask ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) (); 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient . [ UpdateQuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_UpdateQuotaPreference_Google_Cloud_CloudQuotas_V1_QuotaPreference_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_) ( quotaPreference , updateMask ); 
// End snippet 
} 

/// Snippet for UpdateQuotaPreferenceAsync 
public async Task UpdateQuotaPreferenceAsync () 
{ 
// Snippet: UpdateQuotaPreferenceAsync(QuotaPreference, FieldMask, CallSettings) 
// Additional: UpdateQuotaPreferenceAsync(QuotaPreference, FieldMask, CancellationToken) 
// Create client 
[ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [ CloudQuotasClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_) (); 
// Initialize request argument(s) 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) (); 
[ FieldMask ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) updateMask = new [ FieldMask ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) (); 
// Make the request 
[ QuotaPreference ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient . [ UpdateQuotaPreferenceAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_UpdateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_QuotaPreference_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_) ( quotaPreference , updateMask ); 
// End snippet 
} 
} 
} 
```


































































```
// Copyright 2026 Google LLC 
// 
// Licensed under the Apache License, Version 2.0 (the "License"); 
// you may not use this file except in compliance with the License. 
// You may obtain a copy of the License at 
// 
// https://www.apache.org/licenses/LICENSE-2.0 
// 
// Unless required by applicable law or agreed to in writing, software 
// distributed under the License is distributed on an "AS IS" BASIS, 
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and 
// limitations under the License. 

// Code generated by protoc-gen-go_gapic. DO NOT EDIT. 

package cloudquotas_test 

import ( 
"context" 

cloudquotas "cloud.google.com/go/cloudquotas/apiv1" 
cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb" 
"google.golang.org/api/iterator" 
) 

func ExampleNewClient () { 
ctx := context . Background () 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in: 
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options 
c , err := cloudquotas . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
// TODO: Handle error. 
} 
defer c . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_Close) () 

// TODO: Use client. 
_ = c 
} 

func ExampleNewRESTClient () { 
ctx := context . Background () 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in: 
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options 
c , err := cloudquotas . [ NewRESTClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewRESTClient) ( ctx ) 
if err != nil { 
// TODO: Handle error. 
} 
defer c . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_Close) () 

// TODO: Use client. 
_ = c 
} 

func ExampleClient_CreateQuotaPreference () { 
ctx := context . Background () 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in: 
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options 
c , err := cloudquotas . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
// TODO: Handle error. 
} 
defer c . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_Close) () 

req := & cloudquotaspb . CreateQuotaPreferenceRequest { 
// TODO: Fill request struct fields. 
// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#CreateQuotaPreferenceRequest. 
} 
resp , err := c . CreateQuotaPreference ( ctx , req ) 
if err != nil { 
// TODO: Handle error. 
} 
// TODO: Use resp. 
_ = resp 
} 

func ExampleClient_GetQuotaInfo () { 
ctx := context . Background () 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in: 
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options 
c , err := cloudquotas . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
// TODO: Handle error. 
} 
defer c . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_Close) () 

req := & cloudquotaspb . GetQuotaInfoRequest { 
// TODO: Fill request struct fields. 
// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#GetQuotaInfoRequest. 
} 
resp , err := c . GetQuotaInfo ( ctx , req ) 
if err != nil { 
// TODO: Handle error. 
} 
// TODO: Use resp. 
_ = resp 
} 

func ExampleClient_GetQuotaPreference () { 
ctx := context . Background () 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in: 
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options 
c , err := cloudquotas . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
// TODO: Handle error. 
} 
defer c . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_Close) () 

req := & cloudquotaspb . GetQuotaPreferenceRequest { 
// TODO: Fill request struct fields. 
// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#GetQuotaPreferenceRequest. 
} 
resp , err := c . GetQuotaPreference ( ctx , req ) 
if err != nil { 
// TODO: Handle error. 
} 
// TODO: Use resp. 
_ = resp 
} 

func ExampleClient_ListQuotaInfos () { 
ctx := context . Background () 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in: 
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options 
c , err := cloudquotas . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
// TODO: Handle error. 
} 
defer c . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_Close) () 

req := & cloudquotaspb . ListQuotaInfosRequest { 
// TODO: Fill request struct fields. 
// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#ListQuotaInfosRequest. 
} 
it := c . ListQuotaInfos ( ctx , req ) 
for { 
resp , err := it . Next () 
if err == iterator . Done { 
break 
} 
if err != nil { 
// TODO: Handle error. 
} 
// TODO: Use resp. 
_ = resp 

// If you need to access the underlying RPC response, 
// you can do so by casting the `Response` as below. 
// Otherwise, remove this line. Only populated after 
// first call to Next(). Not safe for concurrent access. 
_ = it . Response .( * cloudquotaspb . ListQuotaInfosResponse ) 
} 
} 

func ExampleClient_ListQuotaPreferences () { 
ctx := context . Background () 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in: 
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options 
c , err := cloudquotas . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
// TODO: Handle error. 
} 
defer c . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_Close) () 

req := & cloudquotaspb . ListQuotaPreferencesRequest { 
// TODO: Fill request struct fields. 
// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#ListQuotaPreferencesRequest. 
} 
it := c . ListQuotaPreferences ( ctx , req ) 
for { 
resp , err := it . Next () 
if err == iterator . Done { 
break 
} 
if err != nil { 
// TODO: Handle error. 
} 
// TODO: Use resp. 
_ = resp 

// If you need to access the underlying RPC response, 
// you can do so by casting the `Response` as below. 
// Otherwise, remove this line. Only populated after 
// first call to Next(). Not safe for concurrent access. 
_ = it . Response .( * cloudquotaspb . ListQuotaPreferencesResponse ) 
} 
} 

func ExampleClient_UpdateQuotaPreference () { 
ctx := context . Background () 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in: 
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options 
c , err := cloudquotas . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
// TODO: Handle error. 
} 
defer c . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_Close) () 

req := & cloudquotaspb . UpdateQuotaPreferenceRequest { 
// TODO: Fill request struct fields. 
// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#UpdateQuotaPreferenceRequest. 
} 
resp , err := c . UpdateQuotaPreference ( ctx , req ) 
if err != nil { 
// TODO: Handle error. 
} 
// TODO: Use resp. 
_ = resp 
} 
```



































































```
/* 
* Copyright 2026 Google LLC 
* 
* Licensed under the Apache License, Version 2.0 (the "License"); 
* you may not use this file except in compliance with the License. 
* You may obtain a copy of the License at 
* 
* https://www.apache.org/licenses/LICENSE-2.0 
* 
* Unless required by applicable law or agreed to in writing, software 
* distributed under the License is distributed on an "AS IS" BASIS, 
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
* See the License for the specific language governing permissions and 
* limitations under the License. 
*/ 

package com.google.api.cloudquotas.v1.samples ; 

import com.google.api.cloudquotas.v1.[CloudQuotasClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasClient.html) ; 
import com.google.api.cloudquotas.v1.[GetQuotaInfoRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaInfoRequest.html) ; 
import com.google.api.cloudquotas.v1.[QuotaInfo](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfo.html) ; 
import com.google.api.cloudquotas.v1.[QuotaInfoName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfoName.html) ; 

public class SyncGetQuotaInfo { 

public static void main ( String [] args ) throws Exception { 
syncGetQuotaInfo (); 
} 

public static void syncGetQuotaInfo () throws Exception { 
// This snippet has been automatically generated and should be regarded as a code template only. 
// It will require modifications to work: 
// - It may require correct/in-range values for request initialization. 
// - It may require specifying regional endpoints when creating the service client as shown in 
// https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library 
try ( [ CloudQuotasClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasClient.html) cloudQuotasClient = [ CloudQuotasClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasClient.html) . create ()) { 
[ GetQuotaInfoRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaInfoRequest.html) request = 
[ GetQuotaInfoRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaInfoRequest.html) . newBuilder () 
. setName ( 
[ QuotaInfoName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfoName.html) . [ ofProjectLocationServiceQuotaInfoName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfoName.html#com_google_api_cloudquotas_v1_QuotaInfoName_ofProjectLocationServiceQuotaInfoName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_) ( 
"[PROJECT]" , "[LOCATION]" , "[SERVICE]" , "[QUOTA_INFO]" ) 
. toString ()) 
. build (); 
[ QuotaInfo ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfo.html) response = cloudQuotasClient . getQuotaInfo ( request ); 
} 
} 
} 
```



































































```
// Copyright 2026 Google LLC 
// 
// Licensed under the Apache License, Version 2.0 (the "License"); 
// you may not use this file except in compliance with the License. 
// You may obtain a copy of the License at 
// 
// https://www.apache.org/licenses/LICENSE-2.0 
// 
// Unless required by applicable law or agreed to in writing, software 
// distributed under the License is distributed on an "AS IS" BASIS, 
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and 
// limitations under the License. 
// 
// ** This file is automatically generated by gapic-generator-typescript. ** 
// ** https://github.com/googleapis/gapic-generator-typescript ** 
// ** All changes to this file may be overwritten. ** 

'use strict' ; 

function main ( name ) { 
/** 
* This snippet has been automatically generated and should be regarded as a code template only. 
* It will require modifications to work. 
* It may require correct/in-range values for request initialization. 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
/** 
* Required. The resource name of the quota info. 
* An example name: 
* `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion` 
*/ 
// const name = 'abc123' 

// Imports the Cloudquotas library 
const { CloudQuotasClient } = require ( '[@google-cloud/cloudquotas](https://berlin.devsitetest.how/nodejs/docs/reference/cloudquotas/latest/overview.html)' ). v1 ; 

// Instantiates a client 
const cloudquotasClient = new [ CloudQuotasClient ](https://berlin.devsitetest.how/nodejs/docs/reference/cloudquotas/latest/overview.html) (); 

async function callGetQuotaInfo () { 
// Construct request 
const request = { 
name , 
}; 

// Run request 
const response = await cloudquotasClient . getQuotaInfo ( request ); 
console . log ( response ); 
} 

callGetQuotaInfo (); 
} 

process . on ( 'unhandledRejection' , err = > { 
console . error ( err . message ); 
process . exitCode = 1 ; 
}); 
main (... process . argv . slice ( 2 )); 
```


































































```
?php 
/* 
* Copyright 2023 Google LLC 
* 
* Licensed under the Apache License, Version 2.0 (the "License"); 
* you may not use this file except in compliance with the License. 
* You may obtain a copy of the License at 
* 
* https://www.apache.org/licenses/LICENSE-2.0 
* 
* Unless required by applicable law or agreed to in writing, software 
* distributed under the License is distributed on an "AS IS" BASIS, 
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
* See the License for the specific language governing permissions and 
* limitations under the License. 
*/ 

/* 
* GENERATED CODE WARNING 
* This file was automatically generated - do not edit! 
*/ 

require_once __DIR__ . '/../../../vendor/autoload.php'; 

use Google\ApiCore\ApiException; 
use Google\Cloud\CloudQuotas\V1\Client\CloudQuotasClient; 
use Google\Cloud\CloudQuotas\V1\GetQuotaInfoRequest; 
use Google\Cloud\CloudQuotas\V1\QuotaInfo; 

/** 
* Retrieve the QuotaInfo of a quota for a project, folder or organization. 
* 
* @param string $formattedName The resource name of the quota info. 
* 
* An example name: 
* `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion` 
* Please see {@see CloudQuotasClient::quotaInfoName()} for help formatting this field. 
*/ 
function get_quota_info_sample(string $formattedName): void 
{ 
// Create a client. 
$cloudQuotasClient = new CloudQuotasClient(); 

// Prepare the request message. 
$request = (new GetQuotaInfoRequest()) 
->setName($formattedName); 

// Call the API and handle any network failures. 
try { 
/** @var QuotaInfo $response */ 
$response = $cloudQuotasClient->getQuotaInfo($request); 
printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString()); 
} catch (ApiException $ex) { 
printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage()); 
} 
} 

/** 
* Helper to execute the sample. 
* 
* This sample has been automatically generated and should be regarded as a code 
* template only. It will require modifications to work: 
* - It may require correct/in-range values for request initialization. 
* - It may require specifying regional endpoints when creating the service client, 
* please see the apiEndpoint client configuration option for more details. 
*/ 
function callSample(): void 
{ 
$formattedName = CloudQuotasClient::quotaInfoName( 
'[PROJECT]', 
'[LOCATION]', 
'[SERVICE]', 
'[QUOTA_INFO]' 
); 

get_quota_info_sample($formattedName); 
} 
```



































































```
# -*- coding: utf-8 -*- 
# Copyright 2026 Google LLC 
# 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
# http://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License. 
# 
# Generated code. DO NOT EDIT! 
# 
# Snippet for GetQuotaInfo 
# NOTE: This snippet has been automatically generated for illustrative purposes only. 
# It may require modifications to work in your environment. 

# To install the latest published package dependency, execute the following: 
# python3 -m pip install google-cloud-quotas 

# This snippet has been automatically generated and should be regarded as a 
# code template only. 
# It will require modifications to work: 
# - It may require correct/in-range values for request initialization. 
# - It may require specifying regional endpoints when creating the service 
# client as shown in: 
# https://googleapis.dev/python/google-api-core/latest/client_options.html 
from google.cloud import [ cloudquotas_v1 ](https://berlin.devsitetest.how/python/docs/reference/google-cloud-cloudquotas/latest)

def sample_get_quota_info (): 
# Create a client 
client = [ cloudquotas_v1 ](https://berlin.devsitetest.how/python/docs/reference/google-cloud-cloudquotas/latest) . [ CloudQuotasClient ](https://berlin.devsitetest.how/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html) () 

# Initialize request argument(s) 
request = [ cloudquotas_v1 ](https://berlin.devsitetest.how/python/docs/reference/google-cloud-cloudquotas/latest) . [ GetQuotaInfoRequest ](https://berlin.devsitetest.how/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.GetQuotaInfoRequest.html) ( 
name = "name_value" , 
) 

# Make the request 
response = client . [ get_quota_info ](https://berlin.devsitetest.how/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html#google_cloud_cloudquotas_v1_services_cloud_quotas_CloudQuotasClient_get_quota_info) ( request = request ) 

# Handle the response 
print ( response ) 
```



































































```
# frozen_string_literal: true 

# Copyright 2024 Google LLC 
# 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
# https://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License. 

# Auto-generated by gapic-generator-ruby. DO NOT EDIT! 

require "google/cloud/cloud_quotas/v1" 

## 
# Snippet for the get_quota_info call in the CloudQuotas service 
# 
# This snippet has been automatically generated and should be regarded as a code 
# template only. It will require modifications to work: 
# - It may require correct/in-range values for request initialization. 
# - It may require specifying regional endpoints when creating the service 
# client as shown in https://cloud.google.com/ruby/docs/reference. 
# 
# This is an auto-generated example demonstrating basic usage of 
# Google::Cloud::CloudQuotas::V1::CloudQuotas::Client#get_quota_info. 
# 
def get_quota_info 
# Create a client object. The client can be reused for multiple calls. 
client = Google :: Cloud :: CloudQuotas :: V1 :: CloudQuotas :: Client . new 

# Create a request. To set request fields, pass in keyword arguments. 
request = Google :: Cloud :: CloudQuotas :: V1 :: GetQuotaInfoRequest . new 

# Call the get_quota_info method. 
result = client . get_quota_info request 

# The returned object is of type Google::Cloud::CloudQuotas::V1::QuotaInfo. 
p result 
end 
```



























## Additional resources















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 










The following list contains links to more resources related to the
client library for C++:

- [API reference](/cpp/docs/reference/cloudquotas/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues) 

- [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D%5Bc%2B%2B%5D) 

- [Source code](https://github.com/googleapis/google-cloud-cpp) 






































The following list contains links to more resources related to the
client library for C#:

- [API reference](/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues) 

- [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bc%23%5D) 

- [Source code](https://github.com/googleapis/google-cloud-dotnet) 





































The following list contains links to more resources related to the
client library for Go:

- [API reference](/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-go/issues) 

- [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bgo%5D) 

- [Source code](https://github.com/googleapis/google-cloud-go) 







































The following list contains links to more resources related to the
client library for Java:

- [API reference](/java/docs/reference/google-cloud-cloudquotas/latest/overview) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-java/issues) 

- [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bjava%5D) 

- [Source code](https://github.com/googleapis/google-cloud-java) 







































The following list contains links to more resources related to the
client library for Node.js:

- [API reference](/nodejs/docs/reference/cloudquotas/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-node/issues) 

- [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bnode.js%5D) 

- [Source code](https://github.com/GoogleCloudPlatform/google-cloud-node) 






































The following list contains links to more resources related to the
client library for PHP:

- [API reference](/php/docs/reference/cloud-quotas/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-php/issues) 

- [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bphp%5D) 

- [Source code](https://github.com/googleapis/google-cloud-php) 







































The following list contains links to more resources related to the
client library for Python:

- [API reference](/python/docs/reference/google-cloud-cloudquotas/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-python/issues) 

- [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bpython%5D) 

- [Source code](https://github.com/googleapis/google-cloud-python) 







































The following list contains links to more resources related to the
client library for Ruby:

- [API reference](/ruby/docs/reference/google-cloud-cloud_quotas/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues) 

- [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bruby%5D) 

- [Source code](https://github.com/googleapis/google-cloud-ruby)