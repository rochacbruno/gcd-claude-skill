# Use developer tools

Source: https://berlin.devsitetest.how/docs/get-started/developer-tools
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/get-started/tpc-differences) for more details.














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












# Use developer tools 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Cloud Workstations: Develop in standardized environments ](#workstations)
- [ Google Cloud CLI: Write scripts and automate ](#cli)
- [ Cloud Code: Develop directly in your IDE ](#ide-extensions)

- [ Gemini Code Assist: Develop and deploy with AI assistance ](#code-assist)

- [ What's next? ](#whats_next)
- 









Google Cloud Dedicated in Germany provides several ways for developers to improve the efficiency of
their development workflow, including the following tools:

- [Cloud Workstations: Develop in standardized environments](#workstations)

- [Google Cloud CLI: Write scripts and automate](#cli)

- [Cloud Code: Develop directly in your IDE](#ide-extensions)

## Before you begin 

To make sure you can set up APIs and use tools, ask your administrators to
complete the following tasks:

- Create an account that you use to sign in and use Google Cloud Dedicated
products, including Google Cloud Dedicated console and Google Cloud CLI.

- Create a project that serves as an access boundary for your
Google Cloud Dedicated resources.

- Enable billing on your project so you can pay for service and API usage.

For detailed instructions to complete setup steps, see [Google Cloud Dedicated in Germany Setup
guided flow](/docs/enterprise/cloud-setup).

## Cloud Workstations: Develop in standardized environments

As a developer, you require software and specific configurations to perform your
tasks. The administrators at your company can help you with your workflows by
creating and distributing a development environment template that is suited to
your specific project.

Developers can use Cloud Workstations to obtain the following benefits:

- A standardized environment that is consistent for each developer on a team.

- Preconfigured settings established by administrators.

- Options to access the web-based environment from a browser, SSH, or IDE.

For more details, see [Cloud Workstations overview](/workstations/docs/overview).

## Google Cloud CLI: Write scripts and automate

The [Google Cloud CLI](/sdk/gcloud) tools help you create and manage Google Cloud Dedicated
resources from the command line, or through scripts and other automation. For
example, you might create an automated script to push files to VMs.

Use the gcloud CLI to do the following:

- Manage your local configuration.

- Establish authentication.

- Access Google Cloud Dedicated services through the command line.

For installation steps, see [Install the Google Cloud CLI](/sdk/docs/install-sdk).

## Cloud Code: Develop directly in your IDE

[Cloud Code](/code/docs) includes tools that help you use
Cloud Client Libraries and develop cloud applications. Use Cloud Code to
do the following directly in VS Code or
[supported JetBrains IDEs](/code/docs/intellij/ides):

- Integrate Google Cloud Dedicated APIs to work with Google Cloud Dedicated services.

- Access documentation.

- Debug your application.

- Use [Gemini Code Assist](#code-assist).

Cloud Code is automatically installed on Cloud Workstations and
Cloud Shell. To install the extension for your IDE, see the following:

- [Install the Cloud Code for VS Code extension](/code/docs/vscode/install)

- [Install the Cloud Code for IntelliJ plugin](/code/docs/intellij/install)

### Gemini Code Assist: Develop and deploy with AI assistance

When you install the Cloud Code extension, the
Gemini Code Assist extension is also installed by default.
Gemini Code Assist provides AI assistance with your code, including the
following:

- Generate and debug code.

- Generate unit tests.

- Chat to answer questions about code and other technical topics.

For more information, see the
[Gemini Code Assist overview](/gemini/docs/codeassist/overview).

## What's next?

To explore more developer tools, see [Google Cloud SDK, languages, frameworks, and
tools overview](/docs/devtools).

To get familiar with development workflows, experiment with the following
guides:

- 

For sample solutions, see the following:

- [Jump Start Solution guides](/architecture/all-jss-guides).

- [Google Cloud Dedicated in Germany web hosting](/solutions/web-hosting).

- 

To learn about deployment options, see the following:

- [Continuous deployment from Git using
Cloud Build](/run/docs/continuous-deployment-with-cloud-build).

- [CI/CD pipeline for developing and delivering containerized
apps](/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke).

- [Quickstart: Deploy a Node.js service toCloud Run](/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service).