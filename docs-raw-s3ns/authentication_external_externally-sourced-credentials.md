# Authenticate with client libraries

Source: https://documentation.s3ns.fr/docs/authentication/external/externally-sourced-credentials
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/authentication/tpc-differences) for more details.














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

Developer tools

](https://documentation.s3ns.fr/docs/costs-usage)






- 








[

Google Cloud SDK

](https://documentation.s3ns.fr/sdk/docs)






- 








[

Authentication

](https://documentation.s3ns.fr/docs/authentication)






- 








[

Guides

](https://documentation.s3ns.fr/sdk/docs/overview)












# Authenticate with client libraries 














This page describes how you can use client libraries to access Google APIs.

Client libraries make it easier to access [Cloud de Confiance by S3NS APIs](/apis/docs/overview)
using a supported language. You can use Cloud de Confiance by S3NS APIs directly by
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
`s3nsapis.fr`.



### Go






















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
func authenticateImplicitWithAdc ( w io . [ Writer ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer) , projectId string ) error { 
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

it := client . [ Buckets ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Buckets) ( ctx , projectId ) 
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





### Java






















```
import com.google.api.gax.paging.[Page](https://documentation.s3ns.fr/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) ; 
import com.google.cloud.storage.[Bucket](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) ; 
import com.google.cloud.storage.[Storage](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) ; 
import com.google.cloud.storage.[StorageOptions](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) ; 
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
[ Storage ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [ StorageOptions ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) . newBuilder (). setProjectId ( project ). build (). [ getService ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__) (); 

System . out . println ( "Buckets:" ); 
Page buckets = storage . [ list ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_list_com_google_cloud_storage_Storage_BucketListOption____) (); 
for ( [ Bucket ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket : buckets . iterateAll ()) { 
System . out . println ( bucket . toString ()); 
} 
System . out . println ( "Listed all storage buckets." ); 
} 
} 
```





### Node.js






















```
/** 
* TODO(developer): 
* 1. Uncomment and replace these variables before running the sample. 
* 2. Set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc 
* 3. Make sure you have the necessary permission to list storage buckets "storage.buckets.list" 
* (https://cloud.google.com/storage/docs/access-control/iam-permissions#bucket_permissions) 
*/ 
// const projectId = 'YOUR_PROJECT_ID'; 

const { Storage } = require ( '[@google-cloud/storage](https://documentation.s3ns.fr/nodejs/docs/reference/storage/latest/overview.html)' ); 

async function authenticateImplicitWithAdc () { 
// This snippet demonstrates how to list buckets. 
// NOTE: Replace the client created below with the client required for your application. 
// Note that the credentials are not specified when constructing the client. 
// The client library finds your credentials using ADC. 
const storage = new [ Storage ](https://documentation.s3ns.fr/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html) ({ 
projectId , 
}); 
const [ buckets ] = await storage . [ getBuckets ](https://documentation.s3ns.fr/nodejs/docs/reference/storage/latest/storage/storage_2.html) (); 
console . log ( 'Buckets:' ); 

for ( const bucket of buckets ) { 
console . log ( `- ${ bucket . name } ` ); 
} 

console . log ( 'Listed all storage buckets.' ); 
} 

authenticateImplicitWithAdc (); 
```





### PHP






















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





### Python






















```
from google.cloud import [ storage ](https://documentation.s3ns.fr/python/docs/reference/storage/latest)

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
storage_client = [ storage ](https://documentation.s3ns.fr/python/docs/reference/storage/latest) . [ Client ](https://documentation.s3ns.fr/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html) ( project = project_id ) 
buckets = storage_client . [ list_buckets ](https://documentation.s3ns.fr/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_buckets) () 
print ( "Buckets:" ) 
for bucket in buckets : 
print ( bucket . name ) 
print ( "Listed all storage buckets." ) 
```





### Ruby






















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
storage = Google :: Cloud :: [ Storage ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html) . [ new ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html) project_id : project_id 
buckets = storage . buckets 
puts "Buckets: " 
buckets . [ each ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do | bucket | 
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
[Google Cloud express mode FAQ](https://documentation.s3ns.fr/resources/cloud-express-faqs).




When you use API keys in your applications, ensure that they are kept secure
during both storage and transmission. Publicly exposing your API keys can
lead to unexpected charges on your account. For more information, see
[Best practices for managing API keys](/docs/authentication/api-keys-best-practices).

## Security requirements when using credential configurations from an external source

Typically, you generate credential configurations by using gcloud CLI
commands or by using the Cloud de Confiance console. For example, you can use the
gcloud CLI to generate a local ADC file or a login configuration
file. Similarly, you can use the Cloud de Confiance console to create and download
a service account key.

For some use cases, however, credential configurations are provided to you by an
external entity; these credential configurations are intended to be used to
authenticate to Google APIs.

Some types of credential configurations include endpoints and file paths, which
the authentication libraries use to acquire a token. When you accept credential
configurations from an external source, you must validate the configuration
before using it. If you don't validate the configuration, a malicious actor
could use the credential to compromise your systems and data.

### Validate credential configurations from external sources

How you need to validate your external credentials depends on what types of
credential your application accepts.

#### Validate service account keys

If your application accepts *only* service account keys, use a credential
loader specific to service account keys, as shown in the following examples. The
type-specific credential loader parses only the fields present for service
account keys, which don't expose any vulnerabilities.



### C#

```
var saCredential = CredentialFactory . FromStream ( stream ); 
```


### C++

```
auto cred = google :: cloud :: MakeServiceAccountCredentials ( json ) 
```


### Java

```
ServiceAccountCredentials credentials = 
ServiceAccountCredentials . fromStream ( credentialsStream ); 
```


### Node.js

```
const keys = JSON . parse ( json_input ) 
const authClient = JWT . fromJSON ( keys ); 
```


### PHP

```
$cred = new Google\Auth\Credentials\ServiceAccountCredentials($scope, $jsonKey); 
```


### Python

```
cred = service_account . Credentials . from_service_account_info ( json_data ) 
```


### Ruby

```
creds = Google :: Auth :: [ ServiceAccountCredentials ](https://documentation.s3ns.fr/ruby/docs/reference/googleauth/latest/Google-Auth-ServiceAccountCredentials.html) . [ make_creds ](https://documentation.s3ns.fr/ruby/docs/reference/googleauth/latest/Google-Auth-ServiceAccountCredentials.html) ( json_key_io : json_stream ) 
```



If you can't use a type-specific credential loader, validate the credential by
confirming that the value for the `type` field is `service_account`. If the
value for the `type` field is any other value, don't use the service account
key.

#### Validate other credential configurations

If your application accepts *any* type of credential besides a service account
key, you must perform additional verification. Examples of other types of
credential configurations include
[ADC credential files](/docs/authentication/application-default-credentials#personal),
[Workload Identity Federation credential files](/iam/docs/workload-identity-federation-with-other-clouds#create-cred-config),
or [Workforce Identity Federation login configuration files](/iam/docs/workforce-obtaining-short-lived-credentials#create-login-config).

The following table lists the fields you need to validate, if they are present
in your credentials. Not all of these fields are present for all credential
configurations.



| 
Field | 
Purpose | 
Expected value | 
|

| 
`service_account_impersonation_url` | 

The authentication libraries use this field to access an endpoint to
generate an access token for the service account being impersonated.
| 
`https://iamcredentials.s3nsapis.fr/v1/projects/-/serviceAccounts/ service account email :generateAccessToken` | 
|

| 
`token_url` | 

The authentication libraries send an external token to this endpoint to
exchange it for a
[federated access token](/docs/authentication/token-types#fed-access-tokens).
| 
`https://sts.s3nsapis.fr/v1/token` | 
|

| 
`credential_source.file` | 

The authentication libraries read an external token from the file at the
location specified by this field and send it to the
`token_url` endpoint.
| 

The path for a file containing an external token. You should
recognize this path.
| 
|

| 
`credential_source.url` | 

An endpoint that returns an external token. The authentication libraries
send a request to this URL and send the response to the
`token_url` endpoint.
| 



One of the following items:




- A well-known endpoint provided by your cloud provider.

- An endpoint that you have explicitly set up to provide tokens.


| 
|

| 
`credential_source.executable.command` | 

If the `GOOGLE_EXTERNAL_ACCOUNT_ALLOW_EXECUTABLES`
environment variable is set to `1`, the authentication
libraries run this command or executable file.
| 

An executable file or command that returns an external token.
You should recognize this command and validate that it is safe.
| 
|

| 
`credential_source.aws.url` | 

The authentication libraries issue a request to this URL to retrieve
an AWS security token.
| 



Either one of these exact values:




- 
`http://169.254.169.254/latest/meta-data/iam/security-credentials`


- 
`http://[fd00:ec2::254]/latest/meta-data/iam/security-credentials`



| 
|

| 
`credential_source.aws.region_url` | 

The authentication libraries issue a request to this URL to retrieve
the active AWS region.
| 



Either one of these exact values:




- 
`http://169.254.169.254/latest/meta-data/placement/availability-zone`


- 
`http://[fd00:ec2::254]/latest/meta-data/placement/availability-zone`



| 
|

| 
`credential_source.aws.imdsv2_session_token_url` | 

The authentication libraries issue a request to this URL to retrieve
the AWS session token.
| 



Either one of these exact values:




- 
`http://169.254.169.254/latest/api/token`


- 
`http://[fd00:ec2::254]/latest/api/token`



| 
|


## What's next

- Learn more about [Application Default Credentials](/docs/authentication/application-default-credentials).

- Learn more about [API keys](/docs/authentication/api-keys).

- See an overview of [Authentication methods](/docs/authentication).