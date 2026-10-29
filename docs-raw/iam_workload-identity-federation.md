# Workload Identity Federation

Source: https://berlin.devsitetest.how/iam/docs/workload-identity-federation
Last updated: 2026-10-26

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

Identity and Access Management (IAM)

](https://berlin.devsitetest.how/iam/docs)






- 








[

Guides

](https://berlin.devsitetest.how/iam/docs/overview)












# Workload Identity Federation 















This document provides an overview of Workload Identity Federation.
Using Workload Identity Federation, you can provide on-premises or multicloud
workloads with access to Google Cloud Dedicated in Germany resources by using federated identities
instead of a service account key.

You can use Workload Identity Federation with workloads that authenticate
using
[X.509 client certificates](/iam/docs/workload-identity-federation-with-x509-certificates);
that run on
[Amazon Web Services (AWS) or Azure](/iam/docs/workload-identity-federation-with-other-clouds);
on-premises
[Active Directory](/iam/docs/workload-identity-federation-with-active-directory);
deployment services, such as
[GitHub and GitLab](/iam/docs/workload-identity-federation-with-deployment-pipelines);
and with any identity provider (IdP) that supports
[OpenID Connect (OIDC) or Security Assertion Markup Language (SAML) V2.0](/iam/docs/workload-identity-federation-with-other-providers).

## Why Workload Identity Federation?

Applications running outside Google Cloud Dedicated can use
[service account keys](/iam/docs/service-account-creds#key-types)
to access Google Cloud Dedicated resources. However, service account keys are
powerful credentials, and can present a security risk if they are not managed
correctly. Workload Identity Federation eliminates the maintenance and
security burden associated with service account keys.

With Workload Identity Federation, you can use Identity and Access Management (IAM)
to grant [IAM roles](/iam/docs/overview#roles) to [principals](/iam/docs/principals-overview)
that are based on federated identities in a workload identity pool. You can
grant access to the principals on specific Google Cloud Dedicated resources. This
approach is called *direct access*. Alternatively, you can grant access to a
service account, which can then access Google Cloud Dedicated resources. This
approach is called *service account impersonation*.

## Workload identity pools

A *workload identity pool* is an entity that lets you manage external
identities.

In general, we recommend creating a new pool for each non-Google Cloud Dedicated
environment that needs to access Google Cloud Dedicated resources, such as
development, staging, or production environments.

## Workload identity pool providers

A *workload identity pool provider* is an entity that describes a relationship
between Google Cloud Dedicated and your IdP, including the following:

- AWS

- Microsoft Entra ID

- GitHub

- GitLab

- Kubernetes clusters

- Okta

- On-premises Active Directory Federation Services (AD FS)

- Terraform

Workload Identity Federation follows the [OAuth 2.0 token exchange](https://tools.ietf.org/html/rfc8693)
specification. You provide a credential from your IdP to the [Security Token Service](/iam/docs/reference/sts/rest),
which verifies the identity on the credential, and then returns a federated
token in exchange.

### OIDC provider with local JWKs

To federate workloads that don't have a public OIDC endpoint, you can upload
OIDC JSON Web Key Sets (JWKS) directly to the pool. This is common if you have
Terraform or GitHub Enterprise hosted in your own environment or you have
regulatory requirements not to expose public URLs. For more information, see
[Manage OIDC JWKs (Optional)](/iam/docs/workload-identity-federation-with-other-providers#manage-oidc-keys).

### Attribute mappings

The tokens issued by your external IdP contain one or more
attributes. Some IdPs refer to these attributes as *claims*.

Google Security Token Service tokens also contain one or more attributes, as listed
in the following table:



| 
Attribute | 
Description | 
|

| 
`google.subject` | 

Required. A unique identifier for the user. This attribute is used in
IAM `principal://` role bindings and appears in
Cloud Logging logs.
The value must be unique and can't exceed 127 characters.
| 
|

| 
`google.groups` | 

Optional. A set of groups that the identity belongs to. This attribute is
used in IAM `principalSet://` role bindings to
grant access to all members of a group.
| 
|

| 
`attribute. NAME ` | 

Optional. You can define up to 50 custom attributes and use these
attributes in IAM `principalSet://` role
bindings to grant access to all identities with a certain attribute.
| 
|


An attribute mapping defines how to derive the value of the Google
Security Token Service token attribute from an external token. For each Google
Security Token Service token attribute, you can define an attribute mapping,
formatted as follows:

` TARGET_ATTRIBUTE `=` SOURCE_EXPRESSION `

Replace the following:

- ` TARGET_ATTRIBUTE ` is an attribute of the Google
Security Token Service token

- ` SOURCE_EXPRESSION ` is a
[Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md#introduction)
expression that transforms one or more attributes from the tokens issued by
your external IdP

The following list provides attribute mapping examples:

- 

Assign the assertion attribute `sub` to `google.subject`:


```
google.subject=assertion.sub
```


- 

Concatenate multiple assertion attributes:


```
google.subject='myprovider::' + assertion.aud + '::' + assertion.sub
```


- 

Map a GUID-valued assertion attribute `workload_id`
to a name, and assign the result to a custom attribute named `attribute.my_display_name`:


```
attribute.my_display_name={
"8bb39bdb-1cc5-4447-b7db-a19e920eb111": "Workload1",
"55d36609-9bcf-48e0-a366-a3cf19027d2a": "Workload2"
}[assertion.workload_id]
```


- 

Use CEL [logical operators and functions](https://github.com/google/cel-spec/blob/master/doc/langdef.md#list-of-standard-definitions)
to set a custom attribute named `attribute.environment` to either
`prod` or `test`, depending on the identity's Amazon Resource Name (ARN):


```
attribute.environment=assertion.arn.contains(":instance-profile/Production") ? "prod" : "test"
```


- 

Use the [`extract` function](/iam/docs/conditions-attribute-reference#extract)
to populate a custom attribute `aws_role` with the name of the assumed role or,
if no role has been assumed, with the identity's ARN.


```
attribute.aws_role=assertion.arn.contains('assumed-role') ? assertion.arn.extract('{account_arn}assumed-role/') + 'assumed-role/' + assertion.arn.extract('assumed-role/{role_name}/') : assertion.arn
```


- 

Use the [`split` function](https://pkg.go.dev/github.com/google/cel-go/ext#readme-split)
to split a string on a specified separator. For example, to extract the
attribute `username` from an email address attribute by splitting its value
at the `@` symbol and using the first string, use the following attribute
mapping:


```
attribute.username=assertion.email.split("@")[0]
```


- 

Use the [`join` function](https://pkg.go.dev/github.com/google/cel-go/ext#readme-join)
to join a list of strings on a specified separator. For example, to
populate the custom attribute `department` by concatenating a list of
strings with `.` as a separator, use the following attribute mapping:


```
attribute.department=assertion.department.join(".")
```


When you use
[X.509 client certificates](/iam/docs/workload-identity-federation-with-x509-certificates#mappings-and-conditions),
Workload Identity Federation maps `google.subject` to the client certificate
subject common name (`assertion.subject.dn.cn`) by default:


```
google.subject=assertion.subject.dn.cn
```


You can also map additional attributes from the leaf and intermediate
certificates.

For [AWS](/iam/docs/workload-identity-federation-with-other-clouds#mappings-and-conditions),
if you don't specify an attribute mapping, Google applies the following default
mapping, which covers most common scenarios:


```
google.subject=assertion.arn
attribute.aws_role=assertion.arn.contains('assumed-role') ? assertion.arn.extract('{account_arn}assumed-role/') + 'assumed-role/' + assertion.arn.extract('assumed-role/{role_name}/') : assertion.arn
```


This mapping sets `google.subject` to the caller's ARN and sets
`attribute.aws_role` to the assumed role ARN (without the session name) if a
role is assumed, or to the caller's ARN otherwise. You can also supply custom
mappings.

For OIDC and SAML providers, you must supply the attribute mappings. To
construct the mapping, consult the provider's documentation for a list of
attributes on their credentials.

For more details, see the API documentation for the
[`attributeMapping` field](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider.FIELDS.attribute_mapping).

### Attribute conditions

An *attribute condition* is a CEL expression that can check assertion attributes
and target attributes. If the attribute condition evaluates to `true` for a
given credential, the credential is accepted. Otherwise, the credential is
rejected.

You can use an attribute condition to restrict which identities can authenticate
using your workload identity pool.

Attribute conditions are useful in scenarios such as the following:

- 

If your workload uses an IdP that's available to the general
public, you can restrict access so only the identities you choose have access
to your workload identity pool.

- 

If you're using an IdP with multiple cloud platforms, you can
prevent credentials intended for use with another platform from being used
with Google Cloud Dedicated, and vice-versa. This helps avoid the
[confused deputy problem](https://wikipedia.org/wiki/Confused_deputy_problem).

The attribute condition for a workload identity pool provider can use the
`assertion` keyword, which refers to a map that represents the authentication
credential issued by the IdP. You can use dot notation to access
the map's values. For example, AWS credentials include an `arn` value, which you
can access as `assertion.arn`. In addition, the attribute condition can use any
attribute that is defined in the provider's [attribute mapping](#mapping).

The following example only allows requests from identities that have a specific
AWS role:


```
attribute.aws_role == " ROLE_MAPPING " 
```


For more details, see the API documentation for the
[`attributeCondition` field](/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers#WorkloadIdentityPoolProvider.FIELDS.attribute_condition).

## Access management

The token exchange flow returns a federated access token. You can use this
federated access token to grant your workload access on behalf of
[principal identities](#principal-types) on Google Cloud Dedicated resources and obtain a
[short-lived OAuth 2.0 access token](/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth).

You can use this access token to provide IAM access.

We recommend that you use Workload Identity Federation to provide access
[directly to a Google Cloud Dedicated resource](#direct-resource-access).
Although most Google Cloud Dedicated APIs support Workload Identity Federation,
some APIs have [limitations](/iam/docs/federated-identity-supported-services).
As an alternative, you can use [service account impersonation](#impersonation).

The short-lived access token lets you call any Google Cloud Dedicated APIs that the
resource or service account has access to.

### Direct resource access

You can use *direct resource access* to grant to your external identity access
directly on a Google Cloud Dedicated resource using resource-specific roles.

### Alternative: Service account impersonation

As an alternative to providing [direct resource access](#direct-resource-access) you
can use [service account impersonation](/iam/docs/workload-identity-federation-with-other-clouds#impersonation).

You must grant your service account the role Workload Identity User
(`roles/iam.workloadIdentityUser`).

### Principal scopes and security

You grant access to principals or subsets thereof by using [principal types](#principal-types).

## Principal types

The following table describes how to define principals as individuals and groups
of identities:




| 
Identities | 

Identifier format | 

|









| 
Single identity | 


`principal://iam.googleapis.com/projects/ PROJECT_NUMBER /locations/global/ workloadIdentityPools/ POOL_ID /subject/ SUBJECT_ATTRIBUTE_VALUE `
| 

|




| 
All identities in a group | 


`principalSet://iam.googleapis.com/projects/ PROJECT_NUMBER /locations/global/ workloadIdentityPools/ POOL_ID /group/ GROUP_ID `
| 

|



| 

All identities with a specific *attribute value*
| 


`principalSet://iam.googleapis.com/projects/ PROJECT_NUMBER /locations/global/ workloadIdentityPools/ POOL_ID /attribute. ATTRIBUTE_NAME / ATTRIBUTE_VALUE `
| 

|



## What's next

- 

Use Workload Identity Federation to let your workloads access resources
from [AWS or Azure](/iam/docs/workload-identity-federation-with-other-clouds),
[X.509 Certificates](/iam/docs/workload-identity-federation-with-x509-certificates),
[Active Directory](/iam/docs/workload-identity-federation-with-active-directory),
[Deployment pipelines](/iam/docs/workload-identity-federation-with-deployment-pipelines), or
[OIDC or SAML providers](/iam/docs/workload-identity-federation-with-other-providers).

- 

Learn how to [manage workload identity pools](/iam/docs/manage-workload-identity-pools-providers)
using the Google Cloud CLI or the REST API.