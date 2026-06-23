# Logging client libraries

Source: https://berlin.devsitetest.how/logging/docs/reference/libraries
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/logging/docs/tpc-differences) for more details.














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

Cloud Logging

](https://berlin.devsitetest.how/logging/docs)






- 








[

Reference

](https://berlin.devsitetest.how/logging/docs/apis)












# Logging client libraries 






- On this page 
- [ Install the client library ](#install)
- [ Set up authentication ](#authentication)
- [ Use the client library ](#use)
- [ Code samples ](#writ-logs-neos)
- [ Additional resources ](#resources)
- [ Additional client libraries ](#more-libraries)
- 












This page shows how to get started with the Cloud Client Libraries for the
Cloud Logging API. Client libraries make it easier to access
Google Cloud Dedicated in Germany APIs from a supported language. Although you can use
Google Cloud Dedicated in Germany APIs directly by making raw requests to the server, client
libraries provide simplifications that significantly reduce the amount of code
you need to write.

Read more about the Cloud Client Libraries
and the older Google API Client Libraries in
[Client libraries explained](/apis/docs/client-libraries-explained).

Cloud Logging client libraries are idiomatic interfaces around the API.
Client libraries provide an integration option with Logging.
You can use client libraries in addition to using an agent.
Some Google Cloud Dedicated in Germany services, such as Google Kubernetes Engine,
contain an integrated logging agent that sends the data written
to `stdout` or `stderr` as logs to Cloud Logging.

To learn more about setting up
Logging using a language runtime, see
[Setting up Language Runtimes](/logging/docs/setup).

Incoming log entries with timestamps that are more than the
[logs retention period](/logging/quotas#logs_retention_periods) in the past or that
are more than 24 hours in the future are discarded.



## Install the client library















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 










See [Setting up a C++ development environment](/cpp/docs/setup)
for details about this client library's requirements and install dependencies.


































```
dotnet add package Google.Cloud.Logging.V2
```





For more information, see [Setting Up a C# Development Environment](/dotnet/docs/setup).


































```
go get cloud.google.com/go/logging
```





For more information, see [Setting Up a Go Development Environment](/go/docs/setup).




































If you are using [Maven](https://maven.apache.org/) with
a BOM, add the following to your `pom.xml` file:

























```



com.google.cloud 
libraries-bom 
26.55.0 
pom 
import 






com.google.cloud 
google-cloud-logging 


...

```



If you are using [Maven](https://maven.apache.org/)
without a BOM, add this to your dependencies:

























```

com.google.cloud 
google-cloud-logging 
3.21.3 

```



If you are using [Gradle](https://gradle.org/),
add the following to your dependencies:
























```
implementation platform ( ' com . google . cloud : libraries - bom : 26.74.0 ' ) 

implementation ' com . google . cloud : google - cloud - logging ' 
```



If you are using [sbt](https://www.scala-sbt.org/), add
the following to your dependencies:
























```
libraryDependencies += "com.google.cloud" % "google-cloud-logging" % "3.24.0" 
```



If you're using Visual Studio Code or IntelliJ, you can add client libraries to your
project using the following IDE plugins:


- [Cloud Code for VS Code](/code/docs/vscode/client-libraries)

- [Cloud Code for IntelliJ](/code/docs/intellij/client-libraries)

The plugins provide additional functionality, such as key management for service accounts. Refer
to each plugin's documentation for details.





For more information, see [Setting Up a Java Development Environment](/java/docs/setup).



































```
npm install @google-cloud/logging
```





For more information, see [Setting Up a Node.js Development Environment](/nodejs/docs/setup).


































```
composer require google/cloud-logging
```





For more information, see [Using PHP on Google Cloud](/php/docs).



































```
pip install --upgrade google-cloud-logging
```

Install the `google-cloud-logging` library, not an explicitly versioned library.




For more information, see [Setting Up a Python Development Environment](/python/docs/setup).



































```
gem install google-cloud-logging
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
#include "google/cloud/logging/v2/logging_service_v2_client.h" 
#include "google/cloud/project.h" 
#include 

int main ( int argc , char * argv []) try { 
if ( argc != 2 ) { 
std :: cerr "Usage: " argv [ 0 ] " project-id \n " ; 
return 1 ; 
} 

namespace logging = :: google :: cloud :: logging_v2 ; 
auto client = logging :: LoggingServiceV2Client ( 
logging :: MakeLoggingServiceV2Connection ()); 
auto const project = google :: cloud :: Project ( argv [ 1 ]); 
for ( auto l : client . ListLogs ( project . FullName ())) { 
if ( ! l ) throw std :: move ( l ). status (); 
std :: cout * l " \n " ; 
} 

return 0 ; 
} catch ( google :: cloud :: Status const & status ) { 
std :: cerr "google::cloud::Status thrown: " status " \n " ; 
return 1 ; 
} 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
using System ; 
// Imports the Google Cloud Logging client library 
using [ Google.Cloud.Logging.V2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.html) ; 
using [ Google.Cloud.Logging.Type ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.Type/latest/Google.Cloud.Logging.Type.html) ; 
using System.Collections.Generic ; 
using [ Google.Api ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.html) ; 

namespace GoogleCloudSamples 
{ 
public class QuickStart 
{ 
public static void Main ( string [] args ) 
{ 
// Your Google Cloud Platform project ID. 
string projectId = "YOUR-PROJECT-ID" ; 

// Instantiates a client. 
var client = [ LoggingServiceV2Client ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LoggingServiceV2Client.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LoggingServiceV2Client.html#Google_Cloud_Logging_V2_LoggingServiceV2Client_Create) (); 

// Prepare new log entry. 
[ LogEntry ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html) logEntry = new [ LogEntry ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html) (); 
string logId = "my-log" ; 
[ LogName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogName.html) logName = new [ LogName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogName.html) ( projectId , logId ); 
logEntry . [ LogNameAsLogName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html#Google_Cloud_Logging_V2_LogEntry_LogNameAsLogName) = logName ; 
logEntry . [ Severity ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html#Google_Cloud_Logging_V2_LogEntry_Severity) = [ LogSeverity ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.Type/latest/Google.Cloud.Logging.Type.LogSeverity.html) . [ Info ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.Type/latest/Google.Cloud.Logging.Type.LogSeverity.html#Google_Cloud_Logging_Type_LogSeverity_Info) ; 

// Create log entry message. 
string message = "Hello World!" ; 
string messageId = DateTime . Now . Millisecond . ToString (); 
Type myType = typeof ( QuickStart ); 
string entrySeverity = logEntry . [ Severity ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html#Google_Cloud_Logging_V2_LogEntry_Severity) . ToString (). ToUpper (); 
logEntry . [ TextPayload ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html#Google_Cloud_Logging_V2_LogEntry_TextPayload) = 
$"{messageId} {entrySeverity} {myType.Namespace}.LoggingSample - {message}" ; 

// Set the resource type to control which GCP resource the log entry belongs to. 
// See the list of resource types at: 
// https://cloud.google.com/logging/docs/api/v2/resource-list 
// This sample uses resource type 'global' causing log entries to appear in the 
// "Global" resource list of the Developers Console Logs Viewer: 
// https://console.cloud.google.com/logs/viewer 
[ MonitoredResource ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html) resource = new [ MonitoredResource ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html)
{ 
Type = "global" 
}; 

// Create dictionary object to add custom labels to the log entry. 
IDictionary , string > entryLabels = new Dictionary , string > (); 
entryLabels . [ Add ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_) ( "size" , "large" ); 
entryLabels . [ Add ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_) ( "color" , "red" ); 

// Add log entry to collection for writing. Multiple log entries can be added. 
IEnumerable logEntries = new [ LogEntry ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html) [] { logEntry }; 

// Write new log entry. 
client . WriteLogEntries ( logName , resource , entryLabels , logEntries ); 

Console . WriteLine ( "Log Entry created." ); 
} 
} 
} 
```








































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
// Sample logging-quickstart writes a log entry to Cloud Logging. 
package main 

import ( 
"context" 
"fmt" 
"log" 

"cloud.google.com/go/logging" 
) 

func main () { 
ctx := context . Background () 

// Sets your Google Cloud Platform project ID. 
projectID := "YOUR_PROJECT_ID" 

// Creates a client. 
client , err := logging . NewClient ( ctx , projectID ) 
if err != nil { 
log . Fatalf ( "Failed to create client: %v" , err ) 
} 

// Sets the name of the log to write to. 
logName := "my-log" 

// Selects the log to write to. 
logger := client . Logger ( logName ) 

// Sets the data to log. 
text := "Hello, world!" 

// Adds an entry to the log buffer. 
logger . [ Log ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Logger_Log) ( logging . [ Entry ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry) { Payload : text }) 

// Closes the client and flushes the buffer to the Cloud Logging 
// service. 
if err := client . Close (); err != nil { 
log . Fatalf ( "Failed to close client: %v" , err ) 
} 

fmt . Printf ( "Logged: %v\n" , text ) 
} 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
import com.google.cloud.[MonitoredResource](https://berlin.devsitetest.how/java/docs/reference/google-cloud-core/latest/com.google.cloud.MonitoredResource.html) ; 
import com.google.cloud.logging.[LogEntry](https://berlin.devsitetest.how/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) ; 
import com.google.cloud.logging.[Logging](https://berlin.devsitetest.how/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) ; 
import com.google.cloud.logging.[LoggingOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html) ; 
import com.google.cloud.logging.[Payload](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apigee-connect/latest/com.google.cloud.apigeeconnect.v1.Payload.html).StringPayload ; 
import com.google.cloud.logging.[Severity](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Severity.html) ; 
import java.util.Collections ; 

/** 
* This sample demonstrates writing logs using the Cloud Logging API. The library also offers a 
* java.util.logging Handler `com.google.cloud.logging.LoggingHandler` Logback integration is also 
* available : 
* https://github.com/googleapis/google-cloud-java/tree/master/google-cloud-clients/google-cloud-contrib/google-cloud-logging-logback 
* Using the java.util.logging handler / Logback appender should be preferred to using the API 
* directly. 
*/ 
public class QuickstartSample { 

/** Expects a new or existing Cloud log name as the first argument. */ 
public static void main ( [ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) ... args ) throws Exception { 
// The name of the log to write to 
[ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) logName = args [ 0 ] ; // "my-log"; 
[ String ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) textPayload = "Hello, world!" ; 

// Instantiates a client 
try ( [ Logging ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = [ LoggingOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html) . getDefaultInstance (). getService ()) { 

[ LogEntry ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) entry = 
[ LogEntry ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) . newBuilder ( StringPayload . of ( textPayload )) 
. setSeverity ( [ Severity ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Severity.html) . ERROR ) 
. setLogName ( logName ) 
. setResource ( [ MonitoredResource ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-core/latest/com.google.cloud.MonitoredResource.html) . newBuilder ( "global" ). build ()) 
. build (); 

// Writes the log entry asynchronously 
logging . write ( Collections . singleton ( entry )); 

// Optional - flush any pending log entries just before Logging is closed 
logging . flush (); 
} 
System . out . printf ( "Logged: %s%n" , textPayload ); 
} 
} 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
// Imports the Google Cloud client library 
const { Logging } = require ( '[@google-cloud/logging](https://berlin.devsitetest.how/nodejs/docs/reference/logging/latest/overview.html)' ); 

async function quickstart ( 
projectId = 'YOUR_PROJECT_ID' , // Your Google Cloud Platform project ID 
logName = 'my-log' // The name of the log to write to 
) { 
// Creates a client 
const logging = new [ Logging ](https://berlin.devsitetest.how/nodejs/docs/reference/logging/latest/logging/logging.html) ({ projectId }); 

// Selects the log to write to 
const log = logging . log ( logName ); 

// The data to write to the log 
const text = 'Hello, world!' ; 

// The metadata associated with the entry 
const metadata = { 
resource : { type : 'global' }, 
// See: https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity 
severity : '[INFO](https://berlin.devsitetest.how/nodejs/docs/reference/logging/latest/logging/protos.google.logging.type.logseverity.html)' , 
}; 

// Prepares a log entry 
const entry = log . entry ( metadata , text ); 

async function writeLog () { 
// Writes the log entry 
await log . write ( entry ); 
console . log ( `Logged: ${ text } ` ); 
} 
writeLog (); 
} 
```








































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
# Includes the autoloader for libraries installed with composer 
require __DIR__ . '/vendor/autoload.php'; 

# Imports the Google Cloud client library 
use Google\Cloud\Logging\LoggingClient; 

# Your Google Cloud Platform project ID 
$projectId = 'YOUR_PROJECT_ID'; 

# Instantiates a client 
$logging = new LoggingClient([ 
'projectId' => $projectId 
]); 

# The name of the log to write to 
$logName = 'my-log'; 

# Selects the log to write to 
$logger = $logging->logger($logName); 

# The data to log 
$text = 'Hello, world!'; 

# Creates the log entry 
$entry = $logger->entry($text); 

# Writes the log entry 
$logger->write($entry); 

echo 'Logged ' . $text; 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
# Imports the Google Cloud client library 
from google.cloud import logging 

# Instantiates a client 
logging_client = logging . [ Client ](https://berlin.devsitetest.how/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html) () 

# The name of the log to write to 
log_name = "my-log" 
# Selects the log to write to 
logger = logging_client . [ logger ](https://berlin.devsitetest.how/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html#google_cloud_logging_v2_client_Client_logger) ( log_name ) 

# The data to log 
text = "Hello, world!" 

# Writes the log entry 
logger . log_text ( text ) 

print ( "Logged: {} " . format ( text )) 
```









































Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
# Imports the Google Cloud client library 
require "google/cloud/logging" 

# Instantiates a client 
logging = Google :: Cloud :: [ Logging ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-Logging.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html)

# Prepares a log entry 
entry = logging . [ entry ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Project.html)
# payload = "The data you want to log" 
entry . [ payload ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry.html) = payload 
# log_name = "The name of the log to write to" 
entry . log_name = log_name 
# The resource associated with the data 
entry . resource . type = "global" 

# Writes the log entry 
logging . write_entries entry 

puts "Logged #{ entry . [ payload ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry.html) } " 
```

























## Code samples

For all code samples, see [All logging samples](/logging/docs/samples).



## Additional resources















[ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 










The following list contains links to more resources related to the
client library for C++:

- [API reference](/cpp/docs/reference/logging/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues) 

- [`google-cloud-logging` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-logging%5D%5Bc%2B%2B%5D) 

- [Source code](https://github.com/googleapis/google-cloud-cpp) 


































The following list contains links to more resources related to the
client library for C#:

- [API reference](/dotnet/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues) 

- [`google-cloud-logging` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-logging%5D+%5Bc%23%5D) 

- [Source code](https://github.com/googleapis/google-cloud-dotnet) 

































The following list contains links to more resources related to the
client library for Go:

- [API reference](https://godoc.org/cloud.google.com/go/logging) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-go/issues) 

- [`google-cloud-logging` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-logging%5D+%5Bgo%5D) 

- [Source code](https://github.com/googleapis/google-cloud-go) 



































The following list contains links to more resources related to the
client library for Java:

- [API reference](/java/docs/reference) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-java/issues) 

- [`google-cloud-logging` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-logging%5D+%5Bjava%5D) 

- [Source code](https://github.com/googleapis/google-cloud-java) 



































The following list contains links to more resources related to the
client library for Node.js:

- [API reference](/nodejs/docs/reference/logging/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/nodejs-logging/issues) 

- [`google-cloud-logging` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-logging%5D+%5Bnode.js%5D) 

- [Source code](https://github.com/googleapis/nodejs-logging) 


































The following list contains links to more resources related to the
client library for PHP:

- [API reference](https://googleapis.github.io/google-cloud-php/#/docs/latest/logging/loggingclient) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-php/issues) 

- [`google-cloud-logging` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-logging%5D+%5Bphp%5D) 

- [Source code](https://github.com/googleapis/google-cloud-php) 



































The following list contains links to more resources related to the
client library for Python:

- [API reference](/python/docs/reference/logging/latest) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-python/issues) 

- [`google-cloud-logging` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-logging%5D+%5Bpython%5D) 

- [Source code](https://github.com/googleapis/google-cloud-python) 



































The following list contains links to more resources related to the
client library for Ruby:

- [API reference](https://googleapis.dev/ruby/google-cloud-logging/latest/Google/Cloud/Logging.html) 

- [Client libraries best practices](/apis/docs/client-libraries-best-practices) 

- [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues) 

- [`google-cloud-logging` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-logging%5D+%5Bruby%5D) 

- [Source code](https://github.com/googleapis/google-cloud-ruby) 






















## Additional client libraries

In addition to the libraries previously listed, a set of integration libraries
are available to support using popular third-party logging libraries with
Cloud Logging.



| 
Language | 
Library | 
|




| 
C# | 
[ASP.NET](https://www.nuget.org/packages/Google.Cloud.Diagnostics.AspNetCore) | 
|

| 
C# | 
[log4Net](https://www.nuget.org/packages/Google.Cloud.Logging.Log4Net) | 
|

| 
Java | 
[logback](https://github.com/googleapis/java-logging-logback) | 
|

| 
Node | 
[bunyan](https://www.npmjs.com/package/@google-cloud/logging-bunyan) | 
|

| 
Node | 
[winston](https://www.npmjs.com/package/@google-cloud/logging-winston) | 
|

| 
PHP | 
[PSR-3](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logger-interface.md) | 
|