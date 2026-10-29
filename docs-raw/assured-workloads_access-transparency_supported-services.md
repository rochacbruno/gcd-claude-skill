# Supported services

Source: https://berlin.devsitetest.how/assured-workloads/access-transparency/docs/supported-services
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/assured-workloads/access-transparency/docs/tpc-differences) for more details.














- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Access Transparency

](https://berlin.devsitetest.how/assured-workloads/access-transparency/docs)






- 








[

Guides

](https://berlin.devsitetest.how/assured-workloads/access-transparency/docs/overview)

























# Supported services



This page lists all the Google Cloud Dedicated in Germany services that write Access Transparency logs.

*GA* indicates that a log type is generally available for a
service. *Preview* indicates that a log type is available, but might be changed in
backward-incompatible ways and is not subject to any SLA or deprecation policy.

If you want to enable Access Transparency logs, see
[Enabling Access Transparency](/assured-workloads/access-transparency/docs/enable#enabling).

## Supported Google Cloud Dedicated in Germany services

Access Transparency supports the following Google Cloud Dedicated in Germany services:






| 
Supported service | 
Launch stage | 
Notes | 
|





| 


[Access Context Manager](/access-context-manager/docs)
| 



GA
| 



None

| 
|


| 


[Access Transparency](/assured-workloads/access-transparency/docs)
| 



GA
| 



None

| 
|


| 


[Agent Assist](/agent-assist/docs)
| 



GA
| 



None

| 
|


| 


[Agent Identity](/iam/docs/agent-identity-overview)
| 



GA
| 



None

| 
|


| 


[Agent Platform Feature Store](/gemini-enterprise-agent-platform/machine-learning/featurestore)
| 



GA
| 



None

| 
|


| 


[Agent Runtime on Gemini Enterprise Agent Platform](/agent-builder/agent-engine/overview)
| 



GA
| 



None

| 
|


| 


[Agent Search](/generative-ai-app-builder/docs)
| 



GA
| 



Access to your data in Gemini Enterprise Agent Platform by personnel isn't always logged. See
[Limitations of Access Transparency in Agent Platform](/gemini-enterprise-agent-platform/machine-learning/general/access-transparency#limitations)
for more information.


| 
|


| 


[AlloyDB for PostgreSQL](/alloydb)
| 



GA
| 



None

| 
|


| 


[Anti Money Laundering AI](/financial-services/anti-money-laundering/docs)
| 



GA
| 



None

| 
|


| 


[Apigee](/apigee)
| 



GA
| 



The following Apigee features are not supported by Access Transparency:


- Apigee portal

- Features in the Preview launch stage

Additionally, Apigee Hybrid customers must
[upgrade to the latest version](/apigee/docs/hybrid/supported-platforms#release-history)
to get full Access Transparency support.


| 
|


| 


[API keys](/api-keys/docs/overview)
| 



Preview
| 



None

| 
|


| 


[App Engine](/appengine)
| 



GA
| 



Cloud Storage and Cloud SQL are the only
[compatible storage backends](/appengine/docs/standard/java/storage) for App Engine
supported by Access Transparency.


| 
|


| 


[App Hub](/app-hub/docs)
| 



GA
| 



None

| 
|


| 


[App Topology](/app-topology)
| 



GA
| 



Access Transparency supports One Graph.


| 
|


| 


[Application Design Center](/application-design-center/docs)
| 



GA
| 



None

| 
|


| 


[Application Integration](/application-integration/docs)
| 



GA
| 



None

| 
|


| 


[Artifact Analysis](/artifact-analysis/docs/artifact-analysis)
| 



GA
| 



None

| 
|


| 


[Artifact Registry](/artifact-registry/docs)
| 



GA
| 



None

| 
|


| 


[Automotive AI Agent](/solutions/vertical-ai-agents?e=48754805#automotive-agent)
| 



GA
| 



None

| 
|


| 


[Backup for GKE](/kubernetes-engine/docs/add-on/backup-for-gke)
| 



GA
| 



None

| 
|


| 


[Backup and DR Service](/backup-disaster-recovery/docs/concepts/backup-dr)
| 



GA
| 



Workloads that depend on a management console and backup/recovery appliances are not supported by Access Transparency.


| 
|


| 


[BigQuery](/bigquery)
| 



GA
| 



Some information about your queries, tables, and datasets might not generate an
Access Transparency log entry if viewed by Cloud Customer Care. Viewing query text, table names,
dataset names, and dataset access control lists might not generate Access Transparency log
entries; this access pathway gives read-only access. Viewing query results and table or dataset
data generates Access Transparency log entries.

Data in queries residing in
[non-Google regions for BigQuery Omni](/bigquery-omni/docs/locations) does
not generate an Access Transparency log entry.

Gemini in BigQuery is not supported in Assured Workloads.

Access Transparency supports [
BigQuery data preparation](/bigquery/docs/data-prep-introduction).

Access Transparency supports [Lakehouse
tables](/lakehouse/docs/introduction).


| 
|


| 


[Bigtable](/bigtable)
| 



GA
| 



None

| 
|


| 


[BigQuery Data Transfer Service](/bigquery/docs/dts-introduction)
| 



GA
| 



None

| 
|


| 


[Binary Authorization](/binary-authorization/docs)
| 



GA
| 



None

| 
|


| 


[Certificate Authority Service](/certificate-authority-service)
| 



GA
| 



None

| 
|


| 


[Certificate Manager](/certificate-manager/docs/overview)
| 



GA
| 



None

| 
|


| 


[Chrome Enterprise Premium](/chrome-enterprise-premium/docs/overview)
| 



GA
| 



Access Transparency supports
[Chrome Enterprise Premium secure gateway](/chrome-enterprise-premium/docs/security-gateway-private-web-apps#create-gateway).


| 
|


| 


[Cloud Asset Inventory](/asset-inventory/docs/asset-inventory-overview)
| 



GA
| 



None

| 
|


| 


[Cloud Billing](/billing/docs)
| 



Preview
| 



None

| 
|


| 


[Cloud Build](/build)
| 



GA
| 



None

| 
|


| 


[Managed Service for Apache Airflow](/composer)
| 



GA
| 



None

| 
|


| 


[Cloud Data Fusion](/data-fusion)
| 



GA
| 



None

| 
|


| 


[Cloud Deploy](/deploy/docs/overview)
| 



GA
| 



None

| 
|


| 


[Cloud DNS](/dns)
| 



GA
| 



None

| 
|


| 


[Cloud Domains](/domains/docs/overview)
| 



GA
| 



None

| 
|


| 


[Cloud External Key Manager (Cloud EKM)](/kms/docs/ekm)
| 



GA
| 



None

| 
|


| 


[Fault Injection Testing](/fault-injection-testing/overview)
| 



GA
| 



None

| 
|


| 


[Cloud Run functions](/functions)
| 



GA
| 



None

| 
|


| 


[Cloud Healthcare API](/healthcare-api)
| 



GA
| 



Features within Cloud Healthcare API that are not yet generally available might not
generate Access Transparency logs. For more information, see the
[Cloud Healthcare API documentation](/healthcare-api/docs).


| 
|


| 


[Cloud Interconnect](/network-connectivity/docs/interconnect)
| 



GA
| 



None

| 
|


| 


[Cloud Key Management Service (Cloud KMS)](/kms/docs)
| 



GA
| 



None

| 
|


| 


[Cloud Logging](/logging)
| 



GA
| 



None

| 
|


| 


[Cloud NAT](/nat)
| 



GA
| 



None

| 
|


| 


[Cloud OS Login API](/compute/docs/oslogin)
| 



GA
| 



None

| 
|


| 


[Cloud Router](/network-connectivity/docs/router)
| 



GA
| 



None

| 
|


| 


[Cloud Run](/run/docs)
| 



GA
| 



None

| 
|


| 


[Cloud Scheduler](/scheduler/docs/overview)
| 



GA
| 



None

| 
|


| 


[Cloud SQL](/sql)
| 



GA
| 



None

| 
|


| 


[Cloud Service Mesh](/service-mesh)
| 



GA
| 



None

| 
|


| 


[Cloud Storage](/storage)
| 



GA
| 



None

| 
|


| 


[Cloud Tasks](/tasks)
| 



GA
| 



None

| 
|


| 


[Cloud TPU](/tpu/docs/intro-to-tpu)
| 



GA
| 



None

| 
|


| 


[Cloud Trace](/trace/docs)
| 



GA
| 



None

| 
|


| 


[Cloud VPN](/network-connectivity/docs/vpn)
| 



GA
| 



None

| 
|


| 


[Cloud Vision API](/vision)
| 



GA
| 



None

| 
|


| 


[Cloud Workstations](/workstations/docs)
| 



GA
| 



None

| 
|


| 


[Colab Enterprise](/colab/docs/introduction)
| 



GA
| 



None

| 
|


| 


[Compute Engine](/compute-engine)
| 



GA
| 



None

| 
|


| 


[Container Registry](/container-registry/docs)
| 



Preview
| 



None

| 
|


| 


[Customer Experience Agent Studio](/customer-engagement-ai/conversational-agents/ps)
| 



GA
| 



None

| 
|


| 


[Customer Experience Insights](/contact-center/insights/docs)
| 



GA
| 



None

| 
|


| 


[Database Center](/database-center)
| 



GA
| 



None

| 
|


| 


[Database Migration Service](/database-migration/docs)
| 



GA
| 



None

| 
|


| 


[Dataflow](/dataflow/docs)
| 



GA
| 



None

| 
|


| 


[Dataform](/dataform)
| 



GA
| 



None

| 
|


| 


[Knowledge Catalog](/dataplex)
| 



GA
| 



None

| 
|


| 


[Managed Service for Apache Spark](/dataproc/docs)
| 



GA
| 



None

| 
|


| 


[Datastream](/datastream/docs)
| 



GA
| 



None

| 
|


| 


[Developer Connect](/developer-connect/docs)
| 



GA
| 



None

| 
|


| 


[Dialogflow CX](/dialogflow/cx/docs)
| 



GA
| 



None

| 
|


| 


[Google Distributed Cloud](/distributed-cloud/edge/latest/docs)
| 



GA
| 



None

| 
|


| 


[DNS Armor](/assured-workloads/access-transparency/docs/dns/docs/threat-detection)
| 



GA
| 



None

| 
|


| 


[Document AI](/document-ai/docs)
| 



GA
| 



None

| 
|


| 


[Eventarc](/eventarc/docs)
| 



GA
| 



None

| 
|


| 


[External passthrough Network Load Balancer](/load-balancing/docs/passthrough-network-load-balancer)
| 



GA
| 



None

| 
|


| 


[Filestore](/filestore)
| 



GA
| 



None

| 
|


| 


[Firebase App Hosting](https://firebase.google.com/docs/app-hosting)
| 



Preview
| 



None

| 
|


| 


[Firebase Data Connect](https://firebase.google.com/docs/data-connect)
| 



GA
| 



None

| 
|


| 


[Firebase Security Rules](https://firebase.google.com/docs/rules)
| 



GA
| 



None

| 
|


| 


[Firestore](https://firebase.google.com/docs/firestore)
| 



GA
| 



None

| 
|


| 


[Flow Analyzer](/network-intelligence-center/docs/flow-analyzer/overview)
| 



GA
| 



None

| 
|


| 


[Gemini Data Analytics](/gemini/data-agents)
| 



GA
| 



None

| 
|


| 


[Gemini Enterprise Agent Platform](/gemini-enterprise-agent-platform/machine-learning/general/access-transparency)
| 



GA
| 



Access to your data in Gemini Enterprise Agent Platform by personnel isn't always logged. See
[Limitations of Access Transparency in Agent Platform](/gemini-enterprise-agent-platform/machine-learning/general/access-transparency#limitations)
for more information.


| 
|


| 


[Gemini Enterprise Agent Platform Workbench instances](/gemini-enterprise-agent-platform/notebooks/workbench/instances/introduction)
| 



GA
| 



None

| 
|


| 


[Gemini Enterprise Agent Platform Workbench managed notebooks](/gemini-enterprise-agent-platform/notebooks/workbench/managed/introduction)
| 



GA
| 



None

| 
|


| 


[Gemini Enterprise Agent Platform Workbench user-managed notebooks](/gemini-enterprise-agent-platform/notebooks/workbench/user-managed/introduction)
| 



GA
| 



None

| 
|


| 


[Gemini Enterprise for Customer Experience](/customer-engagement-ai)
| 



GA
| 



None

| 
|


| 


[GKE Connect](/kubernetes-engine/docs)
| 



GA
| 



None

| 
|


| 


[GKE Hub](/anthos/fleet-management/docs)
| 



GA
| 



None

| 
|


| 


[GKE Identity Service](/anthos/identity)
| 



GA
| 



None

| 
|


| 


[Google Cloud Armor](/armor)
| 



GA
| 



Access Transparency logs are generated for regional Google Cloud Armor security policies. Global
Google Cloud Armor security policies won't generate logs.


| 
|


| 


[Google Cloud Managed Lustre](/managed-lustre/docs/overview)
| 



GA
| 



None

| 
|


| 


[Google Cloud Managed Service for Apache Kafka](/managed-service-for-apache-kafka/docs/overview)
| 



GA
| 



None

| 
|


| 


[Google Cloud NetApp Volumes](/netapp/volumes/docs)
| 



GA
| 



None

| 
|


| 


[Google Cloud Observability](/stackdriver/docs)
| 



GA
| 



None

| 
|


| 


[Google Distributed Cloud](/anthos/gke/docs/on-prem)
| 



GA
| 



None

| 
|


| 


[Google Kubernetes Engine](/kubernetes-engine/docs)
| 



GA
| 



Access Transparency supports
[Image streaming](/kubernetes-engine/docs/how-to/image-streaming).


| 
|


| 


[Google Security Operations SIEM](/chronicle-siem)
| 



GA
| 



None

| 
|


| 


[Google Security Operations SOAR](/chronicle/docs/soar)
| 



GA
| 



None

| 
|


| 


[Cloud HSM](/kms/docs/hsm)
| 



GA
| 



None

| 
|


| 


[Identity and Access Management (IAM)](/iam/docs)
| 



GA
| 



Access Transparency supports System for Cross-domain Identity Management (SCIM) through Workforce Identity Federation.


| 
|


| 


[Identity-Aware Proxy](/iap/docs)
| 



GA
| 



None

| 
|


| 


[Image streaming](/kubernetes-engine/docs/how-to/image-streaming)
| 



GA
| 



None

| 
|


| 


[Infrastructure Manager](/infrastructure-manager/docs)
| 



GA
| 



None

| 
|


| 


[Integration Connectors](/integration-connectors/docs)
| 



GA
| 



None

| 
|


| 


[Internal passthrough Network Load Balancer](/load-balancing/docs/internal)
| 



GA
| 



None

| 
|


| 


[Jurisdictional Google Cloud Dedicated console](/assured-workloads/docs/jurisdictional-console)
| 



GA
| 



None

| 
|


| 


[Looker (Google Cloud core)](/looker/docs/looker-core-overview)
| 



GA
| 



None

| 
|


| 


[Data Studio](/looker/docs/studio)
| 



GA
| 



None

| 
|


| 


[Memorystore for Redis](/memorystore/docs/redis)
| 



GA
| 



None

| 
|


| 


[Memorystore for Redis Cluster](/memorystore/docs/cluster)
| 



GA
| 



None

| 
|


| 


[Memorystore for Valkey](/memorystore/docs/valkey)
| 



GA
| 



None

| 
|


| 


[Model Armor](/security-command-center/docs/model-armor-overview)
| 



GA
| 



None

| 
|


| 


[Cloud Monitoring](/monitoring)
| 



GA
| 



None

| 
|


| 


[NCC Gateway](/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview)
| 



GA
| 



None

| 
|


| 


[Network Connectivity Center](/network-connectivity/docs/network-connectivity-center/concepts/overview)
| 



GA
| 



None

| 
|


| 


[Org Lifecycle API](/resource-manager/reference/rest/v1/organizations#LifecycleState)
| 



GA
| 



None

| 
|


| 


[Organization Policy Service](/resource-manager/docs/organization-policy/overview)
| 



GA
| 



None

| 
|


| 


[Parameter Manager](/secret-manager/parameter-manager/docs/overview)
| 



GA
| 



None

| 
|


| 


[Persistent Disk](/compute/docs/disks)
| 



GA
| 



None

| 
|


| 


[Privileged Access Manager](/iam/docs/pam-overview)
| 



GA
| 



None

| 
|


| 


[Pub/Sub](/pubsub/docs)
| 



GA
| 



None

| 
|


| 


[regional external Application Load Balancer](/load-balancing/docs/https#regional-td)
| 



GA
| 



None

| 
|


| 


[regional external proxy Network Load Balancer](/load-balancing/docs/tcp#regional-external-proxy-network-load-balancer)
| 



GA
| 



None

| 
|


| 


[regional internal Application Load Balancer](/load-balancing/docs/l7-internal)
| 



GA
| 



None

| 
|


| 


[regional internal proxy Network Load Balancer](/load-balancing/docs/tcp#regional-internal-proxy-network-load-balancer)
| 



GA
| 



None

| 
|


| 


[Resource Manager](/resource-manager/docs)
| 



GA
| 



None

| 
|


| 


[Secret Manager](/secret-manager/docs)
| 



GA
| 



None

| 
|


| 


[Secure Source Manager](/secure-source-manager/docs)
| 



GA
| 



None

| 
|


| 


[Secure Web Proxy](/secure-web-proxy/docs/overview)
| 



GA
| 



None

| 
|


| 


[Security Command Center](/security-command-center/docs/security-command-center-overview)
| 



GA
| 



Access Transparency supports the Security Command Center Premium tier.


| 
|


| 


[Sensitive Data Protection](/dlp/docs)
| 



GA
| 



None

| 
|


| 


[Serverless VPC Access](/vpc/docs/serverless-vpc-access)
| 



GA
| 



None

| 
|


| 


[Service Management](/service-infrastructure/docs/service-management/reference/rest)
| 



GA
| 



None

| 
|


| 


[Service Usage](/service-usage/docs/reference/rest)
| 



Preview
| 



None

| 
|


| 


[Spanner](/spanner)
| 



GA
| 



None

| 
|


| 


[Speaker ID](/speaker-id)
| 



GA
| 



None

| 
|


| 


[Speech-to-Text](/speech-to-text)
| 



GA
| 



None

| 
|


| 


[Storage Intelligence](/storage/docs/storage-intelligence/overview)
| 



GA
| 



None

| 
|


| 


[Storage Transfer Service](/storage-transfer-service)
| 



GA
| 



None

| 
|


| 


[Text-to-Speech](/text-to-speech/docs)
| 



GA
| 





| 
|


| 


[Unified Maintenance](/unified-maintenance/docs)
| 



GA
| 



None

| 
|


| 


[Vector Search](/gemini-enterprise-agent-platform/build/vector-search/overview)
| 



GA
| 



(except for Vector Search 2.0) Access to your data in Gemini Enterprise Agent Platform by personnel isn't always logged. See
[Limitations of Access Transparency in Agent Platform](/gemini-enterprise-agent-platform/machine-learning/general/access-transparency#limitations)
for more information.


| 
|


| 


[Virtual Private Cloud (VPC)](/vpc/docs)
| 



GA
| 



None

| 
|


| 


[VM Manager](/compute/docs/vm-manager)
| 



GA
| 



None

| 
|


| 


[Web Risk](/web-risk/docs/overview)
| 



GA
| 



None

| 
|


| 


[Workflows](/workflows/docs/overview)
| 



GA
| 



None

| 
|


| 


[Workforce Identity Federation](/iam/docs/workforce-identity-federation)
| 



GA
| 



None

| 
|


| 


[Workload Identity Federation](/iam/docs/workload-identity-federation)
| 



GA
| 



None

| 
|