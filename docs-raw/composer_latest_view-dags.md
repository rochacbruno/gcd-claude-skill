# View DAGs, DAG runs, and tasks

Source: https://berlin.devsitetest.how/composer/docs/latest/view-dags
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/composer/docs/tpc-differences) for more details.














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

Data analytics

](https://berlin.devsitetest.how/docs/data)






- 








[

Managed Service for Apache Airflow

](https://berlin.devsitetest.how/composer/docs)






- 








[

Gen 3 Guides

](https://berlin.devsitetest.how/composer/docs/composer-3/composer-overview)












# View DAGs, DAG runs, and tasks 





















This page explains how to get information about DAGs in your environment.

## Ways to view information about DAGs

Managed Airflow provides several ways to get detailed information about DAGs in your environment:

- DAG UI is a section of Google Cloud Dedicated console interface for
Managed Airflow dedicated to viewing and monitoring DAGs, DAG runs,
and individual tasks.

- [Airflow UI](/composer/docs/composer-3/access-airflow-web-interface) is the built-in web interface of Airflow.

- [Airflow CLI](/composer/docs/composer-3/access-airflow-cli) is the command-line interface of Airflow. You
can get information about DAGs by running Airflow CLI commands with
`gcloud`.

## About Managed Airflow DAG UI

DAG UI is a section of Google Cloud Dedicated console interface for
Managed Airflow dedicated to viewing and monitoring DAGs, DAG runs,
and individual tasks.

In DAG UI, you can:

- 

View a list of DAGs in your environment, including schedule intervals, DAG
states, and descriptions.

- 

Pause, unpause, and [trigger DAGs](/composer/docs/composer-3/schedule-and-trigger-dags#manual).

- 

View DAG run details, including successful, active, and failed runs, time
since the last completed run. For each DAG, you can see the history of DAG
runs and task instances associated with this particular DAG, including logs
for executed tasks.

- 

Filter DAG run details. For example, you can pick a time interval and
create queries to select the information that you need.

- 

View detailed information about individual DAGs and tasks. This includes
visualized DAG diagrams, information about the tasks within a DAG, DAG
source code, and extra information about DAGs.

## Before you begin

- 

Make sure that your account has a role that can access DAG UI and view DAG
details. For more information, see [Access control](/composer/docs/composer-3/access-control).

- 

DAG UI requires enabled [DAG serialization](/composer/docs/composer-1/dag-serialization).

- 

DAG UI is supported in Managed Airflow 1.17.8 and later
versions. 

## View the list of DAGs for your environment



### Console

The **DAGs** tab of your environment shows the list of DAGs along with DAG
run details for each DAG.

To view the list of DAGs:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the **DAG list** column, follow the **DAGs** link for your environment.

You can use filters to view the details only for certain DAGs or for
certain conditions. For example:

- Select the **Filters** field.

- From the drop-down list, select the **DAG id** property.

- Specify the identifier of the DAG. The results show details only for
the selected DAG.

- (Optional) To include more DAGs, add `OR` operators followed by DAG ids.

- (Optional) To filter on other conditions, add other properties in
the **Filters** field. For example, you can filter for DAGs with failed
runs by specifying `Failed runs:>0`.



### Airflow UI

To view the list of DAGs in the Airflow UI:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the **Airflow webserver** column, follow the **Airflow** link for your
environment.

- 

Log in with the Google account that has the appropriate permissions.

- 

In the Airflow UI, on the **DAGs** page, a list of DAGs for
your environment is displayed.



### gcloud

Run the `dags list` Airflow CLI command:


```
gcloud composer environments run ENVIRONMENT_NAME \ 
--location LOCATION \ 
dags list -- -o plain
```


Replace:

- `ENVIRONMENT_NAME` with the name of the environment.

- `LOCATION` with the region where the environment is located.




## View the history of DAG runs and tasks



### Console

The **Runs** tab on the **DAG details** page shows the history of DAG runs
for an individual DAG.

To view the history of DAG runs:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the **DAG list** column, follow the **DAGs** link for your environment.

- 

Select a DAG.

- 

On the **DAG details** page, go to the **Runs** tab.

- 

Select a DAG run from the list to view the DAG run details, such as the
state of task instances for this DAG run, the number of tries and the
execution duration. You can select individual tasks to view
task instance logs.



### Airflow UI

To view the list of DAGs in the Airflow UI:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the **Airflow webserver** column, follow the **Airflow** link for your
environment.

- 

Log in with the Google account that has the appropriate permissions.

- 

View DAG runs:

- 

*(Airflow 3)* In the Airflow UI,
select **Dags** > **Runs**. The **Runs** tab
displays DAG runs for your environment. You can follow the link in the
**Run after** column to get additional information about tasks.

- 

*(Airflow 2)* In the Airflow UI,
select **Browse** > **DAG Runs**. The **DAG Runs** page
displays DAG runs for your environment. You can follow the link in the
**Run ID** column to get additional information about tasks.



### gcloud

Run the `dags list-runs` Airflow CLI command:


```
gcloud composer environments run ENVIRONMENT_NAME \ 
--location LOCATION \ 
dags list-runs -- -d DAG_ID 
```


Replace:

- `ENVIRONMENT_NAME` with the name of the environment.

- `LOCATION` with the region where the environment is located.

- `DAG_ID` with the name of the DAG.

You can get additional information about task instances by running `tasks state` and `tasks states-for-dag-run` Airflow CLI commands.

For more information, see [Access Airflow CLI](/composer/docs/composer-3/access-airflow-cli) and the
[Airflow CLI reference](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html).




## View DAG diagrams



### Console

The **Diagram** tab on the **DAG details** page show the visualisation of a
DAG with task dependencies.

To view the diagram of a DAG:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the **DAG list** column, follow the **DAGs** link for your environment.

- 

Select a DAG.

- 

On the **DAG details** page, go to the **Diagram** tab.

- 

(Optional) To see additional information about tasks, select individual tasks on the diagram.



### Airflow UI

To view the diagram of a DAGs in the Airflow web interface:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the **Airflow webserver** column, follow the **Airflow** link for your
environment.

- 

Log in with the Google account that has the appropriate permissions.

- 

In the Airflow UI, on the **DAGs** page, a list of DAGs for
your environment is displayed.

- 

*(Airflow 3)* Click your DAG to go to the **Dags** page, then click
**Show graph** to switch to the Graph view.

- 

*(Airflow 2)* For your DAG, in the **Links** column, follow the **Graph**
link.




## View DAG source code and additional information about DAGs



### Console

You can view the source code of your DAGs and additional information such as
DAG identifiers and links to DAG definition files in the environment's
bucket.

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the **DAG list** column, follow the **DAGs** link for your environment.

- 

Select a DAG.

- 

To view the DAG source code, go to the **Diagram** tab.

- 

To view additional information about the DAG, go to the **Source** tab.



### Airflow UI

To view the diagram of a DAGs in the Airflow web interface:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the **Airflow webserver** column, follow the **Airflow** link for your
environment.

- 

Log in with the Google account that has the appropriate permissions.

- 

In the Airflow web interface, on the **DAGs** page, click on the name of
your DAG.

- 

In the page with DAG details, navigate to available tabs to view
additional information about the DAG.




## What's next

- [Add and update DAGs](/composer/docs/composer-3/manage-dags)

- [Schedule and trigger DAGs](/composer/docs/composer-3/schedule-and-trigger-dags)