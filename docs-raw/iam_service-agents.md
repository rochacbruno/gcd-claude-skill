# Service agents

Source: https://berlin.devsitetest.how/iam/docs/service-agents
Last updated: 2026-07-21

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

IAM

](https://berlin.devsitetest.how/iam/docs)






- 








[

Reference

](https://berlin.devsitetest.how/iam/docs/apis)












# Service agents 














Some Google Cloud Dedicated in Germany services have [*service agents*](/iam/docs/service-account-types#service-agents) that allow
the service to access your resources. If an API requires a service agent, then
Google Cloud Dedicated creates the service agent at some point after you activate
and use the API. You might see evidence of these service agents in several
different places, including a project's [allow policy](/iam/docs/allow-policies) and
[audit log entries](/iam/docs/audit-logging) for various services. For more information
about when Google Cloud Dedicated creates service agents, see [Service agent
creation](/iam/docs/service-account-types#creation).

If you manage your allow policies with a declarative framework or a
policies-as-code system, you might want to create and grant roles to a service
agent before you use the service it belongs to. In these cases, after you
[identify the service agent](/iam/docs/create-service-agents#identify-agents) you need to create, you can
[trigger service agent creation](/iam/docs/create-service-agents#create) yourself without using the
service.

This page provides details about the service agents for all services that are
publicly available, including the following:

- The domain name used in the service agent's email address.

- 

The role that the service agent is granted on the project.

When the service agent is created, Google Cloud Dedicated grants this role
automatically.

Google Cloud Dedicated can introduce new service agents at any time, both for
existing services and for new services. Both the creation time and the email address format for service agents are subject to change.







| 
Service agent | 
Role | 
|



| 


#### AI Platform Custom Code Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-aiplatform-cc.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Custom Code Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent)

(`roles/aiplatform.customCodeServiceAgent`)




Granted on the project.


| 
|

| 


#### AI Platform Example Store Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-es.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### AI Platform Fine Tuning Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-aiplatform-ft.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent)

(`roles/aiplatform.serviceAgent`)




Granted on the project.


| 
|

| 


#### AI Platform Infra Spanner Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-aiplatform-is.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### AI Platform Private Instance (PIE) Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-aiplatform-pie.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent)

(`roles/aiplatform.serviceAgent`)




Granted on the project.


| 
|

| 


#### AI Platform Rapid Eval Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-eval.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Rapid Eval Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.rapidevalServiceAgent)

(`roles/aiplatform.rapidevalServiceAgent`)




Granted on the project.


| 
|

| 


#### AI Platform Reasoning Engine Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-aiplatform-re.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Reasoning Engine Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent)

(`roles/aiplatform.reasoningEngineServiceAgent`)




Granted on the project.


| 
|

| 


#### AI Platform Resource Identity

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-ri-aiplatform.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### AI Platform Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-aiplatform.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent)

(`roles/aiplatform.serviceAgent`)




Granted on the project.


| 
|

| 


#### API Hub Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `apihub.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apihub.eu0-system.iam.gserviceaccount.com`

| 



[API-Hub Runtime Project Service Agent](/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent)

(`roles/apihub.runtimeProjectServiceAgent`)




Granted on the project.


| 
|

| 


#### API Keys Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `apikeys.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apikeys.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### APIM Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `apim.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apim.eu0-system.iam.gserviceaccount.com`

| 



[APIM API Discovery Service Agent](/iam/docs/roles-permissions/apim#apim.apiDiscoveryServiceAgent)

(`roles/apim.apiDiscoveryServiceAgent`)




Granted on the project.


| 
|

| 


#### ASM Mesh Control Plane Service Account

Service agent for `meshconfig.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-meshcontrolplane.eu0-system.iam.gserviceaccount.com`

| 



[Mesh Managed Control Plane Service Agent](/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent)

(`roles/meshcontrolplane.serviceAgent`)




Granted on the project.


| 
|

| 


#### ASM Mesh Data Plane Service Account

Service agent for `meshconfig.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-meshdataplane.eu0-system.iam.gserviceaccount.com`

| 



[Mesh Data Plane Service Agent](/iam/docs/roles-permissions/anthosservicemesh#meshdataplane.serviceAgent)

(`roles/meshdataplane.serviceAgent`)




Granted on the project.


| 
|

| 


#### Access Approval Service Agent

Service agent for `accessapproval.googleapis.com`. 


For the project:





- `service-p PROJECT_NUMBER @gcp-sa-accessapproval.eu0-system.iam.gserviceaccount.com`




For the folder:





- `service-f FOLDER_NUMBER @gcp-sa-accessapproval.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-o ORGANIZATION_NUMBER @gcp-sa-accessapproval.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Ads Data Hub Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `adsdatahub.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-adsdatahub.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Agent Gateway Service Account

Service agent for `networkservices.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-agentgateway.eu0-system.iam.gserviceaccount.com`

| 



[Agent Gateway Service Agent](/iam/docs/roles-permissions/agentgateway#agentgateway.serviceAgent)

(`roles/agentgateway.serviceAgent`)




Granted on the project.


| 
|

| 


#### Agent Registry Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `agentregistry.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-agentregistry.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### AlloyDB Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `alloydb.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-alloydb.eu0-system.iam.gserviceaccount.com`

| 



[AlloyDB Service Agent](/iam/docs/roles-permissions/alloydb#alloydb.serviceAgent)

(`roles/alloydb.serviceAgent`)




Granted on the project.


| 
|

| 


#### AlloyDB Service Agent

Service agent for `alloydb.googleapis.com`. 


`c- PROJECT_NUMBER - IDENTIFIER @gcp-sa-alloydb.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Analytics Hub Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `analyticshub.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-analyticshub.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Anthos Audit Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `anthosaudit.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-anthosaudit.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Audit Service Agent](/iam/docs/roles-permissions/anthosaudit#anthosaudit.serviceAgent)

(`roles/anthosaudit.serviceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Config Management Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `anthosconfigmanagement.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-anthosconfigmanagement.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Config Management Service Agent](/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent)

(`roles/anthosconfigmanagement.serviceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Identity Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `anthosidentityservice.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-anthosidentityservice.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Identity Service Agent](/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent)

(`roles/anthosidentityservice.serviceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Multi-Cloud Container Service Agent

Service agent for `gkemulticloud.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkemulticloudcontainer.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Multi-Cloud Container Service Agent](/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent)

(`roles/gkemulticloud.containerServiceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Multi-Cloud Control Plane Machine Service Agent

Service agent for `gkemulticloud.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkemulticloudcpmachine.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Multi-Cloud Control Plane Machine Service Agent](/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.controlPlaneMachineServiceAgent)

(`roles/gkemulticloud.controlPlaneMachineServiceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Multi-Cloud Node Pool Machine Service Agent

Service agent for `gkemulticloud.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkemulticloudnpmachine.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Multi-Cloud Node Pool Machine Service Agent](/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.nodePoolMachineServiceAgent)

(`roles/gkemulticloud.nodePoolMachineServiceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Multi-Cloud Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `gkemulticloud.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkemulticloud.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Multi-Cloud Service Agent](/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent)

(`roles/gkemulticloud.serviceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Policy Controller Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `anthospolicycontroller.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-anthospolicycontroller.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Policy Controller Service Agent](/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent)

(`roles/anthospolicycontroller.serviceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `anthos.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-anthos.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Service Agent](/iam/docs/roles-permissions/anthos#anthos.serviceAgent)

(`roles/anthos.serviceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Service Mesh Service Account

Service agent for `meshconfig.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-servicemesh.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Service Mesh Service Agent](/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent)

(`roles/anthosservicemesh.serviceAgent`)




Granted on the project.


| 
|

| 


#### Anthos Support Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `connectgateway.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-anthossupport.eu0-system.iam.gserviceaccount.com`

| 



[Anthos Support Service Agent](/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent)

(`roles/anthossupport.serviceAgent`)




Granted on the project.


| 
|

| 


#### Apigee Registry Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `apigeeregistry.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apigeeregistry.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Apigee Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `apigee.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apigee.eu0-system.iam.gserviceaccount.com`

| 



[Apigee Service Agent](/iam/docs/roles-permissions/apigee#apigee.serviceAgent)

(`roles/apigee.serviceAgent`)




Granted on the project.


| 
|

| 


#### Apigee Service Agent

Service agent for `apigee.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apigee.eu0-system.iam.gserviceaccount.com`

| 



[Apigee Core Service Agent](/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent)

(`roles/apigee.coreServiceAgent`)




Granted on the project.


| 
|

| 


#### App Development Experience Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `appdevelopmentexperience.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-appdevexperience.eu0-system.iam.gserviceaccount.com`

| 



[App Development Experience Service Agent](/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent)

(`roles/appdevelopmentexperience.serviceAgent`)




Granted on the project.


| 
|

| 


#### App Engine Flexible Environment Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `appengineflex.googleapis.com`. 


`service- PROJECT_NUMBER @gae-api-prod.eu0-system.iam.gserviceaccount.com`

| 



[App Engine flexible environment Service Agent](/iam/docs/roles-permissions/appengineflex#appengineflex.serviceAgent)

(`roles/appengineflex.serviceAgent`)




Granted on the project.


| 
|

| 


#### App Engine Standard Environment Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `appenginestandard.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-gae-service.eu0-system.iam.gserviceaccount.com`

| 



[App Engine Standard Environment Service Agent](/iam/docs/roles-permissions/appengine#appengine.serviceAgent)

(`roles/appengine.serviceAgent`)




Granted on the project.


| 
|

| 


#### App Hub Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `apphub.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apphub.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### App Optimize Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `appoptimize.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-appoptimize.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Application Integration Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `integrations.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-integrations.eu0-system.iam.gserviceaccount.com`

| 



[Application Integration Service Agent](/iam/docs/roles-permissions/integrations#integrations.serviceAgent)

(`roles/integrations.serviceAgent`)




Granted on the project.


| 
|

| 


#### Artifact Registry Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `artifactregistry.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-artifactregistry.eu0-system.iam.gserviceaccount.com`

| 



[Artifact Registry Service Agent](/iam/docs/roles-permissions/artifactregistry#artifactregistry.serviceAgent)

(`roles/artifactregistry.serviceAgent`)




Granted on the project.


| 
|

| 


#### Assured OSS Service Agent

Service agent for `assuredoss.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-assuredoss.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Assured Workloads Service Agent

Service agent for `assuredworkloads.googleapis.com`. 


`service-folder- FOLDER_NUMBER @gcp-sa-assuredworkloads.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### AssuredWorkloads Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `assuredworkloads.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-assuredworkloads.eu0-system.iam.gserviceaccount.com`

| 



[Assured Workloads Service Agent](/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.serviceAgent)

(`roles/assuredworkloads.serviceAgent`)




Granted on the project.


| 
|

| 


#### Attack Surface Management Service Agent

Service agent for `securitycenter.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-asm-hpsa.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Audit Manager Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `auditmanager.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-audit-manager.eu0-system.iam.gserviceaccount.com`

| 



[Audit Manager Auditing Service Agent](/iam/docs/roles-permissions/auditmanager#auditmanager.serviceAgent)

(`roles/auditmanager.serviceAgent`)




Granted on the project.


| 
|

| 


#### Audit Manager Service Agent

Service agent for `auditmanager.googleapis.com`. 


For the folder:





- `service-folder- FOLDER_NUMBER @gcp-sa-audit-manager.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-audit-manager.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Auto Annotate Service Account

Service agent for `storage.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-autoannotate.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### AutoML Recommendations Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `recommendationengine.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-recommendationengine.eu0-system.iam.gserviceaccount.com`

| 



[Recommendations AI Service Agent](/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.serviceAgent)

(`roles/automlrecommendations.serviceAgent`)




Granted on the project.


| 
|

| 


#### AutoML Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `automl.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-automl.eu0-system.iam.gserviceaccount.com`

| 



[AutoML Service Agent](/iam/docs/roles-permissions/automl#automl.serviceAgent)

(`roles/automl.serviceAgent`)




Granted on the project.


| 
|

| 


#### Backup and DR Runner Service Agent

Service agent for `backupdr.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-backupdr-run.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Backup and DR Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `backupdr.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-backupdr.eu0-system.iam.gserviceaccount.com`

| 



[Backup and DR Service Agent](/iam/docs/roles-permissions/backupdr#backupdr.serviceAgent)

(`roles/backupdr.serviceAgent`)




Granted on the project.


| 
|

| 


#### Backup and DR Vault Service Agent

Service agent for `backupdr.googleapis.com`. 


`vault- PROJECT_NUMBER - IDENTIFIER @gcp-sa-backupdr-pr.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Backup for GKE Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `gkebackup.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkebackup.eu0-system.iam.gserviceaccount.com`

| 



[Backup for GKE Service Agent](/iam/docs/roles-permissions/gkebackup#gkebackup.serviceAgent)

(`roles/gkebackup.serviceAgent`)




Granted on the project.


| 
|

| 


#### Bare Metal Solution Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `baremetalsolution.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bms.eu0-system.iam.gserviceaccount.com`

| 



[Bare Metal Solution Service Agent](/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.serviceAgent)

(`roles/baremetalsolution.serviceAgent`)




Granted on the project.


| 
|

| 


#### Batch Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `batch.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloudbatch.eu0-system.iam.gserviceaccount.com`

| 



[Google Batch Service Agent](/iam/docs/roles-permissions/batch#batch.serviceAgent)

(`roles/batch.serviceAgent`)




Granted on the project.


| 
|

| 


#### Big Query Service Agent

Service agent for `bigquery.googleapis.com`. 


`bq- PROJECT_NUMBER @bigquery-encryption.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### BigLake Iceberg Rest Catalog API Service Agent

Service agent for `biglake.googleapis.com`. 


`blirc- PROJECT_NUMBER - IDENTIFIER @gcp-sa-biglakerestcatalog.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### BigQuery Connected Sheets Service Agent

Service agent for `bigquery.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-connectedsheets.eu0-system.iam.gserviceaccount.com`

| 



[Connected Sheets Service Agent](/iam/docs/roles-permissions/bigquery#bigquery.connectedSheetsServiceAgent)

(`roles/bigquery.connectedSheetsServiceAgent`)




Granted on the project.


| 
|

| 


#### BigQuery Connection Delegation Service Agent

Service agent for `bigqueryconnection.googleapis.com`. 



- `bqcx- PROJECT_NUMBER - IDENTIFIER @gcp-sa-bigquery-condel.eu0-system.iam.gserviceaccount.com`

- `connection- PROJECT_NUMBER - IDENTIFIER @gcp-sa-bigquery-condel.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### BigQuery Connection Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `bigqueryconnection.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bigqueryconnection.eu0-system.iam.gserviceaccount.com`

| 



[BigQuery Connection Service Agent](/iam/docs/roles-permissions/bigqueryconnection#bigqueryconnection.serviceAgent)

(`roles/bigqueryconnection.serviceAgent`)




Granted on the project.


| 
|

| 


#### BigQuery Continuous Query Service Agent

Service agent for `bigquery.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bigquerytardis.eu0-system.iam.gserviceaccount.com`

| 



[BigQuery Continuous Query Service Agent](/iam/docs/roles-permissions/bigquerycontinuousquery#bigquerycontinuousquery.serviceAgent)

(`roles/bigquerycontinuousquery.serviceAgent`)




Granted on the project.


| 
|

| 


#### BigQuery Data Transfer Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `bigquerydatatransfer.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bigquerydatatransfer.eu0-system.iam.gserviceaccount.com`

| 



[BigQuery Data Transfer Service Agent](/iam/docs/roles-permissions/bigquerydatatransfer#bigquerydatatransfer.serviceAgent)

(`roles/bigquerydatatransfer.serviceAgent`)




Granted on the project.


| 
|

| 


#### BigQuery Migration Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `bigquerymigration.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bqms.eu0-system.iam.gserviceaccount.com`

| 



[BigQuery Migration Service Agent](/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.serviceAgent)

(`roles/bigquerymigration.serviceAgent`)




Granted on the project.


| 
|

| 


#### BigQuery Omni Service Agent

Service agent for `bigquery.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-prod-bigqueryomni.eu0-system.iam.gserviceaccount.com`

| 



[BigQuery Omni Service Agent](/iam/docs/roles-permissions/bigqueryomni#bigqueryomni.serviceAgent)

(`roles/bigqueryomni.serviceAgent`)




Granted on the project.


| 
|

| 


#### BigQuery Resource Identity Service Account

Service agent for `bigquery.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bigqueryri.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### BigQuery Spark Connection Delegate Service Agent

Service agent for `bigqueryconnection.googleapis.com`. 


`bqcx- PROJECT_NUMBER - IDENTIFIER @gcp-sa-bigquery-consp.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### BigQuery Spark Service Agent

Service agent for `bigquery.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bigqueryspark.eu0-system.iam.gserviceaccount.com`

| 



[BigQuery Spark Service Agent](/iam/docs/roles-permissions/bigqueryspark#bigqueryspark.serviceAgent)

(`roles/bigqueryspark.serviceAgent`)




Granted on the project.


| 
|

| 


#### Binary Authorization Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `binaryauthorization.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-binaryauthorization.eu0-system.iam.gserviceaccount.com`

| 



[Binary Authorization Service Agent](/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.serviceAgent)

(`roles/binaryauthorization.serviceAgent`)




Granted on the project.


| 
|

| 


#### Blockchain Node Engine Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `blockchainnodeengine.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bne.eu0-system.iam.gserviceaccount.com`

| 



[Blockchain Node Engine Service Agent](/iam/docs/roles-permissions/blockchainnodeengine#blockchainnodeengine.serviceAgent)

(`roles/blockchainnodeengine.serviceAgent`)




Granted on the project.


| 
|

| 


#### Bundles Service Agent

Service agent for `integrations.googleapis.com`. 


`b PROJECT_NUMBER - IDENTIFIER @gcp-sa-bundles.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Business AI Code Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `businessaicode.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-businessaicode.eu0-system.iam.gserviceaccount.com`

| 



[Business AI Code Service Agent](/iam/docs/roles-permissions/businessaicode#businessaicode.serviceAgent)

(`roles/businessaicode.serviceAgent`)




Granted on the project.


| 
|

| 


#### Chronicle Organization Service Account

Service agent for `chronicle.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-chronicle-org.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Chronicle Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `chronicle.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-chronicle.eu0-system.iam.gserviceaccount.com`

| 



[Chronicle Service Agent](/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent)

(`roles/chronicle.serviceAgent`)




Granted on the project.


| 
|

| 


#### Chronicle Soar Service Agent

Service agent for `chronicle.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-chronicle-soar.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud AI Platform Notebooks Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `notebooks.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-notebooks.eu0-system.iam.gserviceaccount.com`

| 



[AI Platform Notebooks Service Agent](/iam/docs/roles-permissions/notebooks#notebooks.serviceAgent)

(`roles/notebooks.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud AI Platform Notebooks VM Service Account

Service agent for `notebooks.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-notebooks-vm.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Notebook Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.notebookServiceAgent)

(`roles/aiplatform.notebookServiceAgent`)




Granted on the project.


| 
|

| 


#### Cloud API Gateway Management Plane Service Account

Service agent for `apigateway.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apigateway-mgmt.eu0-system.iam.gserviceaccount.com`

| 



[Cloud API Gateway Management Service Agent](/iam/docs/roles-permissions/apigateway#apigateway_management.serviceAgent)

(`roles/apigateway_management.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud API Gateway Service Account

Service agent for `apigateway.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-apigateway.eu0-system.iam.gserviceaccount.com`

| 



[Cloud API Gateway Service Agent](/iam/docs/roles-permissions/apigateway#apigateway.serviceAgent)

(`roles/apigateway.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Asset Effective Policy Service Agent

Service agent for `cloudasset.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-effectivepolicy.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Asset Other Cloud Config Service Agent

Service agent for `cloudasset.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-othercloudcfg.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Asset Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudasset.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloudasset.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Asset Service Agent](/iam/docs/roles-permissions/cloudasset#cloudasset.serviceAgent)

(`roles/cloudasset.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Bigtable Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `bigtableadmin.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-bigtable.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Build Service Agent

Service agent for `cloudbuild.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloudbuild.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Build Service Agent](/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent)

(`roles/cloudbuild.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Certificate Manager Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `certificatemanager.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-certificatemanager.eu0-system.iam.gserviceaccount.com`

| 



[Certificate Manager Service Agent](/iam/docs/roles-permissions/certificatemanager#certificatemanager.serviceAgent)

(`roles/certificatemanager.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Composer Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `composer.googleapis.com`. 


`service- PROJECT_NUMBER @cloudcomposer-accounts.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Composer API Service Agent](/iam/docs/roles-permissions/composer#composer.serviceAgent)

(`roles/composer.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Controls Partner Service Agent

Service agent for `cloudcontrolspartner.googleapis.com`. 


`service-folder- FOLDER_NUMBER @gcp-sa-cloudcontrolspartner.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud DNS Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `dns.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-dns.eu0-system.iam.gserviceaccount.com`

| 



[Cloud DNS Service Agent](/iam/docs/roles-permissions/dns#dns.serviceAgent)

(`roles/dns.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Data Fusion Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `datafusion.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-datafusion.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Data Fusion API Service Agent](/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent)

(`roles/datafusion.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Data Loss Prevention Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `dlp.googleapis.com`. 


`service- PROJECT_NUMBER @dlp-api.eu0-system.iam.gserviceaccount.com`

| 



[DLP API Service Agent](/iam/docs/roles-permissions/dlp#dlp.serviceAgent)

(`roles/dlp.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Database Migration Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `datamigration.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-datamigration.eu0-system.iam.gserviceaccount.com`

| 



[Database Migration Service Agent](/iam/docs/roles-permissions/datamigration#datamigration.serviceAgent)

(`roles/datamigration.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Dataflow Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `dataflow.googleapis.com`. 


`service- PROJECT_NUMBER @dataflow-service-producer-prod.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Dataflow Service Agent](/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent)

(`roles/dataflow.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Dataplex Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `dataplex.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-dataplex.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Dataplex Service Agent](/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent)

(`roles/dataplex.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Datastream Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `datastream.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-datastream.eu0-system.iam.gserviceaccount.com`

| 



[Datastream Service Agent](/iam/docs/roles-permissions/datastream#datastream.serviceAgent)

(`roles/datastream.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Deploy Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `clouddeploy.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-clouddeploy.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Deploy Service Agent](/iam/docs/roles-permissions/clouddeploy#clouddeploy.serviceAgent)

(`roles/clouddeploy.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Endpoints Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `endpoints.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-endpoints.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Endpoints Service Agent](/iam/docs/roles-permissions/endpoints#endpoints.serviceAgent)

(`roles/endpoints.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud File Storage Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `file.googleapis.com`. 


`service- PROJECT_NUMBER @cloud-filer.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Filestore Service Agent](/iam/docs/roles-permissions/file#file.serviceAgent)

(`roles/file.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Firestore Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `firestore.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firestore.eu0-system.iam.gserviceaccount.com`

| 



[Firestore Service Agent](/iam/docs/roles-permissions/firestore#firestore.serviceAgent)

(`roles/firestore.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Healthcare Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `healthcare.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-healthcare.eu0-system.iam.gserviceaccount.com`

| 



[Healthcare Service Agent](/iam/docs/roles-permissions/healthcare#healthcare.serviceAgent)

(`roles/healthcare.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Identity Platform Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `identitytoolkit.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-identitytoolkit.eu0-system.iam.gserviceaccount.com`

| 



[Identity Platform Service Agent](/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.serviceAgent)

(`roles/identitytoolkit.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud KMS Organization Service Agent

Service agent for `cloudkms.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-cloudkms.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud KMS Service Agent

Service agent for `cloudkms.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloudkms.eu0-system.iam.gserviceaccount.com`

| 



[Cloud KMS Service Agent](/iam/docs/roles-permissions/cloudkms#cloudkms.serviceAgent)

(`roles/cloudkms.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Logging Service Account

Service agent for `logging.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-logging.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Logging Service Agent](/iam/docs/roles-permissions/logging#logging.serviceAgent)

(`roles/logging.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Logging Service Agent

Service agent for `logging.googleapis.com`. 


For the folder:





- `service-folder- FOLDER_NUMBER @gcp-sa-logging.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-logging.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Cloud Managed Identities Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `managedidentities.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-mi.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Managed Identities Service Agent](/iam/docs/roles-permissions/managedidentities#managedidentities.serviceAgent)

(`roles/managedidentities.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Memorystore Memcache Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `memcache.googleapis.com`. 


`service- PROJECT_NUMBER @cloud-memcache-sa.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Memorystore Memcached Service Agent](/iam/docs/roles-permissions/memcache#memcache.serviceAgent)

(`roles/memcache.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Memorystore Redis Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `redis.googleapis.com`. 


`service- PROJECT_NUMBER @cloud-redis.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Memorystore Redis Service Agent](/iam/docs/roles-permissions/redis#redis.serviceAgent)

(`roles/redis.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Migration Center Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `migrationcenter.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-migcenter.eu0-system.iam.gserviceaccount.com`

| 



[Migration Center Service Agent](/iam/docs/roles-permissions/migrationcenter#migrationcenter.serviceAgent)

(`roles/migrationcenter.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Network Management Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `networkmanagement.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-networkmanagement.eu0-system.iam.gserviceaccount.com`

| 



[GCP Network Management Service Agent](/iam/docs/roles-permissions/networkmanagement#networkmanagement.serviceAgent)

(`roles/networkmanagement.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Notebook Security Scanner Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `notebooksecurityscanner.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-notebooksecurityscanner.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Notebook Security Scanner Service Agent

Service agent for `notebooksecurityscanner.googleapis.com`. 


For the project:





- `service- PROJECT_NUMBER @gcp-sa-nss-hpsa.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-nss-hpsa.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Cloud Observability Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `observability.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-observability.eu0-system.iam.gserviceaccount.com`

| 



[Observability Service Agent](/iam/docs/roles-permissions/observability#observability.serviceAgent)

(`roles/observability.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Observability Service Account

Service agent for `observability.googleapis.com`. 


For the folder:





- `service-folder- FOLDER_NUMBER @gcp-sa-observability.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-observability.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Cloud Optimization Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudoptimization.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloudoptim.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Optimization Service Agent](/iam/docs/roles-permissions/cloudoptimization#cloudoptimization.serviceAgent)

(`roles/cloudoptimization.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Optimization Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `routeoptimization.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-routeoptim.eu0-system.iam.gserviceaccount.com`

| 



[Route Optimization Service Agent](/iam/docs/roles-permissions/routeoptimization#routeoptimization.serviceAgent)

(`roles/routeoptimization.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Pub/Sub Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `pubsub.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-pubsub.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Pub/Sub Service Agent](/iam/docs/roles-permissions/pubsub#pubsub.serviceAgent)

(`roles/pubsub.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Resource Manager Service Agent

Service agent for `cloudresourcemanager.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-cloudresourcemanager.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Risk Manager Service Agent

Service agent for `dlp.googleapis.com`. 


`organizations- ORGANIZATION_NUMBER @gcp-sa-riskmanager.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud SQL Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `sqladmin.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloud-sql.eu0-system.iam.gserviceaccount.com`

| 



[Cloud SQL Service Agent](/iam/docs/roles-permissions/cloudsql#cloudsql.serviceAgent)

(`roles/cloudsql.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud SQL Service Agent

Service agent for `sqladmin.googleapis.com`. 


For the project:





- `p PROJECT_NUMBER - IDENTIFIER @gcp-sa-cloud-sql.eu0-system.iam.gserviceaccount.com`




For the folder:





- `f FOLDER_NUMBER - IDENTIFIER @gcp-sa-cloud-sql.eu0-system.iam.gserviceaccount.com`




For the organization:





- `o ORGANIZATION_NUMBER - IDENTIFIER @gcp-sa-cloud-sql.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Cloud Scheduler Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudscheduler.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloudscheduler.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Scheduler Service Agent](/iam/docs/roles-permissions/cloudscheduler#cloudscheduler.serviceAgent)

(`roles/cloudscheduler.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Security Command Center Bulk Export Service Account

Service agent for `securitycenter.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-scc-bulk-export.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Security Command Center Notification Service Account

Service agent for `securitycenter.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-scc-notification.eu0-system.iam.gserviceaccount.com`

| 



[Security Center Notification Service Agent](/iam/docs/roles-permissions/securitycenter#securitycenter.notificationServiceAgent)

(`roles/securitycenter.notificationServiceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Security Command Center Notification Service Account

Service agent for `securitycenter.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-scc-notification.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Security Command Center Service Account

Service agent for `securitycenter.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-securitycenter.eu0-system.iam.gserviceaccount.com`

| 



[Security Center Service Agent](/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent)

(`roles/securitycenter.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Security Command Center Service Agent

Service agent for `securitycenter.googleapis.com`. 


For the project:





- `service- PROJECT_NUMBER @security-center-api.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @security-center-api.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Cloud Security Compliance Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudsecuritycompliance.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-csc-hpsa.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Security Compliance Service Agent](/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent)

(`roles/cloudsecuritycompliance.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Security Compliance Service Agent

Service agent for `cloudsecuritycompliance.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-csc-hpsa.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Spanner Production Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `spanner.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-spanner.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Spanner API Service Agent](/iam/docs/roles-permissions/spanner#spanner.serviceAgent)

(`roles/spanner.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Storage for Firebase Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `firebasestorage.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebasestorage.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Storage for Firebase Service Agent](/iam/docs/roles-permissions/firebasestorage#firebasestorage.serviceAgent)

(`roles/firebasestorage.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Tasks Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudtasks.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloudtasks.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Tasks Service Agent](/iam/docs/roles-permissions/cloudtasks#cloudtasks.serviceAgent)

(`roles/cloudtasks.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Trace Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudtrace.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloud-trace.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Cloud Translation Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `translate.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-translation.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Translation API Service Agent](/iam/docs/roles-permissions/cloudtranslate#cloudtranslate.serviceAgent)

(`roles/cloudtranslate.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud VM Migration Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `vmmigration.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vmmigration.eu0-system.iam.gserviceaccount.com`

| 



[VM Migration Service Agent](/iam/docs/roles-permissions/vmmigration#vmmigration.serviceAgent)

(`roles/vmmigration.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Web Security Scanner Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `websecurityscanner.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-websecurityscanner.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Web Security Scanner Service Agent](/iam/docs/roles-permissions/cloudsecurityscanner#websecurityscanner.serviceAgent)

(`roles/websecurityscanner.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Workflows Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `workflows.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-workflows.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Workflows Service Agent](/iam/docs/roles-permissions/workflows#workflows.serviceAgent)

(`roles/workflows.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cloud Workstations Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `workstations.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-workstations.eu0-system.iam.gserviceaccount.com`

| 



[Workstations Service Agent](/iam/docs/roles-permissions/workstations#workstations.serviceAgent)

(`roles/workstations.serviceAgent`)




Granted on the project.


| 
|

| 


#### Cluster Director Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `hypercomputecluster.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-hypercomputecluster.eu0-system.iam.gserviceaccount.com`

| 



[Cluster Director Service Agent](/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent)

(`roles/hypercomputecluster.serviceAgent`)




Granted on the project.


| 
|

| 


#### Compute Engine Service Agent

Service agent for `compute.googleapis.com`. 


`service- PROJECT_NUMBER @compute-system.eu0-system.iam.gserviceaccount.com`

| 



[Compute Engine Service Agent](/iam/docs/roles-permissions/compute#compute.serviceAgent)

(`roles/compute.serviceAgent`)




Granted on the project.


| 
|

| 


#### Compute Usage Export Service Agent

Service agent for `compute.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-compute-usage.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Config Delivery Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `configdelivery.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-configdelivery.eu0-system.iam.gserviceaccount.com`

| 



[Config Delivery Service Agent](/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent)

(`roles/configdelivery.serviceAgent`)




Granted on the project.


| 
|

| 


#### Connectors Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `connectors.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-connectors.eu0-system.iam.gserviceaccount.com`

| 



[Connectors Platform Service Agent](/iam/docs/roles-permissions/connectors#connectors.serviceAgent)

(`roles/connectors.serviceAgent`)




Granted on the project.


| 
|

| 


#### Contact Center AI Insights Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `contactcenterinsights.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-contactcenterinsights.eu0-system.iam.gserviceaccount.com`

| 



[Contact Center AI Insights Service Agent](/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent)

(`roles/contactcenterinsights.serviceAgent`)




Granted on the project.


| 
|

| 


#### Contact Center AI Insights Service Account for CMEK (prod)

Service agent for `contactcenterinsights.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ccinsights-cmek.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Contact Center AI Platform Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `contactcenteraiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ccaip.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Contact Center AI shared Service Account for CMEK (prod)

Service agent for `contactcenterinsights.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ccai-cmek.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Contact Center Insights Resource Identity (prod)

Service agent for `contactcenterinsights.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-ri-contactcenterinsights.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Container Analysis Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `containeranalysis.googleapis.com`. 


`service- PROJECT_NUMBER @container-analysis.eu0-system.iam.gserviceaccount.com`

| 



[Container Analysis Service Agent](/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent)

(`roles/containeranalysis.ServiceAgent`)




Granted on the project.


| 
|

| 


#### Container Scanning Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `containerscanning.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-containerscanning.eu0-system.iam.gserviceaccount.com`

| 



[Container Scanner Service Agent](/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent)

(`roles/containerscanning.ServiceAgent`)




Granted on the project.


| 
|

| 


#### Container Security Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `containersecurity.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-containersec.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Container Threat Detection Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `containerthreatdetection.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ktd-control.eu0-system.iam.gserviceaccount.com`

| 



[Container Threat Detection Service Agent](/iam/docs/roles-permissions/containerthreatdetection#containerthreatdetection.serviceAgent)

(`roles/containerthreatdetection.serviceAgent`)




Granted on the project.


| 
|

| 


#### Container Threat Detection Service Agent

Service agent for `containerthreatdetection.googleapis.com`. 


For the project:





- `service- PROJECT_NUMBER @gcp-sa-ktd-hpsa.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-ktd-hpsa.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Content Warehouse Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `contentwarehouse.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloud-cw.eu0-system.iam.gserviceaccount.com`

| 



[Content Warehouse Service Agent](/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent)

(`roles/contentwarehouse.serviceAgent`)




Granted on the project.


| 
|

| 


#### Customer Engagement Suite Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `ces.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ces.eu0-system.iam.gserviceaccount.com`

| 



[Customer Engagement Suite Service Agent](/iam/docs/roles-permissions/ces#ces.serviceAgent)

(`roles/ces.serviceAgent`)




Granted on the project.


| 
|

| 


#### Data Connectors Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `dataconnectors.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-dataconnectors.eu0-system.iam.gserviceaccount.com`

| 



[Data Connectors Service Agent](/iam/docs/roles-permissions/dataconnectors#dataconnectors.serviceAgent)

(`roles/dataconnectors.serviceAgent`)




Granted on the project.


| 
|

| 


#### Data Labeling Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `datalabeling.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-datalabeling.eu0-system.iam.gserviceaccount.com`

| 



[Data Labeling Service Agent](/iam/docs/roles-permissions/datalabeling#datalabeling.serviceAgent)

(`roles/datalabeling.serviceAgent`)




Granted on the project.


| 
|

| 


#### Data Lineage Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `datalineage.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-datalineage.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Data Pipelines Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `datapipelines.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-datapipelines.eu0-system.iam.gserviceaccount.com`

| 



[Datapipelines Service Agent](/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent)

(`roles/datapipelines.serviceAgent`)




Granted on the project.


| 
|

| 


#### Data Studio CMEK Service Account

Service agent for `datastudio.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-datastudio-cmek.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Data Studio Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `datastudio.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-datastudio.eu0-system.iam.gserviceaccount.com`

| 



[Data Studio Service Agent](/iam/docs/roles-permissions/datastudio#datastudio.serviceAgent)

(`roles/datastudio.serviceAgent`)




Granted on the project.


| 
|

| 


#### Dataform Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `dataform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-dataform.eu0-system.iam.gserviceaccount.com`

| 



[Dataform Service Agent](/iam/docs/roles-permissions/dataform#dataform.serviceAgent)

(`roles/dataform.serviceAgent`)




Granted on the project.


| 
|

| 


#### Dataplex Cmek Service Agent

Service agent for `dataplex.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-dataplex-cmek.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Dataplex Service Agent

Service agent for `dataplex.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-dataplex.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Dataproc Metastore Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `metastore.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-metastore.eu0-system.iam.gserviceaccount.com`

| 



[Dataproc Metastore Service Agent](/iam/docs/roles-permissions/metastore#metastore.serviceAgent)

(`roles/metastore.serviceAgent`)




Granted on the project.


| 
|

| 


#### Deprecated Monitoring Service Account

Service agent for `monitoring.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-monitoring.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Design Center Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `designcenter.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-designcenter.eu0-system.iam.gserviceaccount.com`

| 



[DesignCenter Service Agent](/iam/docs/roles-permissions/designcenter#designcenter.serviceAgent)

(`roles/designcenter.serviceAgent`)




Granted on the project.


| 
|

| 


#### Developer Connect Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `developerconnect.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-devconnect.eu0-system.iam.gserviceaccount.com`

| 



[Developer Connect Service Agent](/iam/docs/roles-permissions/developerconnect#developerconnect.serviceAgent)

(`roles/developerconnect.serviceAgent`)




Granted on the project.


| 
|

| 


#### Dialogflow Service Account for CMEK (prod)

Service agent for `dialogflow.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-dialogflow-cmek.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Dialogflow Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `dialogflow.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-dialogflow.eu0-system.iam.gserviceaccount.com`

| 



[Dialogflow Service Agent](/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent)

(`roles/dialogflow.serviceAgent`)




Granted on the project.


| 
|

| 


#### Discovery Engine Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `discoveryengine.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-discoveryengine.eu0-system.iam.gserviceaccount.com`

| 



[Discovery Engine Service Agent](/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent)

(`roles/discoveryengine.serviceAgent`)




Granted on the project.


| 
|

| 


#### Document AI Warehouse CMEK Infra Spanner Service Account

Service agent for `contentwarehouse.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloud-cw-cmek.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### DocumentAI Core Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `documentai.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-prod-dai-core.eu0-system.iam.gserviceaccount.com`

| 



[DocumentAI Core Service Agent](/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent)

(`roles/documentaicore.serviceAgent`)




Granted on the project.


| 
|

| 


#### Edge Container Cluster Service Agent

Service agent for `edgecontainer.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-edgecontainercluster.eu0-system.iam.gserviceaccount.com`

| 



[Edge Container Cluster Service Agent](/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent)

(`roles/edgecontainer.clusterServiceAgent`)




Granted on the project.


| 
|

| 


#### Edge Container GCR Service Agent

Service agent for `edgecontainer.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-edgecontainergcr.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Edge Container Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `edgecontainer.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-edgecontainer.eu0-system.iam.gserviceaccount.com`

| 



[Edge Container Service Agent](/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent)

(`roles/edgecontainer.serviceAgent`)




Granted on the project.


| 
|

| 


#### Enterprise Knowledge Graph Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `enterpriseknowledgegraph.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloud-ekg.eu0-system.iam.gserviceaccount.com`

| 



[Enterprise Knowledge Graph Service Agent](/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.serviceAgent)

(`roles/enterpriseknowledgegraph.serviceAgent`)




Granted on the project.


| 
|

| 


#### Eventarc Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `eventarc.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-eventarc.eu0-system.iam.gserviceaccount.com`

| 



[Eventarc Service Agent](/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent)

(`roles/eventarc.serviceAgent`)




Granted on the project.


| 
|

| 


#### External Key Management Service Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudkms.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ekms.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Firebase AI Logic Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `firebasevertexai.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebasevertexai.eu0-system.iam.gserviceaccount.com`

| 



[Firebase AI Logic Service Agent](/iam/docs/roles-permissions/firebaseml#firebaseml.serviceAgent)

(`roles/firebaseml.serviceAgent`)




Granted on the project.


| 
|

| 


#### Firebase App Check Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `firebaseappcheck.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebaseappcheck.eu0-system.iam.gserviceaccount.com`

| 



[Firebase App Check Service Agent](/iam/docs/roles-permissions/firebaseappcheck#firebaseappcheck.serviceAgent)

(`roles/firebaseappcheck.serviceAgent`)




Granted on the project.


| 
|

| 


#### Firebase App Hosting Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `firebaseapphosting.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebaseapphosting.eu0-system.iam.gserviceaccount.com`

| 



[Firebase App Hosting Service Agent](/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.serviceAgent)

(`roles/firebaseapphosting.serviceAgent`)




Granted on the project.


| 
|

| 


#### Firebase Crashlytics Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `firebasecrashlytics.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-crashlytics.eu0-system.iam.gserviceaccount.com`

| 



[Firebase Crashlytics Service Agent](/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.serviceAgent)

(`roles/firebasecrashlytics.serviceAgent`)




Granted on the project.


| 
|

| 


#### Firebase Data Connect Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `firebasedataconnect.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebasedataconnect.eu0-system.iam.gserviceaccount.com`

| 



[Firebase Data Connect Service Agent](/iam/docs/roles-permissions/firebasedataconnect#firebasedataconnect.serviceAgent)

(`roles/firebasedataconnect.serviceAgent`)




Granted on the project.


| 
|

| 


#### Firebase Extensions Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `firebaseextensions.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebasemods.eu0-system.iam.gserviceaccount.com`

| 



[Firebase Extensions API Service Agent](/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent)

(`roles/firebasemods.serviceAgent`)




Granted on the project.


| 
|

| 


#### Firebase Machine Learning Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `firebaseml.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebaseml.eu0-system.iam.gserviceaccount.com`

| 



[Firebase AI Logic Service Agent](/iam/docs/roles-permissions/firebaseml#firebaseml.serviceAgent)

(`roles/firebaseml.serviceAgent`)




Granted on the project.


| 
|

| 


#### Firebase Management Service Agent

Service agent for `firebase.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebase.eu0-system.iam.gserviceaccount.com`

| 



[Firebase Service Management Service Agent](/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent)

(`roles/firebase.managementServiceAgent`)




Granted on the project.


| 
|

| 


#### Firebase Realtime Database Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `firebasedatabase.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firebasedatabase.eu0-system.iam.gserviceaccount.com`

| 



[Firebase Realtime Database Service Agent](/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.serviceAgent)

(`roles/firebasedatabase.serviceAgent`)




Granted on the project.


| 
|

| 


#### Firebase Rules Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `firebaserules.googleapis.com`. 


`service- PROJECT_NUMBER @firebase-rules.eu0-system.iam.gserviceaccount.com`

| 



[Firebase Rules System](/iam/docs/roles-permissions/firebaserules#firebaserules.system)

(`roles/firebaserules.system`)




Granted on the project.


| 
|

| 


#### Firewall Insights Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `firewallinsights.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-firewallinsights.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Firewall Insights Service Agent](/iam/docs/roles-permissions/firewallinsights#firewallinsights.serviceAgent)

(`roles/firewallinsights.serviceAgent`)




Granted on the project.


| 
|

| 


#### G Suite Add-ons Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `gsuiteaddons.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gsuiteaddons.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### GCS Search Service Account

Service agent for `storage.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-storage-search.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### GKE Dataplane V2 Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `gkedataplanev2.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkedataplanev2.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### GKE Hub API Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `gkehub.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkehub.eu0-system.iam.gserviceaccount.com`

| 



[GKE Hub Service Agent](/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent)

(`roles/gkehub.serviceAgent`)




Granted on the project.


| 
|

| 


#### Gemini Code Assist Management Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `geminicodeassistmanagement.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-geminicodeassistmp.eu0-system.iam.gserviceaccount.com`

| 



[Gemini Code Assist Management Service Agent](/iam/docs/roles-permissions/geminicodeassistmanagement#geminicodeassistmanagement.serviceAgent)

(`roles/geminicodeassistmanagement.serviceAgent`)




Granted on the project.


| 
|

| 


#### Gemini Data Analytics Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `geminidataanalytics.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-geminidataanalytics.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Gemini for Google Cloud Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudaicompanion.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-cloudaicompanion.eu0-system.iam.gserviceaccount.com`

| 



[Gemini for Google Cloud Service Agent](/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.serviceAgent)

(`roles/cloudaicompanion.serviceAgent`)




Granted on the project.


| 
|

| 


#### Generative Language Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `generativelanguage.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-generativelanguage.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Generative Language Service Agent

Service agent for `generativelanguage.googleapis.com`. 


`p- PROJECT_NUMBER - IDENTIFIER @gcp-sa-generativelanguage.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Gke On-Prem Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `gkeonprem.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkeonprem.eu0-system.iam.gserviceaccount.com`

| 



[GKE On-Prem Service Agent](/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent)

(`roles/gkeonprem.serviceAgent`)




Granted on the project.


| 
|

| 


#### Google APIs Service Agent

Service agent used internally by Google Cloud Dedicated. 


` PROJECT_NUMBER @cloudservices.eu0-system.iam.gserviceaccount.com`

| 



[Editor](/iam/docs/roles-overview#basic)

(`roles/editor`)




Granted on the project.


| 
|

| 


#### Google Cloud Dataproc Resource Manager Node Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `dataprocrm.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-dataprocrmnode.eu0-system.iam.gserviceaccount.com`

| 



[Dataproc Resource Manager Node Service Agent](/iam/docs/roles-permissions/dataprocrm#dataprocrm.nodeServiceAgent)

(`roles/dataprocrm.nodeServiceAgent`)




Granted on the project.


| 
|

| 


#### Google Cloud Dataproc Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `dataproc.googleapis.com`. 


`service- PROJECT_NUMBER @dataproc-accounts.eu0-system.iam.gserviceaccount.com`

| 



[Dataproc Service Agent](/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent)

(`roles/dataproc.serviceAgent`)




Granted on the project.


| 
|

| 


#### Google Cloud Functions Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `cloudfunctions.googleapis.com`. 


`service- PROJECT_NUMBER @gcf-admin-robot.eu0-system.iam.gserviceaccount.com`

| 



[(Deprecated) Cloud Functions Service Agent](/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent)

(`roles/cloudfunctions.serviceAgent`)




Granted on the project.


| 
|

| 


#### Google Cloud ML Engine Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `ml.googleapis.com`. 


`service- PROJECT_NUMBER @cloud-ml.eu0-system.iam.gserviceaccount.com`

| 



[AI Platform Service Agent](/iam/docs/roles-permissions/ml#ml.serviceAgent)

(`roles/ml.serviceAgent`)




Granted on the project.


| 
|

| 


#### Google Cloud NetApp Volumes Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `netapp.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-netapp.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Google Cloud Network Security Authz Service Account

Service agent for `networksecurity.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ns-authz.eu0-system.iam.gserviceaccount.com`

| 



[Network Security Authz Service Agent](/iam/docs/roles-permissions/networksecurity#networksecurity.authzServiceAgent)

(`roles/networksecurity.authzServiceAgent`)




Granted on the project.


| 
|

| 


#### Google Cloud OS Config Rollout Service Agent

Service agent for `osconfig.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-osconfig-rollout.eu0-system.iam.gserviceaccount.com`

| 



[Cloud OS Config Rollout Service Agent](/iam/docs/roles-permissions/osconfig#osconfig.rolloutServiceAgent)

(`roles/osconfig.rolloutServiceAgent`)




Granted on the project.


| 
|

| 


#### Google Cloud OS Config Rollout Service Agent

Service agent for `osconfig.googleapis.com`. 


For the folder:





- `service-folder- FOLDER_NUMBER @gcp-sa-osconfig-rollout.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-osconfig-rollout.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Google Cloud OS Config Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `osconfig.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-osconfig.eu0-system.iam.gserviceaccount.com`

| 



[Cloud OS Config Service Agent](/iam/docs/roles-permissions/osconfig#osconfig.serviceAgent)

(`roles/osconfig.serviceAgent`)




Granted on the project.


| 
|

| 


#### Google Cloud OS Config Service Agent

Service agent for `osconfig.googleapis.com`. 


For the folder:





- `service-folder- FOLDER_NUMBER @gcp-sa-osconfig.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-osconfig.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Google Cloud Run AI Bundle Service Agent

Service agent for `run.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-run-ai.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Google Cloud Run Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `run.googleapis.com`. 


`service- PROJECT_NUMBER @serverless-robot-prod.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Run Service Agent](/iam/docs/roles-permissions/run#run.serviceAgent)

(`roles/run.serviceAgent`)




Granted on the project.


| 
|

| 


#### Google Cloud Service Extensions Service Account

Service agent for `networkservices.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-dep.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Google Container Registry Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `containerregistry.googleapis.com`. 


`service- PROJECT_NUMBER @containerregistry.eu0-system.iam.gserviceaccount.com`

| 



[Container Registry Service Agent](/iam/docs/roles-permissions/containerregistry#containerregistry.ServiceAgent)

(`roles/containerregistry.ServiceAgent`)




Granted on the project.


| 
|

| 


#### Google Storage Service Agent

Service agent for `storage.googleapis.com`. 


`service- PROJECT_NUMBER @gs-project-accounts.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### IAP Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `iap.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-iap.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Identity Pool Resource Identity

Service agent for `iam.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-ri-identitypool.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Infra Spanner Production Service Account

Service agent for `spanner.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-global-spanner.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Infrastructure Manager Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `config.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-config.eu0-system.iam.gserviceaccount.com`

| 



[Infrastructure Manager Service Agent](/iam/docs/roles-permissions/cloudconfig#cloudconfig.serviceAgent)

(`roles/cloudconfig.serviceAgent`)




Granted on the project.


| 
|

| 


#### Integrated Vulnerability Scanner Service Account

Service agent for `securitycenter.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ivs.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Internal Cloud Firestore Spanner Service Agent

Service agent for `firestore.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-fs-spanner.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### KRM API Hosting Service Account

Service agent for `krmapihosting.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-krmapihosting.eu0-system.iam.gserviceaccount.com`

| 



[KRM API Hosting Service Agent](/iam/docs/roles-permissions/krmapihosting#krmapihosting.serviceAgent)

(`roles/krmapihosting.serviceAgent`)




Granted on the project.


| 
|

| 


#### KRM API Hosting Service Account

Service agent for `krmapihosting.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-krmapihosting-dataplane.eu0-system.iam.gserviceaccount.com`

| 



[KRM API Hosting AnthosApiEndpoint Service Agent](/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent)

(`roles/krmapihosting.anthosApiEndpointServiceAgent`)




Granted on the project.


| 
|

| 


#### Kubernetes Engine Node Service Agent

Service agent for `container.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-gkenode.eu0-system.iam.gserviceaccount.com`

| 



[Kubernetes Engine Default Node Service Agent](/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent)

(`roles/container.defaultNodeServiceAgent`)




Granted on the project.


| 
|

| 


#### Kubernetes Engine Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `container.googleapis.com`. 


`service- PROJECT_NUMBER @container-engine-robot.eu0-system.iam.gserviceaccount.com`

| 



[Kubernetes Engine Service Agent](/iam/docs/roles-permissions/container#container.serviceAgent)

(`roles/container.serviceAgent`)




Granted on the project.


| 
|

| 


#### Legacy Cloud Build service account

Service agent for `cloudbuild.googleapis.com`. 


` PROJECT_NUMBER @cloudbuild.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Build Service Account](/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder)

(`roles/cloudbuild.builds.builder`)




Granted on the project.


| 
|

| 


#### Livestream Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `livestream.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-livestream.eu0-system.iam.gserviceaccount.com`

| 



[Live Stream Service Agent](/iam/docs/roles-permissions/livestream#livestream.serviceAgent)

(`roles/livestream.serviceAgent`)




Granted on the project.


| 
|

| 


#### Logging Service Agent

Service agent for `logging.googleapis.com`. 


For the project:





- `p PROJECT_NUMBER - IDENTIFIER @gcp-sa-logging.eu0-system.iam.gserviceaccount.com`




For the folder:





- `f FOLDER_NUMBER - IDENTIFIER @gcp-sa-logging.eu0-system.iam.gserviceaccount.com`




For the organization:





- `o ORGANIZATION_NUMBER - IDENTIFIER @gcp-sa-logging.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Looker Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `looker.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-looker.eu0-system.iam.gserviceaccount.com`

| 



[Looker Service Agent](/iam/docs/roles-permissions/looker#looker.restrictedServiceAgent)

(`roles/looker.restrictedServiceAgent`)




Granted on the project.


| 
|

| 


#### Lustre Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `lustre.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-lustre.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Managed Flink Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `managedflink.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-managedflink.eu0-system.iam.gserviceaccount.com`

| 



[Managed Flink Service Agent](/iam/docs/roles-permissions/managedflink#managedflink.serviceAgent)

(`roles/managedflink.serviceAgent`)




Granted on the project.


| 
|

| 


#### Managed Kafka Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `managedkafka.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-managedkafka.eu0-system.iam.gserviceaccount.com`

| 



[Managed Kafka Service Agent](/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent)

(`roles/managedkafka.serviceAgent`)




Granted on the project.


| 
|

| 


#### Memorystore Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `memorystore.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-memorystore.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Memorystore Service Agent](/iam/docs/roles-permissions/memorystore#memorystore.serviceAgent)

(`roles/memorystore.serviceAgent`)




Granted on the project.


| 
|

| 


#### Mesh Config Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `meshconfig.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-meshconfig.eu0-system.iam.gserviceaccount.com`

| 



[Mesh Config Service Agent](/iam/docs/roles-permissions/anthosservicemesh#meshconfig.serviceAgent)

(`roles/meshconfig.serviceAgent`)




Granted on the project.


| 
|

| 


#### Model Armor Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `modelarmor.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-modelarmor.eu0-system.iam.gserviceaccount.com`

| 



[Model Armor Service Agent](/iam/docs/roles-permissions/modelarmor#modelarmor.serviceAgent)

(`roles/modelarmor.serviceAgent`)




Granted on the project.


| 
|

| 


#### Monitoring Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `monitoring.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-monitoring-notification.eu0-system.iam.gserviceaccount.com`

| 



[Monitoring Service Agent](/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent)

(`roles/monitoring.notificationServiceAgent`)




Granted on the project.


| 
|

| 


#### Multi Cluster Ingress Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `multiclusteringress.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-multiclusteringress.eu0-system.iam.gserviceaccount.com`

| 



[Multi Cluster Ingress Service Agent](/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent)

(`roles/multiclusteringress.serviceAgent`)




Granted on the project.


| 
|

| 


#### Multi cluster metering Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `multiclustermetering.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-mcmetering.eu0-system.iam.gserviceaccount.com`

| 



[Multi-cluster metering Service Agent](/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent)

(`roles/multiclustermetering.serviceAgent`)




Granted on the project.


| 
|

| 


#### Multi-cluster Service Discovery Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `multiclusterservicediscovery.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-mcsd.eu0-system.iam.gserviceaccount.com`

| 



[Multi-Cluster Service Discovery Service Agent](/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent)

(`roles/multiclusterservicediscovery.serviceAgent`)




Granted on the project.


| 
|

| 


#### Network Actions Service Account

Service agent for `networkservices.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-networkactions.eu0-system.iam.gserviceaccount.com`

| 



[Network Actions Service Agent](/iam/docs/roles-permissions/networkactions#networkactions.serviceAgent)

(`roles/networkactions.serviceAgent`)




Granted on the project.


| 
|

| 


#### Network Connectivity Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `networkconnectivity.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-networkconnectivity.eu0-system.iam.gserviceaccount.com`

| 



[Network Connectivity Service Agent](/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent)

(`roles/networkconnectivity.serviceAgent`)




Granted on the project.


| 
|

| 


#### Network Security Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `networksecurity.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-networksecurity.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### On-Demand Scanning Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `ondemandscanning.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-ondemandscanning.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Oracle Database@Google Cloud Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `oracledatabase.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-oci.eu0-system.iam.gserviceaccount.com`

| 



[Oracle Database@Google Cloud Service Agent](/iam/docs/roles-permissions/oci#oci.serviceAgent)

(`roles/oci.serviceAgent`)




Granted on the project.


| 
|

| 


#### Parallelstore Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `parallelstore.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-parallelstore.eu0-system.iam.gserviceaccount.com`

| 



[Parallelstore Service Agent](/iam/docs/roles-permissions/parallelstore#parallelstore.serviceAgent)

(`roles/parallelstore.serviceAgent`)




Granted on the project.


| 
|

| 


#### Parameter Manager Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `parametermanager.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-pm.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Playbook Runner Service Agent

Service agent for `integrations.googleapis.com`. 


For the project:





- `p PROJECT_NUMBER - IDENTIFIER @gcp-sa-playbooks.eu0-system.iam.gserviceaccount.com`




For the folder:





- `f FOLDER_NUMBER - IDENTIFIER @gcp-sa-playbooks.eu0-system.iam.gserviceaccount.com`




For the organization:





- `o ORGANIZATION_NUMBER - IDENTIFIER @gcp-sa-playbooks.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Policy Remediator Service Agent (prod)

Service agent for `policyremediator.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-v1-remediator.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Private CA Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `privateca.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-privateca.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Privileged Access Manager Service Agent

Service agent for `privilegedaccessmanager.googleapis.com`. 


For the project:





- `service- PROJECT_NUMBER @gcp-sa-pam.eu0-system.iam.gserviceaccount.com`




For the folder:





- `service-folder- FOLDER_NUMBER @gcp-sa-pam.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-pam.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Progressive Rollout Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `progressiverollout.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-progrollout.eu0-system.iam.gserviceaccount.com`

| 



[Progressive Rollout Service Agent](/iam/docs/roles-permissions/progressiverollout#progressiverollout.serviceAgent)

(`roles/progressiverollout.serviceAgent`)




Granted on the project.


| 
|

| 


#### Progressive Rollout Service Agent

Service agent for `progressiverollout.googleapis.com`. 


For the folder:





- `service-folder- FOLDER_NUMBER @gcp-sa-progrollout.eu0-system.iam.gserviceaccount.com`




For the organization:





- `service-org- ORGANIZATION_NUMBER @gcp-sa-progrollout.eu0-system.iam.gserviceaccount.com`


| 

None
| 
|

| 


#### Pub/Sub Lite Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `pubsublite.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-pubsublite.eu0-system.iam.gserviceaccount.com`

| 



[Pub/Sub Lite Service Agent](/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent)

(`roles/pubsublite.serviceAgent`)




Granted on the project.


| 
|

| 


#### Rapid Migration Assessment Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `rapidmigrationassessment.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-rma.eu0-system.iam.gserviceaccount.com`

| 



[RMA Service Agent](/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent)

(`roles/rapidmigrationassessment.serviceAgent`)




Granted on the project.


| 
|

| 


#### Remote Build Execution Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `remotebuildexecution.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-rbe.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Remote Build Execution Service Agent

Service agent for `remotebuildexecution.googleapis.com`. 


`service- PROJECT_NUMBER @remotebuildexecution.eu0-system.iam.gserviceaccount.com`

| 



[Remote Build Execution Service Agent](/iam/docs/roles-permissions/remotebuildexecution#remotebuildexecution.serviceAgent)

(`roles/remotebuildexecution.serviceAgent`)




Granted on the project.


| 
|

| 


#### Remote Build Execution Service Agent

Service agent for `remotebuildexecution.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-remotebuild.eu0-system.iam.gserviceaccount.com`

| 



[Remote Build Execution Service Agent](/iam/docs/roles-permissions/remotebuildexecution#remotebuildexecution.serviceAgent)

(`roles/remotebuildexecution.serviceAgent`)




Granted on the project.


| 
|

| 


#### Retail Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `retail.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-retail.eu0-system.iam.gserviceaccount.com`

| 



[Retail Service Agent](/iam/docs/roles-permissions/retail#retail.serviceAgent)

(`roles/retail.serviceAgent`)




Granted on the project.


| 
|

| 


#### SCC CMEK Spanner Service Agent (PROD)

Service agent for `securitycenter.googleapis.com`. 


`service-org- ORGANIZATION_NUMBER @gcp-sa-sccspanner.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### SaaS Service Management Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `saasservicemgmt.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-saasservicemgmt.eu0-system.iam.gserviceaccount.com`

| 



[SaaS Service Management Service Agent](/iam/docs/roles-permissions/saasservicemgmt#saasservicemgmt.serviceAgent)

(`roles/saasservicemgmt.serviceAgent`)




Granted on the project.


| 
|

| 


#### Secret Manager Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `secretmanager.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-secretmanager.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Secure Source Manager Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `securesourcemanager.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-sourcemanager.eu0-system.iam.gserviceaccount.com`

| 



[Secure Source Manager Service Agent](/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.serviceAgent)

(`roles/securesourcemanager.serviceAgent`)




Granted on the project.


| 
|

| 


#### Secure Web Proxy Service Account

Service agent for `networkservices.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-securewebproxy.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Serverless Integrations Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `runapps.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-runapps.eu0-system.iam.gserviceaccount.com`

| 



[Serverless Integrations Service Agent](/iam/docs/roles-permissions/runapps#runapps.serviceAgent)

(`roles/runapps.serviceAgent`)




Granted on the project.


| 
|

| 


#### Serverless VPC Access Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `vpcaccess.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vpcaccess.eu0-system.iam.gserviceaccount.com`

| 



[Serverless VPC Access Service Agent](/iam/docs/roles-permissions/vpcaccess#vpcaccess.serviceAgent)

(`roles/vpcaccess.serviceAgent`)




Granted on the project.


| 
|

| 


#### Service Agent Manager

Service agent used internally by Google Cloud Dedicated. 


`service-agent-manager@eu0-system.system.gserviceaccount.com`

| 

None
| 
|

| 


#### Service Consumer Management Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `serviceconsumermanagement.googleapis.com`. 


`service- PROJECT_NUMBER @service-consumer-management.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Service Directory Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `servicedirectory.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-servicedirectory.eu0-system.iam.gserviceaccount.com`

| 



[Service Directory Service Agent](/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent)

(`roles/servicedirectory.serviceAgent`)




Granted on the project.


| 
|

| 


#### Service Networking Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `servicenetworking.googleapis.com`. 


`service- PROJECT_NUMBER @service-networking.eu0-system.iam.gserviceaccount.com`

| 



[Service Networking Service Agent](/iam/docs/roles-permissions/servicenetworking#servicenetworking.serviceAgent)

(`roles/servicenetworking.serviceAgent`)




Granted on the project.


| 
|

| 


#### Skill Registry Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-skills.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Spectrum SAS Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `sasportal.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-spectrumsas.eu0-system.iam.gserviceaccount.com`

| 



[Spectrum SAS Service Agent](/iam/docs/roles-permissions/spectrumsas#spectrumsas.serviceAgent)

(`roles/spectrumsas.serviceAgent`)




Granted on the project.


| 
|

| 


#### Speech-to-Text Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `speech.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-speech.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Speech-to-Text Service Agent](/iam/docs/roles-permissions/speech#speech.serviceAgent)

(`roles/speech.serviceAgent`)




Granted on the project.


| 
|

| 


#### Storage Insights Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `storageinsights.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-storageinsights.eu0-system.iam.gserviceaccount.com`

| 



[StorageInsights Service Agent](/iam/docs/roles-permissions/storageinsights#storageinsights.serviceAgent)

(`roles/storageinsights.serviceAgent`)




Granted on the project.


| 
|

| 


#### Storage Transfer Service Service Agent

Service agent for `storagetransfer.googleapis.com`. 


`project- PROJECT_NUMBER @storage-transfer-service.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Stream Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `stream.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-stream.eu0-system.iam.gserviceaccount.com`

| 



[Stream Service Agent](/iam/docs/roles-permissions/stream#stream.serviceAgent)

(`roles/stream.serviceAgent`)




Granted on the project.


| 
|

| 


#### TPU Service Agent

[Primary service agent](/iam/docs/service-account-types#primary) for `tpu.googleapis.com`. 


`service- PROJECT_NUMBER @cloud-tpu.eu0-system.iam.gserviceaccount.com`

| 



[Cloud TPU API Service Agent](/iam/docs/roles-permissions/tpu#tpu.serviceAgent)

(`roles/tpu.serviceAgent`)




Granted on the project.


| 
|

| 


#### TPU Service Agent (v2)

Service agent for `tpu.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-tpu.eu0-system.iam.gserviceaccount.com`

| 



[Cloud TPU V2 API Service Agent](/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent)

(`roles/cloudtpu.serviceAgent`)




Granted on the project.


| 
|

| 


#### Transcoder Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `transcoder.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-transcoder.eu0-system.iam.gserviceaccount.com`

| 



[Transcoder Service Agent](/iam/docs/roles-permissions/transcoder#transcoder.serviceAgent)

(`roles/transcoder.serviceAgent`)




Granted on the project.


| 
|

| 


#### Transfer Appliance Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `transferappliance.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-transferappliance.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### VMwareEngine Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `vmwareengine.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vmwareengine.eu0-system.iam.gserviceaccount.com`

| 



[VMware Engine Service Agent](/iam/docs/roles-permissions/vmwareengine#vmwareengine.serviceAgent)

(`roles/vmwareengine.serviceAgent`)




Granted on the project.


| 
|

| 


#### Vector Search Cmek Service Account

Service agent for `vectorsearch.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vs-cmek.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Vector Search Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `vectorsearch.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vectorsearch.eu0-system.iam.gserviceaccount.com`

| 



[Vector Search Service Agent](/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent)

(`roles/vectorsearch.serviceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Agent Sandbox Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-sandbox.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Agent Sandbox Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.agentSandboxServiceAgent)

(`roles/aiplatform.agentSandboxServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Ancillary Secure Fine Tuning Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-shtune.eu0-system.iam.gserviceaccount.com`

| 



[Agent Platform User](/iam/docs/roles-permissions/aiplatform#aiplatform.user)

(`roles/aiplatform.user`)




Granted on the project.


| 
|

| 


#### Vertex AI Batch Prediction Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-bp.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Batch Prediction Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.batchPredictionServiceAgent)

(`roles/aiplatform.batchPredictionServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Colab Service Account

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-nb.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Colab Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.colabServiceAgent)

(`roles/aiplatform.colabServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Extension Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-ex.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Extension Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.extensionServiceAgent)

(`roles/aiplatform.extensionServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Extension Service Agent for Custom Code

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-ex-cc.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Extension Custom Code Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.extensionCustomCodeServiceAgent)

(`roles/aiplatform.extensionCustomCodeServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Logging Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-logging.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Vertex AI Managed OSS Fine Tuning Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-moss-ft.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Tuning Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent)

(`roles/aiplatform.tuningServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Model Monitoring Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-mm.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Model Monitoring Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.modelMonitoringServiceAgent)

(`roles/aiplatform.modelMonitoringServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Notebook Service Account

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-aiplatform-vm.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Notebook Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.notebookServiceAgent)

(`roles/aiplatform.notebookServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Online Prediction Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-op.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Online Prediction Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent)

(`roles/aiplatform.onlinePredictionServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Secure Fine Tuning Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-tune.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Tuning Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.tuningServiceAgent)

(`roles/aiplatform.tuningServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Telemetry Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-telemetry.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI Telemetry Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.telemetryServiceAgent)

(`roles/aiplatform.telemetryServiceAgent`)




Granted on the project.


| 
|

| 


#### Vertex AI Training Cluster Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-vtc.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Vertex Agent Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-agent.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Vertex RAG Data Service Agent

Service agent for `aiplatform.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-vertex-rag.eu0-system.iam.gserviceaccount.com`

| 



[Vertex AI RAG Data Service Agent](/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent)

(`roles/aiplatform.ragServiceAgent`)




Granted on the project.


| 
|

| 


#### Virtual Machine Threat Detection Service Account

Service agent for `securitycenter.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-scc-vmtd.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|

| 


#### Vision AI Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `visionai.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-visionai.eu0-system.iam.gserviceaccount.com`

| 



[Cloud Vision AI Service Agent](/iam/docs/roles-permissions/visionai#visionai.serviceAgent)

(`roles/visionai.serviceAgent`)




Granted on the project.


| 
|

| 


#### Workload Manager Service Account

[Primary service agent](/iam/docs/service-account-types#primary) for `workloadmanager.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-workloadmanager.eu0-system.iam.gserviceaccount.com`

| 



[Workload Manager Service Agent](/iam/docs/roles-permissions/workloadmanager#workloadmanager.serviceAgent)

(`roles/workloadmanager.serviceAgent`)




Granted on the project.


| 
|

| 


#### Workstations VM Default Service Account

Service agent for `workstations.googleapis.com`. 


`service- PROJECT_NUMBER @gcp-sa-workstationsvm.eu0-system.iam.gserviceaccount.com`

| 

None
| 
|