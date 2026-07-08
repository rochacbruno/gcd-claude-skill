# Quickstart: Publish and receive messages in Pub/Sub using the Google Cloud Dedicated console

Source: https://berlin.devsitetest.how/pubsub/docs/publish-receive-messages-console
Last updated: 2026-07-07

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

















- On this page ** 
- [ Before you begin ](#before-you-begin)
- [ Create a topic ](#create_a_topic)
- [ Add a second subscription ](#add_a_second_subscription)
- [ Publish a message to the topic ](#publish_a_message_to_the_topic)
- [ Pull the messages from the subscription ](#pull_the_messages_from_the_subscription)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Publish and receive messages in Pub/ Sub using the Google Cloud Dedicated console 




This page shows you how to perform basic tasks in Pub/Sub using the
Google Cloud Dedicated console.





## Before you begin 



















- 




In the Google Cloud Dedicated console, on the project selector page,
select or create a Google Cloud Dedicated project.




Roles required to select or create a project**





- 
**Select a project**: Selecting a project doesn't require a specific
IAM role—you can select any project that you've been
granted a role on.


- 
**Create a project**: To create a project, you need the Project Creator role
(`roles/resourcemanager.projectCreator`), which contains the
`resourcemanager.projects.create` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).












[Go to project selector](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)














- 



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the Pub/Sub API.






**Roles required to enable APIs**


To enable APIs, you need the Service Usage Admin IAM
role (`roles/serviceusage.serviceUsageAdmin`), which
contains the `serviceusage.services.enable` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=pubsub.googleapis.com)












- 




Make sure that you have the following role or roles on the project:

Pub/Sub Admin



#### Check for the roles





- 


In the Google Cloud Dedicated console, go to the **IAM** page.


[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project)


- 

Select the project.



- 


In the **Principal** column, find all rows that identify you or a group that
you're included in. To learn which groups you're included in, contact your
administrator.




- 
For all rows that specify or include you, check the **Role** column to see whether
the list of roles includes the required roles.





#### Grant the roles





- 


In the Google Cloud Dedicated console, go to the **IAM** page.





[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project)


- 

Select the project.



- 
Click person_add **Grant access**.


- 


In the **New principals** field, enter your user identifier.

This is typically the identifier for a user in a workforce identity pool. For details,
see [
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users), or contact your administrator.





- 
Click **Select a role**, then search for the role.

- 
To grant additional roles, click add **Add
another role** and add each additional role.


- 
Click **Save**.
























## Create a topic

- 

In the Google Cloud Dedicated console, go to the **Pub/Sub**
page.

[Go to Pub/Sub](https://console.cloud.berlin-build0.goog/cloudpubsub/topicList) 

- 

In the **Topics** page, click **Create topic** .

- 

In the window that opens, enter `MyTopic` in the **Topic ID** field.

Leave the default values for the remaining options, and then click **Create**.

You see the success message: `A new topic and a new subscription have been successfully created.`

You have just created a topic called `MyTopic` and an associated default subscription `MyTopic-sub`.

## Add a second subscription

To add a second subscription to the topic you just created, complete these steps:

- 

In the Google Cloud Dedicated console, go to the **Pub/Sub subscriptions** page.

[Go to Subscriptions](https://console.cloud.berlin-build0.goog/cloudpubsub/subscription/list) 

- 

In the **Subscriptions** page, click **Create subscription**.

- 

Enter `MySub` in the
**Subscription ID** field.

- 

For **Select a Cloud Pub/Sub topic**, select the `MyTopic` topic from the drop-down menu.

- 

Leave the default values for the remaining options.

- 

Click **Create** .

You see the success message: `Subscription successfully added.`

The `MySub` subscription is now attached to the topic
`MyTopic`. Pub/Sub delivers all messages sent to
`MyTopic` to the `MySub` and `MyTopic-sub` subscriptions.

## Publish a message to the topic

- 

In the Google Cloud Dedicated console, go to the **Pub/Sub topics**
page.

[Go to Topics](https://console.cloud.berlin-build0.goog/cloudpubsub/topicList) 

- 

Click the `MyTopic` topic.

- 

Click the
**Topics** 
page and click `MyTopic`.

- 

In the `MyTopic` page, click the **Messages** tab.

- 

Click
**Publish message** .

- 

In the **Message body** window, enter `Hello World`.

- 

Click **Publish** . A message displays at the bottom of the page that says "Message published" if the publish was successful.

## Pull the messages from the subscription

- 

In the Google Cloud Dedicated console, go to the **Pub/Sub subscriptions** page.

[Go to Subscriptions](https://console.cloud.berlin-build0.goog/cloudpubsub/subscription/list) 

- 

In the **Messages** tab, click **Pull**.

You should see the message that you just published. The message has
the data, `Hello World`, and the time when the message was
published.

When using the Google Cloud Dedicated console, an individual pull for a low
message volume can often return zero messages. If you do not see messages, click
**Pull** multiple times to issue multiple pull requests. This is not an issue
with the [Pub/Sub Client Libraries](/pubsub/docs/publish-receive-messages-client-library).






## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






If you no longer need the topic and subscription you created, you
can delete them.

To delete the topic and subscription, complete these steps:

- 

Go to the
**Topics** 
page.

- 

Check the checkbox next to `MyTopic` and click
**Delete** .

- 

Complete the steps in the confirmation window to permanently delete the
topic.

Or you can [delete the project](https://console.cloud.berlin-build0.goog/cloud-resource-manager) that you created.






## What's next



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
or the [Google Cloud CLI](/pubsub/docs/publish-receive-messages-gcloud).

- 

Learn how to create [topics](/pubsub/docs/create-topic) 
and publish [messages](/pubsub/docs/publisher).

- 

[Choose](/pubsub/docs/subscriber) or [create](/pubsub/docs/create-subscription) a subscription.

- 

Learn more about [Pub/Sub APIs](/pubsub/docs/reference/service_apis_overview).