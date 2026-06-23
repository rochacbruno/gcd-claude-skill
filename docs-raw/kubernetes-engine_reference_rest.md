# Kubernetes Engine API

Source: https://berlin.devsitetest.how/kubernetes-engine/docs/reference/rest
Last updated: 2026-04-15

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

Reference

](https://berlin.devsitetest.how/kubernetes-engine/docs/authentication)












# Kubernetes Engine API 






- On this page ** 
- [ Service: container.googleapis.com ](#service:-container.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)

- [ REST Resource: v1beta1.projects.aggregated.usableSubnetworks ](#rest-resource:-v1beta1.projects.aggregated.usablesubnetworks)
- [ REST Resource: v1beta1.projects.locations ](#rest-resource:-v1beta1.projects.locations)
- [ REST Resource: v1beta1.projects.locations.clusters ](#rest-resource:-v1beta1.projects.locations.clusters)
- [ REST Resource: v1beta1.projects.locations.clusters.nodePools ](#rest-resource:-v1beta1.projects.locations.clusters.nodepools)
- [ REST Resource: v1beta1.projects.locations.operations ](#rest-resource:-v1beta1.projects.locations.operations)
- [ REST Resource: v1beta1.projects.zones ](#rest-resource:-v1beta1.projects.zones)
- [ REST Resource: v1beta1.projects.zones.clusters ](#rest-resource:-v1beta1.projects.zones.clusters)
- [ REST Resource: v1beta1.projects.zones.clusters.nodePools ](#rest-resource:-v1beta1.projects.zones.clusters.nodepools)
- [ REST Resource: v1beta1.projects.zones.operations ](#rest-resource:-v1beta1.projects.zones.operations)
- [ REST Resource: v1.projects.aggregated.usableSubnetworks ](#rest-resource:-v1.projects.aggregated.usablesubnetworks)
- [ REST Resource: v1.projects.locations ](#rest-resource:-v1.projects.locations)
- [ REST Resource: v1.projects.locations.clusters ](#rest-resource:-v1.projects.locations.clusters)
- [ REST Resource: v1.projects.locations.clusters.nodePools ](#rest-resource:-v1.projects.locations.clusters.nodepools)
- [ REST Resource: v1.projects.locations.operations ](#rest-resource:-v1.projects.locations.operations)
- [ REST Resource: v1.projects.zones ](#rest-resource:-v1.projects.zones)
- [ REST Resource: v1.projects.zones.clusters ](#rest-resource:-v1.projects.zones.clusters)
- [ REST Resource: v1.projects.zones.clusters.nodePools ](#rest-resource:-v1.projects.zones.clusters.nodepools)
- [ REST Resource: v1.projects.zones.operations ](#rest-resource:-v1.projects.zones.operations)
- 













Builds and manages container-based applications, powered by the open source Kubernetes technology.




- [REST Resource: v1beta1.projects.aggregated.usableSubnetworks](#v1beta1.projects.aggregated.usableSubnetworks)

- [REST Resource: v1beta1.projects.locations](#v1beta1.projects.locations)

- [REST Resource: v1beta1.projects.locations.clusters](#v1beta1.projects.locations.clusters)

- [REST Resource: v1beta1.projects.locations.clusters.nodePools](#v1beta1.projects.locations.clusters.nodePools)

- [REST Resource: v1beta1.projects.locations.operations](#v1beta1.projects.locations.operations)

- [REST Resource: v1beta1.projects.zones](#v1beta1.projects.zones)

- [REST Resource: v1beta1.projects.zones.clusters](#v1beta1.projects.zones.clusters)

- [REST Resource: v1beta1.projects.zones.clusters.nodePools](#v1beta1.projects.zones.clusters.nodePools)

- [REST Resource: v1beta1.projects.zones.operations](#v1beta1.projects.zones.operations)

- [REST Resource: v1.projects.aggregated.usableSubnetworks](#v1.projects.aggregated.usableSubnetworks)

- [REST Resource: v1.projects.locations](#v1.projects.locations)

- [REST Resource: v1.projects.locations.clusters](#v1.projects.locations.clusters)

- [REST Resource: v1.projects.locations.clusters.nodePools](#v1.projects.locations.clusters.nodePools)

- [REST Resource: v1.projects.locations.operations](#v1.projects.locations.operations)

- [REST Resource: v1.projects.zones](#v1.projects.zones)

- [REST Resource: v1.projects.zones.clusters](#v1.projects.zones.clusters)

- [REST Resource: v1.projects.zones.clusters.nodePools](#v1.projects.zones.clusters.nodePools)

- [REST Resource: v1.projects.zones.operations](#v1.projects.zones.operations)





## Service: container. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://apis-berlin-build0.goog/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:




- [https://container.apis-berlin-build0.goog/$discovery/rest?version=v1](https://container.apis-berlin-build0.goog/$discovery/rest?version=v1)

- [https://container.apis-berlin-build0.goog/$discovery/rest?version=v1beta1](https://container.apis-berlin-build0.goog/$discovery/rest?version=v1beta1)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://container.apis-berlin-build0.goog`






## REST Resource: [v1beta1. projects. aggregated. usable Subnetworks](/kubernetes-engine/docs/reference/rest/v1beta1/projects.aggregated.usableSubnetworks)









| 
Methods | 
|



| 

`[list](/kubernetes-engine/docs/reference/rest/v1beta1/projects.aggregated.usableSubnetworks/list)` | 

`GET / v1beta1/ {parent=projects/ *}/ aggregated/ usable Subnetworks` 

Zonal clusters are not supported.
Lists subnetworks that can be used for creating clusters in a project. | 
|






## REST Resource: [v1beta1. projects. locations](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations)









| 
Methods | 
|



| 

`[getServerConfig](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations/getServerConfig)` | 

`GET /v1beta1/{name=projects/*/locations/*}/serverConfig` 

Zonal clusters are not supported.
Returns configuration info about the Google Cloud Dedicated Kubernetes Engine service. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations/list)` | 

`GET /v1beta1/{parent=projects/*}/locations` 

Zonal clusters are not supported.
Fetches locations that offer Google Cloud Dedicated Kubernetes Engine. | 
|






## REST Resource: [v1beta1.projects.locations.clusters](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters)









| 
Methods | 
|



| 

`[checkAutopilotCompatibility](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/checkAutopilotCompatibility)` | 

`GET /v1beta1/{name=projects/*/locations/*/clusters/*}:checkAutopilotCompatibility` 

Zonal clusters are not supported.
Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues. | 
|

| 

`[completeIpRotation](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/completeIpRotation)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:completeIpRotation` 

Zonal clusters are not supported.
Completes master IP rotation. | 
|

| 

`[create](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/create)` | 

`POST /v1beta1/{parent=projects/*/locations/*}/clusters` 

Zonal clusters are not supported.
Creates a cluster, consisting of the specified number and type of Google Cloud Dedicated Compute Engine instances. | 
|

| 

`[delete](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/delete)` | 

`DELETE /v1beta1/{name=projects/*/locations/*/clusters/*}` 

Zonal clusters are not supported.
Deletes the cluster, including the Kubernetes endpoint and all worker nodes. | 
|

| 

`[fetchClusterUpgradeInfo](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/fetchClusterUpgradeInfo)` | 

`GET /v1beta1/{name=projects/*/locations/*/clusters/*}:fetchClusterUpgradeInfo` 

Zonal clusters are not supported.
Fetch upgrade information of a specific cluster. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/get)` | 

`GET /v1beta1/{name=projects/*/locations/*/clusters/*}` 

Zonal clusters are not supported.
Gets the details for a specific cluster. | 
|

| 

`[getJwks](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/getJwks)` | 

`GET /v1beta1/{parent=projects/*/locations/*/clusters/*}/jwks` 

Zonal clusters are not supported.
Gets the public component of the cluster signing keys in JSON Web Key format. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/list)` | 

`GET /v1beta1/{parent=projects/*/locations/*}/clusters` 

Zonal clusters are not supported.
Lists all clusters owned by a project in either the specified zone or all zones. | 
|

| 

`[setAddons](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setAddons)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setAddons` 

Zonal clusters are not supported.
Sets the addons for a specific cluster. | 
|

| 

`[setLegacyAbac](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setLegacyAbac)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setLegacyAbac` 

Zonal clusters are not supported.
Enables or disables the ABAC authorization mechanism on a cluster. | 
|

| 

`[setLocations](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setLocations) 
(deprecated)**` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setLocations` 

Zonal clusters are not supported.
Sets the locations for a specific cluster. | 
|

| 

`[setLogging](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setLogging)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setLogging` 

Zonal clusters are not supported.
Sets the logging service for a specific cluster. | 
|

| 

`[setMaintenancePolicy](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setMaintenancePolicy)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setMaintenancePolicy` 

Zonal clusters are not supported.
Sets the maintenance policy for a cluster. | 
|

| 

`[setMasterAuth](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setMasterAuth)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setMasterAuth` 

Zonal clusters are not supported.
Sets master auth materials. | 
|

| 

`[setMonitoring](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setMonitoring)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setMonitoring` 

Zonal clusters are not supported.
Sets the monitoring service for a specific cluster. | 
|

| 

`[setNetworkPolicy](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setNetworkPolicy)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setNetworkPolicy` 

Zonal clusters are not supported.
Enables or disables Network Policy for a cluster. | 
|

| 

`[setResourceLabels](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/setResourceLabels)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:setResourceLabels` 

Zonal clusters are not supported.
Sets labels on a cluster. | 
|

| 

`[startIpRotation](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/startIpRotation)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:startIpRotation` 

Zonal clusters are not supported.
Starts master IP rotation. | 
|

| 

`[update](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/update)` | 

`PUT /v1beta1/{name=projects/*/locations/*/clusters/*}` 

Zonal clusters are not supported.
Updates the settings for a specific cluster. | 
|

| 

`[updateMaster](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/updateMaster)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*}:updateMaster` 

Zonal clusters are not supported.
Updates the master for a specific cluster. | 
|

| 

`[completeControlPlaneUpgrade](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/completeControlPlaneUpgrade)` | 

The method `google.container.v1beta1.ClusterManager.CompleteControlPlaneUpgrade` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1beta1.projects.locations.clusters.nodePools](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools)









| 
Methods | 
|



| 

`[completeUpgrade](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/completeUpgrade)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}:completeUpgrade` 

Zonal clusters are not supported.
CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete. | 
|

| 

`[create](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/create)` | 

`POST /v1beta1/{parent=projects/*/locations/*/clusters/*}/nodePools` 

Zonal clusters are not supported.
Creates a node pool for a cluster. | 
|

| 

`[delete](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/delete)` | 

`DELETE /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}` 

Zonal clusters are not supported.
Deletes a node pool from a cluster. | 
|

| 

`[fetchNodePoolUpgradeInfo](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/fetchNodePoolUpgradeInfo)` | 

`GET /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}:fetchNodePoolUpgradeInfo` 

Zonal clusters are not supported.
Fetch upgrade information of a specific node pool. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/get)` | 

`GET /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}` 

Zonal clusters are not supported.
Retrieves the requested node pool. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/list)` | 

`GET /v1beta1/{parent=projects/*/locations/*/clusters/*}/nodePools` 

Zonal clusters are not supported.
Lists the node pools for a cluster. | 
|

| 

`[rollback](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/rollback)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}:rollback` 

Zonal clusters are not supported.
Rolls back a previously Aborted or Failed NodePool upgrade. | 
|

| 

`[setAutoscaling](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/setAutoscaling)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setAutoscaling` 

Zonal clusters are not supported.
Sets the autoscaling settings of a specific node pool. | 
|

| 

`[setManagement](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/setManagement)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setManagement` 

Zonal clusters are not supported.
Sets the NodeManagement options for a node pool. | 
|

| 

`[setSize](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/setSize)` | 

`POST /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setSize` 

Zonal clusters are not supported.
SetNodePoolSizeRequest sets the size of a node pool. | 
|

| 

`[update](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools/update)` | 

`PUT /v1beta1/{name=projects/*/locations/*/clusters/*/nodePools/*}` 

Zonal clusters are not supported.
Updates the version and/or image type of a specific node pool. | 
|






## REST Resource: [v1beta1.projects.locations.operations](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.operations)









| 
Methods | 
|



| 

`[cancel](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.operations/cancel)` | 

`POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel` 

Zonal clusters are not supported.
Cancels the specified operation. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.operations/get)` | 

`GET /v1beta1/{name=projects/*/locations/*/operations/*}` 

Zonal clusters are not supported.
Gets the specified operation. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.operations/list)` | 

`GET /v1beta1/{parent=projects/*/locations/*}/operations` 

Zonal clusters are not supported.
Lists all operations in a project in the specified zone or all zones. | 
|






## REST Resource: [v1beta1.projects.zones](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones)









| 
Methods | 
|



| 

`[getServerconfig](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones/getServerconfig)` | 

`GET /v1beta1/projects/{projectId}/zones/{zone}/serverconfig` 

Zonal clusters are not supported.
Returns configuration info about the Google Cloud Dedicated Kubernetes Engine service. | 
|






## REST Resource: [v1beta1.projects.zones.clusters](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters)









| 
Methods | 
|



| 

`[addons](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/addons)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/addons` 

Zonal clusters are not supported.
Sets the addons for a specific cluster. | 
|

| 

`[completeIpRotation](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/completeIpRotation)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:completeIpRotation` 

Zonal clusters are not supported.
Completes master IP rotation. | 
|

| 

`[create](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/create)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters` 

Zonal clusters are not supported.
Creates a cluster, consisting of the specified number and type of Google Cloud Dedicated Compute Engine instances. | 
|

| 

`[delete](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/delete)` | 

`DELETE /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}` 

Zonal clusters are not supported.
Deletes the cluster, including the Kubernetes endpoint and all worker nodes. | 
|

| 

`[fetchClusterUpgradeInfo](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/fetchClusterUpgradeInfo)` | 

`GET /v1beta1/{name=projects/*/zones/*/clusters/*}:fetchClusterUpgradeInfo` 

Zonal clusters are not supported.
Fetch upgrade information of a specific cluster. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/get)` | 

`GET /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}` 

Zonal clusters are not supported.
Gets the details for a specific cluster. | 
|

| 

`[legacyAbac](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/legacyAbac)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/legacyAbac` 

Zonal clusters are not supported.
Enables or disables the ABAC authorization mechanism on a cluster. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/list)` | 

`GET /v1beta1/projects/{projectId}/zones/{zone}/clusters` 

Zonal clusters are not supported.
Lists all clusters owned by a project in either the specified zone or all zones. | 
|

| 

`[locations](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/locations) 
**(deprecated)**` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/locations` 

Zonal clusters are not supported.
Sets the locations for a specific cluster. | 
|

| 

`[logging](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/logging)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/logging` 

Zonal clusters are not supported.
Sets the logging service for a specific cluster. | 
|

| 

`[master](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/master)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/master` 

Zonal clusters are not supported.
Updates the master for a specific cluster. | 
|

| 

`[monitoring](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/monitoring)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring` 

Zonal clusters are not supported.
Sets the monitoring service for a specific cluster. | 
|

| 

`[resourceLabels](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/resourceLabels)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/resourceLabels` 

Zonal clusters are not supported.
Sets labels on a cluster. | 
|

| 

`[setMaintenancePolicy](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/setMaintenancePolicy)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:setMaintenancePolicy` 

Zonal clusters are not supported.
Sets the maintenance policy for a cluster. | 
|

| 

`[setMasterAuth](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/setMasterAuth)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:setMasterAuth` 

Zonal clusters are not supported.
Sets master auth materials. | 
|

| 

`[setNetworkPolicy](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/setNetworkPolicy)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:setNetworkPolicy` 

Zonal clusters are not supported.
Enables or disables Network Policy for a cluster. | 
|

| 

`[startIpRotation](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/startIpRotation)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:startIpRotation` 

Zonal clusters are not supported.
Starts master IP rotation. | 
|

| 

`[update](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/update)` | 

`PUT /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}` 

Zonal clusters are not supported.
Updates the settings for a specific cluster. | 
|

| 

`[completeControlPlaneUpgrade](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters/completeControlPlaneUpgrade)` | 

The method `google.container.v1beta1.ClusterManager.CompleteControlPlaneUpgrade` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1beta1.projects.zones.clusters.nodePools](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools)









| 
Methods | 
|



| 

`[autoscaling](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/autoscaling)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling` 

Zonal clusters are not supported.
Sets the autoscaling settings of a specific node pool. | 
|

| 

`[create](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/create)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools` 

Zonal clusters are not supported.
Creates a node pool for a cluster. | 
|

| 

`[delete](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/delete)` | 

`DELETE /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}` 

Zonal clusters are not supported.
Deletes a node pool from a cluster. | 
|

| 

`[fetchNodePoolUpgradeInfo](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/fetchNodePoolUpgradeInfo)` | 

`GET /v1beta1/{name=projects/*/zones/*/clusters/*/nodePools/*}:fetchNodePoolUpgradeInfo` 

Zonal clusters are not supported.
Fetch upgrade information of a specific node pool. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/get)` | 

`GET /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}` 

Zonal clusters are not supported.
Retrieves the requested node pool. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/list)` | 

`GET /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools` 

Zonal clusters are not supported.
Lists the node pools for a cluster. | 
|

| 

`[rollback](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/rollback)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}:rollback` 

Zonal clusters are not supported.
Rolls back a previously Aborted or Failed NodePool upgrade. | 
|

| 

`[setManagement](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/setManagement)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement` 

Zonal clusters are not supported.
Sets the NodeManagement options for a node pool. | 
|

| 

`[setSize](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/setSize)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setSize` 

Zonal clusters are not supported.
SetNodePoolSizeRequest sets the size of a node pool. | 
|

| 

`[update](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.clusters.nodePools/update)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/update` 

Zonal clusters are not supported.
Updates the version and/or image type of a specific node pool. | 
|






## REST Resource: [v1beta1.projects.zones.operations](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.operations)









| 
Methods | 
|



| 

`[cancel](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.operations/cancel)` | 

`POST /v1beta1/projects/{projectId}/zones/{zone}/operations/{operationId}:cancel` 

Zonal clusters are not supported.
Cancels the specified operation. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.operations/get)` | 

`GET /v1beta1/projects/{projectId}/zones/{zone}/operations/{operationId}` 

Zonal clusters are not supported.
Gets the specified operation. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1beta1/projects.zones.operations/list)` | 

`GET /v1beta1/projects/{projectId}/zones/{zone}/operations` 

Zonal clusters are not supported.
Lists all operations in a project in the specified zone or all zones. | 
|






## REST Resource: [v1.projects.aggregated.usableSubnetworks](/kubernetes-engine/docs/reference/rest/v1/projects.aggregated.usableSubnetworks)









| 
Methods | 
|



| 

`[list](/kubernetes-engine/docs/reference/rest/v1/projects.aggregated.usableSubnetworks/list)` | 

`GET /v1/{parent=projects/*}/aggregated/usableSubnetworks` 

Zonal clusters are not supported.
Lists subnetworks that are usable for creating clusters in a project. | 
|






## REST Resource: [v1.projects.locations](/kubernetes-engine/docs/reference/rest/v1/projects.locations)









| 
Methods | 
|



| 

`[getServerConfig](/kubernetes-engine/docs/reference/rest/v1/projects.locations/getServerConfig)` | 

`GET /v1/{name=projects/*/locations/*}/serverConfig` 

Zonal clusters are not supported.
Returns configuration info about the Google Cloud Dedicated Kubernetes Engine service. | 
|






## REST Resource: [v1.projects.locations.clusters](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters)









| 
Methods | 
|



| 

`[checkAutopilotCompatibility](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/checkAutopilotCompatibility)` | 

`GET /v1/{name=projects/*/locations/*/clusters/*}:checkAutopilotCompatibility` 

Zonal clusters are not supported.
Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues. | 
|

| 

`[completeIpRotation](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/completeIpRotation)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:completeIpRotation` 

Zonal clusters are not supported.
Completes master IP rotation. | 
|

| 

`[create](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/create)` | 

`POST /v1/{parent=projects/*/locations/*}/clusters` 

Zonal clusters are not supported.
Creates a cluster, consisting of the specified number and type of Google Cloud Dedicated Compute Engine instances. | 
|

| 

`[delete](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/clusters/*}` 

Zonal clusters are not supported.
Deletes the cluster, including the Kubernetes endpoint and all worker nodes. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/get)` | 

`GET /v1/{name=projects/*/locations/*/clusters/*}` 

Zonal clusters are not supported.
Gets the details of a specific cluster. | 
|

| 

`[getJwks](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/getJwks)` | 

`GET /v1/{parent=projects/*/locations/*/clusters/*}/jwks` 

Zonal clusters are not supported.
Gets the public component of the cluster signing keys in JSON Web Key format. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/list)` | 

`GET /v1/{parent=projects/*/locations/*}/clusters` 

Zonal clusters are not supported.
Lists all clusters owned by a project in either the specified zone or all zones. | 
|

| 

`[setAddons](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setAddons)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setAddons` 

Zonal clusters are not supported.
Sets the addons for a specific cluster. | 
|

| 

`[setLegacyAbac](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setLegacyAbac)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setLegacyAbac` 

Zonal clusters are not supported.
Enables or disables the ABAC authorization mechanism on a cluster. | 
|

| 

`[setLocations](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setLocations) 
**(deprecated)**` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setLocations` 

Zonal clusters are not supported.
Sets the locations for a specific cluster. | 
|

| 

`[setLogging](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setLogging)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setLogging` 

Zonal clusters are not supported.
Sets the logging service for a specific cluster. | 
|

| 

`[setMaintenancePolicy](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setMaintenancePolicy)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setMaintenancePolicy` 

Zonal clusters are not supported.
Sets the maintenance policy for a cluster. | 
|

| 

`[setMasterAuth](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setMasterAuth)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setMasterAuth` 

Zonal clusters are not supported.
Sets master auth materials. | 
|

| 

`[setMonitoring](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setMonitoring)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setMonitoring` 

Zonal clusters are not supported.
Sets the monitoring service for a specific cluster. | 
|

| 

`[setNetworkPolicy](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setNetworkPolicy)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setNetworkPolicy` 

Zonal clusters are not supported.
Enables or disables Network Policy for a cluster. | 
|

| 

`[setResourceLabels](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/setResourceLabels)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:setResourceLabels` 

Zonal clusters are not supported.
Sets labels on a cluster. | 
|

| 

`[startIpRotation](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/startIpRotation)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:startIpRotation` 

Zonal clusters are not supported.
Starts master IP rotation. | 
|

| 

`[update](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update)` | 

`PUT /v1/{name=projects/*/locations/*/clusters/*}` 

Zonal clusters are not supported.
Updates the settings of a specific cluster. | 
|

| 

`[updateMaster](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/updateMaster)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*}:updateMaster` 

Zonal clusters are not supported.
Updates the master for a specific cluster. | 
|

| 

`[fetchClusterUpgradeInfo](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/fetchClusterUpgradeInfo)` | 

The method `google.container.v1.ClusterManager.FetchClusterUpgradeInfo` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.clusters.nodePools](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools)









| 
Methods | 
|



| 

`[completeUpgrade](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/completeUpgrade)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:completeUpgrade` 

Zonal clusters are not supported.
CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete. | 
|

| 

`[create](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/create)` | 

`POST /v1/{parent=projects/*/locations/*/clusters/*}/nodePools` 

Zonal clusters are not supported.
Creates a node pool for a cluster. | 
|

| 

`[delete](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/delete)` | 

`DELETE /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}` 

Zonal clusters are not supported.
Deletes a node pool from a cluster. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/get)` | 

`GET /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}` 

Zonal clusters are not supported.
Retrieves the requested node pool. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/list)` | 

`GET /v1/{parent=projects/*/locations/*/clusters/*}/nodePools` 

Zonal clusters are not supported.
Lists the node pools for a cluster. | 
|

| 

`[rollback](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/rollback)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:rollback` 

Zonal clusters are not supported.
Rolls back a previously Aborted or Failed NodePool upgrade. | 
|

| 

`[setAutoscaling](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/setAutoscaling)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setAutoscaling` 

Zonal clusters are not supported.
Sets the autoscaling settings for the specified node pool. | 
|

| 

`[setManagement](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/setManagement)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setManagement` 

Zonal clusters are not supported.
Sets the NodeManagement options for a node pool. | 
|

| 

`[setSize](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/setSize)` | 

`POST /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:setSize` 

Zonal clusters are not supported.
Sets the size for a specific node pool. | 
|

| 

`[update](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/update)` | 

`PUT /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}` 

Zonal clusters are not supported.
Updates the version and/or image type for the specified node pool. | 
|

| 

`[fetchNodePoolUpgradeInfo](/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/fetchNodePoolUpgradeInfo)` | 

The method `google.container.v1.ClusterManager.FetchNodePoolUpgradeInfo` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.locations.operations](/kubernetes-engine/docs/reference/rest/v1/projects.locations.operations)









| 
Methods | 
|



| 

`[cancel](/kubernetes-engine/docs/reference/rest/v1/projects.locations.operations/cancel)` | 

`POST /v1/{name=projects/*/locations/*/operations/*}:cancel` 

Zonal clusters are not supported.
Cancels the specified operation. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1/projects.locations.operations/get)` | 

`GET /v1/{name=projects/*/locations/*/operations/*}` 

Zonal clusters are not supported.
Gets the specified operation. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1/projects.locations.operations/list)` | 

`GET /v1/{parent=projects/*/locations/*}/operations` 

Zonal clusters are not supported.
Lists all operations in a project in a specific zone or all zones. | 
|






## REST Resource: [v1.projects.zones](/kubernetes-engine/docs/reference/rest/v1/projects.zones)









| 
Methods | 
|



| 

`[getServerconfig](/kubernetes-engine/docs/reference/rest/v1/projects.zones/getServerconfig)` | 

`GET /v1/projects/{projectId}/zones/{zone}/serverconfig` 

Zonal clusters are not supported.
Returns configuration info about the Google Cloud Dedicated Kubernetes Engine service. | 
|






## REST Resource: [v1.projects.zones.clusters](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters)









| 
Methods | 
|



| 

`[addons](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/addons)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/addons` 

Zonal clusters are not supported.
Sets the addons for a specific cluster. | 
|

| 

`[completeIpRotation](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/completeIpRotation)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:completeIpRotation` 

Zonal clusters are not supported.
Completes master IP rotation. | 
|

| 

`[create](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/create)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters` 

Zonal clusters are not supported.
Creates a cluster, consisting of the specified number and type of Google Cloud Dedicated Compute Engine instances. | 
|

| 

`[delete](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/delete)` | 

`DELETE /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}` 

Zonal clusters are not supported.
Deletes the cluster, including the Kubernetes endpoint and all worker nodes. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/get)` | 

`GET /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}` 

Zonal clusters are not supported.
Gets the details of a specific cluster. | 
|

| 

`[legacyAbac](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/legacyAbac)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/legacyAbac` 

Zonal clusters are not supported.
Enables or disables the ABAC authorization mechanism on a cluster. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/list)` | 

`GET /v1/projects/{projectId}/zones/{zone}/clusters` 

Zonal clusters are not supported.
Lists all clusters owned by a project in either the specified zone or all zones. | 
|

| 

`[locations](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/locations) 
**(deprecated)**` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/locations` 

Zonal clusters are not supported.
Sets the locations for a specific cluster. | 
|

| 

`[logging](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/logging)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/logging` 

Zonal clusters are not supported.
Sets the logging service for a specific cluster. | 
|

| 

`[master](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/master)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/master` 

Zonal clusters are not supported.
Updates the master for a specific cluster. | 
|

| 

`[monitoring](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/monitoring)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring` 

Zonal clusters are not supported.
Sets the monitoring service for a specific cluster. | 
|

| 

`[resourceLabels](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/resourceLabels)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/resourceLabels` 

Zonal clusters are not supported.
Sets labels on a cluster. | 
|

| 

`[setMaintenancePolicy](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/setMaintenancePolicy)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:setMaintenancePolicy` 

Zonal clusters are not supported.
Sets the maintenance policy for a cluster. | 
|

| 

`[setMasterAuth](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/setMasterAuth)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:setMasterAuth` 

Zonal clusters are not supported.
Sets master auth materials. | 
|

| 

`[setNetworkPolicy](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/setNetworkPolicy)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:setNetworkPolicy` 

Zonal clusters are not supported.
Enables or disables Network Policy for a cluster. | 
|

| 

`[startIpRotation](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/startIpRotation)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:startIpRotation` 

Zonal clusters are not supported.
Starts master IP rotation. | 
|

| 

`[update](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/update)` | 

`PUT /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}` 

Zonal clusters are not supported.
Updates the settings of a specific cluster. | 
|

| 

`[fetchClusterUpgradeInfo](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/fetchClusterUpgradeInfo)` | 

The method `google.container.v1.ClusterManager.FetchClusterUpgradeInfo` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.zones.clusters.nodePools](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools)









| 
Methods | 
|



| 

`[autoscaling](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/autoscaling)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling` 

Zonal clusters are not supported.
Sets the autoscaling settings for the specified node pool. | 
|

| 

`[create](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/create)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools` 

Zonal clusters are not supported.
Creates a node pool for a cluster. | 
|

| 

`[delete](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/delete)` | 

`DELETE /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}` 

Zonal clusters are not supported.
Deletes a node pool from a cluster. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/get)` | 

`GET /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}` 

Zonal clusters are not supported.
Retrieves the requested node pool. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/list)` | 

`GET /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools` 

Zonal clusters are not supported.
Lists the node pools for a cluster. | 
|

| 

`[rollback](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/rollback)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}:rollback` 

Zonal clusters are not supported.
Rolls back a previously Aborted or Failed NodePool upgrade. | 
|

| 

`[setManagement](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/setManagement)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement` 

Zonal clusters are not supported.
Sets the NodeManagement options for a node pool. | 
|

| 

`[setSize](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/setSize)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setSize` 

Zonal clusters are not supported.
Sets the size for a specific node pool. | 
|

| 

`[update](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/update)` | 

`POST /v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/update` 

Zonal clusters are not supported.
Updates the version and/or image type for the specified node pool. | 
|

| 

`[fetchNodePoolUpgradeInfo](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/fetchNodePoolUpgradeInfo)` | 

The method `google.container.v1.ClusterManager.FetchNodePoolUpgradeInfo` is not available in Google Cloud Dedicated in Germany. | 
|






## REST Resource: [v1.projects.zones.operations](/kubernetes-engine/docs/reference/rest/v1/projects.zones.operations)









| 
Methods | 
|



| 

`[cancel](/kubernetes-engine/docs/reference/rest/v1/projects.zones.operations/cancel)` | 

`POST /v1/projects/{projectId}/zones/{zone}/operations/{operationId}:cancel` 

Zonal clusters are not supported.
Cancels the specified operation. | 
|

| 

`[get](/kubernetes-engine/docs/reference/rest/v1/projects.zones.operations/get)` | 

`GET /v1/projects/{projectId}/zones/{zone}/operations/{operationId}` 

Zonal clusters are not supported.
Gets the specified operation. | 
|

| 

`[list](/kubernetes-engine/docs/reference/rest/v1/projects.zones.operations/list)` | 

`GET /v1/projects/{projectId}/zones/{zone}/operations` 

Zonal clusters are not supported.
Lists all operations in a project in a specific zone or all zones. | 
|