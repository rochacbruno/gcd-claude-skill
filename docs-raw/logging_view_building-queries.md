# Build and save queries by using the Logging query language

Source: https://berlin.devsitetest.how/logging/docs/view/building-queries
Last updated: 2026-07-06

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












# Build and save queries by using the Logging query language 






- On this page ** 
- [ Before you begin ](#before_you_begin)
- [ Build queries ](#building-queries)
- [ Search for text across log fields ](#search-text)

- [ Boolean operators and the search field ](#boolean-operators)

- [ Construct queries with filter menus ](#query-builder-menus)
- [ View logs by time range ](#queries-with-time-restriction)

- [ Use the time-range selector ](#time-range)
- [ Include a timestamp expression in the query-editor field ](#timestamp-expression)

- [ Write advanced queries using the Logging query language ](#queries-by-expression)
- [ Use recent queries ](#recent-queries)
- [ Save and share queries ](#saved-queries)

- [ View saved queries ](#view-shared)

- [ Use suggested queries ](#suggested_queries)
- [ Select queries from the library ](#library-queries)
- [ What's next ](#whats_next)
- 









This document describes how to retrieve and analyze logs when you use the
Logs Explorer by writing queries in the query-editor field and by
selecting from predefined filter options. The
queries you build are written in the
[Logging query language](/logging/docs/view/logging-query-language).

You can also save your queries in the Logs Explorer page, or by using the
Logging API method
[`savedQueries.create`](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create).

## Before you begin 

The Logs Viewer role (`roles/logging.viewer`) provides access to view logs.
For example, when granted this role, you can write and run queries. You can also
save queries as private queries, and run both private and shared queries.
However, this role doesn't let you save or modify shared queries. If you want
to save or modify shared queries, then ensure that you have been granted the
Logging Admin role (`roles/logging.admin`), which provides full access to
Cloud Logging.

Do one of the following:

- 


































To get the permissions that
you need to write and run queries, to run and save private queries, and
to run shared queries,

ask your administrator to grant you the
[Logs Viewer ](/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) IAM role on your project.


















- 


































To get the permissions that
you need to write and run queries, to run and save private queries,
and to run, create, and manage shared queries,

ask your administrator to grant you the
[Logging Admin ](/iam/docs/roles-permissions/logging#logging.admin) (`roles/logging.admin`) IAM role on your project.


















For more information about the necessary IAM permissions, see
[Permissions for the Google Cloud Dedicated console](/logging/docs/access-control#console_permissions).

## Build queries

To build queries by using the Google Cloud Dedicated console, do the following:

- 

In the Google Cloud Dedicated console, go to the
segment 
Logs Explorer** page:


[Go to **Logs Explorer**](https://console.cloud.berlin-build0.goog/logs/query)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

Select the Google Cloud Dedicated project or other Google Cloud Dedicated
resource for which you want to view logs.

- 

Use the **Query** pane to build your query.

The **Query** pane provides multiple ways to build and run query expressions:

- Search for text across all log fields.

- Select options from filter menus.

- Write or modify queries by using the query editor.

- View and run saved, recent, and suggested queries from the
*menu_book* **Query library**.

## Search for text across log fields

To search for text across all log fields and find all matching log entries,
in the toolbar of the query pane, enter your search terms in the
*search* **Search all fields** field. The search terms you enter in
this field are converted into a Logging query language expression.

You can search for words and phrases, and your search terms can include
[Boolean operators](#boolean-operators) and [regular expressions](/logging/docs/view/logging-query-language#regular-expressions):

- 

To perform a case-sensitive search, you must use a
[regular expression](/logging/docs/view/logging-query-language#regular-expressions).

- 

To perform a case-insensitive search along token boundaries, enter the search
terms without backticks or double quotes.

For example, to search for log entries that contain the word `hello` and
the word `world`, enter `hello world`. This command, which is converted to
`SEARCH("hello world")`, matches log entries that contain the tokens
`hello` and `world`, in any order. Because the search is case-insensitive,
the search also matches a log entry that contains the tokens `Hello` and
`World`. The search doesn't match the token `worlds`.

- 

To perform a case-insensitive search for a phrase along token boundaries,
wrap the phrase in backticks.

For example, to search for the phrase `hello world`,
enter ``hello world``.
This command, which is converted to `SEARCH("`hello world`")`,
matches log entries that contain the token `hello world`.
The search doesn't match the token `hello worlds`.

- 

To perform a case-insensitive search for a substring, wrap the text in
double quotes. For example, `"hello world"` matches `Hello World` and
`Hello world`. The same query also matches `hello worlds`, because the
search isn't performed along token boundaries.

To see your search terms within the query expression, enable **Show query**.

After you enter your search terms, click **Run query** or press the **Enter**
key. The results of the query are displayed in the **Query results** pane.

### Boolean operators and the search field

The *search* **Search all fields** field supports the usage of the
Boolean operators `AND`, `OR`, and `NOT`. If you use Boolean
operators, then do the following:

- 

Capitalize Boolean operators. Lowercase `and`, `or`,
and `not` are parsed as search terms, not as operators.

- 

Don't use parentheses to nest rules. The search terms are parsed according
to [precedence rules](#precedence). Parentheses are parsed like any other
character.

If you don't include any operators, all search terms and phrases are joined by
`AND`. That is, you can omit the `AND` operator between search terms.

#### Examples

Suppose you enter `request AND localhost OR client` into the
*search* **Search all fields** field. Due to the
[precedence rules](#precedence),
the search terms are converted into the following query:


```
SEARCH("`request`")
SEARCH("`localhost`") OR SEARCH("client")
```


Next, suppose that you want to list log entries that contain the string
`client` or that contain both `request` and `localhost`. You can't use the
*search* **Search all fields** field to generate a query that matches
your goal. When your search terms contain both an `AND` and an `OR`
statement, the [precedence rules](#precedence) specify that the `OR` operation
is always performed first. Parentheses aren't treated as special characters
when they are included in search terms.

However, you can use the **Query** pane and enter a query. In the **Query**
pane, you can use parentheses to specify order in which commands are
processed. For example, the following query satisfies your goal:


```
(SEARCH("`request`") AND SEARCH("`localhost`")) OR SEARCH("`client`")
```


#### Operator precedence

The `AND` and `OR` operators are
[short-circuit operators](https://en.wikipedia.org/wiki/Short-circuit_evaluation).
You can combine`AND` and `OR` rules in the same expression. For example, when
the two operators are mixed, the expression `a AND b OR c AND d` turns into the
following Logging query language expression:


```
"a"
"b" OR "c"
"d"
```


The `NOT` operator has the highest precedence, followed by `OR` and `AND`
in that order.

The `NOT` operator performs a negation of the subsequent term. For example,
`NOT error` returns log entries that don't contain `error`. You can also replace
the `NOT` operator with the `-` (minus) operator. For example, the following two
queries are the same:


```
"response" AND "successful" AND NOT "error"
```



```
"response successful" -"error"
```


This logic also works with a phrase, if the `-` (minus) operator is outside the
quotation marks. For example, the following two queries are the same:


```
-"response successful"
```



```
NOT "response successful"
```


## Construct queries with filter menus

You can use the filter menus in the **Query** pane to add resource, log name,
log severity, and correlation parameters to the query-editor field. These
options correspond to the [LogEntry](/logging/docs/reference/v2/rest/v2/LogEntry) fields for all logs in
Logging.

The options in the **Resource** and **Log name** menus are derived from the
log entries that are stored by Cloud Logging.

- **Resource**: Lets you specify the [resource.type](/logging/docs/reference/v2/rest/v2/LogEntry) and
associated `resource.labels`. You can select a single resource type using
this filter menu, and zero or more resource labels to apply to your
query. The resource parameters are joined by the logical operator `AND`.

- **Log name**: Lets you specify the [logName](/logging/docs/reference/v2/rest/v2/LogEntry). You can select
multiple log names to apply to your query. When selecting multiple log
names, the logical operator `OR` is used.

- **Severity**: Lets you specify the [severity](/logging/docs/reference/v2/rest/v2/LogEntry#logseverity). You can select
multiple severity levels at the same time to add to apply to your query.
When selecting multiple severity levels, the logical operator `OR` is
used.

- **Correlate by**: Lets you group and view log entries in a "parent-child"
format. For more information, see [Correlate log entries](/logging/docs/view/correlate-logs).

To use any of the filter menus, do the following:

- 

Expand the *arrow_drop_down* **Menu** on any
of the filter menus in the **Query** pane.

- 

Refine the filter parameters.

- 

Click **Apply**. You see the parameters in the query-editor field.

To see your search terms within the query expression, enable **Show query**.

- 

After you review the query, click **Run query**. The results of the
query are displayed in the **Query results** pane.

For certain Compute Engine resource types, such as `gce_instance` and
`gce_network`, you see the resource name with the resource ID as subtext. For
example, for the `gce_instance` resource type, you see the VM name
alongside the VM ID. The resource names help you identify the correct
resource ID, on which you can build queries.

## View logs by time range

There are two ways to display logs that were written in a specific time range:

- Use the time-range selector.

- Include a timestamp expression in the query-editor field.

### Use the time-range selector

The options in the time-range selector let you select from preset time options,
specify a custom start and end time, or center the time range around a specific
timestamp. For example, if you want to view
the data for the past week, then select **Last 1 week** from the time-range
selector.

You can also set your time zone preferences by using the time-range selector.

### Include a timestamp expression in the query-editor field

To add a timestamp expression directly to the query-editor field,
use the
[Logging query language](/logging/docs/view/logging-query-language).

If the query-editor field contains an expression with a timestamp, then the
time-range selector is disabled, and the query uses the timestamp expression as
its time-range restriction. If a query doesn't use a timestamp expression, then
the query uses the time-range selector as its time-range restriction.

## Write advanced queries using the Logging query language

You can use the
[Logging query language](/logging/docs/view/logging-query-language) to build
more advanced queries in the Logs Explorer query-editor field:

- 

If you don't see the query-editor field in the **Query** pane, enable
**Show query**.

- 

Enter your query expressions directly into the query-editor field.

If you added any search terms in the search field or selected any
parameters in the filter menus, then those also appear in the
query-editor field and are evaluated as part of your query expression.

- 

After you review your query, click **Run query**.

Logs that match your query are listed under the
[**Query results**](/logging/docs/view/logs-explorer-interface#query-results)
pane. The
[**Histogram**](/logging/docs/view/logs-explorer-interface#histogram-panel)
and
[**Log fields**](/logging/docs/view/logs-explorer-interface#logs-field-panel)
panes also adjust according to the query expression.

For examples of common queries you might want to use, see
[Sample queries using the Logs Explorer](/logging/docs/view/query-library-preview).

## Use recent queries

When you run any query, the query is added to the
*menu_book* **Query library**, which contains the last 10,000 unique
queries over a 30-day period.

To view your recent queries, select the *menu_book* **Query library**
button in the primary toolbar. For recent queries, you have the following
options:

- **Stream**: To run the query and [stream](/logging/docs/view/streaming-live-tailing) the results, choose this
option.

- **Run**: To run the query, choose this option.

- 

*more_vert* **More options**:
Lets you view the query expression with the options to run the query or save
it to your list of **Saved** queries. You can also select the query directly
to get these options.

To save the query, do the following:

- Click **Save**. The **Save query** dialog opens.

- 

Complete the following fields:

- **Name** (Required): Provide a name for your query. Names are limited to
64 characters.

- **Description** (Optional): Provide a description to help identify the
purpose of the query.

- **Include summary fields** (Optional): Enable **Include summary fields**
and enter the [summary fields](/logging/docs/view/logs-explorer-interface#add_summary_fields) that you want to display.

- **Truncate summary fields** (Optional): Enable
**Truncate summary fields** and select the number of characters to
truncate to and whether truncation occurs at the beginning or end of the
fields.

- 

Click **Save query**. The query is now available in your
[Saved queries list](#saved-queries).

You can also sort and filter your recent queries; the filter matches on the text
in your query expression.

## Save and share queries

Saved queries let you store query expressions to help you explore your logs more
consistently and efficiently. The Logs Explorer features a
**Query library**, where you can access your saved queries. You can also
save your queries by using the Logging API method
[`savedQueries.create`](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create).

You can save your query so that it is private and visible only to you, or you
can share it with other members of the Google Cloud Dedicated project. Once you share
a query, the query is no longer owned by you, and any member in the project
with the necessary permissions can access the query.


[ Console ](#console) [ API ](#api) 
**More 




To save a query expression that you've built in the query-editor field, do the
following:

- 

Click **Save** in the **Query** pane. The **Save query** dialog opens,
with your query expression in the query-editor field.

- 

Complete the following fields:

- **Name** (Required): Provide a name for your query. Names are limited to
64 characters.

- **Description** (Optional): Provide a description to help identify the
purpose of the query.

- **Include custom summary fields** (Optional): Enable **Include summary
fields** and enter the [summary fields](/logging/docs/view/logs-explorer-interface#add_summary_fields) that you want
to display.

- **Truncate summary fields** (Optional): Enable
**Truncate summary fields** and select the number of characters to
truncate to and whether truncation occurs at the beginning or end of the
fields.

- **Share with project**: Optionally, enable **Share with project** to
share your query with other members of the Google Cloud Dedicated project.

- 

Click **Save query**. Your saved queries appear in a
list under the **Saved** tab.

To run a saved query, click **Run**. To run the query and [stream](/logging/docs/view/streaming-live-tailing)
the results, click **Stream**.

To modify a saved query, select *more_vert* **More options**,
and then select *edit* **Edit**. You can also select the query,
make modifications, and then save the modified query.

To delete a saved query, select *more_vert* **More options**,
and then select delete **Delete**.

You can also sort and filter your saved queries; the filter matches the text
in your query expression.



To save a query by using the Logging API, use the
`savedQueries.create` method. For more information about this method, its
parameters, and the response data, see the reference page for
[`savedQueries.create`](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create).

The following example illustrates a sample request body, which
contains an instance of `SavedQuery`:


```
{
"parent": "projects/my-project/locations/global"
"savedQueryId": "compute-query"
{
"displayName": "compute-admin-activity-query",
"description": "Queries for Compute Engine Admin Activity logs.",

"loggingQuery":
{
"filter": resource.type="gce_instance" AND log_id("cloudaudit.googleapis.com/activity"),
},
"visibility": "PRIVATE"
}
}
```


To share the query with other members of the Google Cloud Dedicated project, specify
a value of `SHARED` in the `visibility` field.



### View saved queries

You can view both private queries and queries that are shared with other members
in the Google Cloud Dedicated project by clicking the *menu_book* **Query
library** button:


[ Console ](#console) [ API ](#api) 
More 




- 

In the Google Cloud Dedicated console, go to the
segment 
Logs Explorer** page:


[Go to **Logs Explorer**](https://console.cloud.berlin-build0.goog/logs/query)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

Select the Google Cloud Dedicated project or other Google Cloud Dedicated
resource for which you want to view logs.

- 

Click the *menu_book* **Query library** button, and click
**Saved**.

You can sort the table by any header. The **Visibility** column indicates
if the queries are shared or private:

- **Shared**: Queries that are shared with other members of the
Google Cloud Dedicated project.

- **Private**: Queries that you have saved and are only visible to you.




You can use the Logging API to view private and shared
queries by using the
[`savedQueries.list`](/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/list) method.

For example, the following request body lists all shared Logs Explorer
queries with a wildcard location ID:


```
{
"parent": "name": projects/PROJECT_ID/locations/-
"visibility": "SHARED"
"filter": "explorer"
}
```



## Use suggested queries

Logging generates suggested queries based on the context of your
Google Cloud Dedicated project, such as the Google Cloud Dedicated products you're using.
Suggested queries can help you identify issues and provide you with insights
into the overall health of your systems. For example, detecting that you're
using Google Kubernetes Engine, Logging might suggest a query that finds
all the error logs for your containers.

To view and run suggested queries, click the *menu_book*
**Query library** button and click **Suggested**. In the **Suggested** tab, you
have the following options:

- **Stream**: To run the query and [stream](/logging/docs/view/streaming-live-tailing) the results, choose this
option.

- **Run**: To run the query, choose this option.

- 

*more_vert* **More options**:
Lets you view the details of the query expression with the options to run the
query or save it. You can also select the query directly
to get these options.

To review the details of a suggested query, do either of the following:

- 

Select the query's row.

- 

Click *more_vert* **More**
and select **View**. The **Query details** dialog opens.

In the **Query details** dialog, you see the query and the options to **Run**,
**Stream** or **Save as**:

- 

To save the query, do the following:

- Click **Save query**.

- Complete the fields in the [**Save query** dialog](#saved-queries).

The edited query shows up in your **Saved** list, where you can choose to
run the query later.

- 

To run the query now, click **Run**. The query runs and appears in the
query-editor field.

- 

To run the query now and [stream](/logging/docs/view/streaming-live-tailing) the results, click **Stream**.

- 

To close the dialog and return to the suggested queries list, click
**Close**.

Note the following expected behaviors:

- Successive page loads might not show the same queries in the same order.

- You might see zero suggested queries.

- Sometimes running a suggested query returns zero logs.

## Select queries from the library

Logging provides a library of queries based on common use
cases and Google Cloud Dedicated products. These queries can help you efficiently
find logs during time-critical troubleshooting sessions and explore your logs
to better understand what Logging data is available.

To view and run the library's queries, do the following:

- 

In the Google Cloud Dedicated console, go to the
segment 
**Logs Explorer** page:


[Go to **Logs Explorer**](https://console.cloud.berlin-build0.goog/logs/query)

If you use the search bar to find this page, then select the result whose subheading is
**Logging**.

- 

Select the Google Cloud Dedicated project or other Google Cloud Dedicated
resource for which you want to view logs.

- 

Click the *menu_book* **Query library** button. You see categories
of available queries and subsets of queries based on Google Cloud Dedicated
products. To narrow the selection of queries that you see, click any of the
products.

You can also use the search field to search the available queries by
category, description, or the contents of the query expression.

- 

To review a query expression, do either of the following:

a. Click the query's row.

b. Click *more_vert* **More** and select **View**.

- 

In the **Query details** dialog, you see the query and the options to
**Run**, **Stream** or **Save as**:

- 

To save the query, do the following:

- Click **Save query**.

- Complete the fields in the [**Save query** dialog](#saved-queries).

The edited query shows up in your **Saved** list, where you can choose to
run the query later.

- 

To run the query now, click **Run**. The query runs and appears in the
query-editor field.

- 

To run the query now and [stream](/logging/docs/view/streaming-live-tailing) the results, click **Stream**.

- 

To close the dialog and return to the suggested queries list, click
**Close**.

## What's next

- [Sample queries](/logging/docs/view/query-library)