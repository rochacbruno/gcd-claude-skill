# How Application Default Credentials works

Source: https://berlin.devsitetest.how/docs/authentication/application-default-credentials
Last updated: 2026-07-21

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

Developer tools

](https://berlin.devsitetest.how/docs/costs-usage)






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












# How Application Default Credentials works 






- On this page 
- [ Search order ](#order)

- [ GOOGLE_APPLICATION_CREDENTIALS environment variable ](#GAC)
- [ A credential file created by using the gcloud auth application-default login command ](#personal)
- [ The attached service account ](#attached-sa)

- [ What's next ](#whats_next)
- 









This page describes the locations where Application Default Credentials (ADC)
looks for credentials. Understanding how ADC works can help you understand which
credentials ADC is using, and how it's finding them.





Application Default Credentials (ADC) is a strategy used by the authentication libraries to automatically find
credentials based on the application environment. The authentication libraries make those
credentials available to
[Cloud Client Libraries and Google API Client Libraries](/apis/docs/client-libraries-explained).
When you use ADC, your code can run in either a development or production environment without
changing how your application authenticates to Google Cloud Dedicated in Germany services and APIs.

For information about how to provide credentials to ADC, including how to
generate a local ADC file, see
[Set up Application Default Credentials](/docs/authentication/provide-credentials-adc).

## Search order

ADC searches for credentials in the following locations:

- [`GOOGLE_APPLICATION_CREDENTIALS` environment variable](#GAC)

- [A credential file created by using the `gcloud auth application-default login` command](#personal)

- [The attached service account, returned by the metadata server](#attached-sa)

The order of the locations ADC checks for credentials is not related to
the relative merit of each location. For help with
understanding the best ways to provide credentials to ADC, see
[Set up Application Default Credentials](/docs/authentication/provide-credentials-adc).

### GOOGLE_ APPLICATION_ CREDENTIALS environment variable

You can use the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to provide
the location of a credential JSON file. This JSON file can be one of the
following types of files:

- 

A credential configuration file for Workforce Identity Federation

Workforce Identity Federation lets you use an external identity provider
(IdP) to authenticate and authorize users to access Google Cloud Dedicated
resources. For more information, see
[Workforce Identity Federation](/iam/docs/workforce-identity-federation) in the
Identity and Access Management (IAM) documentation.

- 

A credential configuration file for Workload Identity Federation

Workload Identity Federation lets you use an external
IdP to authenticate and authorize workloads to access
Google Cloud Dedicated resources. For more information, see
[Authenticating by using client libraries, the gcloud CLI, or Terraform](/iam/docs/using-workload-identity-federation#generate-automatic)
in the Identity and Access Management (IAM) documentation.

- 

A service account key

Service account keys create a security risk and are not recommended. Unlike
the other credential file types, compromised service account keys can be
used by a bad actor without any additional information. For more
information, see
[Best practices for using and managing service account keys](/iam/docs/best-practices-for-managing-service-account-keys).

### A credential file created by using the `gcloud auth application-default login` command

You can [provide credentials to ADC](/docs/authentication/set-up-adc-local-dev-environment) by running the
[`gcloud auth application-default login`](/sdk/gcloud/reference/auth/application-default/login) command. This
command creates a JSON file containing the credentials you provide (either from
your user account or from impersonating a service account) and places it in a
well-known location on your file system. The location depends on your
operating system:

- Linux, macOS: `$HOME/.config/gcloud/application_default_credentials.json`

- Windows: `%APPDATA%\gcloud\application_default_credentials.json`

The credentials you provide to ADC by using the gcloud CLI are
distinct from your gcloud credentials—the credentials the
gcloud CLI uses to authenticate to Google Cloud Dedicated. For more
information about these two sets of credentials, see
[gcloud CLI authentication configuration and ADC configuration ](/docs/authentication/provide-credentials-adc#gcloud-credentials).

### The attached service account

Many Google Cloud Dedicated services let you attach a service account that can be
used to provide credentials for accessing Google Cloud Dedicated APIs. If ADC does
not find credentials it can use in either the `GOOGLE_APPLICATION_CREDENTIALS`
environment variable or the well-known location for local ADC credentials,
it uses the [metadata server](/compute/docs/metadata/overview) to get credentials for the
service where the code is running.

Using the credentials from the attached service account is the preferred method
for finding credentials in a production environment on Google Cloud Dedicated. To
use the attached service account, follow these steps:

- Create a user-managed service account.

- Grant that service account the [least privileged](/iam/docs/using-iam-securely#least_privilege)
IAM roles possible.

- Attach the service account to the resource where your code is running.

For help with creating a service account, see
[Creating and managing service accounts](/iam/docs/service-accounts-create). For help with attaching
a service account, see [Attaching a service account to a resource](/iam/docs/attach-service-accounts#attaching-to-resources).
For help with determining the required IAM roles for your service
account, see [Choose predefined roles](/iam/docs/choose-predefined-roles).

## What's next

- Learn the best ways to [provide credentials to ADC](/docs/authentication/provide-credentials-adc).

- [Authenticate using the Cloud Client Libraries](/docs/authentication/client-libraries).

- Explore [authentication methods](/docs/authentication).

- Learn about [client libraries](/apis/docs/client-libraries-explained).