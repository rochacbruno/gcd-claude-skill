# Use the bq tool

Source: https://berlin.devsitetest.how/bigquery/docs/quickstarts/load-data-bq
Last updated: 2026-07-15

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/bigquery/docs/tpc-differences) for more details.














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

BigQuery

](https://berlin.devsitetest.how/bigquery/docs)






- 








[

Guides

](https://berlin.devsitetest.how/bigquery/docs/introduction)

















- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Required roles ](#required_roles)

- [ Download the file that contains the source data ](#download_the_file_that_contains_the_source_data)
- [ Create a dataset ](#create_a_dataset)
- [ Load data into a table ](#load_data_into_a_table)
- [ Query table data ](#query_table_data)
- [ Clean up ](#clean-up)

- [ Delete the project ](#delete_the_project)
- [ Delete the resources ](#delete_the_resources)

- [ What's next ](#whats-next)
- 










# Use the bq tool 




In this tutorial, you learn how to use `bq`, the Python-based command-line
interface (CLI) tool for BigQuery to create a dataset, load sample
data, and query tables. After completing this tutorial, you'll be familiar with
`bq` and how to work with BigQuery by using a CLI.

For a complete reference of all `bq` commands and flags, see the
[bq command-line tool reference](/bigquery/docs/reference/bq-cli-reference).





## Before you begin 



















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


If you're using an existing project for this guide,
[verify that you have
the permissions required to complete this guide](#required_roles). If you created a new
project, then you already have the required permissions.

















- 




Enable the BigQuery API.






**Roles required to enable APIs**


To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=bigquery)



For new projects, the BigQuery API is
automatically enabled.

- Optional:
[Enable
billing](/billing/docs/how-to/modify-project) for the project. If you don't want to enable billing or provide
a credit card, the steps in this document still work. BigQuery
provides you a sandbox to perform the steps. For more information, see
[Enable the BigQuery sandbox](/bigquery/docs/sandbox#setup).



### Required roles





















































To get the permissions that
you need to create a dataset, create a table, load data, and query data,

ask your administrator to grant you the
following IAM roles on the project:












- 
Run load jobs and query jobs:
[BigQuery Job User ](/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)





- 
Create a dataset, create a table, load data into a table, and query a table:
[BigQuery Data Editor ](/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).














## Download the file that contains the source data

The file that you're downloading contains approximately 7 MB of data about
popular baby names. It's provided by the US Social Security Administration.

For more information about the data, see the Social Security Administration's
[Background information for popular names](http://www.ssa.gov/OACT/babynames/background.html).

- 

Download the US Social Security Administration's data by opening the
following URL in a new browser tab:


```
https://www.ssa.gov/OACT/babynames/names.zip
```


- 

Extract the file.

For more information about the dataset schema, see the
`NationalReadMe.pdf` file you extracted.

- 

To see what the data looks like, open the `yob2024.txt` file. This file
contains comma-separated values for name, assigned sex at birth, and number
of children with that name. The file has no header row.

- 

Move the file to your working directory.

- 

If you're working in Cloud Shell, click

more_vert 
**More**

**Upload**, click **Choose Files**, choose the
`yob2024.txt` file, and then click **Upload**.

- 

If you're working in a local shell, copy or move the file `yob2024.txt`
into the directory where you're running the bq tool.

## Create a dataset

- 

Enter the following command to create a dataset named `babynames`:


```
bq mk --dataset babynames
```


The output is similar to the following:


```
Dataset 'babynames' successfully created.
```


- 

Confirm that the dataset `babynames` now appears in your project:


```
bq ls --datasets = true 
```


The output is similar to the following:


```
datasetId
-------------
babynames
```


## Load data into a table

- 

In the `babynames` dataset, load the source file `yob2024.txt` into a
new table named `names2024`:


```
bq load babynames.names2024 yob2024.txt name:string,assigned_sex_at_birth:string,count:integer
```


The output is similar to the following:


```
Upload complete.
Waiting on bqjob_r3c045d7cbe5ca6d2_0000018292f0815f_1 ... (1s) Current status: DONE
```


- 

Confirm that the table `names2024` now appears in the `babynames` dataset:


```
bq ls --format = pretty babynames
```


The output is similar to the following. Some columns are omitted to simplify
the output.


```
+-----------+-------+
| tableId | Type |
+-----------+-------+
| names2024 | TABLE |
+-----------+-------+
```


- 

Confirm that the table schema of your new `names2024` table is
`name: string`, `assigned_sex_at_birth: string`, and `count: integer`:


```
bq show babynames.names2024
```


The output is similar to the following. Some columns are omitted to simplify
the output.


```
Last modified Schema Total Rows Total Bytes
----------------- ------------------------------- ------------ ------------
14 Mar 17:16:45 |- name: string 31904 607494
|- assigned_sex_at_birth: string
|- count: integer
```


## Query table data

- 

Determine the most popular girls' names in the data:


```
bq query \ 
'SELECT 
name, 
count 
FROM 
babynames.names2024 
WHERE 
assigned_sex_at_birth = "F" 
ORDER BY 
count DESC 
LIMIT 5' 
```


The output is similar to the following:


```
+-----------+-------+
| name | count |
+-----------+-------+
| Olivia | 14718 |
| Emma | 13485 |
| Amelia | 12740 |
| Charlotte | 12552 |
| Mia | 12113 |
+-----------+-------+
```


- 

Determine the least popular boys' names in the data:


```
bq query \ 
'SELECT 
name, 
count 
FROM 
babynames.names2024 
WHERE 
assigned_sex_at_birth = "M" 
ORDER BY 
count ASC 
LIMIT 5' 
```


The output is similar to the following:


```
+---------+-------+
| name | count |
+---------+-------+
| Aaran | 5 |
| Aadiv | 5 |
| Aadarsh | 5 |
| Aarash | 5 |
| Aadrik | 5 |
+---------+-------+
```


The minimum count is 5 because the source data omits names with fewer than
5 occurrences.






## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, delete the Google Cloud Dedicated project with the
resources.






### Delete the project

If you used the [BigQuery sandbox](/bigquery/docs/sandbox) to query
the public dataset, then billing is not enabled for your project, and you don't
need to delete the project.

The easiest way to eliminate billing is to delete the project that you
created for the tutorial.

To delete the project:






- 
In the Google Cloud Dedicated console, go to the **Manage resources** page.


[Go to Manage resources](https://console.cloud.berlin-build0.goog/iam-admin/projects)




- 
In the project list, select the project that you
want to delete, and then click **Delete**.


- 
In the dialog, type the project ID, and then click
**Shut down** to delete the project.




### Delete the resources

If you used an existing project, delete the resources that you created:

- 

Delete the `babynames` dataset:


```
bq rm --recursive = true babynames
```


The `--recursive` flag deletes all tables in the dataset, including the
`names2024` table.

The output is similar to the following:


```
rm: remove dataset 'myproject:babynames'? (y/N)
```


- 

To confirm the delete command, enter `y`.






## What's next



- Learn about the [BigQuery sandbox](/bigquery/docs/sandbox).

- Learn more about
[loading data into BigQuery](/bigquery/docs/loading-data).

- Learn more about
[querying data in BigQuery](/bigquery/docs/query-overview).