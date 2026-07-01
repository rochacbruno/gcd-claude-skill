# Managing access levels

Source: https://berlin.devsitetest.how/access-context-manager/docs/manage-access-levels
Last updated: 2026-06-29

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












# Managing access levels 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ List access levels ](#list_access_levels)
- [ List access levels (formatted) ](#formatted_access_levels)
- [ Describe an access level ](#describe_an_access_level)
- [ Update an access level ](#update_an_access_level)
- [ Delete an access level ](#delete_an_access_level)
- 










This page describes how to manage existing access levels. You can:

- 

[List access levels](#list_access_levels)

- 

[List access levels (formatted)](#formatted_access_levels)

- 

[Describe an access level](#describe_an_access_level)

- 

[Update an access level](#update_an_access_level)

- 

[Delete an access level](#delete_an_access_level)

## Before you begin 

- 

[Set your default access policy](/access-context-manager/docs/manage-access-policy#set-default) for using the `gcloud` command-line tool.

*-or-*

[Get the name of your policy.](/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy) The policy name is required
for commands using the `gcloud` command-line tool and making API calls. If you set a default
access policy, you do not need to specify the policy for the `gcloud` command-line tool.

- 

Ensure that you have an Identity and Access Management (IAM) role at the organization
level that lets you manage access levels. Ask your administrator to grant
you one of the following roles, or a custom role with the same permissions:

- 

**To view access levels:** [Access Context Manager Reader](/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader)
(`roles/accesscontextmanager.policyReader`)

- 

**To view and change access levels:**
[Access Context Manager Editor](/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor)
(`roles/accesscontextmanager.policyEditor`) or
[Access Context Manager Admin](/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin)
(`roles/accesscontextmanager.policyAdmin`)

## List access levels


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To list all access levels, open the **Access Context Manager**
page in the Google Cloud Dedicated console and then, if prompted,
select your organization. Your organization's access levels
are displayed in a grid on the page, including details about the
configuration of each access level.

[Open the Access Context Manager page](https://console.cloud.berlin-build0.goog/security/access-level)



To list all access levels, use the [`list`](/sdk/gcloud/reference/access-context-manager/levels/list) command.


```
gcloud access-context-manager levels list \ 
[ --policy = POLICY_NAME ] 
```


Where:

- POLICY_NAME is the name of your organization's access policy.
This value is required only if you haven't set a
[default access policy](/access-context-manager/docs/manage-access-policy#set-default).

The output will look something like:


```
NAME TITLE LEVEL_TYPE
Device_Trust Device_Trust Extended Basic
Service_Group_A Service_Group_A Basic
```



To list all the access levels for a policy, call
[`accessLevels.list`](/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/list).


```
GET https://accesscontextmanager.googleapis.com/v1alpha/accessPolicies/ POLICY_NAME /accessLevels
```


Where:

- POLICY_NAME is the name of your organization's access policy.

### Request body

The request body must be empty.

### Optional parameters

Optionally, include one or more of the following query parameters.




| 
Parameters | 
|



| 

`pageSize`
| 



`number`




By default, the list of
[
access levels](/access-context-manager/docs/overview#access-levels) returned by `accessLevels.list`
is paginated. Each page is limited to 100 access levels.




You can use this parameter to modify the number of access levels
that are returned per page.


| |

| 

`pageToken`
| 



`string`




If the number of access levels returned by your call exceeded the
page size, the response body will include a page token.




You can use this parameter in a subsequent call to obtain
the next page of results.


| 
|

| 

`accessLevelFormat`
| 



`enum([LevelFormat](/access-context-manager/docs/reference/rest/v1/LevelFormat))`




Normally, access levels are returned as they are defined, either
as `BasicLevel` or `CustomLevel`.




You can specify the value `CEL` for this parameter to
return `BasicLevels` as `CustomLevels` in
Cloud Common Expression Language.


| 
|



### Response body

If successful, the response body for the call contains an
[`AccessLevels`](/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel) object that lists the access levels,
and a [`nextPageToken`](/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/list#body.ListAccessLevelsResponse.FIELDS.next_page_token) string. `nextPageToken` only
has a value if the number of access levels returned exceeds the
[page size](#pageSize). Otherwise, `nextPageToken` is returned as an
empty string.



## List access levels (formatted)

Using the `gcloud` command-line tool, you can obtain a list of your access levels in YAML or JSON
format.

To get a formatted list of access levels, use the [`list`](/sdk/gcloud/reference/access-context-manager/levels/list) command.


```
gcloud access-context-manager levels list \ 
--format = FORMAT \ 
[ --policy = POLICY_NAME ] 
```


Where:

- 

FORMAT is one of the following values:

- 

`list` (YAML format)

- 

`json` (JSON format)

- 

POLICY_NAME is the name of your organization's access policy.
This value is required only if you haven't set a
[default access policy](/access-context-manager/docs/manage-access-policy#set-default).

The YAML output will look something like:


```
- basic : { 'conditions' : [{ 'ipSubnetworks' : [ '8.8.0.0/24' ]}]} 
description : Level for corp access. 
name : accessPolicies/165717541651/accessLevels/corp_level 
title : Corp Level 
- basic : { 'combiningFunction' : 'OR' , 'conditions' : [{ 'ipSubnetworks' : [ '8.8.0.0/24' ]}]} 
description : Level for net access. 
name : accessPolicies/165717541651/accessLevels/net_level 
title : Net Level 
```


The JSON output will look something like:


```
[ 
{ 
"basic" : { 
"conditions" : [ 
{ 
"ipSubnetworks" : [ 
"8.8.0.0/24" 
] 
} 
] 
}, 
"description" : "Level for corp access." , 
"name" : "accessPolicies/165717541651/accessLevels/corp_level" , 
"title" : "Corp Level" 
}, 
{ 
"basic" : { 
"combiningFunction" : "OR" , 
"conditions" : [ 
{ 
"ipSubnetworks" : [ 
"8.8.0.0/24" 
] 
} 
] 
}, 
"description" : "Level for net access." , 
"name" : "accessPolicies/165717541651/accessLevels/net_level" , 
"title" : "Net Level" 
} 
] 
```


## Describe an access level


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




Using Google Cloud Dedicated console, refer to the steps to
[list access levels](#list_access_levels). When you list your access
levels, details are provided in the grid that appears.



Listing access levels only provides their name, title, and level type. To
get detailed information about what a level actually does, use the
`describe` command.


```
gcloud access-context-manager levels describe LEVEL_NAME \ 
[ --policy = POLICY_NAME ] 
```


Where:

- 

LEVEL_NAME is the name of the access level you want to
describe.

- 

POLICY_NAME is the name of your organization's access policy.
This value is required only if you haven't set a
[default access policy](/access-context-manager/docs/manage-access-policy#set-default).

The command will print information about the level formatted as YAML. For
example, if the level restricted access to certain operating system
versions, the output might look something like:


```
basic : 
conditions : 
- devicePolicy : 
allowedEncryptionStatuses : 
- ENCRYPTED 
osConstraints : 
- minimumVersion : 10.13.6 
osType : DESKTOP_MAC 
- minimumVersion : 10.0.18219 
osType : DESKTOP_WINDOWS 
- minimumVersion : 68.0.3440 
osType : DESKTOP_CHROME_OS 
requireScreenlock : true 
name : accessPolicies/330193482019/accessLevels/Device_Trust 
title : Device_Trust Extended 
```




Listing access levels only provides the name, title, and type of the levels.
To get detailed information about an access level,
call [`accessLevels.get`](/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/get).


```
GET https://accesscontextmanager.googleapis.com/v1alpha/accessPolicies/ POLICY_NAME /accessLevels/ LEVEL_NAME 
```


Where:

- 

POLICY_NAME is the name of your organization's access policy.

- 

LEVEL_NAME is the name of the access level you want to
describe.

### Request body

The request body must be empty.

### Optional parameters

Optionally, include the [`accessLevelFormat`](#accessLevelFormat)
query parameter. Normally, access levels are returned as they are defined,
either as `BasicLevel` or `CustomLevel`.

You can specify the value `CEL` for this parameter to return `BasicLevels`
as `CustomLevels` in Cloud Common Expression Language.

### Response body

If successful, the response body for the call contains an
[`AccessLevel`](/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel) resource that includes details about
what the access level does, the last time the level was updated, and more.



## Update an access level

This section describes how to update individual access levels. To update
all of your organization's access levels in one operation, see
[Making bulk changes to access levels](/access-context-manager/docs/bulk-operations).


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To update an access level:

- 

Open the **Access Context Manager** page in the Google Cloud Dedicated console.

[Open the Access Context Manager page](https://console.cloud.berlin-build0.goog/security/access-level)

- 

If you are prompted, select your organization.

- 

In the grid, click the name of the access level that you want to update.

- 

In the **Edit Access Level** pane, make changes to the access level.

For a complete list of the attributes that you can add or modify,
read about [access level attributes](/access-context-manager/docs/access-level-attributes).

- 

Click **Save**.

In addition to updating or removing any existing conditions,
you can add new conditions and add new attributes to existing
conditions.




Use the [`update`](/sdk/gcloud/reference/access-context-manager/levels/update) command to update an access level.

**Basic access level:**


```
gcloud access-context-manager levels update LEVEL_NAME \ 
--basic-level-spec = FILE \ 
[ --policy = POLICY_NAME ] 
```


**Custom access level:**


```
gcloud access-context-manager levels update LEVEL_NAME \ 
--custom-level-spec = FILE \ 
[ --policy = POLICY_NAME ] 
```


Where:

- 

LEVEL_NAME is the name of the access level that you want to
update.

- 

FILE is the name of a .yaml file that defines
[the conditions for the access level](/access-context-manager/docs/example-yaml-file) (for basic access levels)
or a [CEL expression](/access-context-manager/docs/custom-access-level-spec) that resolves to a single boolean
value (for custom access levels).

For a complete list of the attributes that you can use in your basic
access level conditions,
read about [access level attributes](/access-context-manager/docs/access-level-attributes).

- 

POLICY_NAME is the name of your organization's access policy.
This value is required only if you haven't set a
[default access policy](/access-context-manager/docs/manage-access-policy#set-default).

- 

You can include one or more of the following options.




| 
Options | 
|



| 
`combine-function` | 



This option is only used for *basic access levels*.



Determines how conditions are combined.



Valid values: `AND`, `OR`

| 
|

| 
`description` | 



A long-form description of the access level.

| 
|

| 
`title` | 



A short title for the access level. The access level's title
is displayed in the Google Cloud Dedicated console.

| 
|



You can include any of the [gcloud-wide flags](/sdk/gcloud/reference).

### Example command


```
gcloud access-context-manager levels update Device_Trust \ 
--basic-level-spec = corpdevspec.yaml \ 
--combine-function = OR \ 
--description = 'Access level that conforms to updated corporate spec.' \ 
--title = 'Device_Trust Extended' \ 
--policy = 1034095178592 
```



To update an access level, call [`accessLevels.patch`](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/patch).


```
PATCH https://accesscontextmanager.googleapis.com/v1/accessPolicies/ POLICY_NAME /accessLevels/ LEVEL_NAME ?updateMask= FIELDS 
```


Where:

- 

POLICY_NAME is the name of your organization's access policy.

- 

LEVEL_NAME is the name of the access level you want to
describe.

- 

FIELDS is a comma-separated list of
[fully-qualified field names](/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/patch#query-parameters) that you are updating.

### Request body

The request body must include an [`AccessLevel`](/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel)
resource that specifies the changes you want to make to the access level.

### Response body

If successful, the response body for the call contains an
[`Operation`](/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the
patch operation.



## Delete an access level


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To delete an access level:

- 

Open the **Access Context Manager** page in the Google Cloud Dedicated console

[Open the Access Context Manager page](https://console.cloud.berlin-build0.goog/security/access-level)

- 

If you are prompted, select your organization.

- 

In the grid, in the row for the access level that you want to delete,
click the * more_vert * button.

- 

Click **Delete**.

- 

In the dialog box that appears, confirm that you want to delete the
access level.




To delete an access level:

- 

Use the [`delete`](/sdk/gcloud/reference/access-context-manager/levels/delete) command to delete an access level.


```
gcloud access-context-manager levels delete LEVEL_NAME \ 
[ --policy = POLICY_NAME ] 
```


Where:

- 

LEVEL_NAME is the name of the access level that you want
to delete.

- 

POLICY_NAME is the name of your organization's
access policy. This value is required only if you haven't set a
[default access policy](/access-context-manager/docs/manage-access-policy#set-default).

- 

Confirm that you want to delete the access level.

For example:


```
You are about to delete level Device_Trust

Do you want to continue (Y/n)?


You should see output similar to the following:



Waiting for operation [accessPolicies/330193482019/accessLevels/Device_Trust/delete/1531171874311645] to complete...done.
Deleted level [Device_Trust].
```






To delete an access level, call [`accessLevels.delete`](/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/delete).


```
DELETE https://accesscontextmanager.googleapis.com/v1alpha/accessPolicies/ POLICY_NAME /accessLevels/ LEVEL_NAME 
```


Where:

- 

POLICY_NAME is the name of your organization's access policy.

- 

LEVEL_NAME is the name of the access level you want to
describe.

### Request body

The request body must be empty.

### Response body

If successful, the response body for the call contains an
[`Operation`](/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the
delete operation.