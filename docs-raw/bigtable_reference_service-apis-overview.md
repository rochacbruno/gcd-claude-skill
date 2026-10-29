# Service APIs overview

Source: https://berlin.devsitetest.how/bigtable/docs/reference/service-apis-overview
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

Reference

](https://berlin.devsitetest.how/bigtable/docs/apis)

























# Service APIs overview



Bigtable provides REST/HTTP and [gRPC](https://grpc.io) interfaces.

**We strongly recommend that you use our
[Cloud Bigtable client libraries](/bigtable/docs/reference/libraries) instead of writing your
own**. Our client libraries include many important features that can be
challenging to implement correctly, such as authentication and retries.

If the [Cloud Bigtable client library](/bigtable/docs/reference/libraries) for your preferred
language does not meet your needs, open a [GitHub issue](/bigtable/docs/reference/libraries#additional_resources)
for it instead of writing your own client library.

Supported languages include C#, C++, Java, Go, Node.js, Python, PHP, and Ruby.
You should write your own client library only when you use a programming
language that is not supported.

## gRPC API

You can use the .proto service definition for Bigtable to generate
your own gRPC client library in any language that gRPC supports. Use these
resources to generate a client library:

- [Cloud Bigtable Data API service definition](https://github.com/googleapis/googleapis/blob/master/google/bigtable/v2/bigtable.proto)

- [Cloud Bigtable Instance Admin API service
definition](https://github.com/googleapis/googleapis/blob/master/google/bigtable/admin/v2/bigtable_instance_admin.proto)

- [Cloud Bigtable Table Admin API service
definition](https://github.com/googleapis/googleapis/blob/master/google/bigtable/admin/v2/bigtable_table_admin.proto)

- [gRPC documentation](https://grpc.io/docs/): Everything you need to generate and use your
own gRPC client code

- [RPC Data API reference](/bigtable/docs/reference/data/rpc): Language-independent overview of the
RPC surface of Cloud Bigtable API (the Data API)

- [RPC Admin API reference](/bigtable/docs/reference/admin/rpc): Language-independent overview of the
RPC surface of the Cloud Bigtable Admin API

## REST/HTTP API

Bigtable provides a REST interface for the Admin API. We don't
recommend using REST to access the Data API.

There are many different ways to access the REST interface for
Bigtable. To create your own clients, use the following resources:

- [REST Admin API reference](/bigtable/docs/reference/admin/rest)

- [Guidelines for working with Google HTTP APIs](/apis/docs/http)

- [API Discovery Service](https://developers.google.com/discovery/v1/getting_started): Exposes machine-readable metadata about
the REST/HTTP API surface to help you create client libraries, tools, and
plugins

- [Client samples](https://developers.google.com/discovery/libraries): Built with REST/HTTP APIs and the Google API
Discovery Service.

## What's next

- Learn about the [client libraries for Cloud Bigtable](/bigtable/docs/reference/libraries).

- Complete a [quickstart for creating a gRPC client library](https://grpc.io/docs/quickstart/).

- Read reference documentation for the Cloud Bigtable [RPC Data
API](/bigtable/docs/reference/data/rpc) and [RPC Admin API](/bigtable/docs/reference/admin/rpc).

- Read reference documentation for the [REST Admin API](/bigtable/docs/reference/admin/rest).