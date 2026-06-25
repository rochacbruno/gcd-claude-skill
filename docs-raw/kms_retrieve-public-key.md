# Retrieve a public key

Source: https://berlin.devsitetest.how/kms/docs/retrieve-public-key
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












# Retrieve a public key 






- On this page 
- [ Required roles ](#required-roles)
- [ Retrieve a public key ](#retrieve)
- 









This page shows you how to retrieve the public key portion of an enabled
asymmetric key version.

The format of the public key depends on whether it is a post-quantum computing
(PQC) or conventional algorithm:

- 

For non-PQC algorithms, the default format of the public key is the
Privacy-enhanced Electronic Mail (PEM) format. You can also retrieve non-PQC
public keys in the Distinguished Encoding Rules (DER) format. For more
information, see the [RFC 7468](https://tools.ietf.org/html/rfc7468), particularly the sections
"General Considerations" and "Textual Encoding of Subject Public Key Info".

- 

For PQC algorithms standardized by NIST ([Preview](https://berlin.devsitetest.how/products#product-launch-stages)), you can retrieve the
public key in the format identified in the NIST PCQ standards for that
algorithm. For more information, see [FIPS-203](https://csrc.nist.gov/pubs/fips/203/final), [FIPS-204](https://csrc.nist.gov/pubs/fips/204/final), and [FIPS-205](https://csrc.nist.gov/pubs/fips/205/final).
The PEM and DER formats are only supported for ML-DSA keys.

- 

For X-Wing, you can retrieve the public key in the raw bytes format
specified by the [X-Wing standard](https://datatracker.ietf.org/doc/draft-connolly-cfrg-xwing-kem/).
PEM and DER formats are not supported for these keys.

## Required roles


































































































To get the permissions that
you need to retrieve a public key,

ask your administrator to grant you the
[Cloud KMS CryptoKey Public Key Viewer ](/iam/docs/roles-permissions/cloudkms#cloudkms.publicKeyViewer) (`roles/cloudkms.publicKeyViewer`) IAM role on your key or a parent resource.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).








This predefined role contains

the permissions required to retrieve a public key. To see the exact permissions that are
required, expand the **Required permissions** section:





#### Required permissions




The following permissions are required to retrieve a public key:






- 
`cloudkms.cryptoKeyVersions.viewPublicKey`



- 
`cloudkms.locations.get`



- 
`cloudkms.locations.list`



- 
`resourcemanager.projects.get`














You might also be able to get
these permissions
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









## Retrieve a public key

You can specify the format in which you want to retrieve the public key.
If the format is specified, the key will be returned in the specified format
in the `public_key` field of the response. Otherwise, it is returned in the
`pem` field of the response.

To download the public key for an enabled asymmetric key version:












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