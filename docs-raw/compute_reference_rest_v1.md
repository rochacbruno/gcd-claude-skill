# Compute Engine API

Source: https://berlin.devsitetest.how/compute/docs/reference/rest/v1
Last updated: 2025-04-24

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/compute/docs/tpc-differences) for more details.














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

Compute

](https://berlin.devsitetest.how/docs/compute-area)






- 








[

Compute Engine

](https://berlin.devsitetest.how/compute/docs)






- 








[

APIs & Reference

](https://berlin.devsitetest.how/compute/docs/apis)












# Compute Engine API 






- On this page ** 
- [ Service: compute.googleapis.com ](#service:-compute.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)

- [ REST Resource: v1.acceleratorTypes ](#rest-resource:-v1.acceleratortypes)
- [ REST Resource: v1.addresses ](#rest-resource:-v1.addresses)
- [ REST Resource: v1.autoscalers ](#rest-resource:-v1.autoscalers)
- [ REST Resource: v1.backendBuckets ](#rest-resource:-v1.backendbuckets)
- [ REST Resource: v1.backendServices ](#rest-resource:-v1.backendservices)
- [ REST Resource: v1.diskTypes ](#rest-resource:-v1.disktypes)
- [ REST Resource: v1.disks ](#rest-resource:-v1.disks)
- [ REST Resource: v1.externalVpnGateways ](#rest-resource:-v1.externalvpngateways)
- [ REST Resource: v1.firewallPolicies ](#rest-resource:-v1.firewallpolicies)
- [ REST Resource: v1.firewalls ](#rest-resource:-v1.firewalls)
- [ REST Resource: v1.forwardingRules ](#rest-resource:-v1.forwardingrules)
- [ REST Resource: v1.globalAddresses ](#rest-resource:-v1.globaladdresses)
- [ REST Resource: v1.globalForwardingRules ](#rest-resource:-v1.globalforwardingrules)
- [ REST Resource: v1.globalNetworkEndpointGroups ](#rest-resource:-v1.globalnetworkendpointgroups)
- [ REST Resource: v1.globalOperations ](#rest-resource:-v1.globaloperations)
- [ REST Resource: v1.globalOrganizationOperations ](#rest-resource:-v1.globalorganizationoperations)
- [ REST Resource: v1.globalPublicDelegatedPrefixes ](#rest-resource:-v1.globalpublicdelegatedprefixes)
- [ REST Resource: v1.healthChecks ](#rest-resource:-v1.healthchecks)
- [ REST Resource: v1.httpHealthChecks ](#rest-resource:-v1.httphealthchecks)
- [ REST Resource: v1.httpsHealthChecks ](#rest-resource:-v1.httpshealthchecks)
- [ REST Resource: v1.imageFamilyViews ](#rest-resource:-v1.imagefamilyviews)
- [ REST Resource: v1.images ](#rest-resource:-v1.images)
- [ REST Resource: v1.instanceGroupManagerResizeRequests ](#rest-resource:-v1.instancegroupmanagerresizerequests)
- [ REST Resource: v1.instanceGroupManagers ](#rest-resource:-v1.instancegroupmanagers)
- [ REST Resource: v1.instanceGroups ](#rest-resource:-v1.instancegroups)
- [ REST Resource: v1.instanceSettings ](#rest-resource:-v1.instancesettings)
- [ REST Resource: v1.instanceTemplates ](#rest-resource:-v1.instancetemplates)
- [ REST Resource: v1.instances ](#rest-resource:-v1.instances)
- [ REST Resource: v1.instantSnapshots ](#rest-resource:-v1.instantsnapshots)
- [ REST Resource: v1.interconnectAttachments ](#rest-resource:-v1.interconnectattachments)
- [ REST Resource: v1.interconnectLocations ](#rest-resource:-v1.interconnectlocations)
- [ REST Resource: v1.interconnectRemoteLocations ](#rest-resource:-v1.interconnectremotelocations)
- [ REST Resource: v1.interconnects ](#rest-resource:-v1.interconnects)
- [ REST Resource: v1.licenseCodes ](#rest-resource:-v1.licensecodes)
- [ REST Resource: v1.licenses ](#rest-resource:-v1.licenses)
- [ REST Resource: v1.machineImages ](#rest-resource:-v1.machineimages)
- [ REST Resource: v1.machineTypes ](#rest-resource:-v1.machinetypes)
- [ REST Resource: v1.networkAttachments ](#rest-resource:-v1.networkattachments)
- [ REST Resource: v1.networkEdgeSecurityServices ](#rest-resource:-v1.networkedgesecurityservices)
- [ REST Resource: v1.networkEndpointGroups ](#rest-resource:-v1.networkendpointgroups)
- [ REST Resource: v1.networkFirewallPolicies ](#rest-resource:-v1.networkfirewallpolicies)
- [ REST Resource: v1.networkProfiles ](#rest-resource:-v1.networkprofiles)
- [ REST Resource: v1.networks ](#rest-resource:-v1.networks)
- [ REST Resource: v1.nodeGroups ](#rest-resource:-v1.nodegroups)
- [ REST Resource: v1.nodeTemplates ](#rest-resource:-v1.nodetemplates)
- [ REST Resource: v1.nodeTypes ](#rest-resource:-v1.nodetypes)
- [ REST Resource: v1.packetMirrorings ](#rest-resource:-v1.packetmirrorings)
- [ REST Resource: v1.projects ](#rest-resource:-v1.projects)
- [ REST Resource: v1.publicAdvertisedPrefixes ](#rest-resource:-v1.publicadvertisedprefixes)
- [ REST Resource: v1.publicDelegatedPrefixes ](#rest-resource:-v1.publicdelegatedprefixes)
- [ REST Resource: v1.regionAutoscalers ](#rest-resource:-v1.regionautoscalers)
- [ REST Resource: v1.regionBackendServices ](#rest-resource:-v1.regionbackendservices)
- [ REST Resource: v1.regionCommitments ](#rest-resource:-v1.regioncommitments)
- [ REST Resource: v1.regionDiskTypes ](#rest-resource:-v1.regiondisktypes)
- [ REST Resource: v1.regionDisks ](#rest-resource:-v1.regiondisks)
- [ REST Resource: v1.regionHealthCheckServices ](#rest-resource:-v1.regionhealthcheckservices)
- [ REST Resource: v1.regionHealthChecks ](#rest-resource:-v1.regionhealthchecks)
- [ REST Resource: v1.regionInstanceGroupManagers ](#rest-resource:-v1.regioninstancegroupmanagers)
- [ REST Resource: v1.regionInstanceGroups ](#rest-resource:-v1.regioninstancegroups)
- [ REST Resource: v1.regionInstanceTemplates ](#rest-resource:-v1.regioninstancetemplates)
- [ REST Resource: v1.regionInstances ](#rest-resource:-v1.regioninstances)
- [ REST Resource: v1.regionInstantSnapshots ](#rest-resource:-v1.regioninstantsnapshots)
- [ REST Resource: v1.regionNetworkEndpointGroups ](#rest-resource:-v1.regionnetworkendpointgroups)
- [ REST Resource: v1.regionNetworkFirewallPolicies ](#rest-resource:-v1.regionnetworkfirewallpolicies)
- [ REST Resource: v1.regionNotificationEndpoints ](#rest-resource:-v1.regionnotificationendpoints)
- [ REST Resource: v1.regionOperations ](#rest-resource:-v1.regionoperations)
- [ REST Resource: v1.regionSecurityPolicies ](#rest-resource:-v1.regionsecuritypolicies)
- [ REST Resource: v1.regionSslCertificates ](#rest-resource:-v1.regionsslcertificates)
- [ REST Resource: v1.regionSslPolicies ](#rest-resource:-v1.regionsslpolicies)
- [ REST Resource: v1.regionTargetHttpProxies ](#rest-resource:-v1.regiontargethttpproxies)
- [ REST Resource: v1.regionTargetHttpsProxies ](#rest-resource:-v1.regiontargethttpsproxies)
- [ REST Resource: v1.regionTargetTcpProxies ](#rest-resource:-v1.regiontargettcpproxies)
- [ REST Resource: v1.regionUrlMaps ](#rest-resource:-v1.regionurlmaps)
- [ REST Resource: v1.regionZones ](#rest-resource:-v1.regionzones)
- [ REST Resource: v1.regions ](#rest-resource:-v1.regions)
- [ REST Resource: v1.reservations ](#rest-resource:-v1.reservations)
- [ REST Resource: v1.resourcePolicies ](#rest-resource:-v1.resourcepolicies)
- [ REST Resource: v1.routers ](#rest-resource:-v1.routers)
- [ REST Resource: v1.routes ](#rest-resource:-v1.routes)
- [ REST Resource: v1.securityPolicies ](#rest-resource:-v1.securitypolicies)
- [ REST Resource: v1.serviceAttachments ](#rest-resource:-v1.serviceattachments)
- [ REST Resource: v1.snapshotSettings ](#rest-resource:-v1.snapshotsettings)
- [ REST Resource: v1.snapshots ](#rest-resource:-v1.snapshots)
- [ REST Resource: v1.sslCertificates ](#rest-resource:-v1.sslcertificates)
- [ REST Resource: v1.sslPolicies ](#rest-resource:-v1.sslpolicies)
- [ REST Resource: v1.storagePoolTypes ](#rest-resource:-v1.storagepooltypes)
- [ REST Resource: v1.storagePools ](#rest-resource:-v1.storagepools)
- [ REST Resource: v1.subnetworks ](#rest-resource:-v1.subnetworks)
- [ REST Resource: v1.targetGrpcProxies ](#rest-resource:-v1.targetgrpcproxies)
- [ REST Resource: v1.targetHttpProxies ](#rest-resource:-v1.targethttpproxies)
- [ REST Resource: v1.targetHttpsProxies ](#rest-resource:-v1.targethttpsproxies)
- [ REST Resource: v1.targetInstances ](#rest-resource:-v1.targetinstances)
- [ REST Resource: v1.targetPools ](#rest-resource:-v1.targetpools)
- [ REST Resource: v1.targetSslProxies ](#rest-resource:-v1.targetsslproxies)
- [ REST Resource: v1.targetTcpProxies ](#rest-resource:-v1.targettcpproxies)
- [ REST Resource: v1.targetVpnGateways ](#rest-resource:-v1.targetvpngateways)
- [ REST Resource: v1.urlMaps ](#rest-resource:-v1.urlmaps)
- [ REST Resource: v1.vpnGateways ](#rest-resource:-v1.vpngateways)
- [ REST Resource: v1.vpnTunnels ](#rest-resource:-v1.vpntunnels)
- [ REST Resource: v1.zoneOperations ](#rest-resource:-v1.zoneoperations)
- [ REST Resource: v1.zones ](#rest-resource:-v1.zones)
- 













Creates and runs virtual machines on Google Cloud Platform.




- [REST Resource: v1.acceleratorTypes](#v1.acceleratorTypes)

- [REST Resource: v1.addresses](#v1.addresses)

- [REST Resource: v1.autoscalers](#v1.autoscalers)

- [REST Resource: v1.backendBuckets](#v1.backendBuckets)

- [REST Resource: v1.backendServices](#v1.backendServices)

- [REST Resource: v1.diskTypes](#v1.diskTypes)

- [REST Resource: v1.disks](#v1.disks)

- [REST Resource: v1.externalVpnGateways](#v1.externalVpnGateways)

- [REST Resource: v1.firewallPolicies](#v1.firewallPolicies)

- [REST Resource: v1.firewalls](#v1.firewalls)

- [REST Resource: v1.forwardingRules](#v1.forwardingRules)

- [REST Resource: v1.globalAddresses](#v1.globalAddresses)

- [REST Resource: v1.globalForwardingRules](#v1.globalForwardingRules)

- [REST Resource: v1.globalNetworkEndpointGroups](#v1.globalNetworkEndpointGroups)

- [REST Resource: v1.globalOperations](#v1.globalOperations)

- [REST Resource: v1.globalOrganizationOperations](#v1.globalOrganizationOperations)

- [REST Resource: v1.globalPublicDelegatedPrefixes](#v1.globalPublicDelegatedPrefixes)

- [REST Resource: v1.healthChecks](#v1.healthChecks)

- [REST Resource: v1.httpHealthChecks](#v1.httpHealthChecks)

- [REST Resource: v1.httpsHealthChecks](#v1.httpsHealthChecks)

- [REST Resource: v1.imageFamilyViews](#v1.imageFamilyViews)

- [REST Resource: v1.images](#v1.images)

- [REST Resource: v1.instanceGroupManagerResizeRequests](#v1.instanceGroupManagerResizeRequests)

- [REST Resource: v1.instanceGroupManagers](#v1.instanceGroupManagers)

- [REST Resource: v1.instanceGroups](#v1.instanceGroups)

- [REST Resource: v1.instanceSettings](#v1.instanceSettings)

- [REST Resource: v1.instanceTemplates](#v1.instanceTemplates)

- [REST Resource: v1.instances](#v1.instances)

- [REST Resource: v1.instantSnapshots](#v1.instantSnapshots)

- [REST Resource: v1.interconnectAttachments](#v1.interconnectAttachments)

- [REST Resource: v1.interconnectLocations](#v1.interconnectLocations)

- [REST Resource: v1.interconnectRemoteLocations](#v1.interconnectRemoteLocations)

- [REST Resource: v1.interconnects](#v1.interconnects)

- [REST Resource: v1.licenseCodes](#v1.licenseCodes)

- [REST Resource: v1.licenses](#v1.licenses)

- [REST Resource: v1.machineImages](#v1.machineImages)

- [REST Resource: v1.machineTypes](#v1.machineTypes)

- [REST Resource: v1.networkAttachments](#v1.networkAttachments)

- [REST Resource: v1.networkEdgeSecurityServices](#v1.networkEdgeSecurityServices)

- [REST Resource: v1.networkEndpointGroups](#v1.networkEndpointGroups)

- [REST Resource: v1.networkFirewallPolicies](#v1.networkFirewallPolicies)

- [REST Resource: v1.networkProfiles](#v1.networkProfiles)

- [REST Resource: v1.networks](#v1.networks)

- [REST Resource: v1.nodeGroups](#v1.nodeGroups)

- [REST Resource: v1.nodeTemplates](#v1.nodeTemplates)

- [REST Resource: v1.nodeTypes](#v1.nodeTypes)

- [REST Resource: v1.packetMirrorings](#v1.packetMirrorings)

- [REST Resource: v1.projects](#v1.projects)

- [REST Resource: v1.publicAdvertisedPrefixes](#v1.publicAdvertisedPrefixes)

- [REST Resource: v1.publicDelegatedPrefixes](#v1.publicDelegatedPrefixes)

- [REST Resource: v1.regionAutoscalers](#v1.regionAutoscalers)

- [REST Resource: v1.regionBackendServices](#v1.regionBackendServices)

- [REST Resource: v1.regionCommitments](#v1.regionCommitments)

- [REST Resource: v1.regionDiskTypes](#v1.regionDiskTypes)

- [REST Resource: v1.regionDisks](#v1.regionDisks)

- [REST Resource: v1.regionHealthCheckServices](#v1.regionHealthCheckServices)

- [REST Resource: v1.regionHealthChecks](#v1.regionHealthChecks)

- [REST Resource: v1.regionInstanceGroupManagers](#v1.regionInstanceGroupManagers)

- [REST Resource: v1.regionInstanceGroups](#v1.regionInstanceGroups)

- [REST Resource: v1.regionInstanceTemplates](#v1.regionInstanceTemplates)

- [REST Resource: v1.regionInstances](#v1.regionInstances)

- [REST Resource: v1.regionInstantSnapshots](#v1.regionInstantSnapshots)

- [REST Resource: v1.regionNetworkEndpointGroups](#v1.regionNetworkEndpointGroups)

- [REST Resource: v1.regionNetworkFirewallPolicies](#v1.regionNetworkFirewallPolicies)

- [REST Resource: v1.regionNotificationEndpoints](#v1.regionNotificationEndpoints)

- [REST Resource: v1.regionOperations](#v1.regionOperations)

- [REST Resource: v1.regionSecurityPolicies](#v1.regionSecurityPolicies)

- [REST Resource: v1.regionSslCertificates](#v1.regionSslCertificates)

- [REST Resource: v1.regionSslPolicies](#v1.regionSslPolicies)

- [REST Resource: v1.regionTargetHttpProxies](#v1.regionTargetHttpProxies)

- [REST Resource: v1.regionTargetHttpsProxies](#v1.regionTargetHttpsProxies)

- [REST Resource: v1.regionTargetTcpProxies](#v1.regionTargetTcpProxies)

- [REST Resource: v1.regionUrlMaps](#v1.regionUrlMaps)

- [REST Resource: v1.regionZones](#v1.regionZones)

- [REST Resource: v1.regions](#v1.regions)

- [REST Resource: v1.reservations](#v1.reservations)

- [REST Resource: v1.resourcePolicies](#v1.resourcePolicies)

- [REST Resource: v1.routers](#v1.routers)

- [REST Resource: v1.routes](#v1.routes)

- [REST Resource: v1.securityPolicies](#v1.securityPolicies)

- [REST Resource: v1.serviceAttachments](#v1.serviceAttachments)

- [REST Resource: v1.snapshotSettings](#v1.snapshotSettings)

- [REST Resource: v1.snapshots](#v1.snapshots)

- [REST Resource: v1.sslCertificates](#v1.sslCertificates)

- [REST Resource: v1.sslPolicies](#v1.sslPolicies)

- [REST Resource: v1.storagePoolTypes](#v1.storagePoolTypes)

- [REST Resource: v1.storagePools](#v1.storagePools)

- [REST Resource: v1.subnetworks](#v1.subnetworks)

- [REST Resource: v1.targetGrpcProxies](#v1.targetGrpcProxies)

- [REST Resource: v1.targetHttpProxies](#v1.targetHttpProxies)

- [REST Resource: v1.targetHttpsProxies](#v1.targetHttpsProxies)

- [REST Resource: v1.targetInstances](#v1.targetInstances)

- [REST Resource: v1.targetPools](#v1.targetPools)

- [REST Resource: v1.targetSslProxies](#v1.targetSslProxies)

- [REST Resource: v1.targetTcpProxies](#v1.targetTcpProxies)

- [REST Resource: v1.targetVpnGateways](#v1.targetVpnGateways)

- [REST Resource: v1.urlMaps](#v1.urlMaps)

- [REST Resource: v1.vpnGateways](#v1.vpnGateways)

- [REST Resource: v1.vpnTunnels](#v1.vpnTunnels)

- [REST Resource: v1.zoneOperations](#v1.zoneOperations)

- [REST Resource: v1.zones](#v1.zones)





## Service: compute. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://berlin.devsitetest.how/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:




- [https://compute.apis-berlin-build0.goog/$discovery/rest?version=v1](https://compute.apis-berlin-build0.goog/$discovery/rest?version=v1)





### Service endpoint



A [service endpoint](https://berlin.devsitetest.how/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://compute.apis-berlin-build0.goog`






## REST Resource: [v1. accelerator Types](/compute/docs/reference/rest/v1/acceleratorTypes)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/acceleratorTypes/aggregatedList)` | 

The method `compute. v1. Accelerator Types Service. Aggregated List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/acceleratorTypes/get)` | 

The method `compute. v1. Accelerator Types Service. Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/acceleratorTypes/list)` | 

The method `compute. v1. Accelerator Types Service. List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1. addresses](/compute/docs/reference/rest/v1/addresses)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/addresses/aggregatedList)` | 

The method `compute.v1.RegionAddressesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/addresses/delete)` | 

The method `compute.v1.RegionAddressesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/addresses/get)` | 

The method `compute.v1.RegionAddressesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/addresses/insert)` | 

The method `compute.v1.RegionAddressesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/addresses/list)` | 

The method `compute.v1.RegionAddressesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[move](/compute/docs/reference/rest/v1/addresses/move)` | 

The method `compute.v1.RegionAddressesService.Move` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/addresses/setLabels)` | 

The method `compute.v1.RegionAddressesService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.autoscalers](/compute/docs/reference/rest/v1/autoscalers)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/autoscalers/aggregatedList)` | 

The method `compute.v1.AutoscalersService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/autoscalers/delete)` | 

The method `compute.v1.AutoscalersService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/autoscalers/get)` | 

The method `compute.v1.AutoscalersService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/autoscalers/insert)` | 

The method `compute.v1.AutoscalersService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/autoscalers/list)` | 

The method `compute.v1.AutoscalersService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/autoscalers/patch)` | 

The method `compute.v1.AutoscalersService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/autoscalers/update)` | 

The method `compute.v1.AutoscalersService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.backendBuckets](/compute/docs/reference/rest/v1/backendBuckets)









| 
Methods | 
|



| 

`[add Signed Url Key](/compute/docs/reference/rest/v1/backendBuckets/addSignedUrlKey)` | 

The method `compute.v1.BackendBucketsService.AddSignedUrlKey` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/backendBuckets/delete)` | 

The method `compute.v1.BackendBucketsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete Signed Url Key](/compute/docs/reference/rest/v1/backendBuckets/deleteSignedUrlKey)` | 

The method `compute.v1.BackendBucketsService.DeleteSignedUrlKey` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/backendBuckets/get)` | 

The method `compute.v1.BackendBucketsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/backendBuckets/getIamPolicy)` | 

The method `compute.v1.BackendBucketsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/backendBuckets/insert)` | 

The method `compute.v1.BackendBucketsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/backendBuckets/list)` | 

The method `compute.v1.BackendBucketsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/backendBuckets/patch)` | 

The method `compute.v1.BackendBucketsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Edge Security Policy](/compute/docs/reference/rest/v1/backendBuckets/setEdgeSecurityPolicy)` | 

The method `compute.v1.BackendBucketsService.SetEdgeSecurityPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/backendBuckets/setIamPolicy)` | 

The method `compute.v1.BackendBucketsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/backendBuckets/testIamPermissions)` | 

The method `compute.v1.BackendBucketsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/backendBuckets/update)` | 

The method `compute.v1.BackendBucketsService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.backendServices](/compute/docs/reference/rest/v1/backendServices)









| 
Methods | 
|



| 

`[add Signed Url Key](/compute/docs/reference/rest/v1/backendServices/addSignedUrlKey)` | 

The method `compute.v1.BackendServicesService.AddSignedUrlKey` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/backendServices/aggregatedList)` | 

The method `compute.v1.BackendServicesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/backendServices/delete)` | 

The method `compute.v1.BackendServicesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete Signed Url Key](/compute/docs/reference/rest/v1/backendServices/deleteSignedUrlKey)` | 

The method `compute.v1.BackendServicesService.DeleteSignedUrlKey` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/backendServices/get)` | 

The method `compute.v1.BackendServicesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Health](/compute/docs/reference/rest/v1/backendServices/getHealth)` | 

The method `compute.v1.BackendServicesService.GetHealth` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/backendServices/getIamPolicy)` | 

The method `compute.v1.BackendServicesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/backendServices/insert)` | 

The method `compute.v1.BackendServicesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/backendServices/list)` | 

The method `compute.v1.BackendServicesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Usable](/compute/docs/reference/rest/v1/backendServices/listUsable)` | 

The method `compute.v1.BackendServicesService.ListUsable` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/backendServices/patch)` | 

The method `compute.v1.BackendServicesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Edge Security Policy](/compute/docs/reference/rest/v1/backendServices/setEdgeSecurityPolicy)` | 

The method `compute.v1.BackendServicesService.SetEdgeSecurityPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/backendServices/setIamPolicy)` | 

The method `compute.v1.BackendServicesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Security Policy](/compute/docs/reference/rest/v1/backendServices/setSecurityPolicy)` | 

The method `compute.v1.BackendServicesService.SetSecurityPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/backendServices/testIamPermissions)` | 

The method `compute.v1.BackendServicesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/backendServices/update)` | 

The method `compute.v1.BackendServicesService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.diskTypes](/compute/docs/reference/rest/v1/diskTypes)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/diskTypes/aggregatedList)` | 

The method `compute.v1.DiskTypesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/diskTypes/get)` | 

The method `compute.v1.DiskTypesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/diskTypes/list)` | 

The method `compute.v1.DiskTypesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.disks](/compute/docs/reference/rest/v1/disks)









| 
Methods | 
|



| 

`[add Resource Policies](/compute/docs/reference/rest/v1/disks/addResourcePolicies)` | 

The method `compute.v1.DisksService.AddResourcePolicies` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/disks/aggregatedList)` | 

The method `compute.v1.DisksService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[bulk Insert](/compute/docs/reference/rest/v1/disks/bulkInsert)` | 

The method `compute.v1.DisksService.BulkInsert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[create Snapshot](/compute/docs/reference/rest/v1/disks/createSnapshot)` | 

The method `compute.v1.DisksService.CreateSnapshot` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/disks/delete)` | 

The method `compute.v1.DisksService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/disks/get)` | 

The method `compute.v1.DisksService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/disks/getIamPolicy)` | 

The method `compute.v1.DisksService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/disks/insert)` | 

The method `compute.v1.DisksService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/disks/list)` | 

The method `compute.v1.DisksService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Resource Policies](/compute/docs/reference/rest/v1/disks/removeResourcePolicies)` | 

The method `compute.v1.DisksService.RemoveResourcePolicies` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/disks/resize)` | 

The method `compute.v1.DisksService.Resize` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/disks/setIamPolicy)` | 

The method `compute.v1.DisksService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/disks/setLabels)` | 

The method `compute.v1.DisksService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[start Async Replication](/compute/docs/reference/rest/v1/disks/startAsyncReplication)` | 

The method `compute.v1.DisksService.StartAsyncReplication` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[stop Async Replication](/compute/docs/reference/rest/v1/disks/stopAsyncReplication)` | 

The method `compute.v1.DisksService.StopAsyncReplication` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[stop Group Async Replication](/compute/docs/reference/rest/v1/disks/stopGroupAsyncReplication)` | 

The method `compute.v1.DisksService.StopGroupAsyncReplication` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/disks/testIamPermissions)` | 

The method `compute.v1.DisksService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/disks/update)` | 

The method `compute.v1.DisksService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.externalVpnGateways](/compute/docs/reference/rest/v1/externalVpnGateways)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/externalVpnGateways/delete)` | 

The method `compute.v1.ExternalVpnGatewaysService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/externalVpnGateways/get)` | 

The method `compute.v1.ExternalVpnGatewaysService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/externalVpnGateways/insert)` | 

The method `compute.v1.ExternalVpnGatewaysService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/externalVpnGateways/list)` | 

The method `compute.v1.ExternalVpnGatewaysService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/externalVpnGateways/setLabels)` | 

The method `compute.v1.ExternalVpnGatewaysService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/externalVpnGateways/testIamPermissions)` | 

The method `compute.v1.ExternalVpnGatewaysService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.firewallPolicies](/compute/docs/reference/rest/v1/firewallPolicies)









| 
Methods | 
|



| 

`[add Association](/compute/docs/reference/rest/v1/firewallPolicies/addAssociation)` | 

The method `compute.v1.FirewallPoliciesService.AddAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[add Rule](/compute/docs/reference/rest/v1/firewallPolicies/addRule)` | 

The method `compute.v1.FirewallPoliciesService.AddRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[clone Rules](/compute/docs/reference/rest/v1/firewallPolicies/cloneRules)` | 

The method `compute.v1.FirewallPoliciesService.CloneRules` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/firewallPolicies/delete)` | 

The method `compute.v1.FirewallPoliciesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/firewallPolicies/get)` | 

The method `compute.v1.FirewallPoliciesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Association](/compute/docs/reference/rest/v1/firewallPolicies/getAssociation)` | 

The method `compute.v1.FirewallPoliciesService.GetAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/firewallPolicies/getIamPolicy)` | 

The method `compute.v1.FirewallPoliciesService.GetOrganizationPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Rule](/compute/docs/reference/rest/v1/firewallPolicies/getRule)` | 

The method `compute.v1.FirewallPoliciesService.GetRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/firewallPolicies/insert)` | 

The method `compute.v1.FirewallPoliciesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/firewallPolicies/list)` | 

The method `compute.v1.FirewallPoliciesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Associations](/compute/docs/reference/rest/v1/firewallPolicies/listAssociations)` | 

The method `compute.v1.FirewallPoliciesService.ListAssociations` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[move](/compute/docs/reference/rest/v1/firewallPolicies/move)` | 

The method `compute.v1.FirewallPoliciesService.Move` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/firewallPolicies/patch)` | 

The method `compute.v1.FirewallPoliciesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch Rule](/compute/docs/reference/rest/v1/firewallPolicies/patchRule)` | 

The method `compute.v1.FirewallPoliciesService.PatchRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Association](/compute/docs/reference/rest/v1/firewallPolicies/removeAssociation)` | 

The method `compute.v1.FirewallPoliciesService.RemoveAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Rule](/compute/docs/reference/rest/v1/firewallPolicies/removeRule)` | 

The method `compute.v1.FirewallPoliciesService.RemoveRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/firewallPolicies/setIamPolicy)` | 

The method `compute.v1.FirewallPoliciesService.SetOrganizationPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/firewallPolicies/testIamPermissions)` | 

The method `compute.v1.FirewallPoliciesService.TestOrganizationPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.firewalls](/compute/docs/reference/rest/v1/firewalls)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/firewalls/delete)` | 

The method `compute.v1.FirewallsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/firewalls/get)` | 

The method `compute.v1.FirewallsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/firewalls/insert)` | 

The method `compute.v1.FirewallsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/firewalls/list)` | 

The method `compute.v1.FirewallsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/firewalls/patch)` | 

The method `compute.v1.FirewallsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/firewalls/update)` | 

The method `compute.v1.FirewallsService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.forwardingRules](/compute/docs/reference/rest/v1/forwardingRules)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/forwardingRules/aggregatedList)` | 

The method `compute.v1.RegionForwardingRulesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/forwardingRules/delete)` | 

The method `compute.v1.RegionForwardingRulesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/forwardingRules/get)` | 

The method `compute.v1.RegionForwardingRulesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/forwardingRules/insert)` | 

The method `compute.v1.RegionForwardingRulesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/forwardingRules/list)` | 

The method `compute.v1.RegionForwardingRulesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/forwardingRules/patch)` | 

The method `compute.v1.RegionForwardingRulesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/forwardingRules/setLabels)` | 

The method `compute.v1.RegionForwardingRulesService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Target](/compute/docs/reference/rest/v1/forwardingRules/setTarget)` | 

The method `compute.v1.RegionForwardingRulesService.SetTarget` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.globalAddresses](/compute/docs/reference/rest/v1/globalAddresses)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/globalAddresses/delete)` | 

The method `compute.v1.GlobalAddressesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalAddresses/get)` | 

The method `compute.v1.GlobalAddressesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalAddresses/insert)` | 

The method `compute.v1.GlobalAddressesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalAddresses/list)` | 

The method `compute.v1.GlobalAddressesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[move](/compute/docs/reference/rest/v1/globalAddresses/move)` | 

The method `compute.v1.GlobalAddressesService.Move` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/globalAddresses/setLabels)` | 

The method `compute.v1.GlobalAddressesService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.globalForwardingRules](/compute/docs/reference/rest/v1/globalForwardingRules)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/globalForwardingRules/delete)` | 

The method `compute.v1.GlobalForwardingRulesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalForwardingRules/get)` | 

The method `compute.v1.GlobalForwardingRulesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalForwardingRules/insert)` | 

The method `compute.v1.GlobalForwardingRulesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalForwardingRules/list)` | 

The method `compute.v1.GlobalForwardingRulesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/globalForwardingRules/patch)` | 

The method `compute.v1.GlobalForwardingRulesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/globalForwardingRules/setLabels)` | 

The method `compute.v1.GlobalForwardingRulesService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Target](/compute/docs/reference/rest/v1/globalForwardingRules/setTarget)` | 

The method `compute.v1.GlobalForwardingRulesService.SetTarget` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.globalNetworkEndpointGroups](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups)









| 
Methods | 
|



| 

`[attach Network Endpoints](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/attachNetworkEndpoints)` | 

The method `compute.v1.GlobalNetworkEndpointGroupsService.AttachNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/delete)` | 

The method `compute.v1.GlobalNetworkEndpointGroupsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[detach Network Endpoints](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/detachNetworkEndpoints)` | 

The method `compute.v1.GlobalNetworkEndpointGroupsService.DetachNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/get)` | 

The method `compute.v1.GlobalNetworkEndpointGroupsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/insert)` | 

The method `compute.v1.GlobalNetworkEndpointGroupsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/list)` | 

The method `compute.v1.GlobalNetworkEndpointGroupsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Network Endpoints](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/listNetworkEndpoints)` | 

The method `compute.v1.GlobalNetworkEndpointGroupsService.ListNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.globalOperations](/compute/docs/reference/rest/v1/globalOperations)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/globalOperations/aggregatedList)` | 

The method `compute.v1.GlobalOperationsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/globalOperations/delete)` | 

The method `compute.v1.GlobalOperationsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalOperations/get)` | 

The method `compute.v1.GlobalOperationsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalOperations/list)` | 

The method `compute.v1.GlobalOperationsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[wait](/compute/docs/reference/rest/v1/globalOperations/wait)` | 

The method `compute.v1.GlobalOperationsService.Wait` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.globalOrganizationOperations](/compute/docs/reference/rest/v1/globalOrganizationOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/globalOrganizationOperations/delete)` | 

The method `compute.v1.GlobalOrganizationOperationsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalOrganizationOperations/get)` | 

The method `compute.v1.GlobalOrganizationOperationsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalOrganizationOperations/list)` | 

The method `compute.v1.GlobalOrganizationOperationsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.globalPublicDelegatedPrefixes](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/delete)` | 

The method `compute.v1.GlobalPublicDelegatedPrefixesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/get)` | 

The method `compute.v1.GlobalPublicDelegatedPrefixesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/insert)` | 

The method `compute.v1.GlobalPublicDelegatedPrefixesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/list)` | 

The method `compute.v1.GlobalPublicDelegatedPrefixesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/patch)` | 

The method `compute.v1.GlobalPublicDelegatedPrefixesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.healthChecks](/compute/docs/reference/rest/v1/healthChecks)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/healthChecks/aggregatedList)` | 

The method `compute.v1.HealthChecksService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/healthChecks/delete)` | 

The method `compute.v1.HealthChecksService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/healthChecks/get)` | 

The method `compute.v1.HealthChecksService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/healthChecks/insert)` | 

The method `compute.v1.HealthChecksService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/healthChecks/list)` | 

The method `compute.v1.HealthChecksService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/healthChecks/patch)` | 

The method `compute.v1.HealthChecksService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/healthChecks/update)` | 

The method `compute.v1.HealthChecksService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.httpHealthChecks](/compute/docs/reference/rest/v1/httpHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/httpHealthChecks/delete)` | 

The method `compute.v1.HttpHealthChecksService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/httpHealthChecks/get)` | 

The method `compute.v1.HttpHealthChecksService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/httpHealthChecks/insert)` | 

The method `compute.v1.HttpHealthChecksService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/httpHealthChecks/list)` | 

The method `compute.v1.HttpHealthChecksService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/httpHealthChecks/patch)` | 

The method `compute.v1.HttpHealthChecksService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/httpHealthChecks/update)` | 

The method `compute.v1.HttpHealthChecksService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.httpsHealthChecks](/compute/docs/reference/rest/v1/httpsHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/httpsHealthChecks/delete)` | 

The method `compute.v1.HttpsHealthChecksService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/httpsHealthChecks/get)` | 

The method `compute.v1.HttpsHealthChecksService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/httpsHealthChecks/insert)` | 

The method `compute.v1.HttpsHealthChecksService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/httpsHealthChecks/list)` | 

The method `compute.v1.HttpsHealthChecksService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/httpsHealthChecks/patch)` | 

The method `compute.v1.HttpsHealthChecksService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/httpsHealthChecks/update)` | 

The method `compute.v1.HttpsHealthChecksService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.imageFamilyViews](/compute/docs/reference/rest/v1/imageFamilyViews)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/imageFamilyViews/get)` | 

The method `compute.v1.ImageFamilyViewsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.images](/compute/docs/reference/rest/v1/images)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/images/delete)` | 

The method `compute.v1.ImagesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[deprecate](/compute/docs/reference/rest/v1/images/deprecate)` | 

The method `compute.v1.ImagesService.Deprecate` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/images/get)` | 

The method `compute.v1.ImagesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get From Family](/compute/docs/reference/rest/v1/images/getFromFamily)` | 

The method `compute.v1.ImagesService.GetFromFamily` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/images/getIamPolicy)` | 

The method `compute.v1.ImagesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/images/insert)` | 

The method `compute.v1.ImagesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/images/list)` | 

The method `compute.v1.ImagesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/images/patch)` | 

The method `compute.v1.ImagesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/images/setIamPolicy)` | 

The method `compute.v1.ImagesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/images/setLabels)` | 

The method `compute.v1.ImagesService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/images/testIamPermissions)` | 

The method `compute.v1.ImagesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.instanceGroupManagerResizeRequests](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests)









| 
Methods | 
|



| 

`[cancel](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/cancel)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.Cancel` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/delete)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/get)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/list)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.instanceGroupManagers](/compute/docs/reference/rest/v1/instanceGroupManagers)









| 
Methods | 
|



| 

`[abandon Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/abandonInstances)` | 

The method `compute.v1.InstanceGroupManagersService.AbandonInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/instanceGroupManagers/aggregatedList)` | 

The method `compute.v1.InstanceGroupManagersService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[apply Updates To Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/applyUpdatesToInstances)` | 

The method `compute.v1.InstanceGroupManagersService.ApplyUpdatesToInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[create Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/createInstances)` | 

The method `compute.v1.InstanceGroupManagersService.CreateInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instanceGroupManagers/delete)` | 

The method `compute.v1.InstanceGroupManagersService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/deleteInstances)` | 

The method `compute.v1.InstanceGroupManagersService.DeleteInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete Per Instance Configs](/compute/docs/reference/rest/v1/instanceGroupManagers/deletePerInstanceConfigs)` | 

The method `compute.v1.InstanceGroupManagersService.DeletePerInstanceConfigs` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instanceGroupManagers/get)` | 

The method `compute.v1.InstanceGroupManagersService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instanceGroupManagers/insert)` | 

The method `compute.v1.InstanceGroupManagersService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instanceGroupManagers/list)` | 

The method `compute.v1.InstanceGroupManagersService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Errors](/compute/docs/reference/rest/v1/instanceGroupManagers/listErrors)` | 

The method `compute.v1.InstanceGroupManagersService.ListErrors` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Managed Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances)` | 

The method `compute.v1.InstanceGroupManagersService.ListManagedInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Per Instance Configs](/compute/docs/reference/rest/v1/instanceGroupManagers/listPerInstanceConfigs)` | 

The method `compute.v1.InstanceGroupManagersService.ListPerInstanceConfigs` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/instanceGroupManagers/patch)` | 

The method `compute.v1.InstanceGroupManagersService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch Per Instance Configs](/compute/docs/reference/rest/v1/instanceGroupManagers/patchPerInstanceConfigs)` | 

The method `compute.v1.InstanceGroupManagersService.PatchPerInstanceConfigs` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[recreate Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/recreateInstances)` | 

The method `compute.v1.InstanceGroupManagersService.RecreateInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/instanceGroupManagers/resize)` | 

The method `compute.v1.InstanceGroupManagersService.Resize` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[resume Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/resumeInstances)` | 

The method `compute.v1.InstanceGroupManagersService.ResumeInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Instance Template](/compute/docs/reference/rest/v1/instanceGroupManagers/setInstanceTemplate)` | 

The method `compute.v1.InstanceGroupManagersService.SetInstanceTemplate` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Target Pools](/compute/docs/reference/rest/v1/instanceGroupManagers/setTargetPools)` | 

The method `compute.v1.InstanceGroupManagersService.SetTargetPools` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[start Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/startInstances)` | 

The method `compute.v1.InstanceGroupManagersService.StartInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[stop Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/stopInstances)` | 

The method `compute.v1.InstanceGroupManagersService.StopInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[suspend Instances](/compute/docs/reference/rest/v1/instanceGroupManagers/suspendInstances)` | 

The method `compute.v1.InstanceGroupManagersService.SuspendInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update Per Instance Configs](/compute/docs/reference/rest/v1/instanceGroupManagers/updatePerInstanceConfigs)` | 

The method `compute.v1.InstanceGroupManagersService.UpdatePerInstanceConfigs` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.instanceGroups](/compute/docs/reference/rest/v1/instanceGroups)









| 
Methods | 
|



| 

`[add Instances](/compute/docs/reference/rest/v1/instanceGroups/addInstances)` | 

The method `compute.v1.InstanceGroupsService.AddInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/instanceGroups/aggregatedList)` | 

The method `compute.v1.InstanceGroupsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instanceGroups/delete)` | 

The method `compute.v1.InstanceGroupsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instanceGroups/get)` | 

The method `compute.v1.InstanceGroupsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instanceGroups/insert)` | 

The method `compute.v1.InstanceGroupsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instanceGroups/list)` | 

The method `compute.v1.InstanceGroupsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Instances](/compute/docs/reference/rest/v1/instanceGroups/listInstances)` | 

The method `compute.v1.InstanceGroupsService.ListInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Instances](/compute/docs/reference/rest/v1/instanceGroups/removeInstances)` | 

The method `compute.v1.InstanceGroupsService.RemoveInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Named Ports](/compute/docs/reference/rest/v1/instanceGroups/setNamedPorts)` | 

The method `compute.v1.InstanceGroupsService.SetNamedPorts` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.instanceSettings](/compute/docs/reference/rest/v1/instanceSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/instanceSettings/get)` | 

The method `compute.v1.InstanceSettingsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/instanceSettings/patch)` | 

The method `compute.v1.InstanceSettingsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.instanceTemplates](/compute/docs/reference/rest/v1/instanceTemplates)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/instanceTemplates/aggregatedList)` | 

The method `compute.v1.InstanceTemplatesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instanceTemplates/delete)` | 

The method `compute.v1.InstanceTemplatesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instanceTemplates/get)` | 

The method `compute.v1.InstanceTemplatesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/instanceTemplates/getIamPolicy)` | 

The method `compute.v1.InstanceTemplatesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instanceTemplates/insert)` | 

The method `compute.v1.InstanceTemplatesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instanceTemplates/list)` | 

The method `compute.v1.InstanceTemplatesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/instanceTemplates/setIamPolicy)` | 

The method `compute.v1.InstanceTemplatesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/instanceTemplates/testIamPermissions)` | 

The method `compute.v1.InstanceTemplatesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.instances](/compute/docs/reference/rest/v1/instances)









| 
Methods | 
|



| 

`[add Access Config](/compute/docs/reference/rest/v1/instances/addAccessConfig)` | 

The method `compute.v1.InstancesService.AddAccessConfig` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[add Resource Policies](/compute/docs/reference/rest/v1/instances/addResourcePolicies)` | 

The method `compute.v1.InstancesService.AddResourcePolicies` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/instances/aggregatedList)` | 

The method `compute.v1.InstancesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[attach Disk](/compute/docs/reference/rest/v1/instances/attachDisk)` | 

The method `compute.v1.InstancesService.AttachDisk` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[bulk Insert](/compute/docs/reference/rest/v1/instances/bulkInsert)` | 

The method `compute.v1.InstancesService.BulkInsert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instances/delete)` | 

The method `compute.v1.InstancesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete Access Config](/compute/docs/reference/rest/v1/instances/deleteAccessConfig)` | 

The method `compute.v1.InstancesService.DeleteAccessConfig` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[detach Disk](/compute/docs/reference/rest/v1/instances/detachDisk)` | 

The method `compute.v1.InstancesService.DetachDisk` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instances/get)` | 

The method `compute.v1.InstancesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Effective Firewalls](/compute/docs/reference/rest/v1/instances/getEffectiveFirewalls)` | 

The method `compute.v1.InstancesService.GetEffectiveFirewalls` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Guest Attributes](/compute/docs/reference/rest/v1/instances/getGuestAttributes)` | 

The method `compute.v1.InstancesService.GetGuestAttributes` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/instances/getIamPolicy)` | 

The method `compute.v1.InstancesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Screenshot](/compute/docs/reference/rest/v1/instances/getScreenshot)` | 

The method `compute.v1.InstancesService.GetScreenshot` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Serial Port Output](/compute/docs/reference/rest/v1/instances/getSerialPortOutput)` | 

The method `compute.v1.InstancesService.GetSerialPortOutput` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Shielded Instance Identity](/compute/docs/reference/rest/v1/instances/getShieldedInstanceIdentity)` | 

The method `compute.v1.InstancesService.GetShieldedInstanceIdentity` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instances/insert)` | 

The method `compute.v1.InstancesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instances/list)` | 

The method `compute.v1.InstancesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Referrers](/compute/docs/reference/rest/v1/instances/listReferrers)` | 

The method `compute.v1.InstancesService.ListReferrers` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[perform Maintenance](/compute/docs/reference/rest/v1/instances/performMaintenance)` | 

The method `compute.v1.InstancesService.PerformMaintenance` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Resource Policies](/compute/docs/reference/rest/v1/instances/removeResourcePolicies)` | 

The method `compute.v1.InstancesService.RemoveResourcePolicies` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[reset](/compute/docs/reference/rest/v1/instances/reset)` | 

The method `compute.v1.InstancesService.Reset` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[resume](/compute/docs/reference/rest/v1/instances/resume)` | 

The method `compute.v1.InstancesService.Resume` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[send Diagnostic Interrupt](/compute/docs/reference/rest/v1/instances/sendDiagnosticInterrupt)` | 

The method `compute.v1.InstancesService.SendDiagnosticInterrupt` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Deletion Protection](/compute/docs/reference/rest/v1/instances/setDeletionProtection)` | 

The method `compute.v1.InstancesService.SetDeletionProtection` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Disk Auto Delete](/compute/docs/reference/rest/v1/instances/setDiskAutoDelete)` | 

The method `compute.v1.InstancesService.SetDiskAutoDelete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/instances/setIamPolicy)` | 

The method `compute.v1.InstancesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/instances/setLabels)` | 

The method `compute.v1.InstancesService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Machine Resources](/compute/docs/reference/rest/v1/instances/setMachineResources)` | 

The method `compute.v1.InstancesService.SetMachineResources` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Machine Type](/compute/docs/reference/rest/v1/instances/setMachineType)` | 

The method `compute.v1.InstancesService.SetMachineType` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Metadata](/compute/docs/reference/rest/v1/instances/setMetadata)` | 

The method `compute.v1.InstancesService.SetMetadata` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Min Cpu Platform](/compute/docs/reference/rest/v1/instances/setMinCpuPlatform)` | 

The method `compute.v1.InstancesService.SetMinCpuPlatform` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Name](/compute/docs/reference/rest/v1/instances/setName)` | 

The method `compute.v1.InstancesService.SetName` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Scheduling](/compute/docs/reference/rest/v1/instances/setScheduling)` | 

The method `compute.v1.InstancesService.SetScheduling` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Security Policy](/compute/docs/reference/rest/v1/instances/setSecurityPolicy)` | 

The method `compute.v1.InstancesService.SetSecurityPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Service Account](/compute/docs/reference/rest/v1/instances/setServiceAccount)` | 

The method `compute.v1.InstancesService.SetServiceAccount` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Shielded Instance Integrity Policy](/compute/docs/reference/rest/v1/instances/setShieldedInstanceIntegrityPolicy)` | 

The method `compute.v1.InstancesService.SetShieldedInstanceIntegrityPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Tags](/compute/docs/reference/rest/v1/instances/setTags)` | 

The method `compute.v1.InstancesService.SetTags` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[simulate Maintenance Event](/compute/docs/reference/rest/v1/instances/simulateMaintenanceEvent)` | 

The method `compute.v1.InstancesService.SimulateMaintenanceEvent` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[start](/compute/docs/reference/rest/v1/instances/start)` | 

The method `compute.v1.InstancesService.Start` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[start With Encryption Key](/compute/docs/reference/rest/v1/instances/startWithEncryptionKey)` | 

The method `compute.v1.InstancesService.StartWithEncryptionKey` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[stop](/compute/docs/reference/rest/v1/instances/stop)` | 

The method `compute.v1.InstancesService.Stop` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[suspend](/compute/docs/reference/rest/v1/instances/suspend)` | 

The method `compute.v1.InstancesService.Suspend` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/instances/testIamPermissions)` | 

The method `compute.v1.InstancesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/instances/update)` | 

The method `compute.v1.InstancesService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update Access Config](/compute/docs/reference/rest/v1/instances/updateAccessConfig)` | 

The method `compute.v1.InstancesService.UpdateAccessConfig` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update Display Device](/compute/docs/reference/rest/v1/instances/updateDisplayDevice)` | 

The method `compute.v1.InstancesService.UpdateDisplayDevice` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update Network Interface](/compute/docs/reference/rest/v1/instances/updateNetworkInterface)` | 

The method `compute.v1.InstancesService.UpdateNetworkInterface` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update Shielded Instance Config](/compute/docs/reference/rest/v1/instances/updateShieldedInstanceConfig)` | 

The method `compute.v1.InstancesService.UpdateShieldedInstanceConfig` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.instantSnapshots](/compute/docs/reference/rest/v1/instantSnapshots)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/instantSnapshots/aggregatedList)` | 

The method `compute.v1.InstantSnapshotsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instantSnapshots/delete)` | 

The method `compute.v1.InstantSnapshotsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instantSnapshots/get)` | 

The method `compute.v1.InstantSnapshotsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/instantSnapshots/getIamPolicy)` | 

The method `compute.v1.InstantSnapshotsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instantSnapshots/insert)` | 

The method `compute.v1.InstantSnapshotsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instantSnapshots/list)` | 

The method `compute.v1.InstantSnapshotsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/instantSnapshots/setIamPolicy)` | 

The method `compute.v1.InstantSnapshotsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/instantSnapshots/setLabels)` | 

The method `compute.v1.InstantSnapshotsService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/instantSnapshots/testIamPermissions)` | 

The method `compute.v1.InstantSnapshotsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.interconnectAttachments](/compute/docs/reference/rest/v1/interconnectAttachments)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/interconnectAttachments/aggregatedList)` | 

The method `compute.v1.InterconnectAttachmentsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/interconnectAttachments/delete)` | 

The method `compute.v1.InterconnectAttachmentsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/interconnectAttachments/get)` | 

The method `compute.v1.InterconnectAttachmentsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/interconnectAttachments/insert)` | 

The method `compute.v1.InterconnectAttachmentsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnectAttachments/list)` | 

The method `compute.v1.InterconnectAttachmentsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/interconnectAttachments/patch)` | 

The method `compute.v1.InterconnectAttachmentsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/interconnectAttachments/setLabels)` | 

The method `compute.v1.InterconnectAttachmentsService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.interconnectLocations](/compute/docs/reference/rest/v1/interconnectLocations)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/interconnectLocations/get)` | 

The method `compute.v1.InterconnectLocationsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnectLocations/list)` | 

The method `compute.v1.InterconnectLocationsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.interconnectRemoteLocations](/compute/docs/reference/rest/v1/interconnectRemoteLocations)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/interconnectRemoteLocations/get)` | 

The method `compute.v1.InterconnectRemoteLocationsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnectRemoteLocations/list)` | 

The method `compute.v1.InterconnectRemoteLocationsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.interconnects](/compute/docs/reference/rest/v1/interconnects)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/interconnects/delete)` | 

The method `compute.v1.InterconnectsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/interconnects/get)` | 

The method `compute.v1.InterconnectsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Diagnostics](/compute/docs/reference/rest/v1/interconnects/getDiagnostics)` | 

The method `compute.v1.InterconnectsService.GetDiagnostics` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Macsec Config](/compute/docs/reference/rest/v1/interconnects/getMacsecConfig)` | 

The method `compute.v1.InterconnectsService.GetMacsecConfig` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/interconnects/insert)` | 

The method `compute.v1.InterconnectsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnects/list)` | 

The method `compute.v1.InterconnectsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/interconnects/patch)` | 

The method `compute.v1.InterconnectsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/interconnects/setLabels)` | 

The method `compute.v1.InterconnectsService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.licenseCodes](/compute/docs/reference/rest/v1/licenseCodes)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/licenseCodes/get)` | 

The method `compute.v1.LicenseCodesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/licenseCodes/testIamPermissions)` | 

The method `compute.v1.LicenseCodesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.licenses](/compute/docs/reference/rest/v1/licenses)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/licenses/delete)` | 

The method `compute.v1.LicensesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/licenses/get)` | 

The method `compute.v1.LicensesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/licenses/getIamPolicy)` | 

The method `compute.v1.LicensesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/licenses/insert)` | 

The method `compute.v1.LicensesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/licenses/list)` | 

The method `compute.v1.LicensesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/licenses/setIamPolicy)` | 

The method `compute.v1.LicensesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/licenses/testIamPermissions)` | 

The method `compute.v1.LicensesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.machineImages](/compute/docs/reference/rest/v1/machineImages)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/machineImages/delete)` | 

The method `compute.v1.MachineImagesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/machineImages/get)` | 

The method `compute.v1.MachineImagesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/machineImages/getIamPolicy)` | 

The method `compute.v1.MachineImagesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/machineImages/insert)` | 

The method `compute.v1.MachineImagesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/machineImages/list)` | 

The method `compute.v1.MachineImagesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/machineImages/setIamPolicy)` | 

The method `compute.v1.MachineImagesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/machineImages/testIamPermissions)` | 

The method `compute.v1.MachineImagesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.machineTypes](/compute/docs/reference/rest/v1/machineTypes)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/machineTypes/aggregatedList)` | 

The method `compute.v1.MachineTypesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/machineTypes/get)` | 

The method `compute.v1.MachineTypesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/machineTypes/list)` | 

The method `compute.v1.MachineTypesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.networkAttachments](/compute/docs/reference/rest/v1/networkAttachments)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/networkAttachments/aggregatedList)` | 

The method `compute.v1.NetworkAttachmentsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networkAttachments/delete)` | 

The method `compute.v1.NetworkAttachmentsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networkAttachments/get)` | 

The method `compute.v1.NetworkAttachmentsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/networkAttachments/getIamPolicy)` | 

The method `compute.v1.NetworkAttachmentsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networkAttachments/insert)` | 

The method `compute.v1.NetworkAttachmentsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networkAttachments/list)` | 

The method `compute.v1.NetworkAttachmentsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/networkAttachments/patch)` | 

The method `compute.v1.NetworkAttachmentsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/networkAttachments/setIamPolicy)` | 

The method `compute.v1.NetworkAttachmentsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/networkAttachments/testIamPermissions)` | 

The method `compute.v1.NetworkAttachmentsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.networkEdgeSecurityServices](/compute/docs/reference/rest/v1/networkEdgeSecurityServices)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/aggregatedList)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/delete)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/get)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/insert)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/patch)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.networkEndpointGroups](/compute/docs/reference/rest/v1/networkEndpointGroups)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/networkEndpointGroups/aggregatedList)` | 

The method `compute.v1.NetworkEndpointGroupsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[attach Network Endpoints](/compute/docs/reference/rest/v1/networkEndpointGroups/attachNetworkEndpoints)` | 

The method `compute.v1.NetworkEndpointGroupsService.AttachNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networkEndpointGroups/delete)` | 

The method `compute.v1.NetworkEndpointGroupsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[detach Network Endpoints](/compute/docs/reference/rest/v1/networkEndpointGroups/detachNetworkEndpoints)` | 

The method `compute.v1.NetworkEndpointGroupsService.DetachNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networkEndpointGroups/get)` | 

The method `compute.v1.NetworkEndpointGroupsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networkEndpointGroups/insert)` | 

The method `compute.v1.NetworkEndpointGroupsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networkEndpointGroups/list)` | 

The method `compute.v1.NetworkEndpointGroupsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Network Endpoints](/compute/docs/reference/rest/v1/networkEndpointGroups/listNetworkEndpoints)` | 

The method `compute.v1.NetworkEndpointGroupsService.ListNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/networkEndpointGroups/testIamPermissions)` | 

The method `compute.v1.NetworkEndpointGroupsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.networkFirewallPolicies](/compute/docs/reference/rest/v1/networkFirewallPolicies)









| 
Methods | 
|



| 

`[add Association](/compute/docs/reference/rest/v1/networkFirewallPolicies/addAssociation)` | 

The method `compute.v1.NetworkFirewallPoliciesService.AddAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[add Rule](/compute/docs/reference/rest/v1/networkFirewallPolicies/addRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.AddRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/networkFirewallPolicies/aggregatedList)` | 

The method `compute.v1.NetworkFirewallPoliciesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[clone Rules](/compute/docs/reference/rest/v1/networkFirewallPolicies/cloneRules)` | 

The method `compute.v1.NetworkFirewallPoliciesService.CloneRules` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networkFirewallPolicies/delete)` | 

The method `compute.v1.NetworkFirewallPoliciesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networkFirewallPolicies/get)` | 

The method `compute.v1.NetworkFirewallPoliciesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Association](/compute/docs/reference/rest/v1/networkFirewallPolicies/getAssociation)` | 

The method `compute.v1.NetworkFirewallPoliciesService.GetAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/networkFirewallPolicies/getIamPolicy)` | 

The method `compute.v1.NetworkFirewallPoliciesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Rule](/compute/docs/reference/rest/v1/networkFirewallPolicies/getRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.GetRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networkFirewallPolicies/insert)` | 

The method `compute.v1.NetworkFirewallPoliciesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networkFirewallPolicies/list)` | 

The method `compute.v1.NetworkFirewallPoliciesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/networkFirewallPolicies/patch)` | 

The method `compute.v1.NetworkFirewallPoliciesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch Rule](/compute/docs/reference/rest/v1/networkFirewallPolicies/patchRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.PatchRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Association](/compute/docs/reference/rest/v1/networkFirewallPolicies/removeAssociation)` | 

The method `compute.v1.NetworkFirewallPoliciesService.RemoveAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Rule](/compute/docs/reference/rest/v1/networkFirewallPolicies/removeRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.RemoveRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/networkFirewallPolicies/setIamPolicy)` | 

The method `compute.v1.NetworkFirewallPoliciesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/networkFirewallPolicies/testIamPermissions)` | 

The method `compute.v1.NetworkFirewallPoliciesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.networkProfiles](/compute/docs/reference/rest/v1/networkProfiles)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/networkProfiles/get)` | 

The method `compute.v1.NetworkProfilesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networkProfiles/list)` | 

The method `compute.v1.NetworkProfilesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.networks](/compute/docs/reference/rest/v1/networks)









| 
Methods | 
|



| 

`[add Peering](/compute/docs/reference/rest/v1/networks/addPeering)` | 

The method `compute.v1.NetworksService.AddPeering` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networks/delete)` | 

The method `compute.v1.NetworksService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networks/get)` | 

The method `compute.v1.NetworksService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Effective Firewalls](/compute/docs/reference/rest/v1/networks/getEffectiveFirewalls)` | 

The method `compute.v1.NetworksService.GetEffectiveFirewalls` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networks/insert)` | 

The method `compute.v1.NetworksService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networks/list)` | 

The method `compute.v1.NetworksService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Peering Routes](/compute/docs/reference/rest/v1/networks/listPeeringRoutes)` | 

The method `compute.v1.NetworksService.ListPeeringRoutes` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/networks/patch)` | 

The method `compute.v1.NetworksService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Peering](/compute/docs/reference/rest/v1/networks/removePeering)` | 

The method `compute.v1.NetworksService.RemovePeering` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[switch To Custom Mode](/compute/docs/reference/rest/v1/networks/switchToCustomMode)` | 

The method `compute.v1.NetworksService.SwitchToCustomMode` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update Peering](/compute/docs/reference/rest/v1/networks/updatePeering)` | 

The method `compute.v1.NetworksService.UpdatePeering` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.nodeGroups](/compute/docs/reference/rest/v1/nodeGroups)









| 
Methods | 
|



| 

`[add Nodes](/compute/docs/reference/rest/v1/nodeGroups/addNodes)` | 

The method `compute.v1.NodeGroupsService.AddNodes` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/nodeGroups/aggregatedList)` | 

The method `compute.v1.NodeGroupsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/nodeGroups/delete)` | 

The method `compute.v1.NodeGroupsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete Nodes](/compute/docs/reference/rest/v1/nodeGroups/deleteNodes)` | 

The method `compute.v1.NodeGroupsService.DeleteNodes` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/nodeGroups/get)` | 

The method `compute.v1.NodeGroupsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/nodeGroups/getIamPolicy)` | 

The method `compute.v1.NodeGroupsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/nodeGroups/insert)` | 

The method `compute.v1.NodeGroupsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/nodeGroups/list)` | 

The method `compute.v1.NodeGroupsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Nodes](/compute/docs/reference/rest/v1/nodeGroups/listNodes)` | 

The method `compute.v1.NodeGroupsService.ListNodes` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/nodeGroups/patch)` | 

The method `compute.v1.NodeGroupsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[perform Maintenance](/compute/docs/reference/rest/v1/nodeGroups/performMaintenance)` | 

The method `compute.v1.NodeGroupsService.PerformMaintenance` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/nodeGroups/setIamPolicy)` | 

The method `compute.v1.NodeGroupsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Node Template](/compute/docs/reference/rest/v1/nodeGroups/setNodeTemplate)` | 

The method `compute.v1.NodeGroupsService.SetNodeTemplate` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[simulate Maintenance Event](/compute/docs/reference/rest/v1/nodeGroups/simulateMaintenanceEvent)` | 

The method `compute.v1.NodeGroupsService.SimulateMaintenanceEvent` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/nodeGroups/testIamPermissions)` | 

The method `compute.v1.NodeGroupsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.nodeTemplates](/compute/docs/reference/rest/v1/nodeTemplates)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/nodeTemplates/aggregatedList)` | 

The method `compute.v1.NodeTemplatesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/nodeTemplates/delete)` | 

The method `compute.v1.NodeTemplatesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/nodeTemplates/get)` | 

The method `compute.v1.NodeTemplatesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/nodeTemplates/getIamPolicy)` | 

The method `compute.v1.NodeTemplatesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/nodeTemplates/insert)` | 

The method `compute.v1.NodeTemplatesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/nodeTemplates/list)` | 

The method `compute.v1.NodeTemplatesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/nodeTemplates/setIamPolicy)` | 

The method `compute.v1.NodeTemplatesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/nodeTemplates/testIamPermissions)` | 

The method `compute.v1.NodeTemplatesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.nodeTypes](/compute/docs/reference/rest/v1/nodeTypes)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/nodeTypes/aggregatedList)` | 

The method `compute.v1.NodeTypesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/nodeTypes/get)` | 

The method `compute.v1.NodeTypesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/nodeTypes/list)` | 

The method `compute.v1.NodeTypesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.packetMirrorings](/compute/docs/reference/rest/v1/packetMirrorings)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/packetMirrorings/aggregatedList)` | 

The method `compute.v1.PacketMirroringsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/packetMirrorings/delete)` | 

The method `compute.v1.PacketMirroringsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/packetMirrorings/get)` | 

The method `compute.v1.PacketMirroringsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/packetMirrorings/insert)` | 

The method `compute.v1.PacketMirroringsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/packetMirrorings/list)` | 

The method `compute.v1.PacketMirroringsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/packetMirrorings/patch)` | 

The method `compute.v1.PacketMirroringsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/packetMirrorings/testIamPermissions)` | 

The method `compute.v1.PacketMirroringsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.projects](/compute/docs/reference/rest/v1/projects)









| 
Methods | 
|



| 

`[disable Xpn Host](/compute/docs/reference/rest/v1/projects/disableXpnHost)` | 

The method `compute.v1.ProjectsService.DisableXpnHost` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[disable Xpn Resource](/compute/docs/reference/rest/v1/projects/disableXpnResource)` | 

The method `compute.v1.ProjectsService.DisableXpnResource` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[enable Xpn Host](/compute/docs/reference/rest/v1/projects/enableXpnHost)` | 

The method `compute.v1.ProjectsService.EnableXpnHost` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[enable Xpn Resource](/compute/docs/reference/rest/v1/projects/enableXpnResource)` | 

The method `compute.v1.ProjectsService.EnableXpnResource` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/projects/get)` | 

The method `compute.v1.ProjectsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Xpn Host](/compute/docs/reference/rest/v1/projects/getXpnHost)` | 

The method `compute.v1.ProjectsService.GetXpnHost` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Xpn Resources](/compute/docs/reference/rest/v1/projects/getXpnResources)` | 

The method `compute.v1.ProjectsService.GetXpnResources` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Xpn Hosts](/compute/docs/reference/rest/v1/projects/listXpnHosts)` | 

The method `compute.v1.ProjectsService.ListXpnHosts` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[move Disk](/compute/docs/reference/rest/v1/projects/moveDisk)` | 

The method `compute.v1.ProjectsService.MoveDisk` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[move Instance](/compute/docs/reference/rest/v1/projects/moveInstance) 
(deprecated)**` | 

The method `compute.v1.ProjectsService.MoveInstance` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Cloud Armor Tier](/compute/docs/reference/rest/v1/projects/setCloudArmorTier)` | 

The method `compute.v1.ProjectsService.SetCloudArmorTier` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Common Instance Metadata](/compute/docs/reference/rest/v1/projects/setCommonInstanceMetadata)` | 

The method `compute.v1.ProjectsService.SetCommonInstanceMetadata` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Default Network Tier](/compute/docs/reference/rest/v1/projects/setDefaultNetworkTier)` | 

The method `compute.v1.ProjectsService.SetDefaultNetworkTier` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Usage Export Bucket](/compute/docs/reference/rest/v1/projects/setUsageExportBucket)` | 

The method `compute.v1.ProjectsService.SetUsageExportBucket` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.publicAdvertisedPrefixes](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes)









| 
Methods | 
|



| 

`[announce](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/announce)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.Announce` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/delete)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/get)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/insert)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/list)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/patch)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[withdraw](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/withdraw)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.Withdraw` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.publicDelegatedPrefixes](/compute/docs/reference/rest/v1/publicDelegatedPrefixes)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/aggregatedList)` | 

The method `compute.v1.PublicDelegatedPrefixesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[announce](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/announce)` | 

The method `compute.v1.PublicDelegatedPrefixesService.Announce` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/delete)` | 

The method `compute.v1.PublicDelegatedPrefixesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/get)` | 

The method `compute.v1.PublicDelegatedPrefixesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/insert)` | 

The method `compute.v1.PublicDelegatedPrefixesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/list)` | 

The method `compute.v1.PublicDelegatedPrefixesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/patch)` | 

The method `compute.v1.PublicDelegatedPrefixesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[withdraw](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/withdraw)` | 

The method `compute.v1.PublicDelegatedPrefixesService.Withdraw` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionAutoscalers](/compute/docs/reference/rest/v1/regionAutoscalers)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionAutoscalers/delete)` | 

The method `compute.v1.RegionAutoscalersService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionAutoscalers/get)` | 

The method `compute.v1.RegionAutoscalersService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionAutoscalers/insert)` | 

The method `compute.v1.RegionAutoscalersService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionAutoscalers/list)` | 

The method `compute.v1.RegionAutoscalersService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionAutoscalers/patch)` | 

The method `compute.v1.RegionAutoscalersService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionAutoscalers/update)` | 

The method `compute.v1.RegionAutoscalersService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionBackendServices](/compute/docs/reference/rest/v1/regionBackendServices)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionBackendServices/delete)` | 

The method `compute.v1.RegionBackendServicesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionBackendServices/get)` | 

The method `compute.v1.RegionBackendServicesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Health](/compute/docs/reference/rest/v1/regionBackendServices/getHealth)` | 

The method `compute.v1.RegionBackendServicesService.GetHealth` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/regionBackendServices/getIamPolicy)` | 

The method `compute.v1.RegionBackendServicesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionBackendServices/insert)` | 

The method `compute.v1.RegionBackendServicesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionBackendServices/list)` | 

The method `compute.v1.RegionBackendServicesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Usable](/compute/docs/reference/rest/v1/regionBackendServices/listUsable)` | 

The method `compute.v1.RegionBackendServicesService.ListUsable` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionBackendServices/patch)` | 

The method `compute.v1.RegionBackendServicesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/regionBackendServices/setIamPolicy)` | 

The method `compute.v1.RegionBackendServicesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Security Policy](/compute/docs/reference/rest/v1/regionBackendServices/setSecurityPolicy)` | 

The method `compute.v1.RegionBackendServicesService.SetSecurityPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/regionBackendServices/testIamPermissions)` | 

The method `compute.v1.RegionBackendServicesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionBackendServices/update)` | 

The method `compute.v1.RegionBackendServicesService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionCommitments](/compute/docs/reference/rest/v1/regionCommitments)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/regionCommitments/aggregatedList)` | 

The method `compute.v1.RegionCommitmentsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionCommitments/get)` | 

The method `compute.v1.RegionCommitmentsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionCommitments/insert)` | 

The method `compute.v1.RegionCommitmentsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionCommitments/list)` | 

The method `compute.v1.RegionCommitmentsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionCommitments/update)` | 

The method `compute.v1.RegionCommitmentsService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionDiskTypes](/compute/docs/reference/rest/v1/regionDiskTypes)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/regionDiskTypes/get)` | 

The method `compute.v1.RegionDiskTypesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionDiskTypes/list)` | 

The method `compute.v1.RegionDiskTypesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionDisks](/compute/docs/reference/rest/v1/regionDisks)









| 
Methods | 
|



| 

`[add Resource Policies](/compute/docs/reference/rest/v1/regionDisks/addResourcePolicies)` | 

The method `compute.v1.RegionDisksService.AddResourcePolicies` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[bulk Insert](/compute/docs/reference/rest/v1/regionDisks/bulkInsert)` | 

The method `compute.v1.RegionDisksService.BulkInsert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[create Snapshot](/compute/docs/reference/rest/v1/regionDisks/createSnapshot)` | 

The method `compute.v1.RegionDisksService.CreateSnapshot` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionDisks/delete)` | 

The method `compute.v1.RegionDisksService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionDisks/get)` | 

The method `compute.v1.RegionDisksService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/regionDisks/getIamPolicy)` | 

The method `compute.v1.RegionDisksService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionDisks/insert)` | 

The method `compute.v1.RegionDisksService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionDisks/list)` | 

The method `compute.v1.RegionDisksService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Resource Policies](/compute/docs/reference/rest/v1/regionDisks/removeResourcePolicies)` | 

The method `compute.v1.RegionDisksService.RemoveResourcePolicies` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/regionDisks/resize)` | 

The method `compute.v1.RegionDisksService.Resize` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/regionDisks/setIamPolicy)` | 

The method `compute.v1.RegionDisksService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/regionDisks/setLabels)` | 

The method `compute.v1.RegionDisksService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[start Async Replication](/compute/docs/reference/rest/v1/regionDisks/startAsyncReplication)` | 

The method `compute.v1.RegionDisksService.StartAsyncReplication` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[stop Async Replication](/compute/docs/reference/rest/v1/regionDisks/stopAsyncReplication)` | 

The method `compute.v1.RegionDisksService.StopAsyncReplication` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[stop Group Async Replication](/compute/docs/reference/rest/v1/regionDisks/stopGroupAsyncReplication)` | 

The method `compute.v1.RegionDisksService.StopGroupAsyncReplication` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/regionDisks/testIamPermissions)` | 

The method `compute.v1.RegionDisksService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionDisks/update)` | 

The method `compute.v1.RegionDisksService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionHealthCheckServices](/compute/docs/reference/rest/v1/regionHealthCheckServices)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionHealthCheckServices/delete)` | 

The method `compute.v1.RegionHealthCheckServicesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionHealthCheckServices/get)` | 

The method `compute.v1.RegionHealthCheckServicesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionHealthCheckServices/insert)` | 

The method `compute.v1.RegionHealthCheckServicesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionHealthCheckServices/list)` | 

The method `compute.v1.RegionHealthCheckServicesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionHealthCheckServices/patch)` | 

The method `compute.v1.RegionHealthCheckServicesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionHealthChecks](/compute/docs/reference/rest/v1/regionHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionHealthChecks/delete)` | 

The method `compute.v1.RegionHealthChecksService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionHealthChecks/get)` | 

The method `compute.v1.RegionHealthChecksService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionHealthChecks/insert)` | 

The method `compute.v1.RegionHealthChecksService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionHealthChecks/list)` | 

The method `compute.v1.RegionHealthChecksService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionHealthChecks/patch)` | 

The method `compute.v1.RegionHealthChecksService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionHealthChecks/update)` | 

The method `compute.v1.RegionHealthChecksService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionInstanceGroupManagers](/compute/docs/reference/rest/v1/regionInstanceGroupManagers)









| 
Methods | 
|



| 

`[abandon Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/abandonInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.AbandonInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[apply Updates To Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/applyUpdatesToInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.ApplyUpdatesToInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[create Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/createInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.CreateInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/delete)` | 

The method `compute.v1.RegionInstanceGroupManagersService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/deleteInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.DeleteInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete Per Instance Configs](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/deletePerInstanceConfigs)` | 

The method `compute.v1.RegionInstanceGroupManagersService.DeletePerInstanceConfigs` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get)` | 

The method `compute.v1.RegionInstanceGroupManagersService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert)` | 

The method `compute.v1.RegionInstanceGroupManagersService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/list)` | 

The method `compute.v1.RegionInstanceGroupManagersService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Errors](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listErrors)` | 

The method `compute.v1.RegionInstanceGroupManagersService.ListErrors` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Managed Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.ListManagedInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Per Instance Configs](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listPerInstanceConfigs)` | 

The method `compute.v1.RegionInstanceGroupManagersService.ListPerInstanceConfigs` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch)` | 

The method `compute.v1.RegionInstanceGroupManagersService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch Per Instance Configs](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patchPerInstanceConfigs)` | 

The method `compute.v1.RegionInstanceGroupManagersService.PatchPerInstanceConfigs` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[recreate Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/recreateInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.RecreateInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/resize)` | 

The method `compute.v1.RegionInstanceGroupManagersService.Resize` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[resume Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/resumeInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.ResumeInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Instance Template](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/setInstanceTemplate)` | 

The method `compute.v1.RegionInstanceGroupManagersService.SetInstanceTemplate` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Target Pools](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/setTargetPools)` | 

The method `compute.v1.RegionInstanceGroupManagersService.SetTargetPools` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[start Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/startInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.StartInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[stop Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/stopInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.StopInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[suspend Instances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/suspendInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.SuspendInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update Per Instance Configs](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/updatePerInstanceConfigs)` | 

The method `compute.v1.RegionInstanceGroupManagersService.UpdatePerInstanceConfigs` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionInstanceGroups](/compute/docs/reference/rest/v1/regionInstanceGroups)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/regionInstanceGroups/get)` | 

The method `compute.v1.RegionInstanceGroupsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstanceGroups/list)` | 

The method `compute.v1.RegionInstanceGroupsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Instances](/compute/docs/reference/rest/v1/regionInstanceGroups/listInstances)` | 

The method `compute.v1.RegionInstanceGroupsService.ListInstances` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Named Ports](/compute/docs/reference/rest/v1/regionInstanceGroups/setNamedPorts)` | 

The method `compute.v1.RegionInstanceGroupsService.SetNamedPorts` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionInstanceTemplates](/compute/docs/reference/rest/v1/regionInstanceTemplates)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionInstanceTemplates/delete)` | 

The method `compute.v1.RegionInstanceTemplatesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionInstanceTemplates/get)` | 

The method `compute.v1.RegionInstanceTemplatesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionInstanceTemplates/insert)` | 

The method `compute.v1.RegionInstanceTemplatesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstanceTemplates/list)` | 

The method `compute.v1.RegionInstanceTemplatesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionInstances](/compute/docs/reference/rest/v1/regionInstances)









| 
Methods | 
|



| 

`[bulk Insert](/compute/docs/reference/rest/v1/regionInstances/bulkInsert)` | 

The method `compute.v1.RegionInstancesService.BulkInsert` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionInstantSnapshots](/compute/docs/reference/rest/v1/regionInstantSnapshots)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionInstantSnapshots/delete)` | 

The method `compute.v1.RegionInstantSnapshotsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionInstantSnapshots/get)` | 

The method `compute.v1.RegionInstantSnapshotsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/regionInstantSnapshots/getIamPolicy)` | 

The method `compute.v1.RegionInstantSnapshotsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionInstantSnapshots/insert)` | 

The method `compute.v1.RegionInstantSnapshotsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstantSnapshots/list)` | 

The method `compute.v1.RegionInstantSnapshotsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/regionInstantSnapshots/setIamPolicy)` | 

The method `compute.v1.RegionInstantSnapshotsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/regionInstantSnapshots/setLabels)` | 

The method `compute.v1.RegionInstantSnapshotsService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/regionInstantSnapshots/testIamPermissions)` | 

The method `compute.v1.RegionInstantSnapshotsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionNetworkEndpointGroups](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups)









| 
Methods | 
|



| 

`[attach Network Endpoints](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/attachNetworkEndpoints)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.AttachNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/delete)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[detach Network Endpoints](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/detachNetworkEndpoints)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.DetachNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/get)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/insert)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/list)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Network Endpoints](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/listNetworkEndpoints)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.ListNetworkEndpoints` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionNetworkFirewallPolicies](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies)









| 
Methods | 
|



| 

`[add Association](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/addAssociation)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.AddAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[add Rule](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/addRule)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.AddRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[clone Rules](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/cloneRules)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.CloneRules` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/delete)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/get)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Association](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/getAssociation)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.GetAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Effective Firewalls](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/getEffectiveFirewalls)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.GetEffectiveFirewalls` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/getIamPolicy)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Rule](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/getRule)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.GetRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/insert)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/list)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/patch)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch Rule](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/patchRule)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.PatchRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Association](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/removeAssociation)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.RemoveAssociation` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Rule](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/removeRule)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.RemoveRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/setIamPolicy)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/testIamPermissions)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionNotificationEndpoints](/compute/docs/reference/rest/v1/regionNotificationEndpoints)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionNotificationEndpoints/delete)` | 

The method `compute.v1.RegionNotificationEndpointsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionNotificationEndpoints/get)` | 

The method `compute.v1.RegionNotificationEndpointsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionNotificationEndpoints/insert)` | 

The method `compute.v1.RegionNotificationEndpointsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionNotificationEndpoints/list)` | 

The method `compute.v1.RegionNotificationEndpointsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionOperations](/compute/docs/reference/rest/v1/regionOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionOperations/delete)` | 

The method `compute.v1.RegionOperationsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionOperations/get)` | 

The method `compute.v1.RegionOperationsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionOperations/list)` | 

The method `compute.v1.RegionOperationsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[wait](/compute/docs/reference/rest/v1/regionOperations/wait)` | 

The method `compute.v1.RegionOperationsService.Wait` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionSecurityPolicies](/compute/docs/reference/rest/v1/regionSecurityPolicies)









| 
Methods | 
|



| 

`[add Rule](/compute/docs/reference/rest/v1/regionSecurityPolicies/addRule)` | 

The method `compute.v1.RegionSecurityPoliciesService.AddRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionSecurityPolicies/delete)` | 

The method `compute.v1.RegionSecurityPoliciesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionSecurityPolicies/get)` | 

The method `compute.v1.RegionSecurityPoliciesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Rule](/compute/docs/reference/rest/v1/regionSecurityPolicies/getRule)` | 

The method `compute.v1.RegionSecurityPoliciesService.GetRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionSecurityPolicies/insert)` | 

The method `compute.v1.RegionSecurityPoliciesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionSecurityPolicies/list)` | 

The method `compute.v1.RegionSecurityPoliciesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionSecurityPolicies/patch)` | 

The method `compute.v1.RegionSecurityPoliciesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch Rule](/compute/docs/reference/rest/v1/regionSecurityPolicies/patchRule)` | 

The method `compute.v1.RegionSecurityPoliciesService.PatchRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Rule](/compute/docs/reference/rest/v1/regionSecurityPolicies/removeRule)` | 

The method `compute.v1.RegionSecurityPoliciesService.RemoveRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/regionSecurityPolicies/setLabels)` | 

The method `compute.v1.RegionSecurityPoliciesService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionSslCertificates](/compute/docs/reference/rest/v1/regionSslCertificates)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionSslCertificates/delete)` | 

The method `compute.v1.RegionSslCertificatesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionSslCertificates/get)` | 

The method `compute.v1.RegionSslCertificatesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionSslCertificates/insert)` | 

The method `compute.v1.RegionSslCertificatesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionSslCertificates/list)` | 

The method `compute.v1.RegionSslCertificatesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionSslPolicies](/compute/docs/reference/rest/v1/regionSslPolicies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionSslPolicies/delete)` | 

The method `compute.v1.RegionSslPoliciesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionSslPolicies/get)` | 

The method `compute.v1.RegionSslPoliciesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionSslPolicies/insert)` | 

The method `compute.v1.RegionSslPoliciesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionSslPolicies/list)` | 

The method `compute.v1.RegionSslPoliciesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Available Features](/compute/docs/reference/rest/v1/regionSslPolicies/listAvailableFeatures)` | 

The method `compute.v1.RegionSslPoliciesService.ListAvailableFeatures` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionSslPolicies/patch)` | 

The method `compute.v1.RegionSslPoliciesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionTargetHttpProxies](/compute/docs/reference/rest/v1/regionTargetHttpProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionTargetHttpProxies/delete)` | 

The method `compute.v1.RegionTargetHttpProxiesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionTargetHttpProxies/get)` | 

The method `compute.v1.RegionTargetHttpProxiesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionTargetHttpProxies/insert)` | 

The method `compute.v1.RegionTargetHttpProxiesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionTargetHttpProxies/list)` | 

The method `compute.v1.RegionTargetHttpProxiesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Url Map](/compute/docs/reference/rest/v1/regionTargetHttpProxies/setUrlMap)` | 

The method `compute.v1.RegionTargetHttpProxiesService.SetUrlMap` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionTargetHttpsProxies](/compute/docs/reference/rest/v1/regionTargetHttpsProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/delete)` | 

The method `compute.v1.RegionTargetHttpsProxiesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/get)` | 

The method `compute.v1.RegionTargetHttpsProxiesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/insert)` | 

The method `compute.v1.RegionTargetHttpsProxiesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/list)` | 

The method `compute.v1.RegionTargetHttpsProxiesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/patch)` | 

The method `compute.v1.RegionTargetHttpsProxiesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Ssl Certificates](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/setSslCertificates)` | 

The method `compute.v1.RegionTargetHttpsProxiesService.SetSslCertificates` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Url Map](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/setUrlMap)` | 

The method `compute.v1.RegionTargetHttpsProxiesService.SetUrlMap` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionTargetTcpProxies](/compute/docs/reference/rest/v1/regionTargetTcpProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionTargetTcpProxies/delete)` | 

The method `compute.v1.RegionTargetTcpProxiesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionTargetTcpProxies/get)` | 

The method `compute.v1.RegionTargetTcpProxiesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionTargetTcpProxies/insert)` | 

The method `compute.v1.RegionTargetTcpProxiesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionTargetTcpProxies/list)` | 

The method `compute.v1.RegionTargetTcpProxiesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionUrlMaps](/compute/docs/reference/rest/v1/regionUrlMaps)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionUrlMaps/delete)` | 

The method `compute.v1.RegionUrlMapsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionUrlMaps/get)` | 

The method `compute.v1.RegionUrlMapsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionUrlMaps/insert)` | 

The method `compute.v1.RegionUrlMapsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionUrlMaps/list)` | 

The method `compute.v1.RegionUrlMapsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionUrlMaps/patch)` | 

The method `compute.v1.RegionUrlMapsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionUrlMaps/update)` | 

The method `compute.v1.RegionUrlMapsService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[validate](/compute/docs/reference/rest/v1/regionUrlMaps/validate)` | 

The method `compute.v1.RegionUrlMapsService.Validate` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regionZones](/compute/docs/reference/rest/v1/regionZones)









| 
Methods | 
|



| 

`[list](/compute/docs/reference/rest/v1/regionZones/list)` | 

The method `compute.v1.RegionZonesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.regions](/compute/docs/reference/rest/v1/regions)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/regions/get)` | 

The method `compute.v1.RegionsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regions/list)` | 

The method `compute.v1.RegionsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.reservations](/compute/docs/reference/rest/v1/reservations)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/reservations/aggregatedList)` | 

The method `compute.v1.AllocationsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/reservations/delete)` | 

The method `compute.v1.AllocationsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/reservations/get)` | 

The method `compute.v1.AllocationsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/reservations/getIamPolicy)` | 

The method `compute.v1.AllocationsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/reservations/insert)` | 

The method `compute.v1.AllocationsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/reservations/list)` | 

The method `compute.v1.AllocationsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/reservations/resize)` | 

The method `compute.v1.AllocationsService.Resize` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/reservations/setIamPolicy)` | 

The method `compute.v1.AllocationsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/reservations/testIamPermissions)` | 

The method `compute.v1.AllocationsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/reservations/update)` | 

The method `compute.v1.AllocationsService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.resourcePolicies](/compute/docs/reference/rest/v1/resourcePolicies)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/resourcePolicies/aggregatedList)` | 

The method `compute.v1.ResourcePoliciesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/resourcePolicies/delete)` | 

The method `compute.v1.ResourcePoliciesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/resourcePolicies/get)` | 

The method `compute.v1.ResourcePoliciesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/resourcePolicies/getIamPolicy)` | 

The method `compute.v1.ResourcePoliciesService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/resourcePolicies/insert)` | 

The method `compute.v1.ResourcePoliciesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/resourcePolicies/list)` | 

The method `compute.v1.ResourcePoliciesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/resourcePolicies/patch)` | 

The method `compute.v1.ResourcePoliciesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/resourcePolicies/setIamPolicy)` | 

The method `compute.v1.ResourcePoliciesService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/resourcePolicies/testIamPermissions)` | 

The method `compute.v1.ResourcePoliciesService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.routers](/compute/docs/reference/rest/v1/routers)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/routers/aggregatedList)` | 

The method `compute.v1.RegionRoutersService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/routers/delete)` | 

The method `compute.v1.RegionRoutersService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/routers/get)` | 

The method `compute.v1.RegionRoutersService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Nat Ip Info](/compute/docs/reference/rest/v1/routers/getNatIpInfo)` | 

The method `compute.v1.RegionRoutersService.GetNatIpInfo` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Nat Mapping Info](/compute/docs/reference/rest/v1/routers/getNatMappingInfo)` | 

The method `compute.v1.RegionRoutersService.GetNatMappingInfo` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Router Status](/compute/docs/reference/rest/v1/routers/getRouterStatus)` | 

The method `compute.v1.RegionRoutersService.GetRouterStatus` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/routers/insert)` | 

The method `compute.v1.RegionRoutersService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/routers/list)` | 

The method `compute.v1.RegionRoutersService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/routers/patch)` | 

The method `compute.v1.RegionRoutersService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[preview](/compute/docs/reference/rest/v1/routers/preview)` | 

The method `compute.v1.RegionRoutersService.Preview` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/routers/update)` | 

The method `compute.v1.RegionRoutersService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.routes](/compute/docs/reference/rest/v1/routes)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/routes/delete)` | 

The method `compute.v1.RoutesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/routes/get)` | 

The method `compute.v1.RoutesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/routes/insert)` | 

The method `compute.v1.RoutesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/routes/list)` | 

The method `compute.v1.RoutesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.securityPolicies](/compute/docs/reference/rest/v1/securityPolicies)









| 
Methods | 
|



| 

`[add Rule](/compute/docs/reference/rest/v1/securityPolicies/addRule)` | 

The method `compute.v1.SecurityPoliciesService.AddRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/securityPolicies/aggregatedList)` | 

The method `compute.v1.SecurityPoliciesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/securityPolicies/delete)` | 

The method `compute.v1.SecurityPoliciesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/securityPolicies/get)` | 

The method `compute.v1.SecurityPoliciesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Rule](/compute/docs/reference/rest/v1/securityPolicies/getRule)` | 

The method `compute.v1.SecurityPoliciesService.GetRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/securityPolicies/insert)` | 

The method `compute.v1.SecurityPoliciesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/securityPolicies/list)` | 

The method `compute.v1.SecurityPoliciesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Preconfigured Expression Sets](/compute/docs/reference/rest/v1/securityPolicies/listPreconfiguredExpressionSets)` | 

The method `compute.v1.SecurityPoliciesService.ListPreconfiguredExpressionSets` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/securityPolicies/patch)` | 

The method `compute.v1.SecurityPoliciesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch Rule](/compute/docs/reference/rest/v1/securityPolicies/patchRule)` | 

The method `compute.v1.SecurityPoliciesService.PatchRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Rule](/compute/docs/reference/rest/v1/securityPolicies/removeRule)` | 

The method `compute.v1.SecurityPoliciesService.RemoveRule` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/securityPolicies/setLabels)` | 

The method `compute.v1.SecurityPoliciesService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.serviceAttachments](/compute/docs/reference/rest/v1/serviceAttachments)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/serviceAttachments/aggregatedList)` | 

The method `compute.v1.ServiceAttachmentsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/serviceAttachments/delete)` | 

The method `compute.v1.ServiceAttachmentsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/serviceAttachments/get)` | 

The method `compute.v1.ServiceAttachmentsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/serviceAttachments/getIamPolicy)` | 

The method `compute.v1.ServiceAttachmentsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/serviceAttachments/insert)` | 

The method `compute.v1.ServiceAttachmentsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/serviceAttachments/list)` | 

The method `compute.v1.ServiceAttachmentsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/serviceAttachments/patch)` | 

The method `compute.v1.ServiceAttachmentsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/serviceAttachments/setIamPolicy)` | 

The method `compute.v1.ServiceAttachmentsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/serviceAttachments/testIamPermissions)` | 

The method `compute.v1.ServiceAttachmentsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.snapshotSettings](/compute/docs/reference/rest/v1/snapshotSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/snapshotSettings/get)` | 

The method `compute.v1.SnapshotSettingsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/snapshotSettings/patch)` | 

The method `compute.v1.SnapshotSettingsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.snapshots](/compute/docs/reference/rest/v1/snapshots)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/snapshots/delete)` | 

The method `compute.v1.SnapshotsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/snapshots/get)` | 

The method `compute.v1.SnapshotsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/snapshots/getIamPolicy)` | 

The method `compute.v1.SnapshotsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/snapshots/insert)` | 

The method `compute.v1.SnapshotsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/snapshots/list)` | 

The method `compute.v1.SnapshotsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/snapshots/setIamPolicy)` | 

The method `compute.v1.SnapshotsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/snapshots/setLabels)` | 

The method `compute.v1.SnapshotsService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/snapshots/testIamPermissions)` | 

The method `compute.v1.SnapshotsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.sslCertificates](/compute/docs/reference/rest/v1/sslCertificates)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/sslCertificates/aggregatedList)` | 

The method `compute.v1.SslCertificatesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/sslCertificates/delete)` | 

The method `compute.v1.SslCertificatesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/sslCertificates/get)` | 

The method `compute.v1.SslCertificatesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/sslCertificates/insert)` | 

The method `compute.v1.SslCertificatesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/sslCertificates/list)` | 

The method `compute.v1.SslCertificatesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.sslPolicies](/compute/docs/reference/rest/v1/sslPolicies)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/sslPolicies/aggregatedList)` | 

The method `compute.v1.SslPoliciesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/sslPolicies/delete)` | 

The method `compute.v1.SslPoliciesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/sslPolicies/get)` | 

The method `compute.v1.SslPoliciesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/sslPolicies/insert)` | 

The method `compute.v1.SslPoliciesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/sslPolicies/list)` | 

The method `compute.v1.SslPoliciesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Available Features](/compute/docs/reference/rest/v1/sslPolicies/listAvailableFeatures)` | 

The method `compute.v1.SslPoliciesService.ListAvailableFeatures` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/sslPolicies/patch)` | 

The method `compute.v1.SslPoliciesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.storagePoolTypes](/compute/docs/reference/rest/v1/storagePoolTypes)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/storagePoolTypes/aggregatedList)` | 

The method `compute.v1.StoragePoolTypesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/storagePoolTypes/get)` | 

The method `compute.v1.StoragePoolTypesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/storagePoolTypes/list)` | 

The method `compute.v1.StoragePoolTypesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.storagePools](/compute/docs/reference/rest/v1/storagePools)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/storagePools/aggregatedList)` | 

The method `compute.v1.StoragePoolsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/storagePools/delete)` | 

The method `compute.v1.StoragePoolsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/storagePools/get)` | 

The method `compute.v1.StoragePoolsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/storagePools/getIamPolicy)` | 

The method `compute.v1.StoragePoolsService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/storagePools/insert)` | 

The method `compute.v1.StoragePoolsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/storagePools/list)` | 

The method `compute.v1.StoragePoolsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Disks](/compute/docs/reference/rest/v1/storagePools/listDisks)` | 

The method `compute.v1.StoragePoolsService.ListDisks` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/storagePools/setIamPolicy)` | 

The method `compute.v1.StoragePoolsService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/storagePools/testIamPermissions)` | 

The method `compute.v1.StoragePoolsService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/storagePools/update)` | 

The method `compute.v1.StoragePoolsService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.subnetworks](/compute/docs/reference/rest/v1/subnetworks)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/subnetworks/aggregatedList)` | 

The method `compute.v1.SubnetworksService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/subnetworks/delete)` | 

The method `compute.v1.SubnetworksService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[expand Ip Cidr Range](/compute/docs/reference/rest/v1/subnetworks/expandIpCidrRange)` | 

The method `compute.v1.SubnetworksService.ExpandIpCidrRange` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/subnetworks/get)` | 

The method `compute.v1.SubnetworksService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Iam Policy](/compute/docs/reference/rest/v1/subnetworks/getIamPolicy)` | 

The method `compute.v1.SubnetworksService.GetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/subnetworks/insert)` | 

The method `compute.v1.SubnetworksService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/subnetworks/list)` | 

The method `compute.v1.SubnetworksService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list Usable](/compute/docs/reference/rest/v1/subnetworks/listUsable)` | 

The method `compute.v1.SubnetworksService.ListUsable` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/subnetworks/patch)` | 

The method `compute.v1.SubnetworksService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Iam Policy](/compute/docs/reference/rest/v1/subnetworks/setIamPolicy)` | 

The method `compute.v1.SubnetworksService.SetPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Private Ip Google Access](/compute/docs/reference/rest/v1/subnetworks/setPrivateIpGoogleAccess)` | 

The method `compute.v1.SubnetworksService.SetPrivateIpGoogleAccess` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/subnetworks/testIamPermissions)` | 

The method `compute.v1.SubnetworksService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.targetGrpcProxies](/compute/docs/reference/rest/v1/targetGrpcProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/targetGrpcProxies/delete)` | 

The method `compute.v1.TargetGrpcProxiesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetGrpcProxies/get)` | 

The method `compute.v1.TargetGrpcProxiesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetGrpcProxies/insert)` | 

The method `compute.v1.TargetGrpcProxiesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetGrpcProxies/list)` | 

The method `compute.v1.TargetGrpcProxiesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/targetGrpcProxies/patch)` | 

The method `compute.v1.TargetGrpcProxiesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.targetHttpProxies](/compute/docs/reference/rest/v1/targetHttpProxies)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/targetHttpProxies/aggregatedList)` | 

The method `compute.v1.TargetHttpProxiesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetHttpProxies/delete)` | 

The method `compute.v1.TargetHttpProxiesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetHttpProxies/get)` | 

The method `compute.v1.TargetHttpProxiesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetHttpProxies/insert)` | 

The method `compute.v1.TargetHttpProxiesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetHttpProxies/list)` | 

The method `compute.v1.TargetHttpProxiesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/targetHttpProxies/patch)` | 

The method `compute.v1.TargetHttpProxiesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Url Map](/compute/docs/reference/rest/v1/targetHttpProxies/setUrlMap)` | 

The method `compute.v1.TargetHttpProxiesService.SetUrlMap` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.targetHttpsProxies](/compute/docs/reference/rest/v1/targetHttpsProxies)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/targetHttpsProxies/aggregatedList)` | 

The method `compute.v1.TargetHttpsProxiesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetHttpsProxies/delete)` | 

The method `compute.v1.TargetHttpsProxiesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetHttpsProxies/get)` | 

The method `compute.v1.TargetHttpsProxiesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetHttpsProxies/insert)` | 

The method `compute.v1.TargetHttpsProxiesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetHttpsProxies/list)` | 

The method `compute.v1.TargetHttpsProxiesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/targetHttpsProxies/patch)` | 

The method `compute.v1.TargetHttpsProxiesService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Certificate Map](/compute/docs/reference/rest/v1/targetHttpsProxies/setCertificateMap)` | 

The method `compute.v1.TargetHttpsProxiesService.SetCertificateMap` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Quic Override](/compute/docs/reference/rest/v1/targetHttpsProxies/setQuicOverride)` | 

The method `compute.v1.TargetHttpsProxiesService.SetQuicOverride` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Ssl Certificates](/compute/docs/reference/rest/v1/targetHttpsProxies/setSslCertificates)` | 

The method `compute.v1.TargetHttpsProxiesService.SetSslCertificates` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Ssl Policy](/compute/docs/reference/rest/v1/targetHttpsProxies/setSslPolicy)` | 

The method `compute.v1.TargetHttpsProxiesService.SetSslPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Url Map](/compute/docs/reference/rest/v1/targetHttpsProxies/setUrlMap)` | 

The method `compute.v1.TargetHttpsProxiesService.SetUrlMap` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.targetInstances](/compute/docs/reference/rest/v1/targetInstances)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/targetInstances/aggregatedList)` | 

The method `compute.v1.TargetInstancesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetInstances/delete)` | 

The method `compute.v1.TargetInstancesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetInstances/get)` | 

The method `compute.v1.TargetInstancesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetInstances/insert)` | 

The method `compute.v1.TargetInstancesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetInstances/list)` | 

The method `compute.v1.TargetInstancesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Security Policy](/compute/docs/reference/rest/v1/targetInstances/setSecurityPolicy)` | 

The method `compute.v1.TargetInstancesService.SetSecurityPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.targetPools](/compute/docs/reference/rest/v1/targetPools)









| 
Methods | 
|



| 

`[add Health Check](/compute/docs/reference/rest/v1/targetPools/addHealthCheck)` | 

The method `compute.v1.TargetPoolsService.AddHealthCheck` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[add Instance](/compute/docs/reference/rest/v1/targetPools/addInstance)` | 

The method `compute.v1.TargetPoolsService.AddInstance` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[aggregated List](/compute/docs/reference/rest/v1/targetPools/aggregatedList)` | 

The method `compute.v1.TargetPoolsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetPools/delete)` | 

The method `compute.v1.TargetPoolsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetPools/get)` | 

The method `compute.v1.TargetPoolsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Health](/compute/docs/reference/rest/v1/targetPools/getHealth)` | 

The method `compute.v1.TargetPoolsService.GetHealth` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetPools/insert)` | 

The method `compute.v1.TargetPoolsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetPools/list)` | 

The method `compute.v1.TargetPoolsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Health Check](/compute/docs/reference/rest/v1/targetPools/removeHealthCheck)` | 

The method `compute.v1.TargetPoolsService.RemoveHealthCheck` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[remove Instance](/compute/docs/reference/rest/v1/targetPools/removeInstance)` | 

The method `compute.v1.TargetPoolsService.RemoveInstance` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Backup](/compute/docs/reference/rest/v1/targetPools/setBackup)` | 

The method `compute.v1.TargetPoolsService.SetBackup` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Security Policy](/compute/docs/reference/rest/v1/targetPools/setSecurityPolicy)` | 

The method `compute.v1.TargetPoolsService.SetSecurityPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.targetSslProxies](/compute/docs/reference/rest/v1/targetSslProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/targetSslProxies/delete)` | 

The method `compute.v1.TargetSslProxiesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetSslProxies/get)` | 

The method `compute.v1.TargetSslProxiesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetSslProxies/insert)` | 

The method `compute.v1.TargetSslProxiesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetSslProxies/list)` | 

The method `compute.v1.TargetSslProxiesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Backend Service](/compute/docs/reference/rest/v1/targetSslProxies/setBackendService)` | 

The method `compute.v1.TargetSslProxiesService.SetBackendService` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Certificate Map](/compute/docs/reference/rest/v1/targetSslProxies/setCertificateMap)` | 

The method `compute.v1.TargetSslProxiesService.SetCertificateMap` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Proxy Header](/compute/docs/reference/rest/v1/targetSslProxies/setProxyHeader)` | 

The method `compute.v1.TargetSslProxiesService.SetProxyHeader` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Ssl Certificates](/compute/docs/reference/rest/v1/targetSslProxies/setSslCertificates)` | 

The method `compute.v1.TargetSslProxiesService.SetSslCertificates` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Ssl Policy](/compute/docs/reference/rest/v1/targetSslProxies/setSslPolicy)` | 

The method `compute.v1.TargetSslProxiesService.SetSslPolicy` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.targetTcpProxies](/compute/docs/reference/rest/v1/targetTcpProxies)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/targetTcpProxies/aggregatedList)` | 

The method `compute.v1.TargetTcpProxiesService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetTcpProxies/delete)` | 

The method `compute.v1.TargetTcpProxiesService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetTcpProxies/get)` | 

The method `compute.v1.TargetTcpProxiesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetTcpProxies/insert)` | 

The method `compute.v1.TargetTcpProxiesService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetTcpProxies/list)` | 

The method `compute.v1.TargetTcpProxiesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Backend Service](/compute/docs/reference/rest/v1/targetTcpProxies/setBackendService)` | 

The method `compute.v1.TargetTcpProxiesService.SetBackendService` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Proxy Header](/compute/docs/reference/rest/v1/targetTcpProxies/setProxyHeader)` | 

The method `compute.v1.TargetTcpProxiesService.SetProxyHeader` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.targetVpnGateways](/compute/docs/reference/rest/v1/targetVpnGateways)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/targetVpnGateways/aggregatedList)` | 

The method `compute.v1.TargetVpnGatewaysService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetVpnGateways/delete)` | 

The method `compute.v1.TargetVpnGatewaysService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetVpnGateways/get)` | 

The method `compute.v1.TargetVpnGatewaysService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetVpnGateways/insert)` | 

The method `compute.v1.TargetVpnGatewaysService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetVpnGateways/list)` | 

The method `compute.v1.TargetVpnGatewaysService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/targetVpnGateways/setLabels)` | 

The method `compute.v1.TargetVpnGatewaysService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.urlMaps](/compute/docs/reference/rest/v1/urlMaps)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/urlMaps/aggregatedList)` | 

The method `compute.v1.UrlMapsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/urlMaps/delete)` | 

The method `compute.v1.UrlMapsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/urlMaps/get)` | 

The method `compute.v1.UrlMapsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/urlMaps/insert)` | 

The method `compute.v1.UrlMapsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[invalidate Cache](/compute/docs/reference/rest/v1/urlMaps/invalidateCache)` | 

The method `compute.v1.UrlMapsService.InvalidateCache` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/urlMaps/list)` | 

The method `compute.v1.UrlMapsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/urlMaps/patch)` | 

The method `compute.v1.UrlMapsService.Patch` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[update](/compute/docs/reference/rest/v1/urlMaps/update)` | 

The method `compute.v1.UrlMapsService.Update` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[validate](/compute/docs/reference/rest/v1/urlMaps/validate)` | 

The method `compute.v1.UrlMapsService.Validate` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.vpnGateways](/compute/docs/reference/rest/v1/vpnGateways)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/vpnGateways/aggregatedList)` | 

The method `compute.v1.VpnGatewaysService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/vpnGateways/delete)` | 

The method `compute.v1.VpnGatewaysService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/vpnGateways/get)` | 

The method `compute.v1.VpnGatewaysService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get Status](/compute/docs/reference/rest/v1/vpnGateways/getStatus)` | 

The method `compute.v1.VpnGatewaysService.GetStatus` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/vpnGateways/insert)` | 

The method `compute.v1.VpnGatewaysService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/vpnGateways/list)` | 

The method `compute.v1.VpnGatewaysService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/vpnGateways/setLabels)` | 

The method `compute.v1.VpnGatewaysService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[test Iam Permissions](/compute/docs/reference/rest/v1/vpnGateways/testIamPermissions)` | 

The method `compute.v1.VpnGatewaysService.TestPermissions` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.vpnTunnels](/compute/docs/reference/rest/v1/vpnTunnels)









| 
Methods | 
|



| 

`[aggregated List](/compute/docs/reference/rest/v1/vpnTunnels/aggregatedList)` | 

The method `compute.v1.VpnTunnelsService.AggregatedList` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/vpnTunnels/delete)` | 

The method `compute.v1.VpnTunnelsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/vpnTunnels/get)` | 

The method `compute.v1.VpnTunnelsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/vpnTunnels/insert)` | 

The method `compute.v1.VpnTunnelsService.Insert` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/vpnTunnels/list)` | 

The method `compute.v1.VpnTunnelsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[set Labels](/compute/docs/reference/rest/v1/vpnTunnels/setLabels)` | 

The method `compute.v1.VpnTunnelsService.SetLabels` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.zoneOperations](/compute/docs/reference/rest/v1/zoneOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/zoneOperations/delete)` | 

The method `compute.v1.ZoneOperationsService.Delete` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[get](/compute/docs/reference/rest/v1/zoneOperations/get)` | 

The method `compute.v1.ZoneOperationsService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/zoneOperations/list)` | 

The method `compute.v1.ZoneOperationsService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[wait](/compute/docs/reference/rest/v1/zoneOperations/wait)` | 

The method `compute.v1.ZoneOperationsService.Wait` is not available in this (apis-berlin-build0.goog) universe. | 
|






## REST Resource: [v1.zones](/compute/docs/reference/rest/v1/zones)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/zones/get)` | 

The method `compute.v1.ZonesService.Get` is not available in this (apis-berlin-build0.goog) universe. | 
|

| 

`[list](/compute/docs/reference/rest/v1/zones/list)` | 

The method `compute.v1.ZonesService.List` is not available in this (apis-berlin-build0.goog) universe. | 
|