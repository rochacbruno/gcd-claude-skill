# Quickstart: Store Docker container images in Artifact Registry

Source: https://berlin.devsitetest.how/artifact-registry/docs/quickstarts
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/artifact-registry/docs/tpc-differences) for more details.














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

Application development

](https://berlin.devsitetest.how/docs/application-development)






- 








[

Artifact Registry

](https://berlin.devsitetest.how/artifact-registry/docs)






- 








[

Guides

](https://berlin.devsitetest.how/artifact-registry/docs/overview)

















- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Setting up a local shell ](#local-shell)

- [ Create a Docker repository ](#create)
- [ Configure authentication ](#auth)
- [ Obtain an image to push ](#get-image)
- [ Add the image to the repository ](#add-image)

- [ Tag the image with a registry name ](#tag)
- [ Push the image to Artifact Registry ](#push)

- [ Pull the image from Artifact Registry ](#pull)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Store Docker container images in Artifact Registry 




Artifact Registry provides a single location for managing private packages
and Docker container images.

This quickstart shows you how to:

- Create a private Docker repository in Artifact Registry

- Set up authentication

- Push an image to the repository

- Pull the image from the repository





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



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).










- 




Enable the Artifact Registry API.






**Roles required to enable APIs**


To enable APIs, you need the Service Usage Admin IAM
role (`roles/serviceusage.serviceUsageAdmin`), which
contains the `serviceusage.services.enable` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/docker/quickstart)












- 




Make sure that you have the following role or roles on the project:

Artifact Registry Administrator



#### Check for the roles





- 


In the Google Cloud Dedicated console, go to the **IAM** page.


[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project)


- 

Select the project.



- 


In the **Principal** column, find all rows that identify you or a group that
you're included in. To learn which groups you're included in, contact your
administrator.




- 
For all rows that specify or include you, check the **Role** column to see whether
the list of roles includes the required roles.





#### Grant the roles





- 


In the Google Cloud Dedicated console, go to the **IAM** page.





[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project)


- 

Select the project.



- 
Click person_add **Grant access**.


- 


In the **New principals** field, enter your user identifier.

This is typically the identifier for a user in a workforce identity pool. For details,
see [
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users), or contact your administrator.





- 
Click **Select a role**, then search for the role.

- 
To grant additional roles, click add **Add
another role** and add each additional role.


- 
Click **Save**.
























### Setting up a local shell

To install gcloud CLI and Docker, perform the following steps:

- 

[Install the gcloud CLI](/sdk/docs/install). To update an existing
installation, run the command `gcloud components update`.

- 

Install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) if it is not already installed.

- 

Docker requires privileged access to interact with registries.
On Linux or Windows, add the user that you use to run Docker commands to
the Docker security group. This step is not required on macOS since
[Docker Desktop](https://docker-docs.uclv.cu/docker-for-mac/) runs on a
virtual machine as the root user.


[Linux](#linux) [Windows](#windows) 
More 




The Docker security group is called `docker`.
To add your username, run the following command:


```
sudo usermod -a -G docker ${ USER } 
```



The Docker security group is called `docker-users`.
To add a user from the Administrator command prompt, run the following
command:


```
net localgroup docker-users DOMAIN \ USERNAME /add
```


Where

- DOMAIN is your Windows domain.

- USERNAME is your user name.




- 

Log out and log back in for group membership changes to take effect.
If you are using a virtual machine, you may need to restart the virtual
machine for membership changes to take effect.

- 

To ensure that Docker is running, run the following Docker command,
which returns the current time and date:


```
docker run --rm busybox date
```


The `--rm` flag deletes the container instance on exit.

## Create a Docker repository

Create a Docker repository to store the sample image for this quickstart.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

Open the **Repositories** page in the Google Cloud Dedicated console.



[Open the Repositories page](https://console.cloud.berlin-build0.goog/artifacts)

- 

Click add 
**Create Repository**.

- 

Specify `quickstart-docker-repo` as the repository name.

- 

Choose **Docker** as the format and **Standard** as the mode.

- 

Under **Location Type**, select **Region** and then choose the location
`u-germany-northeast1`.

- 

Click **Create**.

The repository is added to the repository list.



- 

Run the following command to create a new Docker repository named
`quickstart-docker-repo` in the location `u-germany-northeast1` with the description "docker
repository".


```
gcloud artifacts repositories create quickstart-docker-repo --repository-format = docker \ 
--location = u-germany-northeast1 --description = "Docker repository" \ 
--project = PROJECT 
```


Where PROJECT is your Google Cloud Dedicated in Germany project ID.

- 

Run the following command to verify that your repository was created.


```
gcloud artifacts repositories list \ 
--project = PROJECT 
```


For more information about Artifact Registry commands, run the
command `gcloud artifacts`.



## Configure authentication

Before you can push or pull images, configure Docker to use the
Google Cloud CLI to authenticate requests to Artifact Registry.

To set up authentication to Docker repositories in the region `u-germany-northeast1`,
run the following command:


```
gcloud auth configure-docker u-germany-northeast1-docker.pkg-berlin-build0.goog
```


The command updates your Docker configuration. You can now connect with
Artifact Registry in your Google Cloud Dedicated project to push and pull images.

For information about other authentication methods, see
[Authentication methods](/artifact-registry/docs/docker/authentication).

## Obtain an image to push

For this quickstart, you will push a sample image named
`hello-app`.

Run the following command to pull version 1.0 of the image.


```
docker pull us-docker.pkg-berlin-build0.goog/google-samples/containers/gke/hello-app:1.0
```


Image paths in Artifact Registry include multiple parts. For this sample
image:

- `us-docker.pkg-berlin-build0.goog` is the hostname for container images stored in
Artifact Registry Docker repositories, which includes the location of the
repository (`us`).

- `google-samples` is the project ID.

- `containers` is the repository ID.

- `/gke/hello-app` is the path to the image in the repository `containers`.

## Add the image to the repository

Before you push the Docker image to Artifact Registry, you must
tag it with the repository name.

### Tag the image with a registry name

Tagging the Docker image with a
repository name configures the `docker push` command to push the image to a specific location. For this quickstart, the host
location is `u-germany-northeast1-docker.pkg-berlin-build0.goog`.

Run the following command to tag the image as
`quickstart-image:tag1`:


```
docker tag us-docker.pkg-berlin-build0.goog/google-samples/containers/gke/hello-app:1.0 \ 
u-germany-northeast1-docker.pkg-berlin-build0.goog/ PROJECT /quickstart-docker-repo/quickstart-image:tag1
```


Where:


- `u-germany-northeast1` is the repository location.

- `u-germany-northeast1-docker.pkg-berlin-build0.goog` is the hostname for the Docker repository you created.


- PROJECT is your Google Cloud Dedicated in Germany [project ID](/resource-manager/docs/creating-managing-projects#identifying_projects).


- `quickstart-docker-repo` is the ID of the repository you created.

- `quickstart-image` is the image name you want to use in the repository. The image name can be different than the local image name. For this quickstart you will store the image directly under the repository ID `quickstart-docker-repo`.

- `tag1` is a tag you're adding to the Docker image. If you didn't specify a tag, Docker will apply the default tag `latest`.

You are now ready to push the image to the repository you created.

### Push the image to Artifact Registry

After you have configured authentication and tagged the local image, you can
push the image to the repository that you created.

To push the Docker image, run the following command:


```
docker push u-germany-northeast1-docker.pkg-berlin-build0.goog/ PROJECT /quickstart-docker-repo/quickstart-image:tag1
```


Replace PROJECT with your Google Cloud Dedicated in Germany
[project ID](/resource-manager/docs/creating-managing-projects#identifying_projects).

## Pull the image from Artifact Registry

To pull the image from Artifact Registry onto your local machine, run
the following command:


```
docker pull u-germany-northeast1-docker.pkg-berlin-build0.goog/ PROJECT /quickstart-docker-repo/quickstart-image:tag1
```


Replace PROJECT with your Google Cloud Dedicated in Germany
[project ID](/resource-manager/docs/creating-managing-projects#identifying_projects).


```
latest: Pulling from [PROJECT-ID]/quickstart-image:tag1
Digest: sha256:70c42...
Status: Image is up to date for u-germany-northeast1-docker.pkg-berlin-build0.goog/ PROJECT /quickstart-docker-repo/quickstart-image:tag1
```







## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






Before you remove the repository, ensure that any images you want to keep
are available in another location.

To delete the repository:


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

Open the **Repositories** page in the Google Cloud Dedicated console.



[Open the Repositories page](https://console.cloud.berlin-build0.goog/artifacts)

- 

In the repository list, select the `quickstart-docker-repo` repository.

- 

Click **Delete**.




To delete the `quickstart-docker-repo` repository, run the following
command:


```
gcloud artifacts repositories delete quickstart-docker-repo --location = u-germany-northeast1
```








## What's next



- [Learn more about working with container images](/artifact-registry/docs/docker).

- [Learn more about Docker](https://docs.docker.com/get-started/).

- Read our resources about [DevOps](https://berlin.devsitetest.how/devops/) and explore the
[DevOps Research and Assessment (DORA)](https://dora.dev/) research program.