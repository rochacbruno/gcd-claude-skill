# Infrastructure as Code on Google Cloud Dedicated

Source: https://berlin.devsitetest.how/docs/terraform/iac-overview
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/terraform/tpc-differences) for more details.














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

Developer tools

](https://berlin.devsitetest.how/docs/costs-usage)






- 








[

Terraform on Google Cloud

](https://berlin.devsitetest.how/docs/terraform)






- 








[

Guides

](https://berlin.devsitetest.how/docs/terraform/terraform-overview)












# Infrastructure as Code on Google Cloud Dedicated 






- On this page 
- [ Benefits of IaC ](#benefits)
- [ IaC tools for Google Cloud Dedicated ](#iac-usecases-tools)
- [ What's next ](#whats-next)
- 










Infrastructure as Code (IaC) is the process of provisioning and managing software
application infrastructure using *code* instead of graphical user interfaces or
command-line scripts.

Provisioning application infrastructure typically involves setting up and
managing virtual machines, database connections, storage, and other
infrastructure elements. Manually managing this infrastructure is time consuming
and error prone, especially when managing applications at scale.

IaC lets you define your infrastructure with configuration files, which allow
you to build, change, and manage your infrastructure in a safe and repeatable
way. You can define resource configurations that you can version, reuse, and
share. IaC lets you specify the desired state of your infrastructure. You can
then deploy the same configuration multiple times to create reproducible
development, test, and production environments.

IaC allows you to treat your infrastructure provisioning and configuration in
the same manner as you handle application code. You can store your provisioning
configuration logic in source control and you can take advantage of continuous
integration and continuous deployment (CI/CD) pipelines.

## Benefits of Ia C

Using IaC to set up and manage your application infrastructure is a best
practice for a number of common use cases. [Google manages its
systems with
IaC](https://www.usenix.org/publications/loginonline/prodspec-and-annealing-intent-based-actuation-google-production),
and established it as a [standard
practice](https://sre.google/workbook/configuration-design/) internally.

IaC offers the following benefits:

- You can define your infrastructure based on your requirements and
reuse the same configuration to create multiple environments consistently.

- You can automate the creation and management of your cloud resources,
including for deployment and test environments.

- You can treat infrastructure changes like you treat application changes. For
example, you can ensure that changes to the configuration are reviewed and
automatically validated. Managing production environments through
change-controlled processes using IaC is a best practice.

- You can keep a history of all configuration changes. Changes can be audited
and reverted.

- You can have a single source of truth for your cloud infrastructure.

## Ia C tools for Google Cloud Dedicated

Google Cloud Dedicated in Germany is tightly integrated with many IaC tools. Choose one of the
following tools depending on your use case:

- 

**Terraform**

In general, to configure and manage Google Cloud Dedicated infrastructure using
code, use the Terraform provider for Google Cloud Dedicated.

HashiCorp Terraform is an IaC tool that lets you define
resources in cloud and on-premises in human-readable configuration files
that you can version, reuse, and share. You can then use a consistent
workflow to provision and manage all of your infrastructure throughout its
lifecycle. For more information, see
[Overview of Terraform on Google Cloud Dedicated](/docs/terraform/terraform-overview).

- 

**Terraform Cloud and Terraform Enterprise**

If you require full change management with Terraform across your
organization, use Terraform Cloud or Terraform Enterprise.

Terraform Cloud is a software as a service (SaaS) application that runs Terraform in a stable,
remote environment and securely stores state and secrets. Terraform Cloud
also integrates with the Terraform CLI and connects to common version
control systems (VCS) like GitHub, GitLab, and Bitbucket. When you connect a
Terraform Cloud workspace to a VCS repository, new commits and changes can
automatically trigger Terraform plans. Terraform Cloud also offers an API,
allowing you to integrate it into existing workflows.

Terraform Enterprise lets you set up a self-hosted distribution of Terraform
Cloud. It offers customizable resource limits and is ideal for organizations
with strict security and compliance requirements.

For more information, see the [Terraform Editions page in the Hashicorp
documentation](https://developer.hashicorp.com/terraform/intro/terraform-editions).

- 

**Cloud Development Kit for Terraform**

If you want to generate infrastructure with a general-purpose programming
language instead of using Hashicorp Configuration Language (HCL), use Cloud
Development Kit for Terraform (CDKTF).

[CDKTF](https://developer.hashicorp.com/terraform/cdktf) 
lets you configure Terraform using a programming language to define and
provision Google Cloud Dedicated infrastructure and lets you use your existing
toolchain for processes like testing and dependency management.

- 

**Pulumi**

[Pulumi](https://www.pulumi.com/docs/clouds/gcp/) 
is another tool you can use to provision infrastructure using programming
languages. You can use Google Cloud Dedicated provider for Pulumi to author
infrastructure code using programming languages such as TypeScript, Python,
Go, C#, Java or YAML.

- 

**Crossplane**

Another option to manage Google Cloud Dedicated resources through Kubernetes is
by using Crossplane.

Crossplane connects your Kubernetes cluster to external, non-Kubernetes
resources, and allows platform teams to build custom Kubernetes APIs to
consume those resources. Crossplane acts as a
[Kubernetes controller](https://kubernetes.io/docs/concepts/architecture/controller/)
to watch the state of the external resources and provide state enforcement.
With Crossplane installed in a Kubernetes cluster, users only communicate
with Kubernetes. Crossplane manages the communication to external resources
like Google Cloud Dedicated. If something modifies or deletes a resource outside
of Kubernetes, Crossplane reverses the change or recreates the deleted
resource.

For more information, see the
[Crossplane documentation](https://docs.crossplane.io/v1.18/).

- 

**Ansible**

If you want to automate provisioning, configuration management, application
deployment, orchestration, and other IT processes, use Ansible. For more
information, see [Ansible for
Google Cloud Dedicated](https://docs.ansible.com/ansible/latest/collections/google/cloud/).

## What's next

- Learn about the [differences in Google Cloud Dedicated versus Google Cloud](/docs/terraform/tpc-differences)

- Learn more about [Terraform](/docs/terraform/terraform-overview)

- Learn how to
[create a basic web server on Compute Engine using Terraform](/docs/terraform/get-started-with-terraform)

- Learn how to
[store Terraform state in a Cloud Storage bucket](/docs/terraform/resource-management/store-state)