# Troubleshoot quota errors

Source: https://documentation.s3ns.fr/docs/quotas/troubleshoot
Last updated: 2026-11-25

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://documentation.s3ns.fr/docs/quotas)






- 








[

Guides

](https://documentation.s3ns.fr/docs/quotas/overview)












# Troubleshoot quota errors 






- On this page 
- [ Exceeding rate quotas ](#exceeding_rate_quotas)

- [ Causes of HTTP 429 errors while usage is low ](#low-usage-rate-quotas)
- [ Examine quota usage with Cloud Logging ](#examine-quota-usage)
- [ Resolve HTTP 429 errors ](#resolve-rate-limits)

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
values or not setting the quota on a project correctly. If you want to be
alerted when errors happen, you can create custom alerts for specific quota
errors, as described in [Set up quota
alerts](/docs/quotas/set-up-quota-alerts).

## Exceeding rate quotas 

Rate quotas define the maximum number of requests that you can make to an API
within a specific time interval (for example, every second or every minute).
When your application exceeds a rate quota value for a service, that service
returns an HTTP `429 TOO MANY REQUESTS` status code or a gRPC
`RESOURCE_EXHAUSTED` error (status code 8). Some services may return an HTTP
`403` instead of an HTTP `429`.

Rate quota usage resets automatically after each predefined time interval.

### Causes of HTTP 429 errors while usage is low

If your workloads receive HTTP `429` or gRPC `RESOURCE_EXHAUSTED` errors while
the Cloud de Confiance console or Cloud Monitoring charts show low peak usage, consider
the following common architectural causes.

#### Subminute micro-bursting and metric smoothing

A common pattern for rate quotas is using a rate limiter based on a [token
bucket](https://en.wikipedia.org/wiki/Token_bucket) (on Wikipedia) with subminute refill windows rather than full-minute
windows. When requests exhaust the tokens in a bucket, you might see quota
exhaustion errors alongside low reported usage for the following reasons:

- **The micro-burst effect**: If your application sends a high concentration
of requests concurrently (for example, 50 requests in 200 milliseconds
during a batch job startup), it instantly exhausts the token bucket's burst
capacity and triggers an HTTP `429` error.

- **Metric chart smoothing**: Monitoring and
Cloud Quotas charts in the Cloud de Confiance console display usage metrics
averaged over [alignment periods](/monitoring/alerts/concepts-indepth#alignment_period) (for example, 1-minute or 10-minute
periods). For a chart aligned to a 1-minute period, a brief 200-millisecond
spike that exhausts burst capacity is averaged out over 1 minute, making
your aggregate traffic appear as a flat, low percentage of the overall quota
value.

- **Thundering herd problem**: If multiple client workers receive an HTTP
`429` error and immediately retry at fixed intervals without randomized
delays (jitter), their retries synchronize into repeated bursts that
perpetuate throttling. This behavior is known as the [thundering herd
problem](https://en.wikipedia.org/wiki/Thundering_herd_problem) (on Wikipedia).

#### Per-dimension quota exhaustion

Many Cloud de Confiance by S3NS APIs enforce rate quotas based on dimensions, such as `Queries
per minute per user (1/min/{project}/{user})`, or action per IP address (for
example, `Requests/IP address/hour`). For these quotas, the quota value is
enforced separately for each dimension value. For example, per-user quota is
enforced for each user, per-region quota is enforced for each region, and per-IP
address is enforced for each IP address. Per-user quotas don't show usage in
Cloud Quotas. For more details, see [per-user quota usage doesn't
appear](/docs/quotas/known-issues#per-user_quota_usage_doesnt_appear).

- **Per-user quota exhaustion**: For per-user rate quotas, the quota value is
enforced separately for each authenticated principal (such as a user account
or service account), while the Cloud de Confiance console displays the aggregate quota
value for your entire project. If all backend instances of your application
authenticate using the same service account, that single principal can
exhaust its per-user rate quota while overall project utilization remains
low.

- **Client IP fallback**: When requests don't include an authenticated
principal (for example, unauthenticated or API-key-only calls), per-user
quotas fall back to the client IP address. Multiple callers behind a shared
Cloud NAT gateway or corporate proxy share that single IP bucket, which
can exhaust its per-user quota value and trigger HTTP `429` errors.

#### Quota projects

Unlike [resource-based APIs](/docs/quotas/quota-project#project-resource-based), which only ever count quota usage against the
project in which the resource is located, [client-based APIs](/docs/quotas/quota-project#project-client-based) can have their
quota usage applied to a client-specified quota or billing project.

If a client-based API accesses resources in Project A while specifying Project B
as its quota project, rate quota rejections apply to Project B. Checking Project
A in the Cloud de Confiance console shows low usage because usage is charged to Project B.
To check which quota project is active, see [Identify the current quota project
for client-based
APIs](/docs/quotas/quota-project#identify_the_current_quota_project_for_client-based_apis).

### Examine quota usage with Cloud Logging

When receiving unexpected 429 errors, use Cloud Logging to identify the exact
service account, client IP, user agent, and API method sending the rejected
traffic.

#### Before you begin

Except for BigQuery, Data Access audit logs are disabled by default and
can incur Logging charges. To inspect throttled read or
data-plane API calls, you must [enable Data Access audit
logs](/logging/docs/audit/configure-data-access) and have the [Private Logs
Viewer role](/iam/docs/roles-permissions/logging#logging.privateLogViewer)
(`roles/logging.privateLogViewer`). If Data Access audit logs aren't enabled or
a service doesn't log quota rejections, use Metrics Explorer
(`serviceruntime.googleapis.com/api/request_count`) as described in
[Cloud Quotas limitations in the
Cloud de Confiance console](/docs/quotas/known-issues#per-user_quota_usage_doesnt_appear).

#### Query quota usage

- In the Cloud de Confiance console, go to the [**Logs
Explorer**](https://console.cloud.s3nscloud.fr/logs/query) page.

- 

In the query editor, enter the following query to filter for API calls with
the gRPC `RESOURCE_EXHAUSTED` status code:


```
logName:"cloudaudit.googleapis.com"
protoPayload.status.code=8 -- gRPC code 8: RESOURCE_EXHAUSTED (HTTP 429)
```


To narrow the results to a specific service experiencing throttling, specify
the service name:


```
logName:"cloudaudit.googleapis.com"
protoPayload.serviceName=" SERVICE_NAME .googleapis.com"
protoPayload.status.code=8
```


Replace ` SERVICE_NAME ` with the API name (for
example, `compute`, `storage`, or `identitytoolkit`).

- 

Click **Run query**.

- 

Expand a log entry and inspect the following fields:

- `protoPayload.authenticationInfo.principalEmail`: The exact service
account or user email making the calls. For third-party or federated
identities (such as Workload Identity Federation principals), check
`protoPayload.authenticationInfo.principalSubject`. For more information
about when caller identities might be redacted, see [Caller identities
in audit logs](/logging/docs/audit#user-id).

- `protoPayload.methodName`: The specific API method being rejected.

- `protoPayload.requestMetadata.callerIp`: The originating IP address of
the client.

- `protoPayload.requestMetadata.callerSuppliedUserAgent`: The user agent
specified by the client request.

### Resolve HTTP 429 errors

When facing HTTP `429` or gRPC `RESOURCE_EXHAUSTED` errors, consider the
following design approaches in your client applications.

#### Implement exponential backoff with jitter

Ensure all API clients implement an [exponential backoff algorithm](https://en.wikipedia.org/wiki/Exponential_backoff) (on
Wikipedia) with jitter when retrying failed requests. Adding jitter spreads
retries over time and helps prevent retry synchronization. For more information
about implementing automatic retries with exponential backoff, see [Addressing
Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) in the *Site Reliability Engineering* book.

#### Apply client-side rate limiting

If your workloads emit periodic bursts of traffic (such as worker queues or
parallel cron jobs), use an in-memory client-side rate limiter (such as a
token-bucket or leaky-bucket algorithm that meters outgoing calls) in your
client code to control the outgoing request rate.

#### Isolate per-user quota usage

If your application is throttled on a per-user rate quota, consider the
following options:

- 

**Specify the `quotaUser` parameter**: For APIs that support per-user quotas
and the [`quotaUser`](/apis/docs/system-parameters#definitions) query
parameter (or the `X-Goog-Quota-User` header), pass an opaque string under
40 characters that doesn't contain personally identifiable information (PII)
to identify each end user. You must also identify the quota project with a
valid API key that has service restrictions (such as IP address or HTTP
referrer restrictions); otherwise, `quotaUser` is ignored and requests fall
back to the authenticated principal or client IP bucket. For details, see
[Capping your API usage](/apis/docs/capping-api-usage).

- 

**Isolate distinct workloads with separate service accounts**: Rather than
sharing one service account across unrelated applications or environments,
assign a dedicated service account to each distinct workload so one workload
doesn't exhaust another's per-user quota. Note that separate service
accounts still share project-level rate quotas, and you must not create or
rotate multiple service accounts for a single workload to circumvent quotas.

#### Consolidate calls with API batching

Combine individual operations into batch requests to reduce the number of
discrete API requests per minute, where supported by the service (such as
`BatchAnnotateImages` in Cloud Vision, `CreateTimeSeries` in
Cloud Monitoring, or `BatchTranslateText` in Cloud Translation). Check each
service's quota documentation to confirm how batched items are counted—for
example, Cloud Storage JSON API batch requests still count each sub-request
separately toward your rate quota, and Cloud Vision still counts each image
toward per-image feature quotas.

## Exceeding quota values

If your project exceeds its maximum quota value while using a service,
Cloud de Confiance by S3NS returns an error based on how you accessed the service:

- If you exceed a quota value with an API request, Cloud de Confiance by S3NS returns an
HTTP `413 REQUEST ENTITY TOO LARGE` status code. Note that when using the
BigQuery legacy streaming API in a production environment, you may
receive an HTTP `413 REQUEST ENTITY TOO LARGE` status code if your HTTP
requests are larger than 10 MB. You may also receive this error if you
exceed 300 MB per second. For more information see [Streaming
inserts.](/bigquery/quotas#streaming_inserts) 

- If you exceeded a quota value with an HTTP/REST request, Cloud de Confiance by S3NS
returns an HTTP `429 TOO MANY REQUESTS` status code.

- If you exceed a quota for Compute Engine, Cloud de Confiance by S3NS typically returns
an HTTP `403 QUOTA_EXCEEDED` status code, whether it was from API,
HTTP/REST, or gRPC. If the quota is a rate quota, then HTTP `403
RATE_LIMIT_EXCEEDED` is returned.

- If you exceeded a quota value using
[gRPC](https://grpc.io),
Cloud de Confiance by S3NS returns a `ResourceExhausted` error. How this error appears
to you depends on the service.

- If you exceeded a quota value using a Google Cloud CLI command, the
gcloud CLI outputs a quota-exceeded error message and returns
with the exit code `1`.

- If you received a `QUOTA_EXCEEDED` message during a service rollout, see the
following section.

## Exceeding quota values during a service rollout

Cloud de Confiance by S3NS sometimes changes the default quota values for resources and APIs.
These changes take place gradually, which means that during the rollout of a new
default quota, the quota value that appears in the Cloud de Confiance console might not
reflect the new quota value that is available to you.

If a quota rollout is in progress, you may receive an error message that states
`The future limit is the new default quota that will be available after a
service rollout completes.` If you see this error message, the cited quota value
and future value are correct, even if what appears in the Cloud de Confiance console
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

To view charts that show current and peak usage, in the Cloud de Confiance console, go
to the [**IAM & Admin  > 
Quotas & System Limits**](https://console.cloud.s3nscloud.fr/quotas?project=_) page and then
click monitoring **Monitoring**. You might need to go to the end of the
table.

- 

If you need more quota, you can [request a quota
adjustment](/docs/quotas/help/request_increase).

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

These and other errors can often be fixed by setting the quota project. For more
information, see [Quota project overview](/docs/quotas/quota-project).

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
`gcloud config set billing/quota_project CURRENT_PROJECT` to set the quota
project as the current project.

For more information, see the following:

- [Set the quota project
programmatically](/docs/quotas/set-quota-project#set-project-programmatically).

- [Set the billing project](/sdk/gcloud/reference#--billing-project) through
the gcloud CLI.

### Update gcloud CLI components

If you receive an error that the quotas command contains an `Invalid choice`,
you might have an older version of the gcloud CLI installed. Update
the gcloud CLI components with the following command:


```
gcloud components update
```


For more details about `gcloud quotas` commands and flags, see the [`gcloud
quotas`](/sdk/gcloud/reference/quotas) 
section of the Google Cloud CLI reference.

## What's next

- [Known issues](/docs/quotas/known-issues)

- [Billing questions](/docs/quotas/billing-questions)

- [View and manage quotas](/docs/quotas/view-manage)