# cbt CLI overview

Source: https://documentation.s3ns.fr/bigtable/docs/cbt-overview
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

























# cbt CLI
overview



The 
`cbt` CLI
lets you perform administrative and data operations on
Bigtable directly from your terminal. You can use it to manage
instances, create and modify tables, and read or write data without writing
custom code. For general information about Bigtable, see the
[Bigtable overview](/bigtable/docs/overview).

## Install the 
`cbt` CLI

You can install the 
`cbt` CLI
as a
[gcloud CLI component](/sdk/docs/managing-components).

The 
`cbt` CLI
doesn't implement smart retries or error handling. When you
work in production environment, use a Bigtable client library or
the Cloud de Confiance console.

- [Install the gcloud CLI](/bigtable/docs/installing-cloud-sdk).

- 

Run the following commands:


```
gcloud components update
gcloud components install cbt
```


If the 
`cbt` CLI
is already installed, the terminal window displays the `All components are up to date` message.

## Verify the installation

Run the following 
`cbt` CLI
command to verify installation of the CLI:


```
cbt listinstances
```


The terminal window displays two columns named `Instance Name` and `Info`.

## Create a .cbtrc file

You can store required options and parameters, such as `-project`, `-instance`, `-creds`, `-admin-endpoint`, or `-data-endpoint` options, in a single `.cbtrc` file for convenience.

- 

In your `.cbtrc` file, configure `cbt` to use your project and instance by
replacing project-id with the ID for the project where you created
your Bigtable instance:


```
echo project = project-id > ~/.cbtrc
echo instance = quickstart-instance >> ~/.cbtrc
```


- 

Verify that you set up the `.cbtrc` file correctly:


```
cat ~/.cbtrc
```


The terminal displays the contents of the `.cbtrc` file, which looks similar
to the following settings:


```
project = project-id 
instance = quickstart-instance
```


Now you can use the 
`cbt` CLI
with your instance.

## Use the 
`cbt` CLI

For details about using the 
`cbt` CLI
, including a list of available commands,
see the [
`cbt` CLI
reference](/bigtable/docs/cbt-reference).

The 
`cbt` CLI
is written in [Go](https://golang.org) using the
[Go client library for Bigtable](/bigtable/docs/reference/libraries). Source code is
available in the [GoogleCloudPlatform/google-cloud-go](https://github.com/GoogleCloudPlatform/google-cloud-go/tree/master/bigtable/cmd/cbt) GitHub
repository, which mirrors [code.googlesource.com/gocloud](https://code.googlesource.com/gocloud/+/master/bigtable/cmd/cbt/).