# Schema design best practices

Source: https://berlin.devsitetest.how/bigtable/docs/schema-design
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/bigtable/docs/tpc-differences) for more details.














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

Databases

](https://berlin.devsitetest.how/docs/databases)






- 








[

Bigtable

](https://berlin.devsitetest.how/bigtable/docs)






- 








[

Guides

](https://berlin.devsitetest.how/bigtable/docs/overview)

























# Schema design best practices



An effective Bigtable schema lets you maximize read and write
throughput, prevent hotspots, and scale your storage efficiently. Before you
begin, review the [Bigtable overview](/bigtable/docs/overview) to understand the
underlying architecture and storage model.

## General concepts

Designing a Bigtable schema is different from designing a schema
for a relational database. A Bigtable schema is defined by
application logic rather than by a schema definition object or file. You can
add column families to a table when you create or update the table, but columns
and row key patterns are defined by the data that you write to the table.

In Bigtable, a schema is a blueprint or
model of a table, including the structure of the following table components:

- Row keys

- Column families, including their garbage collection policies

- Columns

In Bigtable, schema design is driven primarily by the *queries*,
or read requests, that you plan to send to the table. Because [reading a row
range](/bigtable/docs/reads#row-range) is the fastest way to read your
Bigtable data, the recommendations on this page are designed to
help you optimize for row range reads. In most cases, that means sending a query
based on row key prefixes.

A secondary consideration is the avoidance of hotspots – to prevent hotspots,
you need to consider write patterns and how you can avoid accessing a small key
space in a short amount of time.

The following general concepts apply to Bigtable schema design:

- **Bigtable is a key/value store, not a relational store.** It
does not support joins, and transactions are supported only within a single row.

- **Each table has an index: the row key.** Each row key must be unique. To
create a secondary index, use a continuous materialized view. For more
information, see [Create an asynchronous secondary index](/bigtable/docs/asynchronous-secondary-index).

- **Row keys sort rows lexicographically** from the lowest to the highest byte
string. This order is big-endian (sometimes called network byte order), the
binary equivalent of alphabetical order.

- **Column families are not stored in any specific order.**

- **Columns are grouped by column family and sorted in lexicographic order
within the column family**. For example, in a column family called
`SysMonitor` with column qualifiers of `ProcessName`, `User`, `%CPU`, `ID`,
`Memory`, `DiskRead`, and `Priority`, Bigtable stores the columns
in this order:



| 
| 
| 
| 
SysMonitor | 
| 
|



| 
%CPU | 
DiskRead | 
ID | 
Memory | 
Priority | 
ProcessName | 
User | 
|



- **The intersection of a row and column can contain multiple timestamped
cells.** Each cell contains a unique, timestamped version of the data for
that row and column.

- **Aggregate column families contain aggregate cells.** You can create
column families that contain only aggregate cells. An aggregate lets you
merge new data with data already in the cell.

- **All operations are atomic at the row level.** An operation affects either
an entire row or none of the row.

- **Ideally, both reads and writes should be distributed evenly** across the
row space of a table.

- **Bigtable tables are sparse.** A column doesn't take up any
space in a row that doesn't use the column.

## Best practices

A good schema results in excellent performance and scalability, and a poorly
designed schema can lead to a poorly performing system. Every use case is
different and requires its own design, but the following best practices apply to
most use cases. Exceptions are noted.

Starting at the table level and working down to the row key level, the following
sections describe the best practices for schema design:

- [Tables](#tables)

- [Column families](#column-families)

- [Columns](#columns)

- [Rows](#rows)

- [Cells](#cells)

- [Row keys](#row-keys)

All table elements, **especially row keys**, should be designed with planned
read requests in mind. Check [quotas and limits](/bigtable/quotas#limits-data-size) for recommended
and hard size limits for all table elements.

Because all tables in an instance are stored on the same
[tablets](/bigtable/docs/overview#architecture), a schema design that results in
hotspots in one table can affect the latency of other tables in the same
instance. Hotspots are caused by frequently accessing one part of the table in a
short period of time.

### Tables

**Store datasets with similar schemas in the same table**, rather than in
separate tables.

In other database systems, you might choose to store data in multiple tables
based on the subject and number of columns. In Bigtable, however,
it's usually better to store all your data in one table. You can assign a unique
row key prefix to use for each dataset, so that Bigtable
stores the related data in a contiguous range of rows that you can then query by
row key prefix.

Bigtable has a limit of 1,000 tables per
instance, but we recommend that you **avoid creating a large number of tables**
for the following reasons:

- Sending requests to many different tables can increase backend connection
overhead, resulting in increased tail latency.

- Creating more tables doesn't improve load balancing and can increase management overhead.

You might justifiably want a separate table for a different use case that
requires a different schema, but you shouldn't use separate tables for similar
data. For example, you shouldn't create a new table because it's a new year or
you have a new customer.

### Column families

**Put related columns in the same column family.** When a row contains multiple
values that are related to one another, it's a good practice to group the
columns that contain those values in the same column family. Group data as
closely as you can to avoid needing to design complex filters and so you get
just the information that you need, but no more, in your most frequent read
requests.

**Create up to about 100 column families per table.**
Creating more than 100 column families may cause
performance degradation.

**Choose short names for your column families**. Names are included in the data
that is transferred for each request.

**Put columns that have different data retention needs in different column
families**. This practice is important if you want to limit storage costs.
Garbage collection policies are set at the column family level, not at the
column level. For example, if you only need to keep the most recent version of a
particular piece of data, don't store it in a column family that is set to store
1,000 versions of something else. Otherwise you're paying to store 999 cells of
data that you don't need.

### Columns

**Create as many columns as you need in the table**. Bigtable
tables are sparse, and there's no space penalty for a column that is not used in
a row. You can have millions of columns in a table, as long as no row exceeds
the maximum limit of 256 MB per row.

**Avoid using too many columns in any single row**. Even though a *table* can
have millions of columns, a *row* shouldn't. A few factors contribute to this
best practice:

- It takes time for Bigtable to process each cell in a row.

- Each cell adds some overhead to the amount of data that's stored in your
table and sent over the network. For example, if you're storing 1 KB (1,024
bytes) of data, it's much more space-efficient to store that data in a
single cell, rather than spreading the data across 1,024 cells that each
contain 1 byte.

If your dataset logically requires more columns per row than
Bigtable can process efficiently, consider storing the data as a
[protobuf in a single column](#protobuf-data).

**Optionally, you can treat column qualifiers as data**. Since you have to store
a column qualifier for every column, you can save space by naming the column
with a value. As an example, consider a table that stores data about friendships
in a `Friends` column family. Each row represents a person and all their
friendships. Each column qualifier can be the ID of a friend. Then the value for
each column in that row can be the social circle the friend is in. In this
example, rows might look like this:



| 
Row key | 
Fred | 
Gabriel | 
Hiroshi | 
Seo Yoon | 
Jakob | 
|

| 
Jose | 
book-club | 
work | 
tennis | 
| 
| 
|


| 
Sofia | 
| 
| 
work | 
school | 
chess-club | 
|



Contrast this schema with a schema for the same data that *doesn't* treat column
qualifiers as data and instead has the same columns in every row:



| 
Row key | 
Friend | 
Circle | 
|

| 
Jose#1 | 
Fred | 
book-club | 
|


| 
Jose#2 | 
Gabriel | 
work | 
|

| 
Jose#3 | 
Hiroshi | 
tennis | 
|

| 
Sofia#1 | 
Hiroshi | 
work | 
|

| 
Sofia#2 | 
Seo Yoon | 
school | 
|

| 
Sofia#3 | 
Jakob | 
chess-club | 
|



The second schema design causes the table to grow much faster.

If you're [using column qualifiers to store data](#columns),
**give column qualifiers short but meaningful names**. This approach lets you
reduce the amount of data that is transferred for each request. The maximum size
is 16 KB.

### Rows

**Keep the size of all values in a single row under
100 MB**. Make sure that data in a single row doesn't
exceed 256 MB. Rows that exceed this limit can result in
reduced read performance.

**Keep all information for an entity in a single row**. For most use cases,
avoid storing data that you must read atomically, or all at once, in more than
one row to avoid inconsistencies. For example, if you update two rows in a
table, it's possible that one row will be updated successfully and the other
update will fail. Make sure your schema does not require more than one row to be
updated at the same time for related data to be accurate. This practice ensures
that if part of a write request fails or must be sent again, that piece of data
is not temporarily incomplete.

*Exception:* If keeping an entity in a single row results in rows that are
hundreds of MB, you should split the data across multiple rows.

**Store related entities in adjacent rows,** to make reads more efficient.

### Cells

**Don't store more than 10 MB of data in a single
cell**. Recall that a cell is the data stored for a given row and column with a
unique timestamp, and that multiple cells can be stored at the intersection of
that row and column. The number of cells retained in a column is governed by the
[garbage collection policy](/bigtable/docs/garbage-collection) that you set for the column
family that contains that column.

**Use aggregate cells to store and update aggregate data.** If you only care
about the aggregated value of events for an entity, such as the monthly sum of
sales per employee at a retail store, you can use aggregates. For more
information, see [Aggregate values at write time](/bigtable/docs/aggregates).

### Row keys

**Design your row key based on the queries you will use to retrieve the data**.
Well-designed row keys get the best performance out of Bigtable.
The most efficient Bigtable queries retrieve data using one of the
following:

- Row key

- Row key prefix

- Range of rows defined by starting and ending row keys

Other types of queries trigger a full table scan, which is much less efficient.
*By choosing the correct row key now, you can avoid a painful data migration
process later*.

**Keep your row keys short**. A row key must be 4 KB or less. Long row keys take
up additional memory and storage and increase the time it takes to get responses
from the Bigtable server.

**Store multiple delimited values in each row key.** Because the best way to
query Bigtable efficiently is by row key, it's often useful to
include multiple identifiers in your row key. When your row key includes
multiple values, it's especially important to have a clear understanding of how
you use your data.

Row key segments are usually separated by a delimiter, such as a colon, slash,
or hash symbol. The first segment or set of contiguous segments is the row key
prefix, and the last segment or set of contiguous segments is the row key
suffix.



Well-planned row key prefixes let you take advantage of Bigtable's
built-in sorting order to store related data in contiguous rows. Storing related
data in contiguous rows lets you access related data as a range of rows, rather
than running inefficient table scans.

If your data includes integers that you want to store or sort numerically,
**pad the integers with leading zeroes.** Bigtable [stores data
lexicographically](#general-concepts). For example, lexicographically, 3 > 20
but 20 > 03. Padding the 3 with a leading zero ensures that the numbers are
sorted numerically. This tactic is important for timestamps where range-based
queries are used.

It's important to **create a row key that makes it possible to retrieve a
well-defined range of rows**. Otherwise, your query requires a table scan, which
is much slower than retrieving specific rows.

For example, if your application tracks mobile device data, you can have a row
key that consists of device type, device ID, and the day the data is recorded.
Row keys for this data might look like this:


```
phone#4c410523#20200501
phone#4c410523#20200502
tablet#a0b81f74#20200501
tablet#a0b81f74#20200502
```


This row key design lets you retrieve data with a single request for:

- A device type

- A combination of device type and device ID

This row key design would *not* be optimal if you want to retrieve all data for
a given day. Because the day is stored in the third segment, or the row key
suffix, you cannot just request a range of rows based on the suffix or a middle
segment of the row key. Instead, you have to send a read request with a filter
that scans the entire table looking for the day value.

**Use human-readable string values in your row keys** whenever possible. This
practice makes it easier to use the [Key Visualizer tool](/bigtable/docs/keyvis-overview) to
troubleshoot issues with Bigtable.

**Often, you should design row keys that start with a common value and end with
a granular value**. For example, if your row key includes a continent, country,
and city, you can create row keys that look like the following so that they
automatically sort first by values with lower cardinality:


```
asia#india#bangalore
asia#india#mumbai
asia#japan#osaka
asia#japan#sapporo
southamerica#bolivia#cochabamba
southamerica#bolivia#lapaz
southamerica#chile#santiago
southamerica#chile#temuco
```


#### Structured row keys



If you plan to query your table using SQL, you can define *structured row keys*,
which let you access your Bigtable data using multi-part keys,
similar to composite keys in relational databases. Defining structured row keys
for a table lets you access specific segments of the row keys using
GoogleSQL for Bigtable queries.

Structured row keys are created automatically when you create a [continuous
materialized view](/bigtable/docs/continuous-materialized-views). To implement
structured row keys for a Bigtable
table, you can create a *row key schema* that defines that data type and
encoding of each segment the row key. Bigtable stores the row keys
as lexicographically sorted bytes, and the row key schema tells
GoogleSQL for Bigtable how to decode and interpret
those bytes.

Row key schemas are ignored when you query the table using the
Bigtable Data API `ReadRows` method with a Bigtable
client library.

For more information, see [Manage row key
schemas](/bigtable/docs/manage-row-key-schemas) and [Structured row key
queries](/bigtable/docs/structured-row-key-queries).

#### Row keys to avoid

Some types of row keys can make it difficult to query your data, and some result
in poor performance. This section describes some types of row keys that you
should avoid using in Bigtable.

**Row keys that start with a timestamp**. This pattern causes sequential writes
to be pushed onto a single node, [creating a hotspot](/bigtable/docs/schema-design-time-series#ensure_that_your_row_key_avoids_hotspotting). If
you put a timestamp in a row key, precede it with a high-cardinality value like
a user ID to avoid hotspots.

**Row keys that cause related data to not be grouped**. Avoid row keys that
cause related data to be stored in non-contiguous row ranges, which are
inefficient to read together.

**Sequential numeric IDs**. Suppose that your system assigns a numeric ID to
each of your application's users. You might be tempted to use the user's numeric
ID as the row key for your table. However, because new users are more likely to
be active users, this approach is likely to push most of your traffic to a small
number of nodes.

A safer approach is to use a reversed version of the user's numeric ID, which
spreads traffic more evenly across all of the nodes for your
Bigtable table.


**Frequently updated identifiers.** Avoid using a single row key to identify a
value that must be updated frequently. For example, if you store memory-usage
data for a number of devices once per second, *do not* use a single row key for
each device that is made up of the device ID and the metric being stored, such
as `4c410523#memusage`, and update the row repeatedly. This type of operation
overloads the tablet that stores the frequently used row. It can also cause a
row to exceed its size limit, because a column's previous values take up space
until the cells are removed during garbage collection.

Instead, store each new reading in a new row. Using the memory usage example,
each row key can contain the device ID, the type of metric, and a timestamp, so
the row keys are similar to `4c410523#memusage#1423523569918`. This strategy is
efficient because in Bigtable, creating a new row takes no more
time than creating a new cell. In addition, this strategy lets you quickly
read data from a specific date range by calculating the appropriate start and
end keys.

For values that change frequently, such as a counter that is updated hundreds of
times each minute, it's best to keep the data in memory, at the
application layer, and write new rows to Bigtable
periodically.

**Hashed values**. Hashing a row key removes your ability to take advantage of
Bigtable's natural sorting order, making it impossible to store
rows in a way that are optimal for querying. For the same reason, hashing values
makes it challenging to use the Key Visualizer tool to troubleshoot issues with
Bigtable. Use human-readable values instead of hashed values.

**Values expressed as raw bytes** rather than human-readable strings. Raw bytes
are fine for column values, but for readability and troubleshooting, use string
values in row keys.

## Special use cases

You may have a unique dataset that requires special consideration when designing
a schema to store it in Bigtable. This section describes some, but
not all, different types of Bigtable data and some suggested
tactics for storing it in the most optimal way.

### Time-based data

If you often retrieve data based on the time when it was recorded, you can
include a timestamp as part of your row key.

For example, your application might record performance-related data, such as CPU
and memory usage, once per second for many machines. Your row key for this data
could combine an identifier for the machine with a timestamp for the data (for
example, `machine_4223421#1425330757685`). Keep in mind that row keys are
[sorted lexicographically](#row-keys).

If you include timestamps in the row key, **don't use a timestamp by itself or at
the beginning of a row key**. This pattern causes sequential writes to be pushed
onto a single node, creating a hotspot.

If you usually retrieve the most recent records first in your queries, a pattern
to consider is using **reversed timestamps** in the row key. This pattern causes
rows to be ordered from most recent to least recent, so more recent data is
earlier in the table. As with any timestamp, avoid starting a row key with a
reversed timestamp so that you don't cause hotspots.

You can get a reversed timestamp by subtracting the timestamp from your
programming language's maximum value for long integers (in Java,
`java.lang.Long.MAX_VALUE`).

For information specifically about working with time series data, see [Schema
design for time series data](/bigtable/docs/schema-design-time-series).

### Multi-tenancy

Row key prefixes provide a scalable solution for a "multi-tenancy" use case, a
scenario in which you store similar data, using the same data model, on behalf
of multiple clients. **Using one table for all tenants is the most efficient way
to store and access multi-tenant data.**

For example, say you store and track purchase histories on behalf of many
companies. You can use your unique ID for each company as a row key prefix. All
data for a tenant is stored in contiguous rows in the same table, and you can
query or filter using the row key prefix. Then, when a company is no longer your
customer and you need to delete the purchase history data you were storing for
the company, you can [drop the range of rows](/bigtable/docs/reference/admin/rpc/google.bigtable.admin.v2#google.bigtable.admin.v2.BigtableTableAdmin.DropRowRange) that use that
customer's row key prefix.

For example, if you are storing mobile device data for customers `altostrat` and
`examplepetstore`, you can create row keys like the following. Then, if
`altostrat` is no longer your customer, you drop all rows with the row key
prefix `altostrat`.


```
altostrat#phone#4c410523#20190501
altostrat#phone#4c410523#20190502
altostrat#tablet#a0b41f74#20190501
examplepetstore#phone#4c410523#20190502
examplepetstore#tablet#a6b81f79#20190501
examplepetstore#tablet#a0b81f79#20190502
```


In contrast, if you store data on behalf of each company in its own table, you
can experience performance and scalability issues. You are also more likely to
inadvertently reach Bigtable's limit of 1,000 tables per instance.
After an instance reaches this limit, Bigtable prevents you from
creating more tables in the instance.

### Privacy

Unless your use case demands it, avoid using personally identifiable information
(PII) or user data in row keys or column family IDs. The values in row keys and
column families are both customer data and service data, and applications that
use them, like encryption or logging, can inadvertently expose them to users who
shouldn't have access to private data.

For more information about how service data is handled, see the [Google Cloud Dedicated in Germany
Privacy
Notice](https://berlin.devsitetest.how/terms/cloud-privacy-notice).

### Domain names

You can store domain names as Bigtable data.

#### Wide range of domain names

If you're storing data about entities that can be represented as domain names,
consider using a reverse domain name (for example, `com.company.product`) as the
row key. Using a reverse domain name is an especially good idea if each row's
data tends to overlap with adjacent rows. In this case, Bigtable
can compress your data more efficiently.

In contrast, standard domain names that are not reversed can cause rows to be
sorted in such a way that related data is not grouped together in one place,
which can result in less efficient compression and less efficient reads.

This approach works best when your data is spread across many different reverse
domain names.

To illustrate this point, consider the following domain names, automatically
sorted in lexicographic order by Bigtable:


```
drive.google.com
en.wikipedia.org
maps.google.com
```


This is undesirable for the use case where you want to query all rows for the
`google.com`. In contrast, consider the same rows where the domain names have
been reversed:


```
com.google.drive
com.google.maps
org.wikipedia.en
```


In the second example, the related rows are automatically sorted in a way that
makes it easier to retrieve them as a range of rows.

#### Few domain names

If you expect to store a lot of data for only *one or a small number of domain
names*, consider other values for your row key. Otherwise, you might push writes
to a single node in your cluster, resulting in hotspots, or your rows might grow
too large.

### Storing data in a protobuf format

To reduce storage costs and improve read and write efficiency, you can group
related data into a [protocol buffer (protobuf)](https://protobuf.dev/overview/) message and
store it in a single column instead of storing each field in its own column. If
you typically read a set of fields together, storing them in a single column as
one value is more efficient, because reading a single column is faster than
reading many individual columns. If you store data as protobuf messages, you can
take advantage of the following Bigtable features:

- Using protocol buffers to store flexible data structures reduces storage
costs by keeping your data in place and avoiding duplication.

- Uploading your protobuf schema to Bigtable in schema bundles
enables server-side querying. The schema bundle lets Bigtable
understand and parse the structure of your serialized data during query
execution.

- Using GoogleSQL to query and filter individual fields within your
protobuf messages directly in Bigtable is fast and efficient.
By deserializing the data on the server-side, you can perform granular
queries and projections without the need to transfer the entire protobuf
object to your client.

- Using BigQuery external tables to analyze protobuf
data stored in Bigtable lets you simplify your analytics.

For more information, see [Create and manage protobuf schemas](/bigtable/docs/create-manage-protobuf-schemas)
and [Create and manage Avro schemas](/bigtable/docs/create-manage-avro-schemas) ([Preview](/products#product-launch-stages)).

## What's next

- [Design a schema for time-series data](/bigtable/docs/schema-design-time-series)

- [Review the steps involved in planning a schema](/bigtable/docs/schema-design-steps)

- [Learn the types of write requests that you can send to
Bigtable](/bigtable/docs/writes)

- [Implement counters by using aggregate cells](/bigtable/docs/aggregates)

- [Review the applicable quotas and limits](/bigtable/quotas)

- [Query protobuf data](/bigtable/docs/query-protobuf-data)

- [Query Avro data](/bigtable/docs/query-avro-data)