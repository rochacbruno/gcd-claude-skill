# Compute Engine API

Source: https://documentation.s3ns.fr/compute/docs/reference/rest/v1
Last updated: 2026-08-14

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/compute/docs/tpc-differences) for more details.














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

Compute

](https://documentation.s3ns.fr/docs/compute-area)






- 








[

Compute Engine

](https://documentation.s3ns.fr/compute/docs)






- 








[

APIs & Reference

](https://documentation.s3ns.fr/compute/docs/apis)












# Compute Engine API 






- On this page ** 
- [ Service: compute.googleapis.com ](#service:-compute.googleapis.com)

- [ Discovery document ](#discovery-document)
- [ Service endpoint ](#service-endpoint)
- [ Regional service endpoint ](#regional-service-endpoint)

- [ REST Resource: v1.acceleratorTypes ](#rest-resource:-v1.acceleratortypes)
- [ REST Resource: v1.addresses ](#rest-resource:-v1.addresses)
- [ REST Resource: v1.advice ](#rest-resource:-v1.advice)
- [ REST Resource: v1.autoscalers ](#rest-resource:-v1.autoscalers)
- [ REST Resource: v1.backendBuckets ](#rest-resource:-v1.backendbuckets)
- [ REST Resource: v1.backendServices ](#rest-resource:-v1.backendservices)
- [ REST Resource: v1.crossSiteNetworks ](#rest-resource:-v1.crosssitenetworks)
- [ REST Resource: v1.diskTypes ](#rest-resource:-v1.disktypes)
- [ REST Resource: v1.disks ](#rest-resource:-v1.disks)
- [ REST Resource: v1.externalVpnGateways ](#rest-resource:-v1.externalvpngateways)
- [ REST Resource: v1.firewallPolicies ](#rest-resource:-v1.firewallpolicies)
- [ REST Resource: v1.firewalls ](#rest-resource:-v1.firewalls)
- [ REST Resource: v1.forwardingRules ](#rest-resource:-v1.forwardingrules)
- [ REST Resource: v1.futureReservations ](#rest-resource:-v1.futurereservations)
- [ REST Resource: v1.globalAddresses ](#rest-resource:-v1.globaladdresses)
- [ REST Resource: v1.globalForwardingRules ](#rest-resource:-v1.globalforwardingrules)
- [ REST Resource: v1.globalNetworkEndpointGroups ](#rest-resource:-v1.globalnetworkendpointgroups)
- [ REST Resource: v1.globalOperations ](#rest-resource:-v1.globaloperations)
- [ REST Resource: v1.globalOrganizationOperations ](#rest-resource:-v1.globalorganizationoperations)
- [ REST Resource: v1.globalPublicDelegatedPrefixes ](#rest-resource:-v1.globalpublicdelegatedprefixes)
- [ REST Resource: v1.globalVmExtensionPolicies ](#rest-resource:-v1.globalvmextensionpolicies)
- [ REST Resource: v1.healthChecks ](#rest-resource:-v1.healthchecks)
- [ REST Resource: v1.hosts ](#rest-resource:-v1.hosts)
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
- [ REST Resource: v1.instantSnapshotGroups ](#rest-resource:-v1.instantsnapshotgroups)
- [ REST Resource: v1.instantSnapshots ](#rest-resource:-v1.instantsnapshots)
- [ REST Resource: v1.interconnectAttachmentGroups ](#rest-resource:-v1.interconnectattachmentgroups)
- [ REST Resource: v1.interconnectAttachments ](#rest-resource:-v1.interconnectattachments)
- [ REST Resource: v1.interconnectGroups ](#rest-resource:-v1.interconnectgroups)
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
- [ REST Resource: v1.organizationSecurityPolicies ](#rest-resource:-v1.organizationsecuritypolicies)
- [ REST Resource: v1.packetMirrorings ](#rest-resource:-v1.packetmirrorings)
- [ REST Resource: v1.previewFeatures ](#rest-resource:-v1.previewfeatures)
- [ REST Resource: v1.projects ](#rest-resource:-v1.projects)
- [ REST Resource: v1.publicAdvertisedPrefixes ](#rest-resource:-v1.publicadvertisedprefixes)
- [ REST Resource: v1.publicDelegatedPrefixes ](#rest-resource:-v1.publicdelegatedprefixes)
- [ REST Resource: v1.regionAutoscalers ](#rest-resource:-v1.regionautoscalers)
- [ REST Resource: v1.regionBackendBuckets ](#rest-resource:-v1.regionbackendbuckets)
- [ REST Resource: v1.regionBackendServices ](#rest-resource:-v1.regionbackendservices)
- [ REST Resource: v1.regionCommitments ](#rest-resource:-v1.regioncommitments)
- [ REST Resource: v1.regionCompositeHealthChecks ](#rest-resource:-v1.regioncompositehealthchecks)
- [ REST Resource: v1.regionDiskTypes ](#rest-resource:-v1.regiondisktypes)
- [ REST Resource: v1.regionDisks ](#rest-resource:-v1.regiondisks)
- [ REST Resource: v1.regionHealthAggregationPolicies ](#rest-resource:-v1.regionhealthaggregationpolicies)
- [ REST Resource: v1.regionHealthCheckServices ](#rest-resource:-v1.regionhealthcheckservices)
- [ REST Resource: v1.regionHealthChecks ](#rest-resource:-v1.regionhealthchecks)
- [ REST Resource: v1.regionHealthSources ](#rest-resource:-v1.regionhealthsources)
- [ REST Resource: v1.regionInstanceGroupManagerResizeRequests ](#rest-resource:-v1.regioninstancegroupmanagerresizerequests)
- [ REST Resource: v1.regionInstanceGroupManagers ](#rest-resource:-v1.regioninstancegroupmanagers)
- [ REST Resource: v1.regionInstanceGroups ](#rest-resource:-v1.regioninstancegroups)
- [ REST Resource: v1.regionInstanceTemplates ](#rest-resource:-v1.regioninstancetemplates)
- [ REST Resource: v1.regionInstances ](#rest-resource:-v1.regioninstances)
- [ REST Resource: v1.regionInstantSnapshotGroups ](#rest-resource:-v1.regioninstantsnapshotgroups)
- [ REST Resource: v1.regionInstantSnapshots ](#rest-resource:-v1.regioninstantsnapshots)
- [ REST Resource: v1.regionNetworkEndpointGroups ](#rest-resource:-v1.regionnetworkendpointgroups)
- [ REST Resource: v1.regionNetworkFirewallPolicies ](#rest-resource:-v1.regionnetworkfirewallpolicies)
- [ REST Resource: v1.regionNotificationEndpoints ](#rest-resource:-v1.regionnotificationendpoints)
- [ REST Resource: v1.regionOperations ](#rest-resource:-v1.regionoperations)
- [ REST Resource: v1.regionSecurityPolicies ](#rest-resource:-v1.regionsecuritypolicies)
- [ REST Resource: v1.regionSnapshotSettings ](#rest-resource:-v1.regionsnapshotsettings)
- [ REST Resource: v1.regionSnapshots ](#rest-resource:-v1.regionsnapshots)
- [ REST Resource: v1.regionSslCertificates ](#rest-resource:-v1.regionsslcertificates)
- [ REST Resource: v1.regionSslPolicies ](#rest-resource:-v1.regionsslpolicies)
- [ REST Resource: v1.regionTargetHttpProxies ](#rest-resource:-v1.regiontargethttpproxies)
- [ REST Resource: v1.regionTargetHttpsProxies ](#rest-resource:-v1.regiontargethttpsproxies)
- [ REST Resource: v1.regionTargetTcpProxies ](#rest-resource:-v1.regiontargettcpproxies)
- [ REST Resource: v1.regionUrlMaps ](#rest-resource:-v1.regionurlmaps)
- [ REST Resource: v1.regionZones ](#rest-resource:-v1.regionzones)
- [ REST Resource: v1.regions ](#rest-resource:-v1.regions)
- [ REST Resource: v1.reliabilityRisks ](#rest-resource:-v1.reliabilityrisks)
- [ REST Resource: v1.reservationBlocks ](#rest-resource:-v1.reservationblocks)
- [ REST Resource: v1.reservationSlots ](#rest-resource:-v1.reservationslots)
- [ REST Resource: v1.reservationSubBlocks ](#rest-resource:-v1.reservationsubblocks)
- [ REST Resource: v1.reservations ](#rest-resource:-v1.reservations)
- [ REST Resource: v1.resourcePolicies ](#rest-resource:-v1.resourcepolicies)
- [ REST Resource: v1.rolloutPlans ](#rest-resource:-v1.rolloutplans)
- [ REST Resource: v1.rollouts ](#rest-resource:-v1.rollouts)
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
- [ REST Resource: v1.wireGroups ](#rest-resource:-v1.wiregroups)
- [ REST Resource: v1.zoneOperations ](#rest-resource:-v1.zoneoperations)
- [ REST Resource: v1.zoneVmExtensionPolicies ](#rest-resource:-v1.zonevmextensionpolicies)
- [ REST Resource: v1.zones ](#rest-resource:-v1.zones)
- [ REST Resource: beta.acceleratorTypes ](#rest-resource:-beta.acceleratortypes)
- [ REST Resource: beta.addresses ](#rest-resource:-beta.addresses)
- [ REST Resource: beta.advice ](#rest-resource:-beta.advice)
- [ REST Resource: beta.autoscalers ](#rest-resource:-beta.autoscalers)
- [ REST Resource: beta.backendBuckets ](#rest-resource:-beta.backendbuckets)
- [ REST Resource: beta.backendServices ](#rest-resource:-beta.backendservices)
- [ REST Resource: beta.crossSiteNetworks ](#rest-resource:-beta.crosssitenetworks)
- [ REST Resource: beta.diskSettings ](#rest-resource:-beta.disksettings)
- [ REST Resource: beta.diskTypes ](#rest-resource:-beta.disktypes)
- [ REST Resource: beta.disks ](#rest-resource:-beta.disks)
- [ REST Resource: beta.externalVpnGateways ](#rest-resource:-beta.externalvpngateways)
- [ REST Resource: beta.firewallPolicies ](#rest-resource:-beta.firewallpolicies)
- [ REST Resource: beta.firewalls ](#rest-resource:-beta.firewalls)
- [ REST Resource: beta.forwardingRules ](#rest-resource:-beta.forwardingrules)
- [ REST Resource: beta.futureReservations ](#rest-resource:-beta.futurereservations)
- [ REST Resource: beta.globalAddresses ](#rest-resource:-beta.globaladdresses)
- [ REST Resource: beta.globalForwardingRules ](#rest-resource:-beta.globalforwardingrules)
- [ REST Resource: beta.globalNetworkEndpointGroups ](#rest-resource:-beta.globalnetworkendpointgroups)
- [ REST Resource: beta.globalOperations ](#rest-resource:-beta.globaloperations)
- [ REST Resource: beta.globalOrganizationOperations ](#rest-resource:-beta.globalorganizationoperations)
- [ REST Resource: beta.globalPublicDelegatedPrefixes ](#rest-resource:-beta.globalpublicdelegatedprefixes)
- [ REST Resource: beta.globalVmExtensionPolicies ](#rest-resource:-beta.globalvmextensionpolicies)
- [ REST Resource: beta.healthChecks ](#rest-resource:-beta.healthchecks)
- [ REST Resource: beta.hosts ](#rest-resource:-beta.hosts)
- [ REST Resource: beta.httpHealthChecks ](#rest-resource:-beta.httphealthchecks)
- [ REST Resource: beta.httpsHealthChecks ](#rest-resource:-beta.httpshealthchecks)
- [ REST Resource: beta.imageFamilyViews ](#rest-resource:-beta.imagefamilyviews)
- [ REST Resource: beta.imageViews ](#rest-resource:-beta.imageviews)
- [ REST Resource: beta.images ](#rest-resource:-beta.images)
- [ REST Resource: beta.instanceGroupManagerResizeRequests ](#rest-resource:-beta.instancegroupmanagerresizerequests)
- [ REST Resource: beta.instanceGroupManagers ](#rest-resource:-beta.instancegroupmanagers)
- [ REST Resource: beta.instanceGroups ](#rest-resource:-beta.instancegroups)
- [ REST Resource: beta.instanceSettings ](#rest-resource:-beta.instancesettings)
- [ REST Resource: beta.instanceTemplates ](#rest-resource:-beta.instancetemplates)
- [ REST Resource: beta.instances ](#rest-resource:-beta.instances)
- [ REST Resource: beta.instantSnapshotGroups ](#rest-resource:-beta.instantsnapshotgroups)
- [ REST Resource: beta.instantSnapshots ](#rest-resource:-beta.instantsnapshots)
- [ REST Resource: beta.interconnectAttachmentGroups ](#rest-resource:-beta.interconnectattachmentgroups)
- [ REST Resource: beta.interconnectAttachments ](#rest-resource:-beta.interconnectattachments)
- [ REST Resource: beta.interconnectGroups ](#rest-resource:-beta.interconnectgroups)
- [ REST Resource: beta.interconnectLocations ](#rest-resource:-beta.interconnectlocations)
- [ REST Resource: beta.interconnectRemoteLocations ](#rest-resource:-beta.interconnectremotelocations)
- [ REST Resource: beta.interconnects ](#rest-resource:-beta.interconnects)
- [ REST Resource: beta.licenseCodes ](#rest-resource:-beta.licensecodes)
- [ REST Resource: beta.licenses ](#rest-resource:-beta.licenses)
- [ REST Resource: beta.machineImages ](#rest-resource:-beta.machineimages)
- [ REST Resource: beta.machineTypes ](#rest-resource:-beta.machinetypes)
- [ REST Resource: beta.networkAttachments ](#rest-resource:-beta.networkattachments)
- [ REST Resource: beta.networkEdgeSecurityServices ](#rest-resource:-beta.networkedgesecurityservices)
- [ REST Resource: beta.networkEndpointGroups ](#rest-resource:-beta.networkendpointgroups)
- [ REST Resource: beta.networkFirewallPolicies ](#rest-resource:-beta.networkfirewallpolicies)
- [ REST Resource: beta.networkProfiles ](#rest-resource:-beta.networkprofiles)
- [ REST Resource: beta.networks ](#rest-resource:-beta.networks)
- [ REST Resource: beta.nodeGroups ](#rest-resource:-beta.nodegroups)
- [ REST Resource: beta.nodeTemplates ](#rest-resource:-beta.nodetemplates)
- [ REST Resource: beta.nodeTypes ](#rest-resource:-beta.nodetypes)
- [ REST Resource: beta.organizationRolloutPlans ](#rest-resource:-beta.organizationrolloutplans)
- [ REST Resource: beta.organizationRollouts ](#rest-resource:-beta.organizationrollouts)
- [ REST Resource: beta.organizationSecurityPolicies ](#rest-resource:-beta.organizationsecuritypolicies)
- [ REST Resource: beta.packetMirrorings ](#rest-resource:-beta.packetmirrorings)
- [ REST Resource: beta.previewFeatures ](#rest-resource:-beta.previewfeatures)
- [ REST Resource: beta.projectViews ](#rest-resource:-beta.projectviews)
- [ REST Resource: beta.projects ](#rest-resource:-beta.projects)
- [ REST Resource: beta.publicAdvertisedPrefixes ](#rest-resource:-beta.publicadvertisedprefixes)
- [ REST Resource: beta.publicDelegatedPrefixes ](#rest-resource:-beta.publicdelegatedprefixes)
- [ REST Resource: beta.regionAutoscalers ](#rest-resource:-beta.regionautoscalers)
- [ REST Resource: beta.regionBackendBuckets ](#rest-resource:-beta.regionbackendbuckets)
- [ REST Resource: beta.regionBackendServices ](#rest-resource:-beta.regionbackendservices)
- [ REST Resource: beta.regionCommitments ](#rest-resource:-beta.regioncommitments)
- [ REST Resource: beta.regionCompositeHealthChecks ](#rest-resource:-beta.regioncompositehealthchecks)
- [ REST Resource: beta.regionDiskSettings ](#rest-resource:-beta.regiondisksettings)
- [ REST Resource: beta.regionDiskTypes ](#rest-resource:-beta.regiondisktypes)
- [ REST Resource: beta.regionDisks ](#rest-resource:-beta.regiondisks)
- [ REST Resource: beta.regionHealthAggregationPolicies ](#rest-resource:-beta.regionhealthaggregationpolicies)
- [ REST Resource: beta.regionHealthCheckServices ](#rest-resource:-beta.regionhealthcheckservices)
- [ REST Resource: beta.regionHealthChecks ](#rest-resource:-beta.regionhealthchecks)
- [ REST Resource: beta.regionHealthSources ](#rest-resource:-beta.regionhealthsources)
- [ REST Resource: beta.regionInstanceGroupManagerResizeRequests ](#rest-resource:-beta.regioninstancegroupmanagerresizerequests)
- [ REST Resource: beta.regionInstanceGroupManagers ](#rest-resource:-beta.regioninstancegroupmanagers)
- [ REST Resource: beta.regionInstanceGroups ](#rest-resource:-beta.regioninstancegroups)
- [ REST Resource: beta.regionInstanceTemplates ](#rest-resource:-beta.regioninstancetemplates)
- [ REST Resource: beta.regionInstances ](#rest-resource:-beta.regioninstances)
- [ REST Resource: beta.regionInstantSnapshotGroups ](#rest-resource:-beta.regioninstantsnapshotgroups)
- [ REST Resource: beta.regionInstantSnapshots ](#rest-resource:-beta.regioninstantsnapshots)
- [ REST Resource: beta.regionMultiMigMembers ](#rest-resource:-beta.regionmultimigmembers)
- [ REST Resource: beta.regionMultiMigs ](#rest-resource:-beta.regionmultimigs)
- [ REST Resource: beta.regionNetworkEndpointGroups ](#rest-resource:-beta.regionnetworkendpointgroups)
- [ REST Resource: beta.regionNetworkFirewallPolicies ](#rest-resource:-beta.regionnetworkfirewallpolicies)
- [ REST Resource: beta.regionNetworkPolicies ](#rest-resource:-beta.regionnetworkpolicies)
- [ REST Resource: beta.regionNotificationEndpoints ](#rest-resource:-beta.regionnotificationendpoints)
- [ REST Resource: beta.regionOperations ](#rest-resource:-beta.regionoperations)
- [ REST Resource: beta.regionSecurityPolicies ](#rest-resource:-beta.regionsecuritypolicies)
- [ REST Resource: beta.regionSnapshotSettings ](#rest-resource:-beta.regionsnapshotsettings)
- [ REST Resource: beta.regionSnapshots ](#rest-resource:-beta.regionsnapshots)
- [ REST Resource: beta.regionSslCertificates ](#rest-resource:-beta.regionsslcertificates)
- [ REST Resource: beta.regionSslPolicies ](#rest-resource:-beta.regionsslpolicies)
- [ REST Resource: beta.regionTargetHttpProxies ](#rest-resource:-beta.regiontargethttpproxies)
- [ REST Resource: beta.regionTargetHttpsProxies ](#rest-resource:-beta.regiontargethttpsproxies)
- [ REST Resource: beta.regionTargetTcpProxies ](#rest-resource:-beta.regiontargettcpproxies)
- [ REST Resource: beta.regionUrlMaps ](#rest-resource:-beta.regionurlmaps)
- [ REST Resource: beta.regionZones ](#rest-resource:-beta.regionzones)
- [ REST Resource: beta.regions ](#rest-resource:-beta.regions)
- [ REST Resource: beta.reliabilityRisks ](#rest-resource:-beta.reliabilityrisks)
- [ REST Resource: beta.reservationBlocks ](#rest-resource:-beta.reservationblocks)
- [ REST Resource: beta.reservationSlots ](#rest-resource:-beta.reservationslots)
- [ REST Resource: beta.reservationSubBlocks ](#rest-resource:-beta.reservationsubblocks)
- [ REST Resource: beta.reservations ](#rest-resource:-beta.reservations)
- [ REST Resource: beta.resourcePolicies ](#rest-resource:-beta.resourcepolicies)
- [ REST Resource: beta.rolloutPlans ](#rest-resource:-beta.rolloutplans)
- [ REST Resource: beta.rollouts ](#rest-resource:-beta.rollouts)
- [ REST Resource: beta.routers ](#rest-resource:-beta.routers)
- [ REST Resource: beta.routes ](#rest-resource:-beta.routes)
- [ REST Resource: beta.securityPolicies ](#rest-resource:-beta.securitypolicies)
- [ REST Resource: beta.serviceAttachments ](#rest-resource:-beta.serviceattachments)
- [ REST Resource: beta.snapshotGroups ](#rest-resource:-beta.snapshotgroups)
- [ REST Resource: beta.snapshotSettings ](#rest-resource:-beta.snapshotsettings)
- [ REST Resource: beta.snapshots ](#rest-resource:-beta.snapshots)
- [ REST Resource: beta.sslCertificates ](#rest-resource:-beta.sslcertificates)
- [ REST Resource: beta.sslPolicies ](#rest-resource:-beta.sslpolicies)
- [ REST Resource: beta.storagePoolTypes ](#rest-resource:-beta.storagepooltypes)
- [ REST Resource: beta.storagePools ](#rest-resource:-beta.storagepools)
- [ REST Resource: beta.subnetworks ](#rest-resource:-beta.subnetworks)
- [ REST Resource: beta.targetGrpcProxies ](#rest-resource:-beta.targetgrpcproxies)
- [ REST Resource: beta.targetHttpProxies ](#rest-resource:-beta.targethttpproxies)
- [ REST Resource: beta.targetHttpsProxies ](#rest-resource:-beta.targethttpsproxies)
- [ REST Resource: beta.targetInstances ](#rest-resource:-beta.targetinstances)
- [ REST Resource: beta.targetPools ](#rest-resource:-beta.targetpools)
- [ REST Resource: beta.targetSslProxies ](#rest-resource:-beta.targetsslproxies)
- [ REST Resource: beta.targetTcpProxies ](#rest-resource:-beta.targettcpproxies)
- [ REST Resource: beta.targetVpnGateways ](#rest-resource:-beta.targetvpngateways)
- [ REST Resource: beta.urlMaps ](#rest-resource:-beta.urlmaps)
- [ REST Resource: beta.vpnGateways ](#rest-resource:-beta.vpngateways)
- [ REST Resource: beta.vpnTunnels ](#rest-resource:-beta.vpntunnels)
- [ REST Resource: beta.wireGroups ](#rest-resource:-beta.wiregroups)
- [ REST Resource: beta.zoneOperations ](#rest-resource:-beta.zoneoperations)
- [ REST Resource: beta.zoneVmExtensionPolicies ](#rest-resource:-beta.zonevmextensionpolicies)
- [ REST Resource: beta.zones ](#rest-resource:-beta.zones)
- 













Creates and runs virtual machines on Cloud Platform.




- [REST Resource: v1.acceleratorTypes](#v1.acceleratorTypes)

- [REST Resource: v1.addresses](#v1.addresses)

- [REST Resource: v1.advice](#v1.advice)

- [REST Resource: v1.autoscalers](#v1.autoscalers)

- [REST Resource: v1.backendBuckets](#v1.backendBuckets)

- [REST Resource: v1.backendServices](#v1.backendServices)

- [REST Resource: v1.crossSiteNetworks](#v1.crossSiteNetworks)

- [REST Resource: v1.diskTypes](#v1.diskTypes)

- [REST Resource: v1.disks](#v1.disks)

- [REST Resource: v1.externalVpnGateways](#v1.externalVpnGateways)

- [REST Resource: v1.firewallPolicies](#v1.firewallPolicies)

- [REST Resource: v1.firewalls](#v1.firewalls)

- [REST Resource: v1.forwardingRules](#v1.forwardingRules)

- [REST Resource: v1.futureReservations](#v1.futureReservations)

- [REST Resource: v1.globalAddresses](#v1.globalAddresses)

- [REST Resource: v1.globalForwardingRules](#v1.globalForwardingRules)

- [REST Resource: v1.globalNetworkEndpointGroups](#v1.globalNetworkEndpointGroups)

- [REST Resource: v1.globalOperations](#v1.globalOperations)

- [REST Resource: v1.globalOrganizationOperations](#v1.globalOrganizationOperations)

- [REST Resource: v1.globalPublicDelegatedPrefixes](#v1.globalPublicDelegatedPrefixes)

- [REST Resource: v1.globalVmExtensionPolicies](#v1.globalVmExtensionPolicies)

- [REST Resource: v1.healthChecks](#v1.healthChecks)

- [REST Resource: v1.hosts](#v1.hosts)

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

- [REST Resource: v1.instantSnapshotGroups](#v1.instantSnapshotGroups)

- [REST Resource: v1.instantSnapshots](#v1.instantSnapshots)

- [REST Resource: v1.interconnectAttachmentGroups](#v1.interconnectAttachmentGroups)

- [REST Resource: v1.interconnectAttachments](#v1.interconnectAttachments)

- [REST Resource: v1.interconnectGroups](#v1.interconnectGroups)

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

- [REST Resource: v1.organizationSecurityPolicies](#v1.organizationSecurityPolicies)

- [REST Resource: v1.packetMirrorings](#v1.packetMirrorings)

- [REST Resource: v1.previewFeatures](#v1.previewFeatures)

- [REST Resource: v1.projects](#v1.projects)

- [REST Resource: v1.publicAdvertisedPrefixes](#v1.publicAdvertisedPrefixes)

- [REST Resource: v1.publicDelegatedPrefixes](#v1.publicDelegatedPrefixes)

- [REST Resource: v1.regionAutoscalers](#v1.regionAutoscalers)

- [REST Resource: v1.regionBackendBuckets](#v1.regionBackendBuckets)

- [REST Resource: v1.regionBackendServices](#v1.regionBackendServices)

- [REST Resource: v1.regionCommitments](#v1.regionCommitments)

- [REST Resource: v1.regionCompositeHealthChecks](#v1.regionCompositeHealthChecks)

- [REST Resource: v1.regionDiskTypes](#v1.regionDiskTypes)

- [REST Resource: v1.regionDisks](#v1.regionDisks)

- [REST Resource: v1.regionHealthAggregationPolicies](#v1.regionHealthAggregationPolicies)

- [REST Resource: v1.regionHealthCheckServices](#v1.regionHealthCheckServices)

- [REST Resource: v1.regionHealthChecks](#v1.regionHealthChecks)

- [REST Resource: v1.regionHealthSources](#v1.regionHealthSources)

- [REST Resource: v1.regionInstanceGroupManagerResizeRequests](#v1.regionInstanceGroupManagerResizeRequests)

- [REST Resource: v1.regionInstanceGroupManagers](#v1.regionInstanceGroupManagers)

- [REST Resource: v1.regionInstanceGroups](#v1.regionInstanceGroups)

- [REST Resource: v1.regionInstanceTemplates](#v1.regionInstanceTemplates)

- [REST Resource: v1.regionInstances](#v1.regionInstances)

- [REST Resource: v1.regionInstantSnapshotGroups](#v1.regionInstantSnapshotGroups)

- [REST Resource: v1.regionInstantSnapshots](#v1.regionInstantSnapshots)

- [REST Resource: v1.regionNetworkEndpointGroups](#v1.regionNetworkEndpointGroups)

- [REST Resource: v1.regionNetworkFirewallPolicies](#v1.regionNetworkFirewallPolicies)

- [REST Resource: v1.regionNotificationEndpoints](#v1.regionNotificationEndpoints)

- [REST Resource: v1.regionOperations](#v1.regionOperations)

- [REST Resource: v1.regionSecurityPolicies](#v1.regionSecurityPolicies)

- [REST Resource: v1.regionSnapshotSettings](#v1.regionSnapshotSettings)

- [REST Resource: v1.regionSnapshots](#v1.regionSnapshots)

- [REST Resource: v1.regionSslCertificates](#v1.regionSslCertificates)

- [REST Resource: v1.regionSslPolicies](#v1.regionSslPolicies)

- [REST Resource: v1.regionTargetHttpProxies](#v1.regionTargetHttpProxies)

- [REST Resource: v1.regionTargetHttpsProxies](#v1.regionTargetHttpsProxies)

- [REST Resource: v1.regionTargetTcpProxies](#v1.regionTargetTcpProxies)

- [REST Resource: v1.regionUrlMaps](#v1.regionUrlMaps)

- [REST Resource: v1.regionZones](#v1.regionZones)

- [REST Resource: v1.regions](#v1.regions)

- [REST Resource: v1.reliabilityRisks](#v1.reliabilityRisks)

- [REST Resource: v1.reservationBlocks](#v1.reservationBlocks)

- [REST Resource: v1.reservationSlots](#v1.reservationSlots)

- [REST Resource: v1.reservationSubBlocks](#v1.reservationSubBlocks)

- [REST Resource: v1.reservations](#v1.reservations)

- [REST Resource: v1.resourcePolicies](#v1.resourcePolicies)

- [REST Resource: v1.rolloutPlans](#v1.rolloutPlans)

- [REST Resource: v1.rollouts](#v1.rollouts)

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

- [REST Resource: v1.wireGroups](#v1.wireGroups)

- [REST Resource: v1.zoneOperations](#v1.zoneOperations)

- [REST Resource: v1.zoneVmExtensionPolicies](#v1.zoneVmExtensionPolicies)

- [REST Resource: v1.zones](#v1.zones)

- [REST Resource: beta.acceleratorTypes](#beta.acceleratorTypes)

- [REST Resource: beta.addresses](#beta.addresses)

- [REST Resource: beta.advice](#beta.advice)

- [REST Resource: beta.autoscalers](#beta.autoscalers)

- [REST Resource: beta.backendBuckets](#beta.backendBuckets)

- [REST Resource: beta.backendServices](#beta.backendServices)

- [REST Resource: beta.crossSiteNetworks](#beta.crossSiteNetworks)

- [REST Resource: beta.diskSettings](#beta.diskSettings)

- [REST Resource: beta.diskTypes](#beta.diskTypes)

- [REST Resource: beta.disks](#beta.disks)

- [REST Resource: beta.externalVpnGateways](#beta.externalVpnGateways)

- [REST Resource: beta.firewallPolicies](#beta.firewallPolicies)

- [REST Resource: beta.firewalls](#beta.firewalls)

- [REST Resource: beta.forwardingRules](#beta.forwardingRules)

- [REST Resource: beta.futureReservations](#beta.futureReservations)

- [REST Resource: beta.globalAddresses](#beta.globalAddresses)

- [REST Resource: beta.globalForwardingRules](#beta.globalForwardingRules)

- [REST Resource: beta.globalNetworkEndpointGroups](#beta.globalNetworkEndpointGroups)

- [REST Resource: beta.globalOperations](#beta.globalOperations)

- [REST Resource: beta.globalOrganizationOperations](#beta.globalOrganizationOperations)

- [REST Resource: beta.globalPublicDelegatedPrefixes](#beta.globalPublicDelegatedPrefixes)

- [REST Resource: beta.globalVmExtensionPolicies](#beta.globalVmExtensionPolicies)

- [REST Resource: beta.healthChecks](#beta.healthChecks)

- [REST Resource: beta.hosts](#beta.hosts)

- [REST Resource: beta.httpHealthChecks](#beta.httpHealthChecks)

- [REST Resource: beta.httpsHealthChecks](#beta.httpsHealthChecks)

- [REST Resource: beta.imageFamilyViews](#beta.imageFamilyViews)

- [REST Resource: beta.imageViews](#beta.imageViews)

- [REST Resource: beta.images](#beta.images)

- [REST Resource: beta.instanceGroupManagerResizeRequests](#beta.instanceGroupManagerResizeRequests)

- [REST Resource: beta.instanceGroupManagers](#beta.instanceGroupManagers)

- [REST Resource: beta.instanceGroups](#beta.instanceGroups)

- [REST Resource: beta.instanceSettings](#beta.instanceSettings)

- [REST Resource: beta.instanceTemplates](#beta.instanceTemplates)

- [REST Resource: beta.instances](#beta.instances)

- [REST Resource: beta.instantSnapshotGroups](#beta.instantSnapshotGroups)

- [REST Resource: beta.instantSnapshots](#beta.instantSnapshots)

- [REST Resource: beta.interconnectAttachmentGroups](#beta.interconnectAttachmentGroups)

- [REST Resource: beta.interconnectAttachments](#beta.interconnectAttachments)

- [REST Resource: beta.interconnectGroups](#beta.interconnectGroups)

- [REST Resource: beta.interconnectLocations](#beta.interconnectLocations)

- [REST Resource: beta.interconnectRemoteLocations](#beta.interconnectRemoteLocations)

- [REST Resource: beta.interconnects](#beta.interconnects)

- [REST Resource: beta.licenseCodes](#beta.licenseCodes)

- [REST Resource: beta.licenses](#beta.licenses)

- [REST Resource: beta.machineImages](#beta.machineImages)

- [REST Resource: beta.machineTypes](#beta.machineTypes)

- [REST Resource: beta.networkAttachments](#beta.networkAttachments)

- [REST Resource: beta.networkEdgeSecurityServices](#beta.networkEdgeSecurityServices)

- [REST Resource: beta.networkEndpointGroups](#beta.networkEndpointGroups)

- [REST Resource: beta.networkFirewallPolicies](#beta.networkFirewallPolicies)

- [REST Resource: beta.networkProfiles](#beta.networkProfiles)

- [REST Resource: beta.networks](#beta.networks)

- [REST Resource: beta.nodeGroups](#beta.nodeGroups)

- [REST Resource: beta.nodeTemplates](#beta.nodeTemplates)

- [REST Resource: beta.nodeTypes](#beta.nodeTypes)

- [REST Resource: beta.organizationRolloutPlans](#beta.organizationRolloutPlans)

- [REST Resource: beta.organizationRollouts](#beta.organizationRollouts)

- [REST Resource: beta.organizationSecurityPolicies](#beta.organizationSecurityPolicies)

- [REST Resource: beta.packetMirrorings](#beta.packetMirrorings)

- [REST Resource: beta.previewFeatures](#beta.previewFeatures)

- [REST Resource: beta.projectViews](#beta.projectViews)

- [REST Resource: beta.projects](#beta.projects)

- [REST Resource: beta.publicAdvertisedPrefixes](#beta.publicAdvertisedPrefixes)

- [REST Resource: beta.publicDelegatedPrefixes](#beta.publicDelegatedPrefixes)

- [REST Resource: beta.regionAutoscalers](#beta.regionAutoscalers)

- [REST Resource: beta.regionBackendBuckets](#beta.regionBackendBuckets)

- [REST Resource: beta.regionBackendServices](#beta.regionBackendServices)

- [REST Resource: beta.regionCommitments](#beta.regionCommitments)

- [REST Resource: beta.regionCompositeHealthChecks](#beta.regionCompositeHealthChecks)

- [REST Resource: beta.regionDiskSettings](#beta.regionDiskSettings)

- [REST Resource: beta.regionDiskTypes](#beta.regionDiskTypes)

- [REST Resource: beta.regionDisks](#beta.regionDisks)

- [REST Resource: beta.regionHealthAggregationPolicies](#beta.regionHealthAggregationPolicies)

- [REST Resource: beta.regionHealthCheckServices](#beta.regionHealthCheckServices)

- [REST Resource: beta.regionHealthChecks](#beta.regionHealthChecks)

- [REST Resource: beta.regionHealthSources](#beta.regionHealthSources)

- [REST Resource: beta.regionInstanceGroupManagerResizeRequests](#beta.regionInstanceGroupManagerResizeRequests)

- [REST Resource: beta.regionInstanceGroupManagers](#beta.regionInstanceGroupManagers)

- [REST Resource: beta.regionInstanceGroups](#beta.regionInstanceGroups)

- [REST Resource: beta.regionInstanceTemplates](#beta.regionInstanceTemplates)

- [REST Resource: beta.regionInstances](#beta.regionInstances)

- [REST Resource: beta.regionInstantSnapshotGroups](#beta.regionInstantSnapshotGroups)

- [REST Resource: beta.regionInstantSnapshots](#beta.regionInstantSnapshots)

- [REST Resource: beta.regionMultiMigMembers](#beta.regionMultiMigMembers)

- [REST Resource: beta.regionMultiMigs](#beta.regionMultiMigs)

- [REST Resource: beta.regionNetworkEndpointGroups](#beta.regionNetworkEndpointGroups)

- [REST Resource: beta.regionNetworkFirewallPolicies](#beta.regionNetworkFirewallPolicies)

- [REST Resource: beta.regionNetworkPolicies](#beta.regionNetworkPolicies)

- [REST Resource: beta.regionNotificationEndpoints](#beta.regionNotificationEndpoints)

- [REST Resource: beta.regionOperations](#beta.regionOperations)

- [REST Resource: beta.regionSecurityPolicies](#beta.regionSecurityPolicies)

- [REST Resource: beta.regionSnapshotSettings](#beta.regionSnapshotSettings)

- [REST Resource: beta.regionSnapshots](#beta.regionSnapshots)

- [REST Resource: beta.regionSslCertificates](#beta.regionSslCertificates)

- [REST Resource: beta.regionSslPolicies](#beta.regionSslPolicies)

- [REST Resource: beta.regionTargetHttpProxies](#beta.regionTargetHttpProxies)

- [REST Resource: beta.regionTargetHttpsProxies](#beta.regionTargetHttpsProxies)

- [REST Resource: beta.regionTargetTcpProxies](#beta.regionTargetTcpProxies)

- [REST Resource: beta.regionUrlMaps](#beta.regionUrlMaps)

- [REST Resource: beta.regionZones](#beta.regionZones)

- [REST Resource: beta.regions](#beta.regions)

- [REST Resource: beta.reliabilityRisks](#beta.reliabilityRisks)

- [REST Resource: beta.reservationBlocks](#beta.reservationBlocks)

- [REST Resource: beta.reservationSlots](#beta.reservationSlots)

- [REST Resource: beta.reservationSubBlocks](#beta.reservationSubBlocks)

- [REST Resource: beta.reservations](#beta.reservations)

- [REST Resource: beta.resourcePolicies](#beta.resourcePolicies)

- [REST Resource: beta.rolloutPlans](#beta.rolloutPlans)

- [REST Resource: beta.rollouts](#beta.rollouts)

- [REST Resource: beta.routers](#beta.routers)

- [REST Resource: beta.routes](#beta.routes)

- [REST Resource: beta.securityPolicies](#beta.securityPolicies)

- [REST Resource: beta.serviceAttachments](#beta.serviceAttachments)

- [REST Resource: beta.snapshotGroups](#beta.snapshotGroups)

- [REST Resource: beta.snapshotSettings](#beta.snapshotSettings)

- [REST Resource: beta.snapshots](#beta.snapshots)

- [REST Resource: beta.sslCertificates](#beta.sslCertificates)

- [REST Resource: beta.sslPolicies](#beta.sslPolicies)

- [REST Resource: beta.storagePoolTypes](#beta.storagePoolTypes)

- [REST Resource: beta.storagePools](#beta.storagePools)

- [REST Resource: beta.subnetworks](#beta.subnetworks)

- [REST Resource: beta.targetGrpcProxies](#beta.targetGrpcProxies)

- [REST Resource: beta.targetHttpProxies](#beta.targetHttpProxies)

- [REST Resource: beta.targetHttpsProxies](#beta.targetHttpsProxies)

- [REST Resource: beta.targetInstances](#beta.targetInstances)

- [REST Resource: beta.targetPools](#beta.targetPools)

- [REST Resource: beta.targetSslProxies](#beta.targetSslProxies)

- [REST Resource: beta.targetTcpProxies](#beta.targetTcpProxies)

- [REST Resource: beta.targetVpnGateways](#beta.targetVpnGateways)

- [REST Resource: beta.urlMaps](#beta.urlMaps)

- [REST Resource: beta.vpnGateways](#beta.vpnGateways)

- [REST Resource: beta.vpnTunnels](#beta.vpnTunnels)

- [REST Resource: beta.wireGroups](#beta.wireGroups)

- [REST Resource: beta.zoneOperations](#beta.zoneOperations)

- [REST Resource: beta.zoneVmExtensionPolicies](#beta.zoneVmExtensionPolicies)

- [REST Resource: beta.zones](#beta.zones)





## Service: compute. googleapis. com 



To call this service, we recommend that you use the Google-provided [client libraries](https://documentation.s3ns.fr/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.



### Discovery document 



A [Discovery Document](https://s3nsapis.fr/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:




- [https://compute.s3nsapis.fr/$discovery/rest?version=v1](https://compute.s3nsapis.fr/$discovery/rest?version=v1)

- [https://compute.s3nsapis.fr/$discovery/rest?version=beta](https://compute.s3nsapis.fr/$discovery/rest?version=beta)





### Service endpoint



A [service endpoint](https://documentation.s3ns.fr/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:




- `https://compute.s3nsapis.fr`





### Regional service endpoint



A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 
global 

- `https://compute.s3nsapis.fr` 





## REST Resource: [v1. accelerator Types](/compute/docs/reference/rest/v1/acceleratorTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/acceleratorTypes/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/acceleratorTypes` 

Retrieves an aggregated list of accelerator types. | 
|

| 

`[get](/compute/docs/reference/rest/v1/acceleratorTypes/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/acceleratorTypes/{acceleratorType}` 

Returns the specified accelerator type. | 
|

| 

`[list](/compute/docs/reference/rest/v1/acceleratorTypes/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/acceleratorTypes` 

Retrieves a list of accelerator types that are available to the specified project. | 
|






## REST Resource: [v1.addresses](/compute/docs/reference/rest/v1/addresses)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/addresses/aggregatedList)` | 

The method `compute.v1.RegionAddressesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/addresses/delete)` | 

The method `compute.v1.RegionAddressesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/addresses/get)` | 

The method `compute.v1.RegionAddressesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/addresses/insert)` | 

The method `compute.v1.RegionAddressesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/addresses/list)` | 

The method `compute.v1.RegionAddressesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[move](/compute/docs/reference/rest/v1/addresses/move)` | 

The method `compute.v1.RegionAddressesService.Move` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/addresses/setLabels)` | 

The method `compute.v1.RegionAddressesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/addresses/testIamPermissions)` | 

The method `compute.v1.RegionAddressesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.advice](/compute/docs/reference/rest/v1/advice)









| 
Methods | 
|



| 

`[calendarMode](/compute/docs/reference/rest/v1/advice/calendarMode)` | 

The method `compute.v1.AdviceService.CalendarMode` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.autoscalers](/compute/docs/reference/rest/v1/autoscalers)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/autoscalers/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/autoscalers` 

Retrieves an aggregated list of autoscalers. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/autoscalers/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/autoscalers/{autoscaler}` 

Deletes the specified autoscaler. | 
|

| 

`[get](/compute/docs/reference/rest/v1/autoscalers/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/autoscalers/{autoscaler}` 

Returns the specified autoscaler resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/autoscalers/insert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/autoscalers` 

Creates an autoscaler in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/autoscalers/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/autoscalers` 

Retrieves a list of autoscalers contained within the specified zone. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/autoscalers/patch)` | 

`PATCH /compute/v1/projects/{project}/zones/{zone}/autoscalers` 

Updates an autoscaler in the specified project using the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/autoscalers/update)` | 

`PUT /compute/v1/projects/{project}/zones/{zone}/autoscalers` 

Updates an autoscaler in the specified project using the data included in the request. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/autoscalers/testIamPermissions)` | 

The method `compute.v1.AutoscalersService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.backendBuckets](/compute/docs/reference/rest/v1/backendBuckets)









| 
Methods | 
|



| 

`[addSignedUrlKey](/compute/docs/reference/rest/v1/backendBuckets/addSignedUrlKey)` | 

`POST /compute/v1/projects/{project}/global/backendBuckets/{backendBucket}/addSignedUrlKey` 

Adds a key for validating requests with signed URLs for this backend bucket. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/backendBuckets/delete)` | 

`DELETE /compute/v1/projects/{project}/global/backendBuckets/{backendBucket}` 

Deletes the specified BackendBucket resource. | 
|

| 

`[deleteSignedUrlKey](/compute/docs/reference/rest/v1/backendBuckets/deleteSignedUrlKey)` | 

`POST /compute/v1/projects/{project}/global/backendBuckets/{backendBucket}/deleteSignedUrlKey` 

Deletes a key for validating requests with signed URLs for this backend bucket. | 
|

| 

`[get](/compute/docs/reference/rest/v1/backendBuckets/get)` | 

`GET /compute/v1/projects/{project}/global/backendBuckets/{backendBucket}` 

Returns the specified BackendBucket resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/backendBuckets/insert)` | 

`POST /compute/v1/projects/{project}/global/backendBuckets` 

Creates a BackendBucket resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/backendBuckets/list)` | 

`GET /compute/v1/projects/{project}/global/backendBuckets` 

Retrieves the list of BackendBucket resources available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/backendBuckets/patch)` | 

`PATCH /compute/v1/projects/{project}/global/backendBuckets/{backendBucket}` 

Updates the specified BackendBucket resource with the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/backendBuckets/update)` | 

`PUT /compute/v1/projects/{project}/global/backendBuckets/{backendBucket}` 

Updates the specified BackendBucket resource with the data included in the request. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/backendBuckets/aggregatedList)` | 

The method `compute.v1.BackendBucketsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/backendBuckets/getIamPolicy)` | 

The method `compute.v1.BackendBucketsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/v1/backendBuckets/listUsable)` | 

The method `compute.v1.BackendBucketsService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setEdgeSecurityPolicy](/compute/docs/reference/rest/v1/backendBuckets/setEdgeSecurityPolicy)` | 

The method `compute.v1.BackendBucketsService.SetEdgeSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/backendBuckets/setIamPolicy)` | 

The method `compute.v1.BackendBucketsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/backendBuckets/testIamPermissions)` | 

The method `compute.v1.BackendBucketsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.backendServices](/compute/docs/reference/rest/v1/backendServices)









| 
Methods | 
|



| 

`[addSignedUrlKey](/compute/docs/reference/rest/v1/backendServices/addSignedUrlKey)` | 

`POST /compute/v1/projects/{project}/global/backendServices/{backendService}/addSignedUrlKey` 

Adds a key for validating requests with signed URLs for this backend service. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/backendServices/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/backendServices` 

Retrieves the list of all BackendService resources, regional and global, available to the specified project. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/backendServices/delete)` | 

`DELETE /compute/v1/projects/{project}/global/backendServices/{backendService}` 

Deletes the specified BackendService resource. | 
|

| 

`[deleteSignedUrlKey](/compute/docs/reference/rest/v1/backendServices/deleteSignedUrlKey)` | 

`POST /compute/v1/projects/{project}/global/backendServices/{backendService}/deleteSignedUrlKey` 

Deletes a key for validating requests with signed URLs for this backend service. | 
|

| 

`[get](/compute/docs/reference/rest/v1/backendServices/get)` | 

`GET /compute/v1/projects/{project}/global/backendServices/{backendService}` 

Returns the specified BackendService resource. | 
|

| 

`[getHealth](/compute/docs/reference/rest/v1/backendServices/getHealth)` | 

`POST /compute/v1/projects/{project}/global/backendServices/{backendService}/getHealth` 

Gets the most recent health check results for this BackendService. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/backendServices/insert)` | 

`POST /compute/v1/projects/{project}/global/backendServices` 

Creates a BackendService resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/backendServices/list)` | 

`GET /compute/v1/projects/{project}/global/backendServices` 

Retrieves the list of BackendService resources available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/backendServices/patch)` | 

`PATCH /compute/v1/projects/{project}/global/backendServices/{backendService}` 

Patches the specified BackendService resource with the data included in the request. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/v1/backendServices/setSecurityPolicy)` | 

`POST /compute/v1/projects/{project}/global/backendServices/{backendService}/setSecurityPolicy` 

Sets the Cloud de Confiance Armor security policy for the specified backend service. | 
|

| 

`[update](/compute/docs/reference/rest/v1/backendServices/update)` | 

`PUT /compute/v1/projects/{project}/global/backendServices/{backendService}` 

Updates the specified BackendService resource with the data included in the request. | 
|

| 

`[getEffectiveSecurityPolicies](/compute/docs/reference/rest/v1/backendServices/getEffectiveSecurityPolicies)` | 

The method `compute.v1.BackendServicesService.GetEffectiveSecurityPolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/backendServices/getIamPolicy)` | 

The method `compute.v1.BackendServicesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/v1/backendServices/listUsable)` | 

The method `compute.v1.BackendServicesService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setEdgeSecurityPolicy](/compute/docs/reference/rest/v1/backendServices/setEdgeSecurityPolicy)` | 

The method `compute.v1.BackendServicesService.SetEdgeSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/backendServices/setIamPolicy)` | 

The method `compute.v1.BackendServicesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/backendServices/testIamPermissions)` | 

The method `compute.v1.BackendServicesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.crossSiteNetworks](/compute/docs/reference/rest/v1/crossSiteNetworks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/crossSiteNetworks/delete)` | 

The method `compute.v1.CrossSiteNetworksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/crossSiteNetworks/get)` | 

The method `compute.v1.CrossSiteNetworksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/crossSiteNetworks/insert)` | 

The method `compute.v1.CrossSiteNetworksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/crossSiteNetworks/list)` | 

The method `compute.v1.CrossSiteNetworksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/crossSiteNetworks/patch)` | 

The method `compute.v1.CrossSiteNetworksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.diskTypes](/compute/docs/reference/rest/v1/diskTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/diskTypes/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/diskTypes` 

Retrieves an aggregated list of disk types. | 
|

| 

`[get](/compute/docs/reference/rest/v1/diskTypes/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/diskTypes/{diskType}` 

Returns the specified disk type. | 
|

| 

`[list](/compute/docs/reference/rest/v1/diskTypes/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/diskTypes` 

Retrieves a list of disk types available to the specified project. | 
|






## REST Resource: [v1.disks](/compute/docs/reference/rest/v1/disks)









| 
Methods | 
|



| 

`[addResourcePolicies](/compute/docs/reference/rest/v1/disks/addResourcePolicies)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/disks/{disk}/addResourcePolicies` 

Adds existing resource policies to a disk. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/disks/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/disks` 

Retrieves an aggregated list of persistent disks. | 
|

| 

`[createSnapshot](/compute/docs/reference/rest/v1/disks/createSnapshot)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/disks/{disk}/createSnapshot` 

Creates a snapshot of a specified persistent disk. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/disks/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/disks/{disk}` 

Deletes the specified persistent disk. | 
|

| 

`[get](/compute/docs/reference/rest/v1/disks/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/disks/{disk}` 

Returns the specified persistent disk. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/disks/insert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/disks` 

Creates a persistent disk in the specified project using the data in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/disks/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/disks` 

Retrieves a list of persistent disks contained within the specified zone. | 
|

| 

`[removeResourcePolicies](/compute/docs/reference/rest/v1/disks/removeResourcePolicies)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/disks/{disk}/removeResourcePolicies` 

Removes resource policies from a disk. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/disks/resize)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/disks/{disk}/resize` 

Resizes the specified persistent disk. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/disks/setLabels)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/disks/{resource}/setLabels` 

Sets the labels on a disk. | 
|

| 

`[bulkInsert](/compute/docs/reference/rest/v1/disks/bulkInsert)` | 

The method `compute.v1.DisksService.BulkInsert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[bulkSetLabels](/compute/docs/reference/rest/v1/disks/bulkSetLabels)` | 

The method `compute.v1.DisksService.BulkSetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/disks/getIamPolicy)` | 

The method `compute.v1.DisksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/disks/setIamPolicy)` | 

The method `compute.v1.DisksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startAsyncReplication](/compute/docs/reference/rest/v1/disks/startAsyncReplication)` | 

The method `compute.v1.DisksService.StartAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopAsyncReplication](/compute/docs/reference/rest/v1/disks/stopAsyncReplication)` | 

The method `compute.v1.DisksService.StopAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopGroupAsyncReplication](/compute/docs/reference/rest/v1/disks/stopGroupAsyncReplication)` | 

The method `compute.v1.DisksService.StopGroupAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/disks/testIamPermissions)` | 

The method `compute.v1.DisksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/disks/update)` | 

The method `compute.v1.DisksService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateKmsKey](/compute/docs/reference/rest/v1/disks/updateKmsKey)` | 

The method `compute.v1.DisksService.UpdateKmsKey` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.externalVpnGateways](/compute/docs/reference/rest/v1/externalVpnGateways)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/externalVpnGateways/delete)` | 

`DELETE /compute/v1/projects/{project}/global/externalVpnGateways/{externalVpnGateway}` 

Deletes the specified externalVpnGateway. | 
|

| 

`[get](/compute/docs/reference/rest/v1/externalVpnGateways/get)` | 

`GET /compute/v1/projects/{project}/global/externalVpnGateways/{externalVpnGateway}` 

Returns the specified externalVpnGateway. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/externalVpnGateways/insert)` | 

`POST /compute/v1/projects/{project}/global/externalVpnGateways` 

Creates a ExternalVpnGateway in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/externalVpnGateways/list)` | 

`GET /compute/v1/projects/{project}/global/externalVpnGateways` 

Retrieves the list of ExternalVpnGateway available to the specified project. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/externalVpnGateways/setLabels)` | 

`POST /compute/v1/projects/{project}/global/externalVpnGateways/{resource}/setLabels` 

Sets the labels on an ExternalVpnGateway. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/externalVpnGateways/testIamPermissions)` | 

The method `compute.v1.ExternalVpnGatewaysService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.firewallPolicies](/compute/docs/reference/rest/v1/firewallPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/v1/firewallPolicies/addAssociation)` | 

`POST /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/addAssociation` 

Inserts an association for the specified firewall policy. | 
|

| 

`[addRule](/compute/docs/reference/rest/v1/firewallPolicies/addRule)` | 

`POST /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/addRule` 

Inserts a rule into a firewall policy. | 
|

| 

`[cloneRules](/compute/docs/reference/rest/v1/firewallPolicies/cloneRules)` | 

`POST /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/cloneRules` 

Copies rules to the specified firewall policy. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/firewallPolicies/delete)` | 

`DELETE /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}` 

Deletes the specified policy. | 
|

| 

`[get](/compute/docs/reference/rest/v1/firewallPolicies/get)` | 

`GET /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}` 

Returns the specified firewall policy. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/v1/firewallPolicies/getAssociation)` | 

`GET /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/getAssociation` 

Gets an association with the specified name. | 
|

| 

`[getRule](/compute/docs/reference/rest/v1/firewallPolicies/getRule)` | 

`GET /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/getRule` 

Gets a rule of the specified priority. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/firewallPolicies/insert)` | 

`POST /compute/v1/locations/global/firewallPolicies` 

Creates a new policy in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/firewallPolicies/list)` | 

`GET /compute/v1/locations/global/firewallPolicies` 

Lists all the policies that have been configured for the specified folder or organization. | 
|

| 

`[listAssociations](/compute/docs/reference/rest/v1/firewallPolicies/listAssociations)` | 

`GET /compute/v1/locations/global/firewallPolicies/listAssociations` 

Lists associations of a specified target, i.e., organization or folder. | 
|

| 

`[move](/compute/docs/reference/rest/v1/firewallPolicies/move)` | 

`POST /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/move` 

Moves the specified firewall policy. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/firewallPolicies/patch)` | 

`PATCH /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}` 

Patches the specified policy with the data included in the request. | 
|

| 

`[patchRule](/compute/docs/reference/rest/v1/firewallPolicies/patchRule)` | 

`POST /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/patchRule` 

Patches a rule of the specified priority. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/v1/firewallPolicies/removeAssociation)` | 

`POST /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/removeAssociation` 

Removes an association for the specified firewall policy. | 
|

| 

`[removeRule](/compute/docs/reference/rest/v1/firewallPolicies/removeRule)` | 

`POST /compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}/removeRule` 

Deletes a rule of the specified priority. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/firewallPolicies/getIamPolicy)` | 

The method `compute.v1.FirewallPoliciesService.GetOrganizationPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/firewallPolicies/setIamPolicy)` | 

The method `compute.v1.FirewallPoliciesService.SetOrganizationPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/firewallPolicies/testIamPermissions)` | 

The method `compute.v1.FirewallPoliciesService.TestOrganizationPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.firewalls](/compute/docs/reference/rest/v1/firewalls)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/firewalls/delete)` | 

`DELETE /compute/v1/projects/{project}/global/firewalls/{firewall}` 

Deletes the specified firewall. | 
|

| 

`[get](/compute/docs/reference/rest/v1/firewalls/get)` | 

`GET /compute/v1/projects/{project}/global/firewalls/{firewall}` 

Returns the specified firewall. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/firewalls/insert)` | 

`POST /compute/v1/projects/{project}/global/firewalls` 

Creates a firewall rule in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/firewalls/list)` | 

`GET /compute/v1/projects/{project}/global/firewalls` 

Retrieves the list of firewall rules available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/firewalls/patch)` | 

`PATCH /compute/v1/projects/{project}/global/firewalls/{firewall}` 

Updates the specified firewall rule with the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/firewalls/update)` | 

`PUT /compute/v1/projects/{project}/global/firewalls/{firewall}` 

Updates the specified firewall rule with the data included in the request. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/firewalls/testIamPermissions)` | 

The method `compute.v1.FirewallsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.forwardingRules](/compute/docs/reference/rest/v1/forwardingRules)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/forwardingRules/aggregatedList)` | 

The method `compute.v1.RegionForwardingRulesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/forwardingRules/delete)` | 

The method `compute.v1.RegionForwardingRulesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/forwardingRules/get)` | 

The method `compute.v1.RegionForwardingRulesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/forwardingRules/insert)` | 

The method `compute.v1.RegionForwardingRulesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/forwardingRules/list)` | 

The method `compute.v1.RegionForwardingRulesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/forwardingRules/patch)` | 

The method `compute.v1.RegionForwardingRulesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/forwardingRules/setLabels)` | 

The method `compute.v1.RegionForwardingRulesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setTarget](/compute/docs/reference/rest/v1/forwardingRules/setTarget)` | 

The method `compute.v1.RegionForwardingRulesService.SetTarget` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.futureReservations](/compute/docs/reference/rest/v1/futureReservations)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/futureReservations/aggregatedList)` | 

The method `compute.v1.FutureReservationsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cancel](/compute/docs/reference/rest/v1/futureReservations/cancel)` | 

The method `compute.v1.FutureReservationsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/futureReservations/delete)` | 

The method `compute.v1.FutureReservationsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/futureReservations/get)` | 

The method `compute.v1.FutureReservationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/futureReservations/insert)` | 

The method `compute.v1.FutureReservationsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/futureReservations/list)` | 

The method `compute.v1.FutureReservationsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/futureReservations/update)` | 

The method `compute.v1.FutureReservationsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.globalAddresses](/compute/docs/reference/rest/v1/globalAddresses)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/globalAddresses/delete)` | 

`DELETE /compute/v1/projects/{project}/global/addresses/{address}` 

Deletes the specified address resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalAddresses/get)` | 

`GET /compute/v1/projects/{project}/global/addresses/{address}` 

Returns the specified address resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalAddresses/insert)` | 

`POST /compute/v1/projects/{project}/global/addresses` 

Creates an address resource in the specified project by using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalAddresses/list)` | 

`GET /compute/v1/projects/{project}/global/addresses` 

Retrieves a list of global addresses. | 
|

| 

`[move](/compute/docs/reference/rest/v1/globalAddresses/move)` | 

The method `compute.v1.GlobalAddressesService.Move` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/globalAddresses/setLabels)` | 

The method `compute.v1.GlobalAddressesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/globalAddresses/testIamPermissions)` | 

The method `compute.v1.GlobalAddressesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.globalForwardingRules](/compute/docs/reference/rest/v1/globalForwardingRules)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/globalForwardingRules/delete)` | 

`DELETE /compute/v1/projects/{project}/global/forwardingRules/{forwardingRule}` 

Deletes the specified GlobalForwardingRule resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalForwardingRules/get)` | 

`GET /compute/v1/projects/{project}/global/forwardingRules/{forwardingRule}` 

Returns the specified GlobalForwardingRule resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalForwardingRules/insert)` | 

`POST /compute/v1/projects/{project}/global/forwardingRules` 

Creates a GlobalForwardingRule resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalForwardingRules/list)` | 

`GET /compute/v1/projects/{project}/global/forwardingRules` 

Retrieves a list of GlobalForwardingRule resources available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/globalForwardingRules/patch)` | 

`PATCH /compute/v1/projects/{project}/global/forwardingRules/{forwardingRule}` 

Updates the specified forwarding rule with the data included in the request. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/globalForwardingRules/setLabels)` | 

`POST /compute/v1/projects/{project}/global/forwardingRules/{resource}/setLabels` 

Sets the labels on the specified resource. | 
|

| 

`[setTarget](/compute/docs/reference/rest/v1/globalForwardingRules/setTarget)` | 

`POST /compute/v1/projects/{project}/global/forwardingRules/{forwardingRule}/setTarget` 

Changes target URL for the GlobalForwardingRule resource. | 
|






## REST Resource: [v1.globalNetworkEndpointGroups](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups)









| 
Methods | 
|



| 

`[attachNetworkEndpoints](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/attachNetworkEndpoints)` | 

`POST /compute/v1/projects/{project}/global/networkEndpointGroups/{networkEndpointGroup}/attachNetworkEndpoints` 

Attach a network endpoint to the specified network endpoint group. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/delete)` | 

`DELETE /compute/v1/projects/{project}/global/networkEndpointGroups/{networkEndpointGroup}` 

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it. | 
|

| 

`[detachNetworkEndpoints](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/detachNetworkEndpoints)` | 

`POST /compute/v1/projects/{project}/global/networkEndpointGroups/{networkEndpointGroup}/detachNetworkEndpoints` 

Detach the network endpoint from the specified network endpoint group. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/get)` | 

`GET /compute/v1/projects/{project}/global/networkEndpointGroups/{networkEndpointGroup}` 

Returns the specified network endpoint group. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/insert)` | 

`POST /compute/v1/projects/{project}/global/networkEndpointGroups` 

Creates a network endpoint group in the specified project using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/list)` | 

`GET /compute/v1/projects/{project}/global/networkEndpointGroups` 

Retrieves the list of network endpoint groups that are located in the specified project. | 
|

| 

`[listNetworkEndpoints](/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/listNetworkEndpoints)` | 

`POST /compute/v1/projects/{project}/global/networkEndpointGroups/{networkEndpointGroup}/listNetworkEndpoints` 

Lists the network endpoints in the specified network endpoint group. | 
|






## REST Resource: [v1.globalOperations](/compute/docs/reference/rest/v1/globalOperations)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/globalOperations/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/operations` 

Retrieves an aggregated list of all operations. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/globalOperations/delete)` | 

`DELETE /compute/v1/projects/{project}/global/operations/{operation}` 

Deletes the specified Operations resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalOperations/get)` | 

`GET /compute/v1/projects/{project}/global/operations/{operation}` 

Retrieves the specified Operations resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalOperations/list)` | 

`GET /compute/v1/projects/{project}/global/operations` 

Retrieves a list of Operation resources contained within the specified project. | 
|

| 

`[wait](/compute/docs/reference/rest/v1/globalOperations/wait)` | 

`POST /compute/v1/projects/{project}/global/operations/{operation}/wait` 

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. | 
|






## REST Resource: [v1.globalOrganizationOperations](/compute/docs/reference/rest/v1/globalOrganizationOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/globalOrganizationOperations/delete)` | 

`DELETE /compute/v1/locations/global/operations/{operation}` 

Deletes the specified Operations resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalOrganizationOperations/get)` | 

`GET /compute/v1/locations/global/operations/{operation}` 

Retrieves the specified Operations resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalOrganizationOperations/list)` | 

`GET /compute/v1/locations/global/operations` 

Retrieves a list of Operation resources contained within the specified organization. | 
|






## REST Resource: [v1.globalPublicDelegatedPrefixes](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/delete)` | 

`DELETE /compute/v1/projects/{project}/global/publicDelegatedPrefixes/{publicDelegatedPrefix}` 

Deletes the specified global PublicDelegatedPrefix. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/get)` | 

`GET /compute/v1/projects/{project}/global/publicDelegatedPrefixes/{publicDelegatedPrefix}` 

Returns the specified global PublicDelegatedPrefix resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/insert)` | 

`POST /compute/v1/projects/{project}/global/publicDelegatedPrefixes` 

Creates a global PublicDelegatedPrefix in the specified project using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/list)` | 

`GET /compute/v1/projects/{project}/global/publicDelegatedPrefixes` 

Lists the global PublicDelegatedPrefixes for a project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/globalPublicDelegatedPrefixes/patch)` | 

`PATCH /compute/v1/projects/{project}/global/publicDelegatedPrefixes/{publicDelegatedPrefix}` 

Patches the specified global PublicDelegatedPrefix resource with the data included in the request. | 
|






## REST Resource: [v1.globalVmExtensionPolicies](/compute/docs/reference/rest/v1/globalVmExtensionPolicies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/globalVmExtensionPolicies/aggregatedList)` | 

The method `compute.v1.GlobalVmExtensionPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/globalVmExtensionPolicies/delete)` | 

The method `compute.v1.GlobalVmExtensionPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/globalVmExtensionPolicies/get)` | 

The method `compute.v1.GlobalVmExtensionPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/globalVmExtensionPolicies/insert)` | 

The method `compute.v1.GlobalVmExtensionPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/globalVmExtensionPolicies/list)` | 

The method `compute.v1.GlobalVmExtensionPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/globalVmExtensionPolicies/update)` | 

The method `compute.v1.GlobalVmExtensionPoliciesService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.healthChecks](/compute/docs/reference/rest/v1/healthChecks)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/healthChecks/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/healthChecks` 

Retrieves the list of all HealthCheck resources, regional and global, available to the specified project. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/healthChecks/delete)` | 

`DELETE /compute/v1/projects/{project}/global/healthChecks/{healthCheck}` 

Deletes the specified HealthCheck resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/healthChecks/get)` | 

`GET /compute/v1/projects/{project}/global/healthChecks/{healthCheck}` 

Returns the specified HealthCheck resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/healthChecks/insert)` | 

`POST /compute/v1/projects/{project}/global/healthChecks` 

Creates a HealthCheck resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/healthChecks/list)` | 

`GET /compute/v1/projects/{project}/global/healthChecks` 

Retrieves the list of HealthCheck resources available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/healthChecks/patch)` | 

`PATCH /compute/v1/projects/{project}/global/healthChecks/{healthCheck}` 

Updates a HealthCheck resource in the specified project using the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/healthChecks/update)` | 

`PUT /compute/v1/projects/{project}/global/healthChecks/{healthCheck}` 

Updates a HealthCheck resource in the specified project using the data included in the request. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/healthChecks/testIamPermissions)` | 

The method `compute.v1.HealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.hosts](/compute/docs/reference/rest/v1/hosts)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/hosts/get)` | 

The method `compute.v1.HostsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getVersion](/compute/docs/reference/rest/v1/hosts/getVersion)` | 

The method `compute.v1.HostsService.GetVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/hosts/list)` | 

The method `compute.v1.HostsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.httpHealthChecks](/compute/docs/reference/rest/v1/httpHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/httpHealthChecks/delete)` | 

The method `compute.v1.HttpHealthChecksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/httpHealthChecks/get)` | 

The method `compute.v1.HttpHealthChecksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/httpHealthChecks/insert)` | 

The method `compute.v1.HttpHealthChecksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/httpHealthChecks/list)` | 

The method `compute.v1.HttpHealthChecksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/httpHealthChecks/patch)` | 

The method `compute.v1.HttpHealthChecksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/httpHealthChecks/testIamPermissions)` | 

The method `compute.v1.HttpHealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/httpHealthChecks/update)` | 

The method `compute.v1.HttpHealthChecksService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.httpsHealthChecks](/compute/docs/reference/rest/v1/httpsHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/httpsHealthChecks/delete)` | 

The method `compute.v1.HttpsHealthChecksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/httpsHealthChecks/get)` | 

The method `compute.v1.HttpsHealthChecksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/httpsHealthChecks/insert)` | 

The method `compute.v1.HttpsHealthChecksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/httpsHealthChecks/list)` | 

The method `compute.v1.HttpsHealthChecksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/httpsHealthChecks/patch)` | 

The method `compute.v1.HttpsHealthChecksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/httpsHealthChecks/testIamPermissions)` | 

The method `compute.v1.HttpsHealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/httpsHealthChecks/update)` | 

The method `compute.v1.HttpsHealthChecksService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.imageFamilyViews](/compute/docs/reference/rest/v1/imageFamilyViews)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/imageFamilyViews/get)` | 

The method `compute.v1.ImageFamilyViewsService.Get` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.images](/compute/docs/reference/rest/v1/images)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/images/delete)` | 

`DELETE /compute/v1/projects/{project}/global/images/{image}` 

Deletes the specified image. | 
|

| 

`[deprecate](/compute/docs/reference/rest/v1/images/deprecate)` | 

`POST /compute/v1/projects/{project}/global/images/{image}/deprecate` 

Sets the deprecation status of an image. | 
|

| 

`[get](/compute/docs/reference/rest/v1/images/get)` | 

`GET /compute/v1/projects/{project}/global/images/{image}` 

Returns the specified image. | 
|

| 

`[getFromFamily](/compute/docs/reference/rest/v1/images/getFromFamily)` | 

`GET /compute/v1/projects/{project}/global/images/family/{family}` 

Returns the latest image that is part of an image family and is not deprecated. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/images/insert)` | 

`POST /compute/v1/projects/{project}/global/images` 

Creates an image in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/images/list)` | 

`GET /compute/v1/projects/{project}/global/images` 

Retrieves the list of [custom images](/compute/docs/images) available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/images/patch)` | 

`PATCH /compute/v1/projects/{project}/global/images/{image}` 

Patches the specified image with the data included in the request. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/images/setLabels)` | 

`POST /compute/v1/projects/{project}/global/images/{resource}/setLabels` 

Sets the labels on an image. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/images/getIamPolicy)` | 

The method `compute.v1.ImagesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/images/setIamPolicy)` | 

The method `compute.v1.ImagesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/images/testIamPermissions)` | 

The method `compute.v1.ImagesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.instanceGroupManagerResizeRequests](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests)









| 
Methods | 
|



| 

`[cancel](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/cancel)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/delete)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/get)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/list)` | 

The method `compute.v1.InstanceGroupManagerResizeRequestsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.instanceGroupManagers](/compute/docs/reference/rest/v1/instanceGroupManagers)









| 
Methods | 
|



| 

`[abandonInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/abandonInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/abandonInstances` 

Flags the specified instances to be removed from the managed instance group. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/instanceGroupManagers/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/instanceGroupManagers` 

Retrieves the list of managed instance groups and groups them by zone. | 
|

| 

`[applyUpdatesToInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/applyUpdatesToInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/applyUpdatesToInstances` 

Applies changes to selected instances on the managed instance group. | 
|

| 

`[createInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/createInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/createInstances` 

Creates instances with per-instance configurations in this managed instance group. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instanceGroupManagers/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}` 

Deletes the specified managed instance group and all of the instances in that group. | 
|

| 

`[deleteInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/deleteInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/deleteInstances` 

Flags the specified instances in the managed instance group for immediate deletion. | 
|

| 

`[deletePerInstanceConfigs](/compute/docs/reference/rest/v1/instanceGroupManagers/deletePerInstanceConfigs)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/deletePerInstanceConfigs` 

Deletes selected per-instance configurations for the managed instance group. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instanceGroupManagers/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}` 

Returns all of the details about the specified managed instance group. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instanceGroupManagers/insert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers` 

Creates a managed instance group using the information that you specify in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instanceGroupManagers/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers` 

Retrieves a list of managed instance groups that are contained within the specified project and zone. | 
|

| 

`[listErrors](/compute/docs/reference/rest/v1/instanceGroupManagers/listErrors)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/listErrors` 

Lists all errors thrown by actions on instances for a given managed instance group. | 
|

| 

`[listManagedInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/listManagedInstances` 

Lists all of the instances in the managed instance group. | 
|

| 

`[listPerInstanceConfigs](/compute/docs/reference/rest/v1/instanceGroupManagers/listPerInstanceConfigs)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/listPerInstanceConfigs` 

Lists all of the per-instance configurations defined for the managed instance group. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/instanceGroupManagers/patch)` | 

`PATCH /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}` 

Updates a managed instance group using the information that you specify in the request. | 
|

| 

`[patchPerInstanceConfigs](/compute/docs/reference/rest/v1/instanceGroupManagers/patchPerInstanceConfigs)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/patchPerInstanceConfigs` 

Inserts or patches per-instance configurations for the managed instance group. | 
|

| 

`[recreateInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/recreateInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/recreateInstances` 

Flags the specified VM instances in the managed instance group to be immediately recreated. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/instanceGroupManagers/resize)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/resize` 

Resizes the managed instance group. | 
|

| 

`[setInstanceTemplate](/compute/docs/reference/rest/v1/instanceGroupManagers/setInstanceTemplate)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/setInstanceTemplate` 

Specifies the instance template to use when creating new instances in this group. | 
|

| 

`[setTargetPools](/compute/docs/reference/rest/v1/instanceGroupManagers/setTargetPools)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/setTargetPools` 

Modifies the target pools to which all instances in this managed instance group are assigned. | 
|

| 

`[updatePerInstanceConfigs](/compute/docs/reference/rest/v1/instanceGroupManagers/updatePerInstanceConfigs)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/updatePerInstanceConfigs` 

Inserts or updates per-instance configurations for the managed instance group. | 
|

| 

`[resumeInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/resumeInstances)` | 

The method `compute.v1.InstanceGroupManagersService.ResumeInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/startInstances)` | 

The method `compute.v1.InstanceGroupManagersService.StartInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/stopInstances)` | 

The method `compute.v1.InstanceGroupManagersService.StopInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[suspendInstances](/compute/docs/reference/rest/v1/instanceGroupManagers/suspendInstances)` | 

The method `compute.v1.InstanceGroupManagersService.SuspendInstances` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.instanceGroups](/compute/docs/reference/rest/v1/instanceGroups)









| 
Methods | 
|



| 

`[addInstances](/compute/docs/reference/rest/v1/instanceGroups/addInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroups/{instanceGroup}/addInstances` 

Adds a list of instances to the specified instance group. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/instanceGroups/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/instanceGroups` 

Retrieves the list of instance groups and sorts them by zone. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instanceGroups/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/instanceGroups/{instanceGroup}` 

Deletes the specified instance group. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instanceGroups/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instanceGroups/{instanceGroup}` 

Returns the specified zonal instance group. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instanceGroups/insert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroups` 

Creates an instance group in the specified project using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instanceGroups/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instanceGroups` 

Retrieves the list of zonal instance group resources contained within the specified zone. | 
|

| 

`[listInstances](/compute/docs/reference/rest/v1/instanceGroups/listInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroups/{instanceGroup}/listInstances` 

Lists the instances in the specified instance group. | 
|

| 

`[removeInstances](/compute/docs/reference/rest/v1/instanceGroups/removeInstances)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroups/{instanceGroup}/removeInstances` 

Removes one or more instances from the specified instance group, but does not delete those instances. | 
|

| 

`[setNamedPorts](/compute/docs/reference/rest/v1/instanceGroups/setNamedPorts)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instanceGroups/{instanceGroup}/setNamedPorts` 

Sets the named ports for the specified instance group. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/instanceGroups/testIamPermissions)` | 

The method `compute.v1.InstanceGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.instanceSettings](/compute/docs/reference/rest/v1/instanceSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/instanceSettings/get)` | 

The method `compute.v1.InstanceSettingsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/instanceSettings/patch)` | 

The method `compute.v1.InstanceSettingsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.instanceTemplates](/compute/docs/reference/rest/v1/instanceTemplates)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/instanceTemplates/delete)` | 

`DELETE /compute/v1/projects/{project}/global/instanceTemplates/{instanceTemplate}` 

Deletes the specified instance template. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instanceTemplates/get)` | 

`GET /compute/v1/projects/{project}/global/instanceTemplates/{instanceTemplate}` 

Returns the specified instance template. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instanceTemplates/insert)` | 

`POST /compute/v1/projects/{project}/global/instanceTemplates` 

Creates an instance template in the specified project using the data that is included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instanceTemplates/list)` | 

`GET /compute/v1/projects/{project}/global/instanceTemplates` 

Retrieves a list of instance templates that are contained within the specified project. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/instanceTemplates/aggregatedList)` | 

The method `compute.v1.InstanceTemplatesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/instanceTemplates/getIamPolicy)` | 

The method `compute.v1.InstanceTemplatesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/instanceTemplates/setIamPolicy)` | 

The method `compute.v1.InstanceTemplatesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/instanceTemplates/testIamPermissions)` | 

The method `compute.v1.InstanceTemplatesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.instances](/compute/docs/reference/rest/v1/instances)









| 
Methods | 
|



| 

`[addAccessConfig](/compute/docs/reference/rest/v1/instances/addAccessConfig)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/addAccessConfig` 

Adds an access config to an instance's network interface. | 
|

| 

`[addResourcePolicies](/compute/docs/reference/rest/v1/instances/addResourcePolicies)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/addResourcePolicies` 

Adds existing resource policies to an instance. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/instances/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/instances` 

Retrieves an aggregated list of all of the instances in your project across all regions and zones. | 
|

| 

`[attachDisk](/compute/docs/reference/rest/v1/instances/attachDisk)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/attachDisk` 

Attaches an existing Disk resource to an instance. | 
|

| 

`[bulkInsert](/compute/docs/reference/rest/v1/instances/bulkInsert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/bulkInsert` 

Creates multiple instances. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instances/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/instances/{instance}` 

Deletes the specified Instance resource. | 
|

| 

`[deleteAccessConfig](/compute/docs/reference/rest/v1/instances/deleteAccessConfig)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/deleteAccessConfig` 

Deletes an access config from an instance's network interface. | 
|

| 

`[detachDisk](/compute/docs/reference/rest/v1/instances/detachDisk)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/detachDisk` 

Detaches a disk from an instance. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instances/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instances/{instance}` 

Returns the specified Instance resource. | 
|

| 

`[getEffectiveFirewalls](/compute/docs/reference/rest/v1/instances/getEffectiveFirewalls)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/getEffectiveFirewalls` 

Returns effective firewalls applied to an interface of the instance. | 
|

| 

`[getGuestAttributes](/compute/docs/reference/rest/v1/instances/getGuestAttributes)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/getGuestAttributes` 

Returns the specified guest attributes entry. | 
|

| 

`[getScreenshot](/compute/docs/reference/rest/v1/instances/getScreenshot)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/screenshot` 

Returns the screenshot from the specified instance. | 
|

| 

`[getSerialPortOutput](/compute/docs/reference/rest/v1/instances/getSerialPortOutput)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/serialPort` 

Returns the last 1 MB of serial port output from the specified instance. | 
|

| 

`[getShieldedInstanceIdentity](/compute/docs/reference/rest/v1/instances/getShieldedInstanceIdentity)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/getShieldedInstanceIdentity` 

Returns the Shielded Instance Identity of an instance | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instances/insert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances` 

Creates an instance resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instances/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instances` 

Retrieves the list of instances contained within the specified zone. | 
|

| 

`[listReferrers](/compute/docs/reference/rest/v1/instances/listReferrers)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/referrers` 

Retrieves a list of resources that refer to the VM instance specified in the request. | 
|

| 

`[removeResourcePolicies](/compute/docs/reference/rest/v1/instances/removeResourcePolicies)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/removeResourcePolicies` 

Removes resource policies from an instance. | 
|

| 

`[reset](/compute/docs/reference/rest/v1/instances/reset)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/reset` 

Performs a reset on the instance. | 
|

| 

`[setDeletionProtection](/compute/docs/reference/rest/v1/instances/setDeletionProtection)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{resource}/setDeletionProtection` 

Sets deletion protection on the instance. | 
|

| 

`[setDiskAutoDelete](/compute/docs/reference/rest/v1/instances/setDiskAutoDelete)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setDiskAutoDelete` 

Sets the auto-delete flag for a disk attached to an instance. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/instances/setLabels)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setLabels` 

Sets labels on an instance. | 
|

| 

`[setMachineResources](/compute/docs/reference/rest/v1/instances/setMachineResources)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setMachineResources` 

Changes the number and/or type of accelerator for a stopped instance to the values specified in the request. | 
|

| 

`[setMachineType](/compute/docs/reference/rest/v1/instances/setMachineType)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setMachineType` 

Changes the machine type for a stopped instance to the machine type specified in the request. | 
|

| 

`[setMetadata](/compute/docs/reference/rest/v1/instances/setMetadata)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setMetadata` 

Sets metadata for the specified instance to the data included in the request. | 
|

| 

`[setMinCpuPlatform](/compute/docs/reference/rest/v1/instances/setMinCpuPlatform)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setMinCpuPlatform` 

Changes the minimum CPU platform that this instance should use. | 
|

| 

`[setScheduling](/compute/docs/reference/rest/v1/instances/setScheduling)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setScheduling` 

Sets an instance's scheduling options. | 
|

| 

`[setServiceAccount](/compute/docs/reference/rest/v1/instances/setServiceAccount)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setServiceAccount` 

Sets the service account on the instance. | 
|

| 

`[setShieldedInstanceIntegrityPolicy](/compute/docs/reference/rest/v1/instances/setShieldedInstanceIntegrityPolicy)` | 

`PATCH /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setShieldedInstanceIntegrityPolicy` 

Sets the Shielded Instance integrity policy for an instance. | 
|

| 

`[setTags](/compute/docs/reference/rest/v1/instances/setTags)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/setTags` 

Sets [network tags](/vpc/docs/add-remove-network-tags) for the specified instance to the data included in the request. | 
|

| 

`[simulateMaintenanceEvent](/compute/docs/reference/rest/v1/instances/simulateMaintenanceEvent)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/simulateMaintenanceEvent` 

Simulates a host maintenance event on a VM. | 
|

| 

`[start](/compute/docs/reference/rest/v1/instances/start)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/start` 



Starts an instance that was stopped using the [`instances().stop`](/compute/docs/reference/rest/v1/instances/stop) method.
| 
|

| 

`[startWithEncryptionKey](/compute/docs/reference/rest/v1/instances/startWithEncryptionKey)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/startWithEncryptionKey` 



Starts an instance that was stopped using the [`instances().stop`](/compute/docs/reference/rest/v1/instances/stop) method.
| 
|

| 

`[stop](/compute/docs/reference/rest/v1/instances/stop)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/stop` 

Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. | 
|

| 

`[update](/compute/docs/reference/rest/v1/instances/update)` | 

`PUT /compute/v1/projects/{project}/zones/{zone}/instances/{instance}` 

Updates an instance only if the necessary resources are available. | 
|

| 

`[updateAccessConfig](/compute/docs/reference/rest/v1/instances/updateAccessConfig)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/updateAccessConfig` 

Updates the specified access config from an instance's network interface with the data included in the request. | 
|

| 

`[updateDisplayDevice](/compute/docs/reference/rest/v1/instances/updateDisplayDevice)` | 

`PATCH /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/updateDisplayDevice` 

Updates the Display config for a VM instance. | 
|

| 

`[updateNetworkInterface](/compute/docs/reference/rest/v1/instances/updateNetworkInterface)` | 

`PATCH /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/updateNetworkInterface` 

Updates an instance's network interface. | 
|

| 

`[updateShieldedInstanceConfig](/compute/docs/reference/rest/v1/instances/updateShieldedInstanceConfig)` | 

`PATCH /compute/v1/projects/{project}/zones/{zone}/instances/{instance}/updateShieldedInstanceConfig` 

Updates the Shielded Instance config for an instance. | 
|

| 

`[addNetworkInterface](/compute/docs/reference/rest/v1/instances/addNetworkInterface)` | 

The method `compute.v1.InstancesService.AddNetworkInterface` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteNetworkInterface](/compute/docs/reference/rest/v1/instances/deleteNetworkInterface)` | 

The method `compute.v1.InstancesService.DeleteNetworkInterface` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/instances/getIamPolicy)` | 

The method `compute.v1.InstancesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/v1/instances/performMaintenance)` | 

The method `compute.v1.InstancesService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[reportHostAsFaulty](/compute/docs/reference/rest/v1/instances/reportHostAsFaulty)` | 

The method `compute.v1.InstancesService.ReportHostAsFaulty` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resume](/compute/docs/reference/rest/v1/instances/resume)` | 

The method `compute.v1.InstancesService.Resume` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[sendDiagnosticInterrupt](/compute/docs/reference/rest/v1/instances/sendDiagnosticInterrupt)` | 

The method `compute.v1.InstancesService.SendDiagnosticInterrupt` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/instances/setIamPolicy)` | 

The method `compute.v1.InstancesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setName](/compute/docs/reference/rest/v1/instances/setName)` | 

The method `compute.v1.InstancesService.SetName` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/v1/instances/setSecurityPolicy)` | 

The method `compute.v1.InstancesService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[suspend](/compute/docs/reference/rest/v1/instances/suspend)` | 

The method `compute.v1.InstancesService.Suspend` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/instances/testIamPermissions)` | 

The method `compute.v1.InstancesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.instantSnapshotGroups](/compute/docs/reference/rest/v1/instantSnapshotGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/instantSnapshotGroups/delete)` | 

The method `compute.v1.InstantSnapshotGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instantSnapshotGroups/get)` | 

The method `compute.v1.InstantSnapshotGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/instantSnapshotGroups/getIamPolicy)` | 

The method `compute.v1.InstantSnapshotGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instantSnapshotGroups/insert)` | 

The method `compute.v1.InstantSnapshotGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instantSnapshotGroups/list)` | 

The method `compute.v1.InstantSnapshotGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/instantSnapshotGroups/setIamPolicy)` | 

The method `compute.v1.InstantSnapshotGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/instantSnapshotGroups/testIamPermissions)` | 

The method `compute.v1.InstantSnapshotGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.instantSnapshots](/compute/docs/reference/rest/v1/instantSnapshots)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/instantSnapshots/aggregatedList)` | 

The method `compute.v1.InstantSnapshotsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/instantSnapshots/delete)` | 

The method `compute.v1.InstantSnapshotsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/instantSnapshots/get)` | 

The method `compute.v1.InstantSnapshotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/instantSnapshots/getIamPolicy)` | 

The method `compute.v1.InstantSnapshotsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/instantSnapshots/insert)` | 

The method `compute.v1.InstantSnapshotsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/instantSnapshots/list)` | 

The method `compute.v1.InstantSnapshotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/instantSnapshots/setIamPolicy)` | 

The method `compute.v1.InstantSnapshotsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/instantSnapshots/setLabels)` | 

The method `compute.v1.InstantSnapshotsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/instantSnapshots/testIamPermissions)` | 

The method `compute.v1.InstantSnapshotsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.interconnectAttachmentGroups](/compute/docs/reference/rest/v1/interconnectAttachmentGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/delete)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/get)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/getIamPolicy)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getOperationalStatus](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/getOperationalStatus)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.GetOperationalStatus` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/insert)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/list)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/patch)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/setIamPolicy)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/interconnectAttachmentGroups/testIamPermissions)` | 

The method `compute.v1.InterconnectAttachmentGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.interconnectAttachments](/compute/docs/reference/rest/v1/interconnectAttachments)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/interconnectAttachments/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/interconnectAttachments` 

Retrieves an aggregated list of interconnect attachments. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/interconnectAttachments/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/interconnectAttachments/{interconnectAttachment}` 

Deletes the specified interconnect attachment. | 
|

| 

`[get](/compute/docs/reference/rest/v1/interconnectAttachments/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/interconnectAttachments/{interconnectAttachment}` 

Returns the specified interconnect attachment. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/interconnectAttachments/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/interconnectAttachments` 

Creates an InterconnectAttachment in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnectAttachments/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/interconnectAttachments` 

Retrieves the list of interconnect attachments contained within the specified region. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/interconnectAttachments/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/interconnectAttachments/{interconnectAttachment}` 

Updates the specified interconnect attachment with the data included in the request. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/interconnectAttachments/setLabels)` | 

The method `compute.v1.InterconnectAttachmentsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.interconnectGroups](/compute/docs/reference/rest/v1/interconnectGroups)









| 
Methods | 
|



| 

`[createMembers](/compute/docs/reference/rest/v1/interconnectGroups/createMembers)` | 

The method `compute.v1.InterconnectGroupsService.CreateMembers` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/interconnectGroups/delete)` | 

The method `compute.v1.InterconnectGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/interconnectGroups/get)` | 

The method `compute.v1.InterconnectGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/interconnectGroups/getIamPolicy)` | 

The method `compute.v1.InterconnectGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getOperationalStatus](/compute/docs/reference/rest/v1/interconnectGroups/getOperationalStatus)` | 

The method `compute.v1.InterconnectGroupsService.GetOperationalStatus` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/interconnectGroups/insert)` | 

The method `compute.v1.InterconnectGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnectGroups/list)` | 

The method `compute.v1.InterconnectGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/interconnectGroups/patch)` | 

The method `compute.v1.InterconnectGroupsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/interconnectGroups/setIamPolicy)` | 

The method `compute.v1.InterconnectGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/interconnectGroups/testIamPermissions)` | 

The method `compute.v1.InterconnectGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.interconnectLocations](/compute/docs/reference/rest/v1/interconnectLocations)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/interconnectLocations/get)` | 

`GET /compute/v1/projects/{project}/global/interconnectLocations/{interconnectLocation}` 

Returns the details for the specified interconnect location. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnectLocations/list)` | 

`GET /compute/v1/projects/{project}/global/interconnectLocations` 

Retrieves the list of interconnect locations available to the specified project. | 
|






## REST Resource: [v1.interconnectRemoteLocations](/compute/docs/reference/rest/v1/interconnectRemoteLocations)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/interconnectRemoteLocations/get)` | 

The method `compute.v1.InterconnectRemoteLocationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnectRemoteLocations/list)` | 

The method `compute.v1.InterconnectRemoteLocationsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.interconnects](/compute/docs/reference/rest/v1/interconnects)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/interconnects/delete)` | 

`DELETE /compute/v1/projects/{project}/global/interconnects/{interconnect}` 

Deletes the specified Interconnect. | 
|

| 

`[get](/compute/docs/reference/rest/v1/interconnects/get)` | 

`GET /compute/v1/projects/{project}/global/interconnects/{interconnect}` 

Returns the specified Interconnect. | 
|

| 

`[getDiagnostics](/compute/docs/reference/rest/v1/interconnects/getDiagnostics)` | 

`GET /compute/v1/projects/{project}/global/interconnects/{interconnect}/getDiagnostics` 

Returns the `interconnectDiagnostics` for the specified Interconnect. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/interconnects/insert)` | 

`POST /compute/v1/projects/{project}/global/interconnects` 

Creates an Interconnect in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/interconnects/list)` | 

`GET /compute/v1/projects/{project}/global/interconnects` 

Retrieves the list of Interconnects available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/interconnects/patch)` | 

`PATCH /compute/v1/projects/{project}/global/interconnects/{interconnect}` 

Updates the specified Interconnect with the data included in the request. | 
|

| 

`[getMacsecConfig](/compute/docs/reference/rest/v1/interconnects/getMacsecConfig)` | 

The method `compute.v1.InterconnectsService.GetMacsecConfig` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/interconnects/setLabels)` | 

The method `compute.v1.InterconnectsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.licenseCodes](/compute/docs/reference/rest/v1/licenseCodes)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/licenseCodes/get)` | 

`GET /compute/v1/projects/{project}/global/licenseCodes/{licenseCode}` 

Return a specified license code. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/licenseCodes/getIamPolicy)` | 

The method `compute.v1.LicenseCodesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/licenseCodes/setIamPolicy)` | 

The method `compute.v1.LicenseCodesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/licenseCodes/testIamPermissions)` | 

The method `compute.v1.LicenseCodesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.licenses](/compute/docs/reference/rest/v1/licenses)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/licenses/delete)` | 

`DELETE /compute/v1/projects/{project}/global/licenses/{license}` 

Deletes the specified license. | 
|

| 

`[get](/compute/docs/reference/rest/v1/licenses/get)` | 

`GET /compute/v1/projects/{project}/global/licenses/{license}` 

Returns the specified License resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/licenses/insert)` | 

`POST /compute/v1/projects/{project}/global/licenses` 

Create a License resource in the specified project. | 
|

| 

`[list](/compute/docs/reference/rest/v1/licenses/list)` | 

`GET /compute/v1/projects/{project}/global/licenses` 

Retrieves the list of licenses available in the specified project. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/licenses/getIamPolicy)` | 

The method `compute.v1.LicensesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/licenses/setIamPolicy)` | 

The method `compute.v1.LicensesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/licenses/testIamPermissions)` | 

The method `compute.v1.LicensesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/licenses/update)` | 

The method `compute.v1.LicensesService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.machineImages](/compute/docs/reference/rest/v1/machineImages)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/machineImages/delete)` | 

The method `compute.v1.MachineImagesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/machineImages/get)` | 

The method `compute.v1.MachineImagesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/machineImages/getIamPolicy)` | 

The method `compute.v1.MachineImagesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/machineImages/insert)` | 

The method `compute.v1.MachineImagesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/machineImages/list)` | 

The method `compute.v1.MachineImagesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/machineImages/setIamPolicy)` | 

The method `compute.v1.MachineImagesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/machineImages/setLabels)` | 

The method `compute.v1.MachineImagesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/machineImages/testIamPermissions)` | 

The method `compute.v1.MachineImagesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.machineTypes](/compute/docs/reference/rest/v1/machineTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/machineTypes/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/machineTypes` 

Retrieves an aggregated list of machine types. | 
|

| 

`[get](/compute/docs/reference/rest/v1/machineTypes/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/machineTypes/{machineType}` 

Returns the specified machine type. | 
|

| 

`[list](/compute/docs/reference/rest/v1/machineTypes/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/machineTypes` 

Retrieves a list of machine types available to the specified project. | 
|






## REST Resource: [v1.networkAttachments](/compute/docs/reference/rest/v1/networkAttachments)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/networkAttachments/aggregatedList)` | 

The method `compute.v1.NetworkAttachmentsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networkAttachments/delete)` | 

The method `compute.v1.NetworkAttachmentsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networkAttachments/get)` | 

The method `compute.v1.NetworkAttachmentsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/networkAttachments/getIamPolicy)` | 

The method `compute.v1.NetworkAttachmentsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networkAttachments/insert)` | 

The method `compute.v1.NetworkAttachmentsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networkAttachments/list)` | 

The method `compute.v1.NetworkAttachmentsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/networkAttachments/patch)` | 

The method `compute.v1.NetworkAttachmentsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/networkAttachments/setIamPolicy)` | 

The method `compute.v1.NetworkAttachmentsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/networkAttachments/testIamPermissions)` | 

The method `compute.v1.NetworkAttachmentsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.networkEdgeSecurityServices](/compute/docs/reference/rest/v1/networkEdgeSecurityServices)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/aggregatedList)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/delete)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/get)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/insert)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/networkEdgeSecurityServices/patch)` | 

The method `compute.v1.NetworkEdgeSecurityServicesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.networkEndpointGroups](/compute/docs/reference/rest/v1/networkEndpointGroups)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/networkEndpointGroups/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/networkEndpointGroups` 

Retrieves the list of network endpoint groups and sorts them by zone. | 
|

| 

`[attachNetworkEndpoints](/compute/docs/reference/rest/v1/networkEndpointGroups/attachNetworkEndpoints)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}/attachNetworkEndpoints` 

Attach a list of network endpoints to the specified network endpoint group. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networkEndpointGroups/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}` 

Deletes the specified network endpoint group. | 
|

| 

`[detachNetworkEndpoints](/compute/docs/reference/rest/v1/networkEndpointGroups/detachNetworkEndpoints)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}/detachNetworkEndpoints` 

Detach a list of network endpoints from the specified network endpoint group. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networkEndpointGroups/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}` 

Returns the specified network endpoint group. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networkEndpointGroups/insert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/networkEndpointGroups` 

Creates a network endpoint group in the specified project using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networkEndpointGroups/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/networkEndpointGroups` 

Retrieves the list of network endpoint groups that are located in the specified project and zone. | 
|

| 

`[listNetworkEndpoints](/compute/docs/reference/rest/v1/networkEndpointGroups/listNetworkEndpoints)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}/listNetworkEndpoints` 

Lists the network endpoints in the specified network endpoint group. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/networkEndpointGroups/testIamPermissions)` | 

The method `compute.v1.NetworkEndpointGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.networkFirewallPolicies](/compute/docs/reference/rest/v1/networkFirewallPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/v1/networkFirewallPolicies/addAssociation)` | 

The method `compute.v1.NetworkFirewallPoliciesService.AddAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addPacketMirroringRule](/compute/docs/reference/rest/v1/networkFirewallPolicies/addPacketMirroringRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.AddPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addRule](/compute/docs/reference/rest/v1/networkFirewallPolicies/addRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/networkFirewallPolicies/aggregatedList)` | 

The method `compute.v1.NetworkFirewallPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cloneRules](/compute/docs/reference/rest/v1/networkFirewallPolicies/cloneRules)` | 

The method `compute.v1.NetworkFirewallPoliciesService.CloneRules` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networkFirewallPolicies/delete)` | 

The method `compute.v1.NetworkFirewallPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networkFirewallPolicies/get)` | 

The method `compute.v1.NetworkFirewallPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/v1/networkFirewallPolicies/getAssociation)` | 

The method `compute.v1.NetworkFirewallPoliciesService.GetAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/networkFirewallPolicies/getIamPolicy)` | 

The method `compute.v1.NetworkFirewallPoliciesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getPacketMirroringRule](/compute/docs/reference/rest/v1/networkFirewallPolicies/getPacketMirroringRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.GetPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/v1/networkFirewallPolicies/getRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networkFirewallPolicies/insert)` | 

The method `compute.v1.NetworkFirewallPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networkFirewallPolicies/list)` | 

The method `compute.v1.NetworkFirewallPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/networkFirewallPolicies/patch)` | 

The method `compute.v1.NetworkFirewallPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchPacketMirroringRule](/compute/docs/reference/rest/v1/networkFirewallPolicies/patchPacketMirroringRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.PatchPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/v1/networkFirewallPolicies/patchRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/v1/networkFirewallPolicies/removeAssociation)` | 

The method `compute.v1.NetworkFirewallPoliciesService.RemoveAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removePacketMirroringRule](/compute/docs/reference/rest/v1/networkFirewallPolicies/removePacketMirroringRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.RemovePacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/v1/networkFirewallPolicies/removeRule)` | 

The method `compute.v1.NetworkFirewallPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/networkFirewallPolicies/setIamPolicy)` | 

The method `compute.v1.NetworkFirewallPoliciesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/networkFirewallPolicies/testIamPermissions)` | 

The method `compute.v1.NetworkFirewallPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.networkProfiles](/compute/docs/reference/rest/v1/networkProfiles)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/networkProfiles/get)` | 

The method `compute.v1.NetworkProfilesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networkProfiles/list)` | 

The method `compute.v1.NetworkProfilesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.networks](/compute/docs/reference/rest/v1/networks)









| 
Methods | 
|



| 

`[addPeering](/compute/docs/reference/rest/v1/networks/addPeering)` | 

`POST /compute/v1/projects/{project}/global/networks/{network}/addPeering` 

Adds a peering to the specified network. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/networks/delete)` | 

`DELETE /compute/v1/projects/{project}/global/networks/{network}` 

Deletes the specified network. | 
|

| 

`[get](/compute/docs/reference/rest/v1/networks/get)` | 

`GET /compute/v1/projects/{project}/global/networks/{network}` 

Returns the specified network. | 
|

| 

`[getEffectiveFirewalls](/compute/docs/reference/rest/v1/networks/getEffectiveFirewalls)` | 

`GET /compute/v1/projects/{project}/global/networks/{network}/getEffectiveFirewalls` 

Returns the effective firewalls on a given network. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/networks/insert)` | 

`POST /compute/v1/projects/{project}/global/networks` 

Creates a network in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/networks/list)` | 

`GET /compute/v1/projects/{project}/global/networks` 

Retrieves the list of networks available to the specified project. | 
|

| 

`[listPeeringRoutes](/compute/docs/reference/rest/v1/networks/listPeeringRoutes)` | 

`GET /compute/v1/projects/{project}/global/networks/{network}/listPeeringRoutes` 

Lists the peering routes exchanged over peering connection. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/networks/patch)` | 

`PATCH /compute/v1/projects/{project}/global/networks/{network}` 

Patches the specified network with the data included in the request. | 
|

| 

`[removePeering](/compute/docs/reference/rest/v1/networks/removePeering)` | 

`POST /compute/v1/projects/{project}/global/networks/{network}/removePeering` 

Removes a peering from the specified network. | 
|

| 

`[switchToCustomMode](/compute/docs/reference/rest/v1/networks/switchToCustomMode)` | 

`POST /compute/v1/projects/{project}/global/networks/{network}/switchToCustomMode` 

Switches the network mode from auto subnet mode to custom subnet mode. | 
|

| 

`[updatePeering](/compute/docs/reference/rest/v1/networks/updatePeering)` | 

`PATCH /compute/v1/projects/{project}/global/networks/{network}/updatePeering` 

Updates the specified network peering with the data included in the request. | 
|

| 

`[cancelRequestRemovePeering](/compute/docs/reference/rest/v1/networks/cancelRequestRemovePeering)` | 

The method `compute.v1.NetworksService.CancelRequestRemovePeering` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[requestRemovePeering](/compute/docs/reference/rest/v1/networks/requestRemovePeering)` | 

The method `compute.v1.NetworksService.RequestRemovePeering` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.nodeGroups](/compute/docs/reference/rest/v1/nodeGroups)









| 
Methods | 
|



| 

`[addNodes](/compute/docs/reference/rest/v1/nodeGroups/addNodes)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/nodeGroups/{nodeGroup}/addNodes` 

Adds specified number of nodes to the node group. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/nodeGroups/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/nodeGroups` 

Retrieves an aggregated list of node groups. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/nodeGroups/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/nodeGroups/{nodeGroup}` 

Deletes the specified NodeGroup resource. | 
|

| 

`[deleteNodes](/compute/docs/reference/rest/v1/nodeGroups/deleteNodes)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/nodeGroups/{nodeGroup}/deleteNodes` 

Deletes specified nodes from the node group. | 
|

| 

`[get](/compute/docs/reference/rest/v1/nodeGroups/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/nodeGroups/{nodeGroup}` 

Returns the specified NodeGroup. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/nodeGroups/insert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/nodeGroups` 

Creates a NodeGroup resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/nodeGroups/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/nodeGroups` 

Retrieves a list of node groups available to the specified project. | 
|

| 

`[listNodes](/compute/docs/reference/rest/v1/nodeGroups/listNodes)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/nodeGroups/{nodeGroup}/listNodes` 

Lists nodes in the node group. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/nodeGroups/patch)` | 

`PATCH /compute/v1/projects/{project}/zones/{zone}/nodeGroups/{nodeGroup}` 

Updates the specified node group. | 
|

| 

`[setNodeTemplate](/compute/docs/reference/rest/v1/nodeGroups/setNodeTemplate)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/nodeGroups/{nodeGroup}/setNodeTemplate` 

Updates the node template of the node group. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/nodeGroups/getIamPolicy)` | 

The method `compute.v1.NodeGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/v1/nodeGroups/performMaintenance)` | 

The method `compute.v1.NodeGroupsService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/nodeGroups/setIamPolicy)` | 

The method `compute.v1.NodeGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[simulateMaintenanceEvent](/compute/docs/reference/rest/v1/nodeGroups/simulateMaintenanceEvent)` | 

The method `compute.v1.NodeGroupsService.SimulateMaintenanceEvent` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/nodeGroups/testIamPermissions)` | 

The method `compute.v1.NodeGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.nodeTemplates](/compute/docs/reference/rest/v1/nodeTemplates)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/nodeTemplates/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/nodeTemplates` 

Retrieves an aggregated list of node templates. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/nodeTemplates/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/nodeTemplates/{nodeTemplate}` 

Deletes the specified NodeTemplate resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/nodeTemplates/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/nodeTemplates/{nodeTemplate}` 

Returns the specified node template. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/nodeTemplates/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/nodeTemplates` 

Creates a NodeTemplate resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/nodeTemplates/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/nodeTemplates` 

Retrieves a list of node templates available to the specified project. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/nodeTemplates/getIamPolicy)` | 

The method `compute.v1.NodeTemplatesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/nodeTemplates/setIamPolicy)` | 

The method `compute.v1.NodeTemplatesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/nodeTemplates/testIamPermissions)` | 

The method `compute.v1.NodeTemplatesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.nodeTypes](/compute/docs/reference/rest/v1/nodeTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/nodeTypes/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/nodeTypes` 

Retrieves an aggregated list of node types. | 
|

| 

`[get](/compute/docs/reference/rest/v1/nodeTypes/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/nodeTypes/{nodeType}` 

Returns the specified node type. | 
|

| 

`[list](/compute/docs/reference/rest/v1/nodeTypes/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/nodeTypes` 

Retrieves a list of node types available to the specified project. | 
|






## REST Resource: [v1.organizationSecurityPolicies](/compute/docs/reference/rest/v1/organizationSecurityPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/v1/organizationSecurityPolicies/addAssociation)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.AddAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addRule](/compute/docs/reference/rest/v1/organizationSecurityPolicies/addRule)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[copyRules](/compute/docs/reference/rest/v1/organizationSecurityPolicies/copyRules)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.CopyRules` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/organizationSecurityPolicies/delete)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/organizationSecurityPolicies/get)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/v1/organizationSecurityPolicies/getAssociation)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.GetAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/v1/organizationSecurityPolicies/getRule)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/organizationSecurityPolicies/insert)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/organizationSecurityPolicies/list)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listAssociations](/compute/docs/reference/rest/v1/organizationSecurityPolicies/listAssociations)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.ListAssociations` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listPreconfiguredExpressionSets](/compute/docs/reference/rest/v1/organizationSecurityPolicies/listPreconfiguredExpressionSets)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.ListPreconfiguredExpressionSets` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[move](/compute/docs/reference/rest/v1/organizationSecurityPolicies/move)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.Move` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/organizationSecurityPolicies/patch)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/v1/organizationSecurityPolicies/patchRule)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/v1/organizationSecurityPolicies/removeAssociation)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.RemoveAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/v1/organizationSecurityPolicies/removeRule)` | 

The method `compute.v1.OrganizationSecurityPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.packetMirrorings](/compute/docs/reference/rest/v1/packetMirrorings)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/packetMirrorings/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/packetMirrorings` 

Retrieves an aggregated list of packetMirrorings. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/packetMirrorings/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/packetMirrorings/{packetMirroring}` 

Deletes the specified PacketMirroring resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/packetMirrorings/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/packetMirrorings/{packetMirroring}` 

Returns the specified PacketMirroring resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/packetMirrorings/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/packetMirrorings` 

Creates a PacketMirroring resource in the specified project and region using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/packetMirrorings/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/packetMirrorings` 

Retrieves a list of PacketMirroring resources available to the specified project and region. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/packetMirrorings/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/packetMirrorings/{packetMirroring}` 

Patches the specified PacketMirroring resource with the data included in the request. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/packetMirrorings/testIamPermissions)` | 

The method `compute.v1.PacketMirroringsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.previewFeatures](/compute/docs/reference/rest/v1/previewFeatures)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/previewFeatures/get)` | 

The method `compute.v1.PreviewFeaturesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/previewFeatures/list)` | 

The method `compute.v1.PreviewFeaturesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/previewFeatures/update)` | 

The method `compute.v1.PreviewFeaturesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.projects](/compute/docs/reference/rest/v1/projects)









| 
Methods | 
|



| 

`[disableXpnHost](/compute/docs/reference/rest/v1/projects/disableXpnHost)` | 

`POST /compute/v1/projects/{project}/disableXpnHost` 

Disable this project as a shared VPC host project. | 
|

| 

`[disableXpnResource](/compute/docs/reference/rest/v1/projects/disableXpnResource)` | 

`POST /compute/v1/projects/{project}/disableXpnResource` 

Disable a service resource (also known as service project) associated with this host project. | 
|

| 

`[enableXpnHost](/compute/docs/reference/rest/v1/projects/enableXpnHost)` | 

`POST /compute/v1/projects/{project}/enableXpnHost` 

Enable this project as a shared VPC host project. | 
|

| 

`[enableXpnResource](/compute/docs/reference/rest/v1/projects/enableXpnResource)` | 

`POST /compute/v1/projects/{project}/enableXpnResource` 

Enable service resource (a.k.a service project) for a host project, so that subnets in the host project can be used by instances in the service project. | 
|

| 

`[get](/compute/docs/reference/rest/v1/projects/get)` | 

`GET /compute/v1/projects/{project}` 

Returns the specified Project resource. | 
|

| 

`[getXpnHost](/compute/docs/reference/rest/v1/projects/getXpnHost)` | 

`GET /compute/v1/projects/{project}/getXpnHost` 

Gets the shared VPC host project that this project links to. | 
|

| 

`[getXpnResources](/compute/docs/reference/rest/v1/projects/getXpnResources)` | 

`GET /compute/v1/projects/{project}/getXpnResources` 

Gets service resources (a.k.a service project) associated with this host project. | 
|

| 

`[listXpnHosts](/compute/docs/reference/rest/v1/projects/listXpnHosts)` | 

`POST /compute/v1/projects/{project}/listXpnHosts` 

Lists all shared VPC host projects visible to the user in an organization. | 
|

| 

`[moveDisk](/compute/docs/reference/rest/v1/projects/moveDisk) 
(deprecated)**` | 

`POST /compute/v1/projects/{project}/moveDisk` 

Moves a persistent disk from one zone to another. | 
|

| 

`[moveInstance](/compute/docs/reference/rest/v1/projects/moveInstance) 
**(deprecated)**` | 

`POST /compute/v1/projects/{project}/moveInstance` 

Moves an instance and its attached persistent disks from one zone to another. | 
|

| 

`[setCommonInstanceMetadata](/compute/docs/reference/rest/v1/projects/setCommonInstanceMetadata)` | 

`POST /compute/v1/projects/{project}/setCommonInstanceMetadata` 

Sets metadata common to all instances within the specified project using the data included in the request. | 
|

| 

`[setDefaultNetworkTier](/compute/docs/reference/rest/v1/projects/setDefaultNetworkTier)` | 

`POST /compute/v1/projects/{project}/setDefaultNetworkTier` 

Sets the default network tier of the project. | 
|

| 

`[setUsageExportBucket](/compute/docs/reference/rest/v1/projects/setUsageExportBucket)` | 

`POST /compute/v1/projects/{project}/setUsageExportBucket` 

Enables the usage export feature and sets the [usage export bucket](/compute/docs/usage-export) where reports are stored. | 
|

| 

`[setCloudArmorTier](/compute/docs/reference/rest/v1/projects/setCloudArmorTier)` | 

The method `compute.v1.ProjectsService.SetCloudArmorTier` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.publicAdvertisedPrefixes](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/delete)` | 

`DELETE /compute/v1/projects/{project}/global/publicAdvertisedPrefixes/{publicAdvertisedPrefix}` 

Deletes the specified PublicAdvertisedPrefix | 
|

| 

`[get](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/get)` | 

`GET /compute/v1/projects/{project}/global/publicAdvertisedPrefixes/{publicAdvertisedPrefix}` 

Returns the specified PublicAdvertisedPrefix resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/insert)` | 

`POST /compute/v1/projects/{project}/global/publicAdvertisedPrefixes` 

Creates a PublicAdvertisedPrefix in the specified project using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/list)` | 

`GET /compute/v1/projects/{project}/global/publicAdvertisedPrefixes` 

Lists the PublicAdvertisedPrefixes for a project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/patch)` | 

`PATCH /compute/v1/projects/{project}/global/publicAdvertisedPrefixes/{publicAdvertisedPrefix}` 

Patches the specified Router resource with the data included in the request. | 
|

| 

`[announce](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/announce)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.Announce` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[withdraw](/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/withdraw)` | 

The method `compute.v1.PublicAdvertisedPrefixesService.Withdraw` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.publicDelegatedPrefixes](/compute/docs/reference/rest/v1/publicDelegatedPrefixes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/publicDelegatedPrefixes` 

Lists all PublicDelegatedPrefix resources owned by the specific project across all scopes. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/publicDelegatedPrefixes/{publicDelegatedPrefix}` 

Deletes the specified PublicDelegatedPrefix in the given region. | 
|

| 

`[get](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/publicDelegatedPrefixes/{publicDelegatedPrefix}` 

Returns the specified PublicDelegatedPrefix resource in the given region. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/publicDelegatedPrefixes` 

Creates a PublicDelegatedPrefix in the specified project in the given region using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/publicDelegatedPrefixes` 

Lists the PublicDelegatedPrefixes for a project in the given region. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/publicDelegatedPrefixes/{publicDelegatedPrefix}` 

Patches the specified PublicDelegatedPrefix resource with the data included in the request. | 
|

| 

`[announce](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/announce)` | 

The method `compute.v1.PublicDelegatedPrefixesService.Announce` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[withdraw](/compute/docs/reference/rest/v1/publicDelegatedPrefixes/withdraw)` | 

The method `compute.v1.PublicDelegatedPrefixesService.Withdraw` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionAutoscalers](/compute/docs/reference/rest/v1/regionAutoscalers)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionAutoscalers/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/autoscalers/{autoscaler}` 

Deletes the specified autoscaler. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionAutoscalers/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/autoscalers/{autoscaler}` 

Returns the specified autoscaler. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionAutoscalers/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/autoscalers` 

Creates an autoscaler in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionAutoscalers/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/autoscalers` 

Retrieves a list of autoscalers contained within the specified region. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionAutoscalers/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/autoscalers` 

Updates an autoscaler in the specified project using the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionAutoscalers/update)` | 

`PUT /compute/v1/projects/{project}/regions/{region}/autoscalers` 

Updates an autoscaler in the specified project using the data included in the request. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionAutoscalers/testIamPermissions)` | 

The method `compute.v1.RegionAutoscalersService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionBackendBuckets](/compute/docs/reference/rest/v1/regionBackendBuckets)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionBackendBuckets/delete)` | 

The method `compute.v1.RegionBackendBucketsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionBackendBuckets/get)` | 

The method `compute.v1.RegionBackendBucketsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/regionBackendBuckets/getIamPolicy)` | 

The method `compute.v1.RegionBackendBucketsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionBackendBuckets/insert)` | 

The method `compute.v1.RegionBackendBucketsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionBackendBuckets/list)` | 

The method `compute.v1.RegionBackendBucketsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/v1/regionBackendBuckets/listUsable)` | 

The method `compute.v1.RegionBackendBucketsService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionBackendBuckets/patch)` | 

The method `compute.v1.RegionBackendBucketsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/regionBackendBuckets/setIamPolicy)` | 

The method `compute.v1.RegionBackendBucketsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionBackendBuckets/testIamPermissions)` | 

The method `compute.v1.RegionBackendBucketsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionBackendServices](/compute/docs/reference/rest/v1/regionBackendServices)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionBackendServices/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}` 

Deletes the specified regional BackendService resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionBackendServices/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}` 

Returns the specified regional BackendService resource. | 
|

| 

`[getHealth](/compute/docs/reference/rest/v1/regionBackendServices/getHealth)` | 

`POST /compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}/getHealth` 

Gets the most recent health check results for this regional BackendService. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionBackendServices/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/backendServices` 

Creates a regional BackendService resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionBackendServices/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/backendServices` 

Retrieves the list of regional BackendService resources available to the specified project in the given region. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionBackendServices/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}` 

Updates the specified regional BackendService resource with the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionBackendServices/update)` | 

`PUT /compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}` 

Updates the specified regional BackendService resource with the data included in the request. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/regionBackendServices/getIamPolicy)` | 

The method `compute.v1.RegionBackendServicesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/v1/regionBackendServices/listUsable)` | 

The method `compute.v1.RegionBackendServicesService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/regionBackendServices/setIamPolicy)` | 

The method `compute.v1.RegionBackendServicesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/v1/regionBackendServices/setSecurityPolicy)` | 

The method `compute.v1.RegionBackendServicesService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionBackendServices/testIamPermissions)` | 

The method `compute.v1.RegionBackendServicesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionCommitments](/compute/docs/reference/rest/v1/regionCommitments)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/regionCommitments/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/commitments` 

Retrieves an aggregated list of commitments by region. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionCommitments/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/commitments/{commitment}` 

Returns the specified commitment resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionCommitments/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/commitments` 

Creates a commitment in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionCommitments/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/commitments` 

Retrieves a list of commitments contained within the specified region. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionCommitments/update)` | 

The method `compute.v1.RegionCommitmentsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionCompositeHealthChecks](/compute/docs/reference/rest/v1/regionCompositeHealthChecks)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/regionCompositeHealthChecks/aggregatedList)` | 

The method `compute.v1.RegionCompositeHealthChecksService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionCompositeHealthChecks/delete)` | 

The method `compute.v1.RegionCompositeHealthChecksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionCompositeHealthChecks/get)` | 

The method `compute.v1.RegionCompositeHealthChecksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getHealth](/compute/docs/reference/rest/v1/regionCompositeHealthChecks/getHealth)` | 

The method `compute.v1.RegionCompositeHealthChecksService.GetHealth` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionCompositeHealthChecks/insert)` | 

The method `compute.v1.RegionCompositeHealthChecksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionCompositeHealthChecks/list)` | 

The method `compute.v1.RegionCompositeHealthChecksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionCompositeHealthChecks/patch)` | 

The method `compute.v1.RegionCompositeHealthChecksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionCompositeHealthChecks/testIamPermissions)` | 

The method `compute.v1.RegionCompositeHealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionDiskTypes](/compute/docs/reference/rest/v1/regionDiskTypes)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/regionDiskTypes/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/diskTypes/{diskType}` 

Returns the specified regional disk type. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionDiskTypes/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/diskTypes` 

Retrieves a list of regional disk types available to the specified project. | 
|






## REST Resource: [v1.regionDisks](/compute/docs/reference/rest/v1/regionDisks)









| 
Methods | 
|



| 

`[addResourcePolicies](/compute/docs/reference/rest/v1/regionDisks/addResourcePolicies)` | 

`POST /compute/v1/projects/{project}/regions/{region}/disks/{disk}/addResourcePolicies` 

Adds existing resource policies to a regional disk. | 
|

| 

`[createSnapshot](/compute/docs/reference/rest/v1/regionDisks/createSnapshot)` | 

`POST /compute/v1/projects/{project}/regions/{region}/disks/{disk}/createSnapshot` 

Creates a snapshot of a specified persistent disk. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionDisks/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/disks/{disk}` 

Deletes the specified regional persistent disk. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionDisks/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/disks/{disk}` 

Returns a specified regional persistent disk. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionDisks/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/disks` 

Creates a persistent regional disk in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionDisks/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/disks` 

Retrieves the list of persistent disks contained within the specified region. | 
|

| 

`[removeResourcePolicies](/compute/docs/reference/rest/v1/regionDisks/removeResourcePolicies)` | 

`POST /compute/v1/projects/{project}/regions/{region}/disks/{disk}/removeResourcePolicies` 

Removes resource policies from a regional disk. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/regionDisks/resize)` | 

`POST /compute/v1/projects/{project}/regions/{region}/disks/{disk}/resize` 

Resizes the specified regional persistent disk. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/regionDisks/setLabels)` | 

`POST /compute/v1/projects/{project}/regions/{region}/disks/{resource}/setLabels` 

Sets the labels on the target regional disk. | 
|

| 

`[bulkInsert](/compute/docs/reference/rest/v1/regionDisks/bulkInsert)` | 

The method `compute.v1.RegionDisksService.BulkInsert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/regionDisks/getIamPolicy)` | 

The method `compute.v1.RegionDisksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/regionDisks/setIamPolicy)` | 

The method `compute.v1.RegionDisksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startAsyncReplication](/compute/docs/reference/rest/v1/regionDisks/startAsyncReplication)` | 

The method `compute.v1.RegionDisksService.StartAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopAsyncReplication](/compute/docs/reference/rest/v1/regionDisks/stopAsyncReplication)` | 

The method `compute.v1.RegionDisksService.StopAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopGroupAsyncReplication](/compute/docs/reference/rest/v1/regionDisks/stopGroupAsyncReplication)` | 

The method `compute.v1.RegionDisksService.StopGroupAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionDisks/testIamPermissions)` | 

The method `compute.v1.RegionDisksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionDisks/update)` | 

The method `compute.v1.RegionDisksService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateKmsKey](/compute/docs/reference/rest/v1/regionDisks/updateKmsKey)` | 

The method `compute.v1.RegionDisksService.UpdateKmsKey` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionHealthAggregationPolicies](/compute/docs/reference/rest/v1/regionHealthAggregationPolicies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/aggregatedList)` | 

The method `compute.v1.RegionHealthAggregationPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/delete)` | 

The method `compute.v1.RegionHealthAggregationPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/get)` | 

The method `compute.v1.RegionHealthAggregationPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/insert)` | 

The method `compute.v1.RegionHealthAggregationPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/list)` | 

The method `compute.v1.RegionHealthAggregationPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/patch)` | 

The method `compute.v1.RegionHealthAggregationPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/testIamPermissions)` | 

The method `compute.v1.RegionHealthAggregationPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionHealthCheckServices](/compute/docs/reference/rest/v1/regionHealthCheckServices)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionHealthCheckServices/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/healthCheckServices/{healthCheckService}` 

Deletes the specified regional HealthCheckService. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionHealthCheckServices/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/healthCheckServices/{healthCheckService}` 

Returns the specified regional `HealthCheckService` resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionHealthCheckServices/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/healthCheckServices` 

Creates a regional `HealthCheckService` resource in the specified project and region using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionHealthCheckServices/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/healthCheckServices` 

Lists all the `HealthCheckService` resources that have been configured for the specified project in the given region. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionHealthCheckServices/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/healthCheckServices/{healthCheckService}` 

Updates the specified regional `HealthCheckService` resource with the data included in the request. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/regionHealthCheckServices/aggregatedList)` | 

The method `compute.v1.RegionHealthCheckServicesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionHealthCheckServices/testIamPermissions)` | 

The method `compute.v1.RegionHealthCheckServicesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionHealthChecks](/compute/docs/reference/rest/v1/regionHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionHealthChecks/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/healthChecks/{healthCheck}` 

Deletes the specified HealthCheck resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionHealthChecks/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/healthChecks/{healthCheck}` 

Returns the specified HealthCheck resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionHealthChecks/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/healthChecks` 

Creates a HealthCheck resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionHealthChecks/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/healthChecks` 

Retrieves the list of HealthCheck resources available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionHealthChecks/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/healthChecks/{healthCheck}` 

Updates a HealthCheck resource in the specified project using the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionHealthChecks/update)` | 

`PUT /compute/v1/projects/{project}/regions/{region}/healthChecks/{healthCheck}` 

Updates a HealthCheck resource in the specified project using the data included in the request. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionHealthChecks/testIamPermissions)` | 

The method `compute.v1.RegionHealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionHealthSources](/compute/docs/reference/rest/v1/regionHealthSources)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/regionHealthSources/aggregatedList)` | 

The method `compute.v1.RegionHealthSourcesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionHealthSources/delete)` | 

The method `compute.v1.RegionHealthSourcesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionHealthSources/get)` | 

The method `compute.v1.RegionHealthSourcesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getHealth](/compute/docs/reference/rest/v1/regionHealthSources/getHealth)` | 

The method `compute.v1.RegionHealthSourcesService.GetHealth` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionHealthSources/insert)` | 

The method `compute.v1.RegionHealthSourcesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionHealthSources/list)` | 

The method `compute.v1.RegionHealthSourcesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionHealthSources/patch)` | 

The method `compute.v1.RegionHealthSourcesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionHealthSources/testIamPermissions)` | 

The method `compute.v1.RegionHealthSourcesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionInstanceGroupManagerResizeRequests](/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests)









| 
Methods | 
|



| 

`[cancel](/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/cancel)` | 

The method `compute.v1.RegionInstanceGroupManagerResizeRequestsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/delete)` | 

The method `compute.v1.RegionInstanceGroupManagerResizeRequestsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/get)` | 

The method `compute.v1.RegionInstanceGroupManagerResizeRequestsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert)` | 

The method `compute.v1.RegionInstanceGroupManagerResizeRequestsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/list)` | 

The method `compute.v1.RegionInstanceGroupManagerResizeRequestsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionInstanceGroupManagers](/compute/docs/reference/rest/v1/regionInstanceGroupManagers)









| 
Methods | 
|



| 

`[abandonInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/abandonInstances)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/abandonInstances` 

Flags the specified instances to be immediately removed from the managed instance group. | 
|

| 

`[applyUpdatesToInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/applyUpdatesToInstances)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/applyUpdatesToInstances` 

Apply updates to selected instances the managed instance group. | 
|

| 

`[createInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/createInstances)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/createInstances` 

Creates instances with per-instance configurations in this regional managed instance group. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}` 

Deletes the specified managed instance group and all of the instances in that group. | 
|

| 

`[deleteInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/deleteInstances)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/deleteInstances` 

Flags the specified instances in the managed instance group to be immediately deleted. | 
|

| 

`[deletePerInstanceConfigs](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/deletePerInstanceConfigs)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/deletePerInstanceConfigs` 

Deletes selected per-instance configurations for the managed instance group. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}` 

Returns all of the details about the specified managed instance group. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers` 

Creates a managed instance group using the information that you specify in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers` 

Retrieves the list of managed instance groups that are contained within the specified region. | 
|

| 

`[listErrors](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listErrors)` | 

`GET /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/listErrors` 

Lists all errors thrown by actions on instances for a given regional managed instance group. | 
|

| 

`[listManagedInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/listManagedInstances` 

Lists the instances in the managed instance group and instances that are scheduled to be created. | 
|

| 

`[listPerInstanceConfigs](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listPerInstanceConfigs)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/listPerInstanceConfigs` 

Lists all of the per-instance configurations defined for the managed instance group. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}` 

Updates a managed instance group using the information that you specify in the request. | 
|

| 

`[patchPerInstanceConfigs](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patchPerInstanceConfigs)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/patchPerInstanceConfigs` 

Inserts or patches per-instance configurations for the managed instance group. | 
|

| 

`[recreateInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/recreateInstances)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/recreateInstances` 

Flags the specified VM instances in the managed instance group to be immediately recreated. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/resize)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/resize` 

Changes the intended size of the managed instance group. | 
|

| 

`[setInstanceTemplate](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/setInstanceTemplate)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/setInstanceTemplate` 

Sets the instance template to use when creating new instances or recreating instances in this group. | 
|

| 

`[setTargetPools](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/setTargetPools)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/setTargetPools` 

Modifies the target pools to which all new instances in this group are assigned. | 
|

| 

`[updatePerInstanceConfigs](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/updatePerInstanceConfigs)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/updatePerInstanceConfigs` 

Inserts or updates per-instance configurations for the managed instance group. | 
|

| 

`[resumeInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/resumeInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.ResumeInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/startInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.StartInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/stopInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.StopInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[suspendInstances](/compute/docs/reference/rest/v1/regionInstanceGroupManagers/suspendInstances)` | 

The method `compute.v1.RegionInstanceGroupManagersService.SuspendInstances` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionInstanceGroups](/compute/docs/reference/rest/v1/regionInstanceGroups)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/regionInstanceGroups/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/instanceGroups/{instanceGroup}` 

Returns the specified instance group resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstanceGroups/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/instanceGroups` 

Retrieves the list of instance group resources contained within the specified region. | 
|

| 

`[listInstances](/compute/docs/reference/rest/v1/regionInstanceGroups/listInstances)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroups/{instanceGroup}/listInstances` 

Lists the instances in the specified instance group and displays information about the named ports. | 
|

| 

`[setNamedPorts](/compute/docs/reference/rest/v1/regionInstanceGroups/setNamedPorts)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instanceGroups/{instanceGroup}/setNamedPorts` 

Sets the named ports for the specified regional instance group. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionInstanceGroups/testIamPermissions)` | 

The method `compute.v1.RegionInstanceGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionInstanceTemplates](/compute/docs/reference/rest/v1/regionInstanceTemplates)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionInstanceTemplates/delete)` | 

The method `compute.v1.RegionInstanceTemplatesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionInstanceTemplates/get)` | 

The method `compute.v1.RegionInstanceTemplatesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionInstanceTemplates/insert)` | 

The method `compute.v1.RegionInstanceTemplatesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstanceTemplates/list)` | 

The method `compute.v1.RegionInstanceTemplatesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionInstances](/compute/docs/reference/rest/v1/regionInstances)









| 
Methods | 
|



| 

`[bulkInsert](/compute/docs/reference/rest/v1/regionInstances/bulkInsert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/instances/bulkInsert` 

Creates multiple instances in a given region. | 
|






## REST Resource: [v1.regionInstantSnapshotGroups](/compute/docs/reference/rest/v1/regionInstantSnapshotGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionInstantSnapshotGroups/delete)` | 

The method `compute.v1.RegionInstantSnapshotGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionInstantSnapshotGroups/get)` | 

The method `compute.v1.RegionInstantSnapshotGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/regionInstantSnapshotGroups/getIamPolicy)` | 

The method `compute.v1.RegionInstantSnapshotGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionInstantSnapshotGroups/insert)` | 

The method `compute.v1.RegionInstantSnapshotGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstantSnapshotGroups/list)` | 

The method `compute.v1.RegionInstantSnapshotGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/regionInstantSnapshotGroups/setIamPolicy)` | 

The method `compute.v1.RegionInstantSnapshotGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionInstantSnapshotGroups/testIamPermissions)` | 

The method `compute.v1.RegionInstantSnapshotGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionInstantSnapshots](/compute/docs/reference/rest/v1/regionInstantSnapshots)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionInstantSnapshots/delete)` | 

The method `compute.v1.RegionInstantSnapshotsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionInstantSnapshots/get)` | 

The method `compute.v1.RegionInstantSnapshotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/regionInstantSnapshots/getIamPolicy)` | 

The method `compute.v1.RegionInstantSnapshotsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionInstantSnapshots/insert)` | 

The method `compute.v1.RegionInstantSnapshotsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionInstantSnapshots/list)` | 

The method `compute.v1.RegionInstantSnapshotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/regionInstantSnapshots/setIamPolicy)` | 

The method `compute.v1.RegionInstantSnapshotsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/regionInstantSnapshots/setLabels)` | 

The method `compute.v1.RegionInstantSnapshotsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionInstantSnapshots/testIamPermissions)` | 

The method `compute.v1.RegionInstantSnapshotsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionNetworkEndpointGroups](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/networkEndpointGroups/{networkEndpointGroup}` 

Deletes the specified network endpoint group. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/networkEndpointGroups/{networkEndpointGroup}` 

Returns the specified network endpoint group. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/networkEndpointGroups` 

Creates a network endpoint group in the specified project using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/networkEndpointGroups` 

Retrieves the list of regional network endpoint groups available to the specified project in the given region. | 
|

| 

`[attachNetworkEndpoints](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/attachNetworkEndpoints)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.AttachNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[detachNetworkEndpoints](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/detachNetworkEndpoints)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.DetachNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listNetworkEndpoints](/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/listNetworkEndpoints)` | 

The method `compute.v1.RegionNetworkEndpointGroupsService.ListNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionNetworkFirewallPolicies](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/addAssociation)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.AddAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addRule](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/addRule)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cloneRules](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/cloneRules)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.CloneRules` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/delete)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/get)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/getAssociation)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.GetAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getEffectiveFirewalls](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/getEffectiveFirewalls)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.GetEffectiveFirewalls` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/getIamPolicy)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/getRule)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/insert)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/list)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/patch)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/patchRule)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/removeAssociation)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.RemoveAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/removeRule)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/setIamPolicy)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/testIamPermissions)` | 

The method `compute.v1.RegionNetworkFirewallPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionNotificationEndpoints](/compute/docs/reference/rest/v1/regionNotificationEndpoints)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionNotificationEndpoints/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/notificationEndpoints/{notificationEndpoint}` 

Deletes the specified NotificationEndpoint in the given region | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionNotificationEndpoints/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/notificationEndpoints/{notificationEndpoint}` 

Returns the specified NotificationEndpoint resource in the given region. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionNotificationEndpoints/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/notificationEndpoints` 

Create a NotificationEndpoint in the specified project in the given region using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionNotificationEndpoints/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/notificationEndpoints` 

Lists the NotificationEndpoints for a project in the given region. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/regionNotificationEndpoints/aggregatedList)` | 

The method `compute.v1.RegionNotificationEndpointsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionNotificationEndpoints/testIamPermissions)` | 

The method `compute.v1.RegionNotificationEndpointsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionOperations](/compute/docs/reference/rest/v1/regionOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionOperations/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/operations/{operation}` 

Deletes the specified region-specific Operations resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionOperations/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/operations/{operation}` 

Retrieves the specified region-specific Operations resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionOperations/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/operations` 

Retrieves a list of Operation resources contained within the specified region. | 
|

| 

`[wait](/compute/docs/reference/rest/v1/regionOperations/wait)` | 

`POST /compute/v1/projects/{project}/regions/{region}/operations/{operation}/wait` 

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. | 
|






## REST Resource: [v1.regionSecurityPolicies](/compute/docs/reference/rest/v1/regionSecurityPolicies)









| 
Methods | 
|



| 

`[addRule](/compute/docs/reference/rest/v1/regionSecurityPolicies/addRule)` | 

The method `compute.v1.RegionSecurityPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/regionSecurityPolicies/delete)` | 

The method `compute.v1.RegionSecurityPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionSecurityPolicies/get)` | 

The method `compute.v1.RegionSecurityPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/v1/regionSecurityPolicies/getRule)` | 

The method `compute.v1.RegionSecurityPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionSecurityPolicies/insert)` | 

The method `compute.v1.RegionSecurityPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionSecurityPolicies/list)` | 

The method `compute.v1.RegionSecurityPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionSecurityPolicies/patch)` | 

The method `compute.v1.RegionSecurityPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/v1/regionSecurityPolicies/patchRule)` | 

The method `compute.v1.RegionSecurityPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/v1/regionSecurityPolicies/removeRule)` | 

The method `compute.v1.RegionSecurityPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/regionSecurityPolicies/setLabels)` | 

The method `compute.v1.RegionSecurityPoliciesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionSnapshotSettings](/compute/docs/reference/rest/v1/regionSnapshotSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/regionSnapshotSettings/get)` | 

The method `compute.v1.RegionSnapshotSettingsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionSnapshotSettings/patch)` | 

The method `compute.v1.RegionSnapshotSettingsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionSnapshots](/compute/docs/reference/rest/v1/regionSnapshots)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionSnapshots/delete)` | 

The method `compute.v1.RegionSnapshotsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionSnapshots/get)` | 

The method `compute.v1.RegionSnapshotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/regionSnapshots/getIamPolicy)` | 

The method `compute.v1.RegionSnapshotsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionSnapshots/insert)` | 

The method `compute.v1.RegionSnapshotsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionSnapshots/list)` | 

The method `compute.v1.RegionSnapshotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/regionSnapshots/setIamPolicy)` | 

The method `compute.v1.RegionSnapshotsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/regionSnapshots/setLabels)` | 

The method `compute.v1.RegionSnapshotsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/regionSnapshots/testIamPermissions)` | 

The method `compute.v1.RegionSnapshotsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateKmsKey](/compute/docs/reference/rest/v1/regionSnapshots/updateKmsKey)` | 

The method `compute.v1.RegionSnapshotsService.UpdateKmsKey` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionSslCertificates](/compute/docs/reference/rest/v1/regionSslCertificates)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionSslCertificates/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/sslCertificates/{sslCertificate}` 

Deletes the specified SslCertificate resource in the region. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionSslCertificates/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/sslCertificates/{sslCertificate}` 

Returns the specified SslCertificate resource in the specified region. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionSslCertificates/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/sslCertificates` 

Creates a SslCertificate resource in the specified project and region using the data included in the request | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionSslCertificates/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/sslCertificates` 

Retrieves the list of SslCertificate resources available to the specified project in the specified region. | 
|






## REST Resource: [v1.regionSslPolicies](/compute/docs/reference/rest/v1/regionSslPolicies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionSslPolicies/delete)` | 

The method `compute.v1.RegionSslPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionSslPolicies/get)` | 

The method `compute.v1.RegionSslPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionSslPolicies/insert)` | 

The method `compute.v1.RegionSslPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionSslPolicies/list)` | 

The method `compute.v1.RegionSslPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listAvailableFeatures](/compute/docs/reference/rest/v1/regionSslPolicies/listAvailableFeatures)` | 

The method `compute.v1.RegionSslPoliciesService.ListAvailableFeatures` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionSslPolicies/patch)` | 

The method `compute.v1.RegionSslPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionTargetHttpProxies](/compute/docs/reference/rest/v1/regionTargetHttpProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionTargetHttpProxies/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/targetHttpProxies/{targetHttpProxy}` 

Deletes the specified TargetHttpProxy resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionTargetHttpProxies/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/targetHttpProxies/{targetHttpProxy}` 

Returns the specified TargetHttpProxy resource in the specified region. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionTargetHttpProxies/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetHttpProxies` 

Creates a TargetHttpProxy resource in the specified project and region using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionTargetHttpProxies/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/targetHttpProxies` 

Retrieves the list of TargetHttpProxy resources available to the specified project in the specified region. | 
|

| 

`[setUrlMap](/compute/docs/reference/rest/v1/regionTargetHttpProxies/setUrlMap)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetHttpProxies/{targetHttpProxy}/setUrlMap` 

Changes the URL map for TargetHttpProxy. | 
|






## REST Resource: [v1.regionTargetHttpsProxies](/compute/docs/reference/rest/v1/regionTargetHttpsProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/targetHttpsProxies/{targetHttpsProxy}` 

Deletes the specified TargetHttpsProxy resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/targetHttpsProxies/{targetHttpsProxy}` 

Returns the specified TargetHttpsProxy resource in the specified region. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetHttpsProxies` 

Creates a TargetHttpsProxy resource in the specified project and region using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/targetHttpsProxies` 

Retrieves the list of TargetHttpsProxy resources available to the specified project in the specified region. | 
|

| 

`[setSslCertificates](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/setSslCertificates)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetHttpsProxies/{targetHttpsProxy}/setSslCertificates` 

Replaces SslCertificates for TargetHttpsProxy. | 
|

| 

`[setUrlMap](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/setUrlMap)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetHttpsProxies/{targetHttpsProxy}/setUrlMap` 

Changes the URL map for TargetHttpsProxy. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionTargetHttpsProxies/patch)` | 

The method `compute.v1.RegionTargetHttpsProxiesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionTargetTcpProxies](/compute/docs/reference/rest/v1/regionTargetTcpProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionTargetTcpProxies/delete)` | 

The method `compute.v1.RegionTargetTcpProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionTargetTcpProxies/get)` | 

The method `compute.v1.RegionTargetTcpProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionTargetTcpProxies/insert)` | 

The method `compute.v1.RegionTargetTcpProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionTargetTcpProxies/list)` | 

The method `compute.v1.RegionTargetTcpProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regionUrlMaps](/compute/docs/reference/rest/v1/regionUrlMaps)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/regionUrlMaps/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/urlMaps/{urlMap}` 

Deletes the specified UrlMap resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/regionUrlMaps/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/urlMaps/{urlMap}` 

Returns the specified UrlMap resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/regionUrlMaps/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/urlMaps` 

Creates a UrlMap resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regionUrlMaps/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/urlMaps` 

Retrieves the list of UrlMap resources available to the specified project in the specified region. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/regionUrlMaps/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/urlMaps/{urlMap}` 

Patches the specified UrlMap resource with the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/regionUrlMaps/update)` | 

`PUT /compute/v1/projects/{project}/regions/{region}/urlMaps/{urlMap}` 

Updates the specified UrlMap resource with the data included in the request. | 
|

| 

`[validate](/compute/docs/reference/rest/v1/regionUrlMaps/validate)` | 

`POST /compute/v1/projects/{project}/regions/{region}/urlMaps/{urlMap}/validate` 

Runs static validation for the UrlMap. | 
|






## REST Resource: [v1.regionZones](/compute/docs/reference/rest/v1/regionZones)









| 
Methods | 
|



| 

`[list](/compute/docs/reference/rest/v1/regionZones/list)` | 

The method `compute.v1.RegionZonesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.regions](/compute/docs/reference/rest/v1/regions)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/regions/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}` 

Returns the specified Region resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/regions/list)` | 

`GET /compute/v1/projects/{project}/regions` 

Retrieves the list of region resources available to the specified project. | 
|






## REST Resource: [v1.reliabilityRisks](/compute/docs/reference/rest/v1/reliabilityRisks)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/reliabilityRisks/get)` | 

The method `compute.v1.ReliabilityRisksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/reliabilityRisks/list)` | 

The method `compute.v1.ReliabilityRisksService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.reservationBlocks](/compute/docs/reference/rest/v1/reservationBlocks)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/reservationBlocks/get)` | 

The method `compute.v1.ReservationBlocksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/reservationBlocks/getIamPolicy)` | 

The method `compute.v1.ReservationBlocksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/reservationBlocks/list)` | 

The method `compute.v1.ReservationBlocksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/v1/reservationBlocks/performMaintenance)` | 

The method `compute.v1.ReservationBlocksService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/reservationBlocks/setIamPolicy)` | 

The method `compute.v1.ReservationBlocksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/reservationBlocks/testIamPermissions)` | 

The method `compute.v1.ReservationBlocksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.reservationSlots](/compute/docs/reference/rest/v1/reservationSlots)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/reservationSlots/get)` | 

The method `compute.v1.ReservationSlotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getVersion](/compute/docs/reference/rest/v1/reservationSlots/getVersion)` | 

The method `compute.v1.ReservationSlotsService.GetVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/reservationSlots/list)` | 

The method `compute.v1.ReservationSlotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/reservationSlots/update)` | 

The method `compute.v1.ReservationSlotsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.reservationSubBlocks](/compute/docs/reference/rest/v1/reservationSubBlocks)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/reservationSubBlocks/get)` | 

The method `compute.v1.ReservationSubBlocksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/reservationSubBlocks/getIamPolicy)` | 

The method `compute.v1.ReservationSubBlocksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getVersion](/compute/docs/reference/rest/v1/reservationSubBlocks/getVersion)` | 

The method `compute.v1.ReservationSubBlocksService.GetVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/reservationSubBlocks/list)` | 

The method `compute.v1.ReservationSubBlocksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/v1/reservationSubBlocks/performMaintenance)` | 

The method `compute.v1.ReservationSubBlocksService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[reportFaulty](/compute/docs/reference/rest/v1/reservationSubBlocks/reportFaulty)` | 

The method `compute.v1.ReservationSubBlocksService.ReportFaulty` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/reservationSubBlocks/setIamPolicy)` | 

The method `compute.v1.ReservationSubBlocksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/reservationSubBlocks/testIamPermissions)` | 

The method `compute.v1.ReservationSubBlocksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.reservations](/compute/docs/reference/rest/v1/reservations)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/reservations/aggregatedList)` | 

The method `compute.v1.AllocationsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/reservations/delete)` | 

The method `compute.v1.AllocationsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/reservations/get)` | 

The method `compute.v1.AllocationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/reservations/getIamPolicy)` | 

The method `compute.v1.AllocationsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/reservations/insert)` | 

The method `compute.v1.AllocationsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/reservations/list)` | 

The method `compute.v1.AllocationsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/v1/reservations/performMaintenance)` | 

The method `compute.v1.AllocationsService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resize](/compute/docs/reference/rest/v1/reservations/resize)` | 

The method `compute.v1.AllocationsService.Resize` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/reservations/setIamPolicy)` | 

The method `compute.v1.AllocationsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/reservations/testIamPermissions)` | 

The method `compute.v1.AllocationsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/reservations/update)` | 

The method `compute.v1.AllocationsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.resourcePolicies](/compute/docs/reference/rest/v1/resourcePolicies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/resourcePolicies/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/resourcePolicies` 

Retrieves an aggregated list of resource policies. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/resourcePolicies/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/resourcePolicies/{resourcePolicy}` 

Deletes the specified resource policy. | 
|

| 

`[get](/compute/docs/reference/rest/v1/resourcePolicies/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/resourcePolicies/{resourcePolicy}` 

Retrieves all information of the specified resource policy. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/resourcePolicies/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/resourcePolicies` 

Creates a new resource policy. | 
|

| 

`[list](/compute/docs/reference/rest/v1/resourcePolicies/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/resourcePolicies` 

A list all the resource policies that have been configured for the specified project in specified region. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/resourcePolicies/getIamPolicy)` | 

The method `compute.v1.ResourcePoliciesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/resourcePolicies/patch)` | 

The method `compute.v1.ResourcePoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/resourcePolicies/setIamPolicy)` | 

The method `compute.v1.ResourcePoliciesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/resourcePolicies/testIamPermissions)` | 

The method `compute.v1.ResourcePoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.rolloutPlans](/compute/docs/reference/rest/v1/rolloutPlans)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/rolloutPlans/delete)` | 

The method `compute.v1.RolloutPlansService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/rolloutPlans/get)` | 

The method `compute.v1.RolloutPlansService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/rolloutPlans/insert)` | 

The method `compute.v1.RolloutPlansService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/rolloutPlans/list)` | 

The method `compute.v1.RolloutPlansService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.rollouts](/compute/docs/reference/rest/v1/rollouts)









| 
Methods | 
|



| 

`[advance](/compute/docs/reference/rest/v1/rollouts/advance)` | 

The method `compute.v1.RolloutsService.Advance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cancel](/compute/docs/reference/rest/v1/rollouts/cancel)` | 

The method `compute.v1.RolloutsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/rollouts/delete)` | 

The method `compute.v1.RolloutsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/rollouts/get)` | 

The method `compute.v1.RolloutsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/rollouts/list)` | 

The method `compute.v1.RolloutsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[pause](/compute/docs/reference/rest/v1/rollouts/pause)` | 

The method `compute.v1.RolloutsService.Pause` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resume](/compute/docs/reference/rest/v1/rollouts/resume)` | 

The method `compute.v1.RolloutsService.Resume` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.routers](/compute/docs/reference/rest/v1/routers)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/routers/aggregatedList)` | 

The method `compute.v1.RegionRoutersService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/routers/delete)` | 

The method `compute.v1.RegionRoutersService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteNamedSet](/compute/docs/reference/rest/v1/routers/deleteNamedSet)` | 

The method `compute.v1.RegionRoutersService.DeleteNamedSet` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteRoutePolicy](/compute/docs/reference/rest/v1/routers/deleteRoutePolicy)` | 

The method `compute.v1.RegionRoutersService.DeleteRoutePolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/routers/get)` | 

The method `compute.v1.RegionRoutersService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getNamedSet](/compute/docs/reference/rest/v1/routers/getNamedSet)` | 

The method `compute.v1.RegionRoutersService.GetNamedSet` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getNatIpInfo](/compute/docs/reference/rest/v1/routers/getNatIpInfo)` | 

The method `compute.v1.RegionRoutersService.GetNatIpInfo` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getNatMappingInfo](/compute/docs/reference/rest/v1/routers/getNatMappingInfo)` | 

The method `compute.v1.RegionRoutersService.GetNatMappingInfo` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRoutePolicy](/compute/docs/reference/rest/v1/routers/getRoutePolicy)` | 

The method `compute.v1.RegionRoutersService.GetRoutePolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRouterStatus](/compute/docs/reference/rest/v1/routers/getRouterStatus)` | 

The method `compute.v1.RegionRoutersService.GetRouterStatus` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/routers/insert)` | 

The method `compute.v1.RegionRoutersService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/routers/list)` | 

The method `compute.v1.RegionRoutersService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listBgpRoutes](/compute/docs/reference/rest/v1/routers/listBgpRoutes)` | 

The method `compute.v1.RegionRoutersService.ListBgpRoutes` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listNamedSets](/compute/docs/reference/rest/v1/routers/listNamedSets)` | 

The method `compute.v1.RegionRoutersService.ListNamedSets` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listRoutePolicies](/compute/docs/reference/rest/v1/routers/listRoutePolicies)` | 

The method `compute.v1.RegionRoutersService.ListRoutePolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/routers/patch)` | 

The method `compute.v1.RegionRoutersService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchNamedSet](/compute/docs/reference/rest/v1/routers/patchNamedSet)` | 

The method `compute.v1.RegionRoutersService.PatchNamedSet` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRoutePolicy](/compute/docs/reference/rest/v1/routers/patchRoutePolicy)` | 

The method `compute.v1.RegionRoutersService.PatchRoutePolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[preview](/compute/docs/reference/rest/v1/routers/preview)` | 

The method `compute.v1.RegionRoutersService.Preview` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/routers/update)` | 

The method `compute.v1.RegionRoutersService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateNamedSet](/compute/docs/reference/rest/v1/routers/updateNamedSet)` | 

The method `compute.v1.RegionRoutersService.UpdateNamedSet` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateRoutePolicy](/compute/docs/reference/rest/v1/routers/updateRoutePolicy)` | 

The method `compute.v1.RegionRoutersService.UpdateRoutePolicy` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.routes](/compute/docs/reference/rest/v1/routes)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/routes/delete)` | 

`DELETE /compute/v1/projects/{project}/global/routes/{route}` 

Deletes the specified Route resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/routes/get)` | 

`GET /compute/v1/projects/{project}/global/routes/{route}` 

Returns the specified Route resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/routes/insert)` | 

`POST /compute/v1/projects/{project}/global/routes` 

Creates a Route resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/routes/list)` | 

`GET /compute/v1/projects/{project}/global/routes` 

Retrieves the list of Route resources available to the specified project. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/routes/testIamPermissions)` | 

The method `compute.v1.RoutesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.securityPolicies](/compute/docs/reference/rest/v1/securityPolicies)









| 
Methods | 
|



| 

`[addRule](/compute/docs/reference/rest/v1/securityPolicies/addRule)` | 

`POST /compute/v1/projects/{project}/global/securityPolicies/{securityPolicy}/addRule` 

Inserts a rule into a security policy. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/securityPolicies/delete)` | 

`DELETE /compute/v1/projects/{project}/global/securityPolicies/{securityPolicy}` 

Deletes the specified policy. | 
|

| 

`[get](/compute/docs/reference/rest/v1/securityPolicies/get)` | 

`GET /compute/v1/projects/{project}/global/securityPolicies/{securityPolicy}` 

List all of the ordered rules present in a single specified policy. | 
|

| 

`[getRule](/compute/docs/reference/rest/v1/securityPolicies/getRule)` | 

`GET /compute/v1/projects/{project}/global/securityPolicies/{securityPolicy}/getRule` 

Gets a rule at the specified priority. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/securityPolicies/insert)` | 

`POST /compute/v1/projects/{project}/global/securityPolicies` 

Creates a new policy in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/securityPolicies/list)` | 

`GET /compute/v1/projects/{project}/global/securityPolicies` 

List all the policies that have been configured for the specified project. | 
|

| 

`[listPreconfiguredExpressionSets](/compute/docs/reference/rest/v1/securityPolicies/listPreconfiguredExpressionSets)` | 

`GET /compute/v1/projects/{project}/global/securityPolicies/listPreconfiguredExpressionSets` 

Gets the current list of preconfigured Web Application Firewall (WAF) expressions. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/securityPolicies/patch)` | 

`PATCH /compute/v1/projects/{project}/global/securityPolicies/{securityPolicy}` 

Patches the specified policy with the data included in the request. | 
|

| 

`[patchRule](/compute/docs/reference/rest/v1/securityPolicies/patchRule)` | 

`POST /compute/v1/projects/{project}/global/securityPolicies/{securityPolicy}/patchRule` 

Patches a rule at the specified priority. | 
|

| 

`[removeRule](/compute/docs/reference/rest/v1/securityPolicies/removeRule)` | 

`POST /compute/v1/projects/{project}/global/securityPolicies/{securityPolicy}/removeRule` 

Deletes a rule at the specified priority. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/securityPolicies/aggregatedList)` | 

The method `compute.v1.SecurityPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/securityPolicies/setLabels)` | 

The method `compute.v1.SecurityPoliciesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.serviceAttachments](/compute/docs/reference/rest/v1/serviceAttachments)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/serviceAttachments/aggregatedList)` | 

The method `compute.v1.ServiceAttachmentsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/serviceAttachments/delete)` | 

The method `compute.v1.ServiceAttachmentsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/serviceAttachments/get)` | 

The method `compute.v1.ServiceAttachmentsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/serviceAttachments/getIamPolicy)` | 

The method `compute.v1.ServiceAttachmentsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/serviceAttachments/insert)` | 

The method `compute.v1.ServiceAttachmentsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/serviceAttachments/list)` | 

The method `compute.v1.ServiceAttachmentsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/serviceAttachments/patch)` | 

The method `compute.v1.ServiceAttachmentsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/serviceAttachments/setIamPolicy)` | 

The method `compute.v1.ServiceAttachmentsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/serviceAttachments/testIamPermissions)` | 

The method `compute.v1.ServiceAttachmentsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.snapshotSettings](/compute/docs/reference/rest/v1/snapshotSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/snapshotSettings/get)` | 

The method `compute.v1.SnapshotSettingsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/snapshotSettings/patch)` | 

The method `compute.v1.SnapshotSettingsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.snapshots](/compute/docs/reference/rest/v1/snapshots)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/snapshots/delete)` | 

`DELETE /compute/v1/projects/{project}/global/snapshots/{snapshot}` 

Deletes the specified Snapshot resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/snapshots/get)` | 

`GET /compute/v1/projects/{project}/global/snapshots/{snapshot}` 

Returns the specified Snapshot resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/snapshots/list)` | 

`GET /compute/v1/projects/{project}/global/snapshots` 

Retrieves the list of Snapshot resources contained within the specified project. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/snapshots/setLabels)` | 

`POST /compute/v1/projects/{project}/global/snapshots/{resource}/setLabels` 

Sets the labels on a snapshot. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/snapshots/getIamPolicy)` | 

The method `compute.v1.SnapshotsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/snapshots/insert)` | 

The method `compute.v1.SnapshotsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/snapshots/setIamPolicy)` | 

The method `compute.v1.SnapshotsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/snapshots/testIamPermissions)` | 

The method `compute.v1.SnapshotsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateKmsKey](/compute/docs/reference/rest/v1/snapshots/updateKmsKey)` | 

The method `compute.v1.SnapshotsService.UpdateKmsKey` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.sslCertificates](/compute/docs/reference/rest/v1/sslCertificates)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/sslCertificates/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/sslCertificates` 

Retrieves the list of all SslCertificate resources, regional and global, available to the specified project. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/sslCertificates/delete)` | 

`DELETE /compute/v1/projects/{project}/global/sslCertificates/{sslCertificate}` 

Deletes the specified SslCertificate resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/sslCertificates/get)` | 

`GET /compute/v1/projects/{project}/global/sslCertificates/{sslCertificate}` 

Returns the specified SslCertificate resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/sslCertificates/insert)` | 

`POST /compute/v1/projects/{project}/global/sslCertificates` 

Creates a SslCertificate resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/sslCertificates/list)` | 

`GET /compute/v1/projects/{project}/global/sslCertificates` 

Retrieves the list of SslCertificate resources available to the specified project. | 
|






## REST Resource: [v1.sslPolicies](/compute/docs/reference/rest/v1/sslPolicies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/sslPolicies/delete)` | 

`DELETE /compute/v1/projects/{project}/global/sslPolicies/{sslPolicy}` 

Deletes the specified SSL policy. | 
|

| 

`[get](/compute/docs/reference/rest/v1/sslPolicies/get)` | 

`GET /compute/v1/projects/{project}/global/sslPolicies/{sslPolicy}` 

Lists all of the ordered rules present in a single specified policy. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/sslPolicies/insert)` | 

`POST /compute/v1/projects/{project}/global/sslPolicies` 

Returns the specified SSL policy resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/sslPolicies/list)` | 

`GET /compute/v1/projects/{project}/global/sslPolicies` 

Lists all the SSL policies that have been configured for the specified project. | 
|

| 

`[listAvailableFeatures](/compute/docs/reference/rest/v1/sslPolicies/listAvailableFeatures)` | 

`GET /compute/v1/projects/{project}/global/sslPolicies/listAvailableFeatures` 

Lists all features that can be specified in the SSL policy when using custom profile. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/sslPolicies/patch)` | 

`PATCH /compute/v1/projects/{project}/global/sslPolicies/{sslPolicy}` 

Patches the specified SSL policy with the data included in the request. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/sslPolicies/aggregatedList)` | 

The method `compute.v1.SslPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.storagePoolTypes](/compute/docs/reference/rest/v1/storagePoolTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/storagePoolTypes/aggregatedList)` | 

The method `compute.v1.StoragePoolTypesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/storagePoolTypes/get)` | 

The method `compute.v1.StoragePoolTypesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/storagePoolTypes/list)` | 

The method `compute.v1.StoragePoolTypesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.storagePools](/compute/docs/reference/rest/v1/storagePools)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/storagePools/aggregatedList)` | 

The method `compute.v1.StoragePoolsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/storagePools/delete)` | 

The method `compute.v1.StoragePoolsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/storagePools/get)` | 

The method `compute.v1.StoragePoolsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/storagePools/getIamPolicy)` | 

The method `compute.v1.StoragePoolsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/storagePools/insert)` | 

The method `compute.v1.StoragePoolsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/storagePools/list)` | 

The method `compute.v1.StoragePoolsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listDisks](/compute/docs/reference/rest/v1/storagePools/listDisks)` | 

The method `compute.v1.StoragePoolsService.ListDisks` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/storagePools/setIamPolicy)` | 

The method `compute.v1.StoragePoolsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/storagePools/testIamPermissions)` | 

The method `compute.v1.StoragePoolsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/storagePools/update)` | 

The method `compute.v1.StoragePoolsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.subnetworks](/compute/docs/reference/rest/v1/subnetworks)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/subnetworks/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/subnetworks` 

Retrieves an aggregated list of subnetworks. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/subnetworks/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}` 

Deletes the specified subnetwork. | 
|

| 

`[expandIpCidrRange](/compute/docs/reference/rest/v1/subnetworks/expandIpCidrRange)` | 

`POST /compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}/expandIpCidrRange` 

Expands the IP CIDR range of the subnetwork to a specified value. | 
|

| 

`[get](/compute/docs/reference/rest/v1/subnetworks/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}` 

Returns the specified subnetwork. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/subnetworks/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/subnetworks` 

Creates a subnetwork in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/subnetworks/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/subnetworks` 

Retrieves a list of subnetworks available to the specified project. | 
|

| 

`[listUsable](/compute/docs/reference/rest/v1/subnetworks/listUsable)` | 

`GET /compute/v1/projects/{project}/aggregated/subnetworks/listUsable` 

Retrieves an aggregated list of all usable subnetworks in the project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/subnetworks/patch)` | 

`PATCH /compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}` 

Patches the specified subnetwork with the data included in the request. | 
|

| 

`[setPrivateIpGoogleAccess](/compute/docs/reference/rest/v1/subnetworks/setPrivateIpGoogleAccess)` | 

`POST /compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}/setPrivateIpGoogleAccess` 

Set whether VMs in this subnet can access Cloud de Confiance services without assigning external IP addresses through Private Cloud de Confiance Access. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/v1/subnetworks/getIamPolicy)` | 

The method `compute.v1.SubnetworksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/v1/subnetworks/setIamPolicy)` | 

The method `compute.v1.SubnetworksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/subnetworks/testIamPermissions)` | 

The method `compute.v1.SubnetworksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.targetGrpcProxies](/compute/docs/reference/rest/v1/targetGrpcProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/targetGrpcProxies/delete)` | 

`DELETE /compute/v1/projects/{project}/global/targetGrpcProxies/{targetGrpcProxy}` 

Deletes the specified TargetGrpcProxy in the given scope | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetGrpcProxies/get)` | 

`GET /compute/v1/projects/{project}/global/targetGrpcProxies/{targetGrpcProxy}` 

Returns the specified TargetGrpcProxy resource in the given scope. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetGrpcProxies/insert)` | 

`POST /compute/v1/projects/{project}/global/targetGrpcProxies` 

Creates a TargetGrpcProxy in the specified project in the given scope using the parameters that are included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetGrpcProxies/list)` | 

`GET /compute/v1/projects/{project}/global/targetGrpcProxies` 

Lists the TargetGrpcProxies for a project in the given scope. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/targetGrpcProxies/patch)` | 

`PATCH /compute/v1/projects/{project}/global/targetGrpcProxies/{targetGrpcProxy}` 

Patches the specified TargetGrpcProxy resource with the data included in the request. | 
|






## REST Resource: [v1.targetHttpProxies](/compute/docs/reference/rest/v1/targetHttpProxies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/targetHttpProxies/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/targetHttpProxies` 

Retrieves the list of all TargetHttpProxy resources, regional and global, available to the specified project. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetHttpProxies/delete)` | 

`DELETE /compute/v1/projects/{project}/global/targetHttpProxies/{targetHttpProxy}` 

Deletes the specified TargetHttpProxy resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetHttpProxies/get)` | 

`GET /compute/v1/projects/{project}/global/targetHttpProxies/{targetHttpProxy}` 

Returns the specified TargetHttpProxy resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetHttpProxies/insert)` | 

`POST /compute/v1/projects/{project}/global/targetHttpProxies` 

Creates a TargetHttpProxy resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetHttpProxies/list)` | 

`GET /compute/v1/projects/{project}/global/targetHttpProxies` 

Retrieves the list of TargetHttpProxy resources available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/targetHttpProxies/patch)` | 

`PATCH /compute/v1/projects/{project}/global/targetHttpProxies/{targetHttpProxy}` 

Patches the specified TargetHttpProxy resource with the data included in the request. | 
|

| 

`[setUrlMap](/compute/docs/reference/rest/v1/targetHttpProxies/setUrlMap)` | 

`POST /compute/v1/projects/{project}/targetHttpProxies/{targetHttpProxy}/setUrlMap` 

Changes the URL map for TargetHttpProxy. | 
|






## REST Resource: [v1.targetHttpsProxies](/compute/docs/reference/rest/v1/targetHttpsProxies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/targetHttpsProxies/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/targetHttpsProxies` 

Retrieves the list of all TargetHttpsProxy resources, regional and global, available to the specified project. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetHttpsProxies/delete)` | 

`DELETE /compute/v1/projects/{project}/global/targetHttpsProxies/{targetHttpsProxy}` 

Deletes the specified TargetHttpsProxy resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetHttpsProxies/get)` | 

`GET /compute/v1/projects/{project}/global/targetHttpsProxies/{targetHttpsProxy}` 

Returns the specified TargetHttpsProxy resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetHttpsProxies/insert)` | 

`POST /compute/v1/projects/{project}/global/targetHttpsProxies` 

Creates a TargetHttpsProxy resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetHttpsProxies/list)` | 

`GET /compute/v1/projects/{project}/global/targetHttpsProxies` 

Retrieves the list of TargetHttpsProxy resources available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/targetHttpsProxies/patch)` | 

`PATCH /compute/v1/projects/{project}/global/targetHttpsProxies/{targetHttpsProxy}` 

Patches the specified TargetHttpsProxy resource with the data included in the request. | 
|

| 

`[setQuicOverride](/compute/docs/reference/rest/v1/targetHttpsProxies/setQuicOverride)` | 

`POST /compute/v1/projects/{project}/global/targetHttpsProxies/{targetHttpsProxy}/setQuicOverride` 

Sets the QUIC override policy for TargetHttpsProxy. | 
|

| 

`[setSslCertificates](/compute/docs/reference/rest/v1/targetHttpsProxies/setSslCertificates)` | 

`POST /compute/v1/projects/{project}/targetHttpsProxies/{targetHttpsProxy}/setSslCertificates` 

Replaces SslCertificates for TargetHttpsProxy. | 
|

| 

`[setSslPolicy](/compute/docs/reference/rest/v1/targetHttpsProxies/setSslPolicy)` | 

`POST /compute/v1/projects/{project}/global/targetHttpsProxies/{targetHttpsProxy}/setSslPolicy` 

Sets the SSL policy for TargetHttpsProxy. | 
|

| 

`[setUrlMap](/compute/docs/reference/rest/v1/targetHttpsProxies/setUrlMap)` | 

`POST /compute/v1/projects/{project}/targetHttpsProxies/{targetHttpsProxy}/setUrlMap` 

Changes the URL map for TargetHttpsProxy. | 
|

| 

`[setCertificateMap](/compute/docs/reference/rest/v1/targetHttpsProxies/setCertificateMap)` | 

The method `compute.v1.TargetHttpsProxiesService.SetCertificateMap` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.targetInstances](/compute/docs/reference/rest/v1/targetInstances)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/targetInstances/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/targetInstances` 

Retrieves an aggregated list of target instances. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetInstances/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/targetInstances/{targetInstance}` 

Deletes the specified TargetInstance resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetInstances/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/targetInstances/{targetInstance}` 

Returns the specified TargetInstance resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetInstances/insert)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/targetInstances` 

Creates a TargetInstance resource in the specified project and zone using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetInstances/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/targetInstances` 

Retrieves a list of TargetInstance resources available to the specified project and zone. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/v1/targetInstances/setSecurityPolicy)` | 

The method `compute.v1.TargetInstancesService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/targetInstances/testIamPermissions)` | 

The method `compute.v1.TargetInstancesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.targetPools](/compute/docs/reference/rest/v1/targetPools)









| 
Methods | 
|



| 

`[addHealthCheck](/compute/docs/reference/rest/v1/targetPools/addHealthCheck)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}/addHealthCheck` 

Adds health check URLs to a target pool. | 
|

| 

`[addInstance](/compute/docs/reference/rest/v1/targetPools/addInstance)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}/addInstance` 

Adds an instance to a target pool. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/targetPools/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/targetPools` 

Retrieves an aggregated list of target pools. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetPools/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}` 

Deletes the specified target pool. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetPools/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}` 

Returns the specified target pool. | 
|

| 

`[getHealth](/compute/docs/reference/rest/v1/targetPools/getHealth)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}/getHealth` 

Gets the most recent health check results for each IP for the instance that is referenced by the given target pool. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetPools/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetPools` 

Creates a target pool in the specified project and region using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetPools/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/targetPools` 

Retrieves a list of target pools available to the specified project and region. | 
|

| 

`[removeHealthCheck](/compute/docs/reference/rest/v1/targetPools/removeHealthCheck)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}/removeHealthCheck` 

Removes health check URL from a target pool. | 
|

| 

`[removeInstance](/compute/docs/reference/rest/v1/targetPools/removeInstance)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}/removeInstance` 

Removes instance URL from a target pool. | 
|

| 

`[setBackup](/compute/docs/reference/rest/v1/targetPools/setBackup)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}/setBackup` 

Changes a backup target pool's configurations. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/v1/targetPools/setSecurityPolicy)` | 

The method `compute.v1.TargetPoolsService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/targetPools/testIamPermissions)` | 

The method `compute.v1.TargetPoolsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.targetSslProxies](/compute/docs/reference/rest/v1/targetSslProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/targetSslProxies/delete)` | 

`DELETE /compute/v1/projects/{project}/global/targetSslProxies/{targetSslProxy}` 

Deletes the specified TargetSslProxy resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetSslProxies/get)` | 

`GET /compute/v1/projects/{project}/global/targetSslProxies/{targetSslProxy}` 

Returns the specified TargetSslProxy resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetSslProxies/insert)` | 

`POST /compute/v1/projects/{project}/global/targetSslProxies` 

Creates a TargetSslProxy resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetSslProxies/list)` | 

`GET /compute/v1/projects/{project}/global/targetSslProxies` 

Retrieves the list of `TargetSslProxy` resources available to the specified project. | 
|

| 

`[setBackendService](/compute/docs/reference/rest/v1/targetSslProxies/setBackendService)` | 

`POST /compute/v1/projects/{project}/global/targetSslProxies/{targetSslProxy}/setBackendService` 

Changes the BackendService for TargetSslProxy. | 
|

| 

`[setProxyHeader](/compute/docs/reference/rest/v1/targetSslProxies/setProxyHeader)` | 

`POST /compute/v1/projects/{project}/global/targetSslProxies/{targetSslProxy}/setProxyHeader` 

Changes the ProxyHeaderType for TargetSslProxy. | 
|

| 

`[setSslCertificates](/compute/docs/reference/rest/v1/targetSslProxies/setSslCertificates)` | 

`POST /compute/v1/projects/{project}/global/targetSslProxies/{targetSslProxy}/setSslCertificates` 

Changes SslCertificates for TargetSslProxy. | 
|

| 

`[setSslPolicy](/compute/docs/reference/rest/v1/targetSslProxies/setSslPolicy)` | 

`POST /compute/v1/projects/{project}/global/targetSslProxies/{targetSslProxy}/setSslPolicy` 

Sets the SSL policy for TargetSslProxy. | 
|

| 

`[setCertificateMap](/compute/docs/reference/rest/v1/targetSslProxies/setCertificateMap)` | 

The method `compute.v1.TargetSslProxiesService.SetCertificateMap` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/targetSslProxies/testIamPermissions)` | 

The method `compute.v1.TargetSslProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.targetTcpProxies](/compute/docs/reference/rest/v1/targetTcpProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/targetTcpProxies/delete)` | 

`DELETE /compute/v1/projects/{project}/global/targetTcpProxies/{targetTcpProxy}` 

Deletes the specified TargetTcpProxy resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetTcpProxies/get)` | 

`GET /compute/v1/projects/{project}/global/targetTcpProxies/{targetTcpProxy}` 

Returns the specified TargetTcpProxy resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetTcpProxies/insert)` | 

`POST /compute/v1/projects/{project}/global/targetTcpProxies` 

Creates a TargetTcpProxy resource in the specified project using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetTcpProxies/list)` | 

`GET /compute/v1/projects/{project}/global/targetTcpProxies` 

Retrieves the list of `TargetTcpProxy` resources available to the specified project. | 
|

| 

`[setBackendService](/compute/docs/reference/rest/v1/targetTcpProxies/setBackendService)` | 

`POST /compute/v1/projects/{project}/global/targetTcpProxies/{targetTcpProxy}/setBackendService` 

Changes the BackendService for TargetTcpProxy. | 
|

| 

`[setProxyHeader](/compute/docs/reference/rest/v1/targetTcpProxies/setProxyHeader)` | 

`POST /compute/v1/projects/{project}/global/targetTcpProxies/{targetTcpProxy}/setProxyHeader` 

Changes the ProxyHeaderType for TargetTcpProxy. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/v1/targetTcpProxies/aggregatedList)` | 

The method `compute.v1.TargetTcpProxiesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/targetTcpProxies/testIamPermissions)` | 

The method `compute.v1.TargetTcpProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.targetVpnGateways](/compute/docs/reference/rest/v1/targetVpnGateways)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/targetVpnGateways/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/targetVpnGateways` 

Retrieves an aggregated list of target VPN gateways. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/targetVpnGateways/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/targetVpnGateways/{targetVpnGateway}` 

Deletes the specified target VPN gateway. | 
|

| 

`[get](/compute/docs/reference/rest/v1/targetVpnGateways/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/targetVpnGateways/{targetVpnGateway}` 

Returns the specified target VPN gateway. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/targetVpnGateways/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/targetVpnGateways` 

Creates a target VPN gateway in the specified project and region using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/targetVpnGateways/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/targetVpnGateways` 

Retrieves a list of target VPN gateways available to the specified project and region. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/targetVpnGateways/setLabels)` | 

The method `compute.v1.TargetVpnGatewaysService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.urlMaps](/compute/docs/reference/rest/v1/urlMaps)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/urlMaps/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/urlMaps` 

Retrieves the list of all UrlMap resources, regional and global, available to the specified project. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/urlMaps/delete)` | 

`DELETE /compute/v1/projects/{project}/global/urlMaps/{urlMap}` 

Deletes the specified UrlMap resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/urlMaps/get)` | 

`GET /compute/v1/projects/{project}/global/urlMaps/{urlMap}` 

Returns the specified UrlMap resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/urlMaps/insert)` | 

`POST /compute/v1/projects/{project}/global/urlMaps` 

Creates a UrlMap resource in the specified project using the data included in the request. | 
|

| 

`[invalidateCache](/compute/docs/reference/rest/v1/urlMaps/invalidateCache)` | 

`POST /compute/v1/projects/{project}/global/urlMaps/{urlMap}/invalidateCache` 

Initiates a cache invalidation operation, invalidating the specified path, scoped to the specified UrlMap. | 
|

| 

`[list](/compute/docs/reference/rest/v1/urlMaps/list)` | 

`GET /compute/v1/projects/{project}/global/urlMaps` 

Retrieves the list of UrlMap resources available to the specified project. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/urlMaps/patch)` | 

`PATCH /compute/v1/projects/{project}/global/urlMaps/{urlMap}` 

Patches the specified UrlMap resource with the data included in the request. | 
|

| 

`[update](/compute/docs/reference/rest/v1/urlMaps/update)` | 

`PUT /compute/v1/projects/{project}/global/urlMaps/{urlMap}` 

Updates the specified UrlMap resource with the data included in the request. | 
|

| 

`[validate](/compute/docs/reference/rest/v1/urlMaps/validate)` | 

`POST /compute/v1/projects/{project}/global/urlMaps/{urlMap}/validate` 

Runs static validation for the UrlMap. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/urlMaps/testIamPermissions)` | 

The method `compute.v1.UrlMapsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.vpnGateways](/compute/docs/reference/rest/v1/vpnGateways)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/vpnGateways/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/vpnGateways` 

Retrieves an aggregated list of VPN gateways. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/vpnGateways/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/vpnGateways/{vpnGateway}` 

Deletes the specified VPN gateway. | 
|

| 

`[get](/compute/docs/reference/rest/v1/vpnGateways/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/vpnGateways/{vpnGateway}` 

Returns the specified VPN gateway. | 
|

| 

`[getStatus](/compute/docs/reference/rest/v1/vpnGateways/getStatus)` | 

`GET /compute/v1/projects/{project}/regions/{region}/vpnGateways/{vpnGateway}/getStatus` 

Returns the status for the specified VPN gateway. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/vpnGateways/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/vpnGateways` 

Creates a VPN gateway in the specified project and region using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/vpnGateways/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/vpnGateways` 

Retrieves a list of VPN gateways available to the specified project and region. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/vpnGateways/setLabels)` | 

`POST /compute/v1/projects/{project}/regions/{region}/vpnGateways/{resource}/setLabels` 

Sets the labels on a VpnGateway. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/v1/vpnGateways/testIamPermissions)` | 

The method `compute.v1.VpnGatewaysService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.vpnTunnels](/compute/docs/reference/rest/v1/vpnTunnels)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/v1/vpnTunnels/aggregatedList)` | 

`GET /compute/v1/projects/{project}/aggregated/vpnTunnels` 

Retrieves an aggregated list of VPN tunnels. | 
|

| 

`[delete](/compute/docs/reference/rest/v1/vpnTunnels/delete)` | 

`DELETE /compute/v1/projects/{project}/regions/{region}/vpnTunnels/{vpnTunnel}` 

Deletes the specified VpnTunnel resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/vpnTunnels/get)` | 

`GET /compute/v1/projects/{project}/regions/{region}/vpnTunnels/{vpnTunnel}` 

Returns the specified VpnTunnel resource. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/vpnTunnels/insert)` | 

`POST /compute/v1/projects/{project}/regions/{region}/vpnTunnels` 

Creates a VpnTunnel resource in the specified project and region using the data included in the request. | 
|

| 

`[list](/compute/docs/reference/rest/v1/vpnTunnels/list)` | 

`GET /compute/v1/projects/{project}/regions/{region}/vpnTunnels` 

Retrieves a list of VpnTunnel resources contained in the specified project and region. | 
|

| 

`[setLabels](/compute/docs/reference/rest/v1/vpnTunnels/setLabels)` | 

The method `compute.v1.VpnTunnelsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.wireGroups](/compute/docs/reference/rest/v1/wireGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/wireGroups/delete)` | 

The method `compute.v1.WireGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/wireGroups/get)` | 

The method `compute.v1.WireGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/wireGroups/insert)` | 

The method `compute.v1.WireGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/wireGroups/list)` | 

The method `compute.v1.WireGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/v1/wireGroups/patch)` | 

The method `compute.v1.WireGroupsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.zoneOperations](/compute/docs/reference/rest/v1/zoneOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/zoneOperations/delete)` | 

`DELETE /compute/v1/projects/{project}/zones/{zone}/operations/{operation}` 

Deletes the specified zone-specific Operations resource. | 
|

| 

`[get](/compute/docs/reference/rest/v1/zoneOperations/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/operations/{operation}` 

Retrieves the specified zone-specific Operations resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/zoneOperations/list)` | 

`GET /compute/v1/projects/{project}/zones/{zone}/operations` 

Retrieves a list of Operation resources contained within the specified zone. | 
|

| 

`[wait](/compute/docs/reference/rest/v1/zoneOperations/wait)` | 

`POST /compute/v1/projects/{project}/zones/{zone}/operations/{operation}/wait` 

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. | 
|






## REST Resource: [v1.zoneVmExtensionPolicies](/compute/docs/reference/rest/v1/zoneVmExtensionPolicies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/delete)` | 

The method `compute.v1.ZoneVmExtensionPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/get)` | 

The method `compute.v1.ZoneVmExtensionPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/insert)` | 

The method `compute.v1.ZoneVmExtensionPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/list)` | 

The method `compute.v1.ZoneVmExtensionPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/update)` | 

The method `compute.v1.ZoneVmExtensionPoliciesService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [v1.zones](/compute/docs/reference/rest/v1/zones)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/v1/zones/get)` | 

`GET /compute/v1/projects/{project}/zones/{zone}` 

Returns the specified Zone resource. | 
|

| 

`[list](/compute/docs/reference/rest/v1/zones/list)` | 

`GET /compute/v1/projects/{project}/zones` 

Retrieves the list of Zone resources available to the specified project. | 
|






## REST Resource: [beta.acceleratorTypes](/compute/docs/reference/rest/beta/acceleratorTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/acceleratorTypes/aggregatedList)` | 

The method `compute.beta.AcceleratorTypesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/acceleratorTypes/get)` | 

The method `compute.beta.AcceleratorTypesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/acceleratorTypes/list)` | 

The method `compute.beta.AcceleratorTypesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.addresses](/compute/docs/reference/rest/beta/addresses)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/addresses/aggregatedList)` | 

The method `compute.beta.RegionAddressesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/addresses/delete)` | 

The method `compute.beta.RegionAddressesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/addresses/get)` | 

The method `compute.beta.RegionAddressesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/addresses/insert)` | 

The method `compute.beta.RegionAddressesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/addresses/list)` | 

The method `compute.beta.RegionAddressesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[move](/compute/docs/reference/rest/beta/addresses/move)` | 

The method `compute.beta.RegionAddressesService.Move` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/addresses/setLabels)` | 

The method `compute.beta.RegionAddressesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/addresses/testIamPermissions)` | 

The method `compute.beta.RegionAddressesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.advice](/compute/docs/reference/rest/beta/advice)









| 
Methods | 
|



| 

`[calendarMode](/compute/docs/reference/rest/beta/advice/calendarMode)` | 

The method `compute.beta.AdviceService.CalendarMode` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[capacity](/compute/docs/reference/rest/beta/advice/capacity)` | 

The method `compute.beta.AdviceService.Capacity` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[capacityHistory](/compute/docs/reference/rest/beta/advice/capacityHistory)` | 

The method `compute.beta.AdviceService.CapacityHistory` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.autoscalers](/compute/docs/reference/rest/beta/autoscalers)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/autoscalers/aggregatedList)` | 

The method `compute.beta.AutoscalersService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/autoscalers/delete)` | 

The method `compute.beta.AutoscalersService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/autoscalers/get)` | 

The method `compute.beta.AutoscalersService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/autoscalers/insert)` | 

The method `compute.beta.AutoscalersService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/autoscalers/list)` | 

The method `compute.beta.AutoscalersService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/autoscalers/patch)` | 

The method `compute.beta.AutoscalersService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/autoscalers/testIamPermissions)` | 

The method `compute.beta.AutoscalersService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/autoscalers/update)` | 

The method `compute.beta.AutoscalersService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.backendBuckets](/compute/docs/reference/rest/beta/backendBuckets)









| 
Methods | 
|



| 

`[addSignedUrlKey](/compute/docs/reference/rest/beta/backendBuckets/addSignedUrlKey)` | 

The method `compute.beta.BackendBucketsService.AddSignedUrlKey` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/backendBuckets/aggregatedList)` | 

The method `compute.beta.BackendBucketsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/backendBuckets/delete)` | 

The method `compute.beta.BackendBucketsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteSignedUrlKey](/compute/docs/reference/rest/beta/backendBuckets/deleteSignedUrlKey)` | 

The method `compute.beta.BackendBucketsService.DeleteSignedUrlKey` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/backendBuckets/get)` | 

The method `compute.beta.BackendBucketsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/backendBuckets/getIamPolicy)` | 

The method `compute.beta.BackendBucketsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/backendBuckets/insert)` | 

The method `compute.beta.BackendBucketsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/backendBuckets/list)` | 

The method `compute.beta.BackendBucketsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/beta/backendBuckets/listUsable)` | 

The method `compute.beta.BackendBucketsService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/backendBuckets/patch)` | 

The method `compute.beta.BackendBucketsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setEdgeSecurityPolicy](/compute/docs/reference/rest/beta/backendBuckets/setEdgeSecurityPolicy)` | 

The method `compute.beta.BackendBucketsService.SetEdgeSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/backendBuckets/setIamPolicy)` | 

The method `compute.beta.BackendBucketsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/backendBuckets/testIamPermissions)` | 

The method `compute.beta.BackendBucketsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/backendBuckets/update)` | 

The method `compute.beta.BackendBucketsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.backendServices](/compute/docs/reference/rest/beta/backendServices)









| 
Methods | 
|



| 

`[addSignedUrlKey](/compute/docs/reference/rest/beta/backendServices/addSignedUrlKey)` | 

The method `compute.beta.BackendServicesService.AddSignedUrlKey` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/backendServices/aggregatedList)` | 

The method `compute.beta.BackendServicesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/backendServices/delete)` | 

The method `compute.beta.BackendServicesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteSignedUrlKey](/compute/docs/reference/rest/beta/backendServices/deleteSignedUrlKey)` | 

The method `compute.beta.BackendServicesService.DeleteSignedUrlKey` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/backendServices/get)` | 

The method `compute.beta.BackendServicesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getEffectiveSecurityPolicies](/compute/docs/reference/rest/beta/backendServices/getEffectiveSecurityPolicies)` | 

The method `compute.beta.BackendServicesService.GetEffectiveSecurityPolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getHealth](/compute/docs/reference/rest/beta/backendServices/getHealth)` | 

The method `compute.beta.BackendServicesService.GetHealth` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/backendServices/getIamPolicy)` | 

The method `compute.beta.BackendServicesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/backendServices/insert)` | 

The method `compute.beta.BackendServicesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/backendServices/list)` | 

The method `compute.beta.BackendServicesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/beta/backendServices/listUsable)` | 

The method `compute.beta.BackendServicesService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/backendServices/patch)` | 

The method `compute.beta.BackendServicesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setEdgeSecurityPolicy](/compute/docs/reference/rest/beta/backendServices/setEdgeSecurityPolicy)` | 

The method `compute.beta.BackendServicesService.SetEdgeSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/backendServices/setIamPolicy)` | 

The method `compute.beta.BackendServicesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/beta/backendServices/setSecurityPolicy)` | 

The method `compute.beta.BackendServicesService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/backendServices/testIamPermissions)` | 

The method `compute.beta.BackendServicesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/backendServices/update)` | 

The method `compute.beta.BackendServicesService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.crossSiteNetworks](/compute/docs/reference/rest/beta/crossSiteNetworks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/crossSiteNetworks/delete)` | 

The method `compute.beta.CrossSiteNetworksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/crossSiteNetworks/get)` | 

The method `compute.beta.CrossSiteNetworksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/crossSiteNetworks/insert)` | 

The method `compute.beta.CrossSiteNetworksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/crossSiteNetworks/list)` | 

The method `compute.beta.CrossSiteNetworksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/crossSiteNetworks/patch)` | 

The method `compute.beta.CrossSiteNetworksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.diskSettings](/compute/docs/reference/rest/beta/diskSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/diskSettings/get)` | 

The method `compute.beta.DiskSettingsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/diskSettings/patch)` | 

The method `compute.beta.DiskSettingsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.diskTypes](/compute/docs/reference/rest/beta/diskTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/diskTypes/aggregatedList)` | 

The method `compute.beta.DiskTypesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/diskTypes/get)` | 

The method `compute.beta.DiskTypesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/diskTypes/list)` | 

The method `compute.beta.DiskTypesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.disks](/compute/docs/reference/rest/beta/disks)









| 
Methods | 
|



| 

`[addResourcePolicies](/compute/docs/reference/rest/beta/disks/addResourcePolicies)` | 

The method `compute.beta.DisksService.AddResourcePolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/disks/aggregatedList)` | 

The method `compute.beta.DisksService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[bulkInsert](/compute/docs/reference/rest/beta/disks/bulkInsert)` | 

The method `compute.beta.DisksService.BulkInsert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[bulkSetLabels](/compute/docs/reference/rest/beta/disks/bulkSetLabels)` | 

The method `compute.beta.DisksService.BulkSetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[createSnapshot](/compute/docs/reference/rest/beta/disks/createSnapshot)` | 

The method `compute.beta.DisksService.CreateSnapshot` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/disks/delete)` | 

The method `compute.beta.DisksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/disks/get)` | 

The method `compute.beta.DisksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/disks/getIamPolicy)` | 

The method `compute.beta.DisksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/disks/insert)` | 

The method `compute.beta.DisksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/disks/list)` | 

The method `compute.beta.DisksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeResourcePolicies](/compute/docs/reference/rest/beta/disks/removeResourcePolicies)` | 

The method `compute.beta.DisksService.RemoveResourcePolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resize](/compute/docs/reference/rest/beta/disks/resize)` | 

The method `compute.beta.DisksService.Resize` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/disks/setIamPolicy)` | 

The method `compute.beta.DisksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/disks/setLabels)` | 

The method `compute.beta.DisksService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startAsyncReplication](/compute/docs/reference/rest/beta/disks/startAsyncReplication)` | 

The method `compute.beta.DisksService.StartAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopAsyncReplication](/compute/docs/reference/rest/beta/disks/stopAsyncReplication)` | 

The method `compute.beta.DisksService.StopAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopGroupAsyncReplication](/compute/docs/reference/rest/beta/disks/stopGroupAsyncReplication)` | 

The method `compute.beta.DisksService.StopGroupAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/disks/testIamPermissions)` | 

The method `compute.beta.DisksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/disks/update)` | 

The method `compute.beta.DisksService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateKmsKey](/compute/docs/reference/rest/beta/disks/updateKmsKey)` | 

The method `compute.beta.DisksService.UpdateKmsKey` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.externalVpnGateways](/compute/docs/reference/rest/beta/externalVpnGateways)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/externalVpnGateways/delete)` | 

The method `compute.beta.ExternalVpnGatewaysService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/externalVpnGateways/get)` | 

The method `compute.beta.ExternalVpnGatewaysService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/externalVpnGateways/insert)` | 

The method `compute.beta.ExternalVpnGatewaysService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/externalVpnGateways/list)` | 

The method `compute.beta.ExternalVpnGatewaysService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/externalVpnGateways/setLabels)` | 

The method `compute.beta.ExternalVpnGatewaysService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/externalVpnGateways/testIamPermissions)` | 

The method `compute.beta.ExternalVpnGatewaysService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.firewallPolicies](/compute/docs/reference/rest/beta/firewallPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/beta/firewallPolicies/addAssociation)` | 

The method `compute.beta.FirewallPoliciesService.AddAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addPacketMirroringRule](/compute/docs/reference/rest/beta/firewallPolicies/addPacketMirroringRule)` | 

The method `compute.beta.FirewallPoliciesService.AddPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addRule](/compute/docs/reference/rest/beta/firewallPolicies/addRule)` | 

The method `compute.beta.FirewallPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cloneRules](/compute/docs/reference/rest/beta/firewallPolicies/cloneRules)` | 

The method `compute.beta.FirewallPoliciesService.CloneRules` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/firewallPolicies/delete)` | 

The method `compute.beta.FirewallPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/firewallPolicies/get)` | 

The method `compute.beta.FirewallPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/beta/firewallPolicies/getAssociation)` | 

The method `compute.beta.FirewallPoliciesService.GetAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/firewallPolicies/getIamPolicy)` | 

The method `compute.beta.FirewallPoliciesService.GetOrganizationPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getPacketMirroringRule](/compute/docs/reference/rest/beta/firewallPolicies/getPacketMirroringRule)` | 

The method `compute.beta.FirewallPoliciesService.GetPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/beta/firewallPolicies/getRule)` | 

The method `compute.beta.FirewallPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/firewallPolicies/insert)` | 

The method `compute.beta.FirewallPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/firewallPolicies/list)` | 

The method `compute.beta.FirewallPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listAssociations](/compute/docs/reference/rest/beta/firewallPolicies/listAssociations)` | 

The method `compute.beta.FirewallPoliciesService.ListAssociations` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[move](/compute/docs/reference/rest/beta/firewallPolicies/move)` | 

The method `compute.beta.FirewallPoliciesService.Move` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/firewallPolicies/patch)` | 

The method `compute.beta.FirewallPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchPacketMirroringRule](/compute/docs/reference/rest/beta/firewallPolicies/patchPacketMirroringRule)` | 

The method `compute.beta.FirewallPoliciesService.PatchPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/beta/firewallPolicies/patchRule)` | 

The method `compute.beta.FirewallPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/beta/firewallPolicies/removeAssociation)` | 

The method `compute.beta.FirewallPoliciesService.RemoveAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removePacketMirroringRule](/compute/docs/reference/rest/beta/firewallPolicies/removePacketMirroringRule)` | 

The method `compute.beta.FirewallPoliciesService.RemovePacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/beta/firewallPolicies/removeRule)` | 

The method `compute.beta.FirewallPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/firewallPolicies/setIamPolicy)` | 

The method `compute.beta.FirewallPoliciesService.SetOrganizationPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/firewallPolicies/testIamPermissions)` | 

The method `compute.beta.FirewallPoliciesService.TestOrganizationPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.firewalls](/compute/docs/reference/rest/beta/firewalls)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/firewalls/delete)` | 

The method `compute.beta.FirewallsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/firewalls/get)` | 

The method `compute.beta.FirewallsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/firewalls/insert)` | 

The method `compute.beta.FirewallsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/firewalls/list)` | 

The method `compute.beta.FirewallsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/firewalls/patch)` | 

The method `compute.beta.FirewallsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/firewalls/testIamPermissions)` | 

The method `compute.beta.FirewallsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/firewalls/update)` | 

The method `compute.beta.FirewallsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.forwardingRules](/compute/docs/reference/rest/beta/forwardingRules)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/forwardingRules/aggregatedList)` | 

The method `compute.beta.RegionForwardingRulesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/forwardingRules/delete)` | 

The method `compute.beta.RegionForwardingRulesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/forwardingRules/get)` | 

The method `compute.beta.RegionForwardingRulesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/forwardingRules/insert)` | 

The method `compute.beta.RegionForwardingRulesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/forwardingRules/list)` | 

The method `compute.beta.RegionForwardingRulesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/forwardingRules/patch)` | 

The method `compute.beta.RegionForwardingRulesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/forwardingRules/setLabels)` | 

The method `compute.beta.RegionForwardingRulesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setTarget](/compute/docs/reference/rest/beta/forwardingRules/setTarget)` | 

The method `compute.beta.RegionForwardingRulesService.SetTarget` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/forwardingRules/testIamPermissions)` | 

The method `compute.beta.RegionForwardingRulesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.futureReservations](/compute/docs/reference/rest/beta/futureReservations)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/futureReservations/aggregatedList)` | 

The method `compute.beta.FutureReservationsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cancel](/compute/docs/reference/rest/beta/futureReservations/cancel)` | 

The method `compute.beta.FutureReservationsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/futureReservations/delete)` | 

The method `compute.beta.FutureReservationsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/futureReservations/get)` | 

The method `compute.beta.FutureReservationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/futureReservations/insert)` | 

The method `compute.beta.FutureReservationsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/futureReservations/list)` | 

The method `compute.beta.FutureReservationsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/futureReservations/update)` | 

The method `compute.beta.FutureReservationsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.globalAddresses](/compute/docs/reference/rest/beta/globalAddresses)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/globalAddresses/delete)` | 

The method `compute.beta.GlobalAddressesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/globalAddresses/get)` | 

The method `compute.beta.GlobalAddressesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/globalAddresses/insert)` | 

The method `compute.beta.GlobalAddressesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/globalAddresses/list)` | 

The method `compute.beta.GlobalAddressesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[move](/compute/docs/reference/rest/beta/globalAddresses/move)` | 

The method `compute.beta.GlobalAddressesService.Move` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/globalAddresses/setLabels)` | 

The method `compute.beta.GlobalAddressesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/globalAddresses/testIamPermissions)` | 

The method `compute.beta.GlobalAddressesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.globalForwardingRules](/compute/docs/reference/rest/beta/globalForwardingRules)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/globalForwardingRules/delete)` | 

The method `compute.beta.GlobalForwardingRulesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/globalForwardingRules/get)` | 

The method `compute.beta.GlobalForwardingRulesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/globalForwardingRules/insert)` | 

The method `compute.beta.GlobalForwardingRulesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/globalForwardingRules/list)` | 

The method `compute.beta.GlobalForwardingRulesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/globalForwardingRules/patch)` | 

The method `compute.beta.GlobalForwardingRulesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/globalForwardingRules/setLabels)` | 

The method `compute.beta.GlobalForwardingRulesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setTarget](/compute/docs/reference/rest/beta/globalForwardingRules/setTarget)` | 

The method `compute.beta.GlobalForwardingRulesService.SetTarget` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/globalForwardingRules/testIamPermissions)` | 

The method `compute.beta.GlobalForwardingRulesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.globalNetworkEndpointGroups](/compute/docs/reference/rest/beta/globalNetworkEndpointGroups)









| 
Methods | 
|



| 

`[attachNetworkEndpoints](/compute/docs/reference/rest/beta/globalNetworkEndpointGroups/attachNetworkEndpoints)` | 

The method `compute.beta.GlobalNetworkEndpointGroupsService.AttachNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/globalNetworkEndpointGroups/delete)` | 

The method `compute.beta.GlobalNetworkEndpointGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[detachNetworkEndpoints](/compute/docs/reference/rest/beta/globalNetworkEndpointGroups/detachNetworkEndpoints)` | 

The method `compute.beta.GlobalNetworkEndpointGroupsService.DetachNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/globalNetworkEndpointGroups/get)` | 

The method `compute.beta.GlobalNetworkEndpointGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/globalNetworkEndpointGroups/insert)` | 

The method `compute.beta.GlobalNetworkEndpointGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/globalNetworkEndpointGroups/list)` | 

The method `compute.beta.GlobalNetworkEndpointGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listNetworkEndpoints](/compute/docs/reference/rest/beta/globalNetworkEndpointGroups/listNetworkEndpoints)` | 

The method `compute.beta.GlobalNetworkEndpointGroupsService.ListNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.globalOperations](/compute/docs/reference/rest/beta/globalOperations)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/globalOperations/aggregatedList)` | 

The method `compute.beta.GlobalOperationsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/globalOperations/delete)` | 

The method `compute.beta.GlobalOperationsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/globalOperations/get)` | 

The method `compute.beta.GlobalOperationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/globalOperations/list)` | 

The method `compute.beta.GlobalOperationsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[wait](/compute/docs/reference/rest/beta/globalOperations/wait)` | 

The method `compute.beta.GlobalOperationsService.Wait` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.globalOrganizationOperations](/compute/docs/reference/rest/beta/globalOrganizationOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/globalOrganizationOperations/delete)` | 

The method `compute.beta.GlobalOrganizationOperationsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/globalOrganizationOperations/get)` | 

The method `compute.beta.GlobalOrganizationOperationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/globalOrganizationOperations/list)` | 

The method `compute.beta.GlobalOrganizationOperationsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.globalPublicDelegatedPrefixes](/compute/docs/reference/rest/beta/globalPublicDelegatedPrefixes)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/globalPublicDelegatedPrefixes/delete)` | 

The method `compute.beta.GlobalPublicDelegatedPrefixesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/globalPublicDelegatedPrefixes/get)` | 

The method `compute.beta.GlobalPublicDelegatedPrefixesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/globalPublicDelegatedPrefixes/insert)` | 

The method `compute.beta.GlobalPublicDelegatedPrefixesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/globalPublicDelegatedPrefixes/list)` | 

The method `compute.beta.GlobalPublicDelegatedPrefixesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/globalPublicDelegatedPrefixes/patch)` | 

The method `compute.beta.GlobalPublicDelegatedPrefixesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.globalVmExtensionPolicies](/compute/docs/reference/rest/beta/globalVmExtensionPolicies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/globalVmExtensionPolicies/aggregatedList)` | 

The method `compute.beta.GlobalVmExtensionPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/globalVmExtensionPolicies/delete)` | 

The method `compute.beta.GlobalVmExtensionPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/globalVmExtensionPolicies/get)` | 

The method `compute.beta.GlobalVmExtensionPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/globalVmExtensionPolicies/insert)` | 

The method `compute.beta.GlobalVmExtensionPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/globalVmExtensionPolicies/list)` | 

The method `compute.beta.GlobalVmExtensionPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/globalVmExtensionPolicies/update)` | 

The method `compute.beta.GlobalVmExtensionPoliciesService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.healthChecks](/compute/docs/reference/rest/beta/healthChecks)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/healthChecks/aggregatedList)` | 

The method `compute.beta.HealthChecksService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/healthChecks/delete)` | 

The method `compute.beta.HealthChecksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/healthChecks/get)` | 

The method `compute.beta.HealthChecksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/healthChecks/insert)` | 

The method `compute.beta.HealthChecksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/healthChecks/list)` | 

The method `compute.beta.HealthChecksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/healthChecks/patch)` | 

The method `compute.beta.HealthChecksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/healthChecks/testIamPermissions)` | 

The method `compute.beta.HealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/healthChecks/update)` | 

The method `compute.beta.HealthChecksService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.hosts](/compute/docs/reference/rest/beta/hosts)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/hosts/get)` | 

The method `compute.beta.HostsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getVersion](/compute/docs/reference/rest/beta/hosts/getVersion)` | 

The method `compute.beta.HostsService.GetVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/hosts/list)` | 

The method `compute.beta.HostsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.httpHealthChecks](/compute/docs/reference/rest/beta/httpHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/httpHealthChecks/delete)` | 

The method `compute.beta.HttpHealthChecksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/httpHealthChecks/get)` | 

The method `compute.beta.HttpHealthChecksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/httpHealthChecks/insert)` | 

The method `compute.beta.HttpHealthChecksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/httpHealthChecks/list)` | 

The method `compute.beta.HttpHealthChecksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/httpHealthChecks/patch)` | 

The method `compute.beta.HttpHealthChecksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/httpHealthChecks/testIamPermissions)` | 

The method `compute.beta.HttpHealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/httpHealthChecks/update)` | 

The method `compute.beta.HttpHealthChecksService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.httpsHealthChecks](/compute/docs/reference/rest/beta/httpsHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/httpsHealthChecks/delete)` | 

The method `compute.beta.HttpsHealthChecksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/httpsHealthChecks/get)` | 

The method `compute.beta.HttpsHealthChecksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/httpsHealthChecks/insert)` | 

The method `compute.beta.HttpsHealthChecksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/httpsHealthChecks/list)` | 

The method `compute.beta.HttpsHealthChecksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/httpsHealthChecks/patch)` | 

The method `compute.beta.HttpsHealthChecksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/httpsHealthChecks/testIamPermissions)` | 

The method `compute.beta.HttpsHealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/httpsHealthChecks/update)` | 

The method `compute.beta.HttpsHealthChecksService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.imageFamilyViews](/compute/docs/reference/rest/beta/imageFamilyViews)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/imageFamilyViews/get)` | 

The method `compute.beta.ImageFamilyViewsService.Get` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.imageViews](/compute/docs/reference/rest/beta/imageViews)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/imageViews/get)` | 

The method `compute.beta.ImageViewsService.Get` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.images](/compute/docs/reference/rest/beta/images)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/images/delete)` | 

The method `compute.beta.ImagesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deprecate](/compute/docs/reference/rest/beta/images/deprecate)` | 

The method `compute.beta.ImagesService.Deprecate` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/images/get)` | 

The method `compute.beta.ImagesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getFromFamily](/compute/docs/reference/rest/beta/images/getFromFamily)` | 

The method `compute.beta.ImagesService.GetFromFamily` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/images/getIamPolicy)` | 

The method `compute.beta.ImagesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/images/insert)` | 

The method `compute.beta.ImagesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/images/list)` | 

The method `compute.beta.ImagesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/images/patch)` | 

The method `compute.beta.ImagesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/images/setIamPolicy)` | 

The method `compute.beta.ImagesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/images/setLabels)` | 

The method `compute.beta.ImagesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/images/testIamPermissions)` | 

The method `compute.beta.ImagesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.instanceGroupManagerResizeRequests](/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests)









| 
Methods | 
|



| 

`[cancel](/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/cancel)` | 

The method `compute.beta.InstanceGroupManagerResizeRequestsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/delete)` | 

The method `compute.beta.InstanceGroupManagerResizeRequestsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/get)` | 

The method `compute.beta.InstanceGroupManagerResizeRequestsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/insert)` | 

The method `compute.beta.InstanceGroupManagerResizeRequestsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/list)` | 

The method `compute.beta.InstanceGroupManagerResizeRequestsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.instanceGroupManagers](/compute/docs/reference/rest/beta/instanceGroupManagers)









| 
Methods | 
|



| 

`[abandonInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/abandonInstances)` | 

The method `compute.beta.InstanceGroupManagersService.AbandonInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/instanceGroupManagers/aggregatedList)` | 

The method `compute.beta.InstanceGroupManagersService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[applyUpdatesToInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/applyUpdatesToInstances)` | 

The method `compute.beta.InstanceGroupManagersService.ApplyUpdatesToInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[configureAcceleratorTopologies](/compute/docs/reference/rest/beta/instanceGroupManagers/configureAcceleratorTopologies)` | 

The method `compute.beta.InstanceGroupManagersService.ConfigureAcceleratorTopologies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[createInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/createInstances)` | 

The method `compute.beta.InstanceGroupManagersService.CreateInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/instanceGroupManagers/delete)` | 

The method `compute.beta.InstanceGroupManagersService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/deleteInstances)` | 

The method `compute.beta.InstanceGroupManagersService.DeleteInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deletePerInstanceConfigs](/compute/docs/reference/rest/beta/instanceGroupManagers/deletePerInstanceConfigs)` | 

The method `compute.beta.InstanceGroupManagersService.DeletePerInstanceConfigs` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/instanceGroupManagers/get)` | 

The method `compute.beta.InstanceGroupManagersService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAvailableAcceleratorTopologies](/compute/docs/reference/rest/beta/instanceGroupManagers/getAvailableAcceleratorTopologies)` | 

The method `compute.beta.InstanceGroupManagersService.GetAvailableAcceleratorTopologies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/instanceGroupManagers/insert)` | 

The method `compute.beta.InstanceGroupManagersService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/instanceGroupManagers/list)` | 

The method `compute.beta.InstanceGroupManagersService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listErrors](/compute/docs/reference/rest/beta/instanceGroupManagers/listErrors)` | 

The method `compute.beta.InstanceGroupManagersService.ListErrors` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listManagedInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/listManagedInstances)` | 

The method `compute.beta.InstanceGroupManagersService.ListManagedInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listPerInstanceConfigs](/compute/docs/reference/rest/beta/instanceGroupManagers/listPerInstanceConfigs)` | 

The method `compute.beta.InstanceGroupManagersService.ListPerInstanceConfigs` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/instanceGroupManagers/patch)` | 

The method `compute.beta.InstanceGroupManagersService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchPerInstanceConfigs](/compute/docs/reference/rest/beta/instanceGroupManagers/patchPerInstanceConfigs)` | 

The method `compute.beta.InstanceGroupManagersService.PatchPerInstanceConfigs` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[recreateInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/recreateInstances)` | 

The method `compute.beta.InstanceGroupManagersService.RecreateInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resize](/compute/docs/reference/rest/beta/instanceGroupManagers/resize)` | 

The method `compute.beta.InstanceGroupManagersService.Resize` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resizeAdvanced](/compute/docs/reference/rest/beta/instanceGroupManagers/resizeAdvanced)` | 

The method `compute.beta.InstanceGroupManagersService.ResizeAdvanced` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resumeInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/resumeInstances)` | 

The method `compute.beta.InstanceGroupManagersService.ResumeInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setAutoHealingPolicies](/compute/docs/reference/rest/beta/instanceGroupManagers/setAutoHealingPolicies) 
**(deprecated)**` | 

The method `compute.beta.InstanceGroupManagersService.SetAutoHealingPolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setInstanceTemplate](/compute/docs/reference/rest/beta/instanceGroupManagers/setInstanceTemplate)` | 

The method `compute.beta.InstanceGroupManagersService.SetInstanceTemplate` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setTargetPools](/compute/docs/reference/rest/beta/instanceGroupManagers/setTargetPools)` | 

The method `compute.beta.InstanceGroupManagersService.SetTargetPools` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/startInstances)` | 

The method `compute.beta.InstanceGroupManagersService.StartInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/stopInstances)` | 

The method `compute.beta.InstanceGroupManagersService.StopInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[suspendInstances](/compute/docs/reference/rest/beta/instanceGroupManagers/suspendInstances)` | 

The method `compute.beta.InstanceGroupManagersService.SuspendInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/instanceGroupManagers/testIamPermissions)` | 

The method `compute.beta.InstanceGroupManagersService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/instanceGroupManagers/update)` | 

The method `compute.beta.InstanceGroupManagersService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updatePerInstanceConfigs](/compute/docs/reference/rest/beta/instanceGroupManagers/updatePerInstanceConfigs)` | 

The method `compute.beta.InstanceGroupManagersService.UpdatePerInstanceConfigs` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.instanceGroups](/compute/docs/reference/rest/beta/instanceGroups)









| 
Methods | 
|



| 

`[addInstances](/compute/docs/reference/rest/beta/instanceGroups/addInstances)` | 

The method `compute.beta.InstanceGroupsService.AddInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/instanceGroups/aggregatedList)` | 

The method `compute.beta.InstanceGroupsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/instanceGroups/delete)` | 

The method `compute.beta.InstanceGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/instanceGroups/get)` | 

The method `compute.beta.InstanceGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/instanceGroups/insert)` | 

The method `compute.beta.InstanceGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/instanceGroups/list)` | 

The method `compute.beta.InstanceGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listInstances](/compute/docs/reference/rest/beta/instanceGroups/listInstances)` | 

The method `compute.beta.InstanceGroupsService.ListInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeInstances](/compute/docs/reference/rest/beta/instanceGroups/removeInstances)` | 

The method `compute.beta.InstanceGroupsService.RemoveInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setNamedPorts](/compute/docs/reference/rest/beta/instanceGroups/setNamedPorts)` | 

The method `compute.beta.InstanceGroupsService.SetNamedPorts` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/instanceGroups/testIamPermissions)` | 

The method `compute.beta.InstanceGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.instanceSettings](/compute/docs/reference/rest/beta/instanceSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/instanceSettings/get)` | 

The method `compute.beta.InstanceSettingsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/instanceSettings/patch)` | 

The method `compute.beta.InstanceSettingsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.instanceTemplates](/compute/docs/reference/rest/beta/instanceTemplates)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/instanceTemplates/aggregatedList)` | 

The method `compute.beta.InstanceTemplatesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/instanceTemplates/delete)` | 

The method `compute.beta.InstanceTemplatesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/instanceTemplates/get)` | 

The method `compute.beta.InstanceTemplatesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/instanceTemplates/getIamPolicy)` | 

The method `compute.beta.InstanceTemplatesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/instanceTemplates/insert)` | 

The method `compute.beta.InstanceTemplatesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/instanceTemplates/list)` | 

The method `compute.beta.InstanceTemplatesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/instanceTemplates/setIamPolicy)` | 

The method `compute.beta.InstanceTemplatesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/instanceTemplates/testIamPermissions)` | 

The method `compute.beta.InstanceTemplatesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.instances](/compute/docs/reference/rest/beta/instances)









| 
Methods | 
|



| 

`[addAccessConfig](/compute/docs/reference/rest/beta/instances/addAccessConfig)` | 

The method `compute.beta.InstancesService.AddAccessConfig` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addNetworkInterface](/compute/docs/reference/rest/beta/instances/addNetworkInterface)` | 

The method `compute.beta.InstancesService.AddNetworkInterface` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addResourcePolicies](/compute/docs/reference/rest/beta/instances/addResourcePolicies)` | 

The method `compute.beta.InstancesService.AddResourcePolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/instances/aggregatedList)` | 

The method `compute.beta.InstancesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[attachDisk](/compute/docs/reference/rest/beta/instances/attachDisk)` | 

The method `compute.beta.InstancesService.AttachDisk` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[bulkInsert](/compute/docs/reference/rest/beta/instances/bulkInsert)` | 

The method `compute.beta.InstancesService.BulkInsert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/instances/delete)` | 

The method `compute.beta.InstancesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteAccessConfig](/compute/docs/reference/rest/beta/instances/deleteAccessConfig)` | 

The method `compute.beta.InstancesService.DeleteAccessConfig` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteNetworkInterface](/compute/docs/reference/rest/beta/instances/deleteNetworkInterface)` | 

The method `compute.beta.InstancesService.DeleteNetworkInterface` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[detachDisk](/compute/docs/reference/rest/beta/instances/detachDisk)` | 

The method `compute.beta.InstancesService.DetachDisk` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/instances/get)` | 

The method `compute.beta.InstancesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getEffectiveFirewalls](/compute/docs/reference/rest/beta/instances/getEffectiveFirewalls)` | 

The method `compute.beta.InstancesService.GetEffectiveFirewalls` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getGuestAttributes](/compute/docs/reference/rest/beta/instances/getGuestAttributes)` | 

The method `compute.beta.InstancesService.GetGuestAttributes` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/instances/getIamPolicy)` | 

The method `compute.beta.InstancesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getPartnerMetadata](/compute/docs/reference/rest/beta/instances/getPartnerMetadata)` | 

The method `compute.beta.InstancesService.GetPartnerMetadata` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getScreenshot](/compute/docs/reference/rest/beta/instances/getScreenshot)` | 

The method `compute.beta.InstancesService.GetScreenshot` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getSerialPortOutput](/compute/docs/reference/rest/beta/instances/getSerialPortOutput)` | 

The method `compute.beta.InstancesService.GetSerialPortOutput` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getShieldedInstanceIdentity](/compute/docs/reference/rest/beta/instances/getShieldedInstanceIdentity)` | 

The method `compute.beta.InstancesService.GetShieldedInstanceIdentity` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getShieldedVmIdentity](/compute/docs/reference/rest/beta/instances/getShieldedVmIdentity)` | 

The method `compute.beta.InstancesService.GetShieldedVmIdentity` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/instances/insert)` | 

The method `compute.beta.InstancesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/instances/list)` | 

The method `compute.beta.InstancesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listReferrers](/compute/docs/reference/rest/beta/instances/listReferrers)` | 

The method `compute.beta.InstancesService.ListReferrers` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchPartnerMetadata](/compute/docs/reference/rest/beta/instances/patchPartnerMetadata)` | 

The method `compute.beta.InstancesService.PatchPartnerMetadata` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/beta/instances/performMaintenance)` | 

The method `compute.beta.InstancesService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeResourcePolicies](/compute/docs/reference/rest/beta/instances/removeResourcePolicies)` | 

The method `compute.beta.InstancesService.RemoveResourcePolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[reportHostAsFaulty](/compute/docs/reference/rest/beta/instances/reportHostAsFaulty)` | 

The method `compute.beta.InstancesService.ReportHostAsFaulty` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[reset](/compute/docs/reference/rest/beta/instances/reset)` | 

The method `compute.beta.InstancesService.Reset` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resume](/compute/docs/reference/rest/beta/instances/resume)` | 

The method `compute.beta.InstancesService.Resume` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[sendDiagnosticInterrupt](/compute/docs/reference/rest/beta/instances/sendDiagnosticInterrupt)` | 

The method `compute.beta.InstancesService.SendDiagnosticInterrupt` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setDeletionProtection](/compute/docs/reference/rest/beta/instances/setDeletionProtection)` | 

The method `compute.beta.InstancesService.SetDeletionProtection` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setDiskAutoDelete](/compute/docs/reference/rest/beta/instances/setDiskAutoDelete)` | 

The method `compute.beta.InstancesService.SetDiskAutoDelete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/instances/setIamPolicy)` | 

The method `compute.beta.InstancesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/instances/setLabels)` | 

The method `compute.beta.InstancesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setMachineResources](/compute/docs/reference/rest/beta/instances/setMachineResources)` | 

The method `compute.beta.InstancesService.SetMachineResources` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setMachineType](/compute/docs/reference/rest/beta/instances/setMachineType)` | 

The method `compute.beta.InstancesService.SetMachineType` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setMetadata](/compute/docs/reference/rest/beta/instances/setMetadata)` | 

The method `compute.beta.InstancesService.SetMetadata` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setMinCpuPlatform](/compute/docs/reference/rest/beta/instances/setMinCpuPlatform)` | 

The method `compute.beta.InstancesService.SetMinCpuPlatform` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setName](/compute/docs/reference/rest/beta/instances/setName)` | 

The method `compute.beta.InstancesService.SetName` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setScheduling](/compute/docs/reference/rest/beta/instances/setScheduling)` | 

The method `compute.beta.InstancesService.SetScheduling` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/beta/instances/setSecurityPolicy)` | 

The method `compute.beta.InstancesService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setServiceAccount](/compute/docs/reference/rest/beta/instances/setServiceAccount)` | 

The method `compute.beta.InstancesService.SetServiceAccount` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setShieldedInstanceIntegrityPolicy](/compute/docs/reference/rest/beta/instances/setShieldedInstanceIntegrityPolicy)` | 

The method `compute.beta.InstancesService.SetShieldedInstanceIntegrityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setShieldedVmIntegrityPolicy](/compute/docs/reference/rest/beta/instances/setShieldedVmIntegrityPolicy)` | 

The method `compute.beta.InstancesService.SetShieldedVmIntegrityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setTags](/compute/docs/reference/rest/beta/instances/setTags)` | 

The method `compute.beta.InstancesService.SetTags` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[simulateMaintenanceEvent](/compute/docs/reference/rest/beta/instances/simulateMaintenanceEvent)` | 

The method `compute.beta.InstancesService.SimulateMaintenanceEvent` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[start](/compute/docs/reference/rest/beta/instances/start)` | 

The method `compute.beta.InstancesService.Start` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startWithEncryptionKey](/compute/docs/reference/rest/beta/instances/startWithEncryptionKey)` | 

The method `compute.beta.InstancesService.StartWithEncryptionKey` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stop](/compute/docs/reference/rest/beta/instances/stop)` | 

The method `compute.beta.InstancesService.Stop` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[suspend](/compute/docs/reference/rest/beta/instances/suspend)` | 

The method `compute.beta.InstancesService.Suspend` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/instances/testIamPermissions)` | 

The method `compute.beta.InstancesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/instances/update)` | 

The method `compute.beta.InstancesService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateAccessConfig](/compute/docs/reference/rest/beta/instances/updateAccessConfig)` | 

The method `compute.beta.InstancesService.UpdateAccessConfig` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateDisplayDevice](/compute/docs/reference/rest/beta/instances/updateDisplayDevice)` | 

The method `compute.beta.InstancesService.UpdateDisplayDevice` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateNetworkInterface](/compute/docs/reference/rest/beta/instances/updateNetworkInterface)` | 

The method `compute.beta.InstancesService.UpdateNetworkInterface` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateShieldedInstanceConfig](/compute/docs/reference/rest/beta/instances/updateShieldedInstanceConfig)` | 

The method `compute.beta.InstancesService.UpdateShieldedInstanceConfig` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateShieldedVmConfig](/compute/docs/reference/rest/beta/instances/updateShieldedVmConfig)` | 

The method `compute.beta.InstancesService.UpdateShieldedVmConfig` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.instantSnapshotGroups](/compute/docs/reference/rest/beta/instantSnapshotGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/instantSnapshotGroups/delete)` | 

The method `compute.beta.InstantSnapshotGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/instantSnapshotGroups/get)` | 

The method `compute.beta.InstantSnapshotGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/instantSnapshotGroups/getIamPolicy)` | 

The method `compute.beta.InstantSnapshotGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/instantSnapshotGroups/insert)` | 

The method `compute.beta.InstantSnapshotGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/instantSnapshotGroups/list)` | 

The method `compute.beta.InstantSnapshotGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/instantSnapshotGroups/setIamPolicy)` | 

The method `compute.beta.InstantSnapshotGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/instantSnapshotGroups/testIamPermissions)` | 

The method `compute.beta.InstantSnapshotGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.instantSnapshots](/compute/docs/reference/rest/beta/instantSnapshots)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/instantSnapshots/aggregatedList)` | 

The method `compute.beta.InstantSnapshotsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/instantSnapshots/delete)` | 

The method `compute.beta.InstantSnapshotsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/instantSnapshots/get)` | 

The method `compute.beta.InstantSnapshotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/instantSnapshots/getIamPolicy)` | 

The method `compute.beta.InstantSnapshotsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/instantSnapshots/insert)` | 

The method `compute.beta.InstantSnapshotsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/instantSnapshots/list)` | 

The method `compute.beta.InstantSnapshotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/instantSnapshots/setIamPolicy)` | 

The method `compute.beta.InstantSnapshotsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/instantSnapshots/setLabels)` | 

The method `compute.beta.InstantSnapshotsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/instantSnapshots/testIamPermissions)` | 

The method `compute.beta.InstantSnapshotsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.interconnectAttachmentGroups](/compute/docs/reference/rest/beta/interconnectAttachmentGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/delete)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/get)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/getIamPolicy)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getOperationalStatus](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/getOperationalStatus)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.GetOperationalStatus` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/insert)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/list)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/patch)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/setIamPolicy)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/interconnectAttachmentGroups/testIamPermissions)` | 

The method `compute.beta.InterconnectAttachmentGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.interconnectAttachments](/compute/docs/reference/rest/beta/interconnectAttachments)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/interconnectAttachments/aggregatedList)` | 

The method `compute.beta.InterconnectAttachmentsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/interconnectAttachments/delete)` | 

The method `compute.beta.InterconnectAttachmentsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/interconnectAttachments/get)` | 

The method `compute.beta.InterconnectAttachmentsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/interconnectAttachments/insert)` | 

The method `compute.beta.InterconnectAttachmentsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/interconnectAttachments/list)` | 

The method `compute.beta.InterconnectAttachmentsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/interconnectAttachments/patch)` | 

The method `compute.beta.InterconnectAttachmentsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/interconnectAttachments/setLabels)` | 

The method `compute.beta.InterconnectAttachmentsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/interconnectAttachments/testIamPermissions)` | 

The method `compute.beta.InterconnectAttachmentsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.interconnectGroups](/compute/docs/reference/rest/beta/interconnectGroups)









| 
Methods | 
|



| 

`[createMembers](/compute/docs/reference/rest/beta/interconnectGroups/createMembers)` | 

The method `compute.beta.InterconnectGroupsService.CreateMembers` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/interconnectGroups/delete)` | 

The method `compute.beta.InterconnectGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/interconnectGroups/get)` | 

The method `compute.beta.InterconnectGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/interconnectGroups/getIamPolicy)` | 

The method `compute.beta.InterconnectGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getOperationalStatus](/compute/docs/reference/rest/beta/interconnectGroups/getOperationalStatus)` | 

The method `compute.beta.InterconnectGroupsService.GetOperationalStatus` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/interconnectGroups/insert)` | 

The method `compute.beta.InterconnectGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/interconnectGroups/list)` | 

The method `compute.beta.InterconnectGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/interconnectGroups/patch)` | 

The method `compute.beta.InterconnectGroupsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/interconnectGroups/setIamPolicy)` | 

The method `compute.beta.InterconnectGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/interconnectGroups/testIamPermissions)` | 

The method `compute.beta.InterconnectGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.interconnectLocations](/compute/docs/reference/rest/beta/interconnectLocations)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/interconnectLocations/get)` | 

The method `compute.beta.InterconnectLocationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/interconnectLocations/list)` | 

The method `compute.beta.InterconnectLocationsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.interconnectRemoteLocations](/compute/docs/reference/rest/beta/interconnectRemoteLocations)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/interconnectRemoteLocations/get)` | 

The method `compute.beta.InterconnectRemoteLocationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/interconnectRemoteLocations/list)` | 

The method `compute.beta.InterconnectRemoteLocationsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.interconnects](/compute/docs/reference/rest/beta/interconnects)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/interconnects/delete)` | 

The method `compute.beta.InterconnectsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/interconnects/get)` | 

The method `compute.beta.InterconnectsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getDiagnostics](/compute/docs/reference/rest/beta/interconnects/getDiagnostics)` | 

The method `compute.beta.InterconnectsService.GetDiagnostics` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getMacsecConfig](/compute/docs/reference/rest/beta/interconnects/getMacsecConfig)` | 

The method `compute.beta.InterconnectsService.GetMacsecConfig` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/interconnects/insert)` | 

The method `compute.beta.InterconnectsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/interconnects/list)` | 

The method `compute.beta.InterconnectsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/interconnects/patch)` | 

The method `compute.beta.InterconnectsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/interconnects/setLabels)` | 

The method `compute.beta.InterconnectsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/interconnects/testIamPermissions)` | 

The method `compute.beta.InterconnectsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.licenseCodes](/compute/docs/reference/rest/beta/licenseCodes)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/licenseCodes/get)` | 

The method `compute.beta.LicenseCodesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/licenseCodes/getIamPolicy)` | 

The method `compute.beta.LicenseCodesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/licenseCodes/setIamPolicy)` | 

The method `compute.beta.LicenseCodesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/licenseCodes/testIamPermissions)` | 

The method `compute.beta.LicenseCodesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.licenses](/compute/docs/reference/rest/beta/licenses)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/licenses/delete)` | 

The method `compute.beta.LicensesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/licenses/get)` | 

The method `compute.beta.LicensesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/licenses/getIamPolicy)` | 

The method `compute.beta.LicensesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/licenses/insert)` | 

The method `compute.beta.LicensesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/licenses/list)` | 

The method `compute.beta.LicensesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/licenses/setIamPolicy)` | 

The method `compute.beta.LicensesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/licenses/testIamPermissions)` | 

The method `compute.beta.LicensesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/licenses/update)` | 

The method `compute.beta.LicensesService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.machineImages](/compute/docs/reference/rest/beta/machineImages)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/machineImages/delete)` | 

The method `compute.beta.MachineImagesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/machineImages/get)` | 

The method `compute.beta.MachineImagesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/machineImages/getIamPolicy)` | 

The method `compute.beta.MachineImagesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/machineImages/insert)` | 

The method `compute.beta.MachineImagesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/machineImages/list)` | 

The method `compute.beta.MachineImagesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/machineImages/setIamPolicy)` | 

The method `compute.beta.MachineImagesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/machineImages/setLabels)` | 

The method `compute.beta.MachineImagesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/machineImages/testIamPermissions)` | 

The method `compute.beta.MachineImagesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.machineTypes](/compute/docs/reference/rest/beta/machineTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/machineTypes/aggregatedList)` | 

The method `compute.beta.MachineTypesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/machineTypes/get)` | 

The method `compute.beta.MachineTypesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/machineTypes/list)` | 

The method `compute.beta.MachineTypesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.networkAttachments](/compute/docs/reference/rest/beta/networkAttachments)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/networkAttachments/aggregatedList)` | 

The method `compute.beta.NetworkAttachmentsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/networkAttachments/delete)` | 

The method `compute.beta.NetworkAttachmentsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/networkAttachments/get)` | 

The method `compute.beta.NetworkAttachmentsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/networkAttachments/getIamPolicy)` | 

The method `compute.beta.NetworkAttachmentsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/networkAttachments/insert)` | 

The method `compute.beta.NetworkAttachmentsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/networkAttachments/list)` | 

The method `compute.beta.NetworkAttachmentsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/networkAttachments/patch)` | 

The method `compute.beta.NetworkAttachmentsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/networkAttachments/setIamPolicy)` | 

The method `compute.beta.NetworkAttachmentsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/networkAttachments/testIamPermissions)` | 

The method `compute.beta.NetworkAttachmentsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.networkEdgeSecurityServices](/compute/docs/reference/rest/beta/networkEdgeSecurityServices)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/networkEdgeSecurityServices/aggregatedList)` | 

The method `compute.beta.NetworkEdgeSecurityServicesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/networkEdgeSecurityServices/delete)` | 

The method `compute.beta.NetworkEdgeSecurityServicesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/networkEdgeSecurityServices/get)` | 

The method `compute.beta.NetworkEdgeSecurityServicesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/networkEdgeSecurityServices/insert)` | 

The method `compute.beta.NetworkEdgeSecurityServicesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/networkEdgeSecurityServices/patch)` | 

The method `compute.beta.NetworkEdgeSecurityServicesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.networkEndpointGroups](/compute/docs/reference/rest/beta/networkEndpointGroups)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/networkEndpointGroups/aggregatedList)` | 

The method `compute.beta.NetworkEndpointGroupsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[attachNetworkEndpoints](/compute/docs/reference/rest/beta/networkEndpointGroups/attachNetworkEndpoints)` | 

The method `compute.beta.NetworkEndpointGroupsService.AttachNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/networkEndpointGroups/delete)` | 

The method `compute.beta.NetworkEndpointGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[detachNetworkEndpoints](/compute/docs/reference/rest/beta/networkEndpointGroups/detachNetworkEndpoints)` | 

The method `compute.beta.NetworkEndpointGroupsService.DetachNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/networkEndpointGroups/get)` | 

The method `compute.beta.NetworkEndpointGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/networkEndpointGroups/insert)` | 

The method `compute.beta.NetworkEndpointGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/networkEndpointGroups/list)` | 

The method `compute.beta.NetworkEndpointGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listNetworkEndpoints](/compute/docs/reference/rest/beta/networkEndpointGroups/listNetworkEndpoints)` | 

The method `compute.beta.NetworkEndpointGroupsService.ListNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/networkEndpointGroups/testIamPermissions)` | 

The method `compute.beta.NetworkEndpointGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.networkFirewallPolicies](/compute/docs/reference/rest/beta/networkFirewallPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/beta/networkFirewallPolicies/addAssociation)` | 

The method `compute.beta.NetworkFirewallPoliciesService.AddAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addPacketMirroringRule](/compute/docs/reference/rest/beta/networkFirewallPolicies/addPacketMirroringRule)` | 

The method `compute.beta.NetworkFirewallPoliciesService.AddPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addRule](/compute/docs/reference/rest/beta/networkFirewallPolicies/addRule)` | 

The method `compute.beta.NetworkFirewallPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/networkFirewallPolicies/aggregatedList)` | 

The method `compute.beta.NetworkFirewallPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cloneRules](/compute/docs/reference/rest/beta/networkFirewallPolicies/cloneRules)` | 

The method `compute.beta.NetworkFirewallPoliciesService.CloneRules` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/networkFirewallPolicies/delete)` | 

The method `compute.beta.NetworkFirewallPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/networkFirewallPolicies/get)` | 

The method `compute.beta.NetworkFirewallPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/beta/networkFirewallPolicies/getAssociation)` | 

The method `compute.beta.NetworkFirewallPoliciesService.GetAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/networkFirewallPolicies/getIamPolicy)` | 

The method `compute.beta.NetworkFirewallPoliciesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getPacketMirroringRule](/compute/docs/reference/rest/beta/networkFirewallPolicies/getPacketMirroringRule)` | 

The method `compute.beta.NetworkFirewallPoliciesService.GetPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/beta/networkFirewallPolicies/getRule)` | 

The method `compute.beta.NetworkFirewallPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/networkFirewallPolicies/insert)` | 

The method `compute.beta.NetworkFirewallPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/networkFirewallPolicies/list)` | 

The method `compute.beta.NetworkFirewallPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/networkFirewallPolicies/patch)` | 

The method `compute.beta.NetworkFirewallPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchPacketMirroringRule](/compute/docs/reference/rest/beta/networkFirewallPolicies/patchPacketMirroringRule)` | 

The method `compute.beta.NetworkFirewallPoliciesService.PatchPacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/beta/networkFirewallPolicies/patchRule)` | 

The method `compute.beta.NetworkFirewallPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/beta/networkFirewallPolicies/removeAssociation)` | 

The method `compute.beta.NetworkFirewallPoliciesService.RemoveAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removePacketMirroringRule](/compute/docs/reference/rest/beta/networkFirewallPolicies/removePacketMirroringRule)` | 

The method `compute.beta.NetworkFirewallPoliciesService.RemovePacketMirroringRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/beta/networkFirewallPolicies/removeRule)` | 

The method `compute.beta.NetworkFirewallPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/networkFirewallPolicies/setIamPolicy)` | 

The method `compute.beta.NetworkFirewallPoliciesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/networkFirewallPolicies/testIamPermissions)` | 

The method `compute.beta.NetworkFirewallPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.networkProfiles](/compute/docs/reference/rest/beta/networkProfiles)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/networkProfiles/get)` | 

The method `compute.beta.NetworkProfilesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/networkProfiles/list)` | 

The method `compute.beta.NetworkProfilesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.networks](/compute/docs/reference/rest/beta/networks)









| 
Methods | 
|



| 

`[addPeering](/compute/docs/reference/rest/beta/networks/addPeering)` | 

The method `compute.beta.NetworksService.AddPeering` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cancelRequestRemovePeering](/compute/docs/reference/rest/beta/networks/cancelRequestRemovePeering)` | 

The method `compute.beta.NetworksService.CancelRequestRemovePeering` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/networks/delete)` | 

The method `compute.beta.NetworksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/networks/get)` | 

The method `compute.beta.NetworksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getEffectiveFirewalls](/compute/docs/reference/rest/beta/networks/getEffectiveFirewalls)` | 

The method `compute.beta.NetworksService.GetEffectiveFirewalls` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/networks/insert)` | 

The method `compute.beta.NetworksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/networks/list)` | 

The method `compute.beta.NetworksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listPeeringRoutes](/compute/docs/reference/rest/beta/networks/listPeeringRoutes)` | 

The method `compute.beta.NetworksService.ListPeeringRoutes` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/networks/patch)` | 

The method `compute.beta.NetworksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removePeering](/compute/docs/reference/rest/beta/networks/removePeering)` | 

The method `compute.beta.NetworksService.RemovePeering` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[requestRemovePeering](/compute/docs/reference/rest/beta/networks/requestRemovePeering)` | 

The method `compute.beta.NetworksService.RequestRemovePeering` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[switchToCustomMode](/compute/docs/reference/rest/beta/networks/switchToCustomMode)` | 

The method `compute.beta.NetworksService.SwitchToCustomMode` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/networks/testIamPermissions)` | 

The method `compute.beta.NetworksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updatePeering](/compute/docs/reference/rest/beta/networks/updatePeering)` | 

The method `compute.beta.NetworksService.UpdatePeering` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.nodeGroups](/compute/docs/reference/rest/beta/nodeGroups)









| 
Methods | 
|



| 

`[addNodes](/compute/docs/reference/rest/beta/nodeGroups/addNodes)` | 

The method `compute.beta.NodeGroupsService.AddNodes` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/nodeGroups/aggregatedList)` | 

The method `compute.beta.NodeGroupsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/nodeGroups/delete)` | 

The method `compute.beta.NodeGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteNodes](/compute/docs/reference/rest/beta/nodeGroups/deleteNodes)` | 

The method `compute.beta.NodeGroupsService.DeleteNodes` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/nodeGroups/get)` | 

The method `compute.beta.NodeGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/nodeGroups/getIamPolicy)` | 

The method `compute.beta.NodeGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/nodeGroups/insert)` | 

The method `compute.beta.NodeGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/nodeGroups/list)` | 

The method `compute.beta.NodeGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listNodes](/compute/docs/reference/rest/beta/nodeGroups/listNodes)` | 

The method `compute.beta.NodeGroupsService.ListNodes` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/nodeGroups/patch)` | 

The method `compute.beta.NodeGroupsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/beta/nodeGroups/performMaintenance)` | 

The method `compute.beta.NodeGroupsService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/nodeGroups/setIamPolicy)` | 

The method `compute.beta.NodeGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setNodeTemplate](/compute/docs/reference/rest/beta/nodeGroups/setNodeTemplate)` | 

The method `compute.beta.NodeGroupsService.SetNodeTemplate` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[simulateMaintenanceEvent](/compute/docs/reference/rest/beta/nodeGroups/simulateMaintenanceEvent)` | 

The method `compute.beta.NodeGroupsService.SimulateMaintenanceEvent` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/nodeGroups/testIamPermissions)` | 

The method `compute.beta.NodeGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.nodeTemplates](/compute/docs/reference/rest/beta/nodeTemplates)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/nodeTemplates/aggregatedList)` | 

The method `compute.beta.NodeTemplatesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/nodeTemplates/delete)` | 

The method `compute.beta.NodeTemplatesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/nodeTemplates/get)` | 

The method `compute.beta.NodeTemplatesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/nodeTemplates/getIamPolicy)` | 

The method `compute.beta.NodeTemplatesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/nodeTemplates/insert)` | 

The method `compute.beta.NodeTemplatesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/nodeTemplates/list)` | 

The method `compute.beta.NodeTemplatesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/nodeTemplates/setIamPolicy)` | 

The method `compute.beta.NodeTemplatesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/nodeTemplates/testIamPermissions)` | 

The method `compute.beta.NodeTemplatesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.nodeTypes](/compute/docs/reference/rest/beta/nodeTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/nodeTypes/aggregatedList)` | 

The method `compute.beta.NodeTypesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/nodeTypes/get)` | 

The method `compute.beta.NodeTypesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/nodeTypes/list)` | 

The method `compute.beta.NodeTypesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.organizationRolloutPlans](/compute/docs/reference/rest/beta/organizationRolloutPlans)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/organizationRolloutPlans/delete)` | 

The method `compute.beta.OrganizationRolloutPlansService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/organizationRolloutPlans/get)` | 

The method `compute.beta.OrganizationRolloutPlansService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/organizationRolloutPlans/insert)` | 

The method `compute.beta.OrganizationRolloutPlansService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/organizationRolloutPlans/list)` | 

The method `compute.beta.OrganizationRolloutPlansService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.organizationRollouts](/compute/docs/reference/rest/beta/organizationRollouts)









| 
Methods | 
|



| 

`[advance](/compute/docs/reference/rest/beta/organizationRollouts/advance)` | 

The method `compute.beta.OrganizationRolloutsService.Advance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cancel](/compute/docs/reference/rest/beta/organizationRollouts/cancel)` | 

The method `compute.beta.OrganizationRolloutsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/organizationRollouts/delete)` | 

The method `compute.beta.OrganizationRolloutsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/organizationRollouts/get)` | 

The method `compute.beta.OrganizationRolloutsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/organizationRollouts/list)` | 

The method `compute.beta.OrganizationRolloutsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[pause](/compute/docs/reference/rest/beta/organizationRollouts/pause)` | 

The method `compute.beta.OrganizationRolloutsService.Pause` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resume](/compute/docs/reference/rest/beta/organizationRollouts/resume)` | 

The method `compute.beta.OrganizationRolloutsService.Resume` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.organizationSecurityPolicies](/compute/docs/reference/rest/beta/organizationSecurityPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/beta/organizationSecurityPolicies/addAssociation)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.AddAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addRule](/compute/docs/reference/rest/beta/organizationSecurityPolicies/addRule)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[copyRules](/compute/docs/reference/rest/beta/organizationSecurityPolicies/copyRules)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.CopyRules` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/organizationSecurityPolicies/delete)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/organizationSecurityPolicies/get)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/beta/organizationSecurityPolicies/getAssociation)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.GetAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/beta/organizationSecurityPolicies/getRule)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/organizationSecurityPolicies/insert)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/organizationSecurityPolicies/list)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listAssociations](/compute/docs/reference/rest/beta/organizationSecurityPolicies/listAssociations)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.ListAssociations` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listPreconfiguredExpressionSets](/compute/docs/reference/rest/beta/organizationSecurityPolicies/listPreconfiguredExpressionSets)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.ListPreconfiguredExpressionSets` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[move](/compute/docs/reference/rest/beta/organizationSecurityPolicies/move)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.Move` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/organizationSecurityPolicies/patch)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/beta/organizationSecurityPolicies/patchRule)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/beta/organizationSecurityPolicies/removeAssociation)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.RemoveAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/beta/organizationSecurityPolicies/removeRule)` | 

The method `compute.beta.OrganizationSecurityPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.packetMirrorings](/compute/docs/reference/rest/beta/packetMirrorings)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/packetMirrorings/aggregatedList)` | 

The method `compute.beta.PacketMirroringsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/packetMirrorings/delete)` | 

The method `compute.beta.PacketMirroringsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/packetMirrorings/get)` | 

The method `compute.beta.PacketMirroringsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/packetMirrorings/insert)` | 

The method `compute.beta.PacketMirroringsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/packetMirrorings/list)` | 

The method `compute.beta.PacketMirroringsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/packetMirrorings/patch)` | 

The method `compute.beta.PacketMirroringsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/packetMirrorings/testIamPermissions)` | 

The method `compute.beta.PacketMirroringsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.previewFeatures](/compute/docs/reference/rest/beta/previewFeatures)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/previewFeatures/get)` | 

The method `compute.beta.PreviewFeaturesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/previewFeatures/list)` | 

The method `compute.beta.PreviewFeaturesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/previewFeatures/update)` | 

The method `compute.beta.PreviewFeaturesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.projectViews](/compute/docs/reference/rest/beta/projectViews)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/projectViews/get)` | 

The method `compute.beta.ProjectViewsService.Get` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.projects](/compute/docs/reference/rest/beta/projects)









| 
Methods | 
|



| 

`[disableXpnHost](/compute/docs/reference/rest/beta/projects/disableXpnHost)` | 

The method `compute.beta.ProjectsService.DisableXpnHost` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[disableXpnResource](/compute/docs/reference/rest/beta/projects/disableXpnResource)` | 

The method `compute.beta.ProjectsService.DisableXpnResource` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[enableXpnHost](/compute/docs/reference/rest/beta/projects/enableXpnHost)` | 

The method `compute.beta.ProjectsService.EnableXpnHost` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[enableXpnResource](/compute/docs/reference/rest/beta/projects/enableXpnResource)` | 

The method `compute.beta.ProjectsService.EnableXpnResource` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/projects/get)` | 

The method `compute.beta.ProjectsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getXpnHost](/compute/docs/reference/rest/beta/projects/getXpnHost)` | 

The method `compute.beta.ProjectsService.GetXpnHost` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getXpnResources](/compute/docs/reference/rest/beta/projects/getXpnResources)` | 

The method `compute.beta.ProjectsService.GetXpnResources` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listXpnHosts](/compute/docs/reference/rest/beta/projects/listXpnHosts)` | 

The method `compute.beta.ProjectsService.ListXpnHosts` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[moveDisk](/compute/docs/reference/rest/beta/projects/moveDisk) 
**(deprecated)**` | 

The method `compute.beta.ProjectsService.MoveDisk` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[moveInstance](/compute/docs/reference/rest/beta/projects/moveInstance) 
**(deprecated)**` | 

The method `compute.beta.ProjectsService.MoveInstance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setCloudArmorTier](/compute/docs/reference/rest/beta/projects/setCloudArmorTier)` | 

The method `compute.beta.ProjectsService.SetCloudArmorTier` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setCommonInstanceMetadata](/compute/docs/reference/rest/beta/projects/setCommonInstanceMetadata)` | 

The method `compute.beta.ProjectsService.SetCommonInstanceMetadata` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setDefaultNetworkTier](/compute/docs/reference/rest/beta/projects/setDefaultNetworkTier)` | 

The method `compute.beta.ProjectsService.SetDefaultNetworkTier` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setManagedProtectionTier](/compute/docs/reference/rest/beta/projects/setManagedProtectionTier)` | 

The method `compute.beta.ProjectsService.SetManagedProtectionTier` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setUsageExportBucket](/compute/docs/reference/rest/beta/projects/setUsageExportBucket)` | 

The method `compute.beta.ProjectsService.SetUsageExportBucket` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.publicAdvertisedPrefixes](/compute/docs/reference/rest/beta/publicAdvertisedPrefixes)









| 
Methods | 
|



| 

`[announce](/compute/docs/reference/rest/beta/publicAdvertisedPrefixes/announce)` | 

The method `compute.beta.PublicAdvertisedPrefixesService.Announce` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/publicAdvertisedPrefixes/delete)` | 

The method `compute.beta.PublicAdvertisedPrefixesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/publicAdvertisedPrefixes/get)` | 

The method `compute.beta.PublicAdvertisedPrefixesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/publicAdvertisedPrefixes/insert)` | 

The method `compute.beta.PublicAdvertisedPrefixesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/publicAdvertisedPrefixes/list)` | 

The method `compute.beta.PublicAdvertisedPrefixesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/publicAdvertisedPrefixes/patch)` | 

The method `compute.beta.PublicAdvertisedPrefixesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[withdraw](/compute/docs/reference/rest/beta/publicAdvertisedPrefixes/withdraw)` | 

The method `compute.beta.PublicAdvertisedPrefixesService.Withdraw` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.publicDelegatedPrefixes](/compute/docs/reference/rest/beta/publicDelegatedPrefixes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/publicDelegatedPrefixes/aggregatedList)` | 

The method `compute.beta.PublicDelegatedPrefixesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[announce](/compute/docs/reference/rest/beta/publicDelegatedPrefixes/announce)` | 

The method `compute.beta.PublicDelegatedPrefixesService.Announce` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/publicDelegatedPrefixes/delete)` | 

The method `compute.beta.PublicDelegatedPrefixesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/publicDelegatedPrefixes/get)` | 

The method `compute.beta.PublicDelegatedPrefixesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/publicDelegatedPrefixes/insert)` | 

The method `compute.beta.PublicDelegatedPrefixesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/publicDelegatedPrefixes/list)` | 

The method `compute.beta.PublicDelegatedPrefixesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/publicDelegatedPrefixes/patch)` | 

The method `compute.beta.PublicDelegatedPrefixesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[withdraw](/compute/docs/reference/rest/beta/publicDelegatedPrefixes/withdraw)` | 

The method `compute.beta.PublicDelegatedPrefixesService.Withdraw` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionAutoscalers](/compute/docs/reference/rest/beta/regionAutoscalers)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionAutoscalers/delete)` | 

The method `compute.beta.RegionAutoscalersService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionAutoscalers/get)` | 

The method `compute.beta.RegionAutoscalersService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionAutoscalers/insert)` | 

The method `compute.beta.RegionAutoscalersService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionAutoscalers/list)` | 

The method `compute.beta.RegionAutoscalersService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionAutoscalers/patch)` | 

The method `compute.beta.RegionAutoscalersService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionAutoscalers/testIamPermissions)` | 

The method `compute.beta.RegionAutoscalersService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/regionAutoscalers/update)` | 

The method `compute.beta.RegionAutoscalersService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionBackendBuckets](/compute/docs/reference/rest/beta/regionBackendBuckets)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionBackendBuckets/delete)` | 

The method `compute.beta.RegionBackendBucketsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionBackendBuckets/get)` | 

The method `compute.beta.RegionBackendBucketsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/regionBackendBuckets/getIamPolicy)` | 

The method `compute.beta.RegionBackendBucketsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionBackendBuckets/insert)` | 

The method `compute.beta.RegionBackendBucketsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionBackendBuckets/list)` | 

The method `compute.beta.RegionBackendBucketsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/beta/regionBackendBuckets/listUsable)` | 

The method `compute.beta.RegionBackendBucketsService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionBackendBuckets/patch)` | 

The method `compute.beta.RegionBackendBucketsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/regionBackendBuckets/setIamPolicy)` | 

The method `compute.beta.RegionBackendBucketsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionBackendBuckets/testIamPermissions)` | 

The method `compute.beta.RegionBackendBucketsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionBackendServices](/compute/docs/reference/rest/beta/regionBackendServices)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionBackendServices/delete)` | 

The method `compute.beta.RegionBackendServicesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionBackendServices/get)` | 

The method `compute.beta.RegionBackendServicesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getHealth](/compute/docs/reference/rest/beta/regionBackendServices/getHealth)` | 

The method `compute.beta.RegionBackendServicesService.GetHealth` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/regionBackendServices/getIamPolicy)` | 

The method `compute.beta.RegionBackendServicesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionBackendServices/insert)` | 

The method `compute.beta.RegionBackendServicesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionBackendServices/list)` | 

The method `compute.beta.RegionBackendServicesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/beta/regionBackendServices/listUsable)` | 

The method `compute.beta.RegionBackendServicesService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionBackendServices/patch)` | 

The method `compute.beta.RegionBackendServicesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/regionBackendServices/setIamPolicy)` | 

The method `compute.beta.RegionBackendServicesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/beta/regionBackendServices/setSecurityPolicy)` | 

The method `compute.beta.RegionBackendServicesService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionBackendServices/testIamPermissions)` | 

The method `compute.beta.RegionBackendServicesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/regionBackendServices/update)` | 

The method `compute.beta.RegionBackendServicesService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionCommitments](/compute/docs/reference/rest/beta/regionCommitments)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/regionCommitments/aggregatedList)` | 

The method `compute.beta.RegionCommitmentsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionCommitments/get)` | 

The method `compute.beta.RegionCommitmentsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionCommitments/insert)` | 

The method `compute.beta.RegionCommitmentsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionCommitments/list)` | 

The method `compute.beta.RegionCommitmentsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionCommitments/testIamPermissions)` | 

The method `compute.beta.RegionCommitmentsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/regionCommitments/update)` | 

The method `compute.beta.RegionCommitmentsService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateReservations](/compute/docs/reference/rest/beta/regionCommitments/updateReservations)` | 

The method `compute.beta.RegionCommitmentsService.UpdateAllocations` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionCompositeHealthChecks](/compute/docs/reference/rest/beta/regionCompositeHealthChecks)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/regionCompositeHealthChecks/aggregatedList)` | 

The method `compute.beta.RegionCompositeHealthChecksService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionCompositeHealthChecks/delete)` | 

The method `compute.beta.RegionCompositeHealthChecksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionCompositeHealthChecks/get)` | 

The method `compute.beta.RegionCompositeHealthChecksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getHealth](/compute/docs/reference/rest/beta/regionCompositeHealthChecks/getHealth)` | 

The method `compute.beta.RegionCompositeHealthChecksService.GetHealth` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionCompositeHealthChecks/insert)` | 

The method `compute.beta.RegionCompositeHealthChecksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionCompositeHealthChecks/list)` | 

The method `compute.beta.RegionCompositeHealthChecksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionCompositeHealthChecks/patch)` | 

The method `compute.beta.RegionCompositeHealthChecksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionCompositeHealthChecks/testIamPermissions)` | 

The method `compute.beta.RegionCompositeHealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionDiskSettings](/compute/docs/reference/rest/beta/regionDiskSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/regionDiskSettings/get)` | 

The method `compute.beta.RegionDiskSettingsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionDiskSettings/patch)` | 

The method `compute.beta.RegionDiskSettingsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionDiskTypes](/compute/docs/reference/rest/beta/regionDiskTypes)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/regionDiskTypes/get)` | 

The method `compute.beta.RegionDiskTypesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionDiskTypes/list)` | 

The method `compute.beta.RegionDiskTypesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionDisks](/compute/docs/reference/rest/beta/regionDisks)









| 
Methods | 
|



| 

`[addResourcePolicies](/compute/docs/reference/rest/beta/regionDisks/addResourcePolicies)` | 

The method `compute.beta.RegionDisksService.AddResourcePolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[bulkInsert](/compute/docs/reference/rest/beta/regionDisks/bulkInsert)` | 

The method `compute.beta.RegionDisksService.BulkInsert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[createSnapshot](/compute/docs/reference/rest/beta/regionDisks/createSnapshot)` | 

The method `compute.beta.RegionDisksService.CreateSnapshot` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionDisks/delete)` | 

The method `compute.beta.RegionDisksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionDisks/get)` | 

The method `compute.beta.RegionDisksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/regionDisks/getIamPolicy)` | 

The method `compute.beta.RegionDisksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionDisks/insert)` | 

The method `compute.beta.RegionDisksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionDisks/list)` | 

The method `compute.beta.RegionDisksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeResourcePolicies](/compute/docs/reference/rest/beta/regionDisks/removeResourcePolicies)` | 

The method `compute.beta.RegionDisksService.RemoveResourcePolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resize](/compute/docs/reference/rest/beta/regionDisks/resize)` | 

The method `compute.beta.RegionDisksService.Resize` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/regionDisks/setIamPolicy)` | 

The method `compute.beta.RegionDisksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/regionDisks/setLabels)` | 

The method `compute.beta.RegionDisksService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startAsyncReplication](/compute/docs/reference/rest/beta/regionDisks/startAsyncReplication)` | 

The method `compute.beta.RegionDisksService.StartAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopAsyncReplication](/compute/docs/reference/rest/beta/regionDisks/stopAsyncReplication)` | 

The method `compute.beta.RegionDisksService.StopAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopGroupAsyncReplication](/compute/docs/reference/rest/beta/regionDisks/stopGroupAsyncReplication)` | 

The method `compute.beta.RegionDisksService.StopGroupAsyncReplication` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionDisks/testIamPermissions)` | 

The method `compute.beta.RegionDisksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/regionDisks/update)` | 

The method `compute.beta.RegionDisksService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateKmsKey](/compute/docs/reference/rest/beta/regionDisks/updateKmsKey)` | 

The method `compute.beta.RegionDisksService.UpdateKmsKey` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionHealthAggregationPolicies](/compute/docs/reference/rest/beta/regionHealthAggregationPolicies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/regionHealthAggregationPolicies/aggregatedList)` | 

The method `compute.beta.RegionHealthAggregationPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionHealthAggregationPolicies/delete)` | 

The method `compute.beta.RegionHealthAggregationPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionHealthAggregationPolicies/get)` | 

The method `compute.beta.RegionHealthAggregationPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionHealthAggregationPolicies/insert)` | 

The method `compute.beta.RegionHealthAggregationPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionHealthAggregationPolicies/list)` | 

The method `compute.beta.RegionHealthAggregationPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionHealthAggregationPolicies/patch)` | 

The method `compute.beta.RegionHealthAggregationPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionHealthAggregationPolicies/testIamPermissions)` | 

The method `compute.beta.RegionHealthAggregationPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionHealthCheckServices](/compute/docs/reference/rest/beta/regionHealthCheckServices)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/regionHealthCheckServices/aggregatedList)` | 

The method `compute.beta.RegionHealthCheckServicesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionHealthCheckServices/delete)` | 

The method `compute.beta.RegionHealthCheckServicesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionHealthCheckServices/get)` | 

The method `compute.beta.RegionHealthCheckServicesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionHealthCheckServices/insert)` | 

The method `compute.beta.RegionHealthCheckServicesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionHealthCheckServices/list)` | 

The method `compute.beta.RegionHealthCheckServicesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionHealthCheckServices/patch)` | 

The method `compute.beta.RegionHealthCheckServicesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionHealthCheckServices/testIamPermissions)` | 

The method `compute.beta.RegionHealthCheckServicesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionHealthChecks](/compute/docs/reference/rest/beta/regionHealthChecks)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionHealthChecks/delete)` | 

The method `compute.beta.RegionHealthChecksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionHealthChecks/get)` | 

The method `compute.beta.RegionHealthChecksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionHealthChecks/insert)` | 

The method `compute.beta.RegionHealthChecksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionHealthChecks/list)` | 

The method `compute.beta.RegionHealthChecksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionHealthChecks/patch)` | 

The method `compute.beta.RegionHealthChecksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionHealthChecks/testIamPermissions)` | 

The method `compute.beta.RegionHealthChecksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/regionHealthChecks/update)` | 

The method `compute.beta.RegionHealthChecksService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionHealthSources](/compute/docs/reference/rest/beta/regionHealthSources)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/regionHealthSources/aggregatedList)` | 

The method `compute.beta.RegionHealthSourcesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionHealthSources/delete)` | 

The method `compute.beta.RegionHealthSourcesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionHealthSources/get)` | 

The method `compute.beta.RegionHealthSourcesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getHealth](/compute/docs/reference/rest/beta/regionHealthSources/getHealth)` | 

The method `compute.beta.RegionHealthSourcesService.GetHealth` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionHealthSources/insert)` | 

The method `compute.beta.RegionHealthSourcesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionHealthSources/list)` | 

The method `compute.beta.RegionHealthSourcesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionHealthSources/patch)` | 

The method `compute.beta.RegionHealthSourcesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionHealthSources/testIamPermissions)` | 

The method `compute.beta.RegionHealthSourcesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionInstanceGroupManagerResizeRequests](/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests)









| 
Methods | 
|



| 

`[cancel](/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/cancel)` | 

The method `compute.beta.RegionInstanceGroupManagerResizeRequestsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/delete)` | 

The method `compute.beta.RegionInstanceGroupManagerResizeRequestsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/get)` | 

The method `compute.beta.RegionInstanceGroupManagerResizeRequestsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/insert)` | 

The method `compute.beta.RegionInstanceGroupManagerResizeRequestsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/list)` | 

The method `compute.beta.RegionInstanceGroupManagerResizeRequestsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionInstanceGroupManagers](/compute/docs/reference/rest/beta/regionInstanceGroupManagers)









| 
Methods | 
|



| 

`[abandonInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/abandonInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.AbandonInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[adoptInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/adoptInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.AdoptInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[applyUpdatesToInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/applyUpdatesToInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.ApplyUpdatesToInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[createInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/createInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.CreateInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/delete)` | 

The method `compute.beta.RegionInstanceGroupManagersService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/deleteInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.DeleteInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deletePerInstanceConfigs](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/deletePerInstanceConfigs)` | 

The method `compute.beta.RegionInstanceGroupManagersService.DeletePerInstanceConfigs` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/get)` | 

The method `compute.beta.RegionInstanceGroupManagersService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/insert)` | 

The method `compute.beta.RegionInstanceGroupManagersService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/list)` | 

The method `compute.beta.RegionInstanceGroupManagersService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listErrors](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/listErrors)` | 

The method `compute.beta.RegionInstanceGroupManagersService.ListErrors` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listManagedInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/listManagedInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.ListManagedInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listPerInstanceConfigs](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/listPerInstanceConfigs)` | 

The method `compute.beta.RegionInstanceGroupManagersService.ListPerInstanceConfigs` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)` | 

The method `compute.beta.RegionInstanceGroupManagersService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchPerInstanceConfigs](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patchPerInstanceConfigs)` | 

The method `compute.beta.RegionInstanceGroupManagersService.PatchPerInstanceConfigs` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[recreateInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/recreateInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.RecreateInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resize](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/resize)` | 

The method `compute.beta.RegionInstanceGroupManagersService.Resize` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resizeAdvanced](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/resizeAdvanced)` | 

The method `compute.beta.RegionInstanceGroupManagersService.ResizeAdvanced` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resumeInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/resumeInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.ResumeInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setAutoHealingPolicies](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/setAutoHealingPolicies) 
**(deprecated)**` | 

The method `compute.beta.RegionInstanceGroupManagersService.SetAutoHealingPolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setInstanceTemplate](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/setInstanceTemplate)` | 

The method `compute.beta.RegionInstanceGroupManagersService.SetInstanceTemplate` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setTargetPools](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/setTargetPools)` | 

The method `compute.beta.RegionInstanceGroupManagersService.SetTargetPools` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[startInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/startInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.StartInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[stopInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/stopInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.StopInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[suspendInstances](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/suspendInstances)` | 

The method `compute.beta.RegionInstanceGroupManagersService.SuspendInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/testIamPermissions)` | 

The method `compute.beta.RegionInstanceGroupManagersService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/update)` | 

The method `compute.beta.RegionInstanceGroupManagersService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updatePerInstanceConfigs](/compute/docs/reference/rest/beta/regionInstanceGroupManagers/updatePerInstanceConfigs)` | 

The method `compute.beta.RegionInstanceGroupManagersService.UpdatePerInstanceConfigs` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionInstanceGroups](/compute/docs/reference/rest/beta/regionInstanceGroups)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/regionInstanceGroups/get)` | 

The method `compute.beta.RegionInstanceGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionInstanceGroups/list)` | 

The method `compute.beta.RegionInstanceGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listInstances](/compute/docs/reference/rest/beta/regionInstanceGroups/listInstances)` | 

The method `compute.beta.RegionInstanceGroupsService.ListInstances` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setNamedPorts](/compute/docs/reference/rest/beta/regionInstanceGroups/setNamedPorts)` | 

The method `compute.beta.RegionInstanceGroupsService.SetNamedPorts` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionInstanceGroups/testIamPermissions)` | 

The method `compute.beta.RegionInstanceGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionInstanceTemplates](/compute/docs/reference/rest/beta/regionInstanceTemplates)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionInstanceTemplates/delete)` | 

The method `compute.beta.RegionInstanceTemplatesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionInstanceTemplates/get)` | 

The method `compute.beta.RegionInstanceTemplatesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionInstanceTemplates/insert)` | 

The method `compute.beta.RegionInstanceTemplatesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionInstanceTemplates/list)` | 

The method `compute.beta.RegionInstanceTemplatesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionInstances](/compute/docs/reference/rest/beta/regionInstances)









| 
Methods | 
|



| 

`[bulkInsert](/compute/docs/reference/rest/beta/regionInstances/bulkInsert)` | 

The method `compute.beta.RegionInstancesService.BulkInsert` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionInstantSnapshotGroups](/compute/docs/reference/rest/beta/regionInstantSnapshotGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionInstantSnapshotGroups/delete)` | 

The method `compute.beta.RegionInstantSnapshotGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionInstantSnapshotGroups/get)` | 

The method `compute.beta.RegionInstantSnapshotGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/regionInstantSnapshotGroups/getIamPolicy)` | 

The method `compute.beta.RegionInstantSnapshotGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionInstantSnapshotGroups/insert)` | 

The method `compute.beta.RegionInstantSnapshotGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionInstantSnapshotGroups/list)` | 

The method `compute.beta.RegionInstantSnapshotGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/regionInstantSnapshotGroups/setIamPolicy)` | 

The method `compute.beta.RegionInstantSnapshotGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionInstantSnapshotGroups/testIamPermissions)` | 

The method `compute.beta.RegionInstantSnapshotGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionInstantSnapshots](/compute/docs/reference/rest/beta/regionInstantSnapshots)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionInstantSnapshots/delete)` | 

The method `compute.beta.RegionInstantSnapshotsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionInstantSnapshots/get)` | 

The method `compute.beta.RegionInstantSnapshotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/regionInstantSnapshots/getIamPolicy)` | 

The method `compute.beta.RegionInstantSnapshotsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionInstantSnapshots/insert)` | 

The method `compute.beta.RegionInstantSnapshotsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionInstantSnapshots/list)` | 

The method `compute.beta.RegionInstantSnapshotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/regionInstantSnapshots/setIamPolicy)` | 

The method `compute.beta.RegionInstantSnapshotsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/regionInstantSnapshots/setLabels)` | 

The method `compute.beta.RegionInstantSnapshotsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionInstantSnapshots/testIamPermissions)` | 

The method `compute.beta.RegionInstantSnapshotsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionMultiMigMembers](/compute/docs/reference/rest/beta/regionMultiMigMembers)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/regionMultiMigMembers/get)` | 

The method `compute.beta.RegionMultiMigMembersService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionMultiMigMembers/list)` | 

The method `compute.beta.RegionMultiMigMembersService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionMultiMigs](/compute/docs/reference/rest/beta/regionMultiMigs)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionMultiMigs/delete)` | 

The method `compute.beta.RegionMultiMigsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionMultiMigs/get)` | 

The method `compute.beta.RegionMultiMigsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionMultiMigs/insert)` | 

The method `compute.beta.RegionMultiMigsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionMultiMigs/list)` | 

The method `compute.beta.RegionMultiMigsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionNetworkEndpointGroups](/compute/docs/reference/rest/beta/regionNetworkEndpointGroups)









| 
Methods | 
|



| 

`[attachNetworkEndpoints](/compute/docs/reference/rest/beta/regionNetworkEndpointGroups/attachNetworkEndpoints)` | 

The method `compute.beta.RegionNetworkEndpointGroupsService.AttachNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionNetworkEndpointGroups/delete)` | 

The method `compute.beta.RegionNetworkEndpointGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[detachNetworkEndpoints](/compute/docs/reference/rest/beta/regionNetworkEndpointGroups/detachNetworkEndpoints)` | 

The method `compute.beta.RegionNetworkEndpointGroupsService.DetachNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionNetworkEndpointGroups/get)` | 

The method `compute.beta.RegionNetworkEndpointGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionNetworkEndpointGroups/insert)` | 

The method `compute.beta.RegionNetworkEndpointGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionNetworkEndpointGroups/list)` | 

The method `compute.beta.RegionNetworkEndpointGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listNetworkEndpoints](/compute/docs/reference/rest/beta/regionNetworkEndpointGroups/listNetworkEndpoints)` | 

The method `compute.beta.RegionNetworkEndpointGroupsService.ListNetworkEndpoints` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionNetworkFirewallPolicies](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/addAssociation)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.AddAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addRule](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/addRule)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cloneRules](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/cloneRules)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.CloneRules` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/delete)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/get)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/getAssociation)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.GetAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getEffectiveFirewalls](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/getEffectiveFirewalls)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.GetEffectiveFirewalls` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/getIamPolicy)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/getRule)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/insert)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/list)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/patch)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchAssociation](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/patchAssociation)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.PatchAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/patchRule)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/removeAssociation)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.RemoveAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/removeRule)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/setIamPolicy)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionNetworkFirewallPolicies/testIamPermissions)` | 

The method `compute.beta.RegionNetworkFirewallPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionNetworkPolicies](/compute/docs/reference/rest/beta/regionNetworkPolicies)









| 
Methods | 
|



| 

`[addAssociation](/compute/docs/reference/rest/beta/regionNetworkPolicies/addAssociation)` | 

The method `compute.beta.RegionNetworkPoliciesService.AddAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addTrafficClassificationRule](/compute/docs/reference/rest/beta/regionNetworkPolicies/addTrafficClassificationRule)` | 

The method `compute.beta.RegionNetworkPoliciesService.AddTrafficClassificationRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/regionNetworkPolicies/aggregatedList)` | 

The method `compute.beta.RegionNetworkPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionNetworkPolicies/delete)` | 

The method `compute.beta.RegionNetworkPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionNetworkPolicies/get)` | 

The method `compute.beta.RegionNetworkPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getAssociation](/compute/docs/reference/rest/beta/regionNetworkPolicies/getAssociation)` | 

The method `compute.beta.RegionNetworkPoliciesService.GetAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getTrafficClassificationRule](/compute/docs/reference/rest/beta/regionNetworkPolicies/getTrafficClassificationRule)` | 

The method `compute.beta.RegionNetworkPoliciesService.GetTrafficClassificationRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionNetworkPolicies/insert)` | 

The method `compute.beta.RegionNetworkPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionNetworkPolicies/list)` | 

The method `compute.beta.RegionNetworkPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionNetworkPolicies/patch)` | 

The method `compute.beta.RegionNetworkPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchTrafficClassificationRule](/compute/docs/reference/rest/beta/regionNetworkPolicies/patchTrafficClassificationRule)` | 

The method `compute.beta.RegionNetworkPoliciesService.PatchTrafficClassificationRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeAssociation](/compute/docs/reference/rest/beta/regionNetworkPolicies/removeAssociation)` | 

The method `compute.beta.RegionNetworkPoliciesService.RemoveAssociation` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeTrafficClassificationRule](/compute/docs/reference/rest/beta/regionNetworkPolicies/removeTrafficClassificationRule)` | 

The method `compute.beta.RegionNetworkPoliciesService.RemoveTrafficClassificationRule` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionNotificationEndpoints](/compute/docs/reference/rest/beta/regionNotificationEndpoints)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/regionNotificationEndpoints/aggregatedList)` | 

The method `compute.beta.RegionNotificationEndpointsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionNotificationEndpoints/delete)` | 

The method `compute.beta.RegionNotificationEndpointsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionNotificationEndpoints/get)` | 

The method `compute.beta.RegionNotificationEndpointsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionNotificationEndpoints/insert)` | 

The method `compute.beta.RegionNotificationEndpointsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionNotificationEndpoints/list)` | 

The method `compute.beta.RegionNotificationEndpointsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionNotificationEndpoints/testIamPermissions)` | 

The method `compute.beta.RegionNotificationEndpointsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionOperations](/compute/docs/reference/rest/beta/regionOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionOperations/delete)` | 

The method `compute.beta.RegionOperationsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionOperations/get)` | 

The method `compute.beta.RegionOperationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionOperations/list)` | 

The method `compute.beta.RegionOperationsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[wait](/compute/docs/reference/rest/beta/regionOperations/wait)` | 

The method `compute.beta.RegionOperationsService.Wait` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionSecurityPolicies](/compute/docs/reference/rest/beta/regionSecurityPolicies)









| 
Methods | 
|



| 

`[addRule](/compute/docs/reference/rest/beta/regionSecurityPolicies/addRule)` | 

The method `compute.beta.RegionSecurityPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/regionSecurityPolicies/delete)` | 

The method `compute.beta.RegionSecurityPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionSecurityPolicies/get)` | 

The method `compute.beta.RegionSecurityPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/beta/regionSecurityPolicies/getRule)` | 

The method `compute.beta.RegionSecurityPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionSecurityPolicies/insert)` | 

The method `compute.beta.RegionSecurityPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionSecurityPolicies/list)` | 

The method `compute.beta.RegionSecurityPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionSecurityPolicies/patch)` | 

The method `compute.beta.RegionSecurityPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/beta/regionSecurityPolicies/patchRule)` | 

The method `compute.beta.RegionSecurityPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/beta/regionSecurityPolicies/removeRule)` | 

The method `compute.beta.RegionSecurityPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/regionSecurityPolicies/setLabels)` | 

The method `compute.beta.RegionSecurityPoliciesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionSnapshotSettings](/compute/docs/reference/rest/beta/regionSnapshotSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/regionSnapshotSettings/get)` | 

The method `compute.beta.RegionSnapshotSettingsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionSnapshotSettings/patch)` | 

The method `compute.beta.RegionSnapshotSettingsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionSnapshots](/compute/docs/reference/rest/beta/regionSnapshots)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionSnapshots/delete)` | 

The method `compute.beta.RegionSnapshotsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionSnapshots/get)` | 

The method `compute.beta.RegionSnapshotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/regionSnapshots/getIamPolicy)` | 

The method `compute.beta.RegionSnapshotsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionSnapshots/insert)` | 

The method `compute.beta.RegionSnapshotsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionSnapshots/list)` | 

The method `compute.beta.RegionSnapshotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/regionSnapshots/setIamPolicy)` | 

The method `compute.beta.RegionSnapshotsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/regionSnapshots/setLabels)` | 

The method `compute.beta.RegionSnapshotsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionSnapshots/testIamPermissions)` | 

The method `compute.beta.RegionSnapshotsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateKmsKey](/compute/docs/reference/rest/beta/regionSnapshots/updateKmsKey)` | 

The method `compute.beta.RegionSnapshotsService.UpdateKmsKey` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionSslCertificates](/compute/docs/reference/rest/beta/regionSslCertificates)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionSslCertificates/delete)` | 

The method `compute.beta.RegionSslCertificatesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionSslCertificates/get)` | 

The method `compute.beta.RegionSslCertificatesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionSslCertificates/insert)` | 

The method `compute.beta.RegionSslCertificatesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionSslCertificates/list)` | 

The method `compute.beta.RegionSslCertificatesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionSslCertificates/testIamPermissions)` | 

The method `compute.beta.RegionSslCertificatesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionSslPolicies](/compute/docs/reference/rest/beta/regionSslPolicies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionSslPolicies/delete)` | 

The method `compute.beta.RegionSslPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionSslPolicies/get)` | 

The method `compute.beta.RegionSslPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionSslPolicies/insert)` | 

The method `compute.beta.RegionSslPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionSslPolicies/list)` | 

The method `compute.beta.RegionSslPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listAvailableFeatures](/compute/docs/reference/rest/beta/regionSslPolicies/listAvailableFeatures)` | 

The method `compute.beta.RegionSslPoliciesService.ListAvailableFeatures` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionSslPolicies/patch)` | 

The method `compute.beta.RegionSslPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionSslPolicies/testIamPermissions)` | 

The method `compute.beta.RegionSslPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionTargetHttpProxies](/compute/docs/reference/rest/beta/regionTargetHttpProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionTargetHttpProxies/delete)` | 

The method `compute.beta.RegionTargetHttpProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionTargetHttpProxies/get)` | 

The method `compute.beta.RegionTargetHttpProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionTargetHttpProxies/insert)` | 

The method `compute.beta.RegionTargetHttpProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionTargetHttpProxies/list)` | 

The method `compute.beta.RegionTargetHttpProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setUrlMap](/compute/docs/reference/rest/beta/regionTargetHttpProxies/setUrlMap)` | 

The method `compute.beta.RegionTargetHttpProxiesService.SetUrlMap` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionTargetHttpProxies/testIamPermissions)` | 

The method `compute.beta.RegionTargetHttpProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionTargetHttpsProxies](/compute/docs/reference/rest/beta/regionTargetHttpsProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionTargetHttpsProxies/delete)` | 

The method `compute.beta.RegionTargetHttpsProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionTargetHttpsProxies/get)` | 

The method `compute.beta.RegionTargetHttpsProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionTargetHttpsProxies/insert)` | 

The method `compute.beta.RegionTargetHttpsProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionTargetHttpsProxies/list)` | 

The method `compute.beta.RegionTargetHttpsProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionTargetHttpsProxies/patch)` | 

The method `compute.beta.RegionTargetHttpsProxiesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSslCertificates](/compute/docs/reference/rest/beta/regionTargetHttpsProxies/setSslCertificates)` | 

The method `compute.beta.RegionTargetHttpsProxiesService.SetSslCertificates` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setUrlMap](/compute/docs/reference/rest/beta/regionTargetHttpsProxies/setUrlMap)` | 

The method `compute.beta.RegionTargetHttpsProxiesService.SetUrlMap` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionTargetHttpsProxies/testIamPermissions)` | 

The method `compute.beta.RegionTargetHttpsProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionTargetTcpProxies](/compute/docs/reference/rest/beta/regionTargetTcpProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionTargetTcpProxies/delete)` | 

The method `compute.beta.RegionTargetTcpProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionTargetTcpProxies/get)` | 

The method `compute.beta.RegionTargetTcpProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionTargetTcpProxies/insert)` | 

The method `compute.beta.RegionTargetTcpProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionTargetTcpProxies/list)` | 

The method `compute.beta.RegionTargetTcpProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionTargetTcpProxies/testIamPermissions)` | 

The method `compute.beta.RegionTargetTcpProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionUrlMaps](/compute/docs/reference/rest/beta/regionUrlMaps)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/regionUrlMaps/delete)` | 

The method `compute.beta.RegionUrlMapsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/regionUrlMaps/get)` | 

The method `compute.beta.RegionUrlMapsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/regionUrlMaps/insert)` | 

The method `compute.beta.RegionUrlMapsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[invalidateCache](/compute/docs/reference/rest/beta/regionUrlMaps/invalidateCache)` | 

The method `compute.beta.RegionUrlMapsService.InvalidateCache` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regionUrlMaps/list)` | 

The method `compute.beta.RegionUrlMapsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/regionUrlMaps/patch)` | 

The method `compute.beta.RegionUrlMapsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/regionUrlMaps/testIamPermissions)` | 

The method `compute.beta.RegionUrlMapsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/regionUrlMaps/update)` | 

The method `compute.beta.RegionUrlMapsService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[validate](/compute/docs/reference/rest/beta/regionUrlMaps/validate)` | 

The method `compute.beta.RegionUrlMapsService.Validate` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regionZones](/compute/docs/reference/rest/beta/regionZones)









| 
Methods | 
|



| 

`[list](/compute/docs/reference/rest/beta/regionZones/list)` | 

The method `compute.beta.RegionZonesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.regions](/compute/docs/reference/rest/beta/regions)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/regions/get)` | 

The method `compute.beta.RegionsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/regions/list)` | 

The method `compute.beta.RegionsService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.reliabilityRisks](/compute/docs/reference/rest/beta/reliabilityRisks)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/reliabilityRisks/get)` | 

The method `compute.beta.ReliabilityRisksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/reliabilityRisks/list)` | 

The method `compute.beta.ReliabilityRisksService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.reservationBlocks](/compute/docs/reference/rest/beta/reservationBlocks)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/reservationBlocks/get)` | 

The method `compute.beta.ReservationBlocksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/reservationBlocks/getIamPolicy)` | 

The method `compute.beta.ReservationBlocksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/reservationBlocks/list)` | 

The method `compute.beta.ReservationBlocksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/beta/reservationBlocks/performMaintenance)` | 

The method `compute.beta.ReservationBlocksService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/reservationBlocks/setIamPolicy)` | 

The method `compute.beta.ReservationBlocksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/reservationBlocks/testIamPermissions)` | 

The method `compute.beta.ReservationBlocksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.reservationSlots](/compute/docs/reference/rest/beta/reservationSlots)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/reservationSlots/get)` | 

The method `compute.beta.ReservationSlotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getVersion](/compute/docs/reference/rest/beta/reservationSlots/getVersion)` | 

The method `compute.beta.ReservationSlotsService.GetVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/reservationSlots/list)` | 

The method `compute.beta.ReservationSlotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/reservationSlots/update)` | 

The method `compute.beta.ReservationSlotsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.reservationSubBlocks](/compute/docs/reference/rest/beta/reservationSubBlocks)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/reservationSubBlocks/get)` | 

The method `compute.beta.ReservationSubBlocksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/reservationSubBlocks/getIamPolicy)` | 

The method `compute.beta.ReservationSubBlocksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getVersion](/compute/docs/reference/rest/beta/reservationSubBlocks/getVersion)` | 

The method `compute.beta.ReservationSubBlocksService.GetVersion` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/reservationSubBlocks/list)` | 

The method `compute.beta.ReservationSubBlocksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/beta/reservationSubBlocks/performMaintenance)` | 

The method `compute.beta.ReservationSubBlocksService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[reportFaulty](/compute/docs/reference/rest/beta/reservationSubBlocks/reportFaulty)` | 

The method `compute.beta.ReservationSubBlocksService.ReportFaulty` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/reservationSubBlocks/setIamPolicy)` | 

The method `compute.beta.ReservationSubBlocksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/reservationSubBlocks/testIamPermissions)` | 

The method `compute.beta.ReservationSubBlocksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.reservations](/compute/docs/reference/rest/beta/reservations)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/reservations/aggregatedList)` | 

The method `compute.beta.AllocationsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/reservations/delete)` | 

The method `compute.beta.AllocationsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/reservations/get)` | 

The method `compute.beta.AllocationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/reservations/getIamPolicy)` | 

The method `compute.beta.AllocationsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/reservations/insert)` | 

The method `compute.beta.AllocationsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/reservations/list)` | 

The method `compute.beta.AllocationsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[performMaintenance](/compute/docs/reference/rest/beta/reservations/performMaintenance)` | 

The method `compute.beta.AllocationsService.PerformMaintenance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resize](/compute/docs/reference/rest/beta/reservations/resize)` | 

The method `compute.beta.AllocationsService.Resize` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/reservations/setIamPolicy)` | 

The method `compute.beta.AllocationsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/reservations/testIamPermissions)` | 

The method `compute.beta.AllocationsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/reservations/update)` | 

The method `compute.beta.AllocationsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.resourcePolicies](/compute/docs/reference/rest/beta/resourcePolicies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/resourcePolicies/aggregatedList)` | 

The method `compute.beta.ResourcePoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/resourcePolicies/delete)` | 

The method `compute.beta.ResourcePoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/resourcePolicies/get)` | 

The method `compute.beta.ResourcePoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/resourcePolicies/getIamPolicy)` | 

The method `compute.beta.ResourcePoliciesService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/resourcePolicies/insert)` | 

The method `compute.beta.ResourcePoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/resourcePolicies/list)` | 

The method `compute.beta.ResourcePoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/resourcePolicies/patch)` | 

The method `compute.beta.ResourcePoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/resourcePolicies/setIamPolicy)` | 

The method `compute.beta.ResourcePoliciesService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/resourcePolicies/testIamPermissions)` | 

The method `compute.beta.ResourcePoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.rolloutPlans](/compute/docs/reference/rest/beta/rolloutPlans)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/rolloutPlans/delete)` | 

The method `compute.beta.RolloutPlansService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/rolloutPlans/get)` | 

The method `compute.beta.RolloutPlansService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/rolloutPlans/insert)` | 

The method `compute.beta.RolloutPlansService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/rolloutPlans/list)` | 

The method `compute.beta.RolloutPlansService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.rollouts](/compute/docs/reference/rest/beta/rollouts)









| 
Methods | 
|



| 

`[advance](/compute/docs/reference/rest/beta/rollouts/advance)` | 

The method `compute.beta.RolloutsService.Advance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[cancel](/compute/docs/reference/rest/beta/rollouts/cancel)` | 

The method `compute.beta.RolloutsService.Cancel` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/rollouts/delete)` | 

The method `compute.beta.RolloutsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/rollouts/get)` | 

The method `compute.beta.RolloutsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/rollouts/list)` | 

The method `compute.beta.RolloutsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[pause](/compute/docs/reference/rest/beta/rollouts/pause)` | 

The method `compute.beta.RolloutsService.Pause` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[resume](/compute/docs/reference/rest/beta/rollouts/resume)` | 

The method `compute.beta.RolloutsService.Resume` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.routers](/compute/docs/reference/rest/beta/routers)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/routers/aggregatedList)` | 

The method `compute.beta.RegionRoutersService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/routers/delete)` | 

The method `compute.beta.RegionRoutersService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteNamedSet](/compute/docs/reference/rest/beta/routers/deleteNamedSet)` | 

The method `compute.beta.RegionRoutersService.DeleteNamedSet` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[deleteRoutePolicy](/compute/docs/reference/rest/beta/routers/deleteRoutePolicy)` | 

The method `compute.beta.RegionRoutersService.DeleteRoutePolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/routers/get)` | 

The method `compute.beta.RegionRoutersService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getNamedSet](/compute/docs/reference/rest/beta/routers/getNamedSet)` | 

The method `compute.beta.RegionRoutersService.GetNamedSet` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getNatIpInfo](/compute/docs/reference/rest/beta/routers/getNatIpInfo)` | 

The method `compute.beta.RegionRoutersService.GetNatIpInfo` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getNatMappingInfo](/compute/docs/reference/rest/beta/routers/getNatMappingInfo)` | 

The method `compute.beta.RegionRoutersService.GetNatMappingInfo` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRoutePolicy](/compute/docs/reference/rest/beta/routers/getRoutePolicy)` | 

The method `compute.beta.RegionRoutersService.GetRoutePolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRouterStatus](/compute/docs/reference/rest/beta/routers/getRouterStatus)` | 

The method `compute.beta.RegionRoutersService.GetRouterStatus` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/routers/insert)` | 

The method `compute.beta.RegionRoutersService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/routers/list)` | 

The method `compute.beta.RegionRoutersService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listBgpRoutes](/compute/docs/reference/rest/beta/routers/listBgpRoutes)` | 

The method `compute.beta.RegionRoutersService.ListBgpRoutes` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listNamedSets](/compute/docs/reference/rest/beta/routers/listNamedSets)` | 

The method `compute.beta.RegionRoutersService.ListNamedSets` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listRoutePolicies](/compute/docs/reference/rest/beta/routers/listRoutePolicies)` | 

The method `compute.beta.RegionRoutersService.ListRoutePolicies` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/routers/patch)` | 

The method `compute.beta.RegionRoutersService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchNamedSet](/compute/docs/reference/rest/beta/routers/patchNamedSet)` | 

The method `compute.beta.RegionRoutersService.PatchNamedSet` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRoutePolicy](/compute/docs/reference/rest/beta/routers/patchRoutePolicy)` | 

The method `compute.beta.RegionRoutersService.PatchRoutePolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[preview](/compute/docs/reference/rest/beta/routers/preview)` | 

The method `compute.beta.RegionRoutersService.Preview` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/routers/testIamPermissions)` | 

The method `compute.beta.RegionRoutersService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/routers/update)` | 

The method `compute.beta.RegionRoutersService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateNamedSet](/compute/docs/reference/rest/beta/routers/updateNamedSet)` | 

The method `compute.beta.RegionRoutersService.UpdateNamedSet` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateRoutePolicy](/compute/docs/reference/rest/beta/routers/updateRoutePolicy)` | 

The method `compute.beta.RegionRoutersService.UpdateRoutePolicy` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.routes](/compute/docs/reference/rest/beta/routes)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/routes/delete)` | 

The method `compute.beta.RoutesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/routes/get)` | 

The method `compute.beta.RoutesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/routes/insert)` | 

The method `compute.beta.RoutesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/routes/list)` | 

The method `compute.beta.RoutesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/routes/testIamPermissions)` | 

The method `compute.beta.RoutesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.securityPolicies](/compute/docs/reference/rest/beta/securityPolicies)









| 
Methods | 
|



| 

`[addRule](/compute/docs/reference/rest/beta/securityPolicies/addRule)` | 

The method `compute.beta.SecurityPoliciesService.AddRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/securityPolicies/aggregatedList)` | 

The method `compute.beta.SecurityPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/securityPolicies/delete)` | 

The method `compute.beta.SecurityPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/securityPolicies/get)` | 

The method `compute.beta.SecurityPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getRule](/compute/docs/reference/rest/beta/securityPolicies/getRule)` | 

The method `compute.beta.SecurityPoliciesService.GetRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/securityPolicies/insert)` | 

The method `compute.beta.SecurityPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/securityPolicies/list)` | 

The method `compute.beta.SecurityPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listPreconfiguredExpressionSets](/compute/docs/reference/rest/beta/securityPolicies/listPreconfiguredExpressionSets)` | 

The method `compute.beta.SecurityPoliciesService.ListPreconfiguredExpressionSets` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/securityPolicies/patch)` | 

The method `compute.beta.SecurityPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patchRule](/compute/docs/reference/rest/beta/securityPolicies/patchRule)` | 

The method `compute.beta.SecurityPoliciesService.PatchRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeRule](/compute/docs/reference/rest/beta/securityPolicies/removeRule)` | 

The method `compute.beta.SecurityPoliciesService.RemoveRule` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/securityPolicies/setLabels)` | 

The method `compute.beta.SecurityPoliciesService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/securityPolicies/testIamPermissions)` | 

The method `compute.beta.SecurityPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.serviceAttachments](/compute/docs/reference/rest/beta/serviceAttachments)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/serviceAttachments/aggregatedList)` | 

The method `compute.beta.ServiceAttachmentsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/serviceAttachments/delete)` | 

The method `compute.beta.ServiceAttachmentsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/serviceAttachments/get)` | 

The method `compute.beta.ServiceAttachmentsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/serviceAttachments/getIamPolicy)` | 

The method `compute.beta.ServiceAttachmentsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/serviceAttachments/insert)` | 

The method `compute.beta.ServiceAttachmentsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/serviceAttachments/list)` | 

The method `compute.beta.ServiceAttachmentsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/serviceAttachments/patch)` | 

The method `compute.beta.ServiceAttachmentsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/serviceAttachments/setIamPolicy)` | 

The method `compute.beta.ServiceAttachmentsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/serviceAttachments/testIamPermissions)` | 

The method `compute.beta.ServiceAttachmentsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.snapshotGroups](/compute/docs/reference/rest/beta/snapshotGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/snapshotGroups/delete)` | 

The method `compute.beta.SnapshotGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/snapshotGroups/get)` | 

The method `compute.beta.SnapshotGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/snapshotGroups/getIamPolicy)` | 

The method `compute.beta.SnapshotGroupsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/snapshotGroups/insert)` | 

The method `compute.beta.SnapshotGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/snapshotGroups/list)` | 

The method `compute.beta.SnapshotGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/snapshotGroups/setIamPolicy)` | 

The method `compute.beta.SnapshotGroupsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/snapshotGroups/testIamPermissions)` | 

The method `compute.beta.SnapshotGroupsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.snapshotSettings](/compute/docs/reference/rest/beta/snapshotSettings)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/snapshotSettings/get)` | 

The method `compute.beta.SnapshotSettingsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/snapshotSettings/patch)` | 

The method `compute.beta.SnapshotSettingsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.snapshots](/compute/docs/reference/rest/beta/snapshots)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/snapshots/aggregatedList)` | 

The method `compute.beta.SnapshotsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/snapshots/delete)` | 

The method `compute.beta.SnapshotsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/snapshots/get)` | 

The method `compute.beta.SnapshotsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/snapshots/getIamPolicy)` | 

The method `compute.beta.SnapshotsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/snapshots/insert)` | 

The method `compute.beta.SnapshotsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/snapshots/list)` | 

The method `compute.beta.SnapshotsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/snapshots/setIamPolicy)` | 

The method `compute.beta.SnapshotsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/snapshots/setLabels)` | 

The method `compute.beta.SnapshotsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/snapshots/testIamPermissions)` | 

The method `compute.beta.SnapshotsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[updateKmsKey](/compute/docs/reference/rest/beta/snapshots/updateKmsKey)` | 

The method `compute.beta.SnapshotsService.UpdateKmsKey` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.sslCertificates](/compute/docs/reference/rest/beta/sslCertificates)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/sslCertificates/aggregatedList)` | 

The method `compute.beta.SslCertificatesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/sslCertificates/delete)` | 

The method `compute.beta.SslCertificatesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/sslCertificates/get)` | 

The method `compute.beta.SslCertificatesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/sslCertificates/insert)` | 

The method `compute.beta.SslCertificatesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/sslCertificates/list)` | 

The method `compute.beta.SslCertificatesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/sslCertificates/testIamPermissions)` | 

The method `compute.beta.SslCertificatesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.sslPolicies](/compute/docs/reference/rest/beta/sslPolicies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/sslPolicies/aggregatedList)` | 

The method `compute.beta.SslPoliciesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/sslPolicies/delete)` | 

The method `compute.beta.SslPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/sslPolicies/get)` | 

The method `compute.beta.SslPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/sslPolicies/insert)` | 

The method `compute.beta.SslPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/sslPolicies/list)` | 

The method `compute.beta.SslPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listAvailableFeatures](/compute/docs/reference/rest/beta/sslPolicies/listAvailableFeatures)` | 

The method `compute.beta.SslPoliciesService.ListAvailableFeatures` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/sslPolicies/patch)` | 

The method `compute.beta.SslPoliciesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/sslPolicies/testIamPermissions)` | 

The method `compute.beta.SslPoliciesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.storagePoolTypes](/compute/docs/reference/rest/beta/storagePoolTypes)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/storagePoolTypes/aggregatedList)` | 

The method `compute.beta.StoragePoolTypesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/storagePoolTypes/get)` | 

The method `compute.beta.StoragePoolTypesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/storagePoolTypes/list)` | 

The method `compute.beta.StoragePoolTypesService.List` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.storagePools](/compute/docs/reference/rest/beta/storagePools)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/storagePools/aggregatedList)` | 

The method `compute.beta.StoragePoolsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/storagePools/delete)` | 

The method `compute.beta.StoragePoolsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/storagePools/get)` | 

The method `compute.beta.StoragePoolsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/storagePools/getIamPolicy)` | 

The method `compute.beta.StoragePoolsService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/storagePools/insert)` | 

The method `compute.beta.StoragePoolsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/storagePools/list)` | 

The method `compute.beta.StoragePoolsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listDisks](/compute/docs/reference/rest/beta/storagePools/listDisks)` | 

The method `compute.beta.StoragePoolsService.ListDisks` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/storagePools/setIamPolicy)` | 

The method `compute.beta.StoragePoolsService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/storagePools/testIamPermissions)` | 

The method `compute.beta.StoragePoolsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/storagePools/update)` | 

The method `compute.beta.StoragePoolsService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.subnetworks](/compute/docs/reference/rest/beta/subnetworks)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/subnetworks/aggregatedList)` | 

The method `compute.beta.SubnetworksService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/subnetworks/delete)` | 

The method `compute.beta.SubnetworksService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[expandIpCidrRange](/compute/docs/reference/rest/beta/subnetworks/expandIpCidrRange)` | 

The method `compute.beta.SubnetworksService.ExpandIpCidrRange` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/subnetworks/get)` | 

The method `compute.beta.SubnetworksService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getIamPolicy](/compute/docs/reference/rest/beta/subnetworks/getIamPolicy)` | 

The method `compute.beta.SubnetworksService.GetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/subnetworks/insert)` | 

The method `compute.beta.SubnetworksService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/subnetworks/list)` | 

The method `compute.beta.SubnetworksService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[listUsable](/compute/docs/reference/rest/beta/subnetworks/listUsable)` | 

The method `compute.beta.SubnetworksService.ListUsable` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/subnetworks/patch)` | 

The method `compute.beta.SubnetworksService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setIamPolicy](/compute/docs/reference/rest/beta/subnetworks/setIamPolicy)` | 

The method `compute.beta.SubnetworksService.SetPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setPrivateIpGoogleAccess](/compute/docs/reference/rest/beta/subnetworks/setPrivateIpGoogleAccess)` | 

The method `compute.beta.SubnetworksService.SetPrivateIpGoogleAccess` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/subnetworks/testIamPermissions)` | 

The method `compute.beta.SubnetworksService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.targetGrpcProxies](/compute/docs/reference/rest/beta/targetGrpcProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/targetGrpcProxies/delete)` | 

The method `compute.beta.TargetGrpcProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/targetGrpcProxies/get)` | 

The method `compute.beta.TargetGrpcProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/targetGrpcProxies/insert)` | 

The method `compute.beta.TargetGrpcProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/targetGrpcProxies/list)` | 

The method `compute.beta.TargetGrpcProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/targetGrpcProxies/patch)` | 

The method `compute.beta.TargetGrpcProxiesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/targetGrpcProxies/testIamPermissions)` | 

The method `compute.beta.TargetGrpcProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.targetHttpProxies](/compute/docs/reference/rest/beta/targetHttpProxies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/targetHttpProxies/aggregatedList)` | 

The method `compute.beta.TargetHttpProxiesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/targetHttpProxies/delete)` | 

The method `compute.beta.TargetHttpProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/targetHttpProxies/get)` | 

The method `compute.beta.TargetHttpProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/targetHttpProxies/insert)` | 

The method `compute.beta.TargetHttpProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/targetHttpProxies/list)` | 

The method `compute.beta.TargetHttpProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/targetHttpProxies/patch)` | 

The method `compute.beta.TargetHttpProxiesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setUrlMap](/compute/docs/reference/rest/beta/targetHttpProxies/setUrlMap)` | 

The method `compute.beta.TargetHttpProxiesService.SetUrlMap` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/targetHttpProxies/testIamPermissions)` | 

The method `compute.beta.TargetHttpProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.targetHttpsProxies](/compute/docs/reference/rest/beta/targetHttpsProxies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/targetHttpsProxies/aggregatedList)` | 

The method `compute.beta.TargetHttpsProxiesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/targetHttpsProxies/delete)` | 

The method `compute.beta.TargetHttpsProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/targetHttpsProxies/get)` | 

The method `compute.beta.TargetHttpsProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/targetHttpsProxies/insert)` | 

The method `compute.beta.TargetHttpsProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/targetHttpsProxies/list)` | 

The method `compute.beta.TargetHttpsProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/targetHttpsProxies/patch)` | 

The method `compute.beta.TargetHttpsProxiesService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setCertificateMap](/compute/docs/reference/rest/beta/targetHttpsProxies/setCertificateMap)` | 

The method `compute.beta.TargetHttpsProxiesService.SetCertificateMap` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setQuicOverride](/compute/docs/reference/rest/beta/targetHttpsProxies/setQuicOverride)` | 

The method `compute.beta.TargetHttpsProxiesService.SetQuicOverride` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSslCertificates](/compute/docs/reference/rest/beta/targetHttpsProxies/setSslCertificates)` | 

The method `compute.beta.TargetHttpsProxiesService.SetSslCertificates` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSslPolicy](/compute/docs/reference/rest/beta/targetHttpsProxies/setSslPolicy)` | 

The method `compute.beta.TargetHttpsProxiesService.SetSslPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setUrlMap](/compute/docs/reference/rest/beta/targetHttpsProxies/setUrlMap)` | 

The method `compute.beta.TargetHttpsProxiesService.SetUrlMap` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/targetHttpsProxies/testIamPermissions)` | 

The method `compute.beta.TargetHttpsProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.targetInstances](/compute/docs/reference/rest/beta/targetInstances)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/targetInstances/aggregatedList)` | 

The method `compute.beta.TargetInstancesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/targetInstances/delete)` | 

The method `compute.beta.TargetInstancesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/targetInstances/get)` | 

The method `compute.beta.TargetInstancesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/targetInstances/insert)` | 

The method `compute.beta.TargetInstancesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/targetInstances/list)` | 

The method `compute.beta.TargetInstancesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/beta/targetInstances/setSecurityPolicy)` | 

The method `compute.beta.TargetInstancesService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/targetInstances/testIamPermissions)` | 

The method `compute.beta.TargetInstancesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.targetPools](/compute/docs/reference/rest/beta/targetPools)









| 
Methods | 
|



| 

`[addHealthCheck](/compute/docs/reference/rest/beta/targetPools/addHealthCheck)` | 

The method `compute.beta.TargetPoolsService.AddHealthCheck` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[addInstance](/compute/docs/reference/rest/beta/targetPools/addInstance)` | 

The method `compute.beta.TargetPoolsService.AddInstance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[aggregatedList](/compute/docs/reference/rest/beta/targetPools/aggregatedList)` | 

The method `compute.beta.TargetPoolsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/targetPools/delete)` | 

The method `compute.beta.TargetPoolsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/targetPools/get)` | 

The method `compute.beta.TargetPoolsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getHealth](/compute/docs/reference/rest/beta/targetPools/getHealth)` | 

The method `compute.beta.TargetPoolsService.GetHealth` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/targetPools/insert)` | 

The method `compute.beta.TargetPoolsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/targetPools/list)` | 

The method `compute.beta.TargetPoolsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeHealthCheck](/compute/docs/reference/rest/beta/targetPools/removeHealthCheck)` | 

The method `compute.beta.TargetPoolsService.RemoveHealthCheck` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[removeInstance](/compute/docs/reference/rest/beta/targetPools/removeInstance)` | 

The method `compute.beta.TargetPoolsService.RemoveInstance` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setBackup](/compute/docs/reference/rest/beta/targetPools/setBackup)` | 

The method `compute.beta.TargetPoolsService.SetBackup` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSecurityPolicy](/compute/docs/reference/rest/beta/targetPools/setSecurityPolicy)` | 

The method `compute.beta.TargetPoolsService.SetSecurityPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/targetPools/testIamPermissions)` | 

The method `compute.beta.TargetPoolsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.targetSslProxies](/compute/docs/reference/rest/beta/targetSslProxies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/targetSslProxies/delete)` | 

The method `compute.beta.TargetSslProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/targetSslProxies/get)` | 

The method `compute.beta.TargetSslProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/targetSslProxies/insert)` | 

The method `compute.beta.TargetSslProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/targetSslProxies/list)` | 

The method `compute.beta.TargetSslProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setBackendService](/compute/docs/reference/rest/beta/targetSslProxies/setBackendService)` | 

The method `compute.beta.TargetSslProxiesService.SetBackendService` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setCertificateMap](/compute/docs/reference/rest/beta/targetSslProxies/setCertificateMap)` | 

The method `compute.beta.TargetSslProxiesService.SetCertificateMap` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setProxyHeader](/compute/docs/reference/rest/beta/targetSslProxies/setProxyHeader)` | 

The method `compute.beta.TargetSslProxiesService.SetProxyHeader` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSslCertificates](/compute/docs/reference/rest/beta/targetSslProxies/setSslCertificates)` | 

The method `compute.beta.TargetSslProxiesService.SetSslCertificates` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setSslPolicy](/compute/docs/reference/rest/beta/targetSslProxies/setSslPolicy)` | 

The method `compute.beta.TargetSslProxiesService.SetSslPolicy` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/targetSslProxies/testIamPermissions)` | 

The method `compute.beta.TargetSslProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.targetTcpProxies](/compute/docs/reference/rest/beta/targetTcpProxies)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/targetTcpProxies/aggregatedList)` | 

The method `compute.beta.TargetTcpProxiesService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/targetTcpProxies/delete)` | 

The method `compute.beta.TargetTcpProxiesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/targetTcpProxies/get)` | 

The method `compute.beta.TargetTcpProxiesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/targetTcpProxies/insert)` | 

The method `compute.beta.TargetTcpProxiesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/targetTcpProxies/list)` | 

The method `compute.beta.TargetTcpProxiesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setBackendService](/compute/docs/reference/rest/beta/targetTcpProxies/setBackendService)` | 

The method `compute.beta.TargetTcpProxiesService.SetBackendService` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setProxyHeader](/compute/docs/reference/rest/beta/targetTcpProxies/setProxyHeader)` | 

The method `compute.beta.TargetTcpProxiesService.SetProxyHeader` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/targetTcpProxies/testIamPermissions)` | 

The method `compute.beta.TargetTcpProxiesService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.targetVpnGateways](/compute/docs/reference/rest/beta/targetVpnGateways)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/targetVpnGateways/aggregatedList)` | 

The method `compute.beta.TargetVpnGatewaysService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/targetVpnGateways/delete)` | 

The method `compute.beta.TargetVpnGatewaysService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/targetVpnGateways/get)` | 

The method `compute.beta.TargetVpnGatewaysService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/targetVpnGateways/insert)` | 

The method `compute.beta.TargetVpnGatewaysService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/targetVpnGateways/list)` | 

The method `compute.beta.TargetVpnGatewaysService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/targetVpnGateways/setLabels)` | 

The method `compute.beta.TargetVpnGatewaysService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/targetVpnGateways/testIamPermissions)` | 

The method `compute.beta.TargetVpnGatewaysService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.urlMaps](/compute/docs/reference/rest/beta/urlMaps)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/urlMaps/aggregatedList)` | 

The method `compute.beta.UrlMapsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/urlMaps/delete)` | 

The method `compute.beta.UrlMapsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/urlMaps/get)` | 

The method `compute.beta.UrlMapsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/urlMaps/insert)` | 

The method `compute.beta.UrlMapsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[invalidateCache](/compute/docs/reference/rest/beta/urlMaps/invalidateCache)` | 

The method `compute.beta.UrlMapsService.InvalidateCache` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/urlMaps/list)` | 

The method `compute.beta.UrlMapsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/urlMaps/patch)` | 

The method `compute.beta.UrlMapsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/urlMaps/testIamPermissions)` | 

The method `compute.beta.UrlMapsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/urlMaps/update)` | 

The method `compute.beta.UrlMapsService.Update` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[validate](/compute/docs/reference/rest/beta/urlMaps/validate)` | 

The method `compute.beta.UrlMapsService.Validate` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.vpnGateways](/compute/docs/reference/rest/beta/vpnGateways)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/vpnGateways/aggregatedList)` | 

The method `compute.beta.VpnGatewaysService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/vpnGateways/delete)` | 

The method `compute.beta.VpnGatewaysService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/vpnGateways/get)` | 

The method `compute.beta.VpnGatewaysService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[getStatus](/compute/docs/reference/rest/beta/vpnGateways/getStatus)` | 

The method `compute.beta.VpnGatewaysService.GetStatus` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/vpnGateways/insert)` | 

The method `compute.beta.VpnGatewaysService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/vpnGateways/list)` | 

The method `compute.beta.VpnGatewaysService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/vpnGateways/setLabels)` | 

The method `compute.beta.VpnGatewaysService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/vpnGateways/testIamPermissions)` | 

The method `compute.beta.VpnGatewaysService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.vpnTunnels](/compute/docs/reference/rest/beta/vpnTunnels)









| 
Methods | 
|



| 

`[aggregatedList](/compute/docs/reference/rest/beta/vpnTunnels/aggregatedList)` | 

The method `compute.beta.VpnTunnelsService.AggregatedList` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[delete](/compute/docs/reference/rest/beta/vpnTunnels/delete)` | 

The method `compute.beta.VpnTunnelsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/vpnTunnels/get)` | 

The method `compute.beta.VpnTunnelsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/vpnTunnels/insert)` | 

The method `compute.beta.VpnTunnelsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/vpnTunnels/list)` | 

The method `compute.beta.VpnTunnelsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[setLabels](/compute/docs/reference/rest/beta/vpnTunnels/setLabels)` | 

The method `compute.beta.VpnTunnelsService.SetLabels` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[testIamPermissions](/compute/docs/reference/rest/beta/vpnTunnels/testIamPermissions)` | 

The method `compute.beta.VpnTunnelsService.TestPermissions` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.wireGroups](/compute/docs/reference/rest/beta/wireGroups)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/wireGroups/delete)` | 

The method `compute.beta.WireGroupsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/wireGroups/get)` | 

The method `compute.beta.WireGroupsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/wireGroups/insert)` | 

The method `compute.beta.WireGroupsService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/wireGroups/list)` | 

The method `compute.beta.WireGroupsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[patch](/compute/docs/reference/rest/beta/wireGroups/patch)` | 

The method `compute.beta.WireGroupsService.Patch` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.zoneOperations](/compute/docs/reference/rest/beta/zoneOperations)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/zoneOperations/delete)` | 

The method `compute.beta.ZoneOperationsService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/zoneOperations/get)` | 

The method `compute.beta.ZoneOperationsService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/zoneOperations/list)` | 

The method `compute.beta.ZoneOperationsService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[wait](/compute/docs/reference/rest/beta/zoneOperations/wait)` | 

The method `compute.beta.ZoneOperationsService.Wait` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.zoneVmExtensionPolicies](/compute/docs/reference/rest/beta/zoneVmExtensionPolicies)









| 
Methods | 
|



| 

`[delete](/compute/docs/reference/rest/beta/zoneVmExtensionPolicies/delete)` | 

The method `compute.beta.ZoneVmExtensionPoliciesService.Delete` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[get](/compute/docs/reference/rest/beta/zoneVmExtensionPolicies/get)` | 

The method `compute.beta.ZoneVmExtensionPoliciesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[insert](/compute/docs/reference/rest/beta/zoneVmExtensionPolicies/insert)` | 

The method `compute.beta.ZoneVmExtensionPoliciesService.Insert` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/zoneVmExtensionPolicies/list)` | 

The method `compute.beta.ZoneVmExtensionPoliciesService.List` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[update](/compute/docs/reference/rest/beta/zoneVmExtensionPolicies/update)` | 

The method `compute.beta.ZoneVmExtensionPoliciesService.Update` is not available in Cloud de Confiance by S3NS. | 
|






## REST Resource: [beta.zones](/compute/docs/reference/rest/beta/zones)









| 
Methods | 
|



| 

`[get](/compute/docs/reference/rest/beta/zones/get)` | 

The method `compute.beta.ZonesService.Get` is not available in Cloud de Confiance by S3NS. | 
|

| 

`[list](/compute/docs/reference/rest/beta/zones/list)` | 

The method `compute.beta.ZonesService.List` is not available in Cloud de Confiance by S3NS. | 
|