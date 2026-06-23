# GCD Product Differences vs Public GCP

Per-product differences and limitations when running on Google Cloud Dedicated (GCD)
compared to public Google Cloud. Each section lists what is unavailable or changed.

All products share these constraints: single region (`u-germany-northeast1`) with
three zones, no multi-region features, no Cloud Shell, project IDs prefixed with
`eu0:`, service endpoints use `*.apis-berlin-build0.goog` instead of `*.googleapis.com`.

---

## Access Context Manager

- Only **basic** access levels are supported. Advanced and custom access levels are unavailable.
- Only **IP subnetworks** and **geographic location** conditions are available. Other conditions (device attributes, request time) are unavailable.

---

## API Keys

The `api-keys_tpc-differences.md` source covers general GCD platform differences rather than API Keys-specific ones. The key platform-wide differences relevant to API Keys:

- Service names stay the same (e.g. `bigquery.googleapis.com`) but endpoints differ (e.g. `bigquery.apis-berlin-build0.goog`).
- Cloud Identity is unavailable - use Workforce Identity Federation or service accounts.
- No default VPC network is created for new projects.
- No Cloud Shell - install CLI tools locally.
- No free trial tier, no committed use discounts (CUDs).

---

## Artifact Registry

- **Supported formats:** Docker, Apt, Yum only. All other formats (Maven, npm, Python, Go, etc.) are unavailable.
- **Repository modes:** Only standard mode. Remote and virtual repositories are unavailable.
- **Domain:** Use `pkg-berlin-build0.goog` instead of `pkg.dev`.
- **GPG Keys** for Apt and Yum repositories are unavailable.
- **Cleanup policies** are unavailable.
- **Client tools:** Only Docker CLI, `critcl`, Apt client, and Yum client.
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
- Terraform support
- Cloud Asset Inventory integration
- Committed use discounts (CUDs)

**Other limitations:**
- CMEK provisioning requires manual setup.
- Data Transfer Service: email notifications unavailable.
- No cross-region replication or failover.

---

## Cloud DNS

- **Only private DNS zones** are supported. Public DNS zones are unavailable.
- Reverse DNS lookup of public IPv4/IPv6 addresses is not supported.
- Supported private zone types: forwarding zones, peering zones, managed reverse lookup zones, Service Directory zones.
- DNS server policies and response policy zones are fully available.

---

## Cloud KMS

**Unavailable protection levels:**
- `HSM` (multi-tenant Cloud HSM keys)
- `HSM_SINGLE_TENANT` (single-tenant Cloud HSM)
- `EXTERNAL` (EKM over internet)

**Unavailable features:**
- Cloud KMS Autokey (requires Cloud HSM)
- Key tracking and key usage tracking (including dashboard and Inventory API)
- `generateRandomBytes` method

**Location constraints:**
- Only `u-germany-northeast1` regional location.
- `global` location exists but maps to the single region only.
- Multi-regions other than `global` are not supported.
- CMEK integrations limited to services available in GCD.

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

**Maintenance caveat:** Instances configured with maintenance windows do not receive automatic updates in GCD. Apply updates manually via instance restart or self-service maintenance.

---

## Cloud Storage

**Location and availability:**
- Single region only. Dual-region, multi-region, and bucket relocation are unavailable.
- Rapid Bucket (zone-level placement) is unavailable.
- You must specify a location when creating a bucket - no default location.

**Unavailable features:**
- Storage Transfer Service
- Storage Insights
- Domain-named buckets and custom domain content serving (A/CNAME redirects)
- Regional and locational endpoints
- Rapid Cache
- User account HMAC keys (use service account HMAC keys)
- Usage logs and storage logs (legacy logging)
- Legacy storage classes (Multi-Regional, Regional, DRA)
- Cannot set a default project for interoperability access

**Cloud Storage FUSE:**
- The GKE CSI driver is not available through standard means (see GKE section for workaround).
- Authentication must use a Compute Engine VM in the same project or a service account key file.

---

## Compute Engine

**Machine types:** Only three series available:
- **C3** - up to 176 vCPUs (bare metal instances unavailable)
- **M3** - up to 128 vCPUs (memory-optimized)
- **A3 Edge** - `a3-edgegpu-8g-nolssd` only (NVIDIA H100 GPUs, no local SSD)

All other series (N2, E2, T2A, etc.), AMD, and Arm-based types are unavailable. TPUs are unavailable.

**Disks:** Hyperdisk Balanced only. All other disk types (Persistent Disk, Local SSD, etc.) are unavailable.

**OS images available:** Debian, Ubuntu LTS, Rocky Linux, Container-Optimized OS.
- Image projects use `eu0-system:` prefix (e.g. `eu0-system:debian-cloud`).
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
- Custom constraints and managed constraints for Organization Policy (predefined policies only)

**Service account domains differ:**
- User-managed: `PROJECT_ID.eu0.iam.gserviceaccount.com`
- Compute default: `developer.eu0-system.iam.gserviceaccount.com`
- Service agents: `eu0-system.iam.gserviceaccount.com` or `eu0-system.system.gserviceaccount.com`

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

**Workload identity:** Uses `eu0.svc.id.goog` domain (not `svc.id.goog`).

**Service agent provisioning:** JIT (just-in-time) on first resource creation, not on API enablement. For Shared VPC setup, manually create service agents and grant default roles.

**Cloud Storage FUSE CSI driver:** Supported on GKE >= 1.36.0-gke.1266000. Requires:
- Setting `custom-endpoint=storage.apis-berlin-build0.goog:443` in mount options
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

**Log collection:** Only from GCD resources and applications using client libraries or the Logging API. Ops Agent, legacy Logging agent, and open-source frameworks are unavailable.

**Log sink destinations available:** GCD project, log bucket, Pub/Sub topic.
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

## Monitoring

**Available:** Listing metric/resource types, listing metric values, PromQL queries, Prometheus API export.

**All other Cloud Monitoring API methods are unavailable.**

**Metric collection:** Only from GCD services. The following are unavailable:
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

**Unavailable integrations:** Dataflow, Cloud Functions, App Engine, Cloud Run.

**Architecture:** Data is regional only, not globally available. Resource location restrictions are not supported.

---

## Resource Manager

- Project IDs are automatically prefixed with `eu0:`.
- Organizations are provided by the platform operator. You cannot create your own organization. Google Workspace and Cloud Identity orgs are unavailable.
- Guided organization setup flow in the console is unavailable.

---

## Service Usage

- Only GCD APIs and services can be enabled. Private/third-party APIs created with Cloud Endpoints cannot be enabled.
- Default enabled APIs for new projects include only services available in GCD.
