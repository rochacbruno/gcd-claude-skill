# Create a secret

Source: https://documentation.s3ns.fr/secret-manager/docs/creating-and-accessing-secrets
Last updated: 2026-10-22

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












# Create a secret 















This page describes how to create a secret. A secret contains one or more secret versions, along
with metadata such as labels and replication policies. The actual contents of a secret are stored
in a [secret version](/secret-manager/docs/add-secret-version).

## Before you begin


- 



[Enable the Secret Manager API](/secret-manager/docs/configuring-secret-manager).




- 


[Access regional secrets in your environment](/secret-manager/regional-secrets/config-sm-rs).



- 


Set up authentication.



















Select the tab for how you plan to use the samples on this page:













### Console




When you use the Cloud de Confiance console to access Cloud de Confiance by S3NS services and
APIs, you don't need to set up authentication.












### gcloud




















[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).

After signing in,
[initialize](/sdk/docs/initializing) the Google Cloud CLI by running the following command:





```
gcloud init
```






























































### REST






To use the REST API samples on this page in a local development environment, you use the
credentials you provide to the gcloud CLI.










[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


















For more information, see
[Authenticate for using REST](/docs/authentication/rest)
in the Cloud de Confiance authentication documentation.





















## Required roles


































To get the permissions that
you need to create a secret,

ask your administrator to grant you the
[Secret Manager Admin ](/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) IAM role on the project, folder, or organization.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









## Create a secret

You can create secrets using the Cloud de Confiance console, the Google Cloud CLI, the Secret Manager API, or the
Secret Manager client libraries.
















### Console







- 


In the Cloud de Confiance console, go to the **Secret Manager** page.



[Go to Secret Manager](https://console.cloud.s3nscloud.fr/security/secret-manager)



- 



On the **Secret Manager** page, click **Create secret**.




- 



On the **Create secret** page, enter a name for the secret in the **Name** field.
A secret name can contain uppercase and lowercase letters, numerals, hyphens, and underscores. The maximum allowed length for a name is 255 characters.




- 


(Optional) ([Preview](https://documentation.s3ns.fr/products/#product-launch-stages)) Select the **Secret type**. You can use secret types to
categorize your secrets.




The available global secret types are:




- **Other DB credentials**: For secrets that contain database
credentials.

- **Access key**: For secrets that contain an access key.

- **Certificate**: For secrets that contain a certificate.

- **Other**: For secrets that do not fit into other categories.






- 


Enter a value for the secret (for example, `abcd1234`). The secret value can be in any format
but must not be larger than 64 KiB. You can also upload a text file that contain the secret value using
the **Upload file** option. This action automatically creates the secret version.




- 


Click **Create secret**.































### gcloud 






Before using any of the command data below,
make the following replacements:


- SECRET_ID : the ID of the secret.


- REPLICATION_POLICY : the replication policy for the secret, which can be either automatic or user-managed.



Execute the

following

command:



#### Linux, macOS, or Cloud Shell




```
gcloud secrets create SECRET_ID \ 
--replication-policy = " REPLICATION_POLICY " 
```





#### Windows (PowerShell)




```
gcloud secrets create SECRET_ID ` 
--replication-policy = " REPLICATION_POLICY " 
```





#### Windows (cmd.exe)





```
gcloud secrets create SECRET_ID ^
--replication-policy = " REPLICATION_POLICY " 
```





























### REST





















Before using any of the request data,
make the following replacements:



- PROJECT_ID : the Cloud de Confiance by S3NS project ID.

- SECRET_ID : the ID of the secret.


- REPLICATION_POLICY : the replication policy for the secret, which can be either automatic or user-managed.


HTTP method and URL:



```
POST https://secretmanager.googleapis.com/v1/projects/ PROJECT_ID /secrets?secretId= SECRET_ID 
```



Request JSON body:



```
{
"replication": {
" REPLICATION_POLICY ": {}
}
}
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
"https://secretmanager.googleapis.com/v1/projects/ PROJECT_ID /secrets?secretId= SECRET_ID "
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
-Uri "https://secretmanager.googleapis.com/v1/projects/ PROJECT_ID /secrets?secretId= SECRET_ID " | Select-Object -Expand Content
```







You should receive a JSON response similar to the following:






```
{
"name": "projects/ PROJECT_ID /secrets/ SECRET_ID ",
"createTime": "2024-03-25T08:24:13.153705Z",
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
using [ Google.Api.Gax.ResourceNames ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html) ; 
using [ Google.Cloud.SecretManager.V1 ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html) ; 

public class CreateSecretSample 
{ 
public Secret CreateSecret ( 
string projectId = "my-project" , string secretId = "my-secret" ) 
{ 
// Create the client. 
[ SecretManagerServiceClient ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [ SecretManagerServiceClient ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) . [ Create ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create) (); 

// Build the parent resource name. 
[ ProjectName ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) projectName = new [ ProjectName ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) ( projectId ); 

// Build the secret. 
Secret secret = new Secret 
{ 
Replication = new [ Replication ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Replication.html)
{ 
Automatic = new Replication . Types . Automatic (), 
}, 
}; 

// Call the API. 
Secret createdSecret = client . [ CreateSecret ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_CreateSecret_Google_Api_Gax_ResourceNames_LocationName_System_String_Google_Cloud_SecretManager_V1_Secret_Google_Api_Gax_Grpc_CallSettings_) ( projectName , secretId , secret ); 
return createdSecret ; 
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
"io" 
"time" 

secretmanager "cloud.google.com/go/secretmanager/apiv1" 
"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb" 
"google.golang.org/protobuf/types/known/durationpb" 
) 

// createSecretWithTTL creates a new secret with the given name and ttl. 
func createSecretWithTTL ( w io . Writer , parent , id string , d time . Duration ) error { 
// parent := "projects/my-project" 
// id := "my-secret" 

expiration := & secretmanagerpb . Secret_Ttl { Ttl : durationpb . New ( d )} 

// Create the client. 
ctx := context . Background () 
client , err := secretmanager . [ NewClient ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create secretmanager client: %w" , err ) 
} 
defer client . [ Close ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close) () 

// Build the request. 
req := & secretmanagerpb . CreateSecretRequest { 
Parent : parent , 
SecretId : id , 
Secret : & secretmanagerpb . Secret { 
Replication : & secretmanagerpb . Replication { 
Replication : & secretmanagerpb . Replication_Automatic_ { 
Automatic : & secretmanagerpb . Replication_Automatic {}, 
}, 
}, 
Expiration : expiration , 
}, 
} 

// Call the API. 
result , err := client . CreateSecret ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to create secret: %w" , err ) 
} 
fmt . Fprintf ( w , "Created secret with ttl: %s\n" , result . Name ) 
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
import com.google.cloud.secretmanager.v1.[ProjectName](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html) ; 
import com.google.cloud.secretmanager.v1.[Replication](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html) ; 
import com.google.cloud.secretmanager.v1.[Secret](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) ; 
import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) ; 
import com.google.protobuf.[Duration](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) ; 
import java.io.IOException ; 

public class CreateSecret { 

public static void createSecret () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String secretId = "your-secret-id" ; 
createSecret ( projectId , secretId ); 
} 

// Create a new secret with automatic replication. 
public static void createSecret ( String projectId , String secretId ) throws IOException { 
// Initialize the client that will be used to send requests. This client only needs to be 
// created once, and can be reused for multiple requests. After completing all of your requests, 
// call the "close" method on the client to safely clean up any remaining background resources. 
try ( [ SecretManagerServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [ SecretManagerServiceClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) . create ()) { 
// Build the parent name from the project. 
[ ProjectName ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html) projectName = [ ProjectName ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html) . of ( projectId ); 

// Optionally set a TTL for the secret. This demonstrates how to configure 
// a secret to be automatically deleted after a certain period. The TTL is 
// specified in seconds (e.g., 900 for 15 minutes). This can be useful 
// for managing sensitive data and reducing storage costs. 
[ Duration ](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) ttl = [ Duration ](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) . newBuilder (). setSeconds ( 900 ). build (); 

// Build the secret to create. 
[ Secret ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret = 
[ Secret ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) . newBuilder () 
. [ setReplication ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_setReplication_com_google_cloud_secretmanager_v1_Replication_) ( 
[ Replication ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html) . newBuilder () 
. setAutomatic ( [ Replication ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html) . Automatic . newBuilder (). build ()) 
. build ()) 
. [ setTtl ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_setTtl_com_google_protobuf_Duration_) ( ttl ) 
. build (); 

// Create the secret. 
[ Secret ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createdSecret = client . createSecret ( projectName , secretId , secret ); 
System . out . printf ( "Created secret %s\n" , createdSecret . [ getName ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__) ()); 
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
// const parent = 'projects/my-project'; 
// const secretId = 'my-secret'; 
// const ttl = undefined // Optional: Specify TTL in seconds (e.g., '900s' for 15 minutes). 

// Imports the Secret Manager library 
const { SecretManagerServiceClient } = require ( '[@google-cloud/secret-manager](https://documentation.s3ns.fr/nodejs/docs/reference/secret-manager/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ SecretManagerServiceClient ](https://documentation.s3ns.fr/nodejs/docs/reference/secret-manager/latest/overview.html) (); 

async function createSecret () { 
const secretConfig = { 
replication : { 
automatic : {}, 
}, 
}; 

// Add TTL to the secret configuration if provided 
if ( ttl ) { 
secretConfig . ttl = { 
seconds : parseInt ( ttl . replace ( 's' , '' ), 10 ), 
}; 
console . log ( `Secret TTL set to ${ ttl } ` ); 
} 

const [ secret ] = await client . createSecret ({ 
parent : parent , 
secretId : secretId , 
secret : secretConfig , 
}); 

console . log ( `Created secret ${ secret . name } ` ); 
} 

createSecret (); 
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
use Google\Cloud\SecretManager\V1\CreateSecretRequest; 
use Google\Cloud\SecretManager\V1\Replication; 
use Google\Cloud\SecretManager\V1\Replication\Automatic; 
use Google\Cloud\SecretManager\V1\Secret; 
use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient; 

/** 
* @param string $projectId Your Google Cloud Project ID (e.g. 'my-project') 
* @param string $secretId Your secret ID (e.g. 'my-secret') 
*/ 
function create_secret(string $projectId, string $secretId): void 
{ 
// Create the Secret Manager client. 
$client = new SecretManagerServiceClient(); 

// Build the resource name of the parent project. 
$parent = $client->projectName($projectId); 

$secret = new Secret([ 
'replication' => new Replication([ 
'automatic' => new Automatic(), 
]), 
]); 

// Build the request. 
$request = CreateSecretRequest::build($parent, $secretId, $secret); 

// Create the secret. 
$newSecret = $client->createSecret($request); 

// Print the new secret name. 
printf('Created secret: %s', $newSecret->getName()); 
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
# Import the Secret Manager client library. 
from google.cloud import secretmanager 

def create_secret ( 
project_id : str , secret_id : str , ttl : Optional [ str ] = None 
) - > secretmanager . Secret : 
""" 
Create a new secret with the given name. A secret is a logical wrapper 
around a collection of secret versions. Secret versions hold the actual 
secret material. 

Args: 
project_id (str): The project ID where the secret is to be created. 
secret_id (str): The ID to assign to the new secret. This ID must be unique within the project. 
ttl (Optional[str]): An optional string that specifies the secret's time-to-live in seconds with 
format (e.g., "900s" for 15 minutes). If specified, the secret 
versions will be automatically deleted upon reaching the end of the TTL period. 

Returns: 
secretmanager.Secret: An object representing the newly created secret, containing details like the 
secret's name, replication settings, and optionally its TTL. 

Example: 
# Create a secret with automatic replication and no TTL 
new_secret = create_secret("my-project", "my-new-secret") 

# Create a secret with a TTL of 30 days 
new_secret_with_ttl = create_secret("my-project", "my-timed-secret", "7776000s") 
""" 

# Create the Secret Manager client. 
client = secretmanager . [ SecretManagerServiceClient ](https://documentation.s3ns.fr/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html) () 

# Build the resource name of the parent project. 
parent = f "projects/ { project_id } " 

# Create the secret. 
response = client . [ create_secret ](https://documentation.s3ns.fr/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_create_secret) ( 
request = { 
"parent" : parent , 
"secret_id" : secret_id , 
"secret" : { "replication" : { "automatic" : {}}, "ttl" : ttl }, 
} 
) 

# Print the new secret name. 
print ( f "Created secret: { response . name } " ) 
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
client = Google :: Cloud :: [ SecretManager ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-secret_manager-v1beta1/latest/Google-Cloud-SecretManager.html) . [ secret_manager_service ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)

# Build the resource name of the parent project. 
parent = client . project_path project : project_id 

# Create the secret. 
secret = client . create_secret ( 
parent : parent , 
secret_id : secret_id , 
secret : { 
replication : { 
automatic : {} 
} 
} 
) 

# Print the new secret name. 
puts "Created secret: #{ secret . name } " 
```






















## Add a secret version

Secret Manager automatically versions secret data using secret versions. Key operations, such
as access, destroy, disable, and enable, are applied to specific secret versions. With Secret Manager, you
can associate secrets with specific versions such as `42` or with dynamic aliases
such as `latest`. To learn more, see [Add a secret version](/secret-manager/docs/add-secret-version).

## Access a secret version

To access the secret data from a particular secret version for successful authentication, see
[Access a secret version](/secret-manager/docs/access-secret-version).

## What's next

- Check the [quotas and rate limits](/secret-manager/quotas) for different types of API requests (access, read, and write) per project.

- Learn how to [manage access to secrets](/secret-manager/docs/manage-access-to-secrets).

- Learn how to [set up notifications on a secret](/secret-manager/docs/event-notifications).