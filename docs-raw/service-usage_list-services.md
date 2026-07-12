# List services

Source: https://berlin.devsitetest.how/service-usage/docs/list-services
Last updated: 2026-07-10

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
- [ List enabled services in a project ](#enabled)
- [ List available services in a project ](#available)
- [ Next steps ](#next)
- 









# List services 



This document describes how to list the APIs and services that are enabled or
available in a Google Cloud Dedicated project.

- To list services in a project, we recommend that you use the
Google Cloud Dedicated console or the Google Cloud CLI. This document describes how
to use both interfaces.

- To program against the Service Usage API, use one of our provided
[client libraries](/service-usage/docs/libraries).

- To experiment with the API, we recommend that you use the `curl` command.
You don't need to set up a full application environment; however, there is
some required setup.

## Before you begin 

To list the enabled and available APIs and services you need:

- A Google Cloud Dedicated project. To learn how to create a Google Cloud Dedicated project, see
[Creating and Managing Projects](/resource-manager/docs/creating-managing-projects).

- The correct [Identity and Access Management](/iam) permissions. To learn
about the IAM requirements for Service Usage,
see [Access Control](/service-usage/docs/access-control).

- To install the [Google Cloud CLI](/sdk/docs/install).

- If you want to use the `curl` examples in this guide, make sure you follow the
instructions to complete the initial setup in
[Getting Started](/service-usage/docs/set-up-development-environment). These steps include
defining `gcurl`, which is an authenticated alias for the standard `curl`
command, and defining the environment variable `PROJECT_NUMBER`.

## List enabled services in a project

Listing enabled services uses quota from the
`serviceusage.googleapis.com/list_enabled_requests` quota metric. The default
available quota is 10 queries per second (QPS).


[console](#console) [gcloud](#gcloud) [curl](#curl) 
More 




To list the enabled APIs and services in a project:

- Go to the Google Cloud Dedicated console
[API Dashboard](https://console.cloud.berlin-build0.goog/project/_/apis/dashboard) 
page.

[go to the API Dashboard page](https://console.cloud.berlin-build0.goog/project/_/apis/dashboard) 

- 

Select your Google Cloud Dedicated project by performing one of the following:

- 

Click on a Google Cloud Dedicated project under **Select a recent project**.

- 

Use the Google Cloud Dedicated project browser by performing the following
steps:

- Click **Select project** to open the Google Cloud Dedicated project browser.

- Find your project and then click on the Google Cloud Dedicated project name.

- Click **Open** to open the project.

The **APIs & Services** page appears. You can find the list of APIs
enabled in your Google Cloud Dedicated project in the table on this page.




To list the enabled APIs and services in your current project, run the
following command:


```
gcloud services list
```


The command produces output similar to the following:


```
NAME TITLE
pubsub.googleapis.com Google Cloud Pub/Sub API
bigquery.googleapis.com BigQuery API
cloudtrace.googleapis.com Stackdriver Trace API
servicemanagement.googleapis.com Google Service Management API
monitoring.googleapis.com Stackdriver Monitoring API
storage-api.googleapis.com Google Cloud Storage JSON API
logging.googleapis.com Stackdriver Logging API
clouddebugger.googleapis.com Stackdriver Debugger API
...
```



To list enabled services, call the
[`services.list`](/service-usage/docs/reference/rest/v1/services/list)
method with the `state:ENABLED` filter.

To list the enabled APIs and services in your project, run the following
command:


```
gcurl "https://serviceusage.googleapis.com/v1/projects/${PROJECT_NUMBER}/services?filter=state:ENABLED" 
```



## List available services in a project

Listing all available services uses quota from the
`serviceusage.googleapis.com/list_available_requests` quota. The default
available quota is 1 QPS. The set of available services rarely changes and
can be cached for extended periods of time.


[console](#console) [gcloud](#gcloud) [curl](#curl) 
More 




To list the APIs and services available to you in a project:

- Go to the Google Cloud Dedicated console
[API Library](https://console.cloud.berlin-build0.goog/project/_/apis/library) 
page.

[Go to the API Library page](https://console.cloud.berlin-build0.goog/project/_/apis/library) 

- 

Select your Google Cloud Dedicated project by performing one of the following:

- 

Click on a Google Cloud Dedicated project under **Select a recent project**.

- 

Use the Google Cloud Dedicated project browser by performing the following
steps:

- Click **Select project** to open the Google Cloud Dedicated project browser.

- Find your project and then click on the Google Cloud Dedicated project name.

- Click **Open** to open the project.

The **API Library** screen appears. You can search for or scroll through
available APIs from this screen.




To list the APIs and services available to you in
your current project, run the following command:


```
gcloud services list --available
```


The results include any services that have already been enabled, as
well as services that are available to be enabled for the current project.
The command produces output similar to the following:


```
NAME TITLE
places-backend.googleapis.com Google Places API Web Service
clouderrorreporting.googleapis.com Stackdriver Error Reporting API
analyticsreporting.googleapis.com Google Analytics Reporting API
youtube.googleapis.com YouTube Data API v3
adsense.googleapis.com AdSense Management API
sqladmin.googleapis.com Google Cloud SQL API
genomics.googleapis.com Genomics API
adexchangebuyer.googleapis.com Ad Exchange Buyer API II
...
```



To list available services, call the
[`services.list`](/service-usage/docs/reference/rest/v1/services/list)
method.

To list the available APIs and services in your project, run the following command:


```
gcurl "https://serviceusage.googleapis.com/v1/projects/${PROJECT_NUMBER}/services" 
```


The result includes all public services, all services for which the calling
user has the `servicemanagement.services.bind` permission, and all services
that have already been enabled on the project.

It is possible to exclude the services that are currently active on the
project by passing `filter=state:DISABLED` to the previous call.



## Next steps

For information about how to enable or disable services in your
Google Cloud Dedicated project, see
[Enabling and Disabling Services](/service-usage/docs/enable-disable).