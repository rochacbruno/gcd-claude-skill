# GKE overview

Source: https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/kubernetes-engine-overview
Last updated: 2026-07-16

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

Application hosting

](https://berlin.devsitetest.how/docs/application-hosting)






- 








[

Google Kubernetes Engine (GKE)

](https://berlin.devsitetest.how/kubernetes-engine/docs)






- 








[

Guides

](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/kubernetes-engine-overview)












# GKE overview 






- On this page ** 
- [ Get started with GKE ](#get-started)
- [ When to use GKE ](#when-to-use)

- [ Benefits of GKE ](#benefits)

- [ How GKE works ](#how_works)

- [ Kubernetes versions and features ](#kubernetes_versions_and_features)
- [ Modes of operation ](#modes_of_operation)

- [ What's next ](#whats_next)
- 


















[

Autopilot


](/kubernetes-engine/docs/concepts/autopilot-overview)









[

Standard


](/kubernetes-engine/docs/concepts/choose-cluster-mode)








This page provides an overview of Google Kubernetes Engine (GKE). GKE
is a managed implementation of the [Kubernetes](https://kubernetes.io) open
source container orchestration platform. Kubernetes was developed by Google,
drawing on years of experience operating production workloads at scale on
[Borg](https://research.google/pubs/pub43438/), Google's in-house cluster
management system. With GKE, you can deploy and operate your own
containerized applications at scale using
Google Cloud Dedicated in Germany's infrastructure.

## Get started with GKE 

You can start exploring GKE in minutes.

- 

[Get started in Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/kubernetes/overview/get-started)

- Try the [quickstart](/kubernetes-engine/docs/deploy-app-cluster) to deploy a
containerized web application.

- Read the
[Autopilot overview](/kubernetes-engine/docs/concepts/autopilot-overview),
which has guidance and resources for planning and operating your platform.

## When to use GKE

GKE is ideal if you need a platform that lets you configure the
infrastructure that runs your containerized apps, such as networking, scaling,
hardware, and security. GKE provides the operational power of
Kubernetes while managing many of the underlying components, such as the
control plane and nodes, for you.

### Benefits of GKE

The following table describes some of the benefits of using GKE
as your managed Kubernetes platform:




| 
GKE benefits | 
|

| 
Platform management | 




- Fully-managed nodes in GKE
[Autopilot mode](/kubernetes-engine/docs/concepts/autopilot-overview)
with built-in hardening and best practice configurations automatically
applied.

- Managed upgrade experience with
[release channels](/kubernetes-engine/docs/concepts/release-channels)
to improve security, reliability, and compliance.

- Flexible
[maintenance windows and exclusions](/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)
that let you configure upgrade type and scope
to meet business needs and architecture constraints.



- Automatic scaling of nodes based on the number of Pods in the
cluster with Autopilot mode.


- [Node auto-repair](/kubernetes-engine/docs/concepts/node-auto-repair)
to maintain node health and availability.





| 
|

| 
Improved security posture | 




- Hardened node operating system for apps: [Container-Optimized OS](/container-optimized-os/docs/concepts/security).

- [Built-in security measures](/kubernetes-engine/docs/concepts/autopilot-security).


- [Automatic upgrades](/kubernetes-engine/docs/concepts/release-channels)
to new GKE versions.




| 
|

| 
Cost optimization | 




- 

In Autopilot mode, pay only for the compute resources
your running Pods request.





- Minimized operational overhead in Autopilot mode because
Google Cloud Dedicated manages both the
nodes and the control plane.


| 
|

| 
Reliability and availability | 






- Highly-available control plane and worker nodes in
[Autopilot mode](/kubernetes-engine/docs/concepts/autopilot-overview).


- [Proactive monitoring and recommendations](/kubernetes-engine/docs/deprecations)
to mitigate potential workload disruptions caused by upcoming
deprecations.



| 
|



## How GKE works

A GKE environment consists of *nodes*, which are [Compute Engine
virtual machines (VMs)](/compute), that are grouped together to form a *cluster*. You
package your apps (also called *workloads*) into containers. You deploy sets
of containers as *Pods* to your nodes. You use the Kubernetes API to interact
with your workloads, including administering, scaling, and monitoring.

Kubernetes clusters have a set of management nodes called the *control plane*,
which run system components such as the Kubernetes API server. In
GKE, Google Cloud Dedicated manages the
control plane and system components for you. In Autopilot mode, which
is the recommended way to run GKE,
Google Cloud Dedicated also manages your worker nodes.
Google Cloud Dedicated automatically upgrades
component versions for improved stability and security, which helps ensure high availability and the integrity of data stored in the cluster's
persistent storage.

For more information, refer to
[GKE cluster architecture](/kubernetes-engine/docs/concepts/cluster-architecture).

### Kubernetes versions and features

GKE automatically upgrades the control plane and worker nodes of clusters to new Kubernetes versions so that the clusters receives new features, bug fixes, and security patches. GKE provides various capabilities to manage these upgrades to minimize disruption to your workloads while keeping them performant, reliable, and secure.

For more information, see [About GKE cluster upgrades](/kubernetes-engine/upgrades).


Best practice**:

If you want to try less stable Kubernetes features in the *alpha* or *beta* stages, use
[alpha clusters](/kubernetes-engine/docs/concepts/alpha-clusters), or [use Kubernetes beta APIs with GKE clusters](/kubernetes-engine/docs/how-to/use-beta-apis).
Review the [implications](/kubernetes-engine/docs/how-to/use-beta-apis#considerations-for-beta-apis) before enabling beta APIs in production clusters.



### Modes of operation

GKE in Google Cloud Dedicated has one mode of operation,
Autopilot, which offers a fully managed experience. GKE
Standard clusters are unavailable in Google Cloud Dedicated.

## What's next

- Learn about [GKE differences in Google Cloud Dedicated versus Google Cloud](/kubernetes-engine/docs/tpc-differences).

- [Start learning about GKE](/kubernetes-engine/docs/learn).

- [Learn how to deploy a containerized application in GKE](/kubernetes-engine/docs/deploy-app-cluster).

- [Learn more about types of clusters](/kubernetes-engine/docs/concepts/types-of-clusters).

- [Learn more about Kubernetes](/kubernetes-engine/docs/learn/get-started-with-kubernetes).

- [Explore the GKE documentation](/kubernetes-engine/docs/about).