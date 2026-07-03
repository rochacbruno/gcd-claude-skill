# Cloud Storage client libraries

Source: https://berlin.devsitetest.how/storage/docs/reference/libraries
Last updated: 2026-07-02

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












# Cloud Storage client libraries 






- On this page ** 
- [ Install the client library ](#install)
- [ Set up authentication ](#authentication)
- [ Use the client library ](#use)
- [ Authentication options ](#auth-options)
- [ Using the client library with Cloud Shell Editor ](#cloud-shell-editor)
- [ More examples ](#more_examples)
- [ Additional resources ](#resources)
- 












This page shows how to get started with the Cloud Client Libraries for the
Google Cloud Storage API. Client libraries make it easier to access
Google Cloud Dedicated in Germany APIs from a supported language. Although you can use
Google Cloud Dedicated in Germany APIs directly by making raw requests to the server, client
libraries provide simplifications that significantly reduce the amount of code
you need to write.

Read more about the Cloud Client Libraries
and the older Google API Client Libraries in
[Client libraries explained](/apis/docs/client-libraries-explained).



## Install the client library 















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 










For more information about installing the C++ library,
see [Setting up a C++ development environment](/cpp/docs/setup).






































If you are using Visual Studio 2017 or higher, open nuget package manager window and type the following:


```
Install-Package Google.Cloud.Storage.V1
```


If you are using .NET Core command-line interface tools to install your dependencies, run the following command:


```
dotnet add package Google.Cloud.Storage.V1
```






For more information, see [Setting Up a C# Development Environment](/dotnet/docs/setup).






































```
go get cloud.google.com/go/storage
```





For more information, see [Setting Up a Go Development Environment](/go/docs/setup).








































If you are using [Maven](https://maven.apache.org/), add
the following to your `pom.xml` file. For more information about
BOMs, see [The Google Cloud Platform Libraries BOM](https://berlin.devsitetest.how/java/docs/bom).
























```
dependencyManagement >
dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>libraries - bom / artifactId >
version>26 .78.0 / version >
type>pom / type >
scope>import / scope >
/ dependency >
/ dependencies >
/ dependencyManagement >

dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>google - cloud - storage / artifactId >
/ dependency >
dependency >
groupId>com . google . cloud / groupId >
artifactId>google - cloud - storage - control / artifactId >
/ dependency >
/ dependencies >
```



If you are using [Gradle](https://gradle.org/),
add the following to your dependencies:
























```
implementation platform ( ' com . google . cloud : libraries - bom : 26.83.0 ' ) 

implementation ' com . google . cloud : google - cloud - storage ' 
```



If you are using [sbt](https://www.scala-sbt.org/), add
the following to your dependencies:
























```
libraryDependencies += "com.google.cloud" % "google-cloud-storage" % "2.69.0" 
```



If you're using Visual Studio Code or IntelliJ, you can add client libraries to your
project using the following IDE plugins:


- [Cloud Code for VS Code](/code/docs/vscode/client-libraries)

- [Cloud Code for IntelliJ](/code/docs/intellij/client-libraries)

The plugins provide additional functionality, such as key management for service accounts. Refer
to each plugin's documentation for details.





For more information, see [Setting Up a Java Development Environment](/java/docs/setup).







































```
npm install @google-cloud/storage
```





For more information, see [Setting Up a Node.js Development Environment](/nodejs/docs/setup).






































```
composer require google/cloud-storage
```





For more information, see [Using PHP on Google Cloud](/php/docs).








































```
pip install --upgrade google-cloud-storage
```






For more information, see [Setting Up a Python Development Environment](/python/docs/setup).







































```
gem install google-cloud-storage
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






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








A sign-in screen appears. After you sign in, your credentials are stored in the
[
local credential file used by ADC](/docs/authentication/application-default-credentials#personal).















## Use the client library

The following example shows how to use the client library.

















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 
































```
#include "google/cloud/storage/client.h" 
#include 
#include 
#include 
#include 
#include 
void StorageQuickstart ( std :: string const & bucket_name ) { 
// Create an aliases to make the code easier to read. 
namespace gcs = :: google :: cloud :: storage ; 

// Create a client to communicate with Google Cloud Storage. This client 
// uses the default configuration for authentication and project id. 
auto client = gcs :: Client (); 

// Create a bucket 
google :: cloud :: StatusOr :: BucketMetadata > metadata = client . CreateBucket ( 
bucket_name , gcs :: BucketMetadata (). set_location ( "US" ). set_storage_class ( 
gcs :: storage_class :: Standard ())); 
if ( ! metadata ) throw std :: move ( metadata ). status (); 

std :: cout "Created bucket " metadata - > name () " \n " ; 
} 
```


































































```
using Google.Apis.Storage.v1.Data ; 
using [ Google.Cloud.Storage.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html) ; 
using System ; 

public class CreateBucketSample 
{ 
public Bucket CreateBucket ( 
string projectId = "your-project-id" , 
string bucketName = "your-unique-bucket-name" ) 
{ 
var storage = [ StorageClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create) (); 
var bucket = storage . CreateBucket ( projectId , bucketName ); 
Console . WriteLine ( $"Created {bucketName}." ); 
return bucket ; 
} 
} 
```

































































```
// Sample storage-quickstart creates a Google Cloud Storage bucket. 
package main 

import ( 
"context" 
"fmt" 
"log" 
"time" 

"cloud.google.com/go/storage" 
) 

func main () { 
ctx := context . Background () 

// Sets your Google Cloud Platform project ID. 
projectID := "YOUR_PROJECT_ID" 

// Creates a client. 
client , err := storage . NewClient ( ctx ) 
if err != nil { 
log . Fatalf ( "Failed to create client: %v" , err ) 
} 
defer client . Close () 

// Sets the name for the new bucket. 
bucketName := "my-new-bucket" 

// Creates a Bucket instance. 
bucket := client . [ Bucket ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket) ( bucketName ) 

// Creates the new bucket. 
ctx , cancel := context . WithTimeout ( ctx , time . Second * 10 ) 
defer cancel () 
if err := bucket . [ Create ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create) ( ctx , projectID , nil ); err != nil { 
log . Fatalf ( "Failed to create bucket: %v" , err ) 
} 

fmt . Printf ( "Bucket %v created.\n" , bucketName ) 
} 
```


































































```
// Imports the Google Cloud client library 
import com.google.cloud.storage.[Bucket](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) ; 
import com.google.cloud.storage.[BucketInfo](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html) ; 
import com.google.cloud.storage.[Storage](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) ; 
import com.google.cloud.storage.[StorageOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) ; 

public class QuickstartSample { 
public static void main ( String ... args ) throws Exception { 
// Instantiates a client 
[ Storage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [ StorageOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) . getDefaultInstance (). [ getService ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__) (); 

// The name for the new bucket 
String bucketName = args [ 0 ] ; // "my-new-bucket"; 

// Creates the new bucket 
[ Bucket ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage . [ create ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____) ( BucketInfo . of ( bucketName )); 

System . out . printf ( "Bucket %s created.%n" , bucket . getName ()); 
} 
} 
```


































































```
// Imports the Google Cloud client library 
const { Storage } = require ( '[@google-cloud/storage](https://berlin.devsitetest.how/nodejs/docs/reference/storage/latest/overview.html)' ); 

// For more information on ways to initialize Storage, please see 
// https://googleapis.dev/nodejs/storage/latest/Storage.html 

// Creates a client using Application Default Credentials 
const storage = new [ Storage ](https://berlin.devsitetest.how/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html) (); 

// Creates a client from a Google service account key 
// const storage = new Storage({keyFilename: 'key.json'}); 

/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// The ID of your GCS bucket 
// const bucketName = 'your-unique-bucket-name'; 

async function createBucket () { 
// Creates the new bucket 
await storage . createBucket ( bucketName ); 
console . log ( `Bucket ${ bucketName } created.` ); 
} 

createBucket (). catch ( console . error ); 
```

































































```
# Includes the autoloader for libraries installed with composer 
require __DIR__ . '/vendor/autoload.php'; 

# Imports the Google Cloud client library 
use Google\Cloud\Storage\StorageClient; 

# Your Google Cloud Platform project ID 
$projectId = 'YOUR_PROJECT_ID'; 

# Instantiates a client 
$storage = new StorageClient([ 
'projectId' => $projectId 
]); 

# The name for the new bucket 
$bucketName = 'my-new-bucket'; 

# Creates the new bucket 
$bucket = $storage->createBucket($bucketName); 

echo 'Bucket ' . $bucket->name() . ' created.'; 
```


































































```
# Imports the Google Cloud client library 
from google.cloud import [ storage ](https://berlin.devsitetest.how/python/docs/reference/storage/latest)

# Instantiates a client 
storage_client = [ storage ](https://berlin.devsitetest.how/python/docs/reference/storage/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html) () 

# The name for the new bucket 
bucket_name = "my-new-bucket" 

# Creates the new bucket 
bucket = storage_client . [ create_bucket ](https://berlin.devsitetest.how/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_create_bucket) ( bucket_name ) 

print ( f "Bucket { bucket . name } created." ) 
```


































































```
def quickstart bucket_name : 
# Imports the Google Cloud client library 
require "google/cloud/storage" 

# Instantiates a client 
storage = Google :: Cloud :: [ Storage ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)

# The ID to give your GCS bucket 
# bucket_name = "your-unique-bucket-name" 

# Creates the new bucket 
bucket = storage . [ create_bucket ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) bucket_name 

puts "Bucket #{ bucket . name } was created." 
end 
```

























## Authentication options

By default, the client libraries use Application Default Credentials (ADC) to authenticate. For details on setting up ADC for local development or production, see [Set up authentication](#authentication).

If you want to authenticate dynamically or by using in-memory keys, pass a custom credentials object when you initialize the client. For example, you might load keys from a secure vault or configuration system. For a Python code example and details on this configuration, see [Authorize using service account credentials](/storage/docs/authentication#passing-credentials-in-code).

## Using the client library with Cloud Shell Editor


[Go](#go) [Java](#java) [Node.js](#node.js) [Python](#python) 
More 






For step-by-step guidance on running a client library in Cloud Shell Editor:


- 

Click Guide me**.


- 

You see a panel **Learn**. Click **Start** to follow the tutorial.

[Guide me](https://console.cloud.berlin-build0.goog/?walkthrough_id=storage--client-libs-quickstart-go)






For step-by-step guidance on running a client library in Cloud Shell Editor:


- 

Click **Guide me**.


- 

You see a panel **Learn**. Click **Start** to follow the tutorial.

[Guide me](https://console.cloud.berlin-build0.goog/?walkthrough_id=storage--client-libs-quickstart-java)






For step-by-step guidance on running a client library in Cloud Shell Editor:


- 

Click **Guide me**.


- 

You see a panel **Learn**. Click **Start** to follow the tutorial.

[Guide me](https://console.cloud.berlin-build0.goog/?walkthrough_id=storage--client-libs-quickstart-nodejs)






For step-by-step guidance on running a client library in Cloud Shell Editor:


- 

Click **Guide me**.


- 

You see a panel **Learn**. Click **Start** to follow the tutorial.

[Guide me](https://console.cloud.berlin-build0.goog/?walkthrough_id=storage--client-libs-quickstart-python)




## More examples

For more examples of using client libraries with Cloud Storage, see the
following guides:

- [Create buckets](/storage/docs/creating-buckets#client-libraries)

- [Upload objects from a filesystem](/storage/docs/uploading-objects#storage-upload-object-client-libraries)

- [Download objects](/storage/docs/downloading-objects#client-libraries-download-object)



## Additional resources















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 










The following list contains links to more resources related to the
client library for C++:

- [API reference](/cpp/docs/reference/storage/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues) 

- [`google-cloud-storage` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-storage%5D%5Bc%2B%2B%5D) 

- [Source code](https://github.com/googleapis/google-cloud-cpp) 






































The following list contains links to more resources related to the
client library for C#:

- [API reference](/dotnet/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues) 

- [`google-cloud-storage` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-storage%5D+%5Bc%23%5D) 

- [Source code](https://github.com/googleapis/google-cloud-dotnet) 





































The following list contains links to more resources related to the
client library for Go:

- [API reference](https://godoc.org/cloud.google.com/go/storage) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-go/issues) 

- [`google-cloud-storage` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-storage%5D+%5Bgo%5D) 

- [Source code](https://github.com/googleapis/google-cloud-go) 







































The following list contains links to more resources related to the
client library for Java:

- [API reference](/java/docs/reference/google-cloud-storage/latest/overview) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/java-storage/issues) 

- [`google-cloud-storage` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-storage%5D+%5Bjava%5D) 

- [Source code](https://github.com/googleapis/java-storage) 







































The following list contains links to more resources related to the
client library for Node.js:

- [API reference](/nodejs/docs/reference/storage/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/nodejs-storage/issues) 

- [`google-cloud-storage` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-storage%5D+%5Bnode.js%5D) 

- [Source code](https://github.com/googleapis/nodejs-storage) 






































The following list contains links to more resources related to the
client library for PHP:

- [API reference](https://berlin.devsitetest.how/php/docs/reference/cloud-storage/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-php/issues) 

- [`google-cloud-storage` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-storage%5D+%5Bphp%5D) 

- [Source code](https://github.com/googleapis/google-cloud-php) 







































The following list contains links to more resources related to the
client library for Python:

- [API reference](/python/docs/reference/storage/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/python-storage/issues) 

- [`google-cloud-storage` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-storage%5D+%5Bpython%5D) 

- [Source code](https://github.com/googleapis/python-storage) 







































The following list contains links to more resources related to the
client library for Ruby:

- [API reference](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues) 

- [`google-cloud-storage` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-storage%5D+%5Bruby%5D) 

- [Source code](https://github.com/googleapis/google-cloud-ruby)