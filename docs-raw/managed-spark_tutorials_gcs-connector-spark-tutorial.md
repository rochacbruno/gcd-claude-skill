# Use the Cloud Storage connector with Apache Spark

Source: https://berlin.devsitetest.how/managed-spark/docs/tutorials/gcs-connector-spark-tutorial
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












# Use the Cloud Storage connector with Apache Spark 

















This tutorial show you how to run example code that uses the
[Cloud Storage connector](/managed-spark/docs/concepts/connectors/cloud-storage#clusters) with
[Apache Spark](https://spark.apache.org).

[Lightning Engine](https://berlin.devsitetest.how/products/lightning-engine?e=48754) enhances connectivity to Cloud Storage to optimize the
performance of its native engine. The improved Cloud Storage connector minimizes metadata operations
to reduce costs, while an optimized file output committer unlocks performance
and reliability for Spark workloads. Complete the
[Early Access](https://docs.google.com/forms/d/e/1FAIpQLSdkNW13znxnwskYuEgZ-BWLmyxbwg4aMnAU-Z2f3FGzYhHHmg/viewform?usp=header)
form to request early access to this private preview feature.








## Objectives


Write a simple wordcount Spark job in Java, Scala, or
Python, then run the job on a Managed Service for Apache Spark cluster.








## Costs








In this document, you use the following billable components of Google Cloud Dedicated in Germany:









- Compute Engine

- Managed Service for Apache Spark

- Cloud Storage



















## Before you begin



Run the steps below to prepare to run the code in this tutorial.

- 

**Set up your project.** If necessary, set up a project with the Managed Service for Apache Spark, Compute Engine,
and Cloud Storage APIs enabled and the Google Cloud CLI installed on your local machine.

















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




Enable the Dataproc, Compute Engine, and Cloud Storage APIs, if any are not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the APIs](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=dataproc,compute_component,storage-component.googleapis.com&redirect=https%3A//console.cloud.google.com)


















- 




Create a service account:







- 

Ensure that you have the Create Service Accounts IAM role
(`roles/iam.serviceAccountCreator`) and the Project IAM Admin role
(`roles/resourcemanager.projectIamAdmin`). [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).


- 


In the Google Cloud Dedicated console, go to the **Create service account** page.


[Go to Create service account](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)



- 
Select your project.



- 


In the **Service account name** field, enter a name. The Google Cloud Dedicated console fills
in the **Service account ID** field based on this name.




In the **Service account description** field, enter a description. For example,
`Service account for quickstart`.





- 
Click **Create and continue**.




- 



Grant the **Project > Owner** role to the service account.




To grant the role, find the **Select a role** list, then select
**Project > Owner**.












- 
Click **Continue**.






- 


Click **Done** to finish creating the service account.







Do not close your browser window. You will use it in the next step.
















- 




Create a service account key:








- 
In the Google Cloud Dedicated console, click the email address for the service account that you
created.



- 
Click **Keys**.



- 
Click **Add key**, and then click **Create new key**.



- 
Click **Create**. A JSON key file is downloaded to your computer.



- 
Click **Close**.
















- 



Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS`
to the path of the JSON file that contains your credentials.
This variable applies only to your current shell session, so if you open
a new session, set the variable again.





**Example:** Linux or macOS


```
export GOOGLE_APPLICATION_CREDENTIALS = "` KEY_PATH `" 
```



Replace ` KEY_PATH ` with the path of the JSON file that contains your credentials.



For example:


```
export GOOGLE_APPLICATION_CREDENTIALS = "/home/user/Downloads/service-account-file.json" 
```






**Example:** Windows



For PowerShell:


```
$env :GOOGLE_APPLICATION_CREDENTIALS = "` KEY_PATH `" 
```



Replace ` KEY_PATH ` with the path of the JSON file that contains your credentials.



For example:


```
$env :GOOGLE_APPLICATION_CREDENTIALS = "C:\Users\username\Downloads\service-account-file.json" 
```




For command prompt:


```
set GOOGLE_APPLICATION_CREDENTIALS = ` KEY_PATH `
```



Replace ` KEY_PATH ` with the path of the JSON file that contains your credentials.
















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

**Create a Cloud Storage bucket.** You need a Cloud Storage to hold tutorial data. If you do not have one
ready to use, create a new bucket in your project.





- 
In the Google Cloud Dedicated console, go to the Cloud Storage
**Buckets** page.


[Go to Buckets](https://console.cloud.berlin-build0.goog/storage/browser)

- 
Click add_box **Create**.

- On the **Create a bucket** page, enter your bucket information. To go to the next
step, click **Continue**.



- 


In the **Get started** section, do the following:



- Enter a globally unique name that meets the
[bucket naming requirements](/storage/docs/bucket-naming#requirements).


- To add a
[bucket label](/storage/docs/tags-and-labels#bucket-labels),
expand the **Labels** section ( expand_more ),
click *add_box*
**Add label**, and specify a `key` and a `value` for your label.






- 

In the **Choose where to store your data** section, do the following:



- Select a [Location type](/storage/docs/locations).

- Choose a location where your bucket's data is permanently stored from the **[Location type](/storage/docs/locations#available-locations)** drop-down menu.



- If you select the [dual-region](/storage/docs/locations#location-dr) location type, you can
also choose to enable [turbo replication](/storage/docs/availability-durability#turbo-replication) by using the
relevant checkbox.




- To set up [cross-bucket replication](/storage/docs/availability-durability#cross-bucket-replication), select
**Add cross-bucket replication via Storage Transfer Service** and
follow these steps:



#### Set up cross-bucket replication




- In the **Bucket** menu, select a bucket.

- 

In the **Replication settings** section,
click **Configure** to configure settings for the
replication job.



The **Configure cross-bucket replication** pane
appears.




- To filter objects to replicate by object name prefix,
enter a prefix that you want to include or exclude objects from, then click add 
**Add a prefix**.

- To set a storage class for the replicated objects,
select a storage class from the **Storage class** menu.
If you skip this step, the replicated objects will use the
destination bucket's storage class by default.

- Click **Done**.












- 

In the **Choose how to store your data** section, do the following:



- Select a [default storage class](/storage/docs/storage-classes) for the bucket or
[Autoclass](/storage/docs/autoclass) for automatic storage class management of your
bucket's data.


- To enable [hierarchical namespace](/storage/docs/hns-overview), in the
**Optimize storage for data-intensive workloads** section, select
**Enable hierarchical namespace on this bucket**.





- 
In the **Choose how to control access to objects** section, select
whether or not your bucket enforces [public access prevention](/storage/docs/public-access-prevention),
and select an [access control method](/storage/docs/access-control) for your bucket's objects.




- 
In the **Choose how to protect object data** section, do the
following:



- Select any of the options under **Data protection** that you
want to set for your bucket.



- To enable [soft delete](/storage/docs/soft-delete), click the
**Soft delete policy (For data recovery)** checkbox,
and specify the number of days you want to retain objects
after deletion.

- To set [Object Versioning](/storage/docs/object-versioning), click the
**Object versioning (For version control)** checkbox,
and specify the maximum number of versions per object and the number of days after which
the noncurrent versions expire.

- To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following:



- To enable [Object Retention Lock](/storage/docs/object-lock), click the
**Enable object retention** checkbox.

- To enable [Bucket Lock](/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.






- To choose how your object data will be encrypted, expand the
**Data encryption** section ( expand_more ), and select a
[**Data encryption** method](/storage/docs/encryption).





- 
Click **Create**.

- 

**Set local environment variables.** Set environment variables on your
local machine. Set your Google Cloud Dedicated project-id and the name of the
Cloud Storage bucket you will use for this tutorial. Also provide the
name and [region](/compute/docs/regions-zones#available)
of an existing or new Managed Service for Apache Spark cluster.
You can create a cluster to use in this tutorial in the next step.

```
PROJECT= project-id 
```


```
BUCKET_NAME= bucket-name 
```


```
CLUSTER= cluster-name 
```


```
REGION= cluster-region Example: "us-central1"
```


- 

**Create a Managed Service for Apache Spark cluster.** Run the command, below, to
create a [single-node](/managed-spark/docs/concepts/configuring-clusters/single-node-clusters)
Managed Service for Apache Spark cluster in the specified
[Compute Engine zone](/compute/docs/regions-zones).

```
gcloud dataproc clusters create ${CLUSTER} \
    --project=${PROJECT} \
    --region=${REGION} \
    --single-node
```


- 

**Copy public data to your Cloud Storage bucket.** Copy a public data
Shakespeare text snippet into the `input` folder of your
Cloud Storage bucket:

```
gcloud storage cp gs://pub/shakespeare/rose.txt \
    gs://${BUCKET_NAME}/input/rose.txt
```


- 

**Set up a [Java (Apache Maven)](/java/docs/setup#install_a_build_automation_tool),
[Scala (SBT)](https://www.scala-sbt.org/), or
[Python](/python/docs/setup#installing_python)
development environment.**







## Prepare the Spark wordcount job

Select a tab, below, to follow the steps to prepare a job package or file
to submit to your cluster. You can prepare one of the following job types;

- **[Spark job in Java](https://spark.apache.org/)**
using [Apache Maven](https://maven.apache.org/) to build a
[JAR](https://en.wikipedia.org/wiki/JAR) package

- **[Spark job in Scala](https://www.scala-lang.org/)** using
[SBT](https://www.scala-sbt.org/) to build a
[JAR](https://en.wikipedia.org/wiki/JAR) package

- **[Spark job in Python (PySpark)](https://archive.apache.org/dist/spark/docs/3.5.4/api/python/getting_started/index.html)**




### Java

- **Copy `pom.xml` file to your local machine.**
The following `pom.xml` file specifies Scala and Spark library
dependencies, which are given a `provided` scope to
indicate that the Managed Service for Apache Spark cluster will provide these
libraries at runtime. The `pom.xml` file does not specify a
Cloud Storage dependency because the connector implements the standard
HDFS interface. When a Spark job accesses Cloud Storage cluster files
(files with URIs that start with `gs://`), the system
automatically uses the Cloud Storage connector to access the
files in Cloud Storage


```
? xml version = "1.0" encoding = "UTF-8" ? >
project xmlns = "http://maven.apache.org/POM/4.0.0" 
xmlns : xsi = "http://www.w3.org/2001/XMLSchema-instance" 
xsi : schemaLocation = "http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd" >
modelVersion>4 .0.0 / modelVersion >

groupId>dataproc . codelab / groupId >
artifactId>word - count / artifactId >
version>1 .0 / version >

properties >
maven . compiler . source>1 .8 / maven . compiler . source >
maven . compiler . target>1 .8 / maven . compiler . target >
/ properties >

dependencies >
dependency >
groupId>org . scala - lang / groupId >
artifactId>scala - library / artifactId >
version> Scala version , for example , ` 2.11.8 ` / version >
scope>provided / scope >
/ dependency >
dependency >
groupId>org . apache . spark / groupId >
artifactId>spark - core_ Scala major . minor . version , for example , ` 2.11 ` / artifactId >
version> Spark version , for example , ` 2.3.1 ` / version >
scope>provided / scope >
/ dependency >
/ dependencies >
/ project >
```



- **Copy the `WordCount.java` code listed, below,
to your local machine.**



- Create a set of directories with the path
`src/main/java/managed-spark/codelab`:

```
mkdir -p src/main/java/managed-spark/codelab
```



- Copy `WordCount.java` to your local machine into
`src/main/java/managed-spark/codelab`:

```
cp WordCount.java src/main/java/managed-spark/codelab
```






`WordCount.java` is a Spark job in Java that reads text files
from Cloud Storage, performs a word count, then writes the text file
results to Cloud Storage.


```
package dataproc.codelab ; 

import java.util.Arrays ; 
import org.apache.spark.SparkConf ; 
import org.apache.spark.api.java.JavaPairRDD ; 
import org.apache.spark.api.java.JavaRDD ; 
import org.apache.spark.api.java.JavaSparkContext ; 
import scala.Tuple2 ; 

public class WordCount { 
public static void main ( String [] args ) { 
if ( args . length != 2 ) { 
throw new IllegalArgumentException ( "Exactly 2 arguments are required: " ); 
} 
String inputPath = args [ 0 ] ; 
String outputPath = args [ 1 ] ; 
JavaSparkContext sparkContext = new JavaSparkContext ( new SparkConf (). setAppName ( "Word Count" )); 
JavaRDD lines = sparkContext . textFile ( inputPath ); 
JavaRDD words = lines . flatMap ( 
( String line ) - > Arrays . asList ( line . split ( " " )). iterator () 
); 
JavaPairRDD , Integer > wordCounts = words . mapToPair ( 
( String word ) - > new Tuple2 <> ( word , 1 ) 
). reduceByKey ( 
( Integer count1 , Integer count2 ) - > count1 + count2 
); 
wordCounts . saveAsTextFile ( outputPath ); 
} 
} 
```


- **Build the package.**

```
mvn clean package
```

If the build is successful, a `target/word-count-1.0.jar`
is created.

- **Stage the package to Cloud Storage.**

```
gcloud storage cp target/word-count-1.0.jar \
    gs://${BUCKET_NAME}/java/word-count-1.0.jar
```






### Scala

- **Copy `build.sbt` file to your local machine.**
The following `build.sbt` file specifies Scala and Spark library
dependencies, which are given a `provided` scope to
indicate that the Managed Service for Apache Spark cluster will provide these
libraries at runtime. The `build.sbt` file does not specify a
Cloud Storage dependency because the connector implements the standard
HDFS interface. When a Spark job accesses Cloud Storage cluster files
(files with URIs that start with `gs://`), the system
automatically uses the Cloud Storage connector to access the
files in Cloud Storage


```
scalaVersion := " Scala version, for example, `2.11.8` " 

name := "word-count" 
organization := "dataproc.codelab" 
version := "1.0" 

libraryDependencies ++ = Seq ( 
"org.scala-lang" % "scala-library" % scalaVersion . value % "provided" , 
"org.apache.spark" %% "spark-core" % " Spark version, for example, `2.3.1` " % "provided" 
) 
```


- **Copy `word-count.scala` to your local machine.**
This is a Spark job in Java that reads text files from
Cloud Storage, performs a word count, then writes
the text file results to Cloud Storage.

```
package dataproc.codelab 

import org.apache.spark.SparkContext 
import org.apache.spark.SparkConf 

object WordCount { 
def main ( args : Array [ String ] ) { 
if ( args . length != 2 ) { 
throw new IllegalArgumentException ( 
"Exactly 2 arguments are required: " ) 
} 

val inputPath = args ( 0 ) 
val outputPath = args ( 1 ) 

val sc = new SparkContext ( new SparkConf (). setAppName ( "Word Count" )) 
val lines = sc . textFile ( inputPath ) 
val words = lines . flatMap ( line = > line . split ( " " )) 
val wordCounts = words . map ( word = > ( word , 1 )). reduceByKey ( _ + _ ) 
wordCounts . saveAsTextFile ( outputPath ) 
} 
} 
```


- **Build the package.**

```
sbt clean package
```

If the build is successful, a `target/scala-2.11/word-count_2.11-1.0.jar`
is created.

- **Stage the package to Cloud Storage.**

```
gcloud storage cp target/scala-2.11/word-count_2.11-1.0.jar \
    gs://${BUCKET_NAME}/scala/word-count_2.11-1.0.jar
```






### Python


- **Copy `word-count.py` to your local machine.**
This is a Spark job in Python using PySpark that reads text files from
Cloud Storage, performs a word count, then writes
the text file results to Cloud Storage.

```
# !/ usr / bin / env python 

import pyspark 
import sys 

if len ( sys . argv ) != 3 : 
raise Exception ( "Exactly 2 arguments are required: " ) 

inputUri = sys . argv [ 1 ] 
outputUri = sys . argv [ 2 ] 

sc = pyspark . SparkContext () 
lines = sc . textFile ( sys . argv [ 1 ] ) 
words = lines . flatMap ( lambda line : line . split ()) 
wordCounts = words . map ( lambda word : ( word , 1 )). reduceByKey ( lambda count1 , count2 : count1 + count2 ) 
wordCounts . saveAsTextFile ( sys . argv [ 2 ] ) 
```





## Submit the job

Run the following `gcloud` command to submit the wordcount job to your
Managed Service for Apache Spark cluster.




### Java


```
gcloud dataproc jobs submit spark \
    --cluster=${CLUSTER} \
    --class=dataproc.codelab.WordCount \
    --jars=gs://${BUCKET_NAME}/java/word-count-1.0.jar \
    --region=${REGION} \
    -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
```





### Scala


```
gcloud dataproc jobs submit spark \
    --cluster=${CLUSTER} \
    --class=dataproc.codelab.WordCount \
    --jars=gs://${BUCKET_NAME}/scala/word-count_2.11-1.0.jar \
    --region=${REGION} \
    -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
```





### Python


```
gcloud dataproc jobs submit pyspark word-count.py \
    --cluster=${CLUSTER} \
    --region=${REGION} \
    -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
```




## View the output

After the job finishes, run the following gcloud CLI
command to view the wordcount output.


```
gcloud storage cat gs://${BUCKET_NAME}/output/*
```


The wordcount output should be similar to the following:

```
(a,2)
(call,1)
(What's,1)
(sweet.,1)
(we,1)
(as,1)
(name?,1)
(any,1)
(other,1)
(rose,1)
(smell,1)
(name,1)
(would,1)
(in,1)
(which,1)
(That,1)
(By,1)
```









## Clean up




After you finish the tutorial, you can clean up the resources that you created so that they
stop using quota and incurring charges. The following sections describe how to delete or turn off
these resources.

### Delete the project

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




### Delete the Managed Service for Apache Spark cluster

Instead of deleting your project, you might want to only [delete your cluster](/managed-spark/docs/guides/manage-cluster#deleting_a_cluster) within the project.

### Delete the Cloud Storage bucket








### Google Cloud Dedicated console





- 
In the Google Cloud Dedicated console, go to the Cloud Storage
**Buckets** page.


[Go to Buckets](https://console.cloud.berlin-build0.goog/storage/browser)



- 
Click the checkbox for the bucket that you want to delete.


- 
To delete the bucket,
click delete **Delete**, and then follow the
instructions.











### Command line






Delete the bucket:

```
gcloud storage buckets delete BUCKET_NAME 
```

















## What's next



- See [Spark job tuning tips](/managed-spark/docs/support/spark-job-tuning)