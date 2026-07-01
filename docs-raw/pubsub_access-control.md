# Access control with Identity and Access Management

Source: https://berlin.devsitetest.how/pubsub/docs/access-control
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












# Access control with Identity and Access Management 






- On this page 
- [ Overview ](#overview)
- [ Types of roles in Pub/Sub ](#types_roles)
- [ Required Pub/Sub permissions ](#permissions)

- [ Required permissions for topics ](#required_permissions_for_topics)
- [ Required permissions for subscriptions ](#required_permissions_for_subscriptions)
- [ Required permissions for schemas ](#required_permissions_for_schemas)
- [ Required permissions for snapshots ](#required_permissions_for_snapshots)

- [ Available Pub/Sub roles ](#roles)

- [ Service agent roles ](#service-agent-roles)

- [ Controlling access through the Google Cloud Dedicated console ](#console)
- [ Controlling access through the IAM API ](#api)

- [ Get a policy ](#get-policy)
- [ Set a policy ](#set-policy)
- [ Test permissions ](#test-permissions)

- [ Cross-project communication ](#sample_use_case_cross-project_communication)
- [ Partial availability behavior ](#partial_availability_behavior)
- [ What's Next ](#whats_next)
- 





























This document describes the access control options available to you in Pub/Sub.

## Overview 

Pub/Sub uses [Identity and Access Management (IAM)](/iam) for access
control.

IAM allows you to grant specific **roles** to users, groups,
and service accounts, giving them the necessary **permissions** to perform their
tasks. You can grant these IAM roles using the
Google Cloud Dedicated console or the IAM API.

In Pub/Sub, access control can be configured at the project
level and at the individual resource level. Here are some examples for
using Pub/Sub access control:

- 

Grant access on a per-resource basis, rather than for the whole Cloud project.

- 

Grant access with limited capabilities, such as to only publish messages to a
topic, or to only consume messages from a subscription, but not to delete the
topic or subscription.

- 

Grant access to all Pub/Sub resources within a project to a
group of developers.

If you have view-only access to a single resource such as a topic or a
subscription, you cannot view the resource using the Google Cloud Dedicated console.
Instead, you can use Google Cloud CLI to view the resource.

For a detailed description of IAM and its features, see the
[IAM documentation](/iam). In particular, see
[Granting, changing, and revoking access to resources](/iam/docs/granting-changing-revoking-access).

## Types of roles in Pub/ Sub

Similar to other Google Cloud Dedicated in Germany products, Pub/Sub supports
three types of roles:

- 

**Basic roles**: Basic roles are highly permissive roles that existed prior
to the introduction of IAM. For more information about
basic roles, see [Basic roles](/iam/docs/roles-overview#basic).

- 

**Predefined roles**: Predefined roles give granular access to specific
Google Cloud Dedicated resources. For more information about
predefined roles, see [Predefined roles](/iam/docs/roles-permissions).
The Pub/Sub predefined roles are included in a
later part of this section.

- 

**Custom roles**: Custom roles help you enforce the principle of least
privilege. For more information about custom roles, see
[Custom roles](/iam/docs/roles-overview#custom).

## Required Pub/Sub permissions

The following sections lists Pub/Sub permissions required for
accessing different Pub/Sub resources.

### Required permissions for topics

The following table outlines the required permissions for each
Pub/Sub API method related to topics. It shows which
IAM permission is needed to call each method, along with a description of
what the method does.




| 
Method | 
Description | 
Required permission | 
|



| 
[`projects.topics.create`](/pubsub/docs/reference/rest/v1/projects.topics/create)
| 
Creates the given topic with the given name. | 
`pubsub.topics.create`
on the containing Cloud project | 
|

| 
[`projects.topics.delete`](/pubsub/docs/reference/rest/v1/projects.topics/delete)
| 
Deletes the topic with the given name. | 
`pubsub.topics.delete`
on the requested topic | 
|

| 
[`projects.topics.get`](/pubsub/docs/reference/rest/v1/projects.topics/get)
| 
Gets the configuration of a topic. | 
`pubsub.topics.get`
on the requested topic | 
|

| 
[`projects.topics.getIamPolicy`](/pubsub/docs/reference/rest/v1/projects.topics/getIamPolicy)
| 
Gets the IAM access control policy for a topic. | 
`pubsub.topics.getIamPolicy`
on the requested topic | 
|

| 
[`projects.topics.list`](/pubsub/docs/reference/rest/v1/projects.topics/list)
| 
Lists all topics. | 
`pubsub.topics.list`
on the requested Cloud project | 
|

| 
[`projects.topics.patch`](/pubsub/docs/reference/rest/v1/projects.topics/patch)
| 
Updates an existing topic. | 
`pubsub.topics.update`
on the requested topic | 
|

| 
[`projects.topics.publish`](/pubsub/docs/reference/rest/v1/projects.topics/publish)
| 
Adds one or more messages to the topic. | 
`pubsub.topics.publish`
on the requested topic | 
|

| 
[`projects.topics.setIamPolicy`](/pubsub/docs/reference/rest/v1/projects.topics/setIamPolicy)
| 
Sets the IAM access control policy for a topic. | 
`pubsub.topics.setIamPolicy`
on the requested topic | 
|

| 
[`projects.topics.testIamPermissions`](/pubsub/docs/reference/rest/v1/projects.topics/testIamPermissions)
| 
Returns permissions that a caller has on the specified resource. | 
None | 
|



### Required permissions for subscriptions

The following table outlines the required permissions for each
Pub/Sub API method related to subscriptions.
It shows which IAM permission is needed to call each method, along with a
description of what the method does.




| 
Method | 
Description | 
Required permission | 
|



| 
[`projects.subscriptions.acknowledge`](/pubsub/docs/reference/rest/v1/projects.subscriptions/acknowledge)
| 
Acknowledges the messages associated with the ack_ids in the
AcknowledgeRequest. | 
`pubsub.subscriptions.consume`
on the requested subscription | 
|

| 
[`projects.subscriptions.create`](/pubsub/docs/reference/rest/v1/projects.subscriptions/create)
| 
Creates a subscription to a given topic. | 
`pubsub.subscriptions.create`
on the containing Cloud project and
`pubsub.topics.attachSubscription` on the requested topic.
For creating a Subscription S in Project A that is
attached to a Topic T in Project B, the appropriate permissions must
be granted on both Project A and on Topic T. In this case, user
identity info can be captured in Project B's audit logs. | 
|

| 
[`projects.subscriptions.delete`](/pubsub/docs/reference/rest/v1/projects.subscriptions/delete)
| 
Deletes an existing subscription. | 
`pubsub.subscriptions.delete`
on the requested subscription | 
|

| 
[`projects.subscriptions.detach`](/pubsub/docs/reference/rest/v1/projects.subscriptions/detach)
| 
Detaches a subscription from a topic. | 
`pubsub.topics.detachSubscription` on the topic that the
subscription is attached to. | 
|

| 
[`projects.subscriptions.get`](/pubsub/docs/reference/rest/v1/projects.subscriptions/get)
| 
Gets the configuration details of a subscription. | 
`pubsub.subscriptions.get`
on the requested subscription | 
|

| 
[`projects.subscriptions.getIamPolicy`](/pubsub/docs/reference/rest/v1/projects.subscriptions/getIamPolicy)
| 
Gets the IAM access control policy for a subscription. | 
`pubsub.subscriptions.getIamPolicy`
on the requested subscription | 
|

| 
[`projects.subscriptions.list`](/pubsub/docs/reference/rest/v1/projects.subscriptions/list)
| 
Lists matching subscriptions. | 
`pubsub.subscriptions.list`
on the requested Cloud project | 
|

| 
[`projects.subscriptions.modifyAckDeadline`](/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline)
| 
Modifies the ack deadline for a specific message. | 
`pubsub.subscriptions.consume`
on the requested subscription | 
|

| 
[`projects.subscriptions.modifyPushConfig`](/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyPushConfig)
| 
Modifies the pushConfig for a specified subscription. | 
`pubsub.subscriptions.update`
on the requested subscription | 
|

| 
[`projects.subscriptions.patch`](/pubsub/docs/reference/rest/v1/projects.subscriptions/patch)
| 
Updates an existing subscription. | 
`pubsub.subscriptions.update`
on the requested subscription | 
|

| 
[`projects.subscriptions.pull`](/pubsub/docs/reference/rest/v1/projects.subscriptions/pull)
| 
Pulls messages from the server. | 
`pubsub.subscriptions.consume`
on the requested subscription | 
|

| 
[`projects.subscriptions.seek`](/pubsub/docs/reference/rest/v1/projects.subscriptions/seek)
| 
Seeks an existing subscription to a point in time or a snapshot. | 
`pubsub.subscriptions.consume`
on the requested subscription and `pubsub.snapshots.seek`
on the requested snapshot, if any. | 
|

| 
[`projects.subscriptions.setIamPolicy`](/pubsub/docs/reference/rest/v1/projects.subscriptions/setIamPolicy)
| 
Sets the IAM access control policy for a subscription. | 
`pubsub.subscriptions.setIamPolicy`
on the requested subscription | 
|

| 
[`projects.subscriptions.testIamPermissions`](/pubsub/docs/reference/rest/v1/projects.subscriptions/testIamPermissions)
| 
Returns permissions that a caller has on the specified resource. | 
None | 
|



### Required permissions for schemas

The following table outlines the required permissions for each
Pub/Sub API method related to schemas.
It shows which IAM permission is needed to call each method, along with a
description of what the method does.




| 
Method | 
Description | 
Required permission | 
|



| 
[`projects.schemas.commit`](/pubsub/docs/reference/rest/v1/projects.schemas/commit)
| 
Commits a new schema revision. | 
`pubsub.schemas.commit`
on the requested schema | 
|

| 
[`projects.schemas.create`](/pubsub/docs/reference/rest/v1/projects.schemas/create)
| 
Creates a schema. | 
`pubsub.schemas.create`
on the containing Cloud project | 
|

| 
[`projects.schemas.delete`](/pubsub/docs/reference/rest/v1/projects.schemas/delete)
| 
Deletes a schema. | 
`pubsub.schemas.delete`
on the requested schema | 
|

| 
[`projects.schemas.deleteRevision`](/pubsub/docs/reference/rest/v1/projects.schemas/deleteRevision)
| 
Deletes a specific schema revision. | 
`pubsub.schemas.delete`
on the requested schema | 
|

| 
[`projects.schemas.get`](/pubsub/docs/reference/rest/v1/projects.schemas/get)
| 
Gets a schema. | 
`pubsub.schemas.get`
on the requested schema | 
|

| 
[`projects.schemas.getIamPolicy`](/pubsub/docs/reference/rest/v1/projects.schemas/getIamPolicy)
| 
Gets the IAM access control policy for a schema. | 
`pubsub.schemas.getIamPolicy` on the requested schema | 
|

| 
[`projects.schemas.list`](/pubsub/docs/reference/rest/v1/projects.schemas/list)
| 
Lists schemas in a project. | 
`pubsub.schemas.list`
on the requested Cloud project | 
|

| 
[`projects.schemas.listRevisions`](/pubsub/docs/reference/rest/v1/projects.schemas/listRevisions)
| 
Lists all schema revisions for the named schema. | 
`pubsub.schemas.listRevisions`
on the requested schema | 
|

| 
[`projects.schemas.rollback`](/pubsub/docs/reference/rest/v1/projects.schemas/rollback)
| 
Creates a new schema revision from a previous revision. | 
`pubsub.schemas.rollback`
on the requested schema | 
|

| 
[`projects.schemas.validate`](/pubsub/docs/reference/rest/v1/projects.schemas/validate)
| 
Validates a schema definition. | 
`pubsub.schemas.validate`
on the containing Cloud project | 
|

| 
[`projects.schemas.validateMessage`](/pubsub/docs/reference/rest/v1/projects.schemas/validateMessage)
| 
Validates a message against a schema. | 
`pubsub.schemas.validate`
on the containing Cloud project | 
|



### Required permissions for snapshots

The following table outlines the required permissions for each
Pub/Sub API method related to snapshots.
It shows which IAM permission is needed to call each method, along with a
description of what the method does.




| 
REST method | 
Description | 
Required permission | 
|



| 
[`projects.snapshots.create`](/pubsub/docs/reference/rest/v1/projects.snapshots/create)
| 
Creates a snapshot from the requested subscription. | 
`pubsub.snapshots.create`
on the containing Cloud project and `pubsub.subscriptions.consume`
permission on the source subscription. | 
|

| 
[`projects.snapshots.delete`](/pubsub/docs/reference/rest/v1/projects.snapshots/delete)
| 
Removes an existing snapshot. | 
`pubsub.snapshots.delete`
on the requested snapshot | 
|

| 
[`projects.snapshots.getIamPolicy`](/pubsub/docs/reference/rest/v1/projects.snapshots/getIamPolicy)
| 
Gets the IAM access control policy for a snapshot. | 
`pubsub.snapshots.getIamPolicy`
on the requested snapshot | 
|

| 
[`projects.snapshots.list`](/pubsub/docs/reference/rest/v1/projects.snapshots/list)
| 
Lists the existing snapshots. | 
`pubsub.snapshots.list`
on the requested Cloud project | 
|

| 
[`projects.snapshots.patch`](/pubsub/docs/reference/rest/v1/projects.snapshots/patch)
| 
Updates an existing snapshot. | 
`pubsub.snapshots.update`
on the requested snapshot | 
|

| 
[`projects.snapshots.setIamPolicy`](/pubsub/docs/reference/rest/v1/projects.snapshots/setIamPolicy)
| 
Sets the IAM access control policy for a snapshot. | 
`pubsub.snapshots.setIamPolicy`
on the requested snapshot | 
|

| 
[`projects.snapshots.testIamPermissions`](/pubsub/docs/reference/rest/v1/projects.snapshots/testIamPermissions)
| 
Returns permissions that a caller has on the specified resource. | 
None | 
|



## Available Pub/Sub roles

The following table lists all Pub/Sub roles and the
permissions associated with each role:



5 results 


| 
Role | 
Permissions | 
|



| 

#### Pub/Sub Admin

(`roles/ pubsub.admin`)



Provides full access to topics and subscriptions.



Lowest-level resources where you can grant this role:

- 
Schema

- 
Snapshot

- 
Subscription

- 
Topic

| 



`cloudkms.keyHandles.*` 






- `cloudkms.keyHandles.create`

- `cloudkms.keyHandles.get`

- `cloudkms.keyHandles.list`





`cloudkms.operations.get`



`cloudkms. projects. showEffectiveAutokeyConfig`



`pubsub.*` 






- `pubsub. messageTransforms. validate`

- `pubsub.schemas.attach`

- `pubsub.schemas.commit`

- `pubsub.schemas.create`

- `pubsub.schemas.delete`

- `pubsub.schemas.get`

- `pubsub.schemas.getIamPolicy`

- `pubsub.schemas.list`

- `pubsub.schemas.listRevisions`

- `pubsub.schemas.rollback`

- `pubsub.schemas.setIamPolicy`

- `pubsub.schemas.validate`

- `pubsub.snapshots.create`

- `pubsub. snapshots. createTagBinding`

- `pubsub.snapshots.delete`

- `pubsub. snapshots. deleteTagBinding`

- `pubsub.snapshots.get`

- `pubsub.snapshots.getIamPolicy`

- `pubsub.snapshots.list`

- `pubsub. snapshots. listEffectiveTags`

- `pubsub. snapshots. listTagBindings`

- `pubsub.snapshots.seek`

- `pubsub.snapshots.setIamPolicy`

- `pubsub.snapshots.update`

- `pubsub.subscriptions.consume`

- `pubsub.subscriptions.create`

- `pubsub. subscriptions. createTagBinding`

- `pubsub.subscriptions.delete`

- `pubsub. subscriptions. deleteTagBinding`

- `pubsub.subscriptions.get`

- `pubsub. subscriptions. getIamPolicy`

- `pubsub.subscriptions.list`

- `pubsub. subscriptions. listEffectiveTags`

- `pubsub. subscriptions. listTagBindings`

- `pubsub. subscriptions. setIamPolicy`

- `pubsub.subscriptions.update`

- `pubsub. topics. attachSubscription`

- `pubsub.topics.create`

- `pubsub.topics.createTagBinding`

- `pubsub.topics.delete`

- `pubsub.topics.deleteTagBinding`

- `pubsub. topics. detachSubscription`

- `pubsub.topics.get`

- `pubsub.topics.getIamPolicy`

- `pubsub.topics.list`

- `pubsub. topics. listEffectiveTags`

- `pubsub.topics.listTagBindings`

- `pubsub.topics.publish`

- `pubsub.topics.setIamPolicy`

- `pubsub.topics.update`

- `pubsub.topics.updateTag`





`resourcemanager.projects.get`



`serviceusage. consumerpolicy. analyze`



`serviceusage. consumerpolicy. get`



`serviceusage. effectivepolicy. get`



`serviceusage.groups.*` 






- `serviceusage.groups.list`

- `serviceusage. groups. listExpandedMembers`

- `serviceusage. groups. listMembers`





`serviceusage.quotas.get`



`serviceusage.services.get`



`serviceusage.services.list`



`serviceusage.values.test`

| 
|

| 

#### Pub/Sub Editor

(`roles/ pubsub.editor`)



Provides access to modify topics and subscriptions, and access to publish
and consume messages.



Lowest-level resources where you can grant this role:

- 
Schema

- 
Snapshot

- 
Subscription

- 
Topic

| 



`cloudkms.keyHandles.*` 






- `cloudkms.keyHandles.create`

- `cloudkms.keyHandles.get`

- `cloudkms.keyHandles.list`





`cloudkms.operations.get`



`cloudkms. projects. showEffectiveAutokeyConfig`



`pubsub. messageTransforms. validate`



`pubsub.schemas.attach`



`pubsub.schemas.commit`



`pubsub.schemas.create`



`pubsub.schemas.delete`



`pubsub.schemas.get`



`pubsub.schemas.list`



`pubsub.schemas.listRevisions`



`pubsub.schemas.rollback`



`pubsub.schemas.validate`



`pubsub.snapshots.create`



`pubsub. snapshots. createTagBinding`



`pubsub.snapshots.delete`



`pubsub. snapshots. deleteTagBinding`



`pubsub.snapshots.get`



`pubsub.snapshots.list`



`pubsub. snapshots. listEffectiveTags`



`pubsub. snapshots. listTagBindings`



`pubsub.snapshots.seek`



`pubsub.snapshots.update`



`pubsub.subscriptions.consume`



`pubsub.subscriptions.create`



`pubsub. subscriptions. createTagBinding`



`pubsub.subscriptions.delete`



`pubsub. subscriptions. deleteTagBinding`



`pubsub.subscriptions.get`



`pubsub.subscriptions.list`



`pubsub. subscriptions. listEffectiveTags`



`pubsub. subscriptions. listTagBindings`



`pubsub.subscriptions.update`



`pubsub. topics. attachSubscription`



`pubsub.topics.create`



`pubsub.topics.createTagBinding`



`pubsub.topics.delete`



`pubsub.topics.deleteTagBinding`



`pubsub. topics. detachSubscription`



`pubsub.topics.get`



`pubsub.topics.list`



`pubsub. topics. listEffectiveTags`



`pubsub.topics.listTagBindings`



`pubsub.topics.publish`



`pubsub.topics.update`



`pubsub.topics.updateTag`



`resourcemanager.projects.get`



`serviceusage. consumerpolicy. analyze`



`serviceusage. consumerpolicy. get`



`serviceusage. effectivepolicy. get`



`serviceusage.groups.*` 






- `serviceusage.groups.list`

- `serviceusage. groups. listExpandedMembers`

- `serviceusage. groups. listMembers`





`serviceusage.quotas.get`



`serviceusage.services.get`



`serviceusage.services.list`



`serviceusage.values.test`

| 
|

| 

#### Pub/Sub Publisher

(`roles/ pubsub.publisher`)



Provides access to publish messages to a topic.



Lowest-level resources where you can grant this role:

- 
Topic

| 



`pubsub.topics.publish`

| 
|

| 

#### Pub/Sub Subscriber

(`roles/ pubsub.subscriber`)



Provides access to consume messages from a subscription and to attach
subscriptions to a topic.



Lowest-level resources where you can grant this role:

- 
Snapshot

- 
Subscription

- 
Topic

| 



`pubsub.snapshots.seek`



`pubsub.subscriptions.consume`



`pubsub. topics. attachSubscription`

| 
|

| 

#### Pub/Sub Viewer

(`roles/ pubsub.viewer`)



Provides access to view topics and subscriptions.



Lowest-level resources where you can grant this role:

- 
Schema

- 
Snapshot

- 
Subscription

- 
Topic

| 



`pubsub. messageTransforms. validate`



`pubsub.schemas.get`



`pubsub.schemas.list`



`pubsub.schemas.listRevisions`



`pubsub.schemas.validate`



`pubsub.snapshots.get`



`pubsub.snapshots.list`



`pubsub. snapshots. listEffectiveTags`



`pubsub. snapshots. listTagBindings`



`pubsub.subscriptions.get`



`pubsub.subscriptions.list`



`pubsub. subscriptions. listEffectiveTags`



`pubsub. subscriptions. listTagBindings`



`pubsub.topics.get`



`pubsub.topics.list`



`pubsub. topics. listEffectiveTags`



`pubsub.topics.listTagBindings`



`resourcemanager.projects.get`



`serviceusage. consumerpolicy. analyze`



`serviceusage. consumerpolicy. get`



`serviceusage. effectivepolicy. get`



`serviceusage.groups.*` 






- `serviceusage.groups.list`

- `serviceusage. groups. listExpandedMembers`

- `serviceusage. groups. listMembers`





`serviceusage.quotas.get`



`serviceusage.services.get`



`serviceusage.services.list`



`serviceusage.values.test`

| 
|




### Service agent roles

Service agent roles should only be granted to [service agents](/iam/docs/service-agents).



1 result 


| 
Role | 
Permissions | 
|



| 

#### Cloud Pub/Sub Service Agent

(`roles/ pubsub.serviceAgent`)



Grants Cloud Pub/Sub Service Account access to manage resources.



| 



`iam.serviceAccounts.get`



`iam. serviceAccounts. getAccessToken`



`iam. serviceAccounts. getOpenIdToken`



`iam. serviceAccounts. implicitDelegation`



`iam.serviceAccounts.list`



`iam.serviceAccounts.signBlob`



`iam.serviceAccounts.signJwt`



`resourcemanager.projects.get`



`resourcemanager.projects.list`



`serviceusage.services.use`

| 
|




## Controlling access through the Google Cloud Dedicated console

You can use the Google Cloud Dedicated console to manage access control for your topics
and projects.

To set access controls at the project level, follow these steps:

- 

In the Google Cloud Dedicated console, go to the IAM page.

[Go
to IAM](https://console.cloud.berlin-build0.goog/project/_/iam-admin/iam)

- 

Select your project.

- 

Click person_add **Add**.

- 

Type in one or more principal names.

- 

In the **Select a role** list, select the role you want to grant.

- 

Click **Save**.

- 

Verify that the principal is listed with the role that you granted.

To set access controls for topics and subscriptions, follow these steps:

- 

In the Google Cloud Dedicated console, go to the Pub/Sub **Topics** list.

[Go
to Topics](https://console.cloud.berlin-build0.goog/cloudpubsub/topic/list)

- 

If needed, select your Pub/Sub-enabled project.

- 

Perform one of the following steps:

- 

To set roles for one or more topics, select the topics.

- 

To set roles for a subscription attached to a topic, click the topic
ID. In the **Topic details** page, click the subscription ID. The
**Subscription details** page appears.

- 

If the info panel is hidden, click **Show info panel**.

- 

In the **Permissions** tab, click
person_add **Add principal**.

- 

Type in one or more principal names.

- 

In the **Select a role** list, select the role you want to grant.

- 

Click **Save**.

## Controlling access through the IAM API

The Pub/Sub IAM API lets you set and get policies on
individual topics and subscriptions in a project, and test a user's permissions
for a given resource. As with the regular Pub/Sub methods, you
can invoke the IAM API methods through the client libraries, or the API
Explorer, or directly over HTTP.

Note that you cannot use the Pub/Sub IAM API to
manage policies at the Google Cloud Dedicated project level.

The following sections give examples for how to set and get a policy, and how to
test what permissions a caller has for a given resource.

### Get a policy

The `getIamPolicy()` method allows you to [get an existing policy](/iam/docs/managing-policies).
This method returns a JSON object containing the policy associated with the
resource.

Here is some sample code to [get a policy for a subscription](/pubsub/docs/reference/rest/v1/projects.subscriptions/getIamPolicy):


[C#](#c) [gcloud](#gcloud) [Go](#go) [Java](#java) [ Node.js ](#node.js-javascript) [ Node.js ](#node.js-typescript) [PHP](#php) [Python](#python) [Ruby](#ruby) 
More 






Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.Iam.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html) ; 
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 

public class GetSubscriptionIamPolicySample 
{ 
public Policy GetSubscriptionIamPolicy ( string projectId , string subscriptionId ) 
{ 
[ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create) (); 
[ SubscriptionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [ SubscriptionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) . [ FromProjectSubscription ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_) ( projectId , subscriptionId ); 
[ Policy ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) policy = publisher . [ IAMPolicyClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_IAMPolicyClient) . GetIamPolicy ( new [ GetIamPolicyRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)
{ 
ResourceAsResourceName = subscriptionName 
}); 
return policy ; 
} 
} 
```






Get the subscription policy:


```
gcloud pubsub subscriptions get-iam-policy \
projects/ ${ PROJECT } /subscriptions/ ${ SUBSCRIPTION } \
--format json
```



Output:


```
{ 
"etag" : "BwUjMhCsNvY=" , 
"bindings" : [ 
{ 
"role" : "roles/pubsub.admin" , 
"members" : [ 
"user:user-1@gmail.com" 
] 
}, 
{ 
"role" : "roles/pubsub.editor" , 
"members" : [ 
"serviceAccount:service-account-2@appspot.eu0-system.iam.gserviceaccount.com" , 
"user:user-3@gmail.com" 
] 
} 
] 
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

"cloud.google.com/go/iam/apiv1/iampb" 
"cloud.google.com/go/pubsub/v2" 
) 

func getIAMPolicy ( w io . Writer , projectID , subscription string ) error { 
// projectID := "my-project-id" 
// subscription := "projects/my-project/subscriptions/my-sub" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 
defer client . Close () 

req := & iampb . [ GetIamPolicyRequest ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest) { 
Resource : subscription , 
} 
policy , err := client . SubscriptionAdminClient . [ GetIamPolicy ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_GetIamPolicy) ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "Policy: %w" , err ) 
} 
for _ , b := range policy . Bindings { 
for _ , m := range b . Members { 
fmt . Fprintf ( w , "role: %s, member: %s\n" , b . Role , m ) 
} 
} 
return nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) ; 
import com.google.iam.v1.[GetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import com.google.pubsub.v1.[ProjectSubscriptionName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) ; 
import java.io.IOException ; 

public class GetSubscriptionPolicyExample { 
public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String subscriptionId = "your-subscription-id" ; 

getSubscriptionPolicyExample ( projectId , subscriptionId ); 
} 

public static void getSubscriptionPolicyExample ( String projectId , String subscriptionId ) 
throws IOException { 
try ( [ SubscriptionAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [ SubscriptionAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) . create ()) { 
[ ProjectSubscriptionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName = 
[ ProjectSubscriptionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) . of ( projectId , subscriptionId ); 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) getIamPolicyRequest = 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) . newBuilder (). setResource ( subscriptionName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__) ()). build (); 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = subscriptionAdminClient . getIamPolicy ( getIamPolicyRequest ); 
System . out . println ( "Subscription policy: " + policy ); 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment this variable before running the sample. 
*/ 
// const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID'; 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) (); 

async function getSubscriptionPolicy ( subscriptionNameOrId ) { 
// Retrieves the IAM policy for the subscription 
const [ policy ] = await pubSubClient 
. subscription ( subscriptionNameOrId ) 
. iam . [ getPolicy ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/iam.html) (); 

console . log ( `Policy for subscription: ${ [ JSON ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/protos.google.pubsub.v1.encoding.html) . stringify ( policy . bindings ) } .` ); 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment this variable before running the sample. 
*/ 
// const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID'; 

// Imports the Google Cloud client library 
import { PubSub , Policy } from '@google-cloud/pubsub' ; 

// Creates a client; cache this for further use 
const pubSubClient = new PubSub (); 

async function getSubscriptionPolicy ( subscriptionNameOrId : string ) { 
// Retrieves the IAM policy for the subscription 
const [ policy ] : [ Policy ] = await pubSubClient 
. subscription ( subscriptionNameOrId ) 
. iam . getPolicy (); 

console . log ( `Policy for subscription: ${ JSON . stringify ( policy . bindings ) } .` ); 
} 
```








Before trying this sample, follow the PHP setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub PHP API reference documentation](https://berlin.devsitetest.how/php/docs/reference/cloud-pubsub/latest).























```
use Google\Cloud\PubSub\PubSubClient; 

/** 
* Prints the policy for a PubSub subscription. 
* 
* @param string $projectId The Google project ID. 
* @param string $subscriptionName The Pub/Sub subscription name. 
*/ 
function get_subscription_policy($projectId, $subscriptionName) 
{ 
$pubsub = new PubSubClient([ 
'projectId' => $projectId, 
]); 
$subscription = $pubsub->subscription($subscriptionName); 
$policy = $subscription->iam()->policy(); 
print_r($policy); 
} 
```








Before trying this sample, follow the Python setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Python API reference documentation](/python/docs/reference/pubsub/latest).























```
from google.cloud import pubsub_v1 

# TODO(developer): Choose an existing subscription. 
# project_id = "your-project-id" 
# subscription_id = "your-subscription-id" 

client = pubsub_v1 . [ SubscriberClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html) () 
subscription_path = client . subscription_path ( project_id , subscription_id ) 

policy = client . get_iam_policy ( request = { "resource" : subscription_path }) 

print ( "Policy for subscription {} :" . format ( subscription_path )) 
for binding in policy . bindings : 
print ( "Role: {} , Members: {} " . format ( binding . role , binding . members )) 

client . [ close ](https://berlin.devsitetest.how/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client.html#google_cloud_pubsub_v1_subscriber_client_Client_close) () 
```






The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see
[ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md).
To see a list of Ruby v2 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html).






















```
# subscription_id = "your-subscription-id" 

pubsub = Google :: Cloud :: [ PubSub ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)

policy = pubsub . [ iam ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) . get_iam_policy \ 
resource : pubsub . subscription_path ( subscription_id ) 

puts "Subscription policy:" 
puts policy . bindings . first . role 
```



Here is some sample code to [get a policy for a topic](/pubsub/docs/reference/rest/v1/projects.topics/getIamPolicy):






Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.Iam.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html) ; 
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 

public class GetTopicIamPolicySample 
{ 
public Policy GetTopicIamPolicy ( string projectId , string topicId ) 
{ 
[ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create) (); 
[ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) . [ FromProjectTopic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_) ( projectId , topicId ); 
[ Policy ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) policy = publisher . [ IAMPolicyClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_IAMPolicyClient) . GetIamPolicy ( new [ GetIamPolicyRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)
{ 
ResourceAsResourceName = topicName 
}); 
return policy ; 
} 
} 
```






Get the topic policy


```
gcloud pubsub topics get-iam-policy \
projects/ ${ PROJECT } /topics/ ${ TOPIC } \
--format json
```


Output:


```
{ 
"etag" : "BwUjMhCsNvY=" , 
"bindings" : [ 
{ 
"role":" roles/pubsub.viewer", 
"members": [ 
"user:user-1@gmail.com" 
] 
} 
] 
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

"cloud.google.com/go/iam/apiv1/iampb" 
"cloud.google.com/go/pubsub/v2" 
) 

func getIAMPolicy ( w io . Writer , projectID , topicID string ) error { 
// projectID := "my-project-id" 
// topicID := "my-topic" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 
defer client . Close () 

req := & iampb . [ GetIamPolicyRequest ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest) { 
Resource : fmt . Sprintf ( "projects/%s/topics/%s" , projectID , topicID ), 
} 
policy , err := client . TopicAdminClient . [ GetIamPolicy ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_GetIamPolicy) ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "Policy: %w" , err ) 
} 
for _ , b := range policy . Bindings { 
for _ , m := range b . Members { 
fmt . Fprintf ( w , "role: %s, member: %s\n" , b . Role , m ) 
} 
} 
return nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.cloud.pubsub.v1.[TopicAdminClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) ; 
import com.google.iam.v1.[GetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import com.google.pubsub.v1.[TopicName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) ; 
import java.io.IOException ; 

public class GetTopicPolicyExample { 
public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String topicId = "your-topic-id" ; 

getTopicPolicyExample ( projectId , topicId ); 
} 

public static void getTopicPolicyExample ( String projectId , String topicId ) throws IOException { 
try ( [ TopicAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [ TopicAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) . create ()) { 
[ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) . of ( projectId , topicId ); 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) getIamPolicyRequest = 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) . newBuilder (). setResource ( topicName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__) ()). build (); 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = topicAdminClient . getIamPolicy ( getIamPolicyRequest ); 
System . out . println ( "Topic policy: " + policy ); 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment this variable before running the sample. 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID'; 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) (); 

async function getTopicPolicy ( topicNameOrId ) { 
// Retrieves the IAM policy for the topic 
const [ policy ] = await pubSubClient . topic ( topicNameOrId ). iam . [ getPolicy ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/iam.html) (); 
console . log ( 'Policy for topic: %j.' , policy . bindings ); 
} 
```








Before trying this sample, follow the PHP setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub PHP API reference documentation](https://berlin.devsitetest.how/php/docs/reference/cloud-pubsub/latest).























```
use Google\Cloud\PubSub\PubSubClient; 

/** 
* Prints the policy for a Pub/Sub topic. 
* 
* @param string $projectId The Google project ID. 
* @param string $topicName The Pub/Sub topic name. 
*/ 
function get_topic_policy($projectId, $topicName) 
{ 
$pubsub = new PubSubClient([ 
'projectId' => $projectId, 
]); 
$topic = $pubsub->topic($topicName); 
$policy = $topic->iam()->policy(); 
print_r($policy); 
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

client = pubsub_v1 . [ PublisherClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) () 
topic_path = client . topic_path ( project_id , topic_id ) 

policy = client . get_iam_policy ( request = { "resource" : topic_path }) 

print ( "Policy for topic {} :" . format ( topic_path )) 
for binding in policy . bindings : 
print ( "Role: {} , Members: {} " . format ( binding . role , binding . members )) 
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

policy = pubsub . [ iam ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) . get_iam_policy resource : pubsub . topic_path ( topic_id ) 

puts "Topic policy:" 
puts policy . bindings . first . role 
```






### Set a policy

The `setIamPolicy()` method lets you [attach a policy](/iam/docs/managing-policies)
to a resource. The `setIamPolicy()` method takes a `SetIamPolicyRequest`, which
contains the policy to be set and the resource to which the policy is attached.
It returns the resulting policy.

Here is some sample code to [set a policy for a subscription](/pubsub/docs/reference/rest/v1/projects.subscriptions/setIamPolicy):


[C#](#c) [gcloud](#gcloud) [Go](#go) [Java](#java) [Node.js](#node.js) [PHP](#php) [Python](#python) [Ruby](#ruby) 
More 






Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.Iam.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html) ; 
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 

public class SetSubscriptionIamPolicySample 
{ 
public Policy SetSubscriptionIamPolicy ( string projectId , string subscriptionId , string role , string member ) 
{ 
[ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create) (); 
string roleToBeAddedToPolicy = $"roles/{role}" ; 

[ Policy ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) policy = new [ Policy ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)
{ 
Bindings = { 
new [ Binding ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Binding.html)
{ 
Role = roleToBeAddedToPolicy , 
Members = { member } 
} 
} 
}; 
[ SetIamPolicyRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html) request = new [ SetIamPolicyRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)
{ 
ResourceAsResourceName = [ SubscriptionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) . [ FromProjectSubscription ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_) ( projectId , subscriptionId ), 
Policy = policy 
}; 
[ Policy ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) response = publisher . [ IAMPolicyClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_IAMPolicyClient) . SetIamPolicy ( request ); 
return response ; 
} 
} 
```






1. Save the policy for the subscription.


```
gcloud pubsub subscriptions get-iam-policy \
projects/ ${ PROJECT } /subscriptions/ ${ SUBSCRIPTION } \
--format json > subscription_policy.json
```



2. Open `subscription_policy.json` and update bindings by giving appropriate roles to appropriate principals.
For more information about working with `subscription_policy.json` files, see [
Policy](/iam/reference/rest/v1/Policy) in the IAM documentation.


```
{ 
"etag" : "BwUjMhCsNvY=" , 
"bindings" : [ 
{ 
"role" : "roles/pubsub.admin" , 
"members" : [ 
"user:user-1@gmail.com" 
] 
}, 
{ 
"role" : "roles/pubsub.editor" , 
"members" : [ 
"serviceAccount:service-account-2@appspot.eu0-system.iam.gserviceaccount.com" 
] 
} 
] 
} 
```



3. Apply the new subscription policy.


```
gcloud pubsub subscriptions set-iam-policy \
projects/ ${ PROJECT } /subscriptions/ ${ SUBSCRIPTION } \
subscription_policy.json
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

"cloud.google.com/go/iam/apiv1/iampb" 
"cloud.google.com/go/pubsub/v2" 
) 

func addUsersToSubscription ( w io . Writer , projectID , subID string ) error { 
// projectID := "my-project-id" 
// subID := "my-sub" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 
defer client . Close () 

subName := fmt . Sprintf ( "projects/%s/subscriptions/%s" , projectID , subID ) 
req := & iampb . [ GetIamPolicyRequest ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest) { 
Resource : subName , 
} 
policy , err := client . SubscriptionAdminClient . [ GetIamPolicy ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_GetIamPolicy) ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "error calling GetIamPolicy: %w" , err ) 
} 
b := & iampb . [ Binding ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_Binding) { 
Role : "roles/editor" , 
// Other valid prefixes are "serviceAccount:", "user:" 
// See the documentation for more values. 
Members : [] string { "group:cloud-logs@google.com" }, 
} 
policy . Bindings = append ( policy . Bindings , b ) 

setRequest := & iampb . [ SetIamPolicyRequest ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_SetIamPolicyRequest) { 
Resource : subName , 
Policy : policy , 
} 
_ , err = client . SubscriptionAdminClient . [ SetIamPolicy ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_SetIamPolicy) ( ctx , setRequest ) 
if err != nil { 
return fmt . Errorf ( "error calling SetIamPolicy: %w" , err ) 
} 
fmt . Fprintln ( w , "Added roles to subscription." ) 
return nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) ; 
import com.google.iam.v1.[Binding](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) ; 
import com.google.iam.v1.[GetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import com.google.iam.v1.[SetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) ; 
import com.google.pubsub.v1.[ProjectSubscriptionName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) ; 
import java.io.IOException ; 

public class SetSubscriptionPolicyExample { 
public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String subscriptionId = "your-subscription-id" ; 

setSubscriptionPolicyExample ( projectId , subscriptionId ); 
} 

public static void setSubscriptionPolicyExample ( String projectId , String subscriptionId ) 
throws IOException { 
try ( [ SubscriptionAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [ SubscriptionAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) . create ()) { 
[ ProjectSubscriptionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName = 
[ ProjectSubscriptionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) . of ( projectId , subscriptionId ); 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) getIamPolicyRequest = 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) . newBuilder (). setResource ( subscriptionName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__) ()). build (); 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) oldPolicy = subscriptionAdminClient . getIamPolicy ( getIamPolicyRequest ); 

// Create new role -> members binding 
[ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = 
[ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) . newBuilder () 
. setRole ( "roles/pubsub.editor" ) 
. [ addMembers ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_) ( "domain:google.com" ) 
. build (); 

// Add new binding to updated policy 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . newBuilder ( oldPolicy ). [ addBindings ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_) ( binding ). build (); 

[ SetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) setIamPolicyRequest = 
[ SetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) . newBuilder () 
. setResource ( subscriptionName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__) ()) 
. [ setPolicy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_) ( updatedPolicy ) 
. build (); 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) newPolicy = subscriptionAdminClient . setIamPolicy ( setIamPolicyRequest ); 
System . out . println ( "New subscription policy: " + newPolicy ); 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment this variable before running the sample. 
*/ 
// const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID'; 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) (); 

async function setSubscriptionPolicy ( subscriptionNameOrId ) { 
// The new IAM policy 
const newPolicy = { 
bindings : [ 
{ 
// Add a group as editors 
role : 'roles/pubsub.editor' , 
members : [ 'group:cloud-logs@google.com' ], 
}, 
{ 
// Add all users as viewers 
role : 'roles/pubsub.viewer' , 
members : [ 'allUsers' ], 
}, 
], 
}; 

// Updates the IAM policy for the subscription 
const [ updatedPolicy ] = await pubSubClient 
. subscription ( subscriptionNameOrId ) 
. iam . [ setPolicy ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/iam.html) ( newPolicy ); 

console . log ( 'Updated policy for subscription: %j' , updatedPolicy . bindings ); 
} 
```



























```
use Google\Cloud\PubSub\PubSubClient; 

/** 
* Adds a user to the policy for a Pub/Sub subscription. 
* 
* @param string $projectId The Google project ID. 
* @param string $subscriptionName The Pub/Sub subscription name. 
* @param string $userEmail The user email to add to the policy. 
*/ 
function set_subscription_policy($projectId, $subscriptionName, $userEmail) 
{ 
$pubsub = new PubSubClient([ 
'projectId' => $projectId, 
]); 
$subscription = $pubsub->subscription($subscriptionName); 
$policy = $subscription->iam()->policy(); 
$policy['bindings'][] = [ 
'role' => 'roles/pubsub.subscriber', 
'members' => ['user:' . $userEmail] 
]; 
$subscription->iam()->setPolicy($policy); 

printf( 
'User %s added to policy for %s' . PHP_EOL, 
$userEmail, 
$subscriptionName 
); 
} 
```








Before trying this sample, follow the Python setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Python API reference documentation](/python/docs/reference/pubsub/latest).























```
from google.cloud import pubsub_v1 

# TODO(developer): Choose an existing subscription. 
# project_id = "your-project-id" 
# subscription_id = "your-subscription-id" 

client = pubsub_v1 . [ SubscriberClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html) () 
subscription_path = client . subscription_path ( project_id , subscription_id ) 

policy = client . get_iam_policy ( request = { "resource" : subscription_path }) 

# Add all users as viewers. 
policy . bindings . add ( role = "roles/pubsub.viewer" , members = [ "domain:google.com" ]) 

# Add a group as an editor. 
policy . bindings . add ( role = "roles/editor" , members = [ "group:cloud-logs@google.com" ]) 

# Set the policy 
policy = client . set_iam_policy ( 
request = { "resource" : subscription_path , "policy" : policy } 
) 

print ( "IAM policy for subscription {} set: {} " . format ( subscription_id , policy )) 

client . [ close ](https://berlin.devsitetest.how/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client.html#google_cloud_pubsub_v1_subscriber_client_Client_close) () 
```






The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see
[ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md).
To see a list of Ruby v2 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html).






















```
# subscription_id = "your-subscription-id" 
# role = "roles/pubsub.subscriber" 
# service_account_email = 
# "serviceAccount:account_name@project_name.iam.gserviceaccount.com" 

pubsub = Google :: Cloud :: [ PubSub ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)

bindings = Google :: Iam :: [ V1 ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1.html) :: Binding . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) \ 
role : role , 
members : [ service_account_email ] 

pubsub . [ iam ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) . set_iam_policy resource : pubsub . subscription_path ( subscription_id ), 
policy : { 
bindings : [ bindings ] 
} 
```






Here is some sample code to [set a policy for a topic](/pubsub/docs/reference/rest/v1/projects.topics/setIamPolicy):


[C#](#c) [gcloud](#gcloud) [Go](#go) [Java](#java) [Node.js](#node.js) [PHP](#php) [Python](#python) [Ruby](#ruby) 
More 






Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.Iam.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html) ; 
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 

public class SetTopicIamPolicySample 
{ 
public Policy SetTopicIamPolicy ( string projectId , string topicId , string role , string member ) 
{ 
[ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create) (); 
string roleToBeAddedToPolicy = $"roles/{role}" ; 

[ Policy ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) policy = new [ Policy ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)
{ 
Bindings = { 
new [ Binding ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Binding.html)
{ 
Role = roleToBeAddedToPolicy , 
Members = { member } 
} 
} 
}; 
[ SetIamPolicyRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html) request = new [ SetIamPolicyRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)
{ 
ResourceAsResourceName = [ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) . [ FromProjectTopic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_) ( projectId , topicId ), 
Policy = policy 
}; 
[ Policy ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) response = publisher . [ IAMPolicyClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_IAMPolicyClient) . SetIamPolicy ( request ); 
return response ; 
} 
} 
```






1. Save the policy for the topic.


```
gcloud pubsub topics get-iam-policy \
projects/ ${ PROJECT } /topics/ ${ TOPIC } \
--format json > topic_policy.json
```


2. Open `topic_policy.json` and update bindings by giving appropriate roles to appropriate principals.
For more information about working with `subscription_policy.json` files, see [
Policy](/iam/reference/rest/v1/Policy) in the IAM documentation.



```
{ 
"etag" : "BwUjMhCsNvY=" , 
"bindings" : [ 
{ 
"role": "roles/pubsub.editor", 
"members": [ 
"user:user-1@gmail.com", 
"user:user-2@gmail.com" 
] 
} 
] 
} 
```


3. Apply the new topic policy.


```
gcloud pubsub topics set-iam-policy \
projects/ ${ PROJECT } /topics/ ${ TOPIC } \
topic_policy.json
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

"cloud.google.com/go/iam/apiv1/iampb" 
"cloud.google.com/go/pubsub/v2" 
) 

func addUsersToTopic ( w io . Writer , projectID , topicID string ) error { 
// projectID := "my-project-id" 
// topicID := "my-topic" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 
defer client . Close () 

topicName := fmt . Sprintf ( "projects/%s/topics/%s" , projectID , topicID ) 
req := & iampb . [ GetIamPolicyRequest ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest) { 
Resource : topicName , 
} 
policy , err := client . TopicAdminClient . [ GetIamPolicy ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_GetIamPolicy) ( ctx , req ) 
if err != nil { 
return fmt . Errorf ( "error calling GetIamPolicy: %w" , err ) 
} 
b := & iampb . [ Binding ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_Binding) { 
Role : "roles/editor" , 
// Other valid prefixes are "serviceAccount:", "user:" 
// See the documentation for more values. 
Members : [] string { "group:cloud-logs@google.com" }, 
} 
policy . Bindings = append ( policy . Bindings , b ) 

setRequest := & iampb . [ SetIamPolicyRequest ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_SetIamPolicyRequest) { 
Resource : topicName , 
Policy : policy , 
} 
_ , err = client . TopicAdminClient . [ SetIamPolicy ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_SetIamPolicy) ( ctx , setRequest ) 
if err != nil { 
return fmt . Errorf ( "error calling SetIamPolicy: %w" , err ) 
} 
fmt . Fprintln ( w , "Added roles to topic." ) 
return nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.cloud.pubsub.v1.[TopicAdminClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) ; 
import com.google.iam.v1.[Binding](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) ; 
import com.google.iam.v1.[GetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import com.google.iam.v1.[SetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) ; 
import com.google.pubsub.v1.[TopicName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) ; 
import java.io.IOException ; 

public class SetTopicPolicyExample { 
public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String topicId = "your-topic-id" ; 

setTopicPolicyExample ( projectId , topicId ); 
} 

public static void setTopicPolicyExample ( String projectId , String topicId ) throws IOException { 
try ( [ TopicAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [ TopicAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) . create ()) { 
[ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [ TopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) . of ( projectId , topicId ); 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) getIamPolicyRequest = 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) . newBuilder (). setResource ( topicName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__) ()). build (); 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) oldPolicy = topicAdminClient . getIamPolicy ( getIamPolicyRequest ); 

// Create new role -> members binding 
[ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = 
[ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) . newBuilder () 
. setRole ( "roles/pubsub.editor" ) 
. [ addMembers ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_) ( "domain:google.com" ) 
. build (); 

// Add new binding to updated policy 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . newBuilder ( oldPolicy ). [ addBindings ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_) ( binding ). build (); 

[ SetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) setIamPolicyRequest = 
[ SetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) . newBuilder () 
. setResource ( topicName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__) ()) 
. [ setPolicy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_) ( updatedPolicy ) 
. build (); 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) newPolicy = topicAdminClient . setIamPolicy ( setIamPolicyRequest ); 
System . out . println ( "New topic policy: " + newPolicy ); 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment this variable before running the sample. 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID'; 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) (); 

async function setTopicPolicy ( topicNameOrId ) { 
// The new IAM policy 
const newPolicy = { 
bindings : [ 
{ 
// Add a group as editors 
role : 'roles/pubsub.editor' , 
members : [ 'group:cloud-logs@google.com' ], 
}, 
{ 
// Add all users as viewers 
role : 'roles/pubsub.viewer' , 
members : [ 'allUsers' ], 
}, 
], 
}; 

// Updates the IAM policy for the topic 
const [ updatedPolicy ] = await pubSubClient 
. topic ( topicNameOrId ) 
. iam . [ setPolicy ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/iam.html) ( newPolicy ); 
console . log ( 'Updated policy for topic: %j' , updatedPolicy . bindings ); 
} 
```



























```
use Google\Cloud\PubSub\PubSubClient; 

/** 
* Adds a user to the policy for a Pub/Sub topic. 
* 
* @param string $projectId The Google project ID. 
* @param string $topicName The Pub/Sub topic name. 
* @param string $userEmail The user email to add to the policy. 
*/ 
function set_topic_policy($projectId, $topicName, $userEmail) 
{ 
$pubsub = new PubSubClient([ 
'projectId' => $projectId, 
]); 
$topic = $pubsub->topic($topicName); 
$policy = $topic->iam()->policy(); 
$policy['bindings'][] = [ 
'role' => 'roles/pubsub.publisher', 
'members' => ['user:' . $userEmail] 
]; 
$topic->iam()->setPolicy($policy); 

printf( 
'User %s added to policy for %s' . PHP_EOL, 
$userEmail, 
$topicName 
); 
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

client = pubsub_v1 . [ PublisherClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) () 
topic_path = client . topic_path ( project_id , topic_id ) 

policy = client . get_iam_policy ( request = { "resource" : topic_path }) 

# Add all users as viewers. 
policy . bindings . add ( role = "roles/pubsub.viewer" , members = [ "domain:google.com" ]) 

# Add a group as a publisher. 
policy . bindings . add ( 
role = "roles/pubsub.publisher" , members = [ "group:cloud-logs@google.com" ] 
) 

# Set the policy 
policy = client . set_iam_policy ( request = { "resource" : topic_path , "policy" : policy }) 

print ( "IAM policy for topic {} set: {} " . format ( topic_id , policy )) 
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
# role = "roles/pubsub.publisher" 
# service_account_email = 
# "serviceAccount:account_name@project_name.iam.gserviceaccount.com" 

pubsub = Google :: Cloud :: [ PubSub ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)

bindings = Google :: Iam :: [ V1 ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1.html) :: Binding . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) \ 
role : role , 
members : [ service_account_email ] 

pubsub . [ iam ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) . set_iam_policy resource : pubsub . topic_path ( topic_id ), 
policy : { 
bindings : [ bindings ] 
} 
```






### Test permissions

You can use the `testIamPermissions()` method to check which of the given
permissions can be added or removed for the given resource. It takes
as parameters a resource name and a set of permissions, and returns the subset
of permissions.

Here is some sample code to [test permissions for a subscription](/pubsub/docs/reference/rest/v1/projects.topics/testIamPermissions):


[C#](#c) [gcloud](#gcloud) [Go](#go) [Java](#java) [Node.js](#node.js) [PHP](#php) [Python](#python) [Ruby](#ruby) 
More 






Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.Iam.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html) ; 
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 

public class TestSubscriptionIamPermissionsSample 
{ 
public TestIamPermissionsResponse TestSubscriptionIamPermissionsResponse ( string projectId , string subscriptionId ) 
{ 
[ TestIamPermissionsRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html) request = new [ TestIamPermissionsRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)
{ 
ResourceAsResourceName = [ SubscriptionName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) . [ FromProjectSubscription ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_) ( projectId , subscriptionId ), 
Permissions = { "pubsub.subscriptions.get" , "pubsub.subscriptions.update" } 
}; 
[ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create) (); 
[ TestIamPermissionsResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html) response = publisher . [ IAMPolicyClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_IAMPolicyClient) . TestIamPermissions ( request ); 
return response ; 
} 
} 
```





```
gcloud iam list-testable-permissions \
https://pubsub.googleapis.com/v1/projects/${PROJECT}/subscriptions/${SUBSCRIPTION} \
--format json
```


Output:


```
[
{
"name": "pubsub.subscriptions.consume",
"stage": "GA"
},
{
"name": "pubsub.subscriptions.delete",
"stage": "GA"
},
{
"name": "pubsub.subscriptions.get",
"stage": "GA"
},
{
"name": "pubsub.subscriptions.getIamPolicy",
"stage": "GA"
},
{
"name": "pubsub.subscriptions.setIamPolicy",
"stage": "GA"
},
{
"name": "pubsub.subscriptions.update",
"stage": "GA"
}
]
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

"cloud.google.com/go/iam/apiv1/iampb" 
"cloud.google.com/go/pubsub/v2" 
) 

func testPermissions ( w io . Writer , projectID , subID string ) ([] string , error ) { 
// projectID := "my-project-id" 
// subID := "my-sub" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return nil , fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 

req := & iampb . [ TestIamPermissionsRequest ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsRequest) { 
Resource : fmt . Sprintf ( "projects/%s/subscriptions/%s" , projectID , subID ), 
Permissions : [] string { 
"pubsub.subscriptions.consume" , 
"pubsub.subscriptions.update" , 
}, 
} 
resp , err := client . SubscriptionAdminClient . [ TestIamPermissions ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_TestIamPermissions) ( ctx , req ) 
if err != nil { 
return nil , fmt . Errorf ( "error calling TestIamPermissions: %w" , err ) 
} 
for _ , perm := range resp . Permissions { 
fmt . Fprintf ( w , "Allowed: %v\n" , perm ) 
} 
return resp . Permissions , nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) ; 
import com.google.iam.v1.[TestIamPermissionsRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html) ; 
import com.google.iam.v1.[TestIamPermissionsResponse](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsResponse.html) ; 
import com.google.pubsub.v1.[ProjectSubscriptionName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) ; 
import java.io.IOException ; 
import java.util.LinkedList ; 
import java.util.List ; 

public class TestSubscriptionPermissionsExample { 
public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String subscriptionId = "your-subscription-id" ; 

testSubscriptionPermissionsExample ( projectId , subscriptionId ); 
} 

public static void testSubscriptionPermissionsExample ( String projectId , String subscriptionId ) 
throws IOException { 
try ( [ SubscriptionAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [ SubscriptionAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) . create ()) { 
[ ProjectSubscriptionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName = 
[ ProjectSubscriptionName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) . of ( projectId , subscriptionId ); 

List permissions = new LinkedList <> (); 
permissions . add ( "pubsub.subscriptions.consume" ); 
permissions . add ( "pubsub.subscriptions.update" ); 

[ TestIamPermissionsRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html) testIamPermissionsRequest = 
[ TestIamPermissionsRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html) . newBuilder () 
. setResource ( subscriptionName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__) ()) 
. addAllPermissions ( permissions ) 
. build (); 

[ TestIamPermissionsResponse ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsResponse.html) testedPermissionsResponse = 
subscriptionAdminClient . testIamPermissions ( testIamPermissionsRequest ); 

System . out . println ( "Tested:\n" + testedPermissionsResponse ); 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment this variable before running the sample. 
*/ 
// const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID'; 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) (); 

async function testSubscriptionPermissions ( subscriptionNameOrId ) { 
const permissionsToTest = [ 
'pubsub.subscriptions.consume' , 
'pubsub.subscriptions.update' , 
]; 

// Tests the IAM policy for the specified subscription 
const [ permissions ] = await pubSubClient 
. subscription ( subscriptionNameOrId ) 
. iam . [ testPermissions ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/iam.html) ( permissionsToTest ); 

console . log ( 'Tested permissions for subscription: %j' , permissions ); 
} 
```








Before trying this sample, follow the PHP setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub PHP API reference documentation](https://berlin.devsitetest.how/php/docs/reference/cloud-pubsub/latest).























```
use Google\Cloud\PubSub\PubSubClient; 

/** 
* Prints the permissions of a subscription. 
* 
* @param string $projectId The Google project ID. 
* @param string $subscriptionName The Pub/Sub subscription name. 
*/ 
function test_subscription_permissions($projectId, $subscriptionName) 
{ 
$pubsub = new PubSubClient([ 
'projectId' => $projectId, 
]); 
$subscription = $pubsub->subscription($subscriptionName); 
$permissions = $subscription->iam()->testPermissions([ 
'pubsub.subscriptions.consume', 
'pubsub.subscriptions.update' 
]); 
foreach ($permissions as $permission) { 
printf('Permission: %s' . PHP_EOL, $permission); 
} 
} 
```








Before trying this sample, follow the Python setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Python API reference documentation](/python/docs/reference/pubsub/latest).























```
from google.cloud import pubsub_v1 

# TODO(developer): Choose an existing subscription. 
# project_id = "your-project-id" 
# subscription_id = "your-subscription-id" 

client = pubsub_v1 . [ SubscriberClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html) () 
subscription_path = client . subscription_path ( project_id , subscription_id ) 

permissions_to_check = [ 
"pubsub.subscriptions.consume" , 
"pubsub.subscriptions.update" , 
] 

allowed_permissions = client . test_iam_permissions ( 
request = { "resource" : subscription_path , "permissions" : permissions_to_check } 
) 

print ( 
"Allowed permissions for subscription {} : {} " . format ( 
subscription_path , allowed_permissions 
) 
) 

client . [ close ](https://berlin.devsitetest.how/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client.html#google_cloud_pubsub_v1_subscriber_client_Client_close) () 
```






The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see
[ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md).
To see a list of Ruby v2 code samples, see [
the deprecated code samples](/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html).






















```
# subscription_id = "your-subscription-id" 

pubsub = Google :: Cloud :: [ PubSub ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
subscription_admin = pubsub . [ subscription_admin ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
permissions = [ "pubsub.subscriptions.consume" , "pubsub.subscriptions.update" ] 

response = pubsub . [ iam ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) . test_iam_permissions \ 
resource : pubsub . subscription_path ( subscription_id ), 
permissions : permissions 

puts "Permission to consume" \ 
if response . permissions . include? "pubsub.subscriptions.consume" 
puts "Permission to update" \ 
if response . permissions . include? "pubsub.subscriptions.update" 
```






Here is some sample code to [test permissions for a topic](/pubsub/docs/reference/rest/v1/projects.topics/testIamPermissions):


[C#](#c) [gcloud](#gcloud) [Go](#go) [Java](#java) [Node.js](#node.js) [PHP](#php) [Python](#python) [Ruby](#ruby) 
More 






Before trying this sample, follow the C# setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub C# API reference documentation](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest).























```
using [ Google.Cloud.Iam.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html) ; 
using [ Google.Cloud.PubSub.V1 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html) ; 

public class TestTopicIamPermissionsSample 
{ 
public TestIamPermissionsResponse TestTopicIamPermissions ( string projectId , string topicId ) 
{ 
[ TestIamPermissionsRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html) request = new [ TestIamPermissionsRequest ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)
{ 
ResourceAsResourceName = [ TopicName ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) . [ FromProjectTopic ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_) ( projectId , topicId ), 
Permissions = { "pubsub.topics.get" , "pubsub.topics.update" } 
}; 
[ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [ PublisherServiceApiClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create) (); 
[ TestIamPermissionsResponse ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html) response = publisher . [ IAMPolicyClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_IAMPolicyClient) . TestIamPermissions ( request ); 
return response ; 
} 
} 
```





```
gcloud iam list-testable-permissions \
https://pubsub.googleapis.com/v1/projects/${PROJECT}/topics/${TOPIC} \
--format json
```


Output


```
[
{
"name": "pubsub.topics.attachSubscription",
"stage": "GA"
},
{
"name": "pubsub.topics.delete",
"stage": "GA"
},
{
"name": "pubsub.topics.detachSubscription",
"stage": "GA"
},
{
"name": "pubsub.topics.get",
"stage": "GA"
},
{
"name": "pubsub.topics.getIamPolicy",
"stage": "GA"
},
{
"name": "pubsub.topics.publish",
"stage": "GA"
},
{
"name": "pubsub.topics.setIamPolicy",
"stage": "GA"
},
{
"name": "pubsub.topics.update",
"stage": "GA"
}
]
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

"cloud.google.com/go/iam/apiv1/iampb" 
"cloud.google.com/go/pubsub/v2" 
) 

func testPermissions ( w io . Writer , projectID , topicID string ) ([] string , error ) { 
// projectID := "my-project-id" 
// topicID := "my-topic" 
ctx := context . Background () 
client , err := pubsub . NewClient ( ctx , projectID ) 
if err != nil { 
return nil , fmt . Errorf ( "pubsub.NewClient: %w" , err ) 
} 

req := & iampb . [ TestIamPermissionsRequest ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsRequest) { 
Resource : fmt . Sprintf ( "projects/%s/topics/%s" , projectID , topicID ), 
Permissions : [] string { 
"pubsub.topics.publish" , 
"pubsub.topics.update" , 
}, 
} 
resp , err := client . TopicAdminClient . [ TestIamPermissions ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_TestIamPermissions) ( ctx , req ) 
if err != nil { 
return nil , fmt . Errorf ( "error calling TestIamPermissions: %w" , err ) 
} 
for _ , perm := range resp . Permissions { 
fmt . Fprintf ( w , "Allowed: %v\n" , perm ) 
} 
return resp . Permissions , nil 
} 
```








Before trying this sample, follow the Java setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Java API reference documentation](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/overview).























```
import com.google.cloud.pubsub.v1.[TopicAdminClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) ; 
import com.google.iam.v1.[TestIamPermissionsRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html) ; 
import com.google.iam.v1.[TestIamPermissionsResponse](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsResponse.html) ; 
import com.google.pubsub.v1.[ProjectTopicName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) ; 
import java.io.IOException ; 
import java.util.LinkedList ; 
import java.util.List ; 

public class TestTopicPermissionsExample { 

public static void main ( String ... args ) throws Exception { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "your-project-id" ; 
String topicId = "your-topic-id" ; 

testTopicPermissionsExample ( projectId , topicId ); 
} 

public static void testTopicPermissionsExample ( String projectId , String topicId ) 
throws IOException { 
try ( [ TopicAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [ TopicAdminClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) . create ()) { 
[ ProjectTopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) topicName = [ ProjectTopicName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) . of ( projectId , topicId ); 

List permissions = new LinkedList <> (); 
permissions . add ( "pubsub.topics.attachSubscription" ); 
permissions . add ( "pubsub.topics.publish" ); 
permissions . add ( "pubsub.topics.update" ); 

[ TestIamPermissionsRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html) testIamPermissionsRequest = 
[ TestIamPermissionsRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html) . newBuilder () 
. setResource ( topicName . [ toString ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html#com_google_pubsub_v1_ProjectTopicName_toString__) ()) 
. addAllPermissions ( permissions ) 
. build (); 

[ TestIamPermissionsResponse ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsResponse.html) testedPermissionsResponse = 
topicAdminClient . testIamPermissions ( testIamPermissionsRequest ); 

System . out . println ( "Tested:\n" + testedPermissionsResponse ); 
} 
} 
} 
```








Before trying this sample, follow the Node.js setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest).























```
/** 
* TODO(developer): Uncomment this variable before running the sample. 
*/ 
// const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID'; 

// Imports the Google Cloud client library 
const { PubSub } = require ( '[@google-cloud/pubsub](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/overview.html)' ); 

// Creates a client; cache this for further use 
const pubSubClient = new [ PubSub ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html) (); 

async function testTopicPermissions ( topicNameOrId ) { 
const permissionsToTest = [ 
'pubsub.topics.attachSubscription' , 
'pubsub.topics.publish' , 
'pubsub.topics.update' , 
]; 

// Tests the IAM policy for the specified topic 
const [ permissions ] = await pubSubClient 
. topic ( topicNameOrId ) 
. iam . [ testPermissions ](https://berlin.devsitetest.how/nodejs/docs/reference/pubsub/latest/pubsub/iam.html) ( permissionsToTest ); 

console . log ( 'Tested permissions for topic: %j' , permissions ); 
} 
```








Before trying this sample, follow the PHP setup instructions in
[Quickstart: Using Client Libraries](/pubsub/docs/create-topic-client-libraries).
For more information, see the [Pub/Sub PHP API reference documentation](https://berlin.devsitetest.how/php/docs/reference/cloud-pubsub/latest).























```
use Google\Cloud\PubSub\PubSubClient; 

/** 
* Prints the permissions of a topic. 
* 
* @param string $projectId The Google project ID. 
* @param string $topicName The Pub/Sub topic name. 
*/ 
function test_topic_permissions($projectId, $topicName) 
{ 
$pubsub = new PubSubClient([ 
'projectId' => $projectId, 
]); 
$topic = $pubsub->topic($topicName); 
$permissions = $topic->iam()->testPermissions([ 
'pubsub.topics.attachSubscription', 
'pubsub.topics.publish', 
'pubsub.topics.update' 
]); 
foreach ($permissions as $permission) { 
printf('Permission: %s' . PHP_EOL, $permission); 
} 
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

client = pubsub_v1 . [ PublisherClient ](https://berlin.devsitetest.how/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html) () 
topic_path = client . topic_path ( project_id , topic_id ) 

permissions_to_check = [ "pubsub.topics.publish" , "pubsub.topics.update" ] 

allowed_permissions = client . test_iam_permissions ( 
request = { "resource" : topic_path , "permissions" : permissions_to_check } 
) 

print ( 
"Allowed permissions for topic {} : {} " . format ( topic_path , allowed_permissions ) 
) 
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
topic_admin = pubsub . [ topic_admin ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
permissions = [ "pubsub.topics.attachSubscription" , "pubsub.topics.publish" , 
"pubsub.topics.update" ] 

response = pubsub . [ iam ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) . test_iam_permissions \ 
resource : pubsub . topic_path ( topic_id ), 
permissions : permissions 

puts "Permission to attach subscription" \ 
if permissions . include? "pubsub.topics.attachSubscription" 
puts "Permission to publish" \ 
if response . permissions . include? "pubsub.topics.publish" 
puts "Permission to update" \ 
if response . permissions . include? "pubsub.topics.update" 
```






## Cross-project communication

Pub/Sub IAM is useful for fine-tuning access in
cross-project communication.

Suppose a service account in Cloud Project A wants to publish messages to a
topic in Cloud Project B. First, enable the Pub/Sub API
in Project A.

Second, grant the service account **Edit** permission in
Cloud Project B. However, this approach is often too coarse. You can use the
IAM API to achieve a more fine-grained level of access.



For example, this snippet uses the `setIamPolicy()` method in project-b and a prepared
`topic_policy.json` file to grant the service account
`foobar@` project-a `.eu0.iam.gserviceaccount.com` of project-a the publisher role on the topic
`projects/` project-b `/topics/` topic-b :


```
gcloud pubsub topics set-iam-policy \
projects/ project-b /topics/ topic-b \
topic_policy.json
```

Output:


```
Updated IAM policy for topic topic-b .
bindings:
- members:
- serviceAccount:foobar@ project-a .eu0.iam.gserviceaccount.com
role: roles/pubsub.publisher
etag: BwWGrQYX6R4=
```


## Partial availability behavior

Authorization checks depend on the IAM subsystem. In order to
offer consistently low response latency for data operations (publishing and
message consumption), the system may fall back on cached IAM
policies. For information about when your changes will take effect, see the
[IAM documentation](/iam).

## What's Next

- If you are having issues accessing or authenticating Pub/Sub resources,
see [General troubleshooting](/pubsub/docs/troubleshooting).