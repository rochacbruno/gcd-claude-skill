# Cloud de Confiance by S3NS overview

Source: https://documentation.s3ns.fr/docs/overview/tpc-overview
Last updated: 2026-08-11

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

Get started

](https://documentation.s3ns.fr/docs/get-started)












# Cloud de Confiance by S3NS overview 






- On this page 
- [ Differences from Google Cloud ](#differences-from-google-cloud)
- [ Universes, regions, and zones ](#universes-regions-and-zones)
- [ Cloud de Confiance resources and services ](#resources-and-services)
- [ Interacting with Cloud de Confiance ](#interacting)
- [ Projects ](#projects)
- [ What's next ](#whats-next)
- 














Cloud de Confiance by S3NS is a cloud platform based in France
that provides the benefits of Google's cloud technology and services, while
offering strong data and operational sovereignty guarantees. Cloud de Confiance
is a separate product from Google Cloud, with no data leaving Cloud de Confiance's local jurisdiction. S3NS, rather than
Google Cloud, is responsible for service and infrastructure
management and support.

This makes Cloud de Confiance by S3NS more suitable for projects
and workloads with enhanced regulatory requirements, such as those that need to
be hosted in a
[SecNumCloud](https://cyber.gouv.fr/sites/default/files/document/anssi_Recommendations%20on%20hosting%20sensitive%20IS%20in%20the%20cloud.pdf)
compliant environment.

This page gives you a high-level overview of Cloud de Confiance
and its features and services, with pointers for where to go next in our
documentation.

## Differences from Google Cloud 

While Cloud de Confiance is based on exactly the
same technology as Google Cloud, there are some significant
differences between the universes, with only a subset of
Google Cloud features and products available for Cloud de Confiance. One reason for this is because Cloud de Confiance
helps ensure data sovereignty by operating as a single, completely standalone
Cloud region, with no connection to Google Cloud's network.
Because of this, Google Cloud features that rely on the existence
of multiple Google regions—such as load balancing across regions, or
multi-region storage—are not supported in Cloud de Confiance.

Cloud de Confiance supports common use cases and
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
Compute Engine service is `compute.s3nsapis.fr` rather than `compute.googleapis.com`.

- Some Google Cloud tools and workflows are unavailable, or
work slightly differently.

- Older Compute Engine machine types are unavailable.

You can learn more about the differences between Cloud de Confiance
and Google Cloud in [Key differences from
Google Cloud](/docs/overview/tpc-key-differences). If you are
already familiar with Google Cloud we recommend reviewing this
information carefully before designing or implementing applications.

## Universes, regions, and zones

Underlying everything you do on Cloud de Confiance
are its physical machines that run your workloads and Cloud de Confiance
services. These machines live in data centers, and are logically structured into
universes, regions, and zones.

At the top of this hierarchy is the *universe*. A universe is a fully
self-contained Cloud, with its own networking that is separate from the public
internet and other universes. Google Cloud is the original
universe, with resources in data centers all over the world. Cloud de Confiance
is another, smaller universe, with all its resources in a single jurisdiction,
providing strict sovereignty compliance.

Within each universe there are geographic *regions*. Google Cloud
has many regions around the world, while Cloud de Confiance
currently has a single region, `u-france-east1`.

Finally, regions are divided into *zones*. Zones have high-bandwidth,
low-latency network connections to other zones in the same region. In both
Google Cloud and Cloud de Confiance, putting resources in different zones in a region provides isolation from
many types of infrastructure, hardware, and software failures. Cloud de Confiance
has three zones, `u-france-east1-a`, `u-france-east1-b`, and `u-france-east1-c`.

Some resources and services are zonal (such as a
[Compute Engine](/compute/docs/overview) virtual machine that runs in a
specific zone), regional (replicated and available across a region's zones), or
global/multi-regional (replicated across multiple or all regions). In
Google Cloud, global resources are scoped across all of
Google Cloud's many regions, providing world-wide availability.
Global resources still exist in Cloud de Confiance
(allowing you to, for example, reuse existing Google Cloud code
that targets these resources), but are equivalent to resources scoped to `u-france-east1`.

## Cloud de Confiance resources and services

In cloud computing, what you might be used to thinking of as software and
hardware products become *services*. These services provide access to the
underlying resources, letting you add a wide range of functionality—from
managed Kubernetes to data storage - to your applications. You can see the list
of available Cloud de Confiance services in our
[product list](https://documentation.s3ns.fr/products).

When you develop your applications on Cloud de Confiance, you mix and match these services into combinations that provide the
infrastructure you need, and then add your code to enable the scenarios you want
to build.

## Interacting with Cloud de Confiance

There are multiple ways to interact with resources and services in Cloud de Confiance, including the following:

- The [Cloud de Confiance console](https://console.cloud.s3nscloud.fr/) provides a web-based, graphical user
interface that you can use to manage your Cloud de Confiance
projects and resources.

- The [Google Cloud CLI](/sdk/gcloud) lets you manage development workflow and
Cloud de Confiance resources directly from the
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

You can learn more in [Interacting with Cloud de Confiance](/docs/get-started/interact-with-resources).

## Projects

Any Cloud de Confiance resources that you allocate
and use must belong to a project. You can think of a project as the organizing
entity for what you're building. A project is made up of the settings,
permissions, and other metadata that describe your applications. Resources
within a single project can work together, for example by communicating through
an internal network, subject to regions-and-zones rules. A project can't access
another project's resources unless you use
[Shared VPC](/vpc/docs/shared-vpc) or
[VPC Network Peering](/vpc/docs/vpc-peering).

Each Cloud de Confiance project has the following:

- A project name, which you provide.

- A unique project ID, which you can provide or Cloud de Confiance
can provide for you. All Cloud de Confiance
project IDs are automatically prefixed with `s3ns:`.

- A project number, which Cloud de Confiance
provides.

So, for example, the same project might have:

- The project name `Ponycopter`

- The project ID `s3ns:ponycopter`

- The project number `123456789012`

As you work with Cloud de Confiance, you use these
identifiers in commands and API calls. For example, you might specify that you
want to use the project as your default for the Google Cloud CLI with the
following command:


```
gcloud config set project s3ns:ponycopter
```


You can create multiple projects and use them to separate your work in whatever
way makes sense for you. For example, you might have one project that can be
accessed by all team members and a separate project that can only be accessed by
certain team members.

A project serves as a namespace. This means every resource within each project
must have a unique name, but you can usually reuse resource names if they are in
separate projects. Some resource names must be unique within Cloud de Confiance. Refer to the documentation for the resource for details.

Each project is associated with one billing account. Multiple projects can have
their resource usage billed to the same account.

For more information, see [Creating and managing
projects](/resource-manager/docs/creating-managing-projects).

## What's next

- Learn more about the differences between Cloud de Confiance
and Google Cloud in [Key differences from
Google Cloud](/docs/overview/tpc-key-differences).

- Explore our available [products and services](https://documentation.s3ns.fr/products).

- Find out how to [get started with Cloud de Confiance](/docs/get-started-tpc).