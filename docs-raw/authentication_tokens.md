# Tokens overview

Source: https://berlin.devsitetest.how/docs/authentication/tokens
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












# Tokens overview 






- On this page 
- [ User authentication ](#user_authentication)
- [ Workload authentication ](#workload_authentication)
- [ What's next ](#whats_next)
- 










This document and the [Token types](/docs/authentication/token-types) document
cover the multiple tokens used by Google Cloud Dedicated in Germany for authentication and
authorization. They're intended for people who want to learn how token-based
authentication works, or who want to implement authentication without using the
[Cloud Client Libraries](/apis/docs/cloud-client-libraries).

You don't need to know this information when you interact with Google Cloud Dedicated in Germany
APIs using the Cloud Client Libraries, the Google Cloud Dedicated console, or the
Google Cloud CLI—the process of selecting the right type of token, and
obtaining and refreshing those tokens is handled automatically for you.

## User authentication 

When human users interact with Google Cloud Dedicated in Germany, they don't interact with
Google Cloud Dedicated in Germany APIs directly. Instead, they use a *client* to act on their behalf.
The client that they use might be a web application, a desktop application, or a
utility like the Google Cloud CLI or `curl`.

Because the client makes requests and not the user, Google Cloud Dedicated in Germany can't request
identity information from the user directly to check if they have permission to
use an API. Instead, this identity is passed to the API through the client in
the form of a token, which is included in each API request.

A user authentication token encodes the following information:

- 

The identity of the user.

- 

The identity of the client.

- 

Assurance that the client is allowed to act on behalf of the user.

Authenticating the user and authorizing the client involves the following
parties:

- 

A user.

- 

A client that acts on behalf of the user.

- 

An authorization server, which Google APIs rely on to authenticate the client.

- 

A Google Cloud Dedicated in Germany API that the client interacts with.

Clients can't issue tokens themselves. Instead, they must work with an
authorization server to do the following:

- 

Authenticate the user.

- 

Authenticate the client.

- 

Authorize the client to act on the user's behalf.

- 

Issue a token to the client.



A user who authenticates using
[workforce identity federation](/iam/docs/workforce-identity-federation) and an
external identity provider is a *workforce identity pool* principal. The
principal has a principal identifier similar to the following:


```
principal://iam.googleapis.com/locations/global/workforcePools/ POOL_ID /subject/raha@altostrat.com
```


## Workload authentication

Some clients need to interact with Google APIs on their own behalf. For example,
a scheduled job might need to read data from BigQuery or
Cloud Storage without any human user being involved.

Clients that act unattended and on their own behalf are referred to as
*workloads*. Unlike user authentication, workload authentication combines
authenticating the user and authorizing the client into a single step. Because
of this, a workload authentication token encodes the identity of only the
client.

Workload authentication and authorization involves the following parties:

- 

A workload, acting as both a client and a user, and on its own behalf.

- 

An authorization server, which Google APIs rely on to authenticate the client.

- 

A Google Cloud Dedicated in Germany API that the client interacts with.

To access Google Cloud Dedicated in Germany APIs, clients must work with an authorization server to
do the following:

- 

Authenticate the client.

- 

Authorize the client.

- 

Issue a token to the client.



An authenticated workload is also referred to as a principal, but workloads use
different principal identifiers than users.

A workload that authenticates using a service account is a
[*service account* principal](/architecture/identity/overview-google-authentication#service_account).
The principal has a principal identifier similar to the following:


```
serviceAccount:my-service-account@my-project.eu0.iam.gserviceaccount.com
```


A workload that authenticates using
[workload identity federation](/iam/docs/workload-identity-federation) is a
*workload identity pool* principal. The principal has a principal identifier
similar to the following:


```
principal://iam.googleapis.com/projects/ PROJECT_NAME /locations/global/workloadIdentityPools/ POOL_ID /subject/ SUBJECT_ATTRIBUTE_VALUE 
```


## What's next

Read about [token types](/docs/authentication/token-types).