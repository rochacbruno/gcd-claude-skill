# Troubleshoot your ADC setup

Source: https://berlin.devsitetest.how/docs/authentication/troubleshoot-adc
Last updated: 2026-06-25

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












# Troubleshoot your ADC setup 






- On this page 
- [ User credentials not working ](#user-creds-client-based)
- [ Incorrect credentials ](#incorrect-creds)
- [ Unrecognized credential type ](#unrecognized-cred-type)
- 









This page describes some common problems you might encounter when using
Application Default Credentials (ADC).

For information about how ADC works, including where credentials are found, see
[How Application Default Credentials works](/docs/authentication/application-default-credentials).

## User credentials not working 

If your API request returns an error message about user credentials not being
supported by this API, the API not being enabled in the project, or no quota
project being set, review the following information.

There are two kinds of Google Cloud Dedicated APIs:

- 

*Resource-based APIs*, which use the project associated with the resources
being accessed for billing and quota.

- 

*Client-based APIs*, which use the project associated with the client
accessing the resources for billing and quota.

When you provide user credentials to authenticate to a client-based API, you
must specify the project to use for billing and quota. This project is called
the *quota project*.

There are a number of ways to specify a quota project, including the following
options:

- 

Update your ADC file to use a different project as the quota project:


```
gcloud auth application-default set-quota-project YOUR_PROJECT 
```


- 

If you are using the gcloud CLI to call the API, you can set
your quota project in your gcloud CLI config:


```
gcloud config set billing/quota_project YOUR_PROJECT 
```


- 

If you are calling the REST or RPC API directly, use the
`x-goog-user-project` HTTP header to specify a quota project in each
request. For details, see
[Set the quota project with a REST request](/docs/authentication/rest#set-billing-project).

You must have the `serviceusage.services.use` IAM permission for
a project to be able to designate it as your billing project. The
`serviceusage.services.use` permission is included in the Service Usage Consumer
IAM role. If you don't have the `serviceusage.services.use`
permission for any project, contact your security administrator or a project
owner who can give you the Service Usage Consumer role in the project.

For more information about quota projects, see
[Quota project overview](/docs/quotas/quota-project). For information about additional ways
to set the quota project, see [Set the quota project](/docs/quotas/set-quota-project).

## Incorrect credentials

If your credentials don't seem to be providing the access you expect, or aren't
found, check the following:

- 

If you are using the gcloud CLI to access Google Cloud Dedicated in a
local environment, make sure you understand which credentials you are using.
When you use the gcloud CLI, you are using the credentials you
provided to the gcloud CLI by using the `gcloud auth login`
command. You are not using the credentials you provided to ADC. For more
information about these two sets of credentials, see
[gcloud CLI authentication configuration and ADC configuration](/docs/authentication/provide-credentials-adc#gcloud-credentials).

- 

Make sure that the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is
set *only* if you are using a service account key or other JSON file for ADC.
The credentials pointed to by the environment variable take precedence over
other credentials, including for Workload Identity Federation for GKE.

- 

Confirm that the principal making the request has the required
IAM roles. If you are using user credentials, then the roles
must be granted to the email address associated with the user account. If
you are using a service account, then that service account must have the
required roles.

- 

If you provide an API key with the API request, the API key takes precedence
over ADC in any location. If you have set the `GOOGLE_APPLICATION_CREDENTIALS`
environment variable and you are using an API key, the API might return a
warning telling you that the credentials you provided to ADC are being
ignored. To stop the warning, unset the `GOOGLE_APPLICATION_CREDENTIALS`
environment variable. 

## Unrecognized credential type

If your API request returns an error that includes `Error creating credential
from JSON. Unrecognized credential type`, make sure you are using a valid
credential. Client ID files are not supported to provide credentials for ADC.