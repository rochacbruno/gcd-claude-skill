# Create an access policy

Source: https://berlin.devsitetest.how/access-context-manager/docs/create-access-policy
Last updated: 2026-07-07

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












# Create an access policy 






- On this page 
- [ Before you begin ](#before-you-begin)
- [ Create an organization-level access policy ](#organization-access-policy)
- [ Create a scoped access policy and delegate the policy ](#scoped-access-policy)
- [ What's next ](#whats_next)
- 










This page describes how to create an organization-level access policy for your
organization and scoped policies for the folders and projects in your organization.

## Before you begin 

- Ensure you have the [correct permissions](/access-context-manager/docs/access-control)
to use Access Context Manager.

## Create an organization-level access policy

For an organization, you cannot create an organization-level access policy if an
organization-level access policy exists for that organization.


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




When you [create an access level](/access-context-manager/docs/create-basic-access-level), a default access policy
is created automatically. No additional manual steps are required.



To create an organization-level access policy, use the [`create`](/sdk/gcloud/reference/access-context-manager/policies/create)
command.


```
gcloud access-context-manager policies create \ 
--organization ORGANIZATION_ID --title POLICY_TITLE 
```


Where:

- 

ORGANIZATION_ID is the numeric ID of your organization.

- 

POLICY_TITLE is a human-readable title for your policy.

You should see output similar to the following (where POLICY_NAME 
is a unique [numeric identifier for the policy](https://berlin.devsitetest.how/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy)
assigned by Google Cloud Dedicated in Germany):


```
Create request issued
Waiting for operation [accessPolicies/ POLICY_NAME /create/1521580097614100] to complete...done.
Created.
```


Next, [set your default policy](/access-context-manager/docs/manage-access-policy#set-default).



To create an organization-level access policy:

- 

Create a request body.


```
{ 
"parent" : " ORGANIZATION_ID " , 
"title" : " POLICY_TITLE " 
} 
```


Where:

- 

ORGANIZATION_ID is the numeric ID of your organization.

- 

POLICY_TITLE is a human-readable title for your policy.

- 

Create the access policy by
calling [`accessPolicies.create`](/access-context-manager/docs/reference/rest/v1/accessPolicies/create).


```
POST https://accesscontextmanager.googleapis.com/v1/accessPolicies
```


If successful, the response body for the call contains an
[`Operation`](/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the
`POST` operation.




## Create a scoped access policy and delegate the policy

Only VPC Service Controls supports creating a scoped access policy.
You must continue to use organization-level policies for Google Cloud Dedicated in Germany
services, such as Identity-Aware Proxy (IAP).


[ Console ](#console) [ gcloud ](#gcloud) [ API ](#api) 
More 




- 

In the Google Cloud Dedicated console navigation menu, click **Security**, and then
click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.berlin-build0.goog/security/service-perimeter) 

- 

If you are prompted, select your organization, folder, or project.

- 

On the **VPC Service Controls** page, select the access policy that is the
parent of the scoped policy. For example, you can select the `default policy`
organization policy.

- 

Click **Manage policies**.

- 

On the **Manage VPC Service Controls** page, click **Create**.

- 

On the **Create access policy** page, in the **Access policy name** box,
type a name for the scoped access policy.

The scoped access policy name can have a maximum length of 50 characters, must start
with a letter, and can contain only ASCII Latin letters (a-z, A-Z),
numbers (0-9), or underscores (`_`). The scoped access policy name is case sensitive
and must be unique within an organization's access policy.

- 

To specify a scope for the access policy, click **Scopes**.

- 

Specify either a project or a folder as the scope of the access policy.

- 

To select a project that you want to add to the scope of the access
policy, do the following:

- 

In the **Scopes** pane, click **Add project**.

- 

In the **Add project** dialog, select that project's checkbox.

- 

Click **Done**. The added project appears in the **Scopes** section.

- 

To select a folder that you want to add to the scope of the access policy,
do the following:

- 

In the **Scopes** pane, click **Add folder**.

- 

In the **Add folders** dialog, select that folders's checkbox.

- 

Click **Done**. The added folder appears in the **Scopes** section.

- 

To delegate administration of the scoped access policy, click **Principals**.

- 

To specify the [principal](/iam/docs/overview#concepts_related_identity)
and the role that you want to bind to the access policy, do the following:

- 

In the **Principals** pane, click **Add principals**.

- 

In the **Add principals** dialog, select a principal, such as a user
name or service account.

- 

Select the role that you want to associate with the principal, such
as editor and read roles.

- 

Click **Save**. The added principal and role appear in the **Principals** section.

- 

On the **Create access policy** page, click **Create access policy**.




To create a scoped access policy, use the [`gcloud access-context-manager policies create`](/sdk/gcloud/reference/access-context-manager/policies/create)
command.


```
gcloud access-context-manager policies create \ 
--organization ORGANIZATION_ID [ --scopes = SCOPE ] --title POLICY_TITLE 
```


Where:

- 

ORGANIZATION_ID is the numeric ID of your organization.

- 

POLICY_TITLE is a human-readable title for your policy.
The policy title can have a maximum length of 50 characters, must start
with a letter, and can contain only ASCII Latin letters (a-z, A-Z),
numbers (0-9), or underscores (`_`). The policy title is case sensitive
and must be unique within an organization's access policy.

- 

SCOPE is the folder or project on which this policy is applicable. You
can specify only one folder or project as the scope, and the scope must exist
within the specified organization. If you don't specify a scope, the policy
applies to the entire organization.

The following output appears (where POLICY_NAME 
is a unique [numeric identifier for the policy](https://berlin.devsitetest.how/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy)
assigned by Google Cloud Dedicated in Germany):


```
Create request issued
Waiting for operation [accessPolicies/ POLICY_NAME /create/1521580097614100] to complete...done.
Created.
```


To delegate administration by binding a principal and role with a scoped access policy, use the [`add-iam-policy-binding`](/sdk/gcloud/reference/access-context-manager/policies/add-iam-policy-binding)
command.


```
gcloud access-context-manager policies add-iam-policy-binding \ 
[ POLICY ] --member = PRINCIPAL --role = ROLE 
```


Where:

- 

POLICY is ID of the policy or fully qualified identifier for the policy.

- 

PRINCIPAL is the principal to add the binding for. Specify in the
following format: `user|group|serviceAccount:email` or `domain:domain`.

- 

ROLE is the role name to assign to the principal. The role name
is the complete path of a predefined role, such as `roles/accesscontextmanager.policyReader`,
or the role ID for a custom role, such as
`organizations/{ORGANIZATION_ID}/roles/accesscontextmanager.policyReader`.




To create a scoped access policy, do the following:

- 

Create a request body.


```
{ 
"parent" : " ORGANIZATION_ID " , 
"scope" : " SCOPE " , 
"title" : " POLICY_TITLE " 
} 
```


Where:

- 

ORGANIZATION_ID is the numeric ID of your organization.

- 

SCOPE is the folder or project on which this policy is applicable.

- 

POLICY_TITLE is a human-readable title for your policy.
The policy title can have a maximum length of 50 characters, must start
with a letter, and can contain only ASCII Latin letters (a-z, A-Z),
numbers (0-9), or underscores (`_`). The policy title is case sensitive
and must be unique within an organization's access policy.

- 

Create the access policy by
calling [`accessPolicies.create`](/access-context-manager/docs/reference/rest/v1/accessPolicies/create).


```
POST https://accesscontextmanager.googleapis.com/v1/accessPolicies
```


If successful, the response body for the call contains an
[`Operation`](/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the
`POST` operation.

To delegate administration of the scoped access policy, do the following:

- 

Create a request body.


```
{ 
"policy" : " IAM_POLICY " , 
} 
```


Where:

- IAM_POLICY is a collection of bindings. A binding binds one
or more members, or principals, to a single role. Principals can be user
accounts, service accounts, Google groups, and domains. A role is a named
list of permissions; each role can be an IAM predefined role or a user-created
custom role.

- 

Create the access policy by
calling [`accessPolicies.setIamPolicy`](/access-context-manager/docs/reference/rest/v1/accessPolicies/setIamPolicy).

When the operation completes, the response body contains the
[`accessPolicy`](/access-context-manager/docs/reference/rest/v1/accessPolicies).
The `name` field contains the resource name: `accessPolicy`/`POLICY_ID` 

- To set the IAM policy, use the following endpoint:


```
POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/ POLICY_ID :setIamPolicy
```


Replace ` POLICY_ID ` with the policy ID from that was
returned from `accessPolicies.create`.

The request body must contain the IAM policy to set.

If successful, the response body contains an instance of [`policy`](/access-context-manager/docs/reference/rest/Shared.Types/Policy).




## What's next

- [Manage an access policy](/access-context-manager/docs/manage-access-policy)