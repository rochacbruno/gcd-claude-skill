# Terraform on Google Cloud Dedicated (GCD) & Cloud de Confiance (S3NS)

## Overview

Terraform is the primary Infrastructure as Code (IaC) tool for provisioning and managing infrastructure in Google Cloud Dedicated (GCD Berlin) and Cloud de Confiance (S3NS France). Sovereign cloud environments use the standard HashiCorp Google Cloud Terraform providers (`google` and `google-beta`), but require universe-specific provider configuration (`universe_domain`) to target the correct API endpoints.

## Key Differences from Standard Google Cloud Terraform

The following features are **not available** in GCD or S3NS:

- `gcloud terraform vet` (policy validation) — use [Terraform checks](https://developer.hashicorp.com/terraform/language/checks) instead
- `gcloud beta resource-config bulk-export` (export to Terraform format) — use HashiCorp's [Generating Configuration](https://developer.hashicorp.com/terraform/language/import/generating-configuration) instead
- **Bigtable** Terraform resources (`google_bigtable_*`) — Bigtable in sovereign cloud does **not** support provisioning via Terraform; manage Bigtable instances, clusters, and tables via the `gcloud` CLI, `cbt` CLI, Cloud Client Libraries, or the console
- Preview features are generally not available unless explicitly stated

Everything else in the Google Cloud Terraform provider works the same way, provided you configure the provider to point at the sovereign cloud universe endpoints.

## Provider Configuration

The critical sovereign cloud setting is `universe_domain`. Without it, Terraform will attempt to reach public Google Cloud endpoints (`googleapis.com`) and fail.

| Setting | Berlin (GCD — Germany) | France (S3NS — Cloud de Confiance) |
|---|---|---|
| `universe_domain` | `"apis-berlin-build0.goog"` | `"s3nsapis.fr"` |
| `region` | `"u-germany-northeast1"` | `"u-france-east1"` |
| `zone` | `"u-germany-northeast1-a"` (`a`, `b`, `c`) | `"u-france-east1-a"` (`a`, `b`, `c`) |
| Project ID format | `"eu0:PROJECT_ID"` | `"s3ns:PROJECT_ID"` |
| GCS backend `storage_custom_endpoint` | `"https://storage.apis-berlin-build0.goog/storage/v1/"` | `"https://storage.s3nsapis.fr/storage/v1/"` |

### Basic Provider Setup

Create a `providers.tf` file:

**Berlin (GCD):**

```hcl
provider "google" {
  universe_domain = "apis-berlin-build0.goog"
}

provider "google-beta" {
  universe_domain = "apis-berlin-build0.goog"
}
```

**France (S3NS):**

```hcl
provider "google" {
  universe_domain = "s3nsapis.fr"
}

provider "google-beta" {
  universe_domain = "s3nsapis.fr"
}
```

### Provider with Project and Region

**Berlin (GCD):**

```hcl
provider "google" {
  universe_domain = "apis-berlin-build0.goog"
  project         = "eu0:PROJECT_ID"
  region          = "u-germany-northeast1"
  zone            = "u-germany-northeast1-a"
}
```

**France (S3NS):**

```hcl
provider "google" {
  universe_domain = "s3nsapis.fr"
  project         = "s3ns:PROJECT_ID"
  region          = "u-france-east1"
  zone            = "u-france-east1-a"
}
```

### Setting the Project via Environment Variable

Instead of hardcoding the project in the provider block, you can export it:

```bash
# Berlin (GCD)
export GOOGLE_CLOUD_PROJECT="eu0:PROJECT_ID"

# France (S3NS)
export GOOGLE_CLOUD_PROJECT="s3ns:PROJECT_ID"
```

Most resources can infer `project_id` from this variable. Some resources (such as `project_iam_*`) cannot infer the project ID — use the `data "google_project"` data source or pass the project ID explicitly for those.

## Authentication

GCD and S3NS use Application Default Credentials (ADC), the same mechanism as Google Cloud. The recommended approaches, in order of preference:

### 1. User Account (local development)

```bash
gcloud auth login
gcloud auth application-default login
```

### 2. Service Account Impersonation (local development)

Requires the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) on the target service account.

```bash
gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL
```

Or in the provider block:

```hcl
provider "google" {
  universe_domain             = "s3nsapis.fr" # or "apis-berlin-build0.goog"
  impersonate_service_account = "SERVICE_ACCT_EMAIL"
}
```

### 3. Attached Service Account (running on GCD / S3NS)

When running Terraform on sovereign cloud infrastructure (e.g., Compute Engine), attach a user-managed service account to the resource. The code running on that resource automatically uses the service account identity.

### 4. Workload Identity Federation (external environments)

For running Terraform from on-premises or another cloud provider, configure Workload Identity Federation and set `GOOGLE_APPLICATION_CREDENTIALS` to point to the credential configuration file.

### 5. Service Account Keys (least preferred)

Create a service account key and make it available to ADC. This is the least secure option.

### Sovereign Cloud IAM Note

Service account email addresses use the universe prefix (`eu0` for Berlin, `s3ns` for S3NS) in the domain, while omitting the `eu0:` / `s3ns:` prefix from the project name portion:

```text
# Berlin (GCD)
SERVICE_ACCOUNT_NAME@PROJECT_ID.eu0.iam.gserviceaccount.com

# France (S3NS)
SERVICE_ACCOUNT_NAME@PROJECT_ID.s3ns.iam.gserviceaccount.com
```

## State Storage

### Local State (default)

By default, Terraform stores state in a local `terraform.tfstate` file. This is suitable only for individual use.

### Remote State in Cloud Storage (recommended for teams)

Store state in a GCS bucket for team collaboration and state locking. When using GCD or S3NS, you **must** configure `storage_custom_endpoint` in the `backend "gcs"` block to point to the sovereign cloud storage API.

#### Step 1: Create the storage bucket

```hcl
resource "random_id" "default" {
  byte_length = 8
}

resource "google_storage_bucket" "default" {
  name     = "${random_id.default.hex}-terraform-remote-backend"
  location = "u-france-east1" # or "u-germany-northeast1" for Berlin

  force_destroy               = false
  public_access_prevention    = "enforced"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}
```

#### Step 2: Configure the backend

Create a `backend.tf` file with `storage_custom_endpoint` targeting your sovereign cloud universe:

**Berlin (GCD):**

```hcl
terraform {
  backend "gcs" {
    bucket                  = "BUCKET_NAME"
    prefix                  = "terraform/state"
    storage_custom_endpoint = "https://storage.apis-berlin-build0.goog/storage/v1/"
  }
}
```

**France (S3NS):**

```hcl
terraform {
  backend "gcs" {
    bucket                  = "BUCKET_NAME"
    prefix                  = "terraform/state"
    storage_custom_endpoint = "https://storage.s3nsapis.fr/storage/v1/"
  }
}
```

#### Step 3: Migrate state

```bash
terraform init -migrate-state
```

When prompted, enter `yes` to move the local state into the Cloud Storage bucket.

#### Required IAM Permissions for State Bucket

Grant `roles/storage.admin` to the user or service account managing state, or create a custom role with:

- `storage.buckets.create`
- `storage.buckets.list`
- `storage.objects.get`
- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.update`

Best practice: limit admin access to a small set of administrators. Other developers should only have read/write permissions on objects.

## Available Terraform Resources

GCD and S3NS support the standard `google` and `google-beta` providers from the [Terraform Registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs). Resources correspond to the sovereign cloud services that are available:

- **Compute:** `google_compute_instance` (`c3-*`, `m3-*`, `a3-*`), `google_compute_disk` (`hyperdisk-balanced`), `google_compute_region_instance_group_manager`, etc.
- **GKE (Autopilot only):** `google_container_cluster` (`enable_autopilot = true`).
- **Cloud Run:** `google_cloud_run_v2_service`, `google_cloud_run_v2_job`.
- **Storage & File:** `google_storage_bucket`, `google_storage_bucket_object`, `google_filestore_instance` (`tier = "REGIONAL"`), `google_storage_transfer_job`.
- **Databases:** `google_sql_database_instance` (MySQL / PostgreSQL `ENTERPRISE_PLUS` on `db-perf-optimized-N-*`), `google_sql_database`. *(Note: **Bigtable** does **not** support Terraform in sovereign cloud.)*
- **Data & Analytics:** `google_bigquery_dataset`, `google_bigquery_table`, `google_bigquery_capacity_commitment`, `google_bigquery_reservation`, `google_dataproc_cluster` (Compute Engine clusters on image `2.3+`), `google_composer_environment` (Composer 3, Highly Resilient, Large/Custom), `google_pubsub_topic`, `google_pubsub_subscription`.
- **Containers & Packages:** `google_artifact_registry_repository` (`DOCKER`, `APT`, `YUM`).
- **Security & Identity:** `google_project_iam_*`, `google_service_account`, `google_kms_key_ring`, `google_kms_crypto_key`, `google_secret_manager_secret`, `google_secret_manager_regional_secret`, `google_access_context_manager_*`, `google_org_policy_policy`.
- **Networking:** `google_compute_network`, `google_compute_subnetwork`, `google_compute_firewall`, `google_compute_network_firewall_policy`, `google_dns_managed_zone` (`visibility = "private"`), `google_compute_router`, `google_compute_router_nat`, `google_compute_ha_vpn_gateway`, `google_compute_region_security_policy` (Cloud Armor).
- **Observability:** `google_logging_project_bucket_config`, `google_logging_project_sink`.

Resources for services that are not available in GCD/S3NS (or Bigtable resources) will fail at apply time.

## Practical Example: Create a VPC and VM Instance

Because sovereign cloud projects do **not** automatically create a `default` VPC network and only support modern VM series (`c3`, `m3`, `a3`), Hyperdisk (`hyperdisk-balanced`), and sovereign-prefixed OS images (`eu0-system:` / `s3ns-system:`), always define the VPC, subnet, Hyperdisk boot disk, and sovereign OS image explicitly.

### Prerequisites

```bash
# Select the project (use eu0:PROJECT_ID on Berlin or s3ns:PROJECT_ID on S3NS)
gcloud config set project s3ns:PROJECT_ID

# Enable the Compute Engine API
gcloud services enable compute.googleapis.com

# Grant the required role
gcloud projects add-iam-policy-binding s3ns:PROJECT_ID \
  --member="user:USER_IDENTIFIER" \
  --role=roles/compute.instanceAdmin.v1
```

### main.tf

```hcl
variable "universe_domain" {
  description = "Sovereign cloud universe domain (s3nsapis.fr or apis-berlin-build0.goog)"
  type        = string
  default     = "s3nsapis.fr"
}

variable "universe_prefix" {
  description = "Universe prefix (s3ns or eu0)"
  type        = string
  default     = "s3ns"
}

variable "project_id" {
  description = "Project ID with universe prefix (e.g. s3ns:my-project or eu0:my-project)"
  type        = string
}

variable "region" {
  description = "Sovereign cloud region (u-france-east1 or u-germany-northeast1)"
  type        = string
  default     = "u-france-east1"
}

provider "google" {
  universe_domain = var.universe_domain
  project         = var.project_id
  region          = var.region
  zone            = "${var.region}-a"
}

resource "google_compute_network" "vpc" {
  name                    = "main-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name                     = "main-subnet"
  ip_cidr_range            = "10.0.1.0/24"
  region                   = var.region
  network                  = google_compute_network.vpc.id
  private_ip_google_access = true
}

resource "google_compute_instance" "default" {
  name         = "my-vm"
  machine_type = "c3-standard-4"
  zone         = "${var.region}-a"

  boot_disk {
    initialize_params {
      image = "${var.universe_prefix}-system:debian-cloud/debian-12"
      type  = "hyperdisk-balanced"
      size  = 50
    }
  }

  network_interface {
    network    = google_compute_network.vpc.id
    subnetwork = google_compute_subnetwork.subnet.id
  }
}
```

### Apply

```bash
terraform init
terraform plan
terraform apply
```

### Connect to the VM

```bash
# France (S3NS)
gcloud compute ssh --zone=u-france-east1-a my-vm

# Berlin (GCD)
gcloud compute ssh --zone=u-germany-northeast1-a my-vm
```

### Tear Down

```bash
terraform destroy
```

## Basic Terraform Commands Reference

| Command | Purpose |
|---|---|
| `terraform init` | Initialize working directory, download providers |
| `terraform init -upgrade` | Re-initialize and upgrade to latest provider version |
| `terraform plan` | Preview changes without applying |
| `terraform apply` | Apply configuration changes |
| `terraform destroy` | Remove all managed resources |
| `terraform fmt` | Reformat configuration to standard style |
| `terraform validate` | Check configuration syntax and validity |
| `terraform init -migrate-state` | Migrate state between backends |

## Other IaC Options on GCD & S3NS

While Terraform is the primary recommendation, sovereign cloud deployments also support:

- **Terraform Cloud / Terraform Enterprise** — for organization-wide change management
- **CDKTF (Cloud Development Kit for Terraform)** — define infrastructure using TypeScript, Python, Go, C#, or Java instead of HCL
- **Pulumi** — provision infrastructure using general-purpose programming languages
- **Crossplane** — manage sovereign cloud resources through Kubernetes
- **Ansible** — automate provisioning and configuration management
