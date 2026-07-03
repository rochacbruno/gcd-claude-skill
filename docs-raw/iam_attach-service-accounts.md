# Attach service accounts to resources

Source: https://berlin.devsitetest.how/iam/docs/attach-service-accounts
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

IAM

](https://berlin.devsitetest.how/iam/docs)






- 








[

Guides

](https://berlin.devsitetest.how/iam/docs/overview)












# Attach service accounts to resources 






- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Required roles ](#required_roles)

- [ Configure your organization policies ](#configure-org-policies)
- [ Configure the service account ](#configure-to-resources)

- [ Configure for a resource in the same project ](#configure-same-project)
- [ Configure for a resource in a different project ](#configure-different-project)

- [ Attach the service account to a resource ](#attaching-new-resource)
- [ Enable service accounts to be attached across projects ](#enabling-cross-project)
- [ Disable service accounts from being attached across projects ](#disabling-cross-project)
- [ Audit logs for attaching service accounts ](#audit-logs)
- [ What's next ](#whats-next)
- 










For some Google Cloud Dedicated resources, you can specify a user-managed service account that the
resource uses as its default identity. This process is known as *attaching* the service
account to the resource, or *associating* the service account with the resource.

When code running on the resource accesses Google Cloud Dedicated services and resources, it uses the
service account attached to the resource as its identity. For example, if you [attach a
service account to a Compute Engine instance](/compute/docs/access/service-accounts#associating_a_service_account_to_an_instance), and the applications on the instance use a [client library](/apis/docs/client-libraries-explained) to call Google Cloud Dedicated APIs,
those applications automatically use the attached service account for authentication and
authorization.

This page describes how to configure service accounts so that you can attach
them to resources.

## Before you begin 

- 




Enable the IAM and Resource Manager APIs.






Roles required to enable APIs**


To enable APIs, you need the Service Usage Admin IAM
role (`roles/serviceusage.serviceUsageAdmin`), which
contains the `serviceusage.services.enable` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).



[Enable the APIs](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

- 

Make sure you understand [how service accounts work](/iam/docs/service-accounts) in
IAM.

### Required roles









































































To get the permission that
you need to attach a service account to a resource,

ask your administrator to grant you the
[Service Account User ](/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) IAM role on the service account.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).







This predefined role contains the
`iam.serviceAccounts.actAs`
permission,
which is required to
attach a service account to a resource.







You might also be able to get
this permission
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









## Configure your organization policies

Depending on the location of the service account that you want to attach to the
resource, you might need to update your project's [organization
policies](/resource-manager/docs/organization-policy/overview) before attaching the service account:

- 

If the service account is in the same project as the resource that you want to
attach it to, then you don't need to update your project's organization
policies.

- 

If the service account is in a different project than the resource that you
want to attach it to, then you need to update the organization policies for
the project containing the service account. For details, see [Enable service
accounts to be attached across projects](#enabling-cross-project) on this
page.

This might be the case if, for example, you [create all of your service
accounts in a single project](/iam/docs/service-account-overview#locations).



## Configure the service account

Before you attach a service account to a resource, you must configure the
service account. This process differs depending on whether the service account
and the resource are in the same project or in different projects. After you
configure the service account, you can create the resource and attach the
service account to that resource.



### Configure for a resource in the same project

Before you attach a service account to another resource in the same project,
[grant roles](/iam/docs/granting-changing-revoking-access) to the service account so it can
access the appropriate resources, just as you would grant roles to any other
principal.



### Configure for a resource in a different project

In some cases, you might need to attach a service account to a resource that is
located in a different project. For example, if you
[create all of your service accounts in a single project](/iam/docs/service-account-overview#locations), you
might need to attach one of them to a new resource in a different project.

Before you attach a service account to a resource in another project, do the
following:

- In the project where the service account is located, follow the steps on
this page to
[enable service accounts to be attached across projects](#enabling-cross-project).

- Identify the project where you will create the resource.

- 

Identify the type of resource that you will attach the service account to,
as well as the service that owns that type of resource.

For example, if you are creating a Pub/Sub subscription, then
Pub/Sub is the service that owns the resource.

- 

Find the email address of the service agent for the service.

Different services use different service agents. For details, see
[Service agents](/iam/docs/service-agents).

- 

Grant the Service Account Token Creator role
(`roles/iam.serviceAccountTokenCreator`) to the service agents:















[Console](#console) [ gcloud ](#gcloud) [ REST ](#rest) 
**More 










- 

In the Google Cloud Dedicated console, go to the **Service accounts** page.

[Go to Service
accounts](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/serviceaccounts)

- 

Select the project that owns the service account that you will attach to a
resource.

- 

Click the email address of the service account that you will attach to a
resource.

- 

Go to the **Principals with access** tab.

- 

Click person_add 
**Grant access**, and then enter the email address of the service agent.

- 

Click **Select a role**, type `Service Account Token Creator`, and click
the role.

- 

Click **Save** to save your changes.

- 

Optional: If you need to grant the role to another service agent, repeat the
previous steps.







































Use the
[`gcloud iam service-accounts add-iam-policy-binding`](/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding)
command:


```
gcloud iam service-accounts add-iam-policy-binding \ 
SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com \ 
--member = serviceAccount: SERVICE_AGENT_EMAIL \ 
--role = roles/iam.serviceAccountTokenCreator
```


Replace the following values:

- ` SERVICE_ACCOUNT_NAME `: The name of the user-managed
service account that you are attaching to a resource.

- ` PROJECT_ID `: The project ID where the user-managed
service account is located.

- ` SERVICE_AGENT_EMAIL `: The email address for the service
agent.

The command prints the updated allow policy for the user-managed service
account.

Optional: If you need to grant the role to another service agent, run the
command again.







































To grant this role, use the read-modify-write pattern to update the allow policy
for your user-managed service account.

**First, read the allow policy for the user-managed service account:**

The 
`[projects.serviceAccounts.getIamPolicy](/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)`

method returns the allow policy for the service account.
















Before using any of the request data,
make the following replacements:


- ` PROJECT_ID `: Your Google Cloud Dedicated project
ID. Project IDs are alphanumeric strings, like `my-project`.

- 
` USER_SA_NAME `: The name of the user-managed service account that you are
binding to a resource.


HTTP method and URL:



```
POST https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts/ USER_SA_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com:getIamPolicy
```



Request JSON body:



```
{
"requestedPolicyVersion": 3
}
```



To send your request, expand one of these options:


#### curl (Linux, macOS, or Cloud Shell)













Save the request body in a file named `request.json`,
and execute the following command:






































```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
"https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts/ USER_SA_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com:getIamPolicy"
```




#### PowerShell (Windows)













Save the request body in a file named `request.json`,
and execute the following command:
























































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method POST `
-Headers $headers `
-ContentType: "application/json; charset=utf-8" `
-InFile request.json `
-Uri "https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts/ USER_SA_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com:getIamPolicy" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.







You should receive a JSON response similar to the following:






```
{
"version": 1,
"etag": "BwWl3KCTUMY=",
"bindings": [
{
"role": "roles/iam.serviceAccountUser",
"members": [
"serviceAccount:my-service-account@my-project.eu0.iam.gserviceaccount.com"
]
}
]
}
```



**Next, modify the allow policy to grant the Service Account Token Creator role
to the service agent.**


```
{ 
"version" : 1 , 
"etag" : "BwWl3KCTUMY=" , 
"bindings" : [ 
** { 
"role" : "roles/iam.serviceAccountTokenCreator" , 
"members" : [ 
"serviceAccount: ** SERVICE_AGENT_EMAIL " 
] 
}, **
{ 
"role" : "roles/iam.serviceAccountUser" , 
"members" : [ 
"serviceAccount: SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com" 
] 
} 
] 
} 
```


Replace the following:

- ` SERVICE_AGENT_EMAIL `: The email address for the
service agent

- ` SERVICE_ACCOUNT_NAME `: The name of the user-managed
service account.

- ` PROJECT_ID `: The project ID where the user-managed
service account is located.

**Finally, write the updated allow policy:**

The 
`[projects.serviceAccounts.setIamPolicy](/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy)`

method updates the allow policy for your service account.
















Before using any of the request data,
make the following replacements:


- ` PROJECT_ID `: Your Google Cloud Dedicated project
ID. Project IDs are alphanumeric strings, like `my-project`.

- 
` USER_SERVICE_ACCOUNT_NAME `: The name of the user-managed service account
that you are binding to a resource.


- 
` SERVICE_AGENT_EMAIL `: The email address of the service agent that will
create access tokens for your user-managed service account.


HTTP method and URL:



```
POST https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts/ SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com:setIamPolicy
```



Request JSON body:



```
{
"policy": {
"version": 1,
"etag": "BwWl3KCTUMY=",
"bindings": [
{
"role": "roles/iam.serviceAccountTokenCreator",
"members": [
"serviceAccount: SERVICE_AGENT_EMAIL "
]
},
{
"role": "roles/iam.serviceAccountUser",
"members": [
"serviceAccount: SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com"
]
}
]
}
}
```



To send your request, expand one of these options:


#### curl (Linux, macOS, or Cloud Shell)













Save the request body in a file named `request.json`,
and execute the following command:






































```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
"https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts/ SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com:setIamPolicy"
```




#### PowerShell (Windows)













Save the request body in a file named `request.json`,
and execute the following command:
























































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method POST `
-Headers $headers `
-ContentType: "application/json; charset=utf-8" `
-InFile request.json `
-Uri "https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts/ SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com:setIamPolicy" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.







You should receive a JSON response similar to the following:






```
{
"version": 1,
"etag": "BwWo331TkHE=",
"bindings": [
{
"role": "roles/iam.serviceAccountTokenCreator",
"members": [
"serviceAccount: SERVICE_AGENT_EMAIL "
]
},
{
"role": "roles/iam.serviceAccountUser",
"members": [
"serviceAccount:my-service-account@my-project.eu0.iam.gserviceaccount.com"
]
}
]
}
```























## Attach the service account to a resource

After you configure the user-managed service account, you can create a new
resource and attach the service account to that resource. Make sure you create
the new resource in the appropriate project.

In most cases, you must attach a service account to a resource when you create
that resource. After the resource is created, you cannot change which service
account is attached to the resource. Compute Engine instances are an
exception to this rule; you can
[change which service account is attached to an instance](/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes)
as needed.

See the instructions for the type of resource that you want to create:




| 
Attaching a service account when creating a resource | 
|











| 
Compute Engine | 




- 
[Instances](/compute/docs/access/create-enable-service-accounts-for-instances#using)


- 
[Instance templates](/compute/docs/instance-templates/create-instance-templates)



| 
|




| 
Google Kubernetes Engine | 




- 
[Clusters](/kubernetes-engine/docs/concepts/security-overview#authentication_and_authorization)


- 
[Node pools](/kubernetes-engine/docs/concepts/security-overview#authentication_and_authorization)



| 
|


| 
Pub/Sub | 

[Subscriptions](/sdk/gcloud/reference/pubsub/subscriptions/create)
| 
|





After you have created the resource and attached the service account to that
resource, you can grant roles to the service account so it can access the
appropriate resources. This process is the same as granting a role to any other
principal.

To learn how to grant roles, see
[Granting, changing, and revoking access to resources](/iam/docs/granting-changing-revoking-access).



## Enable service accounts to be attached across projects

If you want to let users attach service accounts in one project to resources in
another project, you must update the [organization policies](/resource-manager/docs/organization-policy/overview) for the
project that contains the service accounts. Check the following [boolean
constraints](/resource-manager/docs/organization-policy/understanding-constraints#boolean_constraint) in the organization policies for that project:

- 

Ensure that the `iam.disableCrossProjectServiceAccountUsage` boolean
constraint *is not enforced* for the project.

This boolean constraint controls whether you can attach a service account to
a resource in another project. It is enforced by default and can only be
configured at the project level, not the folder or organization level.

When this constraint is not enforced, IAM adds a
[project lien](/resource-manager/docs/project-liens) that prevents the project from being deleted.
This lien has the origin
`iam.googleapis.com/cross-project-service-accounts`. We strongly discourage
you from deleting this lien.

- 

Recommended: Ensure that the
`iam.restrictCrossProjectServiceAccountLienRemoval` boolean constraint *is
enforced* for the project.

This boolean constraint ensures that principals can remove the project lien
only if they have the `resourcemanager.projects.updateLiens` permission at
the organization level. If this constraint is not enforced, principals can
remove the project lien if they have this permission at the project level.

To learn how to view or change a boolean constraint in an organization
policy, see [Creating and managing organization policies](/resource-manager/docs/organization-policy/creating-managing-policies).

## Disable service accounts from being attached across projects

If you previously [enabled service accounts to be attached across
projects](#configure-different-project), we strongly discourage you from
disabling this feature, especially in production environments.

Specifically, in the project where your service accounts are located, you
shouldn't make any of these changes:

- Don't update the project's organization policies to *enforce* the
`iam.disableCrossProjectServiceAccountUsage` boolean constraint.

- Don't update the project's organization policies to *not enforce* the
`iam.restrictCrossProjectServiceAccountLienRemoval` boolean constraint.

- Don't remove the [project lien](/resource-manager/docs/project-liens) with the origin
`iam.googleapis.com/cross-project-service-accounts`, which prevents you from
deleting the project.

- Don't delete the project.

If you are willing to accept the risk of disabling this feature, you can reduce
your risk by [disabling the service accounts](/iam/docs/service-accounts-disable-enable#disabling) that you are using
across projects, then monitoring your Google Cloud Dedicated environment for issues.
If you see any issues, you can [re-enable the service accounts](/iam/docs/service-accounts-disable-enable#enabling). If
you don't see any issues, then you might not have any Google Cloud Dedicated
resources that depend on a service account in a different project.

## Audit logs for attaching service accounts

When a principal uses the `iam.serviceAccounts.actAs` permission to attach a
service account to a resource, IAM generates an audit log. This
audit log contains the following information:

- The email address of the principal that attached the service account to the
resource

- Details about the service account that was attached to the resource

For a list of resources that you can attach service accounts to, see [Attach the
service account to the new resource](#attaching-new-resource) on this page.

For an example of this type of audit log, see [Logs for using the
`iam.serviceAccounts.actAs` permission](/iam/docs/audit-logging/examples-service-accounts#use-actas). To learn more about
audit logs in general, see [Cloud Audit Logs overview](/logging/docs/audit).

## What's next

- Find out how to [attach a service account to a Compute Engine
instance](/compute/docs/access/service-accounts#associating_a_service_account_to_an_instance).

- Review and apply [best practices for securing service accounts](/iam/docs/best-practices-service-accounts).

- Learn more about [audit logging for IAM](/iam/docs/audit-logging).