# Troubleshoot quota errors

Source: https://berlin.devsitetest.how/docs/quotas/troubleshoot
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












# Troubleshoot quota errors 






- On this page 
- [ Exceeding rate quotas ](#exceeding_rate_quotas)
- [ Exceeding quota values ](#exceeding-quota-values)
- [ Exceeding quota values during a service rollout ](#exceeding_quota_values_during_a_service_rollout)
- [ Exceeding project quota ](#exceeding_project_quota)
- [ API error messages ](#api_error_messages)
- [ Google Cloud CLI errors ](#gcloud_cli_errors)

- [ Install and initialize ](#install_and_initialize)
- [ Set your quota project ](#set_your_quota_project)
- [ Update gcloud CLI components ](#update_gcloud_components)

- [ What's next ](#whats_next)
- 










You might receive quota errors for a number of reasons, such as exceeding quota
values or not setting the quota on a project correctly. If you want to be alerted
when errors happen, you can create custom alerts for specific
quota errors, as described in
[Set up quota alerts](/docs/quotas/set-up-quota-alerts).

## Exceeding rate quotas 

Rate quotas reset after a predefined time interval that is specific to each
service. For more information, see the quotas documentation for the specific
service.

## Exceeding quota values 

If your project exceeds its maximum quota value while using a service, Google Cloud Dedicated in Germany
returns an error based on how you accessed the service:

- If you exceed a quota value with an API request, Google Cloud Dedicated in Germany returns an HTTP
`413 REQUEST ENTITY TOO LARGE` status code.
Note that when using the BigQuery legacy streaming API in a production
environment, you may receive a `413 REQUEST ENTITY TOO LARGE` status code
if your HTTP requests are larger than 10 MB. You may also receive this error
if you exceed 300 MB per second. For more information see
[Streaming inserts.](/bigquery/quotas#streaming_inserts) 

- If you exceeded a quota value with an HTTP/REST request, Google Cloud Dedicated in Germany returns an
HTTP `429 TOO MANY REQUESTS` status code.

- If you exceed a quota for Compute Engine, Google Cloud Dedicated in Germany typically returns an
HTTP `403 QUOTA_EXCEEDED` status code, whether it was from API, HTTP/REST,
or gRPC. If the quota is a rate quota, then `403 RATE_LIMIT_EXCEEDED` is returned.

- If you exceeded a quota value using [gRPC](https://grpc.io), Google Cloud Dedicated in Germany returns a `ResourceExhausted`
error. How this error appears to you depends on the service.

- If you exceeded a quota value using a Google Cloud CLI command, the
gcloud CLI outputs a quota-exceeded error message and returns
with the exit code `1`.

- If you received a `QUOTA_EXCEEDED` message during a service rollout,
see the following section.

## Exceeding quota values during a service rollout

Google Cloud Dedicated in Germany sometimes changes the default quota values for resources
and APIs. These changes take place gradually, which means that during the
rollout of a new default quota, the quota value that appears in the Google Cloud Dedicated console
might not reflect the new quota value that is available to you.

If a quota rollout is in progress, you may receive an error message that states
`The future limit is the new default quota that will be available after a
service rollout completes.` If you see this error message, the cited quota value
and future value are correct, even if what appears in the Google Cloud Dedicated console
is different.

- 

For additional information, [view the audit logs](/logging/docs/audit#view-logs)
and look for a `QUOTA_EXCEEDED` message.


```
"status": {
...
"message": "QUOTA_EXCEEDED",
"details": [
{
...
"value": {
"quotaExceeded": {
...
"futureLimit": FUTUREVALUE 
}
}
}
]
},
```


- 

To view charts that show current and peak usage,
in the Google Cloud Dedicated console, go to the
[**IAM & Admin  > Quotas & System Limits**](https://console.cloud.berlin-build0.goog/quotas?project=_)
page and then click monitoring **Monitoring**.
You might need to go to the end of the table.

- 

If you need more quota, you can
[request a quota adjustment](/docs/quotas/help/request_increase).

## Exceeding project quota

For more information about requesting additional *project quotas*, refer to the
[Project quota requests](https://support.google.com/cloud/answer/6330231)
support article.

## API error messages

If your quota project (also called a billing project) isn't set correctly, API
requests might return error messages that are similar to the following:

- `User credentials not supported by this API`

- `API not enabled in the project`

- `No quota project set`

These and other errors can often be fixed by setting the quota project.
For more information, see [Quota project overview](/docs/quotas/quota-project).

## Google Cloud CLI errors

This section describes common issues encountered when getting started with the
Google Cloud CLI (gcloud CLI).

### Install and initialize

To use the gcloud CLI for Cloud Quotas, be sure to install and
initialize components:

- 

[Install](/sdk/docs/install) the gcloud CLI.

If you're using Cloud Shell, you can skip this step because
gcloud CLI comes pre-installed.

- 

[Initialize](/sdk/docs/initialize) the gcloud CLI.

- 

[Install the beta component](/sdk/docs/components#alpha_and_beta_components)
by running the following command:


```
gcloud components install beta
```


### Set your quota project

If you haven't set your quota project, gcloud CLI commands might
return an error like the following:


```
PERMISSION_DENIED: Your application is authenticating by using local Application Default Credentials.
The cloudquotas.googleapis.com API requires a quota project, which is not set by default.
```


To resolve this issue, add the `--billing-project` flag on your
gcloud CLI command to explicitly set the quota project, or rerun
`gcloud config set billing/quota_project CURRENT_PROJECT` to set the quota project
as the current project.

For more information, see the following:

- [Set the quota project programmatically](/docs/quotas/set-quota-project#set-project-programmatically).

- [Set the billing project](/sdk/gcloud/reference#--billing-project)
through the gcloud CLI.

### Update gcloud CLI components

If you receive an error that the quotas command contains an `Invalid choice`,
you might have an older version of the gcloud CLI installed.
Update the gcloud CLI components with the following command:


```
gcloud components update
```


For more details about `gcloud beta quotas` commands and flags, see the
[gcloud beta quotas](/sdk/gcloud/reference/beta/quotas) 
section of the Google Cloud CLI reference.

## What's next

- [Known issues](/docs/quotas/known-issues)

- [Billing questions](/docs/quotas/billing-questions)

- [View and manage quotas](/docs/quotas/view-manage)