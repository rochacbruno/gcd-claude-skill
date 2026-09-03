# Container-Optimized OS in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/container-optimized-os/docs/tpc-differences
Last updated: 2026-08-26

- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Container-Optimized OS

](https://documentation.s3ns.fr/container-optimized-os/docs)






- 








[

Guides

](https://documentation.s3ns.fr/container-optimized-os/docs/how-to/create-configure-instance)












# Container-Optimized OS in Cloud de Confiance versus Google Cloud 






- On this page 
- [ Key differences ](#key-differences)

- [ Hardware and OS ](#hardware-and-os-differences)
- [ Creating and configuring instances ](#creating-and-configuring-instances)
- [ Running containers on instances ](#running-containers-on-instances)
- [ Monitoring ](#monitoring)
- [ Building from open source ](#building-from-open-source)
- [ Toolbox ](#toolbox)
- [ GPU accelerators ](#gpu-accelerators)
- [ Workflows and tools ](#workflow-differences)

- [ Related guides ](#related-guides)
- 










Container-Optimized OS (COS) is an operating system image for your Compute Engine VMs that is optimized for running Docker containers. With Container-Optimized OS, you can bring up your Docker containers on Cloud de Confiance quickly, efficiently, and securely.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Container-Optimized OS.



For more detailed information about Container-Optimized OS, see the
[Container-Optimized OS overview](/container-optimized-os/docs) and the rest of the
Container-Optimized OS documentation.




## Key differences 



There are some differences between the Cloud de Confiance version of Container-Optimized OS and
the Google Cloud version.
Some notable differences include the following:






- 
COS milestones 113 and below are unavailable


- 
ARM OS image families are unavailable


- 
[Automatic updates](/container-optimized-os/docs/concepts/auto-update) are unavailable





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Container-Optimized OS feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Hardware and OS



| 
**Operating system details**
| 
The following differences apply to the image project: 




- 
All references to projects should be prefixed with `s3ns-system:cos-cloud`



| 
|


### Creating and configuring instances



| 
**Creating a simple instance**
| 
Creating an instance with a container or containers as described in [Creating and configuring an instance](/container-optimized-os/docs/how-to/create-configure-instance) is not available, as the Konlet workflow is not supported in Cloud de Confiance by S3NS. Instead, follow the instructions in [Create a Compute Engine instance](/compute/docs/instances/create-start-instance) to create an instance, selecting a Container-Optimized OS version as your boot disk.
| 
|

| 
**Other metadata flags**
| 
[Other metadata flags](/container-optimized-os/docs/how-to/create-configure-instance#other_metadata_flags) are unavailable
| 
|

| 
**Enabling or disabling automatic updates**
| 
[Enabling or disabling automatic updates](/container-optimized-os/docs/how-to/create-configure-instance#enabling_or_disabling_automatic_updates) is unavailable
| 
|


### Running containers on instances



| 
**Container Registry**
| 
Container Registry is unavailable
| 
|

| 
**Private images**
| 
[Accessing private images](/container-optimized-os/docs/how-to/run-container-instance#accessing_private_images_in_or) command `docker-credential-gcr configure-docker` should be replaced with `docker-credential-gcr configure-docker --registries s3nsregistry.fr`
| 
|

| 
**Configuring Docker daemon**
| 
[Configuring Docker daemon to pull images from registry cache](/container-optimized-os/docs/how-to/run-container-instance#configuring_docker_daemon_to_pull_images_from_registry_cache) is unavailable
| 
|


### Monitoring



| 
**Node Problem Detector**
| 
[Monitoring system health with Node Problem Detector](/container-optimized-os/docs/how-to/monitoring) is unavailable
| 
|


### Building from open source



| 
**Building from open source**
| 
[Building from open source](/container-optimized-os/docs/how-to/building-from-open-source) is unavailable
| 
|


### Toolbox



| 
**References to gcr.io/cos-cloud/toolbox**
| 
The toolbox Docker image has a different repository path in Cloud de Confiance. Use `docker.s3nsregistry.fr/s3ns-system/cos-cloud/toolbox/toolbox` if you need to pull the image
| 
|


### GPU accelerators



| 
**Pulling cos-gpu-installer**
| 
[The cos-gpu-installer](/container-optimized-os/docs/how-to/run-gpus) Docker image has a different repository path in Cloud de Confiance.Use `docker.s3nsregistry.fr/s3ns-system/cos-cloud/cos-gpu-installer/cos_gpu_installer` if you need to pull the image
| 
|

| 
**Available GPUs**
| 

NVIDIA H100 is available
| 
|

| 
**Unavailable GPUs**
| 

The following machine types and their associated gpu drivers are unavailable: A2, G2, and N1

Pre-compiled close source drivers cannot be mirrored in Cloud de Confiance by S3NS, hence the following GPUs are unavailable:


- 
NVIDIA P4


- 
NVIDIA V100


- 
NVIDIA P100

| 
|


### Workflows and tools



| 
**Artifact Registry domain**
| 
Use `s3nsregistry.fr` instead of `pkg.dev` when using images in Artifact Registry
| 
|

| 
**Oval vulnerability feed**
| 
[Oval vulnerability feed](/container-optimized-os/docs/how-to/scanning-with-oval-vulnerability-feed) is unavailable
| 
|

| 
**Configuring instances with user-defined guest policies**
| 
[OSConfig](/container-optimized-os/docs/how-to/osconfig) is unavailable
| 
|

| 
**OS Policy**
| 
[OS Policy](/container-optimized-os/docs/how-to/cis-compliance#using-os-policy) is unavailable
| 
|





## Related guides



The following information might also affect how you use and design for Container-Optimized OS
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)