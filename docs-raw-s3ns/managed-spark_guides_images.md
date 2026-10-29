# Create a Managed Service for Apache Spark custom image

Source: https://documentation.s3ns.fr/managed-spark/docs/guides/images
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












# Create a Managed Service for Apache Spark custom image 


















You can create a Managed Service for Apache Spark cluster with a
[custom image](/compute/docs/images#custom_images) that includes
your pre-installed packages. This page shows you how to create a custom
image and install it on a Managed Service for Apache Spark cluster.

## Usage considerations and limitations

- 

**Custom image lifetime:** To make sure that the clusters receive the latest
service updates and bug fixes, the creation of clusters with a custom image is
limited to **365 days** from the custom image creation date. Note that
existing clusters created with a custom-image can run indefinitely.

You may need to use automation if you want to create clusters with a specific
custom image for a period of greater than 365 days. For more information, see
[Create a cluster with an expired custom image](#expired-custom-image).

- 

**Linux only:** The instructions in this document apply to Linux operating
systems only. Other operating systems may be supported in future
Managed Service for Apache Spark [releases](/managed-spark/docs/release-notes).

- 

**Supported base images:** Custom image builds require starting from a
Managed Service for Apache Spark base image. The following base images are supported:
[Debian, Rocky Linux, and Ubuntu](/managed-spark/docs/concepts/versioning/dataproc-versions#supported-dataproc-image-versions).

- **Base image availability:** New images announced in the
[Managed Service for Apache Spark release notes](/managed-spark/docs/release-notes)
are not available for use as the base for custom images until one
week from their announcement date.

- 

**Using hosted custom images:** If you use a custom image hosted in another project, the
[Managed Service for Apache Spark Service Agent service account](/managed-spark/docs/concepts/configuring-clusters/service-accounts#service_agent_account)
in your project must have `compute.images.get` permission on
the image in the host project. You can grant this permission by granting the
[`roles/compute.imageUser`](/compute/docs/access/iam#compute.imageUser)
role on the hosted image to your project's
Managed Service for Apache Spark Service Agent service account (see
[Sharing custom images within an organization](/compute/docs/images/managing-access-custom-images#share-images-within-organization)).

- 

**Using secure boot MOK (Machine Owner Key) secrets:**
To enable
[secure boot](https://github.com/cjac/custom-images/blob/secure-boot-readme-20241009/examples/secure-boot/README.md)
with your Managed Service for Apache Spark custom image, do the following:

- 

Enable the
[Secret Manager API (`secretmanager.googleapis.com`](/secret-manager/docs/configuring-secret-manager). Managed Service for Apache Spark generates and manages a key pair
using the [Secret Manager](/secret-manager/docs/overview) service.

- 

Add the
[`--service-account=" SERVICE_ACCOUNT" ` flag](https://github.com/GoogleCloudDataproc/custom-images/blob/main/README.md#optional-arguments)
to the `generate_custom_image.py` command when you
[generate a custom image](#generate_a_custom_image).
Note: You must grant to the service account the Secret Manager Viewer role (`roles/secretmanager.viewer`)
on the project and the Secret Manager Accessor role (`roles/secretmanager.secretAccessor`)
on' the public and private secrets.

For more information with examples, see the `README.md` and other files
within the
[examples/secure-boot directory](https://github.com/GoogleCloudDataproc/custom-images/blob/main/examples/secure-boot/) of the `GoogleCloudDataproc/custom-images` repository on GitHub.

**To disable secure boot:** By default, the Managed Service for Apache Spark custom image
scripts generate and manage a key pair using [Secret Manager](/secret-manager/docs/overview)
when run from a Managed Service for Apache Spark cluster. If you don't want to use
secure-boot with your custom image, include the `--trusted-cert="" `
(empty flag value) to the `generate_custom_image.py` command when you
[generate your custom image](#generate_a_custom_image).

## Before you begin

Make sure to set up your project before generating your custom image.

### Set up your project

















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



[Verify that billing is enabled for your Cloud de Confiance project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the Dataproc API, Compute Engine API, and Cloud Storage APIs, if any are not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the APIs](https://console.cloud.s3nscloud.fr/apis/enableflow?apiid=dataproc,compute_component,storage-component.googleapis.com)














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






















- [Install Python 3.11+](https://www.python.org/downloads/)

- Prepare a customization script that installs custom packages and/or
updates configurations, for example:

```
#! /usr/bin/bash
apt-get -y update
apt-get install python-dev
apt-get install python-pip
pip install numpy
```


### Create a Cloud Storage bucket in your project





- 
In the Cloud de Confiance console, go to the Cloud Storage
**Buckets** page.


[Go to Buckets](https://console.cloud.s3nscloud.fr/storage/browser)

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

## Generate a custom image

You use [generate_custom_image.py](https://github.com/GoogleCloudDataproc/custom-images/blob/master/generate_custom_image.py),
a Python program, to create a Managed Service for Apache Spark custom image.

### How it works

The `generate_custom_image.py` program launches a temporary
Compute Engine VM instance with the specified Managed Service for Apache Spark
base image, then runs the customization script inside the VM instance to install
custom packages and or update configurations. After the customization script
finishes, it shuts down the VM instance and creates a Managed Service for Apache Spark custom
image from the VM instance disk. The temporary VM is deleted after the
custom image is created. The custom image is saved and can be used to
[create Managed Service for Apache Spark clusters](#create_a_cluster_with_a_custom_image).

The `generate_custom_image.py` program uses gcloud CLI
to run multi-step workflows on Compute Engine.

### Run the code

Fork or clone the files on GitHub at
[Managed Service for Apache Spark custom images](https://github.com/GoogleCloudDataproc/custom-images).

Then, run the `generate_custom_image.py` script to have Managed Service for Apache Spark
generate and save your custom image.


```
python3 generate_custom_image.py \
    --image-name= CUSTOM_IMAGE_NAME \
    [--family= CUSTOM_IMAGE_FAMILY_NAME ] \
    --dataproc-version= IMAGE_VERSION \
    --customization-script= LOCAL_PATH \
    --zone= ZONE \
    --gcs-bucket= gs:// BUCKET_NAME \
    [--no-smoke-test]
```


**Required flags**

- 

`--image-name`: the output name for your custom image.

- 

`--dataproc-version`: the [Managed Service for Apache Spark image version](/managed-spark/docs/concepts/versioning/dataproc-versions#supported-dataproc-image-versions)
to use in your custom image. Specify the version in `x.y.z-os` or `x.y.z-rc-os` format,
for example, "2.0.69-debian10".

- 

`--customization-script`: a local path to
your script that the tool will run to install your custom packages or perform
other customizations. This script is run as a
[Linux startup script](/compute/docs/instances/startup-scripts/linux#metadata-keys)
only on the temporary VM used to create the custom image. You can specify a
different initialization script for other initialization actions you want to
perform when you
[create a cluster with your custom image](#create_a_cluster_with_a_custom_image).

**Cross-project images:** If your custom image is used to create
clusters in different projects, an error can occur due to the
`gcloud` or `gsutil` command cache stored within the image. You can avoid
this issue by including the following command in your customization script
to clear cached credentials.


```
rm -r /root/.gsutil /root/.config/gcloud
```


- 

`--zone`: the [Compute Engine zone](/compute/docs/regions-zones#available)
where `generate_custom_image.py` will create a temporary VM to use to create
your custom image.

- 

`--gcs-bucket`: a URI, in the format `gs:// BUCKET_NAME `,
that points to your [Cloud Storage bucket](#create-a-cloud-storage-bucket-in-your-project).
`generate_custom_image.py` writes log files to this bucket.

**Optional flags** 

- `--family`: the image family for the custom image. Image families are used to group
similar images together, and can be used when creating a cluster as a pointer to
the most recent image in the family. For example, `custom-2-2-debian12`.

- `--no-smoke-test`: This is an optional flag that disables smoke testing the
newly built custom image. The smoke test creates a Managed Service for Apache Spark test
cluster with the newly built image, runs a small job, and then deletes the
cluster at the end of the test. The smoke test runs by default to verify
that the newly built custom image can create a functional Managed Service for Apache Spark
cluster. Disabling this step by using the `--no-smoke-test` flag speeds up
the custom image build process, but its use is not recommended.

- `--subnet`: The subnetwork to use to create the VM
that builds the custom Managed Service for Apache Spark image. If your project is part of
a [shared VPC](/vpc/docs/shared-vpc), you must specify the full subnetwork URL
in the following format: `projects/ HOST_PROJECT_ID /regions/ REGION /subnetworks/ SUBNET `.

For a listing of available optional flags, see
[Optional Arguments](https://github.com/GoogleCloudDataproc/custom-images#optional-arguments)
on GitHub.

If `generate_custom_image.py` is successful, the `imageURI` of the custom image is
displayed in the terminal window output (the full `imageUri` is shown in **bold** below):


```
...
managedCluster:
clusterName: verify-image-20180614213641-8308a4cd
config:
gceClusterConfig:
zoneUri: ZONE 
masterConfig:
imageUri: **https://www.googleapis.com/compute/beta/projects/ PROJECT_ID /global/images/ CUSTOM_IMAGE_NAME **
...

INFO:__main__:Successfully built Dataproc custom image: CUSTOM_IMAGE_NAME 
INFO:__main__:

#####################################################################
WARNING: DATAPROC CUSTOM IMAGE ' CUSTOM_IMAGE_NAME '
WILL EXPIRE ON 2018-07-14 21:35:44.133000.
#####################################################################
```


### Custom image version labels (advanced usage)

When using the Managed Service for Apache Spark standard custom image tool, the tool
sets a `goog-dataproc-version` label on the created
custom image. The label reflects the feature capabilities and protocols used by
Managed Service for Apache Spark to manage the software on the image.

Advanced usage: If you use your own process to create a custom Managed Service for Apache Spark
image, you must add the `goog-dataproc-version` label manually to your custom
image, as follows:

- 

Extract the `goog-dataproc-version` label from the base Managed Service for Apache Spark
image used to create the custom image.

```
gcloud compute images describe ${BASE_DATAPROC_IMAGE} \
    --project cloud-dataproc \
    --format="value(labels.goog-dataproc-version)"
```


- 

Set the label on the custom image.

```
gcloud compute images add-labels IMAGE_NAME --labels= [KEY=VALUE,...] 
```


## Use a custom image

You specify the custom image when you create a Managed Service for Apache Spark cluster.
A custom image is saved in
[Cloud Compute Images](/compute/docs/images#custom_images), and
is valid to create a Managed Service for Apache Spark cluster for 365 days from its
creation date (see [Create a cluster with an expired custom image](#expired-custom-image)
to use a custom image after its 365-day expiration date).

### Custom image URI

You pass the `imageUri` of the custom image to the cluster creation operation.
This URI can be specified in one of three ways:

- Full URI: 

`https://www.googleapis.com/compute/beta/projects/ PROJECT_ID /global/images/ `gs://`BUCKET_NAME` `

- Partial URI: `projects/ PROJECT_ID /global/images/ CUSTOM_IMAGE_NAME `

- Short name: CUSTOM_IMAGE_NAME 

Custom images can also be specified by their family URI, which always chooses
the most recent image within the image family.

- Full URI: 

`https://www.googleapis.com/compute/beta/projects/ PROJECT_ID /global/images/family/ CUSTOM_IMAGE_FAMILY_NAME/var>`

- Partial URI: `projects/ PROJECT_ID /global/images/family/ CUSTOM_IMAGE_FAMILY_NAME `

#### Find the custom image URI




### Google Cloud CLI

Run the following command to list the names of your custom images.


```
gcloud compute images list
```


Pass the name of your custom image to the following command to list
the URI (`selfLink`) of your custom image.


```
gcloud compute images describe custom-image-name 
```


Output snippet:


```
...
name: CUSTOM_IMAGE_NAME 
selfLink: https://www.googleapis.com/compute/v1/projects/ PROJECT_ID /global/images/ CUSTOM_IMAGE_NAME 
...
```




### Cloud de Confiance console


- Open the
[**Compute Engine→Images**](https://console.cloud.s3nscloud.fr/compute/images)
page in the Cloud de Confiance console, and then click the image name.
You can insert a query in the `filter images` field to limit the number
of displayed images.



- The **Images details** page opens. Click
**Equivalent REST**.



- The REST response lists additional information about the image, including
the `selfLink`, which is the image URI.

```
{
...
"name": "my-custom-image",
"selfLink": **"projects/ PROJECT_ID /global/images/ CUSTOM_IMAGE_NAME "**,
"sourceDisk": ...,
...
}
```







### Create a cluster with a custom image

[create a cluster](/managed-spark/docs/guides/create-cluster) with
using the gcloud CLI, the Dataproc API, or the
Cloud de Confiance console.




### Cloud de Confiance console


- Open the [**Create cluster**](https://console.cloud.s3nscloud.fr/dataproc/clusters/create) page.


- In the **Define your cluster** section, click **Image type and version**, select **Custom image**, then confirm or change the project and select an
available custom image.





### gcloud CLI

Create a Managed Service for Apache Spark cluster with a custom image using the
[`dataproc clusters create`](/sdk/gcloud/reference/dataproc/clusters/create)
command with the `--image` flag.

**Example:**


```
gcloud dataproc clusters create CLUSTER-NAME \
    --image= CUSTOM_IMAGE_URI \
    --region= REGION \
     ... other flags 
```




### REST API

Create a cluster with a custom image by specifying custom image URI
in the
[InstanceGroupConfig.imageUri](/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig)
field in the `masterConfig`, `workerConfig`, and, if applicable,
`secondaryWorkerConfig` object included in a
[cluster.create](/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create)
API request.



**Example:** REST request to create a standard
Managed Service for Apache Spark cluster (one master, two worker nodes) with a custom
image.



```
POST /v1/projects/ PROJECT_ID /regions/ REGION /clusters/
{
"clusterName": " CLUSTER_NAME ",
"config": {
"masterConfig": {
"imageUri": "projects/ PROJECT_ID /global/images/ CUSTOM_IMAGE_NAME "
},
"workerConfig": {
"imageUri": "projects/ PROJECT_ID /global/images/ CUSTOM_IMAGE_NAME "
}
}
}
```




### Override Managed Service for Apache Spark cluster properties with a custom image

You can use custom images to overwrite
[cluster properties](/managed-spark/docs/concepts/configuring-clusters/cluster-properties)
that are set during cluster creation. If you create a cluster with
a custom image, and the cluster creation operation sets properties with values
that are different from those that are set by your custom image, the property
values set by your custom image will take precedence.

To set cluster properties with your custom image:

- 

In your custom image
[customization script](#run_the_code),
create a `dataproc.custom.properties` file in `/etc/google-dataproc`, then
set cluster property values in the file.

- Sample `dataproc.custom.properties` file:


```
dataproc.conscrypt.provider.enable= VALUE 
dataproc.logging.stackdriver.enable= VALUE 
```


- Sample customization script file-creation snippet to override two
cluster properties:


```
cat /etc/google-managed-spark/dataproc.custom.properties
dataproc.conscrypt.provider.enable=true
dataproc.logging.stackdriver.enable=false
EOF
```


### Create a cluster with an expired custom image

By default, custom images expire 365 days from the date of creation of the image.
You can create a cluster that uses an expired custom image by completing
the following steps.

- 

Attempt to create a Managed Service for Apache Spark cluster with an expired custom
image or a custom image that will expire within 10 days.


```
gcloud dataproc clusters create CLUSTER-NAME \
    --image= CUSTOM-IMAGE-NAME \
    --region= REGION \
     ... other flags 
```


- 

The gcloud CLI will issue an error message that includes the
cluster `dataproc:dataproc.custom.image.expiration.token` property name
and token value.


```
dataproc:dataproc.custom.image.expiration.token= TOKEN_VALUE 
```


Copy the TOKEN_VALUE string to the clipboard.

- 

Use the gcloud CLI to create the Managed Service for Apache Spark cluster again,
adding the copied TOKEN_VALUE as a cluster property.


```
gcloud dataproc clusters create CLUSTER-NAME \
    --image= CUSTOM-IMAGE-NAME \
    --properties=dataproc:dataproc.custom.image.expiration.token= TOKEN_VALUE \
    --region= REGION \
     ... other flags 
```


Cluster creation with the custom image should succeed.