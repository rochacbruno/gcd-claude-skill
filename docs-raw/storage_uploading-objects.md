# Upload objects from a file system

Source: https://berlin.devsitetest.how/storage/docs/uploading-objects
Last updated: 2026-06-18

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












# Upload objects from a file system 






- On this page ** 
- [ Required roles ](#required-roles)
- [ Upload an object to a bucket ](#uploading-an-object)
- [ Upload the contents of a directory to a bucket ](#uploading-directory)
- [ What's next ](#whats_next)
- 


















This page shows you how to upload objects to your Cloud Storage bucket from
your local file system. An uploaded object consists of the data you want to store
along with any associated metadata. For a conceptual overview, including how to
choose the optimal upload method based on your file size, see
[Object uploads](/storage/docs/uploads).

For instructions on uploading from memory, see [Upload objects from memory](/storage/docs/uploading-objects-from-memory).

## Required roles 

To get the permissions that you need to upload objects to a bucket, ask your
administrator to grant you the Storage Object User
(`roles/storage.objectUser`) IAM role on the bucket. This
predefined role contains the permissions required to upload an object to a
bucket. To see the exact permissions that are required, expand the
**Required permissions** section:



#### Required permissions



- `storage.objects.create`

- `storage.objects.delete`

- This permission is only required for uploads that overwrite an existing
object.

- `storage.objects.get`


- This permission is only required if you plan on using the
Google Cloud CLI to perform the tasks on this page.

- `storage.objects.list`


- This permission is only required if you plan on using the
Google Cloud CLI to perform the tasks on this page. This permission
is also required if you want to use the Google Cloud Dedicated console to verify the
objects you've uploaded.




If you plan on using the Google Cloud Dedicated console to perform the tasks on this
page, you'll also need the `storage.buckets.list` permission, which is not
included in the Storage Object User (`roles/storage.objectUser`) role. To get
this permission, ask your administrator to grant you the Storage Admin
(`roles/storage.admin`) role on the project.

You can also get these permissions with other [predefined roles](/iam/docs/roles-permissions) or
[custom roles](/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see
[Set and manage IAM policies on buckets](/storage/docs/access-control/using-iam-permissions).

## Upload an object to a bucket

Complete the following steps to upload an object to a bucket:


[Console](#console) [Command line](#command-line) [Client libraries](#client-libraries) [Terraform](#terraform) [REST APIs](#rest-apis) 
More 




- In the Google Cloud Dedicated console, go to the Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.berlin-build0.goog/storage/browser)

- 

In the list of buckets, click the name of the bucket that you want to
upload an object to.

- 

In the **Objects** tab for the bucket, either:

- 

Drag files from your desktop or file manager
to the main pane in the Google Cloud Dedicated console.

- 

Click **Upload** > **Upload files**, select the files you want to
upload in the dialog that appears, then click **Open**.

To learn how to get detailed error information about failed Cloud Storage
operations in the Google Cloud Dedicated console, see
[Troubleshooting](/storage/docs/troubleshooting#trouble-console).



Use the [`gcloud storage cp`](/sdk/gcloud/reference/storage/cp) command:


```
gcloud storage cp OBJECT_LOCATION gs:// DESTINATION_BUCKET_NAME 
```


Where:

- 

` OBJECT_LOCATION ` is the local path to your
object. For example, `Desktop/dog.png`.

- 

` DESTINATION_BUCKET_NAME ` is the name of the
bucket to which you are uploading your object. For example,
`my-bucket`.

If successful, the response looks like the following example:


```
Completed files 1/1 | 164.3kiB/164.3kiB
```


You can set fixed-key and custom [object metadata](/storage/docs/metadata) as part of your
object upload by using [command flags](/sdk/gcloud/reference/storage/cp#FLAGS).

































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
[]( gcs :: Client client , std :: string const & file_name , 
std :: string const & bucket_name , std :: string const & object_name ) { 
// Note that the client library automatically computes a hash on the 
// client-side to verify data integrity during transmission. 
StatusOr :: ObjectMetadata > metadata = client . UploadFile ( 
file_name , bucket_name , object_name , gcs :: IfGenerationMatch ( 0 )); 
if ( ! metadata ) throw std :: move ( metadata ). status (); 

std :: cout "Uploaded " file_name " to object " metadata - > name () 
" in bucket " metadata - > bucket () 
" \n Full metadata: " * metadata " \n " ; 
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
using [ Google.Cloud.Storage.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html) ; 
using System ; 
using System.IO ; 

public class UploadFileSample 
{ 
public void UploadFile ( 
string bucketName = "your-unique-bucket-name" , 
string localPath = "my-local-path/my-file-name" , 
string objectName = "my-file-name" ) 
{ 
var storage = [ StorageClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create) (); 
using var fileStream = File . OpenRead ( localPath ); 
storage . UploadObject ( bucketName , objectName , null , fileStream ); 
Console . WriteLine ( $"Uploaded {objectName}." ); 
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
"os" 
"time" 

"cloud.google.com/go/storage" 
) 

// uploadFile uploads an object. 
func uploadFile ( w io . [ Writer ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer) , bucket , object string ) error { 
// bucket := "bucket-name" 
// object := "object-name" 
ctx := context . Background () 
client , err := storage . NewClient ( ctx ) 
if err != nil { 
return fmt . Errorf ( "storage.NewClient: %w" , err ) 
} 
defer client . Close () 

// Open local file. 
f , err := os . Open ( "notes.txt" ) 
if err != nil { 
return fmt . Errorf ( "os.Open: %w" , err ) 
} 
defer f . Close () 

ctx , cancel := context . WithTimeout ( ctx , time . Second * 50 ) 
defer cancel () 

o := client . [ Bucket ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket) ( bucket ). [ Object ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object) ( object ) 

// Optional: set a generation-match precondition to avoid potential race 
// conditions and data corruptions. The request to upload is aborted if the 
// object's generation number does not match your precondition. 
// For an object that does not yet exist, set the DoesNotExist precondition. 
o = o . If ( storage . [ Conditions ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions) { DoesNotExist : true }) 
// If the live object already exists in your bucket, set instead a 
// generation-match precondition using the live object's generation number. 
// attrs, err := o.Attrs(ctx) 
// if err != nil { 
// return fmt.Errorf("object.Attrs: %w", err) 
// } 
// o = o.If(storage.Conditions{GenerationMatch: attrs.Generation}) 

// Upload an object with storage.Writer. 
wc := o . [ NewWriter ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter) ( ctx ) 
if _ , err = io . Copy ( wc , f ); err != nil { 
return fmt . Errorf ( "io.Copy: %w" , err ) 
} 
if err := wc . Close (); err != nil { 
return fmt . Errorf ( "Writer.Close: %w" , err ) 
} 
fmt . Fprintf ( w , "Blob %v uploaded.\n" , object ) 
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







The following sample uploads an individual object:
























```
import com.google.cloud.storage.[BlobId](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) ; 
import com.google.cloud.storage.[BlobInfo](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) ; 
import com.google.cloud.storage.[Storage](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) ; 
import com.google.cloud.storage.[StorageOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) ; 
import java.io.IOException ; 
import java.nio.file.Paths ; 

public class UploadObject { 
public static void uploadObject ( 
String projectId , String bucketName , String objectName , String filePath ) throws IOException { 
// The ID of your GCP project 
// String projectId = "your-project-id"; 

// The ID of your GCS bucket 
// String bucketName = "your-unique-bucket-name"; 

// The ID of your GCS object 
// String objectName = "your-object-name"; 

// The path to your file to upload 
// String filePath = "path/to/your/file" 

[ Storage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [ StorageOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) . newBuilder (). setProjectId ( projectId ). build (). [ getService ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__) (); 
[ BlobId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [ BlobId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) . of ( bucketName , objectName ); 
[ BlobInfo ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [ BlobInfo ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) . newBuilder ( blobId ). build (); 

// Optional: set a generation-match precondition to avoid potential race 
// conditions and data corruptions. The request returns a 412 error if the 
// preconditions are not met. 
[ Storage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) . BlobWriteOption precondition ; 
if ( storage . [ get ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_) ( bucketName , objectName ) == null ) { 
// For a target object that does not yet exist, set the DoesNotExist precondition. 
// This will cause the request to fail if the object is created before the request runs. 
precondition = [ Storage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) . BlobWriteOption . doesNotExist (); 
} else { 
// If the destination already exists in your bucket, instead set a generation-match 
// precondition. This will cause the request to fail if the existing object's generation 
// changes before the request runs. 
precondition = 
[ Storage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) . BlobWriteOption . generationMatch ( 
storage . [ get ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_) ( bucketName , objectName ). getGeneration ()); 
} 
storage . [ createFrom ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_createFrom_com_google_cloud_storage_BlobInfo_java_io_InputStream_com_google_cloud_storage_Storage_BlobWriteOption____) ( blobInfo , Paths . get ( filePath ), precondition ); 

System . out . println ( 
"File " + filePath + " uploaded to bucket " + bucketName + " as " + objectName ); 
} 
} 
```





The following sample uploads multiple objects concurrently:
























```
import com.google.cloud.storage.transfermanager.[ParallelUploadConfig](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) ; 
import com.google.cloud.storage.transfermanager.[TransferManager](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) ; 
import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html) ; 
import com.google.cloud.storage.transfermanager.[UploadResult](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html) ; 
import java.io.IOException ; 
import java.nio.file.Path ; 
import java.util.List ; 

class UploadMany { 

public static void uploadManyFiles ( String bucketName , List files ) throws IOException { 
[ TransferManager ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager = [ TransferManagerConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html) . newBuilder (). build (). [ getService ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__) (); 
[ ParallelUploadConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) parallelUploadConfig = 
[ ParallelUploadConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) . newBuilder (). setBucketName ( bucketName ). build (); 
List results = 
transferManager . [ uploadFiles ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html#com_google_cloud_storage_transfermanager_TransferManager_uploadFiles_java_util_List_java_nio_file_Path__com_google_cloud_storage_transfermanager_ParallelUploadConfig_) ( files , parallelUploadConfig ). [ getUploadResults ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadJob.html#com_google_cloud_storage_transfermanager_UploadJob_getUploadResults__) (); 
for ( [ UploadResult ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html) result : results ) { 
System . out . println ( 
"Upload for " 
+ result . getInput (). getName () 
+ " completed with status " 
+ result . getStatus ()); 
} 
} 
} 
```





The following sample uploads all objects with a common prefix concurrently:
























```
import com.google.cloud.storage.transfermanager.[ParallelUploadConfig](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) ; 
import com.google.cloud.storage.transfermanager.[TransferManager](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) ; 
import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html) ; 
import com.google.cloud.storage.transfermanager.[UploadResult](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html) ; 
import java.io.IOException ; 
import java.nio.file.Files ; 
import java.nio.file.Path ; 
import java.util.ArrayList ; 
import java.util.List ; 
import java.util.stream.Stream ; 

class UploadDirectory { 

public static void uploadDirectoryContents ( String bucketName , Path sourceDirectory ) 
throws IOException { 
[ TransferManager ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager = [ TransferManagerConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html) . newBuilder (). build (). [ getService ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__) (); 
[ ParallelUploadConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) parallelUploadConfig = 
[ ParallelUploadConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) . newBuilder (). setBucketName ( bucketName ). build (); 

// Create a list to store the file paths 
List filePaths = new ArrayList <> (); 
// Get all files in the directory 
// try-with-resource to ensure pathStream is closed 
try ( Stream pathStream = Files . walk ( sourceDirectory )) { 
pathStream . filter ( Files :: isRegularFile ). forEach ( filePaths :: add ); 
} 
List results = 
transferManager . [ uploadFiles ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html#com_google_cloud_storage_transfermanager_TransferManager_uploadFiles_java_util_List_java_nio_file_Path__com_google_cloud_storage_transfermanager_ParallelUploadConfig_) ( filePaths , parallelUploadConfig ). [ getUploadResults ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadJob.html#com_google_cloud_storage_transfermanager_UploadJob_getUploadResults__) (); 
for ( [ UploadResult ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html) result : results ) { 
System . out . println ( 
"Upload for " 
+ result . getInput (). getName () 
+ " completed with status " 
+ result . getStatus ()); 
} 
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







The following sample uploads an individual object:
























```
/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// The ID of your GCS bucket 
// const bucketName = 'your-unique-bucket-name'; 

// The path to your file to upload 
// const filePath = 'path/to/your/file'; 

// The new ID for your GCS file 
// const destFileName = 'your-new-file-name'; 

// Imports the Google Cloud client library 
const { Storage } = require ( '[@google-cloud/storage](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/overview.html)' ); 

// Creates a client 
const storage = new [ Storage ](https://berlin.devsitetest.how/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html) (); 

async function uploadFile () { 
const options = { 
destination : destFileName , 
// Optional: 
// Set a generation-match precondition to avoid potential race conditions 
// and data corruptions. The request to upload is aborted if the object's 
// generation number does not match your precondition. For a destination 
// object that does not yet exist, set the ifGenerationMatch precondition to 0 
// If the destination object already exists in your bucket, set instead a 
// generation-match precondition using its generation number. 
preconditionOpts : { ifGenerationMatch : generationMatchPrecondition }, 
}; 

await storage . bucket ( bucketName ). [ upload ](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/storage/bucket.html) ( filePath , options ); 
console . log ( ` ${ filePath } uploaded to ${ bucketName } ` ); 
} 

uploadFile (). catch ( console . error ); 
```





The following sample uploads multiple objects concurrently:
























```
/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// The ID of your GCS bucket 
// const bucketName = 'your-unique-bucket-name'; 

// The ID of the first GCS file to upload 
// const firstFilePath = 'your-first-file-name'; 

// The ID of the second GCS file to upload 
// const secondFilePath = 'your-second-file-name'; 

// Imports the Google Cloud client library 
const { Storage , TransferManager } = require ( '[@google-cloud/storage](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/overview.html)' ); 

// Creates a client 
const storage = new [ Storage ](https://berlin.devsitetest.how/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html) (); 

// Creates a transfer manager client 
const transferManager = new [ TransferManager ](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/storage/transfermanager.html) ( storage . bucket ( bucketName )); 

async function uploadManyFilesWithTransferManager () { 
// Uploads the files 
await transferManager . [ uploadManyFiles ](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/storage/transfermanager.html) ([ firstFilePath , secondFilePath ]); 

for ( const filePath of [ firstFilePath , secondFilePath ]) { 
console . log ( ` ${ filePath } uploaded to ${ bucketName } .` ); 
} 
} 

uploadManyFilesWithTransferManager (). catch ( console . error ); 
```





The following sample uploads all objects with a common prefix concurrently:
























```
/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// The ID of your GCS bucket 
// const bucketName = 'your-unique-bucket-name'; 

// The local directory to upload 
// const directoryName = 'your-directory'; 

// Imports the Google Cloud client library 
const { Storage , TransferManager } = require ( '[@google-cloud/storage](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/overview.html)' ); 

// Creates a client 
const storage = new [ Storage ](https://berlin.devsitetest.how/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html) (); 

// Creates a transfer manager client 
const transferManager = new [ TransferManager ](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/storage/transfermanager.html) ( storage . bucket ( bucketName )); 

async function uploadDirectoryWithTransferManager () { 
// Uploads the directory 
await transferManager . [ uploadManyFiles ](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/storage/transfermanager.html) ( directoryName ); 

console . log ( ` ${ directoryName } uploaded to ${ bucketName } .` ); 
} 

uploadDirectoryWithTransferManager (). catch ( console . error ); 
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
* Upload a file. 
* 
* @param string $bucketName The name of your Cloud Storage bucket. 
* (e.g. 'my-bucket') 
* @param string $objectName The name of your Cloud Storage object. 
* (e.g. 'my-object') 
* @param string $source The path to the file to upload. 
* (e.g. '/path/to/your/file') 
*/ 
function upload_object(string $bucketName, string $objectName, string $source): void 
{ 
$storage = new StorageClient(); 
if (!$file = fopen($source, 'r')) { 
throw new \InvalidArgumentException('Unable to open file for reading'); 
} 
$bucket = $storage->bucket($bucketName); 
$object = $bucket->upload($file, [ 
'name' => $objectName 
]); 
printf('Uploaded %s to gs://%s/%s' . PHP_EOL, basename($source), $bucketName, $objectName); 
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







The following sample uploads an individual object:
























```
from google.cloud import [ storage ](https://berlin.devsitetest.how/python/docs/reference/storage/latest)

def upload_blob ( bucket_name , source_file_name , destination_blob_name ): 
"""Uploads a file to the bucket.""" 
# The ID of your GCS bucket 
# bucket_name = "your-bucket-name" 
# The path to your file to upload 
# source_file_name = "local/path/to/file" 
# The ID of your GCS object 
# destination_blob_name = "storage-object-name" 

storage_client = [ storage ](https://berlin.devsitetest.how/python/docs/reference/storage/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html) () 
bucket = storage_client . [ bucket ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket) ( bucket_name ) 
blob = bucket . blob ( destination_blob_name ) 

# Optional: set a generation-match precondition to avoid potential race conditions 
# and data corruptions. The request to upload is aborted if the object's 
# generation number does not match your precondition. For a destination 
# object that does not yet exist, set the if_generation_match precondition to 0. 
# If the destination object already exists in your bucket, set instead a 
# generation-match precondition using its generation number. 
generation_match_precondition = 0 

blob . [ upload_from_filename ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_filename) ( source_file_name , if_generation_match = generation_match_precondition ) 

print ( 
f "File { source_file_name } uploaded to { destination_blob_name } ." 
) 
```





The following sample uploads multiple objects concurrently:
























```
def upload_many_blobs_with_transfer_manager ( 
bucket_name , filenames , source_directory = "" , workers = 8 
): 
"""Upload every file in a list to a bucket, concurrently in a process pool. 

Each blob name is derived from the filename, not including the 
`source_directory` parameter. For complete control of the blob name for each 
file (and other aspects of individual blob metadata), use 
transfer_manager.upload_many() instead. 
""" 

# The ID of your GCS bucket 
# bucket_name = "your-bucket-name" 

# A list (or other iterable) of filenames to upload. 
# filenames = ["file_1.txt", "file_2.txt"] 

# The directory on your computer that is the root of all of the files in the 
# list of filenames. This string is prepended (with os.path.join()) to each 
# filename to get the full path to the file. Relative paths and absolute 
# paths are both accepted. This string is not included in the name of the 
# uploaded blob; it is only used to find the source files. An empty string 
# means "the current working directory". Note that this parameter allows 
# directory traversal (e.g. "/", "../") and is not intended for unsanitized 
# end user input. 
# source_directory="" 

# The maximum number of processes to use for the operation. The performance 
# impact of this value depends on the use case, but smaller files usually 
# benefit from a higher number of processes. Each additional process occupies 
# some CPU and memory resources until finished. Threads can be used instead 
# of processes by passing `worker_type=transfer_manager.THREAD`. 
# workers=8 

from google.cloud.storage import [ Client ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html) , [ transfer_manager ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)

storage_client = Client () 
bucket = storage_client . [ bucket ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket) ( bucket_name ) 

results = [ transfer_manager ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html) . [ upload_many_from_filenames ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html) ( 
bucket , filenames , source_directory = source_directory , max_workers = workers 
) 

for name , result in zip ( filenames , results ): 
# The results list is either `None` or an exception for each filename in 
# the input list, in order. 

if isinstance ( result , Exception ): 
print ( "Failed to upload {} due to exception: {} " . format ( name , result )) 
else : 
print ( "Uploaded {} to {} ." . format ( name , bucket . name )) 
```





The following sample uploads all objects with a common prefix concurrently:
























```
def upload_directory_with_transfer_manager ( bucket_name , source_directory , workers = 8 ): 
"""Upload every file in a directory, including all files in subdirectories. 

Each blob name is derived from the filename, not including the `directory` 
parameter itself. For complete control of the blob name for each file (and 
other aspects of individual blob metadata), use 
transfer_manager.upload_many() instead. 
""" 

# The ID of your GCS bucket 
# bucket_name = "your-bucket-name" 

# The directory on your computer to upload. Files in the directory and its 
# subdirectories will be uploaded. An empty string means "the current 
# working directory". 
# source_directory="" 

# The maximum number of processes to use for the operation. The performance 
# impact of this value depends on the use case, but smaller files usually 
# benefit from a higher number of processes. Each additional process occupies 
# some CPU and memory resources until finished. Threads can be used instead 
# of processes by passing `worker_type=transfer_manager.THREAD`. 
# workers=8 

from pathlib import Path 

from google.cloud.storage import [ Client ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html) , [ transfer_manager ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)

storage_client = Client () 
bucket = storage_client . [ bucket ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket) ( bucket_name ) 

# Generate a list of paths (in string form) relative to the `directory`. 
# This can be done in a single list comprehension, but is expanded into 
# multiple lines here for clarity. 

# First, recursively get all files in `directory` as Path objects. 
directory_as_path_obj = Path ( source_directory ) 
paths = directory_as_path_obj . rglob ( "*" ) 

# Filter so the list only includes files, not directories themselves. 
file_paths = [ path for path in paths if path . is_file ()] 

# These paths are relative to the current working directory. Next, make them 
# relative to `directory` 
relative_paths = [ path . relative_to ( source_directory ) for path in file_paths ] 

# Finally, convert them all to strings. 
string_paths = [ str ( path ) for path in relative_paths ] 

print ( "Found {} files." . format ( len ( string_paths ))) 

# Start the upload. 
results = [ transfer_manager ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html) . [ upload_many_from_filenames ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html) ( 
bucket , string_paths , source_directory = source_directory , max_workers = workers 
) 

for name , result in zip ( string_paths , results ): 
# The results list is either `None` or an exception for each filename in 
# the input list, in order. 

if isinstance ( result , Exception ): 
print ( "Failed to upload {} due to exception: {} " . format ( name , result )) 
else : 
print ( "Uploaded {} to {} ." . format ( name , bucket . name )) 
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
def upload_file bucket_name :, local_file_path :, file_name : nil 
# The ID of your GCS bucket 
# bucket_name = "your-unique-bucket-name" 

# The path to your file to upload 
# local_file_path = "/local/path/to/file.txt" 

# The ID of your GCS object 
# file_name = "your-file-name" 

require "google/cloud/storage" 

storage = Google :: Cloud :: [ Storage ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
bucket = storage . bucket bucket_name , skip_lookup : true 

file = bucket . [ create_file ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) local_file_path , file_name 

puts "Uploaded #{ local_file_path } as #{ file . name } in bucket #{ bucket_name } " 
end 
```


























































```
use google_cloud_storage :: client :: Storage ; 

pub async fn sample ( 
client : & Storage , 
bucket : & str , 
object : & str , 
file_path : & str , 
) - > Result (), anyhow :: Error > { 
let payload = tokio :: fs :: File :: open ( file_path ). await ? ; 
let _result = client 
. write_object ( format! ( "projects/_/buckets/{bucket}" ), object , payload ) 
. send_unbuffered () 
. await ? ; 

println! ( "Uploaded {file_path} to {object} in bucket {bucket}." ); 
Ok (()) 
} 
```




































You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_object) to upload an object.
Either `content` or `source` must be specified.




















```
# Create a text object in Cloud Storage
resource "google_storage_bucket_object" "default" {
name = "new-object"
# Use `source` or `content`
# source = "/path/to/an/object"
content = "Data as string to be uploaded"
content_type = "text/plain"
bucket = google_storage_bucket.static.id
}
```





[JSON API](#json-api) [XML API](#xml-api) 
More 




The JSON API distinguishes between *media uploads*, in which only
object data is included in the request, and *JSON API multipart uploads*,
in which both object data and [object metadata](/storage/docs/metadata) are included in the
request.

#### Media upload (a single-request upload without object metadata)

- 

Have gcloud CLI [installed and initialized](/sdk/docs/install) , which lets
you generate an access token for the `Authorization` header. 


- 

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](/storage/docs/json_api) with a [`POST` Object](/storage/docs/json_api/v1/objects/insert)
request:


```
curl -X POST --data-binary @ OBJECT_LOCATION \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: OBJECT_CONTENT_TYPE " \
"https://storage.apis-berlin-build0.goog/upload/storage/v1/b/ BUCKET_NAME /o?uploadType=media&name= OBJECT_NAME "
```


Where:

- ` OBJECT_LOCATION ` is the local path to
your object. For example, `Desktop/dog.png`.

- ` OBJECT_CONTENT_TYPE ` is the
[content type](/storage/docs/metadata#content-type) of the object. For example, `image/png`.

- ` BUCKET_NAME ` is the name of the bucket to
which you are uploading your object. For example, `my-bucket`.

- ` OBJECT_NAME ` is the URL-encoded name you
want to give your object. For example, `pets/dog.png`,
URL-encoded as `pets%2Fdog.png`.

#### JSON API multipart upload (a single-request upload that includes object metadata)

- 

Have gcloud CLI [installed and initialized](/sdk/docs/install) , which lets
you generate an access token for the `Authorization` header. 


- 

Create a [`multipart/related`](https://datatracker.ietf.org/doc/html/rfc2387) file that contains the following
information:


```
-- BOUNDARY_STRING 
Content-Type: application/json; charset=UTF-8

OBJECT_METADATA 

-- BOUNDARY_STRING 
Content-Type: OBJECT_CONTENT_TYPE 

OBJECT_DATA 
-- BOUNDARY_STRING --
```


Where:

- ` BOUNDARY_STRING ` is a string
you define that identifies the different parts of the multipart
file. For example, `separator_string`.

- ` OBJECT_METADATA ` is metadata you want to
include for the file, in [JSON format](/storage/docs/json_api/v1/objects#resource-representations). At a minimum, this
section should include a `name` attribute for the object, for
example `{"name": "myObject"}`.

- ` OBJECT_CONTENT_TYPE ` is the
[content type](/storage/docs/metadata#content-type) of the object. For example, `text/plain`.

- ` OBJECT_DATA ` is the data for the object.

For example:


```
--separator_string
Content-Type: application/json; charset=UTF-8

{"name":"my-document.txt"}

--separator_string
Content-Type: text/plain

This is a text file.
--separator_string--
```


- 

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](/storage/docs/json_api) with a [`POST` Object](/storage/docs/json_api/v1/objects/insert)
request:


```
curl -X POST --data-binary @ MULTIPART_FILE_LOCATION \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: multipart/related; boundary= BOUNDARY_STRING " \
-H "Content-Length: MULTIPART_FILE_SIZE " \
"https://storage.apis-berlin-build0.goog/upload/storage/v1/b/ BUCKET_NAME /o?uploadType=multipart"
```


Where:

- ` MULTIPART_FILE_LOCATION ` is the local
path to the multipart file you created in step 2. For example,
`Desktop/my-upload.multipart`.

- ` BOUNDARY_STRING ` is the boundary string
you defined in Step 2. For example, `my-boundary`.

- ` MULTIPART_FILE_SIZE ` is the total size,
in bytes, of the multipart file you created in Step 2. For
example, `2000000`.

- ` BUCKET_NAME ` is the name of the bucket to
which you are uploading your object. For example, `my-bucket`.

If the request succeeds, the server returns the HTTP `200 OK` status
code along with the file's metadata.



- 

Have gcloud CLI [installed and initialized](/sdk/docs/install) , which lets
you generate an access token for the `Authorization` header. 


- 

Use [`cURL`](http://curl.haxx.se/) to call the [XML API](/storage/docs/xml-api/overview) with a [`PUT` Object](/storage/docs/xml-api/put-object-upload)
request:


```
curl -X PUT --data-binary @ OBJECT_LOCATION \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: OBJECT_CONTENT_TYPE " \
"https://storage.apis-berlin-build0.goog/ BUCKET_NAME / OBJECT_NAME "
```


Where:

- ` OBJECT_LOCATION ` is the local path to your
object. For example, `Desktop/dog.png`.

- ` OBJECT_CONTENT_TYPE ` is the
[content type](/storage/docs/metadata#content-type) of the object. For example, `image/png`.

- ` BUCKET_NAME ` is the name of the bucket to
which you are uploading your object. For example, `my-bucket`.

- ` OBJECT_NAME ` is the URL-encoded name you
want to give your object. For example, `pets/dog.png`,
URL-encoded as `pets%2Fdog.png`.

You can set additional [object metadata](/storage/docs/metadata) as part of your object upload
in the headers of the request in the same way the previous example sets
`Content-Type`. When working with the XML API, metadata can only be set at
the time the object is written, such as when uploading, copying, or
replacing the object. For more information, see
[Editing object metadata](/storage/docs/viewing-editing-metadata#set-object-metadata-xml).




## Upload the contents of a directory to a bucket

Complete the following steps to copy the contents of a directory to a bucket:


[Command line](#command-line) 
More 




Use the [`gcloud storage rsync`](/sdk/gcloud/reference/storage/rsync) command with the `--recursive` flag:


```
gcloud storage rsync --recursive LOCAL_DIRECTORY gs:// DESTINATION_BUCKET_NAME / FOLDER_NAME 
```


Where:

- 

` LOCAL_DIRECTORY ` is the path to the directory that
contains the files you want to upload as objects. For example,
`~/my_directory`.

- 

` DESTINATION_BUCKET_NAME ` is the name of the
bucket to which you want to upload objects. For example, `my-bucket`.

- 

` FOLDER_NAME ` (optional) is the name of the folder
within the bucket that you want to upload objects to. For example,
`my-folder`.

If successful, the response looks like the following example:


```
Completed files 1/1 | 5.6kiB/5.6kiB
```


You can set fixed-key and custom [object metadata](/storage/docs/metadata) as part of your
object upload by using [command flags](/sdk/gcloud/reference/storage/cp#FLAGS).



## What's next

- Learn about [naming requirements for objects](/storage/docs/objects#naming).

- Learn about using [folders](/storage/docs/folders-overview) to organize your objects.

- [Transfer objects from your Compute Engine instance](/compute/docs/instances/transfer-files#gcstransfer).

- [Control who has access](/storage/docs/access-control) to your objects and buckets.

- [View your object's metadata](/storage/docs/viewing-editing-metadata), including the URL for the object.