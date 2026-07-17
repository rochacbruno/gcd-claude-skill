# Quickstart: Publish and receive messages in Pub/Sub by using the gcloud CLI

Source: https://berlin.devsitetest.how/pubsub/docs/publish-receive-messages-gcloud
Last updated: 2026-07-17

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

















- On this page 
- [ Before you begin ](#before-you-begin)

- [ Set up your project ](#project_setup)
- [ Required roles ](#required_roles)

- [ Create a topic ](#create_a_topic)
- [ Create a subscription ](#create_a_subscription)
- [ Publish messages ](#publish_messages)
- [ Receive messages ](#receive_messages)
- [ How did it go? ](#how-did-it-go)
- [ What's next ](#whats-next)
- 










# Publish and receive messages in Pub/ Sub by using the gcloud CLI 




This page shows you how to do the following operations in Pub/Sub using the Google Cloud CLI:

- Create a topic and subscription.

- Publish messages to the topic.

- Receive messages from the subscription.





## Before you begin 



Complete the following steps before running your quickstart.

### Set up your project















- 

Set up a Google Cloud Dedicated console project.

Set up a project 


Click to:

- Create or select a project.
- 


Enable the Pub/Sub API for that project.




You can view and manage these resources at any time in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/).
















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).







- 


To [initialize](/sdk/docs/initializing) the gcloud CLI, run the following command:



```
gcloud init
```


























### Required roles

To complete this quickstart, you need the following Identity and Access Management (IAM)
(IAM) roles.


































To get the permissions that
you need to complete this quickstart,

ask your administrator to grant you the
[Pub/Sub Editor ](/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









## Create a topic

Create a topic with the ID `my-topic`:


```
gcloud pubsub topics create my-topic
```


## Create a subscription

Create a subscription with the ID `my-sub` and attach it to `my-topic`:


```
gcloud pubsub subscriptions create my-sub --topic = my-topic
```


## Publish messages

Publish a message to `my-topic`:


```
gcloud pubsub topics publish my-topic --message = "hello" 
```


## Receive messages

Receive the message from `my-sub`:


```
gcloud pubsub subscriptions pull my-sub --auto-ack
```


The gcloud CLI prints the message to the command line.

## How did it go?




It worked!





I got stuck.











## What's next



- 

See all the available
[gcloud CLI commands](/sdk/gcloud/reference/pubsub) for Pub/Sub

- 

Learn more about the Pub/Sub [concepts](/pubsub/docs/overview)
discussed in this page.

- 

Read the [basics of the Pub/Sub service](/pubsub/docs/pubsub-basics).

- 

Work through an [end-to-end example](/pubsub/docs/building-pubsub-messaging-system)
of a Pub/Sub system.

- 

Try another Pub/Sub quickstart that
uses [client libraries](/pubsub/docs/publish-receive-messages-client-library) 
or the [console](/pubsub/docs/publish-receive-messages-console).

- 

Learn how to create [topics](/pubsub/docs/create-topic) 
and publish [messages](/pubsub/docs/publisher).

- 

[Choose](/pubsub/docs/subscriber) a subscription type.

- 

Learn more about [Pub/Sub APIs](/pubsub/docs/reference/service_apis_overview).