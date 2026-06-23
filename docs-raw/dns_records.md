# Add, update, and delete records

Source: https://berlin.devsitetest.how/dns/docs/records
Last updated: 2026-06-18

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












# Add, update, and delete records 






- On this page ** 
- [ Before you begin ](#before_you_begin)
- [ Add a resource record set ](#add-rrset)
- [ Add a collection of resource record sets in a transaction ](#add-transaction)
- [ View resource record sets for a zone ](#view-rrsets)
- [ View details of a resource record set ](#view-rrset)
- [ Update a resource record set ](#update-rrset)
- [ Delete resource record sets ](#delete-rrset)
- [ Import and export resource record sets ](#import-export)
- [ What's next ](#whats_next)
- 










This page describes how to add, update, and delete resource record sets.

To view the list of supported resource record types, see [DNS records overview](/dns/docs/records-overview#supported_dns_record_types).


#### Permissions required for this task 


To perform this task, you must have been granted the following permissions
*or* the following IAM roles.

Permissions**


- `dns.resourceRecordSets.create` to create a resource record set

- `dns.resourceRecordSets.delete` to delete a resource record set

- `dns.resourceRecordSets.get` to retrieve a resource record set

- `dns.resourceRecordSets.list` to list a resource record set

- `dns.changes.create` to update a `ResourceRecordSet` collection

- `dns.changes.get` to fetch the representation of an existing `Change`

- `dns.changes.list` to list changes to a `ResourceRecordSet` collection


**Roles**


- `roles/dns.admin`



## Before you begin 

You must have or create a managed zone before you can create a resource record
set. For details about how to create a managed zone, in which you can create
your resource record set, see
[Create a managed zone](/dns/docs/zones#create_managed_zones).

## Add a resource record set

To add a resource record set, follow these steps:


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) [ Terraform ](#terraform) 
More 




- 

In the Google Cloud Dedicated console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/net-services/dns/) 

- 

Click the name of the managed zone that you want to add the record to.

- 

On the **Zone details** page, click **Add standard**.

- 

On the **Create record set** page, in the **DNS name** field, enter
the subdomain of the DNS zone—for example, `mail`. The trailing
dot is automatically added at the end.

To create a wildcard DNS record, enter an asterisk—for example,
`*.example.com`.

The at sign (@) does not automatically create an apex record.
To create a resource record at the domain apex, leave the **DNS name**
field blank.

- 

Select the **Resource record type**—for example, `MX`.

- 

In the **TTL** field, enter a numeric value for the resource record's
time to live, which is the amount of time that it can be cached. This
value must be a positive integer.

- 

From the **TTL unit** menu, select the unit of time—for example,
`minutes`.

- 

Depending on the resource record type that you have selected,
[populate the remaining fields](/dns/docs/records-overview#supported_dns_record_types).

- 

To enter additional information, click **Add item**.

- 

Click **Create**.




To add a resource record set, use the
[`gcloud dns record-sets create` command](/sdk/gcloud/reference/dns/record-sets/create):


```
gcloud dns record-sets create RRSET_NAME \
--rrdatas= RR_DATA \
--ttl= TTL \
--type= RRSET_TYPE \
--zone= MANAGED_ZONE 
```


Replace the following:

- ` RRSET_NAME `: the DNS name that matches the incoming
queries with this zone's DNS name as its suffix—for example,
`test.example.com`

- ` RR_DATA `: an arbitrary value associated with the resource
record set—for example, `198.51.100.5`; you can also enter multiple
values, `rrdata1` `rrdata2` `rrdata3`—for example, `198.51.100.5`
`10.2.3.4`...

- ` TTL `: the TTL in seconds that the resolver caches this
resource record set—for example, `30`

- ` RRSET_TYPE `: the [resource record type](/dns/docs/records-overview#supported_dns_record_types)
of this resource record set—for example, `A`.

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix




To add a resource record set, use the
[`resourceRecordSets.create` method](/dns/docs/reference/v1/resourceRecordSets/create)
method:


```
POST https://dns.googleapis.com/dns/v1/projects/ PROJECT_ID /managedZones/ MANAGED_ZONE /rrsets
{
"name": " RRSET_NAME ",
"type": " RRSET_TYPE ",
"ttl": TTL ,
"rrdatas": [ RR_DATA ]
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix

- ` RRSET_NAME `: the DNS name that matches the incoming
queries with this zone's DNS name as its suffix—for example,
`test.example.com`

- ` RRSET_TYPE `: the [resource record type](/dns/docs/records-overview#supported_dns_record_types)
of this resource record set—for example, `A`

- ` TTL `: the TTL in seconds that the resolver caches this
resource record set—for example, `30`

- ` RR_DATA `: an arbitrary value associated with the resource
record set—for example, `"198.51.100.5"`; you can also enter
multiple values in a comma-separated list—for example,
`"198.51.100.5","10.2.3.4"`.























```
resource "google_dns_managed_zone" "parent_zone" {
name = "sample-zone"
dns_name = "sample-zone.hashicorptest.com."
description = "Test Description"
}

resource "google_dns_record_set" "default" {
managed_zone = google_dns_managed_zone.parent_zone.name
name = "test-record.sample-zone.hashicorptest.com."
type = "A"
rrdatas = ["10.0.0.1", "10.1.0.1"]
ttl = 86400
}
```






## Add a collection of resource record sets in a transaction

You can add multiple resource record sets by creating a transaction that
specifies the changes. A transaction is a group of one or more DNS record
changes that must be applied as a unit. The entire transaction either succeeds
or fails, ensuring your data is never left in an inconsistent state. You can
create a transaction only by using the gcloud CLI or the
Cloud DNS API.

To create a transaction, follow these steps:


[ gcloud ](#gcloud) [ API ](#api) 
More 




- 

To start a transaction, use the
[`gcloud dns record-sets transaction start` command](/sdk/gcloud/reference/dns/record-sets/transaction/start):


```
gcloud dns record-sets transaction start \
--zone= MANAGED_ZONE 
```


Replace ` MANAGED_ZONE ` with the name of the managed
zone whose resource record sets you want to manage—for example,
`my-zone-name`.

- 

To add a resource record set as part of a transaction, use the
[`gcloud dns record-sets transaction add` command](/sdk/gcloud/reference/dns/record-sets/transaction/add):


```
gcloud dns record-sets transaction add RR_DATA \
--name= DNS_NAME \
--ttl= TTL \
--type= RECORD_TYPE \
--zone= MANAGED_ZONE 
```


Replace the following:

- ` RR_DATA `: an arbitrary value associated with the
resource record set—for example, `198.51.100.5`; you can also
enter multiple values, `rrdata1` `rrdata2` `rrdata3`—for
example, `198.51.100.5` `10.2.3.4`...

- ` DNS_NAME `: the DNS or domain name of the record set
to add—for example, `test.example.com`

- ` TTL `: the time to live (TTL) for the record set in number
of seconds—for example, `300`

- ` RECORD_TYPE `: the [record type](/dns/docs/records-overview#supported_dns_record_types)—for
example, `A`.

- ` MANAGED_ZONE `: the name of the managed zone whose
resource record sets you want to manage—for example, `my-zone-name`

- 

To execute the transaction, use the
[`gcloud dns record-sets transaction execute` command](/sdk/gcloud/reference/dns/record-sets/transaction/execute):


```
gcloud dns record-sets transaction execute \
--zone= MANAGED_ZONE 
```


- 

To add a wildcard transaction, use the
[`gcloud dns record-sets transaction add` command](/sdk/gcloud/reference/dns/record-sets/transaction/add):


```
gcloud dns record-sets transaction add \
--zone= MANAGED_ZONE \
--name= WILDCARD_DNS_NAME \
--type= RECORD_TYPE \
--ttl= TTL 
```


Replace the following:

- ` MANAGED_ZONE `: the name of the managed zone whose
resource record sets you want to manage—for example, `my-zone-name`

- ` WILDCARD_DNS_NAME `: the DNS or domain name of the
resource record set that you want to add—for example, `*.example.com.`
(note the trailing dot)

- ` RECORD_TYPE `: the [record type](/dns/docs/records-overview#supported_dns_record_types)—for
example, `CNAME`.

- ` TTL `: the TTL for the record set in number
of seconds—for example, `300`




To create a transaction with new resource record sets, use the
[`changes.create` method](/dns/docs/reference/v1/changes/create):


```
POST https://dns.googleapis.com/dns/v1/projects/ PROJECT_ID /managedZones/ MANAGED_ZONE /changes
{
"deletions": []
"additions": [
{
"name": DNS_NAME ,
"type": RECORD_TYPE ,
"ttl": TTL ,
"rrdatas": [
RR_DATA 
]
}
]
}
```


Replace the following:

- ` PROJECT_ID `: your project ID

- ` MANAGED_ZONE `: your managed zone name or ID

- ` DNS_NAME `: the DNS or domain name of the record
set—for example, `test.example.com.` (note the trailing dot)

- ` RECORD_TYPE `: the [record type](/dns/docs/records-overview#supported_dns_record_types)

- ` TTL `: the time to live (TTL) for the record set in number of
seconds—for example, `30`

- ` RR_DATA `: an arbitrary value associated with the resource
record set—for example, `198.51.100.5`; you can also enter multiple
values, `rrdata1` `rrdata2` `rrdata3`—for example, `198.51.100.5`
`10.2.3.4`...




To deliver email to your domain, you must add `MX` records to your zone. If you
use Google Workspace as your Simple Mail Transfer Protocol (SMTP) provider, see
the [Set up Google Workspace `MX`
records](https://support.google.com/a/answer/9222085) support page. Otherwise,
use the `MX` record details from your provider and follow the setup
process described for Google Workspace.

## View resource record sets for a zone

To view resource record sets for a zone, follow these steps:


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Google Cloud Dedicated console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.berlin-build0.goog/net-services/dns/zones) 

- 

On the **Zones** tab, click the zone for which you want to view the resource record sets.

The **Zone details** page shows the details of all the resource record sets
in that zone.




To view the DNS records for your zone, use the
[`gcloud dns record-sets list` command](/sdk/gcloud/reference/dns/record-sets/list):


```
gcloud dns record-sets list \
--zone=" ZONE_NAME "
```


Replace ` ZONE_NAME ` with the name of a DNS zone in
your project.

The command outputs the JSON response for the resource record set for
the first 100 records. You can specify these additional parameters:

- `--limit`: maximum number of record sets to list

- `--name`: only list resource record sets with this exact domain name

- `--type`: only list records of this type; if present, the `--name` parameter
must also be present




To view the DNS records for your zone, use the
[`resourceRecordSets.list` method](/dns/docs/reference/rest/v1/resourceRecordSets/list):


```
GET https://dns.googleapis.com/dns/v1/projects/ PROJECT_ID /managedZones/ MANAGED_ZONE /rrsets
```


Replace the following:

- ` PROJECT_ID `: the ID of the project

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix




## View details of a resource record set

This procedure assumes that you have already created a resource record set
within the managed Cloud DNS zone.

To view the details of an existing resource record set, follow these steps:


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Google Cloud Dedicated console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/net-services/dns/zones) 

- 

Click the zone that contains the resource record set.

- 

Click the resource record set for which you want to view the details.

The **Resource record set details** page displays the details of the resource
record set.




To view the details of an existing resource record set, use the
[`gcloud dns record-sets describe` command](/sdk/gcloud/reference/dns/record-sets/describe):


```
gcloud dns record-sets describe RRSET_NAME \
--type= RRSET_TYPE \
--zone= MANAGED_ZONE 
```


Replace the following:

- ` RRSET_NAME `: the DNS name that matches the incoming
queries with this zone's DNS name as its suffix—for example,
`test.example.com`

- ` RRSET_TYPE `: the [resource record type](/dns/docs/records-overview#supported_dns_record_types)
of this resource record set—for example, `A`.

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix




To get the details of an existing resource record set, use the
[`resourceRecordSets.get` method](/dns/docs/reference/v1/resourceRecordSets/get):


```
GET https://dns.googleapis.com/dns/v1/projects/ PROJECT_ID /managedZones/ MANAGED_ZONE /rrsets/ RRSET_NAME / RRSET_TYPE 
```


Replace the following:

- ` PROJECT_ID `: the ID of the project

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix

- ` RRSET_NAME `: the DNS name that matches the incoming
queries with this zone's DNS name as its suffix—for example,
`test.example.com`

- ` RRSET_TYPE `: the [record type](/dns/docs/records-overview#supported_dns_record_types)
of this resource record set—for example, `A`.




## Update a resource record set

To modify a record set, follow these steps:


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To apply a partial update to an existing resource record set,
follow these steps:

- 

In the Google Cloud Dedicated console, go to the **Cloud DNS zones**
page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/net-services/dns/zones) 

- 

Click the zone for which you want to update the resource record set.

- 

On the **Zone details** page, next to the resource record set that you
want to update, click
*edit***Edit**.

- 

After making the necessary updates, click **Save**.




To apply a partial update to an existing resource record set, use the
[`gcloud dns record-sets update` command](/sdk/gcloud/reference/dns/record-sets/update):


```
gcloud dns record-sets update RRSET_NAME \
--rrdatas= RR_DATA \
--ttl= TTL \
--type= RRSET_TYPE \
--zone= MANAGED_ZONE 
```


Replace the following:

- ` RRSET_NAME `: the DNS name that matches the incoming
queries with this zone's DNS name as its suffix—for example,
`test.example.com`

- ` RR_DATA `: an arbitrary value associated with the resource
record set—for example, `198.51.100.5`; you can also enter multiple
values, `rrdata1` `rrdata2` `rrdata3`—for example, `198.51.100.5`
`10.2.3.4`...

- ` TTL `: the TTL in seconds that the resolver caches this
resource record set—for example, `30`

- ` RRSET_TYPE `: the [resource record type](/dns/docs/records-overview#supported_dns_record_types)
of this resource record set—for example, `A`.

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix




To apply a partial update to an existing resource record set, use
the [`resourceRecordSets.patch` method](/dns/docs/reference/v1/resourceRecordSets/patch):


```
PATCH https://dns.googleapis.com/dns/v1/projects/ PROJECT_ID /managedZones/ MANAGED_ZONE /rrsets/ RRSET_NAME / RRSET_TYPE 
{
"ttl": TTL ,
"rrdatas": RR_DATA ,
"update_mask": {
"paths": ["rrset.ttl", "rrset.rrdatas"]
}
}
```


Replace the following:

- ` PROJECT_ID `: the ID of the project

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix

- ` RRSET_NAME `: the DNS name that matches the incoming
queries with this zone's DNS name as its suffix—for example,
`test.example.com`

- ` RRSET_TYPE `: the [resource record type](/dns/docs/records-overview#supported_dns_record_types)
of this resource record set—for example, `A`.

- ` TTL `: the TTL in seconds that the resolver caches this
resource record set—for example, `30`

- ` RR_DATA `: an arbitrary value associated with the resource
record set—for example, `198.51.100.5`; you can also enter multiple
values, `rrdata1` `rrdata2` `rrdata3`—for example, `198.51.100.5`
`10.2.3.4`...




## Delete resource record sets

When you delete resource record sets, their DNS records are permanently removed;
they cannot be recovered. To prevent losing your DNS records, export the
resource record sets before deletion. For information about how
to export resource record sets, see
[Import and export resource record sets](/dns/docs/records#import-export).

Cloud DNS automatically creates `NS` and `SOA` records at the zone
apex. These records can't be deleted by using the Cloud DNS API
and are automatically deleted when the zone is deleted. For more information,
see [RFC 1034](https://tools.ietf.org/html/rfc1034).

To delete resource record sets, follow these steps:


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Google Cloud Dedicated console, go to the **Cloud DNS** page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/net-services/dns/) 

Records for the zone are listed on the **Zone details** page.

- 

To delete resource record sets in a zone, click the name of the zone.

- 

Next to the resource record sets that you want to delete, select the checkbox.

- 

Click **Delete record sets**.




To delete an existing resource record set, use the
[`gcloud dns record-sets delete` command](/sdk/gcloud/reference/dns/record-sets/delete):


```
gcloud dns record-sets delete RRSET_NAME \
--type= RRSET_TYPE \
--zone= MANAGED_ZONE 
```


Replace the following:

- ` RRSET_NAME `: the DNS name that matches the incoming
queries with this zone's DNS name as its suffix—for example,
`test.example.com`

- ` RRSET_TYPE `: the [resource record type](/dns/docs/records-overview#supported_dns_record_types)
of this resource record set—for example, `A`.

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix




To delete an existing resource record set, use the
[`resourceRecordSets.delete` method](/dns/docs/reference/v1/resourceRecordSets/delete):


```
DELETE https://dns.googleapis.com/dns/v1/projects/ PROJECT_ID /managedZones/ MANAGED_ZONE /rrsets/ RRSET_NAME / RRSET_TYPE 
```


Replace the following:

- ` PROJECT_ID `: the ID of the project

- ` MANAGED_ZONE `: the managed zone that this
resource record set is affiliated with—for example, `my-zone-name`;
the name of this resource record set must have the DNS name of the
managed zone as its suffix

- ` RRSET_NAME `: the DNS name that matches the incoming
queries with this zone's DNS name as its suffix—for example,
`test.example.com`

- ` RRSET_TYPE `: the [resource record type](/dns/docs/records-overview#supported_dns_record_types)
of this resource record set—for example, `A`.




## Import and export resource record sets

To copy resource record sets into and out of a managed zone, you can use `import` and
`export` commands. You can import from and export to either the BIND zone file
format or the YAML file format.


[ gcloud ](#gcloud) 
More 




- 

To import a resource record set, use the
[`dns record-sets import` command](/sdk/gcloud/reference/dns/record-sets/import):


```
gcloud dns record-sets import -z= ZONE_NAME 
```


If you want to specify the file format of the zone file, use the previous
command with the `--zone-file-format` flag. If you omit the flag, you must
provide a YAML format zone file.

Replace ` ZONE_NAME ` with a new name for your zone.

- 

When you use the `gcloud dns record-sets import` command with the
`--replace-origin-ns` flag, it replaces the NS records for the zone with the
NS records specified in the zone file. These records must match the [name
servers](/dns/docs/update-name-servers#look-up-cloud-dns-name-servers)
assigned by Cloud DNS to host the zone. They must also match
the `NS` records specified in the parent
(delegating) zone. By default, Cloud DNS does not overwrite `NS`
records. If you use this flag, you must verify that the `NS` records are
correct.

- 

When you import record sets as a BIND zone-formatted file, remove the at
sign (@) that denotes the zone's apex. In the BIND zone-formatted file, for
a DNS name like `example.com`, the at sign (@) refers to `example.com.`.
However, in Cloud DNS, the at sign (@) is treated literally
when defining record names. To create a resource record set for the
zone's apex in Cloud DNS, use the full domain name—for
example, `example.com.`.


```
in.smtp IN MX 5 gmail-smtp-in.l.google.com
in.smtp.example.com. IN MX 5 gmail-smtp-in.l.google.com.example.com.
```


To import your zone files, add a trailing dot (`.`) to the end of
any domain names that must be fully qualified.

- 

To export a resource record set, use the
[`dns record-sets export` command](/sdk/gcloud/reference/dns/record-sets/export).
To specify that the resource record sets are exported into a BIND
zone-formatted file, use the `--zone-file-format` flag. For example:


```
example.com. 21600 IN NS ns-gcp-private.googledomains.com.
example.com. 21600 IN SOA ns-gcp-private.googledomains.com.
cloud-dns-hostmaster.google.com. 1 21600 3600 259200 300
host1.example.com. 300 IN A 192.0.2.91
```


If you omit the `--zone-file-format` flag,
`export` exports the resource record set into a YAML-formatted records file:


```
gcloud dns record-sets export example.zone -z=examplezonename
```


For example:


```
--- 
kind : dns#resourceRecordSet 
name : example.com. 
rrdatas : 
- ns-gcp-private.googledomains.com. 
ttl : 21600 
type : NS 
--- 
kind : dns#resourceRecordSet 
name : example.com. 
rrdatas : 
- ns-gcp-private.googledomains.com. cloud-dns-hostmaster.google.com. 1 21600 3600 259200 300 
ttl : 21600 
type : SOA 
--- 
kind : dns#resourceRecordSet 
name : host1.example.com. 
rrdatas : 
- 192.0.2.91 
ttl : 300 
type : A 
```


Cloud DNS supports the `ALIAS` record type, which isn't a standard DNS
record type and isn't supported in `BIND`. If you're exporting resource record
sets to `BIND`, `ALIAS` records are skipped. If a zone has a routing policy,
it is exported as a record with empty resource record data (rrdata).




## What's next

- To get information about `gcloud` commands for resource record sets, see
[`gcloud dns record-sets`](/sdk/gcloud/reference/dns/record-sets).

- To check the status of `gcloud` or API operations, see [Monitor DNS
propagation](/dns/docs/monitoring#dns-propagation).

- To find solutions for common issues that you might encounter when using
Cloud DNS, see [Troubleshooting](/dns/docs/troubleshooting).

- To get an overview of Cloud DNS, see
[Cloud DNS overview](/dns/docs/overview).