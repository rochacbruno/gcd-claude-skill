# Authentication basics

Source: https://berlin.devsitetest.how/docs/get-started/authentication
Last updated: 2026-07-10

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












# Authentication basics 






- On this page ** 
- [ Principal types ](#principals)
- [ Configure your Google Cloud Dedicated in Germany organization for authentication ](#configure)
- [ Authenticate humans and workloads ](#authenticate)

- [ Authenticate humans ](#interactive-work)
- [ Authenticate workloads ](#workloads)

- [ What's next ](#whats_next)
- 












Before you can interact with Google Cloud Dedicated in Germany APIs and services, you need to prove
that you are who you say you are. This process of proving your identity is known
as authentication.

To authenticate to Google Cloud Dedicated in Germany, you must provide *credentials* as evidence of
your identity. For example, to use a service, you might authenticate using
credentials such as a password and a one-time code.

Google Cloud Dedicated in Germany refers to authenticated users as *principals*. When you attempt to
access a resource such as a Google Cloud Dedicated in Germany project or storage bucket, Google Cloud Dedicated in Germany
checks what level of access your principal has to the requested resource. This
process is called
[*authorization*](/docs/get-started/authorization-access-control), and is
handled by a system called Identity and Access Management (IAM).

These same concepts apply to code performing automated tasks on your behalf,
which are known as *workloads*. A workload must provide credentials to prove its
identity and authenticate as a principal, after which Google Cloud Dedicated in Germany can determine
what level of access the workload has to the resources it has requested.

## Principal types

There are different types of principals that you can authenticate as. You might
even use different principal types at different stages of a task, or across
different development environments.

The primary principal types and the credentials they require to authenticate
include the following:










- 


Service accounts**: These are accounts specific to Google Cloud Dedicated in Germany that workloads
can use to access services or resources. You typically don't authenticate as a service account
directly. Instead, you attach a service account to a resource such as a Compute Engine
VM, or use [service account impersonation](/docs/authentication/use-service-account-impersonation).




- 


**Federated principals**: These are identities that reference user or service accounts in
an external identity provider. There are two types of federated principals supported by
Google Cloud Dedicated in Germany, which have similar names:





- 


**[ Workforce Identity Federation**](/iam/docs/workforce-identity-federation) : Lets human users sign in to Google Cloud Dedicated in Germany with identities managed by
an external identity provider. If your organization already has single sign-on (SSO) set
up, you might use this type of identity to authenticate to Google Cloud Dedicated in Germany.




Your identity provider must support
[OpenID Connect (OIDC)](https://openid.net/connect/) or
[
SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) to use Workforce Identity Federation.




- 


**[Workload Identity Federation](/iam/docs/workload-identity-federation)**: Lets workloads running outside of Google Cloud Dedicated in Germany operate on
Google Cloud Dedicated in Germany resources.




You can use Workload Identity Federation with workloads that authenticate using
[
X.509 client certificates](/iam/docs/workload-identity-federation-with-x509-certificates); that run on
[
Amazon Web Services (AWS) or Azure](/iam/docs/workload-identity-federation-with-other-clouds); on-premises
[
Active Directory](/iam/docs/workload-identity-federation-with-active-directory); deployment services, such as
[
GitHub and GitLab](/iam/docs/workload-identity-federation-with-deployment-pipelines); and with any identity provider that supports
[
OpenID Connect (OIDC) or Security Assertion Markup Language (SAML) V2.0](/iam/docs/workload-identity-federation-with-other-providers).







To learn more about these and other supported principal types in Google Cloud Dedicated in Germany,
see [Principal types](/iam/docs/principals-overview#principal-types).

## Configure your Google Cloud Dedicated in Germany organization for authentication

When setting up authentication for your Google Cloud Dedicated in Germany organization, you might
need to integrate existing systems and workflows into Google Cloud Dedicated in Germany:

- 

If you have an existing identity provider that you want to use, you need to
set up
[Workforce Identity Federation](/iam/docs/workforce-identity-federation).

- 

If you have workloads running outside of Google Cloud Dedicated in Germany that need access to
Google Cloud Dedicated in Germany resources, you need to set up
[Workload Identity Federation](/iam/docs/workload-identity-federation).

We recommend that you also do the following to help secure your Google Cloud Dedicated in Germany
environment:

- 

Make sure
[multi-factor authentication is enabled](/docs/authentication/mfa-requirement)
for your users.

- 

Check if you need to change
[reauthentication settings](/docs/authentication/reauthentication).

- 

Create policies for
[managing API keys](/docs/authentication/api-keys-best-practices).

- 

Create policies for
[managing service account keys](/iam/docs/best-practices-for-managing-service-account-keys).

## Authenticate humans and workloads

How you authenticate to Google Cloud Dedicated in Germany depends on the APIs and services that
you're using, and the way in which you interact with those APIs and services.

### Authenticate humans

When performing manual, interactive work such as incidental administrative
tasks, setting up resources, changing configurations, experimenting, and
browsing logs, you use your user account's credentials to authenticate.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




For interactive work in the Google Cloud Dedicated console, you authenticate by
signing in to the web interface with your user credentials.



[Go to the Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/)

The same credentials for your Google Cloud Dedicated console session are used for
[Cloud Shell](/shell/docs/how-cloud-shell-works), where you can access
the gcloud CLI.



After you
[install the gcloud CLI on your local device](/sdk/docs/install-sdk),
you can use your user credentials to authenticate to Google Cloud Dedicated in Germany by
running the following command in your terminal:


```
gcloud auth login
```


After you authenticate, subsequent `gcloud` commands use the signed-in
principal to make their requests.

For authenticating with Workforce Identity Federation credentials,
Workload Identity Federation credentials, or service account keys, see
[Authentication for the gcloud CLI](/sdk/docs/authenticate).



### Authenticate workloads

Whether you're developing and running code on your local device, in
Google Cloud Dedicated in Germany, on-premises, or in another cloud, the most flexible and portable
way to authenticate your workload is to provide credentials through a mechanism
called *Application Default Credentials (ADC)*.

Libraries that implement ADC (such as the
[Google Cloud Dedicated in Germany client libraries](/apis/docs/client-libraries-explained)) check
known locations in the environment they're run in for credentials. This means
that, if you change where your code runs, you don't need to change the code
itself—only the credentials that are used for that environment.

For example, when developing locally, you can set your environment so that
ADC makes use of your user credentials for authentication. When your code is
ready for production, you can deploy it unchanged to a Compute Engine VM
instance, and set the environment to use short-lived service account credentials
to authenticate instead.

You can't use ADC to authenticate in the following scenarios:

- 

When authenticating the gcloud CLI.

- 

When using an [API key](/docs/authentication/api-keys-use). API keys can only
be used with specific APIs.

To learn how to set up ADC for specific environments, see
[Set up Application Default Credentials](/docs/authentication/provide-credentials-adc).

## What's next

- 

Learn more about the different
[authentication methods for Google Cloud Dedicated in Germany](/docs/authentication).

- 

To understand how you control what a principal can access in Google Cloud Dedicated in Germany, see
[Authorization and access control](/docs/get-started/authorization-access-control).