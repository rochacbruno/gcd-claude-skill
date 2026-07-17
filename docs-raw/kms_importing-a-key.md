# Import a key version into Cloud KMS

Source: https://berlin.devsitetest.how/kms/docs/importing-a-key
Last updated: 2026-07-15

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












# Import a key version into Cloud KMS 






- On this page ** 
- [ Before you begin ](#before_you_begin)

- [ Preparing the project ](#preparing_the_project)
- [ Preparing the local system ](#preparing_the_local_system)
- [ Preparing the key ](#preparing_the_key)

- [ Create the target key and key ring ](#create_targets)
- [ Create the import job ](#create_importjob)

- [ Checking the state of the import job ](#check_import_job)
- [ Preventing modification of import jobs ](#prevent_import_job_modification)

- [ Import the key ](#request_import)

- [ Automatically wrapping and importing a key ](#automatically_wrap_and_import)
- [ Importing a manually-wrapped key ](#importing_a_manually-wrapped_key)
- [ Check the state of the imported key version ](#check_imported_key)

- [ Re-import a previously destroyed key ](#re-import_a_previously_destroyed_key)

- [ Restrictions ](#restrictions)
- [ Re-importing a destroyed key ](#re-importing_a_destroyed_key)

- [ What's next ](#whats_next)
- 









This guide shows you how to import a cryptographic key
into Cloud HSM or Cloud Key Management Service as a new key version.

For more details about importing keys, including limitations and
restrictions, see [key import](/kms/docs/key-import).

You can complete the steps in this guide in 5 to 10 minutes, not including the
[Before you begin](#before_you_begin) steps. Wrapping the key manually adds
complexity to the task.

## Before you begin 

We recommend that you create a new project to test this feature, to ease
clean-up after testing and to ensure that you have adequate
Identity and Access Management (IAM) permissions to import a key.

Before you can import a key, you need to prepare the project, the local system,
and the key itself.

### Preparing the project




















- 





In the Google Cloud Dedicated console, on the project selector page,
select or create a Google Cloud Dedicated project.




Roles required to select or create a project**





- 
**Select a project**: Selecting a project doesn't require a specific
IAM role—you can select any project that you've been
granted a role on.


- 
**Create a project**: To create a project, you need the Project Creator role
(`roles/resourcemanager.projectCreator`), which contains the
`resourcemanager.projects.create` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).












[Go to project selector](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)


















- 



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the required API.






**Roles required to enable APIs**


To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https%3A//console.cloud.google.com)
















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).







- 


To [initialize](/sdk/docs/initializing) the gcloud CLI, run the following command:



```
gcloud init
```





















- 


The user performing the import needs the following IAM
permissions to create key rings, keys, and import jobs. If the user is not
the project owner, you can assign **both** of the following two predefined
roles to the user:




- `roles/editor`

- `roles/cloudkms.importer`




For more information about available IAM roles and
permissions for Cloud KMS, refer to
[Permissions and
roles](/kms/docs/reference/permissions-and-roles).


### Preparing the local system

Prepare the local system by choosing **one** of the following options. Automatic
key wrapping is recommended for most users.

- **If you want to allow the Google Cloud CLI to wrap your keys automatically**
before transmitting them to Google Cloud Dedicated in Germany, you must
[install the Pyca cryptography library](/kms/docs/crypto)
on your local system. The Pyca library is used by the import job that
wraps and protects the key locally before sending it to Google Cloud Dedicated.

- **If you want to wrap your keys manually**, you must
[configure
OpenSSL for manual key wrapping](/kms/docs/configuring-openssl-for-manual-key-wrapping).

### Preparing the key

Verify that your key's [algorithm and length](/kms/docs/algorithms) are
supported. Allowable algorithms for a key depend upon whether the key is
used for symmetric encryption, asymmetric encryption or asymmetric signing, as
well as whether the key is stored in software or an HSM. You specify the key's
algorithm as part of the [import request](#request_import).

Separately, you must also
[verify how the key is encoded](/kms/docs/formatting-keys-for-import),
and make adjustments if necessary.

The following can't be changed for a key version after it is created or
imported:

- 

The **protection level** indicates whether the key persists in software, in
a multi-tenant HSM, in a single-tenant HSM, or in an external key management
system. Key material cannot be moved from one of these storage environments
to another. All versions of a key have the same protection level.

- 

The **purpose** indicates whether versions of the key are used for symmetric
encryption, asymmetric encryption, or asymmetric signing. The purpose of the
key limits the possible algorithms that can be used to create versions of
that key. All versions of a key have the same purpose.

If you don't have a key to import but want to validate the procedure for
importing keys, you can create a symmetric key on the local system, using the
following command:


```
openssl rand 32 > ${HOME}/test.bin
```


Use this key for testing only. A key created this way might not be appropriate
for production use.

If you need to [wrap the key manually](/kms/docs/wrapping-a-key),
do that before continuing with the procedures in this guide.

## Create the target key and key ring

A Cloud KMS key is a container object that contains zero or more
*key versions*. Each key version contains a cryptographic key.

When you import a key into Cloud KMS or Cloud HSM, the
imported key becomes a new key version on an existing Cloud KMS or
Cloud HSM key. In the rest of this guide, this key is called the
*target key*. The target key must exist before you can import key material into
it.

Importing a key version has no effect on that key's existing versions. However,
It is recommended to create an empty key when testing key import. An empty key
has no version, isn't active, and can't be used.

You may optionally specify that your newly created key may only contain imported
versions, which prevents accidental generation of new versions in
Cloud KMS.

A key exists on a key ring; in this guide, this key ring is called the
*target key ring*. The location of the target key ring determines the location
where the key material is available after import. Cloud HSM keys cannot
be created or imported in some [locations](/kms/docs/locations). After a key is
created, it cannot be moved to a different key ring or location.

Follow these steps to create an empty key on a new key ring using the
Google Cloud CLI or the Google Cloud Dedicated console.












[Console](#console) [ gcloud ](#gcloud) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ Python ](#python) [API](#api) 
More 










- 

In the Google Cloud Dedicated console, go to the
**Key Management** page.



[Go to Key Management](https://console.cloud.berlin-build0.goog/security/kms)

- 

Click **Create key ring**.

- 

In the **Key ring name** field, enter the name for your key ring.

- 

Under **Location type**, select a location type and location.

- 

Click **Create**. The **Create key** page opens.

- 

In the **Key name** field, enter the name for your key.

- 

For **Protection level**, select **Software**.

- 

For **Key material**, select **Imported key** and then click **Continue**.
This prevents an initial key version from being created.

- 

Set the **Purpose** and **Algorithm** for the key and then click
**Continue**.

- 

Optional: If you want this key to contain only imported key versions,
select **Restrict key versions to import only**. This prevents you from
accidentally creating new key versions in Cloud KMS.

- 

Optional: For imported keys, automatic rotation is disabled by default.
To enable automatic rotation, select a value from the **Key rotation
period** field.

If you enable automatic rotation, new key versions will be generated in
Cloud KMS, and the imported key version will no longer
be the default key version after a rotation.

- 

Click **Create**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).





- 

Create the target key ring. Choose a location that is compatible with the
protection level that you want to use. For more information about supported
locations, see [Cloud KMS locations](/kms/docs/locations).


```
gcloud kms keyrings create KEY_RING \
--location LOCATION 
```


You can learn more about
[creating key rings](/kms/docs/creating-keys#create_a_key_ring).

- 

Create the target key using the `kms keys create` command with the
`--skip-initial-version-creation` flag. This creates a key with no initial
key version so that your imported key material is version `1`. Use the
`--import-only` flag to prevent Cloud KMS from generating key
material for new key versions. With this flag set, new key versions for this
key must be imported. Keys created as `--import-only` must be rotated
manually.


```
gcloud kms keys create KEY_NAME \
--location LOCATION \
--keyring KEY_RING \
--purpose PURPOSE \
--skip-initial-version-creation \
--import-only
```


Replace the following:

- ` KEY_NAME `: the name that you want to use for the key.

- ` LOCATION `: the location of the key ring.

- ` KEY_RING `: the key ring where you want to create the key.

- ` PURPOSE `: the [purpose](/kms/docs/algorithms#key_purposes) that
you want to use for the key.





































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

// createKeyForImport creates a new asymmetric signing key in Cloud HSM. 
func createKeyForImport ( w io . Writer , parent , id string ) error { 
// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring" 
// id := "my-imported-key" 

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
ProtectionLevel : kmspb . [ ProtectionLevel_HSM ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_ProtectionLevel_PROTECTION_LEVEL_UNSPECIFIED_ProtectionLevel_SOFTWARE_ProtectionLevel_HSM_ProtectionLevel_EXTERNAL_ProtectionLevel_EXTERNAL_VPC_ProtectionLevel_HSM_SINGLE_TENANT) , 
Algorithm : kmspb . [ CryptoKeyVersion_EC_SIGN_P256_SHA256 ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU) , 
}, 
// Ensure that only imported versions may be added to this key. 
ImportOnly : true , 
}, 
SkipInitialVersionCreation : true , 
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
import com.google.cloud.kms.v1.[CreateCryptoKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest.html) ; 
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) ; 
import com.google.cloud.kms.v1.[CryptoKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[KeyRingName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) ; 
import com.google.cloud.kms.v1.[ProtectionLevel](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html) ; 
import java.io.IOException ; 

public class CreateKeyForImport { 

public void createKeyForImport () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String id = "my-import-key" ; 
createKeyForImport ( projectId , locationId , keyRingId , id ); 
} 

// Create a new crypto key to hold imported key versions. 
public void createKeyForImport ( String projectId , String locationId , String keyRingId , String id ) 
throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the parent name from the project, location, and key ring. 
[ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) . of ( projectId , locationId , keyRingId ); 

// Create the crypto key. 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = 
client . createCryptoKey ( 
[ CreateCryptoKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest.html) . newBuilder () 
. setParent ( keyRingName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html#com_google_cloud_kms_v1_KeyRingName_toString__) ()) 
. [ setCryptoKeyId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest.Builder.html#com_google_cloud_kms_v1_CreateCryptoKeyRequest_Builder_setCryptoKeyId_java_lang_String_) ( id ) 
. setCryptoKey ( 
[ CryptoKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) . newBuilder () 
. [ setPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_) ( [ CryptoKeyPurpose ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html) . ASYMMETRIC_SIGN ) 
. [ setVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_) ( 
[ CryptoKeyVersionTemplate ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html) . newBuilder () 
. setProtectionLevel ( [ ProtectionLevel ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html) . HSM ) 
. setAlgorithm ( [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . EC_SIGN_P256_SHA256 )) 
// Ensure that only imported versions may be 
// added to this key. 
. [ setImportOnly ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setImportOnly_boolean_) ( true )) 
. [ setSkipInitialVersionCreation ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest.Builder.html#com_google_cloud_kms_v1_CreateCryptoKeyRequest_Builder_setSkipInitialVersionCreation_boolean_) ( true ) 
. build ()); 

System . out . printf ( "Created crypto key %s%n" , createdKey . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__) ()); 
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
// const id = 'my-imported-key'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the parent key ring name 
const keyRingName = client . keyRingPath ( projectId , locationId , keyRingId ); 

async function createKeyForImport () { 
const [ key ] = await client . createCryptoKey ({ 
parent : keyRingName , 
cryptoKeyId : id , 
cryptoKey : { 
purpose : 'ENCRYPT_DECRYPT' , 
versionTemplate : { 
algorithm : 'GOOGLE_SYMMETRIC_ENCRYPTION' , 
protectionLevel : 'HSM' , 
}, 
// Optional: ensure that only imported versions may be added to this 
// key. 
importOnly : true , 
}, 
// Do not allow KMS to generate an initial version of this key. 
skipInitialVersionCreation : true , 
}); 

console . log ( `Created key for import: ${ key . name } ` ); 
return key ; 
} 

return createKeyForImport (); 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 

def create_key_for_import ( 
project_id : str , location_id : str , key_ring_id : str , crypto_key_id : str 
) - > None : 
""" 

Sets up an empty CryptoKey within a KeyRing for import. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
crypto_key_id (string): ID of the key to import (e.g. 'my-asymmetric-signing-key'). 
""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Build the key. For more information regarding allowed values of these fields, see: 
# https://googleapis.dev/python/cloudkms/latest/_modules/google/cloud/kms_v1/types/resources.html 
purpose = kms . [ CryptoKey ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html) . [ CryptoKeyPurpose ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html) . ASYMMETRIC_SIGN 
algorithm = kms . [ CryptoKeyVersion ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . EC_SIGN_P256_SHA256 
protection_level = kms . [ ProtectionLevel ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ProtectionLevel.html) . HSM 
key = { 
"purpose" : purpose , 
"version_template" : { 
"algorithm" : algorithm , 
"protection_level" : protection_level , 
}, 
} 

# Build the parent key ring name. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path) ( project_id , location_id , key_ring_id ) 

# Call the API. 
created_key = client . [ create_crypto_key ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key) ( 
request = { 
"parent" : key_ring_name , 
"crypto_key_id" : crypto_key_id , 
"crypto_key" : key , 
# Do not allow KMS to generate an initial version of this key. 
"skip_initial_version_creation" : True , 
} 
) 
print ( f "Created hsm key: { created_key . name } " ) 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





- 

Create a new key ring:


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings?keyRingId= KEY_RING " \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--header "x-goog-user-project: PROJECT_ID " \
--data "{}"
```


See the [`KeyRing.create` API documentation](/kms/docs/reference/rest/v1/projects.locations.keyRings/create)
for more information.

- 

Create an empty, import-only key:


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys?cryptoKeyId= KEY_NAME &skipInitialVersionCreation=true" \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--header "x-goog-user-project: PROJECT_ID " \
--data "{"purpose":" PURPOSE ", "importOnly": "true", "versionTemplate":{"protectionLevel":" PROTECTION_LEVEL ","algorithm":" ALGORITHM "}}"
```


See the [`CryptoKey.create` API documentation](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create)
for more information.

















The key ring and key now exist, but the key contains no key material, has no
version, and is not active. Next, you
[create an import job](#create_importjob).

## Create the import job

An [import job](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs) defines the characteristics of the keys it
imports, including properties that cannot be changed after the key is imported.

The [protection level](/kms/docs/algorithms#protection_levels) defines whether
keys imported by this import job will reside in software, in a multi-tenant HSM,
in a single-tenant HSM, or in an external key management system. The protection
level can't be changed after the key is eventually [imported](#request_import).

The [import method](/kms/docs/key-wrapping#import_methods) defines the
algorithm used to create the wrapping key that protects imported keys during
transit from your local system to the target Google Cloud Dedicated project. You
can choose a 3072-bit or a 4096- bit RSA key. Unless you have specific
requirements, the 3072-bit wrapping key is recommended.

You can create an import job using the gcloud CLI, the
Google Cloud Dedicated console, or the Cloud Key Management Service API.












[Console](#console) [ gcloud ](#gcloud) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ Python ](#python) [API](#api) 
More 










- 

Go to the **Key Management** page in the Google Cloud Dedicated console.

[Go to the Key Management page](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the target key ring.

- 

Set the **Protection level** to **Software**.

- 

Click **Create import job**.

- 

In the **Name** field, enter the name for your import job.

- 

From the **Import method** dropdown, set the import method to either
**3072 bit RSA** or **4096 bit RSA**.

- 

Click **Create**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).





Use a command like the following to create an import job.


```
gcloud kms import-jobs create IMPORT_JOB \
--location LOCATION \
--keyring KEY_RING \
--import-method IMPORT_METHOD \
--protection-level PROTECTION_LEVEL 
```


- Use the same key ring and location as the target key.

- Set the protection level to the same value you used for your target key.

- Set the import method to one of the following:

- `rsa-oaep-3072-sha1-aes-256`

- `rsa-oaep-4096-sha1-aes-256`

- `rsa-oaep-3072-sha256-aes-256`

- `rsa-oaep-4096-sha256-aes-256`

- `rsa-oaep-3072-sha256`

- `rsa-oaep-4096-sha256`





































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

// createImportJob creates a new job for importing keys into KMS. 
func createImportJob ( w io . Writer , parent , id string ) error { 
// parent := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring" 
// id := "my-import-job" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Build the request. 
req := & kmspb . CreateImportJobRequest { 
Parent : parent , 
ImportJobId : id , 
ImportJob : & kmspb . ImportJob { 
// See allowed values and their descriptions at 
// https://cloud.google.com/kms/docs/algorithms#protection_levels 
ProtectionLevel : kmspb . [ ProtectionLevel_HSM ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_ProtectionLevel_PROTECTION_LEVEL_UNSPECIFIED_ProtectionLevel_SOFTWARE_ProtectionLevel_HSM_ProtectionLevel_EXTERNAL_ProtectionLevel_EXTERNAL_VPC_ProtectionLevel_HSM_SINGLE_TENANT) , 
// See allowed values and their descriptions at 
// https://cloud.google.com/kms/docs/key-wrapping#import_methods 
ImportMethod : kmspb . [ ImportJob_RSA_OAEP_3072_SHA1_AES_256 ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_ImportJob_IMPORT_METHOD_UNSPECIFIED_ImportJob_RSA_OAEP_3072_SHA1_AES_256_ImportJob_RSA_OAEP_4096_SHA1_AES_256_ImportJob_RSA_OAEP_3072_SHA256_AES_256_ImportJob_RSA_OAEP_4096_SHA256_AES_256_ImportJob_RSA_OAEP_3072_SHA256_ImportJob_RSA_OAEP_4096_SHA256_ImportJob_HPKE_KEM_ML_KEM_768_HKDF_SHA256_AES_256_GCM_ImportJob_HPKE_KEM_ML_KEM_1024_HKDF_SHA256_AES_256_GCM_ImportJob_HPKE_KEM_XWING_HKDF_SHA256_AES_256_GCM) , 
}, 
} 

// Call the API. 
result , err := client . CreateImportJob ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to create import job: %w" , err ) 
} 
fmt . Fprintf ( w , "Created import job: %s\n" , result . Name ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[ImportJob](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) ; 
import com.google.cloud.kms.v1.[ImportJob](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html).[ImportMethod](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.ImportMethod.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.cloud.kms.v1.[KeyRingName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) ; 
import com.google.cloud.kms.v1.[ProtectionLevel](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html) ; 
import java.io.IOException ; 

public class CreateImportJob { 

public void createImportJob () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String id = "my-import-job" ; 
createImportJob ( projectId , locationId , keyRingId , id ); 
} 

// Create a new import job. 
public void createImportJob ( String projectId , String locationId , String keyRingId , String id ) 
throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the parent name from the project, location, and key ring. 
[ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [ KeyRingName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) . of ( projectId , locationId , keyRingId ); 

// Build the import job to create, with parameters. 
[ ImportJob ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) importJob = 
[ ImportJob ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) . newBuilder () 
// See allowed values and their descriptions at 
// https://cloud.google.com/kms/docs/algorithms#protection_levels 
. setProtectionLevel ( [ ProtectionLevel ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html) . HSM ) 
// See allowed values and their descriptions at 
// https://cloud.google.com/kms/docs/key-wrapping#import_methods 
. [ setImportMethod ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.Builder.html#com_google_cloud_kms_v1_ImportJob_Builder_setImportMethod_com_google_cloud_kms_v1_ImportJob_ImportMethod_) ( [ ImportMethod ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.ImportMethod.html) . RSA_OAEP_3072_SHA1_AES_256 ) 
. build (); 

// Create the import job. 
[ ImportJob ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) createdImportJob = client . createImportJob ( keyRingName , id , importJob ); 
System . out . printf ( "Created import job %s%n" , createdImportJob . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html#com_google_cloud_kms_v1_ImportJob_getName__) ()); 
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
// const id = 'my-import-job'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the parent key ring name 
const keyRingName = client . keyRingPath ( projectId , locationId , keyRingId ); 

async function createImportJob () { 
const [ importJob ] = await client . createImportJob ({ 
parent : keyRingName , 
importJobId : id , 
importJob : { 
protectionLevel : 'HSM' , 
importMethod : 'RSA_OAEP_3072_SHA256' , 
}, 
}); 

console . log ( `Created import job: ${ importJob . name } ` ); 
return importJob ; 
} 

return createImportJob (); 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 

def create_import_job ( 
project_id : str , location_id : str , key_ring_id : str , import_job_id : str 
) - > None : 
""" 
Create a new import job in Cloud KMS. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
import_job_id (string): ID of the import job (e.g. 'my-import-job'). 
""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Retrieve the fully-qualified key_ring string. 
key_ring_name = client . [ key_ring_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path) ( project_id , location_id , key_ring_id ) 

# Set paramaters for the import job, allowed values for ImportMethod and ProtectionLevel found here: 
# https://googleapis.dev/python/cloudkms/latest/_modules/google/cloud/kms_v1/types/resources.html 

import_method = kms . [ ImportJob ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ImportJob.html) . [ ImportMethod ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ImportJob.ImportMethod.html) . RSA_OAEP_3072_SHA1_AES_256 
protection_level = kms . [ ProtectionLevel ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ProtectionLevel.html) . HSM 
import_job_params = { 
"import_method" : import_method , 
"protection_level" : protection_level , 
} 

# Call the client to create a new import job. 
import_job = client . [ create_import_job ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_import_job) ( 
{ 
"parent" : key_ring_name , 
"import_job_id" : import_job_id , 
"import_job" : import_job_params , 
} 
) 

print ( f "Created import job: { import_job . name } " ) 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





To create an import job, use the
[`ImportJobs.create`](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create)
method:


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /importJobs?import_job_id= IMPORT_JOB_ID " \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--data '{"import_method": " IMPORT_METHOD ", "protection_level": " PROTECTION_LEVEL "}'
```


Replace the following:

- IMPORT_METHOD : a supported [key-wrapping method](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#importmethod).

- PROTECTION_LEVEL : the [protection
level](/kms/docs/reference/rest/v1/ProtectionLevel) of the key versions
imported by this import job.


















### Checking the state of the import job

The initial state for an import job is `PENDING_GENERATION`. When the state is
`ACTIVE`, you can use it to import keys.

An import job expires after three days. If the import job is expired, you must
create a new one.

You can check the status of an import job using the Google Cloud CLI, the
Google Cloud Dedicated console, or the Cloud Key Management Service API.












[Console](#console) [ gcloud ](#gcloud) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ Python ](#python) [API](#api) 
More 










- 

Go to the **Key Management** page in the Google Cloud Dedicated console.

[Go to the Key Management page](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring that contains your import job.

- 

Click the **Import Jobs** tab at the top of the page.

- 

The state will be visible under **Status** next to your import job's
name.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).





When an import job is active, you can use it to import keys. This may
take a few minutes. Use this command to verify that the import job is
active. Use the location and keyring where you created the import job.


```
gcloud kms import-jobs describe IMPORT_JOB \
--location LOCATION \
--keyring KEY_RING \
--format="value(state)"
```


The output is similar to the following:


```
state: ACTIVE
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

// checkStateImportJob checks the state of an ImportJob in KMS. 
func checkStateImportJob ( w io . Writer , name string ) error { 
// name := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring/importJobs/my-import-job" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Call the API. 
result , err := client . GetImportJob ( ctx , & kmspb . GetImportJobRequest { 
Name : name , 
}) 
if err != nil { 
return fmt . Errorf ( "failed to get import job: %w" , err ) 
} 
fmt . Fprintf ( w , "Current state of import job %q: %s\n" , result . Name , result . State ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[ImportJob](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) ; 
import com.google.cloud.kms.v1.[ImportJobName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import java.io.IOException ; 

public class CheckStateImportJob { 

public void checkStateImportJob () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String importJobId = "my-import-job" ; 
checkStateImportJob ( projectId , locationId , keyRingId , importJobId ); 
} 

// Check the state of an import job in Cloud KMS. 
public void checkStateImportJob ( 
String projectId , String locationId , String keyRingId , String importJobId ) 
throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the parent name from the project, location, and key ring. 
[ ImportJobName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html) importJobName = [ ImportJobName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html) . of ( projectId , locationId , keyRingId , importJobId ); 

// Retrieve the state of an existing import job. 
[ ImportJob ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) importJob = client . getImportJob ( importJobName ); 
System . out . printf ( 
"Current state of import job %s: %s%n" , importJob . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html#com_google_cloud_kms_v1_ImportJob_getName__) (), importJob . [ getState ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html#com_google_cloud_kms_v1_ImportJob_getState__) ()); 
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
// const importJobId = 'my-import-job'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the import job name 
const importJobName = client . importJobPath ( 
projectId , 
locationId , 
keyRingId , 
importJobId 
); 

async function checkStateImportJob () { 
const [ importJob ] = await client . getImportJob ({ 
name : importJobName , 
}); 

console . log ( 
`Current state of import job ${ importJob . name } : ${ importJob . state } ` 
); 
return importJob ; 
} 

return checkStateImportJob (); 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 

def check_state_import_job ( 
project_id : str , location_id : str , key_ring_id : str , import_job_id : str 
) - > None : 
""" 
Check the state of an import job in Cloud KMS. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
import_job_id (string): ID of the import job (e.g. 'my-import-job'). 
""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Retrieve the fully-qualified import_job string. 
import_job_name = client . [ import_job_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_import_job_path) ( 
project_id , location_id , key_ring_id , import_job_id 
) 

# Retrieve the state from an existing import job. 
import_job = client . [ get_import_job ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_import_job) ( name = import_job_name ) 

print ( f "Current state of import job { import_job . name } : { import_job . state } " ) 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





To check the state of an import job, use the
[`ImportJobs.get`](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get)
method:


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /importJobs/ IMPORT_JOB_ID " \
--request "GET" \
--header "authorization: Bearer TOKEN "
```


















As soon as the import job is active, you can
[make a request to import a key](#request_import).

### Preventing modification of import jobs

The import job determines many characteristics of the imported key, including
the key's algorithm and whether an imported key is an HSM key or a software
key. You can configure IAM permissions to prevent users from
**creating** import jobs, while allowing them to **use** import jobs to import
keys.

- Grant the `importjobs.create` permission only to key administrators.

- Grant the `importjobs.useToImport` permission for a specific import job to
the operator who will use that job to import keys.

- When you create the import job, specify the protection level and algorithm
for key versions imported using it.

Until the import job expires, users who have the `importjobs.useToImport` and
do not have the `importjobs.create` permission for a given import job can import
keys, but cannot modify the characteristics of the import job.

## Import the key

After [checking the status of the import job](#check_import_job), you can make
an import request.

You use different flags to make the import request, depending on whether you
want the Google Cloud CLI to wrap your key automatically or if you have already
[wrapped your key manually](/kms/docs/wrapping-a-key).

Regardless of whether you wrapped your key manually or automatically, you must
set the [algorithm](/kms/docs/algorithms) to a supported algorithm that matches
the length of the actual key to be imported, and specifies the key's purpose.

- 

Keys with purpose `ENCRYPT_DECRYPT` use the `google-symmetric-encryption`
algorithm, and have a length of 32.

- 

Keys with purpose `ASYMMETRIC_DECRYPT` or `ASYMMETRIC_SIGN` support a variety
of algorithms and lengths.

A key's purpose cannot be changed after the key is created, but subsequent key
versions can be created at different lengths than the initial key version.

### Automatically wrapping and importing a key

If you want to use automatic wrapping, you must use the Google Cloud CLI.
Use a command like the following. Set `--target-key-file` to the location of the
unwrapped key to wrap and import. Do not set `--wrapped-key-file`.

You can optionally set the
`--public-key-file` flag to the location where the public key has already been
downloaded. When importing a large number of keys, this prevents the public key
from being downloaded during each import. For example, you could write a script
that downloaded the public key once, then provided its location when importing
each key.


```
gcloud kms keys versions import \
--import-job IMPORT_JOB \
--location LOCATION \
--keyring KEY_RING \
--key KEY_NAME \
--algorithm ALGORITHM \
**--target-key-file PATH_TO_UNWRAPPED_KEY **
```


The key is wrapped by the wrapping key associated with the import job,
transmitted to Google Cloud Dedicated, and imported as a new key version on the
target key.

### Importing a manually-wrapped key

Use the instructions in this section to import a key that
[you have wrapped manually](/kms/docs/wrapping-a-key). Set
`--wrapped-key-file` to the location of key that you manually wrapped.
Do not set `--target-key-file`.

You can optionally set the
`--public-key-file` flag to the location where the public key has already been
downloaded. When importing a large number of keys, this prevents the public key
from being downloaded during each import. For example, you could write a script
that downloaded the public key once, then provided its location when importing
each key.












[Console](#console) [ gcloud ](#gcloud) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ Python ](#python) [API](#api) 
More 










- 

Open the **Key Management** page in the
Google Cloud Dedicated console.

- 

Click the name of the key ring that contains your import job. The target
key is shown, along with any other keys on the key ring.

- 

Click the name of the target key, then click **Import key version**.

- 

Select your import job from the **Select import job** dropdown.

- 

In the **Upload the wrapped key** selector, select the key that you have
already [wrapped](/kms/docs/wrapping-a-key).

- 

If you are importing an asymmetric key, select the algorithm from the
**Algorithm** dropdown. Your **Import key version** page should look
similar to:



- 

Click **Import**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).





Use a command like the following.


```
gcloud kms keys versions import \
--import-job IMPORT_JOB \
--location LOCATION \
--keyring KEY_RING \
--key KEY_NAME \
--algorithm ALGORITHM \
**--wrapped-key-file PATH_TO_WRAPPED_KEY **
```


For more information, see the output of the
`gcloud kms keys versions import --help` command.





































To run this code, first [set up a Go development environment](/go/docs/setup) and
[install the Cloud KMS Go SDK](/kms/docs/reference/libraries#client-libraries-install-go).



























```
import ( 
"context" 
"crypto/ecdsa" 
"crypto/elliptic" 
"crypto/rand" 
"crypto/rsa" 
"crypto/sha1" 
"crypto/x509" 
"encoding/pem" 
"fmt" 
"io" 

kms "cloud.google.com/go/kms/apiv1" 
"cloud.google.com/go/kms/apiv1/kmspb" 
"github.com/google/tink/go/kwp/subtle" 
) 

// importManuallyWrappedKey wraps key material and imports it into KMS. 
func importManuallyWrappedKey ( w io . Writer , importJobName , cryptoKeyName string ) error { 
// importJobName := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring/importJobs/my-import-job" 
// cryptoKeyName := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring/cryptoKeys/my-imported-key" 

// Generate a ECDSA keypair, and format the private key as PKCS #8 DER. 
key , err := ecdsa . GenerateKey ( elliptic . P256 (), rand . Reader ) 
if err != nil { 
return fmt . Errorf ( "failed to generate keypair: %w" , err ) 
} 
keyBytes , err := x509 . MarshalPKCS8PrivateKey ( key ) 
if err != nil { 
return fmt . Errorf ( "failed to format private key: %w" , err ) 
} 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Generate a temporary 32-byte key for AES-KWP and wrap the key material. 
kwpKey := make ([] byte , 32 ) 
if _ , err := rand . Read ( kwpKey ); err != nil { 
return fmt . Errorf ( "failed to generate AES-KWP key: %w" , err ) 
} 
kwp , err := subtle . NewKWP ( kwpKey ) 
if err != nil { 
return fmt . Errorf ( "failed to create KWP cipher: %w" , err ) 
} 
wrappedTarget , err := kwp . Wrap ( keyBytes ) 
if err != nil { 
return fmt . Errorf ( "failed to wrap target key with KWP: %w" , err ) 
} 

// Retrieve the public key from the import job. 
importJob , err := client . GetImportJob ( ctx , & kmspb . GetImportJobRequest { 
Name : importJobName , 
}) 
if err != nil { 
return fmt . Errorf ( "failed to retrieve import job: %w" , err ) 
} 
pubBlock , _ := pem . Decode ([] byte ( importJob . PublicKey . Pem )) 
pubAny , err := x509 . ParsePKIXPublicKey ( pubBlock . Bytes ) 
if err != nil { 
return fmt . Errorf ( "failed to parse import job public key: %w" , err ) 
} 
pub , ok := pubAny .( * rsa . PublicKey ) 
if ! ok { 
return fmt . Errorf ( "unexpected public key type %T, want *rsa.PublicKey" , pubAny ) 
} 

// Wrap the KWP key using the import job key. 
wrappedWrappingKey , err := rsa . EncryptOAEP ( sha1 . New (), rand . Reader , pub , kwpKey , nil ) 
if err != nil { 
return fmt . Errorf ( "failed to wrap KWP key: %w" , err ) 
} 

// Concatenate the wrapped KWP key and the wrapped target key. 
combined := append ( wrappedWrappingKey , wrappedTarget ... ) 

// Build the request. 
req := & kmspb . ImportCryptoKeyVersionRequest { 
Parent : cryptoKeyName , 
ImportJob : importJobName , 
Algorithm : kmspb . [ CryptoKeyVersion_EC_SIGN_P256_SHA256 ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU) , 
WrappedKey : combined , 
} 

// Call the API. 
result , err := client . ImportCryptoKeyVersion ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "failed to import crypto key version: %w" , err ) 
} 
fmt . Fprintf ( w , "Created crypto key version: %s\n" , result . Name ) 
return nil 
} 
```









































To run this code, first [set up a Java development environment](/java/docs/setup) and
[install the Cloud KMS Java SDK](/kms/docs/reference/libraries#client-libraries-install-java).



























```
import com.google.cloud.kms.v1.[CryptoKeyName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) ; 
import com.google.cloud.kms.v1.[CryptoKeyVersion](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) ; 
import com.google.cloud.kms.v1.[ImportCryptoKeyVersionRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportCryptoKeyVersionRequest.html) ; 
import com.google.cloud.kms.v1.[ImportJob](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) ; 
import com.google.cloud.kms.v1.[ImportJobName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html) ; 
import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) ; 
import com.google.crypto.tink.subtle.Kwp ; 
import com.google.protobuf.[ByteString](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) ; 
import java.io.IOException ; 
import java.security.GeneralSecurityException ; 
import java.security.KeyFactory ; 
import java.security.KeyPair ; 
import java.security.KeyPairGenerator ; 
import java.security.[PublicKey](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) ; 
import java.security.SecureRandom ; 
import java.security.spec.ECGenParameterSpec ; 
import java.security.spec.MGF1ParameterSpec ; 
import java.security.spec.X509EncodedKeySpec ; 
import java.util.Base64 ; 
import javax.crypto.Cipher ; 
import javax.crypto.spec.OAEPParameterSpec ; 
import javax.crypto.spec.PSource ; 

public class ImportManuallyWrappedKey { 

public void importManuallyWrappedKey () throws GeneralSecurityException , IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String cryptoKeyId = "my-crypto-key" ; 
String importJobId = "my-import-job" ; 
importManuallyWrappedKey ( projectId , locationId , keyRingId , cryptoKeyId , importJobId ); 
} 

// Generates and imports local key material into Cloud KMS. 
public void importManuallyWrappedKey ( 
String projectId , String locationId , String keyRingId , String cryptoKeyId , String importJobId ) 
throws GeneralSecurityException , IOException { 

// Generate a new ECDSA keypair, and format the private key as PKCS #8 DER. 
KeyPairGenerator generator = KeyPairGenerator . getInstance ( "EC" ); 
generator . initialize ( new ECGenParameterSpec ( "secp256r1" )); 
KeyPair kp = generator . generateKeyPair (); 
byte [] privateBytes = kp . getPrivate (). getEncoded (); 

// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the crypto key and import job names from the project, location, 
// key ring, and ID. 
final [ CryptoKeyName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) cryptoKeyName = 
[ CryptoKeyName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) . of ( projectId , locationId , keyRingId , cryptoKeyId ); 
final [ ImportJobName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html) importJobName = 
[ ImportJobName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html) . of ( projectId , locationId , keyRingId , importJobId ); 

// Generate a temporary 32-byte key for AES-KWP and wrap the key material. 
byte [] kwpKey = new byte [ 32 ] ; 
new SecureRandom (). nextBytes ( kwpKey ); 
Kwp kwp = new Kwp ( kwpKey ); 
final byte [] wrappedTargetKey = kwp . [ wrap ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.DiscardUnknownFieldsParser.html#com_google_protobuf_DiscardUnknownFieldsParser__T_wrap_com_google_protobuf_Parser_T__) ( privateBytes ); 

// Retrieve the public key from the import job. 
[ ImportJob ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) importJob = client . getImportJob ( importJobName ); 
String publicKeyStr = importJob . [ getPublicKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html#com_google_cloud_kms_v1_ImportJob_getPublicKey__) (). getPem (); 
// Manually convert PEM to DER. :-( 
publicKeyStr = publicKeyStr . replace ( "-----BEGIN PUBLIC KEY-----" , "" ); 
publicKeyStr = publicKeyStr . replace ( "-----END PUBLIC KEY-----" , "" ); 
publicKeyStr = publicKeyStr . replaceAll ( "\n" , "" ); 
byte [] publicKeyBytes = Base64 . getDecoder (). decode ( publicKeyStr ); 
[ PublicKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) publicKey = 
KeyFactory . getInstance ( "RSA" ). generatePublic ( new X509EncodedKeySpec ( publicKeyBytes )); 

// Wrap the KWP key using the import job key. 
Cipher cipher = Cipher . getInstance ( "RSA/ECB/OAEPWithSHA-1AndMGF1Padding" ); 
cipher . init ( 
Cipher . ENCRYPT_MODE , 
publicKey , 
new OAEPParameterSpec ( 
"SHA-1" , "MGF1" , MGF1ParameterSpec . SHA1 , PSource . PSpecified . DEFAULT )); 
byte [] wrappedWrappingKey = cipher . doFinal ( kwpKey ); 

// Concatenate the wrapped KWP key and the wrapped target key. 
[ ByteString ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) combinedWrappedKeys = 
[ ByteString ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) . [ copyFrom ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___) ( wrappedWrappingKey ). [ concat ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_concat_com_google_protobuf_ByteString_) ( [ ByteString ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) . [ copyFrom ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___) ( wrappedTargetKey )); 

// Import the wrapped key material. 
[ CryptoKeyVersion ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) version = 
client . importCryptoKeyVersion ( 
[ ImportCryptoKeyVersionRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportCryptoKeyVersionRequest.html) . newBuilder () 
. setParent ( cryptoKeyName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html#com_google_cloud_kms_v1_CryptoKeyName_toString__) ()) 
. setImportJob ( importJobName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html#com_google_cloud_kms_v1_ImportJobName_toString__) ()) 
. setAlgorithm ( [ CryptoKeyVersion ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) . CryptoKeyVersionAlgorithm . EC_SIGN_P256_SHA256 ) 
. [ setRsaAesWrappedKey ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportCryptoKeyVersionRequest.Builder.html#com_google_cloud_kms_v1_ImportCryptoKeyVersionRequest_Builder_setRsaAesWrappedKey_com_google_protobuf_ByteString_) ( combinedWrappedKeys ) 
. build ()); 

System . out . printf ( "Imported: %s%n" , version . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__) ()); 
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
// const cryptoKeyId = 'my-imported-key'; 
// const importJobId = 'my-import-job'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the crypto key and importjob resource names 
const cryptoKeyName = client . cryptoKeyPath ( 
projectId , 
locationId , 
keyRingId , 
cryptoKeyId 
); 
const importJobName = client . importJobPath ( 
projectId , 
locationId , 
keyRingId , 
importJobId 
); 

async function wrapAndImportKey () { 
// Generate a 32-byte key to import. 
const crypto = require ( 'crypto' ); 
const targetKey = crypto . randomBytes ( 32 ); 

const [ importJob ] = await client . getImportJob ({ name : importJobName }); 

// Wrap the target key using the import job key 
const wrappedTargetKey = crypto . publicEncrypt ( 
{ 
key : importJob . publicKey . pem , 
oaepHash : 'sha256' , 
padding : crypto . constants . RSA_PKCS1_OAEP_PADDING , 
}, 
targetKey 
); 

// Import the target key version 
const [ version ] = await client . importCryptoKeyVersion ({ 
parent : cryptoKeyName , 
importJob : importJobName , 
algorithm : 'GOOGLE_SYMMETRIC_ENCRYPTION' , 
wrappedKey : wrappedTargetKey , 
}); 

console . log ( `Imported key version: ${ version . name } ` ); 
return version ; 
} 

return wrapAndImportKey (); 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
import os 

# Import the client library and Python standard cryptographic libraries. 
from cryptography.hazmat import backends 
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives import keywrap 
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import ec 
from cryptography.hazmat.primitives.asymmetric import padding 
from google.cloud import kms 

def import_manually_wrapped_key ( 
project_id : str , 
location_id : str , 
key_ring_id : str , 
crypto_key_id : str , 
import_job_id : str , 
) - > None : 
""" 
Generates and imports local key material to Cloud KMS. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
crypto_key_id (string): ID of the key to import (e.g. 'my-asymmetric-signing-key'). 
import_job_id (string): ID of the import job (e.g. 'my-import-job'). 
""" 

# Generate some key material in Python and format it in PKCS #8 DER as 
# required by Google Cloud KMS. 
key = ec . generate_private_key ( ec . SECP256R1 , backends . default_backend ()) 
formatted_key = key . private_bytes ( 
serialization . Encoding . DER , 
serialization . PrivateFormat . PKCS8 , 
serialization . NoEncryption (), 
) 

print ( f "Generated key bytes: { formatted_key !r} " ) 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Retrieve the fully-qualified crypto_key and import_job string. 
crypto_key_name = client . [ crypto_key_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path) ( 
project_id , location_id , key_ring_id , crypto_key_id 
) 
import_job_name = client . [ import_job_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_import_job_path) ( 
project_id , location_id , key_ring_id , import_job_id 
) 

# Generate a temporary 32-byte key for AES-KWP and wrap the key material. 
kwp_key = os . urandom ( 32 ) 
wrapped_target_key = keywrap . aes_key_wrap_with_padding ( 
kwp_key , formatted_key , backends . default_backend () 
) 

# Retrieve the public key from the import job. 
import_job = client . [ get_import_job ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_import_job) ( name = import_job_name ) 
import_job_pub = serialization . load_pem_public_key ( 
bytes ( import_job . public_key . pem , "UTF-8" ), backends . default_backend () 
) 

# Wrap the KWP key using the import job key. 
wrapped_kwp_key = import_job_pub . encrypt ( 
kwp_key , 
padding . OAEP ( 
mgf = padding . MGF1 ( algorithm = hashes . SHA1 ()), 
algorithm = hashes . SHA1 (), 
label = None , 
), 
) 

# Import the wrapped key material. 
client . [ import_crypto_key_version ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_import_crypto_key_version) ( 
{ 
"parent" : crypto_key_name , 
"import_job" : import_job_name , 
"algorithm" : kms . [ CryptoKeyVersion ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html) . [ CryptoKeyVersionAlgorithm ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html) . EC_SIGN_P256_SHA256 , 
"rsa_aes_wrapped_key" : wrapped_kwp_key + wrapped_target_key , 
} 
) 

print ( f "Imported: { import_job . name } " ) 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





Use the [`cryptoKeyVersions.import`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import) method to
import a key.


```
curl "https://cloudkms.googleapis.com/v1/projects/ PROJECT_ID /locations/ LOCATION /keyRings/ KEY_RING /cryptoKeys/ KEY_NAME /cryptoKeyVersions:import" \
--request "POST" \
--header "authorization: Bearer TOKEN " \
--header "content-type: application/json" \
--data '{"importJob": " IMPORT_JOB_ID ", "algorithm": " ALGORITHM ", "wrappedKey": " WRAPPED_KEY "}'
```


Replace the following:

- 

IMPORT_JOB_ID : the full resource name of the corresponding import
job.

- 

ALGORITHM : the [`algorithm`](/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm) of the
key being imported, which is of type
[`CryptoKeyVersionAlgorithm`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion).

- 

WRAPPED_KEY : the manually-wrapped key in base64 format.

















The key-import request is initiated. You can
[monitor its status](#check_imported_key).

### Check the state of the imported key version

The initial state for an imported key version is `PENDING_IMPORT`. When the
state is `ENABLED`, the key version has been imported successfully. If the
import fails, the status is `IMPORT_FAILED`.

You can check the status of an import request using the Google Cloud CLI, the
Google Cloud Dedicated console, or the Cloud Key Management Service API.












[Console](#console) [ gcloud ](#gcloud) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ Python ](#python) [API](#api) 
More 










- 

Open the **Key Management** page in the
Google Cloud Dedicated console.

- 

Click the name of the key ring that contains your import job.

- 

Click the **Import Jobs** tab at the top of the page.

- 

The state will be visible under **Status** next to your import job's
name.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).





Use the `versions list` command to check the state. Use the same
location, target key ring, and target key that you created earlier in this
topic.


```
gcloud kms keys versions list \
--keyring KEY_RING \
--location LOCATION \
--key KEY_NAME 
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

// checkStateImportedKey checks the state of a CryptoKeyVersion in KMS. 
func checkStateImportedKey ( w io . Writer , name string ) error { 
// name := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring/cryptoKeys/my-imported-key/cryptoKeyVersions/1" 

// Create the client. 
ctx := context . Background () 
client , err := kms . [ NewKeyManagementClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient) ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to create kms client: %w" , err ) 
} 
defer client . Close () 

// Call the API. 
result , err := client . GetCryptoKeyVersion ( ctx , & kmspb . GetCryptoKeyVersionRequest { 
Name : name , 
}) 
if err != nil { 
return fmt . Errorf ( "failed to get crypto key version: %w" , err ) 
} 
fmt . Fprintf ( w , "Current state of crypto key version %q: %s\n" , result . Name , result . State ) 
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

public class CheckStateImportedKey { 

public void checkStateImportedKey () throws IOException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String locationId = "us-east1" ; 
String keyRingId = "my-key-ring" ; 
String cryptoKeyId = "my-crypto-key" ; 
String cryptoKeyVersionId = "1" ; 
checkStateImportedKey ( projectId , locationId , keyRingId , cryptoKeyId , cryptoKeyVersionId ); 
} 

// Check the state of an imported key in Cloud KMS. 
public void checkStateImportedKey ( 
String projectId , 
String locationId , 
String keyRingId , 
String cryptoKeyId , 
String cryptoKeyVersionId ) 
throws IOException { 
// Initialize client that will be used to send requests. This client only 
// needs to be created once, and can be reused for multiple requests. After 
// completing all of your requests, call the "close" method on the client to 
// safely clean up any remaining background resources. 
try ( [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [ KeyManagementServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) . create ()) { 
// Build the version name from its path components. 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) versionName = 
[ CryptoKeyVersionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) . of ( 
projectId , locationId , keyRingId , cryptoKeyId , cryptoKeyVersionId ); 

// Retrieve the state of an existing version. 
[ CryptoKeyVersion ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) version = client . getCryptoKeyVersion ( versionName ); 
System . out . printf ( 
"Current state of crypto key version %s: %s%n" , version . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__) (), version . [ getState ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getState__) ()); 
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
// const cryptoKeyId = 'my-imported-key'; 
// const cryptoKeyVersionId = '1'; 

// Imports the Cloud KMS library 
const { KeyManagementServiceClient } = require ( '[@google-cloud/kms](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html)' ); 

// Instantiates a client 
const client = new [ KeyManagementServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/kms/latest/overview.html) (); 

// Build the key version name 
const keyVersionName = client . cryptoKeyVersionPath ( 
projectId , 
locationId , 
keyRingId , 
cryptoKeyId , 
cryptoKeyVersionId 
); 

async function checkStateCryptoKeyVersion () { 
const [ keyVersion ] = await client . getCryptoKeyVersion ({ 
name : keyVersionName , 
}); 

console . log ( 
`Current state of key version ${ keyVersion . name } : ${ keyVersion . state } ` 
); 
return keyVersion ; 
} 

return checkStateCryptoKeyVersion (); 
```









































To run this code, first [set up a Python development environment](/python/docs/setup) and
[install the Cloud KMS Python SDK](/kms/docs/reference/libraries#client-libraries-install-python).



























```
from google.cloud import kms 

def check_state_imported_key ( 
project_id : str , location_id : str , key_ring_id : str , import_job_id : str 
) - > None : 
""" 
Check the state of an import job in Cloud KMS. 

Args: 
project_id (string): Google Cloud project ID (e.g. 'my-project'). 
location_id (string): Cloud KMS location (e.g. 'us-east1'). 
key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring'). 
import_job_id (string): ID of the import job (e.g. 'my-import-job'). 
""" 

# Create the client. 
client = kms . [ KeyManagementServiceClient ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html) () 

# Retrieve the fully-qualified import_job string. 
import_job_name = client . [ import_job_path ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_import_job_path) ( 
project_id , location_id , key_ring_id , import_job_id 
) 

# Retrieve the state from an existing import job. 
import_job = client . [ get_import_job ](https://berlin.devsitetest.how/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_import_job) ( name = import_job_name ) 

print ( f "Current state of import job { import_job . name } : { import_job . state } " ) 
```































These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





Call the [`ImportJob.get`](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get) method and check the
[`state`](/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob.FIELDS.state) field. If
`state` is `PENDING_GENERATION`, the import job is still being created.
Periodically recheck the state until it is `ACTIVE`.

















After the initial key version is imported, the key's status changes to
**Active**. For symmetric keys, you must set the imported key version as the
primary version before you can use the key.

#### Symmetric keys: Set the primary version

This step is required when importing symmetric keys, and is not relevant for
asymmetric keys. An asymmetric key does not have a primary version. You must
use the Google Cloud CLI to set the primary version.


```
gcloud kms keys set-primary-version KEY_NAME \
--location= LOCATION \
--keyring= KEY_RING \
--version= KEY_VERSION 
```


## Re-import a previously destroyed key

Cloud Key Management Service supports key re-import, which allows you to restore a
previously imported key version in `DESTROYED` or `IMPORT_FAILED` state to
`ENABLED` state by providing the original key material. If no original key
material has ever been imported due to initial import failure, any key material
may be supplied.

### Restrictions

- Only previously imported `CryptoKeyVersions` can be re-imported.

- Re-imported key material must match the original key material exactly if the
version was previously successfully imported.

- `CryptoKeyVersions` destroyed prior to the release of this feature can't be
re-imported. The `reimport_eligible` field of the `CryptoKeyVersion` is
`true` if the version is eligible for re-import and `false` if it isn't.

Software and Cloud HSM keys can be re-imported, but external keys can't
be re-imported.

### Re-importing a destroyed key

Create an `ImportJob` for re-import by following the steps in
[Create the import job](#create_importjob). You may use either an existing
`ImportJob` or a new `ImportJob` as long as the protection level matches the
original protection level.












[Console](#console) [ gcloud ](#gcloud) [API](#api) 
More 










- 

Go to the **Key Management** page in the Google Cloud Dedicated console.

[Go to the Key Management page](https://console.cloud.berlin-build0.goog/security/kms) 

- 

Click the name of the key ring that contains the key whose key version you will re-import.

- 

Click the key whose key version you want to re-import.

- 

Click the three dots next to the key version you want to re-import.

- 

Select **Re-import key version**

- 

Select your import job from the **Select import job** dropdown.

- 

In the **Upload the wrapped key** selector, select the key that you have
already [wrapped](/kms/docs/wrapping-a-key). This key must match the original key material.

- 

Click **Re-Import**.




























To use Cloud KMS on the command line, first
[Install or upgrade to the latest version of Google Cloud CLI](/sdk/install).





- 

Re-import the key version using the original key material.


```
gcloud kms keys versions import \
--location LOCATION \
--keyring KEY_RING \
--key KEY_NAME \
--version KEY_VERSION \
--algorithm ALGORITHM \
--import-job IMPORT_JOB \
--target-key-file PATH_TO_KEY \
```





























These examples use [curl](https://curl.haxx.se/) as an HTTP client
to demonstrate using the API. For more information about access control, see
[Accessing the Cloud KMS API](/kms/docs/accessing-the-api).





- 

In the request body of the [`cryptoKeyVersions.import`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import) method, set the `cryptoKeyVersion` field to the key version name of the version being imported. This must be a child of the crypto key.

- 

In the request body, set the [`algorithm`](/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm) field to the algorithm of the key being imported.
This value must match the algorithm of the original key version. The
[`algorithm`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import#body.request_body.FIELDS.algorithm) field
is of type
[`CryptoKeyVersionAlgorithm`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion).

- 

In the request body, set the
[`wrappedKeyMaterial`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyVersionTemplate) field to
the key material that you that you have already
[wrapped](/kms/docs/wrapping-a-key).

- 

Call the [`cryptoKeyVersions.import`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import) method. The
`cryptoKeyVersions.import` response is of type
[`CryptoKeyVersion`](/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion).
When a key is successfully imported, its state is
`ENABLED` and you can use it in Cloud KMS.

















## What's next

- [Verify an imported key](/kms/docs/verifying-imported-key). After you confirm
that the imported key material is identical to the original key, you can use
the key for signing or to protect data.

- [Troubleshoot a failed key import](/kms/docs/troubleshooting-failed-imports).








[

Previous 

arrow_back


Set up automatic key wrapping

](/kms/docs/crypto)




[

Next 

Verify an imported key version


arrow_forward

](/kms/docs/verifying-imported-key)