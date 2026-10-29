# Quickstart: Create a Filestore instance using the Cloud de Confiance console

Source: https://documentation.s3ns.fr/filestore/docs/create-instance-console
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/filestore/docs/tpc-differences) for more details.














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

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Filestore

](https://documentation.s3ns.fr/filestore/docs)






- 








[

Guides

](https://documentation.s3ns.fr/filestore/docs/overview)


























# Create a Filestore instance using the Cloud de Confiance console




This quickstart shows you how to perform basic operations in Filestore
using this Cloud de Confiance console. In the quickstart, you will:

- Create a Filestore instance.

- Mount the file share from that instance on a Compute Engine client VM instance.

- Create a file on the mounted file share.

- Delete the Filestore instance.





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


If you're using an existing project for this guide,
[verify that you have
the permissions required to complete this guide](#required-roles). If you created a new
project, then you already have the required permissions.













- 



[Verify that billing is enabled for your Cloud de Confiance project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the Filestore API, if it is not already enabled.






**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.s3nscloud.fr/apis/enableflow?apiid=file.googleapis.com)












### Required roles




















































































































To get the permissions that
you need to complete this quickstart,

ask your administrator to grant you the
following IAM roles on your project:












- 
Create and manage Filestore instances:
[Cloud Filestore Editor ](/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`)





- 
Create and manage Compute Engine instances:
[Compute Instance Admin (v1) ](/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)





- 
Create, modify, and delete networking resources, except for firewall rules:
[Compute Network Admin ](/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)





- 
Run operations on IAM service accounts:
[Service Account User ](/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)





- 
Manage network and related Cloud de Confiance by S3NS resources:
Network Administrator (`roles/iam.networkAdmin`)












For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









When you finish the tasks that are described in this document, you can avoid
continued billing by deleting the resources that you created. For more information, see
[Clean up](#clean-up).






## Create a Compute Engine VM instance to be the client

- 

In the Cloud de Confiance console, go to the VM Instances page.

[Go to the Compute Engine instances page](https://console.cloud.s3nscloud.fr/compute/instances) 

- 

Click **Create Instance** and configure the instance as follows.

- Set **Name** to `nfs-client`.

- Set **Zone** to **us-central1-c**.

- Keep the default boot disk.

- In the **Networking** > **Firewall** section, select the **Allow HTTP traffic** checkbox.

- Keep the network as **default**.

- 

Click **Create** to create the instance.

## Create a Filestore instance

This quickstart shows how to create an instance in the **Regional** tier with custom performance enabled. For details on creating instances, see [create an instance](/filestore/docs/creating-instances).

- 

In the Cloud de Confiance console, go to the Filestore **Instances** page.

[Go Instances](https://console.cloud.s3nscloud.fr/filestore/instances) 

- 

Click **Create Instance** and configure the instance as follows:

- Set **Instance ID** to `nfs-server`.

- Set **Instance type** to **Regional**.

- In **Capacity**, enter `1 TiB`.

- 

In **Performance**, configure your performance based on the workload and scale.
The **Scale performance with capacity** checkbox is checked, so if you change the value in the **Capacity** field, performance scales accordingly.

For more information on configuration options, see [configure performance](/filestore/docs/creating-instances#configure-performance).

- 

Set **Protocol** to **NFSv4.1**.

- 

Set the **IP stack type** to **IPv6**.

- 

Set **Region** to **us-central1**.

- 

For **VPC network**, select a network from the list.
For more information on creating VPC networks, see [Create and manage VPC networks](/vpc/docs/create-modify-vpc-networks).

- 

Set **File share name** to `vol1`.

- 

Set **Allocated IP range** to **Use an automatically allocated IP range**.

- 

Set **Access controls** to **Grant access to all clients**.

- 

Click **Create**.

## Mount the Filestore file share on the client

- 

In the Cloud de Confiance console, go to the VM Instances page.

[Go VM instances](https://console.cloud.s3nscloud.fr/compute/instances) 

- 

In the list of VM instances, click the **SSH** button for **nfs-client** to
open a terminal window connected to that instance.

- 

Install NFS by running the following commands:


```
sudo apt-get -y update &&
sudo apt-get -y install nfs-common
```


- 

Make a mount directory for the Filestore file share by running the following command:


```
sudo mkdir -p /mnt/test
```


- 

Mount the file share by running the `mount` command
and specifying the Filestore instance IP address and
file share name:


```
sudo mount MOUNT-POINT-DIRECTORY /mnt/test
```


where:

MOUNT-POINT-DIRECTORY is the path to the directory where the Filestore file share is mounted. For example: `10.0.0.2:/vol1`

- 

Optional: Confirm that the Filestore file share is
mounted:


```
df - h -- type = nfs 
```


- 

Make the file share accessible by changing the permissions:


```
sudo chmod go + rw / mnt / test 
```


## Create a file on the file share

- 

In the terminal window that is connected to the **nfs-client** instance, create a file
named `testfile` by running the following command:


```
echo 'This is a test' > /mnt/test/testfile
```


- 

Confirm that the file was created by running the following command:


```
ls /mnt/test
```


and verifying that `testfile` is listed.






## Clean up





To avoid incurring charges to your Cloud de Confiance account for
the resources used on this page, follow these steps.






### Delete the Cloud de Confiance project





- 
In the Cloud de Confiance console, go to the **Manage resources** page.


[Go to Manage resources](https://console.cloud.s3nscloud.fr/iam-admin/projects)




- 
In the project list, select the project that you
want to delete, and then click **Delete**.


- 
In the dialog, type the project ID, and then click
**Shut down** to delete the project.


### Delete the Filestore instance

- 

In the Cloud de Confiance console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.s3nscloud.fr/filestore/instances) 

- 

Click the **`nfs-server`** instance ID to open the instance details page.

- 

Click **Delete** *delete*.

- 

When prompted, type the instance ID.

- 

Click **Delete**.

### Delete the Compute Engine instance

- 

In the Cloud de Confiance console, go to the Filestore Instances page.

[Go to the VM instances page](https://console.cloud.s3nscloud.fr/compute/instances) 

- 

Select the checkbox next to the **`nfs-client`** instance name.

- 

Click **Delete** *delete*.

- 

When prompted, click **Delete** again.






## What's next



- Read the [Filestore Overview](/filestore/docs/overview) to learn more about the basics of Filestore.

- Set up a Filestore instance on your own by following the instructions at [Creating Instances](/filestore/docs/creating-instances).

- Read the [Access Control](/filestore/docs/access-control) page to learn how to control access to Filestore operations
and the resources on an instance.

- See how to [copy data to or from a Filestore instance](/filestore/docs/copying-data).

- See how to [transfer large datasets from Cloud Storage to Filestore](/filestore/docs/transfer-data-from-gcs).