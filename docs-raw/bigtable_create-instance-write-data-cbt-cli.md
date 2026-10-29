# Quickstart: Create an instance and write data with the cbt CLI

Source: https://berlin.devsitetest.how/bigtable/docs/create-instance-write-data-cbt-cli
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

























# Create an instance and write data with the cbt CLI



If you're learning about Bigtable, you can work through a quickstart
to get a taste of the fundamentals that you would use at scale in a production
environment.

In this quickstart, you perform the following actions:

- Connect to a Bigtable instance.

- Perform basic administrative tasks.

- Write data to a table.

- Read data from a table.

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



Enable the Cloud Bigtable and Cloud Bigtable Admin APIs, if any are not already enabled:





**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).


```
gcloud services enable bigtable.googleapis.com  bigtableadmin.googleapis.com
```











- 



Grant roles to your user account. Run the following command once for each of the following
IAM roles:
`roles/bigtable.admin`




```
gcloud projects add-iam-policy-binding PROJECT_ID --member = "user: USER_IDENTIFIER " --role = ROLE 
```



Replace the following:




- ` PROJECT_ID `: Your project ID.


- ` USER_IDENTIFIER `: The identifier for your user

account. For examples, see
[
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users).



- ` ROLE `: The IAM role that you grant to your user account.















- Run the following command to install the 
`cbt` CLI
:

```
gcloud components install cbt
```



## Create a Bigtable instance

- 

Open the **Create instance** page in the Google Cloud Dedicated console.

[Create an instance](https://console.cloud.berlin-build0.goog/bigtable/create-instance) 

- 

For **Instance name**, enter `Quickstart instance`.

- 

For **Instance ID**, enter `quickstart-instance`.

- 

Click **Continue**.

- 

For **Storage type**, select **SSD**.

- 

Click **Continue**.

- 

For **Cluster ID**, enter `quickstart-instance-c1`.

- 

For **Region**, select a region near you.

- 

For **Zone**, select **Any**.

- 

For **Node scaling mode**, choose **Manual allocation**.

- 

For **Quantity**, select **1**.

- 

Click **Create** to create the instance.

## Connect to your instance

- 

Configure the 
`cbt` CLI
to use your project and instance by creating a
`.cbtrc` file, replacing ` PROJECT_ID ` with the ID
for the project where you created your Bigtable instance:


```
echo project = PROJECT_ID >> ~/.cbtrc && echo instance = quickstart-instance >> ~/.cbtrc
```


- 

Verify that you set up the `.cbtrc` file correctly:


```
cat ~/.cbtrc
```


The terminal displays the contents of the `.cbtrc` file, which looks similar
to the following:


```
project = PROJECT_ID 
instance = quickstart-instance
```


Now you can use the 
`cbt` CLI
with your instance.

## Read and write data

Bigtable stores data in *tables*, which contain *rows*. Each row
is identified by a *row key*.

Data in a row is organized into *column families*, which are groups of columns.
A *column qualifier* identifies a single column within a column family.

There can be multiple time-stamped cells at the intersection of
a row and column.

- 

Create a table named `my-table`.


```
cbt createtable my-table
```


- 

List your tables:


```
cbt ls
```


The command displays output similar to the following:


```
my-table
```


- 

Add one column family named `cf1`:


```
cbt createfamily my-table cf1
```


- 

List your column families:


```
cbt ls my-table
```


The command displays output similar to the following:


```
Family Name GC Policy
----------- ---------
cf1 
```


- 

Write the values `test-value1` and `test-value2` to the row `r1`, using the
column family `cf1` and the column qualifier `c1`:


```
cbt set my-table r1 cf1:c1=test-value1
cbt set my-table r1 cf1:c1=test-value2
```


- 

Use the `cbt read` command to read the data you added to the table:


```
cbt read my-table
```


The shell displays output similar to the following:


```
----------------------------------------
r1
cf1:c1 @ 2023/03/22-06:56:11.323000
"test-value1"
cf1:c1 @ 2023/03/22-06:56:04.361000
"test-value2"
```


Two timestamped values are stored for the same column in row `r1`.

## Clean up

To avoid incurring charges to your Google Cloud Dedicated account for the resources
used in this quickstart, delete the instance. Deleting the `.cbtrc` file leaves
you ready to work on a different project.

- 

Delete the table `my-table`:


```
cbt deletetable my-table
```


- 

Delete the instance:


```
cbt deleteinstance quickstart-instance
```


- 

Delete the `.cbtrc` file:

```
rm ~/.cbtrc
```


- 

Optional: Revoke credentials from the gcloud CLI:


```
gcloud auth revoke
```


## What's next

- Work through a [Bigtable codelab](https://codelabs.developers.google.com/codelabs/cloud-bigtable-intro-java/index.html).

- View the [
`cbt` CLI
reference documentation](/bigtable/docs/cbt-reference).

- See sample source code for a [fraud detection use case](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/main/bigtable/use-cases/fraudDetection).

- Write a Hello World application in [C#](/bigtable/docs/samples-c-sharp-hello), [C++](/bigtable/docs/samples-cpp-hello), [Go](/bigtable/docs/samples-go-hello), [Java](/bigtable/docs/samples-java-hello-world), [Node.js](/bigtable/docs/samples-nodejs-hello), [PHP](/bigtable/docs/samples-php-hello),
[Python](/bigtable/docs/samples-python-hello), [Ruby](/bigtable/docs/samples-ruby-hello), or using the [HBase client for Java](/bigtable/docs/samples-hbase-java-hello).