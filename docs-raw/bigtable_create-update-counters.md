# Quickstart: Create and update counters in Bigtable

Source: https://berlin.devsitetest.how/bigtable/docs/create-update-counters
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/bigtable/docs/tpc-differences) for more details.














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

Databases

](https://berlin.devsitetest.how/docs/databases)






- 








[

Bigtable

](https://berlin.devsitetest.how/bigtable/docs)






- 








[

Guides

](https://berlin.devsitetest.how/bigtable/docs/overview)


























# Create and update counters in Bigtable




Learn how to create and update counters in Bigtable using *aggregates*,
table cells that aggregate values at write time. This quickstart uses the
Google Cloud Dedicated console, the Google Cloud CLI, or the 
`cbt` CLI
to create
the following counters:

- A counter that keeps a running sum

- A counter that keeps track of the minimum of all added values

- A counter that keeps track of the maximum of all added values





## Before you begin



















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



After initializing the gcloud CLI, update it and install the required components:



```
gcloud components update
gcloud components install cbt
```














- 




[Create or select a Google Cloud Dedicated project](https://berlin.devsitetest.how/resource-manager/docs/creating-managing-projects).





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













- 


Create a Google Cloud Dedicated project:


```
gcloud projects create PROJECT_ID 
```



Replace ` PROJECT_ID ` with a name for the Google Cloud Dedicated project you are creating.



- 


Select the Google Cloud Dedicated project that you created:


```
gcloud config set project PROJECT_ID 
```



Replace ` PROJECT_ID ` with your Google Cloud Dedicated project name.
















- 



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 



Enable the Cloud Bigtable API and Cloud Bigtable Admin API APIs, if any are not already enabled:





**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).


```
gcloud services enable bigtable.googleapis.com  bigtableadmin.googleapis.com
```









- Run the following commands to ensure that the gcloud CLI is up
to date and includes the 
`cbt` CLI
:

```
gcloud components update
```


```
gcloud components install cbt
```








## Create a Bigtable instance



### Console

- 

In the Google Cloud Dedicated console, go to the **Create instance** page.

[Go to Create instance](https://console.cloud.berlin-build0.goog/bigtable/create-instance) 

- 

In the **Instance name** field, enter `Counters quickstart instance`.

- 

In the **Instance ID** field, enter `counters-quickstart-instance`.

- 

Click **Continue**.

- 

In the **Select your edition** section, select **Enterprise**.

- 

Click **Continue**.

- 

In the **Storage type** section, select **SSD**.

- 

Click **Continue**.

- 

In the **Cluster ID** field, enter `counters-quickstart-cluster`.

- 

In the **Region** list, select **us-east1 (South Carolina)**.

- 

In the **Zone** list, select **us-east1-c**.

- 

In the node scaling section, select **Autoscaling**, and then do the
following:

- For the minimum number of nodes, enter `1`.

- For the maximum number of nodes, enter `3`.

- 

Click **Create** to create the instance.



### gcloud

- 

Use the [`bigtable instances create`
command](/sdk/gcloud/reference/bigtable/instances/create) to create
an instance.


```
gcloud bigtable instances create counters-quickstart-instance \ 
--display-name = "Counters quickstart instance" \ 
--edition = ENTERPRISE \ 
--cluster-config = id = "counters-quickstart-cluster" ,zone = "us-east1-c" 
```





## Connect to your instance

- 

Configure the 
`cbt` CLI
to use your project and
instance by creating a `.cbtrc` file.


```
echo project = PROJECT_ID >> ~/.cbtrc && echo instance = counters-quickstart-instance >> ~/.cbtrc
```


Replace PROJECT_ID with the ID of the project that you are using.

- 

Verify that you set up the `.cbtrc` file correctly.


```
cat ~/.cbtrc
```


The terminal displays the contents of the `.cbtrc` file, which looks similar
to the following:


```
project = PROJECT_ID 
instance = counters-quickstart-instance
```


Now you can use the 
`cbt` CLI
with your instance.

## Create a table with aggregate column families



### Console

- 

In the left navigation pane of the Google Cloud Dedicated console, click
**Tables**.

- 

Click add_box **Create table**.

- 

In the **Table ID** field, enter `counters_quickstart_table`.

- 

Under **Column families**, for each column family that you want to
add, click **Add a column family** and enter the following settings:

- 

**`sum_family`**:

- In the **Column family name** field, enter `sum_family`.

- In the **Column family type** section, select **Aggregate**.

- In the **Aggregator** list, select **Sum**.

- In the **Set garbage collection policy** section, select
**Never collect garbage**.

- Click **Done**.

- 

**`min_family`**:

- In the **Column family name** field, enter `min_family`.

- In the **Column family type** section, select **Aggregate**.

- In the **Aggregator** list, select **Min**.

- In the **Set garbage collection policy** section, select
**Never collect garbage**.

- Click **Done**.

- 

**`max_family`**:

- In the **Column family name** field, enter `max_family`.

- In the **Column family type** section, select **Aggregate**.

- In the **Aggregator** list, select **Max**.

- In the **Set garbage collection policy** section, select
**Never collect garbage**.

- Click **Done**.

- 

Click **Create**.

- 

To view your new column families and their aggregate configurations:

- In the navigation menu, click **Bigtable Studio**.

- In the **Object Explorer** tree on the left, expand **Tables**,
then expand `counters_quickstart_table`, and then expand
**Column Families**.



### cbt

- 

Use the [`cbt createtable`](/bigtable/docs/cbt-reference#create_a_table)
command to create a table named `counters_quickstart_table` that has
three aggregate column families. Configure each column family with a
different aggregation type:

- Column family `max_family` is of type `Max` with an input type of
`Int64`.

- Column family `min_family` is of type `Min` with an input type of
`Int64`.

- Column family `sum_family` is of type `Sum` with an input type of
`Int64`.


```
cbt createtable counters_quickstart_table families = sum_family:never:intsum,min_family:never:intmin,max_family:never:intmax
```


- 

List your column families by running the [`cbt
ls`](/bigtable/docs/cbt-reference#list_tables_and_column_families)
command.


```
cbt ls counters_quickstart_table
```


The shell displays output similar to the following:


```
Family Name GC Policy
----------- ---------
max_family 
min_family 
sum_family 
```





## Create counters in the table

- 

Use the [`cbt
addtocell`](/bigtable/docs/cbt-reference#add_a_value_to_an_aggregate_cell_write)
command to write an initial value of `5` to a new column in each of the
three column families, using a row key of `row-key1` and a timestamp of `0`.
This operation creates aggregate cells, which you use as counters.


```
cbt addtocell counters_quickstart_table row-key1 sum_family:sum_column = 5 @0
cbt addtocell counters_quickstart_table row-key1 min_family:min_column = 5 @0
cbt addtocell counters_quickstart_table row-key1 max_family:max_column = 5 @0
```


## Read the data

You can read the data from your table by querying it with SQL in
the Google Cloud Dedicated console or by using the 
`cbt` CLI
.

### Query the table in the Google Cloud Dedicated console with SQL

- 

In the Google Cloud Dedicated console, open the **Bigtable instances** page.

[Go to instances list](https://console.cloud.berlin-build0.goog/bigtable) 

- 

Select `counters-quickstart-instance` from the list.

- 

In the navigation menu, click **Bigtable Studio**.

- 

Click the **Editor** tab.

- 

Paste this query into the editor:


```
SELECT * FROM `counters_quickstart_table` 
```


- 

Click **Run**. The query results appear in the **Results** table and look
similar to the following:




| 
_key | 
max_family | 
min_family | 
sum_family | 
|



| 
row-key1 | 
{ "max_column": 5 } | 
{ "min_column": 5 } | 
{ "sum_column": 5 } | 
|



### Read with 
`cbt` CLI

- 

To view the counter values as integers rather than bytes, define a YAML
file the 
`cbt` CLI
can use to format the output. Run the following:


```
echo "families:" > ~/cbtformat.yaml
echo " max_family:" >> ~/cbtformat.yaml
echo " default_encoding: BigEndian" >> ~/cbtformat.yaml
echo " default_type: INT64" >> ~/cbtformat.yaml
echo " min_family:" >> ~/cbtformat.yaml
echo " default_encoding: BigEndian" >> ~/cbtformat.yaml
echo " default_type: INT64" >> ~/cbtformat.yaml
echo " sum_family:" >> ~/cbtformat.yaml
echo " default_encoding: BigEndian" >> ~/cbtformat.yaml
echo " default_type: INT64" >> ~/cbtformat.yaml
```


- 

Verify that you set up the `cbtformat.yaml` file correctly.


```
cat ~/cbtformat.yaml
```


The terminal displays the contents of the `cbtformat.yaml` file, which looks
similar to the following:


```
families : 
max_family : 
default_encoding : BigEndian 
default_type : INT64 
min_family : 
default_encoding : BigEndian 
default_type : INT64 
sum_family : 
default_encoding : BigEndian 
default_type : INT64 
```


- 

Use the [`cbt read`](/bigtable/docs/cbt-reference#read_rows) command to pass
the YAML file and read the data you added to the table. The table now
has three columns, each with a different aggregation type.


```
cbt read counters_quickstart_table format-file = $HOME /cbtformat.yaml
```


The shell displays output similar to the following. The values are formatted
as integers, and the timestamps are in UTC format.


```
row-key1
max_family:max_column @ 1970 /01/01-00:00:00.000000
5 
min_family:min_column @ 1970 /01/01-00:00:00.000000
5 
sum_family:sum_column @ 1970 /01/01-00:00:00.000000
5 
```


## Update the counters

- 

Add a value of 3 to each column in the table, using the **same timestamps**
that you used when you created the cells. In each column, the cell value is
merged with the existing value based on the cell's aggregation type.


```
cbt addtocell counters_quickstart_table row-key1 sum_family:sum_column = 3 @0
cbt addtocell counters_quickstart_table row-key1 min_family:min_column = 3 @0
cbt addtocell counters_quickstart_table row-key1 max_family:max_column = 3 @0
```


- 

Use the `cbt read` command again to read the data in the table. Each cell
now contains an aggregated value.


```
cbt read counters_quickstart_table format-file = $HOME /cbtformat.yaml
```


The `sum_column` contains the sum of 5 and 3 (8), `min_column` contains the
minimum of the two values that were written to it (3), and `max_column`
contains the maximum of the two values that were written to it (5).


```
row-key1
max_family:max_column @ 1970 /01/01-00:00:00.000000
5 
min_family:min_column @ 1970 /01/01-00:00:00.000000
3 
sum_family:sum_column @ 1970 /01/01-00:00:00.000000
8 
```







## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, delete the Google Cloud Dedicated project with the
resources.







### Console

- 

Delete the `counters_quickstart_table` table:

- 

In the Google Cloud Dedicated console, go to the **Bigtable instances**
page.

[Go to instances list](https://console.cloud.berlin-build0.goog/bigtable) 

- 

In the list of instances, click **Counters quickstart instance**.

- 

In the left navigation pane, click **Tables**.

- 

Click more_vert next to
`counters_quickstart_table`, and then click **Delete**.

- 

Enter `counters_quickstart_table` to confirm, and then click
**Delete**.

- 

Delete the instance:

- 

In the Google Cloud Dedicated console, go to the **Bigtable instances**
page.

[Go to instances list](https://console.cloud.berlin-build0.goog/bigtable) 

- 

Click **Counters quickstart instance**.

- 

Click **Delete instance**.

- 

Enter `counters-quickstart-instance` to confirm, and then click
**Delete**.

- 

In the terminal, delete the configuration files and optional
credentials:

- 

Delete the `.cbtrc` file:


```
rm ~/.cbtrc
```


- 

Delete the formatting file:


```
rm ~/cbtformat.yaml
```


- 

Optional: Revoke credentials from the gcloud CLI:


```
gcloud auth revoke
```




### cbt

- 

In the terminal, delete the table `counters_quickstart_table`:


```
cbt deletetable counters_quickstart_table
```


- 

Delete the instance:


```
cbt deleteinstance counters-quickstart-instance
```


- 

Delete the `.cbtrc` file:


```
rm ~/.cbtrc
```


- 

Delete the formatting file:


```
rm ~/cbtformat.yaml
```


- 

Optional: Revoke credentials from the gcloud CLI:


```
gcloud auth revoke
```










## What's next



- [Learn more about aggregates](/bigtable/docs/aggregates).

- [Use SQL to query Bigtable data](/bigtable/docs/introduction-sql).

- [Work through a quickstart using the 
`cbt` CLI
](/bigtable/docs/create-instance-write-data-cbt-cli).

- Explore [additional code samples](/bigtable/docs/samples).