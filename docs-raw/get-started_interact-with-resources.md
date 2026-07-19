# Ways to interact with Google Cloud Dedicated in Germany

Source: https://berlin.devsitetest.how/docs/get-started/interact-with-resources
Last updated: 2026-07-17

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












# Ways to interact with Google Cloud Dedicated in Germany 






- On this page 
- [ Graphical interfaces ](#graphical-interfaces)

- [ Google Cloud Dedicated console ](#console)
- [ Google Cloud Dedicated mobile app ](#mobile-app)

- [ Development environments ](#development-environments)

- [ Cloud Shell (and Cloud Shell Editor) ](#cloud-shell)
- [ Antigravity 2.0 ](#antigravity)
- [ Cloud Workstations ](#cloud-workstations)
- [ Cloud Code ](#cloud-code)

- [ Developer tools ](#developer-tools)

- [ Google Cloud SDK ](#cloud-sdk)
- [ AI-powered command-line tools ](#cli-tools)
- [ MCP servers and Agent Skills ](#mcp-servers)
- [ Infrastructure as code (IaC) tools ](#iac-tools)

- [ Integrated AI assistance ](#integrated-ai-assistance)

- [ Gemini for Google Cloud Dedicated (web and mobile) ](#gemini)

- 










Google Cloud Dedicated in Germany provides a wide range of interfaces and tools to help you be more
productive. Whether you prefer a point-and-click graphical interface, a
cloud-hosted development environment, or an AI-assisted command-line,
you can choose the path that best aligns with your workflow. Mix and match
these interfaces and tools to create pipelines for development, deployment,
and monitoring.

## Graphical interfaces 

Use graphical interfaces for visual resource management, administrative tasks,
and high-level overviews of your cloud footprint.

### Google Cloud Dedicated console 

If you prefer to manage your Google Cloud Dedicated projects and resources through
a graphical user interface, use the web-based
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/). It serves as your primary
hub for:

- **Resource creation and orchestration**: Deploy, scale, and monitor cloud
infrastructure.

- **Administration and governance**: Manage Identity and Access Management (IAM) (IAM)
policies, configure billing accounts, and audit system activity.

- **Data management and visualization**: Store, query, and process data across
databases and analytics services.

- **Integrated assistance**: Use AI-assisted features to ask questions about
your architecture or troubleshoot errors as they appear.

To ensure proper console functionality, see
[Allow access to Google Cloud Dedicated console domains](/docs/get-started/required-domains).

### Google Cloud Dedicated mobile app

The [Google Cloud Dedicated mobile app](https://berlin.devsitetest.how/app), available on
[iOS](https://itunes.apple.com/us/app/google-cloud-console/id1005120814) and
[Android](https://play.google.com/store/apps/details?id=com.google.android.apps.cloudconsole),
is a mobile companion to the web-based Google Cloud Dedicated console. Use it to monitor
services, respond to incidents, and perform basic resource management directly
from a mobile device.

## Development environments

Development environments offer pre-configured, contextual, and often
cloud-hosted spaces to build and manage your applications.

### Cloud Shell (and Cloud Shell Editor)

[Cloud Shell](/shell/docs) provides a web-based command-line environment
that includes the Google Cloud CLI and other command-line tools. Use
Cloud Shell as an interactive, web-based terminal to interact with
Google Cloud Dedicated without installing anything locally.

Cloud Shell also comes with [Cloud Shell Editor](/shell/docs/editor-overview),
a built-in code editor that lets you browse file directories, view and edit
files, and maintain continued access to Cloud Shell. Cloud Shell Editor is
available by default with every Cloud Shell instance and is based on
[Code OSS](https://github.com/microsoft/vscode).

### Antigravity 2.0

For agent orchestration, [Antigravity 2.0](https://antigravity.google/docs/get-started)
provides a GUI environment to manage parallel autonomous subagents, run
scheduled tasks, and orchestrate workflows across editor, terminal, and browser.

### Cloud Workstations

[Cloud Workstations](/workstations/docs/overview) provides managed,
customizable development environments on Google Cloud Dedicated. Platform teams can
use Cloud Workstations to provide developers with standardized, containerized
IDEs (such as IntelliJ IDEA or VS Code). This approach helps to ensure
consistent security across the organization by keeping development environments
within your Virtual Private Cloud (VPC) network.

### Cloud Code

[Cloud Code](/code/docs) extends supported integrated development
environments (IDEs)—including VS Code, IntelliJ IDEA, and Cloud Shell
Editor—to help you build and deploy applications on Google Cloud Dedicated. Use
Cloud Code for cluster management for Google Kubernetes Engine, direct deployment to
Cloud Run, and Gemini-powered code assistance within your IDE.

## Developer tools

Developer tools include command-line interfaces (CLIs), programmatic client
libraries, and utilities that enable modern software engineering practices.

### Google Cloud SDK

The [Google Cloud SDK](/sdk/docs/overview) provides programmatic access to
Google Cloud Dedicated through command-line tools and client libraries:

- **Cloud Client Libraries**: Use language-idiomatic libraries (such as Python, Go,
and Java) to call Google Cloud Dedicated APIs directly within your application
code. For centralized client library installation and setup instructions, see
[Cloud Client Libraries](/apis/docs/cloud-client-libraries).

- **Google Cloud CLI**: Use the primary command-line tool to manage and
configure Google Cloud Dedicated resources, create scripts, and automate CI/CD
pipelines. For centralized installation and setup instructions, see
[Install the Google Cloud CLI](/sdk/docs/install-sdk).

### AI-powered command-line tools

AI-powered command-line interfaces let you manage Google Cloud Dedicated resources
and develop applications using natural language. For example, the
[Antigravity CLI](https://antigravity.google/docs/cli) is an agentic
command-line tool that supports coding, code generation, research, task
management, and cloud orchestration.

### MCP servers and Agent Skills

The [Model Context Protocol (MCP)](/discover/what-is-model-context-protocol) is
an open standard that acts as a bridge between AI models and your data
sources or tools. Connect your AI applications (such as Antigravity
IDE, VS Code, or Cursor) to remote MCP servers to gather more context, ground
responses in product data, or perform specific tasks:

- **Developer Knowledge MCP**: Provide your AI tools with direct access to the
latest Google Cloud Dedicated documentation and best practices. For more
information, see [Developer Knowledge MCP](https://developers.google.com/knowledge/mcp).

- **Google Cloud Dedicated remote MCP servers**: Enable large language models (LLMs)
to use Google and Google Cloud Dedicated services in your AI applications through
remote MCP servers and product-specific tools. For an overview of MCP
architecture and capabilities, see [Google Cloud Dedicated MCP servers](/mcp/overview).

- **Agent Skills and Agent Registry**: Use
[Agent Registry](/agent-registry/overview) to discover, reuse, and
govern autonomous AI agents and MCP tools across your organization. Agent
Skills represent high-level capabilities possessed by autonomous agents (such
as Agent2Agent capabilities) that your AI orchestrators can discover and
consume, removing the need to build custom integrations for each new workflow.

#### Discover remote MCP servers and Agent Skills

Google Cloud Dedicated offers remote MCP servers for a growing subset of products.
These remote servers run on Google infrastructure and provide HTTP endpoints for
your AI applications. To discover whether remote MCP servers and agent skills
exist for a given product, use the following methods:

- **Review supported products**: To check if a Google Cloud Dedicated product offers
a remote MCP server, toolsets, or reference documentation, see the centralized
[Supported products](/mcp/supported-products) table. This page provides the
direct MCP server endpoints, MCP reference documentation, and user guides for
each supported service.

- **Discover capabilities programmatically**: Once a remote MCP server is
configured for your project or registered in
[Agent Registry](/agent-registry/overview), AI applications can
programmatically discover the server's capabilities—such as available tools,
prompts, and data resources—using standard MCP discovery methods (for example,
`tools/list`, `prompts/list`, and `resources/list`) or by querying the
Agent Registry API.

### Infrastructure as code (IaC) tools

For teams practicing DevOps, Google Cloud Dedicated supports industry-standard
[infrastructure as code](/docs/iac) (IaC) tools—such as Terraform, Pulumi, and
Config Connector—to manage infrastructure through declarative configuration
files.

Using IaC lets you store your infrastructure definitions in source control,
enabling repeatable deployments, automated testing, and audit logging as part of
your change management process.

## Integrated AI assistance

Google Cloud Dedicated also includes direct AI integration into developer workflows
for contextual knowledge and assistance.

### Gemini for Google Cloud Dedicated (web and mobile)

Gemini for Google Cloud Dedicated offers generative AI-powered assistance
to Google Cloud Dedicated users, including developers and data
scientists. Gemini for Google Cloud Dedicated is embedded in many
Google Cloud Dedicated products and provides an integrated assistance experience
using the context of your specific project:

- **In the Google Cloud Dedicated console**: Use the integrated Gemini Cloud Assist
sidebar to ask natural language questions about your environment (for example,
"Why is my GKE cluster showing a high error rate?") or to
generate complex BigQuery SQL from a prompt.

- **In the Google Cloud Dedicated mobile app**: Use voice and chat interfaces to
monitor incidents and get AI-driven troubleshooting summaries while away from
your desk.

- **In development environments**: Use **Gemini Code Assist** in your
IDE to write, refactor, and document application code.

- **For infrastructure lifecycle management**: Use
**Gemini Cloud Assist** to design, deploy, and optimize your cloud
resources.

To explore more of what Gemini for Google Cloud Dedicated offers, see
[Gemini for Google Cloud Dedicated overview](/gemini/docs/overview).