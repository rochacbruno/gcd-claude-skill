# Understanding and using Access Transparency logs

Source: https://berlin.devsitetest.how/assured-workloads/access-transparency/docs/reading-logs
Last updated: 2026-10-26

- 





[

Home

](https://berlin.devsitetest.how/)






- 








[

Access Transparency

](https://berlin.devsitetest.how/assured-workloads/access-transparency/docs)






- 








[

Guides

](https://berlin.devsitetest.how/assured-workloads/access-transparency/docs/overview)

























# Understanding and using Access Transparency logs



This page describes the contents of Access Transparency log entries and how
to view and use them.

## Access Transparency logs in detail

Access Transparency logs can be integrated with your existing
security information and event management (SIEM) tools to automate your audits
of personnel when they access your content. Access Transparency
logs are available in the Google Cloud Dedicated console alongside your Cloud Audit Logs.

Access Transparency log entries include the following types of details:

- The affected resource and action.

- The time of the action.

- The [reasons](#justification-reason-codes) for the action (for example, the
case number associated with a customer support request).

- Data about who is acting on the content (for example, the 
personnel's location).

## Enabling Access Transparency

For information about enabling Access Transparency for your Google Cloud Dedicated in Germany organization,
see [Enabling Access Transparency](/assured-workloads/access-transparency/docs/enable).

## Viewing Access Transparency logs

After you've configured Access Transparency for your Google Cloud Dedicated
organization, you can set controls for who can access the Access Transparency logs by
assigning a user or group the **Private Logs Viewer** role.

## Sample Access Transparency log entry

The following is an example of an Access Transparency log entry:


```
{ 
insertId : "abcdefg12345" 
jsonPayload : { 
@ type : "type.googleapis.com/google.cloud.audit.TransparencyLog" 
location : { 
principalOfficeCountry : "US" 
principalEmployingEntity : "Google LLC" 
principalPhysicalLocationCountry : "CA" 
} 
principalJobTitle : "Engineering" 
product : [ 
0 : "Cloud Storage" 
] 
reason : [ 
detail : "Case number: bar123" 
type : "CUSTOMER_INITIATED_SUPPORT" 
] 
permissionDetails :[ 
0 : { 
permissionType : "DATA_READ" 
logAccessed : true 
} 
1 : { 
permissionType : "ADMIN_READ" 
} 
] 
eventId : "asdfg12345asdfg12345asdfg12345" 
accesses : [ 
0 : { 
methodName : "GoogleInternal.Read" 
resourceName : "//googleapis.com/storage/buckets/ BUCKET_NAME /objects/foo123" 
} 
] 
accessApprovals : [ 
0 : "projects/123/approvalRequests/abcdef12345" 
] 
} 
logName : "projects/ PROJECT_ID /logs/cloudaudit.googleapis.com %2F access_transparency" 
operation : { 
id : "12345xyz" 
} 
receiveTimestamp : "2017-12-18T16:06:37.400577736Z" 
resource : { 
labels : { 
project_id : "1234567890" 
} 
type : "project" 
} 
severity : "NOTICE" 
timestamp : "2017-12-18T16:06:24.660001Z" 
} 
```


## Log field descriptions




| 
Field | 
Description | 
|



| 
`insertId` | 
Unique identifier for the log. | 
|

| 
`@type` | 
Access Transparency log identifier. | 
|

| 
`principalOfficeCountry` | 
ISO 3166-1 alpha-2 country code of country in which the accessor has
a permanent desk, `??` if location not available, or
3-character continent identifier where personnel are in a
low-population country. | 
|

| 
`principalEmployingEntity` | 
The entity that employs the personnel making the access

| 
|

| 
`principalPhysicalLocationCountry` | 
ISO 3166-1 alpha-2 country code of country from which access was made,
`??` if location not available, or 3-character continent
identifier where personnel are in a low-population country. | 
|

| 
`principalJobTitle` | 
The job family of the identity making the access.


When the job title is `Support Agent`, the actor is an AI support agent, and `principalPhysicalLocationCountry` and `principalOfficeCountry` are not provided (`??`).
| 
|

| 
`product` | 
Customer's Google Cloud Dedicated in Germany product that was accessed. | 
|

| 
`reason:detail` | 
Details of the reason, for example, a support ticket ID. | 
|

| 
`reason:type` | 
Access
[reason type](#justification-reason-codes)
(for example, `CUSTOMER_INITIATED_SUPPORT)`. | 
|

| 
`permissionDetails` | 
Details about permissions linked to an access. Up to two permissionType
details may be present. For more information, see [
Values for permission details.](#permissiondetails) | 
|

| 
`accesses:methodName` | 
What type of access was made. For example, `GoogleInternal.Read`.
For more information about the methods that can appear in the
`methodName` field, see
[Values for `accesses: methodName` field](#methodnames).
| 
|

| 
`accesses:resourceName` | 
[Name](https://berlin.devsitetest.how/apis/design/resource_names)
of resource that was accessed. | 
|


| 
`logName` | 
Name of the log location. | 
|

| 
`operation:id` | 
Log cluster ID. | 
|

| 
`receiveTimestamp` | 
Time the access was received by the logging pipeline. | 
|

| 
`project_id` | 
Project associated with the resource that was accessed. | 
|

| 
`type` | 
Type of resource that was accessed (for example, `project`). | 
|

| 
`eventId` | 
Unique event ID associated with a single access event justification
(for example, a single support case). All accesses logged to the same
justification have the same `event_id` value. | 
|

| 
`severity` | 
Log severity. | 
|

| 
`timestamp` | 
Time the log was written. | 
|



### Values for permissionDetails fields

The following permission details are available in Access Transparency logs:

- 

**permissionType**: Indicates the
[Identity and Access Management (IAM) Permission type](/logging/docs/audit/configure-data-access#permission-types)
associated with the data access by the administrator.
For example, permission types for each public API method for Cloud SQL can be
found [in the SQL documentation](/sql/docs/mysql/audit-logging). Permission
types indicate the maximum permission present, even if an access would have been
possible with a lesser permission type.

- 

**logAccessed**: This field indicates if an administrator or data read access
permission is limited to log accesses. For example a data_read access to
Observability Analytics logs is accompanied by "logAccessed = true", indicating
that the data_read permission is limited to log data. This field is omitted if
the access is not a log.



| 
IAM Permission Type | 
Description | 
Examples | 
|




| 
`ADMIN_READ` | 
Signifies a read access limited to a configuration, log, or similar data. | 
See [IAM Permission type](/logging/docs/audit/configure-data-access#permission-types) for more details. | 
|

| 
`ADMIN_WRITE` | 
Signifies a read or write access limited to a configuration, log, or similar data. | 
See [IAM Permission type](/logging/docs/audit/configure-data-access#permission-types) for more details. | 
|

| 
`DATA_READ` | 
Signifies a read access that *may* contain [Customer Data](https://berlin.devsitetest.how/terms). An access with data_read permission type indicates the administrator had the permission to access Customer Data; however, it is not confirmation that Customer Data was accessed. | 
See [IAM Permission type](/logging/docs/audit/configure-data-access#permission-types) for more details. | 
|

| 
`DATA_WRITE` | 
Signifies a read or write access that *may* contain [Customer Data](https://berlin.devsitetest.how/terms). An access with data_write permission type indicates the administrator *may* have included a permission to access at least resource of Customer Data. See [IAM Permission type](/logging/docs/audit/configure-data-access#permission-types) for more details. | 
| 
|





| 
logAccessed | 
Description | 
|




| 
`true` | 
Signifies an access limited to **read access** of logging data. This property extends the permissionType field. Accesses labeled true indicate the access is to logging data only, without access to the data directly. | 
|



### Values for `accesses:methodNames` field

The following methods can appear in the `accesses:methodNames` field in Access Transparency logs:

- **Standard methods**: These methods are `List`, `Get`, `Create`, `Update`, and `Delete`. For more information, see [Standard methods](/apis/design/standard_methods).

- **Custom methods**: Custom methods refer to API methods besides the 5 standard methods. Common custom methods include `Cancel`, `BatchGet`, `Move`, `Search`, and `Undelete`. For more information, see [Custom methods](/apis/design/custom_methods).

- **GoogleInternal methods**: The following are examples of `GoogleInternal` methods that appear in the `accesses:methodNames` field:



| 
Method name | 
Description | 
Examples | 
|




| 
`GoogleInternal.Read` | 
Signifies a read action performed on customer content with a valid business justification. The read action occurs using an internal API that is specifically designed for administering Google Cloud Dedicated in Germany services. This method doesn't mutate customer content. | 
Reading IAM permissions. | 
|

| 
`GoogleInternal.Write` | 
Signifies a write action performed on customer content with a valid business justification. The write action occurs using an internal API that is specifically designed for administering Google Cloud Dedicated in Germany services. This method can update customer content and/or configurations. | 

- Setting IAM permissions for a resource.
- Suspending a Compute Engine instance.
| 
|

| 
`GoogleInternal.Create` | 
Signifies a create action performed on customer content with a valid business justification. The create action occurs using an internal API that is specifically designed for administering Google Cloud Dedicated in Germany services. This method creates new customer content. | 

- Creating a Cloud Storage bucket.
- Creating a Pub/Sub topic.
| 
|

| 
`GoogleInternal.Delete` | 
Signifies a delete action performed on customer content using an internal API specifically designed for administering Google Cloud Dedicated in Germany services. This method mutates customer content and/or configurations. | 

- Deleting a Cloud Storage object.
- Deleting a BigQuery table.
| 
|

| 
`GoogleInternal.List` | 
Signifies a list action performed on customer content with a valid business justification. The list action occurs using an internal API that is specifically designed for administering Google Cloud Dedicated in Germany services. This method doesn't mutate customer content or configurations. | 

- Listing a customer's Compute Engine instances.
- Listing a customer's Dataflow jobs.
| 
|

| 
`GoogleInternal.Update` | 
Signifies a modification performed on customer content with a valid business justification. The update action occurs using an internal API that is specifically designed for administering Google Cloud Dedicated in Germany services. This method mutates customer content and/or configurations. | 
Updating HMAC keys in Cloud Storage. | 
|

| 
`GoogleInternal.Get` | 
Signifies a get action performed on customer content with a valid business justification. The get action occurs using an internal API that is specifically designed for administering Google Cloud Dedicated in Germany services. This method doesn't mutate customer content or configurations. | 

- Retrieving IAM policy for a resource.
- Retrieving a customer's Dataflow job.
| 
|

| 
`GoogleInternal.Query` | 
Signifies a query action performed on customer content with a valid business justification. The query action occurs using an internal API that is specifically designed for administering Google Cloud Dedicated in Germany services. This method doesn't mutate customer content or configurations. | 

- Running a BigQuery query.
- AI Platform debugging console lookup on customer content.
| 
|



The `GoogleInternal` accesses are strictly restricted to authorized personnel
for justified and auditable access. The presence of a method doesn't indicate
availability to all roles.

## Justification reason codes





| 
**Reason**
| 
**Description**
| 
|






| 
`CUSTOMER_INITIATED_SUPPORT`
| 
Customer-initiated support, for example, "Case Number: ####".
| 
|


| 
`THIRD_PARTY_DATA_REQUEST`
| 
-initiated access in response to a legal request or legal process,
including when responding to legal process from the customer that requires
to access the customer's own data.
| 
|



| 
`CLOUD_INITIATED_ACCESS`
| 
Access initiated by the cloud provider for any reason related to
infrastructure management. This includes system troubleshooting, security
and compliance reviews, and emergency responses to maintain service
reliability.
| 
|

| 
`REASON_UNSPECIFIED`
| 
A specific justification is not available. This might be represented as
an empty string in some logging systems.
| 
|






## Monitoring Access Transparency logs

You can monitor Access Transparency logs by using the Cloud Monitoring API.
To get started, see the [Monitoring documentation](/monitoring/docs).

You can set up a
[logs-based metric](/logging/docs/logs-based-metrics/counter-metrics) and then
set up an
[alerting policy](/logging/docs/logs-based-metrics/charts-and-alerts#alert-on-lbm)
to give you timely awareness of issues surfaced by these logs.
For example, you can create a logs-based metric that captures
personnel accesses of your content and then create an alerting
policy in Monitoring that lets you know if the number of
accesses in a
given period exceeds a specified threshold.