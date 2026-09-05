# "Sovereign standby" with multiple universes

Source: https://berlin.devsitetest.how/docs/gcd-solutions/sovereign-standby
Last updated: 2026-09-04

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

Get started

](https://berlin.devsitetest.how/docs/get-started)












# "Sovereign standby" with multiple universes 






- On this page 
- [ Target audience ](#target_audience)
- [ Core capabilities ](#core_capabilities)
- [ Architecture ](#architecture)
- [ Components ](#components)
- [ Reference implementation ](#reference_implementation)
- 









In today's cloud environment, large regulated organizations can face
multi-layered risks to operational continuity: severe technical outages,
evolving regulatory landscapes such as the EU Digital Operational Resilience Act (DORA) and General Data Protection Regulation (GDPR) mandates, and
macroeconomic pressures.

This guide provides a blueprint for a "sovereign standby" architecture that helps organizations to
address those challenges. In this example, the core retail banking application
runs primarily on Google Cloud to leverage public cloud scale and
global infrastructure. Simultaneously, a synchronized, near-real-time mirror
environment is maintained on Google Cloud Dedicated in Germany.

If primary global cloud connectivity is severed,
organizations can invoke a planned failover protocol. All live
production traffic can be diverted to Google Cloud Dedicated in Germany, enabling core
banking operations to run isolated without losing data or dropping
customer sessions.

You can deploy this example by following the accompanying [reference
implementation](#reference_implementation) with Terraform, with a choice
of two PostgreSQL-compatible database options depending on your needs and preferences:
AlloyDB Omni or Cloud SQL. The example focuses on identity
federation and data synchronization. Additional DNS setup and application
configuration is required for a production deployment.

### Target audience

Although this example uses a banking app, this solution is designed for cloud
architects, platform engineers, and executive leaders in any regulated
industries. It serves the following stakeholders:

- **Lead cloud security architects / Heads of Identity and Access Management** who enforce federated
identity and security policies across administrative boundaries using
Workforce Identity Federation and identity providers, ensuring user access
persists seamlessly between universes without duplicated identities.

- **Lead SREs / Platform architects** who configure automated cross-universe
database replication, set up Storage Transfer Service for background asset sync,
and maintain GitOps templates to ensure complete infrastructure parity.

- **Directors of core operations** who monitor global operational health,
track Recovery Time Objectives and Recovery Point Objectives, and hold
ultimate authority to trigger the failover during disruptions.

### Core capabilities

- **Multi-universe database synchronization**: Real-time cross-universe
database replication supporting both Cloud SQL and AlloyDB Omni
between Google Cloud and Google Cloud Dedicated in Germany.

- **Infrastructure and storage parity**: Automated GitOps deployment templates
and Storage Transfer Service agents maintain identical containerized banking
microservices and Cloud Storage bucket assets across environments.

- **Federated workforce identity**: Single sign-on and role-based access
control across independent administrative domains using
Workforce Identity Federation and an external identity provider.

- **Deterministic sovereign database failover**: One-step database promotion
transitions the read-only replica on Google Cloud Dedicated in Germany into an independent
standalone primary during an outage.

- **Bi-directional secure network bridge**: Encrypted HA VPN
connectivity and Private Service Connect endpoints linking
cross-universe Google Kubernetes Engine (GKE) clusters and databases.

### Architecture

This architecture connects a primary Google Cloud production
universe with a Google Cloud Dedicated in Germany standby universe by using an encrypted
HA VPN bridge. The solution synchronizes data and microservices
continuously to ensure zero data loss and immediate failover readiness.



### Components



| 
Component | 
Tech | 
Purpose | 
|




| 
**Microservices** | 
[GKE](/kubernetes-engine/docs) | 
Identical "Bank of Anthos" containerized banking applications running in the two universes. | 
|

| 
**Database** | 
[AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/docs/overview) (provided by Google Cloud) ***or***
[Cloud SQL](/sql/docs) | 
High-performance PostgreSQL ledger using Write Ahead Log (WAL) streaming for cross-universe transaction synchronization ***or***
Managed PostgreSQL database using pglogical replication for transaction ledger mirroring. | 
|

| 
**Storage and sync** | 
[Cloud Storage](/storage/docs)
Storage Transfer Service running in Google Cloud | 
Secure object storage repositories and automated background transfer agent for assets and backups. | 
|

| 
**Networking** | 
[HA VPN](/network-connectivity/docs/vpn) and [Private Service Connect](/vpc/docs/private-service-connect) | 
Encrypted cross-universe network bridge and Private Service Connect outbound endpoints. | 
|

| 
**Identity** | 
[Workforce Identity Federation](/iam/docs/workforce-identity-federation) and an external identity provider | 
Federated identity provider integration enabling unified single sign-on across universes. | 
|

| 
**Orchestration** | 
Terraform & Helm | 
Automated infrastructure provisioning scripts and Kubernetes Helm chart packaging. | 
|



## Reference implementation

A reference implementation of this solution with Terraform is provided in
GitHub. Note that this is designed solely as a reference architecture to
demonstrate technical capabilities and cross-universe federation principles. It
is not audited, hardened, or secured for production deployment. The Bank of
Anthos sample application uses default JSON Web Token (JWT) secrets, fixed demonstration
passwords, and public ingress endpoints for testing convenience.

For prerequisites and deployment instructions, see [Sovereign Multi-Universe
Federation with Bank of
Anthos](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/demos/federation).