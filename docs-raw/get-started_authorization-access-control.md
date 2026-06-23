# Authorization and access control

Source: https://berlin.devsitetest.how/docs/get-started/authorization-access-control
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/get-started/tpc-differences) for more details.














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

Get started

](https://berlin.devsitetest.how/docs/get-started)












# Authorization and access control 






- On this page 
- [ Permissions and roles ](#permissions-roles)
- [ Using IAM as an administrator ](#admin)
- [ Advanced access control with IAM ](#advanced-iam)
- [ Other forms of access control ](#other)
- [ What's next ](#whats_next)
- 











Identity and Access Management (IAM) is a tool that lets you control who can do what in
your Google Cloud Dedicated in Germany environment.

Access is controlled with IAM permissions, which are required to
work with any resource in a Google Cloud Dedicated environment. When you're given
the permissions to work with a resource, you are *authorized* to access that
resource. Without the proper authorization, you can't access Google Cloud Dedicated
resources.

## Permissions and roles 

To work with a resource, your user account must have the relevant
permissions to access that resource.

Typically, your IAM administrator is responsible for controlling
access to resources. Your administrator can give you permissions to access a
single resource or all the resources in a project, folder, or organization.
Administrators grant the relevant permissions to your user account in bundles
called *roles*. As long as your user account has a role with the appropriate
permissions, you can use that role to access Google Cloud Dedicated resources.

Generally, the workflow to perform an action on any resource in your
Google Cloud Dedicated environment looks like this:

- You want to perform an action on a resource—for example, upload an
object to a Cloud Storage bucket—but you don't have the appropriate
permissions. Without the permissions, you can't perform the action.

- You can request the permissions you need from your IAM
administrator through your preferred request management system or directly
from the permission error message in the Google Cloud Dedicated console.

- Your IAM administrator grants a role that contains the
appropriate permissions to your user account. You can now
perform the action.

## Using IAM as an administrator

Administrators are typically responsible for granting roles to users so they can
access Google Cloud Dedicated resources. Users are represented by authenticated
identities known as *principals*.

Granting roles to a principal on a resource involves editing the *allow policy*
that's attached to the resource. Allow policies list which principals have
access to the resource and what actions they can perform on the resource.
IAM uses allow policies to determine whether a principal has the
required permissions to access the resource. Therefore, to grant a
principal access to a particular resource, you must update the allow
policy for the resource with the principal and the roles that you want to grant.

Administrators can grant roles to principals on the following types of resources:

- **Projects, folders, and organizations**: These resources are the container
resources used to structure your [resource
hierarchy](/iam/docs/resource-hierarchy-access-control). Roles that you grant
on these container resources apply to all of the service-specific resources
they contain.

- **Service-specific resources**: These resources are the features or components
offered by a service. For example, Compute Engine has resources like
instances, disks, and subnetworks. Granting roles on a service-specific
resource provides more granular access control than granting roles on a
container resource, because it limits a user's access to just that resource.

## Advanced access control with IAM

Allow policies are the most common method for controlling access to a
Google Cloud Dedicated environment with IAM. But
IAM also offers other options for access control, including the
following:

- Deny policies

- Conditional attribute-based access controls

## Other forms of access control

Although IAM is the primary method of access control for
Google Cloud Dedicated, there are other Google Cloud Dedicated services that can affect
a user's access to resources.

The following are some examples of other services that can affect a user's
access:

- [Access Context Manager](/access-context-manager/docs/overview):
Access Context Manager lets you define fine-grained, attribute-based access
control for projects and resources in Google Cloud Dedicated.

- [Organization Policy Service](/resource-manager/docs/organization-policy/overview):
Organization Policy lets you configure constraints across your resource
hierarchy to give you centralized and programmatic control over your
organization's cloud resources.

## What's next

- For a more in-depth description of the IAM system and
how it works, see the [IAM
overview page](/iam/docs/overview) in the IAM documentation.