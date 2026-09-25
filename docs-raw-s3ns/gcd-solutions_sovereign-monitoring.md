# Open-source software (OSS)-based monitoring

Source: https://documentation.s3ns.fr/docs/gcd-solutions/sovereign-monitoring
Last updated: 2026-09-24

- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Documentation

](https://documentation.s3ns.fr/docs)






- 








[

Get started

](https://documentation.s3ns.fr/docs/get-started)












# Open-source software (OSS)-based monitoring 






- On this page 
- [ Target audience ](#target-audience)
- [ Core capabilities ](#core-capabilities)
- [ Architecture ](#architecture)
- [ Components ](#components)
- [ Reference implementation ](#reference_implementation)
- 









Regulated industries like finance and healthcare need to monitor critical
infrastructure while keeping data strictly within regional boundaries.

Open-source software (OSS) can complement and extend the Cloud Monitoring and
Cloud Logging features currently available in Cloud de Confiance by S3NS. This example
shows you how to create a complete sovereign observability solution on
Cloud de Confiance by S3NS by adding widely used open source tools.

The architecture uses OpenTelemetry, Grafana Mimir (backed by Cloud Storage),
Grafana, and Fluent Bit to generate metrics, logs, visualizations, and alerts
for Google Kubernetes Engine (GKE) and Compute Engine. All data stays within the
sovereign region, and avoids third-party SaaS fees.

We recommend that you subscribe to the relevant [release notes](/release-notes)
for future updates to the Cloud de Confiance by S3NS observability capabilities.

You can deploy this solution by following the accompanying
[reference implementation](#reference_implementation) with Terraform.

## Target audience

This solution is for companies that need to monitor workloads in sovereign
Cloud de Confiance by S3NS environments. It serves the following stakeholders:

- **Site reliability engineers (SREs) and DevOps leaders** who provision
automated, scalable metrics storage and log pipelines to monitor application
health and track system service level agreements (SLAs) without manual
exporter maintenance.

- **Compliance and security officers** who ensure that sensitive
application logs, metrics, and operational signals remain localized within
sovereign boundary and avoid non-sovereign SaaS data outflow.

- **Enterprise cloud architects** who establish a standardized OpenTelemetry
foundation that unblocks immediate cloud migrations and provides a smooth
transition path to first-party cloud monitoring.

## Core capabilities

- **Sovereign observability and local data retention**: Collect, process,
and store application metrics for Compute Engine and GKE
logs within the local sovereign infrastructure using Cloud Storage
buckets.

- **OpenTelemetry standard ingestion**: Use OpenTelemetry collectors for
pull-based Prometheus scraping and push-based OpenTelemetry Protocol (OTLP)
metrics ingestion. This approach supports future compatibility with
first-party cloud monitoring.

- **Scalable Cloud Storage-backed metric storage**: Configure Grafana
Mimir to use Cloud Storage as a highly available, cost-effective
Prometheus metric block backend.

- **Unified telemetry visualization**: View pre-configured Grafana dashboards
that display real-time application metrics, Compute Engine VM stdout
logs, and integrate Cloud Logging datasources.

- **Compute Engine VM logging pipeline**: Install Fluent Bit and
OpenTelemetry Collector Contrib automatically on Compute Engine VMs
to stream `systemd-journald` and stdout logs to Cloud Logging.

- **Flexible deployment automation**: Use an Infrastructure as Code (IaC)
approach of Terraform and Kubernetes package management with Helm for
consistent environment setup and teardown.

## Architecture

This architecture uses OpenTelemetry collectors, Grafana Mimir, Grafana, and
Fluent Bit to monitor Compute Engine and GKE workloads with
Cloud Storage for metrics and Cloud Logging for logs.



## Components



| 
Component | 
Tech | 
Purpose | 
|




| 
**Telemetry
collector**

| 
OpenTelemetry
collector

| 
Central telemetry pipeline to
process OpenTelemetry Protocol
(OTLP) HTTP/gRPC metrics, scrape
Prometheus endpoints, and forward
to Mimir. | 
|

| 
**Metrics
database**

| 
Grafana Mimir

| 
Highly available, long-term
Prometheus metric storage
database with persistent blocks
in Cloud Storage. | 
|

| 
**Object
storage**
| 
Cloud Storage

| 
Secure, durable object storage
backend that retains Mimir metric
blocks cost-effectively. | 
|

| 
**VM log
collector**

| 
Fluent Bit and
OpenTelemetry Contrib

| 
Collects OS and application
stdout logs on standalone
Compute Engine VMs using
`systemd-journald` and streams to
Cloud Logging. | 
|

| 
**Central
logging**
| 
Cloud Logging

| 
Centralized logging sink for
Compute Engine VM and
platform logs. | 
|

| 
**Visualization
and alerting**

| 
Grafana

| 
Dashboard visualization layer
pre-configured with datasources
for Mimir, Cloud Monitoring,
and Cloud Logging. | 
|

| 
**Push demo
app**

| 
Python (beacon app)

| 
Demo microservice that emits
synthetic OTLP metrics pushed to
OpenTelemetry collector every 5
seconds. | 
|

| 
**Pull demo
app**

| 
Python (sensor app)

| 
Demo microservice to expose a
standard `/metrics` Prometheus
endpoint scraped by
OpenTelemetry collector. | 
|

| 
**Demo app**

| 
Python

| 
Demo application running on
Compute Engine VMs to
produce structured JSON logs to
stdout. | 
|

| 
**Deployment**

| 
Terraform and Helm

| 
Automates
Virtual Private Cloud (VPC),
GKE cluster,
Cloud Storage bucket,
Identity and Access Management (IAM) roles,
Compute Engine VM, and
Helm chart deployment. | 
|



## Reference implementation

A reference implementation of this solution with Terraform is provided in
GitHub. Note that this is a proof-of-concept prototype built for demonstration
purposes, and the implementation is not audited or secured for production use
cases.

For prerequisites and deployment instructions, see
[Sovereign observability and monitoring with Grafana and OpenTelemetry](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/solutions/monitoring/).