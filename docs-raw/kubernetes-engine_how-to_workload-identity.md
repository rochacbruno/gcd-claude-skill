# Authenticate to Google Cloud Dedicated APIs from GKE workloads

Source: https://berlin.devsitetest.how/kubernetes-engine/docs/how-to/workload-identity
Last updated: 2026-07-08

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

GKE security

](https://berlin.devsitetest.how/kubernetes-engine/docs)






- 








[

Guides

](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/security-overview)












# Authenticate to Google Cloud Dedicated APIs from GKE workloads 






- On this page ** 
- [ Before you begin ](#before_you_begin)
- [ Enable Workload Identity Federation for GKE on clusters and node pools ](#enable_on_clusters_and_node_pools)

- [ Migrate existing workloads to Workload Identity Federation for GKE ](#migrate_applications_to)

- [ Configure applications to use Workload Identity Federation for GKE ](#authenticating_to)

- [ Configure authorization and principals ](#configure-authz-principals)
- [ Optional: Configure service mesh options ](#configure-service-mesh)
- [ Verify the Workload Identity Federation for GKE setup ](#verify)
- [ Alternative: link Kubernetes ServiceAccounts to IAM ](#kubernetes-sa-to-iam)

- [ Use Workload Identity Federation for GKE from your code ](#using_from_your_code)
- [ Use quota from a different project with Workload Identity Federation for GKE ](#quota-project)
- [ Clean up ](#clean_up)

- [ Revoke access ](#revoking_access)
- [ Disable Workload Identity Federation for GKE ](#disabling_on_a_cluster)

- [ Disable Workload Identity Federation for GKE in your organization ](#disabling_in_your_organization)
- [ Troubleshooting ](#troubleshoot)
- [ What's next ](#whats_next)
- 


















[

Autopilot


](/kubernetes-engine/docs/concepts/autopilot-overview)









[

Standard


](/kubernetes-engine/docs/concepts/choose-cluster-mode)








This page shows you how to more securely access Google Cloud Dedicated APIs from
your workloads that run in Google Kubernetes Engine (GKE) clusters by using
*Workload Identity Federation for GKE*.

This page is for Identity and account admins, Operators, and
Developers who create and manage policies related to user
permissions. To learn more about common roles and example tasks that we
reference in Google Cloud Dedicated in Germany content, see
[Common GKE user roles and tasks](/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with
[Workload Identity Federation for GKE concepts](/kubernetes-engine/docs/concepts/workload-identity).

## Before you begin

Before you start, make sure that you have performed the following tasks:


- 
Enable





the Google Kubernetes Engine API.

[

Enable Google Kubernetes Engine API

](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=container.googleapis.com)

- To use the Google Cloud CLI for this task,
[install](/sdk/docs/install) and then
[initialize](/sdk/docs/initialize) the
gcloud CLI. If you previously installed the gcloud CLI, get the latest
version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document.



- Ensure that the Google Cloud Dedicated APIs that you want to access are supported
by Workload Identity Federation for GKE. For a list of supported APIs, see
[Supported products and limitations](/iam/docs/federated-identity-supported-services).
If the API isn't supported or if your use case is blocked by the
limitations of Workload Identity Federation for that service, see
[Alternative: link Kubernetes ServiceAccounts to IAM](#kubernetes-sa-to-iam)
in this page.

- 

Ensure that you have enabled the IAM Service Account Credentials API.

[Enable
IAM Credentials API](https://console.cloud.berlin-build0.goog/apis/api/iamcredentials.googleapis.com/overview)

- 

Ensure that you have the following [IAM roles](/iam/docs/roles-permissions/container):

- `roles/container.admin`

- `roles/iam.serviceAccountAdmin`

- 

Ensure that you understand the [limitations of Workload Identity Federation for GKE](/kubernetes-engine/docs/concepts/workload-identity#restrictions).

- 

Ensure that you have an existing Autopilot or Standard
cluster. To create a new cluster, see
[Create an Autopilot cluster](/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).

## Enable Workload Identity Federation for GKE on clusters and node pools

In Autopilot, Workload Identity Federation for GKE is always enabled. Skip to the
[Configure applications to use Workload Identity Federation for GKE](#authenticating_to) section.

In Standard, you enable Workload Identity Federation for GKE on clusters and node
pools using the Google Cloud CLI or the Google Cloud Dedicated console.
Workload Identity Federation for GKE **must** be enabled at the cluster level before you can
enable Workload Identity Federation for GKE on node pools.

You can enable Workload Identity Federation for GKE on an existing Standard cluster by
using the gcloud CLI or the Google Cloud Dedicated console. Existing node pools
are unaffected, but any new node pools in the cluster use Workload Identity Federation for GKE.


[gcloud](#gcloud) [Console](#console) 
More 




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

To enable Workload Identity Federation for GKE on an existing cluster, run the following
command:


```
gcloud container clusters update CLUSTER_NAME \ 
--location = LOCATION \ 
--workload-pool = PROJECT_ID .eu0.svc.id.goog
```


Replace the following:

- ` CLUSTER_NAME `: the name of your existing cluster.

- ` LOCATION `: the Compute Engine
[region or zone](/compute/docs/regions-zones/viewing-regions-zones) of
the cluster control plane, such as `us-central1` or `us-central1-a`.

- ` PROJECT_ID `: your Google Cloud Dedicated project ID.




To enable Workload Identity Federation for GKE on an existing cluster, do the following:

- 

Go to the **Google Kubernetes Engine** page in Google Cloud Dedicated console.

[Go to Google Kubernetes Engine](https://console.cloud.berlin-build0.goog/kubernetes/list)

- 

In the cluster list, click the name of the cluster you want to modify.

- 

On the cluster details page, in the **Security** section, click
edit **Edit Workload Identity**.

- 

In the **Edit Workload Identity** dialog, select the **Enable Workload Identity** checkbox.

- 

Click **Save changes**.




### Migrate existing workloads to Workload Identity Federation for GKE

After you enable Workload Identity Federation for GKE on an existing cluster, you might want to
migrate your running workloads to use Workload Identity Federation for GKE. Select the
migration strategy that is ideal for your environment. You can create new node pools with Workload Identity Federation for GKE
enabled, or update existing node pools to enable Workload Identity Federation for GKE.

You can only enable Workload Identity Federation for GKE on a node pool if Workload Identity Federation for GKE
is enabled on the cluster.


Best practice**:

Create new node pools if you also need to modify your
applications to be compatible with Workload Identity Federation for GKE.



#### Create a new node pool

All new node pools that you create default to using Workload Identity Federation for GKE if the
cluster has Workload Identity Federation for GKE enabled. To create a new node pool with
Workload Identity Federation for GKE enabled, run the following command:


```
gcloud container node-pools create ** NODEPOOL_NAME \ 
--cluster = CLUSTER_NAME \ 
--location = CONTROL_PLANE_LOCATION \ 
--workload-metadata = GKE_METADATA
```


Replace the following:

- ` NODEPOOL_NAME `: the name of the new node pool.

- ` CLUSTER_NAME `: the name of the existing cluster that has
Workload Identity Federation for GKE enabled.

- ` CONTROL_PLANE_LOCATION `: the Compute Engine
[region or zone](/compute/docs/regions-zones/viewing-regions-zones) of
the cluster control plane, such as `us-central1` or `us-central1-a`.

The `--workload-metadata=GKE_METADATA` flag configures the node pool to use
the GKE metadata server.


Best practice**:

Include the flag
so that node pool creation fails if Workload Identity Federation for GKE is not enabled on the
cluster.



#### Update an existing node pool

You can manually enable Workload Identity Federation for GKE on existing node pools after you
enable Workload Identity Federation for GKE on the cluster.


[gcloud](#gcloud) [Console](#console) 
**More 




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

To modify an existing node pool to use Workload Identity Federation for GKE, run the following
command:


```
gcloud container node-pools update NODEPOOL_NAME \ 
--cluster = CLUSTER_NAME \ 
--location = CONTROL_PLANE_LOCATION \ 
--workload-metadata = GKE_METADATA
```


If a cluster has Workload Identity Federation for GKE enabled, you can selectively disable it on a
specific node pool by explicitly specifying
`--workload-metadata=GCE_METADATA`.




To modify an existing node pool to use Workload Identity Federation for GKE, perform the following
steps:

- 

Go to the **Google Kubernetes Engine** page in Google Cloud Dedicated console.

[Go to Google Kubernetes Engine](https://console.cloud.berlin-build0.goog/kubernetes/list)

- 

In the cluster list, click the name of the cluster that you want to modify.

- 

Click the **Nodes** tab.

- 

In the **Node Pools** section, click the name of the node pool that you
want to modify.

- 

On the **Node pool details** page, click edit **Edit**.

- 

On the **Edit node pool** page, in the **Security** section, select the
**Enable GKE Metadata Server** checkbox.

- 

Click **Save**.




## Configure applications to use Workload Identity Federation for GKE

To let your GKE applications authenticate to Google Cloud Dedicated
APIs using Workload Identity Federation for GKE, you create IAM policies for
the specific APIs. The principal in these policies is an IAM
*principal identifier* that corresponds to the workloads, namespaces, or
Kubernetes ServiceAccounts. This process returns a federated access token that
your workload can use in API calls.

Alternatively, you can configure Kubernetes ServiceAccounts to impersonate
IAM service accounts, which configures GKE to exchange the
federated access token for an access token from the IAM
Service Account Credentials API. For details, see the
[Alternative: link Kubernetes ServiceAccounts to IAM](#kubernetes-sa-to-iam)
section.

### Configure authorization and principals

- 

Get credentials for your cluster:


```
gcloud container clusters get-credentials CLUSTER_NAME \ 
--location = CONTROL_PLANE_LOCATION 
```


Replace the following:

- ` CLUSTER_NAME `: the name of your cluster
that has Workload Identity Federation for GKE enabled.

- ` CONTROL_PLANE_LOCATION `: the Compute Engine
[region or zone](/compute/docs/regions-zones/viewing-regions-zones) of
the cluster control plane, such as `us-central1` or `us-central1-a`.

- 

Create a namespace to use for the Kubernetes service account. You can also
use the `default` namespace or any existing namespace.


```
kubectl create namespace NAMESPACE 
```


- 

Create a Kubernetes ServiceAccount for your application to use. You can
also use any existing Kubernetes ServiceAccount in any namespace. If you
don't assign a ServiceAccount to your workload, Kubernetes assigns the
`default` ServiceAccount in the namespace.


```
kubectl create serviceaccount KSA_NAME \ 
--namespace NAMESPACE 
```


Replace the following:

- ` KSA_NAME `: the name of your new Kubernetes
ServiceAccount.

- ` NAMESPACE `: the name of the Kubernetes namespace
for the ServiceAccount.

- 

Create an IAM allow policy that references the Kubernetes
ServiceAccount. As a good practice, grant permissions to specific
Google Cloud Dedicated resources that your application needs to access. You must
have relevant IAM permissions to create allow policies in
your project.

For example, the following command grants the
[Kubernetes Engine Cluster Viewer](/iam/docs/roles-permissions/container#container.clusterViewer)
(`roles/container.clusterViewer`) role to the ServiceAccount that you
created:


```
gcloud projects add-iam-policy-binding projects/ PROJECT_ID \ 
--role = roles/container.clusterViewer \ 
--member = principal://iam.googleapis.com/projects/ PROJECT_NUMBER /locations/global/workloadIdentityPools/ PROJECT_ID .eu0.svc.id.goog/subject/ns/ NAMESPACE /sa/ KSA_NAME \ 
--condition = None
```


Replace the following:

- ` PROJECT_ID `: your Google Cloud Dedicated project ID.

- ` PROJECT_NUMBER `: your numerical Google Cloud Dedicated
project number.

You can grant roles on any Google Cloud Dedicated resource that supports
IAM allow policies. The syntax of the principal identifier
depends on the Kubernetes resource. For a list of supported identifiers, see
[Principal identifiers for Workload Identity Federation for GKE](/kubernetes-engine/docs/concepts/workload-identity#principal-id-examples).

### Optional: Configure service mesh options

If you use Istio or Cloud Service Mesh to manage your environment, add the following
annotation to the `metadata.annotations` field in your Pod specification:


```
metadata:
annotations:
**proxy.istio.io/config: '{ "holdApplicationUntilProxyStarts": true }'**
```


This annotation prevents your containers from starting until the service mesh
proxy is ready to redirect traffic from your applications.

### Verify the Workload Identity Federation for GKE setup

In this section, you create a Cloud Storage bucket and grant view access on
the bucket to the Kubernetes ServiceAccount that you created in the previous
section. You then deploy a workload and test that the container can list
clusters in the project.

- 

Create an empty Cloud Storage bucket:


```
gcloud storage buckets create gs:// BUCKET 
```


Replace ` BUCKET ` with a name for your new bucket.

- 

Grant the
[Storage Object Viewer](/iam/docs/roles-permissions/storage#storage.objectViewer)
(`roles/storage.objectViewer`) role to the ServiceAccount that you
created:


```
gcloud storage buckets add-iam-policy-binding gs:// BUCKET \ 
--role = roles/storage.objectViewer \ 
--member = principal://iam.googleapis.com/projects/ PROJECT_NUMBER /locations/global/workloadIdentityPools/ PROJECT_ID .eu0.svc.id.goog/subject/ns/ NAMESPACE /sa/ KSA_NAME \ 
--condition = None
```


Replace the following:

- ` PROJECT_ID `: your Google Cloud Dedicated project ID.

- ` PROJECT_NUMBER `: your numerical Google Cloud Dedicated
project number.

- ` NAMESPACE `: the Kubernetes namespace that contains
the ServiceAccount.

- ` KSA_NAME `: the name of the ServiceAccount.

- 

Save the following manifest as `test-app.yaml`:


```
apiVersion : v1 
kind : Pod 
metadata : 
name : test-pod 
** namespace : NAMESPACE **
spec : 
** serviceAccountName : KSA_NAME **
containers : 
- name : test-pod 
image : google/cloud-sdk:slim 
command : [ "sleep" , "infinity" ] 
resources : 
requests : 
cpu : 500m 
memory : 512Mi 
ephemeral-storage : 10Mi 
```


- 

**In Standard clusters only**, add the following to the `template.spec`
field to place the Pods on node pools that use Workload Identity Federation for GKE.

Skip this step in Autopilot clusters, which reject this nodeSelector
because every node uses Workload Identity Federation for GKE.


```
spec : 
** nodeSelector : 
iam.gke.io/gke-metadata-server-enabled : "true" **
```


- 

Apply the configuration to your cluster:


```
kubectl apply -f test-app.yaml
```


- 

Wait for the Pod to become ready. To check the status of the Pod, run the
following command:


```
kubectl get pods --namespace = NAMESPACE 
```


When the Pod is ready, the output is similar to the following:


```
NAME READY STATUS RESTARTS AGE
test-pod 1/1 Running 0 5m27s
```


- 

Open a shell session in the Pod:


```
kubectl exec -it pods/test-pod --namespace = NAMESPACE -- /bin/bash
```


- 

Get a list of objects in the bucket:


```
curl -X GET -H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
"https://storage.googleapis.com/storage/v1/b/ BUCKET /o" 
```


The output is the following:


```
{
"kind": "storage#objects"
}
```


This output shows that your Pod can access objects in the bucket.

### Alternative: link Kubernetes ServiceAccounts to IAM


Best practice**:


Use IAM principal identifiers to configure
Workload Identity Federation for GKE. However, this federated identity has specific [limitations](/iam/docs/federated-identity-supported-services) for each
supported Google Cloud Dedicated API. If these limitations apply to you, use the
following steps to configure access to those APIs from your GKE
workloads.



- 

Create a Kubernetes namespace:


```
kubectl create namespace NAMESPACE 
```


- 

Create a Kubernetes ServiceAccount:


```
kubectl create serviceaccount KSA_NAME \ 
--namespace = NAMESPACE 
```


- 

Create an IAM service account. You can also use any existing
IAM service account in any project in your organization.


```
gcloud iam service-accounts create IAM_SA_NAME \ 
--project = IAM_SA_PROJECT_ID 
```


Replace the following:

- ` IAM_SA_NAME `: a name for your new IAM
service account.

- ` IAM_SA_PROJECT_ID `: the project ID for your
IAM service account.

For information on authorizing IAM service accounts to access Google Cloud Dedicated in Germany
APIs, see [Understanding service accounts](/iam/docs/understanding-service-accounts).

- 

Grant your IAM service account the roles that it needs on
specific Google Cloud Dedicated APIs:


```
gcloud projects add-iam-policy-binding IAM_SA_PROJECT_ID \ 
--member "serviceAccount: IAM_SA_NAME @ IAM_SA_PROJECT_ID .eu0.iam.gserviceaccount.com" \ 
--role " ROLE_NAME " 
```


Replace ` ROLE_NAME ` with the name of the role, like
`roles/spanner.viewer`.

- 

Create an IAM allow policy that gives the Kubernetes
ServiceAccount access to impersonate the IAM service account:


```
gcloud iam service-accounts add-iam-policy-binding IAM_SA_NAME @ IAM_SA_PROJECT_ID .eu0.iam.gserviceaccount.com \ 
--role roles/iam.workloadIdentityUser \ 
--member "serviceAccount: PROJECT_ID .eu0.svc.id.goog[ NAMESPACE / KSA_NAME ]" 
```


The member name must include the namespace and Kubernetes ServiceAccount
name. For example, `serviceAccount:example-project.eu0.svc.id.goog[example-namespace/example-serviceaccount]`.

- 

Annotate the Kubernetes ServiceAccount so that GKE sees the
link between the service accounts:


```
kubectl annotate serviceaccount KSA_NAME \ 
--namespace NAMESPACE \ 
iam.gke.io/gcp-service-account = IAM_SA_NAME @ IAM_SA_PROJECT_ID .eu0.iam.gserviceaccount.com
```


Both the IAM allow policy **and** the annotation are
required when you use this method.

- 

Optional: Annotate the Kubernetes ServiceAccount so that your applications
get the identifier in the IAM principal identifier syntax:


```
kubectl annotate serviceaccount KSA_NAME \ 
--namespace = NAMESPACE \ 
iam.gke.io/return-principal-id-as-email = "true" 
```


## Use Workload Identity Federation for GKE from your code

Authenticating to Google Cloud Dedicated services from your code is the same process
as authenticating using the [Compute Engine metadata
server](/compute/docs/storing-retrieving-metadata). When you use Workload Identity Federation for GKE, your
requests to the instance metadata server are routed to the
[GKE metadata server](/kubernetes-engine/docs/concepts/workload-identity#metadata_server).
Existing code that authenticates using the instance metadata server (like code
using the [Google Cloud Dedicated client libraries](/docs/authentication/client-libraries))
should work without modification.

## Use quota from a different project with Workload Identity Federation for GKE

On clusters running GKE version 1.24 or later, you can optionally configure your Kubernetes service account to use quota
from a different Google Cloud Dedicated project when making calls to
the `GenerateAccessToken` and the `GenerateIdToken` methods in the [IAM Service Account Credentials API](/iam/docs/reference/credentials/rest#rest-resource:-v1.projects.serviceaccounts). This lets you avoid using the entire quota in
your main project, and instead use quota from other projects for
these services in your cluster.

To configure a *quota project* with Workload Identity Federation for GKE, do the
following:

- 

Grant the `serviceusage.services.use` permission on the quota project
to the Kubernetes service account.


```
gcloud projects add-iam-policy-binding QUOTA_PROJECT_ID \ 
--role = roles/serviceusage.serviceUsageConsumer \ 
--member = 'principal://iam.googleapis.com/projects/ PROJECT_NUMBER /locations/global/workloadIdentityPools/ PROJECT_ID .eu0.svc.id.goog/subject/ns/ NAMESPACE /sa/ KSA_NAME ' \ 
```


Replace ` QUOTA_PROJECT_ID ` with the project ID
of the quota project.

- 

Annotate the Kubernetes service account with the quota project:


```
kubectl annotate serviceaccount KSA_NAME \ 
--namespace NAMESPACE \ 
iam.gke.io/credential-quota-project = QUOTA_PROJECT_ID 
```


To verify the configuration works correctly, do the following:

- 

Create a Pod and start a shell session. See the Kubernetes documentation
to [Get a Shell to a Running Container](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/).

- 

Make a request to the metadata server:


```
curl -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token
```


- 

Go to the **IAM Service Accounts Credentials API** page
in the Google Cloud Dedicated console for your quota project:

[Go to APIs](https://console.cloud.berlin-build0.goog/apis/api/iamcredentials.googleapis.com/metrics)

- 

Check for changes in traffic.

## Clean up

To stop using Workload Identity Federation for GKE, revoke access to the IAM
service account and disable Workload Identity Federation for GKE on the cluster.

### Revoke access

To revoke access to the principal, remove the IAM allow policy
that you created in the
[Configure applications to use Workload Identity Federation for GKE](#authenticating_to) section.

For example, to revoke access to an Artifact Registry repository, run the following
command:


```
gcloud artifacts repositories remove-iam-policy-binding REPOSITORY_NAME \ 
--location = REPOSITORY_LOCATION \ 
--member = 'principal://iam.googleapis.com/projects/ PROJECT_NUMBER /locations/global/workloadIdentityPools/ PROJECT_ID .eu0.svc.id.goog/subject/ns/ NAMESPACE /sa/ KSA_NAME ' \ 
--role = 'roles/artifactregistry.reader' \ 
--all
```


### Disable Workload Identity Federation for GKE

You can only disable Workload Identity Federation for GKE on Standard
clusters.


[gcloud](#gcloud) [Console](#console) 
More 




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

Disable Workload Identity Federation for GKE on each node pool:


```
gcloud container node-pools update NODEPOOL_NAME \ 
--cluster = CLUSTER_NAME \ 
--location = CONTROL_PLANE_LOCATION \ 
--workload-metadata = GCE_METADATA
```


Repeat this command for every node pool in the cluster.

- 

Disable Workload Identity Federation for GKE in the cluster:


```
gcloud container clusters update CLUSTER_NAME \ 
--location = CONTROL_PLANE_LOCATION \ 
--disable-workload-identity
```





- 

Go to the **Google Kubernetes Engine** page in Google Cloud Dedicated console.

[Go to Google Kubernetes Engine](https://console.cloud.berlin-build0.goog/kubernetes/list)

- 

In the cluster list, click the name of the cluster that you want to modify.

- 

Click the **Nodes** tab.

- 

To disable Workload Identity Federation for GKE on each node pool, do the following for
each node pool in the **Node Pools** section:

- Click the name of the node pool that you want to modify.

- On the **Node pool details** page, click edit **Edit**.

- On the **Edit node pool** page, in the **Security** section, clear the
**Enable GKE Metadata Server** checkbox.

- Click **Save**.

- 

To disable Workload Identity Federation for GKE for the cluster, do the following:

- Click the **Details** tab.

- In the **Security** section, next to **Workload Identity**, click
edit **Edit**.

- In the **Edit Workload Identity** dialog, clear the
**Enable Workload Identity** checkbox.

- Click **Save changes**.




## Disable Workload Identity Federation for GKE in your organization

The steps in the
[link Kubernetes ServiceAccounts to IAM](/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam)
section let Kubernetes ServiceAccounts impersonate the identity of the linked
IAM service account. Long-lived API tokens for the Kubernetes
ServiceAccounts can be exchanged for the corresponding IAM
[service account access tokens](/docs/authentication/token-types#sa-access-tokens).

You might want to disable Workload Identity Federation for GKE for clusters in your
organization, folder, or project when you want to isolate workloads from
IAM service accounts. For example, if you plan to
[disable service account creation](/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_creation_managed)
or
[disable service account key creation](/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation),
disabling Workload Identity Federation for GKE prevents the exchange of ServiceAccount tokens
for IAM service account access tokens.

For more information, see
[Disable workload identity cluster creation](/resource-manager/docs/organization-policy/restricting-service-accounts#disable_workload_identity_cluster_creation).

## Troubleshooting

For troubleshooting information, refer to [Troubleshooting Workload Identity Federation for GKE](/kubernetes-engine/docs/troubleshooting/troubleshooting-security#workload-identity).

## What's next

- Learn more about [Workload Identity Federation for GKE](/kubernetes-engine/docs/concepts/workload-identity).

- Read the [GKE security overview](/kubernetes-engine/docs/concepts/security-overview).

- Learn about [IAM service accounts](/iam/docs/understanding-service-accounts).