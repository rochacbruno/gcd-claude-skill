# Quickstart: Write and query log entries with the gcloud CLI

Source: https://berlin.devsitetest.how/logging/docs/write-query-log-entries-gcloud
Last updated: 2026-06-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/logging/docs/tpc-differences) for more details.














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

Observability

](https://berlin.devsitetest.how/docs/observability)






- 








[

Cloud Logging

](https://berlin.devsitetest.how/logging/docs)






- 








[

Guides

](https://berlin.devsitetest.how/logging/docs/overview)

















- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Required roles ](#required-roles)

- [ Write log entries by using the gcloud CLI ](#write-log-entries-using-sdk)
- [ List log entries by using the gcloud CLI ](#list-log-entries-using-sdk)
- [ View log entries in the Logs Explorer ](#explore)
- [ Query log entries in the Logs Explorer ](#filter-log-entries)
- [ Troubleshooting ](#troubleshooting)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Write and query log entries with the gcloud CLI 




This document introduces you to some of the capabilities of Cloud Logging
and shows you how to do the following:

- Write log entries by using the Google Cloud CLI.

- List log entries by using the gcloud CLI.

- List log entries by using the Logging API.

- View and query log entries by using the Logs Explorer.





## Before you begin 


You must have a Google Cloud Dedicated project with billing enabled to complete this
quickstart.
If you don't have a Google Cloud Dedicated project, or if you don't have
billing enabled for your Google Cloud Dedicated project, then do the following:

















- 


[Install](/sdk/docs/install) the Google Cloud CLI.














- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).







- 


To [initialize](/sdk/docs/initializing) the gcloud CLI, run the following command:



```
gcloud init
```





















- 




[Create or select a Google Cloud Dedicated project](https://berlin.devsitetest.how/resource-manager/docs/creating-managing-projects).




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













- 


Create a Google Cloud Dedicated project:


```
gcloud projects create ** PROJECT_ID 
```



Replace ` PROJECT_ID ` with a name for the Google Cloud Dedicated project you are creating.



- 


Select the Google Cloud Dedicated project that you created:


```
gcloud config set project PROJECT_ID 
```



Replace ` PROJECT_ID ` with your Google Cloud Dedicated project name.













- 


If you're using an existing project for this guide,
[verify that you have the
permissions required to complete this guide](#required-roles). If you created a new project,
then you already have the required permissions.










- 



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).













### Required roles


































To get the permissions that
you need to create, list, and delete log entries,

ask your administrator to grant you the
[Logging Admin ](/iam/docs/roles-permissions/logging#logging.admin) (`roles/logging.admin`) IAM role on your project.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









The Logs Writer (`roles/logging.logWriter`) and Logs Viewer
(`roles/logging.viewer`) roles contain the permissions to create and list
log entries. To delete log entries, grant the Logging Admin
(`roles/logging.admin`) role, which contains the permissions to create, list,
and delete log entries. Note that the Logging Admin
(`roles/logging.admin`) role also grants permissions to perform all actions
in Logging.






## Write log entries by using the gcloud CLI

Logging supports log entries with structured and unstructured
data. Structured data consists of a JSON data structure; for example,
`{"weather": "partly cloudy"}`. Unstructured data
is a string of characters; for example, `"A simple entry"`.

In the next steps, you use the gcloud CLI to write a log entry with
unstructured data and a log entry with structured data.
The [gcloud CLI](/sdk/docs) provide a command-line interface to
the Cloud Logging API.

- 

Write a log entry with unstructured data to the log `my-test-log`, run
the [`gcloud logging write`](/sdk/gcloud/reference/logging/write) command:


```
gcloud logging write my - test - log "A simple entry." 
```


After the command completes, you see the message: `Created log entry`.

- 

Write a log entry with structured data to the log `my-test-log`:


```
gcloud logging write -- payload - type = json my - test - log '{ "message": "My second entry", "weather": "partly cloudy"}' 
```


When you write a log entry with structured data, you must include
`--payload-type=json`. If you omit this field, then Logging
interprets the payload as unstructured data.

If the log `my-test-log` doesn't exist, then Logging creates the
log when the log entry is received.

## List log entries by using the gcloud CLI

You can retrieve log entries from Logging and display them
by using the gcloud CLI. For example, to retrieve and display the log
entries with a resource type of `global`, run the following command:


```
gcloud logging read "resource.type=global" 
```


The command returns a result similar to the following:


```
--- 
insertId : jpj9zjf73t1mn 
jsonPayload : 
message : My second entry 
weather : partly cloudy 
logName : projects / myloggingproject / logs / my - test - log 
receiveTimestamp : '2018-11-01T18:39:31.114507977Z' 
resource : 
labels : 
project_id : myloggingproject 
type : global 
timestamp : '2018-11-01T18:39:31.114507977Z' 
--- 
insertId : vd4m1if7h7u1a 
logName : projects / myloggingproject / logs / my - test - log 
receiveTimestamp : '2018-11-01T18:39:19.718100792Z' 
resource : 
labels : 
project_id : myloggingproject 
type : global 
textPayload : A simple entry 
timestamp : '2018-11-01T18:39:19.718100792Z' 
```


For information about reading logs, see the
[`gcloud logging read`](/sdk/gcloud/reference/logging/read) reference documentation.

## View log entries in the Logs Explorer

To view log entries in the Google Cloud Dedicated console, you can use the
Logs Explorer. Most Google Cloud Dedicated projects store a large number of logs;
you can select certain log entries by writing a query.

To view the log entries that you wrote using the Logs Explorer, do the
following:

- 

In the Google Cloud Dedicated console, go to the
segment 
Logs Explorer** page:


[Go to **Logs Explorer**](https://console.cloud.berlin-build0.goog/logs/query)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

Ensure your Google Cloud Dedicated project is selected in the Google Cloud Dedicated in Germany
navigation bar. If necessary, use the Google Cloud Dedicated project drop-down list
to select your Google Cloud Dedicated project.

- 

In the **Resource** menu, select **Global**.

If you don't see the **Global** menu option or if you don't see your log
entries, then wait a few minutes and refresh the page. It can take a
few minutes for Logging to receive log entries.

- 

To view the details of a log entry, click its *chevron_right*
**Menu**.

The first log entry has its data stored in `textPayload`. The second log
entry contains structured data that is stored in `jsonPayload`. The
structured payload contains the keys `message` and `weather`.

For information about the data format of log entries, see the
[`LogEntry` type](/logging/docs/reference/v2/rest/v2/LogEntry).

## Query log entries in the Logs Explorer

You can query log entries by using the query editor and, with structured logs,
by the key and value. For example, to display all log entries that contain the
text `simple`, do the following:

- 

In the Google Cloud Dedicated console, go to the
segment 
**Logs Explorer** page:


[Go to **Logs Explorer**](https://console.cloud.berlin-build0.goog/logs/query)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

In the **Resource** menu, select **Global**.

- 

In the query editor, enter the string `simple` in quotation marks.
The logs display shows only the log entry `A simple entry.`

- 

After you have viewed your log, remove the query string you added and
click **Run query**. Both log entries reappear in the display.

To display all log entries with structured data that have a key of `weather`
where the `value` field contains `partly`, do the following:

- 

The query editor contains the line `resource.type="global"`.
Enter the following command:


```
jsonPayload . weather : partly 
```


- 

Click **Run query**. The result is the single log entry
`My second entry`.

Logs Explorer also offers saved, suggested, and recent queries.
For more information about queries, see
[Build queries in the Logs Explorer](/logging/docs/view/building-queries).

For sample queries, see [Sample queries using the Logs Explorer](/logging/docs/view/query-library).

## Troubleshooting

- 

Typographical errors and unknown field names result in the
gcloud CLI
commands completing with **invalid argument** messages.
For example, if you forget the period in `resource.type`, then it
results in the error:


```
ERROR : ( gcloud . logging . read ) INVALID_ARGUMENT : Field not found : ' resourcetype ' . 
```


- 

When Cloud Logging hasn't been granted the necessary access permissions,
the gcloud CLI commands complete with
**permission denied** messages.
For example, if a Compute Engine VM
instance is configured with the default API settings, then the `list`
command completes with a permission denied error:


```
ERROR: (gcloud.logging.read) PERMISSION_DENIED: Request had insufficient authentication scopes.
```


To fix this condition, modify your Compute Engine VM instance
permissions to grant Cloud Logging read permission by doing the
following:

- Go to the **VM instance details** page for your VM instance.
Click **Stop**. This action might take a minute or two to complete.

- To modify the configuration, click **Edit**.

- Search for the header **Cloud API access scopes**, and click
**Details** to display the settings for each API. Change the entry
from Cloud Logging API to **Full**. Click **Save**.

- To restart your VM instance, click **Start**. After a few moments,
your VM is ready to use.






## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, delete the Google Cloud Dedicated project with the
resources.






- 

(Optional) To delete the log entries you created, run the following `gcloud`
command:


```
gcloud logging logs delete my-test-log
```


If you don't delete your log entries, then they expire and are removed.
For retention information, see [Quotas & limits](/logging/quotas).






## What's next



- For details on the Logging command-line interface, read the
reference pages for the
[`gcloud logging`](/sdk/gcloud/reference/logging) command group.

- For documentation on the Logging API, see
[Cloud Logging API](/logging/docs/reference/v2/rest).

- For details on the Logs Explorer, see
[Using the Logs Explorer](/logging/docs/view/logs-explorer-interface).