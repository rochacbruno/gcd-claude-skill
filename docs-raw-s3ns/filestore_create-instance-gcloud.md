# Quickstart: Create a Filestore instance by using the gcloud CLI

Source: https://documentation.s3ns.fr/filestore/docs/create-instance-gcloud
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


























# Create a Filestore instance using the gcloud CLI




This quickstart shows you how to get up and running quickly with Filestore
using the Google Cloud CLI. In this quickstart, you learn how to:

- Create a Filestore instance.

- Mount the file share from that instance on a Compute Engine client VM.

- Create a file on the mounted file share.

- Delete the Filestore instance.





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




[Create or select a Cloud de Confiance project](https://documentation.s3ns.fr/resource-manager/docs/creating-managing-projects).





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


Create a Cloud de Confiance project:


```
gcloud projects create PROJECT_ID 
```



Replace ` PROJECT_ID ` with a name for the Cloud de Confiance project you are creating.



- 


Select the Cloud de Confiance project that you created:


```
gcloud config set project PROJECT_ID 
```



Replace ` PROJECT_ID ` with your Cloud de Confiance project name.













- 


If you're using an existing project for this guide,
[verify that you have the
permissions required to complete this guide](#required-roles). If you created a new project,
then you already have the required permissions.













- 



[Verify that billing is enabled for your Cloud de Confiance project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 



Enable the Filestore API, if it is not already enabled:





**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).


```
gcloud services enable file.googleapis.com
```








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










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









When you finish the tasks that are described in this document, you can avoid
continued billing by deleting the resources that you created. For more information, see
[Clean up](#clean-up).






## Create a Compute Engine VM



### Linux









- 


Create a Compute Engine instance. Configure the instance as follows:




- 
Name the instance `nfs-client`.






- 
Set the `--zone` flag to `us-central1-c`.






- 
Set the `--image-project` flag to
`debian-cloud`.






- 
Set the `--image-family` flag to
`debian-11`.
















- 
Set the `--tags` flag to `http-server`.









```
gcloud compute instances create nfs-client --zone = us-central1-c --image-project = debian-cloud --image-family = debian-11 --tags = http-server
```
























### Windows









- 


Create a Compute Engine instance. Configure the instance as follows:




- 
Name the instance `nfs-client`.






- 
Set the `--zone` flag to `us-central1-c`.






- 
Set the `--image-project` flag to
`windows-cloud`.






- 
Set the `--image-family` flag to
`windows-2012-r2`.
















- 
Set the `--tags` flag to `http-server`.









```
gcloud compute instances create nfs-client --zone = us-central1-c --image-project = windows-cloud --image-family = windows-2012-r2 --tags = http-server
```

























## Create a Filestore instance

This quickstart shows how to create an instance in the regional service tier with custom performance enabled. For details on creating instances, see [create an instance](/filestore/docs/creating-instances).

- 

Create a Filestore instance. Configure the instance as follows:

- Name the instance `nfs-server`.

- Set the `--region` flag to `us-central1`.

- Set the `--tier` flag to `REGIONAL`.

- 

Set the `--performance` flag to `max-iops-per-tb=17000`.

- 

Set the `--file-share` flag to `name="vol1",capacity=1TB`.

- 

Set the `--network` flag to `name="default"`.


```
gcloud filestore instances create nfs-server --region = us-central1 --tier = REGIONAL --performance = max-iops-per-tb = 17000 --file-share = name = "vol1" ,capacity = 1TB --network = name = "default" 
```


- 

Get information about the Filestore instance you created:


```
gcloud filestore instances describe nfs-server --region = us-central1 
```


The command returns something like:


```
createTime: '2025-02-12T09:15:08.163246004Z' 
customPerformanceSupported: true 
fileShares:
-capacityGb: '1024' 
name: vol1
name: projects/yourproject/locations/us-central1/instances/nfs-server
networks:
-connectMode: DIRECT_PEERING
ipAddresses:
- 10 .0.0.2
network: default
reservedIpRange: 10 .0.0.2/26
performanceConfig:
iopsPerTb:
maxIopsPerTb: '17000' 
performanceLimits:
maxIops: '17000' 
maxReadIops: '17000' 
maxReadThroughputBps: '417792000' 
maxWriteIops: '5100' 
maxWriteThroughputBps: '139264000' 
protocol: NFS_V3
state: READY
tier: REGIONAL
```


Copy down the IP address of the instance for use when mounting the
file share. For this quickstart, we use the IP address `10.0.0.2`.

## Mount the Filestore file share on the `nfs-client` instance



### Linux









- 

Establish an SSH connection to the

`nfs-client`


instance:

```
gcloud compute ssh nfs-client
```






- 

Install NFS by running the following commands on the terminal window of
`nfs-client`:


```
sudo apt-get -y update &&
sudo apt-get -y install nfs-common
```


- 

Create a mount directory on the `nfs-client` instance for the
Filestore file share:


```
sudo mkdir /mnt/test
```


- 

Mount the file share to the `nfs-client` instance with the [`mount`](https://linux.die.net/man/8/mount)
command by specifying the IP address of the Filestore
instance, the name of the file share, and the mount directory to mount to:


```
sudo mount MOUNT-POINT-DIRECTORY /mnt/test
```


where:

MOUNT-POINT-DIRECTORY is the path to the directory where the Filestore file share is mounted. For example: `10.0.0.2:/vol1`

- 

**Optional**: Confirm that the Filestore file share is
mounted:

df -h --type=nfs

- 

Make the file share accessible by changing its permissions:


```
sudo chmod go + rw / mnt / test 
```




### Windows

### Sign in to the `nfs-client` instance and open a Command Prompt as an administrator

- 

Create an account and set an initial password for the `nfs-client` instance:


```
gcloud compute reset-windows-password nfs-client
```


- 

Configure your instance to enable connecting to serial ports:


```
gcloud compute instances add-metadata nfs-client --metadata=serial-port-enable=1
```


- 

Enter an interactive session:


```
gcloud compute connect-to-serial-port nfs-client --port=2
```


- 

At the `SAC>` prompt, create a new channel:


```
cmd
```


A channel with the name `Cmd0001` is created.

- 

Connect to the channel:


```
ch -sn Cmd0001
```


- 

Enter the username and password of the `nfs-client` instance and leave the
`Domain` field blank. You are connected to the `Command Prompt` interface
of the `nfs-client` instance.

### Install NFS client

- 

In the `Command Prompt` of `nfs-client`, switch to `Windows PowerShell`:


```
powershell
```


- 

Install the `NFS` client:


```
Install-WindowsFeature -Name NFS-Client
```


- 

Restart the `nfs-client` instance when prompted:


```
restart-computer
```


- 

At the `SAC>` prompt, wait for the following notification to appear:


```
EVENT: The CMD command is now available.
```


Then, run the `cmd` and `ch -sn` commands as previously instructed to sign
in and reconnect to the `nfs-client` instance.

### Configure the user ID used by the NFS client

- In the Command Prompt, run `powershell` to switch to Windows PowerShell.

- 

In `PowerShell`, run the following commands to create two new registry entries, `AnonymousUid` and `AnonymousGid`:


```
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" `
-Name "AnonymousUid" -Value "0" -PropertyType DWORD

New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" `
-Name "AnonymousGid" -Value "0" -PropertyType DWORD
```


- 

Restart the NFS client service:


```
nfsadmin client stop

nfsadmin client start
```


### Map the `vol1` file share to the `nfs-client` instance

- 

Exit `PowerShell`:


```
exit
```


- 

From `Command Prompt`, mount the file share to the `nfs-client` instance
with the [`mount`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/mount) command by
specifying the IP address of the Filestore instance, the
name of the file share, and the drive letter to mount to:


```
mount - o mtype = hard 10.0.0.2 : / vol1 z : 
```





## Create a file on the mounted file share



### Linux

- 

In the `nfs-client` terminal window, create a file named `testfile` by
running the following command:


```
echo 'This is a test' > /mnt/test/testfile
```


- 

Confirm the file was created by running the following command and verifying
that `testfile` is in the directory contents returned:


```
ls /mnt/test
```




### Windows

- 

In the Command Prompt window of the `nfs-client` instance, create a file
named `testfile`:


```
echo 'This is a test' > Z:\testfile
```


- 

Confirm the file was created by running the following command:


```
dir Z:
```


and verifying that `testfile` is in the directory contents returned.









## Clean up





To avoid incurring charges to your Cloud de Confiance account for
the resources used on this page, delete the Cloud de Confiance project with the
resources.






### Delete the Cloud de Confiance project






Delete a Cloud de Confiance project:


```
gcloud projects delete PROJECT_ID 
```


### Delete the Filestore instance

Delete the `nfs-server` instance:


```
gcloud filestore instances delete nfs-server --zone=us-central1-c
```


### Delete the Compute Engine instance









Delete the instance:

```
gcloud compute instances delete nfs-client
```








## What's next



- Read the [Filestore Overview](/filestore) to learn more about the basics of Filestore.

- Set up a Filestore instance on your own by following the instructions at [Creating Instances](/filestore/docs/creating-instances).

- Read [Access Control](/filestore/docs/access-control) to learn how to control access to Filestore operations
and the resources on an instance.

- See how to [copy data to or from a Filestore instance](/filestore/docs/copying-data).

- See how to [transfer large datasets from Cloud Storage to Filestore](/filestore/docs/transfer-data-from-gcs).