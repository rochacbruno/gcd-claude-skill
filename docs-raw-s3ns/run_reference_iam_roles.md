# Cloud Run IAM roles

Source: https://documentation.s3ns.fr/run/docs/reference/iam/roles
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/run/docs/tpc-differences) for more details.














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

Application hosting

](https://documentation.s3ns.fr/docs/application-hosting)






- 








[

Cloud Run

](https://documentation.s3ns.fr/run/docs)






- 








[

Reference

](https://documentation.s3ns.fr/run/docs/apis)












# Cloud Run IAM roles 















This page lists the [Identity and Access Management (IAM)](/iam) predefined roles for
accessing Cloud Run resources.

## Predefined roles

The following table describes IAM roles that are associated with
Cloud Run, and lists the permissions that are contained in each role.

Roles can be granted to users on an entire project or on individual
Cloud Run resources. Read
[Managing access using IAM](/run/docs/securing/managing-access)
to learn more.

Roles only apply to Cloud Run resources, they don't apply to
Cloud Run domain mappings. The `Project > Editor` role
is needed to create or update domain mappings.






| 
Role | 
Permissions | 
|



| 

#### Cloud Run Admin

(`roles/ run.admin`)



Full control over all Cloud Run resources.



Lowest-level resources where you can grant this role:

- 
Cloud Run service

- 
Cloud Run job

- 
Cloud Run instance

- 
Cloud Run worker pool

| 




`recommender.locations.*` 





- `recommender.locations.get`

- `recommender.locations.list`






`recommender. runServiceCostInsights.*` 





- `recommender. runServiceCostInsights. get`

- `recommender. runServiceCostInsights. list`

- `recommender. runServiceCostInsights. update`






`recommender. runServiceCostRecommendations.*` 





- `recommender. runServiceCostRecommendations. get`

- `recommender. runServiceCostRecommendations. list`

- `recommender. runServiceCostRecommendations. update`






`recommender. runServiceIdentityInsights.*` 





- `recommender. runServiceIdentityInsights. get`

- `recommender. runServiceIdentityInsights. list`

- `recommender. runServiceIdentityInsights. update`






`recommender. runServiceIdentityRecommendations.*` 





- `recommender. runServiceIdentityRecommendations. get`

- `recommender. runServiceIdentityRecommendations. list`

- `recommender. runServiceIdentityRecommendations. update`






`recommender. runServicePerformanceInsights.*` 





- `recommender. runServicePerformanceInsights. get`

- `recommender. runServicePerformanceInsights. list`

- `recommender. runServicePerformanceInsights. update`






`recommender. runServicePerformanceRecommendations.*` 





- `recommender. runServicePerformanceRecommendations. get`

- `recommender. runServicePerformanceRecommendations. list`

- `recommender. runServicePerformanceRecommendations. update`






`recommender. runServiceSecurityInsights.*` 





- `recommender. runServiceSecurityInsights. get`

- `recommender. runServiceSecurityInsights. list`

- `recommender. runServiceSecurityInsights. update`






`recommender. runServiceSecurityRecommendations.*` 





- `recommender. runServiceSecurityRecommendations. get`

- `recommender. runServiceSecurityRecommendations. list`

- `recommender. runServiceSecurityRecommendations. update`





`resourcemanager.projects.get`



`resourcemanager.projects.list`




`run.*` 





- `run.configurations.get`

- `run.configurations.list`

- `run.executions.cancel`

- `run.executions.delete`

- `run.executions.get`

- `run.executions.list`

- `run.instances.create`

- `run.instances.delete`

- `run.instances.get`

- `run.instances.getIamPolicy`

- `run.instances.invoke`

- `run.instances.list`

- `run.instances.setIamPolicy`

- `run.instances.sshRead`

- `run.instances.sshRoot`

- `run.instances.start`

- `run.instances.stop`

- `run.instances.update`

- `run.jobs.create`

- `run.jobs.createTagBinding`

- `run.jobs.delete`

- `run.jobs.deleteTagBinding`

- `run.jobs.get`

- `run.jobs.getIamPolicy`

- `run.jobs.list`

- `run.jobs.listEffectiveTags`

- `run.jobs.listTagBindings`

- `run.jobs.run`

- `run.jobs.runWithOverrides`

- `run.jobs.setIamPolicy`

- `run.jobs.sshRead`

- `run.jobs.sshRoot`

- `run.jobs.update`

- `run.locations.list`

- `run.locations.uploadSource`

- `run.operations.delete`

- `run.operations.get`

- `run.operations.list`

- `run.prompts.get`

- `run.revisions.delete`

- `run.revisions.get`

- `run.revisions.list`

- `run.routes.get`

- `run.routes.invoke`

- `run.routes.list`

- `run.services.create`

- `run.services.createTagBinding`

- `run.services.delete`

- `run.services.deleteTagBinding`

- `run.services.get`

- `run.services.getIamPolicy`

- `run.services.list`

- `run.services.listEffectiveTags`

- `run.services.listTagBindings`

- `run.services.setIamPolicy`

- `run.services.sshRead`

- `run.services.sshRoot`

- `run.services.update`

- `run.tasks.get`

- `run.tasks.list`

- `run.workerpools.create`

- `run.workerpools.delete`

- `run.workerpools.get`

- `run.workerpools.getIamPolicy`

- `run.workerpools.list`

- `run.workerpools.setIamPolicy`

- `run.workerpools.sshRead`

- `run.workerpools.sshRoot`

- `run.workerpools.update`



| 
|

| 

#### Cloud Run Builder

(`roles/ run.builder`)



Can build Cloud Run functions and source deployed services.


| 



`artifactregistry. repositories. deleteArtifacts`



`artifactregistry. repositories. downloadArtifacts`



`artifactregistry. repositories. uploadArtifacts`



`logging.logEntries.create`



`source.repos.get`



`storage.objects.get`

| 
|

| 

#### Cloud Run Developer

(`roles/ run.developer`)



Read and write access to all Cloud Run resources.



Lowest-level resources where you can grant this role:

- 
Cloud Run service

- 
Cloud Run job

- 
Cloud Run instance

- 
Cloud Run worker pool

| 




`recommender.locations.*` 





- `recommender.locations.get`

- `recommender.locations.list`






`recommender. runServiceCostInsights.*` 





- `recommender. runServiceCostInsights. get`

- `recommender. runServiceCostInsights. list`

- `recommender. runServiceCostInsights. update`






`recommender. runServiceCostRecommendations.*` 





- `recommender. runServiceCostRecommendations. get`

- `recommender. runServiceCostRecommendations. list`

- `recommender. runServiceCostRecommendations. update`






`recommender. runServiceIdentityInsights.*` 





- `recommender. runServiceIdentityInsights. get`

- `recommender. runServiceIdentityInsights. list`

- `recommender. runServiceIdentityInsights. update`






`recommender. runServiceIdentityRecommendations.*` 





- `recommender. runServiceIdentityRecommendations. get`

- `recommender. runServiceIdentityRecommendations. list`

- `recommender. runServiceIdentityRecommendations. update`






`recommender. runServicePerformanceInsights.*` 





- `recommender. runServicePerformanceInsights. get`

- `recommender. runServicePerformanceInsights. list`

- `recommender. runServicePerformanceInsights. update`






`recommender. runServicePerformanceRecommendations.*` 





- `recommender. runServicePerformanceRecommendations. get`

- `recommender. runServicePerformanceRecommendations. list`

- `recommender. runServicePerformanceRecommendations. update`






`recommender. runServiceSecurityInsights.*` 





- `recommender. runServiceSecurityInsights. get`

- `recommender. runServiceSecurityInsights. list`

- `recommender. runServiceSecurityInsights. update`






`recommender. runServiceSecurityRecommendations.*` 





- `recommender. runServiceSecurityRecommendations. get`

- `recommender. runServiceSecurityRecommendations. list`

- `recommender. runServiceSecurityRecommendations. update`





`resourcemanager.projects.get`



`resourcemanager.projects.list`




`run.configurations.*` 





- `run.configurations.get`

- `run.configurations.list`






`run.executions.*` 





- `run.executions.cancel`

- `run.executions.delete`

- `run.executions.get`

- `run.executions.list`





`run.instances.create`



`run.instances.delete`



`run.instances.get`



`run.instances.getIamPolicy`



`run.instances.invoke`



`run.instances.list`



`run.instances.sshRead`



`run.instances.sshRoot`



`run.instances.start`



`run.instances.stop`



`run.instances.update`



`run.jobs.create`



`run.jobs.delete`



`run.jobs.get`



`run.jobs.getIamPolicy`



`run.jobs.list`



`run.jobs.listEffectiveTags`



`run.jobs.listTagBindings`



`run.jobs.run`



`run.jobs.runWithOverrides`



`run.jobs.sshRead`



`run.jobs.sshRoot`



`run.jobs.update`




`run.locations.*` 





- `run.locations.list`

- `run.locations.uploadSource`






`run.operations.*` 





- `run.operations.delete`

- `run.operations.get`

- `run.operations.list`





`run.prompts.get`




`run.revisions.*` 





- `run.revisions.delete`

- `run.revisions.get`

- `run.revisions.list`






`run.routes.*` 





- `run.routes.get`

- `run.routes.invoke`

- `run.routes.list`





`run.services.create`



`run.services.delete`



`run.services.get`



`run.services.getIamPolicy`



`run.services.list`



`run.services.listEffectiveTags`



`run.services.listTagBindings`



`run.services.sshRead`



`run.services.sshRoot`



`run.services.update`




`run.tasks.*` 





- `run.tasks.get`

- `run.tasks.list`





`run.workerpools.create`



`run.workerpools.delete`



`run.workerpools.get`



`run.workerpools.getIamPolicy`



`run.workerpools.list`



`run.workerpools.sshRead`



`run.workerpools.sshRoot`



`run.workerpools.update`

| 
|

| 

#### Cloud Run Editor

(`roles/ run.editor`)



Editor role for Cloud Run


| 




`recommender.locations.*` 





- `recommender.locations.get`

- `recommender.locations.list`






`recommender. runServiceCostInsights.*` 





- `recommender. runServiceCostInsights. get`

- `recommender. runServiceCostInsights. list`

- `recommender. runServiceCostInsights. update`






`recommender. runServiceCostRecommendations.*` 





- `recommender. runServiceCostRecommendations. get`

- `recommender. runServiceCostRecommendations. list`

- `recommender. runServiceCostRecommendations. update`






`recommender. runServiceIdentityInsights.*` 





- `recommender. runServiceIdentityInsights. get`

- `recommender. runServiceIdentityInsights. list`

- `recommender. runServiceIdentityInsights. update`






`recommender. runServiceIdentityRecommendations.*` 





- `recommender. runServiceIdentityRecommendations. get`

- `recommender. runServiceIdentityRecommendations. list`

- `recommender. runServiceIdentityRecommendations. update`






`recommender. runServicePerformanceInsights.*` 





- `recommender. runServicePerformanceInsights. get`

- `recommender. runServicePerformanceInsights. list`

- `recommender. runServicePerformanceInsights. update`






`recommender. runServicePerformanceRecommendations.*` 





- `recommender. runServicePerformanceRecommendations. get`

- `recommender. runServicePerformanceRecommendations. list`

- `recommender. runServicePerformanceRecommendations. update`






`recommender. runServiceSecurityInsights.*` 





- `recommender. runServiceSecurityInsights. get`

- `recommender. runServiceSecurityInsights. list`

- `recommender. runServiceSecurityInsights. update`






`recommender. runServiceSecurityRecommendations.*` 





- `recommender. runServiceSecurityRecommendations. get`

- `recommender. runServiceSecurityRecommendations. list`

- `recommender. runServiceSecurityRecommendations. update`





`resourcemanager.projects.get`



`resourcemanager.projects.list`




`run.configurations.*` 





- `run.configurations.get`

- `run.configurations.list`






`run.executions.*` 





- `run.executions.cancel`

- `run.executions.delete`

- `run.executions.get`

- `run.executions.list`





`run.instances.create`



`run.instances.delete`



`run.instances.get`



`run.instances.getIamPolicy`



`run.instances.invoke`



`run.instances.list`



`run.instances.sshRead`



`run.instances.sshRoot`



`run.instances.start`



`run.instances.stop`



`run.instances.update`



`run.jobs.create`



`run.jobs.delete`



`run.jobs.get`



`run.jobs.getIamPolicy`



`run.jobs.list`



`run.jobs.listEffectiveTags`



`run.jobs.listTagBindings`



`run.jobs.run`



`run.jobs.runWithOverrides`



`run.jobs.sshRead`



`run.jobs.sshRoot`



`run.jobs.update`




`run.locations.*` 





- `run.locations.list`

- `run.locations.uploadSource`






`run.operations.*` 





- `run.operations.delete`

- `run.operations.get`

- `run.operations.list`





`run.prompts.get`




`run.revisions.*` 





- `run.revisions.delete`

- `run.revisions.get`

- `run.revisions.list`






`run.routes.*` 





- `run.routes.get`

- `run.routes.invoke`

- `run.routes.list`





`run.services.create`



`run.services.delete`



`run.services.get`



`run.services.getIamPolicy`



`run.services.list`



`run.services.listEffectiveTags`



`run.services.listTagBindings`



`run.services.sshRead`



`run.services.sshRoot`



`run.services.update`




`run.tasks.*` 





- `run.tasks.get`

- `run.tasks.list`





`run.workerpools.create`



`run.workerpools.delete`



`run.workerpools.get`



`run.workerpools.getIamPolicy`



`run.workerpools.list`



`run.workerpools.sshRead`



`run.workerpools.sshRoot`



`run.workerpools.update`

| 
|

| 

#### Cloud Run Invoker

(`roles/ run.invoker`)



Can invoke Cloud Run services, instances and execute Cloud Run jobs.



Lowest-level resources where you can grant this role:

- 
Cloud Run service

- 
Cloud Run job

- 
Cloud Run instance

| 



`run.instances.invoke`



`run.jobs.run`



`run.routes.invoke`

| 
|

| 

#### Cloud Run Viewer

(`roles/ run.viewer`)



Can view the state of all Cloud Run resources, including IAM policies.



Lowest-level resources where you can grant this role:

- 
Cloud Run service

- 
Cloud Run job

- 
Cloud Run instance

- 
Cloud Run worker pool

| 




`recommender.locations.*` 





- `recommender.locations.get`

- `recommender.locations.list`





`recommender. runServiceCostInsights. get`



`recommender. runServiceCostInsights. list`



`recommender. runServiceCostRecommendations. get`



`recommender. runServiceCostRecommendations. list`



`recommender. runServiceIdentityInsights. get`



`recommender. runServiceIdentityInsights. list`



`recommender. runServiceIdentityRecommendations. get`



`recommender. runServiceIdentityRecommendations. list`



`recommender. runServicePerformanceInsights. get`



`recommender. runServicePerformanceInsights. list`



`recommender. runServicePerformanceRecommendations. get`



`recommender. runServicePerformanceRecommendations. list`



`recommender. runServiceSecurityInsights. get`



`recommender. runServiceSecurityInsights. list`



`recommender. runServiceSecurityRecommendations. get`



`recommender. runServiceSecurityRecommendations. list`



`resourcemanager.projects.get`



`resourcemanager.projects.list`




`run.configurations.*` 





- `run.configurations.get`

- `run.configurations.list`





`run.executions.get`



`run.executions.list`



`run.instances.get`



`run.instances.getIamPolicy`



`run.instances.list`



`run.jobs.get`



`run.jobs.getIamPolicy`



`run.jobs.list`



`run.jobs.listEffectiveTags`



`run.jobs.listTagBindings`



`run.locations.list`



`run.operations.get`



`run.operations.list`



`run.prompts.get`



`run.revisions.get`



`run.revisions.list`



`run.routes.get`



`run.routes.list`



`run.services.get`



`run.services.getIamPolicy`



`run.services.list`



`run.services.listEffectiveTags`



`run.services.listTagBindings`




`run.tasks.*` 





- `run.tasks.get`

- `run.tasks.list`





`run.workerpools.get`



`run.workerpools.getIamPolicy`



`run.workerpools.list`

| 
|

| 

#### Cloud Run Jobs Executor

(`roles/ run.jobsExecutor`)



Can execute and cancel Cloud Run jobs.


| 



`run.executions.cancel`



`run.jobs.run`

| 
|

| 

#### Cloud Run Jobs Executor With Overrides

(`roles/ run.jobsExecutorWithOverrides`)



Can execute and cancel Cloud Run jobs with overrides.


| 



`run.executions.cancel`



`run.jobs.run`



`run.jobs.runWithOverrides`

| 
|

| 

#### Cloud Run Service Invoker

(`roles/ run.servicesInvoker`)



Can invoke Cloud Run services.


| 



`run.routes.invoke`

| 
|

| 

#### Cloud Run Source Developer

(`roles/ run.sourceDeveloper`)



Deploy and manage Cloud Run source deployed resources.


| 



`artifactregistry. attachments. get`



`artifactregistry. attachments. list`




`artifactregistry. dockerimages.*` 





- `artifactregistry. dockerimages. get`

- `artifactregistry. dockerimages. list`





`artifactregistry. files. download`



`artifactregistry.files.get`



`artifactregistry.files.list`




`artifactregistry.locations.*` 





- `artifactregistry.locations.get`

- `artifactregistry. locations. list`






`artifactregistry. mavenartifacts.*` 





- `artifactregistry. mavenartifacts. get`

- `artifactregistry. mavenartifacts. list`






`artifactregistry.npmpackages.*` 





- `artifactregistry. npmpackages. get`

- `artifactregistry. npmpackages. list`





`artifactregistry.packages.get`



`artifactregistry.packages.list`



`artifactregistry. projectconfigs. get`



`artifactregistry. projectsettings. get`




`artifactregistry. pythonpackages.*` 





- `artifactregistry. pythonpackages. get`

- `artifactregistry. pythonpackages. list`





`artifactregistry. repositories. create`



`artifactregistry. repositories. downloadArtifacts`



`artifactregistry. repositories. exportArtifacts`



`artifactregistry. repositories. get`



`artifactregistry. repositories. list`



`artifactregistry. repositories. listEffectiveTags`



`artifactregistry. repositories. listTagBindings`



`artifactregistry. repositories. readViaVirtualRepository`



`artifactregistry.rules.get`



`artifactregistry.rules.list`



`artifactregistry.tags.get`



`artifactregistry.tags.list`



`artifactregistry.versions.get`



`artifactregistry.versions.list`



`cloudbuild.builds.create`



`cloudbuild.builds.get`



`cloudbuild.builds.list`



`cloudbuild.builds.update`




`cloudbuild.locations.*` 





- `cloudbuild.locations.get`

- `cloudbuild.locations.list`






`cloudbuild.operations.*` 





- `cloudbuild.operations.get`

- `cloudbuild.operations.list`






`cloudkms.keyHandles.*` 





- `cloudkms.keyHandles.create`

- `cloudkms.keyHandles.get`

- `cloudkms.keyHandles.list`





`cloudkms.operations.get`



`cloudkms. projects. showEffectiveAutokeyConfig`



`eventarc. channelConnections. create`



`eventarc. channelConnections. createTagBinding`



`eventarc. channelConnections. delete`



`eventarc. channelConnections. deleteTagBinding`



`eventarc. channelConnections. get`



`eventarc. channelConnections. getIamPolicy`



`eventarc. channelConnections. list`



`eventarc. channelConnections. listEffectiveTags`



`eventarc. channelConnections. listTagBindings`



`eventarc. channelConnections. publish`



`eventarc.channels.attach`



`eventarc.channels.create`



`eventarc. channels. createTagBinding`



`eventarc.channels.delete`



`eventarc. channels. deleteTagBinding`



`eventarc.channels.get`



`eventarc.channels.getIamPolicy`



`eventarc.channels.list`



`eventarc. channels. listEffectiveTags`



`eventarc. channels. listTagBindings`



`eventarc.channels.publish`



`eventarc.channels.undelete`



`eventarc.channels.update`



`eventarc.enrollments.create`



`eventarc.enrollments.delete`



`eventarc.enrollments.get`



`eventarc. enrollments. getIamPolicy`



`eventarc.enrollments.list`



`eventarc.enrollments.update`



`eventarc. googleApiSources. create`



`eventarc. googleApiSources. delete`



`eventarc.googleApiSources.get`



`eventarc. googleApiSources. getIamPolicy`



`eventarc.googleApiSources.list`



`eventarc. googleApiSources. update`




`eventarc. googleChannelConfigs.*` 





- `eventarc. googleChannelConfigs. get`

- `eventarc. googleChannelConfigs. update`





`eventarc.kafkaSources.create`



`eventarc.kafkaSources.delete`



`eventarc.kafkaSources.get`



`eventarc. kafkaSources. getIamPolicy`



`eventarc.kafkaSources.list`




`eventarc.locations.*` 





- `eventarc.locations.get`

- `eventarc.locations.list`






`eventarc.operations.*` 





- `eventarc.operations.cancel`

- `eventarc.operations.delete`

- `eventarc.operations.get`

- `eventarc.operations.list`





`eventarc.pipelines.create`



`eventarc.pipelines.delete`



`eventarc.pipelines.get`



`eventarc. pipelines. getIamPolicy`



`eventarc.pipelines.list`



`eventarc.pipelines.update`




`eventarc.providers.*` 





- `eventarc.providers.get`

- `eventarc.providers.list`





`eventarc.triggers.create`



`eventarc. triggers. createTagBinding`



`eventarc.triggers.delete`



`eventarc. triggers. deleteTagBinding`



`eventarc.triggers.get`



`eventarc.triggers.getIamPolicy`



`eventarc.triggers.list`



`eventarc. triggers. listEffectiveTags`



`eventarc. triggers. listTagBindings`



`eventarc.triggers.undelete`



`eventarc.triggers.update`



`orgpolicy.policy.get`



`pubsub. messageTransforms. validate`



`pubsub.schemas.attach`



`pubsub.schemas.commit`



`pubsub.schemas.create`



`pubsub.schemas.delete`



`pubsub.schemas.get`



`pubsub.schemas.getIamPolicy`



`pubsub.schemas.list`



`pubsub.schemas.listRevisions`



`pubsub.schemas.rollback`



`pubsub.schemas.validate`



`pubsub.snapshots.create`



`pubsub. snapshots. createTagBinding`



`pubsub.snapshots.delete`



`pubsub. snapshots. deleteTagBinding`



`pubsub.snapshots.get`



`pubsub.snapshots.list`



`pubsub. snapshots. listEffectiveTags`



`pubsub. snapshots. listTagBindings`



`pubsub.snapshots.seek`



`pubsub.snapshots.update`



`pubsub.subscriptions.consume`



`pubsub.subscriptions.create`



`pubsub. subscriptions. createTagBinding`



`pubsub.subscriptions.delete`



`pubsub. subscriptions. deleteTagBinding`



`pubsub.subscriptions.get`



`pubsub.subscriptions.list`



`pubsub. subscriptions. listEffectiveTags`



`pubsub. subscriptions. listTagBindings`



`pubsub.subscriptions.update`



`pubsub. topics. attachSubscription`



`pubsub.topics.create`



`pubsub.topics.createTagBinding`



`pubsub.topics.delete`



`pubsub.topics.deleteTagBinding`



`pubsub. topics. detachSubscription`



`pubsub.topics.get`



`pubsub.topics.list`



`pubsub. topics. listEffectiveTags`



`pubsub.topics.listTagBindings`



`pubsub.topics.publish`



`pubsub.topics.update`



`pubsub.topics.updateTag`




`recommender.locations.*` 





- `recommender.locations.get`

- `recommender.locations.list`






`recommender. runServiceCostInsights.*` 





- `recommender. runServiceCostInsights. get`

- `recommender. runServiceCostInsights. list`

- `recommender. runServiceCostInsights. update`






`recommender. runServiceCostRecommendations.*` 





- `recommender. runServiceCostRecommendations. get`

- `recommender. runServiceCostRecommendations. list`

- `recommender. runServiceCostRecommendations. update`






`recommender. runServiceIdentityInsights.*` 





- `recommender. runServiceIdentityInsights. get`

- `recommender. runServiceIdentityInsights. list`

- `recommender. runServiceIdentityInsights. update`






`recommender. runServiceIdentityRecommendations.*` 





- `recommender. runServiceIdentityRecommendations. get`

- `recommender. runServiceIdentityRecommendations. list`

- `recommender. runServiceIdentityRecommendations. update`






`recommender. runServicePerformanceInsights.*` 





- `recommender. runServicePerformanceInsights. get`

- `recommender. runServicePerformanceInsights. list`

- `recommender. runServicePerformanceInsights. update`






`recommender. runServicePerformanceRecommendations.*` 





- `recommender. runServicePerformanceRecommendations. get`

- `recommender. runServicePerformanceRecommendations. list`

- `recommender. runServicePerformanceRecommendations. update`






`recommender. runServiceSecurityInsights.*` 





- `recommender. runServiceSecurityInsights. get`

- `recommender. runServiceSecurityInsights. list`

- `recommender. runServiceSecurityInsights. update`






`recommender. runServiceSecurityRecommendations.*` 





- `recommender. runServiceSecurityRecommendations. get`

- `recommender. runServiceSecurityRecommendations. list`

- `recommender. runServiceSecurityRecommendations. update`





`remotebuildexecution.blobs.get`



`resourcemanager.projects.get`



`resourcemanager.projects.list`




`run.configurations.*` 





- `run.configurations.get`

- `run.configurations.list`






`run.executions.*` 





- `run.executions.cancel`

- `run.executions.delete`

- `run.executions.get`

- `run.executions.list`





`run.instances.create`



`run.instances.delete`



`run.instances.get`



`run.instances.getIamPolicy`



`run.instances.invoke`



`run.instances.list`



`run.instances.sshRead`



`run.instances.sshRoot`



`run.instances.start`



`run.instances.stop`



`run.instances.update`



`run.jobs.create`



`run.jobs.delete`



`run.jobs.get`



`run.jobs.getIamPolicy`



`run.jobs.list`



`run.jobs.listEffectiveTags`



`run.jobs.listTagBindings`



`run.jobs.run`



`run.jobs.runWithOverrides`



`run.jobs.sshRead`



`run.jobs.sshRoot`



`run.jobs.update`




`run.locations.*` 





- `run.locations.list`

- `run.locations.uploadSource`






`run.operations.*` 





- `run.operations.delete`

- `run.operations.get`

- `run.operations.list`





`run.prompts.get`




`run.revisions.*` 





- `run.revisions.delete`

- `run.revisions.get`

- `run.revisions.list`






`run.routes.*` 





- `run.routes.get`

- `run.routes.invoke`

- `run.routes.list`





`run.services.create`



`run.services.delete`



`run.services.get`



`run.services.getIamPolicy`



`run.services.list`



`run.services.listEffectiveTags`



`run.services.listTagBindings`



`run.services.sshRead`



`run.services.sshRoot`



`run.services.update`




`run.tasks.*` 





- `run.tasks.get`

- `run.tasks.list`





`run.workerpools.create`



`run.workerpools.delete`



`run.workerpools.get`



`run.workerpools.getIamPolicy`



`run.workerpools.list`



`run.workerpools.sshRead`



`run.workerpools.sshRoot`



`run.workerpools.update`



`serviceusage. catalogs. listMembers`



`serviceusage. consumerpolicy. analyze`



`serviceusage. consumerpolicy. get`



`serviceusage. effectivepolicy. get`




`serviceusage.groups.*` 





- `serviceusage.groups.list`

- `serviceusage. groups. listExpandedMembers`

- `serviceusage. groups. listMembers`





`serviceusage.quotas.get`



`serviceusage.services.get`



`serviceusage.services.list`



`serviceusage.services.listApis`



`serviceusage. services. listDependentServices`



`serviceusage.services.use`



`serviceusage.values.test`



`storage.buckets.create`



`storage.buckets.get`



`storage.buckets.list`



`storage.folders.create`



`storage.folders.get`



`storage.folders.list`



`storage.managedFolders.create`



`storage.managedFolders.get`



`storage.managedFolders.list`



`storage.multipartUploads.abort`



`storage. multipartUploads. create`



`storage. multipartUploads. listParts`



`storage.objects.create`



`storage.objects.createContext`



`storage.objects.get`



`storage.objects.list`

| 
|

| 

#### Cloud Run Source Viewer

(`roles/ run.sourceViewer`)



View Cloud Run source deployed resources.


| 



`artifactregistry. repositories. get`



`artifactregistry. repositories. list`



`cloudbuild.builds.get`



`cloudbuild.builds.list`




`cloudbuild.locations.*` 





- `cloudbuild.locations.get`

- `cloudbuild.locations.list`






`cloudbuild.operations.*` 





- `cloudbuild.operations.get`

- `cloudbuild.operations.list`





`eventarc. channelConnections. get`



`eventarc. channelConnections. getIamPolicy`



`eventarc. channelConnections. list`



`eventarc. channelConnections. listEffectiveTags`



`eventarc. channelConnections. listTagBindings`



`eventarc.channels.get`



`eventarc.channels.getIamPolicy`



`eventarc.channels.list`



`eventarc. channels. listEffectiveTags`



`eventarc. channels. listTagBindings`



`eventarc.enrollments.get`



`eventarc. enrollments. getIamPolicy`



`eventarc.enrollments.list`



`eventarc.googleApiSources.get`



`eventarc. googleApiSources. getIamPolicy`



`eventarc.googleApiSources.list`



`eventarc. googleChannelConfigs. get`



`eventarc.kafkaSources.get`



`eventarc. kafkaSources. getIamPolicy`



`eventarc.kafkaSources.list`




`eventarc.locations.*` 





- `eventarc.locations.get`

- `eventarc.locations.list`





`eventarc.messageBuses.get`



`eventarc. messageBuses. getIamPolicy`



`eventarc.messageBuses.list`



`eventarc.messageBuses.use`



`eventarc. multiProjectSources. collectGoogleApiEvents`



`eventarc.operations.get`



`eventarc.operations.list`



`eventarc.pipelines.get`



`eventarc. pipelines. getIamPolicy`



`eventarc.pipelines.list`




`eventarc.providers.*` 





- `eventarc.providers.get`

- `eventarc.providers.list`





`eventarc.triggers.get`



`eventarc.triggers.getIamPolicy`



`eventarc.triggers.list`



`eventarc. triggers. listEffectiveTags`



`eventarc. triggers. listTagBindings`



`pubsub. messageTransforms. validate`



`pubsub.schemas.get`



`pubsub.schemas.list`



`pubsub.schemas.listRevisions`



`pubsub.schemas.validate`



`pubsub.snapshots.get`



`pubsub.snapshots.list`



`pubsub. snapshots. listEffectiveTags`



`pubsub. snapshots. listTagBindings`



`pubsub.subscriptions.get`



`pubsub.subscriptions.list`



`pubsub. subscriptions. listEffectiveTags`



`pubsub. subscriptions. listTagBindings`



`pubsub.topics.get`



`pubsub.topics.list`



`pubsub. topics. listEffectiveTags`



`pubsub.topics.listTagBindings`




`recommender.locations.*` 





- `recommender.locations.get`

- `recommender.locations.list`





`recommender. runServiceCostInsights. get`



`recommender. runServiceCostInsights. list`



`recommender. runServiceCostRecommendations. get`



`recommender. runServiceCostRecommendations. list`



`recommender. runServiceIdentityInsights. get`



`recommender. runServiceIdentityInsights. list`



`recommender. runServiceIdentityRecommendations. get`



`recommender. runServiceIdentityRecommendations. list`



`recommender. runServicePerformanceInsights. get`



`recommender. runServicePerformanceInsights. list`



`recommender. runServicePerformanceRecommendations. get`



`recommender. runServicePerformanceRecommendations. list`



`recommender. runServiceSecurityInsights. get`



`recommender. runServiceSecurityInsights. list`



`recommender. runServiceSecurityRecommendations. get`



`recommender. runServiceSecurityRecommendations. list`



`remotebuildexecution.blobs.get`



`resourcemanager.projects.get`



`resourcemanager.projects.list`




`run.configurations.*` 





- `run.configurations.get`

- `run.configurations.list`





`run.executions.get`



`run.executions.list`



`run.instances.get`



`run.instances.getIamPolicy`



`run.instances.list`



`run.jobs.get`



`run.jobs.getIamPolicy`



`run.jobs.list`



`run.jobs.listEffectiveTags`



`run.jobs.listTagBindings`



`run.locations.list`



`run.operations.get`



`run.operations.list`



`run.prompts.get`



`run.revisions.get`



`run.revisions.list`



`run.routes.get`



`run.routes.list`



`run.services.get`



`run.services.getIamPolicy`



`run.services.list`



`run.services.listEffectiveTags`



`run.services.listTagBindings`




`run.tasks.*` 





- `run.tasks.get`

- `run.tasks.list`





`run.workerpools.get`



`run.workerpools.getIamPolicy`



`run.workerpools.list`



`serviceusage. catalogs. listMembers`



`serviceusage. consumerpolicy. analyze`



`serviceusage. consumerpolicy. get`



`serviceusage. effectivepolicy. get`




`serviceusage.groups.*` 





- `serviceusage.groups.list`

- `serviceusage. groups. listExpandedMembers`

- `serviceusage. groups. listMembers`





`serviceusage.quotas.get`



`serviceusage.services.get`



`serviceusage.services.list`



`serviceusage.services.listApis`



`serviceusage. services. listDependentServices`



`serviceusage.values.test`



`storage.folders.get`



`storage.folders.list`



`storage.managedFolders.get`



`storage.managedFolders.list`



`storage.objects.get`



`storage.objects.list`

| 
|

| 

#### Cloud Run SSH Read Only
Beta 

(`roles/ run.sshReader`)



Can SSH into Cloud Run instances and read data.


| 



`run.instances.sshRead`



`run.jobs.sshRead`



`run.services.sshRead`



`run.workerpools.sshRead`

| 
|

| 

#### Cloud Run SSH Root Access
Beta 

(`roles/ run.sshRoot`)



Can SSH into Cloud Run instances and run commands as root.


| 



`run.instances.sshRoot`



`run.jobs.sshRoot`



`run.services.sshRoot`



`run.workerpools.sshRoot`

| 
|




### Service agent roles

Service agent roles should only be granted to [service agents](/iam/docs/service-agents).






| 
Role | 
Permissions | 
|



| 

#### Cloud Run Service Agent

(`roles/ run.serviceAgent`)



Gives Cloud Run service account access to managed resources.



| 



`artifactregistry. attachments. get`



`artifactregistry. attachments. list`




`artifactregistry. dockerimages.*` 





- `artifactregistry. dockerimages. get`

- `artifactregistry. dockerimages. list`





`artifactregistry. files. download`



`artifactregistry.files.get`



`artifactregistry.files.list`




`artifactregistry.locations.*` 





- `artifactregistry.locations.get`

- `artifactregistry. locations. list`






`artifactregistry. mavenartifacts.*` 





- `artifactregistry. mavenartifacts. get`

- `artifactregistry. mavenartifacts. list`






`artifactregistry.npmpackages.*` 





- `artifactregistry. npmpackages. get`

- `artifactregistry. npmpackages. list`





`artifactregistry.packages.get`



`artifactregistry.packages.list`



`artifactregistry. projectconfigs. get`



`artifactregistry. projectsettings. get`




`artifactregistry. pythonpackages.*` 





- `artifactregistry. pythonpackages. get`

- `artifactregistry. pythonpackages. list`





`artifactregistry. repositories. downloadArtifacts`



`artifactregistry. repositories. exportArtifacts`



`artifactregistry. repositories. get`



`artifactregistry. repositories. list`



`artifactregistry. repositories. listEffectiveTags`



`artifactregistry. repositories. listTagBindings`



`artifactregistry. repositories. readViaVirtualRepository`



`artifactregistry. repositories. uploadArtifacts`



`artifactregistry.rules.get`



`artifactregistry.rules.list`



`artifactregistry.tags.get`



`artifactregistry.tags.list`



`artifactregistry.versions.get`



`artifactregistry.versions.list`



`binaryauthorization. platformPolicies. evaluatePolicy`



`binaryauthorization. policy. evaluatePolicy`



`clientauthconfig.clients.list`



`cloudbuild.builds.create`



`cloudbuild.builds.get`



`compute.addresses.create`



`compute. addresses. createInternal`



`compute.addresses.delete`



`compute. addresses. deleteInternal`



`compute.addresses.get`



`compute.addresses.list`



`compute.globalOperations.get`



`compute.networks.access`



`compute.networks.get`



`compute.regionOperations.get`



`compute.subnetworks.get`



`compute.subnetworks.use`



`compute.zoneOperations.get`



`iam.serviceAccounts.actAs`



`iam. serviceAccounts. getAccessToken`



`iam. serviceAccounts. getOpenIdToken`



`iam.serviceAccounts.signBlob`



`networkservices.meshes.get`



`resourcemanager.projects.get`



`resourcemanager. projects. getIamPolicy`



`resourcemanager.projects.list`



`run.routes.invoke`



`serviceusage. catalogs. listMembers`



`serviceusage. consumerpolicy. analyze`



`serviceusage. consumerpolicy. get`



`serviceusage. effectivepolicy. get`




`serviceusage.groups.*` 





- `serviceusage.groups.list`

- `serviceusage. groups. listExpandedMembers`

- `serviceusage. groups. listMembers`





`serviceusage.services.get`



`serviceusage.services.listApis`



`serviceusage. services. listDependentServices`



`serviceusage.services.use`



`serviceusage.values.test`



`storage.buckets.create`



`storage.buckets.get`



`storage.buckets.update`



`storage.folders.get`



`storage.folders.list`



`storage.managedFolders.get`



`storage.managedFolders.list`



`storage.objects.create`



`storage.objects.delete`



`storage.objects.get`



`storage.objects.list`



`storage.objects.update`



`vpcaccess.connectors.get`

| 
|




For a reference describing the IAM permissions contained in each
IAM role, refer
to [Cloud Run IAM permissions](/run/docs/reference/iam/permissions).

## Custom roles

For developers that want to define their own roles containing bundles of
permissions that they specify, IAM offers
[custom roles](/iam/docs/creating-custom-roles). Reference the
[additional configuration](#additional-configuration) section and
[Cloud Run permissions](/run/docs/reference/iam/permissions) page
for specific permissions needed to run and manage Cloud Run
resources.

## Deployment permissions

Cloud Run resources run with a
[service identity](/run/docs/securing/service-identity).

To create or update Cloud Run resources, the
[deployer account](/run/docs/securing/service-identity#cloud-run-deployer-account)
must have access on the following resources:

- The Cloud Run resource

- The Artifact Registry repository of the Cloud Run resource's
container image

- The service account used as the service identity

By default, the service identity is the Compute Engine default service
account. However, Google recommends using a user-managed service account with
the most minimal set of permissions. See the service identity configuration
pages for [services](/run/docs/configuring/services/service-identity)
and [jobs](/run/docs/configuring/jobs/service-identity)

for more details.

Select the appropriate expander arrow to learn about the required deployment
permissions.




#### Click to view the required roles for deploying a container



To get the permissions that you need to deploy a container,
you or your administrator must grant IAM roles to the
deployer account on the following resources:




- [Cloud Run Developer](/iam/docs/roles-permissions/run#run.developer)
(`roles/run.developer`) on the Cloud Run resource

- [Artifact Registry Reader](/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader)
(`roles/artifactregistry.reader`) on the Artifact Registry repository of the container images of the Cloud Run resource

- [Service Account User](/iam/docs/roles-permissions/iam#iam.serviceAccountUser)
(`roles/iam.serviceAccountUser`) on the Cloud Run service identity




The following permissions are required to deploy services or revisions:




- `run.services.create` to create services and `run.services.update` to update services

- `run.services.get` and `run.operations.get` to read the status of the service

- `artifactregistry.repositories.downloadArtifacts` on the repository container the container images of the service

- `iam.serviceAccounts.actAs` on the service identity




For permissions that are required to deploy, execute, or run other
Cloud Run resources, see
[Cloud Run
permissions](/run/docs/reference/iam/permissions).



Note that you can find these required permissions in other
[predefined roles](/iam/docs/roles-overview#predefined), or use
them to create a
[custom roles](/iam/docs/creating-custom-roles).







#### Click to view the roles for deploying from source



To get the permissions that you need to deploy a
Cloud Run resource from source code, you or your
administrator must grant the following roles:




- [Cloud Run Source Developer](/iam/docs/roles-permissions/run#run.sourceDeveloper)
(`roles/run.sourceDeveloper`) to the deployer account on your
project.

- [Service Usage Consumer](/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer)
(`roles/serviceusage.serviceUsageConsumer`) on your project

- [Cloud Run Builder](/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) to
the Compute Engine default service account on your project.





If your Cloud Run resource interfaces with Cloud Client Libraries,
you must grant IAM roles to the service identity, as required by
the Cloud Client Libraries.

If you are using a cross-project service account to deploy, execute, or run a
Cloud Run resource, grant the Service Account Token Creator
(`roles/iam.serviceAccountTokenCreator`) role on the service identity. See
[Use service accounts in other projects](/run/docs/configuring/services/service-identity#use_service_accounts_in_other_projects)
for more details.

To grant the Cloud Run deployer account access, see the following
instructions:



### Console

To grant access on the **Cloud Run resource**:

- 

Go to the **Cloud Run** page in the Cloud de Confiance console:

[Go to Cloud Run](https://console.cloud.s3nscloud.fr/run/)

- 

Select **Services**, **Jobs**, or **Worker pools**.

- 

Click the checkbox at the left of the Cloud Run resource
you want to add principals to.

- 

In the information pane in the top right corner click the
**Permissions** tab. If the information pane isn't visible, you may need
to click **Show Info Panel**, then click **Permissions**.

- 

Click **Add principal**.

- 

In the **New principals** field, enter one or more identities that need
access to your job.

- 

From the *Role* drop-down menu, select a role or roles. The roles you
select appear in the pane with a short description of the permissions
they grant.

- 

Click **Save**.

To grant access on the **Artifact Registry repository**:

- 

Go to the **Artifact Registry** page in the Cloud de Confiance console:

[Go to Artifact Registry](https://console.cloud.s3nscloud.fr/artifacts/)

- 

Click the checkbox at the left of the repository you want to add
principals to.

- 

In the information pane in the top right corner click the
**Permissions** tab. If the information pane isn't visible, you may need
to click **Show Info Panel**, then click **Permissions**.

- 

Click **Add principal**.

- 

In the **New principals** field, enter one or more identities that need
access this repository.

- 

From the *Role* drop-down menu, select **Artifact Registry Reader**.

- 

Click **Save**.

To grant access on the **service identity resource**:

- 

Go to the **Service accounts** page in the Cloud de Confiance console:

[Go to Service accounts](https://console.cloud.s3nscloud.fr/iam-admin/serviceaccounts)

- 

Select the service account email address you are using as the service
identity, either:

- The Compute Engine default service account: ` PROJECT_NUMBER -compute@developer.s3ns-system.iam.gserviceaccount.com`

- A service account that was manually created: ` SERVICE_ACCOUNT_NAME @ PROJECT_ID .s3ns.iam.gserviceaccount.com`

- 

Click the **Permissions** tab.

- 

Click the person_add **Grant access**
button.

- 

Enter the principal (e.g. user or group email) that matches the principal
you're granting the Admin or Developer role to.

- 

In the **Select a role** drop-down, select the **Service Accounts** >
**Service Account User** role.

- 

Click **Save**.

If you are deploying from source, grant access to the deployer account and
the Cloud Build service account on your **project**:

- 

Go to the **IAM** page in the Cloud de Confiance console:

[Go to IAM](https://console.cloud.s3nscloud.fr/iam-admin/iam)

- 

Select the email address of the principal you are using as the deployer
account.

- 

Click the edit icon on the left of the principal.

- 

From the *Role* drop-down menu, select **Cloud Run Source Developer**.

- 

From the *Role* drop-down menu, select **Service Usage Consumer**.

- 

Click **Save**.

- 

Select the service account email address you are using as the service
identity, either:

- The Compute Engine default service account: ` PROJECT_NUMBER -compute@developer.s3ns-system.iam.gserviceaccount.com`

- A service account that was manually created: ` SERVICE_ACCOUNT_NAME @ PROJECT_ID .s3ns.iam.gserviceaccount.com`

- 

Click the edit icon on the left of the principal.

- 

From the *Role* drop-down menu, select **Cloud Run Builder**.

- 

Click **Save**.



### gcloud

- 

To grant access on the **Cloud Run resource**, use
gcloud commands such as
`gcloud run services add-iam-policy-binding` or
`gcloud run jobs add-iam-policy-binding`,
replacing the highlighted variables with the appropriate values:


```
gcloud run CLOUD_RUN_RESOURCE_TYPE add-iam-policy-binding NAME \ 
--member = " PRINCIPAL " \ 
--role = " ROLE " 

```


Replace the following:

- CLOUD_RUN_RESOURCE_TYPE : the Cloud Run
resource type, such as `services`, `jobs`, or `worker-pools`.

- NAME : the name of the Cloud Run resource.

- 

PRINCIPAL : the deployer account you are adding the
binding for, using the format `user|group|serviceAccount:email`
or `domain:domain`. For example:

- `user:test-user@gmail.com`

- `group:admins@example.com`

- `serviceAccount:test123@example.domain.com`

- `domain:example.domain.com`

- 

ROLE with the role name to assign to the deployer
account. For example, `roles/run.developer`.

- 

To grant access on the **Artifact Registry repository**, use the
`gcloud artifacts repositories add-iam-policy-binding` command,
replacing the highlighted variables with the appropriate values:


```
gcloud artifacts repositories add-iam-policy-binding REPOSITORY \ 
--location = " LOCATION " \ 
--member = " PRINCIPAL " \ 
--role = "roles/artifactregistry.reader" 

```


Replace the following:

- REPOSITORY : the ID of the repository.

- LOCATION : the location of the repository.

- PRINCIPAL : the deployer account you are adding the
binding for, using the format `user|group|serviceAccount:email`
or `domain:domain`.

- 

To grant access on the **service identity resource**, use the
`gcloud iam service-accounts add-iam-policy-binding` command,
replacing the highlighted variables with the appropriate values:


```
gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \ 
--member = " PRINCIPAL " \ 
--role = "roles/iam.serviceAccountUser" 

```


Replace the following:

- 

SERVICE_ACCOUNT_EMAIL : the service account email address
you are using as the service identity, such as:

- The Compute Engine default service account: ` PROJECT_NUMBER -compute@developer.s3ns-system.iam.gserviceaccount.com`

- A service account that was manually created: ` SERVICE_ACCOUNT_NAME @ PROJECT_ID .s3ns.iam.gserviceaccount.com`

- 

PRINCIPAL : the principal you are adding the binding for,
using the format `user|group|serviceAccount:email` or
`domain:domain`. For example:

- `user:test-user@gmail.com`

- `group:admins@example.com`

- `serviceAccount:test123@example.domain.com`

- `domain:example.domain.com`

- 

If you are deploying from source, grant access to the deployer account
and the Cloud Build service account on your **project** with
the `gcloud projects add-iam-policy-binding` command.

Grant the Cloud Run Builder role to the build service account
on your project:


```
gcloud projects add-iam-policy-binding PROJECT_ID \ 
--member = serviceAccount: BUILD_SERVICE_ACCOUNT_EMAIL \ 
--role = roles/run.builder

```


Replace the following:

- PROJECT_ID : your Cloud de Confiance project ID.

- 

BUILD_SERVICE_ACCOUNT_EMAIL : the service account email
address you are using as the build service account, such as:

- The Compute Engine default service account (default): ` PROJECT_NUMBER -compute@developer.s3ns-system.iam.gserviceaccount.com`.

- A service account that was manually created:
` SERVICE_ACCOUNT_NAME @ PROJECT_ID .s3ns.iam.gserviceaccount.com`.

Grant the Cloud Run Source Developer role to the deployer
account on your project:


```
gcloud projects add-iam-policy-binding PROJECT_ID \ 
--member = PRINCIPAL \ 
--role = roles/run.sourceDeveloper

```


Replace the following:

- PROJECT_NUMBER : your Cloud de Confiance project
number.

- PROJECT_ID : your Cloud de Confiance project ID.

- PRINCIPAL : the deployer account you are adding the
binding for.

Grant the Service Usage Consumer role to the deployer
account on your project:


```
gcloud projects add-iam-policy-binding PROJECT_ID \ 
--member = PRINCIPAL \ 
--role = roles/serviceusage.serviceUsageConsumer

```


Replace the following:

- PROJECT_NUMBER : your Cloud de Confiance project
number.

- PROJECT_ID : your Cloud de Confiance project ID.

- PRINCIPAL : the deployer account you are adding the
binding for.

For detailed instructions on how to find your project ID, and project
number, see
[Creating and managing projects](/resource-manager/docs/creating-managing-projects#identifying_projects).




In addition to the deployer account needing these permissions, the
Cloud Run [service agent](/iam/docs/service-agents) must have
permissions to access the deployed container. By default, Google grants the
[Cloud Run Service Agent](/iam/docs/roles-permissions/run#run.serviceAgent)
role to the Cloud Run service agent automatically.

### Avoid IAM allow policy limits in automated deployments

When using Infrastructure-as-Code (IaC) tools like
[Config Connector](/config-connector/docs/overview) to deploy Cloud Run
services, the deployer account needs permission to read container images from
Artifact Registry. These permissions are enforced by an IAM
[allow policy](/iam/docs/allow-policies), which is attached to the relevant
resource (Artifact Registry repository), and specifies which principals have been
granted which roles.

If numerous Cloud Run services are deployed, each with a unique service
account, IaC tools create individual role bindings in the Artifact Registry allow
policy. This can quickly exceed the [1,500-member-per-policy
limit](/iam/docs/allow-policies#principal-limits), which restricts the number of
principals (service accounts or users) listed in a single resource's allow
policy.

To avoid this limitation, consider using a single service account across
multiple services. This minimizes the number of entries in the Artifact Registry
allow policy.

## Optional permissions

The following optional permissions can be considered when configuring accounts
with minimal permission set:

- `monitoring.timeSeries.list` on the project level. Typically assigned
through the `roles/monitoring.viewer` role. It allows user to access
metrics generated by their Cloud Run resource. For more
information, go to the Cloud Monitoring documentation for
[Access Control](/monitoring/access-control).

- `logging.logEntries.list` on the project level. Typically assigned through
the `roles/logging.viewer` role. It allows user to access logs generated
by their Cloud Run resource. For more information, go to the
[Access Control guide](/logging/docs/access-control)
in the Cloud Logging documentation.