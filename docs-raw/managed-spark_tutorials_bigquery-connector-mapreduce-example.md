# Write a MapReduce job with the BigQuery connector

Source: https://berlin.devsitetest.how/managed-spark/docs/tutorials/bigquery-connector-mapreduce-example
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/managed-spark/docs/tpc-differences) for more details.














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

Managed Service for Apache Spark

](https://berlin.devsitetest.how/managed-spark/docs)






- 








[

Guides

](https://berlin.devsitetest.how/managed-spark/docs/overview/key-concepts)












# Write a MapReduce job with the BigQuery connector 


















The Hadoop BigQuery connector is installed by default on all
Managed Service for Apache Spark 1.0-1.2 cluster nodes under `/usr/lib/hadoop/lib/`.
It is available in both Spark and PySpark environments.

**Managed Service for Apache Spark image versions 1.5+:** The BigQuery
connector is not installed by default in Managed Service for Apache Spark
[image versions 1.5 and higher](/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions).
To use it with these versions:

- 

Install the BigQuery connector using this
[initialization action](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/connectors).

- 

Specify the BigQuery connector in the `jars` parameter when
submitting a job:

```
--jars = gs://hadoop-lib/bigquery/bigquery-connector-hadoop3-latest.jar
```


- 

Include the BigQuery connector classes in the application's
jar-with-dependencies.

**To Avoid Conflicts**: If your application uses a connector version that is
different from the [connector version deployed on your Managed Service for Apache Spark cluster](/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions),
you must either:

- 

Create a new cluster with an
[initialization action](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/connectors) that installs the connector version used by your application, or

- 

Include and
[relocate](https://maven.apache.org/plugins/maven-shade-plugin/examples/class-relocation.html) 
the connector classes and connector dependencies for the version you are
using into your application's jar to avoid conflict between your connector
version and the connector version deployed on your Managed Service for Apache Spark
cluster (see this
[example of dependencies relocation in Maven](https://github.com/GoogleCloudDataproc/hadoop-connectors/blob/a839bd8f237197f98808944ca52d03de96518314/bigquery/pom.xml#L227-L286)).

## GsonBigQueryInputFormat class

`GsonBigQueryInputFormat` provides Hadoop with the BigQuery
objects in a JsonObject format via the following primary
operations:


- Using a user-specified query to select
BigQuery objects


- Splitting the results of the query evenly among Hadoop
nodes


- Parsing the splits into Java objects to pass to the Mapper.
The Hadoop Mapper class receives a `JsonObject` representation of
each selected BigQuery object.

The `BigQueryInputFormat` class provides access to BigQuery records through an extension of the
Hadoop
[InputFormat](http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/InputFormat.html)
class. To use the BigQueryInputFormat class:

- 

Lines must be added to the main Hadoop job to set parameters in the Hadoop
configuration.

- 

The
[InputFormat](http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/InputFormat.html)
class must be set to `GsonBigQueryInputFormat`.

The sections, below, show you how to meet these requirements.

## Input Parameters


QualifiedInputTableId 
The BigQuery table to read from, in the form:
optional-projectId : datasetId . tableId 

**Example:**
`publicdata:samples.shakespeare` 
projectId 
The BigQuery projectId under which all of the input
operations occur.

**Example:**
`my-first-cloud-project` 



```
// Set the job-level projectId. 
conf . set ( BigQueryConfiguration . PROJECT_ID_KEY , projectId ); 

// Configure input parameters. 
BigQueryConfiguration . configureBigQueryInput ( conf , inputQualifiedTableId ); 

// Set InputFormat. 
job . setInputFormatClass ( GsonBigQueryInputFormat . class ); 
```


Notes:

- `job` refers to the `org.apache.hadoop.mapreduce.Job`, the Hadoop job to
run.

- `conf` refers to the `org.apache.hadoop.Configuration` for the Hadoop job.

## Mapper

The `GsonBigQueryInputFormat` class reads from BigQuery and passes
BigQuery objects one at a time as input to the Hadoop `Mapper`
function. The inputs take the form of a pair comprising the following:

- `LongWritable`, the record number

- `JsonObject`, the Json-formatted BigQuery record

The `Mapper` accepts the `LongWritable` and `JsonObject pair` as
input.

Here is a snippet from the `Mapper` for a
[sample WordCount](#completecode) job.


```
// private static final LongWritable ONE = new LongWritable ( 1 ); 
// The configuration key used to specify the BigQuery field name 
// ( "column name" ) . 
public static final String WORDCOUNT_WORD_FIELDNAME_KEY = 
"mapred.bq.samples.wordcount.word.key" ; 

// Default value for the configuration entry specified by 
// WORDCOUNT_WORD_FIELDNAME_KEY . Examples : 'word' in 
// publicdata : samples . shakespeare or 'repository_name' 
// in publicdata : samples . github_timeline . 
public static final String WORDCOUNT_WORD_FIELDNAME_VALUE_DEFAULT = "word" ; 

/** 
* The mapper function for WordCount . 
*/ 
public static class Map 
extends Mapper LongWritable , JsonObject , Text , LongWritable > { 
private static final LongWritable ONE = new LongWritable ( 1 ); 
private Text word = new Text (); 
private String wordKey ; 

@ Override 
public void setup ( Context context ) 
throws IOException , InterruptedException { 
// Find the runtime - configured key for the field name we 're looking for 
// in the map task . 
Configuration conf = context . getConfiguration (); 
wordKey = conf . get ( WORDCOUNT_WORD_FIELDNAME_KEY , 
WORDCOUNT_WORD_FIELDNAME_VALUE_DEFAULT ); 
} 

@ Override 
public void map ( LongWritable key , JsonObject value , Context context ) 
throws IOException , InterruptedException { 
JsonElement countElement = value . get ( wordKey ); 
if ( countElement != null ) { 
String wordInRecord = countElement . getAsString (); 
word . set ( wordInRecord ); 
// Write out the key , value pair ( write out a value of 1 , which will be 
// added to the total count for this word in the Reducer ) . 
context . write ( word , ONE ); 
} 
} 
} 
```


## IndirectBigQueryOutputFormat class

`IndirectBigQueryOutputFormat` provides Hadoop with the ability to write
`JsonObject` values directly into a BigQuery table. This class provides access
to BigQuery records through an extension of the Hadoop
[OutputFormat](http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/OutputFormat.html) 
class. To use it correctly, several parameters must be set in the Hadoop
configuration, and the OutputFormat class must be set to
`IndirectBigQueryOutputFormat`. Below is an example of the
parameters to set and the lines of code needed to correctly use
`IndirectBigQueryOutputFormat`.

## Output Parameters


projectId 

The BigQuery projectId under which all of the output
operations occur.

**Example**:
"my-first-cloud-project" 

QualifiedOutputTableId 

The BigQuery dataset to write the final job results to, in
the form optional-projectId : datasetId . tableId .
The datasetId should already be present in your project.
outputDatasetId _hadoop_temporary dataset will be created in
BigQuery for temporary results. Make sure this does not conflict
with an existing dataset.

**Examples**:

`test_output_dataset.wordcount_output`

`my-first-cloud-project:test_output_dataset.wordcount_output` 
outputTableFieldSchema 
A schema that defines the schema for the output BigQuery table 
GcsOutputPath 
The output path to store temporary Cloud Storage data (`gs:// bucket/dir/ `) 



```
// Define the schema we will be using for the output BigQuery table. 
List outputTableFieldSchema = new ArrayList (); 
outputTableFieldSchema . add ( new TableFieldSchema (). setName ( "Word" ). setType ( "STRING" )); 
outputTableFieldSchema . add ( new TableFieldSchema (). setName ( "Count" ). setType ( "INTEGER" )); 
TableSchema outputSchema = new TableSchema (). setFields ( outputTableFieldSchema ); 

// Create the job and get its configuration. 
Job job = new Job ( parser . getConfiguration (), "wordcount" ); 
Configuration conf = job . getConfiguration (); 

// Set the job-level projectId. 
conf . set ( BigQueryConfiguration . PROJECT_ID_KEY , projectId ); 

// Configure input. 
BigQueryConfiguration . configureBigQueryInput ( conf , inputQualifiedTableId ); 

// Configure output. 
BigQueryOutputConfiguration . configure ( 
conf , 
outputQualifiedTableId , 
outputSchema , 
outputGcsPath , 
BigQueryFileFormat . NEWLINE_DELIMITED_JSON , 
TextOutputFormat . class ); 

// (Optional) Configure the KMS key used to encrypt the output table. 
BigQueryOutputConfiguration . setKmsKeyName ( 
conf , 
"projects/myproject/locations/us-west1/keyRings/r1/cryptoKeys/k1" ); 
); 
```


## Reducer

The `IndirectBigQueryOutputFormat` class writes to BigQuery.
It takes a key and a `JsonObject` value as input and writes only the
JsonObject value to BigQuery (the key is ignored). The `JsonObject` should
contain a Json-formatted BigQuery record. The Reducer should output a key of
any type (`NullWritable` is used in our [sample WordCount](#completecode) job)
and `JsonObject` value pair. The Reducer for the
sample WordCount job is shown below.


```
/** 
* Reducer function for WordCount . 
*/ 
public static class Reduce 
extends Reducer , LongWritable , JsonObject , NullWritable > { 

@ Override 
public void reduce ( Text key , Iterable values , Context context ) 
throws IOException , InterruptedException { 
// Add up the values to get a total number of occurrences of our word . 
long count = 0 ; 
for ( LongWritable val : values ) { 
count = count + val . get (); 
} 

JsonObject jsonObject = new JsonObject (); 
jsonObject . addProperty ( "Word" , key . toString ()); 
jsonObject . addProperty ( "Count" , count ); 
// Key does not matter . 
context . write ( jsonObject , NullWritable . get ()); 
} 
} 
```


## Clean up

After the job completes, clean up Cloud Storage export paths.


```
job.waitForCompletion(true);
GsonBigQueryInputFormat.cleanupJob(job.getConfiguration(), job.getJobID());
```


You can view word counts in the BigQuery output table in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/bigquery).

## Complete Code for a sample WordCount job

The code below is an example of a simple WordCount job that
aggregates word counts from objects in BigQuery.


```
package com . google . cloud . hadoop . io . bigquery . samples ; 

import com.google.api.services.bigquery.model.TableFieldSchema ; 
import com.google.api.services.bigquery.model.TableSchema ; 
import com.google.cloud.hadoop.io.bigquery.BigQueryConfiguration ; 
import com.google.cloud.hadoop.io.bigquery.BigQueryFileFormat ; 
import com.google.cloud.hadoop.io.bigquery.GsonBigQueryInputFormat ; 
import com.google.cloud.hadoop.io.bigquery.output.BigQueryOutputConfiguration ; 
import com.google.cloud.hadoop.io.bigquery.output.IndirectBigQueryOutputFormat ; 
import com.google.gson.JsonElement ; 
import com.google.gson.JsonObject ; 

import org.apache.hadoop.conf.Configuration ; 
import org.apache.hadoop.io.LongWritable ; 
import org.apache.hadoop.io.NullWritable ; 
import org.apache.hadoop.io.Text ; 
import org.apache.hadoop.mapreduce.Job ; 
import org.apache.hadoop.mapreduce.Mapper ; 
import org.apache.hadoop.mapreduce.Reducer ; 
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat ; 
import org.apache.hadoop.util.GenericOptionsParser ; 

import java.io.IOException ; 
import java.util.ArrayList ; 
import java.util.List ; 

/** 
* Sample program to run the Hadoop Wordcount example over tables in BigQuery . 
*/ 
public class WordCount { 

// The configuration key used to specify the BigQuery field name 
// ( "column name" ) . 
public static final String WORDCOUNT_WORD_FIELDNAME_KEY = 
"mapred.bq.samples.wordcount.word.key" ; 

// Default value for the configuration entry specified by 
// WORDCOUNT_WORD_FIELDNAME_KEY . Examples : 'word' in 
// publicdata : samples . shakespeare or 'repository_name' 
// in publicdata : samples . github_timeline . 
public static final String WORDCOUNT_WORD_FIELDNAME_VALUE_DEFAULT = "word" ; 

// Guava might not be available , so define a null / empty helper : 
private static boolean isStringNullOrEmpty ( String toTest ) { 
return toTest == null || "" . equals ( toTest ); 
} 

/** 
* The mapper function for WordCount . For input , it consumes a LongWritable 
* and JsonObject as the key and value . These correspond to a row identifier 
* and Json representation of the row 's values/columns. 
* For output , it produces Text and a LongWritable as the key and value . 
* These correspond to the word and a count for the number of times it has 
* occurred . 
*/ 

public static class Map 
extends Mapper LongWritable , JsonObject , Text , LongWritable > { 
private static final LongWritable ONE = new LongWritable ( 1 ); 
private Text word = new Text (); 
private String wordKey ; 

@Override 
public void setup ( Context context ) 
throws IOException , InterruptedException { 
// Find the runtime - configured key for the field name we 're looking for in 
// the map task . 
Configuration conf = context . getConfiguration (); 
wordKey = conf . get ( WORDCOUNT_WORD_FIELDNAME_KEY , WORDCOUNT_WORD_FIELDNAME_VALUE_DEFAULT ); 
} 

@Override 
public void map ( LongWritable key , JsonObject value , Context context ) 
throws IOException , InterruptedException { 
JsonElement countElement = value . get ( wordKey ); 
if ( countElement != null ) { 
String wordInRecord = countElement . getAsString (); 
word . set ( wordInRecord ); 
// Write out the key , value pair ( write out a value of 1 , which will be 
// added to the total count for this word in the Reducer ) . 
context . write ( word , ONE ); 
} 
} 
} 

/** 
* Reducer function for WordCount . For input , it consumes the Text and 
* LongWritable that the mapper produced . For output , it produces a JsonObject 
* and NullWritable . The JsonObject represents the data that will be 
* loaded into BigQuery . 
*/ 
public static class Reduce 
extends Reducer , LongWritable , JsonObject , NullWritable > { 

@Override 
public void reduce ( Text key , Iterable values , Context context ) 
throws IOException , InterruptedException { 
// Add up the values to get a total number of occurrences of our word . 
long count = 0 ; 
for ( LongWritable val : values ) { 
count = count + val . get (); 
} 

JsonObject jsonObject = new JsonObject (); 
jsonObject . addProperty ( "Word" , key . toString ()); 
jsonObject . addProperty ( "Count" , count ); 
// Key does not matter . 
context . write ( jsonObject , NullWritable . get ()); 
} 
} 

/** 
* Configures and runs the main Hadoop job . Takes a String [] of 5 parameters : 
* [ ProjectId ] [ QualifiedInputTableId ] [ InputTableFieldName ] 
* [ QualifiedOutputTableId ] [ GcsOutputPath ] 
* 
* ProjectId - Project under which to issue the BigQuery 
* operations . Also serves as the default project for table IDs that don 't 
* specify a project for the table . 
* 
* QualifiedInputTableId - Input table ID of the form 
* ( Optional ProjectId ):[ DatasetId ] . [ TableId ] 
* 
* InputTableFieldName - Name of the field to count in the 
* input table , e . g . , 'word' in publicdata : samples . shakespeare or 
* 'repository_name' in publicdata : samples . github_timeline . 
* 
* QualifiedOutputTableId - Input table ID of the form 
* ( Optional ProjectId ):[ DatasetId ] . [ TableId ] 
* 
* GcsOutputPath - The output path to store temporary 
* Cloud Storage data , e . g . , gs : // bucket / dir / 
* 
* @param args a String [] containing ProjectId , QualifiedInputTableId , 
* InputTableFieldName , QualifiedOutputTableId , and GcsOutputPath . 
* @throws IOException on IO Error . 
* @throws InterruptedException on Interrupt . 
* @throws ClassNotFoundException if not all classes are present . 
*/ 
public static void main ( String [] args ) 
throws IOException , InterruptedException , ClassNotFoundException { 

// GenericOptionsParser is a utility to parse command line arguments 
// generic to the Hadoop framework . This example doesn 't cover the specifics, 
// but recognizes several standard command line arguments , enabling 
// applications to easily specify a NameNode , a ResourceManager , additional 
// configuration resources , etc . 
GenericOptionsParser parser = new GenericOptionsParser ( args ); 
args = parser . getRemainingArgs (); 

// Make sure we have the right parameters . 
if ( args . length != 5 ) { 
System . out . println ( 
"Usage: hadoop jar bigquery_wordcount.jar [ProjectId] [QualifiedInputTableId] " 
+ "[InputTableFieldName] [QualifiedOutputTableId] [GcsOutputPath] \n " 
+ " ProjectId - Project under which to issue the BigQuery operations. Also serves " 
+ "as the default project for table IDs that don't explicitly specify a project for " 
+ "the table. \n " 
+ " QualifiedInputTableId - Input table ID of the form " 
+ "(Optional ProjectId):[DatasetId].[TableId] \n " 
+ " InputTableFieldName - Name of the field to count in the input table, e.g., " 
+ "'word' in publicdata:samples.shakespeare or 'repository_name' in " 
+ "publicdata:samples.github_timeline. \n " 
+ " QualifiedOutputTableId - Input table ID of the form " 
+ "(Optional ProjectId):[DatasetId].[TableId] \n " 
+ " GcsOutputPath - The output path to store temporary Cloud Storage data, e.g., " 
+ "gs://bucket/dir/" ); 
System . exit ( 1 ); 
} 

// Get the individual parameters from the command line . 
String projectId = args [ 0 ]; 
String inputQualifiedTableId = args [ 1 ]; 
String inputTableFieldId = args [ 2 ]; 
String outputQualifiedTableId = args [ 3 ]; 
String outputGcsPath = args [ 4 ]; 

// Define the schema we will be using for the output BigQuery table . 
List outputTableFieldSchema = new ArrayList (); 
outputTableFieldSchema . add ( new TableFieldSchema () . setName ( "Word" ) . setType ( "STRING" )); 
outputTableFieldSchema . add ( new TableFieldSchema () . setName ( "Count" ) . setType ( "INTEGER" )); 
TableSchema outputSchema = new TableSchema () . setFields ( outputTableFieldSchema ); 

// Create the job and get its configuration . 
Job job = new Job ( parser . getConfiguration (), "wordcount" ); 
Configuration conf = job . getConfiguration (); 

// Set the job - level projectId . 
conf . set ( BigQueryConfiguration . PROJECT_ID_KEY , projectId ); 

// Configure input . 
BigQueryConfiguration . configureBigQueryInput ( conf , inputQualifiedTableId ); 

// Configure output . 
BigQueryOutputConfiguration . configure ( 
conf , 
outputQualifiedTableId , 
outputSchema , 
outputGcsPath , 
BigQueryFileFormat . NEWLINE_DELIMITED_JSON , 
TextOutputFormat . class ); 

// ( Optional ) Configure the KMS key used to encrypt the output table . 
BigQueryOutputConfiguration . setKmsKeyName ( 
conf , 
"projects/myproject/locations/us-west1/keyRings/r1/cryptoKeys/k1" ); 

conf . set ( WORDCOUNT_WORD_FIELDNAME_KEY , inputTableFieldId ); 

// This helps Hadoop identify the Jar which contains the mapper and reducer 
// by specifying a class in that Jar . This is required if the jar is being 
// passed on the command line to Hadoop . 
job . setJarByClass ( WordCount . class ); 

// Tell the job what data the mapper will output . 
job . setOutputKeyClass ( Text . class ); 
job . setOutputValueClass ( LongWritable . class ); 
job . setMapperClass ( Map . class ); 
job . setReducerClass ( Reduce . class ); 
job . setInputFormatClass ( GsonBigQueryInputFormat . class ); 

// Instead of using BigQueryOutputFormat , we use the newer 
// IndirectBigQueryOutputFormat , which works by first buffering all the data 
// into a Cloud Storage temporary file , and then on commitJob , copies all data from 
// Cloud Storage into BigQuery in one operation . Its use is recommended for large jobs 
// since it only requires one BigQuery "load" job per Hadoop / Spark job , as 
// compared to BigQueryOutputFormat , which performs one BigQuery job for each 
// Hadoop / Spark task . 
job . setOutputFormatClass ( IndirectBigQueryOutputFormat . class ); 

job . waitForCompletion ( true ); 

// After the job completes , clean up the Cloud Storage export paths . 
GsonBigQueryInputFormat . cleanupJob ( job . getConfiguration (), job . getJobID ()); 

// You can view word counts in the BigQuery output table at 
// https://console.cloud.berlin-build0.goog/ . 
} 
} 
```


## Java version

The BigQuery connector requires Java 8.

### [Apache Maven Dependency](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Dependency_Management) Information


```

com.google.cloud.bigdataoss 
bigquery-connector 
[insert "hadoopX-X.X.X" connector version number here](https://search.maven.org/search?q=g:com.google.cloud.bigdataoss%20AND%20a:bigquery-connector%20AND%20v:hadoop*) 

```


For detailed information, see the BigQuery connector
[release notes](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases) 
and [Javadoc reference](http://www.javadoc.io/doc/com.google.cloud.bigdataoss/bigquery-connector/).