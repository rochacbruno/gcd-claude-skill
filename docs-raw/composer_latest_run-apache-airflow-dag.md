# Quickstart: Run an Apache Airflow DAG in Managed Airflow (Gen 3)

Source: https://berlin.devsitetest.how/composer/docs/latest/run-apache-airflow-dag
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


























# Run an Apache Airflow DAG in Managed Airflow (Gen 3)




This quickstart guide shows you how to create a Managed Service for Apache Airflow environment
and run an Apache Airflow DAG in Managed Airflow (Gen 3).

- 

If you are **new to Airflow**, see the
[Airflow concepts tutorial](https://airflow.apache.org/docs/stable/concepts.html) in Apache Airflow
documentation for more information about Airflow concepts, objects, and
their usage.

- 

If you want to **use Google Cloud CLI instead**, see
[Run an Apache Airflow DAG in Managed Service for Apache Airflow (Google Cloud CLI)](/composer/docs/composer-3/run-apache-airflow-dag-gcloud).

- 

If you want to create an environment **using Terraform**, see
[Create environments (Terraform)](/composer/docs/composer-3/terraform-create-environments).





## Before you begin





















- 




In the Google Cloud Dedicated console, on the project selector page,
select or create a Google Cloud Dedicated project.





**Roles required to select or create a project**




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



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).



















- 








Enable the Managed Airflow API, if it is not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=composer.googleapis.com)



- 










































































































To get the permissions that
you need to complete this quickstart,

ask your administrator to grant you the
following IAM roles on your project:












- 
To assign IAM roles and permissions:
[Project IAM Admin ](/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)





- 
To create a service account for the Managed Airflow environment:
[Create Service Accounts ](/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)





- 
To view create and manage the Managed Airflow environment:




- [Environment and Storage Object Administrator ](/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)


- [Service Account User ](/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)







- 
To view logs:
[Logs Viewer ](/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).
















## Create an environment's service account

When you create an environment, you specify a service account. This service
account is called *environment's service account*. Your environment uses this
service account to perform most of the operations.

The service account for your environment is not a user account. A
service account is a special kind of account used by an application or a
virtual machine (VM) instance, not a person.

To create a service account for your environment:

- 

[Create a new service account](/iam/docs/service-accounts-create#creating), as described in
the Identity and Access Management documentation.

- 

[Grant a role to it](/iam/docs/granting-changing-revoking-access#grant-single-role), as described in the Identity and Access Management
documentation. The required role is **Composer Worker** (`composer.worker`).

## Create an environment

- 

In the Google Cloud Dedicated console, go to the **Create environment** page.

[Go to Create environment](https://console.cloud.berlin-build0.goog/composer/environments/create-composer-3) 

- 

In the **Name** field, enter `example-environment`.

- 

In the **Location** drop-down list, select a region for the
Managed Airflow environment. This guide uses `us-central1` region.

- 

For other environment configuration options, use the provided defaults.

- 

Click **Create** and wait until the environment is created.

- 

When done, a green check mark is displayed next to the environment name.

## Create a DAG file

An [Airflow DAG](https://airflow.apache.org/docs/stable/concepts.html) is a collection of organized tasks that
you want to schedule and run. DAGs are defined in standard Python files.

This guide uses an example Airflow DAG defined in the `quickstart.py` file.
Python code in this file does the following:

- Creates a DAG, `composer_sample_dag`. This DAG runs every day.

- Executes one task, `print_dag_run_conf`. The task prints the DAG run's
configuration by using the bash operator.

Save a copy of the `quickstart.py` file on your local machine:























```
import datetime 

from airflow import models 
from airflow.operators import bash 

# If you are running Airflow in more than one time zone 
# see https://airflow.apache.org/docs/apache-airflow/stable/timezone.html 
# for best practices 
YESTERDAY = datetime . datetime . now () - datetime . timedelta ( days = 1 ) 

default_args = { 
"owner" : "Composer Example" , 
"depends_on_past" : False , 
"email" : [ "" ], 
"email_on_failure" : False , 
"email_on_retry" : False , 
"retries" : 1 , 
"retry_delay" : datetime . timedelta ( minutes = 5 ), 
"start_date" : YESTERDAY , 
} 

with models . DAG ( 
"composer_quickstart" , 
catchup = False , 
default_args = default_args , 
schedule_interval = datetime . timedelta ( days = 1 ), 
) as dag : 
# Print the dag_run id from the Airflow logs 
print_dag_run_conf = bash . BashOperator ( 
task_id = "print_dag_run_conf" , bash_command = "echo {{ dag_run.id }}" 
) 
```



## Upload the DAG file to your environment's bucket

Every Managed Airflow environment has a Cloud Storage
bucket associated with it. Airflow in Managed Airflow schedules only
DAGs that are located in the `/dags` folder in this bucket.

To schedule your DAG, upload `quickstart.py` from your local machine to your
environment's `/dags` folder:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the list of environments, click the name of your environment,
`example-environment`. The **Environment details** page opens.

- 

Click **Open DAGs folder**. The **Bucket details** page opens.

- 

Click **Upload files** and then select your copy of `quickstart.py`.

- 

To upload the file, click **Open**.

## View the DAG

After you upload the DAG file, Airflow does the following:

- Parses the DAG file that you uploaded. It might take a few minutes for the
DAG to become available to Airflow.

- Adds the DAG to the list of available DAGs.

- Executes the DAG according to the schedule you provided in the DAG file.

Check that your DAG is processed without errors and is available in Airflow by
viewing it in DAG UI. DAG UI is Managed Airflow interface for viewing
DAG information in Google Cloud Dedicated console. Managed Airflow also provides
access to [Airflow UI](/composer/docs/composer-3/access-airflow-web-interface), which is a native Airflow web
interface.

- 

Wait about five minutes to give Airflow time to process the DAG file
that you uploaded previously, and to complete the first DAG run
(explained later).

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

In the list of environments, click the name of your environment,
`example-environment`. The **Environment details** page opens.

- 

Go to the **DAGs** tab.

- 

Check that the `composer_quickstart` DAG is present
in the list of DAGs.


[

](/static/composer/docs/images/composer-quickstart-dag-list.png)

**Figure 1.** The list of DAGs displays the
composer_quickstart DAG (click to enlarge)



## View DAG run details

A single execution of a DAG is called a *DAG run*. Airflow immediately
executes a DAG run for the example DAG because the start date in the DAG file is
set to yesterday. In this way, Airflow catches up to the specified DAG's
schedule.

The example DAG contains one task, `print_dag_run_conf`, which runs the `echo`
command in the console. This command outputs meta information about the DAG
(DAG run's numeric identifier).

- 

On the **DAGs** tab, click `composer_quickstart`. The **Runs** tab for the
DAG opens.

- 

In the list of DAG runs, click the first entry.


[

](/static/composer/docs/images/composer-quickstart-dag-runs-list.png)

**Figure 2.** The list of DAG runs for the
composer_quickstart DAG (click to enlarge)



- 

DAG run details are displayed, detailing the information about individual
tasks of the example DAG.


[

](/static/composer/docs/images/composer-quickstart-task-list.png)

**Figure 3.** The list of tasks that were executed in
the DAG run (click to enlarge)



- 

The **Logs for DAG run** section lists logs for all tasks in the DAG run.
You can see the output of the `echo` command in the logs.


[

](/static/composer/docs/images/composer-quickstart-task-logs.png)

**Figure 4.** Logs of the print_dag_run_conf task
(click to enlarge)








## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






Delete the **resources** used in this tutorial:

- 

Delete the Managed Airflow environment:

- 

In the Google Cloud Dedicated console, go to the **Environments** page.

[Go to Environments](https://console.cloud.berlin-build0.goog/composer/environments) 

- 

Select `example-environment` and click **Delete**.

- 

Wait until the environment is deleted.

- 

Delete your environment's bucket. Deleting the Managed Airflow
environment does not delete its bucket.

- 

In the Google Cloud Dedicated console, go to the **Storage** > **Browser** page.

[Go to Storage > Browser](https://console.cloud.berlin-build0.goog/storage/browser) 

- 

Select the environment's bucket and click **Delete**. For example, this
bucket can be named `us-central1-example-environ-c1616fe8-bucket`.






## What's next



- [Adding and updating DAGs](/composer/docs/composer-3/manage-dags)

- [Writing DAGs](/composer/docs/composer-3/write-dags)

- [Overriding Airflow configurations](/composer/docs/composer-3/override-airflow-configurations)

- [Accessing Airflow UI](/composer/docs/composer-3/access-airflow-web-interface)