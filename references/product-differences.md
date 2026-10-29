# Sovereign Cloud Product Differences vs Public GCP

Per-product differences and limitations when running on Google Cloud Dedicated (Berlin, `u-germany-northeast1`) and Cloud de Confiance by S3NS (France, `u-france-east1`) compared to public Google Cloud. Each section lists what is unavailable or changed.

All products share these platform-wide constraints:
- **Single region with three zones:** `u-germany-northeast1` (`-a`, `-b`, `-c`) for Berlin; `u-france-east1` (`-a`, `-b`, `-c`) for S3NS. No multi-region features or cross-region failover.
- **Project IDs:** Prefixed with `eu0:` (Berlin) or `s3ns:` (S3NS).
- **Service endpoints:** `*.apis-berlin-build0.goog` (Berlin) or `*.s3nsapis.fr` (S3NS) instead of `*.googleapis.com`.
- **No Cloud Identity or Google Accounts:** Use Workforce Identity Federation or service accounts.
- **No Cloud Shell:** Install `gcloud` and CLI tools locally or on a sovereign cloud VM.

<!-- AUTO-SYNC:TPC-DIFFERENCES-INDEX:START -->
> **Auto-synced coverage:** 38 product-specific `tpc-differences` guides tracked across Berlin (`docs-raw/`) and S3NS (`docs-raw-s3ns/`), latest upstream update `2026-10-28`.

<details>
<summary>Tracked <code>tpc-differences</code> inventory (38 guides)</summary>

| Product | S3NS SecNumCloud 3.2 | Differences File | Last Updated | Digest |
|---|---|---|---|---|
| Access Context Manager | Qualifié SecNumCloud 3.2 | `access-context-manager_tpc-differences.md` | 2026-10-26 | `74571076b2` |
| Agent Platform (Gemini Enterprise Agent Platform) | Qualification en cours | `gemini-enterprise-agent-platform_tpc-differences.md` | 2026-10-26 | `9cf6ccf3df` |
| Artifact Registry | Qualifié SecNumCloud 3.2 | `artifact-registry_tpc-differences.md` | 2026-10-26 | `36706b91a3` |
| BigQuery | Qualifié SecNumCloud 3.2 | `bigquery_tpc-differences.md` | 2026-10-26 | `40eb9066e7` |
| Bigtable | Qualification en cours | `bigtable_tpc-differences.md` | 2026-10-28 | `8399e6dd61` |
| Cloud Armor | Qualifié SecNumCloud 3.2 | `armor_tpc-differences.md` | 2026-10-26 | `82802e7d6b` |
| Cloud Billing | — | `billing_tpc-differences.md` | 2026-10-26 | `c908f78403` |
| Cloud DNS | Qualifié SecNumCloud 3.2 | `dns_tpc-differences.md` | 2026-10-26 | `fbb94d9e80` |
| Cloud Interconnect | Qualifié SecNumCloud 3.2 | `network-connectivity_interconnect_tpc-differences.md` | 2026-10-26 | `e8eefa543b` |
| Cloud KMS | Qualifié SecNumCloud 3.2 | `kms_tpc-differences.md` | 2026-10-27 | `407d108d82` |
| Cloud Load Balancing | Qualifié SecNumCloud 3.2 | `load-balancing_tpc-differences.md` | 2026-10-26 | `fd958c37e7` |
| Cloud Logging | Qualifié SecNumCloud 3.2 | `logging_tpc-differences.md` | 2026-10-26 | `3c7ede3f89` |
| Cloud Monitoring | Qualifié SecNumCloud 3.2 | `monitoring_tpc-differences.md` | 2026-10-26 | `64c4c68e30` |
| Cloud NAT | Qualifié SecNumCloud 3.2 | `nat_tpc-differences.md` | 2026-10-26 | `355f0cd2d2` |
| Cloud NGFW | — | `firewall_tpc-differences.md` | 2026-10-26 | `b038ad3e50` |
| Cloud Quotas | Qualification en cours | `quotas_tpc-differences.md` | 2026-10-26 | `8ab8f5aa35` |
| Cloud Router | Qualifié SecNumCloud 3.2 | `network-connectivity_router_tpc-differences.md` | 2026-10-26 | `539f8b73c2` |
| Cloud Run | Qualification en cours | `run_tpc-differences.md` | 2026-10-26 | `a9f3e4b762` |
| Cloud SQL | Qualifié SecNumCloud 3.2 | `sql_tpc-differences.md` | 2026-10-26 | `b9b3152ce5` |
| Cloud Storage | Qualifié SecNumCloud 3.2 | `storage_tpc-differences.md` | 2026-10-26 | `39c9b8894e` |
| Cloud VPN | Qualifié SecNumCloud 3.2 | `network-connectivity_vpn_concepts_tpc-differences.md` | 2026-10-26 | `09d1827aa5` |
| Compute Engine | Qualifié SecNumCloud 3.2 | `compute_tpc-differences.md` | 2026-10-26 | `e1489a4601` |
| Container-Optimized OS | — | `container-optimized-os_tpc-differences.md` | 2026-10-26 | `e4ae3ed663` |
| Filestore | Qualification en cours | `filestore_tpc-differences.md` | 2026-10-26 | `63ca06de02` |
| Google Kubernetes Engine (GKE) | Qualifié SecNumCloud 3.2 | `kubernetes-engine_tpc-differences.md` | 2026-10-26 | `73814f730e` |
| IAM | Qualifié SecNumCloud 3.2 | `iam_tpc-differences.md` | 2026-10-26 | `3d1ed47caa` |
| Managed Airflow (Cloud Composer 3) | Qualification en cours | `composer_tpc-differences.md` | 2026-10-26 | `8b00656c51` |
| Managed Service for Apache Spark (Dataproc) | Qualification en cours | `managed-spark_tpc-differences.md` | 2026-10-26 | `4fd95170bf` |
| Network Service Tiers | — | `network-tiers_tpc-differences.md` | 2026-10-26 | `2dbc42433d` |
| Organization Policy | Qualifié SecNumCloud 3.2 | `organization-policy_tpc-differences.md` | 2026-10-22 | `4208565439` |
| Pub/Sub | Qualifié SecNumCloud 3.2 | `pubsub_tpc-differences.md` | 2026-10-26 | `d649238759` |
| Resource Manager | Qualifié SecNumCloud 3.2 | `resource-manager_tpc-differences.md` | 2026-10-26 | `4ae45cb244` |
| Secret Manager | Qualification en cours | `secret-manager_tpc-differences.md` | 2026-10-26 | `40aa632c10` |
| Service Usage | Qualifié SecNumCloud 3.2 | `service-usage_tpc-differences.md` | 2026-10-26 | `c466abb91d` |
| Storage Transfer Service | Qualification en cours | `storage-transfer_tpc-differences.md` | 2026-10-26 | `847b76ecde` |
| Terraform | — | `terraform_tpc-differences.md` | 2026-10-26 | `bcb0fd2998` |
| VPC | Qualifié SecNumCloud 3.2 | `vpc_tpc-differences.md` | 2026-10-26 | `06a8de4766` |
| VPC Service Controls | — | `vpc-service-controls_tpc-differences.md` | 2026-10-26 | `1f38179c73` |

</details>
<!-- AUTO-SYNC:TPC-DIFFERENCES-INDEX:END -->

---

## Access Context Manager

- Only **basic** access levels are supported. Advanced and custom access levels (CEL expressions) are unavailable.
- Only **IP subnetworks** and **geographic location** conditions are available. Other conditions (device attributes, request time) are unavailable.

---

## Access Transparency

- Available in both regions under `/assured-workloads/access-transparency/docs` to provide near real-time logs when sovereign cloud operator personnel access customer content during support cases.
- Does not have a separate `tpc-differences` page beyond platform-wide logging and organization constraints.

---

## Agent Platform (Gemini Enterprise Agent Platform)

- **Available components:** Only Model Garden, Model Registry, and synchronous Online inference (`Predict` and `RawPredict` APIs) are available.
- **Models:** Only open-weight models (such as Gemma and Mistral) via self-deploy to Agent Platform endpoints are available. Gemini models, proprietary models, and Model-as-a-Service (MaaS) endpoints are unavailable.
- **Unavailable inference & training features:**
  - Fine-tuning and custom model training
  - Batch inference
  - Streaming and chat completion APIs (`StreamPredict`, `StreamRawPredict`, `DirectPredict`, `DirectRawPredict`, `StreamDirectPredict`, `StreamDirectRawPredict`, `Explain`, `GenerateContent`, `StreamGenerateContent`, `ChatCompletions`, `EmbedContent`)
- **SDKs and tools:** Vertex AI SDK and Google Gen AI SDK are **unavailable**. Use the console, `gcloud`, or REST API calls against the regional endpoint.

---

## Artifact Registry

- **Supported formats:** Docker, Apt, Yum only. All other formats (Maven, npm, Python, Go, Generic, Helm, etc.) are unavailable.
- **Repository modes:** Only standard mode. Remote and virtual repositories are unavailable.
- **Domain:** Use `pkg-berlin-build0.goog` (Berlin) or `s3nsregistry.fr` (S3NS) instead of `pkg.dev`.
- **GPG Keys** for Apt and Yum repositories are unavailable.
- **Cleanup policies** are unavailable.
- **Client tools:** Only Docker CLI, `crictl`, Apt client, and Yum client.
- **Vulnerability scanning** with Artifact Analysis is unavailable.

---

## BigQuery

**Unavailable APIs and services:**
- Dataform API, Migration API, Analytics Hub API, Data Transfer API

**Unavailable features:**
- Data masking
- Column-level access control
- Scheduled queries
- Saved queries and notebooks
- Gemini in BigQuery
- BigQuery ML external models (internal models only)
- BigQuery public datasets
- Terraform support for BigQuery resources (check provider compatibility)
- Cloud Asset Inventory integration
- Committed use discounts (CUDs)

**Other limitations:**
- CMEK provisioning requires manual service account setup.
- Data Transfer Service: email notifications unavailable.
- No cross-region replication or failover.

---

## Bigtable

**Locations and replication:**
- Single region only (`u-germany-northeast1` or `u-france-east1`).
- **Available:** Multi-zone replication within the single region, and multi-cluster app profiles for automatic failover across zones in the same region.
- **Unavailable:** Cross-region replication and cross-region backups.

**Compute and storage:**
- **Available:** SSD and HDD storage (choice is permanent at instance creation).
- **Unavailable:** Tiered storage and Large nodes (2x capacity).

**Backups:**
- **Available:** Automated backups, hot backups, and copying a backup within the same project or another project in the same region.

**Unavailable querying, views, and analytics:**
- GoogleSQL for Bigtable (cannot query Bigtable using SQL, client libraries, or the Bigtable Studio query editor)
- Logical views and continuous materialized views
- BigQuery federation (cannot query Bigtable as an external table from BigQuery)
- Data Boost (serverless compute for batch read jobs/queries)

**Unavailable observability and tooling:**
- Key Visualizer, `ListHotTablets` API, and client-side metrics
- Bigtable Studio (Explorer and Query Editor in the console)
- Terraform provisioning for Bigtable resources
- LangChain integration (`BigtableVectorStore`, `BigtableLoader`, `BigtableChatMessageHistory`)

**Available security and governance:**
- CMEK, VPC Service Controls, IAM, Authorized views, Change streams, and Audit logging.

---

## Cloud Armor

- **Tier:** Only **Cloud Armor Standard** is available. Cloud Armor Enterprise is unavailable.
- **Supported backends:** Only **regional external Application Load Balancers** (`rxlb`) are supported. Global load balancers are unavailable.
- **Unavailable features:**
  - Adaptive Protection
  - Bot management (reCAPTCHA integration)
  - Threat intelligence and named IP lists
  - Rate limiting with `enforceOnKeyConfigs` (basic rate limiting is available)
  - Network edge security policies and advanced network DDoS protection

---

## Cloud Billing

- **Account management:** Billing accounts and invoicing are managed by the sovereign cloud operator (not self-service in Google Cloud).
- **Discounts:** Spend-based Committed Use Discounts (CUDs) require contacting operator support. Resource-based CUDs, Sustained Use Discounts (SUDs), and free tier/trial credits are unavailable.
- **Unavailable features:**
  - Cloud Billing budgets and cost alerts
  - Cost Table, Cost Breakdown, and Pricing reports in the console (BigQuery billing export is the primary way to analyze costs)
  - Gemini Cloud Assist in Billing

---

## Cloud DNS

- **Only private DNS zones** are supported. Public DNS zones are unavailable.
- Reverse DNS lookup of public IPv4/IPv6 addresses is not supported.
- Supported private zone types: forwarding zones, peering zones, managed reverse lookup zones, Service Directory zones.
- DNS server policies and response policy zones are fully available.

---

## Cloud Interconnect

- **Available types:** Only **Dedicated Interconnect** and **Partner Interconnect** (and MACsec for Dedicated Interconnect) are available.
- **Unavailable types:** Cross-Cloud Interconnect (including partner Cross-Cloud Interconnect) is unavailable.
- **SLA / Resiliency:** Critical production 99.99% availability topology (which requires multiple regions) is unavailable; multi-zone deployment within the single region is supported.

---

## Cloud KMS

**Unavailable protection levels:**
- `HSM` (multi-tenant Cloud HSM keys)
- `HSM_SINGLE_TENANT` (single-tenant Cloud HSM)
- `EXTERNAL` (EKM over internet; only EKM via VPC is supported where applicable)

**Unavailable features:**
- Cloud KMS Autokey (requires Cloud HSM)
- Key tracking and key usage tracking (including dashboard and Inventory API)
- `generateRandomBytes` method

**Location constraints:**
- Only the single regional location (`u-germany-northeast1` or `u-france-east1`).
- `global` location exists for API compatibility but maps to the single region only.
- Multi-regions other than `global` are not supported.
- CMEK integrations are limited to services available in the sovereign cloud.

---

## Cloud Load Balancing

- **Regional load balancers only:** All global load balancers and classic load balancers are unavailable.
- **Available load balancers:**
  - Regional external Application Load Balancer
  - Regional internal Application Load Balancer
  - Regional external proxy Network Load Balancer
  - Regional internal proxy Network Load Balancer
  - Regional external passthrough Network Load Balancer
  - Regional internal passthrough Network Load Balancer
- **Network tier:** Only **Premium Tier** is available (Standard Tier is unavailable).
- **Unavailable backends and integrations:**
  - Backend buckets (Cloud Storage cannot be used as a load balancer backend)
  - Serverless NEGs, internet NEGs, and hybrid connectivity NEGs (only zonal NEGs and Private Service Connect NEGs are supported)
  - Cloud CDN
  - Certificate Manager and Google-managed SSL certificates (use self-managed certificates)
  - Service Extensions

---

## Cloud NAT

- **Available:** Only **Public NAT** with IPv4-to-IPv4 translation on **Premium Network Tier**.
- **Unavailable:**
  - Private NAT (NAT between VPC networks or hybrid networks)
  - NAT64 / DNS64 (IPv6-to-IPv4 translation)
  - Standard Network Tier IP addresses

---

## Cloud NGFW (Next Generation Firewall)

- **Tiers:** Only **NGFW Essentials** (VPC firewall rules, hierarchical firewall policies, global/regional network firewall policies, IAM tags) and **NGFW Standard** (FQDN objects, geolocation objects, threat intelligence lists) are available.
- **Unavailable:** **NGFW Enterprise** (intrusion prevention service / IPS, TLS inspection, security profiles, and firewall endpoints) is unavailable.

---

## Cloud Quotas

- **Quota increase requests:** Automated self-service quota increases via the console are unavailable. To request a quota adjustment, contact operator support (`support.s3ns.fr` for S3NS or the GCD support portal for Berlin) with the project ID/number, service name, quota name, dimensions, desired value, and justification.

---

## Cloud Router

- **Routing mode:** Only **regional dynamic routing mode** is supported (global dynamic routing is unavailable because there is only one region).
- **Subnet advertisement and learned routes:** Scoped to the single region only.
- **Unavailable features:**
  - Classic VPN dynamic routing (use HA VPN)
  - Network Connectivity Center (NCC) imported transit dynamic routes and VPC spokes for full-mesh VPC connectivity
  - BGP route policies, BFD (Bidirectional Forwarding Detection), MD5 authentication, named BGP sessions, subinterfaces, and IPv6 BGP sessions

---

## Cloud Run

- **Deployment sources:** Only **Cloud Run services** and **Cloud Run jobs** deployed from container images stored in **Artifact Registry** are supported.
- **Unavailable deployment modes and runtimes:**
  - Deploying from source code (Cloud Build and Buildpacks are unavailable)
  - Cloud Run functions
  - Worker pools and instances
  - Multi-container sidecars that depend on unavailable integrations
- **Assigned URLs and domains:**
  - Services use `*.run-berlin-build0.goog` (Berlin) or `*.s3nsrun.fr` (S3NS) instead of `*.run.app`.
  - Only deterministic URLs are used, and **service names cannot exceed 50 characters**.
  - Custom domain mappings are unavailable (use a regional external Application Load Balancer if custom domains are needed).
- **Networking:**
  - **Direct VPC egress is required** (you must specify a VPC network when deploying; Serverless VPC Access connectors are unavailable).
  - Outbound traffic to the public internet requires **Cloud NAT** on the VPC network.
- **Execution environment & hardware:**
  - Only **2nd generation (`gen2`)** execution environment is available (1st generation is unavailable).
  - Cloud Run GPUs are unavailable.
- **Unavailable integrations:**
  - Cloud Scheduler (for triggering jobs/services on a schedule)
  - Eventarc
  - Identity-Aware Proxy (IAP) and Binary Authorization
  - SLO Monitoring, Error Reporting, and Cloud Trace

---

## Cloud SQL

**Database engines:**
- MySQL and PostgreSQL only. SQL Server is unavailable.

**Edition:**
- Only Enterprise Plus edition. Enterprise edition is unavailable.

**Machine types:** C3 series only:
- `db-perf-optimized-C-4`, `db-perf-optimized-C-8`, `db-perf-optimized-C-22`, `db-perf-optimized-C-44`, `db-perf-optimized-C-88`, `db-perf-optimized-C-176`

**Storage:** Hyperdisk Balanced and Hyperdisk Balanced High Availability only. Data cache is unavailable.

**Networking:**
- Private Service Connect is available.
- Private Service Connect with service automation is unavailable.
- Private services access is unavailable.

**Unavailable features:**
- Database Migration Service
- Serverless export operations
- Query insights
- Maintenance notifications
- Managed Service for Microsoft Active Directory
- User account and group IAM authentication (service account IAM auth only)

**Maintenance caveat:** Instances configured with maintenance windows do not receive automatic updates. Apply updates manually via instance restart or self-service maintenance.

---

## Cloud Storage

**Location and availability:**
- Single region only. Dual-region, multi-region, and bucket relocation are unavailable.
- Rapid Bucket (zone-level placement) is unavailable.
- You must specify a location when creating a bucket (`u-germany-northeast1` or `u-france-east1`) - no default location.

**Unavailable features:**
- Storage Insights
- Domain-named buckets and custom domain content serving (A/CNAME redirects)
- Regional and locational endpoints
- Rapid Cache
- User account HMAC keys (use service account HMAC keys)
- Usage logs and storage logs (legacy logging)
- Legacy storage classes (Multi-Regional, Regional, DRA)
- Cannot set a default project for interoperability access
- *(Note: The older Cloud Storage differences page mentions Storage Transfer Service as unavailable, but Storage Transfer Service is now available with limitations — see **Storage Transfer Service** below.)*

**Cloud Storage FUSE:**
- Supported on GKE >= 1.36.0-gke.1266000 with `custom-endpoint` and `skipCSIBucketAccessCheck` (see GKE section).
- Standalone authentication must use a Compute Engine VM in the same project or a service account key file.

---

## Cloud VPN

- **Available:** Only **HA VPN** is supported.
- **Unavailable:** Classic VPN is unavailable. Multi-region features and cross-region failover are unavailable.

---

## Compute Engine

**Machine types:** Only three series available:
- **C3** - up to 176 vCPUs (bare metal instances unavailable)
- **M3** - up to 128 vCPUs (memory-optimized)
- **A3 Edge** - `a3-edgegpu-8g-nolssd` only (NVIDIA H100 GPUs, no local SSD)

All other series (N2, E2, T2A, etc.), AMD, and Arm-based types are unavailable. TPUs are unavailable.

**Disks:** Hyperdisk Balanced only. All other disk types (Persistent Disk, Local SSD, etc.) are unavailable.

**OS images available:** Debian, Ubuntu LTS, Rocky Linux, Container-Optimized OS.
- Image projects use `eu0-system:` (Berlin) or `s3ns-system:` (S3NS) prefix (e.g. `eu0-system:debian-cloud` or `s3ns-system:debian-cloud`).
- Arm image families, SCSI interfaces, IDPF interfaces are not supported.
- Enterprise OS (Windows, RHEL, SLES) requires BYOL via image adaptation.

**Unavailable instance types:** Bare metal instances, Confidential VMs.

**Unavailable VM features:**
- OS Login, VM Manager
- Interactive serial console access, IAP TCP forwarding
- Bulk VM creation
- Future reservations (on-demand reservations are available)

**Cost:** Spot VMs available (up to 60% discount). Preemptible VMs, CUDs, and SUDs are unavailable.

**Networking:** No default network created for new projects. Only zonal DNS names (no global DNS).

**Migration:** Image adaptation is the only supported path. All other migration options are unavailable.

**Backup:** Snapshots and clones only.

**Encryption:** CMEK available. Customer-supplied encryption keys (CSEK) unavailable.

---

## Container-Optimized OS

- **Image project:** `eu0-system:cos-cloud` (Berlin) or `s3ns-system:cos-cloud` (S3NS).
- **Container registry:** `pkg-berlin-build0.goog` (Berlin) or `s3nsregistry.fr` (S3NS).
- **Available:** NVIDIA H100 GPU driver installation on A3 VMs, Cloud Logging via `fluent-bit`.
- **Unavailable:**
  - COS milestones 113 and earlier
  - Arm-based COS images
  - Automatic OS updates
  - Launching containers at VM startup via the `konlet` workflow (`gce-container-declaration` metadata)
  - Node Problem Detector and OSConfig agent

---

## Filestore

- **Service tiers:** Only the **Regional** service tier (1 TiB to 9.75 TiB capacity) is available. Basic HDD, Basic SSD, Zonal, and Enterprise tiers are unavailable.
- **Protocols:** NFSv3 and NFSv4.1 are available. However, **Managed Microsoft AD is unavailable**, so NFSv4.1 Kerberos authentication with Managed AD is unsupported (use RPCSEC_GSS / system auth within supported bounds).
- **Networking:** Only **Direct Peering** is supported for VPC connectivity. Private Services Access and Private Service Connect are unavailable for Filestore.
- **GKE integration:** The Filestore CSI driver is supported on GKE Autopilot clusters.

---

## IAM

**Supported principal types only:**
- Service accounts
- Workforce Identity Federation identities
- Workload Identity Federation identities
- GKE service accounts

Google Accounts, Google Groups, and Cloud Identity are unavailable.

**Unavailable features:**
- Principal access boundary (PAB) policies
- Privileged Access Manager (PAM)
- Policy Intelligence tools (Activity Analyzer, Policy Analyzer, Policy Simulator, Policy Troubleshooter, role recommendations, service account insights)
- Gemini role suggestions in the IAM role picker

**Service account domains differ:**
- User-managed: `PROJECT_ID.eu0.iam.gserviceaccount.com` (Berlin) or `PROJECT_ID.s3ns.iam.gserviceaccount.com` (S3NS)
- Compute default: `developer.eu0-system.iam.gserviceaccount.com` (Berlin) or `developer.s3ns-system.iam.gserviceaccount.com` (S3NS)
- Service agents: `eu0-system.iam.gserviceaccount.com` / `eu0-system.system.gserviceaccount.com` (Berlin) or `s3ns-system.iam.gserviceaccount.com` / `s3ns-system.system.gserviceaccount.com` (S3NS)

---

## Kubernetes Engine (GKE)

**Cluster modes:** Autopilot only. Standard clusters are unavailable.

**Compute:** C3 and A3 machine series only. GPU available on A3 Edge (`a3-edgegpu-8g-nolssd`) with custom ComputeClass. TPUs unavailable.

**Storage:** Hyperdisk Balanced only. No fallback to Persistent Disk.

**Node configuration unavailable:** Arm workloads, Spot VMs, compact placement.

**Release channels:** Stable and Regular only. Rapid channel features may be preview-only.

**Networking:**
- VPC-native clusters only (no route-based)
- Maximum 32 Pods per node
- Regional external load balancer (`rxlb`) used instead of global (`gxlb`)
- Multi Cluster Ingress and multi-cluster Services (MCS) unavailable
- Cloud Service Mesh unavailable
- Network policies for pod/service communication control unavailable
- Cannot disable control plane endpoints or add authorized networks
- GKE Dataplane V2 observability tools unavailable

**Security unavailable:**
- GKE security posture, Binary Authorization, Confidential GKE Nodes
- GKE control plane authority, Policy Controller
- Application-layer Secret encryption
- Connect gateway
- Privileged workload admission allowlists
- Secure kernel module loading

**Workload identity:** Uses `eu0.svc.id.goog` (Berlin) or `s3ns.svc.id.goog` (S3NS) domain instead of `svc.id.goog`.

**Service agent provisioning:** JIT (just-in-time) on first resource creation, not on API enablement. For Shared VPC setup, manually create service agents and grant default roles.

**Cloud Storage FUSE CSI driver:** Supported on GKE >= 1.36.0-gke.1266000. Requires:
- Setting `custom-endpoint=storage.apis-berlin-build0.goog:443` (Berlin) or `custom-endpoint=storage.s3nsapis.fr:443` (S3NS) in mount options
- Setting `skipCSIBucketAccessCheck: "true"` in volume attributes

**Unavailable:**
- Backup for GKE, GKE Hypercluster
- Config Sync, Config Connector, Config Controller
- Fleets and fleet management
- Google Cloud Observability integrations and dashboards
- Cluster notifications, workload metrics
- Ray Operator, Parallelstore
- Performance HPA profile, VPA InPlaceOrRecreate mode

---

## Logging

**Available:** Audit Logs, Logs Explorer, log buckets (with CMEK and custom retention), log views, log regionalization, aggregated log sinks, default settings configuration.

**Log collection:** Only from sovereign cloud resources and applications using client libraries or the Logging API. Ops Agent, legacy Logging agent, and open-source frameworks are unavailable.

**Log sink destinations available:** Sovereign cloud project, log bucket, Pub/Sub topic.
**Log sink destinations unavailable:** BigQuery datasets, Cloud Storage buckets.

**Unavailable features:**
- Observability Analytics and linked BigQuery datasets
- Log-based metrics (creation and visualization)
- Alerting policies on logs
- Streaming and tailing log entries
- Dashboard log visualization
- Custom indexing
- Retroactive log export
- Configuring log scopes via console

---

## Managed Airflow (Cloud Composer)

- **Version:** Only **Managed Airflow Gen 3 (Cloud Composer 3)** is available. Composer 1 and Composer 2 are unavailable.
- **Resiliency and sizing:**
  - Only **Highly Resilient (HA)** mode is available (Standard resilience mode is unavailable).
  - Only the **Large** environment size and **Custom** environment preset are available (Small and Medium presets are unavailable).
- **Maintenance caveat:** Custom maintenance windows configured on the environment do **not** apply to the underlying Cloud SQL database instance.
- **Airflow operators:** Only operators for services available in the sovereign cloud work. Operators targeting external Google services (Google Docs, Sheets, Ads) or third-party clouds (AWS, Azure, Snowflake) are unavailable.

---

## Managed Service for Apache Spark (Dataproc)

- **Deployment mode:** Only **cluster deployment on Compute Engine** (image version `2.3` and later) is available.
- **Unavailable deployment modes:**
  - Serverless for Apache Spark (batches and interactive sessions) is **unavailable**.
  - Managed Spark on GKE clusters is **unavailable**.
- **Supported machine types & storage:**
  - Only `m3`, `c3-highcpu`, `c3-highmem`, `c3-standard`, and `a3` (with NVIDIA H100 SXM GPUs) machine types.
  - Only **Hyperdisk** boot disks (Persistent Disk and Local SSD are unavailable).
  - Secondary workers **cannot** use Spot or Preemptible VMs.
- **Unavailable cluster & job features:**
  - Autoscaling policies
  - Initialization actions and custom images
  - Optional open-source components (Component Gateway, Jupyter Notebooks, Persistent History Server)
  - Enhanced Flexibility Mode (EFM)
  - Workflow templates
  - Granular IAM and Kerberos / secure multi-tenancy

---

## Monitoring

**Available:** Listing metric/resource types, listing metric values, PromQL queries, Prometheus API export.

**All other Cloud Monitoring API methods are unavailable.**

**Metric collection:** Only from sovereign cloud services. The following are unavailable:
- Ops Agent, legacy Monitoring agent
- Client libraries, OpenTelemetry, open-source frameworks
- On-prem/hybrid-cloud metrics
- Prometheus metrics collection
- Custom metrics

**Unavailable features:**
- Alerting policies, uptime checks, synthetic monitors
- Charts and dashboards
- Multi-project aggregation (metrics scopes)

**Recommendation:** Use PromQL with Grafana for querying and visualization.

---

## Network Service Tiers

- Only **Premium Tier** is available. Standard Network Service Tier is unavailable.

---

## Organization Policy

- **Available constraints:** All legacy managed constraints are available, along with a subset of managed constraints and custom constraints for supported services.
- **Unavailable features:**
  - Dry-run organization policies
  - Policy Intelligence tools (Policy Simulator, Policy Analyzer, Policy Troubleshooter)

---

## Pub/Sub

**Unavailable subscription types:** BigQuery subscriptions, Cloud Storage subscriptions.

**Unavailable features:**
- Dead-letter queues
- Exactly-once delivery
- Filtering
- Ordering keys
- Schemas
- Snapshots and seek
- Authentication for push subscriptions
- Payload unwrapping for push subscriptions
- All import topics (Kinesis, Cloud Storage, Event Hubs, MSK, Confluent Cloud)
- Pub/Sub Lite

**Unavailable integrations:** Dataflow, Cloud Functions, App Engine, Cloud Run event triggers.

**Architecture:** Data is regional only, not globally available. Resource location restrictions are not supported.

---

## Resource Manager

- Project IDs are automatically prefixed with `eu0:` (Berlin) or `s3ns:` (S3NS).
- Organizations are provided by the platform operator. You cannot create your own organization. Google Workspace and Cloud Identity orgs are unavailable.
- Guided organization setup flow in the console is unavailable.

---

## Secret Manager

- **Replication:** Both **automatic replication** (scoped to the sovereign cloud universe) and **regional secrets** are available. User-managed replication is unavailable.
- **Regional secret endpoint difference:** Regional secrets use the global base URL (`https://secretmanager.apis-berlin-build0.goog/v1/projects/PROJECT_ID/locations/REGION/secrets...` or `https://secretmanager.s3nsapis.fr/v1/projects/PROJECT_ID/locations/REGION/secrets...`) rather than a regional `secretmanager.REGION.rep.googleapis.com` endpoint.
- **API versions:** Only the `v1` API is available (`v1beta1` and `v1beta2` are unavailable).
- **Discovery document:** Querying the REST discovery endpoint (`/$discovery/rest?version=v1&key=API_KEY`) requires passing an explicit API key.
- **Unavailable features and integrations:**
  - GKE Secret Manager add-on
  - Parameter Manager

---

## Service Usage

- Only sovereign cloud APIs and services can be enabled. Private/third-party APIs created with Cloud Endpoints cannot be enabled.
- Default enabled APIs for new projects include only services available in the sovereign cloud.

---

## Storage Transfer Service

- **Available transfers:** Transfers between Cloud Storage buckets and **agent-based transfers** from Amazon S3 or S3-compatible object storage (using Transfer Service on-premises/self-hosted agents).
- **Unavailable sources and modes:**
  - Agentless transfers from Amazon S3
  - Microsoft Azure Blob Storage transfers
  - Transfers from URL lists
  - Event-driven transfers

---

## Terraform

- **Provider configuration:** Must set `universe_domain` (`apis-berlin-build0.goog` or `s3nsapis.fr`) and use custom endpoints where required (such as `storage_custom_endpoint` for the GCS state backend).
- **Unavailable CLI tools:**
  - Policy validation with `gcloud beta terraform vet` is unavailable (use native `terraform` checks instead).
  - Bulk resource export with `gcloud beta resource-config bulk-export` is unavailable (use native `terraform import` / configuration generation instead).

---

## VPC (Virtual Private Cloud)

- **No default network:** New projects do not have a `default` VPC network.
- **Auto mode networks:** Create a single subnet in the single sovereign cloud region.
- **Network tier:** Premium Tier only (Standard Tier unavailable).
- **Private Google Access (PGA) domains and VIPs:**
  - Berlin: `private.apis-berlin-build0.goog` and `restricted.apis-berlin-build0.goog`
  - S3NS: `private.s3nsapis.fr` (`177.222.88.0/30`) and `restricted.s3nsapis.fr` (`177.222.88.4/30`)
- **Unavailable features:**
  - Private Services Access (service networking peering; use Private Service Connect or Direct Peering depending on the service)
  - Policy-based routes
  - Network Connectivity Center VPC spokes

---

## VPC Service Controls

- **Access levels:** Only basic access levels bound directly to a policy can be used. Custom access levels and standalone access levels are unavailable.
- **Unavailable perimeter types:** Perimeter bridges are unavailable.
- **Ingress and egress rule limitations:** Ingress and egress rules **cannot** filter by service methods/operations, service identities, or VPC networks.
