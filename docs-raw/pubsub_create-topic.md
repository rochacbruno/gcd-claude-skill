# Create a topic

Source: https://berlin.devsitetest.how/pubsub/docs/create-topic
Last updated: 2026-06-29

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












# Create a topic 






- On this page 
- [ Before you begin ](#before_you_begin)

- [ Required roles and permissions ](#roles-permissions-for-topics)

- [ Properties of a topic ](#properties_of_a_topic)

- [ Add a default subscription ](#add_a_default_subscription)
- [ Enable ingestion ](#enable_ingestion)
- [ Enable message retention ](#enable_message_retention)
- [ Export message data to BigQuery ](#export_bigquery)
- [ Backup message data to Cloud Storage ](#export_storage)
- [ Transforms ](#transforms)
- [ Google Cloud-powered encryption key ](#google-managed_encryption_key)
- [ Cloud KMS key ](#cloud_kms_key)

- [ Create a topic ](#create_a_topic_2)
- [ What's next ](#whats_next)
- 





























Within Pub/Sub, a topic is a named resource that represents
a feed of messages. You must create a topic before you can publish or subscribe
to it. Pub/Sub supports two kinds of topics: a standard topic and
an import topic.

This document describes how to create a Pub/Sub standard topic. If
you want to learn more about an import topic and how to create one, see
[About import topics](/pubsub/docs/publish-message-overview#import-topic-overview).

To create a topic you can use the Google Cloud Dedicated console, the Google Cloud CLI,
the client library, or the Pub/Sub API.

## Before you begin 

- 

Learn about [the Pub/Sub service and its terminology](/pubsub/docs/pubsub-basics).

- 

Learn about the [publish process](/pubsub/docs/publish-message-overview).

### Required roles and permissions









































































To get the permissions that
you need to create a topic,

ask your administrator to grant you the
Pub/Sub Editor(`roles/pubsub.editor`)
IAM role on your project.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).








This predefined role contains

the permissions required to create a topic. To see the exact permissions that are
required, expand the **Required permissions** section:





#### Required permissions




The following permissions are required to create a topic:





- 
Grant this permission to create a topic on the project:
`pubsub.topics.create`














You might also be able to get
these permissions
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









You can configure access control at the project level and at the individual
resource level. You can create a subscription in one project and
attach it to a topic located in a different project.
Ensure that you have the required permissions for
each project.

## Properties of a topic

When you create or update a topic, you must specify its properties.

### Add a default subscription

Adds a default subscription to the Pub/Sub topic.
You can create another subscription for the topic after the topic is created.
The default subscription has the following properties:


- Subscription ID of `-sub`

- Pull delivery type

- Message retention duration of seven days

- Expiration after 31 days of inactivity

- Acknowledgment deadline of 10 seconds

- Immediate retry policy

### Enable ingestion

Enabling this property lets you ingest streaming data
from external sources into a topic so that you can use the
features of Google Cloud Dedicated. To create an import topic for
ingestion, see the following:

- 

[Create an Amazon Kinesis Data Streams import topic](/pubsub/docs/create-aws-kinesis-import-topic)

- 

[Create a Cloud Storage import topic](/pubsub/docs/create-cloud-storage-import-topic)

- 

[Create an Azure Event Hubs topic](/pubsub/docs/create-aws-kinesis-import-topic)

- 

[Create an Amazon MSK topic](/pubsub/docs/create-amazon-msk-import-topic)

- 

[Create a Confluent Cloud topic](/pubsub/docs/create-confluent-cloud-import-topic)

### Enable message retention

Specifies how long the Pub/Sub topic retains messages
after publication. After the message retention duration is over,
Pub/Sub might discard the message regardless of its
acknowledgment state. Message storage fees are charged for storing all
messages published to the topic


- Default = Not enabled

- Minimum value = 10 minutes

- Maximum value = 31 days

### Export message data to BigQuery

Enabling this property lets you create a BigQuery subscription
that writes messages to an existing BigQuery table as
they are received. You don't need to configure a separate subscriber
client. For more information about BigQuery subscriptions,
see [BigQuery subscriptions](/pubsub/docs/bigquery).

### Backup message data to Cloud Storage

Enabling this property lets you create a Cloud Storage
subscription that writes messages to an existing Cloud Storage
table as they are received. You don't need to configure a separate subscriber
client. For more information about Cloud Storage subscriptions,
see [Cloud Storage subscriptions](/pubsub/docs/cloudstorage).

### Transforms

Topic SMTs allow for lightweight modifications to message data and attributes
directly within Pub/Sub. This feature enables data cleaning,
filtering, or format conversion before the messages are published to the topic.

For more information about SMTs, see the [SMTs overview](/pubsub/docs/smts/smts-overview).

### Google Cloud-powered encryption key

Specifies that the topic is encrypted using
Google Cloud-powered encryption keys. Pub/Sub encrypts
messages with Google Cloud-powered encryption keys by default, so choosing
this option maintains the default behavior. Google handles key management and
rotation automatically, ensuring your messages are always protected with the
strongest available encryption. This option requires no further configuration.
For more information about Google Cloud-powered encryption keys,
see [Default encryption with Google Cloud-powered encryption keys](/kms/docs/cmek#default-encryption).

### Cloud KMS key

Specifies if the topic is encrypted with a customer-managed encryption
key (CMEK). Pub/Sub
encrypts messages with Google Cloud-powered encryption keys by default. If you specify
this option, Pub/Sub uses the envelope encryption pattern with
CMEK. In this approach, Cloud KMS does not encrypt the messages. Instead,
Cloud KMS encrypts the Data Encryption Keys (DEKs) that Pub/Sub
creates for each topic. Pub/Sub encrypts the messages using
the newest DEK that was generated for the topic. Pub/Sub
decrypts the messages shortly before they are delivered to subscribers.
For more information about creating a key, see [Configure message encryption](/pubsub/docs/encryption).

## Create a topic

Create a topic before you can publish or subscribe to it.


[Console](#console) [ gcloud ](#gcloud) [REST](#rest) [C++](#c++) [C#](#c) [Go](#go) [Java](#java) 
More 

[Node.js](#node.js) [Node.ts](#node.ts) [PHP](#php) [Python](#python) [Ruby](#ruby) 


To create a topic, follow these steps:

- 

In the Google Cloud Dedicated console, go to the Pub/Sub **Create topic**
page.

[Go to Create topic](https://console.cloud.berlin-build0.goog/cloudpubsub/topic/create)

- 

In the **Topic ID** field, enter an ID for your topic. For more information
about naming topics, see the
[naming guidelines](/pubsub/docs/pubsub-basics#resource_names).

- 

To create a [default subscription](#add_a_default_subscription) for the
topic, select **Add a default subscription**. This option is enabled by
default.

- 

Optional. To use a schema with the topic, click **Use a schema** and
provide the schema. For more information, see
[Create and associate a schema when you create a topic](/pubsub/docs/associate-schema-topic#create-schema-when-creating-topic).

- 

For a standard topic, leave **Enable ingestion** unselected.

- 

Optional. To retain messages after they are published, select
**Enable message retention**. Select the retention period in days, hours,
and minutes. For more information, see
[Enable message retention](#enable_message_retention).

- 

Optional. To export published messages to a BigQuery table,
select **Export data to BigQuery** and enter the details for the table.
For more information, see
[Create BigQuery subscriptions](/pubsub/docs/create-bigquery-subscription).

- 

Optional. To back up published messages to a Cloud Storage bucket,
select **Backup message data to Cloud Storage** and enter the details for
the Cloud Storage bucket. For more information, see
[Create Cloud Storage subscriptions](/pubsub/docs/create-cloudstorage-subscription).

- 

Optional. Under **Transforms**, add one or more
[Single Message Transforms](/pubsub/docs/smts/smts-overview) (SMTs) to
manipulate and filter message data. For more information, see
[Create a topic with SMTs](/pubsub/docs/smts/create-topic-smt).

- 

Optional. To use a customer-managed encryption key (CMEK) to encrypt
messages, select **Cloud KMS key**. By default, Pub/Sub
uses Google default encryption, which doesn't require a CMEK. For more
information, see [Configure message encryption](/pubsub/docs/encryption).

- 

Optional. To manage the keys associated with the topic, click
add **Manage keys**. For more
information, see
[Tags overview](/resource-manager/docs/tags/tags-overview).

- 

Click **Create topic**.




To create a topic, run the
[`gcloud pubsub topics create`](/sdk/gcloud/reference/pubsub/topics/create)
command:


```
gcloud pubsub topics create TOPIC_ID 
```




To create a topic, use the
[`projects.topics.create`](/pubsub/docs/reference/rest/v1/projects.topics/create)
method:

The request must be authenticated with an access token in the `Authorization`
header. To obtain an access token for the current Application Default
Credentials:
[`gcloud auth application-default print-access-token`](/sdk/gcloud/reference/auth/application-default/print-access-token).


```
PUT https://pubsub.googleapis.com/v1/projects/ PROJECT_ID /topics/ TOPIC_ID 
Authorization: Bearer ACCESS_TOKEN 
```


Where:

- PROJECT_ID is your project ID.

- TOPIC_ID is your topic ID.

Response:


```
{ 
"name" : "projects/ PROJECT_ID /topics/ TOPIC_ID " 
} 
```





Before trying this sample, follow the C++ setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/).























```
namespace pubsub = :: google :: cloud :: pubsub ; 
namespace pubsub_admin = :: google :: cloud :: pubsub_admin ; 
[]( pubsub_admin :: TopicAdminClient client , std :: string project_id , 
std :: string topic_id ) { 
auto topic = client . CreateTopic ( 
pubsub :: Topic ( std :: move ( project_id ), std :: move ( topic_id )). FullName ()); 
// Note that kAlreadyExists is a possible error when the library retries. 
if ( topic . status (). code () == google :: cloud :: StatusCode :: kAlreadyExists ) { 
std :: cout "The topic already exists \n " ; 
return ; 
} 
if ( ! topic ) throw std :: move ( topic ). status (); 

std :: cout "The topic was successfully created: " topic - > DebugString () 
" \n " ; 
} 
```








Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 
using [ Grpc.Core ](https://berlin.devsitetest.how/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html) ; 
using System ; 

public class CreateTopicSample 
{ 
public Topic CreateTopic ( string projectId , string topicId ) 
{ 
[ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create) (); 
var topicName = [ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) . [ FromProjectTopic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_) ( projectId , topicId ); 
[ Topic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) topic = null ; 

try 
{ 
topic = publisher . [ CreateTopic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_CreateTopic_Google_Cloud_PubSub_V1_Topic_Google_Api_Gax_Grpc_CallSettings_) ( topicName ); 
Console . WriteLine ( $"Topic {topic.[Name](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html#Google_Cloud_PubSub_V1_Topic_Name)} created." ); 
} 
catch ( [ RpcException ](https://berlin.devsitetest.how/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) e ) when ( e . [ Status ](https://berlin.devsitetest.how/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html) . [ StatusCode ](https://berlin.devsitetest.how/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [ StatusCode ](https://berlin.devsitetest.how/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) . [ AlreadyExists ](https://berlin.devsitetest.how/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_AlreadyExists) ) 
{ 
Console . WriteLine ( $"Topic {topicName} already exists." ); 
} 
return topic ; 
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
"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb" 
) 

func create ( w io . Writer , projectID , topicID string ) error { 
// projectID := "my-project-id" 
// topicID := "my-topic" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 
defer client . Close () 

topic := & pubsubpb . Topic { 
Name : fmt . Sprintf ( "projects/%s/topics/%s" , projectID , topicID ), 
} 
t , err := client . TopicAdminClient . CreateTopic ( ctx , topic ) 
if err != nil { 
return fmt . Errorf ( "CreateTopic: %w" , err ) 
} 
fmt . Fprintf ( w , "Topic created: %v\n" , t ) 
return nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.cloud.pubsub.v1.[TopicAdminClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) ; 
import com.google.pubsub.v1.[Topic](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) ; 
import com.google.pubsub.v1.[TopicName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) ; 
import java.io.IOException ; 

public class CreateTopicExample { 
public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String topicId = "your-topic-id" ; 

createTopicExample ( projectId , topicId ); 
} 

public static void createTopicExample ( String projectId , String topicId ) throws IOException { 
try ( [ TopicAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [ TopicAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) . create ()) { 
[ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) . of ( projectId , topicId ); 
[ Topic ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic = topicAdminClient . createTopic ( topicName ); 
System . out . println ( "Created topic: " + topic . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getName__) ()); 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO ( developer ): Uncomment this variable before running the sample . 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID' ; 

// Imports the Google Cloud client library 
const { PubSub } = require ( '@google-cloud/pubsub' ); 

// Creates a client ; cache this for further use 
const pubSubClient = new PubSub (); 

async function createTopic ( topicNameOrId ) { 
// Creates a new topic 
await pubSubClient . createTopic ( topicNameOrId ); 
console . log ( ` Topic $ { topicNameOrId } created . ` ); 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO ( developer ): Uncomment this variable before running the sample . 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID' ; 

// Imports the Google Cloud client library 
import { PubSub } from '@google-cloud/pubsub' ; 

// Creates a client ; cache this for further use 
const pubSubClient = new PubSub (); 

async function createTopic ( topicNameOrId : string ) { 
// Creates a new topic 
await pubSubClient . createTopic ( topicNameOrId ); 
console . log ( ` Topic $ { topicNameOrId } created . ` ); 
} 
```








Before trying this sample, follow the PHP setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub PHP API reference documentation](https://berlin.devsitetest.how/php/docs/reference/cloud-pubsub/latest).























```
use Google\Cloud\PubSub\PubSubClient; 

/** 
* Creates a Pub/Sub topic. 
* 
* @param string $projectId The Google project ID. 
* @param string $topicName The Pub/Sub topic name. 
*/ 
function create_topic($projectId, $topicName) 
{ 
$pubsub = new PubSubClient([ 
'projectId' => $projectId, 
]); 
$topic = $pubsub->createTopic($topicName); 

printf('Topic created: %s' . PHP_EOL, $topic->name()); 
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

topic = publisher . create_topic ( request = { "name" : topic_path }) 

print ( f "Created topic: { topic . name } " ) 
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

pubsub = Google :: Cloud :: [ PubSub ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
topic_admin = pubsub . [ topic_admin ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)

topic = topic_admin . create_topic name : pubsub . topic_path ( topic_id ) 

puts "Topic #{ topic . name } created." 
```






## What's next

- 

Choose the [type of subscription](/pubsub/docs/subscriber) for your topic.

- 

Learn how to [publish a message to a topic](/pubsub/docs/publisher).

- 

Troubleshoot a [topic](/pubsub/docs/topic-troubleshooting).

- 

Create or modify a topic with [gcloud CLI](/sdk/gcloud/reference/pubsub/topics),
[REST APIs](/pubsub/docs/reference/rest/v1/projects.topics), or [Client libraries](/pubsub/docs/reference/libraries).

*Apache Kafka® is a registered
trademark of The Apache Software Foundation or its affiliates in the United
States and/or other countries.*