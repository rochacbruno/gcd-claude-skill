# Secret Manager client libraries

Source: https://berlin.devsitetest.how/secret-manager/docs/reference/libraries
Last updated: 2026-10-22

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/secret-manager/docs/tpc-differences) for more details.














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

Secret Manager

](https://berlin.devsitetest.how/secret-manager/docs)






- 








[

Reference

](https://berlin.devsitetest.how/secret-manager/docs/apis)












# Secret Manager client libraries 

















This page shows how to get started with the Cloud Client Libraries for the
Secret Manager API. Client libraries make it easier to access
Google Cloud Dedicated in Germany APIs from a supported language. Although you can use
Google Cloud Dedicated in Germany APIs directly by making raw requests to the server, client
libraries provide simplifications that significantly reduce the amount of code
you need to write.

Read more about the Cloud Client Libraries
and the older Google API Client Libraries in
[Client libraries explained](/apis/docs/client-libraries-explained).



## Install the client library


















### C++ 






See [Setting up a C++ development environment](/cpp/docs/setup)
for details about this client library's requirements and install dependencies.


































### C# 






Using PowerShell:


```
$ Install-Package Google.Cloud.SecretManager.V1 -Version 2.5.0
```


Using the dotnet CLI:


```
$ dotnet add package Google.Cloud.SecretManager.V1 --version 2.5.0
```






For more information, see [Setting Up a C# Development Environment](/dotnet/docs/setup).


































### Go 






```
$ go get cloud.google.com/go/secretmanager/apiv1
$ go get google.golang.org/genproto/googleapis/cloud/secretmanager/v1
```






For more information, see [Setting Up a Go Development Environment](/go/docs/setup).



































### Java 






If you are using [Maven](https://maven.apache.org/), add
the following to your `pom.xml` file. For more information about
BOMs, see [The Google Cloud Platform Libraries BOM](https://berlin.devsitetest.how/java/docs/bom).
























```
dependencyManagement >
dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>libraries - bom / artifactId >
version>26 .90.0 / version >
type>pom / type >
scope>import / scope >
/ dependency >
/ dependencies >
/ dependencyManagement >

dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>google - cloud - secretmanager / artifactId >
/ dependency >
/ dependencies >
```



If you are using [Gradle](https://gradle.org/),
add the following to your dependencies:
























```
implementation platform ( ' com . google . cloud : libraries - bom : 26.90.0 ' ) 

implementation ' com . google . cloud : google - cloud - secretmanager ' 
```



If you are using [sbt](https://www.scala-sbt.org/), add
the following to your dependencies:






















```
libraryDependencies += "com.google.cloud" % "google-cloud-secretmanager" % "2.99.0" 
```



If you're using Visual Studio Code or IntelliJ, you can add client libraries to your
project using the following IDE plugins:


- [Cloud Code for VS Code](/code/docs/vscode/client-libraries)

- [Cloud Code for IntelliJ](/code/docs/intellij/client-libraries)

The plugins provide additional functionality, such as key management for service accounts. Refer
to each plugin's documentation for details.





For more information, see [Setting Up a Java Development Environment](/java/docs/setup).



































### Node.js 






```
$ npm install @google-cloud/secret-manager
```






For more information, see [Setting Up a Node.js Development Environment](/nodejs/docs/setup).


































### PHP 






```
$ composer require google/cloud-secret-manager
```






For more information, see [Using PHP on Google Cloud](/php/docs).



































### Python 






```
$ pip install google-cloud-secret-manager
```






For more information, see [Setting Up a Python Development Environment](/python/docs/setup).



































### Ruby 






```
$ gem install google-cloud-secret_manager
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






If an authentication error is returned, confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








A sign-in screen appears. After you sign in, your credentials are stored in the
[
local credential file used by ADC](/docs/authentication/application-default-credentials#personal).















## Use the client library

The following example shows how to use the client library.




















### C++ 





























```
#include "google/cloud/secretmanager/v1/secret_manager_client.h" 
#include 

int main ( int argc , char * argv []) try { 
if ( argc != 2 ) { 
std :: cerr "Usage: " argv [ 0 ] " project-id \n " ; 
return 1 ; 
} 

namespace secretmanager = :: google :: cloud :: secretmanager_v1 ; 
auto client = secretmanager :: SecretManagerServiceClient ( 
secretmanager :: MakeSecretManagerServiceConnection ()); 

auto const parent = std :: string ( "projects/" ) + argv [ 1 ]; 
for ( auto secret : client . ListSecrets ( parent )) { 
if ( ! secret ) throw std :: move ( secret ). status (); 
std :: cout secret - > DebugString () " \n " ; 
} 

return 0 ; 
} catch ( google :: cloud :: Status const & status ) { 
std :: cerr "google::cloud::Status thrown: " status " \n " ; 
return 1 ; 
} 
```







































### C# 




























```
using System ; 
using System.Text ; 
using [ Google.Api.Gax.ResourceNames ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html) ; 
using [ Google.Cloud.SecretManager.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html) ; 
using [ Google.Protobuf ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html) ; 

public class QuickstartSample 
{ 
public void Quickstart ( string projectId = "my-project" , string secretId = "my-secret" ) 
{ 
// Create the client. 
[ SecretManagerServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [ SecretManagerServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create) (); 

// Build the parent project name. 
[ ProjectName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) projectName = new [ ProjectName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) ( projectId ); 

// Build the secret to create. 
Secret secret = new Secret 
{ 
Replication = new [ Replication ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Replication.html)
{ 
Automatic = new Replication . Types . Automatic (), 
}, 
}; 

Secret createdSecret = client . [ CreateSecret ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_CreateSecret_Google_Api_Gax_ResourceNames_LocationName_System_String_Google_Cloud_SecretManager_V1_Secret_Google_Api_Gax_Grpc_CallSettings_) ( projectName , secretId , secret ); 

// Build a payload. 
[ SecretPayload ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html) payload = new [ SecretPayload ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html)
{ 
Data = [ ByteString ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html) . [ CopyFrom ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___) ( "my super secret data" , Encoding . UTF8 ), 
}; 

// Add a secret version. 
[ SecretVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersion.html) createdVersion = client . [ AddSecretVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_AddSecretVersion_Google_Cloud_SecretManager_V1_AddSecretVersionRequest_Google_Api_Gax_Grpc_CallSettings_) ( createdSecret . [ SecretName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret.html#Google_Cloud_SecretManager_V1_Secret_SecretName) , payload ); 

// Access the secret version. 
[ AccessSecretVersionResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.AccessSecretVersionResponse.html) result = client . [ AccessSecretVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_AccessSecretVersion_Google_Cloud_SecretManager_V1_AccessSecretVersionRequest_Google_Api_Gax_Grpc_CallSettings_) ( createdVersion . [ SecretVersionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersion.html#Google_Cloud_SecretManager_V1_SecretVersion_SecretVersionName) ); 

// Print the results 
// 
// WARNING: Do not print secrets in production environments. This 
// snippet is for demonstration purposes only. 
string data = result . [ Payload ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.AccessSecretVersionResponse.html#Google_Cloud_SecretManager_V1_AccessSecretVersionResponse_Payload) . [ Data ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html#Google_Cloud_SecretManager_V1_SecretPayload_Data) . [ ToStringUtf8 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_ToStringUtf8) (); 
Console . WriteLine ( $"Plaintext: {data}" ); 
} 
} 
```






































### Go 




























```
// Sample quickstart is a basic program that uses Secret Manager. 
package main 

import ( 
"context" 
"fmt" 
"log" 

secretmanager "cloud.google.com/go/secretmanager/apiv1" 
"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb" 
) 

func main () { 
// GCP project in which to store secrets in Secret Manager. 
projectID := "your-project-id" 

// Create the client. 
ctx := context . Background () 
client , err := secretmanager . [ NewClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
log . Fatalf ( "failed to setup client: %v" , err ) 
} 
defer client . [ Close ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close) () 

// Create the request to create the secret. 
createSecretReq := & secretmanagerpb . CreateSecretRequest { 
Parent : fmt . Sprintf ( "projects/%s" , projectID ), 
SecretId : "my-secret" , 
Secret : & secretmanagerpb . Secret { 
Replication : & secretmanagerpb . Replication { 
Replication : & secretmanagerpb . Replication_Automatic_ { 
Automatic : & secretmanagerpb . Replication_Automatic {}, 
}, 
}, 
}, 
} 

secret , err := client . CreateSecret ( ctx , createSecretReq ) 
if err != nil { 
log . Fatalf ( "failed to create secret: %v" , err ) 
} 

// Declare the payload to store. 
payload := [] byte ( "my super secret data" ) 

// Build the request. 
addSecretVersionReq := & secretmanagerpb . AddSecretVersionRequest { 
Parent : secret . Name , 
Payload : & secretmanagerpb . SecretPayload { 
Data : payload , 
}, 
} 

// Call the API. 
version , err := client . AddSecretVersion ( ctx , addSecretVersionReq ) 
if err != nil { 
log . Fatalf ( "failed to add secret version: %v" , err ) 
} 

// Build the request. 
accessRequest := & secretmanagerpb . AccessSecretVersionRequest { 
Name : version . Name , 
} 

// Call the API. 
result , err := client . AccessSecretVersion ( ctx , accessRequest ) 
if err != nil { 
log . Fatalf ( "failed to access secret version: %v" , err ) 
} 

// Print the secret payload. 
// 
// WARNING: Do not print the secret in a production environment - this 
// snippet is showing how to access the secret material. 
log . Printf ( "Plaintext: %s" , result . Payload . Data ) 
} 
```







































### Java 




























```
import com.google.cloud.secretmanager.v1.[AccessSecretVersionResponse](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html) ; 
import com.google.cloud.secretmanager.v1.[ProjectName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html) ; 
import com.google.cloud.secretmanager.v1.[Replication](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html) ; 
import com.google.cloud.secretmanager.v1.[Secret](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) ; 
import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) ; 
import com.google.cloud.secretmanager.v1.[SecretPayload](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) ; 
import com.google.cloud.secretmanager.v1.[SecretVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) ; 
import com.google.protobuf.[ByteString](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) ; 

public class Quickstart { 

public void quickstart () throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String secretId = "your-secret-id" ; 
quickstart ( projectId , secretId ); 
} 

public void quickstart ( String projectId , String secretId ) throws Exception { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the "close" method on the client to safely clean up any remaining background resources. 
try ( [ SecretManagerServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [ SecretManagerServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) . create ()) { 
// Build the parent name from the project. 
[ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html) projectName = [ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html) . of ( projectId ); 

// Create the parent secret. 
[ Secret ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret = 
[ Secret ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) . newBuilder () 
. [ setReplication ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_setReplication_com_google_cloud_secretmanager_v1_Replication_) ( 
[ Replication ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html) . newBuilder () 
. setAutomatic ( [ Replication ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html) . Automatic . newBuilder (). build ()) 
. build ()) 
. build (); 

[ Secret ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createdSecret = client . createSecret ( projectName , secretId , secret ); 

// Add a secret version. 
[ SecretPayload ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) payload = 
[ SecretPayload ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) . newBuilder (). [ setData ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.Builder.html#com_google_cloud_secretmanager_v1_SecretPayload_Builder_setData_com_google_protobuf_ByteString_) ( [ ByteString ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) . [ copyFromUtf8 ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_) ( "hello world!" )). build (); 
[ SecretVersion ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) addedVersion = client . addSecretVersion ( createdSecret . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__) (), payload ); 

// Access the secret version. 
[ AccessSecretVersionResponse ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html) response = client . accessSecretVersion ( addedVersion . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getName__) ()); 

// Print the secret payload. 
// 
// WARNING: Do not print the secret in a production environment - this 
// snippet is showing how to access the secret material. 
String data = response . [ getPayload ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html#com_google_cloud_secretmanager_v1_AccessSecretVersionResponse_getPayload__) (). getData (). toStringUtf8 (); 
System . out . printf ( "Plaintext: %s\n" , data ); 
} 
} 
} 
```







































### Node.js 




























```
// Import the Secret Manager client and instantiate it: 
const { SecretManagerServiceClient } = require ( '[@google-cloud/secret-manager](https://berlin.devsitetest.how/nodejs/docs/reference/secret-manager/latest/overview.html)' ); 
const client = new [ SecretManagerServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/secret-manager/latest/overview.html) (); 

/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// parent = 'projects/my-project', // Project for which to manage secrets. 
// secretId = 'foo', // Secret ID. 
// payload = 'hello world!' // String source data. 

async function createAndAccessSecret () { 
// Create the secret with automation replication. 
const [ secret ] = await client . createSecret ({ 
parent : parent , 
secret : { 
name : secretId , 
replication : { 
automatic : {}, 
}, 
}, 
secretId , 
}); 

console . info ( `Created secret ${ secret . name } ` ); 

// Add a version with a payload onto the secret. 
const [ version ] = await client . addSecretVersion ({ 
parent : secret . name , 
payload : { 
data : Buffer . from ( payload , 'utf8' ), 
}, 
}); 

console . info ( `Added secret version ${ version . name } ` ); 

// Access the secret. 
const [ accessResponse ] = await client . accessSecretVersion ({ 
name : version . name , 
}); 

const responsePayload = accessResponse . payload . data . toString ( 'utf8' ); 
console . info ( `Payload: ${ responsePayload } ` ); 
} 
createAndAccessSecret (); 
```






































### PHP 




























```
// Import the Secret Manager client library. 
use Google\Cloud\SecretManager\V1\AccessSecretVersionRequest; 
use Google\Cloud\SecretManager\V1\AddSecretVersionRequest; 
use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient; 
use Google\Cloud\SecretManager\V1\CreateSecretRequest; 
use Google\Cloud\SecretManager\V1\Replication; 
use Google\Cloud\SecretManager\V1\Replication\Automatic; 
use Google\Cloud\SecretManager\V1\Secret; 
use Google\Cloud\SecretManager\V1\SecretPayload; 

/** Uncomment and populate these variables in your code */ 
// $projectId = 'YOUR_GOOGLE_CLOUD_PROJECT' (e.g. 'my-project'); 
// $secretId = 'YOUR_SECRET_ID' (e.g. 'my-secret'); 

// Create the Secret Manager client. 
$client = new SecretManagerServiceClient(); 

// Build the parent name from the project. 
$parent = $client->projectName($projectId); 

// Create the parent secret. 
$createSecretRequest = (new CreateSecretRequest()) 
->setParent($parent) 
->setSecretId($secretId) 
->setSecret(new Secret([ 
'replication' => new Replication([ 
'automatic' => new Automatic(), 
]), 
])); 
$secret = $client->createSecret($createSecretRequest); 

// Add the secret version. 
$addSecretVersionRequest = (new AddSecretVersionRequest()) 
->setParent($secret->getName()) 
->setPayload(new SecretPayload([ 
'data' => 'hello world', 
])); 
$version = $client->addSecretVersion($addSecretVersionRequest); 

// Access the secret version. 
$accessSecretVersionRequest = (new AccessSecretVersionRequest()) 
->setName($version->getName()); 
$response = $client->accessSecretVersion($accessSecretVersionRequest); 

// Print the secret payload. 
// 
// WARNING: Do not print the secret in a production environment - this 
// snippet is showing how to access the secret material. 
$payload = $response->getPayload()->getData(); 
printf('Plaintext: %s' . PHP_EOL, $payload); 
```







































### Python 




























```
# Import the Secret Manager client library. 
from google.cloud import secretmanager 

# GCP project in which to store secrets in Secret Manager. 
project_id = "YOUR_PROJECT_ID" 

# ID of the secret to create. 
secret_id = "YOUR_SECRET_ID" 

# Create the Secret Manager client. 
client = secretmanager . [ SecretManagerServiceClient ](https://berlin.devsitetest.how/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html) () 

# Build the parent name from the project. 
parent = f "projects/ { project_id } " 

# Create the parent secret. 
secret = client . [ create_secret ](https://berlin.devsitetest.how/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_create_secret) ( 
request = { 
"parent" : parent , 
"secret_id" : secret_id , 
"secret" : { "replication" : { "automatic" : {}}}, 
} 
) 

# Add the secret version. 
version = client . [ add_secret_version ](https://berlin.devsitetest.how/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_add_secret_version) ( 
request = { "parent" : secret . name , "payload" : { "data" : b "hello world!" }} 
) 

# Access the secret version. 
response = client . [ access_secret_version ](https://berlin.devsitetest.how/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_access_secret_version) ( request = { "name" : version . name }) 

# Print the secret payload. 
# 
# WARNING: Do not print the secret in a production environment - this 
# snippet is showing how to access the secret material. 
payload = response . payload . data . decode ( "UTF-8" ) 
print ( f "Plaintext: { payload } " ) 
```







































### Ruby 




























```
require "google/cloud/secret_manager" 

## 
# Secret manager quickstart 
# 
# @param project_id [String] Your Google Cloud project (e.g. "my-project") 
# @param secret_id [String] Your secret name (e.g. "my-secret") 
# 
def quickstart project_id :, secret_id : 
# Create the Secret Manager client. 
client = Google :: Cloud :: [ SecretManager ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html) . [ secret_manager_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)

# Build the parent name from the project. 
parent = "projects/ #{ project_id } " 

# Create the parent secret. 
secret = client . create_secret ( 
parent : parent , 
secret_id : secret_id , 
secret : { 
replication : { 
automatic : {} 
} 
} 
) 

# Add a secret version. 
version = client . add_secret_version ( 
parent : secret . name , 
payload : { 
data : "hello world!" 
} 
) 

# Access the secret version. 
response = client . access_secret_version name : version . name 

# Print the secret payload. 
# 
# WARNING: Do not print the secret in a production environment - this 
# snippet is showing how to access the secret material. 
payload = response . payload . data 
puts "Plaintext: #{ payload } " 
end 
```



























## Additional resources


















### C++ 






The following list contains links to more resources related to the
client library for C++:

- [API reference](/cpp/docs/reference/secretmanager/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues) 

- [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D%5Bc%2B%2B%5D) 

- [Source code](https://github.com/googleapis/google-cloud-cpp) 

































### C# 






The following list contains links to more resources related to the
client library for C#:

- [API reference](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.SecretManager.V1/index.html) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues) 

- [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bc%23%5D) 

- [Source code](https://github.com/googleapis/google-cloud-dotnet) 
































### Go 






The following list contains links to more resources related to the
client library for Go:

- [API reference](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-go/issues) 

- [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bgo%5D) 

- [Source code](https://github.com/googleapis/google-cloud-go) 

































### Java 






The following list contains links to more resources related to the
client library for Java:

- [API reference](https://berlin.devsitetest.how/java/docs/reference/google-cloud-secretmanager/latest/overview) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-java/tree/main/java-secretmanager/issues) 

- [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bjava%5D) 

- [Source code](https://github.com/googleapis/google-cloud-java/tree/main/java-secretmanager) 

































### Node.js 






The following list contains links to more resources related to the
client library for Node.js:

- [API reference](https://googleapis.dev/nodejs/secretmanager/latest/index.html) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-secretmanager/issues) 

- [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bnode.js%5D) 

- [Source code](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-secretmanager) 
































### PHP 






The following list contains links to more resources related to the
client library for PHP:

- [API reference](https://googleapis.github.io/google-cloud-php/#/docs/cloud-secret-manager) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-php-secret-manager/issues) 

- [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bphp%5D) 

- [Source code](https://github.com/googleapis/google-cloud-php-secret-manager) 

































### Python 






The following list contains links to more resources related to the
client library for Python:

- [API reference](/python/docs/reference/secretmanager/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-secret-manager/issues) 

- [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bpython%5D) 

- [Source code](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-secret-manager) 

































### Ruby 






The following list contains links to more resources related to the
client library for Ruby:

- [API reference](https://googleapis.dev/ruby/google-cloud-secret_manager/latest/index.html) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues) 

- [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bruby%5D) 

- [Source code](https://github.com/googleapis/google-cloud-ruby)