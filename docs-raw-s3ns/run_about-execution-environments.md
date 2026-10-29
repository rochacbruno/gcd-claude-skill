# Select an execution environment for services

Source: https://documentation.s3ns.fr/run/docs/about-execution-environments
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/run/docs/tpc-differences) for more details.














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

Application hosting

](https://documentation.s3ns.fr/docs/application-hosting)






- 








[

Cloud Run

](https://documentation.s3ns.fr/run/docs)






- 








[

Guides

](https://documentation.s3ns.fr/run/docs/overview/what-is-cloud-run)












# Select an execution environment for services 















All Cloud Run instances are sandboxed. The sandboxing technology and
available features differs depending on the selected *execution environment*.

The first generation execution environment is based on [gVisor](https://gvisor.dev/)
and features fast [cold start](/run/docs/tips/general#using_minimum_instances_to_reduce_cold_starts)
times and emulation of most, but not all operating system calls.

The second generation execution environment is a microVM and provides full
Linux compatibility rather than system call emulation. This execution environment
provides:

- Faster CPU performance

- Faster network performance, especially in the presence of packet loss

- Full Linux compatibility, including support for all system calls, namespaces,
and cgroups

- Network file system support

Although the second generation execution environment generally performs faster
under sustained load, it has longer [cold start times](/run/docs/tips/general#starting_services_quickly)
than first generation for some services.

Both execution environments have the same pricing. See the [Cloud Run pricing page](https://documentation.s3ns.fr/run/pricing)
for details.

## Selecting an execution environment for a Cloud Run service

Cloud Run services by default don't
have an execution environment specified, which means Cloud Run selects
the execution environment based on the features used. If you don't specify an
execution environment for your service, Cloud Run can select either the
first generation or the second generation environment.

Cloud Run jobs and worker pools only use the second generation
execution environment, and this cannot be changed.

### How to choose an execution environment

You should use first generation if any of the following apply:

- Your Cloud Run service has bursty traffic, and needs to scale out
fast to many instances, or your service is sensitive to cold start times.

- Your Cloud Run service has infrequent traffic that causes frequent
scale out from zero.

- You want to use less than 512 MiB of memory.
The second generation execution environment requires at least
512 MiB of memory.

You should use second generation if any of the following apply to your
Cloud Run service:

- Your service needs to use NFS, which is only supported by second generation.

- Your service has fairly steady traffic and is tolerant of somewhat slower cold starts.

- Your service has CPU-intensive workloads.

- Your service could benefit from faster network performance.

- Your service uses [Direct VPC egress](/run/docs/configuring/vpc-direct-vpc) to send
traffic to a VPC network and requires the best possible
network performance.

- Your service needs to use software that has issues running in first generation due to
[unimplemented system calls](/run/docs/troubleshooting#openblas-warning).

- Your service needs Linux cgroup functionality.

- Your service makes use of third-party infrastructure for securing containers.

### Required roles











































To get the permissions that
you need to configure and deploy Cloud Run services,

ask your administrator to grant you the
following IAM roles:













- [Cloud Run Developer ](/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`)
on the Cloud Run service


- [Service Account User ](/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
on the service identity





















If you are deploying a [service](/run/docs/deploying-source-code#required_roles)
or [function](/run/docs/deploy-functions#required-roles) from source code, you
must also have additional roles granted to you on your project and
Cloud Build service account.

For a list of IAM roles and permissions that are associated with
Cloud Run, see
[Cloud Run IAM roles](/run/docs/reference/iam/roles)
and [Cloud Run IAM permissions](/run/docs/reference/iam/permissions).
If your Cloud Run service interfaces with
Cloud de Confiance APIs, such as Cloud Client Libraries, see the
[service identity configuration guide](/run/docs/configuring/services/service-identity).
For more information about granting roles, see
[deployment permissions](/run/docs/reference/iam/roles#additional-configuration)
and [manage access](/iam/docs/granting-changing-revoking-access).

### Set and update execution environment

Any configuration change leads to the
creation of a new revision. Subsequent revisions will also automatically get
this configuration setting unless you make explicit updates to change it.

The default for Cloud Run services is *unspecified*, which means
that Cloud Run selects a suitable execution environment.
Alternatively, you can specify an execution environment. To use second generation,
you must [specify at least 512 MiB of memory](/run/docs/configuring/services/memory-limits).

You can set the execution environment using the Cloud de Confiance console, the gcloud
command line, or a YAML file when you [create a new service](/run/docs/deploying#service) or
[deploy a new revision](/run/docs/deploying#revision):



### Console

- 

In the Cloud de Confiance by S3NS console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.s3nscloud.fr/run) 

- 

Select **Services** from the Cloud Run navigation menu:

- 

If you are configuring a new service, click **Deploy container** and
fill out the initial service settings page. Then click
**Containers, Networking, Security** to expand the service configuration page.

- 

If you are configuring an existing service, click the service.

- 

Click the **Containers** tab.

- 

Select the execution environment using the option buttons. Keep **Default**
to let Cloud Run select a suitable execution environment.

- 

Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.



### gcloud

You can [update the execution environment](/sdk/gcloud/reference/run/services/update)
for a given service by using the following command:


```
gcloud run services update SERVICE --execution-environment ENVIRONMENT 
```


Replace SERVICE with the name of your service and ENVIRONMENT 
with the desired execution environment. Specify the value `gen1` for first
generation or `gen2` for second generation.

You can also set the execution environment during
[deployment](/sdk/gcloud/reference/run/deploy) using the command:


```
gcloud run deploy --image IMAGE_URL --execution-environment ENVIRONMENT 
```


Replace the following:

- ` IMAGE_URL `: a reference to the container image, for
example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry,
the [repository](/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must
already be created. The URL follows the format of ` LOCATION -docker.pkg.dev/ PROJECT_ID / REPO_NAME / PATH : TAG `
.

- ` ENVIRONMENT `: the desired execution
environment. Specify the value `gen1` for first generation or `gen2`
for second generation.



### YAML

- 

If you are creating a new service, skip this step.
If you are updating an existing service, download its [YAML configuration](/run/docs/reference/yaml/v1):


```
gcloud run services describe SERVICE --format export > service.yaml
```


- 

set the `run.googleapis.com/execution-environment` annotation:


```
apiVersion : serving.knative.dev/v1 
kind : Service 
metadata : 
name : SERVICE 
spec : 
template : 
metadata : 
annotations : 
run.googleapis.com/execution-environment : ENVIRONMENT 
```


Replace the following:

- SERVICE : the name of your Cloud Run service.

- ENVIRONMENT : the selected execution environment.
Specify the value `gen1` for first generation or `gen2` for second
generation.

Remove the `run.googleapis.com/execution-environment` annotation for the
default behavior.

- 

Create or update the service using the following command:


```
gcloud run services replace service.yaml
```


The `gcloud run services replace` command defaults to using `service.yaml` file if present.



### Terraform

To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).

Add the following to a
[`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service)
resource in your Terraform configuration:


```
resource "google_cloud_run_v2_service" "default" { 
name = "cloudrun-service-execution-environment" 
location = " REGION " 

template { 
containers { 
image = "us-docker.pkg.dev/cloudrun/container/hello" 
} 
execution_environment = " ENVIRONMENT " 
} 
} 
```


Replace the following:

- REGION : the Cloud de Confiance region. For example,
`europe-west1`.

- ENVIRONMENT : `EXECUTION_ENVIRONMENT_GEN1` for first
generation, or `EXECUTION_ENVIRONMENT_GEN2` for second generation.




## View execution environment settings

To view the current execution environment settings for your
Cloud Run service:



### Console

- 

In the Cloud de Confiance by S3NS console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.s3nscloud.fr/run/services) 

- 

Click the service you are interested in to open the **Service details**
page.

- 

Click the **Containers** tab to view the settings.



### gcloud

- 

Use the following command:


```
gcloud run services describe SERVICE 
```


- 

Locate the execution environment setting in the returned
configuration.




## Graceful shutdowns

When a Cloud Run instance is shutting down, it receives a
[`SIGTERM` signal](/run/docs/container-contract#instance-shutdown)
to enable a 10 second graceful shutdown.

### Handling SIGTERM signal

We recommend that your container install a [SIGTERM handler](/run/docs/container-contract#instance-shutdown),
especially if you are using [request-based billing](/run/docs/configuring/billing-settings).

Handling SIGTERM gives your container a chance to perform any necessary cleanup
tasks such as flushing logs before exiting. If your container does not catch
SIGTERM, it will still be given 10 seconds to
perform these tasks; those 10 seconds are
billed.

#### How to check whether your container handles SIGTERM

To determine whether your container has a SIGTERM handler installed:

- 

Start Cloud Shell. You can find

**Activate Cloud Shell** in the header of the documentation
page you're on. You may need to authorize it and wait for it to provision.
Alternatively, [start a standalone session](/shell/docs/launching-cloud-shell#launch_a_standalone_session).

- 

Run the container locally in Cloud Shell:


```
docker run IMAGE_URL 
```


Replace ` IMAGE_URL ` with a reference to the container image, for
example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry,
the [repository](/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must
already be created. The URL follows the format of ` LOCATION -docker.pkg.dev/ PROJECT_ID / REPO_NAME / PATH : TAG `
.

- 

Open another tab in Cloud Shell and get a list of the containers running
in the current Cloud Shell session:


```
docker container ls
```


You need to locate the container ID returned from the command.

- 

Using the container ID, send your container a SIGTERM signal


```
docker kill -s SIGTERM CONTAINER_ID 
```


- 

Return to the tab where you invoked `docker run` to see whether the container
has exited (stopped). If the SIGTERM signal caused your container to exit, your
container is handling SIGTERM.

### How to handle SIGTERM

If your container does not handle SIGTERM, the simplest way to add a SIGTERM
handler is to wrap your service with `tini`. Doing this makes your service run
as a subprocess of `tini`, which takes on the role of the container init process.
Refer to the [Docker instructions](https://github.com/docker-library/official-images#init)
for instructions.

Alternatively, you can change your application to directly handle SIGTERM.

## What's next

- To use Filestore with Cloud Run, refer to [Using Filestore with Cloud Run](/run/docs/tutorials/network-filesystems-filestore).

- To use Cloud Storage FUSE with Cloud Run, refer to [Using Cloud Storage FUSE with Cloud Run](/run/docs/tutorials/network-filesystems-fuse).