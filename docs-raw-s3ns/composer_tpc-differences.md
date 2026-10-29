# Managed Airflow in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/composer/docs/tpc-differences
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

Data analytics

](https://documentation.s3ns.fr/docs/data)






- 








[

Managed Service for Apache Airflow

](https://documentation.s3ns.fr/composer/docs)






- 








[

Gen 3 Guides

](https://documentation.s3ns.fr/composer/docs/composer-3/composer-overview)












# Managed Airflow in Cloud de Confiance versus Google Cloud 















Managed Airflow is a fully managed workflow orchestration service,
enabling you to create, schedule, monitor, and manage workflow pipelines that
span across clouds and on-premises data centers.

Managed Airflow is built on the popular Apache Airflow open source
project and operates using the Python programming language.

This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Managed Airflow.



For more detailed information about Managed Airflow, see the
[Managed Airflow overview](/composer/docs/composer-3/composer-overview) and the rest of the
Managed Airflow documentation.




## Key differences



There are some differences between the Cloud de Confiance version of Managed Airflow and
the Google Cloud version.

If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Managed Airflow feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Versions



| 

**Managed Airflow versions**
| 

Only [
Managed Airflow (Gen 3) environments](/composer/docs/composer-versions#images-composer-3) are available in
Cloud de Confiance. It isn't possible to
create Managed Airflow (Gen 2) or Managed Airflow (Legacy Gen 1) environments.
| 
|

| 

**Airflow versions**
| 

Only Airflow versions supported by Managed Airflow (Gen 3) are available in
Cloud de Confiance.
| 
|


### Availability



| 

**Resilience modes**
| 

Only
[
highly resilient (highly available) environments](/composer/docs/composer-3/set-up-highly-resilient-environments) are available in
Cloud de Confiance. You can't change the
resilience mode of an existing environment.
| 
|

| 

**Environment size**
| 

Only the Large
[
environment size](/composer/docs/composer-3/scale-environments#environment-size) is available in
Cloud de Confiance. You can't select other
values for the environment's infrastructure size and it's not possible to
adjust this parameter for an existing environment.
| 
|

| 

**Environment presets**
| 

[
Environment presets](/composer/docs/composer-3/scale-environments#presets) other than Custom
are not available in
Cloud de Confiance.
When creating an environment, you must select the Custom preset, the
Large environment's infrastructure size, and manually enter values for
resource limits.
| 
|

| 

**Maintenance windows**
| 



In Cloud de Confiance,
[custom
maintenance windows](/composer/docs/composer-3/specify-maintenance-windows) don't apply to the Cloud SQL instance that
hosts the environment's Airflow database:





- 
The Cloud SQL instance is maintained during standard
maintenance windows provided by Cloud SQL.


- 
Other environment components are maintained as usual, during the
specified maintenance windows (or use default maintenance windows).



| 
|


### Integrations



| 

**Airflow operators**
| 



In Cloud de Confiance, the following Airflow
operators aren't available:





- 
Airflow operators for Google services that are outside of
Cloud de Confiance, such as Google Docs,
Google Sheets, and Google Ads aren't available.


- 
Airflow operators for other service providers like AWS, Azure, Snowflake
aren't available in Cloud de Confiance.



| 
|





## Related guides



The following information might also affect how you use and design for Managed Airflow
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)