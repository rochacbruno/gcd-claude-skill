# Google Cloud Dedicated (GCD) - Available Services Reference

Google Cloud Dedicated (also referred to as "GCD" or "Google Cloud Dedicated in Germany") is a
sovereign cloud offering that provides a subset of Google Cloud services in a dedicated,
regionally constrained environment. Not all Google Cloud services are available - only the
services listed below are supported.

## Available API Services

The following services have confirmed API availability in GCD:

- Access Context Manager
- API Discovery Service
- API Keys
- Artifact Registry
- BigQuery
- BigQuery Data Policy
- BigQuery Reservation
- Cloud DNS
- Cloud Key Management Service (Cloud KMS)
- Cloud Logging
- Cloud Monitoring
- Cloud SQL Admin
- Cloud Storage
- Compute Engine
- Google Kubernetes Engine (GKE)
- Identity and Access Management (IAM)
- Networking (VPC, Load Balancing, Firewall, etc.)
- Organization Policy
- Pub/Sub
- Resource Manager
- Workforce Identity Federation
- Workload Identity Federation
- Service Account Credentials
- Service Directory
- Service Usage

---

## Services by Category

### Compute

| Service | Status | Description |
|---------|--------|-------------|
| Compute Engine | Available | Scalable VMs and instance groups |
| Google Kubernetes Engine (GKE) | Available | Managed Kubernetes for containerized apps |
| Cloud Run | Available | Fully managed serverless application platform |
| Cloud GPUs | Available | GPU acceleration for ML and compute workloads |
| Container-Optimized OS | Available | Optimized OS for running Docker containers |
| Shielded VM | Available | Hardened VMs with rootkit/bootkit protection |
| Hyperdisk | Available | High-performance block storage for VMs |

**Key limitations:** Machine types, regions, and zones are constrained to the GCD environment.
Check the GCD-specific regions and zones documentation for availability.

### Networking

| Service | Status | Description |
|---------|--------|-------------|
| Virtual Private Cloud (VPC) | Available | Core network for workload connectivity |
| Cloud DNS | Available | Managed DNS with anycast name servers |
| Cloud Load Balancing | Available | Traffic distribution across backends |
| Cloud VPN | Available | IPsec tunnels to peer networks |
| Cloud Interconnect | Available | Low-latency dedicated connections |
| Cloud Router | Available | Dynamic BGP route exchange |
| Cloud NAT | Available | Outbound internet connectivity for VMs |
| Private Service Connect | Available | Private access to managed services and Google APIs |
| Network Service Tiers | Available | Connectivity optimization |
| CDN Interconnect | Available | Direct peering with Google edge network |
| Cloud Next Generation Firewall | Available | Distributed firewall with advanced protection |
| VPC Service Controls | Available | Security perimeters for GCD services |
| Google Cloud Armor | Available | DDoS and application attack protection |
| VPC Flow Logs | Available | Network flow sampling for VMs and GKE nodes |
| Packet Mirroring | Available | Traffic cloning for inspection |
| Firewall Rules Logging | Available | Audit and verify firewall rule effects |

**Key limitations:** Networking differs from standard Google Cloud. Consult the
"Differences from Google Cloud" networking section for specifics. Not all Google Cloud
networking features may be available.

### Storage

| Service | Status | Description |
|---------|--------|-------------|
| Cloud Storage | Available | Object storage with edge caching |
| Hyperdisk | Available | Scalable high-performance block storage |

**Key limitations:** Storage classes and lifecycle management may differ from standard
Google Cloud. Data residency is enforced within the GCD environment.

### Databases

| Service | Status | Description |
|---------|--------|-------------|
| Cloud SQL | Available | Managed relational databases (MySQL, PostgreSQL, SQL Server) |

**Key limitations:** Cloud SQL Admin API is the management interface. Not all Cloud SQL
features from standard Google Cloud may be supported. Spanner, Firestore, Bigtable,
and other Google Cloud database products are not available in GCD.

### Data Analytics

| Service | Status | Description |
|---------|--------|-------------|
| BigQuery | Available | Managed data warehouse with built-in ML |
| BigQuery Data Policy | Available | Data governance and access policies |
| BigQuery Reservation | Available | Capacity reservation management |
| BigQuery ML | Available | ML model training via SQL |
| BigQuery Storage | Available | Optimized storage for analytics workloads |
| BigLake | Available | Query external data with access delegation |
| Pub/Sub | Available | Event stream ingestion at scale |

**Key limitations:** Some BigQuery features (such as certain external integrations) may
not be available. Dataflow, Dataproc, Datastream, and other Google Cloud data services
are not available in GCD.

### Security and Identity

| Service | Status | Description |
|---------|--------|-------------|
| Identity and Access Management (IAM) | Available | Fine-grained access control for resources |
| Access Context Manager | Available | Attribute-based access control for projects |
| Cloud KMS | Available | Key management for secrets, disks, images |
| Cloud External Key Manager (EKM) | Available | Externally managed encryption keys |
| API Keys | Available | API key creation and management |
| VPC Service Controls | Available | Security perimeters for data protection |
| Organization Policy Service | Available | Programmatic resource governance |
| Workforce Identity Federation | Available | External identity provider federation for users |
| Workload Identity Federation | Available | External identity federation for workloads |
| Service Account Credentials | Available | Service account key and token management |
| Cloud Audit Logs | Available | Activity tracking and auditing |

**Key limitations:** Security Command Center, Binary Authorization, Certificate Authority
Service, and other advanced Google Cloud security products are not available in GCD.

### Observability

| Service | Status | Description |
|---------|--------|-------------|
| Cloud Logging | Available | Log storage, search, analysis, and alerting |
| Cloud Monitoring | Available | Performance and health monitoring |
| Managed Prometheus | Available | Prometheus-based monitoring at scale |

**Key limitations:** Cloud Trace, Cloud Profiler, and Error Reporting are not available
in GCD. Observability is limited to logging, monitoring, and Prometheus.

### Application Development and Hosting

| Service | Status | Description |
|---------|--------|-------------|
| Artifact Registry | Available | Container image and package storage |
| Cloud Run | Available | Serverless container execution |
| Google Kubernetes Engine (GKE) | Available | Container orchestration |
| Pub/Sub | Available | Event-driven messaging |
| Cloud Code | Available | IDE support for Kubernetes and Cloud Run |
| Cloud Shell | Available | Browser-based dev environment |
| Service Directory | Available | Service registry and discovery |
| Service Usage | Available | API enablement and quota management |
| API Discovery Service | Available | API metadata and discovery |

**Key limitations:** App Engine, Cloud Functions (standalone), Cloud Build, Cloud Deploy,
and other Google Cloud CI/CD products are not available in GCD. Use third-party CI/CD
tools or GKE-based pipelines instead.

### Infrastructure as Code

| Service | Status | Description |
|---------|--------|-------------|
| Terraform | Available | Infrastructure provisioning via HCL |
| Infrastructure Manager | Available | Managed Terraform deployment service |
| Config Connector | Available | Kubernetes-native GCD resource management |

**Key limitations:** Use the GCD-specific Terraform provider configuration. Not all
Terraform Google provider resources are supported - only resources corresponding to
available GCD services will work.

### Resource Management

| Service | Status | Description |
|---------|--------|-------------|
| Resource Manager | Available | Organization, folder, and project management |
| Organization Policy Service | Available | Constraint-based resource governance |
| Cloud APIs | Available | Programmatic resource management |
| Service Usage | Available | API and service lifecycle management |

---

## Notable Unavailable Services

The following commonly used Google Cloud services are NOT available in GCD:

- **AI/ML:** Vertex AI, AutoML, Vision AI, Natural Language AI, Translation AI
- **Databases:** Spanner, Firestore, Bigtable, Memorystore, AlloyDB
- **Data:** Dataflow, Dataproc, Data Fusion, Datastream, Composer
- **Serverless:** App Engine, Cloud Functions (standalone)
- **CI/CD:** Cloud Build, Cloud Deploy, Cloud Source Repositories
- **Observability:** Cloud Trace, Cloud Profiler, Error Reporting
- **Security:** Security Command Center, Binary Authorization, Certificate Authority Service
- **Messaging:** Eventarc (standalone)
- **Other:** Anthos, API Gateway, Apigee, Firebase

---

## Developer Tools and SDK Support

GCD provides client libraries for the following languages:
C#/.NET, C++, Go, Java, JavaScript/Node.js, PHP, Python, Ruby, Rust

Supported frameworks and tools: Spring, Kubernetes, Terraform, Prometheus, Pulumi,
Ansible, Crossplane, CDKTF, Google Cloud MCP servers

The Google Cloud SDK (gcloud CLI) is the primary command-line interface for managing
GCD resources. Use the GCD-specific endpoint configuration.
