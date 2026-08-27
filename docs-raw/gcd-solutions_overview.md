# Solutions for Google Cloud Dedicated

Source: https://berlin.devsitetest.how/docs/gcd-solutions/overview
Last updated: 2026-08-26

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












# Solutions for Google Cloud Dedicated 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Available solutions ](#available_solutions)

- [ Finance ](#finance)
- [ Healthcare ](#healthcare)

- [ Design considerations ](#design_considerations)
- 









To help you understand how you can build and run workloads that use the sovereign
capabilities of Google Cloud Dedicated, we provide
reference architecture guides for a selection of common business scenarios.

Where available, solutions come with a reference implementation in GitHub that you can
deploy and try yourself.

## Before you begin 

- (Recommended) Review the [key differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).

- If a solution has a reference implementation you would like to try, and you haven't done so already, [set up the Google Cloud CLI for your universe](/docs/get-started-tpc/setup-gcloud).

## Available solutions 

The following solutions are available for Google Cloud Dedicated.

### Finance

- 

[**Tax anomaly detection:**](/docs/gcd-solutions/tax-enforcement) Optimize tax enforcement
and ensure data sovereignty with secure, localized AI innovation.

Built for regulated industries and the public financial sector, this
reference architecture uses BigQuery ML and a retrieval-augmented
generation (RAG) pipeline with the open-weight Gemma.

- **[Reference implementation](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/demos/tax-office).**

### Healthcare

- 

[**Health insurance risk analysis:**](/docs/gcd-solutions/health-insurance) Optimize health
insurance risk analysis and claims verification with secure, localized data
modeling and automated claim checks.

Built for highly regulated sectors, this reference architecture uses
BigQuery ML for health risk modeling and a regional open-weight
Gemma for claims document verification.

- **[Reference implementation](https://github.com/GoogleCloudPlatform/google-cloud-dedicated-demos/tree/main/demos/insurance).**

## Design considerations

Google Cloud Dedicated in Germany provides the benefits of Google's
cloud technology and services, while offering strong data and operational
sovereignty guarantees.

This means you can build and run workloads that comply with enhanced regulatory
requirements.

To help ensure data sovereignty,
Google Cloud Dedicated operates as a single,
completely standalone cloud region, with no connection to
Google Cloud's network. As a result,
Google Cloud features that rely on the existence of multiple
Google regions—such as load balancing across regions, or multi-region
storage—are not supported in
Google Cloud Dedicated.

To learn more about these differences so that you can better architect your own
sovereign Cloud solutions, see
[Key differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).