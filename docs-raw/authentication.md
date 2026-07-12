# Authentication for Google Cloud Dedicated in Germany APIs and services

Source: https://berlin.devsitetest.how/docs/authentication
Last updated: 2026-07-10

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












# Authentication for Google Cloud Dedicated in Germany APIs and services 






- On this page 
- [ Introduction ](#introduction)
- [ How to get help with authentication ](#quick-links)
- [ Choose the right authentication method for your use case ](#auth-decision-tree)
- [ Authorization methods for Google Cloud Dedicated services ](#authorization-gcp)
- [ Application Default Credentials ](#adc)
- [ Terminology ](#terminology)

- [ Authentication ](#authentication)
- [ Authorization ](#authorization)
- [ Credentials ](#credentials)
- [ Principal ](#principal)
- [ Token ](#token)
- [ Workload and workforce ](#workload-workforce)

- [ What's next ](#whats_next)
- 









This document helps you understand some key authentication methods and concepts
and where to get help with implementing or troubleshooting authentication.

## Introduction 

Authentication is the process by which your identity is confirmed
through the use of some kind of [credential](#credentials). Authentication is
about proving that you are who you say you are.

Google provides many APIs and services, which require
authentication to access. Google also provides a number of
services that host applications written by our customers; these applications
also need to determine the identity of their users.

Google APIs implement and extend the
[OAuth 2.0 framework](https://datatracker.ietf.org/doc/html/rfc6749).

## How to get help with authentication



| 
Action | 
Instructions | 
|


| 

Authenticate to a Google Cloud Dedicated service from my application using
a high-level programming language.
| 

[Set up Application Default Credentials](/docs/authentication/provide-credentials-adc),
and then use one of the
[Cloud Client Libraries](/docs/authentication/client-libraries).
| 
|

| 


Authenticate to an application that requires an ID token.
| 


[Get an OpenID Connect (OIDC) ID token](/docs/authentication/get-id-token)
and provide it with your request.
| 
|


| 

Try out some `gcloud` commands in my local development
environment.
| 

[Initialize the gcloud CLI](/sdk/docs/initialize).
| 
|

| 

Try out some Google Cloud Dedicated REST API
requests in my local development environment.
| 

Use a command-line tool such as `curl` to
[call the REST API](/docs/authentication/rest).
| 
|

| 

Try out a code snippet included in my product documentation.
| 

[Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment),
and install your product's client library in your local environment. The
client library
[finds your credentials automatically](/docs/authentication/client-libraries).
| 
|



## Choose the right authentication method for your use case

When you access Google Cloud Dedicated in Germany services by using the Google Cloud CLI, Cloud Client Libraries,
tools that support
[
Application Default Credentials (ADC)](/docs/authentication/application-default-credentials)
like Terraform, or REST requests, use the following diagram to help you choose an authentication
method:



This diagram guides you through the following questions:


- 
Are you running code in a single-user development environment, such as your own workstation,
Cloud Shell, or a virtual desktop interface?



- If yes, proceed to question 4.

- If no, proceed to question 2.




- Are you running code in Google Cloud Dedicated in Germany?



- If yes, proceed to question 3.

- If no, proceed to question 5.




- Are you running containers in Google Kubernetes Engine?



- 
If yes, use
[
Workload Identity Federation for GKE](/kubernetes-engine/docs/how-to/workload-identity#authenticating_to)
to attach service accounts to Kubernetes pods.


- 
If no,
[attach a service account](/iam/docs/attach-service-accounts#attaching-to-resources)
to the resource.





- 


Does your use case require a service account?



For example, you want to configure authentication and authorization consistently for your
application across all environments.





- 
If no,
[authenticate with user credentials](/docs/authentication/set-up-adc-local-dev-environment#local-user-cred).


- 
If yes,
[
impersonate a service account with user credentials](/docs/authentication/use-service-account-impersonation).





- 
Does your workload authenticate with an external identity provider that supports
[workload identity federation](/iam/docs/workload-identity-federation#providers)?



- 
If yes,
[
configure Workload Identity Federation](/iam/docs/workload-identity-federation-with-other-clouds)
to let applications running on-premises or on other cloud providers use a service account.


- 
If no,
[create a service account key](/docs/authentication/set-up-adc-local-dev-environment#local-key).





## Authorization methods for Google Cloud Dedicated services

Authorization for Google Cloud Dedicated is primarily handled by
[Identity and Access Management (IAM)](/iam/docs/overview). IAM offers granular
control by principal and by resource.

You can apply another layer of authorization with
[OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) scopes. When you
authenticate to a Google Cloud Dedicated service, you can use a global scope that
authorizes access to *all* Google Cloud Dedicated services
(`https://www.googleapis.com/auth/cloud-platform`), or, if a service supports
it, you can restrict access with a more limited scope. Limited scopes can
help to reduce risk if your code is running in environments where compromised
tokens might be a concern, such as mobile apps.

The authorization scopes that are accepted by an API method are listed in the
API reference documentation for each Google Cloud Dedicated service.

## Application Default Credentials

[Application Default Credentials (ADC)](/docs/authentication/application-default-credentials) is a strategy used by the authentication libraries to automatically find
credentials based on the application environment. The authentication libraries make those
credentials available to
[Cloud Client Libraries and Google API Client Libraries](/apis/docs/client-libraries-explained).
When you use ADC, your code can run in either a development or production environment without
changing how your application authenticates to Google Cloud Dedicated in Germany services and APIs.

Using ADC can simplify your development process, because it lets you use the
same authentication code in a variety of environments. If you're using a service
in express mode, however, you don't need to use ADC.

Before you can use ADC, [you must provide your credentials to ADC](/docs/authentication/provide-credentials-adc),
based on where you want your code to run. ADC
[automatically locates credentials](/docs/authentication/application-default-credentials) and gets a token in the background,
enabling your authentication code to run in different environments without
modification. For example, the same version of your code could authenticate with
Google Cloud Dedicated APIs when running on a development workstation or on
Compute Engine.

Your gcloud credentials are not the same as the credentials you provide to ADC using the
gcloud CLI. For more information, see
[
gcloud CLI authentication configuration and ADC configuration](/docs/authentication/provide-credentials-adc#gcloud-credentials).

## Terminology

The following terms are important to understand when discussing authentication
and authorization.

### Authentication

Authentication is the process of determining the identity of the principal
attempting to access a resource.

### Authorization

Authorization is the process of determining whether the principal or application
attempting to access a resource has been authorized for that level of access.

### Credentials

When this document uses the term *user account*, it refers to a user account managed
by your identity provider and federated with
[Workforce Identity Federation](/iam/docs/workforce-identity-federation).

For authentication, credentials are a digital object that provide proof of
identity. Passwords, PINs, and biometric data can all be used as credentials,
depending on the application requirements. For example, when you log into your
user account, you provide your password and satisfy any two-factor
authentication requirement as proof that the account in fact belongs to you, and
you are not being spoofed by a bad actor.

[Tokens](#token) are not credentials. They are a digital object that proves that
the caller provided proper credentials.

The type of credential you need to provide depends on what you are
authenticating to.

The following types of credentials can be created in the
Google Cloud Dedicated console:


- 

API keys



You can use API keys with APIs that accept them to access the API. API
keys that are not bound to a service account provide a project, which is
used for billing and quota purposes. If the API key is bound to a service
account, the API key also provides the identity and authorization of the
service account ([Preview](https://berlin.devsitetest.how/products#product-launch-stages)).




For more information about API
keys, see [API keys](/docs/authentication/api-keys). For more
information about API keys that are bound to a service account, see the
[Google Cloud express mode FAQ](https://berlin.devsitetest.how/resources/cloud-express-faqs).





- 

Service account keys



Service account keys identify a principal (the service account) and the
project associated with the service account.





You can also create credentials by using the gcloud CLI. These
credentials include the following types:

- [Local ADC files](/docs/authentication/set-up-adc-local-dev-environment#local-user-cred)

- Credential configurations used by
[Workload Identity Federation](/iam/docs/workload-identity-federation)

- Credential configurations used by [Workforce Identity Federation](/iam/docs/workforce-identity-federation)

### Principal

A principal is an identity that can be granted access
to a resource. For authentication, Google APIs support two types of principals:
[user accounts](#user-accounts) and [service accounts](#service-accounts).

Whether you use a user account or a service account to authenticate depends on
your use case. You might use both, each at different stages of your project or
in different development environments.

#### User accounts

User accounts represent a developer, administrator, or any other person who
interacts with Google APIs and services.

User accounts are managed by your identity provider and federated with
[Workforce Identity Federation](/iam/docs/workforce-identity-federation).

With a user account, you can authenticate to Google APIs and services in the
following ways:

- Use the gcloud CLI to
[set up Application Default Credentials (ADC)](/docs/authentication/set-up-adc-local-dev-environment#local-user-cred).

- Use your user credentials to
[sign in to the Google Cloud CLI](/sdk/docs/authenticate), and then use the tool to
access Google Cloud Dedicated services.

- Use your user credentials to [impersonate a service account](/docs/authentication/use-service-account-impersonation).

- Use your user credentials to
[sign in to the Google Cloud CLI](/sdk/docs/authenticate), and then use the tool to
[generate access tokens](/docs/authentication/rest).

#### Service accounts

[Service accounts](/iam/docs/service-account-overview) are accounts that do not
represent a human user. They provide a way to manage authentication and
authorization when a human is not directly involved, such as when an application
needs to access Google Cloud Dedicated resources. Service accounts are managed by
IAM.

The following list provides some methods for using a service account to
authenticate to Google APIs and services, in order from most secure to least
secure. For more information, see
[Choose the right authentication method for your use case](#auth-decision-tree)
on this page.

- 

[Attach a user-managed service account to the resource](/docs/authentication/set-up-adc-attached-service-account) and
[use ADC to authenticate](/docs/authentication/client-libraries).

This is the recommended way to authenticate production code running on
Google Cloud Dedicated.

- 

[Use a service account to impersonate another service account](/iam/docs/create-short-lived-credentials-direct).

Service account impersonation lets you temporarily grant more privileges to
a service account. Granting extra privileges on a temporary basis enables
that service account to perform the required access without having to
permanently acquire more privilege.

- 

Use [Workload Identity Federation](/iam/docs/workload-identity-federation) to authenticate workloads that run
on-premises or on a different cloud provider.

- 

Use the [default service account](/iam/docs/service-account-types#default).

Using the default service account isn't recommended because it's highly privileged by default, which violates the [principle of least privilege](/iam/docs/using-iam-securely#least_privilege).

- 

[Use a service account key](/docs/authentication/set-up-adc-local-dev-environment#local-key).

For an overview of ways to configure workload identities, including service
accounts, for Google Cloud Dedicated in Germany,
see [Identities for workloads](/iam/docs/workload-identities). For best practices,
see [Best practices for using service accounts](/iam/docs/best-practices-service-accounts).

### Token

For authentication and authorization, a token is a digital object that shows
that a caller provided proper credentials that were exchanged for that token.
The token contains information about the identity of the principal making the
request and the type of access they're authorized for.

Tokens can be thought of as being like hotel keys. When you check in to a hotel
and present the proper documentation to the hotel registration desk, you receive
a key that gives you access to specific hotel resources. For example, the key
might give you access to your room and the guest elevator, but would not give
you access to any other room or the service elevator.

With the exception of API keys, Google APIs do not support credentials directly.
Your application must acquire or generate a token and provide it to the API.
There are several different types of tokens. For more information, see
[Tokens overview](/docs/authentication/tokens).

### Workload and workforce

Google Cloud Dedicated identity and access products enable access to
Google Cloud Dedicated services and resources for both programmatic access and human
users. Google Cloud Dedicated uses the terms *workload* for programmatic access and
*workforce* for user access.

[Workload Identity Federation](/iam/docs/workload-identity-federation) lets you provide access to
on-premises or multi-cloud workloads without having to create and manage
service account keys.

[Workforce Identity Federation](/iam/docs/workforce-identity-federation) lets you use an external identity provider
to authenticate and authorize a workforce—a group of users, such as employees,
partners, and contractors—using IAM, so that the users can access
Google Cloud Dedicated services.

## What's next

- Learn more about how Google Cloud Dedicated services
[use IAM to control access to Google Cloud Dedicated resources](/iam/docs/overview).

- Understand [how Application Default Credentials works](/docs/authentication/application-default-credentials), and
[how you can set it up for a variety of development environments](/docs/authentication/provide-credentials-adc).