# Learn about Cloud Billing

Source: https://berlin.devsitetest.how/docs/get-started/learn-about-billing
Last updated: 2026-08-26

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












# Learn about Cloud Billing 






- On this page 
- [ Key components and relationships ](#key_components_and_relationships)
- [ Types of Cloud Billing accounts ](#account-types)
- [ Manage your account and find out your costs ](#manage_your_account_and_find_out_your_costs)

- [ Basic account management ](#basic_account_management)
- [ Control who can access billing ](#control_who_can_access_billing)
- [ View your costs ](#view_your_costs)

- [ Monitor and optimize your cloud spend ](#monitor_and_optimize_your_cloud_spend)

- [ Set budgets and spending alerts ](#set_budgets_and_spending_alerts)
- [ View and manage cost anomalies ](#view_and_manage_cost_anomalies)
- [ Optimize costs (FinOps) ](#optimize_costs_finops)

- [ What's next ](#whats_next)
- 












































Cloud Billing is a collection of services and tools that helps you track,
understand, pay for, and optimize your costs on Google Cloud Dedicated in Germany and
Google Maps Platform.

- 

**Required for all services**: You must have an active Cloud Billing
account linked to your Google Cloud Dedicated in Germany projects to use any Google Cloud Dedicated in Germany
or Google Maps Platform service, including services within the
[Free Tier](/free/docs/free-cloud-features#free-tier).

- 

**Cost visibility**: Gain insight into how your usage translates to costs.

- 

**Cost control**: Implement controls to prevent unexpected expenses.

- 

**Cost optimization**: Find opportunities to reduce your cloud spend.

## Key components and relationships

- Cloud Billing account: This defines who pays for a given set of
Google Cloud Dedicated in Germany resources. It's linked to a Google Payments profile. You
might have one or multiple billing accounts depending on your needs.

- Google Payments profile: This is managed in the Google Payments Center and
includes your payment methods (like credit cards or bank accounts), address,
and tax information.

- Google Cloud Dedicated in Germany projects: Your resources (like virtual machines, storage,
databases) are organized within projects. Each project must be linked to a
Cloud Billing account to function. A single billing account can pay for
many projects.

[Learn more about resource organization and access
management](/billing/docs/onboarding-checklist).

## Types of Cloud Billing accounts

There are two main types of billing accounts:

- ***Self-serve*** (online): Costs are automatically charged to your linked
payment method. This can happen when your costs reach a certain threshold or
on a regular monthly cycle. Most new users start with this type.

- ***Invoiced*** (offline): You receive a monthly invoice for your accrued
costs and pay by using check or bank transfer. This option typically
requires meeting certain eligibility criteria.

[Find out your Cloud Billing account type and charging
cycle](/billing/docs/how-to/billing-cycle).

## Manage your account and find out your costs

Once you have a Cloud Billing account, you'll need to manage it and
understand how to track your spend.

### Basic account management

Common tasks include:

- [Create a new self-serve Cloud Billing account](/billing/docs/how-to/create-billing-account)

- [View projects linked to your billing account](/billing/docs/how-to/view-linked)

- [Enable, disable, or change billing for a project](/billing/docs/how-to/modify-project)

- [Add, remove, or update payment methods](/billing/docs/how-to/payment-methods)

- [Get your invoice, statement, or payment receipt](/billing/docs/how-to/get-invoice)

- [Close or reopen a Cloud Billing account](/billing/docs/how-to/close-or-reopen-billing-account)

### Control who can access billing

Google Cloud Dedicated in Germany uses Identity and Access Management (IAM) to control access to Cloud Billing.
The creator of the billing account is automatically granted the Billing Account
Administrator role. A Billing Account Administrator can grant different roles to
users or groups, such as:

- **Billing Account Administrator:** Full control over the billing account.

- **Billing Account Viewer:** Can view costs and transactions.

- **Billing Account User:** Can link projects to the billing account.

It's important to set these permissions carefully to ensure the right people
have the right level of access.

[Learn about Cloud Billing access control and
permissions](https://berlin.devsitetest.how/billing/docs/how-to/billing-access). You
can also [Create custom roles for
Cloud Billing](https://berlin.devsitetest.how/billing/docs/how-to/custom-roles).

### View your costs

The Google Cloud Dedicated console provides [several tools](/billing/docs/reports)
to help you understand your spend:

- **Billing reports**: See your cost trends, filter by project, service,
SKU, and labels, and see the impact of credits. This is the primary tool for
understanding what drives your costs. [Learn to use Billing
Reports](/billing/docs/how-to/reports).

- **Cost Table**: Get a detailed, tabular view of your costs for an
invoice or statement. This is useful for reconciliation. [View the cost
details of your
invoice](/billing/docs/how-to/cost-table).

- **Cost Breakdown**: See an at-a-glance view of your costs after savings,
helping you understand the net effect of credits and discounts. [Understand
your savings with cost breakdown
reports](/billing/docs/how-to/cost-breakdown).

## Monitor and optimize your cloud spend

Beyond cost visibility, Cloud Billing helps you actively control and
reduce your expenses.

### Set budgets and spending alerts

To avoid surprises on your bill, you can create budgets.

- Track planned versus actual spend: Monitor your charges against a target amount
you set.

- Scope: Budgets can apply to the entire billing account, specific projects,
services, or labels.

- Alerts: Set thresholds (for example, at 50%, 90%, and 100% of your budget
amount) to trigger email notifications to key stakeholders when costs
exceed these points.

Budgets don't automatically cap your spend, but they provide crucial warnings.

[Learn how to Create, edit, or delete budgets and budget
alerts](https://berlin.devsitetest.how/billing/docs/how-to/budgets).

### View and manage cost anomalies

Anomaly detection helps you manage unexpected costs across your billing
account's projects. Anomalies are spikes or deviations in usage costs
that differ from your expected spend.

Access the Anomalies dashboard to do the following:

- Investigate the root causes of anomalies.

- Customize your view by setting thresholds for cost impact amount and
percent of deviation.

- Manage automated alerts and notifications for detected anomalies.

[Learn more about anomaly detection for
costs](/billing/docs/how-to/manage-anomalies)

### Optimize costs (FinOps)

Cloud Billing tools support your Financial Operations (FinOps) journey,
helping you maximize business value from the cloud. Key **optimization** levers
include:

- **FinOps Hub**: Discover personalized recommendations to optimize costs
and track your FinOps health. [Explore the FinOps
hub](/billing/docs/how-to/finops-hub).

- **Committed Use Discounts (CUDs)**: Receive deeply discounted prices in
exchange for committing to a consistent amount of usage or spend over one or
three years. Ideal for stable workloads. [Analyze your CUD
effectiveness](/billing/docs/how-to/cud-analysis).

## What's next

- Dive deeper into the fundamental concepts in the [Cloud Billing
overview](/billing/docs/concepts).

- Try the [Interactive
tutorials](/billing/docs/interactive-tutorials) in
the Google Cloud Dedicated console.

- [Create a billing account](/billing/docs/how-to/create-billing-account).

- [Monitor costs using billing reports](/billing/docs/reports).

- [Optimize costs with FinOps hub](/billing/docs/how-to/finops-hub).