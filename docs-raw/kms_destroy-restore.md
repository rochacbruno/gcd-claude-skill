# Destroy and restore key versions

Source: https://berlin.devsitetest.how/kms/docs/destroy-restore
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/kms/docs/tpc-differences) for more details.














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

Cloud KMS

](https://berlin.devsitetest.how/kms/docs)






- 








[

Guides

](https://berlin.devsitetest.how/kms/docs/key-management-service)












# Destroy and restore key versions 






- On this page 
- [ Before you begin ](#before-begin)

- [ Understand the risks ](#understand-risks)
- [ Required roles ](#required-roles)
- [ Check whether the key version is in use ](#pre-destroy-checklist)

- [ Destroy a key version ](#destroy)

- [ Destroying external keys ](#destroy-external)

- [ Restore a key version ](#restore)
- [ Required IAM permissions ](#iam)
- [ Deletion timeline ](#timeline)
- 









This page shows you how to schedule a Cloud Key Management Service key version for permanent
destruction. In Cloud KMS, the cryptographic key material that you use
to encrypt, decrypt, sign, and verify data is stored in a *key version*. A key
has zero or more key versions. When you rotate a key, you create a new key
version.

Destroying a key version means that the key material is permanently deleted.
When you destroy a key version, other details such as the key name and key
version number aren't deleted. After a key is destroyed, data that was encrypted
with the key version can't be decrypted.

The only exception is
[key re-import](/kms/docs/importing-a-key#re-import_a_previously_destroyed_key),
which lets you restore a previously imported key by providing the same original
key material.

Because key destruction is generally irreversible, Cloud KMS doesn't
let you destroy key versions immediately. Instead, you schedule a key version
for destruction. The key version remains in the scheduled for destruction
[state](/kms/docs/key-states) for a configurable time. During the scheduled for destruction duration,
you can restore a key version to cancel its destruction.

The default scheduled for destruction duration is 30 days. You can [set a
custom scheduled for destruction duration for a key during key
creation](/kms/docs/creating-keys#soft_delete). Your organization can enforce
a minimum scheduled for destruction duration by setting the **Minimum destroy
scheduled duration per key** constraint in your organization policies.

You can also manage access to the key using Identity and Access Management (IAM).
IAM operations are consistent within seconds. For more
information, see [Using IAM](/kms/docs/iam).

You can also temporarily [disable a key version](/kms/docs/enable-disable). We
recommend disabling key versions prior to scheduling them for destruction as
part of your procedures for ensuring that the key can be safely destroyed.
Depending on your organization policies, you might be required to disable a key
version before you can schedule it for destruction. For more information about
controlling key version destruction using organization policies, see [Control
key version destruction](/kms/docs/control-key-destruction).

In the rest of this document, scheduling a key for destruction is referred to
as destroying the key, even though destruction is not immediate.

## Before you begin

### Understand the risks

Destroying a key version is a permanent operation. Destroying a key version that
is still needed has risks including the following:

- 

Service outage: If you destroy a key that is required to start a container
or instance, your services or applications can become unavailable.

- 

Permanent data loss: If you destroy a key that was used to encrypt data,
that data becomes unavailable. Data encrypted with a key that has been
destroyed is considered *crypto-shredded*. In some cases, destroying a key
can cause encrypted resources to be permanently deleted.

- 

Regulatory or compliance issues: If you destroy a key that is required to
access data that is subject to a retention period before that retention
period is complete, you might be in violation of a regulatory or compliance
requirement.

### Required roles


































To get the permissions that
you need to destroy and restore key versions,

ask your administrator to grant you the
[Cloud KMS Admin ](/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) IAM role on the key.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









### Check whether the key version is in use

Before you destroy a key version, complete the following steps to see whether
the key version is in use:

- 

[View key usage tracking details](/kms/docs/view-key-usage) for the key.
If any resources are protected by the key version that you want to destroy,
re-encrypt them with another key version.

- 

Turn on logs for any service or application that could be using the key
version.

- 

Turn on logs on the Cloud KMS project that contains the key.

- 

[Disable the key version](/kms/docs/enable-disable). Disabling the key
version prevents the key version from being used. With the
key version disabled, any attempts to use the key version fail.

- 

Monitor the logs until you're sure that no application or service still
relies on the key version that you disabled. If any errors indicate failed
access to the key version, configure the application or resource to use
another key version.

The length of time that you spend monitoring logs before destroying a
key version depends on the type of key, its usage pattern, and its
sensitivity level. For example, before destroying a key version that is used
in a process that runs quarterly, keep the key version disabled until that
process completes successfully.

- 

Check the usage of the key against any applicable compliance requirements.
For example, the key version and data encrypted with it may be subject to
data retention periods.

These steps help you to identify whether a key might still be needed; however,
they can't guarantee that a key version is no longer needed. Your organization
should implement procedures and guidelines to ensure that key version
destruction won't cause negative effects.

## Destroy a key version

You can destroy an enabled or disabled key version.












[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [API](#api) 
More 










- 

In the Google Cloud Dedicated console, go to the
**Key Management** page.



[Go to Key Management](https://console.cloud.berlin-build0.goog/security/kms)

- 

Check the box next to the key version that you want to schedule for
destruction.

- 

Click **Destroy** in the header.

- 

In the confirmation prompt, enter the key name and then click **Schedule
Destruction**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).






```
gcloud kms keys versions destroy KEY_VERSION \
--key KEY_NAME \
--keyring KEY_RING \
--location LOCATION 
```


Replace the following:

- ` KEY_VERSION `: the version number of the key version that you want
to destroy.

- ` KEY_NAME `: the name of the key for which you want to destroy a key
version.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

For information on all flags and possible values, run the command with the
`--help` flag.






































To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Cloud KMS C# SDK](/kms/docs/reference/libraries#client-libraries-install-csharp).



























```
using [ Google.Cloud.Kms.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html) ; 

public class DestroyKeyVersionSample 
{ 
public CryptoKeyVersion DestroyKeyVersion ( 
string projectId = "my-project" , string locationId = "us-east1" , string keyRingId = "my-key-ring" , string keyId = "my-key" , string keyVersionId = "123" ) 
{ 
// Create the client. 
[ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create) (); 

// Build the key version name. 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) keyVersionName = new [ CryptoKeyVersionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) ( projectId , locationId , keyRingId , keyId , keyVersionId ); 

// Call the API. 
[ CryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) result = client . [ DestroyCryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_DestroyCryptoKeyVersion_Google_Cloud_Kms_V1_CryptoKeyVersionName_Google_Api_Gax_Grpc_CallSettings_) ( keyVersionName ); 

// Return the result. 
return result ; 
} 
} 
```








































To run this code, first [set up a Go development environment](/go/docs/setup) and
[install the Cloud KMS Go SDK](/kms/docs/reference/libraries#client-libraries-install-go).



























```
import ( 
"context" 
"fmt" 
"io" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
) 

// destroyKeyVersion marks a specified key version for deletion. The key can be 
// restored if requested within 24 hours. 
func destroyKeyVersion ( w io . Writer , name string ) error { 
// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . DestroyCryptoKeyVersionRequest { 
Name : name , 
} 

// Call the API. 
result , err := client . DestroyCryptoKeyVersion ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to destroy key version: %w" , err ) 
} 
fmt . Fprintf ( w , "Destroyed key version: %s\n" , result ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import java.io.IOException ; 

public class DestroyKeyVersion { 

public void destroyKeyVersion () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String keyId = "my-key" ; 
String keyVersionId = "123" ; 
destroyKeyVersion ( projectId , locationId , keyRingId , keyId , keyVersionId ); 
} 

// Schedule destruction of the given key version. 
public void destroyKeyVersion ( 
String projectId , String locationId , String keyRingId , String keyId , String keyVersionId ) 
throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the key version name from the project, location, key ring, key, 
// and key version. 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName = 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) . of ( projectId , locationId , keyRingId , keyId , keyVersionId ); 

// Destroy the key version. 
[ CryptoKeyVersion ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) response = client . destroyCryptoKeyVersion ( keyVersionName ); 
System . out . printf ( "Destroyed key version: %s%n" , response . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__) ()); 
} 
} 
} 
```









































To run this code, first [set up a Node.js development environment](/nodejs/docs/setup) and
[install the Cloud KMS Node.js SDK](/kms/docs/reference/libraries#client-libraries-install-nodejs).



























```
// 
// TODO(developer): Uncomment these variables before running the sample. 
// 
// const projectId = 'my-project'; 
// const locationId = 'us-east1'; 
// const keyRingId = 'my-key-ring'; 
// const keyId = 'my-key'; 
// const versionId = '123'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the key version name 
const versionName = client . cryptoKeyVersionPath ( 
projectId , 
locationId , 
keyRingId , 
keyId , 
versionId 
); 

async function destroyKeyVersion () { 
const [ version ] = await client . destroyCryptoKeyVersion ({ 
name : versionName , 
}); 

console . log ( `Destroyed key version: ${ version . name } ` ); 
return version ; 
} 

return destroyKeyVersion (); 
```








































To run this code, first learn about [using PHP on Google Cloud Dedicated](/php/docs) and
[install the Cloud KMS PHP SDK](/kms/docs/reference/libraries#client-libraries-install-php).



























```
use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient; 
use Google\Cloud\Kms\V1\DestroyCryptoKeyVersionRequest; 

function destroy_key_version( 
string $projectId = 'my-project', 
string $locationId = 'us-east1', 
string $keyRingId = 'my-key-ring', 
string $keyId = 'my-key', 
string $versionId = '123' 
) { 
// Create the Cloud KMS client. 
$client = new KeyManagementServiceClient(); 

// Build the key version name. 
$keyVersionName = $client->cryptoKeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId); 

// Call the API. 
$destroyCryptoKeyVersionRequest = (new DestroyCryptoKeyVersionRequest()) 
->setName($keyVersionName); 
$destroyedVersion = $client->destroyCryptoKeyVersion($destroyCryptoKeyVersionRequest); 
printf('Destroyed key version: %s' . PHP_EOL, $destroyedVersion->getName()); 

return $destroyedVersion; 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 

def destroy_key_version ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str , version_id : str 
) - > kms . CryptoKeyVersion : 
""" 
Schedule destruction of the given key version. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to use (e.g. 'my-key'). 
version_id (string): ID of the key version to destroy (e.g. '1'). 

Returns: 
CryptoKeyVersion: The version. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the key version name. 
key_version_name = client . [ crypto_key_version_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path) ( 
project_id , location_id , key_ring_id , key_id , version_id 
) 

# Call the API. 
destroyed_version = client . [ destroy_crypto_key_version ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_destroy_crypto_key_version) ( 
request = { "name" : key_version_name } 
) 
print ( f "Destroyed key version: { destroyed_version . name } " ) 
return destroyed_version 
```









































To run this code, first [set up a Ruby development environment](/ruby/docs/setup) and
[install the Cloud KMS Ruby SDK](/kms/docs/reference/libraries#client-libraries-install-ruby).



























```
# TODO(developer): uncomment these values before running the sample. 
# project_id = "my-project" 
# location_id = "us-east1" 
# key_ring_id = "my-key-ring" 
# key_id = "my-key" 
# version_id = "123" 

# Require the library. 
require "google/cloud/kms" 

# Create the client. 
client = Google :: Cloud :: [ Kms ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html) . [ key_management_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)

# Build the key version name. 
key_version_name = client . [ crypto_key_version_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project : project_id , 
location : location_id , 
key_ring : key_ring_id , 
crypto_key : key_id , 
crypto_key_version : version_id 

# Call the API. 
destroyed_version = client . destroy_crypto_key_version name : key_version_name 
puts "Destroyed key version: #{ destroyed_version . name } " 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





Destroy a key version by calling the
[CryptoKeyVersions.destroy](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/destroy)
method.


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys/ KEY_NAME /cryptoKeyVersions/ KEY_VERSION :destroy" \
--request "POST" \
--header "authorization: Bearer TOKEN "
```


















If you're unable to destroy a key version, your organization might require that
key versions be disabled before destruction. Try disabling the key version
before destroying it.

When you submit the destruction request, the state of the key version becomes
scheduled for destruction. After the key's [configured
scheduled for destruction duration](/kms/docs/creating-keys#soft_delete) has
passed, the state of the key version becomes destroyed, meaning
[logical deletion of the key material from active
systems](/security/deletion#stage_3_-_logical_deletion_from_active_systems)
has started, and the key material can't be recovered by the customer. Key
material can remain in Google systems for up to [45 days](#timeline) from the
scheduled destruction time.

To receive an alert when a key version is scheduled for destruction, see
[Using Cloud Monitoring with Cloud KMS](/kms/docs/monitoring).

Destroyed key versions are not billed resources.

### Destroying external keys

To permanently remove the association between a Cloud EKM key and an
external key, you can destroy the key version.
After the *Scheduled for destruction* period has passed, the key is destroyed.
After the key version is destroyed, you can no longer encrypt data or decrypt
data that was encrypted with the Cloud EKM key version.

Destroying a *manually managed key* version in Cloud KMS doesn't modify
the key in the external key manager. We recommend first destroying the key or
key version in Google Cloud Dedicated in Germany. After the Cloud EKM key version is
destroyed, you can destroy the key material in the external key manager.

Destroying a *coordinated external key* version in Cloud KMS first
destroys the key version in Google Cloud Dedicated, and then sends a destruction
request to the EKM to destroy the external key material.

## Restore a key version

During the period when the state of a key version is scheduled for destruction,
you can restore the key version by submitting a restoration request.












[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [API](#api) 
More 










- 

Go to the **Key Management** page in the Google Cloud Dedicated console.

[Go to the Key Management page](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring that contains the key whose key version you
will restore.

- 

Click the key whose key version you want to restore.

- 

Check the box next to the key version that you want to restore.

- 

Click **Restore** in the header.

- 

In the confirmation prompt, click **Restore**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).






```
gcloud kms keys versions restore key-version \
--key key \
--keyring key-ring \
--location location 
```


Replace key-version with the version of the key to restore. Replace
key with the name of the key. Replace key-ring with
the name of the key ring where the key is located. Replace location 
with the Cloud KMS location for the key ring.

For information on all flags and possible values, run the command with the
`--help` flag.






































To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Cloud KMS C# SDK](/kms/docs/reference/libraries#client-libraries-install-csharp).



























```
using [ Google.Cloud.Kms.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html) ; 

public class RestoreKeyVersionSample 
{ 
public CryptoKeyVersion RestoreKeyVersion ( string projectId = "my-project" , string locationId = "us-east1" , string keyRingId = "my-key-ring" , string keyId = "my-key" , string keyVersionId = "123" ) 
{ 
// Create the client. 
[ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create) (); 

// Build the key version name. 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) cryptoKeyVersionName = new [ CryptoKeyVersionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) ( projectId , locationId , keyRingId , keyId , keyVersionId ); 

// Call the API. 
[ CryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) result = client . [ RestoreCryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_RestoreCryptoKeyVersion_Google_Cloud_Kms_V1_CryptoKeyVersionName_Google_Api_Gax_Grpc_CallSettings_) ( cryptoKeyVersionName ); 

// Return the result. 
return result ; 
} 
} 
```








































To run this code, first [set up a Go development environment](/go/docs/setup) and
[install the Cloud KMS Go SDK](/kms/docs/reference/libraries#client-libraries-install-go).



























```
import ( 
"context" 
"fmt" 
"io" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
) 

// restoreKeyVersion attempts to recover a key that has been marked for 
// destruction in the past 24h. 
func restoreKeyVersion ( w io . Writer , name string ) error { 
// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . RestoreCryptoKeyVersionRequest { 
Name : name , 
} 

// Call the API. 
result , err := client . RestoreCryptoKeyVersion ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to restore key version: %w" , err ) 
} 
fmt . Fprintf ( w , "Restored key version: %s\n" , result ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import java.io.IOException ; 

public class RestoreKeyVersion { 

public void restoreKeyVersion () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String keyId = "my-key" ; 
String keyVersionId = "123" ; 
restoreKeyVersion ( projectId , locationId , keyRingId , keyId , keyVersionId ); 
} 

// Schedule destruction of the given key version. 
public void restoreKeyVersion ( 
String projectId , String locationId , String keyRingId , String keyId , String keyVersionId ) 
throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the key version name from the project, location, key ring, key, 
// and key version. 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName = 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) . of ( projectId , locationId , keyRingId , keyId , keyVersionId ); 

// Restore the key version. 
[ CryptoKeyVersion ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) response = client . restoreCryptoKeyVersion ( keyVersionName ); 
System . out . printf ( "Restored key version: %s%n" , response . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__) ()); 
} 
} 
} 
```









































To run this code, first [set up a Node.js development environment](/nodejs/docs/setup) and
[install the Cloud KMS Node.js SDK](/kms/docs/reference/libraries#client-libraries-install-nodejs).



























```
// 
// TODO(developer): Uncomment these variables before running the sample. 
// 
// const projectId = 'my-project'; 
// const locationId = 'us-east1'; 
// const keyRingId = 'my-key-ring'; 
// const keyId = 'my-key'; 
// const versionId = '123'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the key version name 
const versionName = client . cryptoKeyVersionPath ( 
projectId , 
locationId , 
keyRingId , 
keyId , 
versionId 
); 

async function restoreKeyVersion () { 
const [ version ] = await client . restoreCryptoKeyVersion ({ 
name : versionName , 
}); 

console . log ( `Restored key version: ${ version . name } ` ); 
return version ; 
} 

return restoreKeyVersion (); 
```








































To run this code, first learn about [using PHP on Google Cloud Dedicated](/php/docs) and
[install the Cloud KMS PHP SDK](/kms/docs/reference/libraries#client-libraries-install-php).



























```
use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient; 
use Google\Cloud\Kms\V1\RestoreCryptoKeyVersionRequest; 

function restore_key_version( 
string $projectId = 'my-project', 
string $locationId = 'us-east1', 
string $keyRingId = 'my-key-ring', 
string $keyId = 'my-key', 
string $versionId = '123' 
) { 
// Create the Cloud KMS client. 
$client = new KeyManagementServiceClient(); 

// Build the key version name. 
$keyVersionName = $client->cryptoKeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId); 

// Call the API. 
$restoreCryptoKeyVersionRequest = (new RestoreCryptoKeyVersionRequest()) 
->setName($keyVersionName); 
$restoredVersion = $client->restoreCryptoKeyVersion($restoreCryptoKeyVersionRequest); 
printf('Restored key version: %s' . PHP_EOL, $restoredVersion->getName()); 

return $restoredVersion; 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 

def restore_key_version ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str , version_id : str 
) - > kms . CryptoKeyVersion : 
""" 
Restore a key version scheduled for destruction. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to use (e.g. 'my-key'). 
version_id (string): ID of the version to use (e.g. '1'). 

Returns: 
CryptoKeyVersion: Restored Cloud KMS key version. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the key version name. 
key_version_name = client . [ crypto_key_version_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path) ( 
project_id , location_id , key_ring_id , key_id , version_id 
) 

# Call the API. 
restored_version = client . [ restore_crypto_key_version ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_restore_crypto_key_version) ( 
request = { "name" : key_version_name } 
) 
print ( f "Restored key version: { restored_version . name } " ) 
return restored_version 
```









































To run this code, first [set up a Ruby development environment](/ruby/docs/setup) and
[install the Cloud KMS Ruby SDK](/kms/docs/reference/libraries#client-libraries-install-ruby).



























```
# TODO(developer): uncomment these values before running the sample. 
# project_id = "my-project" 
# location_id = "us-east1" 
# key_ring_id = "my-key-ring" 
# key_id = "my-key" 
# version_id = "123" 

# Require the library. 
require "google/cloud/kms" 

# Create the client. 
client = Google :: Cloud :: [ Kms ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html) . [ key_management_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)

# Build the key version name. 
key_version_name = client . [ crypto_key_version_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project : project_id , 
location : location_id , 
key_ring : key_ring_id , 
crypto_key : key_id , 
crypto_key_version : version_id 

# Call the API. 
restored_version = client . restore_crypto_key_version name : key_version_name 
puts "Restored key version: #{ restored_version . name } " 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





Restore a key version by calling the
[CryptoKeyVersions.restore](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/restore)
method.


```
curl "https://cloudkms.googleapis.com/v1/projects/ project-id /locations/ location-id /keyRings/ key-ring-id /cryptoKeys/ crypto-key-id /cryptoKeyVersions/ version-id :restore" \
--request "POST" \
--header "authorization: Bearer token "
```


















After the restoration request completes, the state of the key version becomes
disabled. You must [enable the key](/kms/docs/enable-disable#enable) before it can be used.

## Required IAM permissions

To destroy a key version, the caller needs the
`cloudkms.cryptoKeyVersions.destroy` IAM permission on the key,
the key ring, or the project, folder, or organization.

To restore a key version, the caller needs the
`cloudkms.cryptoKeyVersions.restore` permission.

Both of these permissions are granted to the Cloud KMS Admin role
(`roles/cloudkms.admin`).

## Deletion timeline

Cloud KMS commits to deleting customer key material from all Google
infrastructure within 45 days of the scheduled destruction time. This includes
removal of data from both active systems and data center backups. Other customer
data is subject to the standard
[Google Cloud deletion timeline](/security/deletion#deletion_timeline)
of 180 days.