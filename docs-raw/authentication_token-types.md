# Token types

Source: https://berlin.devsitetest.how/docs/authentication/token-types
Last updated: 2026-07-21

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/authentication/tpc-differences) for more details.














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

Application development

](https://berlin.devsitetest.how/docs/application-development)






- 








[

Google Cloud SDK

](https://berlin.devsitetest.how/sdk/docs)






- 








[

Authentication

](https://berlin.devsitetest.how/docs/authentication)






- 








[

Guides

](https://berlin.devsitetest.how/sdk/docs/overview)












# Token types 






- On this page 
- [ Access tokens ](#access-tokens)

- [ Service account access tokens ](#sa-access-tokens)
- [ Service account JSON Web Tokens ](#sa-jwts)
- [ Federated access tokens ](#fed-access-tokens)
- [ Agent identity access tokens ](#agent-identity-access-tokens)
- [ Credential access boundary tokens ](#cred-access-boundary-tokens)
- [ Client-issued credential access boundary tokens ](#client-cred-access-boundary-tokens)

- [ Token-granting tokens ](#token-granting-tokens)

- [ Federated refresh tokens ](#federated-refresh-tokens)
- [ Federated authorization codes ](#federated-authorization-codes)
- [ External JSON Web Tokens ](#external-jwts)
- [ External SAML assertions or responses ](#external-saml)
- [ Amazon Web Services (AWS) GetCallerIdentity token ](#aws-token)

- [ Identity tokens ](#identity-tokens)

- [ Service account ID tokens ](#sa-id-tokens)
- [ Agent identity ID tokens ](#agent-identity-id-tokens)
- [ Identity-Aware Proxy assertions ](#iap-assertions)

- 









Google Cloud Dedicated in Germany uses multiple types of tokens for authentication. You can
categorize these types of tokens by their purpose and parties they're exchanged
between.




| 
Token category | 
Communication path | 
Purpose | 
|



| 
[Access tokens](#access-tokens) | 
Authorization server
⭢ Client
⭢ Google API | 
Lets clients call Google Cloud Dedicated in Germany APIs. | 
|

| 
[Token-granting tokens](#token-granting-tokens) | 
Authorization server
⭤ Client
| 

Lets clients obtain new or different tokens, possibly at a later point
in time.
| 
|

| 
[Identity tokens](#identity-tokens) | 
Authorization server
⭢ Client
| 
Lets clients identify the user they're interacting with. | 
|




Most access and identity tokens are *bearer tokens*. Bearer tokens grant access
to the party in possession of the token, regardless of how they obtained the
token. If a bad actor intercepts a bearer token, they can use it to gain
unauthorized access.

*Bound tokens* grant access to a specific client. To use a bound token, a client
must provide additional proof that they're the rightful owner of the token.
Bound tokens are therefore more restrictive than bearer tokens and can help
reduce the risk of token theft.

## Access tokens

Access tokens allow clients to make authenticated calls to Google Cloud Dedicated in Germany APIs.
Google Cloud Dedicated in Germany supports multiple different types of access tokens, which have the
following properties in common:

- 

They authenticate a principal, which can be a user or a workload.

- 

They're issued to one particular client.

- 

They're short-lived and expire after at most a few hours.

- 

They're restricted to certain OAuth scopes, endpoints, or resources. This
means that an access token typically doesn't grant access to all of a user's
resources, but only to a certain subset of them.

Access tokens can differ in the following ways:

- 

**Issuer**: The party that issues the token.

- 

**Principal**: The type of principal that the token can authenticate.

- 

**Restrictions**: The restrictions that can be imposed on the token.

The following table lists the different types of access tokens:




| 
Token type | 
Issuer | 
Principals | 
Restrictions | 
|




| 
[Service account access token](#sa-access-tokens) | 


Google Cloud Dedicated in Germany IAM authorization server

| 
Service account | 
OAuth scope | 
|


| 
[Service account JSON Web Token (JWT)](#sa-jwts) | 
Client | 
Service account | 
OAuth scope or API | 
|

| 
[Federated access token](#fed-access-tokens) | 
Google Cloud Dedicated in Germany IAM authorization server | 




- Workforce identity pool principal

- Workload identity pool principal


| 
OAuth scope | 
|

| 
[Agent identity access token](#agent-identity-access-tokens) | 
Google Cloud Dedicated in Germany IAM authorization server | 
Agent identity principal | 
OAuth scope | 
|

| 

[
Credential access boundary token](#cred-access-boundary-tokens)
| 
Google Cloud Dedicated in Germany IAM authorization server | 




- User (managed user)

- User (consumer account)

- Service account


| 
Specific Cloud Storage objects | 
|

| 

[
Client-issued credential access boundary token](#client-cred-access-boundary-tokens)
| 
Client | 
Service account | 
Specific Cloud Storage objects | 
|



The different types of access tokens also exhibit different security properties:

- **Format**: Some access tokens are opaque, meaning they are in a proprietary
format and can't be inspected. Other tokens are encoded as a JSON Web Token,
which can be decoded by the client.

- **Lifetime**: Tokens differ in lifetime and to what extent they can be
modified.

- **Revocability**: Some tokens can be revoked. Other tokens remain valid until
expiry.

- **Binding**: Some tokens can optionally be bound to an additional credential,
which makes them *bound tokens*.

The following table summarizes the differences between the access token types.




| 
Token type | 
Format | 
Introspectable | 
Lifetime | 
Revocable | 
Binding | 
|




| 
Service account access token | 
Opaque | 

No | 

5 minutes–12 hours | 
No | 
| 
|


| 
Service account JSON Web Token (JWT) | 
JWT | 
N/A | 
5 minutes–1 hour | 
No | 
| 
|

| 
Federated access token | 
Opaque | 
No | 
See [Federated access tokens](#fed-access-tokens) | 
No | 
| 
|

| 
Agent identity access token | 
Opaque | 
No | 
See [Agent identity access tokens](#agent-identity-access-tokens) | 
No | 
X.509 client certificate | 
|

| 
Credential access boundary token | 
Opaque | 
No | 
See
[
Credential access boundary tokens](#cred-access-boundary-tokens)
| 
No | 
| 
|

| 
Client-issued credential access boundary token | 
Opaque | 
No | 
N/A | 
No | 
| 
|



### Service account access tokens

Service account access tokens are bearer tokens that authenticate a service
account. The tokens are opaque.

For a service account access token, the API returns output similar to the
following example:


```
{ 
"azp" : "000000000000000000000" , 
"aud" : "000000000000000000000" , 
"scope" : "https://www.googleapis.com/auth/userinfo.email" , 
"exp" : "1744687132" , 
"expires_in" : "3568" , 
"email" : "service-account@example.eu0.iam.gserviceaccount.com" , 
"email_verified" : "true" , 
"access_type" : "online" 
} 
```


A service account token includes the following fields:




| 
Field | 
Name | 
Description | 
|



| 
`aud` | 
Audience | 

The service account that the token is for, equivalent to the
authorized party.
| 
|

| 
`azp` | 
Authorized party | 

The service account that requested the token, identified by its unique
ID.
| 
|

| 
`email` | 
Primary email address | 



The service account's email address.



This field is only present if the token includes the
[
`https://www.googleapis.com/auth/userinfo.email`](https://www.googleapis.com/auth/userinfo.email)
scope.


| 
|

| 
`exp` | 
Expiry | 
The expiry time of the token, in Unix epoch time format. | 
|



Service account access tokens can't be revoked and stay valid until they expire.


By default, service account access tokens expire after one hour. By using the
[`serviceAccounts.generateAccessToken`](/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateAccessToken)
method, you can request tokens with different lifetimes. Because longer token
lifetimes can increase risk, you must configure the
[`iam.allowServiceAccountCredentialLifetimeExtension`](/resource-manager/docs/organization-policy/restricting-service-accounts#extend_oauth_ttl)
constraint to allow clients to request service account access tokens with
lifetimes longer than one hour.

### Service account JSON Web Tokens

Service account JSON Web Tokens (JWTs) are bearer tokens that authenticate a
service account. Whereas
[service account access tokens](#sa-access-tokens) are issued by an
authorization server, service account JWTs can be issued by the client itself.

Sometimes these are called "self-signed" JWTs. They can be useful when you need
to authenticate to some Google APIs without getting an access token from the
authorization server—for example, when creating your own client libraries.

To issue a service account JWT, clients must perform the following steps:

- 

Prepare a JSON web signature payload that includes the service account's
email address, an OAuth scope or API endpoint, and an expiry time.

- 

Sign the payload using a service account key of the respective service
account. Clients can sign the payload offline by using a user-managed
service account key, or online by using the `signJwt` method and a
Google-managed service account key. For more information, see
[Create a self-signed JSON Web Token](/iam/docs/create-short-lived-credentials-direct#sa-credentials-jwt)

A decoded service account JWT looks similar to the following, with
` SIGNATURE ` replaced by the token's signature:


```
{ 
"alg" : "RS256" , 
"kid" : "290b7bf588eee0c35d02bf1164f4336229373300" , 
"typ" : "JWT" 
} . { 
"iss" : "service-account@example.eu0.iam.gserviceaccount.com" , 
"sub" : "service-account@example.eu0.iam.gserviceaccount.com" , 
"scope" : "https://www.googleapis.com/auth/cloud-platform" , 
"exp" : 1744851267 , 
"iat" : 1744850967 
} . SIGNATURE 
```


Instead of specifying an OAuth scope in the `scope` key, a service account JWT
can specify an API endpoint in the `aud` key:


```
{ 
"alg" : "RS256" , 
"kid" : "290b7bf588eee0c35d02bf1164f4336229373300" , 
"typ" : "JWT" 
} . { 
"iss" : "service-account@example.eu0.iam.gserviceaccount.com" , 
"sub" : "service-account@example.eu0.iam.gserviceaccount.com" , 
"aud" : "https://cloudresourcemanager.googleapis.com/" , 
"exp" : 1744854799 , 
"iat" : 1744851199 
} . SIGNATURE 
```


A service account JWT includes the following fields:




| 
Field | 
Name | 
Description | 
|



| 
`aud` | 
Audience | 

API endpoints that the client is allowed to access. Only valid if
`scope` isn't specified.
| 
|

| 
`exp` | 
Expiry | 
The expiry time of the token, in Unix epoch time format. | 
|

| 
`iat` | 
Issue time | 
The time the token was issued, in Unix epoch time format. | 
|

| 
`iss` | 
Issuer | 
The issuer of the token, which is the service account itself. | 
|

| 
`scope` | 
OAuth scopes | 

The set of APIs that the client is allowed to access, identified by
[
OAuth scope](https://developers.google.com/identity/protocols/oauth2/scopes). Only valid if `aud` isn't specified.
| 
|

| 
`sub` | 
Subject | 
Authenticated principal, which is the service account itself. | 
|



Service account JWTs can be valid for up to one hour, and they can't be revoked.

### Federated access tokens

Federated access tokens are bearer tokens that authenticate an identity
workforce pool principal or a workload identity pool principal.

Workforce Identity Federation lets clients exchange an external token against a
federated access token that authenticates a workforce pool principal. The
workforce identity pool principal is identified by a principal identifier
similar to the following:


```
principal://iam.googleapis.com/locations/global/workforcePools/ POOL /subject/raha@altostrat.com.
```


Workload Identity Federation lets clients exchange an external token against a
federated access token that authenticates a workload pool principal. The
workload identity pool principal is identified by a principal identifier similar
to the following:


```
principal://iam.googleapis.com/projects/ PROJECT /locations/global/workloadIdentityPools/ POOL /subject/ SUBJECT_ATTRIBUTE_VALUE 
```


Federated access tokens are opaque and can't be introspected. The tokens can't
be revoked and remain valid until expiry. The expiries for each token type are
set as follows:

- 

Workforce Identity Federation sets the token expiry to the smaller of the
following two values:

- 

Time left until the Workforce Identity Federation session expires

- 

1 hour

The expiry of the Workforce Identity Federation session is determined based on
the time of sign-in and the session duration configured for the
Workforce Identity Federation pool.

- 

Workload Identity Federation sets the token expiry so that it matches the expiry
of the external token.

### Agent identity access tokens

Agent identity access tokens authenticate an agent that has been assigned an
[agent identity](/agent-builder/agent-engine/agent-identity) and use a principal
identifier similar to the following:


```
principal://agents.global.org- ORGANIZATION_ID .system.id.goog/resources/aiplatform/projects/ PROJECT_NUMBER /locations/us-central1/reasoningEngines/ REASONING_ENGINE_ID 
```


The principal identifier is based on the SPIFFE ID of the agent's X.509 client
certificate, but uses the prefix `principal://` instead of `spiffe://`.

An agent can obtain an agent identity access token from the Compute Engine
metadata server. Optionally, the agent can request the token to be bound to its
X.509 client certificate. A bound agent identity access token is only valid when
used over a mutual TLS connection that is authenticated using the X.509 client
certificate that the token has been bound to.

Like [federated access tokens](#fed-access-tokens), agent identity access tokens
are opaque, can't be introspected or revoked, and remain valid until expiry. By
default, agent identity access tokens are valid for 1 hour, but a token's expiry
might be shorter when bound to an X.509 client certificate that is close to
expiry.

### Credential access boundary tokens

Credential access boundary tokens are bearer tokens that authenticate a user or
service account and
[include an access boundary](/iam/docs/downscoping-short-lived-credentials). The
access boundary restricts the token so that it can only be used to access a
defined subset of Cloud Storage resources.

Credential access boundary tokens are sometimes referred to as *downscoped*
because they're derived from an input token, but are more restricted in the
resources they grant access to.

The expiry of credential access boundary tokens is derived from the expiry of
the input token, which
is a
[service account access token](#sa-access-tokens). Credential access boundary
tokens are opaque and they can't be introspected or revoked.

### Client-issued credential access boundary tokens

Client-issued credential access boundary tokens are similar to
[credential access boundary tokens](#cred-access-boundary-tokens), but are
optimized for scenarios in which clients need to obtain credential access
boundary tokens with different access boundaries at high frequency.

Clients can create client-issued credential access boundary tokens locally by
using the Cloud Client Libraries and an access boundary intermediary token,
which they must refresh periodically.

Client-issued credential access boundary tokens are opaque and they can't be
introspected or revoked.

## Token-granting tokens

Token-granting tokens allow clients to obtain new or different tokens, possibly
at a later time. Google Cloud Dedicated in Germany supports multiple different types of
token-granting tokens, and they all have the following in common:

- 

They represent a prior authentication.

- 

They authenticate a principal, which can be a Google identity (a user or
workload) or an external identity.

- 

They can be redeemed for an access token.

- 

They can't be used for making Google API calls, which distinguishes them from
access tokens.

Token-granting tokens can differ in the following ways:

- 

**Issuer**: The party that issues the token.

- 

**Principal**: The type of principal identity that the token can authenticate.

- 

**Restrictions**: The restrictions that can be imposed on the token.

The following table lists the different types of token-granting tokens.




| 
Token type | 
Issuer | 
Redeemed access token type | 
Principals | 
Restrictions | 
|




| 
[Federated refresh token](#federated-refresh-tokens) | 
Google Cloud Dedicated in Germany IAM authorization server | 
Federated access token | 
Workforce identity pool principal | 
OAuth scope | 
|

| 
[Federated authorization code](#federated-authorization-codes) | 
Google Cloud Dedicated in Germany IAM authorization server | 
Federated access token | 
Workforce identity pool principal | 
OAuth scope | 
|


| 
[External JSON Web Token](#external-jwts) | 
External identity provider | 
Federated access token | 
External principal | 
None | 
|

| 
[External SAML assertion or response](#external-saml) | 
External identity provider | 
Federated access token | 
External principal | 
None | 
|

| 

[
Amazon Web Services (AWS) `GetCallerIdentity` token](#aws-token)
| 
External identity provider | 
Federated access token | 
External principal | 
None | 
|



The different types of token-granting tokens also exhibit different security
properties:

- 

**Format**: Some tokens are opaque. Other tokens can be decoded by the client.

- 

**Lifetime**: Tokens differ in lifetime, and to what extent they can be
modified.

- 

**Multi-use**: Some token-granting tokens can only be used once. Other tokens
can be used multiple times.

- 

**Revocability**: Some tokens can be revoked. Other tokens remain valid until
expiry.

- 

**Binding**: Some tokens are bound to an additional credential, which makes
them *bound tokens*. Other tokens are not bound, which makes them
*bearer tokens*.

The following table summarizes the differences between these properties for
token-granting tokens:




| 
Token type | 
Format | 
Lifetime | 
Revocable | 
Multi-use | 
Binding | 
|




| 
Federated refresh token | 
Opaque | 
Varies, see [Federated refresh tokens](#federated-refresh-tokens) | 
No | 
Yes | 
OAuth client credentials | 
|

| 
Federated authorization code | 
Opaque | 
10 minutes | 
No | 
No | 
OAuth client credentials | 
|


| 
External token or external JSON Web Token | 
JWT | 
Depends on identity provider | 
Depends on identity provider | 
Yes | 
| 
|

| 
External SAML assertion or response | 
SAML | 
Depends on identity provider | 
Depends on identity provider | 
Yes | 
| 
|

| 
Amazon Web Services (AWS) `GetCallerIdentity` token | 
Text blob | 
Depends on identity provider | 
Depends on identity provider | 
Yes | 
| 
|



### Federated refresh tokens

Federated refresh tokens are opaque tokens that let clients obtain access
tokens for a workforce identity pool principal, if the user previously
authorized a client to act on their behalf.

Like [refresh tokens](#refresh-tokens), federated refresh tokens are tied to a
specific client and can only be used in combination with valid client
credentials; for example, a client ID and client secret.

Unlike refresh tokens, federated refresh tokens can't be revoked. The lifetime
of a federated refresh token is linked to the workforce identity session that
was used to obtain the token and it remains valid until the session expires.

### Federated authorization codes

Like [authorization codes](#authorization-codes), federated authorization codes
are opaque, short-lived tokens.
[The codes are only intended to be used during user authentication as an intermediary](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1)
between the client and the Google Cloud Dedicated in Germany IAM authorization server.

Authorization codes are tied to a client, can only be used in combination with
valid client credentials, and can only be used once.

### External JSON Web Tokens

External JSON Web Tokens (JWTs) are issued by an external identity provider such
as Microsoft Entra ID, Okta, Kubernetes, or GitHub. They might differ in their
structure and contents.

By configuring Workforce Identity Federation or Workload Identity Federation, you can
set up a trust relationship between Google Cloud Dedicated in Germany and an external identity
provider. Workloads can then use external JWTs as token-granting tokens to
obtain [federated access tokens](#fed-access-tokens).

When you use Workforce Identity Federation, the resulting federated access token
authenticates a *workforce* identity pool principal.

When you use Workload Identity Federation, the resulting federated access token
authenticates a *workload* identity pool principal.

In both cases, the principal identifier is derived from one or more claims of
the external JWT.

To be compatible with Workforce Identity Federation or Workload Identity Federation,
external JWTs must satisfy
[specific requirements](/iam/docs/workload-identity-federation-with-other-providers#prepare).

### External SAML assertions or responses

External
[Security Assertion Markup Language](https://wiki.oasis-open.org/security)
(SAML) assertions are SAML 2.0 assertions that are issued by an external
identity provider such as Microsoft Entra ID, Okta, or Active Directory
Federation Services. These external SAML assertions can optionally be enclosed
in a SAML 2.0 response or be encrypted.

Like with [external JSON Web Tokens](#external-jwts), you can configure
Workforce Identity Federation or Workload Identity Federation so that workloads can use
external SAML assertions or responses as token-granting tokens to obtain
[federated access tokens](#fed-access-tokens).

To be compatible with Workforce Identity Federation or Workload Identity Federation,
external SAML assertions must satisfy
[specific requirements](/iam/docs/workload-identity-federation-with-other-providers#prepare).

### Amazon Web Services (AWS) `GetCallerIdentity` token

External AWS `GetCallerIdentity` tokens are text blobs that contain a signed
request to the AWS
[`GetCallerIdentity` API](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html).
Similar to external JSON Web Tokens, you can configure Workforce Identity Federation or Workload Identity Federation so
that workloads can use these text blobs as a token-granting token to obtain
[federated access tokens](#fed-access-tokens).

## Identity tokens

Identity (ID) tokens let clients identify the user that they're interacting
with. Google Cloud Dedicated in Germany supports multiple different types of identity tokens, and
they all have the following in common:

- 

They're signed but not encrypted, so that they can be decoded, verified, and
interpreted by the client.

- 

They authenticate a principal, which can be a user or a workload.

- 

They're issued to one particular client.

- 

They're short-lived and expire after at most one hour.

- 

They're not revocable.

- 

They can't be used for making Google API calls, which distinguishes them from
[access tokens](#access-tokens).

- 

They can't be used to obtain access tokens, which distinguishes them from
[token-granting tokens](#token-granting-tokens).

- 

They can be used to authenticate
[calls between microservices](/run/docs/authenticating/service-to-service), or
to [programmatically authenticate to
Identity-Aware Proxy (IAP)](/iap/docs/authentication-howto).

Identity tokens can differ in the following ways:

- 

**Audience**: The party that's intended to decode and consume the token.

- 

**Issuer**: The party that issues the token.

- 

**Principal**: The type of principal identity that the token can authenticate.

The following table lists the different types of identity tokens.




| 
Token type | 
Issuer | 
Audience | 
Principal | 
|




| 
[Service account ID token](#sa-id-tokens) | 
Google Cloud Dedicated in Germany IAM authorization server | 
Free to choose any audience | 
Service account | 
|

| 
[Agent identity ID token](#agent-identity-id-tokens) | 
Google Cloud Dedicated in Germany IAM authorization server | 
Free to choose any audience | 
Agent identity | 
|

| 

[
Identity-Aware Proxy (IAP) assertion](#iap-assertions)
| 
IAP | 




- Backend

- App Engine app


| 




- User (managed user)

- User (consumer account)

- Workforce identity pool principal


| 
|




The different types of identity tokens also exhibit different security
properties:

- 

**Format**: Some tokens are JSON Web Tokens (JWT), other tokens use XML
formatting.

- 

**Lifetime**: Tokens differ in lifetime.

- 

**Binding**: Some tokens can optionally be bound to an additional credential,
which makes them *bound tokens*.

The following table summarizes the differences between the identity token types.




| 
Token type | 
Format | 
Lifetime | 
Binding | 
|




| 
[Service account ID token](#sa-id-tokens) | 
JWT | 
1 hour | 
| 
|

| 
[Agent identity ID token](#agent-identity-id-tokens) | 
JWT | 
1 hour | 
X.509 client certificate | 
|

| 

[Identity-Aware Proxy (IAP) assertion](#iap-assertions)
| 
JWT | 
10 minutes | 
| 
|




### Service account ID tokens

Service account ID tokens are JSON Web Tokens (JWTs) that authenticate a service
account.

Unlike [service account JWTs](#sa-jwts) and
[service account JWT assertions](#sa-jwt-assertions), service account ID tokens
aren't signed by a service account key. Instead, service account ID tokens are
signed by the Google JSON Web Key Set (JWKS).

A decoded service account ID token looks similar to the following, with
` SIGNATURE ` replaced by the token's signature:


```
{ 
"alg" : "RS256" , 
"kid" : "c37da75c9fbe18c2ce9125b9aa1f300dcb31e8d9" , 
"typ" : "JWT" 
} . { 
"aud" : "example-audience" , 
"azp" : "112010400000000710080" , 
"email" : "service-account@example.eu0.iam.gserviceaccount.com" , 
"email_verified" : true , 
"exp" : 1745365618 , 
"iat" : 1745362018 , 
"iss" : "https://accounts.google.com" , 
"sub" : "112010400000000710080" 
} . SIGNATURE 
```


A service account ID token includes the following fields:




| 
Field | 
Name | 
Description | 
|



| 
`aud` | 
Audience | 

Identifier of the party that this token is for. The value can be freely
chosen by the token requester.
| 
|

| 
`azp` | 
Authorized party | 

The service account that requested the token, identified by its unique
ID.
| 
|

| 
`exp` | 
Expiry | 
The expiry time of the token, in Unix epoch time format. | 
|

| 
`iss` | 
Issuer | 

The issuer of the token, always set to
`https://accounts.google.com`.
| 
|

| 
`sub` | 
Subject | 

The service account that requested the token, identified by its unique
ID.
| 
|



The exact set of claims included in an ID token depends on the way the ID token
is requested. For example, ID tokens requested by the Compute Engine
metadata server can optionally include additional claims that
[assert the identity of the VM](/compute/docs/instances/verifying-instance-identity).
ID Tokens requested by using the
[IAM Credentials API](/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateIdToken)
can optionally contain the organization ID of the service account's project.

Service account ID tokens are valid for one hour, and can't be revoked.

### Agent identity ID tokens

Agent identity ID tokens are
[SPIFFE verifiable identity documents (JWT-SVID)](https://spiffe.io/docs/latest/spiffe-specs/jwt-svid/)
and authenticate an agent that has been assigned an
[agent identity](/agent-builder/agent-engine/agent-identity).

An agent can obtain an ID token from the Compute Engine metadata server.
Optionally, the agent can request the token to be bound to its X.509 client
certificate. A bound agent identity ID token contains the fingerprint of the
X.509 client certificate and is only valid when used over a mutual TLS connection
that is authenticated using the same X.509 client certificate.

Unlike [user ID tokens](#user-id-tokens) and
[service account ID tokens](#sa-id-tokens), agent identity ID tokens are not
signed by the Google JSON Web Key Set (JWKS) and they can't be verified.

A decoded agent identity ID token looks similar to the following, with
` SIGNATURE ` replaced by the token's signature:


```
{ 
"alg" : "RS256" , 
"kid" : "78ab40e4a0319f9ced58024f5bb66e6387d68066" , 
"typ" : "JWT" 
} . { 
"iss" : "https://sts.googleapis.com/v1/organizations/1234567890/locations/global/workloadIdentityPools/agents.global.org-1234567890.system.id.goog" , 
"sub" : "spiffe://agents.global.org-1234567890.system.id.goog/resources/aiplatform/projects/1234567890/locations/us-central1/reasoningEngines/987654321" , 
"aud" : [ "https://example.com/" ], 
"iat" : 1775776191 , 
"exp" : 1775779791 , 
"cnf" : { 
"x5t#S256" : "QTB5TSHeDxHrzDzcrrHU+/shhkfCnARcBEvMldp2uis" 
} 
} . SIGNATURE 
```


An agent identity ID token includes the following fields:




| 
Field | 
Name | 
Description | 
|



| 
`aud` | 
Audience | 

Identifier of the party that this token is for. The value can be
chosen by the token requester.
| 
|

| 
`exp` | 
Expiry | 
The expiry time of the token, in Unix epoch time format. | 
|

| 
`iss` | 
Issuer | 

The issuer of the token, which is the agent identity pool of
the organization or project that contains the agent.
| 
|

| 
`sub` | 
Subject | 
The SPIFFE ID of the agent. | 
|

| 
`cnf.x5t#S256` | 
Confirmation | 

The fingerprint of the X.509 client certificate that the token is
bound to. The claim is empty if the token is not bound.
| 
|



### Identity-Aware Proxy assertions

[Identity-Aware Proxy (IAP)](/iap/docs/concepts-overview) assertions are JSON
Web Tokens (JWTs) that IAP passes to
IAP-protected web applications in the `x-goog-iap-jwt-assertion`
HTTP request header. IAP assertions authenticate a user and also
serve as proof that a request was authorized by IAP.

IAP assertions are signed using
the
[IAP JWKS](https://www.gstatic.com/iap/verify/public_key-jwk).
This JWKS is a global resource, and the same signing keys are used for different
types of users, including the following:

- 

Managed user accounts

- 

Consumer accounts

- 

Service accounts

- 

Workforce identity pool principals

A decoded IAP assertion looks similar to the following, with
` SIGNATURE ` replaced by the token's signature:


```
{ 
"alg" : "ES256" , 
"typ" : "JWT" , 
"kid" : "4BCyVw" 
} . { 
"aud" : "/projects/0000000000/global/backendServices/000000000000" , 
"azp" : "/projects/0000000000/global/backendServices/000000000000" , 
"email" : "user@example.com" , 
"exp" : 1745374290 , 
"google" : { 
"access_levels" : [ 
"accessPolicies/0000000000/accessLevels/Australia" 
] 
}, 
"iat" : 1745373690 , 
"identity_source" : "WORKFORCE_IDENTITY" , 
"iss" : "https://cloud.google.com/iap" , 
"sub" : "sts.google.com:AAFTZ...Q" , 
"workforce_identity" : { 
"iam_principal" : "principal://iam.googleapis.com/locations/global/workforcePools/example/subject/user-0000000000" , 
"workforce_pool_name" : "locations/global/workforcePools/example" 
} 
} . SIGNATURE 
```


An IAP assertion includes the following fields:




| 
Field | 
Name | 
Description | 
|



| 
`aud` | 
Audience | 

The backend service, App Engine application, or Cloud Run
service that the IAP assertion is intended for.
| 
|

| 
`iss` | 
Issuer | 

The issuer of the token, always set to
`https://cloud.google.com/iap`
| 
|

| 
`sub` | 
Subject | 



The authenticated principal, identified by their unique ID.



If IAP is configured to use Google identities, this ID
is equivalent to the ID exposed in the
[
Directory API](https://developers.google.com/workspace/admin/directory/reference/rest/v1/users).


| 
|



For further details about the IAP assertion claims, see
[Verifying the JWT payload](/iap/docs/signed-headers-howto#verifying_the_jwt_payload).

IAP assertions are valid for 10 minutes, and can't be revoked.