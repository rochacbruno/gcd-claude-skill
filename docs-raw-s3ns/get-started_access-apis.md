# Set up API access

Source: https://documentation.s3ns.fr/docs/get-started/access-apis
Last updated: 2026-08-25

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












# Set up API access 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Cloud de Confiance APIs: Access services programmatically ](#apis)
- [ Cloud Client Libraries: Access APIs with your preferred language ](#libraries)
- [ What's next? ](#whats_next)
- 









Cloud de Confiance APIs help you programmatically access Cloud de Confiance
services from the command line, through automated scripts, or in your own
applications.

For example, you might want to develop an application that helps administrators
analyze how their resources are utilized
across multiple cloud providers. To do this, you need to access log data from
your Cloud de Confiance resources.

To set up API access, implement the following:

- [Cloud de Confiance APIs: Access services programmatically](#apis)

- [Cloud Client Libraries: Access APIs with your preferred language](#libraries)

## Before you begin 

To make sure you can set up APIs and use tools, ask your administrators to
complete the following tasks:

- Create an account that you use to sign in and use Cloud de Confiance
products, including Cloud de Confiance console and Google Cloud CLI.

- Create a project that serves as an access boundary for your
Cloud de Confiance resources.

- Enable billing on your project so you can pay for service and API usage.

For detailed instructions to complete setup steps, see [Cloud de Confiance by S3NS Setup guided flow](/docs/enterprise/cloud-setup).

## Cloud de Confiance APIs: Access services programmatically

Cloud de Confiance APIs are programmatic interfaces to Cloud de Confiance
services. You can use APIs to access computing, networking, storage, and other
services. For example, you might create a
resource utilization application that pulls log data from your
Cloud de Confiance resources. To retrieve the required data, you use the
Cloud Logging API.

You can access Cloud de Confiance APIs using REST calls or client libraries. We
recommend that you use client libraries, which are available for many popular
programming languages. You can also access Cloud APIs with the Google Cloud CLI
tools or Cloud de Confiance console.

For steps to enable an API, see [Getting started](/apis/docs/getting-started)
in the Cloud APIs documentation.

## Cloud Client Libraries: Access APIs with your preferred language

Cloud Client Libraries help you access Cloud de Confiance APIs from a supported
language of your choice. Each library supports your preferred language
conventions and simplifies the code that you write in your application. The
client libraries can handle common API processes, including authentication,
error handling, retry, and payload validation. For example, if your preferred
development language is Java, you might use the Cloud Logging with Java
library.

To choose and install a library, see
[Cloud Client Libraries](/apis/docs/cloud-client-libraries).

## What's next?

- 

[Understand authentication in Cloud de Confiance by S3NS](/docs/get-started/authentication)

- 

[Cloud de Confiance samples](/docs/samples)