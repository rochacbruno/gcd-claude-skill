# GKE in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/kubernetes-engine/docs/tpc-differences
Last updated: 2026-07-09

- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Technology areas

](https://berlin.devsitetest.how/docs)






- 








[

Google Kubernetes Engine (GKE)

](https://berlin.devsitetest.how/kubernetes-engine)






- 








[

Guides

](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/kubernetes-engine-overview)












# GKE in Google Cloud Dedicated versus Google Cloud 






- On this page ** 
- [ Key differences ](#key-differences)

- [ Hardware and OS ](#hardware-and-os-differences)
- [ Availability and disaster recovery ](#availability-differences)
- [ Cost management ](#cost-management-differences)
- [ Integrations ](#integrations-differences)
- [ Security ](#security-differences)
- [ Network ](#network-differences)
- [ Workloads ](#workflow-differences)
- [ Insights and observability ](#observability-differences)
- [ AI/ML features ](#other-differences)
- [ Resource management ](#resource-management-differences)
- [ Multi-cluster management ](#fleet-and-multi-cluster-differences)

- [ Recommendations ](#recommendations)
- [ Related guides ](#related-guides)
- 










Google Kubernetes Engine is a managed environment for deploying, managing, and scaling
containerized applications. GKE is based on the
[Kubernetes](https://kubernetes.io/) open source container orchestration platform
and built on Compute Engine virtual machines. GKE offers features
like node auto-repair, load balancing, logging and monitoring, automatic
scaling, and automatic upgrades.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of GKE.



For more detailed information about GKE, see the
[GKE overview](/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and the rest of the
GKE documentation.




You can find recommendations and best practices for using GKE in
Google Cloud Dedicated, including recommended alternatives where features differ from
Google Cloud, in the [Recommendations](#recommendations) section.




## Key differences 



There are some differences between the Google Cloud Dedicated version of GKE and
the Google Cloud version.
Some notable differences include the following:






- 
GKE modes:** Only GKE Autopilot clusters are available. GKE Standard clusters are unavailable.


- 
**Storage:** Only Hyperdisk Balanced storage types are available. Other storage types are unavailable.


- 
**Compute Engine virtual machines:** Only the C3 and A3 machine series are available. Other machine types are unavailable.


- 
**GPUs and TPUs:** GPUs are available on A3 machine types only. TPUs are not available.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular GKE feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Hardware and OS



| 
**Modes of operation**
| 
Only GKE Autopilot clusters are available. GKE Standard clusters are unavailable.
| 
|

| 
**Compute Engine virtual machines** | 
Only the C3 and A3 machine series are available. Other machine types are unavailable. | 
|

| 
**GPUs and TPUs** | 


GPUs are available on A3 machine types. The only available Edge machine type is `a3-edgegpu-8g-nolssd` and it must be set explicitly by using a [custom ComputeClass](/kubernetes-engine/docs/how-to/autopilot-gpus#request-machine-custom).



TPUs are unavailable.
| 
|

| 
**Node pools**
| 

The following node configuration features are unavailable:




- Arm workloads

- Spot VMs

- Compact placement


| 
|

| 
**Release channels** | 
Only the Stable and Regular release channels are available. For clusters enrolled in the Rapid channel, the features might be available in preview. | 
|

| 
**GKE Hypercluster** | 
GKE Hypercluster isn't available. | 
|


### Availability and disaster recovery



| 
**Regions and zones** | 
Google Cloud Dedicated has only a single region,
though with multiple zones. Multi-region features and cross-region failover
are not supported. Deployment across multiple zones for resiliency is supported.
| 
|

| 
**Storage** | 
The only storage type available is Hyperdisk Balanced. All other storage
types are unavailable. Because other storage types are unavailable, using automated
disk type selection with a fallback to Persistent Disk is unavailable.
| 
|

| 
**Backup for GKE** | 
Backup for GKE is unavailable. | 
|

| 
**Autoscaling** | 


Some customization options are unavailable:



- The Performance HPA profile is unavailable.

- The VPA `InPlaceOrRecreate` mode is unavailable.

| 
|


### Cost management



| 
**Cost optimization metrics**
| 
Some cost optimization recommendations might be unavailable.
| 
|


### Integrations



| 
**Cloud Storage**
| 
Transferring data from Cloud Storage by using GKE Volume Populator is unavailable.
| 
|

| 
**Cloud Storage FUSE**
| 


The [Cloud Storage FUSE](/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) CSI driver is supported on clusters and node pools running GKE version 1.36.0-gke.1266000 or later.



To use the driver, complete the following tasks:




- 

Specify the `custom-endpoint` mount option in the volume's `mountOptions`, either in a Pod's ephemeral storage volume or in a PersistentVolume, to point to the Cloud Storage API endpoint for your environment. The endpoint value follows the format `storage.apis-berlin-build0.goog:443`.



You can use either the [CLI flag format](/storage/docs/cloud-storage-fuse/cli-options#custom-endpoint) or the [configuration file format](/storage/docs/cloud-storage-fuse/config-file#format-and-fields). Both formats are parsed directly by the driver as mount options, so you don't need to supply a separate configuration file.




- **CLI format**: `custom-endpoint=storage.apis-berlin-build0.goog:443`

- **Configuration file format**: `gcs-connection:custom-endpoint:storage.apis-berlin-build0.goog:443`




- 

Specify the `skipCSIBucketAccessCheck: "true"` volume attribute in the PersistentVolume specification or Pod's ephemeral storage volume attributes. For example:


```
volumeAttributes : 
skipCSIBucketAccessCheck : "true" 
```






For more information about specifying mount options, see [Configure mount options](/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options).

| 
|


### Security



| 
**Security features**
| 


The following security features are unavailable:




- GKE security posture

- Binary Authorization for GKE

- Confidential Google Kubernetes Engine Nodes

- GKE control plane authority

- Policy Controller


| 
|

| 
**Sensitive data encryption**
| 
Encrypting Secrets at the application layer is not supported.
| 
|
| 
**Authentication** | 
Connect gateway is unavailable. | 
|

| 
**Workload identity** | 


Workload identity pool domains (and the Kubernetes principal identifiers that use them) are specified slightly differently in Google Cloud and Google Cloud Dedicated in Germany, using `eu0.svc.id.goog` rather than `svc.id.goog`. So, for example, when specifying a Kubernetes ServiceAccount using Workload Identity Federation for GKE in an [IAM policy](/kubernetes-engine/docs/concepts/workload-identity#kubernetes-resources-iam-policies), you use `.../ PROJECT_ID .eu0.svc.id.goog/subject/ns/ NAMESPACE /sa/ KUBERNETES_SERVICE_ACCOUNT `.


| |

| 
**Privileged workload admission control**
| 
Creating and installing allowlists to run privileged workloads in
Autopilot clusters is not supported. | 
|

| 
**Node security** | 
Secure kernel module loading is unavailable. | 
|

| 
**Service agent provisioning** | 



In Google Cloud Dedicated, service agents (universe-managed service accounts) are provisioned **Just-In-Time (JIT)** when you create your first resource for a service, rather than when the API is enabled.



If you need to grant permissions to a service agent before creating resources (for example, when configuring a [Shared VPC](/kubernetes-engine/docs/how-to/cluster-shared-vpc)), you must manually create the service agent and grant it the required default roles.



For instructions on how to manually trigger service agent creation grant roles, see [Create and grant roles to service agents](/iam/docs/create-service-agent). Then, grant the default `Kubernetes Engine Service Agent` (`service- PROJECT_NUMBER @container-engine-robot.eu0-system.iam.gserviceaccount.com`) to the agent that you create.

| 
|


### Network



| 
**IP addressing**
| 
Only VPC-native clusters are supported. Route-based clusters
are unavailable.
| 
|

| 
**Maximum Pods per node** | 
There is a maximum limit of 32 Pods per node. | 
|

| 
**Network isolation** | 


The following customization options for network isolation are unavailable:




- Disabling internal and external endpoints of the control plane.

- Controlling communication between cluster Pods and Services with GKE network policies.

- Assigning additional Pod IPv4 ranges to a cluster.

- Restricting egress traffic from the API server.


| 
|

| 
**Application exposure** | 


When using the GKE Ingress controller, the global Google Cloud external application load balancer (`gxlb`) is not used. In Google Cloud Dedicated in Germany, a regional external load balancer (`rxlb`) is used.
| 
|

| 
**Multi-cluster networking** | 
Multi Cluster Ingress and multi-cluster Services (MCS) are unavailable. | 
|

| **Observability** | 
GKE Dataplane V2 observability tools are unavailable. | 
|

| 
**Cloud Service Mesh** | 
Cloud Service Mesh is unavailable. | 
|

| 
**Load balancing** | 


The following load balancing features are unavailable:



- Weighted load balancing.

- Zonal affinity for Internal passthrough Network Load Balancer.

- Utilization-based load balancing.


| 
|

| 
**IP ranges** | 


The available IP address ranges, such as for
[ingress firewall rules](/kubernetes-engine/docs/concepts/firewall-rules#ingress-fws),
depend on your environment, as follows:





- 34.3.144.0/23

- 34.3.151.0/26



| 
|


### Workloads



| 
**Predefined compute classes**
| 
Only the general-purpose and `Accelerator` compute classes are available.
All other predefined compute classes are unavailable.
| 
|



### Insights and observability



| 
**Logging and monitoring**
| 
Workload metrics are unavailable. | 
|

| 
**Google Cloud Observability**
| 
All Google Cloud Observability integrations and dashboards are unavailable. | 

|

| 
**Cluster notifications** | 
Cluster notifications are unavailable. | 
|


### AI/ML features



| 
**Ray Operator** | 
The Ray Operator for GKE is unavailable. | 
|



### Resource management



| 
**Config Sync**
| 
Config Sync is unavailable.
| 
|

| 
**Config Connector, Config Controller**
| 
Config Connector and Config Controller are unavailable. | 
|


### Multi-cluster management



| 
**Fleets** | 
Fleets, fleet dashboards, and fleet team management are unavailable. | 
|




## Recommendations





- 
[Learn more about Autopilot.](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/autopilot-overview")






## Related guides



The following information might also affect how you use and design for GKE
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)



### Related products





- 
[Compute Engine](/compute/docs)




### Google Cloud Dedicated guides





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)