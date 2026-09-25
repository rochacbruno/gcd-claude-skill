# Set up a local development environment

Source: https://documentation.s3ns.fr/docs/get-started/developer-environment
Last updated: 2026-09-24

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
- [ Install the google-cloud-developer plugin ](#google-cloud-developer)
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

This document also shows how to install the `google-cloud-developer` plugin to
get help with Cloud de Confiance tasks and coding in a number of different
agents.

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

## Install the `google-cloud-developer` plugin

If you use an agent such as Claude Code CLI, Antigravity CLI, or Codex CLI to assist
you in your development work, you can install the `google-cloud-developer`
plugin to get help with Cloud de Confiance tasks and coding. This plugin
includes:

- Skills to help with account creation, billing setup, project management, and
authentication to Cloud de Confiance services and APIs.

- The `finding-google-skills` skill, which locates and runs the right Google
product skill on demand, thus avoiding the need to preload Google skills.

- The [Developer Knowledge](https://developers.google.com/knowledge/mcp)
remote MCP server, which provides the ability to search Google's official
developer documentation and retrieve information for Google's products such
as Google Cloud, Firebase, Android, Maps, and more.

Install the `google-cloud-developer` plugin using the following instructions
based on your agent.


[Antigravity CLI](#antigravity-cli) [Claude Code CLI](#claude-code-cli) [Codex CLI](#codex-cli) 
More 




- 

Install the plugin by specifying its location in the
[Google Agent Skills](https://g.dev/cloud/agent-plugins) repository:


```
agy plugin install https://github.com/google/skills/plugins/cloud/google-cloud-developer
```


- 

Enable the Developer Knowledge API in your Cloud de Confiance project by
using the gcloud CLI:


```
gcloud services enable developerknowledge.googleapis.com --project= YOUR_PROJECT_ID 
```





- 

Add the Google plugins marketplace and then install the plugin:


```
claude plugin marketplace add google/skills
claude plugin install google-cloud-developer@google-plugins
```


- 

Enable the Developer Knowledge API in your Cloud de Confiance project by
using the gcloud CLI:


```
gcloud services enable developerknowledge.googleapis.com --project= YOUR_PROJECT_ID 
```


- 

Create an API key for the Developer Knowledge API by following the
instructions [Create and secure the API key](https://developers.google.com/knowledge/quickstart#create-secure-key).
Save the key you create in a secure location.

- 

Export the API key to your environment before starting Claude Code CLI:


```
export DEVELOPERKNOWLEDGE_API_KEY= YOUR_API_KEY 
```





- 

Add the Google plugins marketplace and then install the plugin:


```
codex plugin marketplace add google/skills
codex plugin add google-cloud-developer@google-plugins
```


- 

Enable the Developer Knowledge API in your Cloud de Confiance project by
using the gcloud CLI:


```
gcloud services enable developerknowledge.googleapis.com --project= YOUR_PROJECT_ID 
```


- 

Create an API key for the Developer Knowledge API by following the
instructions [Create and secure the API key](https://developers.google.com/knowledge/quickstart#create-secure-key).
Save the key you create in a secure location.

- 

Enable authenticated access to the Developer Knowledge MCP server by
updating `~/.codex/config.toml` (or your project's `.codex/config.toml`)
to include the following lines:


```
[mcp_servers.developer-knowledge] 
url = "https://developerknowledge.googleapis.com/mcp" 
env_http_headers = { "X-Goog-Api-Key" = "DEVELOPERKNOWLEDGE_API_KEY" } 
```


- 

Export the API key to your environment before starting Codex:


```
export DEVELOPERKNOWLEDGE_API_KEY= YOUR_API_KEY 
```





## Alternative tools and environments

If your workflow requires specific development environments or infrastructure
tooling, consider the following:

- **IDEs and extensions**: Develop in [VS Code](/code/docs/vscode) or
[supported JetBrains IDEs](/code/docs/intellij) with Cloud Code support.

- **Cloud workspaces**: Use containerized, managed cloud environments with
[Cloud Workstations](/workstations/docs/overview).

## What's next

- Learn about [Authentication in Cloud de Confiance](/docs/get-started/authentication).