# Workforce Identity Federation

Source: https://documentation.s3ns.fr/iam/docs/workforce-identity-federation
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

IAM

](https://documentation.s3ns.fr/iam/docs)






- 








[

Identity and Access Management (IAM)

](https://documentation.s3ns.fr/iam/docs)






- 








[

Guides

](https://documentation.s3ns.fr/iam/docs/overview)












# Workforce Identity Federation 















With Workforce Identity Federation, users in your external IdP
can use single sign-on (SSO) to access Cloud de Confiance by S3NS resources.

## What is Workforce Identity Federation?

Workforce Identity Federation lets you use your external IdP
to authenticate your workforce—*users* and *groups* of users, such as employees,
partners, and contractors. Users can then access Cloud de Confiance using
single sign-on (SSO), through your IdP. Use allow policies to
[authorize your workforce users to access Cloud de Confiance services](#workforce-principal-identifiers).

### Federation versus synchronization

Workforce Identity Federation federates identities from your IdP, so it
doesn't store user accounts in Cloud de Confiance. Because of this,
Workforce Identity Federation is sync-less, meaning that you don't need to
use tools to synchronize user identities from your IdP to Google-managed
identities that require Google Accounts. For example, by using
Workforce Identity Federation, you don't need to use Cloud Identity's
[Google Cloud Directory Sync (GCDS)](https://tools.google.com/dlpage/dirsync/).

To compare this approach with other federation architectures, see
[Architecture patterns for identity federation](/iam/docs/federated-identity-architectures).

### Workforce Identity Federation versus Workload Identity Federation

Workforce Identity Federation federates user identities whereas Workload Identity Federation federates workload identities.

For more information, see [Workload Identity Federation](/iam/docs/workload-identity-federation).

### Attribute-based access

Workforce Identity Federation extends Cloud de Confiance's identity
capabilities to support attribute-based access. In some IdPs, attributes are
also known as *claims* or *assertions*.

After user authentication, attributes that are received from the IdP are used to
determine the scope of access to Cloud de Confiance resources.

### Supported protocols

You can use Workforce Identity Federation with any IdP that supports [OpenID
Connect (OIDC)](https://openid.net/connect/) or [SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html),
such as Microsoft Entra ID, Active Directory Federation Services
(AD FS), Okta, and others.

## Key concepts

This section describes the key concepts of
Workforce Identity Federation.

### Workforce identity pools

Workforce identity pools let you manage groups of workforce
identities and their access to Cloud de Confiance resources.

Pools let you do the following:

- Group user identities; for example, `employees` or `partners`

- Grant IAM access to an entire pool or a subset of the pool.

- Federate identities from one or more IdPs.

- Define policies on a group of users that require similar access permissions.

- Specify IdP-specific configuration information, including [attribute mapping](#attribute-mappings)
and [attribute conditions](#attribute-conditions).

- Enable the Google Cloud CLI and API access for third-party identities.

- Log access by users within a pool to Cloud Audit Logs, along with the pool ID.

You can create multiple pools. For an example that describes one such approach,
see [Example: Multiple workforce identity pools](#example-multiple-workforce-pools).

Pools are configured at the [Cloud de Confiance organization level](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations), which
motivates the following considerations:

- When you first set up Workforce Identity Federation for your
organization, provide a unique ID for the pool. The pool ID must be globally unique across all workforce identity pools in Cloud de Confiance, and should clearly describe the identities it contains.

- If you have the appropriate IAM permissions to view the pool,
it can be referenced by its ID across all projects and folders within the organization.

### Workforce identity pool providers

A workforce identity pool provider is an entity that describes a relationship
between your Cloud de Confiance organization and your IdP.

Workforce Identity Federation follows the [OAuth 2.0 Token Exchange specification (RFC 8693)](https://datatracker.ietf.org/doc/html/rfc8693).
You provide a credential from your external IdP to the
Security Token Service, which verifies the identity in the credential, and then returns a
short-lived Cloud de Confiance access token in exchange.

### OIDC flow types

For OIDC providers, Workforce Identity Federation supports both
[authorization code flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth) 
and [implicit flow](https://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth).
Authorization code flow is considered to be the most secure, because
tokens are returned from the IdP in a separate, secure backend transaction,
directly from the IdP to Cloud de Confiance, after users authenticate. As a
result, code flow transactions can retrieve tokens of any size, so you can have
more claims to use for attribute mapping and attribute condition.
In implicit flow, by comparison, the ID Token is returned from the IdP to the
browser. Tokens are subject to individual browser URL size limits.

When you use the authorization code flow, you can configure the provider to
either merge claims from the OIDC `UserInfo` endpoint with ID token claims
(`merge-user-info-over-id-token-claims`) or include only ID token claims
(`only-id-token-claims`). The implicit flow supports only ID token claims
(`only-id-token-claims`).

### Cloud de Confiance Workforce Identity Federation console

Users in a [workforce identity pool](#workforce-identity-pools) can [access the Cloud de Confiance by S3NS Workforce Identity Federation console, also known as the console (federated)](/iam/docs/workforce-console-sso). The console provides these users with UI access to
Cloud de Confiance [products that support Workforce Identity Federation](/iam/docs/federated-identity-supported-services).

### Attributes

Your IdP provides attributes, referred to by some IdPs as *claims*. Attributes
contain information about your users. You can use these attributes in
[attribute mappings](#attribute-mappings) and [attribute conditions](#attribute-conditions).

#### Attribute mappings

You can map these attributes for use by Cloud de Confiance using
[Common Expression Language (CEL)](https://github.com/google/cel-spec).

This section describes the set of required and optional attributes that
Cloud de Confiance provides.

You can also define custom attributes in your IdP that can then be used by
specific Cloud de Confiance products—for example, in IAM allow
policies.

The maximum size for attribute mappings is 16 KB. If
the size of attribute mappings exceeds the 16 KB
limit, the sign-in attempt will fail.

The attributes are as follows:

- 

`google.subject` (Required): a unique identifier for the authenticating
user. It is *often the subject assertion of the JWT*, because
Cloud Audit Logs logs record the contents of this field as the principal.
You can use this field to configure IAM for authorization
decisions. We recommend that you don't use a mutable value because if you
change the value in your IdP's user directory, the user loses access.

The maximum length is 127 bytes.

- 

`google.groups` (Optional): the collection of groups that the authenticating
user is a member of. You can configure a logic expression using a subset
of CEL that produces *an array of strings*. You can also use this field
to configure IAM for authorization decisions. Limitations
for `google.groups` are as follows:

- 

We recommend that you limit the group name to 40 characters.

- 

If a single user belongs to more than 400 groups, that
user's sign-in attempt will fail. To mitigate this, you must define a
smaller set of groups in the assertion, and map only those groups that are
used to federate the user to Cloud de Confiance.

- 

If you use this attribute to grant access in IAM, every
member in the mapped groups is granted access. Therefore, we recommend
that you ensure that only authorized users in your organization can
modify the membership of the mapped groups.

- 

`google.display_name` (Optional): attribute that is *used to set
the name* of the signed-in user in the Cloud de Confiance console. This attribute
can't be used in IAM allow policies nor in the attribute
condition.

The maximum length is 100 bytes.

- 

`google.profile_photo` (Optional): a URL of the user's thumbnail photo.
We recommend the photo to be 400x400 pixels. When this attribute is set, the
image is visible as the user's profile picture in the Cloud de Confiance console.
If this value isn't set, or it can't be fetched, a generic user icon is
displayed instead. This attribute can't be used in either IAM
allow policies or in the attribute condition.

- 

`google.posix_username` (Optional): a unique POSIX-compliant username string
used for the following:

- 

[SSH-in-browser](/compute/docs/ssh-in-browser).

This attribute can't be used in IAM allow policies or in the
attribute condition. The maximum length is 32 characters.

- 

`attribute. KEY ` (Optional): an external IdP-defined
attribute that is present in a user's IdP token. You can use the custom
attribute to define your authorization strategy in an IAM
allow policy.

For example, in your IdP, you can choose to define an attribute such as the
user's cost center as `costcenter = "1234"`, and then refer to the
principal in the following way:


```
principalSet://iam.googleapis.com/projects/ PROJECT_NUMBER /locations/global/workforcePools/ WORKFORCE_POOL_ID /attribute.costcenter/1234
```


After you grant access on Cloud de Confiance resources to this principal
identifier, all identities that are configured in the IdP to have the
`costcenter` attribute set to `1234` have access to the resources.

You can configure a maximum of 50 custom attribute mapping rules. The
maximum size of each such rule is 2048 characters.

Although we don't have restrictions on the attributes you can map here, we
strongly recommend that you choose attributes whose values are stable. For
example, an attribute like `attribute.job_description` might change for many
reasons (such as improving its readability). As an alternative, consider using
`attribute.role`. Changes to the latter indicate a change of assigned
responsibility and align with changes in the access granted to the user.

You can transform attribute values using [standard CEL functions](https://github.com/google/cel-spec/blob/master/doc/langdef.md). You can also use the following custom functions:

- 

The [`split` function](https://pkg.go.dev/github.com/google/cel-go/ext#readme-split)
splits a string on the provided separator value. For example, to extract the attribute `username` from an email address attribute by splitting its value at the `@` and using the first string, use the following attribute mapping:

```
attribute.username=assertion.email.split("@")[0]
```


- 

The [`join` function](https://pkg.go.dev/github.com/google/cel-go/ext#readme-join)
joins a list of strings on the provided separator value. For example, to populate the custom attribute `department` by concatenating a list of strings
with `.` as a separator, use the following attribute mapping:

```
attribute.department=assertion.department.join(".")
```


#### Attribute conditions

Attribute conditions are optional CEL expressions that let you set constraints
on the identity attributes that Cloud de Confiance accepts.

The benefits of using attribute conditions include the following:

- You can use attribute conditions to allow only a subset of external
identities to authenticate to your Cloud de Confiance project. For example,
you might want to allow only those identities that are in a specific
team to sign in, especially if you are using a public IdP.
For another example, you might want to allow your accounting team to sign
in, but not your engineering team.

- Attribute conditions let you prevent credentials intended for use with
another platform from being used with Cloud de Confiance, and vice-versa.
This helps avoid the [confused deputy problem](https://wikipedia.org/wiki/Confused_deputy_problem).


#### Attribute conditions for multi-tenant IdPs

Workforce Identity Federation doesn't maintain a directory of user accounts;
instead, it implements claims-based identities. As a result, when two tokens are
issued by the same IdP and their claims map to the same
`google.subject` value, the two tokens are assumed to identify the same user. To
find out which IdP issued a token, Workforce Identity Federation inspects and
verifies the token's issuer URL.

Multi-tenant IdPs, such as GitHub and Terraform Cloud, use a single issuer URL
across all of their tenants. For these providers, the issuer URL identifies all
of GitHub or Terraform Cloud, not a specific GitHub or Terraform Cloud
organization.

When you use these IdPs, it's insufficient to let
Workforce Identity Federation check a token's issuer URL to ensure that it
comes from a trusted source and that its claims can be trusted. If your
multi-tenant IdP has a single issuer URL, you must use
attribute conditions to ensure that access is restricted to the correct tenant.

### Detailed audit logging

*Detailed audit logging* is a feature of Workforce Identity Federation that
logs attributes that were received from your IdP to Cloud Audit Logs.

You can enable detailed audit logging when you create your workforce identity
pool provider.

To learn how to troubleshoot attribute mapping errors with detailed audit
logging, see [General attribute mapping errors](/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors).

### JSON web keys

The workforce pool provider can access [JSON web keys (JWKs)](https://www.rfc-editor.org/rfc/rfc7517)
that are provided by your IdP in the `jwks_uri` field in the
`/.well-known/openid-configuration` document. If your OIDC provider doesn't
provide this information, or your issuer is not publicly accessible, you can
manually upload the JWKs when you create or update the OIDC provider.

### SCIM support

If your IdP supports the [System for Cross-domain Identity Management (SCIM)](https://en.wikipedia.org/wiki/System_for_Cross-domain_Identity_Management),
you can configure your IdP to provision and manage groups in Cloud de Confiance.

For more information, see
[SCIM provisioning for Workforce Identity Federation](/iam/docs/workforce-identity-federation-scim)
and [Configure your identity provider for Gemini Enterprise](/gemini/enterprise/docs/configure-identity-provider).





## Workforce principal identifiers for allow policies

The following table shows the principal identifiers that you can use to grant roles
to individual users and groups of users.




| 
Identities | 
Identifier format | 
|



| 
Single identity in a workforce identity pool | 

`principal://iam.googleapis.com/locations/global/workforcePools/ POOL_ID /subject/ SUBJECT_ATTRIBUTE_VALUE `
| 
|

| 
All workforce identities in a group | 

`principalSet://iam.googleapis.com/locations/global/workforcePools/ POOL_ID /group/ GROUP_ID `
| 
|

| 
All workforce identities with a specific attribute value | 

`principalSet://iam.googleapis.com/locations/global/workforcePools/ POOL_ID /attribute. ATTRIBUTE_NAME / ATTRIBUTE_VALUE `
| 
|

| 
All identities in a workforce identity pool | 

`principalSet://iam.googleapis.com/locations/global/workforcePools/ POOL_ID /*`
| 
|



For a complete list of principal identifiers, see
[Principal identifiers](/iam/docs/principal-identifiers).

## Other considerations

This section describes other considerations when using Workforce Identity Federation.

### Restrict cross-organization access

Workforce identity pool principals can't directly access resources
outside of the organization that they belong to. However, if a principal is
given permission to [impersonate a service account](/iam/docs/impersonating-service-accounts)
within the organization, this constraint can be bypassed as service accounts
aren't equally restricted.

### Workforce pools user project

Most Cloud de Confiance APIs (resource-based APIs) charge billing and quota to
the project containing the resource. Some APIs (client-based APIs) charge the
project associated with the client, known as the *quota project*.

When you create a Workforce Identity Federation configuration file, you
specify a *workforce pools user project*. This project identifies your
application to Google APIs and serves as the default quota project for
client-based APIs, unless you use the gcloud CLI to make the request.
You must have the `serviceusage.services.use` permission, included in the
Service Usage Consumer role, (`roles/serviceusage.serviceUsageConsumer`), for the
specified project.

For more information about the quota project, resource-based APIs, and
client-based APIs, see [Quota project overview](/docs/quotas/quota-project).

### Example: multiple workforce identity pools

This section contains an example that illustrates typical use of multiple
pools.

You can create one pool for employees and another for partners. Multinational
organizations might create separate pools for different divisions in their
organization. Pools allow for distributed management, in which different groups
can independently manage their specific pool where roles are granted only to the
identities in the pool.

For example, suppose that a company named Enterprise Example Organization
contracts a different company named Partner Example Organization Inc to provide
Google Kubernetes Engine (GKE) DevOps services. For Partner Example Organization
workforce to provide the services, their workforce must be allowed to access
Google Kubernetes Engine (GKE) and other Cloud de Confiance resources in Enterprise
Example Organization's organization. Enterprise Example organization already
has a workforce identity pool called `enterprise-example-organization-employees`.

To allow Partner Example Organization to manage access to Enterprise Example
Organization's resources, Enterprise Example Organization creates a separate
workforce pool for Partner Example Organization workforce users so that Partner
Example Organization can manage it. Enterprise Example Organization provides
the workforce pool to a Partner Example Organization administrator. Partner
Example Organization's administrator uses their own IdP to grant access to their
workforce.

To do this, Enterprise Example Organization's Admin performs the following
tasks:

- 

Create an identity such as `partner-organization-admin@example.com` for the
Partner Example Organization administrator in Enterprise Example
Organization's IdP, which is already configured in the pool called
`enterprise-example-organization-employees`.

- 

Create a new workforce pool called `example-organization-partner`.

- 

Create the following allow policy for the `example-organization-partner`
pool:


```
{ 
"bindings" : [ 
{ 
"role" : "roles/iam.workforcePoolEditor" , 
"members" : [ 
"principalSet://iam.googleapis.com/locations/global/workforcePools/enterprise-example-organization-employees/subject/partner-organization-admin@example.com" 
] 
} 
] 
} 
```


- 

Grant roles for the `example-organization-partner` pool on the resources they
need access to in Enterprise Example Organization's organization.

Partner Example Organization's administrator can now configure the
`example-organization-partner` pool to connect with their IdP. They can then
allow Partner Example Organization workforce to sign in with Partner Example
Organization's IdP credentials. After they sign in, Partner Example Organization
workforce users can access Cloud de Confiance resources, constrained by policies
that are defined by Enterprise Example Organization.

### Security groups best practices

In large enterprises, IT administrators often create security groups as part
of a best-practices access-control model. Security groups govern access to
internal resources. Further, companies often create additional groups for
employees and other groups for partners to extend this access-control model to
cloud resources. This can result in proliferation of deeply nested groups that
can become very difficult to manage.

Your organization might also have policies that limit the number of groups that
you can create so as to keep the user directory hierarchy reasonably flat. A
better solution to prevent misconfiguration of allow policies and limit growth
of groups is to use multiple pools to create a broader separation of users from
different organizational units and business units, and partner organizations.
You can then reference these pools and groups contained within these pools to
define allow policies (see examples in the Configuring IAM step).
For additional recommendations on group governance and pool management, see
[Best practices for using Workforce Identity Federation](/iam/docs/best-practices-workforce-identity-federation).

### VPC Service Controls limitations

Workforce Identity Federation administrative features, including workforce pool
configuration APIs don't support VPC Service Controls.
However, Cloud de Confiance products that support both [Workforce Identity Federation](/iam/docs/federated-identity-supported-services)
and [VPC Service Controls](/vpc-service-controls/docs/supported-products) operate
as documented and are subject to VPC Service Controls policy checks. Additionally, you can
use [third-party identities](/vpc-service-controls/docs/configure-identity-groups)
such as workforce pool users and workload identities in the ingress or egress rules of VPC Service Controls.

For Security Token Service API requests where the audience is a [Workforce Identity Federation](/iam/docs/federated-identity-supported-services)
pool (which is an organization-level resource), you must configure egress rules. This
is necessary because VPC Service Controls does not support adding organization-level
resources directly to perimeters. The following egress rules allow requests originating from
the perimeter to reach the Workforce STS APIs that interact with
organization-level Workforce pools:


```
- egressTo : 
operations : 
- serviceName : 'sts.googleapis.com' 
methodSelectors : 
- method : '*' 
resources : 
- '*' 
egressFrom : 
identityType : ANY_IDENTITY 
```


### Workforce Identity Federation and Essential Contacts

To receive important information about changes to your organization or
Cloud de Confiance products, you must provide [Essential Contacts](/resource-manager/docs/managing-notification-contacts) when using
Workforce Identity Federation. Cloud Identity users can be contacted through
their Cloud Identity email address, but Workforce Identity Federation users
are contacted using Essential Contacts.

When you use the Cloud de Confiance console to create or manage workforce identity pools,
you see a banner that asks you to configure an essential contact with the
**Legal** and **Suspension** category. Alternatively, define a contact in the
**All** category if you don't have separate contacts. Supplying the contacts
removes the banner.

## What's next

- Review [Architecture patterns for identity federation](/iam/docs/federated-identity-architectures).

- Review [Best practices for using Workforce Identity Federation](/iam/docs/best-practices-workforce-identity-federation).

- To learn how to set up Workforce Identity Federation, see [Configuring Workforce Identity Federation](/iam/docs/configuring-workforce-identity-federation).
For IdP-specific instructions, see the following:

- [Configure Workforce Identity Federation with Microsoft Entra ID and sign in users](/iam/docs/workforce-sign-in-microsoft-entra-id)

- [Configure Workforce Identity Federation with Okta and sign in users](/iam/docs/workforce-sign-in-okta)

- [Obtain short-lived tokens for Workforce Identity Federation](/iam/docs/workforce-obtaining-short-lived-credentials)

- [Manage workforce pools providers](/iam/docs/manage-workforce-identity-pools-providers)

- [Delete Workforce Identity Federation users and their data](/iam/docs/workforce-delete-user-data)

- [View Workforce Identity Federation audit logs](/iam/docs/audit-logging/examples-workforce-identity)

- [View products that support Workforce Identity Federation](/iam/docs/federated-identity-supported-services)

- [Set up user access to console (federated)](/iam/docs/workforce-console-sso)