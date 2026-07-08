# Configure Cloud Quotas dimensions

Source: https://berlin.devsitetest.how/docs/quotas/configure-dimensions
Last updated: 2026-07-07

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://berlin.devsitetest.how/docs/quotas)






- 








[

Guides

](https://berlin.devsitetest.how/docs/quotas/overview)












# Configure Cloud Quotas dimensions 






- On this page 
- [ View dimensions ](#view_dimensions)
- [ Dimension precedence ](#dimension_precedence)
- [ Combining dimensions ](#combining_dimensions)
- [ What's next ](#whats_next)
- 









Cloud Quotas dimensions represent different ways of measuring resource
usage in Google Cloud Dedicated in Germany. Dimensions are typically a region, zone, Google Cloud Dedicated in Germany
user, or product attribute.

The Cloud Quotas API represents dimensions as key-value pairs. The `key` is
the dimension name (for example, `region`). The `value` is the assigned value
for the dimension (for example, a region such as `us-central1`). Keys and values
are case sensitive.

For example, Compute Engine measures VM use by using different dimensions. The
`region` dimension measures the number of VMs you have in a given region.
Compute Engine also has a number of product attribute dimensions, including
`gpu_family`. The `gpu_family` dimension measures the number of GPUs of a
given family in your Google Cloud Dedicated in Germany project.

## View dimensions

You can view the dimensions for quotas and system limits by looking in the
Google Cloud Dedicated console, using the Google Cloud CLI, querying the REST API, or through
client libraries. To view dimensions that you haven't specified a value for, use
the gcloud CLI. Also use the gcloud CLI to view dimensions
for quotas and system limits that don't have regional or zonal dimensions if
your project doesn't already use the associated resource. This section shows how
to view dimensions by using the console and by using the gcloud CLI.


[Console](#console) [gcloud](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

The table on this page displays dimensions in the **Dimensions** column.

- 

If you don't see the **Dimensions** column, take the following steps.
Otherwise, skip this step.

- Click view_column **Column display options**.

- Select **Dimensions**.

- Click **OK**. The **Dimensions** column appears in the table.

- 

To filter the results, enter a property name or value in the field next to
filter_list **Filter**.

- To filter by product, begin entering the product name and select from the
list that appears.

- To filter by dimension, enter your dimension using the following format:
`dimension_name:dimension_value`. For example, to see quotas and system limits
defined for the us-central1 region, enter: `region:us-central`.

### Understand blank dimensions

Sometimes the **Dimensions** column is empty. This can happen for the
following reasons:

- 

The quota or system limit value is the default value and applies for all
dimensions. For some quotas and system limits, the console shows a line
that lists the default quota or system limit value for reference. Because
the default applies to all dimension values, the **Dimensions** column is
blank. Look at the **Name** column to identify these entries. The **Name**
column indicates these entries with the word "default" in parenthesis at
the end of the quota or system limit name.

For example, the quota `SetIamPolicyRequestsPerMinutePerProject` is defined
on the `region` dimension. The console shows a reference entry, and an
entry for each region. In the **Name** column, the reference entry is
listed as
"SetIAMPolicy requests per minute per region (default)." For this entry,
the **Dimensions** column is empty.

- 

No dimensions apply. For example, the Compute Engine quota
`NETWORKS-per-project` isn't associated with a region, zone, or product
attribute, so there are no dimensions to display.






You can use the gcloud CLI to view dimensions for a single quota or
system limit, or for all quotas and system limits associated with a given
product. Viewing dimensions for a single quota or system limit is usually
faster than viewing dimensions for all quotas and system limits associated
with a product. The response to a query for a single quota is typically about
200 lines. The response to a query for a product can exceed 2,000 lines.

### View dimensions for a single quota or system limit with gcloud

To view dimensions for a single quota or system limit using the
gcloud CLI, run the following command in your terminal:


```
gcloud beta quotas info describe QUOTA_ID --project = PROJECT_ID --service = SERVICE_ID 
```


Replace the following:

- 

` QUOTA_ID `: the ID for the quota or system limit. If
you don't know your quota ID, choose one of the following options:

- Find it by using the console as described in
[Find your quota ID](/docs/quotas/gcloud-cli-examples#find_your_quota_id).

- View all dimensions for the product associated with the quota or system
limit you're interested in. This command doesn't require the quota ID.
See the section
[View dimensions for a product with gcloud CLI](#gcloud-view-product).

- 

` PROJECT_ID `: The ID of your Google Cloud Dedicated
project. To find your project ID, choose one of the following options:

- To find your project ID by using the console, see
[Identifying projects](/resource-manager/docs/creating-managing-projects#identifying_projects).

- If you set your current project as your default project in the
gcloud CLI configuration, find your project ID get by running the
following gcloud command in your terminal:

```
gcloud config get-value project
```


- 

` SERVICE_ID `: the service ID of the product associated
with the quota or system limit. For example, if the quota is for Compute Engine
A2 CPUs, the service ID is `compute.googleapis.com`.

### View dimensions for a product with gcloud CLI

To view dimensions for a single quota or system limit using the
gcloud CLI, run the following command in your terminal:


```
gcloud beta quotas info list --project = PROJECT_ID --service = SERVICE_ID 
```


Replace the following:

- 

` PROJECT_ID `: The ID of your Google Cloud Dedicated
project. To find your project ID, choose one of the following options:

- To find your project ID by using the console, see
[Identifying projects](/resource-manager/docs/creating-managing-projects#identifying_projects).

- If you set your current project as your default project in the
gcloud CLI configuration, find your project ID get by running the
following gcloud command in your terminal:

```
gcloud config get-value project
```


- 

` SERVICE_ID `: the service ID of the product associated
with the quota or system limit. For example, if the quota is for Compute Engine
A2 CPUs, the service ID is `compute.googleapis.com`.




## Dimension precedence

Some use cases for the Cloud Quotas API have complex dimension setups.
Quotas can be configured at a more granular level than just regions and zones.
You can accomplish this granularity when you use service-specific dimensions.
For example, the `gpu_family` and `network_id` are service-specific dimensions
in the Compute Engine service. Dimensions are defined by each individual
service and each service might have a different set of service-specific
dimensions.

When working with either location dimensions or service-specific dimensions,
the following precedence is applied:

- 

A quota preference configuration with all location and service-specific
dimensions specified takes precedence over any other configuration.

- 

Configurations that specify location dimensions only take precedence over
configurations containing only service-specific dimensions.

## Combining dimensions

In a quota preference configuration, you can combine dimensions in the following
ways:

- 

The configuration may contain *both* location dimensions and service-specific
dimensions. This is the highest order in precedence.

- 

The configuration may *only* contain location dimensions. This configuration
applies to all service-specific dimensions, except the ones explicitly
configured with method 1.

- 

The configuration may *only* contain service-specific dimensions. This configuration
applies to all locations except those explicitly configured with method 1 or 2.

- 

If the configuration contains *any* service-specific dimensions, it must contain
all service-specific dimensions.

- 

You can have configurations *without any* dimensions. Such configurations
apply to all locations and all service-specific dimensions, except the ones
explicitly configured.

## What's next

- [View and manage quotas](/docs/quotas/view-manage)

- [Set up quota alerts and monitoring](/docs/quotas/set-up-quota-alerts)

- [Quota and system limit terminology](/docs/quotas/terminology)