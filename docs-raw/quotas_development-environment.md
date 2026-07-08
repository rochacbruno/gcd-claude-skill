# Set up the Cloud Quotas API

Source: https://berlin.devsitetest.how/docs/quotas/development-environment
Last updated: 2026-07-07

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












# Set up the Cloud Quotas API 






- On this page 
- [ Enable the API ](#enable-cloud-quotas-api)
- [ What's next ](#whats_next)
- 










To use the Cloud Quotas API, you must first enable it for your
Google Cloud Dedicated project. This document describes how to enable the Cloud Quotas API.

## Enable the API 

You can enable the Cloud Quotas API by using the Google Cloud Dedicated console or the
[Google Cloud CLI](/sdk/gcloud).


[Console](#console) [gcloud](#gcloud) 
More 




- 

Go to the Google Cloud Dedicated console **API Library** page.

[Go to API Library](https://console.cloud.berlin-build0.goog/project/_/apis/library/cloudquotas.googleapis.com)

- 

Select the Google Cloud Dedicated project that you want to access the API.

- 

On the API Library page, enable **Cloud Quotas API**.

- 

Make sure that your user account has the required [IAM
roles](/docs/quotas/permissions).



## Before you begin

Authenticate to the gcloud CLI before you use it to enable
APIs. For more information about the authentication process, see
[Authenticate for the gcloud CLI](/sdk/docs/authenticate).

## Enable the API

- 

Run the [`gcloud services enable`](/sdk/gcloud/reference/services/enable)
command and specify the Cloud Quotas API:


```
gcloud services enable cloudquotas.googleapis.com --project= PROJECT_ID 
```


Replace ` PROJECT_ID ` with the ID of the project
that needs access to the Cloud Quotas API. You can find your project ID on the
[Welcome](https://console.cloud.berlin-build0.goog/welcome) page of the Google Cloud Dedicated console.

- 

To confirm that the Cloud Quotas API is enabled in your project, run the
[`gcloud services list`](/sdk/gcloud/reference/services/list) command
and filter for `cloudquotas.googleapis.com` by passing the output to a
command such as `grep` or using a gcloud CLI
[`filter`](/sdk/gcloud/reference/topic/filters):


```
gcloud services list --filter="cloudquotas.googleapis.com"
```





## What's next 

- 

About the [Cloud Quotas API](/docs/quotas/api-overview) 

- 

Cloud Quotas API [reference](/docs/quotas/reference/rest)