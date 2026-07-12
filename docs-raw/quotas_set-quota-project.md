# Set the quota project

Source: https://berlin.devsitetest.how/docs/quotas/set-quota-project
Last updated: 2026-07-10

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












# Set the quota project 






- On this page 
- [ Set the quota project programmatically ](#set-project-programmatically)

- [ Client library ](#client_library)
- [ gcloud CLI ](#gcloud-cli-commands)
- [ REST request ](#rest_request)

- [ Set the quota project using an environment variable ](#set-project-variable)
- [ Set the quota project using authentication credentials ](#set-project-credentials)
- [ Permissions required to set and use the quota project ](#project-permissions)
- [ Set the quota user ](#set_the_quota_user)
- [ What's next ](#whats_next)
- 










This document describes how to set a quota project for your
[client-based APIs.](/docs/quotas/quota-project#project-client-based) 
For information about what the quota project
is, how to set the quota API, and how the quota project is determined,
see [About the quota project.](/docs/quotas/quota-project) 

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

There are several ways to set quota projects. If the quota project is specified
by more than one method, the following precedence is applied:

- Programmatically

- Environment variable

- Credentials used to authenticate the request

## Set the quota project programmatically

You can explicitly set the quota project in your application. This method
overrides all other definitions. The [principal](/docs/authentication#principal) 
used to authenticate the request must have the required permission on the
specified quota project.

How you set the quota project programmatically depends on whether
you're using a client library, the gcloud CLI, or REST API request.

### Client library

You can set the value for the quota project by using client options when you
create the client. This method works well if you want to control the value for
your quota project from your application, regardless of what environment it's
running in.

For more information about implementing client options, see your client library
documentation.

### gcloud CLI

You can set the quota project for all gcloud CLI commands by using
the `billing/quota_project` property in your gcloud CLI configuration. You can
also set the quota project for a specific command by using the `--billing-project`
flag, which takes precedence over the configuration property.

For more information about `gcloud` CLI configurations, see the
[`gcloud config` documentation](/sdk/gcloud/reference/config).
For more information about the `--billing-project` flag, see the
[`--billing-project` documentation](/sdk/gcloud/reference#--billing-project).

### REST request

You can specify the quota project in a REST request using the
[`x-goog-user-project` header.](/apis/docs/system-parameters#definitions) 
The principal making the request must have the required permissions on the quota
project.

For more information and sample code, see
[Set the quota project with a REST request](/docs/authentication/rest#set-billing-project).

## Set the quota project using an environment variable

Client libraries for some languages support setting the quota project using an
environment variable. This approach can be helpful if you want to set the quota
project differently in different shells, or to override the quota project
associated with the credential. The principal for any request must have the
required permissions on the quota project specified by the environment variable.

The environment variable is language dependent:




| 
Language | 
Environment variable | 
|



| 
C++ | 


`GOOGLE_CLOUD_CPP_USER_PROJECT`
| 
|

| 
C# | 


`GOOGLE_CLOUD_QUOTA_PROJECT`
| 
|

| 
Go | 


`GOOGLE_CLOUD_QUOTA_PROJECT`
| 
|

| 
Java | 


`GOOGLE_CLOUD_QUOTA_PROJECT`
| 
|

| 
Node.js | 


`GOOGLE_CLOUD_QUOTA_PROJECT`
| 
|

| 
Python | 


`GOOGLE_CLOUD_QUOTA_PROJECT`
| 
|

| 
PHP | 


`GOOGLE_CLOUD_QUOTA_PROJECT`
| 
|

| 
Ruby | 
Not available | 
|



## Set the quota project using authentication credentials

If the quota project isn't specified, the authentication libraries try to
determine it from the credentials that were used for the request. This process
depends on the type of credentials that were used to authenticate the request:

- **Service account** – The project associated with the service account is
used as the quota project.

- **User credentials** – For a local development environment,
[Application Default Credentials](/docs/authentication/application-default-credentials) 
finds your user credentials from the local ADC file. That file can also specify
a quota project. If you have the project set in your Google Cloud CLI config, and you
have the required permissions on that project, the quota project is set by
default when you create the local ADC file. You can also set the ADC quota
project by using the
[`auth application-default set-quota-project` command.](/sdk/gcloud/reference/auth/application-default/set-quota-project) 

- **API keys** – When you use an API key to provide credentials for a request,
the project associated with the API key is used as the quota project.

## Permissions required to set and use the quota project









































































To get the permission that
you need to set a project as the quota project, or use that quota project in a request,

ask your administrator to grant you the
[Service Usage Consumer ](/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) IAM role on the project.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).







This predefined role contains the
`serviceusage.services.use`
permission,
which is required to
set a project as the quota project, or use that quota project in a request.







You might also be able to get
this permission
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









If you use a project you created as your quota project, you have the necessary
permissions.

For more information about permissions, see [Quota permissions](/docs/quotas/permissions).

## Set the quota user

Some APIs also restrict the number of requests per user, which is different from
the per-project quotas described in prior sections of this document.

By default, the system uses the authenticated principal, such as user accounts
using OAuth tokens, service accounts, or federated workload identities. If
there is no authenticated principal, the system uses the client IP address.
Using client IP fallback might group multiple users behind a shared NAT or
proxy into the same quota bucket, risking premature quota limits.

If you need to override the quota user—for example, if you make requests from
a common server on behalf of different users—you can set the `quotaUser`
parameter through the Cloud API [System parameters](/apis/docs/system-parameters).
If you do specify a `quotaUser` or `X-Goog-Quota-User`, a valid API key with
service restrictions, such as IP address restrictions or HTTP referrer
restrictions, must be used to identify the quota project. Otherwise, the
`quotaUser` parameter is ignored.

To protect user privacy and restrict metric volume, the Google Cloud Dedicated console
doesn't show individual per-user or client IP quota usage telemetry; system
limits are configured and monitored at the project and consumer level.

To learn more about Cloud API system parameters and their definitions, see the
system parameters [definitions table](/apis/docs/system-parameters#definitions).

## What's next

- About the [quota project](/docs/quotas/quota-project) 

- Learn more about [Application Default Credentials](/docs/authentication/application-default-credentials) 

- Get more information about [authentication](/docs/authentication) 

- Understand [quotas](/docs/quotas/overview)