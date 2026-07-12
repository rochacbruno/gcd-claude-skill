# Create a key

Source: https://berlin.devsitetest.how/kms/docs/creating-keys
Last updated: 2026-07-10

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












# Create a key 






- On this page 
- [ Before you begin ](#before-begin)

- [ Required roles ](#required-roles)

- [ Create a symmetric encryption key ](#create-symmetric)

- [ Create a symmetric encryption key with custom automatic rotation ](#rotation)
- [ Set the duration of the 'scheduled for destruction' state ](#soft_delete)

- [ Create an asymmetric key ](#create-asymmetric)

- [ Create an asymmetric decryption key ](#create-asymmetric-decrypt)
- [ Create an asymmetric signing key ](#create-asymmetric-sign)
- [ Create a KEM key ](#create-key-encapsulation)
- [ Retrieve the public key ](#retrieve-public)
- [ Convert a public key to JWK format ](#retrieve-public-jwk)
- [ Control access to asymmetric keys ](#access)

- [ Create a MAC signing key ](#create-mac)
- [ What's next ](#whats-next)
- 









This page shows how to create a key in Cloud KMS. A key can be a
symmetric or asymmetric encryption key, an asymmetric signing key, or a MAC
signing key.

When you create a key, you add it to a key ring in a specific
[Cloud KMS location](/kms/docs/locations). You can [create a new key
ring](/kms/docs/create-key-ring) or use an existing one.

In this page, you generate a new Cloud KMS key and add it to an
existing key ring.

To create a Cloud EKM key, see [Create an external
key](/kms/docs/create-external-key). To import a Cloud KMS or Cloud HSM key,
see [Import a key](/kms/docs/formatting-keys-for-import).

## Before you begin 

Before completing the tasks on this page, you need the following:


- A Google Cloud Dedicated project resource to contain your
Cloud KMS resources. We recommend using a separate project for your
Cloud KMS resources that does not contain any other
Google Cloud Dedicated resources.

- The name and location of the key ring where you want to create your key.
Choose a key ring in a location that is near your other resources and that
supports your chosen [protection
level](/kms/docs/protection-levels).

To create a key ring, see [Create a key
ring](/kms/docs/create-key-ring).


### Required roles















































































































































































































































To get the permissions that
you need to create keys,

ask your administrator to grant you the
following IAM roles on the project or a parent resource:













- [Cloud KMS Admin ](/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`)




- 
To create single-tenant HSM keys:
[Cloud KMS single-tenant HSM Key Creator ](/iam/docs/roles-permissions/cloudkms#cloudkms.hsmSingleTenantKeyCreator) (`roles/cloudkms.hsmSingleTenantKeyCreator`)










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).








These predefined roles contain

the permissions required to create keys. To see the exact permissions that are
required, expand the **Required permissions** section:





#### Required permissions




The following permissions are required to create keys:






- 
`cloudkms.cryptoKeys.create`



- 
`cloudkms.cryptoKeys.get`



- 
`cloudkms.cryptoKeys.list`



- 
`cloudkms.cryptoKeyVersions.create`



- 
`cloudkms.cryptoKeyVersions.get`



- 
`cloudkms.cryptoKeyVersions.list`



- 
`cloudkms.keyRings.get`



- 
`cloudkms.keyRings.list`



- 
`cloudkms.locations.get`



- 
`cloudkms.locations.list`



- 
`resourcemanager.projects.get`





- 
To retrieve a public key:
`cloudkms.cryptoKeyVersions.viewPublicKey`





- 
To create single-tenant HSM keys:




- 
`cloudkms.singleTenantHsmInstances.get`


- 
`cloudkms.singleTenantHsmInstances.use`
















You might also be able to get
these permissions
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









## Create a symmetric encryption key












[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [API](#api) 
More 










- 

In the Google Cloud Dedicated console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring for which you will create a key.

- 

Click **Create key**.

- 

For **Key name**, enter a name for your key.

- 

For **Protection level**, select **Software**.

- 

For **Key material**, select **Generated key**.

- 

For **Purpose**, select **Symmetric encrypt/decrypt**.

- 

Accept the default values for **Rotation period** and **Starting on**.

- 

Click **Create**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).





To create a software key, use the `kms keys create` command:


```
gcloud kms keys create KEY_NAME \
--keyring KEY_RING \
--location LOCATION \
--purpose "encryption"
```


Replace the following:

- ` KEY_NAME `: the name of the key.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

For information on all flags and possible values, run the command with the
`--help` flag.






































To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Cloud KMS C# SDK](/kms/docs/reference/libraries#client-libraries-install-csharp).



























```
using [ Google.Cloud.Kms.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html) ; 

public class CreateKeySymmetricEncryptDecryptSample 
{ 
public CryptoKey CreateKeySymmetricEncryptDecrypt ( 
string projectId = "my-project" , string locationId = "us-east1" , string keyRingId = "my-key-ring" , 
string id = "my-symmetric-encryption-key" ) 
{ 
// Create the client. 
[ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create) (); 

// Build the parent key ring name. 
[ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) keyRingName = new [ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) ( projectId , locationId , keyRingId ); 

// Build the key. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
{ 
Purpose = [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html) . [ EncryptDecrypt ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html#Google_Cloud_Kms_V1_CryptoKey_Types_CryptoKeyPurpose_EncryptDecrypt) , 
VersionTemplate = new [ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate.html)
{ 
Algorithm = [ CryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html) . [ GoogleSymmetricEncryption ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionAlgorithm_GoogleSymmetricEncryption) , 
} 
}; 

// Call the API. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client . [ CreateCryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateCryptoKey_Google_Cloud_Kms_V1_CreateCryptoKeyRequest_Google_Api_Gax_Grpc_CallSettings_) ( keyRingName , id , key ); 

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

// createKeySymmetricEncryptDecrypt creates a new symmetric encrypt/decrypt key 
// on Cloud KMS. 
func createKeySymmetricEncryptDecrypt ( w io . Writer , parent , id string ) error { 
// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring" 
// id := "my-symmetric-encryption-key" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . CreateCryptoKeyRequest { 
Parent : parent , 
CryptoKeyId : id , 
CryptoKey : & kmspb . CryptoKey { 
Purpose : kmspb . [ CryptoKey_ENCRYPT_DECRYPT ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKey_CRYPTO_KEY_PURPOSE_UNSPECIFIED_CryptoKey_ENCRYPT_DECRYPT_CryptoKey_ASYMMETRIC_SIGN_CryptoKey_ASYMMETRIC_DECRYPT_CryptoKey_RAW_ENCRYPT_DECRYPT_CryptoKey_MAC_CryptoKey_KEY_ENCAPSULATION) , 
VersionTemplate : & kmspb . CryptoKeyVersionTemplate { 
Algorithm : kmspb . [ CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU) , 
}, 
}, 
} 

// Call the API. 
result , err := client . CreateCryptoKey ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to create key: %w" , err ) 
} 
fmt . Fprintf ( w , "Created key: %s\n" , result . Name ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) ; 
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[KeyRingName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) ; 
import java.io.IOException ; 

public class CreateKeySymmetricEncryptDecrypt { 

public void createKeySymmetricEncryptDecrypt () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String id = "my-key" ; 
createKeySymmetricEncryptDecrypt ( projectId , locationId , keyRingId , id ); 
} 

// Create a new key that is used for symmetric encryption and decryption. 
public void createKeySymmetricEncryptDecrypt ( 
String projectId , String locationId , String keyRingId , String id ) throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the parent name from the project, location, and key ring. 
[ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) . of ( projectId , locationId , keyRingId ); 

// Build the symmetric key to create. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key = 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) . newBuilder () 
. [ setPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_) ( [ CryptoKeyPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) . ENCRYPT_DECRYPT ) 
. [ setVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_) ( 
[ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) . newBuilder () 
. setAlgorithm ( [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . GOOGLE_SYMMETRIC_ENCRYPTION )) 
. build (); 

// Create the key. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client . createCryptoKey ( keyRingName , id , key ); 
System . out . printf ( "Created symmetric key %s%n" , createdKey . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__) ()); 
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
// const id = 'my-symmetric-encryption-key'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the parent key ring name 
const keyRingName = client . keyRingPath ( projectId , locationId , keyRingId ); 

async function createKeySymmetricEncryptDecrypt () { 
const [ key ] = await client . createCryptoKey ({ 
parent : keyRingName , 
cryptoKeyId : id , 
cryptoKey : { 
purpose : 'ENCRYPT_DECRYPT' , 
versionTemplate : { 
algorithm : 'GOOGLE_SYMMETRIC_ENCRYPTION' , 
}, 
}, 
}); 

console . log ( `Created symmetric key: ${ key . name } ` ); 
return key ; 
} 

return createKeySymmetricEncryptDecrypt (); 
```








































To run this code, first learn about [using PHP on Google Cloud Dedicated](/php/docs) and
[install the Cloud KMS PHP SDK](/kms/docs/reference/libraries#client-libraries-install-php).



























```
use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient; 
use Google\Cloud\Kms\V1\CreateCryptoKeyRequest; 
use Google\Cloud\Kms\V1\CryptoKey; 
use Google\Cloud\Kms\V1\CryptoKey\CryptoKeyPurpose; 
use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionAlgorithm; 
use Google\Cloud\Kms\V1\CryptoKeyVersionTemplate; 

function create_key_symmetric_encrypt_decrypt( 
string $projectId = 'my-project', 
string $locationId = 'us-east1', 
string $keyRingId = 'my-key-ring', 
string $id = 'my-symmetric-key' 
): CryptoKey { 
// Create the Cloud KMS client. 
$client = new KeyManagementServiceClient(); 

// Build the parent key ring name. 
$keyRingName = $client->keyRingName($projectId, $locationId, $keyRingId); 

// Build the key. 
$key = (new CryptoKey()) 
->setPurpose(CryptoKeyPurpose::ENCRYPT_DECRYPT) 
->setVersionTemplate((new CryptoKeyVersionTemplate()) 
->setAlgorithm(CryptoKeyVersionAlgorithm::GOOGLE_SYMMETRIC_ENCRYPTION) 
); 

// Call the API. 
$createCryptoKeyRequest = (new CreateCryptoKeyRequest()) 
->setParent($keyRingName) 
->setCryptoKeyId($id) 
->setCryptoKey($key); 
$createdKey = $client->createCryptoKey($createCryptoKeyRequest); 
printf('Created symmetric key: %s' . PHP_EOL, $createdKey->getName()); 

return $createdKey; 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 

def create_key_symmetric_encrypt_decrypt ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str 
) - > kms . CryptoKey : 
""" 
Creates a new symmetric encryption/decryption key in Cloud KMS. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to create (e.g. 'my-symmetric-key'). 

Returns: 
CryptoKey: Cloud KMS key. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path) ( project_id , location_id , key_ring_id ) 

# Build the key. 
purpose = kms . [ CryptoKey ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html) . ENCRYPT_DECRYPT 
algorithm = ( 
kms . [ CryptoKeyVersion ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . GOOGLE_SYMMETRIC_ENCRYPTION 
) 
key = { 
"purpose" : purpose , 
"version_template" : { 
"algorithm" : algorithm , 
}, 
} 

# Call the API. 
created_key = client . [ create_crypto_key ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key) ( 
request = { "parent" : key_ring_name , "crypto_key_id" : key_id , "crypto_key" : key } 
) 
print ( f "Created symmetric key: { created_key . name } " ) 
return created_key 
```









































To run this code, first [set up a Ruby development environment](/ruby/docs/setup) and
[install the Cloud KMS Ruby SDK](/kms/docs/reference/libraries#client-libraries-install-ruby).



























```
# TODO(developer): uncomment these values before running the sample. 
# project_id = "my-project" 
# location_id = "us-east1" 
# key_ring_id = "my-key-ring" 
# id = "my-symmetric-key" 

# Require the library. 
require "google/cloud/kms" 

# Create the client. 
client = Google :: Cloud :: [ Kms ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html) . [ key_management_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project : project_id , location : location_id , key_ring : key_ring_id 

# Build the key. 
key = { 
purpose : :ENCRYPT_DECRYPT , 
version_template : { 
algorithm : :GOOGLE_SYMMETRIC_ENCRYPTION 
} 
} 

# Call the API. 
created_key = client . create_crypto_key parent : key_ring_name , crypto_key_id : id , crypto_key : key 
puts "Created symmetric key: #{ created_key . name } " 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





To create a software key, use the
[`CryptoKey.create`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create)
method:


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys?crypto_key_id= KEY_NAME " \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--data '{"purpose": "ENCRYPT_DECRYPT", "versionTemplate": { "protectionLevel": "SOFTWARE", "algorithm": " ALGORITHM " }}'
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the key ring.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` KEY_NAME `: the name of the key.

- ` ALGORITHM `: the HMAC signing algorithm—for example,
`HMAC_SHA256`. To see all supported HMAC algorithms, see [HMAC signing
algorithms](/kms/docs/algorithms#hmac_signing_algorithms).

















### Create a symmetric encryption key with custom automatic rotation

When you create a key, you can specify its [rotation
period](/kms/docs/key-rotation#automatic_rotation), which is the time between the automatic creation of
new key versions. You can also independently specify the next rotation time,
so that the next rotation happens earlier or later than one rotation period from
now.












[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [API](#api) 
More 










When you use the Google Cloud Dedicated console to create a key, Cloud KMS sets the
rotation period and next rotation time automatically. You can choose to use
the default values or specify different values.

To specify a different rotation period and starting time, when you're [creating
your key](/kms/docs/creating-keys#create_a_key), but *before* you click
the **Create** button:

- 

For **Key rotation period**, select an option.

- 

For **Starting on**, select the date when you want the first automatic
rotation to happen. You can leave **Starting on** at its default value to
start the first automatic rotation one key rotation period from when you
create the key.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).






```
gcloud kms keys create KEY_NAME \
--keyring KEY_RING \
--location LOCATION \
--purpose "encryption" \
--rotation-period ROTATION_PERIOD \
--next-rotation-time NEXT_ROTATION_TIME 
```


Replace the following:

- ` KEY_NAME `: the name of the key.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` ROTATION_PERIOD `: the interval to
rotate the key—for example, `30d` to rotate the key every 30 days. The rotation
period must be at least 1 day and at most 100 years. For more information, see
[CryptoKey.rotationPeriod](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.rotation_period).

- ` NEXT_ROTATION_TIME `: the timestamp at which to complete the first
rotation—for example, `2023-01-01T01:02:03`. You can omit
`--next-rotation-time` to schedule the first rotation for one rotation
period from when you run the command. For more information, see
[`CryptoKey.nextRotationTime`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time).

For information on all flags and possible values, run the command with the
`--help` flag.






































To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Cloud KMS C# SDK](/kms/docs/reference/libraries#client-libraries-install-csharp).



























```
using [ Google.Cloud.Kms.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html) ; 
using [ Google.Protobuf.WellKnownTypes ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html) ; 
using System ; 

public class CreateKeyRotationScheduleSample 
{ 
public CryptoKey CreateKeyRotationSchedule ( 
string projectId = "my-project" , string locationId = "us-east1" , string keyRingId = "my-key-ring" , 
string id = "my-key-with-rotation-schedule" ) 
{ 
// Create the client. 
[ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create) (); 

// Build the parent key ring name. 
[ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) keyRingName = new [ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) ( projectId , locationId , keyRingId ); 

// Build the key. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
{ 
Purpose = [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html) . [ EncryptDecrypt ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html#Google_Cloud_Kms_V1_CryptoKey_Types_CryptoKeyPurpose_EncryptDecrypt) , 
VersionTemplate = new [ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate.html)
{ 
Algorithm = [ CryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html) . [ GoogleSymmetricEncryption ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionAlgorithm_GoogleSymmetricEncryption) , 
}, 

// Rotate the key every 30 days. 
RotationPeriod = new [ Duration ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
{ 
Seconds = 60 * 60 * 24 * 30 , // 30 days 
}, 

// Start the first rotation in 24 hours. 
NextRotationTime = new [ Timestamp ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)
{ 
Seconds = new DateTimeOffset ( DateTime . UtcNow . AddHours ( 24 )). ToUnixTimeSeconds (), 
} 
}; 

// Call the API. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client . [ CreateCryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateCryptoKey_Google_Cloud_Kms_V1_CreateCryptoKeyRequest_Google_Api_Gax_Grpc_CallSettings_) ( keyRingName , id , key ); 

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
"time" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
"google.golang.org/protobuf/types/known/durationpb" 
"google.golang.org/protobuf/types/known/timestamppb" 
) 

// createKeyRotationSchedule creates a key with a rotation schedule. 
func createKeyRotationSchedule ( w io . Writer , parent , id string ) error { 
// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring" 
// id := "my-key-with-rotation-schedule" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . CreateCryptoKeyRequest { 
Parent : parent , 
CryptoKeyId : id , 
CryptoKey : & kmspb . CryptoKey { 
Purpose : kmspb . [ CryptoKey_ENCRYPT_DECRYPT ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKey_CRYPTO_KEY_PURPOSE_UNSPECIFIED_CryptoKey_ENCRYPT_DECRYPT_CryptoKey_ASYMMETRIC_SIGN_CryptoKey_ASYMMETRIC_DECRYPT_CryptoKey_RAW_ENCRYPT_DECRYPT_CryptoKey_MAC_CryptoKey_KEY_ENCAPSULATION) , 
VersionTemplate : & kmspb . CryptoKeyVersionTemplate { 
Algorithm : kmspb . [ CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU) , 
}, 

// Rotate the key every 30 days 
RotationSchedule : & kmspb . CryptoKey_RotationPeriod { 
RotationPeriod : & durationpb . Duration { 
Seconds : int64 ( 60 * 60 * 24 * 30 ), // 30 days 
}, 
}, 

// Start the first rotation in 24 hours 
NextRotationTime : & timestamppb . Timestamp { 
Seconds : time . Now (). Add ( 24 * time . Hour ). Unix (), 
}, 
}, 
} 

// Call the API. 
result , err := client . CreateCryptoKey ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to create key: %w" , err ) 
} 
fmt . Fprintf ( w , "Created key: %s\n" , result . Name ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) ; 
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[KeyRingName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) ; 
import com.google.protobuf.[Duration](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) ; 
import com.google.protobuf.[Timestamp](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) ; 
import java.io.IOException ; 
import java.time.temporal.ChronoUnit ; 

public class CreateKeyRotationSchedule { 

public void createKeyRotationSchedule () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String id = "my-key" ; 
createKeyRotationSchedule ( projectId , locationId , keyRingId , id ); 
} 

// Create a new key that automatically rotates on a schedule. 
public void createKeyRotationSchedule ( 
String projectId , String locationId , String keyRingId , String id ) throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the parent name from the project, location, and key ring. 
[ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) . of ( projectId , locationId , keyRingId ); 

// Calculate the date 24 hours from now (this is used below). 
long tomorrow = java . time . Instant . now (). plus ( 24 , ChronoUnit . HOURS ). getEpochSecond (); 

// Build the key to create with a rotation schedule. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key = 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) . newBuilder () 
. [ setPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_) ( [ CryptoKeyPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) . ENCRYPT_DECRYPT ) 
. [ setVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_) ( 
[ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) . newBuilder () 
. setAlgorithm ( [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . GOOGLE_SYMMETRIC_ENCRYPTION )) 

// Rotate every 30 days. 
. [ setRotationPeriod ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setRotationPeriod_com_google_protobuf_Duration_) ( 
[ Duration ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) . newBuilder (). setSeconds ( java . time . Duration . ofDays ( 30 ). getSeconds ())) 

// Start the first rotation in 24 hours. 
. [ setNextRotationTime ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setNextRotationTime_com_google_protobuf_Timestamp_) ( [ Timestamp ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) . newBuilder (). setSeconds ( tomorrow )) 
. build (); 

// Create the key. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client . createCryptoKey ( keyRingName , id , key ); 
System . out . printf ( "Created key with rotation schedule %s%n" , createdKey . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__) ()); 
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
// const id = 'my-rotating-encryption-key'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the parent key ring name 
const keyRingName = client . keyRingPath ( projectId , locationId , keyRingId ); 

async function createKeyRotationSchedule () { 
const [ key ] = await client . createCryptoKey ({ 
parent : keyRingName , 
cryptoKeyId : id , 
cryptoKey : { 
purpose : 'ENCRYPT_DECRYPT' , 
versionTemplate : { 
algorithm : 'GOOGLE_SYMMETRIC_ENCRYPTION' , 
}, 

// Rotate the key every 30 days. 
rotationPeriod : { 
seconds : 60 * 60 * 24 * 30 , 
}, 

// Start the first rotation in 24 hours. 
nextRotationTime : { 
seconds : new Date (). getTime () / 1000 + 60 * 60 * 24 , 
}, 
}, 
}); 

console . log ( `Created rotating key: ${ key . name } ` ); 
return key ; 
} 

return createKeyRotationSchedule (); 
```








































To run this code, first learn about [using PHP on Google Cloud Dedicated](/php/docs) and
[install the Cloud KMS PHP SDK](/kms/docs/reference/libraries#client-libraries-install-php).



























```
use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient; 
use Google\Cloud\Kms\V1\CreateCryptoKeyRequest; 
use Google\Cloud\Kms\V1\CryptoKey; 
use Google\Cloud\Kms\V1\CryptoKey\CryptoKeyPurpose; 
use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionAlgorithm; 
use Google\Cloud\Kms\V1\CryptoKeyVersionTemplate; 
use Google\Protobuf\Duration; 
use Google\Protobuf\Timestamp; 

function create_key_rotation_schedule( 
string $projectId = 'my-project', 
string $locationId = 'us-east1', 
string $keyRingId = 'my-key-ring', 
string $id = 'my-key-with-rotation-schedule' 
): CryptoKey { 
// Create the Cloud KMS client. 
$client = new KeyManagementServiceClient(); 

// Build the parent key ring name. 
$keyRingName = $client->keyRingName($projectId, $locationId, $keyRingId); 

// Build the key. 
$key = (new CryptoKey()) 
->setPurpose(CryptoKeyPurpose::ENCRYPT_DECRYPT) 
->setVersionTemplate((new CryptoKeyVersionTemplate()) 
->setAlgorithm(CryptoKeyVersionAlgorithm::GOOGLE_SYMMETRIC_ENCRYPTION)) 

// Rotate the key every 30 days. 
->setRotationPeriod((new Duration()) 
->setSeconds(60 * 60 * 24 * 30) 
) 

// Start the first rotation in 24 hours. 
->setNextRotationTime((new Timestamp()) 
->setSeconds(time() + 60 * 60 * 24) 
); 

// Call the API. 
$createCryptoKeyRequest = (new CreateCryptoKeyRequest()) 
->setParent($keyRingName) 
->setCryptoKeyId($id) 
->setCryptoKey($key); 
$createdKey = $client->createCryptoKey($createCryptoKeyRequest); 
printf('Created key with rotation: %s' . PHP_EOL, $createdKey->getName()); 

return $createdKey; 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
import time 

from google.cloud import kms 

def create_key_rotation_schedule ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str 
) - > kms . CryptoKey : 
""" 
Creates a new key in Cloud KMS that automatically rotates. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to create (e.g. 'my-rotating-key'). 

Returns: 
CryptoKey: Cloud KMS key. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path) ( project_id , location_id , key_ring_id ) 

# Build the key. 
purpose = kms . [ CryptoKey ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html) . ENCRYPT_DECRYPT 
algorithm = ( 
kms . [ CryptoKeyVersion ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . GOOGLE_SYMMETRIC_ENCRYPTION 
) 
key = { 
"purpose" : purpose , 
"version_template" : { 
"algorithm" : algorithm , 
}, 
# Rotate the key every 30 days. 
"rotation_period" : { "seconds" : 60 * 60 * 24 * 30 }, 
# Start the first rotation in 24 hours. 
"next_rotation_time" : { "seconds" : int ( time . time ()) + 60 * 60 * 24 }, 
} 

# Call the API. 
created_key = client . [ create_crypto_key ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key) ( 
request = { "parent" : key_ring_name , "crypto_key_id" : key_id , "crypto_key" : key } 
) 
print ( f "Created labeled key: { created_key . name } " ) 
return created_key 
```









































To run this code, first [set up a Ruby development environment](/ruby/docs/setup) and
[install the Cloud KMS Ruby SDK](/kms/docs/reference/libraries#client-libraries-install-ruby).



























```
# TODO(developer): uncomment these values before running the sample. 
# project_id = "my-project" 
# location_id = "us-east1" 
# key_ring_id = "my-key-ring" 
# id = "my-key-with-rotation" 

# Require the library. 
require "google/cloud/kms" 

# Create the client. 
client = Google :: Cloud :: [ Kms ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html) . [ key_management_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project : project_id , location : location_id , key_ring : key_ring_id 

# Build the key. 
key = { 
purpose : :ENCRYPT_DECRYPT , 
version_template : { 
algorithm : :GOOGLE_SYMMETRIC_ENCRYPTION 
}, 

# Rotate the key every 30 days. 
rotation_period : { 
seconds : 60 * 60 * 24 * 30 
}, 

# Start the first rotation in 24 hours. 
next_rotation_time : { 
seconds : ( Time . now + ( 60 * 60 * 24 )) . to_i 
} 
} 

# Call the API. 
created_key = client . create_crypto_key parent : key_ring_name , crypto_key_id : id , crypto_key : key 
puts "Created rotating key: #{ created_key . name } " 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





To create a key, use the
[`CryptoKey.create`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create)
method:


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys?crypto_key_id= KEY_NAME " \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--data '{"purpose": " PURPOSE ", "rotationPeriod": " ROTATION_PERIOD ", "nextRotationTime": " NEXT_ROTATION_TIME "}'
```


Replace the following:

- ` PURPOSE `: the
[purpose](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)
of the key.

- ` ROTATION_PERIOD `: the interval to
rotate the key—for example, `30d` to rotate the key every 30 days. The rotation
period must be at least 1 day and at most 100 years. For more information, see
[CryptoKey.rotationPeriod](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.rotation_period).

- ` NEXT_ROTATION_TIME `: the timestamp at which to complete the first
rotation—for example, `2023-01-01T01:02:03`. For more information, see
[`CryptoKey.nextRotationTime`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time).


















### Set the duration of the 'scheduled for destruction' state

By default, key versions in Cloud KMS spend
30 days in the scheduled for destruction
(`DESTROY_SCHEDULED`) state before they are
destroyed. The scheduled for destruction state is sometimes called the
*soft deleted state*. The duration for which key versions remain in this state
is configurable, with the following constraints:

- You can only set the duration during key creation.

- After the duration for the key has been specified, it can't be changed.

- The duration applies to all versions of the key created in the future.

- The minimum duration is 24 hours for all keys, except for import-only keys
which have a minimum duration of 0.

- The maximum duration is 120 days.

- The default duration is 30 days.

Your organization might have a minimum scheduled for destruction duration
value defined by organization policies. For more information, see [Control
key destruction](/kms/docs/control-key-destruction).

To create a key which uses a custom duration for the *scheduled for destruction*
state, use the following steps:












[Console](#console) [ gcloud ](#gcloud) 
More 










- 

In the Google Cloud Dedicated console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring for which you will create a key.

- 

Click **Create key**.

- 

Configure the settings of the key for your application.

- 

Click **Additional settings**.

- 

In **Duration of 'scheduled for destruction' state**, choose the number of
days the key will remain *scheduled for destruction* before being
permanently destroyed.

- 

Click **Create key**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).






```
gcloud kms keys create KEY_NAME \
--keyring KEY_RING \
--location LOCATION \
--purpose PURPOSE \
--destroy-scheduled-duration DURATION 
```


Replace the following:

- ` KEY_NAME `: the name of the key.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` PURPOSE `: the purpose of the key—for example,
`encryption`.

- ` DURATION `: the amount of time for the key to remain in the
*scheduled for destruction* state before being permanently destroyed.

For information on all flags and possible values, run the command with the
`--help` flag.

















We recommend using the default duration of 30 days
for all keys unless you have specific application or regulatory requirements
that require a different value.

## Create an asymmetric key

The following sections show you how to create asymmetric keys.

### Create an asymmetric decryption key

Follow these steps to create an asymmetric decryption key on the specified key
ring and location. These examples can be adapted to specify a different
protection level or algorithm. For more information and alternative values, see
[Algorithms](/kms/docs/algorithms) and [Protection levels](/kms/docs/algorithms#protection_levels).

When you first create the key, the initial key version has a state of
**Pending generation**. When the state changes to **Enabled**, you can use
the key. To learn more about key version states, see [Key version
states](/kms/docs/key-states).












[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [API](#api) 
More 










- 

In the Google Cloud Dedicated console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring for which you will create a key.

- 

Click **Create key**.

- 

For **Key name**, enter a name for your key.

- 

For **Protection level**, select **Software**.

- 

For **Key material**, select **Generated key**.

- 

For **Purpose**, select **Asymmetric decrypt**.

- 

For **Algorithm**, select **3072 bit RSA - OAEP Padding - SHA256 Digest**.
You can change this value on future key versions.

- 

Click **Create**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).






```
gcloud kms keys create KEY_NAME \
--keyring KEY_RING \
--location LOCATION \
--purpose "asymmetric-encryption" \
--default-algorithm " ALGORITHM " \
--protection-level " PROTECTION_LEVEL "
```


Replace the following:

- ` KEY_NAME `: the name of the key.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` ALGORITHM `: the algorithm to use for the key—for
example, `rsa-decrypt-oaep-3072-sha256`. For a list of supported asymmetric
encryption algorithms, see [Asymmetric encryption
algorithms](/kms/docs/algorithms#asymmetric_encryption_algorithms).

- ` PROTECTION_LEVEL `: the protection level that you want to use for
the key.

For information on all flags and possible values, run the command with the
`--help` flag.






































To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Cloud KMS C# SDK](/kms/docs/reference/libraries#client-libraries-install-csharp).



























```
using [ Google.Cloud.Kms.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html) ; 
using [ Google.Protobuf.WellKnownTypes ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html) ; 

public class CreateKeyAsymmetricDecryptSample 
{ 
public CryptoKey CreateKeyAsymmetricDecrypt ( 
string projectId = "my-project" , string locationId = "us-east1" , string keyRingId = "my-key-ring" , 
string id = "my-asymmetric-encrypt-key" ) 
{ 
// Create the client. 
[ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create) (); 

// Build the parent key ring name. 
[ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) keyRingName = new [ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) ( projectId , locationId , keyRingId ); 

// Build the key. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
{ 
Purpose = [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html) . [ AsymmetricDecrypt ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html#Google_Cloud_Kms_V1_CryptoKey_Types_CryptoKeyPurpose_AsymmetricDecrypt) , 
VersionTemplate = new [ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate.html)
{ 
Algorithm = [ CryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html) . [ RsaDecryptOaep2048Sha256 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionAlgorithm_RsaDecryptOaep2048Sha256) , 
}, 

// Optional: customize how long key versions should be kept before destroying. 
DestroyScheduledDuration = new [ Duration ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
{ 
Seconds = 24 * 60 * 60 , 
} 
}; 

// Call the API. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client . [ CreateCryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateCryptoKey_Google_Cloud_Kms_V1_CreateCryptoKeyRequest_Google_Api_Gax_Grpc_CallSettings_) ( keyRingName , id , key ); 

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
"time" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
"google.golang.org/protobuf/types/known/durationpb" 
) 

// createKeyAsymmetricDecrypt creates a new asymmetric RSA encrypt/decrypt key 
// pair where the private key is stored in Cloud KMS. 
func createKeyAsymmetricDecrypt ( w io . Writer , parent , id string ) error { 
// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring" 
// id := "my-asymmetric-encryption-key" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . CreateCryptoKeyRequest { 
Parent : parent , 
CryptoKeyId : id , 
CryptoKey : & kmspb . CryptoKey { 
Purpose : kmspb . [ CryptoKey_ASYMMETRIC_DECRYPT ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKey_CRYPTO_KEY_PURPOSE_UNSPECIFIED_CryptoKey_ENCRYPT_DECRYPT_CryptoKey_ASYMMETRIC_SIGN_CryptoKey_ASYMMETRIC_DECRYPT_CryptoKey_RAW_ENCRYPT_DECRYPT_CryptoKey_MAC_CryptoKey_KEY_ENCAPSULATION) , 
VersionTemplate : & kmspb . CryptoKeyVersionTemplate { 
Algorithm : kmspb . [ CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256 ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU) , 
}, 

// Optional: customize how long key versions should be kept before destroying. 
DestroyScheduledDuration : durationpb . New ( 24 * time . Hour ), 
}, 
} 

// Call the API. 
result , err := client . CreateCryptoKey ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to create key: %w" , err ) 
} 
fmt . Fprintf ( w , "Created key: %s\n" , result . Name ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) ; 
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[KeyRingName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) ; 
import com.google.protobuf.[Duration](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) ; 
import java.io.IOException ; 

public class CreateKeyAsymmetricDecrypt { 

public void createKeyAsymmetricDecrypt () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String id = "my-asymmetric-decryption-key" ; 
createKeyAsymmetricDecrypt ( projectId , locationId , keyRingId , id ); 
} 

// Create a new asymmetric key for the purpose of encrypting and decrypting 
// data. 
public void createKeyAsymmetricDecrypt ( 
String projectId , String locationId , String keyRingId , String id ) throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the parent name from the project, location, and key ring. 
[ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) . of ( projectId , locationId , keyRingId ); 

// Build the asymmetric key to create. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key = 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) . newBuilder () 
. [ setPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_) ( [ CryptoKeyPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) . ASYMMETRIC_DECRYPT ) 
. [ setVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_) ( 
[ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) . newBuilder () 
. setAlgorithm ( [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . RSA_DECRYPT_OAEP_2048_SHA256 )) 

// Optional: customize how long key versions should be kept before destroying. 
. [ setDestroyScheduledDuration ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setDestroyScheduledDuration_com_google_protobuf_Duration_) ( [ Duration ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) . newBuilder (). setSeconds ( 24 * 60 * 60 )) 
. build (); 

// Create the key. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client . createCryptoKey ( keyRingName , id , key ); 
System . out . printf ( "Created asymmetric key %s%n" , createdKey . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__) ()); 
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
// const id = 'my-asymmetric-decrypt-key'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the parent key ring name 
const keyRingName = client . keyRingPath ( projectId , locationId , keyRingId ); 

async function createKeyAsymmetricDecrypt () { 
const [ key ] = await client . createCryptoKey ({ 
parent : keyRingName , 
cryptoKeyId : id , 
cryptoKey : { 
purpose : 'ASYMMETRIC_DECRYPT' , 
versionTemplate : { 
algorithm : 'RSA_DECRYPT_OAEP_2048_SHA256' , 
}, 

// Optional: customize how long key versions should be kept before 
// destroying. 
destroyScheduledDuration : { seconds : 60 * 60 * 24 }, 
}, 
}); 

console . log ( `Created asymmetric key: ${ key . name } ` ); 
return key ; 
} 

return createKeyAsymmetricDecrypt (); 
```








































To run this code, first learn about [using PHP on Google Cloud Dedicated](/php/docs) and
[install the Cloud KMS PHP SDK](/kms/docs/reference/libraries#client-libraries-install-php).



























```
use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient; 
use Google\Cloud\Kms\V1\CreateCryptoKeyRequest; 
use Google\Cloud\Kms\V1\CryptoKey; 
use Google\Cloud\Kms\V1\CryptoKey\CryptoKeyPurpose; 
use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionAlgorithm; 
use Google\Cloud\Kms\V1\CryptoKeyVersionTemplate; 
use Google\Protobuf\Duration; 

function create_key_asymmetric_decrypt( 
string $projectId = 'my-project', 
string $locationId = 'us-east1', 
string $keyRingId = 'my-key-ring', 
string $id = 'my-asymmetric-decrypt-key' 
): CryptoKey { 
// Create the Cloud KMS client. 
$client = new KeyManagementServiceClient(); 

// Build the parent key ring name. 
$keyRingName = $client->keyRingName($projectId, $locationId, $keyRingId); 

// Build the key. 
$key = (new CryptoKey()) 
->setPurpose(CryptoKeyPurpose::ASYMMETRIC_DECRYPT) 
->setVersionTemplate((new CryptoKeyVersionTemplate()) 
->setAlgorithm(CryptoKeyVersionAlgorithm::RSA_DECRYPT_OAEP_2048_SHA256) 
) 

// Optional: customize how long key versions should be kept before destroying. 
->setDestroyScheduledDuration((new Duration()) 
->setSeconds(24 * 60 * 60) 
); 

// Call the API. 
$createCryptoKeyRequest = (new CreateCryptoKeyRequest()) 
->setParent($keyRingName) 
->setCryptoKeyId($id) 
->setCryptoKey($key); 
$createdKey = $client->createCryptoKey($createCryptoKeyRequest); 
printf('Created asymmetric decryption key: %s' . PHP_EOL, $createdKey->getName()); 

return $createdKey; 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
import datetime 

# Import the client library. 
from google.cloud import kms 
from google.protobuf import duration_pb2 # type: ignore 

def create_key_asymmetric_decrypt ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str 
) - > kms . CryptoKey : 
""" 
Creates a new asymmetric decryption key in Cloud KMS. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to create (e.g. 'my-asymmetric-decrypt-key'). 

Returns: 
CryptoKey: Cloud KMS key. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path) ( project_id , location_id , key_ring_id ) 

# Build the key. 
purpose = kms . [ CryptoKey ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html) . ASYMMETRIC_DECRYPT 
algorithm = ( 
kms . [ CryptoKeyVersion ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . RSA_DECRYPT_OAEP_2048_SHA256 
) 
key = { 
"purpose" : purpose , 
"version_template" : { 
"algorithm" : algorithm , 
}, 
# Optional: customize how long key versions should be kept before 
# destroying. 
"destroy_scheduled_duration" : duration_pb2 . Duration () . FromTimedelta ( 
datetime . timedelta ( days = 1 ) 
), 
} 

# Call the API. 
created_key = client . [ create_crypto_key ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key) ( 
request = { "parent" : key_ring_name , "crypto_key_id" : key_id , "crypto_key" : key } 
) 
print ( f "Created asymmetric decrypt key: { created_key . name } " ) 
return created_key 
```









































To run this code, first [set up a Ruby development environment](/ruby/docs/setup) and
[install the Cloud KMS Ruby SDK](/kms/docs/reference/libraries#client-libraries-install-ruby).



























```
# TODO(developer): uncomment these values before running the sample. 
# project_id = "my-project" 
# location_id = "us-east1" 
# key_ring_id = "my-key-ring" 
# id = "my-asymmetric-decrypt-key" 

# Require the library. 
require "google/cloud/kms" 

# Create the client. 
client = Google :: Cloud :: [ Kms ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html) . [ key_management_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project : project_id , location : location_id , key_ring : key_ring_id 

# Build the key. 
key = { 
purpose : :ASYMMETRIC_DECRYPT , 
version_template : { 
algorithm : :RSA_DECRYPT_OAEP_2048_SHA256 
}, 

# Optional: customize how long key versions should be kept before destroying. 
destroy_scheduled_duration : { 
seconds : 24 * 60 * 60 
} 
} 

# Call the API. 
created_key = client . create_crypto_key parent : key_ring_name , crypto_key_id : id , crypto_key : key 
puts "Created asymmetric decryption key: #{ created_key . name } " 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





Create an asymmetric decryption key using the
[
`CryptoKey.create`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method.


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys?crypto_key_id= KEY_NAME " \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--data '{"purpose": "ASYMMETRIC_DECRYPT", "protectionLevel": " PROTECTION_LEVEL ", "versionTemplate": {"algorithm": " ALGORITHM "}}'
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the key ring.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` KEY_NAME `: the name of the key.

- ` ALGORITHM `: the algorithm to use for
the key—for example, `RSA_DECRYPT_OAEP_3072_SHA256`. For a list of
supported asymmetric encryption algorithms, see [Asymmetric encryption
algorithms](/kms/docs/algorithms#asymmetric_encryption_algorithms).

- ` PROTECTION_LEVEL `: the protection level that you want to use for
the key.

















### Create an asymmetric signing key

Follow these steps to create an asymmetric signing key on the specified key ring
and location. These examples can be adapted to specify a different
protection level or algorithm. For more information and alternative values, see
[Algorithms](/kms/docs/algorithms) and [Protection levels](/kms/docs/algorithms#protection_levels).

When you first create the key, the initial key version has a state of
**Pending generation**. When the state changes to **Enabled**, you can use
the key. To learn more about key version states, see [Key version
states](/kms/docs/key-states).












[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [API](#api) 
More 










- 

In the Google Cloud Dedicated console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring for which you will create a key.

- 

Click **Create key**.

- 

For **Key name**, enter a name for your key.

- 

For **Protection level**, select **Software**.

- 

For **Key material**, select **Generated key**.

- 

For **Purpose**, select **Asymmetric sign**.

- 

For **Algorithm**, select **Elliptic Curve P-256 - SHA256 Digest**. You can
change this value on future key versions.

- 

Click **Create**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).






```
gcloud kms keys create KEY_NAME \
--keyring KEY_RING \
--location LOCATION \
--purpose "asymmetric-signing" \
--default-algorithm " ALGORITHM " \
--protection-level " PROTECTION_LEVEL "
```


Replace the following:

- ` KEY_NAME `: the name of the key.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` ALGORITHM `: the algorithm to use for the key—for example,
`ec-sign-p256-sha256`. For a list of supported algorithms, see [Asymmetric
signing algorithms](/kms/docs/algorithms#asymmetric_signing_algorithms).

- ` PROTECTION_LEVEL `: the protection level that you want to use for
the key.

For information on all flags and possible values, run the command with the
`--help` flag.






































To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Cloud KMS C# SDK](/kms/docs/reference/libraries#client-libraries-install-csharp).



























```
using [ Google.Cloud.Kms.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html) ; 
using [ Google.Protobuf.WellKnownTypes ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html) ; 

public class CreateKeyAsymmetricSignSample 
{ 
public CryptoKey CreateKeyAsymmetricSign ( 
string projectId = "my-project" , string locationId = "us-east1" , string keyRingId = "my-key-ring" , 
string id = "my-asymmetric-signing-key" ) 
{ 
// Create the client. 
[ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create) (); 

// Build the parent key ring name. 
[ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) keyRingName = new [ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) ( projectId , locationId , keyRingId ); 

// Build the key. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
{ 
Purpose = [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html) . [ AsymmetricSign ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html#Google_Cloud_Kms_V1_CryptoKey_Types_CryptoKeyPurpose_AsymmetricSign) , 
VersionTemplate = new [ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate.html)
{ 
Algorithm = [ CryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html) . [ RsaSignPkcs12048Sha256 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionAlgorithm_RsaSignPkcs12048Sha256) , 
}, 

// Optional: customize how long key versions should be kept before destroying. 
DestroyScheduledDuration = new [ Duration ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
{ 
Seconds = 24 * 60 * 60 , 
} 
}; 

// Call the API. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client . [ CreateCryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateCryptoKey_Google_Cloud_Kms_V1_CreateCryptoKeyRequest_Google_Api_Gax_Grpc_CallSettings_) ( keyRingName , id , key ); 

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
"time" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
"google.golang.org/protobuf/types/known/durationpb" 
) 

// createKeyAsymmetricSign creates a new asymmetric RSA sign/verify key pair 
// where the private key is stored in Cloud KMS. 
func createKeyAsymmetricSign ( w io . Writer , parent , id string ) error { 
// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring" 
// id := "my-asymmetric-signing-key" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . CreateCryptoKeyRequest { 
Parent : parent , 
CryptoKeyId : id , 
CryptoKey : & kmspb . CryptoKey { 
Purpose : kmspb . [ CryptoKey_ASYMMETRIC_SIGN ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKey_CRYPTO_KEY_PURPOSE_UNSPECIFIED_CryptoKey_ENCRYPT_DECRYPT_CryptoKey_ASYMMETRIC_SIGN_CryptoKey_ASYMMETRIC_DECRYPT_CryptoKey_RAW_ENCRYPT_DECRYPT_CryptoKey_MAC_CryptoKey_KEY_ENCAPSULATION) , 
VersionTemplate : & kmspb . CryptoKeyVersionTemplate { 
Algorithm : kmspb . [ CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256 ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU) , 
}, 

// Optional: customize how long key versions should be kept before destroying. 
DestroyScheduledDuration : durationpb . New ( 24 * time . Hour ), 
}, 
} 

// Call the API. 
result , err := client . CreateCryptoKey ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to create key: %w" , err ) 
} 
fmt . Fprintf ( w , "Created key: %s\n" , result . Name ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) ; 
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[KeyRingName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) ; 
import com.google.protobuf.[Duration](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) ; 
import java.io.IOException ; 

public class CreateKeyAsymmetricSign { 

public void createKeyAsymmetricSign () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String id = "my-asymmetric-signing-key" ; 
createKeyAsymmetricSign ( projectId , locationId , keyRingId , id ); 
} 

// Create a new asymmetric key for the purpose of signing and verifying data. 
public void createKeyAsymmetricSign ( 
String projectId , String locationId , String keyRingId , String id ) throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the parent name from the project, location, and key ring. 
[ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) . of ( projectId , locationId , keyRingId ); 

// Build the asymmetric key to create. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key = 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) . newBuilder () 
. [ setPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_) ( [ CryptoKeyPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) . ASYMMETRIC_SIGN ) 
. [ setVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_) ( 
[ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) . newBuilder () 
. setAlgorithm ( [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . RSA_SIGN_PKCS1_2048_SHA256 )) 

// Optional: customize how long key versions should be kept before destroying. 
. [ setDestroyScheduledDuration ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setDestroyScheduledDuration_com_google_protobuf_Duration_) ( [ Duration ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) . newBuilder (). setSeconds ( 24 * 60 * 60 )) 
. build (); 

// Create the key. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client . createCryptoKey ( keyRingName , id , key ); 
System . out . printf ( "Created asymmetric key %s%n" , createdKey . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__) ()); 
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
// const id = 'my-asymmetric-sign-key'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the parent key ring name 
const keyRingName = client . keyRingPath ( projectId , locationId , keyRingId ); 

async function createKeyAsymmetricSign () { 
const [ key ] = await client . createCryptoKey ({ 
parent : keyRingName , 
cryptoKeyId : id , 
cryptoKey : { 
purpose : 'ASYMMETRIC_SIGN' , 
versionTemplate : { 
algorithm : 'RSA_SIGN_PKCS1_2048_SHA256' , 
}, 

// Optional: customize how long key versions should be kept before 
// destroying. 
destroyScheduledDuration : { seconds : 60 * 60 * 24 }, 
}, 
}); 

console . log ( `Created asymmetric key: ${ key . name } ` ); 
return key ; 
} 

return createKeyAsymmetricSign (); 
```








































To run this code, first learn about [using PHP on Google Cloud Dedicated](/php/docs) and
[install the Cloud KMS PHP SDK](/kms/docs/reference/libraries#client-libraries-install-php).



























```
use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient; 
use Google\Cloud\Kms\V1\CreateCryptoKeyRequest; 
use Google\Cloud\Kms\V1\CryptoKey; 
use Google\Cloud\Kms\V1\CryptoKey\CryptoKeyPurpose; 
use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionAlgorithm; 
use Google\Cloud\Kms\V1\CryptoKeyVersionTemplate; 
use Google\Protobuf\Duration; 

function create_key_asymmetric_sign( 
string $projectId = 'my-project', 
string $locationId = 'us-east1', 
string $keyRingId = 'my-key-ring', 
string $id = 'my-asymmetric-signing-key' 
): CryptoKey { 
// Create the Cloud KMS client. 
$client = new KeyManagementServiceClient(); 

// Build the parent key ring name. 
$keyRingName = $client->keyRingName($projectId, $locationId, $keyRingId); 

// Build the key. 
$key = (new CryptoKey()) 
->setPurpose(CryptoKeyPurpose::ASYMMETRIC_SIGN) 
->setVersionTemplate((new CryptoKeyVersionTemplate()) 
->setAlgorithm(CryptoKeyVersionAlgorithm::RSA_SIGN_PKCS1_2048_SHA256) 
) 

// Optional: customize how long key versions should be kept before destroying. 
->setDestroyScheduledDuration((new Duration()) 
->setSeconds(24 * 60 * 60) 
); 

// Call the API. 
$createCryptoKeyRequest = (new CreateCryptoKeyRequest()) 
->setParent($keyRingName) 
->setCryptoKeyId($id) 
->setCryptoKey($key); 
$createdKey = $client->createCryptoKey($createCryptoKeyRequest); 
printf('Created asymmetric signing key: %s' . PHP_EOL, $createdKey->getName()); 

return $createdKey; 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
import datetime 

# Import the client library. 
from google.cloud import kms 
from google.protobuf import duration_pb2 # type: ignore 

def create_key_asymmetric_sign ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str 
) - > kms . CryptoKey : 
""" 
Creates a new asymmetric signing key in Cloud KMS. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to create (e.g. 'my-asymmetric-signing-key'). 

Returns: 
CryptoKey: Cloud KMS key. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path) ( project_id , location_id , key_ring_id ) 

# Build the key. 
purpose = kms . [ CryptoKey ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html) . ASYMMETRIC_SIGN 
algorithm = ( 
kms . [ CryptoKeyVersion ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . RSA_SIGN_PKCS1_2048_SHA256 
) 
key = { 
"purpose" : purpose , 
"version_template" : { 
"algorithm" : algorithm , 
}, 
# Optional: customize how long key versions should be kept before 
# destroying. 
"destroy_scheduled_duration" : duration_pb2 . Duration () . FromTimedelta ( 
datetime . timedelta ( days = 1 ) 
), 
} 

# Call the API. 
created_key = client . [ create_crypto_key ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key) ( 
request = { "parent" : key_ring_name , "crypto_key_id" : key_id , "crypto_key" : key } 
) 
print ( f "Created asymmetric signing key: { created_key . name } " ) 
return created_key 
```









































To run this code, first [set up a Ruby development environment](/ruby/docs/setup) and
[install the Cloud KMS Ruby SDK](/kms/docs/reference/libraries#client-libraries-install-ruby).



























```
# TODO(developer): uncomment these values before running the sample. 
# project_id = "my-project" 
# location_id = "us-east1" 
# key_ring_id = "my-key-ring" 
# id = "my-asymmetric-signing-key" 

# Require the library. 
require "google/cloud/kms" 

# Create the client. 
client = Google :: Cloud :: [ Kms ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html) . [ key_management_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project : project_id , location : location_id , key_ring : key_ring_id 

# Build the key. 
key = { 
purpose : :ASYMMETRIC_SIGN , 
version_template : { 
algorithm : :RSA_SIGN_PKCS1_2048_SHA256 
}, 

# Optional: customize how long key versions should be kept before destroying. 
destroy_scheduled_duration : { 
seconds : 24 * 60 * 60 
} 
} 

# Call the API. 
created_key = client . create_crypto_key parent : key_ring_name , crypto_key_id : id , crypto_key : key 
puts "Created asymmetric signing key: #{ created_key . name } " 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





Create an asymmetric signing key by calling
[`CryptoKey.create`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create).


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys?crypto_key_id= KEY_NAME " \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--data '{"purpose": "ASYMMETRIC_SIGN", "versionTemplate": {"protectionLevel": " PROTECTION_LEVEL ", "algorithm": " ALGORITHM "}}'
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the key ring.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` KEY_NAME `: the name of the key.

- ` PROTECTION_LEVEL `: the protection level that you want to use for
the key.

- 

` ALGORITHM `: the algorithm to use for
the key—for example, `EC_SIGN_P256_SHA256`. For a list of supported
algorithms, see [Asymmetric signing
algorithms](/kms/docs/algorithms#asymmetric_signing_algorithms).

















### Create a KEM key

Follow these steps to create a key for use in a key encapsulation mechanism (KEM) for the specified key ring
and location. These examples can be adapted to specify a different
protection level or algorithm. For more information and alternative values, see
[Algorithms](/kms/docs/algorithms) and [Protection levels](/kms/docs/algorithms#protection_levels).

When you first create the key, the initial key version has a state of
**Pending generation**. When the state changes to **Enabled**, you can use
the key. To learn more about key version states, see [Key version
states](/kms/docs/key-states).








[ gcloud ](#gcloud) [API](#api) 
More 









To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).






```
gcloud kms keys create KEY_NAME \
--keyring KEY_RING \
--location LOCATION \
--purpose "key-encapsulation" \
--default-algorithm " ALGORITHM "
```


Replace the following:

- ` KEY_NAME `: the name of the key.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` ALGORITHM `: the algorithm to use for the key—for
example, `ml-kem-768`. For a list of supported key encapsulation algorithms, see [Key encapsulation
algorithms](/kms/docs/algorithms#key_encapsulation_algorithms).

For information on all flags and possible values, run the command with the
`--help` flag.




























These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





Create a key with purpose `KEY_ENCAPSULATION` by calling
[`CryptoKey.create`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create).


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys?crypto_key_id= KEY_NAME " \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--data '{"purpose": "KEY_ENCAPSULATION", "versionTemplate": {"algorithm": " ALGORITHM "}}'
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the key ring.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` KEY_NAME `: the name of the key.

- ` ALGORITHM `: the algorithm to use for
the key—for example, `ML_KEM_768`. For a list of
supported key encapsulation algorithms, see [Key encapsulation algorithms](/kms/docs/algorithms#key_encapsulation_algorithms).


















### Retrieve the public key

When you create an asymmetric key, Cloud KMS creates a public/private
key pair. You can retrieve the public key of an enabled asymmetric key at any
time after the key is generated.

The public key is in the Privacy-enhanced Electronic Mail (PEM) format. For more
information, see the [RFC 7468](https://tools.ietf.org/html/rfc7468) sections [General
Considerations](https://tools.ietf.org/html/rfc7468#section-2) and [Textual Encoding of Subject Public
Key Info](https://tools.ietf.org/html/rfc7468#section-13).

To download the public key for an existing asymmetric key version, follow these
steps:












[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [API](#api) 
More 










- 

In the Google Cloud Dedicated console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring that contains the asymmetric key for which
you want to retrieve the public key.

- 

Click the name of the key for which you want to retrieve the public key.

- 

On the row corresponding to the key version for which you want to retrieve
the public key, click **View More more_vert **.

- 

Click **Get public key**.

- 

The public key is displayed in the prompt. You can copy the public key to
your clipboard. To download the public key, click **Download**.

If you do not see the **Get public key** option, verify the following:

- The key is an asymmetric key.

- The key version is enabled.

- You have the `cloudkms.cryptoKeyVersions.viewPublicKey` permission.

The filename of a public key downloaded from the Google Cloud Dedicated console is of
the form:


```
KEY_RING - KEY_NAME - KEY_VERSION .pub
```


Each portion of the filename is separated by a hyphen, for example
`ringname-keyname-version.pub`.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).






```
gcloud kms keys versions get-public-key KEY_VERSION \
--key KEY_NAME \
--keyring KEY_RING \
--location LOCATION \
--public-key-format PUBLIC_KEY_FORMAT \
--output-file OUTPUT_FILE_PATH 
```


Replace the following:

- ` KEY_VERSION `: the key version number.

- ` KEY_NAME `: the name of the key.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` PUBLIC_KEY_FORMAT `: the format in which you want to export
the public key. For NIST PQC algorithms
([Preview](https://berlin.devsitetest.how/products#product-launch-stages)), use `nist-pqc` and for X-Wing use `xwing-raw-bytes`. For all other
keys, you can use `pem`, `der`, or omit this parameter.

- ` OUTPUT_FILE_PATH `: the path where you want to save the
public key file—for example, `public-key.pub`.

For information on all flags and possible values, run the command with the
`--help` flag.






































To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Cloud KMS C# SDK](/kms/docs/reference/libraries#client-libraries-install-csharp).



























```
using [ Google.Cloud.Kms.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html) ; 

public class GetPublicKeySample 
{ 
public PublicKey GetPublicKey ( string projectId = "my-project" , string locationId = "us-east1" , string keyRingId = "my-key-ring" , string keyId = "my-key" , string keyVersionId = "123" ) 
{ 
// Create the client. 
[ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create) (); 

// Build the key version name. 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) keyVersionName = new [ CryptoKeyVersionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) ( projectId , locationId , keyRingId , keyId , keyVersionId ); 

// Call the API. 
[ PublicKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey.html) result = client . [ GetPublicKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_GetPublicKey_Google_Cloud_Kms_V1_CryptoKeyVersionName_Google_Api_Gax_Grpc_CallSettings_) ( keyVersionName ); 

// Return the ciphertext. 
return result ; 
} 
} 
```








































To run this code, first [set up a Go development environment](/go/docs/setup) and
[install the Cloud KMS Go SDK](/kms/docs/reference/libraries#client-libraries-install-go).



























```
import ( 
"context" 
"crypto/x509" 
"encoding/pem" 
"fmt" 
"hash/crc32" 
"io" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
) 

// getPublicKey retrieves the public key from an asymmetric key pair on 
// Cloud KMS. 
func getPublicKey ( w io . Writer , name string ) error { 
// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . GetPublicKeyRequest { 
Name : name , 
} 

// Call the API. 
result , err := client . GetPublicKey ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to get public key: %w" , err ) 
} 

// The 'Pem' field is the raw string representation of the public key. 
// Convert 'Pem' into bytes for further processing. 
key := [] byte ( result . Pem ) 

// Optional, but recommended: perform integrity verification on result. 
// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit: 
// https://cloud.google.com/kms/docs/data-integrity-guidelines 
crc32c := func ( data [] byte ) uint32 { 
t := crc32 . MakeTable ( crc32 . Castagnoli ) 
return crc32 . Checksum ( data , t ) 
} 
if int64 ( crc32c ( key )) != result . PemCrc32C . Value { 
return fmt . Errorf ( "getPublicKey: response corrupted in-transit" ) 
} 

// Optional - parse the public key. This transforms the string key into a Go 
// PublicKey. 
block , _ := pem . Decode ( key ) 
publicKey , err := x509 . ParsePKIXPublicKey ( block . Bytes ) 
if err != nil { 
return fmt . Errorf ( "failed to parse public key: %w" , err ) 
} 
fmt . Fprintf ( w , "Retrieved public key: %v\n" , publicKey ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[PublicKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) ; 
import java.io.IOException ; 
import java.security.GeneralSecurityException ; 

public class GetPublicKey { 

public void getPublicKey () throws IOException , GeneralSecurityException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String keyId = "my-key" ; 
String keyVersionId = "123" ; 
getPublicKey ( projectId , locationId , keyRingId , keyId , keyVersionId ); 
} 

// Get the public key associated with an asymmetric key. 
public void getPublicKey ( 
String projectId , String locationId , String keyRingId , String keyId , String keyVersionId ) 
throws IOException , GeneralSecurityException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the key version name from the project, location, key ring, key, 
// and key version. 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName = 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) . of ( projectId , locationId , keyRingId , keyId , keyVersionId ); 

// Get the public key. 
[ PublicKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) publicKey = client . getPublicKey ( keyVersionName ); 
System . out . printf ( "Public key: %s%n" , publicKey . [ getPem ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html#com_google_cloud_kms_v1_PublicKey_getPem__) ()); 
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

async function getPublicKey () { 
const [ publicKey ] = await client . getPublicKey ({ 
name : versionName , 
}); 

// Optional, but recommended: perform integrity verification on publicKey. 
// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit: 
// https://cloud.google.com/kms/docs/data-integrity-guidelines 
const crc32c = require ( 'fast-crc32c' ); 
if ( publicKey . name !== versionName ) { 
throw new Error ( 'GetPublicKey: request corrupted in-transit' ); 
} 
if ( crc32c . calculate ( publicKey . pem ) !== Number ( publicKey . pemCrc32c . value )) { 
throw new Error ( 'GetPublicKey: response corrupted in-transit' ); 
} 

console . log ( `Public key pem: ${ publicKey . pem } ` ); 

return publicKey ; 
} 

return getPublicKey (); 
```








































To run this code, first learn about [using PHP on Google Cloud Dedicated](/php/docs) and
[install the Cloud KMS PHP SDK](/kms/docs/reference/libraries#client-libraries-install-php).



























```
use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient; 
use Google\Cloud\Kms\V1\GetPublicKeyRequest; 

function get_public_key( 
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
$getPublicKeyRequest = (new GetPublicKeyRequest()) 
->setName($keyVersionName); 
$publicKey = $client->getPublicKey($getPublicKeyRequest); 
printf('Public key: %s' . PHP_EOL, $publicKey->getPem()); 

return $publicKey; 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 

def get_public_key ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str , version_id : str 
) - > kms . PublicKey : 
""" 
Get the public key for an asymmetric key. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to use (e.g. 'my-key'). 
version_id (string): ID of the key to use (e.g. '1'). 

Returns: 
PublicKey: Cloud KMS public key response. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the key version name. 
key_version_name = client . [ crypto_key_version_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path) ( 
project_id , location_id , key_ring_id , key_id , version_id 
) 

# Call the API. 
public_key = client . [ get_public_key ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_public_key) ( request = { "name" : key_version_name }) 

# Optional, but recommended: perform integrity verification on public_key. 
# For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit: 
# https://cloud.google.com/kms/docs/data-integrity-guidelines 
if not public_key . name == key_version_name : 
raise Exception ( "The request sent to the server was corrupted in-transit." ) 
# See crc32c() function defined below. 
if not public_key . pem_crc32c == crc32c ( public_key . pem . encode ( "utf-8" )): 
raise Exception ( 
"The response received from the server was corrupted in-transit." 
) 
# End integrity verification 

print ( f "Public key: { public_key . pem } " ) 
return public_key 

def crc32c ( data : bytes ) - > int : 
""" 
Calculates the CRC32C checksum of the provided data. 
Args: 
data: the bytes over which the checksum should be calculated. 
Returns: 
An int representing the CRC32C checksum of the provided bytes. 
""" 
import crcmod # type: ignore 

crc32c_fun = crcmod . predefined . mkPredefinedCrcFun ( "crc-32c" ) 
return crc32c_fun ( data ) 
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
public_key = client . get_public_key name : key_version_name 
puts "Public key: #{ public_key . pem } " 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





Retrieve the public key by calling the
[CryptoKeyVersions.getPublicKey](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey)
method.


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys/ KEY_NAME /cryptoKeyVersions/ KEY_VERSION /publicKey?public_key_format= PUBLIC_KEY_FORMAT " \
--request "GET" \
--header "authorization: Bearer TOKEN "
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the key ring.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` KEY_NAME `: the name of the key.

- ` KEY_VERSION `: the key version number.

- ` PUBLIC_KEY_FORMAT `: the format in which you want to export
the public key. For PQC algorithms
([Preview](https://berlin.devsitetest.how/products#product-launch-stages)), use `NIST_PQC`. For all other
keys, you can use `PEM` or omit this parameter.

If the public key format is omitted for a non-PQC key, the output is similar to
the following:


```
{ 
"pem" : "-----BEGIN PUBLIC KEY-----\nQ29uZ3JhdHVsYXRpb25zLCB5b3UndmUgZGlzY292ZX 
JlZCB0aGF0IHRoaXMgaXNuJ3QgYWN0dWFsbHkgYSBwdWJsaWMga2V5ISBIYXZlIGEgbmlj 
ZSBkYXkgOik=\n-----END PUBLIC KEY-----\n" , 
"algorithm" : " ALGORITHM " , 
"pemCrc32c" : "2561089887" , 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /keyRings/ 
KEY_RING /cryptoKeys/ KEY_NAME /cryptoKeyVersions/
KEY_VERSION " , 
"protectionLevel" : " PROTECTION_LEVEL " 
} 
```


For a PQC algorithm with public key format `NIST_PQC`, the output is similar to
the following:


```
{ 
"publicKeyFormat" : "NIST_PQC" , 
"publicKey" : { 
"crc32cChecksum" : "1985843562" , 
"data" : "kdcOIrFCC5kN8S4i0+R+AoSc9gYIJ9jEQ6zG235ZmCQ=" 
} 
"algorithm" : " ALGORITHM " , 
"name" : "projects/ PROJECT_ID /locations/ LOCATION /keyRings/ 
KEY_RING /cryptoKeys/ KEY_NAME /cryptoKeyVersions/
KEY_VERSION " , 
"protectionLevel" : " PROTECTION_LEVEL " 
} 
```


















### Convert a public key to JWK format

Cloud KMS lets you retrieve a public key in PEM format.
Some applications might require other key formats such as JSON Web Key (JWK).
For more information about the JWK format, see [RFC 7517](https://www.rfc-editor.org/rfc/pdfrfc/rfc7517.txt.pdf).

To convert a public key to JWK format, follow these steps:

















[ Go ](#go) [ Java ](#java) [ Python ](#python) 
More 









To run this code, first [set up a Go development environment](/go/docs/setup) and
[install the Cloud KMS Go SDK](/kms/docs/reference/libraries#client-libraries-install-go).



























```
import ( 
"context" 
"crypto/x509" 
"encoding/json" 
"encoding/pem" 
"fmt" 
"hash/crc32" 
"io" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
"github.com/lestrrat-go/jwx/v2/jwk" 
) 

// getPublicKeyJwk retrieves the public key from an asymmetric key pair on Cloud KMS. 
func getPublicKeyJwk ( w io . Writer , cryptoKeyVersionName string ) error { 
// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . GetPublicKeyRequest { 
Name : cryptoKeyVersionName , 
} 

// Call the API to get the public key. 
result , err := client . GetPublicKey ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to get public key: %w" , err ) 
} 

// The 'Pem' field is the raw string representation of the public key. 
// Convert 'Pem' into bytes for further processing. 
key := [] byte ( result . Pem ) 

// Optional, but recommended: perform integrity verification on result. 
// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit: 
// https://cloud.google.com/kms/docs/data-integrity-guidelines 
crc32c := func ( data [] byte ) uint32 { 
t := crc32 . MakeTable ( crc32 . Castagnoli ) 
return crc32 . Checksum ( data , t ) 
} 
if int64 ( crc32c ( key )) != result . PemCrc32C . Value { 
return fmt . Errorf ( "getPublicKey: response corrupted in-transit" ) 
} 

// Optional - parse the public key. 
// This transforms the string key into a Go PublicKey. 
block , _ := pem . Decode ( key ) 
_ , err = x509 . ParsePKIXPublicKey ( block . Bytes ) 
if err != nil { 
return fmt . Errorf ( "failed to parse public key: %w" , err ) 
} 

// If all above checks pass, convert it into JWK format. 
jwkKey , err := jwk . ParseKey ( key , jwk . WithPEM ( true )) 
if err != nil { 
return fmt . Errorf ( "Failed to parse the PEM public key: %w" , err ) 
} 

fmt . Fprintf ( w , "The public key in JWK format: " ) 
json . NewEncoder ( w ). Encode ( jwkKey ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[PublicKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) ; 
// NOTE: The library nimbusds is NOT endorsed for anything beyond conversion to JWK. 
import com.nimbusds.jose.JOSEException ; 
import com.nimbusds.jose.jwk.JWK ; 
import java.io.IOException ; 
import java.security.GeneralSecurityException ; 

public class ConvertPublicKeyToJwk { 

public void convertPublicKey () throws IOException , GeneralSecurityException , JOSEException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String keyId = "my-key" ; 
String keyVersionId = "123" ; 
convertPublicKey ( projectId , locationId , keyRingId , keyId , keyVersionId ); 
} 

// (Get and) Convert the public key associated with an asymmetric key. 
public void convertPublicKey ( 
String projectId , String locationId , String keyRingId , String keyId , String keyVersionId ) 
throws IOException , GeneralSecurityException , JOSEException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the key version name from the project, location, key ring, key, 
// and key version. 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName = 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) . of ( projectId , locationId , keyRingId , keyId , keyVersionId ); 

// Get the public key and convert it to JWK format. 
[ PublicKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) publicKey = client . getPublicKey ( keyVersionName ); 
JWK jwk = JWK . parseFromPEMEncodedObjects ( publicKey . [ getPem ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html#com_google_cloud_kms_v1_PublicKey_getPem__) ()); 
System . out . println ( jwk . toJSONString ()); 
} 
} 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 
from jwcrypto import jwk 

def get_public_key_jwk ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str , version_id : str 
) - > kms . PublicKey : 
""" 
Get the public key of an asymmetric key in JWK format. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to use (e.g. 'my-key'). 
version_id (string): ID of the key to use (e.g. '1'). 

Returns: 
PublicKey: Cloud KMS public key response. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the key version name. 
key_version_name = client . [ crypto_key_version_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path) ( 
project_id , location_id , key_ring_id , key_id , version_id 
) 

# Call the API. 
public_key = client . [ get_public_key ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_public_key) ( request = { "name" : key_version_name }) 

# Optional, but recommended: perform integrity verification on public_key. 
# For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit: 
# https://cloud.google.com/kms/docs/data-integrity-guidelines 
if not public_key . name == key_version_name : 
raise Exception ( "The request sent to the server was corrupted in-transit." ) 
# See crc32c() function defined below. 
if not public_key . pem_crc32c == crc32c ( public_key . pem . encode ( "utf-8" )): 
raise Exception ( 
"The response received from the server was corrupted in-transit." 
) 
# End integrity verification 

# Convert to JWK format. 
jwk_key = jwk . JWK . from_pem ( public_key . pem . encode ()) 
return jwk_key . export ( private_key = False ) 

def crc32c ( data : bytes ) - > int : 
""" 
Calculates the CRC32C checksum of the provided data. 
Args: 
data: the bytes over which the checksum should be calculated. 
Returns: 
An int representing the CRC32C checksum of the provided bytes. 
""" 
import crcmod # type: ignore 

crc32c_fun = crcmod . predefined . mkPredefinedCrcFun ( "crc-32c" ) 
return crc32c_fun ( data ) 
```




















### Control access to asymmetric keys

A signer or validator requires the appropriate permission or role on the
asymmetric key.

- 

For a user or service that will perform signing, grant the
`cloudkms.cryptoKeyVersions.useToSign` permission on the asymmetric key.

- 

For a user or service that will retrieve the public key, grant the
`cloudkms.cryptoKeyVersions.viewPublicKey` on the asymmetric key. The public key
is required for signature validation.

Learn about permissions and roles in Cloud KMS release at
[Permissions and roles](/kms/docs/reference/permissions-and-roles).

## Create a MAC signing key












[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [API](#api) 
More 










- 

In the Google Cloud Dedicated console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring for which you will create a key.

- 

Click **Create key**.

- 

For **Key name**, enter a name for your key.

- 

For **Protection level**, select **Software**.

- 

For **Key material**, select **Generated key**.

- 

For **Purpose**, select **MAC signing/verification**.

- 

Optional: for **Algorithm**, select an [HMAC signing
algorithm](/kms/docs/algorithms#mac_signing_algorithms).

- 

Click **Create**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).





To create a software key, use the `kms keys create` command:


```
gcloud kms keys create KEY_NAME \
--keyring KEY_RING \
--location LOCATION \
--purpose "mac" \
--default-algorithm " ALGORITHM "
```


Replace the following:

- ` KEY_NAME `: the name of the key.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` ALGORITHM `: the HMAC signing algorithm—for example,
`hmac-sha256`. To see all supported HMAC algorithms, see [HMAC signing
algorithms](/kms/docs/algorithms#hmac_signing_algorithms).

For the details on all flags and possible values, run the command with the
`--help` flag.






































To run this code, first [set up a C# development environment](/dotnet/docs/setup) and
[install the Cloud KMS C# SDK](/kms/docs/reference/libraries#client-libraries-install-csharp).



























```
using [ Google.Cloud.Kms.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html) ; 
using [ Google.Protobuf.WellKnownTypes ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html) ; 

public class CreateKeyMacSample 
{ 
public CryptoKey CreateKeyMac ( 
string projectId = "my-project" , string locationId = "us-east1" , string keyRingId = "my-key-ring" , 
string id = "my-mac-key" ) 
{ 
// Create the client. 
[ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create) (); 

// Build the parent key ring name. 
[ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) keyRingName = new [ KeyRingName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) ( projectId , locationId , keyRingId ); 

// Build the key. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
{ 
Purpose = [ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html) . [ Mac ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html#Google_Cloud_Kms_V1_CryptoKey_Types_CryptoKeyPurpose_Mac) , 
VersionTemplate = new [ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate.html)
{ 
Algorithm = [ CryptoKeyVersion ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) . [ Types ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html) . [ HmacSha256 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionAlgorithm_HmacSha256) , 
}, 

// Optional: customize how long key versions should be kept before destroying. 
DestroyScheduledDuration = new [ Duration ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
{ 
Seconds = 24 * 60 * 60 , 
} 
}; 

// Call the API. 
[ CryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client . [ CreateCryptoKey ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateCryptoKey_Google_Cloud_Kms_V1_CreateCryptoKeyRequest_Google_Api_Gax_Grpc_CallSettings_) ( keyRingName , id , key ); 

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
"time" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
"google.golang.org/protobuf/types/known/durationpb" 
) 

// createKeyMac creates a new key for use with MacSign. 
func createKeyMac ( w io . Writer , parent , id string ) error { 
// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring" 
// id := "my-mac-key" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . CreateCryptoKeyRequest { 
Parent : parent , 
CryptoKeyId : id , 
CryptoKey : & kmspb . CryptoKey { 
Purpose : kmspb . [ CryptoKey_MAC ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKey_CRYPTO_KEY_PURPOSE_UNSPECIFIED_CryptoKey_ENCRYPT_DECRYPT_CryptoKey_ASYMMETRIC_SIGN_CryptoKey_ASYMMETRIC_DECRYPT_CryptoKey_RAW_ENCRYPT_DECRYPT_CryptoKey_MAC_CryptoKey_KEY_ENCAPSULATION) , 
VersionTemplate : & kmspb . CryptoKeyVersionTemplate { 
Algorithm : kmspb . [ CryptoKeyVersion_HMAC_SHA256 ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU) , 
}, 

// Optional: customize how long key versions should be kept before destroying. 
DestroyScheduledDuration : durationpb . New ( 24 * time . Hour ), 
}, 
} 

// Call the API. 
result , err := client . CreateCryptoKey ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to create key: %w" , err ) 
} 
fmt . Fprintf ( w , "Created key: %s\n" , result . Name ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) ; 
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[KeyRingName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) ; 
import java.io.IOException ; 

public class CreateKeyMac { 

public void createKeyMac () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String id = "my-mac-key" ; 
createKeyMac ( projectId , locationId , keyRingId , id ); 
} 

// Create a new key for use with MacSign. 
public void createKeyMac ( String projectId , String locationId , String keyRingId , String id ) 
throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the parent name from the project, location, and key ring. 
[ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) . of ( projectId , locationId , keyRingId ); 

// Build the mac key to create. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key = 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) . newBuilder () 
. [ setPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_) ( [ CryptoKeyPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) . MAC ) 
. [ setVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_) ( 
[ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) . newBuilder () 
. setAlgorithm ( [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . HMAC_SHA256 )) 
. build (); 

// Create the key. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client . createCryptoKey ( keyRingName , id , key ); 
System . out . printf ( "Created mac key %s%n" , createdKey . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__) ()); 
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
// const id = 'my-mac-key'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the parent key ring name 
const keyRingName = client . keyRingPath ( projectId , locationId , keyRingId ); 

async function createKeyMac () { 
const [ key ] = await client . createCryptoKey ({ 
parent : keyRingName , 
cryptoKeyId : id , 
cryptoKey : { 
purpose : 'MAC' , 
versionTemplate : { 
algorithm : 'HMAC_SHA256' , 
}, 

// Optional: customize how long key versions should be kept before 
// destroying. 
destroyScheduledDuration : { seconds : 60 * 60 * 24 }, 
}, 
}); 

console . log ( `Created mac key: ${ key . name } ` ); 
return key ; 
} 

return createKeyMac (); 
```








































To run this code, first learn about [using PHP on Google Cloud Dedicated](/php/docs) and
[install the Cloud KMS PHP SDK](/kms/docs/reference/libraries#client-libraries-install-php).



























```
use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient; 
use Google\Cloud\Kms\V1\CreateCryptoKeyRequest; 
use Google\Cloud\Kms\V1\CryptoKey; 
use Google\Cloud\Kms\V1\CryptoKey\CryptoKeyPurpose; 
use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionAlgorithm; 
use Google\Cloud\Kms\V1\CryptoKeyVersionTemplate; 
use Google\Protobuf\Duration; 

function create_key_mac( 
string $projectId = 'my-project', 
string $locationId = 'us-east1', 
string $keyRingId = 'my-key-ring', 
string $id = 'my-mac-key' 
): CryptoKey { 
// Create the Cloud KMS client. 
$client = new KeyManagementServiceClient(); 

// Build the parent key ring name. 
$keyRingName = $client->keyRingName($projectId, $locationId, $keyRingId); 

// Build the key. 
$key = (new CryptoKey()) 
->setPurpose(CryptoKeyPurpose::MAC) 
->setVersionTemplate((new CryptoKeyVersionTemplate()) 
->setAlgorithm(CryptoKeyVersionAlgorithm::HMAC_SHA256) 
) 

// Optional: customize how long key versions should be kept before destroying. 
->setDestroyScheduledDuration((new Duration()) 
->setSeconds(24 * 60 * 60) 
); 

// Call the API. 
$createCryptoKeyRequest = (new CreateCryptoKeyRequest()) 
->setParent($keyRingName) 
->setCryptoKeyId($id) 
->setCryptoKey($key); 
$createdKey = $client->createCryptoKey($createCryptoKeyRequest); 
printf('Created mac key: %s' . PHP_EOL, $createdKey->getName()); 

return $createdKey; 
} 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
import datetime 

from google.cloud import kms 
from google.protobuf import duration_pb2 # type: ignore 

def create_key_mac ( 
project_id : str , location_id : str , key_ring_id : str , key_id : str 
) - > kms . CryptoKey : 
""" 
Creates a new key in Cloud KMS for HMAC operations. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
key_id (string): ID of the key to create (e.g. 'my-mac-key'). 

Returns: 
CryptoKey: Cloud KMS key. 

""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path) ( project_id , location_id , key_ring_id ) 

# Build the key. 
purpose = kms . [ CryptoKey ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html) . MAC 
algorithm = kms . [ CryptoKeyVersion ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . HMAC_SHA256 
key = { 
"purpose" : purpose , 
"version_template" : { 
"algorithm" : algorithm , 
}, 
# Optional: customize how long key versions should be kept before 
# destroying. 
"destroy_scheduled_duration" : duration_pb2 . Duration () . FromTimedelta ( 
datetime . timedelta ( days = 1 ) 
), 
} 

# Call the API. 
created_key = client . [ create_crypto_key ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key) ( 
request = { "parent" : key_ring_name , "crypto_key_id" : key_id , "crypto_key" : key } 
) 
print ( f "Created mac key: { created_key . name } " ) 
return created_key 
```









































To run this code, first [set up a Ruby development environment](/ruby/docs/setup) and
[install the Cloud KMS Ruby SDK](/kms/docs/reference/libraries#client-libraries-install-ruby).



























```
# TODO(developer): uncomment these values before running the sample. 
# project_id = "my-project" 
# location_id = "us-east1" 
# key_ring_id = "my-key-ring" 
# id = "my-mac-key" 

# Require the library. 
require "google/cloud/kms" 

# Create the client. 
client = Google :: Cloud :: [ Kms ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html) . [ key_management_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project : project_id , location : location_id , key_ring : key_ring_id 

# Build the key. 
key = { 
purpose : :MAC , 
version_template : { 
algorithm : :HMAC_SHA256 
} 
} 

# Call the API. 
created_key = client . create_crypto_key parent : key_ring_name , crypto_key_id : id , crypto_key : key 
puts "Created mac key: #{ created_key . name } " 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





To create a software key, use the
[`CryptoKey.create`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create)
method:


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys?crypto_key_id= KEY_NAME " \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--data '{"purpose": "MAC", "versionTemplate": { "protectionLevel": "SOFTWARE", "algorithm": " ALGORITHM " }}'
```


Replace the following:

- ` PROJECT_ID `: the ID of the project that contains the key ring.

- ` LOCATION `: the Cloud KMS location of the key ring.

- ` KEY_RING `: the name of the key ring that contains the key.

- ` KEY_NAME `: the name of the key.

- ` ALGORITHM `: the HMAC signing algorithm, for example `HMAC_SHA256`.
To see all supported HMAC algorithms, see [HMAC signing
algorithms](/kms/docs/algorithms#hmac_signing_algorithms).

















## What's next

- Learn about [key rotation](/kms/docs/rotate-key).

- Learn about [Creating and validating
signatures](/kms/docs/create-validate-signatures).

- Learn about [Encrypting and decrypting data with an RSA
key](/kms/docs/encrypt-decrypt-rsa).

- Learn about [Retrieving a public key](/kms/docs/retrieve-public-key).