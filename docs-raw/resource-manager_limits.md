# Quotas and usage limits

Source: https://berlin.devsitetest.how/resource-manager/docs/limits
Last updated: 2026-07-17

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

Resources

](https://berlin.devsitetest.how/resource-manager/docs/resources)












# Quotas and usage limits 






- On this page ** 
- [ Project limits ](#project-limits)
- [ Tag limits ](#tag-limits)
- [ Folder limits ](#folder-limits)
- 










## 
Project limits


The number of projects any user or service account can create is limited. If you create a project
outside an organization, the quota on your account is used. If you are creating a project within
an organization, the quota on both your account and organization are checked, and if either one
has quota remaining, the project can be created. 

Once your quota is reached,
you can request an increase. If you have less than 30 projects remaining in your quota, you can
see the number of projects you have remaining in your quota
on the [New Project](https://console.cloud.berlin-build0.goog/projectcreate) page. For more information, see
[Managing project quotas](https://berlin.devsitetest.how/resource-manager/docs/creating-managing-projects#managing_project_quotas).

The following usage limits apply per API consumer project.




| 
Limit | 
Limit Description | 
Limit value per second | 
Limit value per minute | 
|



| 
v1 API list | 
Includes list operations for projects. | 
Up to 4 requests | 
Up to 240 requests | 
|

| 
v1 API search | 
Includes search operations for organizations. | 
Up to 10 requests | 
Up to 600 requests | 
|

| 
v2 API list | 
Includes list operations for folders. | 
Up to 10 requests | 
Up to 600 requests | 
|

| 
v2 API search | 
Includes search operations for folders. | 
Up to 10 requests | 
Up to 600 requests | 
|

| 
v1 API read operations | 
Includes read operations for projects. | 
Up to 10 requests | 
Up to 600 requests | 
|

| 
Other API read operations | 
Includes all other read operations for tags and other resources. | 
Up to 10 requests | 
Up to 600 requests | 
|

| 
v3 API list | 
Includes list operations for projects, folders, and organizations. | 
Up to 10 requests | 
Up to 600 requests | 
|

| 
v3 API search | 
Includes search operations for projects, folders, and organizations. | 
Up to 4 requests | 
Up to 240 requests | 
|

| 
Write operations | 
Includes updating projects, tags, and other resources,
with the exception of moving or creating folders. The `Create Project` operation
costs 10 requests per second. | 
Up to 10 requests | 
Up to 600 requests | 
|

| 
Creating folders | 
Includes creation of folders. | 
Up to 0.1 requests | 
Up to 6 requests | 
|

| 
Moving folders | 
Includes moving folders to other folders. | 
Up to 0.1 requests | 
Up to 6 requests | 
|



To view or change usage limits for your project, or to request an increase to
your quota, do the following:


- If you don't already have a [billing account](//cloud.google.com/billing/docs/how-to/manage-billing-account)
for your project, then create one.

- [Visit the Enabled APIs page of the
API library](https://console.cloud.berlin-build0.goog/apis/enabled) in the Google Cloud Dedicated console, and select an API from the
list.

- To view and change quota-related settings, select Quotas**. To view
usage statistics, select **Usage**.

To view or change usage limits for your project, or to request an increase
to your quota, visit the [Quotas page](https://console.developers.google.com/iam-admin/quotas) in the
API Console.

## Tag limits

Each resource can have a maximum of 50 key-value pairs attached. There is a maximum of 1000 keys
allowed to be created under a given organization or project. Each key supports a maximum of 1000
values. For more information about the specifications for firewall secure tags,
see [Specifications](/firewall/docs/tags-firewalls-overview#specifications).

For more information about tags, see [Creating and managing tags](/resource-manager/docs/tags/tags-creating-and-managing).

## Folder limits

Following are some limits to consider when using folders in your resource hierarchy:



- You can nest folders up to 10 levels deep.

- A parent folder cannot contain more than 300 folders. This limit applies to direct child
folders only. Those child folders can, in turn, contain additional folders or projects.


For more information about folders, see [Creating and managing folders](/resource-manager/docs/creating-managing-folders).