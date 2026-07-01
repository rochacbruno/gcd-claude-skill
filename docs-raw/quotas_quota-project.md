# Quota project overview

Source: https://berlin.devsitetest.how/docs/quotas/quota-project
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://berlin.devsitetest.how/docs/quotas)






- 








[

Guides

](https://berlin.devsitetest.how/docs/quotas/overview)












# Quota project overview 






- On this page 
- [ How the quota project is determined ](#project-determined)

- [ Resource-based APIs ](#project-resource-based)
- [ Client-based APIs ](#project-client-based)

- [ Determine if an API is resource-based or client-based ](#determine-api)
- [ What's next ](#whats_next)
- 










This document describes the *quota project* and how the quota project is
determined. Make sure that your quota project is set correctly to help avoid
errors and failed requests to the Cloud APIs.

You must specify a quota project because every request to a Google Cloud Dedicated in Germany API is
counted against a quota and because quotas are enforced by project. For more
information, see [How to set the quota
project](/docs/quotas/set-quota-project) 
.

Note for gcloud CLI users: the *quota project* is sometimes referred
to as the *billing project*. This is because the [`billing_project`
flag](/sdk/gcloud/reference#--billing-project) 
takes precedence over the [`billing/quota_project`
property](/sdk/gcloud/reference/config/set#quota_project) in your
gcloud CLI configuration.

## How the quota project is determined 

How the quota project is determined depends on the type of API method that you
use: *resource-based API* or *client-based API*. In rare cases, a service might
have both types of API methods.

### Resource-based APIs

For resource-based Cloud APIs, the project that provides quota for
an API call is also the project that contains the resource that is being
accessed. For example, when you create a Compute Engine instance, you must
specify the project for that new instance. The project then contains the newly
created instance. Later, if you perform operations on the Compute Engine
instance, the project that contains the instance provides the quota for the
request. This applies regardless of whether you use the Google Cloud CLI, REST
API, or client libraries.

You cannot change the quota project used by a request to a resource-based API.
The request always uses the project that contains the resource that the request
is operating on.

### Client-based APIs

If an API is not a resource-based API, it's a client-based API. For example, the
Cloud Translation API is a commonly used client-based API.

Requests can fail if you make a request to a client-based API and the quota
project cannot be identified. The quota project can be set in multiple ways and
is verified by checking the following options. They appear in the order of
precedence:

- 

**Specified in request**: The quota project that was specified in the
[request](/docs/quotas/set-quota-project#set-project-programmatically).
(When using client libraries, you can also use [environment
variables](/docs/quotas/set-quota-project#set-project-variable) 
in your requests.)

- 

**API key**: If you use an API key to provide credentials for a
request, the project associated with the API key is used as the quota
project.

- 

**Google Cloud CLI credentials**: If you use the gcloud CLI
to get your access token, and you've authenticated to the
gcloud CLI with your user credentials, the gcloud CLI
shared project is sometimes used as the quota project. However, not all
client-based APIs fall back on the shared project.

- 

**Service account**: If the principal for the API call is a service
account, including by impersonation, the project associated with the service
account is used as the quota project.

- 

**Workforce identity federation**: If the principal for the API is a
workforce identity federation user, the
[workforce pools user project](/iam/docs/workforce-identity-federation#workforce-pools-user-project) 
is used as the quota project.

If none of the previous checks yield a quota project, the request fails.

#### About the gcloud CLI shared project for client-based APIs

If you use the gcloud CLI to make a request to a client-based API
without setting the quota project, the request might fall back on the
*gcloud CLI shared project*, or the request might fail. The
gcloud CLI shared project is used by all gcloud CLI
requests in all projects, so if many other gcloud CLI requests are
also using this project as their quota project, the quota for the shared project
might temporarily be depleted. If this happens, your request fails with an
out-of-quota error message.

#### Identify the current quota project for client-based APIs

The method for identifying the quota project depends on how your project is
configured:

- 

If an API method is configured to use a resource-based API, the client
project uses the resource project as the quota project.

- 

If a user project override is in place, use the
[`gcloud [command] --log-http` command](/sdk/gcloud/reference#--log-http)
to print a log and check the quota project that appears in the
`x-goog-user-project` field.

- 

If an API key was used for authentication, use the
[`gcloud [command] --log-http` command](/sdk/gcloud/reference#--log-http)
to print a log and check the quota project that appears in the
`x-goog-api-key` field.

For other configurations, the quota project doesn't appear in HTTP headers.

## Determine if an API is resource-based or client-based

It can be difficult to determine which type of API you're using. However,
activation and quotas are enforced in the same way. For example, if a service
account from project A calls a read method in project B, and neither project has
the API enabled, the `API not enabled` error message indicates which project is
checked for activation. The project checked for activation is the same project
checked for
[rate quota](/docs/quotas/overview#types_of_quota).

## What's next

- 

Learn how to set the [quota
project](/docs/quotas/set-quota-project) 

- 

Learn more about [Application Default
Credentials](/docs/authentication/application-default-credentials) 

- 

Get more information about
[authentication](/docs/authentication) 

- 

Understand [quotas](/docs/quotas/overview)

- 

For gcloud CLI users:

- For more information about
gcloud CLI configurations, see the
[`gcloud config`](/sdk/gcloud/reference/config) 
reference documentation

- For more information about the `--billing_project` flag, see the [
Google Cloud SDK reference](/sdk/gcloud/reference#--billing-project)