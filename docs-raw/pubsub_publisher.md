# Publish messages to topics

Source: https://berlin.devsitetest.how/pubsub/docs/publisher
Last updated: 2026-07-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/pubsub/docs/tpc-differences) for more details.














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

Pub/Sub

](https://berlin.devsitetest.how/pubsub/docs)






- 








[

Guides

](https://berlin.devsitetest.how/pubsub/docs/overview)












# Publish messages to topics 






- On this page 
- [ Before you begin ](#before_you_begin)

- [ Required roles ](#required_roles)

- [ Message format ](#message_format)
- [ Publish messages ](#publish-messages)

- [ Use attributes to publish a message ](#using-attributes)
- [ Use ordering keys to publish a message ](#using-ordering-keys)

- [ Monitor a publisher ](#monitor_a_publisher)
- [ What's next ](#whats_next)
- 





























This document provides information about publishing messages.

A publisher application creates and sends messages to a **topic**.
Pub/Sub offers at-least-once message delivery and best-effort
ordering to existing subscribers.

The general flow for a publisher application is:

- Create a message containing your data.

- Send a request to the Pub/Sub server to publish the message
to the specified topic.

## Before you begin 

Before configuring the publish workflow, ensure you have completed the following
tasks:

- Learn about the [publishing workflow](/pubsub/docs/publish-message-overview).

- [Create a topic](/pubsub/docs/create-topic).

- [Choose and create a subscription](/pubsub/docs/subscription-overview#push_pull).

### Required roles


































To get the permissions that
you need to publish messages to a topic,

ask your administrator to grant you the
[Pub/Sub Publisher ](/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) IAM role on the topic.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









You need [additional permissions](/pubsub/docs/access-control) to
create or update topics and subscriptions.

## Message format

A message consists of fields with the message data and metadata. Specify at
least one of the following in the message:

- The message data

- An [ordering key](#using-ordering-keys)

- [Attributes](#using-attributes) with additional metadata

The Pub/Sub service adds the following fields to the message:

- A message ID unique to the topic

- A timestamp for when the Pub/Sub service receives the message

To learn more about messages, see [Message format](/pubsub/docs/publish-message-overview#about_messages).

## Publish messages

You can publish messages with the Google Cloud Dedicated console, Google Cloud CLI, Pub/Sub API,
and the client libraries. The client libraries can asynchronously publish messages.

The following samples demonstrate how to publish a message to a topic.


[Console](#console) [gcloud](#gcloud) [REST](#rest) [C++](#c++) [C#](#c) [Go](#go) [Java](#java) 
More 

[ Node.js ](#node.js-javascript) [ Node.js ](#node.js-typescript) [PHP](#php) [Python](#python) [Ruby](#ruby) 


To publish a message, follow these steps:

- 

In the Google Cloud Dedicated console, go to the **Pub/Sub topics** page.

[Go to the Pub/Sub topics page](https://console.cloud.berlin-build0.goog/cloudpubsub/topic/list) 

- 

Click the topic ID.

- 

In the **Topic details** page under **Messages**, click
**Publish message**.

- 

In the **Message body** field, enter the message data.

- 

Click **Publish**.




To publish a message, use the
[gcloud pubsub topics publish](/sdk/gcloud/reference/pubsub/topics/publish)
command:


```
gcloud pubsub topics publish TOPIC_ID \
--message= MESSAGE_DATA \
[--attribute= KEY =" VALUE ",...]
```


Replace the following:

- TOPIC_ID : the ID of the topic

- MESSAGE_DATA : a string with the message data

- KEY : the key of a [message attribute](#using-attributes)

- VALUE : the value for the key of the message attribute




To publish a message, send a POST request like the following:


```
POST https://pubsub.googleapis.com/v1/projects/ PROJECT_ID /topics/ TOPIC_ID :publish
Content-Type: application/json
Authorization: Bearer $(gcloud auth application-default print-access-token)
```


Replace the following:

- PROJECT_ID : the project ID of the project with the topic

- TOPIC_ID : the ID of the topic

Specify the following fields in the request body:


```
{
"messages": [
{
"attributes": {
" KEY ": " VALUE ",
... 
}, 
"data": " MESSAGE_DATA ", 
} 
] 
}
```


Replace the following:

- KEY : the key of a [message attribute](#using-attributes)

- VALUE : the value for the key of the message attribute

- MESSAGE_DATA : a base64-encoded string with the message data

The message must contain either a non-empty data field or at least one attribute.

If the request is successful, the response is a JSON object with the message
ID. The following example is a response with a message ID:


```
{
"messageIds": [
"19916711285",
]
}
```





Before trying this sample, follow the C++ setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/).























```
namespace pubsub = :: google :: cloud :: pubsub ; 
using :: google :: cloud :: future ; 
using :: google :: cloud :: StatusOr ; 
[]( pubsub :: Publisher publisher ) { 
auto message_id = publisher . Publish ( 
pubsub :: MessageBuilder {}. SetData ( "Hello World!" ). Build ()); 
auto done = message_id . then ([]( future :: string >> f ) { 
auto id = f . get (); 
if ( ! id ) throw std :: move ( id ). status (); 
std :: cout "Hello World! published with id=" * id " \n " ; 
}); 
// Block until the message is published 
done . get (); 
} 
```








Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 
using System ; 
using System.Collections.Generic ; 
using System.Linq ; 
using System.Threading ; 
using System.Threading.Tasks ; 

public class PublishMessagesAsyncSample 
{ 
public async Task PublishMessagesAsync ( string projectId , string topicId , IEnumerable messageTexts ) 
{ 
[ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) . [ FromProjectTopic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_) ( projectId , topicId ); 
[ PublisherClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) publisher = await [ PublisherClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_CreateAsync_Google_Cloud_PubSub_V1_TopicName_) ( topicName ); 

int publishedMessageCount = 0 ; 
var publishTasks = messageTexts . Select ( async text = >
{ 
try 
{ 
string message = await publisher . PublishAsync ( text ); 
Console . WriteLine ( $"Published message {message}" ); 
Interlocked . Increment ( ref publishedMessageCount ); 
} 
catch ( Exception exception ) 
{ 
Console . WriteLine ( $"An error occurred when publishing message {text}: {exception.Message}" ); 
} 
}); 
await Task . WhenAll ( publishTasks ); 
// PublisherClient instance should be shutdown after use. 
// The TimeSpan specifies for how long to attempt to publish locally queued messages. 
await publisher . [ ShutdownAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_ShutdownAsync_System_Threading_CancellationToken_) ( TimeSpan . FromSeconds ( 15 )); 
return publishedMessageCount ; 
} 
} 
```






The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see
[the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md).
To see a list of v1 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).






















```
import ( 
"context" 
"fmt" 
"io" 
"strconv" 
"sync" 
"sync/atomic" 

"cloud.google.com/go/pubsub/v2" 
) 

func publishThatScales ( w io . Writer , projectID , topicID string , n int ) error { 
// projectID := "my-project-id" 
// topicID := "my-topic" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 
defer client . Close () 

var wg sync . WaitGroup 
var totalErrors uint64 

// client.Publisher can be passed a topic ID (e.g. "my-topic") or 
// a fully qualified name (e.g. "projects/my-project/topics/my-topic"). 
// If a topic ID is provided, the project ID from the client is used. 
// Reuse this publisher for all publish calls to send messages in batches. 
publisher := client . Publisher ( topicID ) 

for i := 0 ; i n ; i ++ { 
result := publisher . Publish ( ctx , & pubsub . Message { 
Data : [] byte ( "Message " + strconv . Itoa ( i )), 
}) 

wg . Add ( 1 ) 
go func ( i int , res * pubsub . PublishResult ) { 
defer wg . Done () 
// The Get method blocks until a server-generated ID or 
// an error is returned for the published message. 
id , err := res . Get ( ctx ) 
if err != nil { 
// Error handling code can be added here. 
fmt . Fprintf ( w , "Failed to publish: %v" , err ) 
atomic . AddUint64 ( & totalErrors , 1 ) 
return 
} 
fmt . Fprintf ( w , "Published message %d; msg ID: %v\n" , i , id ) 
}( i , result ) 
} 

wg . Wait () 

if totalErrors > 0 { 
return fmt . Errorf ( "%d of %d messages did not publish successfully" , totalErrors , n ) 
} 
return nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.api.core.[ApiFuture](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html) ; 
import com.google.api.core.[ApiFutureCallback](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFutureCallback.html) ; 
import com.google.api.core.[ApiFutures](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html) ; 
import com.google.api.gax.rpc.[ApiException](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ; 
import com.google.cloud.pubsub.v1.[Publisher](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) ; 
import com.google.common.util.concurrent.MoreExecutors ; 
import com.google.protobuf.[ByteString](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) ; 
import com.google.pubsub.v1.[PubsubMessage](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) ; 
import com.google.pubsub.v1.[TopicName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) ; 
import java.io.IOException ; 
import java.util.Arrays ; 
import java.util.List ; 
import java.util.concurrent.TimeUnit ; 

public class PublishWithErrorHandlerExample { 

public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String topicId = "your-topic-id" ; 

publishWithErrorHandlerExample ( projectId , topicId ); 
} 

public static void publishWithErrorHandlerExample ( String projectId , String topicId ) 
throws IOException , InterruptedException { 
[ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) . of ( projectId , topicId ); 
[ Publisher ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null ; 

try { 
// Create a publisher instance with default settings bound to the topic 
publisher = [ Publisher ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) . newBuilder ( topicName ). build (); 

List messages = Arrays . asList ( "first message" , "second message" ); 

for ( final String message : messages ) { 
[ ByteString ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ ByteString ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) . [ copyFromUtf8 ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_) ( message ); 
[ PubsubMessage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [ PubsubMessage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) . newBuilder (). [ setData ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_) ( data ). build (); 

// Once published, returns a server-assigned message id (unique within the topic) 
ApiFuture future = [ publish ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er . [ publish ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_) ( pubsubMessage ); 

// Add an asynchronous callback to handle success / failure 
[ ApiFutures ](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html) . [ addCallback ](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_addCallback_com_google_api_core_ApiFuture_V__com_google_api_core_ApiFutureCallback___super_V__) ( 
future , 
new ApiFutureCallback () { 

@Override 
public void onFailure ( Throwable throwable ) { 
if ( throwable instanceof [ ApiException ](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ) { 
[ ApiException ](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) apiException = (( [ ApiException ](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ) throwable ); 
// details on the API exception 
System . out . println ( apiException . [ getStatusCode ](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html#com_google_api_gax_rpc_ApiException_getStatusCode__) (). getCode ()); 
System . out . println ( apiException . [ isRetryable ](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html#com_google_api_gax_rpc_ApiException_isRetryable__) ()); 
} 
System . out . println ( "Error publishing message : " + message ); 
} 

@Override 
public void onSuccess ( String messageId ) { 
// Once published, returns server-assigned message ids (unique within the topic) 
System . out . println ( "Published message ID: " + messageId ); 
} 
}, 
MoreExecutors . directExecutor ()); 
} 
} finally { 
if ( publisher != null ) { 
// When finished with the publisher, shutdown to free up resources. 
publisher . [ shutdown ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__) (); 
publisher . [ awaitTermination ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_) ( 1 , TimeUnit . MINUTES ); 
} 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID'; 
// const data = JSON.stringify({foo: 'bar'}); 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) (); 

async function publishMessage ( topicNameOrId , data ) { 
// Publishes the message as a string, e.g. "Hello, world!" or JSON.stringify(someObject) 
const dataBuffer = Buffer . [ from ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/duration.html) ( data ); 

// Cache topic objects (publishers) and reuse them. 
const topic = pubSubClient . topic ( topicNameOrId ); 

try { 
const messageId = await topic . [ publishMessage ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/topic.html) ({ data : dataBuffer }); 
console . log ( `Message ${ messageId } published.` ); 
} catch ( error ) { 
console . error ( `Received error while publishing: ${ error . message } ` ); 
process . exitCode = 1 ; 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID'; 
// const data = JSON.stringify({foo: 'bar'}); 

// Imports the Google Cloud client library 
import { PubSub } from '@google-cloud/pubsub' ; 

// Creates a client; cache this for further use 
const pubSubClient = new PubSub (); 

async function publishMessage ( topicNameOrId : string , data : string ) { 
// Publishes the message as a string, e.g. "Hello, world!" or JSON.stringify(someObject) 
const dataBuffer = Buffer . from ( data ); 

// Cache topic objects (publishers) and reuse them. 
const topic = pubSubClient . topic ( topicNameOrId ); 

try { 
const messageId = await topic . publishMessage ({ data : dataBuffer }); 
console . log ( `Message ${ messageId } published.` ); 
} catch ( error ) { 
console . error ( 
`Received error while publishing: ${ ( error as Error ). message } ` , 
); 
process . exitCode = 1 ; 
} 
} 
```








Before trying this sample, follow the PHP setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub PHP API reference documentation](https://berlin.devsitetest.how/php/docs/reference/cloud-pubsub/latest).























```
use Google\Cloud\PubSub\MessageBuilder; 
use Google\Cloud\PubSub\PubSubClient; 

/** 
* Publishes a message for a Pub/Sub topic. 
* 
* @param string $projectId The Google project ID. 
* @param string $topicName The Pub/Sub topic name. 
* @param string $message The message to publish. 
*/ 
function publish_message($projectId, $topicName, $message) 
{ 
$pubsub = new PubSubClient([ 
'projectId' => $projectId, 
]); 

$topic = $pubsub->topic($topicName); 
$topic->publish((new MessageBuilder)->setData($message)->build()); 

print('Message published' . PHP_EOL); 
} 
```








Before trying this sample, follow the Python setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Python API reference documentation](/python/docs/reference/pubsub/latest).























```
"""Publishes multiple messages to a Pub/Sub topic with an error handler.""" 
from concurrent import futures 
from google.cloud import pubsub_v1 
from typing import Callable 

# TODO(developer) 
# project_id = "your-project-id" 
# topic_id = "your-topic-id" 

publisher = pubsub_v1 . [ PublisherClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) () 
topic_path = publisher . topic_path ( project_id , topic_id ) 
publish_futures = [] 

def get_callback ( 
publish_future : pubsub_v1 . publisher . futures . Future , data : str 
) - > Callable [[ pubsub_v1 . publisher . futures . Future ], None ]: 
def callback ( publish_future : pubsub_v1 . publisher . futures . Future ) - > None : 
try : 
# Wait 60 seconds for the publish call to succeed. 
print ( publish_future . [ result ](https://berlin.devsitetest.how/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.futures.Future.html#google_cloud_pubsub_v1_publisher_futures_Future_result) ( timeout = 60 )) 
except futures . TimeoutError : 
print ( f "Publishing { [ data ](https://berlin.devsitetest.how/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data) } timed out." ) 

return callback 

for i in range ( 10 ): 
data = str ( i ) 
# When you publish a message, the client returns a future. 
publish_future = [ publish ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er . [ publish ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) ( topic_path , [ data ](https://berlin.devsitetest.how/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data) . encode ( "utf-8" )) 
# Non-blocking. Publish failures are handled in the callback function. 
publish_future . [ add_done_callback ](https://berlin.devsitetest.how/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.futures.Future.html#google_cloud_pubsub_v1_publisher_futures_Future_add_done_callback) ( get_callback ( publish_future , data )) 
publish_futures . append ( publish_future ) 

# Wait for all the publish futures to resolve before exiting. 
futures . wait ( publish_futures , return_when = futures . ALL_COMPLETED ) 

print ( f "Published messages with error handler to { topic_path } ." ) 
```






The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see
[ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md).
To see a list of Ruby v2 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html).






















```
# topic_id = "your-topic-id" 

pubsub = Google :: Cloud :: [ PubSub ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
publisher = pubsub . [ publisher ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) topic_id 

begin 
publisher . [ publish_async ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) "This is a test message." do | result | 
raise "Failed to publish the message." unless result . succeeded? 
puts "Message published asynchronously." 
end 
# Stop the async_publisher to send all queued messages immediately. 
publisher . [ async_publisher ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) . stop . wait! 
rescue StandardError = > e 
puts "Received error while publishing: #{ e . message } " 
end 
```






After you publish a message, the Pub/Sub service returns the
message ID to the publisher.

### Use attributes to publish a message

You can embed custom attributes as metadata in Pub/Sub messages.
Attributes are used to provide additional information about the message,
such as its priority, origin, or destination.
Attributes can also be used to filter messages on the subscription.

Follow these guidelines for using attributes in your messages:

- 

You can have at most 100 attributes per message.

- 

Attribute keys and values must be string types. There is no required encoding.

- 

Attribute keys must not start with `goog` and must not exceed 256 bytes.

- 

Attribute values must not exceed 1024 bytes.

The message schema can be represented as follows:


```
{
"data": string,
"attributes": {
string: string,
...
},
"messageId": string,
"publishTime": string,
"orderingKey": string
}
```


For publish-side duplicates, it's possible to see different `publishTime` values
for the same client-side original message, even with the same `messageId`.

The `PubsubMessage` JSON schema is published as part of the
[REST](/pubsub/docs/reference/rest/v1/PubsubMessage) and
[RPC](/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage) 
documentation. You can use custom attributes for event timestamps.

The following samples demonstrate how to publish a message with attributes
to a topic.


[Console](#console) [gcloud](#gcloud) [C++](#c++) [C#](#c) [Go](#go) [Java](#java) [Node.js](#node.js) [Python](#python) [Ruby](#ruby) 
More 




To publish a message with attributes, follow these steps:

- 

In the Google Cloud Dedicated console, go to the **Topics** page.

[Go to the Pub/Sub topics page](https://console.cloud.berlin-build0.goog/cloudpubsub/topic/list) 

- 

Click the topic for which you want to publish messages.

- 

In the topic details page, click **Messages**.

- 

Click **Publish message**.

- 

In the **Message body** field, enter the message data.

- 

Under **Message attributes**, click **Add an attribute**.

- 

Enter a key-value pair.

- 

Add more attributes, if required.

- 

Click **Publish**.



```
gcloud pubsub topics publish my-topic --message = "hello" \ 
--attribute = "origin=gcloud-sample,username=gcp,eventTime='2021-01-01T12:00:00Z'" 
```





Before trying this sample, follow the C++ setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/).























```
namespace pubsub = :: google :: cloud :: pubsub ; 
using :: google :: cloud :: future ; 
using :: google :: cloud :: StatusOr ; 
[]( pubsub :: Publisher publisher ) { 
std :: vector > done ; 
for ( int i = 0 ; i != 10 ; ++ i ) { 
auto message_id = publisher . Publish ( 
pubsub :: MessageBuilder {} 
. SetData ( "Hello World! [" + std :: to_string ( i ) + "]" ) 
. SetAttribute ( "origin" , "cpp-sample" ) 
. SetAttribute ( "username" , "gcp" ) 
. Build ()); 
done . push_back ( message_id . then ([ i ]( future :: string >> f ) { 
auto id = f . get (); 
if ( ! id ) throw std :: move ( id ). status (); 
std :: cout "Message " i " published with id=" * id " \n " ; 
})); 
} 
publisher . Flush (); 
// Block until all the messages are published (optional) 
for ( auto & f : done ) f . get (); 
} 
```








Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 
using [ Google.Protobuf ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html) ; 
using System ; 
using System.Threading.Tasks ; 

public class PublishMessageWithCustomAttributesAsyncSample 
{ 
public async Task PublishMessageWithCustomAttributesAsync ( string projectId , string topicId , string messageText ) 
{ 
[ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) . [ FromProjectTopic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_) ( projectId , topicId ); 
[ PublisherClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) publisher = await [ PublisherClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) . [ CreateAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_CreateAsync_Google_Cloud_PubSub_V1_TopicName_) ( topicName ); 

var pubsubMessage = new [ PubsubMessage ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html)
{ 
// The data is any arbitrary ByteString. Here, we're using text. 
Data = [ ByteString ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html) . [ CopyFromUtf8 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_) ( messageText ), 
// The attributes provide metadata in a string-to-string dictionary. 
Attributes = 
{ 
{ "year" , "2020" }, 
{ "author" , "unknown" } 
} 
}; 
string message = await publisher . [ PublishAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_PublishAsync_Google_Cloud_PubSub_V1_PubsubMessage_) ( pubsubMessage ); 
Console . WriteLine ( $"Published message {message}" ); 
// PublisherClient instance should be shutdown after use. 
// The TimeSpan specifies for how long to attempt to publish locally queued messages. 
await publisher . [ ShutdownAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_ShutdownAsync_System_Threading_CancellationToken_) ( TimeSpan . FromSeconds ( 15 )); 
} 
} 
```






The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see
[the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md).
To see a list of v1 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).






















```
import ( 
"context" 
"fmt" 
"io" 

"cloud.google.com/go/pubsub/v2" 
) 

func publishCustomAttributes ( w io . Writer , projectID , topicID string ) error { 
// projectID := "my-project-id" 
// topicID := "my-topic" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 
defer client . Close () 

// client.Publisher can be passed a topic ID (e.g. "my-topic") or 
// a fully qualified name (e.g. "projects/my-project/topics/my-topic"). 
// If a topic ID is provided, the project ID from the client is used. 
// Reuse this publisher for all publish calls to send messages in batches. 
publisher := client . Publisher ( topicID ) 
result := publisher . Publish ( ctx , & pubsub . Message { 
Data : [] byte ( "Hello world!" ), 
Attributes : map [ string ] string { 
"origin" : "golang" , 
"username" : "gcp" , 
}, 
}) 
// Block until the result is returned and a server-generated 
// ID is returned for the published message. 
id , err := result . Get ( ctx ) 
if err != nil { 
return fmt . Errorf ( "Get: %w" , err ) 
} 
fmt . Fprintf ( w , "Published message with custom attributes; msg ID: %v\n" , id ) 
return nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.api.core.[ApiFuture](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html) ; 
import com.google.cloud.pubsub.v1.[Publisher](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) ; 
import com.google.common.collect.ImmutableMap ; 
import com.google.protobuf.[ByteString](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) ; 
import com.google.pubsub.v1.[PubsubMessage](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) ; 
import com.google.pubsub.v1.[TopicName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) ; 
import java.io.IOException ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.TimeUnit ; 

public class PublishWithCustomAttributesExample { 
public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String topicId = "your-topic-id" ; 

publishWithCustomAttributesExample ( projectId , topicId ); 
} 

public static void publishWithCustomAttributesExample ( String projectId , String topicId ) 
throws IOException , ExecutionException , InterruptedException { 
[ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) . of ( projectId , topicId ); 
[ Publisher ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null ; 

try { 
// Create a publisher instance with default settings bound to the topic 
publisher = [ Publisher ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) . newBuilder ( topicName ). build (); 

String message = "first message" ; 
[ ByteString ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ ByteString ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) . [ copyFromUtf8 ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_) ( message ); 
[ PubsubMessage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = 
[ PubsubMessage ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) . newBuilder () 
. [ setData ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_) ( data ) 
. putAllAttributes ( ImmutableMap . of ( "year" , "2020" , "author" , "unknown" )) 
. build (); 

// Once published, returns a server-assigned message id (unique within the topic) 
ApiFuture messageIdFuture = [ publish ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er . [ publish ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_) ( pubsubMessage ); 
String messageId = messageIdFuture . get (); 
System . out . println ( "Published a message with custom attributes: " + messageId ); 

} finally { 
if ( publisher != null ) { 
// When finished with the publisher, shutdown to free up resources. 
publisher . [ shutdown ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__) (); 
publisher . [ awaitTermination ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_) ( 1 , TimeUnit . MINUTES ); 
} 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID'; 
// const data = JSON.stringify({foo: 'bar'}); 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) (); 

async function publishMessageWithCustomAttributes ( topicNameOrId , data ) { 
// Publishes the message as a string, e.g. "Hello, world!" or JSON.stringify(someObject) 
const dataBuffer = Buffer . [ from ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/duration.html) ( data ); 

// Add two custom attributes, origin and username, to the message 
const customAttributes = { 
origin : 'nodejs-sample' , 
username : 'gcp' , 
}; 

// Cache topic objects (publishers) and reuse them. 
const topic = pubSubClient . topic ( topicNameOrId ); 

const messageId = await topic . [ publishMessage ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/topic.html) ({ 
data : dataBuffer , 
attributes : customAttributes , 
}); 
console . log ( `Message ${ messageId } published.` ); 
} 
```








Before trying this sample, follow the Python setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Python API reference documentation](/python/docs/reference/pubsub/latest).























```
from google.cloud import pubsub_v1 

# TODO(developer) 
# project_id = "your-project-id" 
# topic_id = "your-topic-id" 

publisher = pubsub_v1 . [ PublisherClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) () 
topic_path = publisher . topic_path ( project_id , topic_id ) 

for n in range ( 1 , 10 ): 
data_str = f "Message number { n } " 
# Data must be a bytestring 
data = data_str . encode ( "utf-8" ) 
# Add two attributes, origin and username, to the message 
future = [ publish ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er . [ publish ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) ( 
topic_path , data , origin = "python-sample" , username = "gcp" 
) 
print ( future . result ()) 

print ( f "Published messages with custom attributes to { topic_path } ." ) 
```






The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see
[ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md).
To see a list of Ruby v2 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html).






















```
# topic_id = "your-topic-id" 

pubsub = Google :: Cloud :: [ PubSub ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
publisher = pubsub . [ publisher ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) topic_id 

# Add two attributes, origin and username, to the message 
publisher . [ publish_async ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) "This is a test message." , 
origin : "ruby-sample" , 
username : "gcp" do | result | 
raise "Failed to publish the message." unless result . succeeded? 
puts "Message with custom attributes published asynchronously." 
end 

# Stop the async_publisher to send all queued messages immediately. 
publisher . [ async_publisher ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) . stop . wait! 
```






### Use ordering keys to publish a message

To receive messages in order in your subscriber clients, you must configure
your publisher clients to publish messages with ordering keys.

To understand the concept of ordering keys, see [Order messages](/pubsub/docs/ordering).

Here is a list of key considerations for ordered messaging for publisher
clients:

- 

**Ordering in a single publisher client**: When a single publisher client
publishes messages with the same ordering key in the same region,
the subscriber client receives those messages in the exact order they
were published. For example, if a publisher client publishes
messages 1, 2, and 3 with the ordering key A, the subscriber client
receives them in the order 1, 2, 3.

- 

**Ordering across multiple publisher clients**: The order of messages received
by subscriber clients is consistent with the order in which they were
published in the same region, even when multiple publisher clients use the
same ordering key. However, the publisher clients themselves don't have
knowledge of this order.

For example, if publisher clients X and Y each
publish messages with ordering key A, and X's message is received by
Pub/Sub before Y's, then all subscriber clients
receive X's message before Y's. If strict message order across different
publisher clients is required, those clients must implement an additional
coordination mechanism to ensure they don't publish messages with the
same ordering key simultaneously. For example, a locking service
can be used to maintain ownership of an ordering key while publishing.

- 

**Ordering across regions**: The ordered delivery guarantee only applies
when publishes for an ordering key are in the same region. If your publisher
application publishes messages with the same ordering key to different
regions, order cannot be enforced across those publishes. Subscribers can
connect to any region and the ordering guarantee is still maintained.

When you run your application within Google Cloud Dedicated, by default it
connects to the Pub/Sub endpoint in the same region.
Therefore, running your application in a single region within
Google Cloud Dedicated generally ensures you are interacting with a single
region.

When you run your publisher application outside of
Google Cloud Dedicated or in multiple regions, you can guarantee you are
connecting to a single region by using a locational endpoint when
configuring your Pub/Sub client. All location endpoints for
Pub/Sub point to single regions. To learn more about
locational endpoints, see
[Pub/Sub endpoints](/pubsub/docs/reference/service_apis_overview#pubsub_endpoints).
For a list of all locational endpoints for Pub/Sub, see
[List of locational endpoints](/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints).

- 

**Publishing failures**: When publishing with an ordering key fails, queued-up
messages of the same ordering key in the publisher fail, including future
publish requests of this ordering key. You must resume publishing with
ordering keys when such failures occur. For an example of resuming the
publish operation, see [Retry requests with ordering keys](/pubsub/docs/retry-requests#retry_ordering).

You can publish messages with ordering keys using the Google Cloud Dedicated console,
Google Cloud CLI, Pub/Sub API, or the client libraries.


[Console](#console) [gcloud](#gcloud) [REST](#rest) [C++](#c++) [C#](#c) [Go](#go) [Java](#java) [Node.js](#node.js) [Python](#python) [Ruby](#ruby) 
More 




To publish a message with attributes, follow these steps:

- 

In the Google Cloud Dedicated console, go to the **Topics** page.

[Go to the Pub/Sub topics page](https://console.cloud.berlin-build0.goog/cloudpubsub/topic/list) 

- 

Click the topic for which you want to publish messages.

- 

In the topic details page, click **Messages**.

- 

Click **Publish message**.

- 

In the **Message body** field, enter the message data.

- 

In the **Message ordering** field, enter an ordering key.

- 

Click **Publish**.




To publish a message with an ordering key, use the
[`gcloud pubsub topics publish`](/sdk/gcloud/reference/pubsub/topics/publish)
command and the `--ordering-key` flag:


```
gcloud pubsub topics publish TOPIC_ID \
--message= MESSAGE_DATA \
--ordering-key= ORDERING_KEY 
```


Replace the following:

- TOPIC_ID : the ID of the topic

- MESSAGE_DATA : a string with the message data

- ORDERING_KEY : a string with an ordering key




To publish a message with an ordering key, send a POST request like the
following:


```
POST https://pubsub.googleapis.com/v1/projects/ PROJECT_ID /topics/ TOPIC_ID :publish
Content-Type: application/json
Authorization: Bearer $(gcloud auth application-default print-access-token)
```


Replace the following:

- PROJECT_ID : the project ID of the project with the topic

- TOPIC_ID : the ID of the topic

Specify the following fields in the request body:


```
{
"messages": [
{
"attributes": {
" KEY ": " VALUE ",
... 
}, 
"data": " MESSAGE_DATA ", 
"ordering_key": " ORDERING_KEY ", 
} 
] 
}
```


Replace the following:

- KEY : the key of a [message attribute](#using-attributes)

- VALUE : the value for the key of the message attribute

- MESSAGE_DATA : a base64-encoded string with the message data

- ORDERING_KEY : a string with an ordering key

The message must contain either a non-empty data field or at least one attribute.

If the request is successful, the response is a JSON object with the message
ID. The following example is a response with a message ID:


```
{
"messageIds": [
"19916711285",
]
}
```





Before trying this sample, follow the C++ setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/).























```
namespace pubsub = :: google :: cloud :: pubsub ; 
using :: google :: cloud :: future ; 
using :: google :: cloud :: StatusOr ; 
[]( pubsub :: Publisher publisher ) { 
struct SampleData { 
std :: string ordering_key ; 
std :: string data ; 
} data [] = { 
{ "key1" , "message1" }, { "key2" , "message2" }, { "key1" , "message3" }, 
{ "key1" , "message4" }, { "key1" , "message5" }, 
}; 
std :: vector > done ; 
for ( auto & datum : data ) { 
auto message_id = 
publisher . Publish ( pubsub :: MessageBuilder {} 
. SetData ( "Hello World! [" + datum . data + "]" ) 
. SetOrderingKey ( datum . ordering_key ) 
. Build ()); 
std :: string ack_id = datum . ordering_key + "#" + datum . data ; 
done . push_back ( message_id . then ([ ack_id ]( future :: string >> f ) { 
auto id = f . get (); 
if ( ! id ) throw std :: move ( id ). status (); 
std :: cout "Message " ack_id " published with id=" * id 
" \n " ; 
})); 
} 
publisher . Flush (); 
// Block until all the messages are published (optional) 
for ( auto & f : done ) f . get (); 
} 
```








Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 
using System ; 
using System.Collections.Generic ; 
using System.Linq ; 
using System.Threading ; 
using System.Threading.Tasks ; 

public class PublishOrderedMessagesAsyncSample 
{ 
public async Task PublishOrderedMessagesAsync ( string projectId , string topicId , IEnumerable ( string , string ) > keysAndMessages ) 
{ 
[ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) . [ FromProjectTopic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_) ( projectId , topicId ); 

var customSettings = new PublisherClient . Settings 
{ 
EnableMessageOrdering = true 
}; 

[ PublisherClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) publisher = await new [ PublisherClientBuilder ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClientBuilder.html)
{ 
TopicName = topicName , 
// Sending messages to the same region ensures they are received in order even when multiple publishers are used. 
Endpoint = "us-east1-pubsub.googleapis.com:443" , 
Settings = customSettings 
}. BuildAsync (); 

int publishedMessageCount = 0 ; 
var publishTasks = keysAndMessages . Select ( async keyAndMessage = >
{ 
try 
{ 
string message = await publisher . PublishAsync ( keyAndMessage . Item1 , keyAndMessage . Item2 ); 
Console . WriteLine ( $"Published message {message}" ); 
Interlocked . Increment ( ref publishedMessageCount ); 
} 
catch ( Exception exception ) 
{ 
Console . WriteLine ( $"An error occurred when publishing message {keyAndMessage.Item2}: {exception.Message}" ); 
} 
}); 
await Task . WhenAll ( publishTasks ); 
// PublisherClient instance should be shutdown after use. 
// The TimeSpan specifies for how long to attempt to publish locally queued messages. 
await publisher . [ ShutdownAsync ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_ShutdownAsync_System_Threading_CancellationToken_) ( TimeSpan . FromSeconds ( 15 )); 
return publishedMessageCount ; 
} 
} 
```






The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see
[the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md).
To see a list of v1 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).






















```
import ( 
"context" 
"fmt" 
"io" 
"sync" 
"sync/atomic" 

"cloud.google.com/go/pubsub/v2" 
"google.golang.org/api/option" 
) 

func publishWithOrderingKey ( w io . Writer , projectID , topicID string ) { 
// projectID := "my-project-id" 
// topicID := "my-topic" 
ctx := context . Background () 

// Pub/Sub's ordered delivery guarantee only applies when publishes for an ordering key are in the same region. 
// For list of locational endpoints for Pub/Sub, see https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints 
client , err := pubsub . NewClient ( ctx , projectID , 
option . WithEndpoint ( "us-east1-pubsub.googleapis.com:443" )) 
if err != nil { 
fmt . Fprintf ( w , "pubsub.NewClient: %v" , err ) 
return 
} 
defer client . Close () 

var wg sync . WaitGroup 
var totalErrors uint64 

// client.Publisher can be passed a topic ID (e.g. "my-topic") or 
// a fully qualified name (e.g. "projects/my-project/topics/my-topic"). 
// If a topic ID is provided, the project ID from the client is used. 
// Reuse this publisher for all publish calls to send messages in batches. 
publisher := client . Publisher ( topicID ) 
publisher . EnableMessageOrdering = true 

messages := [] struct { 
message string 
orderingKey string 
}{ 
{ 
message : "message1" , 
orderingKey : "key1" , 
}, 
{ 
message : "message2" , 
orderingKey : "key2" , 
}, 
{ 
message : "message3" , 
orderingKey : "key1" , 
}, 
{ 
message : "message4" , 
orderingKey : "key2" , 
}, 
} 

for _ , m := range messages { 
result := publisher . Publish ( ctx , & pubsub . Message { 
Data : [] byte ( m . message ), 
OrderingKey : m . orderingKey , 
}) 

wg . Add ( 1 ) 
go func ( res * pubsub . PublishResult ) { 
defer wg . Done () 
// The Get method blocks until a server-generated ID or 
// an error is returned for the published message. 
_ , err := res . Get ( ctx ) 
if err != nil { 
// Error handling code can be added here. 
fmt . Printf ( "Failed to publish: %s\n" , err ) 
atomic . AddUint64 ( & totalErrors , 1 ) 
return 
} 
}( result ) 
} 

wg . Wait () 

if totalErrors > 0 { 
fmt . Fprintf ( w , "%d of 4 messages did not publish successfully" , totalErrors ) 
return 
} 

fmt . Fprint ( w , "Published 4 messages with ordering keys successfully\n" ) 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.api.core.[ApiFuture](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html) ; 
import com.google.api.core.[ApiFutureCallback](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFutureCallback.html) ; 
import com.google.api.core.[ApiFutures](https://berlin.devsitetest.how/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html) ; 
import com.google.api.gax.rpc.[ApiException](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ; 
import com.google.cloud.pubsub.v1.[Publisher](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) ; 
import com.google.common.util.concurrent.MoreExecutors ; 
import com.google.protobuf.[ByteString](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) ; 
import com.google.pubsub.v1.[PubsubMessage](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) ; 
import com.google.pubsub.v1.[TopicName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) ; 
import java.io.IOException ; 
import java.util.LinkedHashMap ; 
import java.util.Map ; 
import java.util.concurrent.TimeUnit ; 

public class PublishWithOrderingKeys { 
public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
// Choose an existing topic. 
String topicId = "your-topic-id" ; 

publishWithOrderingKeysExample ( projectId , topicId ); 
} 

public static void publishWithOrderingKeysExample ( String projectId , String topicId ) 
throws IOException , InterruptedException { 
[ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) . of ( projectId , topicId ); 
// Create a publisher and set message ordering to true. 
[ Publisher ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = 
[ Publisher ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) . newBuilder ( topicName ) 
// Sending messages to the same region ensures they are received in order 
// even when multiple publishers are used. 
. setEndpoint ( "us-east1-pubsub.googleapis.com:443" ) 
. setEnableMessageOrdering ( true ) 
. build (); 

try { 
Map , String > messages = new LinkedHashMap , String > (); 
messages . put ( "message1" , "key1" ); 
messages . put ( "message2" , "key2" ); 
messages . put ( "message3" , "key1" ); 
messages . put ( "message4" , "key2" ); 

for ( Map . Entry , String > entry : messages . entrySet ()) { 
ByteString data = ByteString . copyFromUtf8 ( entry . getKey ()); 
PubsubMessage pubsubMessage = 
PubsubMessage . newBuilder (). setData ( data ). setOrderingKey ( entry . getValue ()). build (); 
ApiFuture future = publisher . publish ( pubsubMessage ); 

// Add an asynchronous callback to handle publish success / failure. 
ApiFutures . addCallback ( 
future , 
new ApiFutureCallback () { 

@Override 
public void onFailure ( Throwable throwable ) { 
if ( throwable instanceof ApiException ) { 
ApiException apiException = (( ApiException ) throwable ); 
// Details on the API exception. 
System . out . println ( apiException . getStatusCode (). getCode ()); 
System . out . println ( apiException . isRetryable ()); 
} 
System . out . println ( "Error publishing message : " + pubsubMessage . getData ()); 
} 

@Override 
public void onSuccess ( String messageId ) { 
// Once published, returns server-assigned message ids (unique within the topic). 
System . out . println ( pubsubMessage . getData () + " : " + messageId ); 
} 
}, 
MoreExecutors . directExecutor ()); 
} 
} finally { 
// When finished with the publisher, shutdown to free up resources. 
publisher . shutdown (); 
publisher . awaitTermination ( 1 , TimeUnit . MINUTES ); 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment these variables before running the sample. 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID'; 
// const data = JSON.stringify({foo: 'bar'}); 
// const orderingKey = 'key1'; 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) ({ 
// Sending messages to the same region ensures they are received in order 
// even when multiple publishers are used. 
apiEndpoint : 'us-east1-pubsub.googleapis.com:443' , 
}); 

async function publishOrderedMessage ( topicNameOrId , data , orderingKey ) { 
// Publishes the message as a string, e.g. "Hello, world!" or JSON.stringify(someObject) 
const dataBuffer = Buffer . [ from ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/duration.html) ( data ); 

// Be sure to set an ordering key that matches other messages 
// you want to receive in order, relative to each other. 
const message = { 
data : dataBuffer , 
orderingKey : orderingKey , 
}; 

// Cache topic objects (publishers) and reuse them. 
// 
// Pub/Sub's ordered delivery guarantee only applies when publishes for an ordering 
// key are in the same region. For list of locational endpoints for Pub/Sub, see: 
// https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints 
const publishOptions = { 
messageOrdering : true , 
}; 
const topic = pubSubClient . topic ( topicNameOrId , publishOptions ); 

// Publishes the message 
const messageId = await topic . [ publishMessage ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/topic.html) ( message ); 

console . log ( `Message ${ messageId } published.` ); 

return messageId ; 
} 
```








Before trying this sample, follow the Python setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Python API reference documentation](/python/docs/reference/pubsub/latest).























```
from google.cloud import pubsub_v1 

# TODO(developer): Choose an existing topic. 
# project_id = "your-project-id" 
# topic_id = "your-topic-id" 

publisher_options = pubsub_v1 . types . [ PublisherOptions ](https://berlin.devsitetest.how/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions.html) ( enable_message_ordering = True ) 
# Sending messages to the same region ensures they are received in order 
# even when multiple publishers are used. 
client_options = { "api_endpoint" : "us-east1-pubsub.googleapis.com:443" } 
publisher = pubsub_v1 . [ PublisherClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) ( 
publisher_options = publisher_options , client_options = client_options 
) 
# The `topic_path` method creates a fully qualified identifier 
# in the form `projects/{project_id}/topics/{topic_id}` 
topic_path = publisher . topic_path ( project_id , topic_id ) 

for message in [ 
( "message1" , "key1" ), 
( "message2" , "key2" ), 
( "message3" , "key1" ), 
( "message4" , "key2" ), 
]: 
# Data must be a bytestring 
data = message [ 0 ] . encode ( "utf-8" ) 
ordering_key = message [ 1 ] 
# When you publish a message, the client returns a future. 
future = [ publish ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er . [ publish ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) ( topic_path , data = data , ordering_key = ordering_key ) 
print ( future . result ()) 

print ( f "Published messages with ordering keys to { topic_path } ." ) 
```






The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see
[ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md).
To see a list of Ruby v2 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html).






















```
# topic_id = "your-topic-id" 

pubsub = Google :: Cloud :: [ PubSub ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
# Start sending messages in one request once the size of all queued messages 
# reaches 1 MB or the number of queued messages reaches 20 
publisher = pubsub . [ publisher ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) topic_id , async : { 
max_bytes : 1_000_000 , 
max_messages : 20 
} 

publisher . enable_message_ordering! 
10 . times do | i | 
publisher . [ publish_async ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) "This is message # #{ i } ." , 
ordering_key : "ordering-key" 
end 

# Stop the async_publisher to send all queued messages immediately. 
publisher . [ async_publisher ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) . stop! 
puts "Messages published with ordering key." 
```






## Monitor a publisher

Cloud Monitoring provides a number of metrics to monitor topics.

To monitor a topic and maintain a healthy publisher, see
[Maintain a healthy publisher](/pubsub/docs/monitoring#keeping_publishers_healthy).

## What's next

- 

To restrict the locations in which Pub/Sub stores message data, see
[Restricting Pub/Sub resource locations](/pubsub/docs/resource-location-restriction).

- 

To publish messages with schema, see [Schema overview](/pubsub/docs/schemas).

- 

To learn how to configure advanced delivery options, see the following:

- 

[Compress messages](/pubsub/docs/compress-messages)

- 

[Retry requests](/pubsub/docs/retry-requests)

- 

[Flow control](/pubsub/docs/flow-control-messages)

- 

[Concurrency control](/pubsub/docs/concurrency-control-messages)

- 

[Batch messaging](/pubsub/docs/batch-messaging)