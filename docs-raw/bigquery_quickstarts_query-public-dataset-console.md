# Try BigQuery using the sandbox

Source: https://berlin.devsitetest.how/bigquery/docs/quickstarts/query-public-dataset-console
Last updated: 2026-07-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/bigquery/docs/tpc-differences) for more details.














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

Data analytics

](https://berlin.devsitetest.how/docs/data)






- 








[

BigQuery

](https://berlin.devsitetest.how/bigquery/docs)






- 








[

Guides

](https://berlin.devsitetest.how/bigquery/docs/introduction)

















- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Enable the BigQuery sandbox ](#setup)

- [ Limitations ](#limitations)
- [ View a public dataset ](#view_a_public_dataset)
- [ Query a public dataset ](#query_a_public_dataset)
- [ Upgrade from the BigQuery sandbox ](#upgrade)
- [ Clean up ](#clean-up)

- [ Delete the project ](#delete_the_project)

- [ What's next ](#whats-next)
- 










# Try Big Query using the sandbox 




The BigQuery sandbox lets you explore limited BigQuery capabilities
at no cost to confirm whether BigQuery fits your needs. The
BigQuery sandbox lets you experience BigQuery without
providing a credit card or creating a billing account for your project. If you
already created a billing account, you can still use BigQuery at
no cost in the free usage tier.

The BigQuery sandbox lets you learn BigQuery with a
limited set of BigQuery features at no charge. You can evaluate
BigQuery by using the BigQuery sandbox to view and query a
public dataset.

Google Cloud Dedicated in Germany offers public datasets that are stored in BigQuery
and made available to the general public through the
[Google Cloud Public Dataset Program](https://berlin.devsitetest.how/datasets). For more information about
working with public datasets, see [BigQuery public datasets](/bigquery/public-data).





## Before you begin 



### Enable the Big Query sandbox

- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery)

You can also open BigQuery in the Google Cloud Dedicated console
by entering the following URL in your browser:


```
https://console.cloud.berlin-build0.goog/bigquery
```


The Google Cloud Dedicated console is the graphical interface that you use to create
and manage BigQuery resources and to run SQL queries.

- 

Authenticate with your Google Account, or create a new one.

- 

On the welcome page, do the following:

- 

For **Country**, select your country.

- 

For **Terms of Service**, select the checkbox if you agree to the terms
of service.

- 

Optional: If you are asked about email updates, select the checkbox if
you want to receive email updates.

- 

Click **Agree and continue**.



- 

Click **Create project**.

- 

On the **New Project** page, do the following:

- 

For **Project name**, enter a name for your project.

- 

For **Organization**, select an organization or select
**No organization** if you are not part of one. Managed accounts, such
as those associated with academic institutions, must select an
organization.

- 

If you are asked to select a **Location**, click **Browse** and select a
location for your project.

- 

Click **Create**. You are redirected back to the **BigQuery** page in
the Google Cloud Dedicated console.



You have successfully enabled the BigQuery sandbox. A
BigQuery sandbox notice is now displayed on the **BigQuery** page:








## Limitations

The BigQuery sandbox is subject to the following limits:

- All BigQuery [quotas and limits](/bigquery/quotas) apply.

- You are granted the same free usage limits as the BigQuery
[free tier](https://berlin.devsitetest.how/bigquery/pricing#free-tier), including 10 GB of active storage
and 1 TB of processed query data each month.

- All BigQuery [datasets](/bigquery/docs/datasets-intro) have a
[default table expiration time](/bigquery/docs/updating-datasets#table-expiration),
and all [tables](/bigquery/docs/tables-intro),
[views](/bigquery/docs/views-intro), and
[partitions](/bigquery/docs/partitioned-tables) automatically expire after 60
days.

- 

The BigQuery sandbox does not support several BigQuery
features, including the following:

- [Streaming data](/bigquery/docs/write-api)

- [Data manipulation language (DML) statements](/bigquery/docs/data-manipulation-language)

- [BigQuery Data Transfer Service](/bigquery/docs/dts-introduction)

## View a public dataset

BigQuery public datasets are available by default in
BigQuery Studio in a project named `bigquery-public-data`. In this
tutorial you query the NYC Citi Bike Trips dataset. Citi Bike is a large bike
share program, with 10,000 bikes and 600 stations across Manhattan, Brooklyn,
Queens, and Jersey City. This dataset includes Citi Bike trips since Citi Bike
launched in September 2013.

- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the left pane, click explore **Explorer**:



If you don't see the left pane, click last_page **Expand left pane** to open the pane.

- 

In the **Explorer** pane, click
** add Add data**.

- 

In the **Add data** dialog, click
**Public datasets**.

- 

On the **Marketplace** page, in the **Search Marketplace** field, type `NYC
Citi Bike Trips` to narrow your search.

- 

In the search results, click **NYC Citi Bike Trips**.

- 

On the **Product details** page, click **View dataset**. You can view
information about the dataset on the **Details** tab.

## Query a public dataset

In the following steps, you query the `citibike_trips` table to determine the
100 most popular Citi Bike stations in the NYC Citi Bike Trips public dataset.
The query retrieves the station's name and location, and the number of
trips that started at that station.

The query uses the [ST_GEOGPOINT function](/bigquery/docs/reference/standard-sql/geography_functions#st_geogpoint)
to create a point from each station's longitude and latitude parameters and
returns that point in a `GEOGRAPHY` column. The `GEOGRAPHY` column is used to
generate a heatmap in the integrated geography data viewer.

- 

In the Google Cloud Dedicated console, open the
**BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

Click add_box 

**SQL query** .

- 

In the 
query editor , enter the following query:


```
SELECT 
start_station_name , 
start_station_latitude , 
start_station_longitude , 
ST_GEOGPOINT ( start_station_longitude , start_station_latitude ) AS geo_location , 
COUNT ( * ) AS num_trips 
FROM 
`bigquery-public-data.new_york.citibike_trips` 
GROUP BY 
1 , 
2 , 
3 
ORDER BY 
num_trips DESC 
LIMIT 
100 ; 
```


If the query is valid, then a check mark appears along with the amount of
data that the query processes. If the query is invalid, then an
exclamation point appears along with an error message.



- 

Click
**Run** .
The most popular stations are listed in the
**Query results** 
section.



- 

Optional: To display the duration of the job and the amount of data that the
query job processed, click the **Job information** tab in the **Query
results** section.

- 

Switch to the **Visualization** 
tab. This tab generates a map to quickly visualize your results.

- 

In the **Visualization configuration** panel:

- Verify that **Visualization type** is set to **Map**.

- Verify that **Geography column** is set to **`geo_location`**.

- For **Data column**, choose **`num_trips`**.

- Use the add **Zoom in** option to
reveal the map of Manhattan.



## Upgrade from the BigQuery sandbox

The BigQuery sandbox lets you explore
[limited BigQuery capabilities](#limitations)
at no cost. When you are ready to increase your storage and query
capabilities, upgrade from the BigQuery sandbox.

To upgrade, do the following:

- 

[Enable billing](/billing/docs/how-to/modify-project#enable_billing_for_a_project)
for your project.

- 

Explore [BigQuery editions](/bigquery/docs/editions-intro)
and determine the pricing model that is right for you.

Once you have upgraded from the BigQuery sandbox, you should
[update the default expiration times for your BigQuery resources](/bigquery/docs/updating-datasets#table-expiration)
such as tables, views, and partitions.







## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






### Delete the project

If you used the [BigQuery sandbox](/bigquery/docs/sandbox) to query
the public dataset, then billing is not enabled for your project, and you don't
need to delete the project.

The easiest way to eliminate billing is to delete the project that you
created for the tutorial.

To delete the project:






- 
In the Google Cloud Dedicated console, go to the Manage resources** page.


[Go to Manage resources](https://console.cloud.berlin-build0.goog/iam-admin/projects)




- 
In the project list, select the project that you
want to delete, and then click **Delete**.


- 
In the dialog, type the project ID, and then click
**Shut down** to delete the project.









## What's next



- For more information about using BigQuery at no cost in the
free usage tier, see [Free usage tier](https://berlin.devsitetest.how/bigquery/pricing#free-tier).

- Learn how to [create a dataset, load data, and query tables in
BigQuery](/bigquery/docs/quickstarts/load-data-console).