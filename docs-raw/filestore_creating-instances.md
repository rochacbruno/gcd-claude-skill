# Create an instance

Source: https://berlin.devsitetest.how/filestore/docs/creating-instances
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/filestore/docs/tpc-differences) for more details.














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

Storage

](https://berlin.devsitetest.how/docs/storage)






- 








[

Filestore

](https://berlin.devsitetest.how/filestore/docs)






- 








[

Guides

](https://berlin.devsitetest.how/filestore/docs/overview)












# Create an instance 














This page shows you how to create a Filestore instance by using either
the Google Cloud Dedicated console or the Google Cloud CLI.

## Instructions for creating an instance



### Google Cloud Dedicated console

### Before you begin

- 

[Enable Filestore API](/endpoints/docs/openapi/enable-api#console). It might take a few minutes for Filestore API to appear on the **Service** list under **Quotas & System Limits**.

- 

The quota for a zonal or
regional instance starts at `0`. To
use these capacities, you must first create and receive approval for a
[quota increase request](/filestore/docs/requesting-quota-increases)
before you can create an instance.

- 

If you need to create an instance using an
enterprise or high scale SSD tier, you must run your operations directly through
the Filestore API or by using `gcloud`. These `create` operations
are not supported through the Google Cloud Dedicated console.

For more information, see [Service tiers](/filestore/docs/service-tiers).

### Google Cloud Dedicated instructions

- 

In the Google Cloud Dedicated console, go to the Filestore **Instances** page.

[Go to Instances](https://console.cloud.berlin-build0.goog/filestore/instances) 

- 

Click **Create Instance**.

- 

Enter all required fields and optional fields as needed based on the
instructions in the following sections of this page.

- 

Click **Create**.



### gcloud

### Before you begin

- 

To use the gcloud CLI, you must either
[install the gcloud CLI](/sdk/downloads)
or use the Cloud Shell



that's built into the Google Cloud Dedicated console:

[Go to the Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/) 

- 

[Enable Filestore API](/endpoints/docs/openapi/enable-api#gcloud). It might take a few minutes for Filestore API to appear on the **Service** list under **Quotas & System Limits**.

### `gcloud` command for creating a Filestore instance

You can create a Filestore instance by running the [`filestore
instances create`](/sdk/gcloud/reference/filestore/instances/create) command.
Quota for instances varies by project, region, and tier. For more information,
see [Quotas](/filestore/docs/service-tiers#quota) or [Request a quota increase](/filestore/docs/requesting-quota-increases).


```
gcloud filestore instances create INSTANCE_ID \
[--project= PROJECT_ID ] \
[--location= LOCATION ] \
[--description= DESCRIPTION ] \
[--performance= PERFORMANCE ] \
--tier= TIER \
--file-share=name=" FILE_SHARE_NAME ",capacity= FILE_SHARE_SIZE \
--network=name=" VPC-NETWORK ",[connect-mode= CONNECT_MODE ],[reserved-ip-range=" RESERVED_IP_ADDRESS "] \
[--labels= KEY = VALUE ,[ KEY = VALUE ,…]] \
[--kms-key= KMS_KEY ] \
[--deletion-protection] \
[--deletion-protection-reason=" PROTECTION_REASON "]
```


Where:

- INSTANCE_ID with the instance ID of the Filestore
instance that you want to create. See [Name your instance](/filestore/docs/creating-instances#name_your_instance).

- 

PROJECT_ID with the project ID of the Google Cloud Dedicated project that
contains the Filestore instance. You can skip this
flag if the Filestore instance is in the `gcloud` default
project. You can set the default project by running the [`config set project`](/sdk/gcloud/reference/config/set)
command:


```
gcloud config set project PROJECT_ID 
```


- 

LOCATION with the location where you want the
Filestore instance to reside. See
[Select a location](#select_a_location).
You can skip this flag if the Filestore instance is in
the `gcloud` default location. You can set the default location by running
the [`config set filestore/zone`](/sdk/gcloud/reference/config/set) command:


```
gcloud config set filestore/zone zone 
```


For the regional or enterprise tier, use the
[`config set filestore/region`](/sdk/gcloud/reference/config/set) command:


```
gcloud config set filestore/region region 
```


- 

DESCRIPTION A [description](/sdk/gcloud/reference/filestore/instances/create#--description) of the Filestore instance.

- 

PERFORMANCE if you want to use the `--performance` flag to configure [custom performance](/filestore/docs/custom-performance), use one of the following options:

- `max-iops-per-tb` specifies an IOPS per TiB rate that scales IOPS linearly with instance capacity.

- `max-iops` specifies an IOPS rate that doesn't scale IOPS with instance capacity.

The format is as follows:


```
--performance=max-iops-per-tb=17000
```


The `--performance` flag is required when creating regional instances with capacity lower than 1024 GiB. For more information, see [small capacity Filestore instances](/filestore/docs/service-tiers#small-instances).

- 

TIER with the [service tier](/filestore/docs/service-tiers) you
want to use.

- 

FILE_SHARE_NAME with the name you specify for the NFS file share
that is served from the instance. See
[Name the file share](#name_the_file_share).

- 

FILE_SHARE_SIZE with the size you want for the file share. See
[Allocate capacity](#allocate_capacity).

- 

VPC_NETWORK with the name of the Virtual Private Cloud (VPC) network you
want the instance to use. See
[Select the VPC network](#select_vpc_network).
If you want to specify a Shared VPC from a service project, you must
specify the fully qualified network name, which is in the format
`projects/ HOST_PROJECT_ID /global/networks/ SHARED_VPC_NAME `
and you must specify `connect-mode=PRIVATE_SERVICE_ACCESS`. For example:


```
--network = name = projects/host/global/networks/shared-vpc-1,connect-mode = PRIVATE_SERVICE_ACCESS
```


You can't specify a
[legacy network](/vpc/docs/legacy) 
for the VPC_NETWORK value. If necessary, create a new
VPC network to use by following the instructions at
[Creating a new auto mode VPC network](/vpc/docs/create-modify-vpc-networks#create-auto-network).

- 

CONNECT_MODE with `DIRECT_PEERING` or `PRIVATE_SERVICE_ACCESS`.
If you are specifying a Shared VPC as the network, you must also
specify `PRIVATE_SERVICE_ACCESS` as the connect mode.

- 

RESERVED_IP_ADDRESS with the IP address range for the
Filestore instance. If you are specifying
`connect-mode=PRIVATE_SERVICE_ACCESS`, and want to use a reserved IP
address range, you must specify the name of an
[allocated address range](/vpc/docs/configure-private-services-access#allocating-range)
instead of a CIDR range. See
[Configure a reserved IP address](#configure_a_reserved_ip_address_range).
We recommend that you skip this flag to allow Filestore to
automatically find a free IP address range and assign it to the instance.

- 

KEY with a label that you want to add. Adding labels is not
required when creating a Filestore instance. You can also add,
delete, or update labels after you create an instance. For details, see
[Managing labels](/filestore/docs/managing-labels).

- 

VALUE with the value for a label.

- 

KMS_KEY is the fully qualified name of the
[Cloud Key Management Service](/kms) encryption key that you want to use when you
want to manage your own data encryption. The format looks like:


```
projects/ KMS_PROJECT_ID /locations/ REGION /keyRings/ KEY_RING /cryptoKeys/ KEY 
```


- 

PROTECTION_REASON if you choose to use the
`--deletion-protection` flag, you have the option of adding a note
regarding the setting. To add the note, use the optional
`--deletion-protection-reason` flag and include a description of the
justification for the setting you chose. For example, "All genomics data
must adhere to current organization policies." For more information, see
[Deletion protection](/filestore/docs/deletion-protection).

## Name your instance

The following command creates an instance with the following characteristics:

- ID is `render1`.

- Project is `myproject`.

- Region is `us-central1`.

- Tier is `REGIONAL`.

- Performance uses `max-iops-per-tb` parameter with the value of `17000`.

- File share name is `my_vol`.

- File share size is 2 TiB.

- VPC network is `default`.

- Reserved IP address range is `10.0.7.0/29`.

- Grants read and write access with root squashed to the client with IP
address `10.0.2.0`.

- Deletion protection is enabled.

- A justification for the deletion protection setting is provided.


```
gcloud filestore instances create render1 \
--project=myproject \
--region=us-central1 \
--tier=REGIONAL \
--performance=max-iops-per-tb=17000 \
--network=name="default",reserved-ip-range="10.0.7.0/29" \
--flags-file=nfs-export-options.json \
--deletion-protection \
--deletion-protection-reason="All genomics data must adhere to current
organization policies."
```


`nfs-export-options.json` file contents:


```
{
"--file-share":
{
"capacity": "2048",
"name": "my_vol",
"nfs-export-options": [
{
"access-mode": "READ_WRITE",
"ip-ranges": [
"10.0.0.0/29",
"10.2.0.0/29"
],
"squash-mode": "ROOT_SQUASH",
"anon_uid": 1003,
"anon_gid": 1003
},
{
"access-mode": "READ_ONLY",
"ip-ranges": [
"192.168.0.0/26"
],
"squash-mode": "NO_ROOT_SQUASH"
}
]
}
}
```


### REST API

- 

Have gcloud CLI [installed and initialized](/sdk/docs/install), which lets
you generate an access token for the `Authorization` header.

- 

Use [`cURL`](http://curl.haxx.se/) to call the [Filestore API](/filestore/docs/reference/rest/v1/projects.locations.instances/create):


```
curl --request POST \
'https://file.googleapis.com/v1/projects/ PROJECT /locations/ LOCATION /instances?instanceId= NAME ' \
--header "Authorization: Bearer $(gcloud auth print-access-token)" \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
"tier":" TIER ",
"networks":[
{
"network":" NETWORK "
}
],
"performanceConfig": {" PERFORMANCE "}
"fileShares":[
{"capacityGb": CAPACITY ,"name":" SHARE_NAME "}
],
"deletionProtectionEnabled": true,
"deletionProtectionReason": " PROTECTION_REASON "}' \
--compressed
```


Where:

- ` PROJECT ` is the name of the project where your
instance will reside. For example, `my-genomics-project`.

- ` LOCATION ` is the location where the instance
will reside. For example, `us-east1` or `us-central1-a`.

- ` NAME ` is the name of the instance you
want to create. For example, `my-genomics-instance`.

- ` TIER ` is the name of the service tier you want
to use. For example, `REGIONAL`.

- 

` PERFORMANCE ` is the [performance configuration](/filestore/docs/reference/rest/v1beta1/projects.locations.instances#performanceconfig)
used to specify custom performance settings.

You can use only one of the provided options.

- `PerformanceConfig.iopsPerTb.maxIopsPerTb` specifies an IOPS per TiB rate that scales IOPS linearly with instance capacity.

- `PerformanceConfig.fixedIops.maxIops` specifies a fixed IOPS rate that doesn't scale IOPS with instance capacity.

The format is as follows:


```
"performanceConfig": {
"iopsPerTb" : {
"maxIopsPerTb":17000
}
}
```


- 

` NETWORK ` is the name of the network you want
to use. For example, `default`.

- 

` CAPACITY ` is the size, in GiB, you want to
allocate for the instance. For example, `1024`.

- 

` SHARE_NAME ` is the name of the file share. For
example, `vol1`.

- 

` PROTECTION_REASON ` if you choose to use the
`deletionProtectionEnabled` flag, you have the option of adding a note
regarding the setting. To add the note, use the optional
`deletionProtectionReason` flag and include a description of the
justification for the setting you chose. For example, "All genomics
data must adhere to current organization policies." For more
information, see [Deletion protection](/filestore/docs/deletion-protection).




## Understand instances and shares

A Filestore *instance* represents physical storage capacity.

A *share* represents an allocated portion of that storage with an individual,
unique access point.

All service tiers offer storage options with a 1:1 share–to–instance
ratio. Alternatively, [Filestore multishares for Google Kubernetes Engine (GKE)](/filestore/docs/multishares),
available for enterprise-tier instances only, offers access to multiple shares
on a single instance.

Instance names, or instance IDs, are used by administrators to manage instances.
File share names are used by clients to connect to the shares exported from those
instances.

## Name your instance

The name of your Filestore instance, or instance ID, is used to
identify the instance and is used in `gcloud` commands. Instance IDs must comply
with the ` ` element of
[RFC 1035](https://www.ietf.org/rfc/rfc1035.txt).
Specifically, they must:

- Be between 1-63 characters long.

- Begin with a lowercase letter.

- Consist of dashes, lowercase letters, or digits.

- End with lowercase letters or digits.

The instance ID must be unique in the Google Cloud Dedicated project and zone where it's
located. Once an instance is created, its instance ID cannot be changed.

## Configure service tier

Select the service tier that best suits your needs. Once an instance is
created, its service tier cannot be changed. For a detailed description of capabilities available by service tier, see
[Service tiers](/filestore/docs/service-tiers).

`Create` operations for zonal, regional,
and enterprise instances can take anywhere between 15 minutes and
one hour to complete, depending on instance size.

Filestore quota is consumed when instance creation starts but you
are not billed for the instance during this time.

## Allocate capacity

Allocate capacity to the amount you need when you create the instance. As you
approach your capacity limit, you can scale up the capacity as needed without
affecting runtime. To learn about how you can monitor the capacity of your
instances, see [Monitoring instances](/filestore/docs/monitoring-instances).

In the gcloud CLI, you can specify the capacity in whole numbers
using either `GiB` or `TiB`. The default unit is `GiB`.

The following table shows the instance sizes available for each tier:




| 
Tier | 
Minimum size | 
Maximum size | 
Incremental step size | 
|



| 
Zonal | 
1 TiB | 
9.75 TiB | 
256 GiB | 
|

| 
Zonal | 
10 TiB | 
100 TiB | 
2.5 TiB | 
|

| 
Regional | 
100 GiB | 
10,239 GiB | 
1 GiB | 
|

| 
Regional | 
10 TiB | 
100 TiB | 
2.5 TiB | 
|

| 
Basic HDD | 
1 TiB | 
63.9 TiB | 
1 GiB | 
|

| 
Basic SSD | 
2.5 TiB | 
63.9 TiB | 
1 GiB | 
|

| 
Enterprise | 
1 TiB | 
10 TiB | 
256 GiB | 
|



The size of instances can be any whole gibibyte value or its tebibyte
equivalent that's between the minimum and maximum instance size and is divisible
by its incremental step size. For example, valid sizes for zonal-tier instances
with a higher capacity range include 10 TiB, 12.5 TiB, and 15 TiB.

Once created, basic HDD and basic SSD instances can only scale up in size. All other service tiers can scale up or down in capacity. For more information, see
[Edit instances](/filestore/docs/editing-instances) and [Scale capacity](/filestore/docs/scale).

### Total capacity quota

Every project is allocated a separate capacity quota, defined by region and
service tier. Quota limits vary by service tier.

Once you have reached your quota limit, you won't be able to create more
Filestore instances or increase the capacity of your existing instances.
To see your available quota, go to the **Quotas** page in the Google Cloud Dedicated console:

[Go to Quotas](https://console.cloud.berlin-build0.goog/iam-admin/quotas) 

For information on requesting more quota, see [Requesting quota increases](/filestore/docs/requesting-quota-increases).

## Configure performance

Instance performance depends on the [service tier](/filestore/docs/service-tiers) you choose.

### Regional and zonal tiers

- 

For regional and zonal tiers, custom performance is enabled by default when using Google Cloud Dedicated console, letting you configure performance based on workload and scale.
You can set an IOPS per TiB ratio which allows instance IOPS to scale with capacity, or a constant IOPS value that doesn't scale with capacity but can be adjusted at any time if the capacity changes. For details on limits, see [custom performance limits](/filestore/docs/custom-performance#custom-performance-limits).

- 

Creating Regional instances with capacity lower than 1024 GiB requires enabled custom performance. The minimum IOPS value for these instances is 2,000. For more information, see [low capacity Filestore instances](/filestore/docs/service-tiers#small-instances).

### Basic SSD and basic HDD tiers

- For basic SSD tiers the number of IOPS is constant and doesn't change when you change capacity settings.

- For basic HDD tiers the performance limits change depending if the capacity falls within the range of 1 TiB to 10 TiB or from 10 TiB to 63.9 TiB.

For additional information on performance limits and settings,
see [performance](/filestore/docs/performance).

### Specify IOPS per TiB ratio

Custom performance lets you specify the ratio in the **IOPS per TiB** field where the performance scales based on the capacity.

If you want to use fixed IOPS, clear the **Scale performance with capacity** checkbox.

Assuming you have specified the following initial performance values:

- **Capacity**: 1 TiB

- **IOPS per TiB**: 6,000

- **Performance** (when the **Scale performance with capacity** checkbox is selected): 6,000 IOPS

The following examples show how performance scales based on changed settings:

- Increasing **IOPS per TiB** to 7,000 adjusts **Performance** to 7,000 IOPS.

- Increasing **Capacity** to 2 TiB adjusts **Performance** to 14,000 IOPS.

- Decreasing **Performance** to 8,000 IOPS adjusts **IOPS per TiB** to 4,000.

### Specify fixed number of IOPS

If you clear the **Scale performance with capacity** checkbox, the **Performance** field specifies the number of IOPS you want to use. This number must be within the [performance range](/filestore/docs/custom-performance#custom-performance-limits) and a multiple of 1,000.

Setting a fixed number of IOPS independently of capacity allows performance
tuning. However, this option prevents automatic performance scaling with
capacity changes. Changing capacity might require adjusting the performance value,
and the other way around.

For example, you specified the following values:

- **Capacity**: 4 TiB

- **Performance** 40,000 IOPS

At this point, you can increase the performance up to 68,000 IOPS, which is the limit for 4 TiB of capacity.
You want to increase performance to 70,000 IOPS which is beyond the performance range for the capacity of 4 TiB. To maintain compatibility, you must increase the capacity to 4.25 TiB or higher to fall within the performance range.

## Select a location

Location refers to the **Region** and **Zone** where the Filestore
instance is located. For the best performance and to avoid cross-regional
networking charges, ensure that the Filestore instance is located
in the same region as the Compute Engine VMs that need to access them.

For more information about regions and zones, see
[Geography and regions](/filestore/docs/regions).

## Select the file system protocol

Select the file system [protocol](/filestore/docs/about-supported-protocols) that suits your needs. Filestore supports NFSv3 and NFSv4.1 protocols.

## Set up connections

Select the network IP stack type and VPC network.

### Choose network IP stack type

Select either IPv4 or IPv6 as your network IP stack type.

### Choose VPC network

The network that you select to use with Filestore can be either a
standard VPC network or a Shared VPC network.

#### VPC network

If you use Google Cloud Dedicated console, you must use Private Service Connect that allows consumers to access managed services privately from inside their VPC network. Private Service Connect requires the consumer to provision a single internal IP address in its own VPC to create a Private Service Connect endpoint, instead of allocating an entire IP address range to facilitate the connection.

To create a [Private Service Connect endpoint](/vpc/docs/private-service-connect#endpoints) on the consumer target network, you must create a [service connection policy](/vpc/docs/about-service-connection-policies) in your project.

For more information on how to use Private Service Connect, see [Create a Filestore instance with Private Service Connect](/filestore/docs/configure-psc).

The network that you choose must have enough available IP resources to
dedicate to the Filestore instance, otherwise the instance
[fails to create due to IP address exhaustion](/vpc/docs/configure-private-services-access#modify-ip-range).
For more information, see [Networking and IP resource requirements](/filestore/docs/network-ip-requirements).

Clients must be on the same network as the Filestore
instance to access the files stored on that instance. Once an instance is
created, this network selection can't be changed.

#### Shared VPC network

To create a Filestore instance with [Shared VPC network](/vpc/docs/shared-vpc), you must create the instance in the host project.

Before you can create an instance on a
[Shared VPC network](/vpc/docs/shared-vpc)
in a service project, the network administrator must first enable
[private services access](/vpc/docs/private-services-access)
for the Shared VPC network. If you are creating the instance in the host
project, private services access is not required.

Shared VPC networks are displayed in the Google Cloud Dedicated console in the
format:


```
projects/ HOST_PROJECT_ID /global/networks/ SHARED_VPC_NAME 
```


For detailed procedures, see
[Creating an instance on a Shared VPC network](/filestore/docs/shared-vpc).

### NFS file locking

If the applications you plan to use with a Filestore instance
require NFS [file locking](https://en.wikipedia.org/wiki/File_locking),
you might need to open up the ports used by Filestore in the network you choose, if either of the following options applies to your use case:

- A VPC network other than the default network.

- The default VPC network with changed firewall rules.

This consideration applies only to Filestore instances that use private services access or direct peering connection methods.

For more information, see [Configuring firewall rules](/filestore/docs/configuring-firewall).

## Configure the file share

A file share is the directory on a Filestore instance where all
shared files are stored. It is also the thing that you mount or map to on the
client VM.

The name of the file share must comply with the following:

- Be between 1-32 characters long for zonal, regional, and enterprise tiers, and
1-16 characters long for basic tiers.

- Begin with a letter.

- Consist of uppercase or lowercase letters, numbers, and underscores.

- End with a letter or number.

## Configure IP-based access control

By default, a Filestore instance grants root level read and write
access to all clients, including Compute Engine VMs and
GKE clusters, that share the same Google Cloud Dedicated project and
VPC network. If you want to restrict access, you can do so by
creating rules that grant specific access levels to clients based on their IP
address. Once the rules are added, all IP addresses and ranges that are not
specified in a rule are revoked access. Zonal, regional, and enterprise instances
support configuration settings for overlapping IP address ranges. For more
information, see [Overlapping permissions](/filestore/docs/access-control#overlapping-permissions).

The following table describes the privileges of each access level. These access
levels are only used in the Google Cloud Dedicated console. In the gcloud CLI
and the API, you must specify the rule configurations directly.



| 
Access level | 
Rule configuration | 
Description | 
|




| 
`admin` | 

- read-write
- no-root-squash
| 
The client can view and modify all files, folders, and metadata as a root user. It can also grant ownership to files or folders by setting its `uid` and `gid`, and in doing so, grant access to clients that don't have root level access to the file share. | 
|

| 
`admin-viewer` | 

- read-only
- no-root-squash
| 
The client can view all files, folders, and metadata as a root user but cannot modify them. | 
|

| 
`editor` | 

- read-write
- root-squash
| 
The client can view and modify the files, folders, and metadata according to its assigned `uid` and `gid`. | 
|

| 
`viewer` | 

- read-only
- root-squash
| 
The client can view the files, folders, and metadata according to its assigned `uid` and `gid`. | 
|



`root-squash` maps all requests from `uid 0` and `gid 0` to `anon_uid` and
`anon_gid`, respectively. This configuration removes root level access from
clients that attempt to access the file share as a root user.

When creating IP-based access rules:

- You must specify an internal IP address or range and the access level granted.

- At least one rule must grant `admin` access at the time of instance creation.
This rule can be removed once the instance is created.

- Zonal, regional, and enterprise instances support configuration settings for
overlapping IP address ranges. Basic-tier instances are not supported. For more
information, see [Overlapping permissions](/filestore/docs/access-control#overlapping-permissions).

In the Google Cloud Dedicated console, you can create up to 4 different rules (`admin`,
`admin-viewer`, `editor`, `viewer`) involving up to 64 different IP addresses or
ranges.

In the gcloud CLI, you can configure up to 64 different IP addresses
or CIDR blocks per Filestore instance across a maximum of 10
different rules. A rule is defined as the combination of the `access-mode`,
`squash-mode`, and `anon_uid`/`anon_gid` configurations. The `anon_uid` and
`anon_gid` fields have default values of `65534` and can only be configured
through the API and the gcloud CLI.

### Example

Here's an example of three different IP-based access rules:

- `access-mode=READ_ONLY`, `squash-mode=ROOT_SQUASH`, `anon_uid=10000`.

- `access-mode=READ_WRITE`, `squash-mode=ROOT_SQUASH`, `anon_gid=150`.

- `access-mode=READ_WRITE`, `squash-mode=NO_ROOT_SQUASH`.

To create IP-based access control rules using the gcloud CLI, use the
[`--flags-file`](/sdk/gcloud/reference#--flags-file) flag with the
[`instances create`](/sdk/gcloud/reference/filestore/instances/create) or
[`instances update`](/sdk/gcloud/reference/filestore/instances/update) commands
and point it to a JSON configuration file. For example, if the JSON
configuration file is named `nfs-export-options.json`, the flag would be:


```
-- flags - file = nfs - export - options . json 
```


Example JSON configuration file:


```
{
"--file-share":
{
"capacity": "2048",
"name": "my_vol",
"nfs-export-options": [
{
"access-mode": "READ_WRITE",
"ip-ranges": [
"10.0.0.0/29",
"10.2.0.0/29"
],
"squash-mode": "ROOT_SQUASH",
"anon_uid": 1003,
"anon_gid": 1003
},
{
"access-mode": "READ_ONLY",
"ip-ranges": [
"192.168.0.0/26"
],
"squash-mode": "NO_ROOT_SQUASH"
}
]
}
}
```


- **ip-ranges** is the IP address or range to grant access to. You can specify
multiple IP addresses or ranges by separating them with a comma. Only zonal,
regional, and enterprise instances support configuration settings for
overlapping IP address ranges. For more information, see
[Overlapping permissions](/filestore/docs/access-control#overlapping-permissions).

- **access-mode** is the access level to grant to the clients whose
IP address falls within **ip-range**. It can have the values of
`READ_WRITE` or `READ_ONLY`. The default value is `READ_WRITE`.

- **squash-mode** can have the values `ROOT_SQUASH` or
`NO_ROOT_SQUASH`. `ROOT_SQUASH` removes root level access to the clients
whose IP address falls within **ip-range**, while `NO_ROOT_SQUASH`
enables root access. The default value is `NO_ROOT_SQUASH`.

- **anon_uid** is the user ID value that you want to map to `anon_uid`. The
default value is `65534`.

- **anon_gid** is the group ID value that you want to map to `anon_gid`. The
default value is `65534`.

### Clients on non-RFC 1918 ranges

If you plan to connect
non-[RFC 1918](https://tools.ietf.org/html/rfc1918)
clients to your Filestore instance, you must explicitly grant them
access to the Filestore instance using
[IP-based access control](/filestore/docs/creating-instances#configure_ip-based_access_control).

## Optional fields

The following sections describe optional fields.

### Add an instance description

An instance description lets you write descriptions, notes, or instructions
for yourself and other users. For example, you can include information about:

- The types of files stored in the instance.

- Who has access to the instance.

- Instructions for how to get access to the instance.

- What the instance is used for.

Instance descriptions are limited to 2048 characters in length. There are no
restrictions on the characters that are allowed. Once a Filestore
instance is created, you can update its instance description anytime as needed.
For information on updating instance descriptions, see
[Editing instances](/filestore/docs/editing-instances#instructions_for_editing_an_instance).

### Add labels

Labels are key-value pairs that you can use to group related instances and store
metadata about an instance. You can add, delete, or modify labels anytime.
For more information, see [Managing labels](/filestore/docs/managing-labels).

### Configure a reserved IP address range

Each Filestore instance must have an IP address range associated
with it. Both [RFC 1918](https://tools.ietf.org/html/rfc1918)
and non-RFC 1918 IP address ranges ([GA](https://berlin.devsitetest.how/products#product-launch-stages))
are supported.

Once specified, an instance's IP address range is immutable.

Users are encouraged to let Filestore automatically determine a
free IP address range and assign it to the instance. When selecting your own
range, consider the following Filestore IP resource requirements:

- 

Must use CIDR notation.

- 

Must be a [valid VPC subnet range](/vpc/docs/subnets#valid-ranges).

- 

Basic instances require a block size of 29. For example, `10.123.123.0/29`.

- 

Zonal, regional, and enterprise instances require a block size of 26. For
example, `172.16.123.0/26`.

- 

The IP address range must not overlap with the following:

- 

Existing subnets in the VPC network that the
Filestore instance uses.

- 

Existing subnets in a VPC network that's peered with the one
that the Filestore instance uses. For details, see
[Overlapping subnets at time of peering](/vpc/docs/vpc-peering#overlapping_subnets_at_time_of_peering).

- 

IP address ranges assigned to any other existing Filestore
instances in that network.

- 

The `172.17.0.0/16` address range is reserved for internal Filestore
components. As a result, the following limitations apply:

- 

Clients in this range can't be connected to Filestore instances.

- 

Filestore instances can't be created within this IP range. For
more information, see [Known issues](/filestore/docs/known-issues#clients_cant_have_an_ip_address_from_the_172170016_range).

- 

There must be at least one VPC Network Peering or private services access
connections per VPC.

You can see the IP address ranges for the subnets of your network by going to
the VPC networks page in the Google Cloud Dedicated console:

[Go to VPC Networks](https://console.cloud.berlin-build0.goog/networking/networks) 

You can get the reserved IP address range for any Filestore
instance on the Filestore instances page in the
Google Cloud Dedicated console:

[Go to Filestore Instances](https://console.cloud.berlin-build0.goog/filestore/instances) 

If you want to use private services access and specify a reserved IP address
range, you must specify the name of an
[allocated address range](/vpc/docs/configure-private-services-access#allocating-range)
for the connection. If you don't specify a range name, Filestore
automatically uses any of the allocated ranges associated with the private
services access connection.

### Use a customer-managed encryption key

By default, Google Cloud Dedicated in Germany automatically
[encrypts data when it is at rest](https://berlin.devsitetest.how/security/encryption/default-encryption)
using encryption keys managed by Google. If you need more control over the keys
that protect your data, you can use customer-managed encryption keys (CMEK) for
Filestore. For details, see
[Encrypt data with customer-managed encryption keys](/filestore/docs/cmek).

### Enable deletion protection

Set the instance's deletion protection setting. By default, this setting is
disabled. For more information, see [Deletion protection](/filestore/docs/deletion-protection).

### Add a deletion protection setting description

Add a description of the justification behind the deletion protection setting
you chose. For more information, see [Deletion protection](/filestore/docs/deletion-protection).

## What's next

- Learn how to [configure an instance for use with the NFSv4.1 protocol](/filestore/docs/configure-nfsv4).

- Learn how to connect instances to clients:

- [Mount the Filestore file share on a Compute Engine VM instance](/filestore/docs/mounting-fileshares).

- [Access Filestore instances with the Filestore CSI driver](/filestore/docs/csi-driver).

- [Use Filestore instances as external datastores for VMware ESXi
hosts in Google Cloud VMware Engine](/filestore/docs/gcve-datastores).

- [Mount file shares on remote clients](/filestore/docs/remote-mounting).

- [Mount a Filestore instance to a Cloud Run service to
share data between containers and
services](/filestore/docs/mount-filestore-cloud-run).

- [See how to retrieve instance details, such as the instance's IP address, so
that you can access the Filestore file share from clients](/filestore/docs/getting-instance-information#get-instance).

- [Troubleshoot instance creation issues related to Filestore](/filestore/docs/troubleshooting#unable_to_create_an_instance).

- [Learn more about VPC networks and subnets](/vpc/docs/subnets#valid-ranges).

- [Learn more about networking and IP resource requirements for Filestore](/filestore/docs/networking).