# Authenticate with client libraries

Source: https://berlin.devsitetest.how/docs/authentication/external/externally-sourced-credentials
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/authentication/tpc-differences) for more details.














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

Application development

](https://berlin.devsitetest.how/docs/application-development)






- 








[

Google Cloud SDK

](https://berlin.devsitetest.how/sdk/docs)






- 








[

Authentication

](https://berlin.devsitetest.how/docs/authentication)






- 








[

Guides

](https://berlin.devsitetest.how/sdk/docs/overview)












# Authenticate with client libraries 






- On this page 
- [ Use Application Default Credentials with client libraries ](#adc)

- [ Example client creation ](#example)

- [ Use API keys with client libraries ](#use_api_keys_with_client_libraries)
- 









This page describes how you can use client libraries to access Google APIs.

Client libraries make it easier to access [Google Cloud Dedicated in Germany APIs](/apis/docs/overview)
using a supported language. You can use Google Cloud Dedicated in Germany APIs directly by
making raw requests to the server, but client libraries provide simplifications
that significantly reduce the amount of code you need to write. This is
especially true for authentication, because the client libraries support
[Application Default Credentials (ADC)](/docs/authentication/application-default-credentials).

If you accept credential configurations (JSON, files, or streams) from an
external source (for example, a customer), review the
[security requirements when using credential configurations from an external source](#external-credentials).

## Use Application Default Credentials with client libraries

To use Application Default Credentials to authenticate your application, you
must first [set up ADC](/docs/authentication/provide-credentials-adc) for the
environment where your application is running. When you use the client
library to create a client, the client library automatically checks for and
uses the credentials you have provided to ADC to authenticate to the APIs
your code uses. Your application does not need to explicitly authenticate
or manage tokens; these requirements are managed automatically by the
authentication libraries.

For a local development environment, you can set up ADC
[with your user credentials](/docs/authentication/set-up-adc-local-dev-environment) or
[with service account impersonation](/docs/authentication/use-service-account-impersonation#adc)
by using the gcloud CLI. For production environments,
you set up ADC by [attaching a service account](/docs/authentication/set-up-adc-attached-service-account).

### Example client creation

The following code samples create a client for the Cloud Storage service.
Your code is likely to need different clients; these samples are meant only to
show how you can create a client and use it without any code to explicitly
authenticate.

Before you can run the following samples, you must complete the following steps:


- 
[
Set up ADC for your environment](/docs/authentication/provide-credentials-adc)


- 
[
Install the Cloud Storage client library](/storage/docs/reference/libraries)



- 
Set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable to
`apis-berlin-build0.goog`.


[ Go ](#go) [ Java ](#java) [ Node. js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 

























```
import ( 
"context" 
"fmt" 
"io" 

"cloud.google.com/go/storage" 
"google.golang.org/api/iterator" 
) 

// authenticateImplicitWithAdc uses Application Default Credentials 
// to automatically find credentials and authenticate. 
func authenticateImplicitWithAdc ( w io . [ Writer ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer) , projectId string ) error { 
// projectId := "your_project_id" 

ctx := context . Background () 

// NOTE: Replace the client created below with the client required for your application. 
// Note that the credentials are not specified when constructing the client. 
// The client library finds your credentials using ADC. 
client , err := storage . NewClient ( ctx ) 
if err != nil { 
return fmt . Errorf ( "NewClient: %w" , err ) 
} 
defer client . Close () 

it := client . [ Buckets ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Buckets) ( ctx , projectId ) 
for { 
bucketAttrs , err := it . Next () 
if err == iterator . Done { 
break 
} 
if err != nil { 
return err 
} 
fmt . Fprintf ( w , "Bucket: %v\n" , bucketAttrs . Name ) 
} 

fmt . Fprintf ( w , "Listed all storage buckets.\n" ) 

return nil 
} 
```



























```
import com.google.api.gax.paging.[Page](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) ; 
import com.google.cloud.storage.[Bucket](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) ; 
import com.google.cloud.storage.[Storage](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) ; 
import com.google.cloud.storage.[StorageOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) ; 
import java.io.IOException ; 

public class AuthenticateImplicitWithAdc { 

public static void main ( String [] args ) throws IOException { 
// TODO(Developer): 
// 1. Before running this sample, 
// set up Application Default Credentials as described in 
// https://cloud.google.com/docs/authentication/external/set-up-adc 
// 2. Replace the project variable below. 
// 3. Make sure you have the necessary permission to list storage buckets 
// "storage.buckets.list" 
String projectId = "your-google-cloud-project-id" ; 
authenticateImplicitWithAdc ( projectId ); 
} 

// When interacting with Google Cloud Client libraries, the library can auto-detect the 
// credentials to use. 
public static void authenticateImplicitWithAdc ( String project ) throws IOException { 

// *NOTE*: Replace the client created below with the client required for your application. 
// Note that the credentials are not specified when constructing the client. 
// Hence, the client library will look for credentials using ADC. 
// 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
[ Storage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [ StorageOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) . newBuilder (). setProjectId ( project ). build (). [ getService ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__) (); 

System . out . println ( "Buckets:" ); 
Page buckets = storage . [ list ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_list_com_google_cloud_storage_Storage_BucketListOption____) (); 
for ( [ Bucket ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket : buckets . iterateAll ()) { 
System . out . println ( bucket . toString ()); 
} 
System . out . println ( "Listed all storage buckets." ); 
} 
} 
```



























```
/** 
* TODO(developer): 
* 1. Uncomment and replace these variables before running the sample. 
* 2. Set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc 
* 3. Make sure you have the necessary permission to list storage buckets "storage.buckets.list" 
* (https://cloud.google.com/storage/docs/access-control/iam-permissions#bucket_permissions) 
*/ 
// const projectId = 'YOUR_PROJECT_ID'; 

const { Storage } = require ( '[@google-cloud/storage](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/overview.html)' ); 

async function authenticateImplicitWithAdc () { 
// This snippet demonstrates how to list buckets. 
// NOTE: Replace the client created below with the client required for your application. 
// Note that the credentials are not specified when constructing the client. 
// The client library finds your credentials using ADC. 
const storage = new [ Storage ](https://berlin.devsitetest.how/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html) ({ 
projectId , 
}); 
const [ buckets ] = await storage . [ getBuckets ](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/storage/storage_2.html) (); 
console . log ( 'Buckets:' ); 

for ( const bucket of buckets ) { 
console . log ( `- ${ bucket . name } ` ); 
} 

console . log ( 'Listed all storage buckets.' ); 
} 

authenticateImplicitWithAdc (); 
```



























```
// Imports the Cloud Storage client library. 
use Google\Cloud\Storage\StorageClient; 

/** 
* Authenticate to a cloud client library using a service account implicitly. 
* 
* @param string $projectId The Google project ID. 
*/ 
function auth_cloud_implicit($projectId) 
{ 
$config = [ 
'projectId' => $projectId, 
]; 

# If you don't specify credentials when constructing the client, the 
# client library will look for credentials in the environment. 
$storage = new StorageClient($config); 

# Make an authenticated API request (listing storage buckets) 
foreach ($storage->buckets() as $bucket) { 
printf('Bucket: %s' . PHP_EOL, $bucket->name()); 
} 
} 
```



























```
from google.cloud import [ storage ](https://berlin.devsitetest.how/python/docs/reference/storage/latest)

def authenticate_implicit_with_adc ( project_id : str = "your-google-cloud-project-id" ) - > None : 
""" 
When interacting with Google Cloud Client libraries, the library can auto-detect the 
credentials to use. 

// TODO(Developer): 
// 1. Before running this sample, 
// set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc 
// 2. Replace the project variable. 
// 3. Make sure that the user account or service account that you are using 
// has the required permissions. For this sample, you must have "storage.buckets.list". 
Args: 
project_id: The project id of your Google Cloud project. 
""" 

# This snippet demonstrates how to list buckets. 
# *NOTE*: Replace the client created below with the client required for your application. 
# Note that the credentials are not specified when constructing the client. 
# Hence, the client library will look for credentials using ADC. 
storage_client = [ storage ](https://berlin.devsitetest.how/python/docs/reference/storage/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html) ( project = project_id ) 
buckets = storage_client . [ list_buckets ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_buckets) () 
print ( "Buckets:" ) 
for bucket in buckets : 
print ( bucket . name ) 
print ( "Listed all storage buckets." ) 
```



























```
def authenticate_implicit_with_adc project_id : 
# The ID of your Google Cloud project 
# project_id = "your-google-cloud-project-id" 

### 
# When interacting with Google Cloud Client libraries, the library can auto-detect the 
# credentials to use. 
# TODO(Developer): 
# 1. Before running this sample, 
# set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc 
# 2. Replace the project variable. 
# 3. Make sure that the user account or service account that you are using 
# has the required permissions. For this sample, you must have "storage.buckets.list". 
### 

require "google/cloud/storage" 

# This sample demonstrates how to list buckets. 
# *NOTE*: Replace the client created below with the client required for your application. 
# Note that the credentials are not specified when constructing the client. 
# Hence, the client library will look for credentials using ADC. 
storage = Google :: Cloud :: [ Storage ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html) project_id : project_id 
buckets = storage . buckets 
puts "Buckets: " 
buckets . [ each ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do | bucket | 
puts bucket . name 
end 
puts "Plaintext: Listed all storage buckets." 
end 
```






## Use API keys with client libraries

You can use an API keys only with client libraries for APIs that accept API
keys. In addition, the API key must not have an API restriction that prevents it
from being used for the API.

For more information about API keys created in express mode, see the
[Google Cloud express mode FAQ](https://berlin.devsitetest.how/resources/cloud-express-faqs).