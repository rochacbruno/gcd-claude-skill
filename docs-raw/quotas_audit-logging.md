# Cloud Quotas audit logging

Source: https://berlin.devsitetest.how/docs/quotas/audit-logging
Last updated: 2026-07-17

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












# Cloud Quotas audit logging 






- On this page ** 
- [ Service name ](#service_name)
- [ Methods by permission type ](#permission-type)
- [ API interface audit logs ](#api-interface-reference)

- [ google.api.cloudquotas.v1.CloudQuotas ](#google.api.cloudquotas.v1.CloudQuotas)
- [ google.api.cloudquotas.v1beta.CloudQuotas ](#google.api.cloudquotas.v1beta.CloudQuotas)
- [ google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager ](#google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager)

- [ System events ](#system-events)
- [ Methods that don't produce audit logs ](#exempt-methods)
- [ What's next ](#whats_next)
- 










This document lists the audited methods for Cloud Quotas. Google Cloud Dedicated in Germany services
generate audit logs that record administrative and access activities within your Google Cloud Dedicated in Germany resources.
For more information about Cloud Audit Logs, see the following:

- [Types of audit logs](/logging/docs/audit#types)

- [Audit log entry structure](/logging/docs/audit#audit_log_entry_structure)

- [Storing and routing audit logs](/logging/docs/audit#storing_and_routing_audit_logs)

- [Cloud Logging pricing summary](/stackdriver/pricing#logs-pricing-summary)

- [Enable Data Access audit logs](/logging/docs/audit/configure-data-access)

## Service name 

To view the Cloud Quotas audit logs, do the following:

- 

In the Google Cloud Dedicated console, go to the Logs Explorer page:



[Go to Logs Explorer](https://console.cloud.berlin-build0.goog/logs/query)

- 

Copy and paste the following query into the Query** field of the
Logs Explorer, and then click **Run query**.


```
protoPayload . serviceName = "cloudquotas.googleapis.com" 

```


## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum
that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`,
`DATA_READ`, or `DATA_WRITE`. When you call a method,
Cloud Quotas generates an audit log whose category is dependent on the
`type` property of the permission required to perform the method.

Methods that require an IAM permission with the `type` property value
of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate
[Data Access](/logging/docs/audit#data-access) audit logs.

Methods that require an IAM permission with the `type` property value
of `ADMIN_WRITE` generate
[Admin Activity](/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs).
These methods usually generate two audit log entries: one when the operation starts and
another when it ends. For more information see [Audit logs for long-running operations](/logging/docs/audit/understanding-audit-logs#lro).



| 
Permission type | 
Methods | 
|

| 
`ADMIN_ READ` | 
`google. api. cloudquotas. v1. Cloud Quotas. Get Quota Info`
`google. api. cloudquotas. v1. Cloud Quotas. Get Quota Preference`
`google. api. cloudquotas. v1. Cloud Quotas. List Quota Infos`
`google.api.cloudquotas.v1.CloudQuotas.ListQuotaPreferences`
`google.api.cloudquotas.v1beta.CloudQuotas.GetQuotaInfo`
`google.api.cloudquotas.v1beta.CloudQuotas.GetQuotaPreference`
`google.api.cloudquotas.v1beta.CloudQuotas.ListQuotaInfos`
`google.api.cloudquotas.v1beta.CloudQuotas.ListQuotaPreferences`
`google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager.GetQuotaAdjusterSettings` | 
|


| 
`ADMIN_WRITE` | 
`google.api.cloudquotas.v1.CloudQuotas.CreateQuotaPreference`
`google.api.cloudquotas.v1.CloudQuotas.UpdateQuotaPreference`
`google.api.cloudquotas.v1beta.CloudQuotas.CreateQuotaPreference`
`google.api.cloudquotas.v1beta.CloudQuotas.UpdateQuotaPreference`
`google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager.UpdateQuotaAdjusterSettings` | 
|



## API interface audit logs

For information about how and which permissions are evaluated for each method,
see the Identity and Access Management documentation for Cloud Quotas.

### `google.api.cloudquotas.v1.CloudQuotas`

The following audit logs are associated with methods belonging to
`google.api.cloudquotas.v1.CloudQuotas`.

#### `CreateQuotaPreference`


- **Method**: `google.api.cloudquotas.v1.CloudQuotas.CreateQuotaPreference`


- **Audit log type**: [Admin activity](/logging/docs/audit#admin-activity)


- **Permissions**: 

- `cloudquotas.quotas.update - ADMIN_WRITE`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1.CloudQuotas.CreateQuotaPreference"`

#### `GetQuotaInfo`


- **Method**: `google.api.cloudquotas.v1.CloudQuotas.GetQuotaInfo`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1.CloudQuotas.GetQuotaInfo"`

#### `GetQuotaPreference`


- **Method**: `google.api.cloudquotas.v1.CloudQuotas.GetQuotaPreference`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1.CloudQuotas.GetQuotaPreference"`

#### `ListQuotaInfos`


- **Method**: `google.api.cloudquotas.v1.CloudQuotas.ListQuotaInfos`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1.CloudQuotas.ListQuotaInfos"`

#### `ListQuotaPreferences`


- **Method**: `google.api.cloudquotas.v1.CloudQuotas.ListQuotaPreferences`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1.CloudQuotas.ListQuotaPreferences"`

#### `UpdateQuotaPreference`


- **Method**: `google.api.cloudquotas.v1.CloudQuotas.UpdateQuotaPreference`


- **Audit log type**: [Admin activity](/logging/docs/audit#admin-activity)


- **Permissions**: 

- `cloudquotas.quotas.update - ADMIN_WRITE`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1.CloudQuotas.UpdateQuotaPreference"`

### `google.api.cloudquotas.v1beta.CloudQuotas`

The following audit logs are associated with methods belonging to
`google.api.cloudquotas.v1beta.CloudQuotas`.

#### `CreateQuotaPreference`


- **Method**: `google.api.cloudquotas.v1beta.CloudQuotas.CreateQuotaPreference`


- **Audit log type**: [Admin activity](/logging/docs/audit#admin-activity)


- **Permissions**: 

- `cloudquotas.quotas.update - ADMIN_WRITE`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1beta.CloudQuotas.CreateQuotaPreference"`

#### `GetQuotaInfo`


- **Method**: `google.api.cloudquotas.v1beta.CloudQuotas.GetQuotaInfo`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1beta.CloudQuotas.GetQuotaInfo"`

#### `GetQuotaPreference`


- **Method**: `google.api.cloudquotas.v1beta.CloudQuotas.GetQuotaPreference`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1beta.CloudQuotas.GetQuotaPreference"`

#### `ListQuotaInfos`


- **Method**: `google.api.cloudquotas.v1beta.CloudQuotas.ListQuotaInfos`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1beta.CloudQuotas.ListQuotaInfos"`

#### `ListQuotaPreferences`


- **Method**: `google.api.cloudquotas.v1beta.CloudQuotas.ListQuotaPreferences`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1beta.CloudQuotas.ListQuotaPreferences"`

#### `UpdateQuotaPreference`


- **Method**: `google.api.cloudquotas.v1beta.CloudQuotas.UpdateQuotaPreference`


- **Audit log type**: [Admin activity](/logging/docs/audit#admin-activity)


- **Permissions**: 

- `cloudquotas.quotas.update - ADMIN_WRITE`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1beta.CloudQuotas.UpdateQuotaPreference"`

### `google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager`

The following audit logs are associated with methods belonging to
`google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager`.

#### `GetQuotaAdjusterSettings`


- **Method**: `google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager.GetQuotaAdjusterSettings`


- **Audit log type**: [Data access](/logging/docs/audit#data-access)


- **Permissions**: 

- `cloudquotas.quotas.get - ADMIN_READ`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager.GetQuotaAdjusterSettings"`

#### `UpdateQuotaAdjusterSettings`


- **Method**: `google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager.UpdateQuotaAdjusterSettings`


- **Audit log type**: [Admin activity](/logging/docs/audit#admin-activity)


- **Permissions**: 

- `cloudquotas.quotas.update - ADMIN_WRITE`


- **Method is a long-running or streaming operation**:
No.


- **Filter for this method**: `protoPayload.methodName="google.api.cloudquotas.v1beta.QuotaAdjusterSettingsManager.UpdateQuotaAdjusterSettings"`

## System events

System Event audit logs are generated by GCP systems, not
direct user action. For more information, see
[System Event audit logs](/logging/docs/audit#system-event).



| 
Method Name | 
Filter For This Event | 
Notes | 
|

| 
google.cloud.quotaadjuster.v1main.QuotaAdjusterService.AutoAdjustQuota | 

`protoPayload.methodName="google.cloud.quotaadjuster.v1main.QuotaAdjusterService.AutoAdjustQuota"`
| 
| 
|



## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following
reasons:


- It is a high volume method involving significant log generation and storage
costs.

- It has low auditing value.

- Another audit or platform log already provides method coverage.

The following methods don't produce audit logs:

- `google.api.cloudquotas.v1.GdcCloudQuotas.GetGdcQuotaInfo`
- `google.api.cloudquotas.v1.GdcCloudQuotas.ListGdcQuotaInfos`
- `google.api.cloudquotas.v1beta.GdcCloudQuotas.GetGdcQuotaInfo`
- `google.api.cloudquotas.v1beta.GdcCloudQuotas.ListGdcQuotaInfos`

## What's next

- [Set up quota alerts and monitoring](/docs/quotas/set-up-quota-alerts)

- [Troubleshoot quota errors](/docs/quotas/troubleshoot)

- [Quota permissions](/docs/quotas/permissions)