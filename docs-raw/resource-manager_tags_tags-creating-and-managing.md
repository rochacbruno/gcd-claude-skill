# Create and manage tags

Source: https://berlin.devsitetest.how/resource-manager/docs/tags/tags-creating-and-managing
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/resource-manager/docs/tpc-differences) for more details.














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

Resource Manager

](https://berlin.devsitetest.how/resource-manager/docs)






- 








[

Guides

](https://berlin.devsitetest.how/resource-manager/docs/resource-manager-overview)












# Create and manage tags 






- On this page ** 
- [ Before you begin ](#before_you_begin)

- [ Required roles ](#required-permissions)

- [ Create and define a new tag ](#creating)

- [ Create a tag key ](#creating_tag)
- [ Create tag keys with dynamic key values ](#create_dynamic_tags)
- [ View a tag key ](#retrieving_tag_key)
- [ Add tag values ](#add_tag_values)
- [ Retrieve tag values ](#retrieving_tag_value)
- [ Update existing tags ](#updating)
- [ List tag keys ](#listing_keys)
- [ List tag values ](#listing_values)

- [ Manage access to tags ](#managing_access)
- [ Attach tags to resources ](#attaching)
- [ Modify tags on resources ](#modify_dynamic_tags)

- [ Using gcloud CLI ](#using_gcloud)
- [ Using the API ](#using_api)
- [ List all tags attached to a resource ](#listing_tags)
- [ Detach a tag from a resource ](#detaching)

- [ Enforce mandatory tags on resources ](#enforcing_mandatory_tags)

- [ Set up a custom constraint to enforce tags ](#create_custom_constraint_tags)

- [ Protect tag values with tag holds ](#protecting_tags)

- [ Create tag holds ](#creating_holds)
- [ List tag holds ](#listing_holds)
- [ Remove tag holds ](#removing_holds)

- [ Delete tags ](#deleting)
- [ Policies and tags ](#policies)

- [ Identity and Access Management conditions and tags ](#iam_conditions_and_tags)
- [ Organization policies and tags ](#organization_policies_tags)

- [ System tags ](#system_tags)
- [ Supported services ](#supported_services)
- 










This guide describes how to create and manage tags. A tag is a key-value pair
that can be attached to a Google Cloud Dedicated in Germany resource. You can use tags to
conditionally allow or deny policies based on whether a supported resource has a
specific tag.

## Before you begin 

For more information about what tags are and how they work, see the
[Tags overview](/resource-manager/docs/tags/tags-overview).

### Required roles 







































































































To get the permissions that
you need to manage tags,

ask your administrator to grant you the
following IAM roles:













- [Tag Viewer ](/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)
on the resources the tags are attached to




- 
View and manage tags at the organization level:
[Organization Viewer ](/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`)
on the organization





- 
Attach and remove tags from resources:
[Tag User ](/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)
on the tag value and the resources that you are attaching or removing the tag value to





- 
Create, update, and delete tag definitions:
[Tag Administrator ](/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`)
on the resource you're creating, updating, or deleting tags for










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









## Create and define a new tag

Tags are a key-value pair, and are attached to a resource in your
Google Cloud Dedicated in Germany hierarchy. To create a new tag, you must first create a tag key
that describes the tag you are creating. For example, you might want to specify
production, test, and development environments for resources in your resource
hierarchy by creating a key with the name `environment`.

Then, you can create the different values that the key can have. If you created
a tag key named `environment`, you might want to specify that there are three
potential environments, and create a value for each: `production`,`development`,
and `test`.

Finally, you can attach these tags to resources, which carries with it the
key-value pair association. Attaching a tag key and value to a resource is also
known as creating a tag binding. For example, you could
attach `test` to multiple test environment folders across your
organization, and each one would carry the `environment: test` key-value pair.

You can also create tag keys that let users specify values *dynamically* when adding
tag binding to a resource. These are called dynamic tag values([Preview](https://berlin.devsitetest.how/products#product-launch-stages)).
You can configure validation rules for the dynamic tag values that let you enforce
specific formats, values, or constraints on the tags users create at the time of
resource attachment.

Dynamic tag values are useful when it's not practical to pre-define every possible tag
value. For example, attributes such as *owner*, *application Id*, *service Id*, or
*cost center* can have thousands of distinct values. Manually pre-defining and
maintaining such extensive lists of tag values creates a significant administrative
burden.

**Tag key and value limits**

You can create a maximum of 1000 tag keys within a given organization or within
a given project. These limits are independent; for example, tag keys created
under a project do not count towards the limit for the organization node. If you
need to exceed this default, you can request an increase to 10,000 tag keys per
organization or project by submitting a support request.

For predefined tag values, you can associate up to 1000 values per tag key by
default. This limit can also be increased to 10,000 tag values per key through a
support request. However, if you are using dynamic tag values, there is no upper
limit on the number of distinct tag values permissible per tag key.

Dynamic tag values can't be used in Identity and Access Management (IAM) conditions or
in Organization Policy Service constraints.

### Create a tag key

To begin, you need to create a tag key.

The tag key's `shortName` can have a maximum length of 256 characters. The
permitted character set for the `shortName` includes UTF-8 encoded Unicode
characters except single quotes (`'`), double quotes
(`"`), backslashes (`\`), and forward slashes
(`/`).

After the `shortName` has been created, it cannot be changed, and it must be
unique within the same namespace.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




To create a tag key, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the
organization or project under which you want to create a tag key.

- 

Click add **Create**.

- 

In the **Tag key** box, enter the display name of your tag key. This
becomes part of the namespaced name of your tag.

- 

In the **Tag key description** box, enter a description of your tag key.

- 

In the **Tag values** section, click **Predefined values** to create a
fixed list of allowed values.

- 

Click add **Add value** for each value
you want to create.

- 

In the **Tag value** box, enter the display name of your tag value. This
becomes part of the namespaced name of your tag.

- 

In the **Tag value description** box, enter a description of your tag
value.

- 

When you have finished adding tag values, click **Create tag key**.




To create a tag key, use the `gcloud resource-manager tags keys create`
command:


```
gcloud resource-manager tags keys create SHORT_NAME \
--parent= RESOURCE_ID 
```


Where:

- 

` SHORT_NAME ` is the display name for your tag key;
for example: `environment`.

- 

` RESOURCE_ID ` is the ID of the parent organization
or project resource for this tag key; for example:
`organizations/123456789012`, `projects/test-project123`, or
`projects/234567890123`. To learn how to get your organization ID, see
[Creating and managing organizations](/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
To learn how to get your project ID, see
[Creating and managing projects](/resource-manager/docs/creating-managing-projects#identifying_projects).

You should get a response similar to the following:


```
Creating tag key environment in organization 1234567890...

name: tagKeys/123456789012
short_name: environment
namespaced_name: 123456789012/environment
parent: organizations/123456789012
```



Before you create tag keys using Terraform, enable the
[Cloud Resource Manager API](/resource-manager/reference/rest).

You can use the
[`google_tags_tag_key`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/tags_tag_key)
resource to create a tag key.


```
resource "google_tags_tag_key" "key" {
parent = " RESOURCE "
short_name = " KEY_SHORT_NAME "
description = " DESCRIPTION "
}
```


To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).




To create a tag key, create a JSON representation of the key. For
more information about the format of a tag key, see the
[TagKey reference](/resource-manager/reference/rest/v3/tagKeys).

Then, use the
[tagKeys.create](/resource-manager/reference/rest/v3/tagKeys/create)
method:


```
POST https://cloudresourcemanager.googleapis.com/v3/tagKeys/ -d
```


Request JSON body:


```
{
"parent": RESOURCE_ID ,
"shortName": SHORT_NAME ,
"description": DESCRIPTION ,
}
```


Where:

- 

` SHORT_NAME ` is the display name for your tag key;
for example: `environment`.

- 

` RESOURCE_ID ` is the ID of the parent organization
or project resource for this tag key; for example:
`organizations/123456789012`, `projects/test-project123`, or
`projects/234567890123`. To learn how to get your organization ID, see
[Creating and managing organizations](/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
To learn how to get your project ID, see
[Creating and managing projects](/resource-manager/docs/creating-managing-projects#identifying_projects).

- 

` DESCRIPTION ` is a description of the key, and no
longer than 256 characters.




After you have created the key, you can find the unique human-readable display
name called the `namespacedName` that is namespaced within its parent
resource, and a globally unique permanent ID called the `name`.

### Create tag keys with dynamic key values

To create tag keys that support dynamic values, use one of the following methods:


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




To create a tag key, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the
organization or project under which you want to create a tag key.

- 

Click add **Create**.

- 

In the **Tag key** box, enter the display name of your tag key. This
becomes part of the namespaced name of your tag.

- 

In the **Tag key description** box, enter a description of your tag key.

- 

In the **Tag values** section, click **Dynamic values**, and then click
add **Add value constraints**.

- 

Define a validation regular expression to check the format of dynamically
created tag values. Only values matching the pattern you provide are allowed. By
default, the regular expression matches all values, for example `.*`.

- 

After defining the validation regular expression, click **Create tag key**.



```
gcloud resource-manager tags keys create SHORT_NAME \
--parent=RESOURCE_ID \
--allowed-values-regex=VALID_REGEX
```


Replace the following:

- 

` SHORT_NAME `: the display name for your tag key;
for example: `environment`.

- 

` RESOURCE_ID `: the ID of the parent organization
or project resource for this tag key; for example:
`organizations/123456789012`, `projects/test-project123`, or
`projects/234567890123`. To learn how to get your organization ID, see
[Creating and managing organizations](/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
To learn how to get your project ID, see
[Creating and managing projects](/resource-manager/docs/creating-managing-projects#identifying_projects).

- 

` VALID_REGEX `: a regular expression in
[RE2 syntax](https://github.com/google/re2/wiki/syntax) that defines
the allowed format for tag values associated with the newly created tag key
(only to validate dynamic values). To allow any value to be specified use
the regular expression `.*`.

You should get a response similar to the following:


```
allowedValuesRegex: '[abc]'
name: tagKeys/123456789012
shortName: environment
namespacedName: 123456789012/environment
parent: organizations/123456789012
```



Before you create tag keys using Terraform, enable the
[Cloud Resource Manager API](/resource-manager/reference/rest).

You can use the
[`google_tags_tag_key`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/tags_tag_key)
resource to create tag keys that support dynamic values.


```
resource "google_tags_tag_key" "key" {
parent = "organizations/123456789"
short_name = "keyname"
description = "For keyname resources."
allowed_values_regex = "^[a-z]+$"
}
```


To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).

Replace the following:




To create a tag key that supports dynamic tag values, create a JSON representation of the key. For
more information about the format of a tag key, see the
[TagKey reference](/resource-manager/reference/rest/v3/tagKeys).

Then, use the
[tagKeys.create](/resource-manager/reference/rest/v3/tagKeys/create)
method:


```
POST https://cloudresourcemanager.googleapis.com/v3/tagKeys/
```


Request JSON body:


```
{
"parent": RESOURCE_ID ,
"shortName": SHORT_NAME ,
"description": DESCRIPTION ,
"allowedValuesRegex": VALID_REGEX 
}
```


Replace the following:

- 

` RESOURCE_ID `: the ID of the parent organization or project resource for this tag key; for example:
`organizations/123456789012`, `projects/test-project123`, or
`projects/234567890123`. To learn how to get your organization ID, see
[Creating and managing organizations](/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
To learn how to get your project ID, see
[Creating and managing projects](/resource-manager/docs/creating-managing-projects#identifying_projects).

- 

` SHORT_NAME `: the display name for your tag key; for example: `environment`.

- 

` DESCRIPTION `: a description of the key, and no longer than 256 characters.

- 

` VALID_REGEX `: a regular expression that defines the allowed format for tag values associated with the newly created tag key.




After you have created the key, you can find the unique human-readable display
name called the `namespacedName` that is namespaced within its parent resource,
and a globally unique permanent ID called the `name`.

### View a tag key

You can find information about a particular tag key using the permanent ID or
namespaced name that is displayed when you created it.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To view a created tag, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the
organization or project that contains your tag.

- 

All tags in the selected organization or project appear in the list.
Click the tag for which you want to see the tag key.




To display the information related to a given tag key, use the
`gcloud resource-manager tags keys describe` command:


```
gcloud resource-manager tags keys describe TAGKEY_NAME 
```


` TAGKEY_NAME ` is the permanent ID or namespaced
name of the tag key for which you want to display information; for example:
`tagKeys/123456789012` or `project-id/environment`.

You should get a response similar to the following:


```
name: tagKeys/123456789012
short_name: environment
namespaced_name: 123456789012/environment
parent: organizations/123456789012
```


For tags with dynamic values, the response also contains the `allowedValuesRegex` field
that displays the RE2 regular expression used to validate any dynamic tag values
entered when the tag is applied to a resource.



To display the information related to a given tag key, use the
[tagKeys.get](/resource-manager/reference/rest/v3/tagKeys/get) method:


```
GET https://cloudresourcemanager.googleapis.com/v3/{name= TAGKEY_NAME }
```


` TAGKEY_NAME ` is the permanent ID of the tag key
for which you want to display information; for example:
`tagKeys/123456789012`.

To display the information related to a given tag key using its namespaced
name, use the
[`tagKeys.getNamespaced`](/resource-manager/reference/rest/v3/tagKeys/getNamespaced) method:


```
GET https://cloudresourcemanager.googleapis.com/v3/tagKeys/namespaced?name={ TAGKEY_NAMESPACED_NAME }
```


` TAGKEY_NAMESPACED_NAME ` is the namespaced name of the tag
key and is of the format `parentNamespace/tagKeyShortName`.

For tags with dynamic values, the response also contains the `allowedValuesRegex` field
that displays the RE2 regular expression used to validate any dynamic tag values
entered when the tag is applied to a resource.



### Add tag values

Once you have created a tag key, you can then add accepted values for the
key.

Your tag value's `shortName` must meet the following requirements:

- 

A `shortName` can have a maximum length of 256 characters.

- 

A `shortName` must begin with an alphanumeric character.

- 

A `shortName` can contain UTF-8 encoded Unicode characters except single
quotes (`'`), double quotes (`"`), backslashes
(`\`), and forward slashes (`/`).

- 

A `shortName` cannot be changed once it has been created, and must be unique
within the same namespace.


[ Console ](#console) [ gcloud ](#gcloud) [Terraform](#terraform) [ API ](#api) 
More 




To add a tag value, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the
organization or project under which you want to create a tag value.

- 

In the list of tags, click the tag to which you want to add a new value.

- 

In the **Tag values** section, click **Predefined values** to create a
fixed list of allowed values.

- 

Click add **Add value** for each value
you want to create.

- 

In the **Tag value** box, enter the display name of your tag value. This
becomes part of the namespaced name of your tag.

- 

In the **Tag value description** box, enter a description of your tag
value.

- 

Click **Save**.




To create a tag value, use the `gcloud resource-manager tags values
create` command. You must specify the key under which this value is created:


```
gcloud resource-manager tags values create TAGVALUE_SHORTNAME \
--parent= TAGKEY_NAME 
```


Where:

- 

` TAGVALUE_SHORTNAME ` is the short name of the new
tag value; for example: `production`.

- 

` TAGKEY_NAME ` is the permanent ID or namespaced
name of the parent tag key; for example: `tagKeys/4567890123`.

You should get a response similar to the following:


```
Creating tag value production in tag key 123456789012/environment...

name: tagValues/7890123456
short_name: production
namespaced_name: 123456789012/environment/production
parent: tagKeys/123456789012
```



Use the
[`google_tags_tag_value`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/tags_tag_value)
resource.

Before you create tag values using Terraform, enable the
[Cloud Resource Manager API](/resource-manager/reference/rest).

The following example creates tag values named `prod` and `sales`:




















```
data "google_project" "default" {}

resource "google_tags_tag_key" "env_tag_key" {
parent = "projects/${data.google_project.default.project_id}"
short_name = "env1"
}

resource "google_tags_tag_key" "department_tag_key" {
parent = "projects/${data.google_project.default.project_id}"
short_name = "department1"
}

resource "google_tags_tag_value" "env_tag_value" {
parent = "tagKeys/${google_tags_tag_key.env_tag_key.name}"
short_name = "prod"
}

resource "google_tags_tag_value" "department_tag_value" {
parent = "tagKeys/${google_tags_tag_key.department_tag_key.name}"
short_name = "sales"
}
```



To apply your Terraform configuration in a Google Cloud Dedicated project, complete the steps in the
following sections.

## Prepare Cloud Shell


- Launch [Cloud Shell](https://shell.cloud.google.com/).

- 


Set the default Google Cloud Dedicated project
where you want to apply your Terraform configurations.




You only need to run this command once per project, and you can run it in any directory.


```
export GOOGLE_CLOUD_PROJECT= PROJECT_ID 
```



Environment variables are overridden if you set explicit values in the Terraform
configuration file.



## Prepare the directory

Each Terraform configuration file must have its own directory (also
called a *root module*).


- 
In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new
file within that directory. The filename must have the
`.tf` extension—for example `main.tf`. In this
tutorial, the file is referred to as `main.tf`.

```
mkdir DIRECTORY && cd DIRECTORY && touch main.tf
```



- 


If you are following a tutorial, you can copy the sample code in each section or step.



Copy the sample code into the newly created `main.tf`.



Optionally, copy the code from GitHub. This is recommended
when the Terraform snippet is part of an end-to-end solution.




- Review and modify the sample parameters to apply to your environment.

- Save your changes.

- 
Initialize Terraform. You only need to do this once per directory.

```
terraform init
```



Optionally, to use the latest Google provider version, include the `-upgrade`
option:



```
terraform init -upgrade
```



## Apply the changes


- 
Review the configuration and verify that the resources that Terraform is going to create or
update match your expectations:

```
terraform plan
```



Make corrections to the configuration as necessary.



- 
Apply the Terraform configuration by running the following command and entering `yes`
at the prompt:

```
terraform apply
```



Wait until Terraform displays the "Apply complete!" message.



- [Open your Google Cloud Dedicated project](https://console.cloud.berlin-build0.goog/) to view
the results. In the Google Cloud Dedicated console, navigate to your resources in the UI to make sure
that Terraform has created or updated them.





To create a tag value, create a JSON representation of the value.
For more information about the format of a tag value, see the
[TagValue reference](/resource-manager/reference/rest/v3/tagValues).

Then, use the
[tagValues.create](/resource-manager/reference/rest/v3/tagValues/create)
method:


```
POST https://cloudresourcemanager.googleapis.com/v3/tagValues/ -d
```


Request JSON body:


```
{
"parent": TAGKEY_NAME ,
"shortName": SHORT_NAME ,
"description": DESCRIPTION ,
}
```


Where:

- 

` TAGKEY_NAME ` is the permanent ID of the parent tag
key; for example:`tagKeys/4567890123`.

- 

` SHORT_NAME ` is the display name for your tag value;
for example: `environment`.

- 

` DESCRIPTION ` is a description of the value, and no
longer than 256 characters.




After you have created the value, you can find the unique human-readable display
name called the `namespacedName` that is namespaced within its parent
resource, and a globally unique permanent ID called the `name`.

#### Add tag values to dynamic tag keys

For tag keys that support dynamic tag values, provide the tag value when you
attach the tag to a resource. The system checks the dynamic value against the
validation regular expression defined for that tag key. If the value you provide
doesn't match the configured validation regular expression, you'll get an error.

Resources inherit dynamic tag value bindings from their parent resources.

Note that tag keys that support dynamic tag values *can't* also have predefined tag values.

### Retrieve tag values

You can find information about a particular tag value using the permanent ID or
namespaced name that is displayed when you created it. This applies only to
predefined tag values, not dynamic tag values.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To view a created tag, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the
organization or project that contains your tag.

- 

All tags you have created under this organization or project appear in
the list. Click the tag for which you want to see tag values.




To display the information related to a given tag value, use the
`gcloud resource-manager tags values describe` command:


```
gcloud resource-manager tags values describe TAGVALUE_NAME 
```


` TAGVALUE_NAME ` is the permanent ID or
namespaced name of the tag value; for example:
`tagValues/4567890123` or `123456789012/environment/production`.

You should get a response similar to the following:


```
name: tagValues/456789012345
short_name: production
namespaced_name: 123456789012/environment/production
parent: tagKeys/123456789012
```



To display the information related to a given tag value, use the
[tagValues.get](/resource-manager/reference/rest/v3/tagValues/get) method:


```
GET https://cloudresourcemanager.googleapis.com/v3/{name= TAGVALUE_NAME }
```


` TAGVALUE_NAME ` is the permanent ID of the tag
value; for example: `tagValues/4567890123`.

To display the information related to a given tag value using its namespaced
name, use the
[tagValues.getNamespaced](/resource-manager/reference/rest/v3/tagValues/getNamespaced) method:


```
GET https://cloudresourcemanager.googleapis.com/v3/tagValues/namespaced?name={ TAGVALUE_NAMESPACED_NAME }
```


` TAGVALUE_NAMESPACED_NAME ` is the namespaced
name of the tag value and is of the format
`parentNamespace/tagKeyShortName/tagValueShortName`.



When referencing tags using the Google Cloud CLI, you can use either the
namespaced name or the permanent ID for tag keys and values. Calls to the API
except `getNamespaced` should only use the permanent ID. See
[Tag definitions and identifiers](/iam/docs/tags-access-control#definitions)
for more information about the types of identifiers a tag uses.

### Update existing tags

You can modify an existing tag by updating the key or values associated with it.
You can update a tag description, but not the short name. For tags with dynamic values,
you can update both the description and the validation regular expression that defines
the allowed format for tag values associated with the tag key. Changes to the
`allowed_values_regex` field don't apply retroactively and won't
affect existing tag bindings for the tag key.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To update a tag key's description, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the organization
or project that contains your tag key.

- 

Click more_vert **Actions** next to
the tag key you want to update, then click **View details**.

- 

Click edit **Edit** next
to **Description** near the top of the screen.

- 

Depending on what you want to update, select one of the following:

- **Description**: Click edit **Edit** next to **Description**.

- **Validation regular expression**: Click edit **Edit** next
to **Validation regular expression**.

- 

In the edit panel that opens, update the description or enter your new
pattern in the **Allowed value regex** field.

- 

Click **Save**.




To modify a tag key description, use the
`gcloud resource-manager tags keys update` command:


```
gcloud resource-manager tags keys update TAGKEY_NAME \
--description= NEW_DESCRIPTION 
```


Where:

- 

` TAGKEY_NAME ` is the permanent ID or namespaced
name of the key to be updated; for example: `tagKeys/123456789012`.

- 

` NEW_DESCRIPTION ` is a string of no more than 256
characters to use as the new description.

You should get a response similar to the following:


```
name: tagKeys/123456789012
short_name: environment
namespaced_name: 123456789012/environment
description: "new description"
parent: organizations/123456789012
```



To modify a tag key description, use the
[tagKeys.patch](/resource-manager/reference/rest/v3/tagKeys/patch) method:


```
PATCH https://cloudresourcemanager.googleapis.com/v3/{tagKey.name= TAGKEY_NAME } -d
```


Request JSON body:


```
{
"description": DESCRIPTION ,
}
```


Where:

- 

` TAGKEY_NAME ` is the permanent ID of the tag key;
for example: `tagKeys/123456789012`.

- 

` DESCRIPTION ` is a description of the key, and no
longer than 256 characters.




You can also change the description of tag values.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To update a tag value's description, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the organization
or project that contains your tag value.

- 

Click more_vert **Actions** next to
the tag key for the value you want to update, then click
**View details**.

- 

Click more_vert **Actions** next to
the tag value you want to update, then click **View details**.

- 

Click edit **Edit** next
to **Description** and edit the description of the tag value.

- 

Click **Save**.




To modify a tag value description, use the
`gcloud resource-manager tags values update` command:


```
gcloud resource-manager tags values update TAGVALUE_NAME \
--description=" NEW_DESCRIPTION "
```


Where:

- 

` TAGVALUE_NAME ` is the permanent ID or namespaced
name of the tag value to be updated; for example:
`tagValues/4567890123`.

- 

` NEW_DESCRIPTION ` is a string of no more than 256
characters to use as the new description.

You should get a response similar to the following:


```
short_name: production
namespaced_name: 123456789012/environment/production
parent: tagKeys/123456789012
description: "new description"
```



To modify a tag value description, use the
[tagValues.patch](/resource-manager/reference/rest/v3/tagValues/patch)
command:


```
PATCH https://cloudresourcemanager.googleapis.com/v3/{tagKey.name= TAGVALUE_NAME } -d
```


Request JSON body:


```
{
"description": DESCRIPTION ,
}
```


Where:

- 

` TAGVALUE_NAME ` is the permanent ID name of the tag
value; for example: `tagValues/4567890123`.

- 

` DESCRIPTION ` is a description of the key, and no
longer than 256 characters.




### List tag keys

You can list all tag keys associated with a particular organization or project
resource using the Google Cloud Dedicated console, the gcloud CLI, or with a
call to the API.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To view all tags:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the organization
or project that contains your tags.

- 

All tags you have created under this organization or project appear in
the list.




To return a list of all tag keys created under a organization or a project resource, use
the `gcloud resource-manager tags keys list` command:


```
gcloud resource-manager tags keys list --parent= RESOURCE_ID 
```


` RESOURCE_ID ` is the ID of the organization or
project resource for which you want to find attached tag keys.

- An organization or project ID should be provided in the format
`organizations/ ORGANIZATION_ID ` or
`projects/ PROJECT_NAME `;
for example: `organizations/123456789012` and
`projects/test-project123`. To learn how to get your organization ID,
see
[Creating and managing organizations](/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
To learn how to get your project ID, see
[Creating and managing projects](/resource-manager/docs/creating-managing-projects#identifying_projects).
You should get a response similar to the following:


```
NAME SHORT_NAME DESCRIPTION
tagKeys/123456789012 environment description of tag key
```



To return a list of all tag keys for a given resource, use the
[tagKeys.list](/resource-manager/reference/rest/v3/tagKeys/list) method,
with the parent resource specified in the query:


```
GET https://cloudresourcemanager.googleapis.com/v3/tagKeys

{
"parent": " RESOURCE_ID "
}
```


` RESOURCE_ID ` is the ID of the organization or
project resource for which you want to find attached tag keys; for example:
`organizations/123456789012` and `projects/test-project123`.



### List tag values

You can list all tag values associated with a particular tag key using the
Google Cloud Dedicated console, the gcloud CLI, or with a call to the API.

For tag keys that support dynamic values, the console displays the validation
regular expression defined by the user instead of the list of tag values created
under the tag key.

The gcloud CLI command and REST API fetch only the predefined tag values, not the
dynamic tag values.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To view all tag values attached to a tag key, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the
organization or project that contains your tag key.

- 

Click more_vert **Actions** next to
the tag key containing the tag values you want to find, then click
**View details**.

- 

All tag values you have created under this tag key appear in the list.
For dynamic tag keys, you'll see the validation regular expression defined
for this tag key instead of a list of individual values.




To return a list of all tag values attached to a key, use the
`gcloud resource-manager tags values list` command:


```
gcloud resource-manager tags values list --parent= TAGKEY_NAME 
```


` TAGKEY_NAME ` is the permanent ID or namespaced
name of the tag key for which you want to find attached values; for example:
`tagKeys/123456789012` or `1234567/environment`.

You should get a response similar to the following:


```
NAME SHORT_NAME
tagValues/123456789012 production
```



To return a list of all tag values attached to a key, use the
[tagValues.list](/resource-manager/reference/rest/v3/tagValues/list) method,
with the parent tag key specified in the query:


```
GET https://cloudresourcemanager.googleapis.com/v3/tagValues

{
"parent": " TAGKEY_NAME "
}
```


` TAGKEY_NAME ` is the permanent ID name of the
tag key; for example: `tagKeys/123456789012`.



## Manage access to tags

You can give users specific access to manage tags and attach tag values to
resources using the Google Cloud Dedicated console. See
[Required permissions](#required-permissions) for a list of the roles related to
tags, and the permissions they contain.


[ Tag keys ](#tag-keys) [ Tag values ](#tag-values) 
More 




To manage access for users on a tag key, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the organization
or project that contains the tag key on which you want to manage access.

- 

Click the checkbox next to the tag for which you want to manage access.

- 

Click person **Manage access**.

- 

To add a role to a principal, click
person_add **Add principal**.

- 

In the **New principals** text box, enter the email address of the
principal you want to grant a new role.

- 

Select a role from the **Select a role** dropdown menu. If you want to
add more than one role, click
add **Add another role**.

- 

Click **Save**.

- 

To edit a principal's role, click
edit **Edit** next to the principal
you want to edit.

- 

You can change any roles that are assigned to the principals on this
tag by clicking on the **Role** dropdown menu and choosing a new role.

- 

If you want to add more roles, click
add **Add another role**.

- 

To delete a role from this principal on this tag, click
delete **Delete role** next to the
role you want to delete.

- 

Click **Save**.

- 

To delete a principal's role, click
delete **Delete role** next to the
role you want to delete.

- Click **Remove.**




To manage access for users on a tag value, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the organization
or project that contains the tag key for which you want to manage access.

- 

Click more_vert **Actions** next to
the tag key for the value for which you want to manage access, then click
**View details**.

- 

Click person **Manage access**.

- 

To add a role to a principal, click
person_add **Add principal**.

- 

In the **New principals** text box, enter the email address of the
principal you want to grant a new role.

- 

Select a role from the **Select a role** dropdown menu. If you want to
add more than one role, click
add **Add another role**.

- 

Click **Save**.

- 

To edit a principal's role, click
edit **Edit** next to the principal
you want to edit.

- 

You can change any roles that are assigned to the principals on this
tag by clicking on the **Role** dropdown menu and choosing a new role.

- 

If you want to add more roles, click
add **Add another role**.

- 

To delete a role from this principal on this tag, click
delete **Delete role** next to the
role you want to delete.

- 

Click **Save**.

- 

To delete a principal's role, click
delete **Delete role** next to the
role you want to delete.

- Click **Remove.**




## Attach tags to resources

After a tag is created and appropriate
[access is granted](#required-permissions) to both the tag and the resource, the
tag can be attached to a Google Cloud Dedicated in Germany resource as a key-value pair. Exactly one
value can be attached to a resource for a given key. For example, if
`environment: development` is attached, then `environment: production` or
`environment: test` cannot be attached.
Each resource can have a maximum of 50 key-value pairs attached.

Tags are attached to resources by creating a tag binding resource that links
the value to the Google Cloud Dedicated in Germany resource. The following workflow describes how to
attach a tag to an organization, folder, or project resource. For details about
how to attach tags to another type of resource, see the documentation for that
resource in
[Services that support tags](/resource-manager/docs/tags/tags-supported-services).


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To attach a tag to an organization, folder, or project resource, do the
following:

- 

Open the **Manage resources** page in the Google Cloud Dedicated console.

[Open Manage resources page](https://console.cloud.berlin-build0.goog/cloud-resource-manager) 

- 

Click the organization, folder, or project to which you want to attach
a tag.

- 

Click label_important Tags**.

- 

In the **Tags** panel, click **Select scope**.

- 

Select the organization or project that contains your tags, and then
click **Open**.

- 

In the **Tags** panel, select **Add tag**.

- 

In the **Key** field, select the key for the tag you want to attach from
the list. You can filter the list by typing keywords.

- 

For tags with predefined values, select the value to attach from the **Value**
drop-down menu. You can filter the list by typing keywords.

- 

For tags with dynamic values, enter a string that matches the
validation regular expression configured for that tag key.

- 

If you want to attach more tags, click
add **Add Tag**, and then select the
key and value for each.

- 

Click **Save**.

- 

In the **Confirm** dialog, click **Confirm** to attach the tag.

- 

A notification confirms that your tags are updated. The new tags appear under
the **Tags** column on the **Manage resources** page.




To attach a tag to a resource, you must create a tag binding resource by
using the `gcloud resource-manager tags bindings create` command:


```
gcloud resource-manager tags bindings create \
--tag-value= TAGVALUE_NAME \
--parent= RESOURCE_ID \
--location= LOCATION 
```


Where:

- 

` TAGVALUE_NAME ` is the permanent ID or
namespaced name of the tag value to be attached; for example:
`tagValues/4567890123` or `12345678/environment/production`. For tags with dynamic values,
provide only the namespaced name because dynamic tag values don't have an ID.

- 

` RESOURCE_ID ` is the full ID of the resource,
including the API domain name to identify the type of resource
(`//cloudresourcemanager.googleapis.com/`). For
example, to attach a tag to `projects/7890123456`, the full ID would be:
`//cloudresourcemanager.googleapis.com/projects/7890123456`.

- 

` LOCATION ` is the location of your resource. If you
are attaching a tag to a global resource, such as a folder or a project,
you should omit this flag. If you are attaching a tag to a regional
resource, such as a Compute Engine instance, you must specify the
location; for example: `us-central1`.




To attach a tag to a resource, you must first create a JSON representation
of a tag binding that includes the permanent ID or namespaced name of the
tag value and the permanent ID of the resource. For more information about
the format of a tag binding, see the
[TagBinding reference](/resource-manager/reference/rest/v3/tagBindings).

If you are attaching the tag to a global resource such as an organization,
use the
[tagBindings.create](/resource-manager/reference/rest/v3/tagBindings/create)
method with the global endpoint hostname:


```
POST https://cloudresourcemanager.googleapis.com/v3/tagBindings
```


If you are attaching the tag to a regional resource, such as a
Compute Engine instance, use the `tagBindings.create` method with
the regional endpoint where your resource is located.


```
POST https:// LOCATION -cloudresourcemanager.googleapis.com/v3/tagBindings
```


Request JSON body:


```
{
"parent": RESOURCE_ID ,
"tagValue": TAGVALUE_NAME ,
}
```


OR


```
{
"parent": RESOURCE_ID ,
"tagValueNamespacedName": TAGVALUE_NAMESPACED_NAME ,
}
```


Where:

- 

` RESOURCE_ID ` is the full ID of the resource,
including the API domain name to identify the type of resource
(`//cloudresourcemanager.googleapis.com/`). For
example, to attach a tag to `projects/7890123456`, the full ID would be:
`//cloudresourcemanager.googleapis.com/projects/7890123456`.

- 

` TAGVALUE_NAME ` is the permanent ID of the tag value
that is attached; for example: `tagValues/4567890123`.

- 

` TAGVALUE_NAMESPACED_NAME ` is the namespaced name of
the tag value that is attached and is of the format:
`parentNamespace/tagKeyShortName/tagValueShortName`. Tags with dynamic values
can be attached using namespaced name only, because dynamic tag values don't
have an ID.




## Modify tags on resources

You can perform bulk operations to modify tags in the following ways:

- Clear all tag bindings: remove all existing tag bindings from the
resource.

- Replace tag bindings: replace all existing tag bindings on the
resource with a new set of key-value pairs.

- Remove tag bindings: remove specific tag bindings from the resource.

To clear, replace, and remove tag bindings, you can use either the
[`gcloud alpha resource-manager tags bindings update`](/sdk/gcloud/reference/alpha/resource-manager/tags/bindings/update)
command in gcloud CLI or the [locations.tagBindingCollections.patch](/resource-manager/reference/rest/v3/locations.tagBindingCollections/patch)
method if using the API.

### Using gcloud CLI

The gcloud CLI provides the following options for modifying tag bindings:

#### Remove all tags from a resource

To remove all tags from a resource, use the
`--clear-tags` flag with the
[`gcloud alpha resource-manager tags bindings update`](/sdk/gcloud/reference/alpha/resource-manager/tags/bindings/update) command.


[ gcloud ](#gcloud) 
**More 



```
gcloud alpha resource-manager tags bindings update \
--resource-name= RESOURCE_NAME \
--clear-tags
```


Replace ` RESOURCE_NAME ` with the full resource name of the
resource.



#### Remove specific tags from a resource

To remove specific tags from a resource, use the `--remove-tags`
flag with the [`gcloud alpha resource-manager tags bindings update`](/sdk/gcloud/reference/alpha/resource-manager/tags/bindings/update) command.


[ gcloud ](#gcloud) 
More 



```
gcloud alpha resource-manager tags bindings update \
--resource-name= RESOURCE_NAME \
--remove-tags= TAG_KEY_NAMESPACED_NAME 
```


Replace the following:

- ` RESOURCE_NAME `: the full resource
name of the tag binding to remove.

- ` TAG_KEY_NAMESPACED_NAME `: the namespaced name of the
tag key (for example, `123456789012/environment` or `my-project-123/cost-center`).

You can specify multiple tag key namespaced names as a comma-separated list. For
example: `--remove-tags=123456789012/environment,my-project-123/cost-center`.



#### Replace tags

To replace all existing tag bindings on a resource with new key-value pairs,
use the `--replace-tags` flag with the [`gcloud alpha resource-manager tags bindings update`](/sdk/gcloud/reference/alpha/resource-manager/tags/bindings/update) command.


[ gcloud ](#gcloud) 
More 



```
gcloud alpha resource-manager tags bindings update \
--resource-name= RESOURCE_NAME \
--replace-tags= TAG_KEY_NAMESPACED_NAME = TAG_VALUE_SHORT_NAME 
```


Replace the following:

- ` RESOURCE_NAME `: the full resource
name of the resource.

- ` TAG_KEY_NAMESPACED_NAME `: the namespaced name of the
tag key (for example, `123456789012/environment` or `my-project-123/cost-center`).

- ` TAG_VALUE_SHORT_NAME `: the short name of the tag value.

You can specify multiple key-value pairs as a comma-separated list. For
example: `--replace-tags=123456789012/environment=dev,my-project-123/cost-center=frontend`.



### Using the API

The request body of the `locations.tagBindingCollections.patch` method accepts
a JSON object representing the tags map, where keys and values are strings. The API
uses this *map* to perform all tag operations—including clear, replace, and remove,
as a single bulk operation. The API supports only `PUT` semantics. When you send a
request, the API replaces all current bindings attached to a resource with the new
set of bindings provided in your request map.

When you send a tags map to the API, the API processes it against the resource's
current tags as follows:

- Clear: Sending an empty tags map ({}) removes all existing tag bindings from the
resource.

- Remove: Any existing key-value pair on the resource that is not included in your
provided tags map is removed.

- Replace: A non-empty tags map replaces all existing tags on the resource with
the new tags that you provide.

### List all tags attached to a resource

You can get a list of all tags attached to a resource, for tags that are either
inherited or directly attached.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To see all tags that are attached to or inherited by a resource, do the
following:

- 

Open the **Manage resources** page in the Google Cloud Dedicated console.

[Open Manage resources page](https://console.cloud.berlin-build0.goog/cloud-resource-manager) 

- 

Find your organization, folder, or project in the list of resources.

- 

The tags attached to the resource appear under the **Tags** column. Tags
that are inherited will be marked as
lan Inherited**.




To get a list of tag bindings directly attached to a resource, use the
`gcloud resource-manager tags bindings list` command. If you add the
`--effective` flag, you will also return a list of tags inherited by this
resource.


```
gcloud resource-manager tags bindings list \
--parent= RESOURCE_ID \
--location= LOCATION 
```


Where:

- 

` RESOURCE_ID ` is the full ID of the resource; for
example: `//cloudresourcemanager.googleapis.com/projects/7890123456`

- 

` LOCATION ` is the location of your resource. If you
are listing the tags attached to a global resource, such as a folder or
a project, you should omit this flag. If you are attaching a tag to a
regional resource, such as a Compute Engine instance, you must
specify the location; for example: `us-central1`.

You should get a response similar to the following:

For predefined tags:


```
tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2FPROJECT_NUMBER%2Flocations%2FLOCATION%2Fresources%2FRESOURCE_ID/tagValues/TAG_VALUE_ID
parent: //cloudresourcemanager.googleapis.com/projects/123456789012/locations/us-central1/example-resource/res-01
tagValue: tagValues/987654321098
tagValueNamespacedName: 961309089256/environment/production
```


For tags with dynamic values:


```
tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2FPROJECT_NUMBER%2Flocations%2FLOCATION%2Fresources%2FRESOURCE_ID/tagKeys/TAG_KEY_ID
parent: //cloudresourcemanager.googleapis.com/projects/123456789012/locations/us-central1/example-resource/res-01
tagValueNamespacedName: your-org-id/environment/staging
```


For tags with dynamic values, the `tagValue` field is not present in the response; only
the `tagValueNamespacedName` is populated.

If you add the `--effective` flag to the `tags bindings list` command, you
will also return a list of all tags inherited by this resource. You should
get a response similar to the following:

For predefined tags:


```
inherited: true
namespacedTagKey: 433637338589/environment
namespacedTagValue: 433637338589/environment/production
tagKey: tagKeys/162008917964
tagKeyParentName: organizations/433637338589
tagValue: tagValues/281482214193975
```


For tags with dynamic values:


```
inherited: true
namespacedTagKey: my-sample-org/dynamic-key
namespacedTagValue: my-sample-org/dynamic-key/staging
tagKey: tagKeys/281476834141096
tagKeyParentName: projects/357710452272
```


If all tags evaluated on a resource are directly attached, the `inherited`
field is false and is omitted.



To get a list of tag bindings directly attached to a global resource such as
an organization, use the
[tagBindings.list](/resource-manager/reference/rest/v3/tagBindings/list)
method, specifying the parent resource in the query:


```
GET https://cloudresourcemanager.googleapis.com/v3/tagBindings

{
"parent": " RESOURCE_ID "
}
```


If you want to list the tag bindings attached to a regional resource,
such as Compute Engine instances, use the `tagBindings.list` method
with the regional endpoint where your resource is located.


```
GET https:// LOCATION -cloudresourcemanager.googleapis.com/v3/tagBindings

{
"parent": " RESOURCE_ID "
}
```


Where:

- 

` RESOURCE_ID ` is the full ID of the resource; for
example:
`//cloudresourcemanager.googleapis.com/projects/7890123456`.

- 

` LOCATION ` is the regional endpoint for your
resource; for example: `us-central1`.

If successful, the response body should include a list of `TagBinding`
objects. For example:


```
name: tagBindings/cloudresourcemanager.googleapis.com/projects/7890123456/567890123456
tagValue: tagValues/567890123456
tagValueNamespacedName: example-org/cost-center/1000
resource: //cloudresourcemanager.googleapis.com/projects/7890123456
```


For tags with dynamic values, the `tagValue` field is not present in the response; only
the `tagValueNamespacedName` is populated.



### Detach a tag from a resource

You can detach a tag from a resource by deleting the tag binding resource.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
**More 




To detach a tag from an organization, folder, or project resource, do the
following:

- 

Open the **Manage resources** page in the Google Cloud Dedicated console.

[Open Manage resources page](https://console.cloud.berlin-build0.goog/cloud-resource-manager) 

- 

Click the organization, folder, or project from which you want to
detach a tag.

- 

Click label_important Tags**.

- 

In the **Tags** panel, next to the tag you want to detach, click
delete **Delete item**.

- 

Click **Save**.

- 

In the **Confirm** dialog, click **Confirm** to detach the tag.

- 

A notification confirms that your tags are updated. The updated list of tags
appears under the **Tags** column on the **Manage resources** page.




To delete a tag binding, use the
`gcloud resource-manager tags bindings delete` command:


```
gcloud resource-manager tags bindings delete \
--tag-value= TAGVALUE_NAME \
--parent= RESOURCE_ID \
--location= LOCATION 
```


Where:

- 

` TAGVALUE_NAME ` is the permanent ID or namespaced
name of the tag value that is attached; for example:
`tagValues/567890123456`. For tags with dynamic values,
provide only the namespaced name because dynamic tag values don't have an ID.

- 

` RESOURCE_ID ` is the full ID of the resource. For
example: `//cloudresourcemanager.googleapis.com/projects/7890123456`

- 

` LOCATION ` is the location of your resource. If you
are deleting a tag binding that is attached to a global resource, such
as a folder or a project, you should omit this flag. If you are deleting
a tag binding attached to a regional resource, such as a
Compute Engine instance, you must specify the location; for
example: `us-central1`.




To delete a tag binding that is attached to a global resource such as an
organization, use the
[tagBindings.delete](/resource-manager/reference/rest/v3/tagBindings/delete)
method:


```
DELETE https://cloudresourcemanager.googleapis.com/v3/{name= TAGBINDINGS_NAME }
```


If you want to delete a tag binding that is attached to a regional resource,
such as a Compute Engine instance, use the `tagBindings.delete`
method with the regional endpoint where your resource is located.


```
DELETE https:// LOCATION -cloudresourcemanager.googleapis.com/v3/{name= TAGBINDINGS_NAME }
```


Where:

- 

` TAGBINDINGS_NAME ` is the permanent ID of the
TagBinding. For predefined tags, the format is
`tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F1234567890/tagValues/567890123456`.
For tags with dynamic values, the format is
`tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F1234567890/tagKeys/12345678`.

- 

` LOCATION ` is the regional endpoint for your
resource; for example: `us-central1`.




## Enforce mandatory tags on resources



To enforce mandatory tags on resources, create a custom organization policy and
set the policy on an organization, folder, or project resource to enforce the
custom constraint.

To learn more about tags enforcement, see
[Enforcement of mandatory tags using organization policies](/resource-manager/docs/tags/tags-overview#enforce_tags).

### Set up a custom constraint to enforce tags


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.berlin-build0.goog/iam-admin/orgpolicies) 

- 

Select the project picker at the top of the page.

- 

From the project picker, select the organization where you want to
enforce the custom constraint.

- 

[Set up a custom constraint](/resource-manager/docs/organization-policy/creating-managing-custom-constraints#set_up_custom_constraint)
with the following parameters:

- **Enforcement method**: `Govern tags`

- **Resource type**: the fully qualified name of the Google Cloud Dedicated
REST resource that you want to enforce mandatory tags on, for example,
`file.googleapis.com/Instance`

- **Condition**: a Common Expression Language (CEL) condition specifying
the tag keys that you want to enforce on the resource, for example
`resource.hasDirectTagKey("1234567890/owner")` to enforce a tag binding for
the tag key `1234567890/owner`. The `resource.hasDirectTagKey` CEL function
only matches tags directly applied to a resource and doesn't consider
tags inherited from ancestors in the resource hierarchy.

- **Action**: `Allow` or `Deny`.

- Allow: If the specified condition is met, the action to create or update
the resource is permitted.

- Deny: If the specified condition is met, the action to create or update
the resource is blocked.

- 

Click **Create constraint**.




Create a YAML file for the custom constraint:


```
name : organizations/ ORGANIZATION_ID /customConstraints/ CONSTRAINT_NAME 
resourceTypes : 
- RESOURCE_NAME 
methodTypes : 
- GOVERN_TAGS 
condition : " CONDITION " 
actionType : ACTION 
displayName : DISPLAY_NAME 
description : DESCRIPTION 
```


Replace the following:

- 

` ORGANIZATION_ID `: your organization ID, such as
`1234567890`.

- 

` CONSTRAINT_NAME `: the name you want for your new
custom constraint. A custom constraint must start with `custom.`, and can
only include uppercase letters, lowercase letters, or numbers, for
example, `custom.enforceMandatoryTags`.

- 

` RESOURCE_NAME `: the fully qualified name of the
Google Cloud Dedicated REST resource that you want to enforce mandatory tags on,
for example, `file.googleapis.com/Instance`.

- 

` CONDITION `: a Common Expression Language (CEL) condition
specifying the tag keys that you want to enforce on the resource, for example
`resource.hasDirectTagKey("1234567890/owner")` to enforce a tag binding for
the tag key `1234567890/owner`.

- 

` ACTION `: the action to take if the `condition` is
met. This can be either `ALLOW` or `DENY`.

The deny action means that if the specified condition is met, the
operation to create or update the resource is blocked.

The allow action means that if the specified condition is met,
the operation to create or update the resource is permitted. This also
means that every other case except the one explicitly listed in the
condition is blocked.

- 

` DISPLAY_NAME `: a human-friendly name for the
constraint. This field has a maximum length of 200 characters.

- 

` DESCRIPTION `: a human-friendly description of the
constraint to display as an error message when the policy is violated. This
field has a maximum length of 2000 characters.

[Set up the custom constraint](/resource-manager/docs/organization-policy/creating-managing-custom-constraints#set_up_custom_constraint) to make it
available for organization policies in your organization.



After you've defined the custom constraint, you can
[test and analyze the organization policy changes](/resource-manager/docs/organization-policy/creating-managing-custom-constraints#test_and_analyze) and
[enforce the constraint](/resource-manager/docs/organization-policy/creating-managing-custom-constraints#enforcing_custom_constraints).

## Protect tag values with tag holds

A tag hold is a resource that you can create to protect a tag value from being
deleted. If a tag value has a tag hold, it cannot be deleted by users unless the
tag hold is first deleted.

Tag holds can't be applied on dynamic tag values.

### Create tag holds

You can manually create a tag hold using the gcloud CLI or the API.


[ gcloud ](#gcloud) [ API ](#api) 
More 




To create a tag hold, use the
[`gcloud resource-manager tags holds create`](/resource-manager/docs/tags/sdk/gcloud/reference/alpha/resource-manager/tags/holds)
gcloud CLI command:


```
gcloud resource-manager tags holds create TAGVALUE_NAME \
--holder= HOLDER_NAME \
--location= LOCATION 
```


Where:

- 

` TAGVALUE_NAME ` is the permanent ID or namespaced
name of the tag value for which this tag hold should be created; for
example: `tagValues/567890123456`.

- 

` HOLDER_NAME ` is the name of the resource where
the tag value is attached. Must be less than 200 characters.

- 

` LOCATION ` is the location of your resource. If
you are creating a tag hold for a global resource, such as a
Google Cloud Dedicated project, you should omit this flag. If you are
creating a tag hold for a regional or zonal resource you must specify
the location; for example: `us-central1`.




To create a tag hold for a tag value, you must first create a JSON
representation of a tag hold. This JSON reference must include a reference
to the resource to which the tag value is attached. For more information
about the format of a tag hold, see the
[`TagHolds` reference](/resource-manager/reference/rest/v3/tagValues.tagHolds).

If you are creating a tag hold for a tag value attached to a global resource
such as an organization, use the
[`tagHolds.create`](/resource-manager/reference/rest/v3/tagHolds/create)
method with the global endpoint hostname:


```
POST https://cloudresourcemanager.googleapis.com/v3/tagValues/ TAGVALUE_NAME /tagHolds
```


If you are creating a tag hold for a tag value attached to a regional
resource, such as a Compute Engine instance, use the
`tagHolds.create` method with the regional endpoint where your resource is
located.


```
POST https:// LOCATION -cloudresourcemanager.googleapis.com/v3/ TAGVALUE_NAME /tagHolds
```


Request JSON body:


```
{
"holder": HOLDER_NAME ,
"origin": ORIGIN_NAME 
}
```


Where:

- 

` TAGVALUE_NAME ` is the permanent ID of the tag value
that is attached; for example: `tagValues/4567890123`.

- 

` HOLDER_NAME ` is the name of the resource where
the tag value is attached. Must be less than 200 characters.

- 

` ORIGIN_NAME ` is an optional string representing the
origin of this request. This field should include human-understandable
information to distinguish origins from each other. Must be less than 200
characters.




### List tag holds

You can list all tag holds under a particular tag value using the
gcloud CLI or the API.


[ gcloud ](#gcloud) [ API ](#api) 
More 




To list tag holds that are under a tag value, use the
[`gcloud resource-manager tags holds list`](/resource-manager/docs/tags/sdk/gcloud/reference/alpha/resource-manager/tags/holds)
gcloud CLI command:


```
gcloud resource-manager tags holds list TAGVALUE_NAME \
--location= LOCATION 
```


Where:

- 

` TAGVALUE_NAME ` is the permanent ID or namespaced
name of the tag value; for example: `tagValues/567890123456`.

- 

` LOCATION ` is the location of your resource. If you
are looking for tag holds created globally, you should omit this flag.
If you are looking for tag holds under a regional or zonal resource, you
must specify the location; for example: `us-central1`.




To get a list of tag holds under a tag value, use the
[`tagHolds`](/resource-manager/reference/rest/v3/tagHolds/list)
GET method, specifying the parent tag value in the URL:


```
GET https://cloudresourcemanager.googleapis.com/v3/{TAGVALUE_NAME}/tagHolds
```


Where:

- ` TAGVALUE_NAME ` is the permanent ID or namespaced
name of the tag value; for example: `tagValues/567890123456`.




### Remove tag holds

You can remove tag holds created on a particular tag value using the
gcloud CLI or the API.

Some resources add tag holds to a tag value that is attached to that resource.
If you attach a tag to such a resource, the resource creates a tag hold that
will prevent users from deleting the attached tag value.

You can delete a tag hold using the gcloud CLI or the API.


[ gcloud ](#gcloud) [ API ](#api) 
More 




To delete a tag hold, use the
[`gcloud resource-manager tags holds delete`](/resource-manager/docs/tags/sdk/gcloud/reference/alpha/resource-manager/tags/holds)
gcloud CLI command:


```
gcloud resource-manager tags holds delete TAGHOLD_NAME \
--location= LOCATION 
```


Where:

- 

` TAGHOLD_NAME ` is the namespaced name of the tag
hold, which can be found by using the [`list` command](#listing_holds).
For example:
`tagValues/1012910994523/tagHolds/d1c8f5e2-2954-43d6-8f46-5f812ab48c37`.

- 

` LOCATION ` is the location of your resource. If you
are deleting a tag hold that is under a tag value attached to a global
resource, such as a folder or a project, you should omit this flag. If
you are deleting a tag hold created from a regional or zonal process,
you must specify the location; for example: `us-central1`.




To delete a tag value, use the
[tagHolds.delete](/resource-manager/reference/rest/v3/tagHolds/delete)
method:


```
DELETE https://cloudresourcemanager.googleapis.com/v3/{TAGVALUE_NAME}/tagHolds/{TAGHOLD_NAME}
```


Where:

- 

` TAGVALUE_NAME ` is the permanent ID of the tag
value to which the tag hold you want to delete is attached; for example:
`tagValues/567890123456`.

- 

` TAGHOLD_NAME ` is the namespaced name of the tag
hold you want to delete, which can be found by using the
[`list` command](#listing_holds). For example:
`tagValues/1012910994523/tagHolds/d1c8f5e2-2954-43d6-8f46-5f812ab48c37`.




## Delete tags

To delete a tag, you must delete each of its defining components. First, you
must delete any tag bindings that attach this tag to resources in your
hierarchy. For instructions on deleting tag bindings, see
[Detaching a tag from a resource](#detaching).

If the tag is used by another resource, or a user has manually created a tag
hold, you might need to remove tag holds as well as delete tag bindings before
you can delete the tag values. For information about removing tag holds, see
[Removing tag holds](#removing_holds).

Once there are no more tag bindings for the tag values you want to delete, you
can delete the values.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To delete a tag value, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the organization
or project that contains your tag value.

- 

Click more_vert **Actions** next to
the tag key containing the tag value you want to delete, then click
**View details**.

- 

In the list of tag values associated with this tag key, click the tag
value you want to delete.

- 

Click the checkbox next to the tag value you want to delete, then click
delete **Delete values**.

- 

Click **Confirm**.




To delete a tag value, use the `gcloud resource-manager tag values delete`
command:


```
gcloud resource-manager tags values delete TAGVALUE_NAME 
```


` TAGVALUE_NAME ` is the permanent ID or
namespaced name of the tag value you want to delete; for example:
`tagValues/567890123456`.



To delete a tag value, use the
[tagValues.delete](/resource-manager/reference/rest/v3/tagValues/delete)
method:


```
DELETE https://cloudresourcemanager.googleapis.com/v3/{name= TAGVALUE_NAME }
```


` TAGVALUE_NAME ` is the permanent ID of the tag
value you want to delete; for example: `tagValues/567890123456`.



Once all tag values associated with a key have been deleted, you can then
delete the key. For tags with dynamic values, all the associated bindings must be deleted
before the tag key can be deleted.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




To delete a tag key, do the following:

- 

Open the **Tags** page in the Google Cloud Dedicated console.

[Open Tags page](https://console.cloud.berlin-build0.goog/iam-admin/tags) 

- 

From the **Scope picker** at the top of the page, select the organization
or project that contains your tag key.

- 

Click the checkbox next to the tag key you want to delete.

- 

Click delete **Delete tags**.

- 

Click **Confirm**.




To delete a tag key, use the `gcloud resource-manager tags keys delete`
command:


```
gcloud resource-manager tags keys delete TAGKEYS_NAME 
```


` TAGKEYS_NAME ` is the permanent ID or
namespaced name of the tag key you want to delete; for example:
`tagKeys/123456789012`.



To delete a tag key, use the
[tagKeys.delete](/resource-manager/reference/rest/v3/tagKeys/delete)
method:


```
DELETE https://cloudresourcemanager.googleapis.com/v3/{name= TAGKEYS_NAME }
```


` TAGKEYS_NAME ` is the permanent ID of the tag
key you want to delete; for example: `tagKeys/123456789012`.



## Policies and tags

You can use tags with policies that support them to conditionally enforce those
policies. You can make the presence or absence of a tag value the condition for
that policy.

For example, you can
[conditionally grant Identity and Access Management (IAM) roles](/iam/docs/conditions-overview)
based on whether a resource has a specific tag.

### Identity and Access Management conditions and tags

You can use tags and [Identity and Access Management conditions](/iam/docs/conditions-overview)
to conditionally grant roles to users in your hierarchy. This process makes
resources inaccessible to users until a tag which is associated with a
conditional policy is attached. For example, you may want to require that your
developers assign a cost center to a resource before they can use it.

- 

Create a tag that you can use to associate resources with something that will
identify whether the resources have had proper governance applied. For
example, you could create a tag with the key `costCenter` and values
`0001`, `0002`, and so forth, to associate the resources with the various
cost centers at your company.

- 

Create an organization-level
[custom role](/iam/docs/creating-custom-roles#creating_a_custom_role) that
allows users to add tags to the resources you require tags on. This gives
these permissions to the specified principals anywhere in your organization.

For example, a custom role that allows users to add tags to projects would
include the following permissions:

- `resourcemanager.projects.get`

- `resourcemanager.hierarchyNodes.create`

- `resourcemanager.hierarchyNodes.delete`

- `resourcemanager.hierarchyNodes.list`

- 

When creating projects for your developers, assign them this custom role
on the project.

- 

Assign any other roles to your developers that include
the permissions for them to perform any desired actions inside of that
project. When you grant roles to users on the project, the roles should
always be conditionally granted to require the attachment of the
`costCenter` tag.


```
resource.hasTagKey('123456789012/costCenter')
```


Now, any time a project is created, your developers must attach the `costCenter`
tag to it before they're able to perform the actions in it that are granted by
the allow policy.

### Organization policies and tags

You can use tags and conditional enforcement of organization policies to provide
centralized control of the resources in your hierarchy. For more information,
see
[Setting an organization policy with tags](/resource-manager/docs/organization-policy/tags-organization-policy).

## System tags

System tags are Google-managed tags that Google Cloud Dedicated in Germany services can bind to
resources. These system tags can be viewed and used like any other tag binding
on the resource, but can't be edited or removed from the resource. System tag
keys have the `system:` prefix in their short name and are managed in a tag
namespace that begins with the prefix `google`.



| 
Tag Key (Namespaced Name) | 
Tag Values | 
Description | 
|



| 
`google/system:sdp-data-sensitivity` | 
`HIGH, MODERATE, LOW, UNKNOWN` | 
Tags that the Sensitive Data Protection service can be configured to
automatically attach to resources that it profiles to indicate the discovered data
sensitivity level of the resource. For more information, see
[Enable the automatic tagging in the discovery configuration](/sensitive-data-protection/docs/control-access-based-on-data-sensitivity#enable-automatic-tagging-discovery). | 
|



## Supported services

For a list of services that support tags, see
[Services that support tags](/resource-manager/docs/tags/tags-supported-services).