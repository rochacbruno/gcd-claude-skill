# Manage backups

Source: https://documentation.s3ns.fr/bigtable/docs/managing-backups
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/bigtable/docs/tpc-differences) for more details.














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

Databases

](https://documentation.s3ns.fr/docs/databases)






- 








[

Bigtable

](https://documentation.s3ns.fr/bigtable/docs)






- 








[

Guides

](https://documentation.s3ns.fr/bigtable/docs/overview)

























# Manage backups



Bigtable backups help you protect your tables against accidental data
loss, corruption, or disaster scenarios. You can create, copy, restore, and
monitor these backups using the Cloud de Confiance console, the Google Cloud CLI, or the
Cloud Bigtable [client libraries](/bigtable/docs/reference/libraries).

## Before you begin

Before you begin, review [Backups](/bigtable/docs/backups), and see
[Editions overview](/bigtable/docs/editions-overview) for features that
are available only in the Enterprise Plus edition.

Make sure that you or the user account that you are using have the
[required permissions](/bigtable/docs/backups#access-control) for the action you need to perform.

If you plan to use the gcloud CLI,
[install the gcloud CLI for Bigtable](/bigtable/docs/installing-cloud-sdk).

## Use automated backup

You can use the gcloud CLI or the Cloud de Confiance console to enable
automated backup. Automated backup creates a daily backup of your table with a
default retention period of seven days. To modify the
retention period in a table's automated backup policy or to select cluster
locations where the automated backup is enabled in the Enterprise Plus edition,
see [Update an automated backup policy](#update-automated-backup).

The steps to [delete](#delete), [update](#modify),
[copy](#copy-backup), and [restore](#restoring-backup) a backup are the same
whether the backup is created manually or as a result of automated backup.

You can extend the expiration date of a backup or backup copy. For more
information, see [Modify a backup or backup copy](#modify).

If you plan to enable automated backup, consider the following factors:

- If a cluster is added to an instance that contains a table with automated
backup enabled, daily backups aren't created on the added cluster. To create
daily backups on all clusters, including the newly added cluster, disable
automated backup for the table, and then re-enable automated backup.

- If a table with automated backup enabled is deleted and subsequently
undeleted, you need to re-enable automated backup on the recovered
table.

- Restoring an automated backup of a table doesn't automatically enable
automated backup on the restored table. You need to manually enable automated
backup.

### Enable automated backup

You can enable automatic backup by using the console or the
Google Cloud CLI. When automated backup is enabled, Bigtable
creates a standard backup of the table each day on each cluster in the instance.
In the Enterprise Plus edition, you can selectively configure automated backups
for clusters in specific locations.

You can't use automated backup to create hot backups.

Backups that are created as part of automated backup are assigned IDs that begin
with `auto`. For example, a table with an ID of `my-table` would have an
automated backup ID like`auto.my-table.c7x3.20230220-145537`, where `my-table`
is the truncated table ID, `c7x3` is the unique hash ID, and `20230220-145537`
is the date and time in UTC format.

To create a new table with automated backup enabled, see [Create and manage
tables](/bigtable/docs/managing-tables).



### Console

- 

In the Cloud de Confiance console, open the list of Bigtable instances.

[
Open the instance list
](https://console.cloud.s3nscloud.fr/bigtable/instances)

- 

Click the instance with the table you want to back up.

- 

Click **Tables** in the left pane.

The **Tables** page displays a list of tables in the instance.

- 

In the **Automated backup** column for the table, click **Enable**. It
can take up to an hour for Bigtable to start creating backups.

Optional: You can update the automated backup policy to specify a custom
retention period for automated backups. In the Enterprise Plus edition,
you can enable automated backups for clusters in specific locations.
For more information, see
[Update an automated backup policy](#update-automated-backup).



### gcloud

To enable automated backup for a table, run the [`gcloud bigtable
tables update`](/sdk/gcloud/reference/bigtable/instances/tables/update) command. For more information about enabling
automated backup when creating a table, see [Create a table](/bigtable/docs/managing-tables#create-table).

After the automated backup policy is enabled for a table, the updated
configuration can take up to an hour to take effect.


```
gcloud bigtable tables update TABLE_ID \
--instance= INSTANCE_ID \
--enable-automated-backup
```


Replace the following:

- TABLE_ID : ID of the table to be backed up.

- INSTANCE_ID : 
The permanent identifier for the instance.

Optional: You can update the automated backup policy to specify a custom
retention period for automated backups. In the Enterprise Plus edition,
you can enable automated backups for clusters in specific locations.
For more information, see
[Update an automated backup policy](#update-automated-backup).



### Disable automated backup

After the automated backup policy is disabled for a table, the updated
configuration can take up to an hour to take effect. Backups that were created
before the policy change are retained until they expire, unless you delete
them.



### Console

- 

In the Cloud de Confiance console, open the list of Bigtable instances.

[
Open the instance list
](https://console.cloud.s3nscloud.fr/bigtable/instances)

- 

Click the instance that contains the table you want to disable automated
backup for.

- 

Click **Tables**.

The **Tables** page displays a list of tables in the instance.

- 

In the row of the table that you want to disable automated backup for,
click edit **Edit**.

- 

Clear the **Enable automated backup** checkbox.

- 

Click **Save**.



### gcloud

To disable automated backup for a table, run the [`gcloud bigtable
instances tables update`](/sdk/gcloud/reference/bigtable/instances/tables/update) command.


```
gcloud bigtable instances tables update TABLE_ID \
--instance= INSTANCE_ID \
--disable-automated-backup
```


Replace the following:

- TABLE_ID : ID of the table.

- INSTANCE_ID : 
The permanent identifier for the instance.




### View automated backup policy

To view the automated backup policy for a table, run the [`gcloud bigtable
instances tables describe`](/sdk/gcloud/reference/bigtable/instances/tables/describe) command.


```
gcloud bigtable instances tables describe TABLE_ID \
--instance= INSTANCE_ID 
```


Replace the following:

- TABLE_ID : ID of the table.

- INSTANCE_ID : 
The permanent identifier for the instance.

The output looks similar to the following:


```
automatedBackupPolicy:
frequency: 86400s
retentionPeriod: 604800s
locations: us-central1-a,us-east1-b,europe-west1-c
columnFamilies:
my-family: {}
createTime: '2023-02-07T20:10:55.613546Z'
granularity: MILLIS
name: projects/my-project/instances/my-instance/tables/my-table
updateTime: '2023-02-07T20:10:55.613546Z'
```


Note the following:

- The `automatedBackupPolicy` field is absent when automated backup is not
enabled for a table.

- The `retentionPeriod` indicates the retention period of automatically
created backups. You can modify the retention period for a backup to up to
90 days in the Enterprise edition or up to
365 days in the Enterprise Plus edition,
starting from the backup creation time. To update the backup retention
period, see [Modify a backup or backup copy](#modify).

- The `locations` field is present only when automated backups for clusters in
specific locations are enabled in the Enterprise Plus edition. When
present, it indicates the list of cluster locations where automated backups
are enabled. If automated backups are enabled in all locations (default),
then the field won't be present.

### Update an automated backup policy

Automated backup policy changes don't apply retroactively to existing backups.
New backup policy settings apply only to subsequent backups.

You can configure a custom retention period of up to
90 days in both Enterprise and Enterprise Plus editions.
In the Enterprise Plus edition, you can also select specific cluster locations
for automated backups.

To update the retention period or expiration date of an existing backup,
including an automated backup, see
[Modify a backup or backup copy](#modify).



### Console

- 

In the Cloud de Confiance console, open the list of Bigtable instances.

[
Open the instance list
](https://console.cloud.s3nscloud.fr/bigtable/instances)

- 

Click the instance that contains the table whose automated backup
policy you want to update.

- 

Click **Tables**.

The **Tables** page displays a list of tables in the instance.

- 

In the row of the table that you want to configure the automated backup
policy for, click edit **Edit**.
The table properties pane is displayed.

- 

Under **Configure automated backup**, in the **Retention period** field,
specify the number of days that Bigtable should retain
backups after the change is saved. You can configure a custom retention
period from 3 days and up to 90 days.

- 

**Enterprise Plus edition**: under **Configure automated backup**, in the
**Select clusters to back up** field,
select cluster locations where you want to enable the automated backup.

- 

Click **Save**.



### gcloud

To modify a table's automated backup policy, use the
[`gcloud bigtable tables update`](/sdk/gcloud/reference/bigtable/instances/tables/update)
command with the following flags:

- `--automated-backup-retention-period`: sets a custom retention period.

- `--automated-backup-locations`: In the Enterprise Plus edition, enables
automated backup only for clusters in the specified locations. If not
set, the backups default to all clusters in the table's instance.


```
gcloud bigtable tables update TABLE_ID \
--instance= INSTANCE_ID \
--automated-backup-retention-period= RETENTION_PERIOD \
--automated-backup-locations= BACKUP_LOCATIONS 
```


Replace the following:

- TABLE_ID : the ID of the table that has automated backup.

- INSTANCE_ID : 
The permanent identifier for the instance.

- 

RETENTION_PERIOD : A period of up to
90 days. The value must be expressed as a number
with a unit of `m`, `h`, or `d` (minutes, hours, or days), such as `15d`
for 15 days.

*Examples*: `72h` or `15d`

- 

BACKUP_LOCATIONS : A comma-separated list of cluster locations
where the automated backup must be enabled. If not set, the backups
default to all clusters in the table's instance.

*Example*: `us-central1-a,us-east1-b,europe-west1-c`




### Configure automated backup cluster locations

By default, when you enable automated backup for a table in an instance that has
multiple clusters, Bigtable creates a daily backup on every
cluster in the instance. In the Enterprise Plus edition, you can selectively
configure automated backup to create daily backups on clusters in specific
locations.

You can configure automated backup cluster locations when you create a table,
enable automated backup, or update an automated backup policy.



### Console

- 

In the Cloud de Confiance console, open the list of Bigtable instances.

[
Open the instance list
](https://console.cloud.s3nscloud.fr/bigtable/instances)

- 

Click the instance that contains the table that you want to configure.

- 

In the left pane, click **Tables**.

- 

In the row of the table, click edit **Edit**.

- 

Under **Configure automated backup**, in the
**Select clusters to back up** field, select the cluster locations where
you want daily backups created.

- 

Click **Save**.



### gcloud

To specify cluster locations for automated backup, run the
[`gcloud bigtable tables update`](/sdk/gcloud/reference/bigtable/instances/tables/update) command using the
`--automated-backup-locations` flag:


```
gcloud bigtable tables update TABLE_ID \
--instance= INSTANCE_ID \
--automated-backup-locations= BACKUP_LOCATIONS 
```


Replace the following:

- TABLE_ID : ID of the table to configure.

- INSTANCE_ID : 
The permanent identifier for the instance.

- BACKUP_LOCATIONS : A comma-separated list of cluster locations
where you must enable automated backup, such as `us-central1-a,us-east1-b`.

To remove custom automated backup locations and revert to creating backups
in all cluster locations of the instance, run the
[`gcloud bigtable tables update`](/sdk/gcloud/reference/bigtable/instances/tables/update) command using the
`--clear-automated-backup-locations` flag:


```
gcloud bigtable tables update TABLE_ID \
--instance= INSTANCE_ID \
--clear-automated-backup-locations
```



### View event logs

When automated backup is enabled, Bigtable emits a system event logs
when a backup is created. It also emits an event log if backup creation is
delayed.

To view automated backup system event logs on the Bigtable
cluster overview page in the console, do the following:

- 

In the Cloud de Confiance console, open the list of Bigtable instances.

[
Open the instance list
](https://console.cloud.s3nscloud.fr/bigtable/instances)

- 

Click the instance ID.

- 

Click the cluster ID.

If automated backup event logs were created in the last hour, they are
displayed in the **Logs** pane.

- 

Optional: To view older event logs, click the arrow next to **1 Hour** and
select another time range.

To view automated backup system event logs in the Logs Explorer, follow
these steps:

- 

Navigate to the Logs Explorer:

[Go to the Logs Explorer](https://console.cloud.s3nscloud.fr/logs/query)

Select the appropriate Cloud de Confiance project.

- 

To view backup creation events, enter the following in the **Query** field:


```
resource.type="audited_resource" resource.labels.service="bigtableadmin.googleapis.com"
resource.labels.method="CreateAutomatedBackup"
```


- 

Click **Run query**.

- 

To view backup delay events, enter the following in the **Query** field:


```
resource.type="audited_resource" resource.labels.service="bigtableadmin.googleapis.com"
resource.labels.method="DelayedAutomatedBackup"
```


- 

Click **Run query**.

The query result includes a message similar to the following:


```
Automated backup is delayed for table ab-test on cluster my-cluster-staging-c1.
```


## Create a standard backup

You can create a standard backup of a table using the Google Cloud CLI, the
console, or by using one of the Bigtable client
libraries. You can also [Enable automated backup](#enable-automated-backup) to
let Bigtable create a daily standard backup for you.



### Console

- 

In the Cloud de Confiance console, go to the Bigtable
**Instances** page.

[Open the instance list](https://console.cloud.s3nscloud.fr/bigtable/instances) 

- 

Click the instance that contains the table you want to back up.

- 

In the left navigation pane, click **Backups**.

- 

Click **Create backup**.

- 

In the **Table ID** list, select the table that you want to back up. (If
you click **Create backup** from the more_vert 
**Table action** menu on the table overview page, then Bigtable
populates the table.)

- 

If you use replication, then select the **Cluster ID** for the cluster.
(If you click **Create backup** next to a cluster ID on the cluster overview
page, then Bigtable populates the table and the cluster.)

- 

Enter a unique ID for the backup.

- 

In the **Backup type** section, select **Standard**.

- 

Set an expiration date by selecting one of the options.

- 

Click **Create**.

The Cloud de Confiance console displays the **Backups** page filtered to
show the backup and its details.

- 

Optional: To view the status of the backup, click the **Activity** tab.

After Bigtable finishes backing up your data, the **Backup
complete** status appears in the **Status** column.



### gcloud

For all commands, substitute actual values for the following:

- INSTANCE_ID : 
The permanent identifier for the instance.

- CLUSTER_ID : 
The permanent identifier for the cluster.

- TABLE_ID : The ID of the table to be backed up.

- BACKUP_ID : The ID you assign to the backup.

- 

EXPIRATION_DATE : A date in the future, up to
90 days in the Enterprise edition or up to
365 days in the Enterprise Plus edition.
The value must be formatted as a "Zulu" UTC timestamp, accurate to
nanoseconds.

*Example*: `2022-10-02T15:01:23.045123456Z`

- 

RETENTION_PERIOD : A period of up to
90 days in the Enterprise edition or up to
365 days in the Enterprise Plus edition.
The value must be expressed as a number with a unit of `m`, `h`, or
`d` (minutes, hours, or days), such as `15d` for 15 days.

*Examples*: `36h` or `89d`

- 

If you don't know the instance ID, use the
[`bigtable instances
list` command](/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances:


```
gcloud bigtable instances list
```


- 

View the list of backups for the instance that contains the table you
want to back up, so that you can choose a backup ID that is not already in
use on the intended cluster.


```
gcloud bigtable backups list --instance= INSTANCE_ID \
--cluster= CLUSTER_ID 
```


- 

View the list of tables to confirm the ID of the table you want to back
up.


```
gcloud bigtable instances tables list --instances= INSTANCE_ID 
```


- 

Run the [`gcloud bigtable instances backups create`](/sdk/gcloud/reference/bigtable/instances/backups/create)
command to create a backup from the table, providing either an expiration
date *or* a retention period. The value can be up to
90 days in the Enterprise edition or up to
365 days in the Enterprise Plus edition.


```
gcloud bigtable backups create BACKUP_ID --instance= INSTANCE_ID \
--cluster= CLUSTER_ID \
--table= TABLE_ID \
--async \
--expiration-date= EXPIRATION_DATE \
--retention-period= RETENTION_PERIOD 
```


The `--async` flag is optional. Use it if you want the terminal to return
the operation ID before the operation is complete. This is helpful if you
want to [check the status](#status-backup) of the operation.

- 

View the list of backups to see if your backup has been created.


```
gcloud bigtable backups list --instance= INSTANCE_ID \
--cluster= CLUSTER_ID 
```


- 

If the backup is not listed, check the [status of the operation](#status-backup).

A status of `Ready` indicates the backup is complete.




## Create a hot backup

You can't create a hot backup for a table that has
[tiered storage](/bigtable/docs/tiered-storage) ([Preview](https://documentation.s3ns.fr/products#product-launch-stages)) enabled.



### Console

You can create a hot backup of a table using the Cloud de Confiance console as
follows:

- 

In the Cloud de Confiance console, go to the Bigtable
**Instances** page.

[Open the instance list](https://console.cloud.s3nscloud.fr/bigtable/instances) 

- 

Click the instance that contains the table that you want to back up.

- 

In the left navigation pane, click **Backups**.

- 

Click **Create backup**.

- 

In the **Table ID** list, select the table that you want to back up. (If
you click **Create backup** from the more_vert 
**Table action** menu on the table overview page, then Bigtable
populates the table.)

- 

If you use replication, then select the **Cluster ID** for the cluster.
(If you click **Create backup** next to a cluster ID on the cluster overview
page, then Bigtable populates the table and the cluster.)

- 

In the **Backup ID** field, enter a unique ID for the backup.

- 

In the **Backup type** section, select **Hot**.

- 

In the **Set hot to standard** list, select one of the following options:

- To keep the backup hot until it expires, select **Never**.

- To convert the hot backup to standard after three days, select **3 days**.

- To specify a custom date and time for when you want to convert the hot
backup to standard, select **Custom**. This value must be at least 24
hours after the time when Bigtable creates the backup.

- 

Click **Create**.

The Cloud de Confiance console displays the **Backups** page filtered to
show the backup and its details.

- 

Optional: To view the status of the backup, click the **Activity** tab.

After Bigtable finishes backing up your data, the **Backup
complete** status appears in the **Status** column.



### gcloud

For all commands, substitute actual values for the following:

- INSTANCE_ID : 
The permanent identifier for the instance.

- CLUSTER_ID : 
The permanent identifier for the cluster.

- TABLE_ID : The ID of the table to be backed up.

- BACKUP_ID : The ID you assign to the backup.

- 

EXPIRATION_DATE : A date in the future that is
90 days or less in the Enterprise edition or
365 days or less in the Enterprise Plus
edition. The date must be formatted as a "Zulu" UTC timestamp, accurate
to nanoseconds.

*Example*: `2022-10-02T15:01:23.045123456Z`

- 

RETENTION_PERIOD : A period of up to
90 days in the Enterprise edition or up to
365 days in the Enterprise Plus edition,
expressed as a number with a unit of `m`, `h`, or `d` (minutes, hours, or
days).

*Examples*: `36h` or `89d`

- 

HOT_TO_STANDARD_TIME : (Optional) the date and time when
Bigtable should convert the backup from a hot backup to a
standard backup. This value must be at least 24 hours after the backup
creation time.

*Example*: `2024-08-02T15:01:23.045123456Z`

You can alternatively provide a relative duration date and time. For more
information, see [gcloud topic
datetimes](/sdk/gcloud/reference/topic/datetimes).

*Example*: `+P30D` for 30 days

- 

If you don't know the instance ID, use the
[`bigtable instances
list` command](/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances:


```
gcloud bigtable instances list
```


- 

View the list of backups for the instance that contains the table you
want to back up, so that you can choose a backup ID that is not already in
use on the intended cluster.


```
gcloud bigtable backups list --instance= INSTANCE_ID \
--cluster= CLUSTER_ID 
```


- 

View the list of tables to confirm the ID of the table you want to back
up.


```
gcloud bigtable instances tables list --instances= INSTANCE_ID 
```


- 

Run the [`gcloud bigtable instances backups create`](/sdk/gcloud/reference/bigtable/instances/backups/create)
command to create a hot backup of the table, providing either an expiration
date *or* a retention period. The value can be up to
90 days in the Enterprise edition or up to
365 days in the Enterprise Plus edition.


```
gcloud bigtable backups create BACKUP_ID -- instance = INSTANCE_ID \
-- cluster = CLUSTER_ID \
-- table = TABLE_ID \
-- async \
-- expiration - date = EXPIRATION_DATE \
-- retention - period = RETENTION_PERIOD \
-- backup - type = HOT \
-- hot - to - standard - time = HOT_TO_STANDARD_TIME 
```


The `--async` flag is optional. Use it if you want the terminal to return
the operation ID before the operation is complete. This is helpful if you
want to [check the status](#status-backup) of the operation.

- 

View the list of backups to see if your backup has been created.


```
gcloud bigtable backups list --instance= INSTANCE_ID \
--cluster= CLUSTER_ID 
```


- 

If the backup is not listed, check the [status of the operation](#status-backup).

A status of `Ready` indicates the backup is complete.




## Restore from a backup

A new table restored from a backup doesn't have automated backup enabled even if
the source table did. If you want automated backup on the new table, you must
enable it.

The steps to restore from a backup are the same whether the backup is standard
or hot. Bigtable restores a hot backup to production performance
more quickly than a standard backup.



### Console

You can't restore to a different project using the Cloud de Confiance console.
If you need to do so, use the gcloud CLI instead.

- 

In the Cloud de Confiance console, go to the Bigtable
**Instances** page.

[Open the instance list](https://console.cloud.s3nscloud.fr/bigtable/instances) 

- 

Click the instance that contains the backup you want to restore.

- 

In the left navigation pane, click **Backups**.

- 

Click **Restore** for the backup that you want to restore.

- 

Select the instance that you want to restore to.

Instances that don't have enough storage for the new table are
unavailable. If you don't have permission to create a table in an
instance, the instance is unavailable. Mouse over the
help icon for
more information.

If you restore from a backup that is protected by CMEK, the destination
instance must be CMEK-protected as well.

If you restore from a backup of a table with
[microsecond timestamp granularity](/bigtable/docs/data-types#timestamp_granularity),
the destination instance must be an Enterprise Plus instance.

You are not able to restore to a different project using the
Cloud de Confiance console. If you need to, use the gcloud CLI
instead.

- 

Enter a unique ID for the table that will be created from the backup.
You are not able to change this ID later.

- 

Click **Restore**.

The console displays the **Tables** page filtered to show the new table.

The console displays the restore status for each cluster. When the
status column for all clusters shows **Ready** the table has been
restored and replicated to all clusters in the instance.



### gcloud

For all commands, substitute actual values for the following:

- PROJECT_ID_SOURCE : The ID of the project containing the backup to be restored from.

- INSTANCE_ID_SOURCE : The permanent ID for the source instance.

- PROJECT_ID_DESTINATION : The ID of the project where you want to restore to. This flag
is optional. If you don't specify this option, the backup is restored to
a new table in the same instance where it was created.

- 

INSTANCE_ID_DESTINATION : The permanent ID for the destination instance.

If you restore from a backup of a table with
[microsecond timestamp granularity](/bigtable/docs/data-types#timestamp_granularity),
the destination instance must be an Enterprise Plus instance.

- 

CLUSTER_ID : 
The permanent identifier for the cluster.

- 

BACKUP_ID : The ID of the backup you want to restore from.

- 

TABLE_ID_NEW : The ID for the new table.

- 

If you don't know the instance ID, use the
[`bigtable instances
list` command](/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances:


```
gcloud bigtable instances list
```


- 

View the list of backups for the instance that contains the backup, to
verify the backup exists.


```
gcloud bigtable backups list --instance= INSTANCE_ID_SOURCE \
--cluster= CLUSTER_ID_SOURCE 
```


- 

View the list of tables in the destination instance, so you can choose
an ID for the new table that is not already in use.


```
gcloud bigtable instances tables list --instances= INSTANCE_ID_DESTINATION 
```


- 

Run the [`gcloud bigtable instances tables restore`](/sdk/gcloud/reference/bigtable/instances/tables/restore) command to restore from the backup to a new table.


```
gcloud bigtable instances tables restore \
--source=projects/ PROJECT_ID_SOURCE /instances/ INSTANCE_ID_SOURCE /clusters/ CLUSTER_ID /backups/ BACKUP_ID \
--async \
--destination= TABLE_ID_NEW \
--destination-instance= INSTANCE_ID_DESTINATION \
--project= PROJECT_ID_DESTINATION 
```


The `--async` flag is optional. Use it if you want the terminal to return
the operation ID before the operation is complete. This is helpful if you
want to [check the status](#status-backup) of the operation.

- 

View the list of tables to see if your table has been created.


```
gcloud bigtable instances tables list --instances= INSTANCE_ID_DESTINATION 
```


- 

If the backup is not listed, check the [status of the operation](#status-backup).




## Create a copy of a backup



### Console

You are not able to create a copy of a backup in a different project
using the console. If you need to do so, use the
gcloud CLI instead.

- 

In the Cloud de Confiance console, go to the Bigtable
**Instances** page.

[Open the instance list](https://console.cloud.s3nscloud.fr/bigtable/instances) 

- 

Click the instance that contains the backup you want to copy.

- 

In the left navigation pane, click **Backups**.

- 

For the backup that you want to copy, expand the More menu next to the
word **Restore**, and then click **Copy**.

- 

Click **Copy** for the backup that you want to make a copy of.

If the backup is a copy of another backup, then **Copy** is not
available.

- 

Select the destination instance.

You are not able to create a copy of a backup in a different project
using the console. If you need to do so, use the
gcloud CLI instead.

Instances that don't have enough storage for the backup copy are
unavailable. If you don't have permission to create a backup in an
instance, the instance is unavailable. Hold the pointer over the
help icon for
more information.

If you copy a backup that is protected by CMEK, the destination instance
must be CMEK-protected as well.

- 

Select the destination cluster.

Like any backup, a backup copy is stored on only one cluster in an
instance, even if that instance uses replication.

- 

Enter a unique ID for the copy that will be created from the backup. You
are not able to change this ID later.

- 

Set an expiration time for the backup copy, providing a value for
**Time** and selecting a **Unit** from the drop-down menu.

- 

Click **Copy**.

- 

To view your copy, click **View copy**.

The console displays the **Backups** page for the destination instance,
filtered for the backup copy just created. When the status column shows
**Ready** the copy is complete and ready for further operations.



### gcloud

For all commands, substitute actual values for the following:

- PROJECT_ID_SOURCE : The project containing the backup to be copied.

- INSTANCE_ID_SOURCE : The permanent ID for the source instance.

- CLUSTER_ID_SOURCE : The ID of cluster where the source backup is stored.

- BACKUP_ID_SOURCE : The ID of the backup to copy.

- PROJECT_ID_DESTINATION : The project where you want to put the copy.

- INSTANCE_ID_DESTINATION : The permanent ID for the destination instance.

- CLUSTER_ID_DESTINATION : The ID of the cluster in the destination instance
that you want to store the copy.

- BACKUP_ID_DESTINATION : The ID you assign to the copy of the backup.

- RETENTION_PERIOD : The time to live for the backup copy, expressed as a
number and a unit (d or h). Examples include `5d` for five days or `15h`
for 15 hours. Use either this or an expiration date.

- EXPIRATION_DATE : The date and time to let the backup copy expire,
formatted like `2022-09-01T10:00:00.0Z`.

- 

If you don't know the instance ID, use the
[`bigtable instances
list` command](/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances:


```
gcloud bigtable instances list
```


- 

View the list of backups for the source instance that contains the
backup, to verify that the backup that you want to copy exists.


```
gcloud bigtable backups list --instance= INSTANCE_ID_SOURCE \
--cluster= CLUSTER_ID_SOURCE 
```


- 

View the list of backups in the destination instance, so you can choose
an ID for the copy that is not already in use.


```
gcloud bigtable backups list --instances= DESTINATION_INSTANCE 
```


- 

Run the [`gcloud bigtable instances backups copy`](/sdk/gcloud/reference/bigtable/backups/copy) command to create the backup copy.


```
gcloud bigtable backups copy \
--source-project= PROJECT_ID_SOURCE \
--source-instance= INSTANCE_ID_SOURCE \
--source-cluster= CLUSTER_ID_SOURCE \
--source-backup= BACKUP_ID_SOURCE \
--destination-project= PROJECT_ID_DESTINATION \
--destination-instance= INSTANCE_ID_DESTINATION \
--destination-cluster= CLUSTER_ID_DESTINATION \
--destination-backup= BACKUP_ID_DESTINATION \
```


Append the command with one of the following:

- `--retention-period``= RETENTION_PERIOD : Retention period for the backup copy. Must be at least 6 hours and at most 30 days from the time the source backup was created.

- `--expiration-date``= EXPIRATION_DATE : Expiration for the backup copy. Must be at least 6 hours and at most 30 days from the time the source backup was created.

You can optionally add `--async` to the command. Use it if you want the
terminal to return the operation ID before the operation is complete.
This is helpful if you want to [check the status](#status-backup) of the
operation.

If a timeout message is returned, the backup might have been successful and the copy might have been created.

- 

View the list of backups to see if your copy has been created.


```
gcloud bigtable backups list --instances= INSTANCE_ID_DESTINATION 
```


- 

If the backup is not listed, check the
[status of the operation](#status-backup).




In the rare event that a backup copy operation fails
because of capacity limitations, try again with a different destination
cluster. If that operation also fails, contact Support.

## Check the status of an operation



### Console

- 

In the Cloud de Confiance console, go to the Bigtable
**Instances** page.

[Open the instance list](https://console.cloud.s3nscloud.fr/bigtable/instances) 

- 

Click the instance that contains the backup.

- 

In the left navigation pane, click **Backups**.

- 

On the **Backups** page, click **Activity**. The status column displays
the current status for each operation.

Operation statuses when restoring a table include the following:

- Waiting to copy

- Restoring backup

- Initializing

- Ready-optimizing

- Ready

Operation statuses when creating a backup include the following:

- Creating backup

- Backup complete

Operation statuses when copying a backup include the following:

- Copying backup

- Copied backup



### gcloud

To check the status of a backup or restore operation, you need the unique
ID of the operation. The following is an example of an operation ID:


```
`instances/instance-name/tables/table-name/locations/us-east1-b/operations/917168358249360635`
```


After you run a command to create a backup or restore to a new table using
the option `--async`, the terminal displays the operation ID.

- 

Copy the operation ID.

- 

Run the
[`gcloud bigtable operations describe`](/sdk/gcloud/reference/bigtable/operations/describe)
command, substituting the value you copied for
`OPERATION_ID`.


```
gcloud bigtable operations describe OPERATION_ID 
```


Example:


```
gcloud bigtable operations describe \
instances/instance-name/tables/table-name/locations/us-east1-b/operations/917168358249360635
```


You can execute this command every few moments until the value for `DONE`
is `TRUE`.

If you don't know the operation ID, either because you didn't just execute
the command or you are in a different terminal window, you can view a list
of operations for the instance and determine which operation you want to
check.

- 

View a list of recent operation activity for the instance that
contains the table you are backing up or restoring to, substituting the
ID of the instance for `INSTANCE_ID`:


```
gcloud bigtable operations list --instance= INSTANCE_ID 
```


The terminal displays a list of operations in columns labeled `NAME`,
`START_TIME`, `END_TIME`, and `DONE`. The value in the `NAME` column is
the operation ID.

- 

Beginning with the first item on the list, copy the operation ID.

- 

Use [gcloud bigtable operations describe](/sdk/gcloud/reference/bigtable/operations/describe)
to view metadata for the operation.


```
gcloud bigtable operations describe OPERATION_ID 
```


Example:


```
gcloud bigtable operations describe \
instances/instance-name/tables/table-name/locations/us-east1-b/operations/917168358249360635
```


- 

If the metadata for an operation **shows a value for `backupInfo`**, you
have found the correct operation, and you can repeat this command every so
often until the value for `DONE` is `TRUE`.

If the metadata does not show a value for `backupInfo`, check the next
operation from the list of operations displayed in Step 1.




## Modify a backup or backup copy

You can modify the expiration date or retention period of an existing backup,
whether created manually or by an automated backup policy, or a backup copy.
In the Enterprise edition, you can extend the expiration date of a backup to up
to 90 days from the backup creation time. In the
Enterprise Plus edition, you can extend the expiration date to up to
365 days from the backup creation time. You can also
convert a hot backup to a standard backup.



### Console

- 

In the Cloud de Confiance console, go to the Bigtable
**Instances** page.

[Open the instance list](https://console.cloud.s3nscloud.fr/bigtable/instances) 

- 

Click the instance that contains the backup.

- 

In the left navigation pane, click **Backups**.

- 

To change the backup expiration date and time of a backup, follow these
steps:

- 

For the backup that you want to modify, click the
more_vert menu next to
**Restore**, and then click **Edit**.

- 

In the **Backup expiration** section, set the date and time, and then
click **Save**.

- 

To set the hot to standard transition date and time of a hot backup,
follow these steps:

- 

For the hot backup that you want to modify, click the
more_vert menu next to
**Restore**, and then click **Edit**.

- 

In the **Update hot to standard** section, set the date and time, and
then click **Save**.



### gcloud

The gcloud CLI lets you modify the expiration date or
period for a backup or backup copy. You can also convert a hot backup to a
standard backup.

For all commands, substitute actual values for the following:

- INSTANCE_ID : 
The permanent identifier for the instance.

- CLUSTER_ID : 
The permanent identifier for the cluster.

- BACKUP_ID : The unique ID for a backup.

- 

EXPIRATION_DATE : A date in the future, up to
90 days in the Enterprise edition or up to
365 days in the Enterprise Plus edition.
The value must be formatted as a "Zulu" UTC timestamp, accurate to
nanoseconds.

*Example*: `2019-10-02T15:01:23.045123456Z`

- 

RETENTION_PERIOD : For backups, a period of up to
90 days in the Enterprise edition or up to
365 days in the Enterprise Plus edition.
For backup copies, a period of up to
30 days. The value must be expressed as
a number with a unit of `m`, `h`, or `d` (minutes, hours, or days).

*Examples*: `36h` or `89d`

- 

HOT_TO_STANDARD_TIME : (Optional) the date and time when
Bigtable should convert the backup from a hot backup to a
standard backup. This value must be at least 24 hours after the backup
creation time.

*Example*: `2024-08-02T15:01:23.045123456Z`

You can alternatively provide a relative duration date and time. For more
information, see [gcloud topic
datetimes](/sdk/gcloud/reference/topic/datetimes).

*Example*: `+P30D` for 30 days

- 

View a list of backups:


```
gcloud bigtable backups list --instance= INSTANCE_ID 
```


The terminal displays a list of backups.

- 

Note the backup and cluster IDs for the backup you need to update.

- 

Run the [`gcloud bigtable backups update`](/sdk/gcloud/reference/bigtable/backups/update) command to add a new expiration date or retention period or to convert a hot backup
to a standard backup.


```
gcloud bigtable backups update BACKUP_ID \
--instance= INSTANCE_ID \
--cluster= CLUSTER_ID \
--expiration-date= EXPIRATION_DATE \
--retention-period= RETENTION_PERIOD 
--hot-to-standard-time= HOT_TO_STANDARD_TIME 
```


- 

Run the [`gcloud bigtable instances backups describe`](/sdk/gcloud/reference/bigtable/instances/backups/describe) command to verify that you have successfully updated the expiration.


```
gcloud bigtable backups describe BACKUP_ID \
--instance= INSTANCE_ID \
--cluster= CLUSTER_ID 
```





## Delete a backup

If you want to delete a backup after creating a copy of it, check the status to
verify that the copy operation is complete.



### Console

- 

In the Cloud de Confiance console, go to the Bigtable
**Instances** page.

[Open the instance list](https://console.cloud.s3nscloud.fr/bigtable/instances) 

- 

Click the instance that contains the backup.

- 

In the left navigation pane, click **Backups**.

- 

For the backup you need to delete, expand the More menu next to the word
**Restore**, then click **Delete**.

- 

Enter the backup ID in the **Confirm deletion** field, then click
**Delete**.



### gcloud

- 

View a list of backups, substituting the ID of the
instance for `INSTANCE_ID`:


```
gcloud bigtable backups list --instance= INSTANCE_ID 
```


The terminal displays a list of backups.

- 

Note the backup ID and the ID of the cluster it is stored on.

- 

Run the [`gcloud bigtable instances backups delete`](/sdk/gcloud/reference/bigtable/instances/backups/delete) command, substituting the backup ID you noted for
`BACKUP_ID` and the cluster ID for `CLUSTER_ID`.


```
gcloud bigtable backups delete BACKUP_ID \
--instance= INSTANCE_ID \
--cluster= CLUSTER_ID 
```





## What's next

- Read more about [backups](/bigtable/docs/backups).

- Learn how to [import and export](/bigtable/docs/import-export) Bigtable data.

- Review the Bigtable section of
[Architecting disaster recovery for cloud infrastructure outages](/architecture/disaster-recovery).