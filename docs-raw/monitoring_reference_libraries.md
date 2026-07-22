# Monitoring client libraries

Source: https://berlin.devsitetest.how/monitoring/docs/reference/libraries
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/monitoring/docs/tpc-differences) for more details.














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

Observability

](https://berlin.devsitetest.how/docs/observability)






- 








[

Cloud Monitoring

](https://berlin.devsitetest.how/monitoring/docs)






- 








[

Reference

](https://berlin.devsitetest.how/monitoring/docs/apis)












# Monitoring client libraries 






- On this page 
- [ Install the client library ](#install)
- [ Set up authentication ](#authentication)
- [ Use the client library ](#use)
- [ Additional resources ](#resources)
- 












This page shows how to get started with the Cloud Client Libraries for the
Cloud Monitoring API. Client libraries make it easier to access
Google Cloud Dedicated in Germany APIs from a supported language. Although you can use
Google Cloud Dedicated in Germany APIs directly by making raw requests to the server, client
libraries provide simplifications that significantly reduce the amount of code
you need to write.

Read more about the Cloud Client Libraries
and the older Google API Client Libraries in
[Client libraries explained](/apis/docs/client-libraries-explained).

The samples on this page use custom, or user-defined, metrics to illustrate
the use of the client libraries. The system-defined metrics described in the
[Metrics list](/monitoring/api/metrics) are collected for you. You
don't need to write any code to collect them, although the agent metrics do
require the installation of the Cloud Monitoring agent. For more information
on agent metrics, see the
[Agent metrics list](/monitoring/api/metrics_agent).



## Install the client library















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 










See [Setting up a C++ development environment](/cpp/docs/setup)
for details about this client library's requirements and install dependencies.



































In Visual Studio 2013/2015, open the Package Manager Console and run this command:


```
Install-Package Google.Cloud.Monitoring.V3 -Pre
```





For more information, see [Setting Up a C# Development Environment](/dotnet/docs/setup).


































```
go get cloud.google.com/go/monitoring/apiv3
```





For more information, see [Setting Up a Go Development Environment](/go/docs/setup).




































If you are using [Maven](https://maven.apache.org/) with
a BOM, add the following to your `pom.xml` file:

























```



com.google.cloud 
libraries-bom 
26.32.0 
pom 
import 





com.google.cloud 
google-cloud-monitoring 


```



If you are using [Maven](https://maven.apache.org/)
without a BOM, add this to your dependencies:
























```
dependencyManagement >
dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>libraries - bom / artifactId >
version>26 .83.0 / version >
type>pom / type >
scope>import / scope >
/ dependency >
/ dependencies >
/ dependencyManagement >

dependencies >
dependency >
groupId>com . google . cloud / groupId >
artifactId>google - cloud - monitoring / artifactId >
/ dependency >
/ dependencies >
```



If you are using [Gradle](https://gradle.org/),
add the following to your dependencies:
























```
implementation platform ( ' com . google . cloud : libraries - bom : 26.83.0 ' ) 

implementation ' com . google . cloud : google - cloud - monitoring ' 
```



If you are using [sbt](https://www.scala-sbt.org/), add
the following to your dependencies:
























```
libraryDependencies += "com.google.cloud" % "google-cloud-monitoring" % "3.95.0" 
```



If you're using Visual Studio Code or IntelliJ, you can add client libraries to your
project using the following IDE plugins:


- [Cloud Code for VS Code](/code/docs/vscode/client-libraries)

- [Cloud Code for IntelliJ](/code/docs/intellij/client-libraries)

The plugins provide additional functionality, such as key management for service accounts. Refer
to each plugin's documentation for details.





For more information, see [Setting Up a Java Development Environment](/java/docs/setup).



































```
npm install @google-cloud/monitoring
```





For more information, see [Setting Up a Node.js Development Environment](/nodejs/docs/setup).



































```
composer require google/cloud-monitoring
```






For more information, see [Using PHP on Google Cloud](/php/docs).



































```
pip install --upgrade google-cloud-monitoring
```





For more information, see [Setting Up a Python Development Environment](/python/docs/setup).



































```
gem install google-cloud-monitoring
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











Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
#include "google/cloud/monitoring/v3/alert_policy_client.h" 
#include "google/cloud/project.h" 
#include 

int main ( int argc , char * argv []) try { 
if ( argc != 2 ) { 
std :: cerr "Usage: " argv [ 0 ] " project-id \n " ; 
return 1 ; 
} 

namespace monitoring = :: google :: cloud :: monitoring_v3 ; 
auto client = monitoring :: AlertPolicyServiceClient ( 
monitoring :: MakeAlertPolicyServiceConnection ()); 

auto const project = google :: cloud :: Project ( argv [ 1 ]); 
for ( auto a : client . ListAlertPolicies ( project . FullName ())) { 
if ( ! a ) throw std :: move ( a ). status (); 
std :: cout a - > DebugString () " \n " ; 
} 

return 0 ; 
} catch ( google :: cloud :: Status const & status ) { 
std :: cerr "google::cloud::Status thrown: " status " \n " ; 
return 1 ; 
} 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.

[README.md](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/tree/master/monitoring/api)
for instructions on using Visual Studio to build and run this sample C# code.






















```
using System ; 
using System.Collections.Generic ; 
using [ Google.Cloud.Monitoring.V3 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.html) ; 
using [ Google.Protobuf.WellKnownTypes ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html) ; 
using [ Google.Api ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.html) ; 
using [ Google.Api.Gax.ResourceNames ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html) ; 

namespace GoogleCloudSamples 
{ 
public class QuickStart 
{ 
public static void Main ( string [] args ) 
{ 
// Your Google Cloud Platform project ID. 
string projectId = "YOUR-PROJECT-ID" ; 

// Create client. 
[ MetricServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient.html) metricServiceClient = [ MetricServiceClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient.html#Google_Cloud_Monitoring_V3_MetricServiceClient_Create) (); 

// Initialize request argument(s). 
[ ProjectName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) name = new [ ProjectName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) ( projectId ); 

// Prepare a data point. 
[ TypedValue ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TypedValue.html) salesTotal = new [ TypedValue ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TypedValue.html)
{ 
DoubleValue = 123.45 
}; 
[ Point ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.Point.html) dataPoint = new [ Point ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.Point.html)
{ 
Value = salesTotal 
}; 
// Sets data point's interval end time to current time. 
DateTime UnixEpoch = new DateTime ( 1970 , 1 , 1 , 0 , 0 , 0 , DateTimeKind . Utc ); 
[ Timestamp ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html) timeStamp = new [ Timestamp ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)
{ 
Seconds = ( long )( DateTime . UtcNow - UnixEpoch ). TotalSeconds 
}; 
[ TimeInterval ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeInterval.html) interval = new [ TimeInterval ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeInterval.html)
{ 
EndTime = timeStamp 
}; 
dataPoint . [ Interval ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.Point.html#Google_Cloud_Monitoring_V3_Point_Interval) = interval ; 

// Prepare custom metric. 
[ Metric ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Metric.html) metric = new [ Metric ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Metric.html)
{ 
Type = "custom.googleapis.com/my_metric" 
}; 
metric . [ Labels ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Metric.html#Google_Api_Metric_Labels) . [ Add ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_) ( "store_id" , "Pittsburgh" ); 

// Prepare monitored resource. 
[ MonitoredResource ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html) resource = new [ MonitoredResource ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html)
{ 
Type = "gce_instance" 
}; 

resource . [ Labels ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html#Google_Api_MonitoredResource_Labels) . [ Add ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_) ( "project_id" , projectId ); 
resource . [ Labels ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html#Google_Api_MonitoredResource_Labels) . [ Add ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_) ( "instance_id" , "1234567890123456789" ); 
resource . [ Labels ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html#Google_Api_MonitoredResource_Labels) . [ Add ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_) ( "zone" , "us-central1-f" ); 

// Create a new time series using inputs. 
[ TimeSeries ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeries.html) timeSeriesData = new [ TimeSeries ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeries.html)
{ 
Metric = metric , 
Resource = resource 
}; 
timeSeriesData . [ Points ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeries.html#Google_Cloud_Monitoring_V3_TimeSeries_Points) . [ Add ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_) ( dataPoint ); 

// Add newly created time series to list of time series to be written. 
IEnumerable timeSeries = new List { timeSeriesData }; 
// Write time series data. 
metricServiceClient . [ CreateTimeSeries ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient.html#Google_Cloud_Monitoring_V3_MetricServiceClient_CreateTimeSeries_Google_Api_Gax_ResourceNames_ProjectName_System_Collections_Generic_IEnumerable_Google_Cloud_Monitoring_V3_TimeSeries__Google_Api_Gax_Grpc_CallSettings_) ( name , timeSeries ); 
Console . WriteLine ( "Done writing time series data." ); 
} 
} 
} 
```








































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
// Sample monitoring-quickstart writes a data point to Stackdriver Monitoring. 
package main 

import ( 
"context" 
"fmt" 
"log" 
"time" 

monitoring "cloud.google.com/go/monitoring/apiv3/v2" 
"cloud.google.com/go/monitoring/apiv3/v2/monitoringpb" 
googlepb "github.com/golang/protobuf/ptypes/timestamp" 
metricpb "google.golang.org/genproto/googleapis/api/metric" 
monitoredrespb "google.golang.org/genproto/googleapis/api/monitoredres" 
) 

func main () { 
ctx := context . Background () 

// Creates a client. 
client , err := monitoring . [ NewMetricClient ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/monitoring/latest/apiv3/v2.html#cloud_google_com_go_monitoring_apiv3_v2_MetricClient_NewMetricClient) ( ctx ) 
if err != nil { 
log . Fatalf ( "Failed to create client: %v" , err ) 
} 

// Sets your Google Cloud Platform project ID. 
projectID := "YOUR_PROJECT_ID" 

// Prepares an individual data point 
dataPoint := & monitoringpb . Point { 
Interval : & monitoringpb . TimeInterval { 
EndTime : & googlepb . Timestamp { 
Seconds : time . Now (). Unix (), 
}, 
}, 
Value : & monitoringpb . TypedValue { 
Value : & monitoringpb . TypedValue_DoubleValue { 
DoubleValue : 123.45 , 
}, 
}, 
} 

// Writes time series data. 
if err := client . CreateTimeSeries ( ctx , & monitoringpb . CreateTimeSeriesRequest { 
Name : fmt . Sprintf ( "projects/%s" , projectID ), 
TimeSeries : [] * monitoringpb . TimeSeries { 
{ 
Metric : & metricpb . Metric { 
Type : "custom.googleapis.com/stores/daily_sales" , 
Labels : map [ string ] string { 
"store_id" : "Pittsburg" , 
}, 
}, 
Resource : & monitoredrespb . MonitoredResource { 
Type : "global" , 
Labels : map [ string ] string { 
"project_id" : projectID , 
}, 
}, 
Points : [] * monitoringpb . Point { 
dataPoint , 
}, 
}, 
}, 
}); err != nil { 
log . Fatalf ( "Failed to write time series data: %v" , err ) 
} 

// Closes the client and flushes the data to Stackdriver. 
if err := client . Close (); err != nil { 
log . Fatalf ( "Failed to close client: %v" , err ) 
} 

fmt . Printf ( "Done writing time series data.\n" ) 
} 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
import com.google.api.[Metric](https://berlin.devsitetest.how/java/docs/reference/proto-google-common-protos/latest/com.google.api.Metric.html) ; 
import com.google.api.[MonitoredResource](https://berlin.devsitetest.how/java/docs/reference/proto-google-common-protos/latest/com.google.api.MonitoredResource.html) ; 
import com.google.cloud.monitoring.v3.[MetricServiceClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.MetricServiceClient.html) ; 
import com.google.monitoring.v3.[CreateTimeSeriesRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateTimeSeriesRequest.html) ; 
import com.google.monitoring.v3.[Point](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.Point.html) ; 
import com.google.monitoring.v3.[ProjectName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html) ; 
import com.google.monitoring.v3.[TimeInterval](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeInterval.html) ; 
import com.google.monitoring.v3.[TimeSeries](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.html) ; 
import com.google.monitoring.v3.[TypedValue](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TypedValue.html) ; 
import com.google.protobuf.util.[Timestamps](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.util.Timestamps.html) ; 
import java.io.IOException ; 
import java.util.ArrayList ; 
import java.util.HashMap ; 
import java.util.List ; 
import java.util.Map ; 

public class QuickstartSample { 

public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
quickstart ( projectId ); 
} 

public static void quickstart ( String projectId ) throws IOException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ MetricServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.MetricServiceClient.html) metricServiceClient = [ MetricServiceClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.MetricServiceClient.html) . create ()) { 

// Prepares an individual data point 
[ TimeInterval ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeInterval.html) interval = 
[ TimeInterval ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeInterval.html) . newBuilder () 
. setEndTime ( [ Timestamps ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.util.Timestamps.html) . fromMillis ( System . currentTimeMillis ())) 
. build (); 
[ TypedValue ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TypedValue.html) value = [ TypedValue ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TypedValue.html) . newBuilder (). setDoubleValue ( 123.45 ). build (); 
[ Point ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.Point.html) point = [ Point ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.Point.html) . newBuilder (). setInterval ( interval ). setValue ( value ). build (); 

List pointList = new ArrayList <> (); 
pointList . add ( point ); 

[ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html) name = [ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html) . of ( projectId ); 

// Prepares the metric descriptor 
Map , String > metricLabels = new HashMap <> (); 
metricLabels . put ( "store_id" , "Pittsburg" ); 
[ Metric ](https://berlin.devsitetest.how/java/docs/reference/proto-google-common-protos/latest/com.google.api.Metric.html) metric = 
[ Metric ](https://berlin.devsitetest.how/java/docs/reference/proto-google-common-protos/latest/com.google.api.Metric.html) . newBuilder () 
. setType ( "custom.googleapis.com/stores/daily_sales" ) 
. putAllLabels ( metricLabels ) 
. build (); 

// Prepares the monitored resource descriptor 
Map , String > resourceLabels = new HashMap <> (); 
resourceLabels . put ( "project_id" , projectId ); 
[ MonitoredResource ](https://berlin.devsitetest.how/java/docs/reference/proto-google-common-protos/latest/com.google.api.MonitoredResource.html) resource = 
[ MonitoredResource ](https://berlin.devsitetest.how/java/docs/reference/proto-google-common-protos/latest/com.google.api.MonitoredResource.html) . newBuilder (). setType ( "global" ). putAllLabels ( resourceLabels ). build (); 

// Prepares the time series request 
[ TimeSeries ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.html) timeSeries = 
[ TimeSeries ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.html) . newBuilder () 
. setMetric ( metric ) 
. [ setResource ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.Builder.html#com_google_monitoring_v3_TimeSeries_Builder_setResource_com_google_api_MonitoredResource_) ( resource ) 
. [ addAllPoints ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.Builder.html#com_google_monitoring_v3_TimeSeries_Builder_addAllPoints_java_lang_Iterable___extends_com_google_monitoring_v3_Point__) ( pointList ) 
. build (); 
List timeSeriesList = new ArrayList <> (); 
timeSeriesList . add ( timeSeries ); 

[ CreateTimeSeriesRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateTimeSeriesRequest.html) request = 
[ CreateTimeSeriesRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateTimeSeriesRequest.html) . newBuilder () 
. setName ( name . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html#com_google_monitoring_v3_ProjectName_toString__) ()) 
. addAllTimeSeries ( timeSeriesList ) 
. build (); 

// Writes time series data 
metricServiceClient . createTimeSeries ( request ); 

System . out . printf ( "Done writing time series data.%n" ); 
} 
} 
} 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
// Imports the Google Cloud client library 
const monitoring = require ( '[@google-cloud/monitoring](https://berlin.devsitetest.how/nodejs/docs/reference/monitoring/latest/overview.html)' ); 

async function quickstart () { 
// Creates a client 
const client = new monitoring . [ MetricServiceClient ](https://berlin.devsitetest.how/nodejs/docs/reference/monitoring/latest/overview.html) (); 

// TODO(developer): Uncomment and set the following variables 
// const projectId = "PROJECT_ID" 

// Prepares an individual data point 
const dataPoint = { 
interval : { 
endTime : { 
seconds : Date . now () / 1000 , 
}, 
}, 
value : { 
// The amount of sales 
doubleValue : 123.45 , 
}, 
}; 

// Prepares the time series request 
const request = { 
name : client . projectPath ( projectId ), 
timeSeries : [ 
{ 
// Ties the data point to a custom metric 
metric : { 
type : 'custom.googleapis.com/stores/daily_sales' , 
labels : { 
store_id : 'Pittsburgh' , 
}, 
}, 
resource : { 
type : 'global' , 
labels : { 
project_id : projectId , 
}, 
}, 
points : [ dataPoint ], 
}, 
], 
}; 

// Writes time series data 
const [ result ] = await client . createTimeSeries ( request ); 
console . log ( 'Done writing time series data.' , result ); 
} 
quickstart (); 
```








































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
# Includes the autoloader for libraries installed with composer 
require_once __DIR__ . '/vendor/autoload.php'; 

# Imports the Google Cloud client library 
use Google\Api\Metric; 
use Google\Api\MonitoredResource; 
use Google\Cloud\Monitoring\V3\Client\MetricServiceClient; 
use Google\Cloud\Monitoring\V3\CreateTimeSeriesRequest; 
use Google\Cloud\Monitoring\V3\Point; 
use Google\Cloud\Monitoring\V3\TimeInterval; 
use Google\Cloud\Monitoring\V3\TimeSeries; 
use Google\Cloud\Monitoring\V3\TypedValue; 
use Google\Protobuf\Timestamp; 

// These variables are set by the App Engine environment. To test locally, 
// ensure these are set or manually change their values. 
$projectId = getenv('GCLOUD_PROJECT') ?: 'YOUR_PROJECT_ID'; 
$instanceId = '1234567890123456789'; 
$zone = 'us-central1-f'; 

try { 
$client = new MetricServiceClient(); 
$formattedProjectName = 'projects/' . $projectId; 
$labels = [ 
'instance_id' => $instanceId, 
'zone' => $zone, 
]; 

$m = new Metric(); 
$m->setType('custom.googleapis.com/my_metric'); 

$r = new MonitoredResource(); 
$r->setType('gce_instance'); 
$r->setLabels($labels); 

$value = new TypedValue(); 
$value->setDoubleValue(3.14); 

$timestamp = new Timestamp(); 
$timestamp->setSeconds(time()); 

$interval = new TimeInterval(); 
$interval->setStartTime($timestamp); 
$interval->setEndTime($timestamp); 

$point = new Point(); 
$point->setValue($value); 
$point->setInterval($interval); 
$points = [$point]; 

$timeSeries = new TimeSeries(); 
$timeSeries->setMetric($m); 
$timeSeries->setResource($r); 
$timeSeries->setPoints($points); 
$createTimeSeriesRequest = (new CreateTimeSeriesRequest()) 
->setName($formattedProjectName) 
->setTimeSeries([$timeSeries]); 

$client->createTimeSeries($createTimeSeriesRequest); 
print('Successfully submitted a time series' . PHP_EOL); 
} finally { 
$client->close(); 
} 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
from google.cloud import [ monitoring_v3 ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest)

import time 

client = [ monitoring_v3 ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest) . [ MetricServiceClient ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html) () 
# project_id = 'my-project' # TODO: Update to your project ID. 
project_name = f "projects/ { project_id } " 

series = [ monitoring_v3 ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest) . [ TimeSeries ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeSeries.html) () 
series . metric . type = "custom.googleapis.com/my_metric" 
series . metric . labels [ "store_id" ] = "Pittsburgh" 
series . resource . type = "gce_instance" 
series . resource . labels [ "instance_id" ] = "1234567890123456789" 
series . resource . labels [ "zone" ] = "us-central1-f" 
now = time . time () 
seconds = int ( now ) 
nanos = int (( now - seconds ) * 10 ** 9 ) 
interval = [ monitoring_v3 ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest) . [ TimeInterval ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeInterval.html) ( 
{ "end_time" : { "seconds" : seconds , "nanos" : nanos }} 
) 
point = [ monitoring_v3 ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest) . [ Point ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Point.html) ({ "interval" : interval , "value" : { "double_value" : 3.14 }}) 
series . points = [ point ] 
client . [ create_time_series ](https://berlin.devsitetest.how/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_time_series) ( request = { "name" : project_name , "time_series" : [ series ]}) 
print ( "Successfully wrote time series." ) 
return True 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
gem "google-cloud-monitoring" 
require "google/cloud/monitoring" 

# Your Google Cloud Platform project ID 
# project_id = "YOUR_PROJECT_ID" 

# Example metric label 
# metric_label = "my-value" 

# Instantiates a client 
metric_service_client = Google :: Cloud :: [ Monitoring ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-metrics_scope-v1/latest/Google-Cloud-Monitoring.html) . [ metric_service ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
project_path = metric_service_client . project_path project : project_id 

series = Google :: Cloud :: [ Monitoring ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-metrics_scope-v1/latest/Google-Cloud-Monitoring.html) :: [ V3 ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html) :: TimeSeries . new 
series . [ metric ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) = Google :: Api :: [ Metric ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Metric.html) . new type : "custom.googleapis.com/my_metric" , 
labels : { "my_key" = > metric_label } 

resource = Google :: Api :: [ MonitoredResource ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Api-MonitoredResource.html) . new type : "gce_instance" 
resource . labels [ "project_id" ] = project_id 
resource . labels [ "instance_id" ] = "1234567890123456789" 
resource . labels [ "zone" ] = "us-central1-f" 
series . [ resource ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) = resource 

point = Google :: Cloud :: [ Monitoring ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-metrics_scope-v1/latest/Google-Cloud-Monitoring.html) :: [ V3 ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html) :: Point . new 
point . value = Google :: Cloud :: [ Monitoring ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-metrics_scope-v1/latest/Google-Cloud-Monitoring.html) :: [ V3 ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html) :: TypedValue . new double_value : 3 . 14 
now = Time . now 
end_time = Google :: Protobuf :: [ Timestamp ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-parallelstore-v1/latest/Google-Protobuf-Timestamp.html) . new seconds : now . to_i , nanos : now . nsec 
point . interval = Google :: Cloud :: [ Monitoring ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-metrics_scope-v1/latest/Google-Cloud-Monitoring.html) :: [ V3 ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html) :: TimeInterval . new end_time : end_time 
series . [ points ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) point 

metric_service_client . create_time_series name : project_path , time_series : [ series ] 

puts "Successfully wrote time series." 
```



























## Additional resources















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 










The following list contains links to more resources related to the
client library for C++:

- [API reference](/cpp/docs/reference/monitoring/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues) 

- [`google-cloud-monitoring` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-monitoring%5D%5Bc%2B%2B%5D) 

- [Source code](https://github.com/googleapis/google-cloud-cpp) 


































The following list contains links to more resources related to the
client library for C#:

- [API reference](/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues) 

- [`google-cloud-monitoring` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-monitoring%5D+%5Bc%23%5D) 

- [Source code](https://github.com/googleapis/google-cloud-dotnet) 

































The following list contains links to more resources related to the
client library for Go:

- [API reference](https://godoc.org/cloud.google.com/go/monitoring/apiv3) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-go/issues) 

- [`google-cloud-monitoring` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-monitoring%5D+%5Bgo%5D) 

- [Source code](https://github.com/googleapis/google-cloud-go) 



































The following list contains links to more resources related to the
client library for Java:

- [API reference](/java/docs/reference/google-cloud-monitoring/latest/overview) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-java/issues) 

- [`google-cloud-monitoring` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-monitoring%5D+%5Bjava%5D) 

- [Source code](https://github.com/googleapis/google-cloud-java) 



































- [API Reference Documentation](https://googleapis.dev/nodejs/monitoring/latest/) 

- [Source Code](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-monitoring) 

- [GitHub Issue Tracker](https://github.com/googleapis/google-cloud-node/issues) 

- [Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-monitoring%5D+%5Bnode.js%5D) 

































The following list contains links to more resources related to the
client library for PHP:

- [API reference](https://googleapis.github.io/google-cloud-php/#/docs/latest/monitoring/v3/readme) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-php/issues) 

- [`google-cloud-monitoring` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-monitoring%5D+%5Bphp%5D) 

- [Source code](https://github.com/googleapis/google-cloud-php) 



































The following list contains links to more resources related to the
client library for Python:

- [API reference](/python/docs/reference/monitoring/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-python/issues) 

- [`google-cloud-monitoring` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-monitoring%5D+%5Bpython%5D) 

- [Source code](https://github.com/googleapis/google-cloud-python) 



































The following list contains links to more resources related to the
client library for Ruby:

- [API reference](https://github.com/googleapis/google-cloud-ruby/tree/main/google-cloud-monitoring-v3) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues) 

- [`google-cloud-monitoring` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-monitoring%5D+%5Bruby%5D) 

- [Source code](https://github.com/googleapis/google-cloud-ruby)