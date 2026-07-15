# Create and use tables

Source: https://berlin.devsitetest.how/bigquery/docs/tables
Last updated: 2026-07-14

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
- [ Before you begin ](#before_you_begin)

- [ Required roles ](#required_permissions)

- [ Table naming ](#table_naming)
- [ Create tables ](#create-table)

- [ Create an empty table with a schema definition ](#create_an_empty_table_with_a_schema_definition)
- [ Create an empty table without a schema definition ](#create_an_empty_table_without_a_schema_definition)
- [ Create a table from a query result ](#create_a_table_from_a_query_result)
- [ Create a table that references an external data source ](#create_a_table_that_references_an_external_data_source)
- [ Create a table when you load data ](#create_a_table_when_you_load_data)
- [ Create a multimodal table ](#create_a_multimodal_table)

- [ Control access to tables ](#table-acl)
- [ Get information about tables ](#get_information_about_tables)

- [ Required permissions ](#required_permissions)
- [ Get table information ](#get_table_information)
- [ Get table information using INFORMATION_SCHEMA ](#get_table_information_using_information_schema)

- [ Troubleshooting ](#troubleshooting)

- [ List tables in a dataset ](#list_tables_in_a_dataset)

- [ Audit table history ](#audit_table_history)

- [ Required permissions ](#required_permissions_3)
- [ Get audit data ](#get_audit_data)

- [ Table security ](#table_security)
- [ What's next ](#whats_next)
- 









# Create and use tables 





This document describes how to create and use [standard (built-in) tables in
BigQuery](/bigquery/docs/tables-intro#standard-tables). For
information about creating other table types, see the following:

- [Creating partitioned tables](/bigquery/docs/creating-partitioned-tables)

- [Creating and using clustered tables](/bigquery/docs/creating-clustered-tables)

After creating a table, you can do the following:

- Control access to your table data.

- Get information about your tables.

- List the tables in a dataset.

- Get table metadata.

For more information about managing tables including updating table properties,
copying a table, and deleting a table, see [Managing tables](/bigquery/docs/managing-tables).

## Before you begin

Grant Identity and Access Management (IAM) roles that give users the necessary permissions to
perform each task in this document.

### Required roles





















































































































To get the permissions that
you need to create a table,

ask your administrator to grant you the
following IAM roles:













- [BigQuery Job User ](/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
on the project if you're creating a table by loading data or by saving query results to a table.


- [BigQuery Data Editor ](/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
on the dataset where you're creating the table.









For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).








These predefined roles contain

the permissions required to create a table. To see the exact permissions that are
required, expand the **Required permissions** section:





#### Required permissions




The following permissions are required to create a table:






- 
`bigquery.tables.create`

on the dataset where you're creating the table.


- 
`bigquery.tables.getData`

on all tables and views that your query references if you're saving query results as a table.


- 
`bigquery.jobs.create`

on the project if you're creating the table by loading data or by saving query results to a table.


- 
`bigquery.tables.updateData`

on the table if you're appending to or overwriting a table with query results.













You might also be able to get
these permissions
with [custom roles](/iam/docs/creating-custom-roles) or
other [predefined roles](/iam/docs/roles-overview#predefined).









## Table naming

When you create a table in BigQuery, the table name must
be unique per dataset. The table name can:

- Contain characters with a total of up to 1,024 UTF-8 bytes.

- Contain Unicode characters in category L (letter), M (mark), N (number),
Pc (connector, including underscore), Pd (dash), Zs (space). For more
information, see
[General Category](https://wikipedia.org/wiki/Unicode_character_property#General_Category).

The following are all examples of valid table names:
`table 01`, `ग्राहक`, `00_お客様`, `étudiant-01`.

Caveats:

- Table names are case-sensitive by default. `mytable` and `MyTable` can
coexist in the same dataset, unless they are part of a [dataset with
case-sensitivity turned off](/bigquery/docs/reference/standard-sql/data-definition-language#creating_a_case-insensitive_dataset).

- Some table names and table name prefixes are reserved. If
you receive an error saying that your table name or prefix is
reserved, then select a different name and try again.

- 

If you include multiple dot operators (`.`) in a sequence, the duplicate
operators are implicitly stripped.

For example, this:
`project_name....dataset_name..table_name`

Becomes this:
`project_name.dataset_name.table_name`

## Create tables

You can create a table in BigQuery in the following ways:

- Manually by using the Google Cloud Dedicated console or the bq command-line tool
[`bq mk`](/bigquery/docs/reference/bq-cli-reference#bq_mk) command.

- Programmatically by calling the [`tables.insert`](/bigquery/docs/reference/rest/v2/tables/insert)
API method.

- By using the client libraries.

- From query results.

- By defining a table that references an external data source.

- When you load data.

- By using a [`CREATE TABLE`](/bigquery/docs/reference/standard-sql/data-definition-language#creating_a_new_table)
data definition language (DDL) statement.

### Create an empty table with a schema definition

You can create an empty table with a schema definition in the following ways:

- Enter the schema using the Google Cloud Dedicated console.

- Provide the schema inline using the bq command-line tool.

- Submit a JSON schema file using the bq command-line tool.

- Provide the schema in a [table resource](/bigquery/docs/reference/rest/v2/tables#resource:-table)
when calling the APIs [`tables.insert` method](/bigquery/docs/reference/rest/v2/tables/insert).

For more information about specifying a table schema, see [Specifying a schema](/bigquery/docs/schemas).

After the table is created, you can [load data](/bigquery/docs/loading-data)
into it or populate it by [writing query results](/bigquery/docs/writing-results)
to it.

To create an empty table with a schema definition:


[ Console ](#console) [ SQL ](#sql) [ bq ](#bq) [Terraform](#terraform) [ API ](#api) [ C# ](#c) [ Go ](#go) 
More 

[ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 


- 

In the Google Cloud Dedicated console, go to the BigQuery** page.



[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery)

- In the left pane, click explore **Explorer**.

- In the **Explorer** pane, expand your project, click **Datasets**, and then select a dataset.

- In the **Dataset info** section, click add_box **Create table**.

- In the **Create table** pane, specify the following details: 



- In the **Source** section, select **Empty table** in the **Create table from** list.

- In the **Destination** section, specify the following details:


- For **Dataset**, select the dataset in which you want to create the
table.

- In the **Table** field, enter the name of the table that you want to create.

- Verify that the **Table type** field is set to **Native table**.


- In the **Schema** section, enter the [schema](/bigquery/docs/schemas)
definition.




You can enter schema information manually by using one of
the following methods:


- Option 1: Click **Edit as text** and paste the schema in the form of a
JSON array. When you use a JSON array, you generate the schema using the
same process as [creating a JSON schema file](/bigquery/docs/schemas#specifying_a_json_schema_file).
You can view the schema of an existing table in JSON format by entering the following
command:

```
[bq show](/bigquery/docs/reference/bq-cli-reference#bq_show) --format = prettyjson dataset.table 

```



- Option 2: Click add_box 
**Add field** and enter the table schema. Specify each field's **Name**,
[**Type**](/bigquery/docs/schemas#standard_sql_data_types),
and [**Mode**](/bigquery/docs/schemas#modes).







- Optional: Specify **Partition and cluster settings**. For more information, see
[Creating partitioned tables](/bigquery/docs/creating-partitioned-tables) and
[Creating and using clustered tables](/bigquery/docs/creating-clustered-tables).





- Optional: In the **Advanced options** section, if you want to use a
customer-managed encryption key, then select the **Use a customer-managed
encryption key (CMEK)** option. By default, BigQuery
[encrypts customer content stored at rest](/docs/security/encryption/default-encryption)
by using a Google Cloud-powered encryption key.

- Click **Create table**.




The following example creates a table named `newtable` that expires on
January 1, 2023:

- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the query editor, enter the following statement:


```
CREATE TABLE mydataset . newtable ( 
x INT64 OPTIONS ( description = 'An optional INTEGER field' ), 
y STRUCT a ARRAY STRING > OPTIONS ( description = 'A repeated STRING field' ), 
b BOOL 
>
) OPTIONS ( 
expiration_timestamp = TIMESTAMP '2023-01-01 00:00:00 UTC' , 
description = 'a table that expires in 2023' , 
labels = [ ( 'org_unit' , 'development' ) ] ); 
```


- 

Click play_circle **Run**.

For more information about how to run queries, see [Run an interactive query](/bigquery/docs/running-queries#queries).



- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

Use the [`bq mk` command](/bigquery/docs/reference/bq-cli-reference#bq_mk)
with the `--table` or `-t` flag. You can supply table
schema information inline or with a JSON schema file. For a full list of
parameters, see the
[`bq mk --table` reference](/bigquery/docs/reference/bq-cli-reference#mk-table).
Some optional parameters include:

- `--expiration`

- `--description`

- `--time_partitioning_field`

- `--time_partitioning_type`

- `--range_partitioning`

- `--clustering_fields`

- `--destination_kms_key`

- `--label`

`--time_partitioning_field`, `--time_partitioning_type`,
`--range_partitioning`, `--clustering_fields`, and `--destination_kms_key`
are not demonstrated here. Refer to the following links for more information
on these optional parameters:

- For more information about `--time_partitioning_field`,
`--time_partitioning_type`, and `--range_partitioning` see
[partitioned tables](/bigquery/docs/creating-partitioned-tables).

- For more information about `--clustering_fields`, see
[clustered tables](/bigquery/docs/creating-clustered-tables).

- For more information about `--destination_kms_key`, see
[customer-managed encryption keys](/bigquery/docs/customer-managed-encryption).

If you are creating a table in a project other than your default project,
add the project ID to the dataset in the following format:
`project_id:dataset`.

To create an empty table in an existing dataset with a schema definition,
enter the following:


```
[bq mk](/bigquery/docs/reference/bq-cli-reference#bq_mk) \ 
--table \ 
--expiration = ** integer \ 
--description = description \ 
--label = key_1:value_1 \ 
--label = key_2:value_2 \ 
--add_tags = key_3:value_3 [ ,... ] \ 
project_id : dataset . table \ 
schema 
```


Replace the following:

- integer is the default lifetime (in seconds) for the table. The
minimum value is 3600 seconds (one hour). The expiration time
evaluates to the current UTC time plus the integer value. If you set the
expiration time when you create a table, the dataset's default table
expiration setting is ignored.

- description is a description of the table in quotes.

- key_1 : value_1 and
key_2 : value_2 are key-value pairs
that specify [labels](/bigquery/docs/labels).

- key_3 : value_3 are key-value pairs
that specify [tags](/bigquery/docs/tags). Add multiple tags under the
same flag with commas between key:value pairs.

- project_id is your project ID.

- dataset is a dataset in your project.

- table is the name of the table you're creating.

- schema is an inline schema definition in the format
field:data_type,field:data_type or the path to the JSON schema
file on your local machine.

When you specify the schema on the command line, you cannot include a
`RECORD`
([`STRUCT`](/bigquery/docs/reference/standard-sql/data-types#struct_type))
type, you cannot include a column description, and you cannot specify the
column mode. All modes default to `NULLABLE`. To include descriptions,
modes, and `RECORD` types,
[supply a JSON schema file](/bigquery/docs/schemas#specifying_a_json_schema_file)
instead.

Examples:

Enter the following command to create a table using an inline schema
definition. This command creates a table named `mytable` in `mydataset` in
your default project. The table expiration is set to 3600 seconds (1 hour),
the description is set to `This is my table`, and the label is set to
`organization:development`. The command uses the `-t` shortcut instead of
`--table`. The schema is specified inline as:
`qtr:STRING,sales:FLOAT,year:STRING`.


```
[bq mk](/bigquery/docs/reference/bq-cli-reference#bq_mk) \ 
-t \ 
--expiration 3600 \ 
--description "This is my table" \ 
--label organization:development \ 
mydataset.mytable \ 
qtr:STRING,sales:FLOAT,year:STRING
```


Enter the following command to create a table using a JSON schema file. This
command creates a table named `mytable` in `mydataset` in your default
project. The table expiration is set to 3600 seconds (1 hour), the
description is set to `This is my table`, and the label is set to
`organization:development`. The path to the schema file is
`/tmp/myschema.json`.


```
[bq mk](/bigquery/docs/reference/bq-cli-reference#bq_mk) \ 
--table \ 
--expiration 3600 \ 
--description "This is my table" \ 
--label organization:development \ 
mydataset.mytable \ 
/tmp/myschema.json
```


Enter the following command to create a table using a JSON schema file.
This command creates a table named `mytable` in `mydataset` in
`myotherproject`. The table expiration is set to 3600 seconds (1 hour), the
description is set to `This is my table`, and the label is set to
`organization:development`. The path to the schema file is
`/tmp/myschema.json`.


```
[bq mk](/bigquery/docs/reference/bq-cli-reference#bq_mk) \ 
--table \ 
--expiration 3600 \ 
--description "This is my table" \ 
--label organization:development \ 
myotherproject:mydataset.mytable \ 
/tmp/myschema.json
```


After the table is created, you can [update](/bigquery/docs/managing-tables)
the table's expiration, description, and labels. You can also
[modify the schema definition](/bigquery/docs/managing-table-schemas).




Use the
[`google_bigquery_table`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_table)
resource.

To authenticate to BigQuery, set up Application Default
Credentials. For more information, see
[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).

**Create a table**

The following example creates a table named `mytable`:




















```
resource "google_bigquery_dataset" "default" {
dataset_id = "mydataset"
default_partition_expiration_ms = 2592000000 # 30 days
default_table_expiration_ms = 31536000000 # 365 days
description = "dataset description"
location = "US"
max_time_travel_hours = 96 # 4 days

labels = {
billing_group = "accounting",
pii = "sensitive"
}
}

resource "google_bigquery_table" "default" {
dataset_id = google_bigquery_dataset.default.dataset_id
table_id = "mytable"

schema = 


**Create a table and grant access to it**

The following example creates a table named `mytable`, then uses the
[`google_bigquery_table_iam_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_table_iam#google_bigquery_table_iam_policy) resource to grant
access to it. Take this step only if you want to grant access
to the table to principals who don't have access to the dataset in which
the table resides.




















```
resource "google_bigquery_dataset" "default" {
dataset_id = "mydataset"
default_partition_expiration_ms = 2592000000 # 30 days
default_table_expiration_ms = 31536000000 # 365 days
description = "dataset description"
location = "US"
max_time_travel_hours = 96 # 4 days

labels = {
billing_group = "accounting",
pii = "sensitive"
}
}

resource "google_bigquery_table" "default" {
dataset_id = google_bigquery_dataset.default.dataset_id
table_id = "mytable"

schema = 


**Create a table with a customer-managed encryption key**

The following example creates a table named `mytable`, and also uses the
[`google_kms_crypto_key`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_crypto_key)
and
[`google_kms_key_ring`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_key_ring)
resources to specify a
[Cloud Key Management Service key](/bigquery/docs/customer-managed-encryption) for the
table. You must
[enable the Cloud Key Management Service API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.berlin-build0.goog/) before running this example.




















```
resource "google_bigquery_dataset" "default" {
dataset_id = "mydataset"
default_partition_expiration_ms = 2592000000 # 30 days
default_table_expiration_ms = 31536000000 # 365 days
description = "dataset description"
location = "US"
max_time_travel_hours = 96 # 4 days

labels = {
billing_group = "accounting",
pii = "sensitive"
}
}

resource "google_bigquery_table" "default" {
dataset_id = google_bigquery_dataset.default.dataset_id
table_id = "mytable"

schema = 


To apply your Terraform configuration in a Google Cloud Dedicated project, complete the steps in the
following sections.

## Prepare Cloud Shell


- Launch [Cloud Shell](https://shell.cloud.google.com/).

- 


Set the default Google Cloud Dedicated project
where you want to apply your Terraform configurations.




You only need to run this command once per project, and you can run it in any directory.


```
export GOOGLE_CLOUD_PROJECT= PROJECT_ID 
```



Environment variables are overridden if you set explicit values in the Terraform
configuration file.



## Prepare the directory

Each Terraform configuration file must have its own directory (also
called a *root module*).


- 
In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new
file within that directory. The filename must have the
`.tf` extension—for example `main.tf`. In this
tutorial, the file is referred to as `main.tf`.

```
mkdir DIRECTORY && cd DIRECTORY && touch main.tf
```



- 


If you are following a tutorial, you can copy the sample code in each section or step.



Copy the sample code into the newly created `main.tf`.



Optionally, copy the code from GitHub. This is recommended
when the Terraform snippet is part of an end-to-end solution.




- Review and modify the sample parameters to apply to your environment.

- Save your changes.

- 
Initialize Terraform. You only need to do this once per directory.

```
terraform init
```



Optionally, to use the latest Google provider version, include the `-upgrade`
option:



```
terraform init -upgrade
```



## Apply the changes


- 
Review the configuration and verify that the resources that Terraform is going to create or
update match your expectations:

```
terraform plan
```



Make corrections to the configuration as necessary.



- 
Apply the Terraform configuration by running the following command and entering `yes`
at the prompt:

```
terraform apply
```



Wait until Terraform displays the "Apply complete!" message.



- [Open your Google Cloud Dedicated project](https://console.cloud.berlin-build0.goog/) to view
the results. In the Google Cloud Dedicated console, navigate to your resources in the UI to make sure
that Terraform has created or updated them.





Call the [`tables.insert`](/bigquery/docs/reference/rest/v2/tables/insert)
method with a defined [table resource](/bigquery/docs/reference/rest/v2/tables).

































Before trying this sample, follow the C# setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery C# API
reference documentation](/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
using [ Google.Cloud.BigQuery.V2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html) ; 

public class BigQueryCreateTable 
{ 
public BigQueryTable CreateTable ( 
string projectId = "your-project-id" , 
string datasetId = "your_dataset_id" 
) 
{ 
[ BigQueryClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) client = [ BigQueryClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_) ( projectId ); 
var dataset = client . [ GetDataset ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_GetDataset_Google_Apis_Bigquery_v2_Data_DatasetReference_Google_Cloud_BigQuery_V2_GetDatasetOptions_) ( datasetId ); 
// Create schema for new table. 
var schema = new [ TableSchemaBuilder ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.TableSchemaBuilder.html)
{ 
{ "full_name" , [ BigQueryDbType ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryDbType.html) . [ String ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryDbType.html#Google_Cloud_BigQuery_V2_BigQueryDbType_String) }, 
{ "age" , [ BigQueryDbType ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryDbType.html) . [ Int64 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryDbType.html#Google_Cloud_BigQuery_V2_BigQueryDbType_Int64) } 
}. Build (); 
// Create the table 
return dataset . CreateTable ( tableId : "your_table_id" , schema : schema ); 
} 
} 
```

















































Before trying this sample, follow the Go setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Go API
reference documentation](https://godoc.org/cloud.google.com/go/bigquery).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import ( 
"context" 
"fmt" 
"time" 

"cloud.google.com/go/bigquery" 
) 

// createTableExplicitSchema demonstrates creating a new BigQuery table and specifying a schema. 
func createTableExplicitSchema ( projectID , datasetID , tableID string ) error { 
// projectID := "my-project-id" 
// datasetID := "mydatasetid" 
// tableID := "mytableid" 
ctx := context . Background () 

client , err := bigquery . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "bigquery.NewClient: %v" , err ) 
} 
defer client . Close () 

sampleSchema := bigquery . [ Schema ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Schema) { 
{ Name : "full_name" , Type : bigquery . [ StringFieldType ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType) }, 
{ Name : "age" , Type : bigquery . [ IntegerFieldType ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType) }, 
} 

metaData := & bigquery . [ TableMetadata ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_TableMetadata) { 
Schema : sampleSchema , 
ExpirationTime : time . Now (). AddDate ( 1 , 0 , 0 ), // Table will be automatically deleted in 1 year. 
} 
tableRef := client . Dataset ( datasetID ). Table ( tableID ) 
if err := tableRef . Create ( ctx , metaData ); err != nil { 
return err 
} 
return nil 
} 
```


















































Before trying this sample, follow the Java setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Java API
reference documentation](/java/docs/reference/google-cloud-bigquery/latest/overview).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import com.google.cloud.bigquery.[BigQuery](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) ; 
import com.google.cloud.bigquery.[BigQueryException](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) ; 
import com.google.cloud.bigquery.[BigQueryOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) ; 
import com.google.cloud.bigquery.[Field](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Field.html) ; 
import com.google.cloud.bigquery.[Schema](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html) ; 
import com.google.cloud.bigquery.[StandardSQLTypeName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html) ; 
import com.google.cloud.bigquery.[StandardTableDefinition](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardTableDefinition.html) ; 
import com.google.cloud.bigquery.[TableDefinition](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDefinition.html) ; 
import com.google.cloud.bigquery.[TableId](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) ; 
import com.google.cloud.bigquery.[TableInfo](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html) ; 

public class CreateTable { 

public static void runCreateTable () { 
// TODO(developer): Replace these variables before running the sample. 
String datasetName = "MY_DATASET_NAME" ; 
String tableName = "MY_TABLE_NAME" ; 
[ Schema ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html) schema = 
[ Schema ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html) . of ( 
[ Field ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Field.html) . of ( "stringField" , [ StandardSQLTypeName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html) . STRING ), 
[ Field ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Field.html) . of ( "booleanField" , [ StandardSQLTypeName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html) . BOOL )); 
createTable ( datasetName , tableName , schema ); 
} 

public static void createTable ( String datasetName , String tableName , [ Schema ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html) schema ) { 
try { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
[ BigQuery ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [ BigQueryOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) . getDefaultInstance (). getService (); 

[ TableId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [ TableId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) . of ( datasetName , tableName ); 
[ TableDefinition ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDefinition.html) tableDefinition = [ StandardTableDefinition ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardTableDefinition.html) . of ( schema ); 
[ TableInfo ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html) tableInfo = [ TableInfo ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html) . newBuilder ( tableId , tableDefinition ). build (); 

bigquery . [ create ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____) ( tableInfo ); 
System . out . println ( "Table created successfully" ); 
} catch ( [ BigQueryException ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e ) { 
System . out . println ( "Table was not created. \n" + e . toString ()); 
} 
} 
} 
```


















































Before trying this sample, follow the Node.js setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Node.js API
reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
// Import the Google Cloud client library and create a client 
const { BigQuery } = require ( '[@google-cloud/bigquery](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/overview.html)' ); 
const bigquery = new [ BigQuery ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html) (); 

async function createTable () { 
// Creates a new table named "my_table" in "my_dataset". 

/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// const datasetId = "my_dataset"; 
// const tableId = "my_table"; 
// const schema = 'Name:string, Age:integer, Weight:float, IsMagic:boolean'; 

// For all options, see https://cloud.google.com/bigquery/docs/reference/v2/tables#resource 
const options = { 
schema : schema , 
location : 'US' , 
}; 

// Create a new table in the dataset 
const [ table ] = await bigquery 
. dataset ( datasetId ) 
. [ createTable ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/dataset.html) ( tableId , options ); 

console . log ( `Table ${ table . id } created.` ); 
} 
```

















































Before trying this sample, follow the PHP setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery PHP API
reference documentation](/php/docs/reference/cloud-bigquery/latest/BigQueryClient).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
use Google\Cloud\BigQuery\BigQueryClient; 

/** Uncomment and populate these variables in your code */ 
// $projectId = 'The Google project ID'; 
// $datasetId = 'The BigQuery dataset ID'; 
// $tableId = 'The BigQuery table ID'; 
// $fields = [ 
// [ 
// 'name' => 'field1', 
// 'type' => 'string', 
// 'mode' => 'required' 
// ], 
// [ 
// 'name' => 'field2', 
// 'type' => 'integer' 
// ], 
//]; 

$bigQuery = new BigQueryClient([ 
'projectId' => $projectId, 
]); 
$dataset = $bigQuery->dataset($datasetId); 
$schema = ['fields' => $fields]; 
$table = $dataset->createTable($tableId, ['schema' => $schema]); 
printf('Created table %s' . PHP_EOL, $tableId); 
```


















































Before trying this sample, follow the Python setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Python API
reference documentation](/python/docs/reference/bigquery/latest).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
from google.cloud import [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest)

# Construct a BigQuery client object. 
client = [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html) () 

# TODO(developer): Set table_id to the ID of the table to create. 
# table_id = "your-project.your_dataset.your_table_name" 

schema = [ 
[ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ SchemaField ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html) ( "full_name" , "STRING" , mode = "REQUIRED" ), 
[ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ SchemaField ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html) ( "age" , "INTEGER" , mode = "REQUIRED" ), 
] 

table = [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ Table ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html) ( table_id , schema = schema ) 
table = client . [ create_table ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_table) ( table ) # Make an API request. 
print ( 
"Created table {} . {} . {} " . format ( table . project , table . dataset_id , table . table_id ) 
) 
```


















































Before trying this sample, follow the Ruby setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Ruby API
reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
require "google/cloud/bigquery" 

def create_table dataset_id = "my_dataset" 
bigquery = Google :: Cloud :: [ Bigquery ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Cloud-Bigquery.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html)
dataset = bigquery . dataset dataset_id 
table_id = "my_table" 

table = dataset . create_table table_id do | updater | 
updater . string "full_name" , mode : :required 
updater . integer "age" , mode : :required 
end 

puts "Created table: #{ table_id } " 
end 
```




















### Create an empty table without a schema definition


























[ Java ](#java) 
More 












Before trying this sample, follow the Java setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Java API
reference documentation](/java/docs/reference/google-cloud-bigquery/latest/overview).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import com.google.cloud.bigquery.[BigQuery](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) ; 
import com.google.cloud.bigquery.[BigQueryException](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) ; 
import com.google.cloud.bigquery.[BigQueryOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) ; 
import com.google.cloud.bigquery.[Schema](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html) ; 
import com.google.cloud.bigquery.[StandardTableDefinition](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardTableDefinition.html) ; 
import com.google.cloud.bigquery.[TableDefinition](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDefinition.html) ; 
import com.google.cloud.bigquery.[TableId](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) ; 
import com.google.cloud.bigquery.[TableInfo](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html) ; 

// Sample to create a table without schema 
public class CreateTableWithoutSchema { 

public static void main ( String [] args ) { 
// TODO(developer): Replace these variables before running the sample. 
String datasetName = "MY_DATASET_NAME" ; 
String tableName = "MY_TABLE_NAME" ; 
createTableWithoutSchema ( datasetName , tableName ); 
} 

public static void createTableWithoutSchema ( String datasetName , String tableName ) { 
try { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
[ BigQuery ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [ BigQueryOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) . getDefaultInstance (). getService (); 

[ TableId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [ TableId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) . of ( datasetName , tableName ); 
[ TableDefinition ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDefinition.html) tableDefinition = [ StandardTableDefinition ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardTableDefinition.html) . of ( [ Schema ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html) . of ()); 
[ TableInfo ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html) tableInfo = [ TableInfo ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html) . newBuilder ( tableId , tableDefinition ). build (); 

bigquery . [ create ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____) ( tableInfo ); 
System . out . println ( "Table created successfully" ); 
} catch ( [ BigQueryException ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e ) { 
System . out . println ( "Table was not created. \n" + e . toString ()); 
} 
} 
} 
```




















### Create a table from a query result

To create a table from a query result, write the results to a destination table.


[ Console ](#console) [ SQL ](#sql) [ bq ](#bq) [ API ](#api) [ Go ](#go) [Java](#java) [ Node.js ](#node.js) [Python](#python) 
More 


















- 

Open the BigQuery page in the Google Cloud Dedicated console.

[Go to the BigQuery page](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the left pane, click explore **Explorer**:



If you don't see the left pane, click last_page **Expand left pane** to open the pane.

- 

In the **Explorer** pane, expand your project, click **Datasets**, and
then select a dataset.

- 

In the query editor, enter a valid SQL query.

- 

Click **Edit** > **Query settings**.



- 

Select the **Set a destination table for query results** option.



- 

In the **Destination** section, select the **Dataset** in which you want
to create the table, and then choose a **Table Id**.

- 

In the **Destination table write preference** section, choose one of
the following:

- **Write if empty** — Writes the query results to the table only
if the table is empty.

- **Append to table** — Appends the query results to an existing
table.

- **Overwrite table** — Overwrites an existing table with the same
name using the query results.

- 

Optional: For **Data location**, choose
your [location](/bigquery/docs/locations).

- 

To update the query settings, click **Save**.

- 

Click **Run**. This creates a query job that writes the
query results to the table you specified.

Alternatively, if you forget to specify a destination table before running
your query, you can copy the cached results table to a permanent table by
clicking the [**Save Results**](#save-query-results)
button above the editor.



















The following example uses the
[`CREATE TABLE` statement](/bigquery/docs/reference/standard-sql/data-definition-language#create_table_statement)
to create the `trips` table from data in the public
`bikeshare_trips` table:

- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the query editor, enter the following statement:


```
CREATE TABLE mydataset . trips AS ( 
SELECT 
bike_id , 
start_time , 
duration_minutes 
FROM 
bigquery - public - data . austin_bikeshare . bikeshare_trips 
); 
```


- 

Click play_circle **Run**.

For more information about how to run queries, see [Run an interactive query](/bigquery/docs/running-queries#queries).

For more information, see
[Creating a new table from an existing table](/bigquery/docs/reference/standard-sql/data-definition-language#creating_a_new_table_from_an_existing_table).

















- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

Enter the [`bq query`](/bigquery/docs/reference/bq-cli-reference#bq_query)
command and specify the `--destination_table` flag to
create a permanent table based on the query results. Specify the
`use_legacy_sql=false` flag to use GoogleSQL syntax. To write the query
results to a table that is not in your default project, add the project ID
to the dataset name in the following format:
` project_id : dataset `.

Optional: Supply the `--location` flag and set the value to your
[location](/bigquery/docs/dataset-locations).

To control the write disposition for an existing destination table, specify
one of the following optional flags:

- `--append_table`: If the destination table exists, the query results are
appended to it.

- 

`--replace`: If the destination table exists, it is overwritten with the
query results.


```
bq --location = location query \ 
--destination_table project_id : dataset . table \ 
--use_legacy_sql = false ' query ' 
```


Replace the following:

- 

` location ` is the name of the location used to
process the query. The `--location` flag is optional. For example, if you
are using BigQuery in the Tokyo region, you can set the flag's
value to `asia-northeast1`. You can set a default value for the location by
using the
[`.bigqueryrc` file](/bigquery/docs/bq-command-line-tool#setting_default_values_for_command-line_flags).

- 

` project_id ` is your project ID.

- 

` dataset ` is the name of the dataset that contains
the table to which you are writing the query results.

- 

` table ` is the name of the table to which you're
writing the query results.

- 

` query ` is a query in GoogleSQL syntax.

If no write disposition flag is specified, the default behavior is to
write the results to the table only if it is empty. If the table exists
and it is not empty, the following error is returned:
`BigQuery error in query operation: Error processing job
project_id :bqjob_123abc456789_00000e1234f_1: Already
Exists: Table project_id:dataset.table `.

Examples:

Enter the following command to write query results to a destination table
named `mytable` in `mydataset`. The dataset is in your default project.
Since no write disposition flag is specified in the command, the table must
be new or empty. Otherwise, an `Already exists` error is returned. The query
retrieves data from the [USA Name Data public dataset](https://console.cloud.berlin-build0.goog/marketplace/product/social-security-administration/us-names).


```
[bq query](/bigquery/docs/reference/bq-cli-reference#bq_query) \ 
--destination_table mydataset.mytable \ 
--use_legacy_sql = false \ 
'SELECT 
name, 
number 
FROM 
`bigquery-public-data`.usa_names.usa_1910_current 
WHERE 
gender = "M" 
ORDER BY 
number DESC' 
```


Enter the following command to use query results to overwrite a destination
table named `mytable` in `mydataset`. The dataset is in your default
project. The command uses the `--replace` flag to overwrite the destination
table.


```
[bq query](/bigquery/docs/reference/bq-cli-reference#bq_query) \ 
--destination_table mydataset.mytable \ 
--replace \ 
--use_legacy_sql = false \ 
'SELECT 
name, 
number 
FROM 
`bigquery-public-data`.usa_names.usa_1910_current 
WHERE 
gender = "M" 
ORDER BY 
number DESC' 
```


Enter the following command to append query results to a destination table
named `mytable` in `mydataset`. The dataset is in `my-other-project`, not
your default project. The command uses the `--append_table` flag to append
the query results to the destination table.


```
[bq query](/bigquery/docs/reference/bq-cli-reference#bq_query) \ 
--append_table \ 
--use_legacy_sql = false \ 
--destination_table my-other-project:mydataset.mytable \ 
'SELECT 
name, 
number 
FROM 
`bigquery-public-data`.usa_names.usa_1910_current 
WHERE 
gender = "M" 
ORDER BY 
number DESC' 
```


The output for each of these examples looks like the following. For
readability, some output is truncated.


```
Waiting on bqjob_r123abc456_000001234567_1 ... (2s) Current status: DONE
+---------+--------+
| name | number |
+---------+--------+
| Robert | 10021 |
| John | 9636 |
| Robert | 9297 |
| ... |
+---------+--------+
```


































To save query results to a permanent table, call the
[`jobs.insert`](/bigquery/docs/reference/rest/v2/jobs/insert) method,
configure a `query` job, and include a value for the `destinationTable`
property. To control the write disposition for an existing destination
table, configure the `writeDisposition` property.

To control the processing location for the query job, specify the `location`
property in the `jobReference` section of the [job resource](/bigquery/docs/reference/rest/v2/jobs).








































Before trying this sample, follow the Go setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Go API
reference documentation](https://godoc.org/cloud.google.com/go/bigquery).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.



























```
import ( 
"context" 
"fmt" 
"io" 

"cloud.google.com/go/bigquery" 
"google.golang.org/api/iterator" 
) 

// queryWithDestination demonstrates saving the results of a query to a specific table by setting the destination 
// via the API properties. 
func queryWithDestination ( w io . Writer , projectID , destDatasetID , destTableID string ) error { 
// projectID := "my-project-id" 
// datasetID := "mydataset" 
// tableID := "mytable" 
ctx := context . Background () 
client , err := bigquery . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "bigquery.NewClient: %v" , err ) 
} 
defer client . Close () 

q := client . Query ( "SELECT 17 as my_col" ) 
q . [ Location ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Job_Location) = "US" // Location must match the dataset(s) referenced in query. 
q . [ QueryConfig ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_QueryConfig) . Dst = client . Dataset ( destDatasetID ). Table ( destTableID ) 
// Run the query and print results when the query job is completed. 
job , err := q . Run ( ctx ) 
if err != nil { 
return err 
} 
status , err := job . Wait ( ctx ) 
if err != nil { 
return err 
} 
if err := status . [ Err ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_JobStatus_Err) (); err != nil { 
return err 
} 
it , err := job . Read ( ctx ) 
for { 
var row [] bigquery . [ Value ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Value)
err := it . Next ( & row ) 
if err == iterator . Done { 
break 
} 
if err != nil { 
return err 
} 
fmt . Fprintln ( w , row ) 
} 
return nil 
} 
```










































Before trying this sample, follow the Java setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Java API
reference documentation](/java/docs/reference/google-cloud-bigquery/latest/overview).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






To save query results to a permanent table, set the [destination
table](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.Builder#com_google_cloud_bigquery_QueryJobConfiguration_Builder_setDestinationTable_com_google_cloud_bigquery_TableId_)
to the desired
[TableId](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId)
in a
[QueryJobConfiguration](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration).























```
import com.google.cloud.bigquery.[BigQuery](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) ; 
import com.google.cloud.bigquery.[BigQueryException](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) ; 
import com.google.cloud.bigquery.[BigQueryOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) ; 
import com.google.cloud.bigquery.[QueryJobConfiguration](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) ; 
import com.google.cloud.bigquery.[TableId](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) ; 

public class SaveQueryToTable { 

public static void runSaveQueryToTable () { 
// TODO(developer): Replace these variables before running the sample. 
String query = "SELECT corpus FROM `bigquery-public-data.samples.shakespeare` GROUP BY corpus;" ; 
String destinationTable = "MY_TABLE" ; 
String destinationDataset = "MY_DATASET" ; 

saveQueryToTable ( destinationDataset , destinationTable , query ); 
} 

public static void saveQueryToTable ( 
String destinationDataset , String destinationTableId , String query ) { 
try { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
[ BigQuery ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [ BigQueryOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) . getDefaultInstance (). getService (); 

// Identify the destination table 
[ TableId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) destinationTable = [ TableId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) . of ( destinationDataset , destinationTableId ); 

// Build the query job 
[ QueryJobConfiguration ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig = 
[ QueryJobConfiguration ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) . newBuilder ( query ). setDestinationTable ( destinationTable ). build (); 

// Execute the query. 
bigquery . [ query ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____) ( queryConfig ); 

// The results are now saved in the destination table. 

System . out . println ( "Saved query ran successfully" ); 
} catch ( [ BigQueryException ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e ) { 
System . out . println ( "Saved query did not run \n" + e . toString ()); 
} 
} 
} 
```


















































Before trying this sample, follow the Node.js setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Node.js API
reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
// Import the Google Cloud client library 
const { BigQuery } = require ( '[@google-cloud/bigquery](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/overview.html)' ); 
const bigquery = new [ BigQuery ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html) (); 

async function queryDestinationTable () { 
// Queries the U.S. given names dataset for the state of Texas 
// and saves results to permanent table. 

/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// const datasetId = 'my_dataset'; 
// const tableId = 'my_table'; 

// Create destination table reference 
const dataset = bigquery . dataset ( datasetId ); 
const destinationTable = dataset . table ( tableId ); 

const query = `SELECT name 
FROM \`bigquery-public-data.usa_names.usa_1910_2013\` 
WHERE state = 'TX' 
LIMIT 100` ; 

// For all options, see https://cloud.google.com/bigquery/docs/reference/v2/tables#resource 
const options = { 
query : query , 
// Location must match that of the dataset(s) referenced in the query. 
location : 'US' , 
destination : destinationTable , 
}; 

// Run the query as a job 
const [ job ] = await bigquery . createQueryJob ( options ); 

console . log ( `Job ${ [ job ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html) . id } started.` ); 
console . log ( `Query results loaded to table ${ destinationTable . id } ` ); 
} 
```


















































Before trying this sample, follow the Python setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Python API
reference documentation](/python/docs/reference/bigquery/latest).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.





To save query results to a permanent table, create a
[QueryJobConfig](/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJob#google_cloud_bigquery_job_QueryJob)
and set the
[destination](/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJob#google_cloud_bigquery_job_QueryJob_destination)
to the desired
[TableReference](/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.TableReference).
Pass the job configuration to the [query
method](/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client#google_cloud_bigquery_client_Client_query).


























```
from google.cloud import [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest)

# Construct a BigQuery client object. 
client = [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html) () 

# TODO(developer): Set table_id to the ID of the destination table. 
# table_id = "your-project.your_dataset.your_table_name" 

job_config = [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ QueryJobConfig ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig.html) ( destination = table_id ) 

sql = """ 
SELECT corpus 
FROM `bigquery-public-data.samples.shakespeare` 
GROUP BY corpus; 
""" 

# Start the query, passing in the extra configuration. 
query_job = client . [ query ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html) ( sql , job_config = job_config ) # Make an API request. 
[ query_job ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job) . result () # Wait for the job to complete. 

print ( "Query results loaded to the table {} " . format ( table_id )) 
```





















### Create a table that references an external data source

An external data source is a data source that you can query directly from
BigQuery, even though the data is not stored in
BigQuery storage. For example, you might have data in a
different Google Cloud Dedicated in Germany database, in files in Cloud Storage, or in a
different cloud product altogether that you would like to analyze in
BigQuery, but that you aren't prepared to migrate.

For more information, see
[Introduction to external data sources](/bigquery/external-data-sources).

### Create a table when you load data

When you load data into BigQuery, you can load data into a new
table or partition, you can append data to an existing table or partition, or
you can overwrite a table or partition. You don't need to create an empty
table before loading data into it. You can create the new table and load your
data at the same time.

When you load data into BigQuery, you can supply the table
or partition schema, or for supported data formats, you can use schema
[auto-detection](/bigquery/docs/schema-detect).

For more information about loading data, see
[Introduction to loading data into BigQuery](/bigquery/docs/loading-data).

### Create a multimodal table

You can create a table with one or more
[`ObjectRef`](/bigquery/docs/objectref-columns) columns in order to store metadata
about unstructured data that is related to the other structured data in the
table. For example, in a products table, you could create an `ObjectRef` column
to store product image information along with the other product data. The
unstructured data itself is stored in Cloud Storage, and is made available
in BigQuery by using an
[object table](/bigquery/docs/object-table-introduction).

To learn how to create a multimodal table, see
[Analyze multimodal data with SQL and BigQuery DataFrames](/bigquery/docs/multimodal-data-sql-tutorial).

## Control access to tables

To configure access to tables and views, you can grant an
IAM role to an entity at the following levels, which are listed
in
order of the range of resources allowed (largest to smallest):

- A high level in the
[Google Cloud Dedicated in Germany resource hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy)
such as the project, folder, or organization level

- The dataset level

- The table or view level

You can also restrict data access within tables, by using the following
methods:

- [Column-level security](/bigquery/docs/column-level-security-intro)

- [Column data masking](/bigquery/docs/column-data-masking-intro)

- [Row-level security](/bigquery/docs/row-level-security-intro)

Access to any resource protected by IAM is additive. For
example, if an entity does not have access at a high level such as a project,
you can grant the entity access at the dataset level, and the entity then has
access to the tables and views in the dataset. Similarly, if the entity does
not have access at the high level or the dataset level, you can grant the
entity access at the table or view level.

Granting IAM roles at a higher level in the [Google Cloud Dedicated in Germany
resource hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy)
such as the project, folder, or organization level gives the entity access to a
broad set of resources. For example, granting a role to an entity at the project
level gives that entity permissions that apply to all datasets throughout the
project.

Granting a role at the dataset level specifies the operations an entity is
allowed to perform on tables and views in that specific dataset, even if the
entity does not have access at a higher level. For information on configuring
dataset-level access controls, see
[Controlling access to datasets](/bigquery/docs/dataset-access-controls).

Granting a role at the table or view level specifies the operations an entity is
allowed to perform on specific tables and views, even if the entity does not
have access at a higher level. For information on configuring table-level access
controls, see
[Controlling access to tables and views](/bigquery/docs/table-access-controls).

You can also create [IAM custom roles](/iam/docs/creating-custom-roles).
If you create a custom role, the permissions you grant depend on the specific
operations you want the entity to be able to perform.

You can't set a "deny" permission on any resource protected by
IAM.

For more information about roles and permissions, see [Understanding roles](/iam/docs/understanding-roles)
in the IAM documentation and the BigQuery
[IAM roles and permissions](/bigquery/docs/access-control).

## Get information about tables

You can get information or metadata about tables in the following ways:

- Using the Google Cloud Dedicated console.

- Using the bq command-line tool
[`bq show`](/bigquery/docs/reference/bq-cli-reference#bq_show) command.

- Calling the [`tables.get`](/bigquery/docs/reference/rest/v2/tables/get)
API method.

- Using the client libraries.

- Querying the [`INFORMATION_SCHEMA.VIEWS`](/bigquery/docs/information-schema-views) view.

### Required permissions

At a minimum, to get information about tables, you must be granted
`bigquery.tables.get` permissions. The following predefined IAM
roles include `bigquery.tables.get` permissions:

- `bigquery.metadataViewer`

- `bigquery.dataViewer`

- `bigquery.dataOwner`

- `bigquery.dataEditor`

- `bigquery.admin`

In addition, if a user has `bigquery.datasets.create` permissions, when that
user creates a dataset, they are granted `bigquery.dataOwner` access to it.
`bigquery.dataOwner` access gives the user the ability to retrieve table
metadata.

For more information on IAM roles and permissions in
BigQuery, see [Access control](/bigquery/access-control).

### Get table information

To get information about tables:


[ Console ](#console) [ bq ](#bq) [ API ](#api) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) 
More 




- 

In the navigation panel, in the **Resources** section, expand your
project, and then select a dataset.

- 

Click the dataset name to expand it. The tables and views in the dataset
appear.

- 

Click the table name.

- 

In the **Details** panel, click **Details** to display the table's
description and table information.

- 

Optionally, switch to the **Schema** tab to view the table's schema
definition.




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

Issue the [`bq show`](/bigquery/docs/reference/bq-cli-reference#bq_show)
command to display all table information. Use the
`--schema` flag to display only table schema information. The `--format`
flag can be used to control the output.

If you are getting information about a table in a project other than
your default project, add the project ID to the dataset in the following
format: `project_id:dataset`.


```
[bq show](/bigquery/docs/reference/bq-cli-reference#bq_show) \ 
--schema \ 
--format = prettyjson \ 
project_id : dataset.table 
```


Where:

- project_id is your project ID.

- dataset is the name of the dataset.

- table is the name of the table.

Examples:

Enter the following command to display all information about `mytable` in
`mydataset`. `mydataset` is in your default project.


```
[bq show](/bigquery/docs/reference/bq-cli-reference#bq_show) --format = prettyjson mydataset.mytable
```


Enter the following command to display all information about `mytable` in
`mydataset`. `mydataset` is in `myotherproject`, not your default project.


```
[bq show](/bigquery/docs/reference/bq-cli-reference#bq_show) --format = prettyjson myotherproject:mydataset.mytable
```


Enter the following command to display only schema information about
`mytable` in `mydataset`. `mydataset` is in `myotherproject`, not your
default project.


```
[bq show](/bigquery/docs/reference/bq-cli-reference#bq_show) --schema --format = prettyjson myotherproject:mydataset.mytable
```





Call the [`tables.get`](/bigquery/docs/reference/rest/v2/tables/get)
method and provide any relevant parameters.
































Before trying this sample, follow the Go setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Go API
reference documentation](https://godoc.org/cloud.google.com/go/bigquery).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import ( 
"context" 
"fmt" 
"io" 

"cloud.google.com/go/bigquery" 
) 

// printTableInfo demonstrates fetching metadata from a table and printing some basic information 
// to an io.Writer. 
func printTableInfo ( w io . Writer , projectID , datasetID , tableID string ) error { 
// projectID := "my-project-id" 
// datasetID := "mydataset" 
// tableID := "mytable" 
ctx := context . Background () 
client , err := bigquery . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "bigquery.NewClient: %v" , err ) 
} 
defer client . Close () 

meta , err := client . Dataset ( datasetID ). Table ( tableID ). Metadata ( ctx ) 
if err != nil { 
return err 
} 
// Print basic information about the table. 
fmt . Fprintf ( w , "Schema has %d top-level fields\n" , len ( meta . [ Schema ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Schema) )) 
fmt . Fprintf ( w , "Description: %s\n" , meta . Description ) 
fmt . Fprintf ( w , "Rows in managed storage: %d\n" , meta . NumRows ) 
return nil 
} 
```


















































Before trying this sample, follow the Java setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Java API
reference documentation](/java/docs/reference/google-cloud-bigquery/latest/overview).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import com.google.cloud.bigquery.[BigQuery](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) ; 
import com.google.cloud.bigquery.[BigQueryException](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) ; 
import com.google.cloud.bigquery.[BigQueryOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) ; 
import com.google.cloud.bigquery.[Table](https://berlin.devsitetest.how/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1.Table.html) ; 
import com.google.cloud.bigquery.[TableId](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) ; 

public class GetTable { 

public static void runGetTable () { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "bigquery_public_data" ; 
String datasetName = "samples" ; 
String tableName = "shakespeare" ; 
getTable ( projectId , datasetName , tableName ); 
} 

public static void getTable ( String projectId , String datasetName , String tableName ) { 
try { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
[ BigQuery ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [ BigQueryOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) . getDefaultInstance (). getService (); 

[ TableId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [ TableId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) . of ( projectId , datasetName , tableName ); 
[ Table ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1.Table.html) table = bigquery . [ getTable ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getTable_com_google_cloud_bigquery_TableId_com_google_cloud_bigquery_BigQuery_TableOption____) ( tableId ); 
System . out . println ( "Table info: " + table . getDescription ()); 
} catch ( [ BigQueryException ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e ) { 
System . out . println ( "Table not retrieved. \n" + e . toString ()); 
} 
} 
} 
```


















































Before trying this sample, follow the Node.js setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Node.js API
reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
// Import the Google Cloud client library 
const { BigQuery } = require ( '[@google-cloud/bigquery](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/overview.html)' ); 
const bigquery = new [ BigQuery ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html) (); 

async function getTable () { 
// Retrieves table named "my_table" in "my_dataset". 

/** 
* TODO(developer): Uncomment the following lines before running the sample 
*/ 
// const datasetId = "my_dataset"; 
// const tableId = "my_table"; 

// Retrieve table reference 
const dataset = bigquery . dataset ( datasetId ); 
const [ table ] = await dataset . table ( tableId ). get (); 

console . log ( 'Table:' ); 
console . log ( table . metadata . tableReference ); 
} 
getTable (); 
```

















































Before trying this sample, follow the PHP setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery PHP API
reference documentation](/php/docs/reference/cloud-bigquery/latest/BigQueryClient).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
use Google\Cloud\BigQuery\BigQueryClient; 

/** Uncomment and populate these variables in your code */ 
//$projectId = 'The Google project ID'; 
//$datasetId = 'The BigQuery dataset ID'; 
//$tableId = 'The BigQuery table ID'; 

$bigQuery = new BigQueryClient([ 
'projectId' => $projectId, 
]); 
$dataset = $bigQuery->dataset($datasetId); 
$table = $dataset->table($tableId); 
```


















































Before trying this sample, follow the Python setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Python API
reference documentation](/python/docs/reference/bigquery/latest).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
from google.cloud import [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest)

# Construct a BigQuery client object. 
client = [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html) () 

# TODO(developer): Set table_id to the ID of the model to fetch. 
# table_id = 'your-project.your_dataset.your_table' 

table = client . [ get_table ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table) ( table_id ) # Make an API request. 

# View table properties 
print ( 
"Got table ' {} . {} . {} '." . format ( table . project , table . dataset_id , table . table_id ) 
) 
print ( "Table schema: {} " . format ( table . schema )) 
print ( "Table description: {} " . format ( table . description )) 
print ( "Table has {} rows" . format ( table . [ num_rows ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html#google_cloud_bigquery_table_Table_num_rows) )) 
```




















### Get table information using `INFORMATION_SCHEMA`

`INFORMATION_SCHEMA` is a series of views that provide access to metadata
about datasets, routines, tables, views, jobs, reservations, and streaming data.

You can query the following views to get table information:

- Use the `INFORMATION_SCHEMA.TABLES` and `INFORMATION_SCHEMA.TABLE_OPTIONS`
views to retrieve metadata about tables and views in a project.

- Use the `INFORMATION_SCHEMA.COLUMNS` and
`INFORMATION_SCHEMA.COLUMN_FIELD_PATHS` views to retrieve metadata about the
columns (fields) in a table.

- Use the `INFORMATION_SCHEMA.TABLE_STORAGE` views to retrieve metadata
about current and historical storage usage by a table.

The `TABLES` and `TABLE_OPTIONS` views also contain high-level
information about views. For detailed information, query the
[`INFORMATION_SCHEMA.VIEWS`](/bigquery/docs/information-schema-views) view
instead.

#### `TABLES` view

When you query the `INFORMATION_SCHEMA.TABLES` view, the query results contain
one row for each table or view in a dataset. For detailed information about
views, query the [`INFORMATION_SCHEMA.VIEWS`
view](/bigquery/docs/information-schema-views) instead.

The `INFORMATION_SCHEMA.TABLES` view has the following schema:







| 
Column name | 
Data type | 
Value | 
|

| 
`table_catalog` | 
`STRING` | 
The project ID of the project that contains the dataset. | 
|

| 
`table_schema` | 
`STRING` | 
The name of the dataset that contains the table or view. Also referred
to as the `datasetId`. | 
|

| 
`table_name` | 
`STRING` | 
The name of the table or view. Also referred to as the
`tableId`. | 
|

| 
`table_type` | 
`STRING` | 
The table type; one of the following:




- `BASE TABLE`: A standard
[table](/bigquery/docs/tables-intro)

- `CLONE`: A
[table clone](/bigquery/docs/table-clones-intro)

- `SNAPSHOT`: A
[table snapshot](/bigquery/docs/table-snapshots-intro)

- `VIEW`: A
[view](/bigquery/docs/views-intro)

- `MATERIALIZED VIEW`: A
[materialized view](/bigquery/docs/materialized-views-intro)
or [materialized view replica](/bigquery/docs/load-data-using-cross-cloud-transfer#materialized_view_replicas)

- `EXTERNAL`: A table that references an
[external data source](/bigquery/external-data-sources)


| 
|

| 
`managed_table_type` | 
`STRING` | 
This column is in Preview. The managed table type; one of the following:




- `NATIVE`: A standard
[table](/bigquery/docs/tables-intro)

- `BIGLAKE`: A [
Apache Iceberg managed table](/bigquery/docs/iceberg-tables)


| 
|

| 
`is_insertable_into` | 
`STRING` | 
`YES` or `NO` depending on whether the table
supports [DML INSERT](/bigquery/docs/reference/standard-sql/dml-syntax#insert_statement)
statements | 
|

| 
`is_fine_grained_mutations_enabled` | 
`STRING` | 

`YES` or `NO` depending on whether
[fine-grained DML mutations](/bigquery/docs/data-manipulation-language#enable_fine-grained_dml)
are enabled on the table
| 
|

| 
`is_typed` | 
`STRING` | 
The value is always `NO` | 
|

| 
`is_change_history_enabled` | 
`STRING` | 
`YES` or `NO` depending on whether
[change history](/bigquery/docs/change-history)
is enabled | 
|

| 
`creation_time` | 
`TIMESTAMP` | 
The table's creation time | 
|

| 
`base_table_catalog` | 
`STRING` | 
For [table clones](/bigquery/docs/table-clones-intro)
and [table snapshots](/bigquery/docs/table-snapshots-intro),
the base table's project. Applicable only to
tables with `table_type` set to `CLONE` or
`SNAPSHOT`.
| 
|

| 
`base_table_schema` | 
`STRING` | 
For [table clones](/bigquery/docs/table-clones-intro)
and [table snapshots](/bigquery/docs/table-snapshots-intro),
the base table's dataset. Applicable only to tables with
`table_type` set to `CLONE` or
`SNAPSHOT`. | 
|

| 
`base_table_name` | 
`STRING` | 
For [table clones](/bigquery/docs/table-clones-intro)
and [table snapshots](/bigquery/docs/table-snapshots-intro),
the base table's name. Applicable only to tables with
`table_type` set to `CLONE` or
`SNAPSHOT`. | 
|

| 
`snapshot_time_ms` | 
`TIMESTAMP` | 
For [table clones](/bigquery/docs/table-clones-intro)
and [table snapshots](/bigquery/docs/table-snapshots-intro),
the time when the [clone](/bigquery/docs/table-clones-create)
or [snapshot](/bigquery/docs/table-snapshots-create)
operation was run on the base table to create this table. If
[time travel](/bigquery/docs/time-travel) was used, then this
field contains the time travel timestamp. Otherwise, the
`snapshot_time_ms` field is the same as the
`creation_time` field. Applicable only to
tables with `table_type` set to `CLONE` or
`SNAPSHOT`.
| 
|

| 
`replica_source_catalog` | 
`STRING` | 
For
[materialized view replicas](/bigquery/docs/load-data-using-cross-cloud-transfer#materialized_view_replicas),
the base materialized view's project. | 
|

| 
`replica_source_schema` | 
`STRING` | 
For
[materialized view replicas](/bigquery/docs/load-data-using-cross-cloud-transfer#materialized_view_replicas),
the base materialized view's dataset. | 
|

| 
`replica_source_name` | 
`STRING` | 
For
[materialized view replicas](/bigquery/docs/load-data-using-cross-cloud-transfer#materialized_view_replicas),
the base materialized view's name. | 
|

| 
`replication_status` | 
`STRING` | 
For
[materialized view replicas](/bigquery/docs/load-data-using-cross-cloud-transfer#materialized_view_replicas),
the status of the replication from the base materialized view to the
materialized view replica; one of the following:




- `REPLICATION_STATUS_UNSPECIFIED`

- `ACTIVE`: Replication is active with no errors

- `SOURCE_DELETED`: The source materialized view has
been deleted

- `PERMISSION_DENIED`: The source materialized view
hasn't been [authorized](/bigquery/docs/authorized-views)
on the dataset that contains the source Amazon S3
BigLake tables used in the query that created the
materialized view.

- `UNSUPPORTED_CONFIGURATION`: There is an issue with
the replica's
[prerequisites](/bigquery/docs/load-data-using-cross-cloud-transfer#create)
other than source materialized view authorization.


| 
|

| 
`replication_error` | 
`STRING` | 
If `replication_status` indicates a replication issue for a
[materialized view replica](/bigquery/docs/load-data-using-cross-cloud-transfer#materialized_view_replicas),
`replication_error` provides further details about the issue. | 
|

| 
`ddl` | 
`STRING` | 
The [DDL statement](/bigquery/docs/reference/standard-sql/data-definition-language)
that can be used to recreate the table, such as
`[CREATE TABLE](/bigquery/docs/reference/standard-sql/data-definition-language#create_table_statement)`
or `[CREATE VIEW](/bigquery/docs/reference/standard-sql/data-definition-language#create_view_statement)` | 
|

| 
`default_collation_name` | 
`STRING` | 

The name of the default [collation specification](/bigquery/docs/reference/standard-sql/collation-concepts)
if it exists; otherwise, `NULL`.
| 
|

| 
`sync_status` | 
`JSON` | 
The status of the sync between the primary and secondary replicas for [cross-region
replication](/bigquery/docs/data-replication) and [disaster recovery](/bigquery/docs/managed-disaster-recovery) datasets. Returns `NULL` if the replica is a primary replica or the dataset doesn't use replication. | 
|

| 
`upsert_stream_apply_watermark` | 
`TIMESTAMP` | 

For tables that use change data capture (CDC), the time when row
modifications were last applied. For more information, see
[Monitor table upsert operation progress](/bigquery/docs/change-data-capture#monitor_table_upsert_operation_progress).
| 
|



#### Examples

##### Example 1:

The following example retrieves table metadata for all of the tables in the
dataset named `mydataset`. The metadata that's
returned is for all types of tables in `mydataset` in your default project.

`mydataset` contains the following tables:

- `mytable1`: a standard BigQuery table

- `myview1`: a BigQuery view

To run the query against a project other than your default project, add the
project ID to the dataset in the following format:
`` project_id `. dataset .INFORMATION_SCHEMA. view `;
for example, ``myproject`.mydataset.INFORMATION_SCHEMA.TABLES`.


```
SELECT 
table_catalog , table_schema , table_name , table_type , 
is_insertable_into , creation_time , ddl 
FROM 
mydataset . INFORMATION_SCHEMA . TABLES ; 
```


The result is similar to the following. For readability, some columns
are excluded from the result.


```
+----------------+---------------+----------------+------------+--------------------+---------------------+---------------------------------------------+
| table_catalog | table_schema | table_name | table_type | is_insertable_into | creation_time | ddl |
+----------------+---------------+----------------+------------+--------------------+---------------------+---------------------------------------------+
| myproject | mydataset | mytable1 | BASE TABLE | YES | 2018-10-29 20:34:44 | CREATE TABLE `myproject.mydataset.mytable1` |
| | | | | | | ( |
| | | | | | | id INT64 |
| | | | | | | ); |
| myproject | mydataset | myview1 | VIEW | NO | 2018-12-29 00:19:20 | CREATE VIEW `myproject.mydataset.myview1` |
| | | | | | | AS SELECT 100 as id; |
+----------------+---------------+----------------+------------+--------------------+---------------------+---------------------------------------------+
```


##### Example 2:

The following example retrieves table metadata for all tables of type `CLONE`
or `SNAPSHOT` from the `INFORMATION_SCHEMA.TABLES` view. The metadata returned
is for tables in `mydataset` in your default project.

To run the query against a project other than your default project, add the
project ID to the dataset in the following format:
`` project_id `. dataset .INFORMATION_SCHEMA. view `;
for example, ``myproject`.mydataset.INFORMATION_SCHEMA.TABLES`.


```
SELECT 
table_name , table_type , base_table_catalog , 
base_table_schema , base_table_name , snapshot_time_ms 
FROM 
mydataset . INFORMATION_SCHEMA . TABLES 
WHERE 
table_type = 'CLONE' 
OR 
table_type = 'SNAPSHOT' ; 
```


The result is similar to the following. For readability, some columns
are excluded from the result.


```
+--------------+------------+--------------------+-------------------+-----------------+---------------------+
| table_name | table_type | base_table_catalog | base_table_schema | base_table_name | snapshot_time_ms |
+--------------+------------+--------------------+-------------------+-----------------+---------------------+
| items_clone | CLONE | myproject | mydataset | items | 2018-10-31 22:40:05 |
| orders_bk | SNAPSHOT | myproject | mydataset | orders | 2018-11-01 08:22:39 |
+--------------+------------+--------------------+-------------------+-----------------+---------------------+

```


##### Example 3:

The following example retrieves `table_name` and `ddl` columns from the `INFORMATION_SCHEMA.TABLES`
view for the `population_by_zip_2010` table in the
[`census_bureau_usa`](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=census_bureau_usa&page=dataset)
dataset. This dataset is part of the BigQuery
[public dataset program](/bigquery/public-data).

Because the table you're querying is in another project, you add the project ID to the dataset in
the following format:
`` project_id `. dataset .INFORMATION_SCHEMA. view `.
In this example, the value is
``bigquery-public-data`.census_bureau_usa.INFORMATION_SCHEMA.TABLES`.


```
SELECT 
table_name , ddl 
FROM 
`bigquery-public-data` . census_bureau_usa . INFORMATION_SCHEMA . TABLES 
WHERE 
table_name = 'population_by_zip_2010' ; 
```


The result is similar to the following:


```
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| table_name | ddl |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| population_by_zip_2010 | CREATE TABLE `bigquery-public-data.census_bureau_usa.population_by_zip_2010` |
| | ( |
| | geo_id STRING OPTIONS(description="Geo code"), |
| | zipcode STRING NOT NULL OPTIONS(description="Five digit ZIP Code Tabulation Area Census Code"), |
| | population INT64 OPTIONS(description="The total count of the population for this segment."), |
| | minimum_age INT64 OPTIONS(description="The minimum age in the age range. If null, this indicates the row as a total for male, female, or overall population."), |
| | maximum_age INT64 OPTIONS(description="The maximum age in the age range. If null, this indicates the row as having no maximum (such as 85 and over) or the row is a total of the male, female, or overall population."), |
| | gender STRING OPTIONS(description="male or female. If empty, the row is a total population summary.") |
| | ) |
| | OPTIONS( |
| | labels=[("freebqcovid", "")] |
| | ); |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```


#### `TABLE_OPTIONS` view

When you query the `INFORMATION_SCHEMA.TABLE_OPTIONS` view, the query results
contain one row for each option, for each table or view in a dataset. For
detailed information about
views, query the
[`INFORMATION_SCHEMA.VIEWS` view](/bigquery/docs/information-schema-views)
instead.

The `INFORMATION_SCHEMA.TABLE_OPTIONS` view has the following schema:




| 
Column name | 
Data type | 
Value | 
|

| 
`table_catalog` | 
`STRING` | 
The project ID of the project that contains the dataset | 
|

| 
`table_schema` | 
`STRING` | 
The name of the dataset that contains the table or view also referred
to as the `datasetId` | 
|

| 
`table_name` | 
`STRING` | 
The name of the table or view also referred to as the `tableId` | 
|

| 
`option_name` | 
`STRING` | 
One of the name values in the [options table](#options_table) | 
|

| 
`option_type` | 
`STRING` | 
One of the data type values in the [options table](#options_table) | 
|

| 
`option_value` | 
`STRING` | 
One of the value options in the [options table](#options_table) | 
|



##### Options table




| 


`OPTION_NAME`
| 


`OPTION_TYPE`
| 


`OPTION_VALUE`
| 
|



| 


`description`
| 


`STRING`
| 
A description of the table | 
|

| 


`enable_refresh`
| 


`BOOL`
| 
Whether automatic refresh is enabled for a materialized view | 
|

| 


`expiration_timestamp`
| 


`TIMESTAMP`
| 
The time when this table expires | 
|

| 


`friendly_name`
| 


`STRING`
| 
The table's descriptive name | 
|

| 


`kms_key_name`
| 


`STRING`
| 
The name of the Cloud KMS key used to encrypt the table | 
|

| 


`labels`
| 


`ARRAY >`
| 
An array of `STRUCT`'s that represent the labels on the
table | 
|

| 


`max_staleness`
| 


`INTERVAL`
| 
The configured table's maximum staleness for
[BigQuery
change data capture (CDC) upserts](/bigquery/docs/change-data-capture#manage_table_staleness) | 
|

| 


`partition_expiration_days`
| 


`FLOAT64`
| 
The default lifetime, in days, of all partitions in a partitioned
table | 
|

| 


`refresh_interval_minutes`
| 


`FLOAT64`
| 
How frequently a materialized view is refreshed | 
|

| 


`require_partition_filter`
| 


`BOOL`
| 
Whether queries over the table require a partition filter | 
|

| 


`tags`
| 


`ARRAY >`
| 
Tags attached to a table in a namespaced <key, value> syntax.
For more information, see
[Tags and
conditional access](/iam/docs/tags-access-control). | 
|



For external tables, the following options are possible:




| 
Options | 
|

| 
`allow_jagged_rows` | 



`BOOL`



If `true`, allow rows that are missing trailing optional
columns.



Applies to CSV data.

| 
|

| 
`allow_quoted_newlines` | 



`BOOL`



If `true`, allow quoted data sections that contain newline
characters in the file.



Applies to CSV data.

| 
|

| 
`bigtable_options` | 



`STRING`



Only required when creating a Bigtable external
table.



Specifies the schema of the Bigtable external table
in JSON format.



For a list of Bigtable table definition options, see
`[BigtableOptions](/bigquery/docs/reference/rest/v2/tables#bigtableoptions)`
in the REST API reference.

| 
|


| 
`column_name_character_map` | 



`STRING`



Defines the scope of supported column name characters and the
handling behavior of unsupported characters. The default setting is
`STRICT`, which means unsupported characters cause
BigQuery to throw errors.
`V1` and `V2` replace any unsupported characters
with underscores.



Supported values include:




- `STRICT`. Enables
[flexible column names](/bigquery/docs/schemas#flexible-column-names).
This is the default value. Load jobs with unsupported characters in column
names fail with an error message. To configure the replacement of
unsupported characters with underscores so that the load job succeeds,
specify the
[`default_column_name_character_map`](/bigquery/docs/default-configuration)
configuration setting.

- `V1`. Column names can only contain
[standard column name characters](/bigquery/docs/schemas#column_names).
Unsupported characters (except [periods in Parquet file column names](/bigquery/docs/loading-data-cloud-storage-parquet#limitations_2))
are replaced with underscores. This is the default behavior for tables
created before the introduction of `column_name_character_map`.

- `V2`. Besides
[standard column name characters](/bigquery/docs/schemas#column_names),
it also supports
[flexible column names](/bigquery/docs/schemas#flexible-column-names).
Unsupported characters (except [periods in Parquet file column names](/bigquery/docs/loading-data-cloud-storage-parquet#limitations_2))
are replaced with underscores.


Applies to CSV and Parquet data.



| 
|


| 
`compression` | 



`STRING`



The compression type of the data source. Supported values include:
`GZIP`. If not specified, the data source is uncompressed.




Applies to CSV and JSON data.

| 
|

| 
`decimal_target_types` | 



`ARRAY `



Determines how to convert a `Decimal` type. Equivalent to
[ExternalDataConfiguration.decimal_target_types](/bigquery/docs/reference/rest/v2/tables#ExternalDataConfiguration.FIELDS.decimal_target_types)



Example: `["NUMERIC", "BIGNUMERIC"]`.

| 
|


| 
`description` | 



`STRING`



A description of this table.

| 
|


| 
`enable_list_inference` | 



`BOOL`



If `true`, use schema inference specifically for
Parquet LIST logical type.



Applies to Parquet data.

| 
|

| 
`enable_logical_types` | 



`BOOL`



If `true`, convert Avro logical types into their
corresponding SQL types. For more information, see
[
Logical types](/bigquery/docs/loading-data-cloud-storage-avro#logical_types).



Applies to Avro data.

| 
|

| 
`encoding` | 



`STRING`



The character encoding of the data. Supported values include:
`UTF8` (or `UTF-8`), `ISO_8859_1` (or
`ISO-8859-1`), `UTF-16BE`,
`UTF-16LE`, `UTF-32BE`, or `UTF-32LE`.
The default value is `UTF-8`.



Applies to CSV data.

| 
|

| 
`enum_as_string` | 



`BOOL`



If `true`, infer Parquet ENUM logical type as STRING
instead of BYTES by default.



Applies to Parquet data.

| 
|


| 
`expiration_timestamp` | 



`TIMESTAMP`



The time when this table expires. If not specified, the table does
not expire.



Example: `"2025-01-01 00:00:00 UTC"`.

| 
|


| 
`field_delimiter` | 



`STRING`



The separator for fields in a CSV file.



Applies to CSV data.

| 
|

| 
`format` | 



`STRING`



The format of the external data.
Supported values for
[
`CREATE EXTERNAL TABLE`](/bigquery/docs/reference/standard-sql/data-definition-language#create_external_table_statement)
include: `AVRO`, `CLOUD_BIGTABLE`, `CSV`,
`DATASTORE_BACKUP`, `DELTA_LAKE` ([preview](https://berlin.devsitetest.how/products/#product-launch-stages)),
`GOOGLE_SHEETS`, `NEWLINE_DELIMITED_JSON` (or
`JSON`), `ORC`, `PARQUET`.




Supported values for
[
`LOAD DATA`](/bigquery/docs/reference/standard-sql/load-statements)
include: `AVRO`, `CSV`,
`DELTA_LAKE` ([preview](https://berlin.devsitetest.how/products/#product-launch-stages))
`NEWLINE_DELIMITED_JSON` (or `JSON`),
`ORC`, `PARQUET`.




The value `JSON` is equivalent to
`NEWLINE_DELIMITED_JSON`.

| 
|

| 
`hive_partition_uri_prefix` | 



`STRING`



A common prefix for all source URIs before the partition key encoding
begins. Applies only to hive-partitioned external tables.



Applies to Avro, CSV, JSON, Parquet, and ORC data.



Example: `"gs://bucket/path"`.

| 
|

| 
`file_set_spec_type` | 



`STRING`



Specifies how to interpret source URIs for load jobs and external tables.



Supported values include:



- `FILE_SYSTEM_MATCH`. Expands source URIs by listing files from the object store. This is the default behavior if FileSetSpecType is not set.

- `NEW_LINE_DELIMITED_MANIFEST`. Indicates that the provided URIs are newline-delimited manifest files, with one URI per line. Wildcard URIs are not supported in the manifest files, and all referenced data files must be in the same bucket as the manifest file.



For example, if you have a source URI of `"gs://bucket/path/file"` and the `file_set_spec_type` is `FILE_SYSTEM_MATCH`, then the file is used directly as a data file. If the `file_set_spec_type` is `NEW_LINE_DELIMITED_MANIFEST`, then each line in the file is interpreted as a URI that points to a data file.

| 
|

| 
`ignore_unknown_values` | 



`BOOL`



If `true`, ignore extra values that are not represented
in the table schema, without returning an error.



Applies to CSV and JSON data.

| 
|

| 
`json_extension` | 



`STRING`



For JSON data, indicates a particular JSON interchange format. If
not specified, BigQuery reads the data as generic JSON
records.



Supported values include: 

`GEOJSON`. Newline-delimited GeoJSON data. For more
information, see
[Creating an
external table from a newline-delimited GeoJSON file](/bigquery/docs/geospatial-data#external-geojson).


| 
|

| 
`max_bad_records` | 



`INT64`



The maximum number of bad records to ignore when reading the data.



Applies to: CSV, JSON, and Google Sheets data.

| 
|

| 
`max_staleness` | 



`INTERVAL`



Applicable for
[BigLake tables](/bigquery/docs/biglake-intro#metadata_caching_for_performance)
and
[object tables](/bigquery/docs/object-table-introduction#metadata_caching_for_performance).



Specifies whether cached metadata is used by operations against the
table, and how fresh the cached metadata must be in order for
the operation to use it.



To disable metadata caching, specify 0. This is the default.



To enable metadata caching, specify an
[interval literal](/bigquery/docs/reference/standard-sql/lexical#interval_literals)
value between 30 minutes and 7 days. For example, specify
`INTERVAL 4 HOUR` for a 4 hour staleness interval.
With this value, operations against the table use cached metadata if
it has been refreshed within the past 4 hours. If the cached metadata
is older than that, the operation falls back to retrieving metadata from
Cloud Storage instead.

| 
|























| 
`null_marker` | 



`STRING`



The string that represents `NULL` values in a CSV file.



Applies to CSV data.

| 
|

| 
`null_markers` | 



`ARRAY `



The list of strings that represent `NULL` values in a CSV
file.



This option cannot be used with `null_marker` option.



Applies to CSV data.

| 
|

| 
`object_metadata` | 



`STRING`



Only required when creating an
[object table](/bigquery/docs/object-table-introduction).



Set the value of this option to `SIMPLE` when
creating an object table.

| 
|

| 
`preserve_ascii_control_characters` | 



`BOOL`



If `true`, then the embedded ASCII control characters
which are the first 32 characters in the ASCII table, ranging from
'\x00' to '\x1F', are preserved.



Applies to CSV data.

| 
|


| 
`projection_fields` | 



`STRING`



A list of entity properties to load.



Applies to Datastore data.

| 
|


| 
`quote` | 



`STRING`



The string used to quote data sections in a CSV file. If your data
contains quoted newline characters, also set the
`allow_quoted_newlines` property to `true`.



Applies to CSV data.

| 
|


| 
`reference_file_schema_uri` | 



`STRING`



User provided reference file with the table schema.



Applies to Parquet/ORC/AVRO data.



Example: `"gs://bucket/path/reference_schema_file.parquet"`.

| 
|

| 
`require_hive_partition_filter` | 



`BOOL`



If `true`, all queries over this table require a partition
filter that can be used to eliminate partitions when reading data.
Applies only to hive-partitioned external tables.



Applies to Avro, CSV, JSON, Parquet, and ORC data.

| 
|



| 
`sheet_range` | 



`STRING`



Range of a Google Sheets spreadsheet to query from.



Applies to Google Sheets data.



Example: `"sheet1!A1:B20"`,

| 
|


| 
`skip_leading_rows` | 



`INT64`



The number of rows at the top of a file to skip when reading the
data.



Applies to CSV and Google Sheets data.

| 
|

| 
`source_column_match` | 



`STRING`



This controls the strategy used to match loaded columns to the
schema.



If this value is unspecified, then the default is based on how the
schema is provided. If autodetect is enabled, then the default behavior
is to match columns by name. Otherwise, the default is to match columns
by position. This is done to keep the behavior backward-compatible.



Supported values include:




- `POSITION`: matches by position. This option assumes
that the columns are ordered the same way as the schema.

- `NAME`: matches by name. This option reads the header
row as column names and reorders columns to match the field names in
the schema. Column names are read from the last skipped row based on
the `skip_leading_rows` property.



| 
|

| 
`tags` | 
` >>`


An array of IAM tags for the table, expressed as
key-value pairs. The key should be the
[namespaced key name](/iam/docs/tags-access-control#definitions),
and the value should be the [short name](/iam/docs/tags-access-control#definitions).
| 
|

| 
`time_zone` | 



`STRING`



Default time zone that will apply when parsing timestamp values that
have no specific time zone.



Check
[valid time zone names](/bigquery/docs/reference/standard-sql/data-types#time_zone_name).



If this value is not present, the timestamp values without specific
time zone is parsed using default time zone UTC.



Applies to CSV and JSON data.

| 
|

| 
`date_format` | 



`STRING`



[Format elements](/bigquery/docs/reference/standard-sql/format-elements#format_string_as_datetime)
that define how the DATE values are formatted in the input files (for
example, `MM/DD/YYYY`).



If this value is present, this format is the only compatible DATE
format.
[Schema autodetection](/bigquery/docs/schema-detect#date_and_time_values)
will also decide DATE column type based on this format instead of the
existing format.



If this value is not present, the DATE field is parsed with the
[default formats](/bigquery/docs/loading-data-cloud-storage-csv#data_types).



Applies to CSV and JSON data.

| 
|

| 
`datetime_format` | 



`STRING`



[Format elements](/bigquery/docs/reference/standard-sql/format-elements#format_string_as_datetime)
that define how the DATETIME values are formatted in the input files
(for example, `MM/DD/YYYY HH24:MI:SS.FF3`).



If this value is present, this format is the only compatible DATETIME
format.
[Schema autodetection](/bigquery/docs/schema-detect#date_and_time_values)
will also decide DATETIME column type based on this format instead of
the existing format.



If this value is not present, the DATETIME field is parsed with the
[default formats](/bigquery/docs/loading-data-cloud-storage-csv#data_types).



Applies to CSV and JSON data.

| 
|

| 
`time_format` | 



`STRING`



[Format elements](/bigquery/docs/reference/standard-sql/format-elements#format_string_as_datetime)
that define how the TIME values are formatted in the input files (for
example, `HH24:MI:SS.FF3`).



If this value is present, this format is the only compatible TIME
format.
[Schema autodetection](/bigquery/docs/schema-detect#date_and_time_values)
will also decide TIME column type based on this format instead of the
existing format.



If this value is not present, the TIME field is parsed with the
[default formats](/bigquery/docs/loading-data-cloud-storage-csv#data_types).



Applies to CSV and JSON data.

| 
|

| 
`timestamp_format` | 



`STRING`



[Format elements](/bigquery/docs/reference/standard-sql/format-elements#format_string_as_datetime)
that define how the TIMESTAMP values are formatted in the input files
(for example, `MM/DD/YYYY HH24:MI:SS.FF3`).



If this value is present, this format is the only compatible
TIMESTAMP format.
[Schema autodetection](/bigquery/docs/schema-detect#date_and_time_values)
will also decide TIMESTAMP column type based on this format instead of
the existing format.



If this value is not present, the TIMESTAMP field is parsed with the
[default formats](/bigquery/docs/loading-data-cloud-storage-csv#data_types).



Applies to CSV and JSON data.

| 
|

| 
`uris` | 



For external tables, including object tables, that aren't
Bigtable tables:



`ARRAY `



An array of fully qualified URIs for the external data locations.
Each URI can contain one
asterisk (`*`)
[wildcard character](/bigquery/docs/loading-data-cloud-storage#load-wildcards),
which must come after the bucket name. When you specify
`uris` values that target multiple files, all of those
files must share a compatible schema.



The following examples show valid `uris` values:




- `['gs://bucket/path1/myfile.csv']`

- `['gs://bucket/path1/*.csv']`

- `['gs://bucket/path1/*', 'gs://bucket/path2/file00*']`






For Bigtable tables:



`STRING`



The URI identifying the Bigtable table to use as a
data source. You can only specify one Bigtable URI.



Example:
`https://googleapis.com/bigtable/projects/ project_id /instances/ instance_id [/appProfiles/ app_profile ]/tables/ table_name `



For more information on constructing a Bigtable
URI, see
[Retrieve the Bigtable URI](/bigquery/docs/create-bigtable-external-table#bigtable-uri).

| 
|



#### Examples

##### Example 1:

The following example retrieves the default table expiration times for all
tables in `mydataset` in your default project (`myproject`) by querying the
`INFORMATION_SCHEMA.TABLE_OPTIONS` view.

To run the query against a project other than your default project, add the
project ID to the dataset in the following format:
`` project_id `. dataset .INFORMATION_SCHEMA. view `;
for example, ``myproject`.mydataset.INFORMATION_SCHEMA.TABLE_OPTIONS`.


```
SELECT 
* 
FROM 
mydataset . INFORMATION_SCHEMA . TABLE_OPTIONS 
WHERE 
option_name = 'expiration_timestamp' ; 
```


The result is similar to the following:


```
+----------------+---------------+------------+----------------------+-------------+--------------------------------------+
| table_catalog | table_schema | table_name | option_name | option_type | option_value |
+----------------+---------------+------------+----------------------+-------------+--------------------------------------+
| myproject | mydataset | mytable1 | expiration_timestamp | TIMESTAMP | TIMESTAMP "2020-01-16T21:12:28.000Z" |
| myproject | mydataset | mytable2 | expiration_timestamp | TIMESTAMP | TIMESTAMP "2021-01-01T21:12:28.000Z" |
+----------------+---------------+------------+----------------------+-------------+--------------------------------------+
```


##### Example 2:

The following example retrieves metadata about all tables in `mydataset` that
contain test data. The query uses the values in the `description` option to find
tables that contain "test" anywhere in the description. `mydataset` is in your
default project — `myproject`.

To run the query against a project other than your default project, add the
project ID to the dataset in the following format:
`` project_id `. dataset .INFORMATION_SCHEMA. view `;
for example,
``myproject`.mydataset.INFORMATION_SCHEMA.TABLE_OPTIONS`.


```
SELECT 
* 
FROM 
mydataset . INFORMATION_SCHEMA . TABLE_OPTIONS 
WHERE 
option_name = 'description' 
AND option_value LIKE '%test%' ; 
```


The result is similar to the following:


```
+----------------+---------------+------------+-------------+-------------+--------------+
| table_catalog | table_schema | table_name | option_name | option_type | option_value |
+----------------+---------------+------------+-------------+-------------+--------------+
| myproject | mydataset | mytable1 | description | STRING | "test data" |
| myproject | mydataset | mytable2 | description | STRING | "test data" |
+----------------+---------------+------------+-------------+-------------+--------------+
```


#### `COLUMNS` view

When you query the `INFORMATION_SCHEMA.COLUMNS` view, the query results contain
one row for each column (field) in a table.

The `INFORMATION_SCHEMA.COLUMNS` view has the following schema:




| 
Column name | 
Data type | 
Value | 
|

| 
`table_catalog` | 
`STRING` | 
The project ID of the project that contains the dataset. | 
|

| 
`table_schema` | 
`STRING` | 
The name of the dataset that contains the table also referred to as
the `datasetId`. | 
|

| 
`table_name` | 
`STRING` | 
The name of the table or view also referred to as the `tableId`. | 
|

| 
`column_name` | 
`STRING` | 
The name of the column. | 
|

| 
`ordinal_position` | 
`INT64` | 
The 1-indexed offset of the column within the table; if it's a pseudo
column such as _PARTITIONTIME or _PARTITIONDATE, the value is
`NULL`. | 
|

| 
`is_nullable` | 
`STRING` | 
`YES` or `NO` depending on whether the column's
mode allows `NULL` values. | 
|

| 
`data_type` | 
`STRING` | 
The column's GoogleSQL [data type](/bigquery/docs/reference/standard-sql/data-types). | 
|

| 
`is_generated` | 
`STRING` | 
The value is `ALWAYS` if the column is an
[automatically
generated embedding column](/bigquery/docs/autonomous-embedding-generation);
otherwise, the value is `NEVER`. | 
|

| 
`generation_expression` | 
`STRING` | 
The value is the generation expression used to define the column
if the column is an automatically
generated embedding column; otherwise the value is `NULL`. | 
|

| 
`is_stored` | 
`STRING` | 
The value is `YES` if the column is an automatically
generated embedding column; otherwise, the value is
`NULL`. | 
|

| 
`async_generation_status` | 
`STRUCT` | 

Contains blocking errors for background embedding generation jobs if the
column is an automatically generated embedding column; otherwise, the
value is `NULL`. For information about blocking errors, see
the `async_generation_status.blocking_error.message` field.
Blocking errors can include the following:



- Permission denied errors

- Not found errors

- Unsupported embedding model endpoint errors

- Vertex AI API not enabled errors


Once the next embedding generation job succeeds, the
`async_generation_status` column is cleared.
| 
|

| 
`is_hidden` | 
`STRING` | 
`YES` or `NO` depending on whether the column is
a pseudo column such as _PARTITIONTIME or _PARTITIONDATE. | 
|

| 
`is_updatable` | 
`STRING` | 
The value is always `NULL`. | 
|

| 
`is_system_defined` | 
`STRING` | 
`YES` or `NO` depending on whether the column is
a pseudo column such as _PARTITIONTIME or _PARTITIONDATE. | 
|

| 
`is_partitioning_column` | 
`STRING` | 
`YES` or `NO` depending on whether the column is
a [partitioning column](/bigquery/docs/partitioned-tables). | 
|

| 
`clustering_ordinal_position` | 
`INT64` | 
The 1-indexed offset of the column within the table's
clustering columns; the value is `NULL` if the table is not a
clustered table. | 
|

| 
`collation_name` | 
`STRING` | 

The name of the [collation specification](/bigquery/docs/reference/standard-sql/collation-concepts)
if it exists; otherwise, `NULL`.

If a `STRING` or `ARRAY ` is passed
in, the collation specification is returned if it exists; otherwise
`NULL` is returned.
| 
|

| 
`column_default` | 
`STRING` | 

The [default value](/bigquery/docs/default-values) of the
column if it exists; otherwise, the value is `NULL`.
| 
|

| 
`rounding_mode` | 
`STRING` | 

The mode of rounding that's used for values written to the field if its
type is a parameterized `NUMERIC` or `BIGNUMERIC`;
otherwise, the value is `NULL`.
| 
|

| 
`data_policies.name` | 
`STRING` | 

The list of data policies that are attached to the column to control access and masking. This field is in ([Preview](https://berlin.devsitetest.how/products#product-launch-stages)).
| 
|

| 
`policy_tags` | 
`ARRAY ` | 

The list of policy tags that are attached to the column.
| 
|



#### Examples

The following example retrieves metadata from the `INFORMATION_SCHEMA.COLUMNS`
view for the `population_by_zip_2010` table in the
[`census_bureau_usa`](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=census_bureau_usa&page=dataset)
dataset. This dataset is part of the BigQuery
[public dataset program](https://berlin.devsitetest.how/public-datasets/).

Because the table you're querying is in another project, the
`bigquery-public-data` project, you add the project ID to the dataset in the
following format:
`` project_id `. dataset .INFORMATION_SCHEMA. view `;
for example,
``bigquery-public-data`.census_bureau_usa.INFORMATION_SCHEMA.TABLES`.

The following column is excluded from the query results:

- `IS_UPDATABLE`


```
SELECT 
* EXCEPT ( is_updatable ) 
FROM 
`bigquery-public-data` . census_bureau_usa . INFORMATION_SCHEMA . COLUMNS 
WHERE 
table_name = 'population_by_zip_2010' ; 
```


The result is similar to the following. For readability, some columns
are excluded from the result.


```
+------------------------+-------------+------------------+-------------+-----------+-----------+-------------------+------------------------+-----------------------------+-------------+
| table_name | column_name | ordinal_position | is_nullable | data_type | is_hidden | is_system_defined | is_partitioning_column | clustering_ordinal_position | policy_tags |
+------------------------+-------------+------------------+-------------+-----------+-----------+-------------------+------------------------+-----------------------------+-------------+
| population_by_zip_2010 | zipcode | 1 | NO | STRING | NO | NO | NO | NULL | 0 rows |
| population_by_zip_2010 | geo_id | 2 | YES | STRING | NO | NO | NO | NULL | 0 rows |
| population_by_zip_2010 | minimum_age | 3 | YES | INT64 | NO | NO | NO | NULL | 0 rows |
| population_by_zip_2010 | maximum_age | 4 | YES | INT64 | NO | NO | NO | NULL | 0 rows |
| population_by_zip_2010 | gender | 5 | YES | STRING | NO | NO | NO | NULL | 0 rows |
| population_by_zip_2010 | population | 6 | YES | INT64 | NO | NO | NO | NULL | 0 rows |
+------------------------+-------------+------------------+-------------+-----------+-----------+-------------------+------------------------+-----------------------------+-------------+
```


#### `COLUMN_FIELD_PATHS` view

When you query the `INFORMATION_SCHEMA.COLUMN_FIELD_PATHS` view, the query
results contain one row for each column
[nested](/bigquery/docs/nested-repeated) within a `RECORD`
(or `STRUCT`) column.

The `INFORMATION_SCHEMA.COLUMN_FIELD_PATHS` view has the following schema:




| 
Column name | 
Data type | 
Value | 
|

| 
`table_catalog` | 
`STRING` | 
The project ID of the project that contains the dataset. | 
|

| 
`table_schema` | 
`STRING` | 
The name of the dataset that contains the table also referred to as
the `datasetId`. | 
|

| 
`table_name` | 
`STRING` | 
The name of the table or view also referred to as the `tableId`. | 
|

| 
`column_name` | 
`STRING` | 
The name of the top-level column. | 
|

| 
`field_path` | 
`STRING` | 
The name of the top-level column or the path to the column
[nested](/bigquery/docs/nested-repeated)
within a `RECORD` or `STRUCT` column. | 
|

| 
`data_type` | 
`STRING` | 
The column's GoogleSQL
[data type](/bigquery/docs/reference/standard-sql/data-types). | 
|

| 
`description` | 
`STRING` | 
The column's description. | 
|

| 
`collation_name` | 
`STRING` | 

The name of the [collation specification](/bigquery/docs/reference/standard-sql/collation-concepts)
if it exists; otherwise, `NULL`.

If a `STRING`, `ARRAY `, or
`STRING` field in a `STRUCT` is passed in, the
collation specification is returned if it exists; otherwise,
`NULL` is returned.
| 
|

| 
`rounding_mode` | 
`STRING` | 

The mode of rounding that's used when applying precision and scale to+
parameterized `NUMERIC` or `BIGNUMERIC` values;
otherwise, the value is `NULL`.
| 
|

| 
`data_policies.name` | 
`STRING` | 

The list of data policies that are attached to the column to control access and masking. This field is in ([Preview](https://berlin.devsitetest.how/products#product-launch-stages)).
| 
|

| 
`policy_tags` | 
`ARRAY ` | 

The list of policy tags that are attached to the column.
| 
|



#### Examples

The following example retrieves metadata from the
`INFORMATION_SCHEMA.COLUMN_FIELD_PATHS` view for the `commits` table in the
[`github_repos` dataset](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=github_repos&page=dataset).
This dataset is part of the BigQuery
[public dataset program](https://berlin.devsitetest.how/public-datasets/).

Because the table you're querying is in another project, the
`bigquery-public-data` project, you add the project ID to the dataset in the
following format:
`` project_id `. dataset .INFORMATION_SCHEMA. view `;
for example,
``bigquery-public-data`.github_repos.INFORMATION_SCHEMA.COLUMN_FIELD_PATHS`.

The `commits` table contains the following nested and nested and repeated
columns:

- `author`: nested `RECORD` column

- `committer`: nested `RECORD` column

- `trailer`: nested and repeated `RECORD` column

- `difference`: nested and repeated `RECORD` column

To view metadata about the `author` and `difference` columns, run the following query.


```
SELECT 
* 
FROM 
`bigquery-public-data` . github_repos . INFORMATION_SCHEMA . COLUMN_FIELD_PATHS 
WHERE 
table_name = 'commits' 
AND ( column_name = 'author' OR column_name = 'difference' ); 
```


The result is similar to the following. For readability, some columns
are excluded from the result.


```
+------------+-------------+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| table_name | column_name | field_path | data_type | description | policy_tags |
+------------+-------------+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| commits | author | author | STRUCT | NULL | 0 rows |
| commits | author | author.name | STRING | NULL | 0 rows |
| commits | author | author.email | STRING | NULL | 0 rows |
| commits | author | author.time_sec | INT64 | NULL | 0 rows |
| commits | author | author.tz_offset | INT64 | NULL | 0 rows |
| commits | author | author.date | TIMESTAMP | NULL | 0 rows |
| commits | difference | difference | ARRAY | NULL | 0 rows |
| commits | difference | difference.old_mode | INT64 | NULL | 0 rows |
| commits | difference | difference.new_mode | INT64 | NULL | 0 rows |
| commits | difference | difference.old_path | STRING | NULL | 0 rows |
| commits | difference | difference.new_path | STRING | NULL | 0 rows |
| commits | difference | difference.old_sha1 | STRING | NULL | 0 rows |
| commits | difference | difference.new_sha1 | STRING | NULL | 0 rows |
| commits | difference | difference.old_repo | STRING | NULL | 0 rows |
| commits | difference | difference.new_repo | STRING | NULL | 0 rows |
+------------+-------------+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
```


#### `TABLE_STORAGE` view

The `TABLE_STORAGE` and `TABLE_STORAGE_BY_ORGANIZATION` views have the following
schema:




| 
Column name | 
Data type | 
Value | 
|


| 
`project_id` | 
`STRING` | 
The project ID of the project that contains the dataset. | 
|

| 
`project_number` | 
`INT64` | 
The project number of the project that contains the dataset. | 
|

| 
`table_catalog` | 
`STRING` | 
The project ID of the project that contains the dataset. | 
|

| 
`table_schema` | 
`STRING` | 
The name of the dataset that contains the table or materialized view,
also referred to as the `datasetId`. | 
|

| 
`table_name` | 
`STRING` | 
The name of the table or materialized view, also referred to as the
`tableId`. | 
|

| 
`creation_time` | 
`TIMESTAMP` | 
The creation time of the table. | 
|

| 
`total_rows` | 
`INT64` | 
The total number of rows in the table or materialized view. | 
|

| 
`total_partitions` | 
`INT64` | 
The number of partitions present in the table or materialized view.
Unpartitioned tables return 0. | 
|

| 
`total_logical_bytes` | 
`INT64` | 
Total number of logical (uncompressed) bytes in the table or
materialized view. | 
|

| 
`active_logical_bytes` | 
`INT64` | 
Number of logical (uncompressed) bytes that are younger than 90 days.
| 
|

| 
`long_term_logical_bytes` | 
`INT64` | 
Number of logical (uncompressed) bytes that are older than 90 days.
| 
|

| 
`current_physical_bytes` | 
`INT64` | 
Total number of physical bytes for the current storage of the
table across all partitions. | 
|

| 
`total_physical_bytes` | 
`INT64` | 
Total number of physical (compressed) bytes used for storage,
including active, long-term, and time-travel (deleted or changed data)
bytes. Fail-safe (deleted or changed data retained after the time-travel
window) bytes aren't included.
| 
|

| 
`active_physical_bytes` | 
`INT64` | 
Number of physical (compressed) bytes younger than 90 days,
including time-travel (deleted or changed data) bytes.
| 
|

| 
`long_term_physical_bytes` | 
`INT64` | 
Number of physical (compressed) bytes older than 90 days.
| 
|

| 
`time_travel_physical_bytes` | 
`INT64` | 
Number of physical (compressed) bytes used by time-travel storage
(deleted or changed data).
| 
|

| 
`storage_last_modified_time` | 
`TIMESTAMP` | 
The most recent time that data was written to the table. Returns
`NULL` if no data exists. | 
|

| 
`deleted` | 
`BOOLEAN` | 
Indicates whether or not the table is deleted. | 
|

| 
`table_type` | 
`STRING` | 
The type of table. For example, `BASE TABLE`.
| 
|

| 
`managed_table_type` | 
`STRING` | 
This column is in Preview. The managed type of the table. For example,
`NATIVE` or `BIGLAKE`.
| 
|

| 
`fail_safe_physical_bytes` | 
`INT64` | 
Number of physical (compressed) bytes used by the fail-safe storage
(deleted or changed data).
| 
|

| 
`last_metadata_index_refresh_time` | 
`TIMESTAMP` | 
The last metadata index refresh time of the table.
| 
|

| 
`table_deletion_reason` | 
`STRING` | 
Table deletion reason if the `deleted` field is true. The
possible values are as follows:



- `TABLE_EXPIRATION:` table deleted after set expiration time

- `DATASET_DELETION:` dataset deleted by user

- `USER_DELETED:` table was deleted by user


| 
|

| 
`table_deletion_time` | 
`TIMESTAMP` | 
The deletion time of the table. | 
|



#### Examples

##### Example 1:

The following example shows you the total logical bytes billed for the
current project.


```
SELECT 
SUM ( total_logical_bytes ) AS total_logical_bytes 
FROM 
`region- REGION ` . INFORMATION_SCHEMA . TABLE_STORAGE ; 
```


The result is similar to the following:


```
+---------------------+
| total_logical_bytes |
+---------------------+
| 971329178274633 |
+---------------------+
```


##### Example 2:

The following example shows different storage bytes in GiB at the dataset(s) level for current project.


```
SELECT 
table_schema AS dataset_name , 
-- Logical 
SUM ( total_logical_bytes ) / power ( 1024 , 3 ) AS total_logical_gib , 
SUM ( active_logical_bytes ) / power ( 1024 , 3 ) AS active_logical_gib , 
SUM ( long_term_logical_bytes ) / power ( 1024 , 3 ) AS long_term_logical_gib , 
-- Physical 
SUM ( total_physical_bytes ) / power ( 1024 , 3 ) AS total_physical_gib , 
SUM ( active_physical_bytes ) / power ( 1024 , 3 ) AS active_physical_gib , 
SUM ( active_physical_bytes - time_travel_physical_bytes ) / power ( 1024 , 3 ) AS active_no_tt_physical_gib , 
SUM ( long_term_physical_bytes ) / power ( 1024 , 3 ) AS long_term_physical_gib , 
SUM ( time_travel_physical_bytes ) / power ( 1024 , 3 ) AS time_travel_physical_gib , 
SUM ( fail_safe_physical_bytes ) / power ( 1024 , 3 ) AS fail_safe_physical_gib 
FROM 
`region- REGION ` . INFORMATION_SCHEMA . TABLE_STORAGE 
WHERE 
table_type = 'BASE TABLE' 
GROUP BY 
table_schema 
ORDER BY 
dataset_name 
```


##### Example 3:

The following example shows you how to forecast the price difference per
dataset between logical and physical billing models for the next 30 days.
This example assumes that future storage usage is constant over the next
30 days from the moment the query was run. Note that the forecast is limited to
base tables, it excludes all other types of tables within a dataset.

The prices used in the pricing variables for this query are for
the `us-central1` region. If you want to run this query for a different region,
update the pricing variables appropriately. See
[Storage pricing](https://berlin.devsitetest.how/bigquery/pricing#storage) for pricing information.

- 

Open the BigQuery page in the Google Cloud Dedicated console.

[Go to the BigQuery page](https://console.cloud.berlin-build0.goog/bigquery) 

- 

Enter the following GoogleSQL query in the **Query editor** box.
`INFORMATION_SCHEMA` requires GoogleSQL syntax. GoogleSQL
is the default syntax in the Google Cloud Dedicated console.


```
DECLARE active_logical_gib_price FLOAT64 DEFAULT 0.02 ; 
DECLARE long_term_logical_gib_price FLOAT64 DEFAULT 0.01 ; 
DECLARE active_physical_gib_price FLOAT64 DEFAULT 0.04 ; 
DECLARE long_term_physical_gib_price FLOAT64 DEFAULT 0.02 ; 

WITH 
storage_sizes AS ( 
SELECT 
table_schema AS dataset_name , 
-- Logical 
SUM ( IF ( deleted = false , active_logical_bytes , 0 )) / power ( 1024 , 3 ) AS active_logical_gib , 
SUM ( IF ( deleted = false , long_term_logical_bytes , 0 )) / power ( 1024 , 3 ) AS long_term_logical_gib , 
-- Physical 
SUM ( active_physical_bytes ) / power ( 1024 , 3 ) AS active_physical_gib , 
SUM ( active_physical_bytes - time_travel_physical_bytes ) / power ( 1024 , 3 ) AS active_no_tt_physical_gib , 
SUM ( long_term_physical_bytes ) / power ( 1024 , 3 ) AS long_term_physical_gib , 
-- Restorable previously deleted physical 
SUM ( time_travel_physical_bytes ) / power ( 1024 , 3 ) AS time_travel_physical_gib , 
SUM ( fail_safe_physical_bytes ) / power ( 1024 , 3 ) AS fail_safe_physical_gib , 
FROM 
`region- REGION ` . INFORMATION_SCHEMA . TABLE_STORAGE_BY_PROJECT 
WHERE total_physical_bytes + fail_safe_physical_bytes > 0 
-- Base the forecast on base tables only for highest precision results 
AND table_type = 'BASE TABLE' 
GROUP BY 1 
) 
SELECT 
dataset_name , 
-- Logical 
ROUND ( active_logical_gib , 2 ) AS active_logical_gib , 
ROUND ( long_term_logical_gib , 2 ) AS long_term_logical_gib , 
-- Physical 
ROUND ( active_physical_gib , 2 ) AS active_physical_gib , 
ROUND ( long_term_physical_gib , 2 ) AS long_term_physical_gib , 
ROUND ( time_travel_physical_gib , 2 ) AS time_travel_physical_gib , 
ROUND ( fail_safe_physical_gib , 2 ) AS fail_safe_physical_gib , 
-- Compression ratio 
ROUND ( SAFE_DIVIDE ( active_logical_gib , active_no_tt_physical_gib ), 2 ) AS active_compression_ratio , 
ROUND ( SAFE_DIVIDE ( long_term_logical_gib , long_term_physical_gib ), 2 ) AS long_term_compression_ratio , 
-- Forecast costs logical 
ROUND ( active_logical_gib * active_logical_gib_price , 2 ) AS forecast_active_logical_cost , 
ROUND ( long_term_logical_gib * long_term_logical_gib_price , 2 ) AS forecast_long_term_logical_cost , 
-- Forecast costs physical 
ROUND (( active_no_tt_physical_gib + time_travel_physical_gib + fail_safe_physical_gib ) * active_physical_gib_price , 2 ) AS forecast_active_physical_cost , 
ROUND ( long_term_physical_gib * long_term_physical_gib_price , 2 ) AS forecast_long_term_physical_cost , 
-- Forecast costs total 
ROUND ((( active_logical_gib * active_logical_gib_price ) + ( long_term_logical_gib * long_term_logical_gib_price )) - 
((( active_no_tt_physical_gib + time_travel_physical_gib + fail_safe_physical_gib ) * active_physical_gib_price ) + ( long_term_physical_gib * long_term_physical_gib_price )), 2 ) AS forecast_total_cost_difference 
FROM 
storage_sizes 
ORDER BY 
( forecast_active_logical_cost + forecast_active_physical_cost ) DESC ; 
```


- 

Click **Run**.

The result is similar to the following:


```
+--------------+--------------------+-----------------------+---------------------+------------------------+--------------------------+-----------------------------+------------------------------+----------------------------------+-------------------------------+----------------------------------+--------------------------------+
| dataset_name | active_logical_gib | long_term_logical_gib | active_physical_gib | long_term_physical_gib | active_compression_ratio | long_term_compression_ratio | forecast_active_logical_cost | forecaset_long_term_logical_cost | forecast_active_physical_cost | forecast_long_term_physical_cost | forecast_total_cost_difference |
+--------------+--------------------+-----------------------+---------------------+------------------------+--------------------------+-----------------------------+------------------------------+----------------------------------+-------------------------------+----------------------------------+--------------------------------+
| dataset1 | 10.0 | 10.0 | 1.0 | 1.0 | 10.0 | 10.0 | 0.2 | 0.1 | 0.04 | 0.02 | 0.24 |
```


## Troubleshooting

To enable this view, you can set the value of
`enable_info_schema_storage` to `TRUE` on your project or organization. For more information on managing your
configuration, see [Manage configuration
settings](/bigquery/docs/default-configuration).

If you haven't configured this setting, you will see the following error:


```
INFORMATION_SCHEMA.TABLE_STORAGE hasn't been enabled for project .
Consider using one of the following SQL statements to enable data collection:
ALTER PROJECT ` `
SET OPTIONS (`region- .enable_info_schema_storage` = TRUE)

Or to enable for the entire organization:
ALTER ORGANIZATION
SET OPTIONS (`region- .enable_info_schema_storage` = TRUE)

After enabling, please allow around 1 day for the complete historical data to
become available.
```


Run the SQL statements described in the error message to enable the view.

### List tables in a dataset

You can list tables in datasets in the following ways:

- Using the Google Cloud Dedicated console.

- Using the bq command-line tool
[`bq ls`](/bigquery/docs/reference/bq-cli-reference#bq_ls) command.

- Calling the [`tables.list`](/bigquery/docs/reference/rest/v2/tables/list)
API method.

- Using the client libraries.

#### Required permissions

At a minimum, to list tables in a dataset, you must be granted
`bigquery.tables.list` permissions. The following predefined IAM
roles include `bigquery.tables.list` permissions:

- `bigquery.user`

- `bigquery.metadataViewer`

- `bigquery.dataViewer`

- `bigquery.dataEditor`

- `bigquery.dataOwner`

- `bigquery.admin`

For more information on IAM roles and permissions in
BigQuery, see [Access control](/bigquery/access-control).

#### List tables

To list the tables in a dataset:


[ Console ](#console) [ bq ](#bq) [ API ](#api) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Node.js ](#node.js) [ PHP ](#php) [ Python ](#python) [ Ruby ](#ruby) 
More 




- 

In the Google Cloud Dedicated console, in the navigation pane, click your dataset
to expand it. This displays the tables and views in the dataset.

- 

Scroll through the list to see the tables in the dataset. Tables and
views are identified by different icons.




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

Issue the [`bq ls`](/bigquery/docs/reference/bq-cli-reference#bq_ls)
command. The `--format` flag can be used to control the
output. If you are listing tables in a project other than your default
project, add the project ID to the dataset in the following format:
`project_id:dataset`.

Additional flags include:

- `--max_results` or `-n`: An integer indicating the maximum number of
results. The default value is `50`.


```
[bq ls](/bigquery/docs/reference/bq-cli-reference#bq_ls) \ 
--format = pretty \ 
--max_results integer \ 
project_id:dataset 
```


Where:

- integer is an integer representing the number of tables to
list.

- project_id is your project ID.

- dataset is the name of the dataset.

When you run the command, the `Type` field displays either `TABLE` or
`VIEW`. For example:


```
+-------------------------+-------+----------------------+-------------------+
| tableId | Type | Labels | Time Partitioning |
+-------------------------+-------+----------------------+-------------------+
| mytable | TABLE | department:shipping | |
| myview | VIEW | | |
+-------------------------+-------+----------------------+-------------------+
```


Examples:

Enter the following command to list tables in dataset `mydataset` in your
default project.


```
[bq ls](/bigquery/docs/reference/bq-cli-reference#bq_ls) --format = pretty mydataset
```


Enter the following command to return more than the default output of 50
tables from `mydataset`. `mydataset` is in your default project.


```
[bq ls](/bigquery/docs/reference/bq-cli-reference#bq_ls) --format = pretty --max_results 60 mydataset
```


Enter the following command to list tables in dataset `mydataset` in
`myotherproject`.


```
[bq ls](/bigquery/docs/reference/bq-cli-reference#bq_ls) --format = pretty myotherproject:mydataset
```





To list tables using the API, call the [`tables.list`](/bigquery/docs/reference/rest/v2/tables/list)
method.

































Before trying this sample, follow the C# setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery C# API
reference documentation](/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
using [ Google.Cloud.BigQuery.V2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html) ; 
using System ; 
using System.Collections.Generic ; 
using System.Linq ; 

public class BigQueryListTables 
{ 
public void ListTables ( 
string projectId = "your-project-id" , 
string datasetId = "your_dataset_id" 
) 
{ 
[ BigQueryClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) client = [ BigQueryClient ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) . [ Create ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_) ( projectId ); 
// Retrieve list of tables in the dataset 
List tables = client . [ ListTables ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_ListTables_Google_Apis_Bigquery_v2_Data_DatasetReference_Google_Cloud_BigQuery_V2_ListTablesOptions_) ( datasetId ). ToList (); 
// Display the results 
if ( tables . Count > 0 ) 
{ 
Console . WriteLine ( $"Tables in dataset {datasetId}:" ); 
foreach ( var table in tables ) 
{ 
Console . WriteLine ( $"\t{table.Reference.TableId}" ); 
} 
} 
else 
{ 
Console . WriteLine ( $"{datasetId} does not contain any tables." ); 
} 
} 
} 
```

















































Before trying this sample, follow the Go setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Go API
reference documentation](https://godoc.org/cloud.google.com/go/bigquery).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import ( 
"context" 
"fmt" 
"io" 

"cloud.google.com/go/bigquery" 
"google.golang.org/api/iterator" 
) 

// listTables demonstrates iterating through the collection of tables in a given dataset. 
func listTables ( w io . Writer , projectID , datasetID string ) error { 
// projectID := "my-project-id" 
// datasetID := "mydataset" 
ctx := context . Background () 
client , err := bigquery . NewClient ( ctx , projectID ) 
if err != nil { 
return fmt . Errorf ( "bigquery.NewClient: %v" , err ) 
} 
defer client . Close () 

ts := client . Dataset ( datasetID ). [ Tables ](https://berlin.devsitetest.how/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Dataset_Tables) ( ctx ) 
for { 
t , err := ts . Next () 
if err == iterator . Done { 
break 
} 
if err != nil { 
return err 
} 
fmt . Fprintf ( w , "Table: %q\n" , t . TableID ) 
} 
return nil 
} 
```


















































Before trying this sample, follow the Java setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Java API
reference documentation](/java/docs/reference/google-cloud-bigquery/latest/overview).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import com.google.api.gax.paging.[Page](https://berlin.devsitetest.how/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) ; 
import com.google.cloud.bigquery.[BigQuery](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) ; 
import com.google.cloud.bigquery.[BigQuery](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html).[TableListOption](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableListOption.html) ; 
import com.google.cloud.bigquery.[BigQueryException](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) ; 
import com.google.cloud.bigquery.[BigQueryOptions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) ; 
import com.google.cloud.bigquery.[DatasetId](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html) ; 
import com.google.cloud.bigquery.[Table](https://berlin.devsitetest.how/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1.Table.html) ; 

public class ListTables { 

public static void runListTables () { 
// TODO(developer): Replace these variables before running the sample. 
String projectId = "bigquery-public-data" ; 
String datasetName = "samples" ; 
listTables ( projectId , datasetName ); 
} 

public static void listTables ( String projectId , String datasetName ) { 
try { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
[ BigQuery ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [ BigQueryOptions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html) . getDefaultInstance (). getService (); 

[ DatasetId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html) datasetId = [ DatasetId ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html) . of ( projectId , datasetName ); 
Page tables = bigquery . [ listTables ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_listTables_com_google_cloud_bigquery_DatasetId_com_google_cloud_bigquery_BigQuery_TableListOption____) ( datasetId , TableListOption . pageSize ( 100 )); 
tables . iterateAll (). forEach ( table - > System . out . print ( table . getTableId (). getTable () + "\n" )); 

System . out . println ( "Tables listed successfully." ); 
} catch ( [ BigQueryException ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e ) { 
System . out . println ( "Tables were not listed. Error occurred: " + e . toString ()); 
} 
} 
} 
```


















































Before trying this sample, follow the Node.js setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Node.js API
reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
// Import the Google Cloud client library 
const { BigQuery } = require ( '[@google-cloud/bigquery](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/overview.html)' ); 
const bigquery = new [ BigQuery ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html) (); 

async function listTables () { 
// Lists tables in 'my_dataset'. 

/** 
* TODO(developer): Uncomment the following lines before running the sample. 
*/ 
// const datasetId = 'my_dataset'; 

// List all tables in the dataset 
const [ tables ] = await bigquery . dataset ( datasetId ). [ getTables ](https://berlin.devsitetest.how/nodejs/docs/reference/bigquery/latest/bigquery/dataset.html) (); 

console . log ( 'Tables:' ); 
tables . forEach ( table = > console . log ( table . id )); 
} 
```

















































Before trying this sample, follow the PHP setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery PHP API
reference documentation](/php/docs/reference/cloud-bigquery/latest/BigQueryClient).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
use Google\Cloud\BigQuery\BigQueryClient; 

/** Uncomment and populate these variables in your code */ 
// $projectId = 'The Google project ID'; 
// $datasetId = 'The BigQuery dataset ID'; 

$bigQuery = new BigQueryClient([ 
'projectId' => $projectId, 
]); 
$dataset = $bigQuery->dataset($datasetId); 
$tables = $dataset->tables(); 
foreach ($tables as $table) { 
print($table->id() . PHP_EOL); 
} 
```


















































Before trying this sample, follow the Python setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Python API
reference documentation](/python/docs/reference/bigquery/latest).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
from google.cloud import [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest)

# Construct a BigQuery client object. 
client = [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html) () 

# TODO(developer): Set dataset_id to the ID of the dataset that contains 
# the tables you are listing. 
# dataset_id = 'your-project.your_dataset' 

tables = client . [ list_tables ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_list_tables) ( dataset_id ) # Make an API request. 

print ( "Tables contained in ' {} ':" . format ( dataset_id )) 
for table in tables : 
print ( " {} . {} . {} " . format ( table . project , table . dataset_id , table . table_id )) 
```


















































Before trying this sample, follow the Ruby setup instructions in the
[BigQuery quickstart using
client libraries](/bigquery/docs/quickstarts/quickstart-client-libraries).



For more information, see the
[BigQuery Ruby API
reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html).





To authenticate to BigQuery, set up Application Default Credentials.
For more information, see

[Set up authentication for client libraries](/bigquery/docs/authentication#client-libs).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
require "google/cloud/bigquery" 

def list_tables dataset_id = "your_dataset_id" 
bigquery = Google :: Cloud :: [ Bigquery ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Cloud-Bigquery.html) . [ new ](https://berlin.devsitetest.how/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html)
dataset = bigquery . dataset dataset_id 

puts "Tables in dataset #{ dataset_id } :" 
dataset . tables . each do | table | 
puts " \t #{ table . table_id } " 
end 
end 
```




















## Audit table history

You can audit the history of BigQuery tables by querying
Cloud Audit Logs in Logs Explorer. These logs help you track when tables were
created, updated, or deleted, and identify the user or service account that made
the changes.

### Required permissions

To browse audit logs, you need the `roles/logging.privateLogViewer`
role. For more information on IAM roles and permissions in
Cloud Logging, see [Access control with IAM](/logging/docs/access-control).

### Get audit data

You can access audit information from the Google Cloud Dedicated console, `gcloud` command
line, REST API, and all supported languages using client libraries. The logging
filter shown in the following example can be used regardless of method used.

- 

In the Google Cloud Dedicated console, go to the Logging** page.

[Go to Logging](https://console.cloud.berlin-build0.goog/logs)

- 

Use the following query to access the audit data:


```
logName = "projects/ PROJECT_ID /logs/cloudaudit.googleapis.com%2Factivity"
AND resource.type = "bigquery_dataset"
AND timestamp >= " STARTING_TIMESTAMP "
AND protoPayload.@type = "type.googleapis.com/google.cloud.audit.AuditLog"
AND (
protoPayload.metadata.tableCreation :*
OR protoPayload.metadata.tableChange :*
OR protoPayload.metadata.tableDeletion :*
)
AND protoPayload.resourceName : "projects/ PROJECT_ID /datasets/ DATASET_ID /tables/"
```


Replace the following:

- ` PROJECT_ID `: the project that contains datasets and tables
you are interested in.

- ` STARTING_TIMESTAMP `: the oldest logs that you want to see.
Use ISO 8601 format, such as `2025-01-01` or `2025-02-03T04:05:06Z`.

- ` DATASET_ID `: the dataset that you want to filter by.

#### Interpret the results

In the Logs Explorer result pane, expand the entry you're interested in,
and then click **Expand nested fields** to show the whole message.

The logging entry contains only one of the following objects to indicate
the operation performed:

- `protoPayload.metadata.tableCreation`: a table was created.

- `protoPayload.metadata.tableChange`: table metadata was changed, such as
schema update, description change, or table replacement.

- `protoPayload.metadata.tableDeletion`: a table was deleted.

The content of these objects describes the requested action.
For a detailed description, see
[`BigQueryAuditMetadata`](/bigquery/docs/reference/auditlogs/rest/Shared.Types/BigQueryAuditMetadata).

#### Explanation of the query

- `logName = "projects/ PROJECT_ID /logs/cloudaudit.googleapis.com%2Factivity"`:
This line filters for Admin Activity audit logs within your Google Cloud Dedicated in Germany
project. These logs record API calls and actions that modify the
configuration or metadata of your resources.

- `resource.type = "bigquery_dataset"`: This narrows the search to events
related to BigQuery datasets, where table operations are
logged.

- `timestamp >= " STARTING_TIMESTAMP "`: Filters log entries to
only show those created on or after the specified timestamp.

- `protoPayload.@type = "type.googleapis.com/google.cloud.audit.AuditLog"`:
Ensures the log message conforms to the standard Cloud Audit Log structure.

- `( ... )`: This block groups conditions to find different types of table
events, as outlined in the previous section. The `:*` operator indicates
that the key must be present. If you are interested in only one event,
such as table creation, remove unnecessary conditions from this block.

- 

`protoPayload.resourceName : "projects/ PROJECT_ID /datasets/ DATASET_ID /tables/"`:
Selects log entries matching tables contained in the specified dataset. The
colon (`:`) operator performs a substring search.

- To filter entries for a single table, replace the condition with the
following one: `protoPayload.resourceName = "projects/ PROJECT_ID /datasets/ DATASET_ID /tables/ TABLE_NAME "`.

- To include all tables in all datasets in the specific project, remove this
condition.

For more information on log filtering, see [logging query language](/logging/docs/view/logging-query-language).

## Table security

To control access to tables in BigQuery, see
[Control access to resources with IAM](/bigquery/docs/control-access-to-resources-iam).

## What's next

- For more information about datasets, see [Introduction to datasets](/bigquery/docs/datasets-intro).

- For more information about handling table data, see [Managing table data](/bigquery/docs/managing-table-data).

- For more information about specifying table schemas, see [Specifying a schema](/bigquery/docs/schemas).

- For more information about modifying table schemas, see
[Modifying table schemas](/bigquery/docs/managing-table-schemas).

- For more information about managing tables, see [Managing tables](/bigquery/docs/managing-tables).

- To see an overview of `INFORMATION_SCHEMA`, go to
[Introduction to BigQuery `INFORMATION_SCHEMA`](/bigquery/docs/information-schema-intro).