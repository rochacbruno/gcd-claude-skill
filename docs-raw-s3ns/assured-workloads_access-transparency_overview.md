# Overview of Access Transparency

Source: https://documentation.s3ns.fr/assured-workloads/access-transparency/docs/overview
Last updated: 2026-10-26

- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Access Transparency

](https://documentation.s3ns.fr/assured-workloads/access-transparency/docs)






- 








[

Guides

](https://documentation.s3ns.fr/assured-workloads/access-transparency/docs/overview)

























# Overview of Access Transparency



This page provides an overview of Access Transparency, which is a part of
S3NS's long-term commitment to transparency, user trust, and customer
ownership of their data.

## Overview

Access Transparency logs record the actions that S3NS personnel take when
accessing Customer Data. Access Transparency log entries include details such as
the affected resource and action, the time of the action, the reason for the
action, and information about the accessor.

Access Transparency logs are designed to fulfill security and regulatory requirements to document, audit, and [restrict](/assured-workloads/access-approval) S3NS personnel access to your workloads.

The information about the
accessor includes details about the S3NS employee, such as their
physical location. For more information about the details
covered in Access Transparency logs, see
[Log field descriptions](/assured-workloads/access-transparency/docs/reading-logs#axt-log-entry-sample).

Access Transparency logs are similar to [Cloud Audit Logs](/logging/docs/audit);
however, Cloud Audit Logs records the actions that members of your
Cloud de Confiance organization have taken in your Cloud de Confiance resources,
whereas Access Transparency logs record the actions taken by S3NS personnel.
When used together, Cloud Audit Logs and Access Transparency logs provide you audit
logging on both customer actions and S3NS administrative access to
Customer Data.

## When to use Access Transparency

You might need Access Transparency logs for the following reasons:

- Verifying that S3NS personnel are accessing your content only for
valid business reasons, such as fixing an outage or attending to your support
requests.

- Verifying that S3NS personnel access aligns with the products and
data that you're seeking assistance with on a customer support case.

- Verifying and tracking compliance with legal or regulatory obligations.

## Use Access Transparency logs to improve the overall security posture

Access Transparency logs are a valuable additional source of information in your
security operations workstreams. By ingesting Access Transparency logs into your
security information and event management (SIEM) tools for compliance or
auditing purposes, you can augment any existing data, such as Security Command Center
security findings. 

## Cloud de Confiance services that produce Access Transparency logs

For the list of Cloud de Confiance by S3NS services that produce Access Transparency logs, see
[Supported services](/assured-workloads/access-transparency/docs/supported-services).

## When can S3NS personnel access customer content?

S3NS personnel are strictly restricted in what is visible to them.
All access to Customer Data requires a valid justification for
[privileged access](/assured-workloads/access-transparency/docs/privileged-access#why-access).
See [Justification reason codes](/assured-workloads/access-transparency/docs/reading-logs#justification_reason_codes)
for the list of valid business justifications.

## How does S3NS handle government requests for customer content?

If S3NS receives a government request for Customer Data, it is
S3NS's policy to direct the government to request such data directly
from the Cloud de Confiance by S3NS customer. 

## What's next

- 

To understand the contents of Access Transparency log entries, see
[Understanding and using Access Transparency logs](/assured-workloads/access-transparency/docs/reading-logs).

- 

For information on Cloud de Confiance by S3NS's privileged access principles, see
[Privileged access](/assured-workloads/access-transparency/docs/privileged-access).