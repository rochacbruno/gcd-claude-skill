# Bigtable client libraries

Source: https://documentation.s3ns.fr/bigtable/docs/reference/libraries
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/bigtable/docs/tpc-differences) for more details.














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

Databases

](https://documentation.s3ns.fr/docs/databases)






- 








[

Bigtable

](https://documentation.s3ns.fr/bigtable/docs)






- 








[

Reference

](https://documentation.s3ns.fr/bigtable/docs/apis)












# Bigtable client libraries 

















This page shows how to get started with the Cloud Client Libraries for the
Cloud Bigtable API. Client libraries make it easier to access
Cloud de Confiance by S3NS APIs from a supported language. Although you can use
Cloud de Confiance by S3NS APIs directly by making raw requests to the server, client
libraries provide simplifications that significantly reduce the amount of code
you need to write.

Read more about the Cloud Client Libraries
and the older Google API Client Libraries in
[Client libraries explained](/apis/docs/client-libraries-explained).



## Install the client library














### C++ 






To install the C++ Bigtable client library, for example, with [vcpkg](https://vcpkg.io), run the following:


```
vcpkg install google-cloud-cpp[core,bigtable]
```


See the [Setting up a C++ development environment](/cpp/docs/setup) guide for
more details about this client library's requirements and install dependencies.






























### C# 






```
Install-Package Google.Cloud.Bigtable.V2 -Pre
Install-Package Google.Cloud.Bigtable.Admin.V2 -Pre
```





For more information, see [Setting Up a C# Development Environment](/dotnet/docs/setup).






























### Go 





```
go get cloud.google.com/go/bigtable
```





For more information, see [Setting Up a Go Development Environment](/go/docs/setup).































### Java 






If you are using [Maven](https://maven.apache.org/), add
the following to your `pom.xml` file. For more information about
BOMs, see [The Google Cloud Platform Libraries BOM](https://documentation.s3ns.fr/java/docs/bom).
























```
dependencyManagement >
dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>libraries - bom / artifactId >
version>26 .69.0 / version >
type>pom / type >
scope>import / scope >
/ dependency >
/ dependencies >
/ dependencyManagement >

dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>google - cloud - bigtable / artifactId >
/ dependency >
```



If you are using [Gradle](https://gradle.org/),
add the following to your dependencies:
























```
implementation platform ( ' com . google . cloud : libraries - bom : 26.80.0 ' ) 

implementation ' com . google . cloud : google - cloud - bigtable ' 
```



If you are using [sbt](https://www.scala-sbt.org/), add
the following to your dependencies:
























```
libraryDependencies += "com.google.cloud" % "google-cloud-bigtable" % "2.78.0" 
```







For more information, see [Setting Up a Java Development Environment](/java/docs/setup).

























### HBase






The Cloud Bigtable HBase client for Java includes the following Maven
artifacts that you can choose to use in your project, depending on your use
case. The `2.x` versions include an HBase async client that the
`1.x`versions do not have.


- 
`bigtable-hbase-1.x` or `bigtable-hbase-2.x`:
Use one of these artifacts for standalone applications where you control your
dependencies.


- 
`bigtable-hbase-1.x-hadoop` or `bigtable-hbase-2.x-hadoop`:
Use one of these artifacts for [Hadoop](https://hadoop.apache.org/)
environments.


- 
`bigtable-hbase-1.x-shaded` or `bigtable-hbase-2.x-shaded`:
Use one of these artifacts for environments other than Hadoop that require
older versions of the HBase client for Java's dependencies, such as
[protobuf](https://github.com/google/protobuf) and
[Guava](https://github.com/google/guava).


The Bigtable Maven artifacts include the
[`netty-tcnative-boringssl-static`
library](https://netty.io/wiki/forked-tomcat-native.html), which requires that you use Linux, macOS, or Windows on an x86
64-bit processor.

If your application runs in the
[App Engine standard
environment](/appengine/docs/standard/java), you must use a current version of the Java runtime. The Java
7 runtime is deprecated and does not support the HBase client for Java.

The following examples assume that you are using the
`bigtable-hbase-1.x` artifact.

If you are using [Maven](https://maven.apache.org/), add
the following to your `pom.xml` file. For more information about
BOMs, see [The Google Cloud Platform Libraries BOM](https://documentation.s3ns.fr/java/docs/bom).
























```

com.google.cloud.bigtable 
bigtable-hbase-1.x 
2.6.5 

```



If you are using [Gradle](https://gradle.org/),
add the following to your dependencies:
























```
compile 'com.google.cloud.bigtable:bigtable-hbase-1.x:2.6.5'
```



If you are using [sbt](https://www.scala-sbt.org/), add
the following to your dependencies:
























```
libraryDependencies += "com.google.cloud.bigtable" % "bigtable-hbase-1.x" % "2.6.5"
```































### Node.js 






```
npm install @google-cloud/bigtable
```





For more information, see [Setting Up a Node.js Development Environment](/nodejs/docs/setup).






























### PHP 





[Install and enable the gRPC extension](/php/grpc) for PHP, then run the following command:

```
composer require google/cloud-bigtable
```






For more information, see [Using PHP on Google Cloud](/php/docs).































### Python 






```
pip install --upgrade google-cloud-bigtable
```






For more information, see [Setting Up a Python Development Environment](/python/docs/setup).































### Ruby 






```
gem install google-cloud-bigtable
```






For more information, see [Setting Up a Ruby Development Environment](/ruby/docs/setup).


























## Set up authentication

To authenticate calls to Cloud de Confiance by S3NS APIs, client libraries support
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

The following example shows how to use the client library. The example connects
to a Bigtable instance and reads a row from a table.

If you haven't stored any data in Bigtable yet, you can use the

`cbt` CLI
to create a table and add some data. See the [quickstart using
the 
`cbt` CLI
](/bigtable/docs/create-instance-write-data-cbt-cli) for
instructions.
















### C++ 




























```
#include "google/cloud/bigtable/table.h" 

int main ( int argc , char * argv []) try { 
if ( argc != 4 && argc != 5 ) { 
std :: string const cmd = argv [ 0 ]; 
auto last_slash = std :: string ( cmd ). find_last_of ( '/' ); 
std :: cerr "Usage: " cmd . substr ( last_slash + 1 ) 
" 

[app_profile_id] \n " ; 
return 1 ; 
} 

std :: string const project_id = argv [ 1 ]; 
std :: string const instance_id = argv [ 2 ]; 
std :: string const table_id = argv [ 3 ]; 
std :: string const app_profile_id = ( argc == 5 ? argv [ 4 ] : "default" ); 

// Create a namespace alias to make the code easier to read. 
namespace cbt = :: google :: cloud :: bigtable ; 

cbt :: Table table ( 
cbt :: MakeDataConnection (), 
cbt :: TableResource ( project_id , instance_id , table_id ), 
google :: cloud :: Options {}. set :: AppProfileIdOption > ( app_profile_id )); 

std :: string row_key = "r1" ; 
std :: string column_family = "cf1" ; 

std :: cout "Getting a single row by row key:" std :: flush ; 
google :: cloud :: StatusOr :: pair , cbt :: Row >> result = 
table . ReadRow ( row_key , cbt :: Filter :: FamilyRegex ( column_family )); 
if ( ! result ) throw std :: move ( result ). status (); 
if ( ! result - > first ) { 
std :: cout "Cannot find row " row_key " in the table: " table_id 
" \n " ; 
return 0 ; 
} 

cbt :: Cell const & cell = result - > second . cells (). front (); 
std :: cout cell . family_name () ":" cell . column_qualifier () " @ " 
cell . timestamp (). count () "us \n " 
'"' cell . value () '"' " \n " ; 

return 0 ; 
} catch ( google :: cloud :: Status const & status ) { 
std :: cerr "google::cloud::Status thrown: " status " \n " ; 
return 1 ; 
} 
```



































### C# 




























```
using System ; 
using [ Google.Cloud.Bigtable.Common.V2 ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.html) ; 
// Imports the Google Cloud client library 
using [ Google.Cloud.Bigtable.V2 ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.html) ; 

namespace GoogleCloudSamples.Bigtable 
{ 
public class QuickStart 
{ 
public static int Main ( string [] args ) 
{ 
// Your Google Cloud Platform project ID 
const string projectId = "YOUR-PROJECT-ID" ; 
// The name of the Cloud Bigtable instance 
const string instanceId = "YOUR-INSTANCE-ID" ; 
// The name of the Cloud Bigtable table 
const string tableId = "my-table" ; 

try 
{ 
// Creates a Bigtable client 
[ BigtableClient ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html) bigtableClient = [ BigtableClient ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html) . [ Create ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_Create) (); 

// Read a row from my-table using a row key 
[ Row ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html) row = bigtableClient . [ ReadRow ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_ReadRow_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_V2_RowFilter_Google_Api_Gax_Grpc_CallSettings_) ( 
new [ TableName ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html) ( projectId , instanceId , tableId ), "r1" , [ RowFilters ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html) . [ CellsPerRowLimit ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html#Google_Cloud_Bigtable_V2_RowFilters_CellsPerRowLimit_System_Int32_) ( 1 )); 
// Print the row key and data (column value, labels, timestamp) 
Console . WriteLine ( $"{" Row key : ",-30}{row.[Key](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Key).ToStringUtf8()}\n" + 
$"{" Column Family : ",-30}{row.[Families](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Name}\n" + 
$"{" Column Qualifyer : ",-30}{row.[Families](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Columns[0].Qualifier.ToStringUtf8()}\n" + 
$"{" Value : ",-30}{row.[Families](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Columns[0].[Cells](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Column.html#Google_Cloud_Bigtable_V2_Column_Cells)[0].[Value](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Value.html).ToStringUtf8()}\n" + 
$"{" Labels : ",-30}{row.[Families](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Columns[0].[Cells](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Column.html#Google_Cloud_Bigtable_V2_Column_Cells)[0].Labels}\n" + 
$"{" Timestamp : ",-30}{row.[Families](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Columns[0].[Cells](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Column.html#Google_Cloud_Bigtable_V2_Column_Cells)[0].TimestampMicros}\n" ); 
} 
catch ( Exception ex ) 
{ 
// Handle error performing the read operation 
Console . WriteLine ( $"Error reading row r1: {ex.Message}" ); 
} 
return 0 ; 
} 
} 
} 
```


































### Go 




























```
// Quickstart is a sample program demonstrating use of the Cloud Bigtable client 
// library to read a row from an existing table. 
package main 

import ( 
"context" 
"flag" 
"log" 

"cloud.google.com/go/bigtable" 
) 

func main () { 
projectID := "my-project-id" // The Google Cloud Platform project ID 
instanceID := "my-instance-id" // The Google Cloud Bigtable instance ID 
tableID := "my-table" // The Google Cloud Bigtable table 

ctx := context . Background () 

// Set up Bigtable data operations client. 
client , err := bigtable . [ NewClient ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient) ( ctx , projectID , instanceID ) 
if err != nil { 
log . Fatalf ( "Could not create data operations client: %v" , err ) 
} 

tbl := client . [ Open ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open) ( tableID ) 

// Read data in a row using a row key 
rowKey := "r1" 
columnFamilyName := "cf1" 

log . Printf ( "Getting a single row by row key:" ) 
row , err := tbl . ReadRow ( ctx , rowKey ) 
if err != nil { 
log . Fatalf ( "Could not read row with key %s: %v" , rowKey , err ) 
} 
log . Printf ( "Row key: %s\n" , rowKey ) 
log . Printf ( "Data: %s\n" , string ( row [ columnFamilyName ][ 0 ]. [ Value ](https://documentation.s3ns.fr/go/docs/reference/cloud.google.com/go/bigtable/latest/apiv2/bigtablepb.html#cloud_google_com_go_bigtable_apiv2_bigtablepb_Value) )) 

if err = client . Close (); err != nil { 
log . Fatalf ( "Could not close data operations client: %v" , err ) 
} 
} 
```



































### Java 




























```
import com.google.api.gax.rpc.[NotFoundException](https://documentation.s3ns.fr/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) ; 
import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) ; 
import com.google.cloud.bigtable.data.v2.[BigtableDataSettings](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html) ; 
import com.google.cloud.bigtable.data.v2.models.[Row](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) ; 
import com.google.cloud.bigtable.data.v2.models.[RowCell](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html) ; 
import com.google.cloud.bigtable.data.v2.models.[TableId](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html) ; 

public class Quickstart { 

public static void main ( String ... args ) { 
String projectId = args [ 0 ] ; // my-gcp-project-id 
String instanceId = args [ 1 ] ; // my-bigtable-instance-id 
String tableId = args [ 2 ] ; // my-bigtable-table-id 

quickstart ( projectId , instanceId , tableId ); 
} 

public static void quickstart ( String projectId , String instanceId , String tableId ) { 
[ BigtableDataSettings ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html) settings = 
[ BigtableDataSettings ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html) . newBuilder (). [ setProjectId ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.Builder.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_Builder_setProjectId_java_lang_String_) ( projectId ). [ setInstanceId ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.Builder.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_Builder_setInstanceId_java_lang_String_) ( instanceId ). build (); 

// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the "close" method on the client to safely clean up any remaining background resources. 
try ( [ BigtableDataClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [ BigtableDataClient ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) . create ( settings )) { 
System . out . println ( "\nReading a single row by row key" ); 
[ Row ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row = dataClient . [ readRow ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRow_com_google_cloud_bigtable_data_v2_models_TargetId_com_google_protobuf_ByteString_) ( [ TableId ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html) . of ( tableId ), "r1" ); 
System . out . println ( "Row: " + row . [ getKey ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getKey__) (). toStringUtf8 ()); 
for ( [ RowCell ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html) cell : row . [ getCells ](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getCells__) ()) { 
System . out . printf ( 
"Family: %s Qualifier: %s Value: %s%n" , 
cell . getFamily (), cell . getQualifier (). toStringUtf8 (), cell . getValue (). toStringUtf8 ()); 
} 
} catch ( [ NotFoundException ](https://documentation.s3ns.fr/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e ) { 
System . err . println ( "Failed to read from a non-existent table: " + e . getMessage ()); 
} catch ( Exception e ) { 
System . out . println ( "Error during quickstart: \n" + e . toString ()); 
} 
} 
} 
```
































### HBase



























```
package com . example . cloud . bigtable . quickstart ; 

import com . google . cloud . bigtable . hbase . BigtableConfiguration ; 

import java . io . IOException ; 
import org . apache . hadoop . hbase . TableName ; 
import org . apache . hadoop . hbase . client . Connection ; 
import org . apache . hadoop . hbase . client . Get ; 
import org . apache . hadoop . hbase . client . Result ; 
import org . apache . hadoop . hbase . client . Table ; 
import org . apache . hadoop . hbase . util . Bytes ; 

/** 
* A quickstart application that shows connecting to a Cloud Bigtable instance 
* using the native HBase API to read a row from a table. 
*/ 
public class Quickstart { 

public static void main ( String ... args ) { 

String projectId = args [ 0 ]; // my-gcp-project-id 
String instanceId = args [ 1 ]; // my-bigtable-instance-id 
String tableId = args [ 2 ]; // my-bigtable-table-id 

// Create a connection to the Cloud Bigtable instance. 
// Use try-with-resources to make sure the connection is closed correctly 
try ( Connection connection = BigtableConfiguration . connect ( projectId , instanceId )) { 

System . out . println ( "--- Connection established with Bigtable Instance ---" ); 
// Create a connection to the table that already exists 
// Use try-with-resources to make sure the connection to the table is closed correctly 
try ( Table table = connection . getTable ( TableName . valueOf ( tableId ))) { 

// Read a row 
String rowKey = "r1" ; 
System . out . printf ( "--- Reading for row-key: %s for provided table: %s ---\n" , 
rowKey , tableId ); 

// Retrieve the result 
Result result = table . get ( new Get ( Bytes . toBytes ( rowKey ))); 

// Convert row data to string 
String rowValue = Bytes . toString ( result . value ()); 

System . out . printf ( "Scanned value for Row r1: %s \n" , rowValue ); 

System . out . println ( " --- Finished reading row --- " ); 

} catch ( IOException e ) { 
// handle exception while connecting to a table 
throw e ; 
} 
} catch ( IOException e ) { 
System . err . println ( "Exception while running quickstart: " + e . getMessage ()); 
e . printStackTrace (); 
} 
} 
} 
```
































### Node.js 




























```
// Imports the Google Cloud client library 
const { Bigtable } = require ( '[@google-cloud/bigtable](https://documentation.s3ns.fr/nodejs/docs/reference/bigtable/latest/overview.html)' ); 

const bigtable = new [ Bigtable ](https://documentation.s3ns.fr/nodejs/docs/reference/bigtable/latest/bigtable/bigtable.html) (); 

async function quickstart () { 
// Connect to an existing instance:my-bigtable-instance 
const instance = bigtable . instance ( INSTANCE_ID ); 

// Connect to an existing table:my-table 
const table = instance . table ( TABLE_ID ); 

// Read a row from my-table using a row key 
const [ singleRow ] = await table . row ( 'r1' ). get (); 

// Print the row key and data (column value, labels, timestamp) 
const rowData = JSON . stringify ( singleRow . data , null , 4 ); 
console . log ( `Row key: ${ singleRow . id } \nData: ${ rowData } ` ); 
} 
quickstart (); 
```


































### PHP 




























```
use Google\Cloud\Bigtable\BigtableClient; 

/** Uncomment and populate these variables in your code */ 
// $projectId = 'The Google project ID'; 
// $instanceId = 'The Bigtable instance ID'; 
// $tableId = 'The Bigtable table ID'; 

// Connect to an existing table with an existing instance. 
$dataClient = new BigtableClient([ 
'projectId' => $projectId, 
]); 
$table = $dataClient->table($instanceId, $tableId); 
$key = 'r1'; 
// Read a row from my-table using a row key 
$row = $table->readRow($key); 

$columnFamilyId = 'cf1'; 
$columnId = 'c1'; 
// Get the Value from the Row, using the column_family_id and column_id 
$value = $row[$columnFamilyId][$columnId][0]['value']; 

printf("Row key: %s\nData: %s\n", $key, $value); 
```



































### Python 







The Python client library for Bigtable offers two APIs, `asyncio`
and a synchronous API. If your application is asynchronous, use `asyncio`.






















```
import argparse 

from google.cloud import [ bigtable ](https://documentation.s3ns.fr/python/docs/reference/bigtable/latest)

def main ( project_id = "project-id" , instance_id = "instance-id" , table_id = "my-table" ): 
# Create a Cloud Bigtable client. 
client = [ bigtable ](https://documentation.s3ns.fr/python/docs/reference/bigtable/latest) . [ Client ](https://documentation.s3ns.fr/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html) ( project = project_id ) 

# Connect to an existing Cloud Bigtable instance. 
instance = [ client ](https://documentation.s3ns.fr/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html) . [ instance ](https://documentation.s3ns.fr/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance) ( instance_id ) 

# Open an existing table. 
table = instance . table ( table_id ) 

row_key = "r1" 
row = table . read_row ( row_key . encode ( "utf-8" )) 

column_family_id = "cf1" 
column_id = "c1" . encode ( "utf-8" ) 
value = row . [ cells ](https://documentation.s3ns.fr/python/docs/reference/bigtable/latest/google.cloud.bigtable.row.PartialRowData.html#google_cloud_bigtable_row_PartialRowData_cells) [ column_family_id ][ column_id ][ 0 ] . value . decode ( "utf-8" ) 

print ( "Row key: {} \n Data: {} " . format ( row_key , value )) 

if __name__ == "__main__" : 
parser = argparse . ArgumentParser ( 
description = __doc__ , formatter_class = argparse . ArgumentDefaultsHelpFormatter 
) 
parser . add_argument ( "project_id" , help = "Your Cloud Platform project ID." ) 
parser . add_argument ( 
"instance_id" , help = "ID of the Cloud Bigtable instance to connect to." 
) 
parser . add_argument ( 
"--table" , help = "Existing table used in the quickstart." , default = "my-table" 
) 

args = parser . parse_args () 
main ( args . project_id , args . instance_id , args . table ) 
```




























### Python asyncio







The Python client library for Bigtable offers two APIs, `asyncio`
and a synchronous API. If your application is asynchronous, use `asyncio`.


























```
import argparse 
import asyncio 

from google.cloud.bigtable.data import BigtableDataClientAsync 

async def main ( project_id = "project-id" , instance_id = "instance-id" , table_id = "my-table" ): 
# Create a Cloud Bigtable client. 
client = BigtableDataClientAsync ( project = project_id ) 

# Open an existing table. 
table = client . get_table ( instance_id , table_id ) 

row_key = "r1" 
row = await table . read_row ( row_key ) 

column_family_id = "cf1" 
column_id = b "c1" 
value = [ row ](https://documentation.s3ns.fr/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row.html) . [ get_cells ](https://documentation.s3ns.fr/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row.Row.html#google_cloud_bigtable_data_row_Row_get_cells) ( column_family_id , column_id )[ 0 ] . value . decode ( "utf-8" ) 

await table . close () 
await client . close () 

print ( "Row key: {} \n Data: {} " . format ( row_key , value )) 

if __name__ == "__main__" : 
parser = argparse . ArgumentParser ( 
description = __doc__ , formatter_class = argparse . ArgumentDefaultsHelpFormatter 
) 
parser . add_argument ( "project_id" , help = "Your Cloud Platform project ID." ) 
parser . add_argument ( 
"instance_id" , help = "ID of the Cloud Bigtable instance to connect to." 
) 
parser . add_argument ( 
"--table" , help = "Existing table used in the quickstart." , default = "my-table" 
) 

args = parser . parse_args () 
asyncio . get_event_loop () . run_until_complete ( 
main ( args . project_id , args . instance_id , args . table ) 
) 
```
































### Ruby 




























```
# Import google bigtable client lib 
require "google/cloud/bigtable" 

# Instantiates a client 
bigtable = Google :: Cloud :: [ Bigtable ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html) . [ new ](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)

# Your Cloud Bigtable instance ID 
# instance_id = "my-instance" 

# Your Cloud Bigtable table ID 
# table_id = "my-table" 

# Get table client 
table = bigtable . table instance_id , table_id 

# Read and print row 
p table . read_row "user0000001" 
```





























## Additional resources














### C++ 






The following list contains links to more resources related to the
client library for C++:

- [API reference](/cpp/docs/reference/bigtable/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues) 

- [`google-cloud-bigtable` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D%5Bc%2B%2B%5D) 

- [Source code](https://github.com/googleapis/google-cloud-cpp) 





























### C# 






The following list contains links to more resources related to the
client library for C#:

- [API reference](/dotnet/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues) 

- [`google-cloud-bigtable` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D+%5Bc%23%5D) 

- [Source code](https://github.com/googleapis/google-cloud-dotnet) 




























### Go 






The following list contains links to more resources related to the
client library for Go:

- [API reference](https://godoc.org/cloud.google.com/go/bigtable) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-go/issues) 

- [`google-cloud-bigtable` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D+%5Bgo%5D) 

- [Source code](https://github.com/googleapis/google-cloud-go) 





























### Java 






The following list contains links to more resources related to the
client library for Java:

- [API reference](https://documentation.s3ns.fr/java/docs/reference/google-cloud-bigtable/latest/overview) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-java/issues) 

- [`google-cloud-bigtable` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D+%5Bjava%5D) 

- [Source code](https://github.com/googleapis/google-cloud-java/tree/main/java-bigtable) 
























### HBase







- [API Reference Documentation
(client library)](/bigtable/docs/hbase-client/javadoc)

- [Source Code](https://github.com/googleapis/java-bigtable-hbase)

- [GitHub Issue Tracker](https://github.com/googleapis/java-bigtable-hbase/issues)

- [Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D+%5Bjava-hbase%5D)




























### Node.js 






The following list contains links to more resources related to the
client library for Node.js:

- [API reference](https://documentation.s3ns.fr/nodejs/docs/reference/bigtable/latest/) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/nodejs-bigtable/issues) 

- [`google-cloud-bigtable` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D+%5Bnode.js%5D) 

- [Source code](https://github.com/googleapis/nodejs-bigtable) 




























### PHP 






The following list contains links to more resources related to the
client library for PHP:

- [API reference](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/bigtable/readme) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-php-bigtable/issues) 

- [`google-cloud-bigtable` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D+%5Bphp%5D) 

- [Source code](https://github.com/googleapis/google-cloud-php-bigtable) 





























### Python 






The following list contains links to more resources related to the
client library for Python:

- [API reference](/python/docs/reference/bigtable/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-python/issues) 

- [`google-cloud-bigtable` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D+%5Bpython%5D) 

- [Source code](https://github.com/googleapis/google-cloud-python) 





























### Ruby 






The following list contains links to more resources related to the
client library for Ruby:

- [API reference](https://documentation.s3ns.fr/ruby/docs/reference/google-cloud-bigtable/latest/) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-ruby#cloud-bigtable-beta/issues) 

- [`google-cloud-bigtable` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-bigtable%5D+%5Bruby%5D) 

- [Source code](https://github.com/googleapis/google-cloud-ruby#cloud-bigtable-beta) 

























## Third-party Cloud Bigtable API client libraries

### Scio

The [Scio client library](https://github.com/spotify/scio) provides a Scala API
for [Dataflow](/dataflow), which can read from and write to
Bigtable. The Scio repository provides [sample
code](https://github.com/spotify/scio/wiki/Bigtable) for a
Dataflow pipeline that uses Bigtable.