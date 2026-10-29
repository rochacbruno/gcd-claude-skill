# Cloud Billing release notes

Source: https://documentation.s3ns.fr/billing/docs/release-notes
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/billing/docs/tpc-differences) for more details.














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

Costs and usage management

](https://documentation.s3ns.fr/docs/costs-usage)






- 








[

Cloud Billing

](https://documentation.s3ns.fr/billing/docs)












# Cloud Billing release notes 


















This page documents production updates to Cloud Billing. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.







You can see the latest product updates for all of Cloud de Confiance by S3NS on the
[
Cloud de Confiance](/release-notes) page, browse and filter all release notes in the
[Cloud de Confiance console](https://console.cloud.s3nscloud.fr/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.s3nscloud.fr/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://documentation.s3ns.fr/feeds/billing-release-notes.xml) directly.









## March 13, 2025


Change 


**Improved consistency in resource-based committed use discount (CUD) string names across experiences.**

We have improved consistency by standardizing CUD string names across the various experiences. This update helps provide a seamless experience in resource-based CUD purchase flows, recommendations, analysis, and the FinOps hub.



## February 03, 2025


Change 


**Google Cloud Marketplace now uses the agency model for marketplace services for UK, FR, and DE customers.** 

As part of this change, customers will receive separate invoices for Google Cloud and third-party vendor transactions in the Cloud Marketplace.

For more information, see [Split invoicing for agency model transactions](/billing/docs/how-to/split-invoice) and [Marketplace Agency Account Migration FAQ](https://support.google.com/cloud/answer/13855075).



## January 29, 2025


Feature 


**Tags data for BigTable instances is available in both the [*Standard usage cost* export](/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [*Detailed usage cost* export](/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)**.

To learn more about Tags, see [Tags overview](/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see more [about tags](/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).



## December 18, 2024


Feature 


**Simulate scenarios in FinOps hub to maximize your savings from resource-based CUDs**

In the FinOps hub, we added support for resource-based CUD recommendations as a starting point to simulate various usage scenarios, and customize the recommendation to purchase a CUD that maximizes your savings.

[Learn about simulating scenarios for resource-based CUDs](/docs/cuds-recommender#simulate-scenarios).



## September 30, 2024


Feature 


**View and manage unexpected costs with Anomaly Detection (in preview)**

You can now view and manage cost spikes that deviate from your historical spend patterns using the Anomalies dashboard (preview). Each anomaly comes with a detailed root cause analysis that identifies the top services, regions, and SKUs that contributed to the spike.

[Learn more about using Anomaly Detection to manage costs](/billing/docs/how-to/manage-anomalies).



## September 27, 2024


Feature 


**Avoid charges for underutilized Compute Engine reservations in the FinOps hub**

You can now get recommendations to modify or delete your underutilized, on-demand reservations for Compute Engine resources when you haven't consumed your specified threshold of resources for at least 7 days.

[Learn about reservation recommendations](/compute/docs/instances/reservation-recommendations-overview)

[View and apply underutilized reservation recommendations](/compute/docs/instances/view-and-apply-underutilized-reservation-recommendations)



## September 26, 2024


Feature 


**Use Gemini AI assistant to find or create Billing Reports (preview)**

[Gemini Cloud Assist in Cloud Billing **Reports**](/billing/docs/how-to/gemini/overview) provides FinOps-focused AI assistance to create the cost reports you need to analyze your cost trends and to summarize key insights from the cost reports.

Gemini Cloud Assist in Cloud Billing Reports helps you to:

- [Use saved reports](/billing/docs/how-to/gemini/overview#saved-reports): Quickly access existing reports to analyze your spending.

- [Create new reports](/billing/docs/how-to/gemini/overview#gemini-ai-reports): Configure custom reports with AI assistance to get the exact data you need.

- [Summarize reports](/billing/docs/how-to/gemini/overview#report-summaries): Get AI-powered summaries of your reports to quickly understand key cost trends and insights.

[Enable the Gemini for Google Cloud API](/billing/docs/how-to/gemini/set-up-gemini) in a project to turn on Gemini Cloud Assist in Cloud Billing Reports.

For more information about Gemini Cloud Assist features in Cloud Billing Reports, see:

- [Gemini Cloud Assist in Cloud Billing](/billing/docs/how-to/gemini/overview) 

- [Set up Gemini Cloud Assist in Cloud Billing](/billing/docs/how-to/gemini/set-up-gemini)

- [Analyze billing data and cost trends with Reports](/billing/docs/how-to/reports)




## August 13, 2024


Feature 


**The *Carbon footprint dashboard* in the FinOps hub now includes market-based emissions data (preview)**

Scope 2 market-based emissions data (preview) for the Carbon footprint dashboard are now available in the [FinOps hub](/billing/docs/how-to/finops-hub). The market-based emissions metric represents purchased electricity, incorporating Google's annual renewable energy purchases. You can use the data in the Carbon footprint dashboard to optimize your cloud spend and reduce your carbon impact.

- 

To learn more about the methodology and the difference between location-based and market-based emission metrics, see the [carbon footprint documentation](/carbon-footprint/docs/methodology#market-based-allocation).

- 

[Learn more about the FinOps hub](/billing/docs/how-to/finops-hub).




## August 08, 2024


Feature 


**Tags data for Secret Manager secret usage is available in both the [*Standard usage cost export*](/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [*Detailed usage cost export*](/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).**

To learn more about Tags, see [Tags overview](/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see [about tags](/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).



Feature 


**View granular cost data from Secret Manager secret usage in Cloud Billing exports to BigQuery**

You can now view granular Secret Manager secret cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed log bucket usage.

[Review the schema of the Detailed cost data export](/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).



## July 22, 2024


Feature 


**Track credits for your spend-based milestone credit programs (contract pricing)**

If you have a custom pricing contract, you might be enrolled in *spend-based milestone credit programs*, where you earn promotional credits for spending specific amounts on Google Cloud.

In the Google Cloud console, you can now track the promotional credits for your spend-based milestone programs. The promotional credits that you receive act as a payment method, and are automatically applied to your costs.

[Learn about tracking spend-based milestone credits](/billing/docs/how-to/spend-milestone-credits).



## July 10, 2024


Feature 


**You can now view granular AlloyDB for PostgreSQL usage in the Cloud Billing Detailed export to BigQuery**

You can now view granular **AlloyDB for PostgreSQL** *cluster*, *instance*, and *backup data* in the Google Cloud Billing detailed export. Use the `resource.global_name` and `resource.name` fields in the export to view and filter your detailed AlloyDB cluster, instance, and backup usage.

[Review the schema of the Detailed cost data export](/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).



Feature 


**Tags data for AlloyDB for PostgreSQL cluster, instance, and backup usage is available in both the [*Standard usage cost export*](/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [*Detailed usage cost export*](/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).**

To learn more about Tags, see [Tags overview](/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see [about tags](/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).



## July 02, 2024


Feature 


**Simulate scenarios in FinOps hub to maximize your savings from spend-based CUDs**

In the FinOps hub, you can now use a spend-based CUD recommendation as a starting
point to simulate various usage scenarios, and customize the recommendation
to purchase a CUD that maximizes your savings.

[Learn about simulating scenarios for spend-based CUDs](/docs/cuds-recommender#simulate-scenarios).



## July 01, 2024


Feature 


**View your Carbon Footprint in the FinOps hub** 

In the [FinOps hub](/billing/docs/how-to/finops-hub#carbon-footprint-dashboard), you can now view the estimated greenhouse gas emissions for your Google Cloud usage by visiting the Carbon Footprint dashboard. 

[Learn about Carbon Footprint data](/carbon-footprint/docs/view-carbon-data).



## June 24, 2024


Feature 


**Avoid getting charged for idle Compute Engine reservations in the FinOps hub**

You can now get recommendations to modify or delete your idle, on-demand reservations for Compute Engine resources when you haven't consumed any resources for at least 7 days.

[Learn about idle reservation recommendations](/compute/docs/instances/idle-reservation-recommendations-overview).



## June 04, 2024


Feature 


**You can now view granular cost data for more Google Cloud services**

- You can now view granular Cloud Logging log bucket cost data in the Google Cloud Billing detailed export. Use the `resource.global_name` field in the export to view and filter your detailed log bucket usage.

- You can now view granular Managed Microsoft Active Directory cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed domain usage.

- You can now view granular Dataproc Metastore cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed service usage.

- You can now view granular Cloud Deploy cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed delivery pipeline usage.

- You can now view granular Cloud Data Fusion cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed instance usage.

[Review the schema of the Detailed cost data export](/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).