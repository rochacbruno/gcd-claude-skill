# Compare global and regional service

Source: https://berlin.devsitetest.how/secret-manager/docs/secret-manager-secrets-comparison
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/secret-manager/docs/tpc-differences) for more details.














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












# Compare global and regional service 















This page explains the key differences between the global and regional service of
Secret Manager.

The *global* service is the default configuration for Secret Manager.
You can start using the service with default settings and the standard API endpoint.
The secret data is replicated across multiple regions and secrets can be accessed
from any region where Google Cloud Dedicated in Germany operates.

Secret Manager also offers a *regional* service where you can
explicitly specify geographical
locations or data residency zones (DRZs) to store your secrets. Secrets can only be accessed from
within that specific region. Traffic to the regional service is directed to the appropriate location
using a global service load balancer.

Because Google Cloud Dedicated in Germany has only a single region,
the global service and the regional service in your universe provide the *same data residency guarantees*.

The following table explains the key differences between the global and
regional service.



| 
Feature | 
Global service | 
Regional service | 
|

| 
Data residency | 
[User managed replication](/secret-manager/docs/choosing-replication#user-managed)
to specific regions or [automatic replication](/secret-manager/docs/choosing-replication#automatic)
without any restriction. | 
Data is stored in a single location. Complete data residency zone (DRZ) compliance with
data at-rest, in-use, and in-transit. | 
|

| 
Endpoints | 
Single, global endpoint | 
Regional endpoints | 
|

| 
Cross-region access | 
Possible with both user managed replication and automatic replication. | 
Not possible. Secret data is tightly restricted to your region of choice
and doesn't flow outside its boundaries. | 
|

| 
Use cases | 



General secret management




- Your data doesn't have to be stored in a specific region. 

- You are only concerned with availability and latency of data, and not regulatory requirements. 


| 



Strict data residency requirements



- Your data must be stored in a specific region.

- You want to restrict movement of your sensitive data within that specific boundary,


| 
|


Not all organizations are subject to stringent DRZ regulations on where data is
stored or accessed, and not all data might fall into the sensitive category to
be subject to the DRZ regulations. So depending upon the sensitivity of the data
being handled, you can choose either between the regional or global service.

If your organization must adhere to specific data residency regulations, choose
the regional service as it ensures that your secret data doesn't leave the designated
region. If your application requires high availability and the ability to access
secrets from anywhere, the global service might be more suitable due to its
multi-region replication.

To learn more about the regional service, refer to the [regional service documentation](/secret-manager/regional-secrets/overview-rs).

## What's next

- [Enable the Secret Manager API](/secret-manager/docs/configuring-secret-manager)

- [Create and access a secret](/secret-manager/docs/create-secret-quickstart)