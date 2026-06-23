# Terraform on Google Cloud Dedicated (GCD)

## Overview

Terraform is the primary Infrastructure as Code (IaC) tool for provisioning and managing GCD infrastructure. GCD uses the standard HashiCorp Google Cloud Terraform providers (`google` and `google-beta`), but requires GCD-specific provider configuration to target the correct API endpoints.

## Key Differences from Standard Google Cloud Terraform

The following features are **not available** in GCD:

- `gcloud terraform vet` (policy validation) - use [Terraform checks](https://developer.hashicorp.com/terraform/language/checks) instead
- `gcloud beta resource-config bulk-export` (export to Terraform format) - use HashiCorp's [Generating Configuration](https://developer.hashicorp.com/terraform/language/import/generating-configuration) instead
- Preview features are generally not available unless explicitly stated

Everything else in the Google Cloud Terraform provider works the same way, but you must configure the provider to point at the GCD universe endpoints.

## Provider Configuration

The critical GCD-specific setting is `universe_domain`. Without it, Terraform will attempt to reach standard Google Cloud endpoints and fail.

### Basic Provider Setup

Create a `providers.tf` file:

```hcl
provider "google" {
  universe_domain = "apis-berlin-build0.goog"
}

provider "google-beta" {
  universe_domain = "apis-berlin-build0.goog"
}
```

### Provider with Project and Region

```hcl
provider "google" {
  universe_domain = "apis-berlin-build0.goog"
  project         = "PROJECT_ID"
  region          = "u-germany-northeast1"
  zone            = "u-germany-northeast1-a"
}
```

### Setting the Project via Environment Variable

Instead of hardcoding the project in the provider block, you can export it:

```bash
export GOOGLE_CLOUD_PROJECT=PROJECT_ID
```

Most resources can infer `project_id` from this variable. Some resources (such as `project_iam_*`) cannot infer the project ID - use the `data "google_project"` data source or pass the project ID explicitly for those.

## Authentication

GCD uses Application Default Credentials (ADC), the same mechanism as Google Cloud. The recommended approaches, in order of preference:

### 1. User Account (local development)

```bash
gcloud init
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
  universe_domain            = "apis-berlin-build0.goog"
  impersonate_service_account = "SERVICE_ACCT_EMAIL"
}
```

### 3. Attached Service Account (running on GCD)

When running Terraform on GCD infrastructure (e.g., Compute Engine), attach a user-managed service account to the resource. The code running on that resource automatically uses the service account identity.

### 4. Workload Identity Federation (external environments)

For running Terraform from on-premises or another cloud provider, configure Workload Identity Federation and set `GOOGLE_APPLICATION_CREDENTIALS` to point to the credential configuration file.

### 5. Service Account Keys (least preferred)

Create a service account key and make it available to ADC. This is the least secure option.

### GCD-Specific IAM Note

Service account email addresses in GCD use the `eu0` prefix:

```
SERVICE_ACCOUNT_NAME@PROJECT_ID.eu0.iam.gserviceaccount.com
```

## State Storage

### Local State (default)

By default, Terraform stores state in a local `terraform.tfstate` file. This is suitable only for individual use.

### Remote State in Cloud Storage (recommended for teams)

Store state in a GCS bucket for team collaboration and state locking. When using GCD, you must configure the `storage_custom_endpoint` to point to the GCD storage API.

#### Step 1: Create the storage bucket

```hcl
resource "random_id" "default" {
  byte_length = 8
}

resource "google_storage_bucket" "default" {
  name     = "${random_id.default.hex}-terraform-remote-backend"
  location = "u-germany-northeast1"

  force_destroy               = false
  public_access_prevention    = "enforced"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}
```

#### Step 2: Configure the backend

Create a `backend.tf` file (or generate it via a `local_file` resource):

```hcl
terraform {
  backend "gcs" {
    bucket = "BUCKET_NAME"
  }
}
```

When using GCD, update the backend configuration to redirect `storage_custom_endpoint` to the GCD universe endpoint.

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

GCD supports the standard `google` and `google-beta` providers from the [Terraform Registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs). Resources correspond to the GCD services that are available:

- **Compute:** `google_compute_instance`, `google_compute_network`, `google_compute_firewall`, etc.
- **Storage:** `google_storage_bucket`, `google_storage_bucket_object`, etc.
- **GKE:** `google_container_cluster`, `google_container_node_pool`, etc.
- **Cloud SQL:** `google_sql_database_instance`, `google_sql_database`, etc.
- **BigQuery:** `google_bigquery_dataset`, `google_bigquery_table`, etc.
- **IAM:** `google_project_iam_*`, `google_service_account`, etc.
- **Networking:** `google_compute_subnetwork`, `google_dns_managed_zone`, `google_compute_router`, etc.
- **KMS:** `google_kms_key_ring`, `google_kms_crypto_key`, etc.
- **Pub/Sub:** `google_pubsub_topic`, `google_pubsub_subscription`, etc.
- **Logging/Monitoring:** `google_logging_*`, `google_monitoring_*`, etc.

Resources for services that are not available in GCD will fail at apply time.

## Practical Example: Create a VM Instance

### Prerequisites

```bash
# Create a project
gcloud projects create PROJECT_ID

# Select the project
gcloud config set project PROJECT_ID

# Enable the Compute Engine API
gcloud services enable compute.googleapis.com

# Grant the required role
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:USER_IDENTIFIER" \
  --role=roles/compute.instanceAdmin.v1
```

### main.tf

```hcl
provider "google" {
  universe_domain = "apis-berlin-build0.goog"
  project         = "PROJECT_ID"
  region          = "u-germany-northeast1"
  zone            = "u-germany-northeast1-a"
}

resource "google_compute_instance" "default" {
  name         = "my-vm"
  machine_type = "n1-standard-1"
  zone         = "u-germany-northeast1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-minimal-2210-kinetic-amd64-v20230126"
    }
  }

  network_interface {
    network = "default"
    access_config {}
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

## Other IaC Options on GCD

While Terraform is the primary recommendation, GCD also supports:

- **Terraform Cloud / Terraform Enterprise** - for organization-wide change management
- **CDKTF (Cloud Development Kit for Terraform)** - define infrastructure using TypeScript, Python, Go, C#, or Java instead of HCL
- **Pulumi** - provision infrastructure using general-purpose programming languages
- **Crossplane** - manage GCD resources through Kubernetes
- **Ansible** - automate provisioning and configuration management
