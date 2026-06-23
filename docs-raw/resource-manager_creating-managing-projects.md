# Create projects

Source: https://berlin.devsitetest.how/resource-manager/docs/creating-managing-projects
Last updated: 2026-06-22

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












# Create projects 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Create a project ](#creating_a_project)

- [ Add tags during project creation ](#add_tags_during_project_creation)
- [ Designate project environments with tags ](#designate_project_environments_with_tags)
- [ Creating a project using a service account ](#creating_a_project_using_a_service_account)

- [ Managing project quotas ](#managing_project_quotas)
- [ What's next ](#whats_next)
- 










Projects are the fundamental operating unit in the Google Cloud Dedicated in Germany resource
hierarchy. Projects exist between folders (or the organization) and resources
such as virtual machines and storage. This page explains how to create
Google Cloud Dedicated projects using the Cloud Resource Manager API and the Google Cloud Dedicated console.

Key characteristics of projects include the following:

- 

The primary service container: A project is the base level where all
Google Cloud Dedicated in Germany services (APIs) are enabled and where resources like
Compute Engine instances or BigQuery datasets are created.

- 

The trust boundary: Projects serve as an isolation layer. By default,
resources in one project don't have access to resources in another,
establishing a secure perimeter for different applications or environments.

- 

The billing unit: Projects are the primary way businesses track, organize, and separate costs
across their organization.

- 

The policy attachment point: While policies often inherit from folders, the
project level is the most common place where specific permissions (
Identity and Access Management (IAM)) are granted to developers and service accounts
for daily tasks.

## Before you begin

Read about the project resource in the
[resource hierarchy overview](/resource-manager/docs/cloud-platform-resource-hierarchy#projects).
For guidance on setting up your resource hierarchy, see
[Decide a resource hierarchy for your Google Cloud Dedicated landing zone](/architecture/landing-zones/decide-resource-hierarchy).


The following identifiers are used for your project:

- 

**Project name**: A human-readable name for your project.

The project name has the following requirements:

- It must be 4 to 30 characters in length.

- It can contain letters, numbers, single quotes, hyphens, spaces, or exclamation points.

- It must end with a letter or a digit.

The project name isn't used by any Google APIs. You can edit the project
name at any time during or after project creation. Project names don't need
to be unique.

- 

**Project ID**: A globally unique identifier for your project.

A project ID is a unique string that differentiates your project from all
others in Google Cloud Dedicated in Germany. After you enter a project name, the
Google Cloud Dedicated console generates a unique project ID that can be a
combination of letters, numbers, and hyphens. Use the generated project
ID, but you can edit it during project creation. After project creation, the
project ID is permanent.

A project ID has the following requirements:

- It must be 6 to 30 characters in length.

- It can only contain lowercase letters, numbers, and hyphens.

- It must start with a letter.

- It cannot end with a hyphen.

- It cannot be in use or previously used; this includes deleted projects.

- It cannot contain restricted strings such as `google` and `ssl`. Avoid
using strings such as `undefined` and `null` in a project ID.

All Google Cloud Dedicated
project IDs are automatically prefixed with `eu0:`.

- 

**Project number**: A project number is an automatically generated
unique identifier for your project. To find the project number, see
[Identifying projects](/resource-manager/docs/view-update-projects#identifying_projects).

Don't include sensitive information, for example, personally identifiable
information or security data, in your project name, project ID, or other
resource names. The project ID appears in the name of many other Google Cloud Dedicated in Germany
resources. Referencing the project or its resources exposes the project ID and
resource name.

## Create a project

To create a project, you must have the `resourcemanager.projects.create`
permission. This permission is included in roles like the Project Creator role
(`roles/resourcemanager.projectCreator`).

For information on how to grant individuals the role and limit organization-resource
wide access, see the [Managing Default Organization
Roles](/resource-manager/docs/default-access-control) page.

If you don't specify the parent resource, a parent resource is selected
automatically if applicable based on the user account's domain.

You can create a new project using the Google Cloud Dedicated console, the
Google Cloud CLI, or
the [`projects.create()`](/resource-manager/reference/rest/v3/projects/create)
method.


[Console](#console) [gcloud](#gcloud) [REST](#rest) 
More 




To create a new project, do the following:


- 
Go to the **Manage resources** page in the Google Cloud Dedicated console.







[Go to Manage Resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager?walkthrough_id=resource-manager--create-project&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud Dedicated console.





- 
On the **Select organization** drop-down list at the top of the page, select the
organization resource in which you want to create a project. If you are a free trial user, skip this
step, as this list does not appear.


- Click **Create Project**.


- 
In the **New Project** window that appears, enter a project name and select a
billing account as applicable. A project name can contain only letters, numbers, single
quotes, hyphens, spaces, or exclamation points, and must be between 4 and 30 characters.


- 
Enter the parent organization or folder resource in the **Location** box. That resource
will be the hierarchical parent of the new project.



- When you're finished entering new project details, click **Create**.




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

To create a new project, use the
[`gcloud projects create`](/sdk/gcloud/reference/projects/create) command:


```
gcloud projects create PROJECT_ID 
```


Where PROJECT_ID is the ID for the project you want to create.
A project ID must start with a lowercase letter, and can contain only
ASCII letters, digits, and hyphens, and must be between 6 and 30 characters.

To create a project with an organization resource or a folder as parent, use the
`--organization` or `--folder` flags. As a resource can only have one
parent, only one of these flags can be used:


```
gcloud projects create PROJECT_ID --organization= ORGANIZATION_ID 
```

```
gcloud projects create PROJECT_ID --folder = FOLDER_ID 
```





You can't use certain words in the project ID when you create a new project
with the `projects.create()` method. Some examples include `google`, `null`, `undefined`, and `ssl`.
When you use a restricted word, the request returns with
an `INVALID_ARGUMENT` error.

The following request only creates a project, and doesn't associate it
automatically with a billing account. Use the
[`projects.updateBillingInfo`](/billing/reference/rest/v1/projects/updateBillingInfo)
method to set or update the billing account associated with a project.

Create Project Request:


```
POST https://cloudresourcemanager.googleapis.com/v3/projects/
Authorization: ********** *** 
Content-Type: application/json

{
"projectId": "our-project-123",
"name": "my project",
"labels": {
"mylabel": "prod"
}
}
```


Create Project Response:


```
{
"name": "operations/pc.123456789",
}
```


Get Operation Request:


```
GET https://cloudresourcemanager.googleapis.com/v3/operations/pc.123456789
Authorization: ********** *** 
Content-Type: application/json
```


Get Operation Response:


```
{
"name": "operations/pc.123456789",
"done": true,
"response": {
"@type": "type.googleapis.com/google.cloudresourcemanager.v3.Project",
"projectNumber": "464036093014",
"projectId": "our-project-123",
"lifecycleState": "ACTIVE",
"name": "my project",
"labels": {
"mylabel": "prod"
},
"createTime": "2016-01-07T21:59:43.314Z"
}
}
```



### Add tags during project creation






Tags provide a way to create annotations for resources. You can add tags at the time of creating projects. You
must assign the **Tag User** role while adding tags. For more information on the permissions assigned
to this role, see [Manage tags on resources](/resource-manager/docs/tags/tags-creating-and-managing#required-permissions-attach).
You can only add the namespace for the tag key-value pairs in one of the following ways:


[gcloud](#gcloud) [REST](#rest) 
More 




To add tags during project creation, run the following command:


```
gcloud projects create PROJECT_ID --organization= ORGANIZATION_ID --tags= KEY_VALUE_PAIRS 
```


Replace the following:

- PROJECT_ID is the unique identifier of the project.

- ORGANIZATION_ID is the unique identifier of the organization.

- KEY_VALUE_PAIRS is a comma-separated list of key-value pairs that you can assign to your
resource. An example of comma-separated key-value pairs is `123/environment=production, 456/create=testresource`.
In this example, `123` and `456` are the unique identifiers (IDs) of the organization or folder resources
where the tag keys are defined.




The following snippet is a JSON request where you create a project and
add tags to it.


```
POST https://cloudresourcemanager.googleapis.com/v3/projects/
Authorization: ********** *** 
Content-Type: application/json

{
"projectId": "our-project-456",
"name": "my project",
"parent": "organizations/123",
"tags": {
"key": "123/environment"
"value": "production"
},
"tags": {
"key": "123/costCenter"
"value": "marketing"
}
}
```



### Designate project environments with tags

You can use tags to visually distinguish projects based on their environment,
such as production, staging, or development. This helps prevent errors and
improves awareness when you are working in sensitive environments. Google adds a
visual indicator to the project in the Google Cloud Dedicated console project picker
when a project with a specific tag key-value pair is selected. This indicator
reminds you that any changes could affect your associated production or non-production
applications. Tags can either be inherited by the project or set directly on the
project.

To use this feature, do the following:

- [Create a tag key](/resource-manager/docs/tags/tags-creating-and-managing#creating-tag-key) named `environment`.

- [Create tag values](/resource-manager/docs/tags/tags-creating-and-managing#creating-tag-value) for the environment categories you use. The following values
are supported and are mapped to a corresponding badge in the console's project picker:

- Prod: Prod , prod , Production , production 

- Dev: Dev , dev , Development , development 

- Test: Test , test , Testing , testing , QA , qa , Quality assurance , quality assurance 

- Staging: Staging , staging , Stage , stage 

- [Attach the appropriate tag to your project](/resource-manager/docs/tags/tags-creating-and-managing#attaching) by
creating a tag binding.

If a project has multiple environment tags (for example, one inherited from a
folder and one directly on the project), the most specific tag is used to
determine the badge.

### Creating a project using a service account

You can use a service account to automate project creation. Like user accounts,
service accounts can be granted permission to create projects within an
organization resource. Service accounts are not allowed to create projects outside of an
organization resource and must specify the parent resource when creating a project.
Service accounts can create a new project using the gcloud CLI or the
`projects.create()` method.

## Managing project quotas

To request additional capacity for projects in your organization quota, open
a support ticket with the Google Cloud Dedicated in Germany team. For details,
see [Request a quota adjustment](/docs/quotas/view-manage#requesting_higher_quota).

## What's next

- Learn about [viewing and updating projects](/resource-manager/docs/view-update-projects).

- Learn about [deleting and restoring projects](/resource-manager/docs/delete-restore-projects).

- Learn how to [move a project within your resource hierarchy](/resource-manager/docs/moving-projects-folders).

- Learn how to [migrate a project from one organization resource to another](/resource-manager/docs/project-migration).