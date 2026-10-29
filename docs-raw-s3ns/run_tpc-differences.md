# Cloud Run in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/run/docs/tpc-differences
Last updated: 2026-10-26

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

Guides

](https://documentation.s3ns.fr/run/docs/overview/what-is-cloud-run)












# Cloud Run in Cloud de Confiance versus Google Cloud 















Cloud Run is a managed compute platform that lets you run
containers directly on top of scalable infrastructure. Because
Cloud de Confiance by S3NS is optimized for specific regulatory
requirements, there are some differences between Cloud Run in
Cloud de Confiance and Google Cloud.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Cloud Run.



For more detailed information about Cloud Run, see the
[Cloud Run overview](/run/docs/overview/what-is-cloud-run) and the rest of the
Cloud Run documentation.




You can find recommendations and best practices for using Cloud Run in
Cloud de Confiance, including recommended alternatives where features differ from
Google Cloud, in the [Recommendations](#recommendations) section.




## Key differences



There are some differences between the Cloud de Confiance version of Cloud Run and
the Google Cloud version.
Some notable differences include the following:






- 
You must create a VPC network and specify the VPC network that you want to
send traffic to. If you need to send traffic to the public internet, you
must also configure Cloud NAT. If your service sends traffic to private
addresses, then you do not need to configure Cloud NAT.


- 
Deployments from source code are unavailable; you must deploy services or
jobs from a [container image](/run/docs/resource-model).


- 
Multi-region functionality is unavailable because
Cloud de Confiance has only a single region.


- 
Only deterministic URLs are available for services.


- 
GPU configurations aren't available.


- 
Deploying Cloud Run functions, Cloud Run
worker pools, and Cloud Run instances are not available.


- 
The Cloud Run domain mappings feature is unavailable.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Cloud Run feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Hardware and OS



| 
**Execution environment**
| 
Only the [second
generation execution environment](/run/docs/about-execution-environments) is available. The second generation
environment provides full Linux compatibility and improved CPU performance.
| 
|

| 
**GPUs**
| 
Attaching GPUs to your Cloud Run services or jobs is
unavailable.
| 
|


### Availability and disaster recovery



| 
**Regions**
| 
Cloud de Confiance has only a
[single region](/docs/get-started-tpc/regions-and-zones).
Multi-region features are unavailable.
| 
|


### Integrations



| 
**Cloud Build**
| 
The integration with Cloud Build to deploy from source code is
unavailable.
| 
|

| 
**Cloud Scheduler**
| 
The integration with Cloud Scheduler is unavailable. If you need to
execute jobs on a schedule, [
create a job scheduler Cloud Run service that uses cron file
to schedule jobs](/run/docs/execute/jobs-on-schedule) .
| 
|

| 
**Eventarc**
| 
The integration with Eventarc is unavailable. You cannot use
Eventarc to trigger Cloud Run services from events.
| 
|

| 
**Identity-Aware Proxy (IAP)**
| 
Using IAP to secure your applications is unavailable.
| 
|


### Security and access control



| 
**Binary Authorization**
| 
Binary Authorization is unavailable.
| 
|

| 
**Identity-Aware Proxy (IAP)**
| 
IAP is unavailable.
| 
|


### Network



| 
**Domain mapping**
| 
The Cloud Run domain mappings feature is unavailable.
| 
|

| 
**VPC networking**
| 
Direct VPC egress is available and required.
Serverless VPC Access connectors are unavailable.
| 
|

| 
**Accessing the internet**
| 
To send requests to the public internet, you must configure
Direct VPC egress and [Cloud NAT](/run/docs/configuring/static-outbound-ip).
If your Cloud Run resource only needs to access private addresses
and Google APIs, you don't need to configure Cloud NAT.
| 
|


### Workflows and tools



| 
**Deploying from source**
| 
Deploying from source code is unavailable. You must build a container
image, push it to Artifact Registry, and deploy the image to
Cloud Run.
| 
|

| 
**Cloud Run functions**
| 
Cloud Run functions are unavailable.
| 
|

| 
**Cloud Run worker pools**
| 
Cloud Run worker pools are unavailable.
| 
|

| 
**Cloud Run instances**
| 
Cloud Run instances are unavailable.
| 
|


### Insights and observability



| 
**Other observability features**
| 
The following features are unavailable:



- SLO Monitoring

- Error Reporting

- Cloud Trace


| 
|


### Other differences



| 
**Service URLs**
| 
Only [
deterministic URLs](/run/docs/triggering/https-request#deterministic) are supported. This limits the service name to a
maximum of 50 characters. Non-deterministic URLs are unavailable.
| 
|

| 
**Assigned HTTPS URL**
| 
Cloud Run in Cloud de Confiance uses the `s3nsrun.fr` URL instead of the `run.app` URL.
| 
|




## Recommendations





- 
If you need to execute jobs on a schedule, use a cron file to
[create a script to schedule
your jobs](/run/docs/execute/jobs-on-schedule) since Cloud Scheduler is unavailable in
Cloud de Confiance.






## Related guides



The following information might also affect how you use and design for Cloud Run
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)


Related products 




- 
[Artifact Registry in
Cloud de Confiance](/artifact-registry/docs/tpc-differences)


- 
[IAM in
Cloud de Confiance](/iam/docs/tpc-differences)



Cloud de Confiance guides 




- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)