# Secret Manager in Cloud de Confiance versus Google Cloud

Source: https://documentation.s3ns.fr/secret-manager/docs/tpc-differences
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

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Secret Manager

](https://documentation.s3ns.fr/secret-manager/docs)






- 








[

Guides

](https://documentation.s3ns.fr/secret-manager/docs/overview)












# Secret Manager in Cloud de Confiance versus Google Cloud 















Secret Manager is a secure and convenient storage system for API keys, passwords,
certificates, and other sensitive data.
This page describes the differences between the
Cloud de Confiance and Google Cloud versions of Secret Manager.



For more detailed information about Secret Manager, see the
[Secret Manager overview](/secret-manager/docs/overview) and the rest of the
Secret Manager documentation.




## Key differences



There are some differences between the Cloud de Confiance version of Secret Manager and
the Google Cloud version.
Some notable differences include the following:






- 
The Secret Manager add-on for Google Kubernetes Engine is unavailable.


- 
User-managed replication for secrets is unavailable.


- 
The regional service uses a global base URL instead of regional endpoints
for secret access.


- 
Parameter Manager is unavailable.


- 
Discovery document endpoint requests require an API key.





A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Cloud de Confiance. We also recommend reviewing the [
general differences between Cloud de Confiance and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Secret Manager feature that isn't currently
available in Cloud de Confiance, contact
[Cloud de Confiance support](https://support.s3ns.fr).
To be notified when new features roll out in Cloud de Confiance, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Cloud de Confiance.




### Availability and disaster recovery



| 
**Secret replication**
| 



Only automatic replication is available for the global secret service.
User-managed replication is unavailable. If you prefer to use the regional
service, regional secrets are available.



Note that because Cloud de Confiance by S3NS
has only a single region, global secrets satisfy the same data residency
requirements as regional secrets: both are stored and processed within that single region.

| 
|


### Workflows and tools



| 
**API versions**
| 



Only the v1 version of the Secret Manager API is available. The v1beta1 and
v1beta2 API versions are unavailable.

| 
|

| 
**Discovery document endpoint**
| 



In Cloud de Confiance, the
Secret Manager REST discovery document endpoint
(`/$discovery/rest`) is not accessible with an
[identity access
token](/docs/authentication/token-types#access-tokens).



To access the discovery document endpoint, use an API key passed as a
query parameter:



`https://secretmanager.s3nsapis.fr/$discovery/rest?version=v1&key= API_KEY `



To learn how to create an API key, see
[Use API keys](/docs/authentication/api-keys). As a security
best practice,
[apply API key
restrictions](/docs/authentication/api-keys#api_key_restrictions) to only allow calls to the
Secret Manager API.

| 
|

| 
**Parameter Manager**
| 



Parameter Manager is unavailable.

| 
|


### Integrations



| 
**Google Kubernetes Engine add-on**
| 



The Secret Manager add-on for Google Kubernetes Engine is unavailable.

| 
|


### Network



| 
**Regional endpoints**
| 



Regional endpoints are unavailable. Instead of using regional endpoints, the regional service in
Cloud de Confiance automatically directs traffic
to the appropriate location using a Global Service Load Balancer.



The URL format for accessing regional secrets differs between Google Cloud and
Cloud de Confiance universes.



Google Cloud:



`https://secretmanager. REGION .rep.googleapis.com/v1/projects/ PROJECT_ID /locations/ REGION /secrets?secret_id= SECRET_ID `



Cloud de Confiance:



`https://secretmanager.s3nsapis.fr/v1/projects/ PROJECT_ID /locations/ REGION /secrets?secret_id= SECRET_ID `

| 
|





## Related guides



The following information might also affect how you use and design for Secret Manager
in Cloud de Confiance by S3NS. These guides include general information about working in Cloud de Confiance,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Cloud de Confiance and their differences from
their Google Cloud counterparts, see the [product list.](https://documentation.s3ns.fr/products)





- 


[Cloud de Confiance by S3NS overview](/docs/overview/tpc-overview)




- 


[Key differences between Cloud de Confiance by S3NS and Google Cloud](/docs/overview/tpc-key-differences)