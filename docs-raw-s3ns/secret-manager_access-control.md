# Access control with IAM

Source: https://documentation.s3ns.fr/secret-manager/docs/access-control
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/secret-manager/docs/tpc-differences) for more details.














- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Documentation

](https://documentation.s3ns.fr/docs)






- 








[

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Secret Manager

](https://documentation.s3ns.fr/secret-manager/docs)






- 








[

Guides

](https://documentation.s3ns.fr/secret-manager/docs/overview)












# Access control with IAM 















This page describes the Identity and Access Management (IAM) roles you can use to
configure Secret Manager. Roles limit a principal's ability to
access resources. Always grant the minimum set of permissions required to
perform a given task.

## Secret Manager roles

Following are the IAM roles that are associated with
Secret Manager. To learn how to grant, change, or revoke access to resources using
IAM roles, see
[Granting, changing, and revoking access to resources](/iam/docs/granting-changing-revoking-access).






| 
Role | 
Permissions | 
|



| 

#### Secret Manager Admin

(`roles/ secretmanager.admin`)



Full access to administer Secret Manager resources.



Lowest-level resources where you can grant this role:

- 
Secret

| 




`cloudkms.keyHandles.*` 





- `cloudkms.keyHandles.create`

- `cloudkms.keyHandles.get`

- `cloudkms.keyHandles.list`





`cloudkms.operations.get`



`cloudkms. projects. showEffectiveAutokeyConfig`



`resourcemanager.projects.get`



`resourcemanager.projects.list`




`secretmanager.*` 





- `secretmanager.locations.get`

- `secretmanager.locations.list`

- `secretmanager.secrets.create`

- `secretmanager. secrets. createTagBinding`

- `secretmanager.secrets.delete`

- `secretmanager. secrets. deleteTagBinding`

- `secretmanager. secrets. enableManagedRotation`

- `secretmanager.secrets.get`

- `secretmanager. secrets. getIamPolicy`

- `secretmanager.secrets.list`

- `secretmanager. secrets. listEffectiveTags`

- `secretmanager. secrets. listTagBindings`

- `secretmanager.secrets.rotate`

- `secretmanager. secrets. setIamPolicy`

- `secretmanager.secrets.update`

- `secretmanager.versions.access`

- `secretmanager.versions.add`

- `secretmanager.versions.destroy`

- `secretmanager.versions.disable`

- `secretmanager.versions.enable`

- `secretmanager.versions.get`

- `secretmanager.versions.list`



| 
|

| 

#### Secret Manager Editor

(`roles/ secretmanager.editor`)



Editor role for Secret Manager


| 



`resourcemanager.projects.get`



`resourcemanager.projects.list`




`secretmanager.locations.*` 





- `secretmanager.locations.get`

- `secretmanager.locations.list`





`secretmanager.secrets.create`



`secretmanager.secrets.delete`



`secretmanager. secrets. enableManagedRotation`



`secretmanager.secrets.get`



`secretmanager. secrets. getIamPolicy`



`secretmanager.secrets.list`



`secretmanager. secrets. listEffectiveTags`



`secretmanager. secrets. listTagBindings`



`secretmanager.secrets.rotate`



`secretmanager.secrets.update`



`secretmanager.versions.add`



`secretmanager.versions.destroy`



`secretmanager.versions.disable`



`secretmanager.versions.enable`



`secretmanager.versions.get`



`secretmanager.versions.list`

| 
|

| 

#### Secret Manager Secret Accessor

(`roles/ secretmanager.secretAccessor`)



Allows accessing the payload of secrets.



Lowest-level resources where you can grant this role:

- 
Secret

| 



`resourcemanager.projects.get`



`resourcemanager.projects.list`



`secretmanager.versions.access`

| 
|

| 

#### Secret Manager Viewer

(`roles/ secretmanager.viewer`)



Allows viewing metadata of all Secret Manager resources



Lowest-level resources where you can grant this role:

- 
Secret

| 



`resourcemanager.projects.get`



`resourcemanager.projects.list`




`secretmanager.locations.*` 





- `secretmanager.locations.get`

- `secretmanager.locations.list`





`secretmanager.secrets.get`



`secretmanager. secrets. getIamPolicy`



`secretmanager.secrets.list`



`secretmanager. secrets. listEffectiveTags`



`secretmanager. secrets. listTagBindings`



`secretmanager.versions.get`



`secretmanager.versions.list`

| 
|

| 

#### Secret Manager Secret Version Adder

(`roles/ secretmanager.secretVersionAdder`)



Allows adding versions to existing secrets.



Lowest-level resources where you can grant this role:

- 
Secret

| 



`resourcemanager.projects.get`



`resourcemanager.projects.list`



`secretmanager.secrets.rotate`



`secretmanager.versions.add`

| 
|

| 

#### Secret Manager Secret Version Manager

(`roles/ secretmanager.secretVersionManager`)



Allows creating and managing versions of existing secrets.



Lowest-level resources where you can grant this role:

- 
Secret

| 



`resourcemanager.projects.get`



`resourcemanager.projects.list`



`secretmanager.secrets.rotate`



`secretmanager.versions.add`



`secretmanager.versions.destroy`



`secretmanager.versions.disable`



`secretmanager.versions.enable`



`secretmanager.versions.get`



`secretmanager.versions.list`

| 
|




## Principle of least privilege






When you follow the principle of least privilege, you grant the minimum level of
access to resources required to perform a given task. For example, if a
principal needs access to a single secret, don't give that principal access to
other secrets or all secrets in the project or organization. If a principal only
needs to read a secret, don't grant that principal the ability to modify the
secret.

You can use [IAM](/iam/docs/overview) to grant IAM
roles and permissions at the level of the Cloud de Confiance secret, project,
folder, or organization. Always apply permissions at the lowest level in the
[resource hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy).

The following table shows the effective capabilities of a service account, based on the
level of the resource hierarchy where the Secret Manager Secret Accessor role
(`roles/secretmanager.secretAccessor`) is granted.




| 
Resource hierarchy | 
Capability | 
|



| 
Secret | 
Access only that secret | 
|

| 
Project | 
Access all secrets in the project | 
|

| 
Folder | 
Access all secrets in all projects in the folder | 
|

| 
Organization | 
Access all secrets in all projects in the organization | 
|



The role `roles/owner` includes the
`secretmanager.versions.access` permission, but the `roles/editor`
and `roles/viewer` do not.

If a principal only needs to access a single secret's value, don't grant that
principal the ability to access **all** secrets. For example, you can grant a
service account the Secret Manager Secret Accessor role
(`roles/secretmanager.secretAccessor`) on a single secret.

If a principal only needs to manage a single secret, don't grant that principal
the ability to manage all secrets. For example, you can grant a service
account the Secret Manager Admin role (`roles/secretmanager.admin`) on a single secret.

## IAM conditions

[IAM Conditions](/iam/docs/conditions-overview)
allow you to define and enforce conditional, attribute-based access control for
some Cloud de Confiance resources, including Secret Manager
resources.

In Secret Manager, you can enforce conditional access
based on the following attributes:


- **[Date/time attributes](/iam/docs/conditions-attribute-reference#date-time)**:
Use to set expirable, scheduled, or limited-duration
access to Secret Manager resources. For example, you could
allow a user to access a secret until a specified date.

- **[Resource attributes](/iam/docs/conditions-attribute-reference#resource)**:
Use to configure conditional access based on a resource name, resource type,
or resource service attributes. In Secret Manager, you can use
attributes of secrets and secret versions to configure conditional access. For
example, you can allow a user to manage secret versions only on secrets that
begin with a specific prefix, or allow a user to access only a specific secret
version.

For more information about IAM Conditions, see the
[Conditions overview](/iam/docs/conditions-overview).

## What's next

- Learn how to [manage access to secrets](/secret-manager/docs/manage-access-to-secrets).

- Learn how to apply the
[principle of least privilege](/iam/docs/using-iam-securely#least_privilege)
when managing Secret Manager resources by
[creating and managing custom roles](/iam/docs/creating-custom-roles).

- Learn about [IAM Conditions](/iam/docs/conditions-overview).