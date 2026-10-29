# cbt CLI reference

Source: https://documentation.s3ns.fr/bigtable/docs/cbt-reference
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

Reference

](https://documentation.s3ns.fr/bigtable/docs/apis)

























# cbt CLI reference



The `cbt` CLI is a command-line interface that lets you interact with Bigtable.
See the [cbt CLI overview](https://documentation.s3ns.fr/bigtable/docs/cbt-overview) to learn how to install the `cbt` CLI.
Before you use the `cbt` CLI, you should be familiar with the [Bigtable overview](https://documentation.s3ns.fr/bigtable/docs/overview).

The examples on this page use [sample data](https://documentation.s3ns.fr/bigtable/docs/using-filters#data) similar to data
that you might store in Bigtable.

Usage:


```
cbt [- ] [optional-argument]
```


The commands are:


```
addtocell Add a value to an aggregate cell ( write ) 
count Count rows in a table 
createappprofile Create app profile for an instance 
createcluster Create a cluster in the configured instance 
createfamily Create a column family 
createinstance Create an instance with an initial cluster 
createtable Create a table 
deleteallrows Delete all rows 
deleteappprofile Delete app profile for an instance 
deletecluster Delete a cluster from the configured instance 
deletecolumn Delete all cells in a column 
deletefamily Delete a column family 
deleteinstance Delete an instance 
deleterow Delete a row 
deletetable Delete a table 
doc Print godoc - suitable documentation for cbt 
getappprofile Read app profile for an instance 
help Print help text 
import Batch write many rows based on the input file 
listappprofile Lists app profile for an instance 
listclusters List clusters in an instance 
listinstances List instances in a project 
lookup Read from a single row 
ls List tables and column families 
mddoc Print documentation for cbt in Markdown format 
notices Display licence information for any third - party dependencies 
read Read rows 
set Set value of a cell ( write ) 
checkandmutate Set the value of a row if the filter matched any cell 
readmodifywrite Update a cell with incremental operations based on the latest value of the cell 
setgcpolicy Set the garbage - collection policy ( age , versions ) for a column family 
setvaluetype Update column family 's value type. 
updateappprofile Update app profile for an instance 
updatecluster Update a cluster in the configured instance 
version Print the current cbt version 
waitforreplication Block until all the completed writes have been replicated to all the clusters 
samplerowkeys Sample the row keys in a table 
sql Execute a SQL query on an instance 
```


The options are:


```
-project string
project ID. If unset uses gcloud configured project
-instance string
Cloud Bigtable instance
-creds string
Path to the credentials file. If set, uses the application credentials in this file
-timeout string
Timeout (e.g. 10s, 100ms, 5m )
```


Example: cbt -instance=my-instance ls

Use "cbt help <command>" for more information about a command.

Preview features are not available to most Bigtable customers, they
might be changed in backward-incompatible ways and are not recommended
for production use. They are not subject to any SLA or deprecation policy.

Syntax rules for the Bash shell apply to the `cbt` CLI. This means, for example,
that you must put quotes around values that contain spaces or operators. It also means that
if a value is arbitrary bytes, you need to prefix it with a dollar sign and use single quotes.

Example:

cbt -project my-project -instance my-instance lookup my-table $'\224\257\312W\365:\205d\333\2471\315\'

For convenience, you can add values for the -project, -instance, -creds, -admin-endpoint and -data-endpoint
options to your ~/.cbtrc file in the following format:


```
project = my-project-123
instance = my-instance
creds = path-to-account-key.json
admin-endpoint = hostname:port
data-endpoint = hostname:port
auth-token = AJAvW039NO1nDcijk_J6_rFXG_...
timeout = 30s
```


All values are optional and can be overridden at the command prompt.

## Add a value to an aggregate cell (write)


```
cbt addtocell table - id > row - key > [ app - profile = app - profile - id > ] family > : column > = val > [@ timestamp > ] ... 

app - profile = app profile id > The app profile ID to use for the request 
family > : column > = val > [@ timestamp > ] may be repeated to set multiple cells . 

If val > can be parsed as an integer it will be used as one , otherwise the call will fail . 
timestamp is an optional integer . 
If the timestamp cannot be parsed , ' @ timestamp > ' will be interpreted as part of the value . 
For most uses , a timestamp is the number of microseconds since 1970 -01-01 00 : 00 : 00 UTC . 

Examples : 
cbt addtocell table1 user1 sum_cf : col1 = 1@12345 
```


## Count rows in a table


```
cbt count [prefix= ] [app-profile= ]
```


## Create app profile for an instance


```
cbt createappprofile (route-any | [ route-to= : transactional-writes]) [-force]
force: Optional flag to override any warnings causing the command to fail

Examples:
cbt createappprofile my-instance multi-cluster-app-profile-1 "Routes to nearest available cluster" route-any
cbt createappprofile my-instance single-cluster-app-profile-1 "Europe routing" route-to=my-instance-cluster-2
```


## Create a cluster in the configured instance


```
cbt createcluster cluster - id > zone > num - nodes > storage - type >

cluster - id Permanent , unique ID for the cluster in the instance 
zone The zone in which to create the cluster 
num - nodes The number of nodes to create 
storage - type SSD or HDD 

Example : cbt createcluster my - instance - c2 europe - west1 - b 3 SSD 
```


## Create a column family


```
cbt createfamily 

Example: cbt createfamily mobile-time-series stats_summary
```


## Create an instance with an initial cluster


```
cbt createinstance instance - id > display - name > cluster - id > zone > num - nodes > storage - type >

instance - id Permanent , unique ID for the instance 
display - name Description of the instance 
cluster - id Permanent , unique ID for the cluster in the instance 
zone The zone in which to create the cluster 
num - nodes The number of nodes to create 
storage - type SSD or HDD 

Example : cbt createinstance my - instance "My instance" my - instance - c1 us - central1 - b 3 SSD 
```


## Create a table


```
cbt createtable table - id > [ families = family > : gcpolicy - expression > : type - expression > , ... ] 
[ splits = split - row - key - 1 > , split - row - key - 2 > , ... ] 

families Column families and their associated garbage collection ( gc ) policies and types . 
Put gc policies in quotes when they include shell operators && and || . For gcpolicy , 
see "setgcpolicy" . 
Types "intsum" , "intmin" , "intmax" , and "inthll" are supported . 
splits Row key ( s ) where the table should initially be split 

Example : cbt createtable mobile - time - series "families=stats_summary:maxage=10d||maxversions=1,stats_detail:maxage=10d||maxversions=1" splits = tablet , phone 
```


## Delete all rows


```
cbt deleteallrows 

Example: cbt deleteallrows mobile-time-series
```


## Delete app profile for an instance


```
cbt deleteappprofile 

Example: cbt deleteappprofile my-instance single-cluster
```


## Delete a cluster from the configured instance


```
cbt deletecluster 

Example: cbt deletecluster my-instance-c2
```


## Delete all cells in a column


```
cbt deletecolumn [app-profile= ]

app-profile= The app profile ID to use for the request

Example: cbt deletecolumn mobile-time-series phone#4c410523#20190501 stats_summary os_name
```


## Delete a column family


```
cbt deletefamily 

Example: cbt deletefamily mobile-time-series stats_summary
```


## Delete an instance


```
cbt deleteinstance 

Example: cbt deleteinstance my-instance
```


## Delete a row


```
cbt deleterow [app-profile= ]

app-profile= The app profile ID to use for the request

Example: cbt deleterow mobile-time-series phone#4c410523#20190501
```


## Delete a table


```
cbt deletetable 

Example: cbt deletetable mobile-time-series
```


## Print godoc-suitable documentation for cbt


```
cbt doc
```


## Read app profile for an instance


```
cbt getappprofile 

```


## Print help text


```
cbt help 

Example: cbt help createtable
```


## Batch write many rows based on the input file


```
cbt import table - id > input - file > [ app - profile = app - profile - id > ] [ column - family = family - name > ] [ batch - size = 500 > ] [ workers = 1 > ] [ timestamp = now | value - encoded > ] 

app - profile = app - profile - id > The app profile ID to use for the request 
column - family = family - name > The column family label to use 
batch - size = 500 > The max number of rows per batch write request 
workers = 1 > The number of worker threads 
timestamp = now | value - encoded > Whether to use current time for all cells or interpret the timestamp from cell value . Defaults to 'now' . 

Import data from a CSV file into an existing Cloud Bigtable table that already has the column families your data requires . 

The CSV file can support two rows of headers : 
- ( Optional ) column families 
- Column qualifiers 
Because the first column is reserved for row keys , leave it empty in the header rows . 
In the column family header , provide each column family once ; it applies to the column it is in and every column to the right until another column family is found . 
Each row after the header rows should contain a row key in the first column , followed by the data cells for the row . 
See the example below . If you don 't provide a column family header row, the column header is your first row and your import command must include the `column-family` flag to specify an existing column family. 

The timestamp for each cell will default to current time ( timestamp = now ), to explicitly set the timestamp for cells , set timestamp = value - encoded use val > [ @ ] as the value for the cell . 
If no timestamp is delimited for a cell , current time will be used . If the timestamp cannot be parsed , '@ ' will be interpreted as part of the value . 
For most uses , a timestamp is the number of microseconds since 1970 - 01 - 01 00 : 00 : 00 UTC . 

, column - family - 1 ,, column - family - 2 , // Optional column family row ( 1 st cell empty ) 
, column - 1 , column - 2 , column - 3 , column - 4 // Column qualifiers row ( 1 st cell empty ) 
a , TRUE ,,, FALSE // Rowkey 'a' followed by data 
b ,,, TRUE , FALSE // Rowkey 'b' followed by data 
c ,, TRUE ,, TRUE // Rowkey 'c' followed by data 
d , TRUE @ 1577862000000000 ,,, FALSE // Rowkey 'd' followed by data 

Examples : 
cbt import csv - import - table data . csv 
cbt import csv - import - table data - no - families . csv app - profile = batch - write - profile column - family = my - family workers = 5 
```


## Lists app profile for an instance


```
cbt listappprofile 
```


## List clusters in an instance


```
cbt listclusters
```


## List instances in a project


```
cbt listinstances
```


## Read from a single row


```
cbt lookup [columns= : ,...] [cells-per-column= ] [app-profile= ]

row-key String or raw bytes. Raw bytes must be enclosed in single quotes and have a dollar-sign prefix
columns= : ,... Read only these columns, comma-separated
cells-per-column= Read only this number of cells per column
app-profile= The app profile ID to use for the request
format-file=

The path to a format-configuration file to use for the request
keys-only=
| Whether to print only row keys
include-stats=full Include a summary of request stats at the end of the request

Example: cbt lookup mobile-time-series phone#4c410523#20190501 columns=stats_summary:os_build,os_name cells-per-column=1
Example: cbt lookup mobile-time-series $'\x41\x42'
```


## List tables and column families


```
cbt ls List tables
cbt ls List a table's column families and garbage collection policies

Example: cbt ls mobile-time-series
```


## Print documentation for cbt in Markdown format


```
cbt mddoc
```


## Display licence information for any third-party dependencies


```
cbt notices
```


## Read rows


```
cbt read table - id > [ authorized - view = authorized - view - id > ] [ start = row - key > ] [ end = row - key > ] [ prefix = row - key - prefix > ] [ regex = regex > ] [ columns = family>: qualifier > ,...] [ count = n > ] [ cells - per - column = n > ] [ app - profile = app - profile - id > ] 

authorized - view = authorized - view - id > Read from the specified authorized view of the table 
start = row - key > Start reading at this row 
end = row - key > Stop reading before this row 
prefix = row - key - prefix > Read rows with this prefix 
regex = regex > Read rows with keys matching this regex 
reversed = true | false > Read rows in reverse order 
columns = family>: qualifier > ,... Read only these columns , comma - separated 
count = n > Read only this many rows 
cells - per - column = n > Read only this many cells per column 
app - profile = app - profile - id > The app profile ID to use for the request 
format - file = path - to - format - file > The path to a format - configuration file to use for the request 
keys - only = true | false > Whether to print only row keys 
include - stats = full Include a summary of request stats at the end of the request 

Examples: ( see ' set ' examples to create data to read ) 
cbt read mobile - time - series prefix = phone columns = stats_summary: os_build , os_name count = 10 
cbt read mobile - time - series start = phone # 4 c410523 # 20190501 end = phone # 4 c410523 # 20190601 
cbt read mobile - time - series regex = "phone.*" cells - per - column = 1 
cbt read mobile - time - series start = phone # 4 c410523 # 20190501 end = phone # 4 c410523 # 20190601 reversed = true count = 10 

Note: Using a regex without also specifying start , end , prefix , or count results in a full 
table scan , which can be slow . 
```


## Set value of a cell (write)


```
cbt set table - id > row - key > [ authorized - view = authorized - view - id > ] [ app - profile = app - profile - id > ] family > : column > = val > [@ timestamp > ] ... 

authorized - view = authorized - view - id > Write to the specified authorized view of the table 
app - profile = app profile id > The app profile ID to use for the request 
family > : column > = val > [@ timestamp > ] may be repeated to set multiple cells . 

timestamp is an optional integer . 
If the timestamp cannot be parsed , ' @ timestamp > ' will be interpreted as part of the value . 
For most uses , a timestamp is the number of microseconds since 1970 -01-01 00 : 00 : 00 UTC . 

Examples : 
cbt set mobile - time - series phone # 4 c410523 # 20190501 stats_summary : connected_cell = 1@12345 stats_summary : connected_cell = 0@1570041766 
cbt set mobile - time - series phone # 4 c410523 # 20190501 stats_summary : os_build = PQ2A .190405.003 stats_summary : os_name = android 
```


## Set the value of a row if the filter matched any cell


```
cbt checkandmutate table - id > rowkey > [ columns = family : qualifier > ,...] ([ true = family > : column > = val > [@ timestamp > ]] | [ false = family > : column > = val > [@ timestamp > ]]) 

row - key String or raw bytes . Raw bytes must be enclosed in single quotes and have a dollar - sign prefix . 
columns = family > : qualifier > ,... Test for values in these columns , comma - separated 
true = family > : column > = val > [@ timestamp > ] A mutation to apply if lookup finds matching cells 
false = family > : column > = val > [@ timestamp > ] A mutation to apply if lookup does not find matching cells 
timestamp is an optional integer . 
If the timestamp cannot be parsed , ' @ timestamp > ' will be interpreted as part of the value . 
For most uses , a timestamp is the number of microseconds since 1970 -01-01 00 : 00 : 00 UTC . 

Optionally columns = ... will restrict the existence test to the indicated columns . 

Examples : 
cbt checkandmutate mobile - time - series phone # 4 c410523 # 20190501 false = presence := 1 
cbt checkandmutate mobile - time - series phone # 4 c410523 # 20190501 columns = stats_summary : os_build true = stats_summary : connected_cell = 1@12345 
```


## Update a cell with incremental operations based on the latest value of the cell


```
cbt readmodifywrite [append= ] [increment= ]

row-key String or raw bytes. Raw bytes must be enclosed in single quotes and have a dollar-sign prefix
family Column family
qualifier Column qualifier
append= Append the given value to the cell
If the cell is unset, it will be treated as an empty value.
increment= Increment the cell by the given integer delta
If the cell is unset, it will be treated as zero. If the cell is set and is not an 8-byte value, the operation will fail.

Examples:
cbt readmodifywrite mobile-time-series phone#4c410523#20190501 stats_summary boot_count increment=1
```


## Set the garbage-collection policy (age, versions) for a column family


```
cbt setgcpolicy table > family > (( maxage = d > | maxversions = n > ) [ (and|or) (maxage= | maxversions= ),... ] | never ) [ force ] 

force : Optional flag to override warnings when relaxing the garbage - collection policy on replicated clusters . 
This may cause your clusters to be temporarily inconsistent , make sure you understand the risks 
listed at https : // cloud . google . com / bigtable / docs / garbage - collection#increasing 

maxage = d > Maximum timestamp age to preserve . Acceptable units : ms , s , m , h , d 
maxversions = n > Maximum number of versions to preserve 
Put garbage collection policies in quotes when they include shell operators && and || . 

Examples : 
cbt setgcpolicy mobile - time - series stats_detail maxage = 10 d 
cbt setgcpolicy mobile - time - series stats_summary maxage = 10 d or maxversions = 1 force 
```


## Update column family's value type.


```
cbt setvaluetype table > family > type >
type : The type to be updated . 
Supported type ( s ): stringutf8bytes : UTF8 encoded string 
Updating to or from aggregate types is currently unsupported . 
Example : 
cbt setvaluetype mobile - time - series vendor - info stringutf8bytes 
```


## Update app profile for an instance


```
cbt updateappprofile 

(route-any | [ route-to= : transactional-writes]) [-force]

force: Optional flag to override any warnings causing the command to fail

Example: cbt updateappprofile my-instance multi-cluster-app-profile-1 "Use this one." route-any
```


## Update a cluster in the configured instance


```
cbt updatecluster [num-nodes= ]

cluster-id Permanent, unique ID for the cluster in the instance
num-nodes The new number of nodes

Example: cbt updatecluster my-instance-c1 num-nodes=5
```


## Print the current cbt version


```
cbt version
```


## Block until all the completed writes have been replicated to all the clusters


```
cbt waitforreplication 
```


## Sample the row keys in a table


```
cbt samplerowkeys 
```


## Execute a SQL query on an Instance


```
cbt sql 

See https://cloud.google.com/bigtable/docs/reference/sql/googlesql-reference-overview for more information.
Note that this does not support parameterized queries.
```