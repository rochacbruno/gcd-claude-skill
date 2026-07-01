# Use client libraries in Google Cloud Dedicated

Source: https://berlin.devsitetest.how/docs/get-started-tpc/use-client-libraries
Last updated: 2026-06-29

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












# Use client libraries in Google Cloud Dedicated 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Differences from Google Cloud ](#differences)
- [ Install client libraries ](#install_client_libraries)
- [ Authenticate and use client Libraries ](#authenticate_and_use_client_libraries)
- [ What's next ](#whats_next)
- 









Google Cloud Dedicated provides a range of client
libraries in many languages, such as Go, Java, and C++, that you can use to
interact with services programmatically. These libraries include our recommended
Cloud Client Libraries, as well as our older Google API Client Libraries. To learn
more about client libraries and accessing services in
Google Cloud Dedicated, see
[Client libraries explained](/apis/docs/client-libraries-explained).

This document explains the specific steps you need to do to use these libraries
in Google Cloud Dedicated, as well as key differences
from using them with Google Cloud.

## Before you begin 

You must specify your universe when using client libraries in
Google Cloud Dedicated. Set the
`GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable to
`apis-berlin-build0.goog` before using
client libraries, including running any of our code samples that use them:


```
export GOOGLE_CLOUD_UNIVERSE_DOMAIN = apis-berlin-build0.goog
```


You can also specify a target universe in your own code. The syntax for this
varies per language.

## Differences from Google Cloud

The following key differences exist between using client libraries in
Google Cloud Dedicated and
Google Cloud:

- 

Default API service names are the same as in Google Cloud,
such as `bigquery.googleapis.com`. These service names are
visible when you enable or disable APIs, for example. However, the service
endpoint FQDN is different, based on
Google Cloud Dedicated's hostname. For example,
`bigquery.googleapis.com` becomes 
`bigquery.apis-berlin-build0.goog`.

- 

You must specify a universe when using client libraries in
Google Cloud Dedicated, as described in the
previous [Before you begin](#before_you_begin) section.

- 

When specifying project IDs,
Google Cloud Dedicated projects all have the
universe prefix
`eu0:`: for
example,
`eu0:example-project`.

- 

Because not all Google Cloud features and services are
available in Google Cloud Dedicated, some client
libraries or REST calls might not work in
Google Cloud Dedicated. If your code makes a
request to an unavailable product or service, the request will fail.

## Install client libraries

Cloud Client Libraries are available for Go, Java, Node.js, Python, Ruby, PHP, C#,
and C++. Each library has a GitHub repository with instructions to install or
implement the libraries, and samples to help you get started. To install and
get started with your preferred library, see
[Cloud Client Libraries by language](/apis/docs/cloud-client-libraries#working_with).

## Authenticate and use client Libraries

To get started using client libraries in a local development or production
environment, learn how to
[authenticate using Application Default Credentials and create a client connection](/docs/authentication/client-libraries).

## What's next

- [Client libraries explained](/apis/docs/client-libraries-explained)

- [Cloud Client Libraries by language](/apis/docs/cloud-client-libraries#by_language)