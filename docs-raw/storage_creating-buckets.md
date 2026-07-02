# Create a bucket

Source: https://berlin.devsitetest.how/storage/docs/creating-buckets
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/storage/docs/tpc-differences) for more details.














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

Storage

](https://berlin.devsitetest.how/docs/storage)






- 








[

Cloud Storage

](https://berlin.devsitetest.how/storage/docs)






- 








[

Guides

](https://berlin.devsitetest.how/storage/docs/discover-object-storage-console)












# Create a bucket 






- On this page ** 
- [ Required roles ](#required-roles)
- [ Create a new bucket ](#create-bucket)
- [ What's next ](#whats_next)
- 




















This page shows you how to create a Cloud Storage [bucket](/storage/docs/buckets). If not
otherwise specified in your request, buckets are created with a default storage
class of [Standard storage](/storage/docs/storage-classes) and have a seven-day [soft delete](/storage/docs/soft-delete)
retention duration.

If you're creating a bucket for the first time, see
[Discover object storage with the Google Cloud Dedicated console](/storage/docs/discover-object-storage-console) or
[Discover object storage with the Google Cloud CLI](/storage/docs/discover-object-storage-gcloud) for a more
comprehensive walkthrough of the tasks you can perform with
Cloud Storage.

## Required roles 

In order to get the required permissions for creating a Cloud Storage
bucket, ask your administrator to grant you the Storage Admin
(`roles/storage.admin`) IAM role for the project.

This [predefined role](/iam/docs/understanding-roles) contains the permission required to create a bucket.
To see the exact permissions that are required, expand the
**Required permissions** section:



#### Required permissions



- `storage.buckets.create`

- `storage.buckets.enableObjectRetention` (only required if
enabling [object retention configurations](/storage/docs/object-lock)
for the bucket)

- `storage.buckets.list` (only required if creating a
bucket using the Google Cloud Dedicated console.)

- `resourcemanager.projects.get` (only required if creating a
bucket using the Google Cloud Dedicated console)




You might also be able to get these permissions with [custom roles](/iam/docs/creating-custom-roles) or other
predefined roles. To see which roles are associated with which permissions,
refer to [IAM roles for Cloud Storage](/storage/docs/access-control/iam-roles).

For instructions on granting roles for projects, see
[Manage access to projects](/iam/docs/granting-changing-revoking-access).

## Create a new bucket

To create a bucket with specific settings or advanced configurations, complete
the following steps.


[Console](#console) [Command line](#command-line) [Client libraries](#client-libraries) [Terraform](#terraform) [REST APIs](#rest-apis) 
More 





- In the Google Cloud Dedicated console, go to the Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.berlin-build0.goog/storage/browser)


- Click add_box **Create**.

- 

On the **Create a bucket** page, enter your bucket information. After
each of the following steps, click **Continue** to proceed to the next
step:




- 


In the **Get started** section, do the following:




- 


Enter a globally unique name that meets the
[bucket name requirements](/storage/docs/buckets#naming).




- 


To add a [bucket label](/storage/docs/tags-and-labels#bucket-labels), click the
expand_more expander arrow to
expand the **Labels** section, click
*add_box* **Add
label**, and specify a `key` and a `value` for
your label.







- 


In the **Choose where to store your data** section, do the
following:




- 



Select a [Location type](/storage/docs/locations).




- 


Use the location type's drop-down menu to select a
[**Location**](/storage/docs/locations#available-locations) where object data
within your bucket will be permanently stored.





- 


If you select the [dual-region](/storage/docs/locations#location-dr) location
type, you can also choose to enable
[turbo replication](/storage/docs/availability-durability#turbo-replication) by
using the relevant checkbox.








- 






- 



In the **Choose how to store your data** section, do the
following:




- 


Select a [default storage class](/storage/docs/storage-classes) for the
bucket or [Autoclass](/storage/docs/autoclass) for automatic storage
class management of your bucket's data.




- 


In the **Optimize storage for data-intensive workloads** section,
do the following:





- 


To enable [hierarchical namespace](/storage/docs/hns-overview), select
**Enable Hierarchical namespace on this bucket**.






- To enable [Rapid Cache](/storage/docs/rapid/rapid-cache), select
**Enable Rapid Cache** and follow the steps:



- 


To create caches, click **Configure**.



- 


In the **Configure cache settings** dialog that appears, click
the drop-down arrow next to the listed regions and select the
zones where you want to create caches.



- 


Click **Done**.














- 



In the **Choose how to control access to objects** section, select
whether or not your bucket enforces
[public access prevention](/storage/docs/public-access-prevention), and select
uniform bucket-level access for your bucket's objects.





- 


In the **Choose how to protect object data** section, do the
following:





- 


Select any of the options under **Data protection** that you
want to set for your bucket.





- 


To change the amount of time that [soft delete](/storage/docs/soft-delete)
retains objects after deletion, select the **Soft delete policy** checkbox, and then
select the **Set custom retention duration** option. Then, specify how long you want to
retain deleted objects.



To disable soft delete, for example if the bucket will primarily contain
short-lived, temporary data, clear the **Soft delete policy** checkbox.





- 


To choose how to [encrypt](/storage/docs/encryption) your object data,
click the expand_more expander arrow labeled
**Data encryption**, and do the following:




- In the **Default encryption key type** section, select the default encryption key
for the bucket. If you select **Cloud KMS key**, then provide a
[Cloud Key Management Service key](/storage/docs/encryption/using-customer-managed-keys).

- In the **Encryption enforcement rules** section, for **Key types**, select
[which encryption types to
allow or restrict](/storage/docs/encryption/enforce-encryption-types) for new objects in the bucket.










- 

Click **Create**.

To learn how to get detailed error information about failed Cloud Storage
operations in the Google Cloud Dedicated console, see
[Troubleshooting](/storage/docs/troubleshooting#trouble-console).




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

In your development environment, run the
[`gcloud storage buckets create`](/sdk/gcloud/reference/storage/buckets/create) command:


```
gcloud storage buckets create gs:// BUCKET_NAME --location= BUCKET_LOCATION 
```


Where:

- ` BUCKET_NAME ` is the name you want to give your
bucket, subject to [naming requirements](/storage/docs/buckets#naming). For example,
`my-bucket`.

- 

` BUCKET_LOCATION ` is the [location](/storage/docs/locations) of your
bucket. For example, `U-GERMANY-NORTHEAST1`.

If the request is successful, the command returns the following message:


```
Creating gs:// BUCKET_NAME /...
```


Set the following flags to have greater control over the creation of
your bucket:

- `--project`: Specify the project ID or project number with which your
bucket will be associated. For example, `my-project`.

- `--default-storage-class`: Specify the default [storage class](/storage/docs/storage-classes)
of your bucket. For example, `STANDARD`.

- `--uniform-bucket-level-access`: Enable [uniform bucket-level access](/storage/docs/uniform-bucket-level-access)
for your bucket.

- `--soft-delete-duration`: Specify a [soft delete](/storage/docs/soft-delete) retention
duration, which is the number of days you want to retain objects after
they get deleted. For example, `10d`.

- `--encryption-enforcement-file`: Provide a file that defines
[which encryption methods are restricted or allowed](/storage/docs/encryption/enforce-encryption-types) for new
objects in the bucket.

For example:


```
gcloud storage buckets create gs:// BUCKET_NAME --project= PROJECT_ID --default-storage-class= STORAGE_CLASS --location= BUCKET_LOCATION --uniform-bucket-level-access
--soft-delete-duration= RETENTION_DURATION --encryption-enforcement-file= ENCRYPTION_ENFORCEMENT_FILE 
```


For a complete list of options for bucket creation using the
gcloud CLI, see [`buckets create` options](/sdk/gcloud/reference/storage/buckets/create#FLAGS).











































[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) [ Rust ](#rust) 
More 












For more information, see the
[Cloud Storage C++ API
reference documentation](/cpp/docs/reference/storage/latest).





To authenticate to Cloud Storage, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/storage/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
namespace gcs = :: google :: cloud :: storage ; 
using :: google :: cloud :: StatusOr ; 
[]( gcs :: Client client , std :: string const & bucket_name , 
std :: string const & storage_class , std :: string const & location ) { 
StatusOr :: BucketMetadata > bucket_metadata = 
client . CreateBucket ( bucket_name , gcs :: BucketMetadata () 
. set_storage_class ( storage_class ) 
. set_location ( location )); 
if ( ! bucket_metadata ) throw std :: move ( bucket_metadata ). status (); 

std :: cout "Bucket " bucket_metadata - > name () " created." 
" \n Full Metadata: " * bucket_metadata " \n " ; 
} 
```


















































For more information, see the
[Cloud Storage C# API
reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest).





To authenticate to Cloud Storage, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/storage/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
using Google.Apis.Storage.v1.Data ; 
using [ Google.Cloud.Storage.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html) ; 
using System ; 

public class CreateRegionalBucketSample 
{ 
/// 
/// Creates a storage bucket with region. 
/// 
/// 

The ID of the project to create the buckets in. 
/// 

The location of the bucket. Object data for objects in the bucket resides in 
/// physical storage within this region. Defaults to US. 
/// 

The name of the bucket to create. 
/// 

The bucket's default storage class, used whenever no storageClass is specified 
/// for a newly-created object. This defines how objects in the bucket are stored 
/// and determines the SLA and the cost of storage. Values include MULTI_REGIONAL, 
/// REGIONAL, STANDARD, NEARLINE, COLDLINE, ARCHIVE, and DURABLE_REDUCED_AVAILABILITY. 
/// If this value is not specified when the bucket is created, it will default to 
/// STANDARD. 
public Bucket CreateRegionalBucket ( 
string projectId = "your-project-id" , 
string bucketName = "your-unique-bucket-name" , 
string location = "us-west1" , 
string storageClass = "REGIONAL" ) 
{ 
var storage = [ StorageClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create) (); 
Bucket bucket = new Bucket 
{ 
Location = location , 
Name = bucketName , 
StorageClass = storageClass 
}; 
var newlyCreatedBucket = storage . CreateBucket ( projectId , bucket ); 
Console . WriteLine ( $"Created {bucketName}." ); 
return newlyCreatedBucket ; 
} 
} 
```

















































For more information, see the
[Cloud Storage Go API
reference documentation](https://pkg.go.dev/cloud.google.com/go/storage).





To authenticate to Cloud Storage, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/storage/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import ( 
"context" 
"fmt" 
"io" 
"time" 

"cloud.google.com/go/storage" 
) 

// createBucketClassLocation creates a new bucket in the project with Storage class and 
// location. 
func createBucketClassLocation ( w io . [ Writer ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer) , projectID , bucketName string ) error { 
// projectID := "my-project-id" 
// bucketName := "bucket-name" 
ctx := context . Background () 
client , err := storage . NewClient ( ctx ) 
if err != nil { 
return fmt . Errorf ( "storage.NewClient: %w" , err ) 
} 
defer client . Close () 

ctx , cancel := context . WithTimeout ( ctx , time . Second * 30 ) 
defer cancel () 

storageClassAndLocation := & storage . [ BucketAttrs ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs) { 
StorageClass : "COLDLINE" , 
Location : "asia" , 
} 
bucket := client . [ Bucket ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket) ( bucketName ) 
if err := bucket . [ Create ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create) ( ctx , projectID , storageClassAndLocation ); err != nil { 
return fmt . Errorf ( "Bucket(%q).Create: %w" , bucketName , err ) 
} 
fmt . Fprintf ( w , "Created bucket %v in %v with storage class %v\n" , bucketName , storageClassAndLocation . Location , storageClassAndLocation . StorageClass ) 
return nil 
} 
```


















































For more information, see the
[Cloud Storage Java API
reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/overview).





To authenticate to Cloud Storage, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/storage/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import com.google.cloud.storage.[Bucket](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) ; 
import com.google.cloud.storage.[BucketInfo](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html) ; 
import com.google.cloud.storage.[Storage](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) ; 
import com.google.cloud.storage.[StorageClass](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html) ; 
import com.google.cloud.storage.[StorageOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) ; 

public class CreateBucketWithStorageClassAndLocation { 
public static void createBucketWithStorageClassAndLocation ( String projectId , String bucketName ) { 
// The ID of your GCP project 
// String projectId = "your-project-id"; 

// The ID to give your GCS bucket 
// String bucketName = "your-unique-bucket-name"; 

[ Storage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [ StorageOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) . newBuilder (). setProjectId ( projectId ). build (). [ getService ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__) (); 

// See the StorageClass documentation for other valid storage classes: 
// https://googleapis.dev/java/google-cloud-clients/latest/com/google/cloud/storage/StorageClass.html 
[ StorageClass ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html) storageClass = [ StorageClass ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html) . COLDLINE ; 

// See this documentation for other valid locations: 
// http://g.co/cloud/storage/docs/bucket-locations#location-mr 
String location = "ASIA" ; 

[ Bucket ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = 
storage . [ create ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____) ( 
BucketInfo . newBuilder ( bucketName ) 
. setStorageClass ( storageClass ) 
. setLocation ( location ) 
. build ()); 

System . out . println ( 
"Created bucket " 
+ bucket . getName () 
+ " in " 
+ bucket . getLocation () 
+ " with storage class " 
+ bucket . getStorageClass ()); 
} 
} 
```


















































For more information, see the
[Cloud Storage Node.js API
reference documentation](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest).





To authenticate to Cloud Storage, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/storage/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// The ID of your GCS bucket 
// const bucketName = 'your-unique-bucket-name'; 

// The name of a storage class 
// See the StorageClass documentation for other valid storage classes: 
// https://googleapis.dev/java/google-cloud-clients/latest/com/google/cloud/storage/StorageClass.html 
// const storageClass = 'coldline'; 

// The name of a location 
// See this documentation for other valid locations: 
// http://g.co/cloud/storage/docs/locations#location-mr 
// const location = 'ASIA'; 

// Imports the Google Cloud client library 
const { Storage } = require ( '[@google-cloud/storage](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/overview.html)' ); 

// Creates a client 
// The bucket in the sample below will be created in the project associated with this client. 
// For more information, please see https://cloud.google.com/docs/authentication/production or https://googleapis.dev/nodejs/storage/latest/Storage.html 
const storage = new [ Storage ](https://berlin.devsitetest.how/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html) (); 

async function createBucketWithStorageClassAndLocation () { 
// For default values see: https://cloud.google.com/storage/docs/locations and 
// https://cloud.google.com/storage/docs/storage-classes 
const [ bucket ] = await storage . createBucket ( bucketName , { 
location , 
[ storageClass ] : true , 
}); 

console . log ( 
` ${ bucket . name } created with ${ storageClass } class in ${ location } ` 
); 
} 

createBucketWithStorageClassAndLocation (). catch ( console . error ); 
```

















































For more information, see the
[Cloud Storage PHP API
reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient).





To authenticate to Cloud Storage, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/storage/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
use Google\Cloud\Storage\StorageClient; 

/** 
* Create a new bucket with a custom default storage class and location. 
* 
* @param string $bucketName The name of your Cloud Storage bucket. 
* (e.g. 'my-bucket') 
*/ 
function create_bucket_class_location(string $bucketName): void 
{ 
$storage = new StorageClient(); 
$storageClass = 'COLDLINE'; 
$location = 'ASIA'; 
$bucket = $storage->createBucket($bucketName, [ 
'storageClass' => $storageClass, 
'location' => $location, 
]); 

$objects = $bucket->objects([ 
'encryption' => [ 
'defaultKmsKeyName' => null, 
] 
]); 

printf('Created bucket %s in %s with storage class %s', $bucketName, $storageClass, $location); 
} 
```


















































For more information, see the
[Cloud Storage Python API
reference documentation](https://berlin.devsitetest.how/python/docs/reference/storage/latest).





To authenticate to Cloud Storage, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/storage/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
from google.cloud import [ storage ](https://berlin.devsitetest.how/python/docs/reference/storage/latest)

def create_bucket_class_location ( bucket_name ): 
""" 
Create a new bucket in the US region with the coldline storage 
class 
""" 
# bucket_name = "your-new-bucket-name" 

storage_client = [ storage ](https://berlin.devsitetest.how/python/docs/reference/storage/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html) () 

bucket = storage_client . [ bucket ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket) ( bucket_name ) 
bucket . storage_class = "COLDLINE" 
new_bucket = storage_client . [ create_bucket ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_create_bucket) ( bucket , location = "us" ) 

print ( 
"Created bucket {} in {} with storage class {} " . format ( 
new_bucket . name , new_bucket . [ location ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location) , new_bucket . storage_class 
) 
) 
return new_bucket 
```


















































For more information, see the
[Cloud Storage Ruby API
reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html).





To authenticate to Cloud Storage, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/storage/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
def create_bucket_class_location bucket_name : 
# The ID to give your GCS bucket 
# bucket_name = "your-unique-bucket-name" 

require "google/cloud/storage" 

storage = Google :: Cloud :: [ Storage ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
bucket = storage . [ create_bucket ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) bucket_name , 
location : "ASIA" , 
storage_class : "COLDLINE" 

puts "Created bucket #{ bucket . name } in #{ bucket . location } with #{ bucket . storage_class } class" 
end 
```

































































```
use google_cloud_storage ::{ client :: StorageControl , model :: Bucket }; 

pub async fn sample ( 
client : & StorageControl , 
project_id : & str , 
bucket_id : & str , 
) - > anyhow :: Result () > { 
let bucket = client 
. create_bucket () 
. set_parent ( "projects/_" ) 
. set_bucket_id ( bucket_id ) 
. set_bucket ( 
Bucket :: new () 
. set_project ( format! ( "projects/{project_id}" )) 
. set_storage_class ( "NEARLINE" ) 
. set_location ( "US-CENTRAL1" ), 
) 
. send () 
. await ? ; 
println! ( "successfully created bucket {bucket:?}" ); 
Ok (()) 
} 
```





































You can use a [Terraform resource to create a storage bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket).




















```
# Create new storage bucket in the US multi-region
# with coldline storage
resource "random_id" "bucket_prefix" {
byte_length = 8
}

resource "google_storage_bucket" "static" {
name = "${random_id.bucket_prefix.hex}-new-bucket"
location = "US"
storage_class = "COLDLINE"

uniform_bucket_level_access = true
}
```





[JSON API](#json-api) [XML API](#xml-api) 
More 




- 

Have gcloud CLI [installed and initialized](/sdk/docs/install) , which lets
you generate an access token for the `Authorization` header. 


- 

Create a JSON file that contains the settings for the bucket, which
must include a `name` for the bucket. See the [Buckets:Insert](/storage/docs/json_api/v1/buckets/insert)
documentation for a complete list of settings. The following are
common settings to include:


```
{ 
"name" : " BUCKET_NAME " , 
"location" : " BUCKET_LOCATION " , 
"storageClass" : " STORAGE_CLASS " , 
"iamConfiguration" : { 
"uniformBucketLevelAccess" : { 
"enabled" : true 
}, 
} 
} 
```


Where:

- 

` BUCKET_NAME ` is the name you want to give
your bucket, subject to [naming requirements](/storage/docs/buckets#naming). For example,
`my-bucket`.

- 

` BUCKET_LOCATION ` is the [location](/storage/docs/locations) where
you want to store your bucket's [object data](/storage/docs/objects). For example,
`U-GERMANY-NORTHEAST1`.

- 

` STORAGE_CLASS ` is the default
[storage class](/storage/docs/storage-classes) of your bucket. For example, `STANDARD`.

- 

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](/storage/docs/json_api):


```
curl -X POST --data-binary @ JSON_FILE_NAME \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://storage.apis-berlin-build0.goog/storage/v1/b?project= PROJECT_IDENTIFIER "
```


Where:

- ` JSON_FILE_NAME ` is name of the JSON file
you created in Step 2.

- ` PROJECT_IDENTIFIER ` is the ID or number of
the project with which your bucket will be associated. For
example, `my-project`.




- 

Have gcloud CLI [installed and initialized](/sdk/docs/install) , which lets
you generate an access token for the `Authorization` header. 


- 

Create an XML file that contains settings for the bucket. See the
[XML: Create a bucket](/storage/docs/xml-api/put-bucket-create) documentation for a complete list of
settings. The following are common settings to include:


```

STORAGE_CLASS 
BUCKET_LOCATION 

```


Where:

- 

` STORAGE_CLASS ` is the default
[storage class](/storage/docs/storage-classes) of your bucket. For example, `STANDARD`.

- 

` BUCKET_LOCATION ` is the [location](/storage/docs/locations) where
you want to store your bucket's [object data](/storage/docs/objects). For example,
`U-GERMANY-NORTHEAST1`.

- 

Use [`cURL`](http://curl.haxx.se/) to call the [XML API](/storage/docs/xml-api/put-bucket-create):


```
curl -X PUT --data-binary @ XML_FILE_NAME \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "x-goog-project-id: PROJECT_ID " \
"https://storage.apis-berlin-build0.goog/ BUCKET_NAME "
```


Where:

- ` XML_FILE_NAME ` is name of the XML file you
created in Step 2.

- ` PROJECT_ID ` is the ID of the project with
which your bucket will be associated. For example, `my-project`.

- ` BUCKET_NAME ` is the name you want to give
your bucket, subject to [naming requirements](/storage/docs/buckets#naming). For example,
`my-bucket`.

If the request was successful, a response is not returned.





## What's next

- [List buckets in a project](/storage/docs/listing-buckets).

- Learn about the [metadata associated with a bucket](/storage/docs/bucket-metadata).

- [Move or rename a bucket](/storage/docs/moving-buckets).

- [Delete a bucket](/storage/docs/deleting-buckets).

- [Upload an object to your bucket](/storage/docs/uploading-objects).

- Create and configure buckets declaratively with the
[Kubernetes Config Connector](/config-connector/docs/overview), which lets you describe Google Cloud Dedicated in Germany resources
using Kubernetes tooling, APIs, and configurations. For more information,
see the [Config Connector API documentation](/config-connector/docs/reference/resource-docs/storage/storagebucket).