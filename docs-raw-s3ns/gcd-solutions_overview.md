# Solutions for Cloud de Confiance

Source: https://documentation.s3ns.fr/docs/gcd-solutions/overview
Last updated: 2026-09-04

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












# Solutions for Cloud de Confiance 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Available solutions ](#available_solutions)

- [ Finance ](#finance)
- [ Healthcare ](#healthcare)
- [ Multi-universe ](#multi-universe)

- [ Design considerations ](#design_considerations)
- 









To help you understand how you can build and run workloads that use the
sovereign capabilities of Cloud de Confiance, we
provide reference architecture guides for a selection of common business
scenarios.

Where available, solutions come with a reference implementation in GitHub that
you can deploy and try yourself.

## Before you begin 

- (Recommended) Review the [key differences between
Cloud de Confiance and
Google Cloud](/docs/overview/tpc-key-differences).

- If a solution has a reference implementation you would like to try, and you
haven't done so already, [set up the Google Cloud CLI for your
universe](/docs/get-started-tpc/setup-gcloud).

## Available solutions 

The following solutions are available for
Cloud de Confiance.

### Finance

- 

[**Tax anomaly detection:**](/docs/gcd-solutions/tax-enforcement) Optimize tax enforcement
and ensure data sovereignty with secure, localized AI innovation.

Built for regulated industries and the public financial sector, this
reference architecture uses BigQuery ML and a retrieval-augmented
generation (RAG) pipeline with the open-weight Gemma.

- **[Reference
implementation](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/demos/tax-office).**

### Healthcare

- 

[**Health insurance risk analysis:**](/docs/gcd-solutions/health-insurance) Optimize health
insurance risk analysis and claims verification with secure, localized data
modeling and automated claim checks.

Built for highly regulated sectors, this reference architecture uses
BigQuery ML for health risk modeling and a regional open-weight
Gemma for claims document verification.

- **[Reference
implementation](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/demos/insurance).**

### Multi-universe

- 

[**Multi-universe federation:**](/docs/gcd-solutions/multi-universe-federation) Achieve
multi-universe digital resilience and data sovereignty by federating
workloads across Google Cloud and Cloud de Confiance by S3NS
environments.

Relevant to any regulated industry, this reference architecture demonstrates
a "sovereign standby" model. It features an example retail banking
application running on Google Cloud with a synchronized,
near-real-time mirror on Cloud de Confiance by S3NS.

- **[Reference
implementation](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/demos/federation)**

## Design considerations

Cloud de Confiance by S3NS provides the benefits of Google's
cloud technology and services, while offering strong data and operational
sovereignty guarantees. You can
build and run workloads that comply with enhanced regulatory requirements, such
as those that need to be hosted in a
[SecNumCloud](https://cyber.gouv.fr/sites/default/files/document/anssi_Recommendations%20on%20hosting%20sensitive%20IS%20in%20the%20cloud.pdf)
compliant environment.

To help ensure data sovereignty,
Cloud de Confiance operates as a single,
completely standalone cloud region, with no connection to
Google Cloud's network. As a result, Google Cloud
features that rely on the existence of multiple Google regions—such as
load balancing across regions, or multi-region storage—are not supported
in
Cloud de Confiance.

To learn more about these differences so that you can better architect your own
sovereign Cloud solutions, see [Key differences between
Cloud de Confiance and
Google Cloud](/docs/overview/tpc-key-differences).