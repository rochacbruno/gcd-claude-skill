# Set up Application Default Credentials

Source: https://berlin.devsitetest.how/docs/authentication/provide-credentials-adc
Last updated: 2026-07-10

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












# Set up Application Default Credentials 






- On this page 
- [ Provide credentials to ADC ](#how-to)
- [ The gcloud CLI and ADC ](#gcloud-credentials)
- [ What's next ](#whats_next)
- 









How you set up Application Default Credentials (ADC) for use by Cloud Client Libraries,
Google API Client Libraries, and the REST and RPC APIs depends on the environment
where your code is running.

For information about where ADC looks for credentials and in what order, see
[How Application Default Credentials works](/docs/authentication/application-default-credentials).

If you are using API keys, then you don't need to set up ADC. For more
information, see [Use API keys to access APIs](/docs/authentication/api-keys-use).

## Provide credentials to ADC 

Select the environment where your code is running:

- 

[Local development environment](/docs/authentication/set-up-adc-local-dev-environment)

- 

[Resource with an attached service account](/docs/authentication/set-up-adc-attached-service-account)

- 

[Containerized environment](/docs/authentication/set-up-adc-containerized-environment)

- 

[On-premises or another cloud provider](/docs/authentication/set-up-adc-on-premises)

- 

[Cloud-based development environment](/docs/authentication/set-up-adc-cloud-dev-environment)

## The gcloud CLI and ADC

You can provide credentials to ADC by using the
[`gcloud auth application-default login`](/sdk/gcloud/reference/auth/application-default/login) command. This makes
credentials available to the Cloud Client Libraries and Google API Client Libraries.

The gcloud CLI itself doesn't use ADC to access Google Cloud Dedicated in Germany
resources. To learn how to provide credentials to the gcloud CLI, see
[Authentication for the gcloud CLI](/sdk/docs/authenticate).

## What's next

- Learn more about [how ADC finds credentials](/docs/authentication/application-default-credentials).

- [Authenticate for using Cloud Client Libraries](/docs/authentication/client-libraries).

- [Authenticate for using REST](/docs/authentication/rest).

- Explore [authentication methods](/docs/authentication).