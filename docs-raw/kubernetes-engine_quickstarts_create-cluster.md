# Quickstart: Create a cluster and deploy a workload

Source: https://berlin.devsitetest.how/kubernetes-engine/docs/quickstarts/create-cluster
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/kubernetes-engine/docs/tpc-differences) for more details.














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

















- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Required roles ](#required-roles)

- [ Create a cluster in GKE Autopilot mode ](#create-cluster)
- [ Deploy a sample app to your cluster ](#deploy-sample-app)
- [ View a live demo in your browser ](#view_a_live_demo_in_your_browser)
- [ Clean up to avoid billing charges ](#cleanup)
- [ What's next ](#whats-next)
- 










# Create a cluster and deploy a workload in the Google Cloud Dedicated console 












[

Autopilot


](/kubernetes-engine/docs/concepts/autopilot-overview)






A Kubernetes *cluster* provides compute, storage, networking,
and other services for applications, similar to a virtual data center. Apps and
their associated services that run in Kubernetes are called *workloads*.

This tutorial lets you quickly see a running Google Kubernetes Engine cluster and sample workload, all set up using the Google Cloud Dedicated console. You can then explore the workload in the Google Cloud Dedicated console before going on to our [more in-depth learning path](/kubernetes-engine/docs/learn/scalable-apps), or to start planning and creating your own production-ready cluster.

If you'd prefer to set up your sample cluster and workload by using Terraform, see [Create a cluster with Terraform](/kubernetes-engine/docs/quickstarts/create-cluster-using-terraform).





## Before you begin



Take the following steps to enable the Kubernetes Engine API:


- 
Visit the
[
Kubernetes Engine page](https://console.cloud.berlin-build0.goog/projectselector/kubernetes) in the Google Cloud Dedicated console.


- 
Create or select a project.


- 
Wait for the API and related services to be enabled.
This can take several minutes.






- 



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).






### Required roles










Make sure that you have the following role or roles on the project:

Compute Admin, Kubernetes Engine Admin, Service Account User



#### Check for the roles





- 


In the Google Cloud Dedicated console, go to the IAM** page.


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












## Create a cluster in GKE Autopilot mode

In Autopilot mode, Google manages your cluster configuration, including
scaling, security, and other preconfigured settings. Clusters in
Autopilot mode are optimized to run most production workloads and
provision compute resources based on your Kubernetes manifests.

- 

In the Google Cloud Dedicated console, go to the
GKE **Create an Autopilot cluster** page.

[Go to Create an Autopilot cluster](https://console.cloud.berlin-build0.goog/kubernetes/auto/add)

- 

Under **Cluster basics**, do the following:

- 

In the **Name** field, enter the following name:


```
hello-world-cluster
```


- 

Keep the default values for the rest of the settings and click
**Create** 
to start creating the cluster.

- 

When you're redirected to the **Kubernetes clusters** page, you can watch the
progress of your cluster as it is being configured, deployed, and verified.

- 

Wait until you see a check mark next to the **hello-world-cluster** page
title.

## Deploy a sample app to your cluster

Deploy a sample "hello world" web app provided by Google and stored as a
container in Artifact Registry.

- 

In the Google Cloud Dedicated console, go to the GKE **Workloads**
page.

[Go to Workloads](https://console.cloud.berlin-build0.goog/kubernetes/workload/overview)

- 

Click **Deploy** .

- 

In **Deployment name**, enter the following name:


```
hello-world-app
```


- 

In Kubernetes Cluster ,
select **hello-world-cluster**.

- 

Click **Next: Container details**

- 

Leave **Existing container image** selected, and in **Image path**
enter the following path:


```
us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
```


This simple "hello world" app is packaged into a single container, but larger
apps typically consist of several related containers that can be deployed
together and run as a single workload.

- 

Click **Next: Expose (optional)**

- 

In the **Expose** section, create a load balancing Kubernetes Service to direct
external requests to your app:

- 

Select **Expose deployment as a new service**.

- 

Leave **Port 1** set to **80**.

- 

In **Target port 1**, enter **8080**.

- 

Click **Deploy**.

GKE automatically assigns an available external IP address
to the Service.

This Service is considered to be part of the hello-world-app workload.

- 

For Autopilot clusters, you might see an error message, such as
`Does not have minimum availability`. This occurs because Autopilot
deletes and then re-creates the nodes. Wait a few minutes, then click
refresh Refresh 
to update the page.

- 

Wait until the deployment completes and you see the **Deployment details**
page.

## View a live demo in your browser

- 

In the Google Cloud Dedicated console, go to
the **Deployment details** page for **hello-world-app**:

- 

In the Google Cloud Dedicated console, go to the GKE **Workloads** page.

[Go to Workloads](https://console.cloud.berlin-build0.goog/kubernetes/workload/overview)

- 

In the **Name** column, click the name of the workload you deployed,
**hello-world-app**.

- 

In the Endpoints 
column, click the IP address, which is publicly available.

GKE opens a new browser tab and sends a request to your
app. Dismiss any secure-site warnings, and you should see
**Hello, world!** in the new browser tab.

If **Endpoints** is empty, your organization might have a policy that
prevents external access.

You have successfully created a GKE cluster in
Autopilot mode and deployed a sample workload.

## Clean up to avoid billing charges

If you plan to take additional tutorials or to [explore your sample further](/kubernetes-engine/docs/quickstarts/tour-cluster), wait until you're finished to perform this cleanup step. You can continue to use the sample Kubernetes cluster
in most GKE tutorials.

If you created a new project to learn about GKE and you no
longer need the project, [delete the project](https://console.cloud.berlin-build0.goog/cloud-resource-manager).

If you used an existing GKE project, delete the resources you
created to avoid incurring charges to your account:

- 

Go to the GKE **Clusters** page.

[Go to Clusters](https://console.cloud.berlin-build0.goog/kubernetes/list/overview)

- 

Select the row containing **hello-world-cluster**, and click

**Delete** .

- 

In the **Delete hello-world-cluster** window, do the following:

- 

In the **hello-world-cluster** field, enter `hello-world-cluster`.

- 

Click **Delete**.

If you receive an error message about the cluster being repaired, you can
wait for the process to complete, and then delete the cluster. This operation
might take some time to complete.

- 

If you created a logs sink and bucket when following instructions in other
tutorials:

- 

Go to the Cloud Logging **Logs storage** page.

[Go to Logs storage](https://console.cloud.berlin-build0.goog/logs/storage)

- 

Select **hello-world-cluster-bucket** and click **Delete**.

- 

Go to the Logging **Log router** page.

[Go to Log router](https://console.cloud.berlin-build0.goog/logs/router)

- 

Select **hello-world-cluster-sink** and click **Delete**.







## What's next



- 

[Explore your cluster and workload](/kubernetes-engine/docs/quickstarts/tour-cluster) 
to learn about the some of the key workload settings and resources that
you deployed.

- 

Try our more in-depth [Learning path: Scalable apps](/kubernetes-engine/docs/learn/scalable-apps).

- 

Learn how to get started with real life cluster administration in our [Cluster administration overview](/kubernetes-engine/docs/how-to/cluster-admin-overview).