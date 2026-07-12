# Create, modify, and delete zones

Source: https://berlin.devsitetest.how/dns/docs/zones
Last updated: 2026-07-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/dns/docs/tpc-differences) for more details.














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

Networking

](https://berlin.devsitetest.how/docs/networking)






- 








[

Cloud DNS

](https://berlin.devsitetest.how/dns/docs)






- 








[

Guides

](https://berlin.devsitetest.how/dns/docs/set-up-dns-records-domain-name)












# Create, modify, and delete zones 






- On this page ** 
- [ Before you begin ](#before_you_begin)
- [ Create managed zones ](#create_managed_zones)

- [ Create a private zone ](#create-private-zone)
- [ Create a zone with specific IAM permissions ](#iam-per-resource-zone)
- [ Create a Service Directory DNS zone ](#create-service-directory-zone)
- [ Create a forwarding zone ](#creating-forwarding-zones)
- [ Create a peering zone ](#peering-zones)
- [ Create a cross-project binding zone ](#create_a_cross-project_binding_zone)

- [ Update managed zones ](#update_managed_zones)

- [ Update labels ](#update_labels)

- [ List and describe managed zones ](#list_and_describe_managed_zones)

- [ List managed zones ](#list_managed_zones)
- [ Describe a managed zone ](#describe_a_managed_zone)

- [ Delete a managed zone ](#delete_a_managed_zone)
- [ What's next ](#whats_next)
- 










This page provides directions for creating, updating, listing, and deleting
Cloud DNS managed zones. Before you use this page, familiarize yourself with
the [Cloud DNS overview](/dns/docs/overview) and
[Key terms](/dns/docs/key-terms).


#### Permissions required for this task 


To perform this task, you must have been granted the following permissions
*or* the following IAM roles.

Permissions**


- `dns.managedZones.create` to create a managed zone

- `dns.managedZones.list` to list managed zones

- `dns.networks.bindPrivateDNSZone`

- `dns.networks.targetWithPeeringZone`

- `dns.gkeClusters.bindPrivateDNSZone`

- `dns.managedZones.update`

- `dns.managedZones.list`

- `dns.managedZones.patch`

- `dns.activePeeringZones.getZoneInfo`

- `dns.activePeeringZones.list`

- `dns.activePeeringZones.deactivate`


**Roles**


- `roles/dns.admin`

- `roles/dns.peer`



## Before you begin ** 

The Cloud DNS API requires that you create a Cloud DNS project and
enable the Cloud DNS API.

If you are creating an application that uses the REST API, you must also
create an OAuth 2.0 client ID.


- 
If you don't already have one, [sign up for a Google Account](https://accounts.google.com/SignUp).

- 
[
Enable the Cloud DNS API in the Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/start/api?id=dns&credential=client_key). You can
choose an existing Compute Engine or App Engine project, or you can
create a new project.


- If you need to make requests to the REST API, you need to create an

OAuth 2.0 ID. See
[Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849).



- In the project, note the following information that you need to input in
later steps:



- 

The client ID (`xxxxxx.apps.googleusercontent.com`).



- 
The project ID that you want to use. You can find the ID at the
top of the Overview** page in the
Google Cloud Dedicated console. You can also ask your user to provide the
project name that they want to use in your app.





If you have not run the Google Cloud CLI previously, you must
run the following command to specify the project name and authenticate with
the Google Cloud Dedicated console:


```
gcloud auth login
```


If you want to run a `gcloud` command on Google Cloud Dedicated in Germany resources
in another project, specify the `--project` option for this command and for the
other `gcloud` commands throughout this page.

## Create managed zones

Each managed zone that you create is associated with a
[Google Cloud Dedicated project](/resource-manager/docs/creating-managing-projects).
The following sections describe how to create the type of managed zone that
Cloud DNS supports.

### Create a private zone

To create a new managed private zone with private DNS records managed by
Cloud DNS, complete the following steps. For more information,
see [Best practices for Cloud DNS private
zones](/dns/docs/best-practices#best_practices_for_private_zones).


[ Console ](#console) [ gcloud ](#gcloud) [ Terraform ](#terraform) [ API ](#api) 
More 




- 

In the Google Cloud Dedicated console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.berlin-build0.goog/net-services/dns/zones/new/create)

- 

For the **Zone type**, select **Private**.

- 

Enter a **Zone name** such as `my-new-zone`.

- 

Enter a **DNS name** suffix for the private zone. All records in the
zone share this suffix, for example: `example.private`.

- 

Optional: Add a description.

- 

Under **Options**, select **Default (private)**.

- 

Select the Virtual Private Cloud (VPC) networks to which the private zone
must be visible. Only the VPC networks that you select are
authorized to query records in the zone.

- 

Click **Create**.




Run the
[`dns managed-zones create`](/sdk/gcloud/reference/dns/managed-zones/create)
command:


```
gcloud dns managed-zones create NAME \
--description= DESCRIPTION \
--dns-name= DNS_SUFFIX \
--networks= VPC_NETWORK_LIST \
--labels= LABELS \
--visibility=private
```


Replace the following:

- ` NAME `: a name for your zone

- ` DESCRIPTION `: a description for your zone

- ` DNS_SUFFIX `: the DNS suffix for your zone, such as
`example.private`

- ` VPC_NETWORK_LIST `: a comma-delimited list of
VPC networks that are authorized to query the zone

- ` LABELS `: an optional comma-delimited list of key-value
pairs such as `dept=marketing` or `project=project1`; for more
information, see the
[SDK documentation](/sdk/gcloud/reference/dns/managed-zones/create#--labels)























```
resource "google_dns_managed_zone" "private_zone" {
name = "private-zone"
dns_name = "private.example.com."
description = "Example private DNS zone"
labels = {
foo = "bar"
}

visibility = "private"

private_visibility_config {
networks {
network_url = google_compute_network.network_1.id
}
networks {
network_url = google_compute_network.network_2.id
}
}
}

resource "google_compute_network" "network_1" {
name = "network-1"
auto_create_subnetworks = false
}

resource "google_compute_network" "network_2" {
name = "network-2"
auto_create_subnetworks = false
}
```






Send a `POST` request using the
[`managedZones.create`](/dns/docs/reference/v1/managedZones/create) method:


```
POST https://dns.googleapis.com/dns/v1/projects/ PROJECT_ID /managedZones
{

"name": " NAME ",
"description": " DESCRIPTION ",
"dnsName": " DNS_NAME ",
"visibility": "private",
"privateVisibilityConfig": {
"kind": "dns#managedZonePrivateVisibilityConfig",
"networks": [
{
"kind": "dns#managedZonePrivateVisibilityConfigNetwork",
"networkUrl": " VPC_NETWORK_1 "
},
{
"kind": "dns#managedZonePrivateVisibilityConfigNetwork",
"networkUrl": " VPC_NETWORK_2 "
},
....
]
}
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project where the managed zone is
created

- ` NAME `: a name for your zone

- ` DESCRIPTION `: a description for your zone

- ` DNS_NAME `: the DNS suffix for your zone, such as
`example.private`

- 

` VPC_NETWORK_1 ` and ` VPC_NETWORK_2 `:
URLs for VPC networks in the same project that can query
records in this zone. You can add multiple VPC networks
as indicated. To determine the URL for a VPC network,
use the following `gcloud` command, replacing
` VPC_NETWORK_NAME ` with the network's name:


```
gcloud compute networks describe VPC_NETWORK_NAME \
--format="get(selfLink)"
```





### Create a zone with specific IAM permissions

The Identity and Access Management (IAM) permission for individual resource managed zone
lets you set up specific read, write, or administrator permissions for
different managed zones under the same project.

For instructions about how to create a zone with specific Identity and Access Management (IAM)
permissions, see [Create a zone with specific IAM
permissions](/dns/docs/zones/iam-per-resource-zones).

### Create a Service Directory DNS zone

You can create a Service Directory zone that allows your Google Cloud Dedicated-based
services to query your Service Directory namespace through DNS.

For detailed instructions about how to create a Service Directory DNS zone, see
[Configuring a Service Directory DNS zone](/service-directory/docs/configuring-service-directory-zone).

For instructions about how to use DNS to query your Service Directory, see
[Querying using DNS](/service-directory/docs/query-dns).

### Create a forwarding zone

Forwarding zones let you target name servers for specific private zones. For
instructions on how to create a new managed private
forwarding zone, see [Create a forwarding
zone](/dns/docs/zones/forwarding-zones).

### Create a peering zone

DNS peering lets you send requests for records that come from one zone's
namespace to another VPC network. For instructions on
how to create a peering zone, see [Create a peering
zone](/dns/docs/zones/peering-zones).

### Create a cross-project binding zone

Create a managed private zone that can be bound to a network that is owned by a
different project within the same organization. For instructions on how to
create a cross-project binding zone, see [Cross-project binding
zones](/dns/docs/zones/cross-project-binding).

## Update managed zones

Cloud DNS lets you modify certain attributes of your managed
managed private zone.

### Update labels

To add new, change existing, remove selected, or clear all labels on a managed
zone, complete the following steps.


[ gcloud ](#gcloud) 
More 




Run the
[`dns managed-zones update`](/sdk/gcloud/reference/dns/managed-zones/update)
command:


```
gcloud dns managed-zones update NAME \
--update-labels= LABELS 
```



```
gcloud dns managed-zones update NAME \
--remove-labels= LABELS 
```



```
gcloud dns managed-zones update NAME \
--clear-labels
```


Replace the following:

- ` NAME `: a name for your zone

- ` LABELS `: an optional comma-delimited list of key-value
pairs such as `dept=marketing` or `project=project1`; for more
information, see the
[SDK documentation](/sdk/gcloud/reference/dns/managed-zones/create#--labels)




## List and describe managed zones

The following sections show how to list or describe a managed zone.

### List managed zones

To list all of your managed zones within a project, complete the following steps.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/networking/dns/zones/)

- 

View managed zones in the right pane.




Run the
[`dns managed-zones list`](/sdk/gcloud/reference/dns/managed-zones/list)
command:


```
gcloud dns managed-zones list
```


To list all managed zones, modify the command as follows:

To list all managed private zones, modify the command as follows:


```
gcloud dns managed-zones list --filter="visibility=private"
```



### Describe a managed zone

To view the attributes of a managed zone, complete the following steps.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/networking/dns/zones/)

- 

Click the zone that you want to inspect.




Run the
[`dns managed-zones describe`](/sdk/gcloud/reference/dns/managed-zones/describe)
command:


```
gcloud dns managed-zones describe NAME 
```


Replace ` NAME ` with the name of your zone.



## Delete a managed zone

When you delete a zone, its DNS records are permanently removed;
they cannot be recovered. To prevent losing your DNS records, export your
zone data before deletion. For information about how to export zone data,
see [Import and export resource record sets](/dns/docs/records#import-export).

To delete a managed zone, complete the following steps.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/networking/dns/zones/)

- 

Click the managed zone that you want to delete.

- 

Click **Delete zone**.




- 

Remove all records in the zone except for the `SOA` and `NS` records.
For more information, see
[Removing a record](/dns/docs/records#removing_a_record).
You can quickly empty an entire zone by importing an empty file into a
record set. For more information, see [Importing and exporting record
sets](/dns/docs/records#importing_and_exporting_record_sets).
For example:


```
touch empty-file
gcloud dns record-sets import -z NAME \
--delete-all-existing \
empty-file
rm empty-file
```


Replace ` NAME ` with the name of your zone.

- 

To delete a new managed private zone, run the [`dns managed-zones
delete`](/sdk/gcloud/reference/dns/managed-zones/delete) command:


```
gcloud dns managed-zones delete NAME 
```


Replace ` NAME ` with the name of your zone.




## What's next

- To find solutions for common issues that you might encounter when using
Cloud DNS, see [Troubleshooting](/dns/docs/troubleshooting).

- To configure Cloud DNS server policies and use them with
VPC networks, see
[Apply Cloud DNS server policies](/dns/docs/policies).

- To use IDNs with Cloud DNS, see
[Create zones with internationalized domain names](/dns/docs/zones/international-domains).

- To display an audit log of operations, see
[View operations on managed zones](/dns/docs/zones/operations).