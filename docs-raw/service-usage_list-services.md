# List services

Source: https://berlin.devsitetest.how/service-usage/docs/list-services
Last updated: 2026-08-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/service-usage/docs/tpc-differences) for more details.














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

Access and resource management

](https://berlin.devsitetest.how/docs/access-resources)






- 








[

Service Usage

](https://berlin.devsitetest.how/service-usage/docs)






- 








[

Guides

](https://berlin.devsitetest.how/service-usage/docs/overview)

















- On this page 
- [ Before you begin ](#before)
- [ List enabled services in an organization or folder ](#org-list-enabled)
- [ List enabled services in a project ](#enabled)
- [ List available services in a project ](#available)
- [ What's next ](#next)
- 









# List services 



This document describes how to list the APIs and services that are enabled or
available in a Google Cloud Dedicated project, folder, or organization.

To program against the Service Usage API, you can also use one of the
[Service Usage client libraries](/service-usage/docs/libraries).

## Before you begin 

To list the enabled and available APIs and services, you need:

- A Google Cloud Dedicated project. To learn how to create a Google Cloud Dedicated project, see
[Create projects](/resource-manager/docs/creating-managing-projects).

- The correct [Identity and Access Management (IAM)](/iam) permissions. To learn
about the IAM requirements for Service Usage, see
[Access control with IAM](/service-usage/docs/access-control).

- If you plan to use the Google Cloud CLI or REST API instructions on this page,
you also need to [install the Google Cloud CLI](/sdk/docs/install).

## List enabled services in an organization or folder



To list the enabled services in an organization or folder, complete the
following steps:


[ gcloud ](#gcloud) [REST API](#rest-api) 
More 




To list the enabled APIs and services for an organization or folder, use the
[`gcloud beta services list`](/sdk/gcloud/reference/beta/services/list)
command:


```
gcloud beta services list RESOURCE_TYPE = RESOURCE_ID 
```


Replace the following:

- 

` RESOURCE_TYPE `: use `--organization` or `--folder`
to list the enabled services for an organization or folder, respectively.

- 

` RESOURCE_ID `: enter the ID of the organization or
folder that you want to list enabled services for.




To list enabled services for an organization or folder, call the
[`consumerPolicies.get`](/service-usage/docs/reference/rest/v2beta/consumerPolicies/get)
method:


```
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://serviceusage.googleapis.com/v2beta/ RESOURCE_TYPE / RESOURCE_ID /consumerPolicies/default?filter=state:ENABLED"
```


Replace the following:

- 

` RESOURCE_TYPE `: use `organizations` or `folders`
to list the enabled services for an organization or folder, respectively.

- 

` RESOURCE_ID `: enter the ID of the organization or
folder that you want to list enabled services for.

If successful, the response body contains a
[`ConsumerPolicy`](/service-usage/docs/reference/rest/v2beta/consumerPolicies#ConsumerPolicy),
which contains a list of enabled APIs:


```
{
"name": "organizations/organization-name/consumerPolicies/default",
...
"enableRules": [
{
"services": [
"services/apphub.googleapis.com",
"services/appoptimize.googleapis.com",
"services/artifactregistry.googleapis.com",
...
]
}
]
}
```



## List enabled services in a project

To list the enabled services in a project, complete the following steps:


[Console](#console) [ gcloud ](#gcloud) [REST API](#rest-api) 
More 




To list the enabled APIs and services in a project:

- 

In the Google Cloud Dedicated console, go to the **APIs & Services** page.

[Go to APIs & Services](https://console.cloud.berlin-build0.goog/project/_/apis/dashboard)

- 

Select the Google Cloud Dedicated project by doing one of the following:

- 

Select a recent project from the available list.

- 

Click **Select project**, find your project, and click the name
of the project.

The **APIs & Services** page opens, listing the APIs enabled in your
Google Cloud Dedicated project.




To list the enabled APIs and services in your current project, use the
[`gcloud services list`](/sdk/gcloud/reference/services/list) command:


```
gcloud services list
```


The output is similar to the following:


```
NAME: analyticshub.googleapis.com
TITLE: Analytics Hub API

NAME: appoptimize.googleapis.com
TITLE: App Optimize API

NAME: artifactregistry.googleapis.com
TITLE: Artifact Registry API

NAME: bigquery.googleapis.com
TITLE: BigQuery API
...
```



To list enabled services for your project, call the
[`services.list`](/service-usage/docs/reference/rest/v1/services/list)
method with the `state:ENABLED` filter:


```
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://serviceusage.googleapis.com/v1/projects/ PROJECT_ID /services?filter=state:ENABLED"
```


Replace ` PROJECT_ID ` with your Google Cloud Dedicated project ID or
number.



## List available services in a project

To list the available services in a project, complete the following steps. The
set of available services rarely changes and can be cached for extended periods
of time.


[Console](#console) [ gcloud ](#gcloud) [REST API](#rest-api) 
More 




To list the APIs and services available to you in a project:

- 

In the Google Cloud Dedicated console, go to the **API Library** page.

[Go to API Library](https://console.cloud.berlin-build0.goog/project/_/apis/library)

- 

Select the Google Cloud Dedicated project by doing one of the following:

- 

Select a recent project from the available list.

- 

Click **Select project**, find your project, and click the name
of the project.

The **API Library** page opens. You can search for or browse through
available APIs.




To list the APIs and services available to you in
your current project, use the
[`gcloud services list`](/sdk/gcloud/reference/services/list) command with
the `--available` flag:


```
gcloud services list --available
```


The results include any services that have already been enabled, as
well as services that are available to be enabled for the current project.
The output is similar to the following:


```
NAME: places-backend.googleapis.com
TITLE: Google Places API Web Service

NAME: clouderrorreporting.googleapis.com
TITLE: Stackdriver Error Reporting API

NAME: analyticsreporting.googleapis.com
TITLE: Google Analytics Reporting API

NAME: youtube.googleapis.com
TITLE: YouTube Data API v3
...
```



To list available services for your project, call the
[`services.list`](/service-usage/docs/reference/rest/v1/services/list)
method:


```
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://serviceusage.googleapis.com/v1/projects/ PROJECT_ID /services"
```


Replace ` PROJECT_ID ` with your Google Cloud Dedicated project ID or
number.

The result includes all public services, all services for which the calling
user has the `servicemanagement.services.bind` permission, and all services
that have already been enabled on the project.

You can filter the results to exclude the services that are enabled on the
project by including the query parameter `?filter=state:DISABLED` as part
of the request.



## What's next

- 

[Enable and disable services](/service-usage/docs/enable-disable) in your
Google Cloud Dedicated project.

- 

[Review quotas and system limits](/service-usage/docs/quotas).