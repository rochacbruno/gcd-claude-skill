# Cloud Quotas in Google Cloud Dedicated (GCD) & Cloud de Confiance (S3NS)

Cloud Quotas enables customers to monitor quota usage, create and modify quota alerts, and request limit adjustments. Quotas are managed through the Cloud Quotas dashboard in the sovereign cloud console or via the Cloud Quotas API and `gcloud` CLI.

> **S3NS SecNumCloud 3.2 Note:** On Cloud de Confiance by S3NS (`u-france-east1`), **Cloud Quotas** is currently in **`Qualification en cours`** for ANSSI SecNumCloud 3.2 qualification (see [services.md](services.md)).

## Key Differences from Public Google Cloud

In GCD and S3NS, quota increase adjustments require contacting sovereign cloud support (for S3NS: [support.s3ns.fr](https://support.s3ns.fr); for Berlin GCD: via your dedicated EU support project). You must provide:

- **Project name or number** — e.g., `eu0:my-project` (Berlin) or `s3ns:my-project` (S3NS)
- **Service name** — e.g., `compute.googleapis.com`
- **Quota name** — e.g., `CPUS-per-project-region`
- **Dimensions** — e.g., `region=u-germany-northeast1, vm_family=C3` (Berlin) or `region=u-france-east1, vm_family=C3` (S3NS)
- **Desired quota value** — e.g., `2000`
- **Justification** — explain why the increase is needed
- **Email address** — for follow-up contact

Preview features from public GCP are generally not available in GCD or S3NS unless explicitly stated.

## Types of Quotas

- **Allocation quotas**: Restrict how much of a resource the sovereign cloud allocates (e.g., number of VMs per project).
- **Rate quotas**: Restrict the rate of resource consumption over a time period (e.g., API calls per minute).
- **Concurrent quotas**: Restrict the number of operations running concurrently (e.g., long-running insert operations).

### Cloud Quotas API Rate Limits

| Quota | Value |
|-------|-------|
| Read requests per minute, per project | 1200 |
| Update requests per minute, per project | 60 |
| Quota increase requests per day, per project | 300 |

## Quota Hierarchy and Scope

Quotas apply at different levels of the resource hierarchy:

- **Project-level**: Most common. Usage in one project does not affect another.
- **Folder-level**: Child folders and projects contribute to usage.
- **Organization-level**: All child folders and projects contribute.

Quotas can also be **regional** (restricting usage in `u-germany-northeast1` or `u-france-east1`) or **zonal** (restricting usage per zone `-a`, `-b`, `-c`). Some resources have both.

## Terminology

| Term | Description |
|------|-------------|
| Quota | A resource and its unit of measurement, e.g., `CPUS-PER-VM-FAMILY-per-project-region` |
| Quota value | The maximum allowed for a given quota; adjustable for most quotas |
| System limit | A fixed architectural constraint that cannot be changed |
| Dimension | An attribute such as region, zone, `gpu_family`, or `network_id` |
| Quota preference | A `QuotaPreference` resource representing your desired quota for a dimension combination |
| Quota info | A read-only `QuotaInfo` resource providing metadata and current quota values |
| Quota adjustment | A request to increase or decrease a quota value, subject to review |

## Viewing Quotas

### Console

View quota values in the sovereign cloud console at **IAM & Admin > Quotas & System Limits**:
- **Berlin (GCD):** `https://console.cloud.berlin-build0.goog/iam-admin/quotas`
- **France (S3NS):** `https://console.cloud.s3nscloud.fr/iam-admin/quotas`

You can also view API-specific quotas from **APIs & Services > [API name] > Quotas & System Limits**.

Current usage is calculated as follows:
- Per-minute rate quotas: average per-minute usage over the past 10 minutes
- Per-day rate quotas: total usage so far in the current day (Pacific Time)
- Allocation quotas: the most recent value (e.g., number of load balancers in use)
- Concurrent quotas: the most recent value of in-flight operations

### gcloud CLI

List quota information for a service:

```bash
gcloud beta quotas info list \
  --service=SERVICE_NAME \
  --project=PROJECT_ID_OR_NUMBER \
  --billing-project=BILLING_PROJECT_ID_OR_NUMBER
```

View details for a specific quota:

```bash
gcloud beta quotas info describe QUOTA_ID \
  --service=SERVICE_NAME \
  --project=PROJECT_ID_OR_NUMBER \
  --billing-project=BILLING_PROJECT_ID_OR_NUMBER
```

View quota info for an organization:

```bash
gcloud beta quotas info list \
  --service=SERVICE_NAME \
  --organization=ORGANIZATION_ID \
  --billing-project=BILLING_PROJECT_ID_OR_NUMBER
```

Get metric names for a service:

```bash
gcloud beta quotas info list \
  --project=PROJECT_ID_OR_NUMBER \
  --service=SERVICE_NAME \
  --format="value(metric)"
```

## Managing Quotas

### Requesting a Quota Increase

In GCD and S3NS, quota increases above the default require filing a support request. From the console:

1. Go to **IAM & Admin > Quotas & System Limits**.
2. Find and select the quota to update.
3. Enter the desired new value.
4. Gather the required details (project, service, quota name, dimensions, desired value, justification, email).
5. File a support request with your sovereign cloud operator (for S3NS: `support.s3ns.fr`; for Berlin GCD: via your EU support project).

Batch requests by product area to reduce review time.

### Quota Overrides (Decreases)

To restrict usage below the default, create a quota override by setting the value lower than the default. This is sometimes called "capping usage." To reset an override, set the value back to the default.

Quota decrease adjustments can be made at project, organization, and folder levels.

### gcloud CLI - Quota Preferences

Check existing preferences:

```bash
gcloud beta quotas preferences list \
  --project=PROJECT_ID_OR_NUMBER \
  --billing-project=BILLING_PROJECT_ID_OR_NUMBER
```

Check preferences with pending adjustments:

```bash
gcloud beta quotas preferences list \
  --project=PROJECT_ID_OR_NUMBER \
  --reconciling-only=true \
  --billing-project=BILLING_PROJECT_ID_OR_NUMBER
```

Create a new quota preference (request adjustment):

```bash
gcloud beta quotas preferences create \
  --project=PROJECT_ID_OR_NUMBER \
  --service=SERVICE_NAME \
  --quota-id=QUOTA_ID \
  --dimensions=DIMENSIONS \
  --preferred-value=PREFERRED_VALUE \
  --billing-project=BILLING_PROJECT_ID_OR_NUMBER \
  --email=EMAIL \
  --justification=JUSTIFICATION \
  --preference-id=PREFERENCE_ID
```

Update an existing preference:

```bash
gcloud beta quotas preferences update PREFERENCE_ID \
  --preferred-value=PREFERRED_VALUE \
  --quota-id=QUOTA_ID \
  --service=SERVICE_NAME \
  --project=PROJECT_ID_OR_NUMBER \
  --billing-project=BILLING_PROJECT_ID_OR_NUMBER \
  --email=EMAIL \
  --justification=JUSTIFICATION
```

View a specific preference:

```bash
gcloud beta quotas preferences describe PREFERENCE_ID \
  --project=PROJECT_ID_OR_NUMBER \
  --billing-project=BILLING_PROJECT_ID_OR_NUMBER
```

## The Quota Project Concept

Every request to a sovereign cloud API is counted against a quota, and quotas are enforced by project. The "quota project" determines which project's quota is consumed.

**Note for gcloud CLI users**: The quota project is sometimes called the "billing project" because the `--billing-project` flag controls it.

### How the Quota Project Is Determined

- **Resource-based APIs**: The project containing the resource provides the quota. You cannot change this.
- **Client-based APIs**: The quota project is resolved in this order of precedence:
  1. Explicitly specified in the request
  2. API key's associated project
  3. gcloud CLI shared project (from user credentials)
  4. Service account's associated project
  5. Workforce identity federation user project

If none of these apply, the request fails.

### Setting the Quota Project

- **gcloud CLI**: Use `--billing-project` flag or set `billing/quota_project` in config.
- **Client libraries**: Set via client options or the `GOOGLE_CLOUD_QUOTA_PROJECT` environment variable (for most languages; C++ uses `GOOGLE_CLOUD_CPP_USER_PROJECT`; Ruby does not support it).
- **REST API**: Use the `x-goog-user-project` header.

Required permission: `serviceusage.services.use` (included in the `roles/serviceusage.serviceUsageConsumer` role).

## Monitoring and Alerting

### Querying Quota Metrics

In GCD and S3NS, native Cloud Monitoring custom dashboards and alerting UI are not available — metrics are queried using **PromQL** or exported via the Prometheus API to self-hosted Grafana (see [product-differences.md](product-differences.md)).

Consumer quota metrics (`serviceruntime.googleapis.com/quota/allocation/usage`, `serviceruntime.googleapis.com/quota/rate/net_usage`, `serviceruntime.googleapis.com/quota/limit`) are available for supported sovereign cloud services such as Compute Engine, Pub/Sub, Cloud Monitoring, and Cloud Logging. Services like Cloud SQL do not emit `serviceruntime` consumer quota metrics.

## Permissions

### Viewing Quotas

Required IAM permissions:
- `resourcemanager.projects.get` (plus `.folders.get` or `.organizations.get` for those levels)
- `monitoring.timeSeries.list`
- `serviceusage.services.list`
- `cloudquotas.quotas.get`

Predefined role: **Quota Viewer** (`roles/servicemanagement.quotaViewer`)

### Changing Quotas

Required IAM permissions:
- `serviceusage.quotas.update`
- `cloudquotas.quotas.update`

Predefined role: **Quota Administrator** (`roles/servicemanagement.quotaAdmin`). Also included in Owner, Editor, and Service Usage Admin roles.

### Viewing Quota Increase Requests

Required permissions: `resourcemanager.projects.get`, `serviceusage.services.list`, `serviceusage.quotas.get`

## Troubleshooting

### Quota Exceeded Errors

Error responses when quota is exceeded:
- API request: HTTP `413 REQUEST ENTITY TOO LARGE`
- HTTP/REST request: HTTP `429 TOO MANY REQUESTS`
- Compute Engine: HTTP `403 QUOTA_EXCEEDED` (or `403 RATE_LIMIT_EXCEEDED` for rate quotas)
- gRPC: `ResourceExhausted` error
- gcloud CLI: quota-exceeded error message with exit code `1`

For **allocation quotas**, free up quota by deleting unused resources. For **rate quotas**, wait for the time period to reset (midnight Pacific for daily, rolling window for per-minute).

### gcloud CLI Errors

**Permission denied on quota project**: Add `--billing-project` to your command, or run:
```bash
gcloud config set billing/quota_project CURRENT_PROJECT
```

**Invalid choice for quotas command**: Update the gcloud CLI:
```bash
gcloud components update
```

**Beta component not installed**: Install it:
```bash
gcloud components install beta
```

### API Error Messages

Common errors when the quota project is not set correctly:
- `User credentials not supported by this API`
- `API not enabled in the project`
- `No quota project set`

Fix these by setting the quota project correctly.

## Known Issues

- **Quota values during rollouts**: When the sovereign cloud operator changes default quota values, the rollout is gradual. The console may not reflect the new value until the rollout completes. An informational banner and rolling update indicator appear during rollouts.
- **contactEmail field required**: When updating `QuotaPreference` via the API, the `contactEmail` field is required and cannot be a group email.
- **Console cannot adjust quotas with no prior usage**: Use the gcloud CLI or REST API instead to request adjustments for quotas that have no prior usage.
- **Per-user quota usage not displayed**: The sovereign cloud console does not show per-user quota usage.
