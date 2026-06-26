# Manage access to other resources

Source: https://berlin.devsitetest.how/iam/docs/manage-access-other-resources
Last updated: 2026-06-25

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












# Manage access to other resources 






- On this page ** 
- [ Before you begin ](#before_you_begin)

- [ Required roles ](#required-permissions)

- [ View current access ](#view-access)
- [ Grant or revoke a single IAM role ](#single-role)

- [ Grant a single IAM role ](#grant-single-role)
- [ Revoke a single IAM role ](#revoke-single-role)

- [ Grant or revoke multiple IAM roles using Google Cloud Dedicated console ](#multiple-roles-console)
- [ Grant or revoke multiple IAM roles programmatically ](#multiple-roles-programmatic)

- [ Get the current allow policy ](#getting-policy)
- [ Modify the allow policy ](#modifying-policy)
- [ Set the allow policy ](#setting-policy)

- [ What's next ](#whats_next)
- 










This page describes the general process for granting, changing, and revoking
access to resources that accept allow policies.

In Identity and Access Management (IAM), access is granted through *allow policies*, also
known as IAM policies. An allow policy is attached to a
Google Cloud Dedicated in Germany resource. Each allow policy contains a collection of *role
bindings* that associate one or more principals, such as users or service
accounts, with an IAM role. These role bindings grant the
specified roles to the principals, both on the resource that the allow policy is
attached to and on all of that resource's [descendants](/resource-manager/docs/cloud-platform-resource-hierarchy). For
more information about allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).

This page describes how to manage access to resources using the
Google Cloud Dedicated console, the Google Cloud CLI, and the REST API. You can also manage
access using the Google Cloud Dedicated client libraries.

## Before you begin

- Review the list of [resource types that accept allow
policies](/iam/docs/resource-types-with-policies).

- Ensure that you have the [required IAM
roles](#required-permissions).

### Required roles

To manage access to a resource, you need permissions to get the resource, and to
get and set the allow policy for the resource. These permissions have the
following form, where ` SERVICE ` is the name of the service
that owns the resource and ` RESOURCE_TYPE ` is the name of
the resource type that you want to manage access to:

- ` SERVICE . RESOURCE_TYPE .get`

- ` SERVICE . RESOURCE_TYPE .getIamPolicy`

- ` SERVICE . RESOURCE_TYPE .setIamPolicy`

For example, to manage access to a Compute Engine instance, you need the
following permissions:

- `compute.instances.get`

- `compute.instances.getIamPolicy`

- `compute.instances.setIamPolicy`

To gain the required permissions, ask your administrator to grant you a
predefined or custom role that includes the permissions. For example, your
administrator could grant you the Security Admin role
(`roles/iam.securityAdmin`), which includes permissions to manage access to
almost all Google Cloud Dedicated resources.

## View current access

The following section shows you how to use the Google Cloud Dedicated console, the
gcloud CLI, and the REST API to view who has access to a
resource. You can also view access by using the Google Cloud Dedicated client
libraries to get the resource's allow policy.















[Console](#console) [ gcloud ](#gcloud) [ REST ](#rest) 
More 










- 

In the Google Cloud Dedicated console, go to the page that lists the resource that
you want to view access to.

For example, to manage access to a Compute Engine instance, go to the
**VM instances** page.

[Go to VM instances](https://console.cloud.berlin-build0.goog/compute/instances)

- 

Select the checkbox next to the resource that you want to view access to.

- 

Ensure that the info panel is visible. If it is not visible, click
**Show info panel**. The info panel's **permissions** tab lists all
principals who have access to the resource.

If the **Show inherited permissions** switch is on, the list includes
principals with inherited roles; that is, principals whose access comes from
roles on parent resources rather than roles on the resource itself. For more
information about policy inheritance, see [Policy inheritance and the
resource hierarchy](/iam/docs/allow-policies#inheritance).







































To see who has access to your resource, get the allow policy for the resource.
To learn how to interpret allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).

To get the allow policy for the resource, run the `get-iam-policy` command for
the resource.

The format for this command varies depending on the resource type you're
managing access to. To find the format for your resource, find the reference
for the resource's `get-iam-policy` command in the [Google Cloud CLI
reference](/sdk/gcloud/reference). This reference is organized by service, then resource.
For example, to get the allow policy of a Compute Engine VM instance,
follow the format described in the [`gcloud compute instances get-iam-policy`
reference](/sdk/gcloud/reference/compute/instances/get-iam-policy).

Optionally, add the following arguments to the command to specify the
format and export the results:


```
--format = FORMAT > PATH 
```


Provide the following values:

- ` FORMAT `: The desired format for the policy. Use `json`
or `yaml`.

- ` PATH `: The path to a new output file for the
policy.

When you run the command, the resource's allow policy is either printed to the
console or exported to the specified file.







































To see who has access to your resource, get the resource's allow policy. To
learn how to interpret allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).

To get the resource's allow policy, use the resource's `getIamPolicy` method.

The HTTP method, URL, and request body depend on the resource that you want to
view access to. To find these details, find the API reference for the service
that owns the resource, then find the reference for the resource's
`getIamPolicy` method. For example, the HTTP method, URL, and request body for a
Compute Engine instance are specified in the [instances `getIamPolicy`
reference](/compute/docs/reference/rest/v1/instances/getIamPolicy).

The response for any resource's `getIamPolicy` method contains the resource's
allow policy.





















## Grant or revoke a single IAM role

You can use the Google Cloud Dedicated console and the gcloud CLI to quickly
grant or revoke a single role for a single principal, without editing the
resource's allow policy directly.

Common types of principals include service accounts, identities in workforce
identity pools, and identities in workload identity pools.

For a list of all principal types, see [Principal types](/iam/docs/principals-overview#principal-types).

In general, policy changes take effect within 2 minutes. However, in some cases, it
can take 7 minutes or more for changes to propagate across the system.

If you need help to identify the most appropriate predefined role, see
[Find the right predefined roles](/iam/docs/choose-predefined-roles).

### Grant a single IAM role

To grant a single role to a principal, do the following:















[Console](#console) [ gcloud ](#gcloud) 
More 










- 

In the Google Cloud Dedicated console, go to the page listing the resource that you
want to view access to.

For example, to manage access to a Compute Engine instance, go to the
**VM instances** page.

[Go to VM instances](https://console.cloud.berlin-build0.goog/compute/instances)

- 

Select the checkbox next to the resource that you want to manage access to.

- 

Ensure that the info panel is visible. If it is not visible, click
**Show info panel**.

- 

Select a principal to grant a role to:

- 

To grant a role to a principal who already has other roles on the resource,
find a row containing the principal, click
edit **Edit
principal** in that row, and click
add **Add another
role**.

- 

To grant a role to a principal who doesn't already have other roles on the
resource, click
person_add **Add
principal**, then enter an identifier for the principal—for example,
`//iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

- 

Click Select a role**, then enter the name of a role or permission to filter for a role to grant.
To follow the principle of least privilege, choose a role that includes only the permissions that
your principal needs.

- 

Optional: Add a [condition](/iam/docs/conditions-overview) to the role.

- 

Click **Save**. The principal is granted the role on the resource.







































To quickly grant a role to a principal, run the `add-iam-policy-binding`
command.

The format for this command varies depending on the resource type you're
managing access to. To find the format for your resource, find the reference
for the resource's `add-iam-policy-binding` command in the [Google Cloud CLI
reference](/sdk/gcloud/reference). This reference is organized by service, then resource.
For example, to grant a principal a role on a Compute Engine instance,
follow the format described in the [`gcloud compute instances add-iam-policy-
binding` reference](/sdk/gcloud/reference/compute/instances/add-iam-policy-binding).





















### Revoke a single IAM role

To revoke a single role from a principal, do the following:















[Console](#console) [ gcloud ](#gcloud) 
**More 










- 

In the Google Cloud Dedicated console, go to the page listing the resource that you
want to revoke access from.

For example, to manage access to a Compute Engine instance, go to the
**VM instances** page:

[Go to VM instances](https://console.cloud.berlin-build0.goog/compute/instances)

- 

Select the checkbox next to the resource that you want to manage access to.

- 

Ensure that the info panel is visible. If it is not visible, click
**Show info panel**.

- 

Find the row containing the principal whose access you want to revoke. Then click
edit **Edit
principal** in that row.

- 

Click the **Delete** delete button for
the role that you want to revoke, and then click **Save**.







































To quickly revoke a role from a principal, run the `remove-iam-policy-binding`
command.

The format for this command varies depending on the resource type you're
managing access to. To find the format for your resource, find the reference
for the resource's `remove-iam-policy-binding` command in the [Google Cloud CLI
reference](/sdk/gcloud/reference). This reference is organized by service, then resource.
For example, to grant a principal a role on a Compute Engine instance,
follow the format described in the [`gcloud compute instances
remove-iam-policy-binding` reference](/sdk/gcloud/reference/compute/instances/remove-iam-policy-binding).





















## Grant or revoke multiple IAM roles using Google Cloud Dedicated console

You can use the Google Cloud Dedicated console to grant and revoke multiple roles for
a single principal:

- 

In the Google Cloud Dedicated console, go to the page listing the resource that you
want to view access to.

For example, to manage access to a Compute Engine instance, go to the
**VM instances** page.

[Go to VM instances](https://console.cloud.berlin-build0.goog/compute/instances)

- 

Select the checkbox next to the resource that you want to manage access to.

- 

If the info panel is not visible, click **Show info panel**.

- 

Select the principal whose roles you want to modify:

- 

To modify roles for a principal who already has roles on the resource,
find a row containing the principal, click
edit **Edit
principal** in that row, and click
add **Add another
role**.

- 

To grant roles to a principal who doesn't have any existing roles on the
resource, click person_add **Grant access**, then enter an
identifier for the principal—for example, `//iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

- 

Modify the principal's roles:

- To grant a role to a principal who doesn't have any existing roles on the resource, click
Select a role**, then filter for a role to grant.

- To grant an additional role to the principal, click **Add another role**, then
filter for a role to grant.

- To replace one of the principal's roles
with a different role, click the existing role, then filter for a different role to grant.

- To revoke one of the principal's roles, click the **Delete** delete button for each role that you want to
revoke.

You can also [add a condition](/iam/docs/managing-conditional-role-bindings#add) to a role, [modify a role's
condition](/iam/docs/managing-conditional-role-bindings#modify), or [remove a role's
condition](/iam/docs/managing-conditional-role-bindings#removing).

- 

Click **Save**.



## Grant or revoke multiple IAM roles programmatically

To make large-scale access changes that involve granting and revoking multiple
roles for multiple principals, use the *read-modify-write* pattern to update the
resource's allow policy:

- Read the current allow policy by calling `getIamPolicy()`.

- Edit the allow policy, either by using a text editor or programmatically, to
add or remove any principals or role bindings.

- Write the updated allow policy by calling `setIamPolicy()`.

This section shows how to use the gcloud CLI and the REST API to
update the allow policy. You can also update the allow policy using the
Google Cloud Dedicated client libraries.

In general, policy changes take effect within 2 minutes. However, in some cases, it
can take 7 minutes or more for changes to propagate across the system.

### Get the current allow policy















[ gcloud ](#gcloud) [ REST ](#rest) 
More 










To get the allow policy for the resource, run the `get-iam-policy` command for
the resource.

The format for this command varies depending on the resource type you're
managing access to. To find the format for your resource, find the reference
for the resource's `get-iam-policy` command in the [Google Cloud CLI
reference](/sdk/gcloud/reference). This reference is organized by service, then resource.
For example, to get the allow policy of a Compute Engine VM instance,
follow the format described in the [`gcloud compute instances get-iam-policy`
reference](/sdk/gcloud/reference/compute/instances/get-iam-policy).

Optionally, add the following arguments to the command to specify the
format and export the results:


```
--format = FORMAT > PATH 
```


Provide the following values:

- ` FORMAT `: The desired format for the allow policy. Use
`json` or `yaml`.

- ` PATH `: The path to a new output file for the allow
policy.

When you run the command, the resource's allow policy is either printed to the
console or exported to the specified file.







































To get the resource's allow policy, use the resource's `getIamPolicy` method.

The HTTP method, URL, and request body depend on the resource that you want to
view access to. To find these details, find the API reference for the service
that owns the resource, then find the reference for the resource's
`getIamPolicy` method. For example, the HTTP method, URL, and request body for a
Compute Engine VM instance are specified in the
[instances `getIamPolicy` reference](/compute/docs/reference/rest/v1/instances/getIamPolicy).

The response for any resource's `getIamPolicy` method contains the resource's
allow policy. Save the response in a file of the appropriate type (`json` or
`yaml`).





















### Modify the allow policy

Programmatically or using a text editor, modify the local copy of your
resource's allow policy to reflect the roles you want to grant or revoke.

To ensure that you do not overwrite other changes, do not edit or remove the
allow policy's `etag` field. The `etag` field identifies the current state of
the allow policy. When you [set the updated allow policy](#setting-policy),
IAM compares the `etag` value in the request with the
existing `etag`, and only writes the allow policy if the values match.

To edit the roles that an allow policy grants, you need to edit the role
bindings in the allow policy. Role bindings have the following format:


```
{ 
"role" : " ROLE_NAME " , 
"members" : [ 
" PRINCIPAL_1 " , 
" PRINCIPAL_2 " , 
... 
" PRINCIPAL_N " 
], 
"conditions:" { 
CONDITIONS 
} 
} 
```


The placeholders have the following values:

- 

` ROLE_NAME `: The name of the role that you want to
grant. Use one of the following formats:

- Predefined roles: `roles/ SERVICE . IDENTIFIER `

- Project-level custom roles: `projects/ PROJECT_ID /roles/ IDENTIFIER `

- Organization-level custom roles: `organizations/ ORG_ID /roles/ IDENTIFIER `

For a list of predefined roles, see [Understanding
roles](/iam/docs/understanding-roles).

- 

` PRINCIPAL_1 `, ` PRINCIPAL_2 `,
`... PRINCIPAL_N `: Identifiers for the principals that
you want to grant the role to.

Principal identifiers usually have the following form:
` PRINCIPAL-TYPE : ID `.
For example, `principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.
For a full list of the values that ` PRINCIPAL ` can have,
see [Principal identifiers](/iam/docs/principal-identifiers).

- 

` CONDITIONS `: Optional. Any [conditions](/iam/docs/conditions-overview)
that specify when access will be granted.

#### Grant a role

To grant roles to your principals, modify the role bindings in the allow policy.
To learn what roles you can grant, see
[Understanding roles](/iam/docs/understanding-roles), or
[view grantable roles](/iam/docs/viewing-grantable-roles) for the resource. If you need help to
identify the most appropriate predefined roles, see
[Find the right predefined roles](/iam/docs/choose-predefined-roles).

Optionally, you can use [conditions](/iam/docs/conditions-overview) to grant roles only when
certain requirements are met.

To grant a role that is already included in the allow policy, add the principal
to an existing role binding:















[ gcloud ](#gcloud) [ REST ](#rest) 
More 










Edit the allow policy by adding the principal to an existing role binding. Note
that this change will not take effect until you
[set the updated allow policy](#setting-policy).

For example, imagine the allow policy contains the following role binding, which
grants the Compute Instance Admin role (`roles/compute.instanceAdmin`) to
Kai:


```
{ 
"role" : "roles/compute.instanceAdmin" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/kai@example.com" 
] 
} 
```


To grant that same role to Raha, add Raha's principal identifier to the
existing role binding:


```
{ 
"role" : "roles/compute.instanceAdmin" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/kai@example.com" , 
** "principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/raha@example.com" **
] 
} 
```









































Edit the allow policy by adding the principal to an existing role binding. Note
that this change will not take effect until you
[set the updated allow policy](#setting-policy).

For example, imagine the allow policy contains the following role binding, which
grants the Compute Instance Admin role (`roles/compute.instanceAdmin`) to
Kai:


```
{ 
"role" : "roles/compute.instanceAdmin" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/kai@example.com" 
] 
} 
```


To grant that same role to Raha, add Raha's principal identifier to the
existing role binding:


```
{ 
"role" : "roles/compute.instanceAdmin" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/kai@example.com" , 
** "principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/raha@example.com" **
] 
} 
```






















To grant a role that is not yet included in the allow policy, add a new role
binding:















[ gcloud ](#gcloud) [ REST ](#rest) 
More 










Edit the allow policy by adding a new role binding that grants the role to the
principal. This change will not take effect until you
[set the updated allow policy](#setting-policy).

For example, to grant the Compute Load Balancer Admin role
(`roles/compute.loadBalancerAdmin`) to Raha, add the following
role binding to the `bindings` array for the allow policy:


```
{ 
"role" : "roles/compute.loadBalancerAdmin" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/raha@example.com" 
] 
} 
```








































Edit the allow policy by adding a new role binding that grants the role to the
principal. This change will not take effect until you
[set the updated allow policy](#setting-policy).

For example, to grant the Compute Load Balancer Admin role
(`roles/compute.loadBalancerAdmin`) to Raha, add the following
role binding to the `bindings` array for the allow policy:


```
{ 
"role" : "roles/compute.loadBalancerAdmin" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/raha@example.com" 
] 
} 
```






















#### Revoke a role

To revoke a role, remove the principal from the role binding. If there are no
other principals in the role binding, remove the entire role binding.















[ gcloud ](#gcloud) [ REST ](#rest) 
More 










Revoke a role by editing the JSON or YAML allow policy returned by the
`get-iam-policy` command. This change will not take effect until you
[set the updated allow policy](#setting-policy).

To revoke a role from a principal, delete the desired principals or bindings
from the `bindings` array for the allow policy.







































Revoke a role by editing the JSON or YAML allow policy returned by the
`get-iam-policy` command. This change will not take effect until you
[set the updated allow policy](#setting-policy).

To revoke a role from a principal, delete the desired principals or bindings
from the `bindings` array for the allow policy.





















### Set the allow policy

After you modify the allow policy to grant and revoke the desired roles, call
`setIamPolicy()` to make the updates.















[ gcloud ](#gcloud) [ REST ](#rest) 
More 










To set the allow policy for the resource, run the `set-iam-policy` command for
the resource.

The format for this command varies depending on the resource type you're
managing access to. To find the format for your resource, find the reference
for the resource's `set-iam-policy` command in the [Google Cloud CLI
reference](/sdk/gcloud/reference). This reference is organized by service, then resource.
For example, to get the allow policy of a Compute Engine VM instance,
follow the format described in the [`gcloud compute instances set-iam-policy`
reference](/sdk/gcloud/reference/compute/instances/set-iam-policy).

The response for any resource's `set-iam-policy` command contains the resource's
updated allow policy.







































To set the resource's allow policy, use the resource's `setIamPolicy` method.

The HTTP method, URL, and request body depend on the resource that you want to
view access to. To find these details, find the API reference for the service
that owns the resource, then find the reference for the resource's
`setIamPolicy` method. For example, the HTTP method, URL, and request body for a
Compute Engine VM instance are specified in the
[instances `setIamPolicy` reference](/compute/docs/reference/rest/v1/instances/getIamPolicy).

The response for any resource's `setIamPolicy` method contains the resource's
updated allow policy.





















## What's next

- Learn how to [manage access to projects, folders, and
organizations](/iam/docs/granting-changing-revoking-access) or how to
[manage access to service accounts](/iam/docs/manage-access-service-accounts).

- Find out how to
[choose the most appropriate predefined roles](/iam/docs/choose-predefined-roles).

- Discover how to
[view the roles that you can grant on a particular
resource](/iam/docs/viewing-grantable-roles).

- Learn how to make a principal's access conditional with
[conditional role bindings](/iam/docs/conditions-overview).