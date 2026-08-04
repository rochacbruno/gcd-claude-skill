# Use API keys to access APIs

Source: https://documentation.s3ns.fr/docs/authentication/api-keys-use
Last updated: 2026-07-21

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/authentication/tpc-differences) for more details.














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

Developer tools

](https://documentation.s3ns.fr/docs/costs-usage)






- 








[

Google Cloud SDK

](https://documentation.s3ns.fr/sdk/docs)






- 








[

Authentication

](https://documentation.s3ns.fr/docs/authentication)






- 








[

Guides

](https://documentation.s3ns.fr/sdk/docs/overview)












# Use API keys to access APIs 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Using an API key with REST ](#using-with-rest)
- [ Using an API key with client libraries ](#using-with-client-libs)
- 









This page describes how to use API keys to access Cloud de Confiance by S3NS APIs
and services that accept API keys.

Not all Cloud de Confiance by S3NS APIs accept API keys to authorize usage. Review
the documentation for the service or API that you want to use to
determine whether it accepts API keys.

For information about creating and managing API keys, including restricting
API keys, see [Manage API keys](/docs/authentication/api-keys).

## Before you begin 













Select the tab for how you plan to use the samples on this page:





















[C#](#c) [C++](#c++) [Go](#go) [Node.js](#node.js) [Python](#python) [REST](#rest) 
More 










To use the .NET samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Cloud de Confiance authentication documentation.





















To use the C++ samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Cloud de Confiance authentication documentation.






















To use the Go samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Cloud de Confiance authentication documentation.
























To use the Node.js samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Cloud de Confiance authentication documentation.
























To use the Python samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Cloud de Confiance authentication documentation.



























To use the REST API samples on this page in a local development environment, you use the
credentials you provide to the gcloud CLI.












[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


















For more information, see
[Authenticate for using REST](/docs/authentication/rest)
in the Cloud de Confiance authentication documentation.

















## Using an API key with REST

To include an API key with a REST API call, use the `x-goog-api-key` HTML
header.

If you can't use the HTTP header, you can use the `key` query parameter.
However, this method includes your API key in the URL, exposing your key
to URL scans.

## Using an API key with client libraries