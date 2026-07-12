# Google Cloud Dedicated in Germany overview

Source: https://berlin.devsitetest.how/docs/overview/tpc-overview
Last updated: 2026-07-10

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

Get started

](https://berlin.devsitetest.how/docs/get-started)












# Google Cloud Dedicated in Germany overview 






- On this page 
- [ Differences from Google Cloud ](#differences-from-google-cloud)
- [ Universes, regions, and zones ](#universes-regions-and-zones)
- [ Google Cloud Dedicated resources and services ](#resources-and-services)
- [ Interacting with Google Cloud Dedicated ](#interacting)
- [ Projects ](#projects)
- [ What's next ](#whats-next)
- 














Google Cloud Dedicated in Germany is a cloud platform based in Berlin, Germany
that provides the benefits of Google's cloud technology and services, while
offering strong data and operational sovereignty guarantees. Google Cloud Dedicated
is a separate product from Google Cloud, with no data leaving Google Cloud Dedicated's local jurisdiction. 

This makes Google Cloud Dedicated in Germany more suitable for projects
and workloads with enhanced regulatory requirements.

This page gives you a high-level overview of Google Cloud Dedicated
and its features and services, with pointers for where to go next in our
documentation.

## Differences from Google Cloud 

While Google Cloud Dedicated is based on exactly the
same technology as Google Cloud, there are some significant
differences between the universes, with only a subset of
Google Cloud features and products available for Google Cloud Dedicated. One reason for this is because Google Cloud Dedicated
helps ensure data sovereignty by operating as a single, completely standalone
Cloud region, with no connection to Google Cloud's network.
Because of this, Google Cloud features that rely on the existence
of multiple Google regions—such as load balancing across regions, or
multi-region storage—are not supported in Google Cloud Dedicated.

Google Cloud Dedicated supports common use cases and
workload types with fully managed services. More advanced use cases are
supported but might require additional configuration and management compared to
Google Cloud. More functionality is planned, however, to reduce
or eliminate that need. Where available we provide guidance for alternative
approaches if you are a Google Cloud user who is used to using an
unavailable feature or product.

Other differences include:

- Only identities from external identity providers are supported for
authentication and authorization

- Domain names are different from their Google Cloud
counterparts. For example, the service endpoint domain name for the
Compute Engine service is `compute.apis-berlin-build0.goog` rather than `compute.googleapis.com`.

- Some Google Cloud tools and workflows are unavailable, or
work slightly differently.

- Older Compute Engine machine types are unavailable.

You can learn more about the differences between Google Cloud Dedicated
and Google Cloud in [Key differences from
Google Cloud](/docs/overview/tpc-key-differences). If you are
already familiar with Google Cloud we recommend reviewing this
information carefully before designing or implementing applications.

## Universes, regions, and zones

Underlying everything you do on Google Cloud Dedicated
are its physical machines that run your workloads and Google Cloud Dedicated
services. These machines live in data centers, and are logically structured into
universes, regions, and zones.

At the top of this hierarchy is the *universe*. A universe is a fully
self-contained Cloud, with its own networking that is separate from the public
internet and other universes. Google Cloud is the original
universe, with resources in data centers all over the world. Google Cloud Dedicated
is another, smaller universe, with all its resources in a single jurisdiction,
providing strict sovereignty compliance.

Within each universe there are geographic *regions*. Google Cloud
has many regions around the world, while Google Cloud Dedicated
currently has a single region, `u-germany-northeast1`.

Finally, regions are divided into *zones*. Zones have high-bandwidth,
low-latency network connections to other zones in the same region. In both
Google Cloud and Google Cloud Dedicated, putting resources in different zones in a region provides isolation from
many types of infrastructure, hardware, and software failures. Google Cloud Dedicated
has three zones, `u-germany-northeast1-a`, `u-germany-northeast1-b`, and `u-germany-northeast1-c`.

Some resources and services are zonal (such as a
[Compute Engine](/compute/docs/overview) virtual machine that runs in a
specific zone), regional (replicated and available across a region's zones), or
global/multi-regional (replicated across multiple or all regions). In
Google Cloud, global resources are scoped across all of
Google Cloud's many regions, providing world-wide availability.
Global resources still exist in Google Cloud Dedicated
(allowing you to, for example, reuse existing Google Cloud code
that targets these resources), but are equivalent to resources scoped to `u-germany-northeast1`.

## Google Cloud Dedicated resources and services

In cloud computing, what you might be used to thinking of as software and
hardware products become *services*. These services provide access to the
underlying resources, letting you add a wide range of functionality—from
managed Kubernetes to data storage - to your applications. You can see the list
of available Google Cloud Dedicated services in our
[product list](https://berlin.devsitetest.how/products).

When you develop your applications on Google Cloud Dedicated, you mix and match these services into combinations that provide the
infrastructure you need, and then add your code to enable the scenarios you want
to build.

## Interacting with Google Cloud Dedicated

There are multiple ways to interact with resources and services in Google Cloud Dedicated, including the following:

- The [Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/) provides a web-based, graphical user
interface that you can use to manage your Google Cloud Dedicated
projects and resources.

- The [Google Cloud CLI](/sdk/gcloud) lets you manage development workflow and
Google Cloud Dedicated resources directly from the
command line. For example, you can create a Compute Engine virtual machine
(VM) instance by running the `gcloud compute instances create` command in
your shell environment.

- Our provided [client libraries](/apis/docs/client-libraries-explained) help
you to interact with services programmatically in a variety of popular
languages. Cloud Client Libraries provide an optimized developer experience by
using each supported language's natural conventions and styles. They also
reduce the boilerplate code you have to write because they're designed to
enable you to work with service metaphors in mind, rather than
implementation details or service API concepts.

- You can use an "infrastructure as code" (IaC) approach by using
[Terraform](/docs/terraform) and the Google Cloud Terraform
provider.

You can learn more in [Interacting with Google Cloud Dedicated](/docs/get-started/interact-with-resources).

## Projects

Any Google Cloud Dedicated resources that you allocate
and use must belong to a project. You can think of a project as the organizing
entity for what you're building. A project is made up of the settings,
permissions, and other metadata that describe your applications. Resources
within a single project can work together, for example by communicating through
an internal network, subject to regions-and-zones rules. A project can't access
another project's resources unless you use
[Shared VPC](/vpc/docs/shared-vpc) or
[VPC Network Peering](/vpc/docs/vpc-peering).

Each Google Cloud Dedicated project has the following:

- A project name, which you provide.

- A unique project ID, which you can provide or Google Cloud Dedicated
can provide for you. All Google Cloud Dedicated
project IDs are automatically prefixed with `eu0:`.

- A project number, which Google Cloud Dedicated
provides.

So, for example, the same project might have:

- The project name `Ponycopter`

- The project ID `eu0:ponycopter`

- The project number `123456789012`

As you work with Google Cloud Dedicated, you use these
identifiers in commands and API calls. For example, you might specify that you
want to use the project as your default for the Google Cloud CLI with the
following command:


```
gcloud config set project eu0:ponycopter
```


You can create multiple projects and use them to separate your work in whatever
way makes sense for you. For example, you might have one project that can be
accessed by all team members and a separate project that can only be accessed by
certain team members.

A project serves as a namespace. This means every resource within each project
must have a unique name, but you can usually reuse resource names if they are in
separate projects. Some resource names must be unique within Google Cloud Dedicated. Refer to the documentation for the resource for details.

Each project is associated with one billing account. Multiple projects can have
their resource usage billed to the same account.

For more information, see [Creating and managing
projects](/resource-manager/docs/creating-managing-projects).

## What's next

- Learn more about the differences between Google Cloud Dedicated
and Google Cloud in [Key differences from
Google Cloud](/docs/overview/tpc-key-differences).

- Explore our available [products and services](https://berlin.devsitetest.how/products).

- Find out how to [get started with Google Cloud Dedicated](/docs/get-started-tpc).