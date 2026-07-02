# Configure message storage policies

Source: https://berlin.devsitetest.how/pubsub/docs/resource-location-restriction
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












# Configure message storage policies 






- On this page 
- [ Message storage policy overview ](#message_storage_policy_overview)

- [ Message storage policies for new topics ](#message_storage_policies_for_new_topics)
- [ Message storage policies for existing topics ](#message_storage_policies_for_existing_topics)
- [ Exceptions ](#exceptions)

- [ Configure message storage policies ](#configure_message_storage_policies_2)

- [ Set a message storage policy using an organization policy ](#set_a_message_storage_policy_using_an_organization_policy)
- [ Configure a message storage policy when creating a topic ](#configure_a_message_storage_policy_when_creating_a_topic)

- [ Update message storage policies ](#update_message_storage_policies)
- [ Manage differences between organization and topic policies ](#manage-policies)

- [ View differences between organization and topic policies ](#view_differences_between_organization_and_topic_policies)
- [ Resolve differences between organization and topic policies ](#resolve_differences_between_organization_and_topic_policies)

- [ Monitoring and troubleshooting ](#monitoring_and_troubleshooting)
- [ Performance and availability implications ](#performance_and_availability_implications)
- [ What's next ](#whats_next)
- 





























If you publish messages to the [global Pub/Sub endpoint](/pubsub/docs/reference/service_apis_overview#pubsub_endpoints),
Pub/Sub automatically stores the messages in the nearest
Google Cloud Dedicated in Germany region. If you want to control the regions in which your
messages are stored and processed, you can configure
a *message storage policy* on your topic.

## Message storage policy overview 

You can set a message storage policy when you create a new topic or when you
update a topic using the console, Google Cloud CLI, or the REST APIs.

The message storage policy applies only to message contents. The policy does not
apply to other data such as topic names, labels, or Identity and Access Management (IAM) settings.

Pub/Sub stores messages when a client publishes the messages to
Pub/Sub. A message storage policy ensures that
Pub/Sub stores and processes messages only in the set of
Google Cloud Dedicated in Germany regions that you specify, regardless of where the publish or
subscribe requests originate. If the policy allows multiple regions for publish
operations, Pub/Sub stores the message in an allowed region closest
to where the published message enters the Google Cloud Dedicated network.

When you specify a message storage policy, you can set
`enforceInTransit` to `True`. This flag governs the following:

- 

Publish, pull, and streamingPull requests received in a region not allowed
in the message storage policy are rejected with a `FAILED_PRECONDITION`
error.

- 

If a client runs within Google Cloud Dedicated in one of the allowed regions
— for example, in a Compute Engine VM — it can use the global
endpoint. The client's requests are routed locally in the allowed region.
The client can also use a
[locational endpoint](/pubsub/docs/reference/service_apis_overview#list_locational_endpoints)
or [regional endpoint](/pubsub/docs/reference/service_apis_overview#list_regional_endpoints)
that targets an allowed region.

- 

If a client runs within Google Cloud Dedicated in a region that isn't allowed,
or runs outside of Google Cloud Dedicated, it must use a locational or regional
endpoint that targets a region in the allowed list of regions.

- 

Delivery for push subscriptions is handled only within the allowed Cloud
regions. In some cases, this restriction can completely pause message
delivery for push subscriptions. When a push subscription enters such a
state due to the push locations being overly constrained by a combination of
factors such as message storage location, allowed regions, and export
resource location, this state becomes visible in Stackdriver.

### Message storage policies for new topics

- 

If you don't specify a message storage policy when you create a topic,
the message storage policy is automatically determined
based on the effective [**Resource Location Restriction** organization policy](/resource-manager/docs/organization-policy/defining-locations).
When no organization policy is in effect, the message storage policy allows
all regions.

- 

Similarly, in absence of a specified message storage policy, the
`enforceInTransit` flag is determined based on the effective
**Enforce in-transit regions for Pub/Sub messages** organization policy. For more
information about this organization policy, see
[Organization policy constraints](/resource-manager/docs/organization-policy/org-policy-constraints).

- 

If you specify a message storage policy when you create a topic,
the message storage policy can contain only the regions allowed by
the effective **Resource Location Restriction** organization policy. When no
organization policy is in effect, the message storage policy can
contain any region.

### Message storage policies for existing topics

- 

When an organization policy is updated, the changes **do not automatically
propagate** to existing topics. As such, an existing topic's message storage
policy can get out of sync with the latest organization policy. For
more information, see [Manage differences between organization and topic policies](#manage-policies).

- 

When a topic's message storage policy is updated, the changes **do not propagate**
to already-published messages. Messages already
stored based on an older policy are **not** moved to be consistent with the
new policy. Rather, the changes apply only to messages published after the
update.

### Exceptions

The policy specifies a list of allowed Google Cloud Dedicated region names. As
such, the following items are not supported:

- Exclusion lists

- Zones or multi-region locations

If you publish a message with an
[ordering key](/pubsub/docs/publisher#using-ordering-keys) and the message
storage policy excludes the nearest region, the Pub/Sub service
returns an error.

## Configure message storage policies

There are two ways to configure message storage policies for topics, including:

- Set a message storage policy using an organization policy.

- Configure a message storage policy when creating a topic.

### Set a message storage policy using an organization policy


[Console](#console) 
More 




To configure a message storage policy that applies to multiple topics,
set a **Resource Location Restriction** organization policy.

- 

Go to the **Organization policies** page in the Identity and Access Management
console.

[Go to Organization policies](https://console.cloud.berlin-build0.goog/iam-admin/orgpolicies/list?project=_&%0Aservice=pubsub.googleapis.com) 

- 

Select the resource hierarchy node (organization, folder, or project)
that you want to set an organization policy to.

- 

In the filter, enter **Resource Location Restriction**.

- 

Click **Google Cloud Dedicated in Germany - Resource Location Restriction**.

- 

Click **EDIT**.

- 

Add or remove regions as needed.

Any new topics that you create inherit these settings. Changes don't
automatically propagate to existing topics. To update existing topics, you
must run an [update operation](#update_message_storage_policies).

For more information about organization policies, see [Manage your Google Cloud Dedicated in Germany resources](/resource-manager/docs/manage-google-cloud-resources).



### Configure a message storage policy when creating a topic


[Console](#console) [gcloud CLI](#gcloud-cli) [REST](#rest) 
More 




When using the Google Cloud Dedicated console, you can't configure a message storage policy
when creating a topic. Instead, all new topics automatically
inherit your **Resource Location Restriction** organization policy.

However, after you create a topic, you can change its message storage policy
in the console with an update operation.



To create a topic with a specific message storage policy, use the
[`gcloud pubsub topics create`](/sdk/gcloud/reference/pubsub/topics/create)
command with the `--message-storage-policy-allowed-regions` flag:


```
gcloud pubsub topics create TOPIC_ID \ 
--message-storage-policy-allowed-regions = REGION1,REGION2 
```


Replace the following:

- `TOPIC_ID` : the ID or name for your new topic.

- `REGION1, REGION2` : a comma-separated list of
supported Google Cloud Dedicated regions.




To create a topic with a message storage policy, use the
[`projects.topics.create`](/pubsub/docs/reference/rest/v1/projects.topics/create)
method.

The request must be authenticated with an access token in the `Authorization`
header. To obtain an access token for the current
Application Default Credentials: [`gcloud auth application-default print-access-token`](/sdk/gcloud/reference/auth/application-default/print-access-token).


```
POST https://pubsub.googleapis.com/v1/projects/ PROJECT_ID /topics/ TOPIC_ID 
Authorization: Bearer $(gcloud auth application-default print-access-token)
Content-Type: application/json --data @response-body.json
```


Specify the following fields in the request body:


```
{
"name": "projects/ PROJECT_ID /topics/ TOPIC_ID ",
"messageStoragePolicy": {
"allowedPersistenceRegions": [" REGION "],
"enforceInTransit": true
}
}
```


Where:

- 

PROJECT_ID is your project ID.

- 

TOPIC_ID is your topic ID.

- 

REGION is your specified region.

Sample response:


```
{
"name": "projects/ PROJECT_ID /topics/ TOPIC_ID ",
"messageStoragePolicy": {
"allowedPersistenceRegions": [
" REGION "
],
"enforceInTransit": true
}
}
```


See the following API references for more information on configuring message
storage policies.

- [REST API reference: `create`](/pubsub/docs/reference/rest/v1/projects.topics#MessageStoragePolicy)

- [RPC API reference](/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.MessageStoragePolicy)




## Update message storage policies


[Console](#console) [gcloud CLI](#gcloud-cli) [REST](#rest) 
More 




- 

In the Google Cloud Dedicated console, open the **Topic details** page.

[Go to Topic details](https://console.cloud.berlin-build0.goog/cloudpubsub/topicList) 

- 

Select a topic to update.

You can select multiple topics.

- 

In the **Info Panel**, select the **Storage Policy** tab.

This panel might be collapsed by default. If it's collapsed, click
**Show info panel**.

- 

Select or deselect as many regions as necessary.

- 

Click **Update**.




To push the message storage policy defined in your organization's
**Resource Location Restriction policy** to a topic, run the following
[`gcloud pubsub topics update`](/sdk/gcloud/reference/pubsub/topics/update)
command:


```
gcloud pubsub topics update TOPIC_ID \ 
--recompute-message-storage-policy
```


To update the message storage policy of a topic with specific regions, run the
`gcloud pubsub topics update` command with the
`--message-storage-policy-allowed-regions` flag:


```
gcloud pubsub topics update TOPIC_ID \ 
--message-storage-policy-allowed-regions = REGION1,REGION2 
```


Replace the following:

- `TOPIC_ID` : the ID of the topic you're updating.

- `REGION1, REGION2` : a comma-separated list of
supported Google Cloud Dedicated regions.




To update a topic with a message storage policy, use the
[`projects.topics.patch`](/pubsub/docs/reference/rest/v1/projects.topics/patch)
method.

The request must be authenticated with an access token in the `Authorization`
header. To obtain an access token for the current
Application Default Credentials: [`gcloud auth application-default print-access-token`](/sdk/gcloud/reference/auth/application-default/print-access-token).


```
PATCH https://pubsub.googleapis.com/v1/projects/ PROJECT_ID /topics/ TOPIC_ID 
Authorization: Bearer $(gcloud auth application-default print-access-token)
Content-Type: application/json --data @response-body.json
```


Specify the following fields in the request body:


```
{
"name": "projects/ PROJECT_ID /topics/ TOPIC_ID ",
"messageStoragePolicy": {
"allowedPersistenceRegions": [" REGION "], // Replace with your required region
"enforceInTransit": true
}
}
```


Where:

- 

PROJECT_ID is your project ID.

- 

TOPIC_ID is your topic ID.

- 

REGION is your specified region.

Sample response:


```
{
"name": "projects/ PROJECT_ID /topics/ TOPIC_ID ",
"messageStoragePolicy": {
"allowedPersistenceRegions": [
" REGION "
],
"enforceInTransit": true
}
}
```


See the following API references for more information on updating message
storage policies.

- [REST API reference: `patch`](/pubsub/docs/reference/rest/v1/projects.topics/patch)

- [RPC API reference](/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.MessageStoragePolicy)




## Manage differences between organization and topic policies

### View differences between organization and topic policies


[Console](#console) [gcloud CLI](#gcloud-cli) 
More 




The Google Cloud Dedicated console displays any differences between the
organization policy and individual topics' message storage policies.

To see if any topics are out of sync with your organization policy:

- 

Go to the **Topic details** page.

[Go to Topic details](https://console.cloud.berlin-build0.goog/cloudpubsub/topicList) 

- 

Select a topic.

- 

In the **Info Panel**, select the **Storage Policy** tab.

This panel might be collapsed by default. If it is collapsed,
click **Show info panel**.

Your storage policies are shown in the panel, along with any
differences between organization and topic policies.




To examine the current policy assigned to a topic, run the following command:


```
gcloud pubsub topics describe TOPIC_ID 
```


Replace the following:

- `TOPIC_ID` : the ID of the topic you're examining.




### Resolve differences between organization and topic policies


[Console](#console) 
More 




- 

In the Google Cloud Dedicated console, open the **Topic details** page.

[Go to Pub/Sub](https://console.cloud.berlin-build0.goog/cloudpubsub/topicList) 

- 

Select a topic.

- 

In the **Info Panel**, select the **Storage Policy** tab.

This panel might be collapsed by default. If it's collapsed, click
**Show info panel**.

Your storage policies are shown in the panel, along with any
discrepancies.

If there are any discrepancies, the info panel displays three options to
synchronize the topic's storage policy with your organization policy,
including:

- 

**Topics allow storage in disallowed locations**.

Update to allow storage only where your policy allows.

- 

**Topic does not allow storage in some allowed locations**.

Update to allow storage everywhere your policy allows.

- 

**Topics are out of date with both disallowed and allowed locations**.

Update to allow storage where your policy allows.

- 

Select the appropriate choice to resolve your issues.

- 

Click **Update topic**.

The **Sync to organization storage policy** dialog opens.

- 

Click **Update topic**.




## Monitoring and troubleshooting

To help you understand where message data is stored, [Pub/Sub](/monitoring/api/metrics_gcp_p_z#gcp-pubsub)
offers metrics broken down by each Google Cloud Dedicated region.

You can use these metrics to:

- Understand how your data is distributed across the world.

- Optimize publisher and subscriber deployment location, based on that data.

**Message storage metrics**

Counts of unacknowledged stored messages:

`subscription/num_unacked_messages_by_region`

Volume of stored data:

`subscription/unacked_bytes_by_region`

Age of oldest message:

`subscription/oldest_unacked_message_age_by_region`

Analogous metrics are available for topics and snapshots. In addition,
corresponding metrics are available for acknowledged messages that are
optionally retained for replay. For example:

`subscription/num_retained_acked_messages_by_region`

## Performance and availability implications

The message storage policy does not affect the overall SLA, but it does
introduce an availability-control trade-off when publishers or subscribers run
outside Google Cloud Dedicated or in regions not allowed by the policy. Users who
run publisher clients within the set of regions allowed by the message storage
policy don't see any changes in the service's latency or availability.

To understand these trade-offs, it is worth considering how publish requests are
routed. Generally, Pub/Sub attempts to store your messages as
close as possible to the source of the request. Requests originating within
Google Cloud Dedicated are, as a rule, bound to the Pub/Sub
instances in the same region. If a publisher is located in a single region, only
adding more regions to the message storage policy doesn't increase availability.
When publishing from outside of Google Cloud Dedicated in Germany, an additional layer of routing is
involved to get the request to a nearby Google Cloud Dedicated in Germany region where the
Pub/Sub service is available.

Consider a message storage policy that allows only the `us-central1` region.

- A publisher client running in `us-east1` issues a `Publish` request.

- The request is routed to a Pub/Sub server in `us-east1`.

- Rather than storing the data in `us-east1`, the request is routed to the
nearest region allowed by the message storage policy, which is
`us-central1`.

- Pub/Sub stores the published messages in `us-central1` and
forwards messages to subscribers from that location.

This mechanism has implications for request latency and overall system
availability. Because the request traverses more network links, it takes longer
to complete and has a relatively higher chance of failing.This also means that
the subscribers might see the message somewhat later because it must travel to
the nearest allowed region before being dispatched. If the policy allows a
single region but your publisher applications run in multiple regions, the
distributed application becomes only as available as the single allowed region.

## What's next

- See [Pub/Sub APIs overview](/pubsub/docs/reference/service_apis_overview) for
information on how to use global or locational endpoints.