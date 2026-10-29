# Google Cloud Dedicated (GCD) & Cloud de Confiance (S3NS) - Available Services Reference

Google Cloud Dedicated in Germany (`u-germany-northeast1`) and Cloud de Confiance by S3NS in France (`u-france-east1`) are sovereign cloud offerings that provide a subset of Google Cloud services in dedicated, regionally constrained environments. Not all Google Cloud services are available — only the services listed below are supported.

## Available API Services

The following services have confirmed documentation and API availability in the sovereign cloud regions:

<!-- AUTO-SYNC:AVAILABLE-API-SERVICES:START -->
- Access Context Manager
- Access Transparency
- Agent Platform (Gemini Enterprise Agent Platform)
- API Discovery Service
- API Keys
- Artifact Registry
- BigLake
- BigQuery
- BigQuery Data Policy
- BigQuery ML
- BigQuery Reservation
- BigQuery Storage
- Bigtable
- Cloud Armor
- Cloud Audit Logs
- Cloud Billing
- Cloud DNS
- Cloud External Key Manager (EKM)
- Cloud GPUs
- Cloud Interconnect
- Cloud KMS
- Cloud Load Balancing
- Cloud Logging
- Cloud Monitoring
- Cloud NAT
- Cloud NGFW
- Cloud Quotas
- Cloud Router
- Cloud Run
- Cloud SQL
- Cloud Storage
- Cloud VPN
- Compute Engine
- Container-Optimized OS
- Filestore
- Google Cloud CLI (gcloud SDK)
- Google Kubernetes Engine (GKE)
- Hyperdisk
- IAM
- Managed Airflow (Cloud Composer 3)
- Managed Service for Apache Spark (Dataproc)
- Network Service Tiers
- Organization Policy
- Private Service Connect
- Pub/Sub
- Resource Manager
- Secret Manager
- Service Account Credentials
- Service Directory
- Service Usage
- Shielded VM
- Storage Transfer Service
- Terraform
- VPC
- VPC Service Controls
- Workforce Identity Federation
- Workload Identity Federation
<!-- AUTO-SYNC:AVAILABLE-API-SERVICES:END -->

---

## S3NS SecNumCloud 3.2 Qualification Status (PREMI3NS)

On **Cloud de Confiance by S3NS** (`u-france-east1`, PREMI3NS offering), services fall into three ANSSI **SecNumCloud 3.2** qualification categories (source: [s3ns.io/offres/premi3ns-cloud-de-confiance](https://www.s3ns.io/offres/premi3ns-cloud-de-confiance)):

- **Qualifié SecNumCloud 3.2:** Fully covered by the ANSSI SecNumCloud 3.2 qualification visa (and ISO 27001 / HDS certification).
- **Qualification en cours:** Available and documented on S3NS today, with ANSSI SecNumCloud 3.2 qualification currently in progress. Verify compliance requirements with the customer before using these services for workloads strictly mandated to run only on SecNumCloud-qualified services.
- **À venir:** Announced on the S3NS PREMI3NS roadmap; not yet generally available on S3NS.

<!-- AUTO-SYNC:SECNUMCLOUD-STATUS:START -->
**Summary (PREMI3NS catalog):** **29** `Qualifié SecNumCloud 3.2` | **10** `Qualification en cours` | **4** `À venir`

### Qualifié SecNumCloud 3.2 (29 services)

**Access Context Manager**, **Artifact Registry**, **BigQuery**, **BigQuery Reservation**, **Cloud Armor**, **Cloud DNS**, **Cloud Interconnect**, **Cloud Key Management Service**, **Cloud Load Balancing**, **Cloud Logging**, **Cloud Monitoring**, **Cloud NAT**, **Cloud Router**, **Cloud SQL**, **Cloud Storage**, **Cloud VPN**, **Compute Engine**, **Google Kubernetes Engine Autopilot**, **Identity and Access Management**, **Networking**, **Organization Policy**, **Pub/Sub**, **Resource Manager**, **Service Account Credentials**, **Service Directory**, **Service Usage**, **Virtual Private Cloud**, **Workforce identity federation**, **Workload identity federation using the Security Token Service API**.

### Qualification en cours (10 services — available on S3NS, ANSSI qualification in progress)

| Service (PREMI3NS) | Status | Documentation Hub |
|---|---|---|
| Access Transparency | `Qualification en cours` | Access Transparency |
| Bigtable | `Qualification en cours` | Bigtable |
| Cloud Quota | `Qualification en cours` | Cloud Quotas |
| Cloud Run | `Qualification en cours` | Cloud Run |
| Filestore | `Qualification en cours` | Filestore |
| Gemini platform | `Qualification en cours` | Agent Platform (Gemini Enterprise Agent Platform) |
| Managed Service for Apache Airflow | `Qualification en cours` | Managed Airflow (Cloud Composer 3) |
| Managed Service for Apache Spark | `Qualification en cours` | Managed Service for Apache Spark (Dataproc) |
| Secret Manager | `Qualification en cours` | Secret Manager |
| Storage Transfer Service | `Qualification en cours` | Storage Transfer Service |

### À venir (4 services — S3NS roadmap, not yet available)

**Cloud Asset Inventory**, **Cloud Build**, **Cloud Spanner**, **Network Connectivity Center**.
<!-- AUTO-SYNC:SECNUMCLOUD-STATUS:END -->

---

## Services by Category

### Compute & Containers

| Service | Status | Description |
|---------|--------|-------------|
| Compute Engine | Available | Scalable VMs (`C3`, `M3`, `A3 Edge`) and instance groups |
| Google Kubernetes Engine (GKE) | Available | Managed Kubernetes (Autopilot mode only) |
| Cloud Run | Available | Managed serverless container services and jobs (from Artifact Registry) |
| Cloud GPUs | Available | NVIDIA H100 GPU acceleration on `A3` machine series |
| Container-Optimized OS | Available | Optimized OS for running containers on Compute Engine and GKE |
| Shielded VM | Available | Hardened VMs with rootkit/bootkit protection |
| Hyperdisk | Available | High-performance block storage (`hyperdisk-balanced`) for VMs |

**Key limitations:** Machine types (`C3`, `M3`, `A3`), single-region zones, and disk types (`Hyperdisk`) are constrained to the sovereign cloud environment. See [product-differences.md](product-differences.md) for per-service constraints.

### AI & Machine Learning

| Service | Status | Description |
|---------|--------|-------------|
| Agent Platform (Gemini Enterprise Agent Platform) | Available | Model Garden, Model Registry, and synchronous online inference (`Predict`/`RawPredict`) for open-weight models (Gemma, Mistral) |
| BigQuery ML | Available | ML model training and inference via SQL (internal models only) |

**Key limitations:** Proprietary Gemini models, Model-as-a-Service, fine-tuning, batch inference, streaming/chat completion endpoints, and Vertex AI / Google Gen AI SDKs are unavailable.

### Networking

| Service | Status | Description |
|---------|--------|-------------|
| Virtual Private Cloud (VPC) | Available | Core network for workload connectivity (no default VPC auto-created) |
| Cloud DNS | Available | Managed private DNS zones and DNS server policies |
| Cloud Load Balancing | Available | Regional Application and Network Load Balancers (Premium Tier only) |
| Cloud VPN | Available | HA VPN IPsec tunnels to peer networks |
| Cloud Interconnect | Available | Dedicated Interconnect and Partner Interconnect (with MACsec) |
| Cloud Router | Available | Regional dynamic BGP route exchange |
| Cloud NAT | Available | Public NAT (IPv4-to-IPv4) outbound internet connectivity |
| Private Service Connect | Available | Private access to managed services and sovereign cloud APIs |
| Network Service Tiers | Available | Premium Network Service Tier |
| Cloud Next Generation Firewall (NGFW) | Available | Essentials and Standard tiers distributed firewall |
| VPC Service Controls | Available | Security perimeters for sovereign cloud services |
| Google Cloud Armor | Available | Standard tier DDoS and WAF protection for regional external ALB |
| Service Directory | Available | Service registry and private DNS discovery |

**Key limitations:** Global load balancers, Cloud CDN, Certificate Manager, Classic VPN, Cross-Cloud Interconnect, Private NAT, Standard Network Tier, and NGFW Enterprise (IPS/TLS inspection) are unavailable.

### Storage & Data Transfer

| Service | Status | Description |
|---------|--------|-------------|
| Cloud Storage | Available | Single-region object storage |
| Filestore | Available | Regional tier managed NFS file storage (1 TiB–9.75 TiB, Direct Peering) |
| Storage Transfer Service | Available | Bucket-to-bucket transfers and agent-based Amazon S3 transfers |
| Hyperdisk | Available | Scalable high-performance block storage |

**Key limitations:** Multi-region/dual-region buckets, Storage Insights, Basic/Zonal/Enterprise Filestore tiers, and agentless AWS / Azure Storage Transfer are unavailable.

### Databases

| Service | Status | Description |
|---------|--------|-------------|
| Cloud SQL | Available | Managed relational databases (MySQL and PostgreSQL, Enterprise Plus on C3) |
| Bigtable | Available | Managed NoSQL wide-column database (single-region, multi-zone replication, SSD/HDD) |

**Key limitations:** Cloud SQL Server engine, Spanner, Firestore, Memorystore, and AlloyDB are not available. Bigtable GoogleSQL, Data Boost, BigQuery federation, and cross-region replication are unavailable.

### Data Analytics & Orchestration

| Service | Status | Description |
|---------|--------|-------------|
| BigQuery | Available | Managed data warehouse with built-in ML |
| BigQuery Data Policy | Available | Data governance and access policies |
| BigQuery Reservation | Available | Capacity reservation management |
| BigQuery Storage | Available | High-throughput read/write API for analytics workloads |
| BigLake | Available | Query external data in Cloud Storage with access delegation |
| Managed Service for Apache Spark (Dataproc) | Available | Apache Spark clusters on Compute Engine (image 2.3+, `C3`/`M3`/`A3`) |
| Managed Airflow (Cloud Composer) | Available | Managed Apache Airflow Gen 3 (Composer 3, Highly Resilient Large/Custom) |
| Pub/Sub | Available | Regional event stream ingestion and messaging |

**Key limitations:** Serverless Spark, Spark on GKE, Composer 1/2, Dataflow, Dataform, Datastream, and Data Fusion are unavailable.

### Security and Identity

| Service | Status | Description |
|---------|--------|-------------|
| Identity and Access Management (IAM) | Available | Fine-grained access control for resources |
| Secret Manager | Available | Secret storage and versioning (automatic and regional replication, `v1` API) |
| Access Context Manager | Available | Basic attribute-based access levels (IP and geo conditions) |
| Access Transparency | Available | Near real-time logs of operator accesses during support cases |
| Cloud KMS | Available | Software key management and CMEK integration |
| Cloud External Key Manager (EKM) | Available | Externally managed encryption keys via VPC |
| API Keys | Available | API key creation and management |
| VPC Service Controls | Available | Security perimeters for data protection |
| Organization Policy Service | Available | Programmatic resource governance and constraints |
| Workforce Identity Federation | Available | External identity provider federation for human users |
| Workload Identity Federation | Available | External identity federation for workloads |
| Service Account Credentials | Available | Service account key and token management |
| Cloud Audit Logs | Available | Activity tracking and auditing |

**Key limitations:** Cloud HSM, KMS Autokey, Security Command Center, Binary Authorization, Certificate Authority Service, and Google Identity/Workspace accounts are not available.

### Observability

| Service | Status | Description |
|---------|--------|-------------|
| Cloud Logging | Available | Log storage, search, analysis, and sinks (Log buckets, Pub/Sub) |
| Cloud Monitoring | Available | Metric listing and PromQL / Prometheus API export |

**Key limitations:** Cloud Trace, Cloud Profiler, Error Reporting, Ops Agent, custom metrics, and native Monitoring dashboards/alerts are unavailable (use PromQL with Grafana).

### Application Development, Billing, and Resource Management

| Service | Status | Description |
|---------|--------|-------------|
| Artifact Registry | Available | Container (`Docker`) and OS package (`Apt`, `Yum`) repositories |
| Resource Manager | Available | Organization, folder, project, and tag management |
| Cloud Billing | Available | Operator-managed billing accounts and BigQuery billing export |
| Cloud Quotas | Available | Quota inspection and support-assisted quota adjustments |
| Service Usage | Available | API enablement and lifecycle management |
| API Discovery Service | Available | API metadata and discovery documents |
| Terraform | Available | Infrastructure provisioning via the Google Terraform provider |

---

## Discovered Documentation Inventory (Auto-Synced)

<!-- AUTO-SYNC:DISCOVERED-PRODUCTS-TABLE:START -->
Total scraped pages: **434** (Berlin GCD) / **433** (France S3NS).

| Service / Documentation Hub | Berlin Pages | S3NS Pages | S3NS SecNumCloud 3.2 | Differences Guide | Last Updated |
|---|---:|---:|---|---|---|
| Access Context Manager | 8 | 8 | Qualifié SecNumCloud 3.2 | `access-context-manager_tpc-differences.md` | 2026-10-26 |
| Access Transparency | 7 | 7 | Qualification en cours | — | 2026-10-26 |
| Agent Platform (Gemini Enterprise Agent Platform) | 7 | 7 | Qualification en cours | `gemini-enterprise-agent-platform_tpc-differences.md` | 2026-10-28 |
| API Keys | 4 | 4 | — | — | 2026-10-26 |
| Artifact Registry | 6 | 6 | Qualifié SecNumCloud 3.2 | `artifact-registry_tpc-differences.md` | 2026-10-26 |
| BigQuery | 16 | 16 | Qualifié SecNumCloud 3.2 | `bigquery_tpc-differences.md` | 2026-10-27 |
| Bigtable | 14 | 14 | Qualification en cours | `bigtable_tpc-differences.md` | 2026-10-28 |
| Cloud Armor | 3 | 3 | Qualifié SecNumCloud 3.2 | `armor_tpc-differences.md` | 2026-10-26 |
| Cloud Billing | 8 | 8 | — | `billing_tpc-differences.md` | 2026-10-26 |
| Cloud DNS | 8 | 8 | Qualifié SecNumCloud 3.2 | `dns_tpc-differences.md` | 2026-10-26 |
| Cloud Interconnect | 2 | 2 | Qualifié SecNumCloud 3.2 | `network-connectivity_interconnect_tpc-differences.md` | 2026-10-26 |
| Cloud KMS | 8 | 8 | Qualifié SecNumCloud 3.2 | `kms_tpc-differences.md` | 2026-10-27 |
| Cloud Load Balancing | 3 | 3 | Qualifié SecNumCloud 3.2 | `load-balancing_tpc-differences.md` | 2026-10-26 |
| Cloud Logging | 10 | 10 | Qualifié SecNumCloud 3.2 | `logging_tpc-differences.md` | 2026-10-26 |
| Cloud Monitoring | 4 | 4 | Qualifié SecNumCloud 3.2 | `monitoring_tpc-differences.md` | 2026-10-26 |
| Cloud NAT | 3 | 3 | Qualifié SecNumCloud 3.2 | `nat_tpc-differences.md` | 2026-10-26 |
| Cloud NGFW | 3 | 3 | — | `firewall_tpc-differences.md` | 2026-10-26 |
| Cloud Quotas | 29 | 29 | Qualification en cours | `quotas_tpc-differences.md` | 2026-10-27 |
| Cloud Router | 2 | 2 | Qualifié SecNumCloud 3.2 | `network-connectivity_router_tpc-differences.md` | 2026-10-26 |
| Cloud Run | 14 | 14 | Qualification en cours | `run_tpc-differences.md` | 2026-10-28 |
| Cloud SQL | 3 | 3 | Qualifié SecNumCloud 3.2 | `sql_tpc-differences.md` | 2026-10-28 |
| Cloud Storage | 10 | 10 | Qualifié SecNumCloud 3.2 | `storage_tpc-differences.md` | 2026-10-26 |
| Cloud VPN | 2 | 2 | Qualifié SecNumCloud 3.2 | `network-connectivity_vpn_concepts_tpc-differences.md` | 2026-10-26 |
| Compute Engine | 9 | 9 | Qualifié SecNumCloud 3.2 | `compute_tpc-differences.md` | 2026-10-26 |
| Container-Optimized OS | 3 | 3 | — | `container-optimized-os_tpc-differences.md` | 2026-10-26 |
| Filestore | 16 | 16 | Qualification en cours | `filestore_tpc-differences.md` | 2026-10-26 |
| Google Cloud CLI (gcloud SDK) | 2 | 2 | — | — | 2026-10-27 |
| Google Kubernetes Engine (GKE) | 9 | 9 | Qualifié SecNumCloud 3.2 | `kubernetes-engine_tpc-differences.md` | 2026-10-27 |
| IAM | 18 | 18 | Qualifié SecNumCloud 3.2 | `iam_tpc-differences.md` | 2026-10-27 |
| Managed Airflow (Cloud Composer 3) | 18 | 18 | Qualification en cours | `composer_tpc-differences.md` | 2026-10-26 |
| Managed Service for Apache Spark (Dataproc) | 10 | 10 | Qualification en cours | `managed-spark_tpc-differences.md` | 2026-10-26 |
| Network Service Tiers | 3 | 3 | — | `network-tiers_tpc-differences.md` | 2026-10-26 |
| Organization Policy | 3 | 3 | Qualifié SecNumCloud 3.2 | `organization-policy_tpc-differences.md` | 2026-10-26 |
| Pub/Sub | 11 | 11 | Qualifié SecNumCloud 3.2 | `pubsub_tpc-differences.md` | 2026-10-26 |
| Resource Manager | 11 | 11 | Qualifié SecNumCloud 3.2 | `resource-manager_tpc-differences.md` | 2026-10-26 |
| Secret Manager | 10 | 10 | Qualification en cours | `secret-manager_tpc-differences.md` | 2026-10-26 |
| Service Directory | 2 | 2 | Qualifié SecNumCloud 3.2 | — | 2026-10-26 |
| Service Usage | 9 | 9 | Qualifié SecNumCloud 3.2 | `service-usage_tpc-differences.md` | 2026-10-26 |
| Storage Transfer Service | 7 | 7 | Qualification en cours | `storage-transfer_tpc-differences.md` | 2026-10-26 |
| Terraform | 32 | 32 | — | `terraform_tpc-differences.md` | 2026-10-26 |
| VPC | 7 | 7 | Qualifié SecNumCloud 3.2 | `vpc_tpc-differences.md` | 2026-10-26 |
| VPC Service Controls | 3 | 3 | — | `vpc-service-controls_tpc-differences.md` | 2026-10-26 |
<!-- AUTO-SYNC:DISCOVERED-PRODUCTS-TABLE:END -->

---

## Recent Sovereign Cloud Release Notes (Auto-Synced)

The following table summarizes the most recent sovereign cloud release notes extracted automatically from `docs-raw-s3ns/release-notes.md` and `docs-raw/release-notes.md`:

<!-- AUTO-SYNC:RECENT-RELEASE-NOTES:START -->
| Date | Product | Type | Summary |
|---|---|---|---|
| October 27, 2026 | **Google Kubernetes Engine** | `Change` | **(2026-R46) Version updates:** GKE cluster versions have been updated. |
| October 26, 2026 | **Compute Engine** | `Security` | A vulnerability (CVE-2026-85299) about incorrect authorization in Compute Engine was discovered and has been addressed. For more information, see the GCP-2026-073 security bulletin (`/compute/docs/security-bulletins#gcp-2026-073`). |
| October 26, 2026 | **Google Kubernetes Engine** | `Change` | **(2026-R45) Version updates:** GKE cluster versions have been updated. |
| October 21, 2026 | **Bigtable** | `Feature` | Bigtable is now available in Google Cloud. For more information, see Bigtable in Google Cloud versus Google Cloud (`/bigtable/docs/tpc-differences`). |
| October 20, 2026 | **Filestore** | `Feature` | Filestore is available in Google Cloud. For more information, see Filestore differences in Google Cloud versus Google Cloud (`/filestore/docs/tpc-differences`). |
| October 19, 2026 | **Google Cloud Armor** | `Security` | Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-stable` rulesets. For more information, see Tuning Google Cloud Armor WAF rules (`/armor/docs/rule-tuning`). |
| October 19, 2026 | **Google Cloud Armor** | `Security` | Security fixes and enhancements to Cloud Armor preconfigured WAF `stable` rulesets for v3.0. For more information, see Tuning Google Cloud Armor WAF rules (`/armor/docs/rule-tuning`). |
| October 19, 2026 | **Virtual Private Cloud** | `Feature` | **General Availability**: VPC Flow Logs adds the following metadata annotations and packet drop reasons for Cloud NAT: |
| October 14, 2026 | **Google Kubernetes Engine** | `Change` | **(2026-R44) Version updates:** GKE cluster versions have been updated. |
| October 10, 2026 | **Cloud SQL for MySQL** | `Change` | MySQL 8.0.46 is now the default minor version (`/sql/docs/mysql/db-versions#database-version-support`) for Cloud SQL for MySQL 8.0. |
| October 08, 2026 | **Cloud SQL for MySQL** | `Feature` | Cloud SQL for MySQL now supports the `innodb_cloudsql_managed_buffer_pool_tuneup_pct` database flag. |
| October 08, 2026 | **Google Kubernetes Engine** | `Change` | **(2026-R43) Version updates:** GKE cluster versions have been updated. |
<!-- AUTO-SYNC:RECENT-RELEASE-NOTES:END -->

---

## Notable Unavailable Services

The following commonly used Google Cloud services are **NOT** available in GCD or S3NS:

- **AI/ML:** Proprietary Gemini APIs, Vertex AI Training/Pipelines/AutoML, Vision AI, Natural Language AI, Translation AI
- **Databases:** Spanner, Firestore, Memorystore (Redis/Memcached), AlloyDB, Database Migration Service
- **Data:** Dataflow, Dataform, Data Fusion, Datastream, Analytics Hub, Serverless Spark
- **Serverless:** App Engine, Cloud Run functions / Cloud Functions, Cloud Scheduler, Cloud Tasks, Eventarc
- **CI/CD:** Cloud Build, Cloud Deploy, Cloud Source Repositories
- **Observability:** Cloud Trace, Cloud Profiler, Error Reporting, Ops Agent
- **Security:** Cloud HSM, Security Command Center, Binary Authorization, Certificate Authority Service, Identity-Aware Proxy (IAP), Managed Microsoft AD
- **Networking:** Cloud CDN, Certificate Manager, Classic VPN, Cross-Cloud Interconnect, Network Connectivity Center VPC spokes
- **Other:** Cloud Shell, Apigee, API Gateway, Firebase

---

## Developer Tools and SDK Support

Client libraries are supported for: C#/.NET, C++, Go, Java, JavaScript/Node.js, PHP, Python, Ruby, Rust (always configure `GOOGLE_CLOUD_UNIVERSE_DOMAIN`).

The Google Cloud CLI (`gcloud`) is the primary command-line interface for managing resources when configured with the sovereign cloud universe domain.
