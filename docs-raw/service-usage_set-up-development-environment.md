# Quickstart: Set up Service Usage for a development environment

Source: https://berlin.devsitetest.how/service-usage/docs/set-up-development-environment
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
- [ Set up to call the API directly ](#api)

- [ Enable the Service Usage API ](#enable)
- [ Test with curl ](#test)

- [ Next steps ](#next)
- 









# Set up Service Usage for a development environment 



This page describes how to set up your development environment to use the
Service Usage API.

- For most operational use cases, the simplest way to
enable and disable services is to use Google Cloud Dedicated console.

- If you need to create
scripts, you can use the Google Cloud CLI.

- If you need to
program against the Service Usage API, use one of
the [client libraries](/service-usage/docs/libraries).

- To experiment with the API, you can follow the alternative setup instructions in this guide
and use the `curl` command to test the API without setting up a full application
development environment.

## Set up to call the API directly

This section describes the basic steps necessary to set up your local
environment to experiment with the Service Usage API using the
`curl` command. It is aimed at developers who need to program against the
Service Usage API.

### Enable the Service Usage API

To use the Service Usage API, you must first enable it in the
Google Cloud Dedicated project you want to use it for:

- Go to the Google Cloud Dedicated console **API Library** page.

[Go to the API Library page](https://console.cloud.berlin-build0.goog/project/_/apis/library/serviceusage.googleapis.com) 

- Select the Google Cloud Dedicated project that you want to use to
access the service.

- On the API Library page, click **Enable**.

- Ensure that your user account has the [Service Usage Admin](https://berlin.devsitetest.how/iam/docs/roles-permissions/serviceusage) role.

### Test with curl

- 

Define a convenient shell alias for calling Google REST APIs:


```
alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
```


- 

Set an environment variable `PROJECT_ID` with the identifier of your
project. This can be the project id or number:


```
PROJECT_ID="my-project-id"
```


- 

Ensure that you are logged into 'gcloud':


```
gcloud auth login
```


- 

List the enabled APIs and services in this project:


```
gcurl "https://serviceusage.googleapis.com/v1/projects/ ${ PROJECT_ID } /services?filter=state:ENABLED&fields=services.config.title,services.config.name"
```


If you see output like this, then your setup is successful:


```
{
"services": [
{
"config": {
"name": "bigquery.googleapis.com",
"title": "BigQuery API"
}
},
{
"config": {
"name": "bigquerystorage.googleapis.com",
"title": "BigQuery Storage API"
}
},
...
```


## Next steps

Follow [Listing Services](/service-usage/docs/list-services) to list the APIs
and services that are enabled or available in your Google Cloud Dedicated projects.