# Dataproc client libraries

Source: https://berlin.devsitetest.how/managed-spark/docs/reference/libraries
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/managed-spark/docs/tpc-differences) for more details.














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

Data analytics

](https://berlin.devsitetest.how/docs/data)






- 








[

Managed Service for Apache Spark

](https://berlin.devsitetest.how/managed-spark/docs)






- 








[

Reference

](https://berlin.devsitetest.how/managed-spark/docs/reference)












# Dataproc client libraries 

















This page shows how to get started with the Cloud Client Libraries for the
Dataproc API. Client libraries make it easier to access
Google Cloud Dedicated in Germany APIs from a supported language. Although you can use
Google Cloud Dedicated in Germany APIs directly by making raw requests to the server, client
libraries provide simplifications that significantly reduce the amount of code
you need to write.

However, we recommend using the older Google API Client
Libraries if running on [
App Engine standard environment](/appengine/docs/about-the-standard-environment). Read more about the Cloud Client Libraries
and the older Google API Client Libraries in
[Client libraries explained](/apis/docs/client-libraries-explained).

Managed Service for Apache Spark Cloud Client Libraries may
be in alpha or beta stage. See the library reference for details.



## Install the client library














### C++ 






See [Setting up a C++ development environment](/cpp/docs/setup)
for details about this client library's requirements and install dependencies.


































### C# 




Also see [Google Cloud Libraries for .NET](https://github.com/googleapis/google-cloud-dotnet?tab=readme-ov-file#google-cloud-libraries-for-net).




For more information, see [Setting Up a C# Development Environment](/dotnet/docs/setup).


































### Go 





```
go get cloud.google.com/go/dataproc/apiv1
```

For more information, see [Install the Cloud Client Libraries for Go](/go/docs/setup#install_the_cloud_client_libraries_for_go).




For more information, see [Setting Up a Go Development Environment](/go/docs/setup).



































### Java 





If you are using Maven, add this to your pom.xml file:


```
dependency >
groupId>com . google . cloud / groupId >
artifactId>google - cloud - dataproc / artifactId >
version> insert dataproc - library - version here / version >
/ dependency >
```


If you are using Gradle, add this to your dependencies:


```
compile group : ' com . google . cloud ' , name : ' google - cloud - dataproc ' , version : ' insert dataproc - library - version here ' 
```






For more information, see [Setting Up a Java Development Environment](/java/docs/setup).



































### Node.js 





```
npm install --save @google-cloud/dataproc
```





For more information, see [Setting Up a Node.js Development Environment](/nodejs/docs/setup).


































### PHP 






```
composer require google/cloud
```






For more information, see [Using PHP on Google Cloud](/php/docs).



































### Python 





```
pip install --upgrade google-cloud-dataproc
```





For more information, see [Setting Up a Python Development Environment](/python/docs/setup).



































### Ruby 





```
gem install google-cloud-dataproc
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






+






















```
#include "google/cloud/dataproc/v1/cluster_controller_client.h" 
#include "google/cloud/common_options.h" 
#include 

int main ( int argc , char * argv []) try { 
if ( argc != 3 ) { 
std :: cerr "Usage: " argv [ 0 ] " project-id region \n " ; 
return 1 ; 
} 
std :: string const project_id = argv [ 1 ]; 
std :: string const region = argv [ 2 ]; 

namespace dataproc = :: google :: cloud :: dataproc_v1 ; 

auto client = dataproc :: ClusterControllerClient ( 
dataproc :: MakeClusterControllerConnection ( region == "global" ? "" 
: region )); 

for ( auto c : client . ListClusters ( project_id , region )) { 
if ( ! c ) throw std :: move ( c ). status (); 
std :: cout c - > cluster_name () " \n " ; 
} 

return 0 ; 
} catch ( google :: cloud :: Status const & status ) { 
std :: cerr "google::cloud::Status thrown: " status " \n " ; 
return 1 ; 
} 
```










































### Go 




























```
import ( 
"context" 
"fmt" 
"io" 

dataproc "cloud.google.com/go/dataproc/apiv1" 
"cloud.google.com/go/dataproc/apiv1/dataprocpb" 
"google.golang.org/api/option" 
) 

func createCluster ( w io . Writer , projectID , region , clusterName string ) error { 
// projectID := "your-project-id" 
// region := "us-central1" 
// clusterName := "your-cluster" 
ctx := context . Background () 

// Create the cluster client. 
endpoint := region + "-dataproc.googleapis.com:443" 
clusterClient , err := dataproc . NewClusterControllerClient ( ctx , option . WithEndpoint ( endpoint )) 
if err != nil { 
return fmt . Errorf ( "dataproc.NewClusterControllerClient: %w" , err ) 
} 
defer clusterClient . Close () 

// Create the cluster config. 
req := & dataprocpb . CreateClusterRequest { 
ProjectId : projectID , 
Region : region , 
Cluster : & dataprocpb . Cluster { 
ProjectId : projectID , 
ClusterName : clusterName , 
Config : & dataprocpb . ClusterConfig { 
MasterConfig : & dataprocpb . InstanceGroupConfig { 
NumInstances : 1 , 
MachineTypeUri : "n1-standard-2" , 
}, 
WorkerConfig : & dataprocpb . InstanceGroupConfig { 
NumInstances : 2 , 
MachineTypeUri : "n1-standard-2" , 
}, 
}, 
}, 
} 

// Create the cluster. 
op , err := clusterClient . CreateCluster ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "CreateCluster: %w" , err ) 
} 

resp , err := op . Wait ( ctx ) 
if err != nil { 
return fmt . Errorf ( "CreateCluster.Wait: %w" , err ) 
} 

// Output a success message. 
fmt . Fprintf ( w , "Cluster created successfully: %s" , resp . ClusterName ) 
return nil 
} 
```







































### Java 




























```
import com.google.api.gax.longrunning.[OperationFuture](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html) ; 
import com.google.cloud.dataproc.v1.[Cluster](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) ; 
import com.google.cloud.dataproc.v1.[ClusterConfig](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html) ; 
import com.google.cloud.dataproc.v1.[ClusterControllerClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html) ; 
import com.google.cloud.dataproc.v1.[ClusterControllerSettings](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html) ; 
import com.google.cloud.dataproc.v1.[ClusterOperationMetadata](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterOperationMetadata.html) ; 
import com.google.cloud.dataproc.v1.[InstanceGroupConfig](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) ; 
import java.io.IOException ; 
import java.util.concurrent.ExecutionException ; 

public class CreateCluster { 

public static void createCluster () throws IOException , InterruptedException { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String region = "your-project-region" ; 
String clusterName = "your-cluster-name" ; 
createCluster ( projectId , region , clusterName ); 
} 

public static void createCluster ( String projectId , String region , String clusterName ) 
throws IOException , InterruptedException { 
String myEndpoint = String . format ( "%s-dataproc.googleapis.com:443" , region ); 

// Configure the settings for the cluster controller client. 
[ ClusterControllerSettings ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html) clusterControllerSettings = 
[ ClusterControllerSettings ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html) . newBuilder (). setEndpoint ( myEndpoint ). build (); 

// Create a cluster controller client with the configured settings. The client only needs to be 
// created once and can be reused for multiple requests. Using a try-with-resources 
// closes the client, but this can also be done manually with the .close() method. 
try ( [ ClusterControllerClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html) clusterControllerClient = 
[ ClusterControllerClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html) . create ( clusterControllerSettings )) { 
// Configure the settings for our cluster. 
[ InstanceGroupConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) masterConfig = 
[ InstanceGroupConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) . newBuilder () 
. [ setMachineTypeUri ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setMachineTypeUri_java_lang_String_) ( "n1-standard-2" ) 
. [ setNumInstances ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setNumInstances_int_) ( 1 ) 
. build (); 
[ InstanceGroupConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) workerConfig = 
[ InstanceGroupConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) . newBuilder () 
. [ setMachineTypeUri ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setMachineTypeUri_java_lang_String_) ( "n1-standard-2" ) 
. [ setNumInstances ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setNumInstances_int_) ( 2 ) 
. build (); 
[ ClusterConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html) clusterConfig = 
[ ClusterConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html) . newBuilder () 
. [ setMasterConfig ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.Builder.html#com_google_cloud_dataproc_v1_ClusterConfig_Builder_setMasterConfig_com_google_cloud_dataproc_v1_InstanceGroupConfig_) ( masterConfig ) 
. setWorkerConfig ( workerConfig ) 
. build (); 
// Create the cluster object with the desired cluster config. 
[ Cluster ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) cluster = 
[ Cluster ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) . newBuilder (). setClusterName ( clusterName ). setConfig ( clusterConfig ). build (); 

// Create the Cloud Dataproc cluster. 
OperationFuture , ClusterOperationMetadata > createClusterAsyncRequest = 
clusterControllerClient . [ createClusterAsync ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html#com_google_cloud_dataproc_v1_ClusterControllerClient_createClusterAsync_com_google_cloud_dataproc_v1_CreateClusterRequest_) ( projectId , region , cluster ); 
[ Cluster ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) response = createClusterAsyncRequest . [ get ](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__) (); 

// Print out a success message. 
System . out . printf ( "Cluster created successfully: %s" , response . [ getClusterName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html#com_google_cloud_dataproc_v1_Cluster_getClusterName__) ()); 

} catch ( ExecutionException e ) { 
System . err . println ( String . format ( "Error executing createCluster: %s " , e . getMessage ())); 
} 
} 
} 
```







































### Node.js 





.






















```
const dataproc = require ( '[@google-cloud/dataproc](https://berlin.devsitetest.how/nodejs/docs/reference/dataproc/latest/overview.html)' ); 

// TODO(developer): Uncomment and set the following variables 
// projectId = 'YOUR_PROJECT_ID' 
// region = 'YOUR_CLUSTER_REGION' 
// clusterName = 'YOUR_CLUSTER_NAME' 

// Create a client with the endpoint set to the desired cluster region 
const client = new dataproc . v1 . [ ClusterControllerClient ](https://berlin.devsitetest.how/nodejs/docs/reference/dataproc/latest/overview.html) ({ 
apiEndpoint : ` ${ region } -dataproc.googleapis.com` , 
projectId : projectId , 
}); 

async function createCluster () { 
// Create the cluster config 
const request = { 
projectId : projectId , 
region : region , 
cluster : { 
clusterName : clusterName , 
config : { 
masterConfig : { 
numInstances : 1 , 
machineTypeUri : 'n1-standard-2' , 
}, 
workerConfig : { 
numInstances : 2 , 
machineTypeUri : 'n1-standard-2' , 
}, 
}, 
}, 
}; 

// Create the cluster 
const [ operation ] = await client . createCluster ( request ); 
const [ response ] = await operation . promise (); 

// Output a success message 
console . log ( `Cluster created successfully: ${ response . clusterName } ` ); 
```











































### Python 




























```
from google.cloud import dataproc_v1 as dataproc 

def create_cluster ( project_id , region , cluster_name ): 
"""This sample walks a user through creating a Cloud Dataproc cluster 
using the Python client library. 

Args: 
project_id (string): Project to use for creating resources. 
region (string): Region where the resources should live. 
cluster_name (string): Name to use for creating a cluster. 
""" 

# Create a client with the endpoint set to the desired cluster region. 
cluster_client = dataproc . ClusterControllerClient ( 
client_options = { "api_endpoint" : f " { region } -dataproc.googleapis.com:443" } 
) 

# Create the cluster config. 
cluster = { 
"project_id" : project_id , 
"cluster_name" : cluster_name , 
"config" : { 
"master_config" : { "num_instances" : 1 , "machine_type_uri" : "n1-standard-2" }, 
"worker_config" : { "num_instances" : 2 , "machine_type_uri" : "n1-standard-2" }, 
}, 
} 

# Create the cluster. 
operation = cluster_client . create_cluster ( 
request = { "project_id" : project_id , "region" : region , "cluster" : cluster } 
) 
result = operation . result () 

# Output a success message. 
print ( f "Cluster created successfully: { result . cluster_name } " ) 
```

































## Additional resources














### C++ 






The following list contains links to more resources related to the
client library for C++:

- [API reference](/cpp/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues) 

- [`google-data-dataproc` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-data-dataproc%5D%5Bc%2B%2B%5D) 

- [Source code](https://github.com/googleapis/google-cloud-cpp) 

































### C# 






The following list contains links to more resources related to the
client library for C#:

- [API reference](/dotnet/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues) 

- [`google-data-dataproc` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-data-dataproc%5D+%5Bc%23%5D) 

- [Source code](https://github.com/googleapis/google-cloud-dotnet) 
































### Go 






The following list contains links to more resources related to the
client library for Go:

- [API reference](/go/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-go/issues) 

- [`google-data-dataproc` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-data-dataproc%5D+%5Bgo%5D) 

- [Source code](https://github.com/googleapis/google-cloud-go) 

































### Java 






The following list contains links to more resources related to the
client library for Java:

- [API reference](/java/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-java/issues) 

- [`google-data-dataproc` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-data-dataproc%5D+%5Bjava%5D) 

- [Source code](https://github.com/googleapis/google-cloud-java) 

































### Node.js 






The following list contains links to more resources related to the
client library for Node.js:

- [API reference](/nodejs/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-node/issues) 

- [`google-data-dataproc` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-data-dataproc%5D+%5Bnode.js%5D) 

- [Source code](https://github.com/GoogleCloudPlatform/google-cloud-node) 
































### PHP 






The following list contains links to more resources related to the
client library for PHP:

- [API reference](/php/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-php/issues) 

- [`google-data-dataproc` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-data-dataproc%5D+%5Bphp%5D) 

- [Source code](https://github.com/googleapis/google-cloud-php) 

































### Python 






The following list contains links to more resources related to the
client library for Python:

- [API reference](/python/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-python/issues) 

- [`google-data-dataproc` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-data-dataproc%5D+%5Bpython%5D) 

- [Source code](https://github.com/googleapis/google-cloud-python) 

































### Ruby 






The following list contains links to more resources related to the
client library for Ruby:

- [API reference](/ruby/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues) 

- [`google-data-dataproc` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-data-dataproc%5D+%5Bruby%5D) 

- [Source code](https://github.com/googleapis/google-cloud-ruby)