# Terraform on Cloud de Confiance maturity model

Source: https://documentation.s3ns.fr/docs/terraform/maturity
Last updated: 2026-07-29

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/terraform/tpc-differences) for more details.














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

Developer tools

](https://documentation.s3ns.fr/docs/costs-usage)






- 








[

Terraform on Google Cloud

](https://documentation.s3ns.fr/docs/terraform)






- 








[

Guides

](https://documentation.s3ns.fr/docs/terraform/terraform-overview)












# Terraform on Cloud de Confiance maturity model 






- On this page 
- [ Overview ](#overview)

- [ Adopt (Learner) ](#adopt_learner)
- [ Build (Builder) ](#build_builder)
- [ Scale (Operator) ](#scale_operator)

- [ Criteria ](#criteria)
- [ Recommendations ](#recommendations)
- 










This page explains the maturity model for Terraform on Cloud de Confiance.
This model provides best practices, recommendations, and learning materials that
meet you at your level of comfort and expertise with Terraform on
Cloud de Confiance.

## Overview 

Terraform on Cloud de Confiance has three user personas (Learners, Builders, and
Operators), and three stages of the maturity model (Adopt, Build, and Scale).

As organizations advance through the process of adopting, building, and scaling
Terraform on Cloud de Confiance for their infrastructure use-cases, they need
accessible learning materials that provide the guidance they need wherever
they are at on their journey.

Determine which of these personas represent you the best and look
at the associated content to find resources that will help you and your
organization advance through the maturity stages, enabling you to apply your use
case to Terraform on Cloud de Confiance at scale.



### Adopt (Learner)

Learners are beginning their journey on Cloud de Confiance and focus on
opinionated guidance to learn how to use Terraform on Cloud de Confiance and adopt it for their use case.

They may have some knowledge of Bash or other scripting languages,
but they don't use automation or CI/CD today to provision infrastructure.

You may be a **Learner** if you are:

- a developer

- new to Cloud de Confiance, Infrastructure as Code, or Terraform

### Build (Builder)

Builders have experience with Infrastructure as Code and use Cloud de Confiance
to build their projects.

They work with foundational infrastructure and a few applications on
Cloud de Confiance. Builders plan on growing their cloud usage, specific use
cases, and customizations, and think about scaling and onboarding more teams or applications.

You may be a **Builder** if you are:

- a developer

- on a platform admin team

- on a Cloud team

- a SRE

- familiar with working on Cloud de Confiance, Terraform, and have a
Infrastructure as Code operation model

### Scale (Operator)

Operators are experienced with Cloud de Confiance and use Terraform to provision infrastructure for their workloads at scale.

They scale and grow cloud usage, specific use cases, customizations, and onboard
more teams and workloads. Operators set policies and self serve workflows for
workload teams.

You may be an **Operator** if you are:

- on a platform admin team

- on a Cloud team

- a SRE

- experienced operating a Cloud de Confiance by S3NS, and a Terraform operation model at scale

## Criteria

This table details some of the criteria for each maturity stage to help you
determine which fits best with your level of familiarity with Terraform on
Cloud de Confiance and your use case. 





| 
| 
Adopt | 
Build | 
Scale | 
|



| 
Method | 
UI, CLI, and/or Terraform as a Service | 
Infrastructure as Code via Infra Manager | 
Infrastructure as Code via (1) Terraform OSS + Custom Pipelines or (2) Terraform Enterprise on Cloud de Confiance | 
|

| 
Automation | 
None or Limited | 
Limited | 
Yes | 
|

| 
Consistency | 
None or Limited | 
Limited | 
Yes | 
|

| 
Configuration | 
Unstructured, stored in a variety of locations | 
Structured, stored in a central location | 
Structured, stored in a version control system and versioned | 
|

| 
Deployment | 
Manual | 
Automated using a CI/CD pipeline | 
Automated using a CI/CD pipeline | 
|

| 
State | 
Not stored | 
Stored in a central location | 
Stored in a central location | 
|

| 
Drift | 
Not monitored or managed | 
Monitored and managed | 
Monitored and managed | 
|

| 
Documentation | 
Not maintained | 
Maintained | 
Well-documented | 
|

| 
Review and Approval | 
Not required | 
Required | 
Required | 
|

| 
Integration with Cloud Management Platform | 
Not integrated | 
Not integrated | 
Integrated with a cloud management platform | 
|

| 
Range of Cloud Resources | 
Limited | 
Wide | 
Wide | 
|

| 
Cost Optimization | 
Some concern | 
Some concern | 
Used | 
|

| 
Security | 
Not a concern | 
Some concern | 
High concern | 
|

| 
Compliance | 
Not a concern | 
Some concern | 
High concern | 
|



## Recommendations

The following table lists some recommended topics based on the maturity stage of your
organization and your use case with Terraform on Cloud de Confiance.





| 
| 
Adopt | 
Build | 
Scale | 
|


| 
Discover & Learn | 




- [Terraform on Cloud de Confiance Landing page](https://documentation.s3ns.fr/docs/terraform)

- [HashiCorp Terraform docs](https://developer.hashicorp.com/terraform/docs)


| 




- [Terraform on Cloud de Confiance docs](https://documentation.s3ns.fr/docs/terraform)

- [HashiCorp Terraform docs](https://developer.hashicorp.com/terraform/docs)


| 




- [Architecture Center](https://documentation.s3ns.fr/architecture)


| 
|

| 
Training & Tutorials | 




- [ Get Started - Google Cloud (HashiCorp Learning Center)](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started)

- [Get started with Terraform](/docs/terraform/get-started-with-terraform)

- [Basic Terraform commands](/docs/terraform/basic-commands)

- [ Best practices](/docs/terraform/best-practices-for-terraform)

- [ Cloud Skill Boost for Terraform](https://www.cloudskillsboost.google/catalog?keywords=terraform&locale=&solution%5B%5D=any&role%5B%5D=any&skill-badge%5B%5D=any&format%5B%5D=any&level%5B%5D=1&duration%5B%5D=any&language%5B%5D=any) (Beginner)


| 




- [Manage infrastructure as code](/docs/terraform/resource-management/managing-infrastructure-as-code)

- [ Cloud Skill Boost for Terraform](https://www.cloudskillsboost.google/catalog?keywords=terraform&locale=&solution%5B%5D=any&role%5B%5D=any&skill-badge%5B%5D=any&format%5B%5D=any&level%5B%5D=3&duration%5B%5D=any&language%5B%5D=any) (Intermediate)

- [ Cloud Foundations Toolkit 101](https://codelabs.developers.google.com/cft-onboarding/#0)

- [ Reuse Configuration with Modules](https://developer.hashicorp.com/terraform/tutorials/modules?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS)


| 




- [Export resources into Terraform](/docs/terraform/resource-management/export)

- [Import resources into Terraform state](/docs/terraform/resource-management/import)

- [ Cloud Skill Boost for Terraform](https://www.cloudskillsboost.google/catalog?keywords=terraform&locale=&solution%5B%5D=any&role%5B%5D=any&skill-badge%5B%5D=any&format%5B%5D=any&level%5B%5D=4&duration%5B%5D=any&language%5B%5D=any) (Advanced)

- Policy:



- `gcloud terraform vet`



| 
|

| 
Templates/
Ready to use | 




- [ Jump Start Solutions](https://documentation.s3ns.fr/solutions#jump-start-solutions)

- [ Cloud de Confiance Terraform modules on GitHub](https://github.com/terraform-google-modules)

- [ Terraform Registry](https://registry.terraform.io/providers/hashicorp/google/latest)

| 




- Customize Jump Start Solutions

- Customize Terraform Blueprints and Modules

- Create your own Terraform Blueprint

- [](https://github.com/terraform-google-modules/terraform-docs-samples/blob/main/CONTRIBUTING.md)Create your own Terraform module


| 




- [ Cloud de Confiance Terraform modules on GitHub](https://github.com/terraform-google-modules) (customize for scale)

- [Create & publish your own standardized Terraform Blueprints and modules](https://googlecloudplatform.github.io/samples-style-guide/)


| 
|

| 
Deploy & Manage | 




- [ Infrastructure Manager](https://documentation.s3ns.fr/infrastructure-manager/docs)

- [ Cloud Shell + Terraform](https://www.hashicorp.com/blog/kickstart-terraform-on-gcp-with-google-cloud-shell)


| 




- [ Infrastructure Manager](https://documentation.s3ns.fr/infrastructure-manager/docs)

- [Terraform GitOps with Cloud Build (CI/CD)](/docs/terraform/resource-management/managing-infrastructure-as-code) 

- [ Terraform Cloud or Enterprise on Cloud de Confiance](https://developer.hashicorp.com/terraform/cloud-docs)


| 




- [ Terraform GitOps with Cloud Build (CI/CD)](/docs/terraform/resource-management/managing-infrastructure-as-code)

- [ Terraform Cloud or Enterprise on Cloud de Confiance](https://developer.hashicorp.com/terraform/cloud-docs)

- [Getting started with Terraform CDK in GCP](https://medium.com/google-cloud/terraform-cdk-gcp-5455c481f364)


| 
|

| 
| 
Support | 
|

| 
| 




- Cloud de Confiance Cloud Customer Care

- Cloud de Confiance + HashiCorp Support (Priority support if customer has support for both)


| 
|