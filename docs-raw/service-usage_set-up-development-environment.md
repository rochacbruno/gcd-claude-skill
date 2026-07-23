# Quickstart: Set up Service Usage for a development environment

Source: https://berlin.devsitetest.how/service-usage/docs/set-up-development-environment
Last updated: 2026-07-22

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

















- On this page ** 
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

To use the Service Usage API, you must first enable it in your
Google Cloud Dedicated project.

















- 




In the Google Cloud Dedicated console, on the project selector page,
select or create a Google Cloud Dedicated project.




Roles required to select or create a project**





- 
**Select a project**: Selecting a project doesn't require a specific
IAM role—you can select any project that you've been
granted a role on.


- 
**Create a project**: To create a project, you need the Project Creator role
(`roles/resourcemanager.projectCreator`), which contains the
`resourcemanager.projects.create` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).












[Go to project selector](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)













- 




Enable the Service Usage API.






**Roles required to enable APIs**


To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=serviceusage.googleapis.com)












- Ensure that your user account has been granted the
[Service Usage Admin](/iam/docs/roles-permissions/serviceusage) role.

### Test with curl

- 

Set an environment variable `PROJECT_ID` with the identifier of your
project:


```
PROJECT_ID= PROJECT_ID 
```


Replace PROJECT_ID with your Google Cloud Dedicated project ID or
number.

- 

Ensure that you are logged into 'gcloud':


```
gcloud auth login
```


- 

List the enabled APIs and services in this project:


```
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://serviceusage.googleapis.com/v1/projects/ ${ PROJECT_ID } /services?filter=state:ENABLED&fields=services.config.title,services.config.name"
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

To list the APIs and services that are enabled or available in your
Google Cloud Dedicated projects, see [List services](/service-usage/docs/list-services).