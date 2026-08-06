# Health insurance risk analysis with BigQuery ML and Gemma

Source: https://berlin.devsitetest.how/docs/gcd-solutions/health-insurance
Last updated: 2026-08-05

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












# Health insurance risk analysis with Big Query ML and Gemma 






- On this page 
- [ Target audience ](#target_audience)
- [ Core capabilities ](#core_capabilities)
- [ Architecture ](#architecture)
- [ Components ](#components)
- [ Reference implementation ](#reference_implementation)
- 









In highly regulated environments such as the healthcare and insurance sectors,
providers often need to perform tasks like analyzing health risks and verifying customer claims, while keeping
data strictly within the relevant jurisdiction.

The solution described in this document provides a blueprint for solving these challenges with Google Cloud Dedicated in Germany. Insurance
providers can deploy BigQuery ML on Google Cloud Dedicated in Germany to analyze health risk scores, model
plans, and claims databases in real time. Simultaneously, a local, open-weight
Gemma LLM system performs verification on claim documentation stored in Cloud Storage.
This approach ensures context-aware compliance and full auditability, without ever
making external API calls or moving data outside the sovereign boundary.

You can deploy this solution by following the accompanying [reference implementation](#reference_implementation) with Terraform.

## Target audience 

This solution is designed for national healthcare agencies or regulated
insurance providers. It serves the following stakeholders:

- **Auditors and claims investigators** who review showroom dashboards to verify
submitted claim documents, audit flagged cases, and interact with the AI
assistant.

- **Data scientists** who securely access raw data using JupyterLab environments to
build, validate, and run health risk analysis models.

## Core capabilities

- **Sovereign health modeling**: Use BigQuery ML to screen claims
and customer datasets to identify health risk factors without moving data
outside the sovereign boundary.

- **AI claim verification**: Run localized document checks using
open-weight Gemma LLM to verify claim details against database records.

- **Interactive chatbot widget**: Query active database claims and receive
real-time, context-aware answers using the AI assistant chatbot.

- **Seamless JupyterLab analytics**: Access a dedicated Jupyter environment
preloaded with direct database connection variables and Workload Identity
bindings.

- **Internationalization**: Instantly switch UI language between
English, French, and German.

## Architecture



## Components

The following technologies and Google Cloud Dedicated in Germany services are used in this solution:



| 
Component | 
Tech | 
Purpose | 
|




| 
**Database** | 
[Cloud SQL](/sql/docs) | 
Storage for insurance claims, plans, and customers. | 
|

| 
**Other storage** | 
[Cloud Storage](/storage/docs) | 
Storage for claims documentation. | 
|

| 
**DWH** | 
[BigQuery](/bigquery/docs) | 
Data warehouse analytical tables and big data storage. | 
|

| 
**Model** | 
[BigQuery ML](/bigquery/docs/bqml-introduction) | 
Machine learning analysis on health risk scores. | 
|

| 
**LLM** | 
Gemma | 
Open-weight model (google/gemma-3-27b-it) for claim document verification and chatbot widget. | 
|

| 
**Container infrastructure** | 
[GKE](/kubernetes-engine/docs) | 
Container infrastructure for the claim application and JupyterHub server. | 
|

| 
**Analysis** | 
JupyterLab | 
Dedicated notebooks preloaded with active data. | 
|

| 
**App** | 
Node.js | 
Web app showroom dashboard. | 
|



## Reference implementation

A reference implementation of this solution with Terraform is provided in
GitHub. Note that this is a proof-of-concept prototype built for demonstration
purposes, and the implementation is not audited or secured for production use
cases.

For prerequisites and deployment instructions, see [Sovereign Health Insurance Risk Analysis with BigQuery ML & Gemma](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/demos/insurance).