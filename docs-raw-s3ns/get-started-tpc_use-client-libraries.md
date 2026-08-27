# Use client libraries in Cloud de Confiance

Source: https://documentation.s3ns.fr/docs/get-started-tpc/use-client-libraries
Last updated: 2026-08-26

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

Get started

](https://documentation.s3ns.fr/docs/get-started)












# Use client libraries in Cloud de Confiance 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Differences from Google Cloud ](#differences)
- [ Install client libraries ](#install_client_libraries)
- [ Authenticate and use client Libraries ](#authenticate_and_use_client_libraries)
- [ What's next ](#whats_next)
- 









Cloud de Confiance provides a range of client
libraries in many languages, such as Go, Java, and C++, that you can use to
interact with services programmatically. These libraries include our recommended
Cloud Client Libraries, as well as our older Google API Client Libraries. To learn
more about client libraries and accessing services in
Cloud de Confiance, see
[Client libraries explained](/apis/docs/client-libraries-explained).

This document explains the specific steps you need to do to use these libraries
in Cloud de Confiance, as well as key differences
from using them with Google Cloud.

## Before you begin 

You must specify your universe when using client libraries in
Cloud de Confiance. Set the
`GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable to
`s3nsapis.fr` before using
client libraries, including running any of our code samples that use them:


```
export GOOGLE_CLOUD_UNIVERSE_DOMAIN = s3nsapis.fr
```


You can also specify a target universe in your own code. The syntax for this
varies per language.

## Differences from Google Cloud

The following key differences exist between using client libraries in
Cloud de Confiance and
Google Cloud:

- 

Default API service names are the same as in Google Cloud,
such as `bigquery.googleapis.com`. These service names are
visible when you enable or disable APIs, for example. However, the service
endpoint FQDN is different, based on
Cloud de Confiance's hostname. For example,
`bigquery.googleapis.com` becomes 
`bigquery.s3nsapis.fr`.

- 

You must specify a universe when using client libraries in
Cloud de Confiance, as described in the
previous [Before you begin](#before_you_begin) section.

- 

When specifying project IDs,
Cloud de Confiance projects all have the
universe prefix
`s3ns:`: for
example,
`s3ns:example-project`.

- 

Because not all Google Cloud features and services are
available in Cloud de Confiance, some client
libraries or REST calls might not work in
Cloud de Confiance. If your code makes a
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