# Ways to interact with Google Cloud Dedicated in Germany

Source: https://berlin.devsitetest.how/docs/get-started/interact-with-resources
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












# Ways to interact with Google Cloud Dedicated in Germany 






- On this page 
- [ Use the browser-based Google Cloud Dedicated console ](#console)
- [ Write commands and create scripts ](#commands-and-scripts)
- [ Develop your own application using Cloud Client Libraries ](#libraries)
- [ Scale resource provisioning and management with Infrastructure as Code (IaC) ](#infrastructure-as-code)
- 










You can use several methods to interact with Google Cloud Dedicated and your
resources. The methods you choose can depend on your preferences, your company
workflows, and your goals.

The following are example interaction methods:

- [Google Cloud Dedicated console](#console): Use a web-based graphical user interface.

- [Google Cloud CLI](#commands-and-scripts): Write commands and scripts.

- [Cloud Client Libraries](#libraries): Create your own application.

- [Infrastructure as Code (IaC)](#infrastructure-as-code): Standardize resource
deployment.

## Use the browser-based Google Cloud Dedicated console 

If you prefer to manage your Google Cloud Dedicated projects and resources through a
graphical user interface, use the browser-based Google Cloud Dedicated console.

Use the Google Cloud Dedicated console to perform a variety of management and
administrative tasks, including the following:

- Manage resources.

- Store, query, and process data.

- Connect to virtual machines (VMs).

- Analyze activity.

- Diagnose production issues.

- Deploy easy-to-launch solutions.

To ensure proper console functionality, see also
[Allow access to Google Cloud Dedicated console domains](/docs/get-started/required-domains).

## Write commands and create scripts

If you prefer to manage development and workflows on the command line or through
automated scripts, use [the Google Cloud CLI](/sdk/gcloud). Use the
Google Cloud CLI to perform tasks efficiently and at scale. For example, you
might do the following:

- Create a script to push a file to all VMs.

- Simulate backend data with a data emulator to help you efficiently write
client-side code.

- Deploy serverless code.

Run `gcloud` commands using the following methods:

- 

Install the [Google Cloud CLI](/sdk/docs), which lets you run commands in
a terminal window on your local computer.

- 

Use the browser-based [Cloud Shell](/shell/docs/features), which doesn't
require local installation. Open Cloud Shell from the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/?cloudshell=true) to use the following
features:

- A temporary Compute Engine VM instance.

- A [built-in code editor](/shell/docs/editor-overview).

- Persistent disk storage.

- Pre-installed gcloud CLI, Terraform, and other tools.

- Language support for Java, Go, Python, Node.js, PHP, Ruby and .NET.

- Web preview.

- Built-in authorization for access to Google Cloud Dedicated console projects and
resources.

For more information about Cloud Shell, see
[How Cloud Shell works](/shell/docs/how-cloud-shell-works).

For a list of `gcloud` commands, as well as flags and examples, see the
[`gcloud` reference](/sdk/gcloud/reference).

## Develop your own application using Cloud Client Libraries

If you want to create your own applications to manage resources, use
[Cloud Client Libraries](/sdk/cloud-client-libraries) to access Google Cloud Dedicated in Germany APIs.

Cloud Client Libraries provide the following benefits to help you build your
application:

- Use conventions that are specific to your preferred language.

- Use a consistent style across services.

- Handle authentication.

For an overview, see [Cloud Client Libraries explained](/apis/docs/client-libraries-explained).

## Scale resource provisioning and management with Infrastructure as Code (IaC)

Infrastructure as Code (IaC) is the process of provisioning and managing
infrastructure using *code* instead of graphical user interfaces or command-line
scripts.

Your company's administrators and architects might use IaC to obtain the
following benefits:

- Incorporate your change management process.

- Test and audit as you make changes.

- Store configurations in source control.

- Standardize your infrastructure.

Google Cloud Dedicated in Germany is integrated with several IaC tools. For example, you might use [Terraform](/docs/terraform/terraform-overview) to provision and manage your infrastructure
through human-readable configuration files that you can version, reuse, and
share.

For an overview of IaC and a list of tools you can use with Google Cloud Dedicated in Germany, see [Infrastructure as Code on Google Cloud Dedicated](/docs/terraform/iac-overview).