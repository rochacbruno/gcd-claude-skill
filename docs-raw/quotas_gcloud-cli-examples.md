# Manage quotas using the gcloud beta CLI

Source: https://berlin.devsitetest.how/docs/quotas/gcloud-cli-examples
Last updated: 2026-07-10

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












# Manage quotas using the gcloud beta CLI 






- On this page 
- [ Limitations ](#limitations)
- [ Before you begin ](#before_you_begin)

- [ Install and initialize the gcloud CLI ](#install_initialize_gcloud)
- [ Find your quota ID ](#find_your_quota_id)

- [ Example gcloud quota information commands ](#example_gcloud_quota_information_commands)

- [ View quota information for a particular service ](#view_quota_information_for_a_particular_service)
- [ View quota information for an organization ](#view_quota_information_for_an_organization)

- [ Example gcloud quota preferences commands ](#example_gcloud_quota_preferences_commands)

- [ Check for existing preferences ](#check_for_existing_preferences)
- [ Check for existing preferences with pending quota adjustments ](#check_for_existing_preferences_with_pending_quota_adjustments)
- [ Request a quota increase adjustment when a quota preference hasn't been set yet ](#request_a_quota_increase_adjustment_for_a_specific_region_when_a_quota_preference_hasnt_been_set)
- [ Request a quota increase adjustment when a quota preference has been set ](#request_a_quota_increase_adjustment_for_a_specific_region_when_a_quota_preference_has_been_set)
- [ View an existing quota preference ](#retrieve_an_existing_quota_preference)

- [ Enable quota adjuster through a client project ](#enable_quota_adjuster_through_client_project)
- [ Other services with quota-related gcloud CLI commands ](#other_services_with_gcloud_cmds)
- [ What's next ](#whats_next)
- 












The following sections contain example
[`gcloud beta quotas info`](/sdk/gcloud/reference/beta/quotas/info)
and
[`gcloud beta quotas preferences`](/sdk/gcloud/reference/beta/quotas/preferences)
commands. These commands allow you to view and manage `QuotaInfo` and
`QuotaPreference` resources.

You can use the Google Cloud CLI (gcloud CLI) to get current
quotas values and specify quota preferences for some Google Cloud Dedicated in Germany APIs and
services.

## Limitations

Cloud Quotas has the following limitations:

- 

In most cases, quota *increase* adjustments must be made at the
[project-level](/resource-manager/docs/creating-managing-projects).
A limited number of products support
[organization-level](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations)
quota increase adjustments. To see if a Google Cloud Dedicated in Germany product supports
organization-level quota increase adjustments, refer to the documentation
for that product.

- 

You can request quota *decrease* adjustments for
project-, organization-, and
[folder-level](/resource-manager/docs/cloud-platform-resource-hierarchy#folders)
quotas.

## Before you begin

Before you use the gcloud CLI, make sure that you
[install and initialize the gcloud CLI](#install_initialize_gcloud).

You may also need your ` QUOTA_ID ` value. If so, see the
[instructions for finding your quota ID](#find_your_quota_id).

### Install and initialize the gcloud CLI

To use the gcloud CLI for Cloud Quotas, be sure to install and
initialize components:

- 

[Install](/sdk/docs/install) the gcloud CLI.

If you're using Cloud Shell, you can skip this step because
gcloud CLI comes pre-installed.

- 

[Initialize](/sdk/docs/initialize) the gcloud CLI.

- 

[Install the beta component](/sdk/docs/components#alpha_and_beta_components)
by running the following command:


```
gcloud components install beta
```


### Find your quota ID

Several gcloud CLI commands in this document refer to your quota ID
value. You can find the quota ID using the Google Cloud Dedicated console, the
gcloud CLI, client libraries, or the REST API. This section shows how
to find the quota ID using either the Google Cloud Dedicated console or gcloud CLI.


[Console](#console) [gcloud](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the
**IAM & Admin  > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.berlin-build0.goog/iam-admin/quotas)

- 

Click filter_list **Filter** to filter for your service.

- 

If you don't see the **Limit name** column, click the icon
view_column **Column display options...**. Select
**Limit name** and click **OK**.

- 

The **Limit name** column shows the quota ID.




To find the quota ID value by using the gcloud CLI, run the
following command to list your quota information for the specified service:

- 

Enter the following gcloud CLI command in a terminal window:


```
gcloud beta quotas info list --service = SERVICE_NAME --project = PROJECT_ID_OR_NUMBER \ 
--billing-project = BILLING_PROJECT_ID_OR_NUMBER 
```


Replace the following:

- 

` SERVICE_NAME `: the service name with quotas that you want to
see—for example, the service name for Compute Engine is `compute.googleapis.com`.

- 

` PROJECT_ID_OR_NUMBER `: the project ID or project number.

To find your project ID using the Google Cloud Dedicated console, navigate to the
Resource Manager page:

[Go to Resource Manager](https://console.cloud.berlin-build0.goog/cloud-resource-manager)

- 

` BILLING_PROJECT_ID_OR_NUMBER `: the ID or project
number of the project whose Cloud Quotas API quota you want to
use for executing this command. This can be different from the
project containing the service that you're finding the quota ID
for.

If you already [set the billing project](/sdk/gcloud/reference#--billing-project)
when setting up the gcloud CLI, this flag is optional.
Otherwise, omitting it might cause a
[permission denied error](/docs/quotas/troubleshoot#gcloud_cli_errors).
For more information, see
[Set the quota project](/docs/quotas/set-quota-project#set-project-programmatically).

- 

The output from the `gcloud beta quotas info list` command contains text
similar to the following sample:


```
... 
"quotaInfos" : [ 
... 
{ 
"name" : "projects/PROJECT_NUMBER/locations/global/services/compute.googleapis.com/quotaInfos/CPUS-per-project-region" , 
** "quotaId" : "CPUS-per-project-region" ** , 
"metric" : "compute.googleapis.com/cpus" , 
"containerType" : "PROJECT" , 
"dimensions" : [ 
"region" 
], 
"dimensionsInfo" : [ 
{ 
"details" : { 
"value" : 20 
}, 
"applicableLocations" : [ 
"us-central1" , 
"us-central2" , 
"us-west1" , 
"us-east1" 
] 
... 
} 
] 
}, 
... 
] 
... 
```


- 

Look for the value that corresponds to `quotaId` and use it when specifying
` QUOTA_ID ` in the following sections.




## Example gcloud quota information commands

This section provides examples that show how to use `gcloud beta quotas info`
commands to view quota information for a particular service or for an
organization.

`QuotaInfo` is a read-only resource that provides metadata and quota value
information about a particular quota for a given project, folder or
organization.

### View quota information for a particular service

To view quota information for a particular service, run the following command:


```
gcloud beta quotas info describe QUOTA_ID --service = SERVICE_NAME \ 
--project = PROJECT_ID_OR_NUMBER --billing-project = BILLING_PROJECT_ID_OR_NUMBER 
```


Replace the following:

- ` QUOTA_ID `: the quota ID value.
To find this value, see [Find your quota ID](#find_your_quota_id).

- ` SERVICE_NAME `: the service name with quotas that you want
to see—for example, the service name for Compute Engine is
`compute.googleapis.com`.

- ` PROJECT_ID_OR_NUMBER `: the project ID or project number.

- 

` BILLING_PROJECT_ID_OR_NUMBER `: the ID or project number of
the project whose Cloud Quotas API quota you want to use for executing
this command. This can be different from the project containing the service
that you're viewing quota info for.

If you already [set the billing project](/sdk/gcloud/reference#--billing-project)
when setting up the gcloud CLI, this flag is optional.
Otherwise, omitting it might cause a
[permission denied error](/docs/quotas/troubleshoot#gcloud_cli_errors).
For more information, see
[Set the quota project](/docs/quotas/set-quota-project#set-project-programmatically).

### View quota information for an organization

To view the same service's quota details for an organization, run the following command:


```
gcloud beta quotas info list --service = SERVICE_NAME --organization = ORGANIZATION_ID \ 
--billing-project = BILLING_PROJECT_ID_OR_NUMBER 
```


Replace the following:

- ` SERVICE_NAME `: the service name with quotas that you want
to see—for example, the service name for Compute Engine is
`compute.googleapis.com`.

- ` ORGANIZATION_ID `: the ID of your organization.

- 

` BILLING_PROJECT_ID_OR_NUMBER `: the ID or project number of
the project whose Cloud Quotas API quota you want to use for executing
this command. This can be different from the project containing the service
that you're viewing quota info for.

If you already [set the billing project](/sdk/gcloud/reference#--billing-project)
when setting up the gcloud CLI, this flag is optional.
Otherwise, omitting it might cause a
[permission denied error](/docs/quotas/troubleshoot#gcloud_cli_errors).
For more information, see
[Set the quota project](/docs/quotas/set-quota-project#set-project-programmatically).

## Example gcloud quota preferences commands

This section provides examples that show how to use `gcloud beta quotas preferences`
commands to check existing quota preferences and adjust the quota value.

The `QuotaPreference` resource represents your preference for a particular
dimension combination. A dimension is an attribute that represents a region
or a zone, or a service-specific dimension, such as `gpu_family`
or `network_id`.

### Check for existing preferences

To check for existing preferences, run the following command:


```
gcloud beta quotas preferences list --project = PROJECT_ID_OR_NUMBER \ 
--billing-project = BILLING_PROJECT_ID_OR_NUMBER 
```


Replace the following:

- ` PROJECT_ID_OR_NUMBER ` : the project ID or project number.

- 

` BILLING_PROJECT_ID_OR_NUMBER `: the ID or project number of
the project whose Cloud Quotas API quota you want to use for executing
this command. This can be different from the project containing the service
that you're checking quota preferences for.

If you already [set the billing project](/sdk/gcloud/reference#--billing-project)
when setting up the gcloud CLI, this flag is optional.
Otherwise, omitting it might cause a
[permission denied error](/docs/quotas/troubleshoot#gcloud_cli_errors).
For more information, see
[Set the quota project](/docs/quotas/set-quota-project#set-project-programmatically).

### Check for existing preferences with pending quota adjustments

To check for existing preferences with pending quota adjustments, add the
`--reconciling-only=true` flag as shown in the following command:


```
gcloud beta quotas preferences list --project = PROJECT_ID_OR_NUMBER --reconciling-only = true \ 
--billing-project = BILLING_PROJECT_ID_OR_NUMBER 
```


Replace the following:

- ` PROJECT_ID_OR_NUMBER ` : the project ID or project number.

- 

` BILLING_PROJECT_ID_OR_NUMBER `: the ID or project number of
the project whose Cloud Quotas API quota you want to use for executing
this command. This can be different from the project containing the service
that you're checking quota preferences for.

If you already [set the billing project](/sdk/gcloud/reference#--billing-project)
when setting up the gcloud CLI, this flag is optional.
Otherwise, omitting it might cause a
[permission denied error](/docs/quotas/troubleshoot#gcloud_cli_errors).
For more information, see
[Set the quota project](/docs/quotas/set-quota-project#set-project-programmatically).

### Request a quota increase adjustment when a quota preference hasn't been set yet

To request a quota adjustment using the gcloud CLI, run the following
command:


```
gcloud beta quotas preferences create --project = PROJECT_ID_OR_NUMBER \ 
--service = SERVICE_NAME \ 
--quota-id = QUOTA_ID \ 
--dimensions = DIMENSIONS \ 
--preferred-value = PREFERRED_VALUE \ 
--billing-project = BILLING_PROJECT_ID_OR_NUMBER \ 
--email = EMAIL \ 
--justification = JUSTIFICATION \ 
--preference-id = PREFERENCE_ID 
```


Replace the following:


- ` PROJECT_ID_OR_NUMBER `: the project ID or project number.

- ` SERVICE_NAME `: the service name with quotas that you want
to adjust—for example, the service name for Compute Engine is
`compute.googleapis.com`.

- ` QUOTA_ID `: the quota ID value.
To find this value, see
[Find your quota ID](/docs/quotas/gcloud-cli-examples#find_your_quota_id).

- ` DIMENSIONS `: the dimensions to adjust, specified as a
comma-separated list of key-value pairs—for example,
`region=us-east4,gpu_family=NVIDIA_H100`.
For more information on quota dimensions, see
[Configure Cloud Quotas dimensions](/docs/quotas/configure-dimensions).

- ` PREFERRED_VALUE `: the preferred quota value.

- ` BILLING_PROJECT_ID_OR_NUMBER `: the ID or project number of the
project whose Cloud Quotas API quota you want to use for executing this command. This can be
different from the project containing the service that you're requesting a quota adjustment
for.



If you already [set the billing project](/sdk/gcloud/reference#--billing-project)
when setting up the gcloud CLI, this flag is optional.
Otherwise, omitting it might cause a
[permission denied error](/docs/quotas/troubleshoot#gcloud_cli_errors).
For more information, see
[Set the quota project](/docs/quotas/set-quota-project#set-project-programmatically).



- ` EMAIL `: an email address that can be used as a contact, in
case Google Cloud Dedicated in Germany needs more information before additional quota can be granted.

- ` JUSTIFICATION `: an optional string that explains your request.

- ` PREFERENCE_ID `: an optional preference ID; if you don't
specify a preference ID, the API generates a Universally Unique Identifier
(UUID) for you.

The output looks similar to the following:


```
{ 
"createTime" : " CREATE_TIME " , 
"dimensions" :{ 
" DIMENSION_KEY_1 " : " DIMENSION_VALUE_1 " , 
" DIMENSION_KEY_2 " : " DIMENSION_VALUE_2 " 
}, 
"etag" : " ETAG_VALUE " , 
"name" : "projects/ PROJECT_ID_OR_NUMBER /locations/global/quotaPreferences/ PREFERENCE_ID " , 
"quotaConfig" :{ 
"grantedValue" : " GRANTED_VALUE " , 
"preferredValue" : " PREFERRED_VALUE " , 
"traceId" : " TRACE_ID " 
}, 
"quotaId" : " QUOTA_ID " , 
"reconciling" : true , 
"service" : " SERVICE_NAME " , 
"updateTime" : " UPDATE_TIME " , 
} 
```


### Request a quota increase adjustment when a quota preference has been set

To request a quota increase adjustment for a specific region and there is already a
preference, run the following command:


```
gcloud beta quotas preferences update PREFERENCE_ID --preferred-value = PREFERRED_VALUE \ 
--quota-id = QUOTA_ID --service = SERVICE_NAME --project = PROJECT_ID_OR_NUMBER \ 
--billing-project = BILLING_PROJECT_ID_OR_NUMBER --email = EMAIL \ 
--justification = JUSTIFICATION 
```


Replace the following:

- ` PREFERENCE_ID `: the preference ID, which is required as
the first argument when using the `gcloud beta quotas preferences update`
command.

- ` PREFERRED_VALUE `: the preferred quota value.

- ` QUOTA_ID `: the quota ID value.
To find this value, see [Find your quota ID](#find_your_quota_id).

- ` SERVICE_NAME `: the service name with quotas that you want
to see—for example, the service name for Compute Engine is
`compute.googleapis.com`.

- ` PROJECT_ID_OR_NUMBER `: the project ID or project number.

- 

` BILLING_PROJECT_ID_OR_NUMBER `: the ID or project number of
the project whose Cloud Quotas API quota you want to use for executing
this command. This can be different from the project containing the service
that you're requesting a quota adjustment for.

If you already [set the billing project](/sdk/gcloud/reference#--billing-project)
when setting up the gcloud CLI, this flag is optional.
Otherwise, omitting it might cause a
[permission denied error](/docs/quotas/troubleshoot#gcloud_cli_errors).
For more information, see
[Set the quota project](/docs/quotas/set-quota-project#set-project-programmatically).

- 

` EMAIL `: an email address that can be used as a contact, in
case Google Cloud Dedicated in Germany needs more information before additional quota can be granted.

- 

` JUSTIFICATION `: an optional string that explains your request.

### View an existing quota preference

To view the details of the quota preference that you just created,
run the following command:


```
gcloud beta quotas preferences describe PREFERENCE_ID \ 
--project = PROJECT_ID_OR_NUMBER \ 
--billing-project = BILLING_PROJECT_ID_OR_NUMBER 
```


Replace the following:

- ` PREFERENCE_ID `: the preference ID, which is required as
the first argument when using the `gcloud beta quotas preferences describe`
command.

- ` PROJECT_ID_OR_NUMBER `: the project ID or project number.

- 

` BILLING_PROJECT_ID_OR_NUMBER `: the ID or project number of
the project whose Cloud Quotas API quota you want to use for executing
this command. This can be different from the project containing the service
that you're viewing the quota preference for.

If you already [set the billing project](/sdk/gcloud/reference#--billing-project)
when setting up the gcloud CLI, this flag is optional.
Otherwise, omitting it might cause a
[permission denied error](/docs/quotas/troubleshoot#gcloud_cli_errors).
For more information, see
[Set the quota project](/docs/quotas/set-quota-project#set-project-programmatically).

The output would contain data specific to your configuration and look similar
to the following example output:


```
createTime : ' CREATE_TIME ' 
dimensions : 
gpu_family : NVIDIA_H100 
region : us-east4 
etag : ETAG_VALUE 
name : projects/12345/locations/global/quotaPreferences/ PREFERENCE_ID 
quotaConfig : 
grantedValue : '0' 
preferredValue : '128' 
traceId : TRACE_ID 
quotaId : GPUS-PER-GPU-FAMILY-per-project-region 
reconciling : true 
service : compute.googleapis.com 
updateTime : ' UPDATE_TIME ' 
```


## Enable quota adjuster through a client project

A client project refers to the project used by an application or user to access
and interact with Google Cloud Dedicated in Germany resources, while a resource project is the
underlying project where those resources are stored and managed.

To enable quota adjuster through a client project using
the gcloud CLI, follow these steps:

- 

Create a client project:


```
gcloud projects create CLIENT_PROJECT_ID 
gcloud config set project CLIENT_PROJECT_ID 
```


Replace ` CLIENT_PROJECT_ID ` with the ID for the project
you want to create. Project IDs are immutable and can be set only during
project creation. They must start with a lowercase letter and can have
lowercase ASCII letters, digits or hyphens. Project IDs must be between
6 and 30 characters.

- 

Enable the Cloud Quotas API on the client project:


```
gcloud services enable cloudquotas.googleapis.com
```


- 

Create a
[service account](/iam/docs/service-accounts-create) in the client project:


```
gcloud iam service-accounts create SA_NAME \
--display-name SA_DISPLAY_NAME \
--project= CLIENT_PROJECT_ID 
```


Replace the following:

- ` SA_NAME `: the internal name of the new service account.
Used to generate an IAM_ACCOUNT (an IAM internal email
address used as an identifier of service account), which must be passed to
subsequent commands.

- ` SA_DISPLAY_NAME `: the display name of the
service account.

- ` CLIENT_PROJECT_ID `: the ID of the client project.

- 

Create a [service account key](/iam/docs/keys-create-delete):



```
gcloud iam service-accounts keys create KEY_FILE \
--iam-account= SA_NAME @ CLIENT_PROJECT_ID .eu0.iam.gserviceaccount.com
```


Replace the following:

- ` KEY_FILE `: the path to the JSON service account key file.

- ` SA_NAME @ CLIENT_PROJECT_ID .eu0.iam.gserviceaccount.com`:
the service account email address.

- 

Grant IAM permissions to the service account:


```
gcloud projects add-iam-policy-binding CLIENT_PROJECT_ID \
--member="serviceAccount: SA_NAME @ CLIENT_PROJECT_ID .eu0.iam.gserviceaccount.com" \
--role="roles/serviceusage.serviceUsageConsumer"

gcloud projects add-iam-policy-binding RESOURCE_PROJECT_ID \
--member="serviceAccount: SA_NAME @ CLIENT_PROJECT_ID .eu0.iam.gserviceaccount.com" \
--role="roles/cloudquotas.admin"
```


Replace the following:

- ` CLIENT_PROJECT_ID `: the ID of the client project.

- ` RESOURCE_PROJECT_ID `: the ID of the resource project.

- ` SA_NAME @ CLIENT_PROJECT_ID .eu0.iam.gserviceaccount.com`:
the service account email address.

- 

Activate the service account using the service account key that you created earlier:


```
gcloud auth activate-service-account --key-file= KEY_FILE 
```


- 

Enable quota adjuster on your resource project by specifying
the project and the enablement setting:


```
gcloud beta quotas adjuster settings update --project= RESOURCE_PROJECT_ID \
--enablement=**enabled**
```


The enablement setting is required when using the gcloud CLI and
must be set to `enabled` or `disabled`.

- 

Optional: To view the current quota adjuster settings, run the
following command:


```
gcloud beta quotas adjuster settings describe --project= RESOURCE_PROJECT_ID 
```


The output is similar to the following example:


```
enablement: ENABLED
etag: 8izmJp6EI__mOfLyhkQU9
name: projects/ RESOURCE_PROJECT_ID /locations/global/quotaAdjusterSettings
updateTime: '2025-01-10T17:22:37.883221181Z'
```


To enable quota adjuster for multiple client projects, follow the previous
steps 5 to 8. When doing so, make sure the following conditions are met:

- The Cloud Quotas API is enabled on the client project.

- The service account has the `cloudquotas.admin` IAM role on
all the resource projects that you want to enable
quota adjuster on.

## Other services with quota-related gcloud CLI commands

In addition to `gcloud beta quotas`, some services have their own command-line access
to quota and resource usage information.

For example, Compute Engine lets you access quota information. For details,
see the following Compute Engine sections:

- [Allocation quotas](/compute/quotas#checking_your_quota) 

- The [gcloud CLI compute overview](/compute/docs/gcloud-compute)

- The [gcloud CLI compute](/sdk/gcloud/reference/compute)
section of the Google Cloud SDK reference

## What's next

- 

To troubleshoot issues with `gcloud beta quotas` commands,
see [Troubleshooting gcloud CLI errors](/docs/quotas/troubleshoot#gcloud_cli_errors).

- 

For details about `gcloud beta quotas` commands and flags, see the
[gcloud beta quotas](/sdk/gcloud/reference/beta/quotas) 
section of the Google Cloud CLI reference.

- 

For more information about quotas terminology, see
[Understand quota and system limit terminology](/docs/quotas/terminology).