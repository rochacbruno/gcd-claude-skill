# Quickstart: Create a cluster by using the Cloud de Confiance console

Source: https://documentation.s3ns.fr/managed-spark/docs/quickstarts/update-cluster-console
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/managed-spark/docs/tpc-differences) for more details.














- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Documentation

](https://documentation.s3ns.fr/docs)






- 








[

Data analytics

](https://documentation.s3ns.fr/docs/data)






- 








[

Managed Service for Apache Spark

](https://documentation.s3ns.fr/managed-spark/docs)






- 








[

Guides

](https://documentation.s3ns.fr/managed-spark/docs/overview/key-concepts)


























# Create a cluster by using the Cloud de Confiance console




This page shows you how to use the Cloud de Confiance console to create a
Managed Service for Apache Spark cluster, run a basic [Apache
Spark](http://spark.apache.org/) job in the cluster, and then modify the number
of workers in the cluster.





## Before you begin






















- 




In the Cloud de Confiance console, on the project selector page,
select or create a Cloud de Confiance project.





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












[Go to project selector](https://console.cloud.s3nscloud.fr/projectselector2/home/dashboard)











- 


[Verify that
you have the permissions required to complete this guide](#required_roles).










- 



[Verify that billing is enabled for your Cloud de Confiance project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the Dataproc API, if it is not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.s3nscloud.fr/apis/enableflow?apiid=dataproc.googleapis.com)












### Required roles

Certain Identity and Access Management (IAM) roles are required to
run the examples on this page. Depending on organization policies, these
roles may have already been granted. To check role grants, see
[Do you need to grant roles?](/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

For more information about granting roles, see
[Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).

#### User roles











































To get the permissions that
you need to create a Managed Service for Apache Spark cluster,

ask your administrator to grant you the
following IAM roles:













- [Dataproc Editor ](/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)
on the project


- [Service Account User ](/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
on the Compute Engine default service account





















#### Service account role


































To ensure that the Compute Engine default service account has the necessary
permissions to create a Managed Service for Apache Spark cluster,

ask your administrator to grant the
following IAM roles to the Compute Engine default service account on the project:














- 
All:
[Dataproc Worker ](/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)



























## Create a cluster

- 

In the Cloud de Confiance console, go to the Managed Service for Apache Spark
**Clusters** page.

[Go to Clusters](https://console.cloud.s3nscloud.fr/dataproc/clusters) 

- 

Click **Create cluster**.

- 

In the **Create Dataproc cluster** dialog, click **Create** in the **Cluster
on Compute Engine** row.

- 

In the **Cluster name** field, enter `example-cluster`.

- 

In the **Region** and **Zone** lists, select a region and zone.

Select a region (for example, `us-east1` or `europe-west1`) to isolate
resources, such as virtual machine (VM) instances and Cloud Storage and
metadata storage locations that are used by
Managed Service for Apache Spark, in the region. For more information, see
[Available regions and zones](/compute/docs/regions-zones/regions-zones#available) 
and [Cluster region](/managed-spark/docs/concepts/cluster-region) 

- 

For all the other options, use the default settings.

- 

To create the cluster, click **Create**.

Your new cluster appears in a list on the **Clusters** page. The status is
**Provisioning** until the cluster is ready to use, and then the status
changes to **Running**. Provisioning the cluster might take a couple of
minutes.

## Submit a Spark job

Submit a Spark job that estimates a value of Pi:

- In the Managed Service for Apache Spark navigation menu, click **Jobs**.

- 

On the **Jobs** page, click
add_box **Submit job**, and then do
the following:

- In the **Job ID** field, use the default setting, or provide an ID that
is unique to your Cloud de Confiance project.

- In the **Cluster** drop-down, select **`example-cluster`**.

- For **Job type**, select **Spark**.

- In the **Main class or jar** field, enter
`org.apache.spark.examples.SparkPi`.

- 

In the **Jar files** field, enter
`file:///usr/lib/spark/examples/jars/spark-examples.jar`. (This sample
jar is pre-installed on the cluster. For custom jobs, specify a
Cloud Storage path; see [Submit a
job](/managed-spark/docs/guides/submit-job).)

- 

In the **Arguments** field, enter `1000` to set the number of tasks.

It generates *x* and *y* points on a coordinate plane that models a
circle enclosed by a unit square. The input argument (`1000`) determines
the number of x-y pairs to generate; the more pairs generated, the
greater the accuracy of the estimation. This estimation uses
Managed Service for Apache Spark worker nodes to parallelize the
computation. For more information, see [Estimating Pi using the Monte
Carlo Method](https://academo.org/demos/estimating-pi-monte-carlo/) 
and [JavaSparkPi.java on
GitHub](https://github.com/apache/spark/blob/master/examples/src/main/java/org/apache/spark/examples/JavaSparkPi.java).

- 

Click **Submit**.

Your job is displayed on the **Job details** page. The job status is
**Running** or **Starting**, and then it changes to **Succeeded** after
it's submitted.

To avoid scrolling in the output, click **Line wrap: off**. The output
is similar to the following:


```
Pi is roughly 3.1416759514167594
```


To view job details, click the **Configuration** tab.

## Update a cluster

Update your cluster by changing the number of worker instances:

- In the Managed Service for Apache Spark navigation menu, click **Clusters**.

- In the list of clusters, click **`example-cluster`**.

- 

On the **Cluster details** page, click the **Configuration** tab.

Your cluster settings are displayed.

- 

Click mode_edit **Edit**.

- 

In the **Worker nodes** field, enter `5`.

- 

Click **Save**.

Your cluster is now updated. To decrease the number of worker nodes to the
original value, follow the same procedure.






## Clean up





To avoid incurring charges to your Cloud de Confiance account for
the resources used on this page, follow these steps.






- To delete the cluster, on the **Cluster details** page for
**`example-cluster`**, click
delete **Delete**.

- To confirm that you want to delete the cluster, click **Delete**.






## What's next



- 

Try this quickstart by using other tools:

- 

[Use the API
Explorer](/managed-spark/docs/quickstarts/create-cluster-template) 

- 

[Use the
Google Cloud CLI](/managed-spark/docs/quickstarts/create-cluster-gcloud) 

- 

Learn how to [create robust firewall rules when you create a
project](/managed-spark/docs/concepts/configuring-clusters/network) 

- 

Learn how to [write and run a Spark Scala
job](/managed-spark/docs/tutorials/spark-scala).