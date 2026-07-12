# Creating a basic access level

Source: https://berlin.devsitetest.how/access-context-manager/docs/create-access-level
Last updated: 2026-07-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/access-context-manager/docs/tpc-differences) for more details.














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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

Access Context Manager

](https://berlin.devsitetest.how/access-context-manager/docs)






- 








[

Guides

](https://berlin.devsitetest.how/access-context-manager/docs/create-access-level)












# Creating a basic access level 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Create a basic access level ](#create_a_basic_access_level)
- [ Example implementations ](#example_implementations)

- [ Limit access on a corporate network ](#corporate-network-example)
- [ Limit access by device attributes ](#device-example)
- [ Grant access by user or service account ](#members-example)

- 










This page describes generally how to create basic access levels. To create
custom access levels and use **Advanced Mode** in the Google Cloud Dedicated console, see
[Creating a custom access level](/access-context-manager/docs/create-custom-access-level).

This page includes more focused implementations of access levels. See the
following examples:

- [Limit access on a corporate network](#corporate-network-example)

- [Limit access by device attributes](#device-example)

- [Grant access by user or service account](#members-example)

## Before you begin 

- Learn about [access levels](/access-context-manager/docs/overview).

## Create a basic access level


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To create a basic access level:

- 

Open the **Access Context Manager** page in the Google Cloud Dedicated console.

[Open the Access Context Manager page](https://console.cloud.berlin-build0.goog/security/access-level)

- 

If you are prompted, select your organization.

- 

At the top of the **Access Context Manager** page, click **New**.

- 

In the **New Access Level** pane:

- 

In the **Access level title** field, enter a title for the access level.
The title must be at most 50 characters, start with a letter, and can
contain only numbers, letters, underscores, and spaces.

- 

In the **Conditions** section, click the
add button for the type
of attribute you want to add, and then provide
the values you want applied to that attribute.

For a complete list of the attributes you can add,
read about [access level attributes](/access-context-manager/docs/access-level-attributes).

For example, if you want the access level to consider where a
request is coming from within your network, you would select the
**IP Subnetworks** attribute.

Repeat this step to add multiple attributes to the same condition.
When a condition has multiple attributes, all of the attributes must
be met by the access request.

An access level condition can include one of each type of
attribute. Some attributes include additional
options, such as the **Device Policy** attribute.

Access levels support conditions based on
user identity. However, to add identities to a condition, you
must create or update the access level using the gcloud CLI or the API.

- 

Use the **When condition is met, return** option to specify whether
you want the condition to require that a request meet all
specified attributes (**TRUE**) or whether the request must
meet anything but those attributes (**FALSE**).

For example, if you want to deny requests from a certain IP address
range of your network, specify the IP address range using the
**IP Subnetworks** attribute and then set the condition to
**FALSE**.

- 

Optionally, click **Add another condition** to add an
additional condition to your access level and then repeat
the previous two steps.

For example, if you want to deny access to a subset of IP
addresses within a broader IP address range, create a new
condition, specify the subset IP address range for the
**IP Subnetworks** attribute, and set the condition to return
**FALSE**.

Repeat this step to add multiple conditions to the same access
level.

- 

If you created more than one condition, use
**Combine condition with** to specify whether you want the
access level to require a request to meet at least one of the
conditions (**OR**), or all of the conditions (**AND**).

- 

Click **Save**.



### Before you begin

- If it doesn't exist yet, [create an access policy](/access-context-manager/docs/create-access-policy) for
your organization.

To create an access level using the `gcloud` command-line tool, use the
[`gcloud access-context-manager levels create`](/sdk/gcloud/reference/access-context-manager/levels/create) command.


```
gcloud access-context-manager levels create LEVEL_NAME OPTIONS \ 
--policy = POLICY 
```


Where:

- 

LEVEL_NAME is the unique name for the access level. It must
begin with a letter and include only letters, numbers, and
underscores. The name can be a maximum of 50 characters.

- 

OPTIONS are the required options from the following table.




| 
Options | 
|



| 
`basic-level-spec` | 



[A YAML file](#yaml-file) that specifies one or
more conditions for the access level.


| 
|

| 
`title` | 



A short title for the access level. The access level's title
is displayed in the Google Cloud Dedicated console.


| 
|

| 
`combine-function` | 



(Optional) Determines how conditions are combined.




Valid values: `AND`, `OR`


| 
|

| 
`description` | 



(Optional) A long-form description of the access level.

| 
|



- 

POLICY is the ID of your organization's access policy.
If you have a default policy set, this parameter is optional.

Optionally, you can include any of the
[gcloud-wide flags](/sdk/gcloud/reference).

### basic-level-spec YAML file

When you use the `gcloud` command-line tool to create an access level, you must provide a YAML
file for the `basic-level-spec` option. The YAML file defines one or more
conditions for the access level. Conditions must contain at least one
attribute. When a condition contains more than one attribute, they are
combined as either an **AND** operation (all must be true) or as a **NAND**
operation (none can be true), depending on whether the `negate` attribute
is included in the condition.

For a complete list of the attributes you can include in your YAML file,
read about [access level attributes](/access-context-manager/docs/access-level-attributes).

For more information about access levels and YAML,
refer to the [example YAML for an access level](/access-context-manager/docs/example-yaml-file).

### Example command


```
gcloud access-context-manager levels create Device_Trust \ 
--basic-level-spec = corpdevspec.yaml \ 
--combine-function = AND \ 
--description = 'Access level that conforms to corporate spec.' \ 
--title = 'Device_Trust Extended' \ 
--policy = 1521580097614100 
```


### Before you begin

- If it doesn't exist yet, [create an access policy](/access-context-manager/docs/create-access-policy) for
your organization.

To create an access level, call [`accessLevels.create`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).


```
POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/ POLICY /accessLevels
```


Where:

- POLICY is the ID of your organization's
access policy.

### Request body

The request body must include an [`AccessLevel`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)
resource that specifies the conditions you want for the new access level.
Each [`Condition`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#condition) has one or more attributes that are
evaluated as an **AND** operation (all must be true) or as a
**NAND** operation (none can be true) depending on whether the `negate`
field is set to `true`. The resulting evaluation determines whether the
condition is met or not.

### Response body

If successful, the response body for the call contains an
[`Operation`](/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the
`POST` operation.



## Example implementations

The following examples cover a few of the practical ways your organization might
want to implement access levels. These examples assume your organization already
has an [access policy](/access-context-manager/docs/create-access-policy).

### Limit access on a corporate network

This example describes how to create an access level condition that allows
access only from a specified range of IP addresses (for example, those within a
corporate network).

By restricting the range of IP addresses that are granted access, you can
make exfiltrating data more difficult for an attacker that is inside or outside
your organization.

For this example, assume you want to create an access level that will allow a
group of internal auditors to access the Cloud Logging service for a
project named *sensitive-data*. All of the devices for the auditors are
assigned IPs on a subnet ranging between 203.0.113.0 and 203.0.113.127. You
know there won't be any devices assigned to that subnet other than those
used by the auditors.

If you want to use a private IP address range (for example, `192.168.0.0/16`
or `172.16.0.0/12`), see [Allow access to protected resources from an internal
IP address](/vpc-service-controls/docs/enable-internal-ip-access) for additional
information and an example implementation using VPC Service Controls.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

Open the **Access Context Manager** page in the Google Cloud Dedicated console.

[Open the Access Context Manager page](https://console.cloud.berlin-build0.goog/security/access-level)

- 

If you are prompted, select your organization.

- 

At the top of the **Access Context Manager** page, click **New**.

- 

In the **New Access Level** pane, in the **Conditions** section, click
**Add attribute** and then click **IP Subnetworks**.

- 

In the **IP Subnetworks** box, select either **Public IP** or **Private
IP**.

- 

If you select **Public IP**, enter one or more IPv4 or IPv6 ranges
formatted as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks.

In this example, to limit access to only the auditors, enter
`203.0.113.0/25` in the **IP Subnetworks** box.

- 

If you select **Private IP**, click **Select VPC networks**. You can
specify VPC networks using one of the three options
available in the **Import options** list.

- 

*Option 1:*

- 

Select **Browse for VPC networks in your organization** and select the
VPC networks.

- 

Click **Add selected VPC networks**.

- 

Click **Select IP subnets** and select the subnets.

- 

Click **Add IP subnets**.

- 

*Option 2:*

- 

Select **Manually enter VPC network address** and enter one or more
VPC networks.

- 

Click **Add VPC network**.

- 

Click **Select IP subnets** and select the subnets.

- 

Click **Add IP subnets**.

- 

*Option 3:*

- 

Select **Upload CSV file (overwrites existing networks)**.

If you use a CSV file to add VPC networks and subnets
to an access level, Access Context Manager overwrites the previously selected VPC
networks and subnets.

- 

Click **Browse** and upload the CSV file. In the CSV file, you must specify
the VPC networks and subnets in the following format:


```
VPC_NETWORK_NAME_1 | IP_RANGE_1 | IP_RANGE_2 | ...
VPC_NETWORK_NAME_2 | . | . | ...
. | . | . | ...
. | . | . | ...
```


- 

Click **Import networks**.

Using the CSV file, Access Context Manager populates the VPC network
names and subnet information in the **VPC network address** and **IP
subnetworks** boxes respectively.

For information about the VPC network name and private
IP address format, see [Use internal IP address in access
levels](/vpc-service-controls/docs/enable-internal-ip-access#enable).

- 

Click **Save**.




- 

Create a YAML file for an access level that includes one or more
IPv4 or IPv6 ranges formatted as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks.

In this example, to limit access to only the auditors, you would enter
the following into the YAML file:


```
- ipSubnetworks : 
- 203.0.113.0/25 
```


If you want to use a private IP address, you need to enter the following
information in the YAML file:


```
- vpcNetworkSources : 
- vpcSubnetwork : 
network : VPC_NETWORK_NAME 
vpcIpSubnetworks : 
- IP_RANGE 
```


Replace VPC_NETWORK_NAME and IP_RANGE with the values
described in the [Use internal IP address in access
levels](/vpc-service-controls/docs/enable-internal-ip-access#enable) section.

- 

Save the file. In this example, the file is named *CONDITIONS.yaml*.

- 

Create the access level.


```
gcloud access-context-manager levels create NAME \ 
--title TITLE \ 
--basic-level-spec CONDITIONS.yaml \ 
--policy = POLICY 
```


Where:

- 

NAME is the unique name for the access level. It must
begin with a letter and include only letters, numbers, and
underscores.

- 

TITLE is a human-readable title. It must be unique to the
policy.

- 

POLICY is the ID of your organization's
access policy. If you have a default policy set, this parameter is
optional.

You should see output similar to:


```
Create request issued for: NAME 
Waiting for operation [accessPolicies/ POLICY /accessLevels/ NAME /create/1521594488380943] to complete...done.
Created level NAME .
```





- 

Craft a request body to create an [`AccessLevel`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)
resource that includes one or more IPv4 or IPv6 ranges formatted
as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks.

In this example, to limit access to only the auditors, you would enter
the following into the request body:


```
{ 
"name" : " NAME " , 
"title" : " TITLE " , 
"basic" : { 
"conditions" : [ 
{ 
"ipSubnetworks" : [ 
"203.0.113.0/25" 
] 
} 
] 
} 
} 
```


Where:

- 

NAME is the unique name for the access level. It must
begin with a letter and include only letters, numbers, and
underscores.

- 

TITLE is a human-readable title. It must be unique to the
policy.

If you want to use a private IP address, you need to enter the following
information in the request body:


```
{ 
"name" : " NAME " , 
"title" : " TITLE " , 
"basic" : { 
"conditions" : [ 
{ 
"vpcNetworkSources" : [ 
{ 
"vpcSubnetwork" : { 
"network" : VPC_NETWORK_NAME , 
"vpcIpSubnetworks" : [ 
IP_RANGE 
] 
} 
} 
] 
} 
] 
} 
} 
```


Replace VPC_NETWORK_NAME and IP_RANGE with the values
described in the [Use internal IP address in access
levels](/vpc-service-controls/docs/enable-internal-ip-access#enable) section.

- 

Create the access level by calling [`accessLevels.create`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).


```
POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/ POLICY /accessLevels
```


Where:

- POLICY is the ID of your organization's
access policy.




### Limit access by device attributes

This example describes how to create an access level that grants access only to
devices, which meet a specified set of requirements, like a certain operating
system (OS) version.

Information about devices is provided to Access Context Manager using
[Endpoint Verification](https://support.google.com/cloudidentity/answer/9007320).
The following criteria can be checked when determining whether to grant access:

- Screen lock is enabled

- Storage encryption is enabled

- Device is running a specified operating system kind and version

For this example, assume your organization uses only machines that have either
Chrome OS or Windows installed. To add a layer of security, you want to create
an access level that will prevent access by anyone using other operating
systems. Additionally, to manage risk, you want to make sure that only certain
versions of the OSes can gain access.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

Open the **Access Context Manager** page in the Google Cloud Dedicated console.

[Open the Access Context Manager page](https://console.cloud.berlin-build0.goog/security/access-level)

- 

If you are prompted, select your organization.

- 

At the top of the **Access Context Manager** page, click **New**.

- 

In the **New Access Level** pane, in the **Conditions** section,
click **Add attribute** and then click **Device Policy**.

- 

Add the device policy attributes:

- 

Click **Add OS Policy** and then click **Chrome OS Policy**.

- 

In the **Minimum version** box, enter the minimum version of Chrome
OS you want to allow.

- 

Repeat steps 1 and 2 for **Windows OS Policy**.

- 

Click **Save**.




- 

Create a YAML file for an access level that includes a device policy with
OS constraints.

In this example, to allow only devices with a minimum acceptable version
of Chrome OS and Windows, you would enter the following into the YAML
file:


```
- devicePolicy : 
osConstraints : 
- osType : DESKTOP_CHROME_OS 
minimumVersion : 11316.165.0 
- osType : DESKTOP_WINDOWS 
minimumVersion : 10.0.1809 
```


- 

Save the file. In this example, the file is named *CONDITIONS.yaml*.

- 

Create the access level.


```
gcloud access-context-manager levels create NAME \ 
--title TITLE \ 
--basic-level-spec CONDITIONS.yaml \ 
--policy = POLICY 
```


Where:

- 

NAME is the unique name for the access level. It must
begin with a letter and include only letters, numbers, and
underscores.

- 

TITLE is a human-readable title. It must be unique to the
policy.

- 

POLICY is the ID of your organization's
access policy. If you have a default policy set, this parameter is
optional.

You should see output similar to:


```
Create request issued for: NAME 
Waiting for operation [accessPolicies/ POLICY /accessLevels/ NAME /create/1521594488380943] to complete...done.
Created level NAME .
```





- 

Craft a request body to create an [`AccessLevel`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)
resource that includes a device policy with OS constraints.

In this example, to allow only devices with a minimum acceptable version
of Chrome OS and Windows, you would enter the following into the request
body:


```
{ 
"name" : " NAME " , 
"title" : " TITLE " , 
"basic" : { 
"conditions" : [ 
{ 
"devicePolicy" : { 
"osConstraints" : [ 
{ 
"osType" : "DESKTOP_CHROME_OS" , 
"minimumVersion" : "11316.165.0" 
}, 
{ 
"osType" : "DESKTOP_WINDOWS" , 
"minimumVersion" : "10.0.1809" 
} 
] 
} 
} 
] 
} 
} 
```


Where:

- 

NAME is the unique name for the access level. It must
begin with a letter and include only letters, numbers, and
underscores.

- 

TITLE is a human-readable title. It must be unique to the
policy.

- 

Create the access level by calling [`accessLevels.create`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).


```
POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/ POLICY /accessLevels
```


Where:

- POLICY is the ID of your organization's
access policy.




### Grant access by user or service account

Access levels for human users often combine identity with other context
like IP addresses. In contrast, access levels for service accounts are defined
based on the specific service account identity. For example, Cloud Functions
requires an identity to interact with other Google Cloud Dedicated in Germany services.

The following information describes how to grant access to specific users and service
accounts, while including existing access levels to show an example of
nested access levels. In this case, the specified users are included in this
access level regardless of whether they meet the conditions specified in the
existing access levels. This new access level could be considered as a
less-restrictive tier than the existing access levels.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




The Google Cloud Dedicated console does not currently support adding principals to
access levels. If you want to add principals to access levels, you must
use the `gcloud` command-line tool or the API.



- 

Create a YAML file that contains a condition that lists the principals
that you want to provide access to.

Add a system administrator
(`sysadmin@example.com`) and a service account
(`service@project.eu0.iam.gserviceaccount.com`).


```
- members : 
- user:sysadmin@example.com 
- serviceAccount:service@project. eu0.iam.gserviceaccount.com
```


- 

Add a condition that lists the existing access levels that you want to
include in this access level.

In this example, assume the access levels are named `Device_Trust` and
`IP_Trust`, and that `247332951433` is the name of your access policy.


```
- members : 
- user:sysadmin@example.com 
- serviceAccount:service@project. eu0.iam.gserviceaccount.com

- requiredAccessLevels : 
- accessPolicies/247332951433/accessLevels/Device_Trust 
- accessPolicies/247332951433/accessLevels/IP_Trust 
```


- 

Save the file. In this example, the file is named *CONDITIONS.yaml*.

- 

Create the access level, using the [`create`](/sdk/gcloud/reference/access-context-manager/levels/create) command.


```
gcloud access-context-manager levels create NAME \ 
--title TITLE \ 
--basic-level-spec CONDITIONS.yaml \ 
--combine-function = OR \ 
--policy = POLICY 
```


Where:

- 

NAME is the unique name for the access level. It must
begin with a letter and include only letters, numbers, and
underscores.

- 

TITLE is a human-readable title. It must be unique to the
policy.

- 

POLICY is the ID of your organization's
access policy. If you have a default policy set, this parameter
is optional.

- 

`combine-function` is set to `OR`. The default value, `AND`, requires
*all* conditions be met before an access level is granted. The `OR`
value will give the principals access even if other conditions are
not met.

You should see output similar to:


```
Create request issued for: NAME 
Waiting for operation [accessPolicies/ POLICY /accessLevels/ NAME /create/1521594488380943] to complete...done.
Created level NAME .
```





- 

Craft a request body to create an [`AccessLevel`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel)
resource that includes a condition that lists the principals
that you want to provide access to.

In this example, you want to add your system administrator
(`sysadmin@example.com`) and a service account
(`service@project.eu0.iam.gserviceaccount.com`).


```
{ 
"name" : " NAME " , 
"title" : " TITLE " , 
"basic" : { 
"conditions" : [ 
{ 
"members" : [ 
"user:sysadmin@example.com" , 
"serviceAccount:service@project.eu0.iam.gserviceaccount.com" 
] 
} 
] 
} 
} 
```


Where:

- 

NAME is the unique name for the access level. It must
begin with a letter and include only letters, numbers, and
underscores.

- 

TITLE is a human-readable title. It must be unique to the
policy.

- 

Add a condition that lists the existing access levels that you want to
include in this access level.

In this example, assume the access levels are named `Device_Trust` and
`IP_Trust`, and that `247332951433` is the name of your access policy.


```
{ 
"name" : " NAME " , 
"title" : " TITLE " , 
"basic" : { 
"conditions" : [ 
{ 
"members" : [ 
"user:sysadmin@example.com" , 
"serviceAccount:service@project.eu0.iam.gserviceaccount.com" 
] 
}, 
{ 
"requiredAccessLevels" : [ 
"accessPolicies/247332951433/accessLevels/Device_Trust" , 
"accessPolicies/247332951433/accessLevels/IP_Trust" 
] 
} 
] 
} 
} 
```


- 

Set `combiningFunction` to `OR`.

The default value for `combiningFunction`, `AND`, requires
*all* conditions be met before an access level is granted. The `OR`
value will give the principals access even if other conditions, such as
IP address or those inherited from other required access levels, are
not met.


```
{ 
"name" : " NAME " , 
"title" : " TITLE " , 
"basic" : { 
"conditions" : [ 
{ 
"members" : [ 
"user:sysadmin@example.com" , 
"serviceAccount:service@project.eu0.iam.gserviceaccount.com" 
] 
}, 
{ 
"requiredAccessLevels" : [ 
"accessPolicies/247332951433/accessLevels/Device_Trust" , 
"accessPolicies/247332951433/accessLevels/IP_Trust" 
] 
} 
], 
"combiningFunction" : "OR" 
} 
} 
```


- 

Create the access level by calling [`accessLevels.create`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).


```
POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/ POLICY /accessLevels
```


Where:

- POLICY is the ID of your organization's
access policy.