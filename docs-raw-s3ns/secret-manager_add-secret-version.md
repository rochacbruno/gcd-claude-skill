# Add a secret version

Source: https://documentation.s3ns.fr/secret-manager/docs/add-secret-version
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/secret-manager/docs/tpc-differences) for more details.














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

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Secret Manager

](https://documentation.s3ns.fr/secret-manager/docs)






- 








[

Guides

](https://documentation.s3ns.fr/secret-manager/docs/overview)












# Add a secret version 















Secret data is immutable and most operations take place on secret versions. A
secret version contains the actual secret data, along with [state](/secret-manager/docs/add-secret-version#states) and
metadata about the secret. This page describes how to add a secret version.

For more information about versioning, see this [video](https://youtu.be/4iddawLDurw?si=Ph22Et2rgiZJLiMr)
on versioning.

## Required roles







































To get the permissions that
you need to add a secret version,

ask your administrator to grant you the
following IAM roles on a secret:













- [Secret Manager Secret Version Adder ](/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionAdder) (`roles/secretmanager.secretVersionAdder`)


- [Secret Manager Secret Version Manager ](/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)









For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









IAM roles can't be granted on a secret version.

## Add a secret version

To add a secret version, use one of the following methods:
















### Console







- 


In the Cloud de Confiance console, go to the **Secret Manager** page.



[Go to Secret Manager](https://console.cloud.s3nscloud.fr/security/secret-manager)



- 



On the **Secret Manager** page, locate the secret for which you want
to add the new version.




- 


Click the more_vert **Actions**
menu associated with that secret, and then click **Add new version**. The
**Add new version** dialog appears.



- 


In the **Secret value** field, enter a value for the secret such as `abcd1234`.
Alternatively, you can upload a file containing the secret value.



- 


Click **Add new version**.































### gcloud 








#### Add a secret version from the contents of a file on disk





Before using any of the command data below,
make the following replacements:


- SECRET_ID : the ID of the secret


- FILE_PATH : the full path (including file name) to the file containing the version details


Execute the

following

command:



#### Linux, macOS, or Cloud Shell




```
gcloud secrets versions add SECRET_ID --data-file = " FILE_PATH " 
```





#### Windows (PowerShell)




```
gcloud secrets versions add SECRET_ID --data-file = " FILE_PATH " 
```





#### Windows (cmd.exe)





```
gcloud secrets versions add SECRET_ID --data-file = " FILE_PATH " 
```





The response contains the newly created secret version.




#### Add a secret version directly on the command line



You can also add a secret version directly on the command line, but this is discouraged because *it appears as plaintext* in the list of processes and may be captured by other system users. Note that the command with the plaintext will also be in your shell history.





```
echo -n " SECRET_DATA " | \
gcloud secrets versions add SECRET_ID --data-file=-
```





Replace the following:



- SECRET_DATA : the data that you want to store in the secret version

- SECRET_ID : the ID of the secret or fully qualified identifier for the secret








#### Optional: Add a version from a file's contents when first creating a secret





Before using any of the command data below,
make the following replacements:


- SECRET_ID : the ID of the secret


- FILE_PATH : the full path (including file name) to the file containing the version details


Execute the

following

command:



#### Linux, macOS, or Cloud Shell




```
gcloud secrets create SECRET_ID --data-file = " FILE_PATH " 
```





#### Windows (PowerShell)




```
gcloud secrets create SECRET_ID --data-file = " FILE_PATH " 
```





#### Windows (cmd.exe)





```
gcloud secrets create SECRET_ID --data-file = " FILE_PATH " 
```





The response contains the newly created secret version.





























### REST






Base64-encode the secret data and save it as a shell variable.


```
$ SECRET_DATA=$(echo "seCr3t" | base64)
```

















Before using any of the request data,
make the following replacements:



- PROJECT_ID : the Cloud de Confiance by S3NS project ID

- SECRET_ID : the ID of the secret

HTTP method and URL:



```
POST https://secretmanager.googleapis.com/v1/projects/ PROJECT_ID /secrets/ SECRET_ID :addVersion
```



Request JSON body:



```
{"payload": {"data": "${SECRET_DATA}"}}
```



To send your request, choose one of these options:




#### curl











Save the request body in a file named `request.json`,
and execute the following command:






































```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
"https://secretmanager.googleapis.com/v1/projects/ PROJECT_ID /secrets/ SECRET_ID :addVersion"
```





#### PowerShell











Save the request body in a file named `request.json`,
and execute the following command:
























































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method POST `
-Headers $headers `
-ContentType: "application/json; charset=utf-8" `
-InFile request.json `
-Uri "https://secretmanager.googleapis.com/v1/projects/ PROJECT_ID /secrets/ SECRET_ID :addVersion" | Select-Object -Expand Content
```







You should receive a JSON response similar to the following:






```
{
"name": "projects/ PROJECT_ID /locations/ LOCATION /secrets/ SECRET_ID /versions/1",
"createTime": "2024-03-25T08:24:13.153705Z",
"state": "ENABLED",
"etag": "\"161477e6071da9\""
}
```





































### C# 





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.

To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Secret Manager C# SDK](/secret-manager/docs/reference/libraries#client-libraries-install-csharp). 
On Compute Engine or GKE, you must
[authenticate with the cloud-platform scope](/secret-manager/docs/accessing-the-api#oauth-scopes).



























```
using System.Text ; 
using [ Google.Cloud.SecretManager.V1 ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html) ; 
using [ Google.Protobuf ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html) ; 

public class AddSecretVersionSample 
{ 
public SecretVersion AddSecretVersion ( 
string projectId = "my-project" , string secretId = "my-secret" , 
string data = "my secret data" ) 
{ 
// Create the client. 
[ SecretManagerServiceClient ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [ SecretManagerServiceClient ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) . [ Create ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create) (); 

// Build the resource name. 
[ SecretName ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html) secretName = new [ SecretName ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html) ( projectId , secretId ); 

// Convert the payload to bytes. 
[ SecretPayload ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html) payload = new [ SecretPayload ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html)
{ 
Data = [ ByteString ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html) . [ CopyFrom ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___) ( data , Encoding . UTF8 ), 
}; 

// Call the API. 
[ SecretVersion ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersion.html) version = client . [ AddSecretVersion ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_AddSecretVersion_Google_Cloud_SecretManager_V1_AddSecretVersionRequest_Google_Api_Gax_Grpc_CallSettings_) ( secretName , payload ); 
return version ; 
} 
} 
```




































### Go 





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.

To run this code, first [set up a Go development environment](/go/docs/setup) and
[install the Secret Manager Go SDK](/secret-manager/docs/reference/libraries#client-libraries-install-go). 
On Compute Engine or GKE, you must
[authenticate with the cloud-platform scope](/secret-manager/docs/accessing-the-api#oauth-scopes).



























```
import ( 
"context" 
"fmt" 
"hash/crc32" 
"io" 

secretmanager "cloud.google.com/go/secretmanager/apiv1" 
"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb" 
) 

// addSecretVersion adds a new secret version to the given secret with the 
// provided payload. 
func addSecretVersion ( w io . Writer , parent string ) error { 
// parent := "projects/my-project/secrets/my-secret" 

// Declare the payload to store. 
payload := [] byte ( "my super secret data" ) 
// Compute checksum, use Castagnoli polynomial. Providing a checksum 
// is optional. 
crc32c := crc32 . MakeTable ( crc32 . Castagnoli ) 
checksum := int64 ( crc32 . Checksum ( payload , crc32c )) 

// Create the client. 
ctx := context . Background () 
client , err := secretmanager . [ NewClient ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create secretmanager client: %w" , err ) 
} 
defer client . [ Close ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close) () 

// Build the request. 
req := & secretmanagerpb . AddSecretVersionRequest { 
Parent : parent , 
Payload : & secretmanagerpb . SecretPayload { 
Data : payload , 
DataCrc32C : & checksum , 
}, 
} 

// Call the API. 
result , err := client . AddSecretVersion ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to add secret version: %w" , err ) 
} 
fmt . Fprintf ( w , "Added secret version: %s\n" , result . Name ) 
return nil 
} 
```





































### Java 





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.

To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Secret Manager Java SDK](/secret-manager/docs/reference/libraries#client-libraries-install-java). 
On Compute Engine or GKE, you must
[authenticate with the cloud-platform scope](/secret-manager/docs/accessing-the-api#oauth-scopes).



























```
import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) ; 
import com.google.cloud.secretmanager.v1.[SecretName](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) ; 
import com.google.cloud.secretmanager.v1.[SecretPayload](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) ; 
import com.google.cloud.secretmanager.v1.[SecretVersion](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) ; 
import com.google.protobuf.[ByteString](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) ; 
import java.io.IOException ; 
import java.util.zip.CRC32C ; 
import java.util.zip.Checksum ; 

public class AddSecretVersion { 

public static void addSecretVersion () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String secretId = "your-secret-id" ; 
addSecretVersion ( projectId , secretId ); 
} 

// Add a new version to the existing secret. 
public static void addSecretVersion ( String projectId , String secretId ) throws IOException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the "close" method on the client to safely clean up any remaining background resources. 
try ( [ SecretManagerServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [ SecretManagerServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) . create ()) { 
[ SecretName ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = [ SecretName ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) . of ( projectId , secretId ); 
byte [] data = "my super secret data" . getBytes (); 
// Calculate data checksum. The library is available in Java 9+. 
// If using Java 8, the following library may be used: 
// https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/files/Crc32c 
Checksum checksum = new CRC32C (); 
checksum . update ( data , 0 , data . length ); 

// Create the secret payload. 
[ SecretPayload ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) payload = 
[ SecretPayload ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) . newBuilder () 
. [ setData ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.Builder.html#com_google_cloud_secretmanager_v1_SecretPayload_Builder_setData_com_google_protobuf_ByteString_) ( [ ByteString ](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) . [ copyFrom ](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___) ( data )) 
// Providing data checksum is optional. 
. [ setDataCrc32C ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.Builder.html#com_google_cloud_secretmanager_v1_SecretPayload_Builder_setDataCrc32C_long_) ( checksum . getValue ()) 
. build (); 

// Add the secret version. 
[ SecretVersion ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) version = client . addSecretVersion ( secretName , payload ); 
System . out . printf ( "Added secret version %s\n" , version . [ getName ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getName__) ()); 
} 
} 
} 
```





































### Node.js 





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.

To run this code, first [set up a Node.js development environment](/nodejs/docs/setup) and
[install the Secret Manager Node.js SDK](/secret-manager/docs/reference/libraries#client-libraries-install-nodejs). 
On Compute Engine or GKE, you must
[authenticate with the cloud-platform scope](/secret-manager/docs/accessing-the-api#oauth-scopes).



























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const parent = 'projects/my-project/secrets/my-secret'; 

// Imports the Secret Manager library 
const { SecretManagerServiceClient } = require ( '[@google-cloud/secret-manager](https://documentation.s3ns.fr/nodejs/docs/reference/secret-manager/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ SecretManagerServiceClient ](https://documentation.s3ns.fr/nodejs/docs/reference/secret-manager/latest/overview.html) (); 

// Payload is the plaintext data to store in the secret 
const payload = Buffer . from ( 'my super secret data' , 'utf8' ); 

async function addSecretVersion () { 
const [ version ] = await client . addSecretVersion ({ 
parent : parent , 
payload : { 
data : payload , 
}, 
}); 

console . log ( `Added secret version ${ version . name } ` ); 
} 

addSecretVersion (); 
```




































### PHP 





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.

To run this code, first learn about [using PHP on Google Cloud](/php/docs) and
[install the Secret Manager PHP SDK](/secret-manager/docs/reference/libraries#client-libraries-install-php). 
On Compute Engine or GKE, you must
[authenticate with the cloud-platform scope](/secret-manager/docs/accessing-the-api#oauth-scopes).



























```
// Import the Secret Manager client library. 
use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient; 
use Google\Cloud\SecretManager\V1\AddSecretVersionRequest; 
use Google\Cloud\SecretManager\V1\SecretPayload; 

/** 
* @param string $projectId Your Google Cloud Project ID (e.g. 'my-project') 
* @param string $secretId Your secret ID (e.g. 'my-secret') 
*/ 
function add_secret_version(string $projectId, string $secretId): void 
{ 
// Create the Secret Manager client. 
$client = new SecretManagerServiceClient(); 

// Build the resource name of the parent secret and the payload. 
$parent = $client->secretName($projectId, $secretId); 
$secretPayload = new SecretPayload([ 
'data' => 'my super secret data', 
]); 

// Build the request. 
$request = AddSecretVersionRequest::build($parent, $secretPayload); 

// Access the secret version. 
$response = $client->addSecretVersion($request); 

// Print the new secret version name. 
printf('Added secret version: %s', $response->getName()); 
} 
```





































### Python 





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.

To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Secret Manager Python SDK](/secret-manager/docs/reference/libraries#client-libraries-install-python). 
On Compute Engine or GKE, you must
[authenticate with the cloud-platform scope](/secret-manager/docs/accessing-the-api#oauth-scopes).



























```
from google.cloud import secretmanager 
import google_crc32c # type: ignore 

def add_secret_version ( 
project_id : str , secret_id : str , payload : str 
) - > secretmanager . SecretVersion : 
""" 
Add a new secret version to the given secret with the provided payload. 
""" 

# Create the Secret Manager client. 
client = secretmanager . [ SecretManagerServiceClient ](https://documentation.s3ns.fr/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html) () 

# Build the resource name of the parent secret. 
parent = client . [ secret_path ](https://documentation.s3ns.fr/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_secret_path) ( project_id , secret_id ) 

# Convert the string payload into a bytes. This step can be omitted if you 
# pass in bytes instead of a str for the payload argument. 
payload_bytes = payload . encode ( "UTF-8" ) 

# Calculate payload checksum. Passing a checksum in add-version request 
# is optional. 
crc32c = google_crc32c . Checksum () 
crc32c . update ( payload_bytes ) 

# Add the secret version. 
response = client . [ add_secret_version ](https://documentation.s3ns.fr/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_add_secret_version) ( 
request = { 
"parent" : parent , 
"payload" : { 
"data" : payload_bytes , 
"data_crc32c" : int ( crc32c . hexdigest (), 16 ), 
}, 
} 
) 

# Print the new secret version name. 
print ( f "Added secret version: { response . name } " ) 
```





































### Ruby 





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.

To run this code, first [set up a Ruby development environment](/ruby/docs/setup) and
[install the Secret Manager Ruby SDK](/secret-manager/docs/reference/libraries#client-libraries-install-ruby). 
On Compute Engine or GKE, you must
[authenticate with the cloud-platform scope](/secret-manager/docs/accessing-the-api#oauth-scopes).



























```
# project_id = "YOUR-GOOGLE-CLOUD-PROJECT" # (e.g. "my-project") 
# secret_id = "YOUR-SECRET-ID" # (e.g. "my-secret") 

# Require the Secret Manager client library. 
require "google/cloud/secret_manager" 

# Create a Secret Manager client. 
client = Google :: Cloud :: [ SecretManager ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html) . [ secret_manager_service ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)

# Build the resource name of the secret version. 
name = client . secret_path project : project_id , secret : secret_id 

# Add the secret version. 
version = client . add_secret_version ( 
parent : name , 
payload : { 
data : "my super secret data" 
} 
) 

# Print the new secret version name. 
puts "Added secret version: #{ version . name } " 
```






















## Secret version states

A secret version can be in one of the following states at any given time:


- 


**Enabled** - In this state, the secret version can be accessed and described.
This is the default state for a new secret version.



- 


**Disabled** - In this state, the secret version cannot be accessed, but the
secret's contents still exist. The secret version can be
re-enabled to restore access.



- 


**Destroyed** - In this state, the secret version's contents are
discarded. The secret version cannot be changed to another state.



You are billed for both enabled and disabled secret versions. You are
not billed for secret versions that are in the destroyed state.

## What's next

- Learn how to [access a secret version](/secret-manager/docs/access-secret-version).

- Learn how to [assign an alias to a secret version](/secret-manager/docs/assign-alias-to-secret-version).

- Learn how to [list secret versions and view version details](/secret-manager/docs/managing-secret-versions).