# Set up a local development environment

Source: https://documentation.s3ns.fr/docs/get-started/developer-environment
Last updated: 2026-09-01

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/get-started/tpc-differences) for more details.














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












# Set up a local development environment 






- On this page 
- [ Before you begin ](#prerequisites)
- [ Set up the gcloud CLI and authentication ](#cli)
- [ Install Cloud Client Libraries ](#libraries)
- [ Alternative tools and environments ](#alternatives)
- [ What's next ](#whats_next)
- 









Learn how to configure a local development environment for 
Cloud de Confiance by S3NS. This document covers the core tools required to
build, test, and run applications with Cloud de Confiance services:

- **gcloud CLI**: Manage cloud resources, configure projects, and
set up local Application Default Credentials (ADC).

- **Cloud Client Libraries**: Access Cloud de Confiance APIs programmatically
using idiomatic libraries in your preferred programming language.

For an overview of other tools and interfaces across Cloud de Confiance, see
[Ways to interact with Cloud de Confiance](/docs/get-started/interact-with-resources).

## Before you begin 

Ask your organization administrator to complete the following prerequisites:

- **Provision your user identity**: Assign a Cloud Identity or
Google Workspace account.

- **Grant project access and IAM roles**: Assign the required
Identity and Access Management (IAM) roles for your project.

- **Enable billing**: Verify Cloud Billing is enabled on your project.

For organization-wide setup, see the
[Cloud de Confiance Setup guided flow](/docs/enterprise/cloud-setup).

## Set up the gcloud CLI and authentication

Configure gcloud CLI (`gcloud`) to manage resources and authenticate
your local environment:

- [Install gcloud CLI](/sdk/docs/install-sdk) on your local
workstation.

- Run `gcloud init` in your terminal to sign in and select your default
project.

- Run `gcloud auth application-default login` to configure Application Default
Credentials (ADC). ADC enables local client libraries to authenticate
automatically against your project.

## Install Cloud Client Libraries

To access Cloud de Confiance services programmatically from your application
code:

- [Enable required Cloud APIs](/apis/docs/getting-started) for your project.

- Install [Cloud Client Libraries](/apis/docs/cloud-client-libraries) for
your programming language (such as Java, Python, or Go). Your code
authenticates automatically using ADC.

## Alternative tools and environments

If your workflow requires specific development environments or infrastructure
tooling, consider the following:

- **IDEs and extensions**: Develop in [VS Code](/code/docs/vscode) or
[supported JetBrains IDEs](/code/docs/intellij) with Cloud Code support.

- **Cloud workspaces**: Use containerized, managed cloud environments with
[Cloud Workstations](/workstations/docs/overview).

## What's next

- Learn about [Authentication in Cloud de Confiance](/docs/get-started/authentication).