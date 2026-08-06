# Tax anomaly detection with BigQuery ML and Gemma

Source: https://documentation.s3ns.fr/docs/gcd-solutions/tax-enforcement
Last updated: 2026-08-05

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












# Tax anomaly detection with Big Query ML and Gemma 






- On this page 
- [ Target audience ](#target_audience)
- [ Core capabilities ](#core_capabilities)
- [ Architecture ](#architecture)
- [ Components ](#components)
- [ Reference implementation ](#reference_implementation)
- 









In the public financial sector, the
ability to detect fraud while keeping data strictly in-country can be a
mission-critical requirement.

This solution provides a blueprint for addressing this challenge with Cloud de Confiance by S3NS. Agencies can
deploy BigQuery ML on Cloud de Confiance by S3NS to analyze millions of tax declarations and identify
high-risk anomalies in real time. Simultaneously, a local, open-weight Gemma RAG
system uses vector search to map those anomalies directly to tax policies. This
ensures context-aware compliance and full auditability, without making
external API calls or moving data outside the sovereign boundary.

You can deploy this solution by following the accompanying [reference implementation](#reference_implementation) with Terraform.

## Target audience 

This solution is designed for national tax authorities or regulated financial
agencies. It serves the following stakeholders:

- **Auditors & tax investigators** who review real-time dashboards to investigate
flagged anomalies and use the grounded Gemma AI assistant to generate
traceable case summaries.

- **Compliance officers** who centrally manage the system's legal knowledge base
by uploading and indexing official tax policy documents within a secure,
local interface.

- **Data scientists** who securely access raw data using GKE-hosted Jupyter
environments to iteratively train, validate, and redeploy anomaly
detection models.

## Core capabilities

- **Sovereign anomaly detection**: Use BigQuery ML to screen
massive datasets and flag high-risk anomalies instantly, ensuring data never
leaves the sovereign boundary.

- **Retrieval-Augmented Generation (RAG)**: Run semantic vector searches
across internal policy libraries to provide grounded, context-aware insights
using the open-weight Gemma LLM.

- **Localized AI assistance**: Generate summaries of policy violations through
an AI assistant running entirely within the regional perimeter.

- **Dynamic knowledge management**: Maintain an up-to-date compliance
database by indexing official regulations as vector embeddings for immediate
use in RAG pipelines.

- **Dynamic internationalization**: Instantly switch UI language between
English, French, and German without reloads or restarts.

## Architecture

This architecture leverages BigQuery ML and a RAG pipeline with Gemma LLM
to deliver secure, context-aware tax anomaly detection.



## Components

The following technologies and Cloud de Confiance by S3NS services are used in this solution:



| 
Component | 
Tech | 
Purpose | 
|




| 
**Data** | 
Python | 
Generate tax data (TRAINING/NEW_FILING). | 
|

| 
**Model** | 
[BigQuery ML](/bigquery/docs/bqml-introduction) | 
Logistic Regression for anomaly detection. | 
|

| 
**LLM** | 
Gemma | 
Open-weight model providing context-aware insights grounded in official tax policy. | 
|

| 
**RAG** | 
[BigQuery](/bigquery/docs) | 
Vector search for semantic matching and RAG grounding. | 
|

| 
**Container infrastructure** | 
[GKE](/kubernetes-engine/docs) | 
Container infrastructure for the tax office application and JupyterHub server. | 
|

| 
**Analysis** | 
Jupyter | 
Notebook for ML model training and analysis/validation. | 
|

| 
**App** | 
Flask | 
Web app for prediction visualization. | 
|



## Reference implementation

A reference implementation of this solution with Terraform is provided in
GitHub. Note that this is a proof-of-concept prototype built for demonstration
purposes, and the implementation is not audited or secured for production use
cases.

For prerequisites and deployment instructions, see [Sovereign Tax Anomaly Detection with BigQuery ML and Gemma](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/demos/tax-office).