# Secret Manager in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/secret-manager/docs/tpc-differences
Last updated: 2026-10-26

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

Secret Manager

](https://berlin.devsitetest.how/secret-manager/docs)






- 








[

Guides

](https://berlin.devsitetest.how/secret-manager/docs/overview)












# Secret Manager in Google Cloud Dedicated versus Google Cloud 















Secret Manager is a secure and convenient storage system for API keys, passwords,
certificates, and other sensitive data.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Secret Manager.



For more detailed information about Secret Manager, see the
[Secret Manager overview](/secret-manager/docs/overview) and the rest of the
Secret Manager documentation.




## Key differences



There are some differences between the Google Cloud Dedicated version of Secret Manager and
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
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Secret Manager feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Availability and disaster recovery



| 
**Secret replication**
| 



Only automatic replication is available for the global secret service.
User-managed replication is unavailable. If you prefer to use the regional
service, regional secrets are available.



Note that because Google Cloud Dedicated in Germany
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



In Google Cloud Dedicated, the
Secret Manager REST discovery document endpoint
(`/$discovery/rest`) is not accessible with an
[identity access
token](/docs/authentication/token-types#access-tokens).



To access the discovery document endpoint, use an API key passed as a
query parameter:



`https://secretmanager.apis-berlin-build0.goog/$discovery/rest?version=v1&key= API_KEY `



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
Google Cloud Dedicated automatically directs traffic
to the appropriate location using a Global Service Load Balancer.



The URL format for accessing regional secrets differs between Google Cloud and
Google Cloud Dedicated universes.



Google Cloud:



`https://secretmanager. REGION .rep.googleapis.com/v1/projects/ PROJECT_ID /locations/ REGION /secrets?secret_id= SECRET_ID `



Google Cloud Dedicated:



`https://secretmanager.apis-berlin-build0.goog/v1/projects/ PROJECT_ID /locations/ REGION /secrets?secret_id= SECRET_ID `

| 
|





## Related guides



The following information might also affect how you use and design for Secret Manager
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)