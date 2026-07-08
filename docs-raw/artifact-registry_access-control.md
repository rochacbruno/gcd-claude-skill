# Access control with IAM

Source: https://berlin.devsitetest.how/artifact-registry/docs/access-control
Last updated: 2026-07-07

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/artifact-registry/docs/tpc-differences) for more details.














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

Application development

](https://berlin.devsitetest.how/docs/application-development)






- 








[

Artifact Registry

](https://berlin.devsitetest.how/artifact-registry/docs)






- 








[

Guides

](https://berlin.devsitetest.how/artifact-registry/docs/overview)












# Access control with IAM 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Overview ](#overview)

- [ Google Cloud Dedicated default permissions ](#gcp)
- [ Third-party integration ](#third-party)

- [ Roles and permissions ](#permissions)

- [ Predefined Artifact Registry roles ](#roles)
- [ Basic IAM roles ](#basic)

- [ Granting roles ](#grant)

- [ Granting project-wide roles ](#grant-project)
- [ Granting repository-specific roles ](#grant-repo)
- [ Configuring public access to a repository ](#public)
- [ Revoking roles ](#revoking_roles)

- [ Granting conditional access with tags ](#tags)
- [ Integrating with Google Cloud Dedicated services ](#integration)

- [ Default service accounts for Google Cloud Dedicated in Germany services ](#gcp-permissions)
- [ Granting access to Compute Engine instances ](#compute)
- [ Granting access to Google Kubernetes Engine clusters ](#gke)

- [ Artifact Registry service account ](#gcr-sa)
- [ What's next ](#whats_next)
- 










This page describes access control with Identity and Access Management (IAM) in
Artifact Registry.

Default permissions for Artifact Registry minimize setup effort when
implementing a CI/CD pipeline. You can also integrate Artifact Registry
with third-party CI/CD tools and configure the permissions and authentication
required to access repositories.

## Before you begin 

- [Enable Artifact Registry](/artifact-registry/docs/enable-service),
including enabling the API and installing the Google Cloud CLI.

- If you want to apply repository-specific permissions, then
[create an Artifact Registry repository](/artifact-registry/docs/repositories/create-repos)
for your packages.

## Overview

IAM [permissions](/iam/docs/overview#permissions) and
[roles](/iam/docs/overview#roles) determine your ability to create, view,
edit, or delete data in an Artifact Registry repository.

A role is a collection of permissions. You can't grant a principal permissions
directly; instead, you grant them a role. When you grant a role to a principal,
you grant them all the permissions that the role contains. You can grant
multiple roles to the same principal.

### Google Cloud Dedicated default permissions

By default, the following permissions apply to Google Cloud Dedicated CI/CD services
in the same project as Artifact Registry:

- Compute Engine and [supported Google Kubernetes Engine versions](/artifact-registry/docs/integrate-gke) use the
Compute Engine
[default service account](/compute/docs/access/service-accounts#default_service_account),
which has read-only access to storage.

If all your services are in the same Google Cloud Dedicated in Germany project and the default
permissions meet your needs, you don't need to configure permissions.

You must configure Artifact Registry permissions for these services if:

- You want to use these services to access Artifact Registry in another
project. In the project with Artifact Registry, [grant](#grant) the
[workload identity pool](/iam/docs/workload-identity-federation#pools) or service account for each service the
required role.

- You're using a GKE version that does not have built-in
support for pulling images from Artifact Registry. See the
[GKE](/artifact-registry/docs/integrate-gke) section for configuration instructions.

- You want the default service account to have read and write access to
repositories. See the following information for details:

- [Compute Engine](#compute)

- [GKE](#gke)

- You're using a user-provided service account for your runtime environments
instead of the default service account. In the project with
Artifact Registry, [grant](#grant) your service account the required
role.

### Third-party integration

For third-party clients, you must configure both permissions and authentication.

Traditionally, applications running outside Google Cloud Dedicated use
[service account keys](/iam/docs/service-account-creds#key-types)
to access Google Cloud Dedicated resources. However, service account keys are
powerful credentials, and can present a security risk if they are not managed
correctly.

Workload Identity Federation lets you use Identity and Access Management to
grant external identities [IAM roles](/iam/docs/overview#roles),
including the ability to impersonate service accounts. This approach eliminates
the maintenance and security burden associated with service
account keys.

**Use Workload Identity Federation**:

- [Create a Workload Identity Federation pool](/iam/docs/manage-workload-identity-pools-providers#create-pools).

- [Create a Workload Identity Federation provider](/iam/docs/manage-workload-identity-pools-providers#create-provider).

- [Grant](#grant) the appropriate Artifact Registry role to the workload
identity pool to allow repository access. For more information, see
[Allow your external workload to access Google Cloud Dedicated in Germany resources](/iam/docs/workload-identity-federation-with-other-providers#access).

- If you need to access Artifact Registry for longer periods of time,
then configure the OIDC token expiration time to a longer period in your
[credential configuration](/iam/docs/workload-identity-federation-with-other-providers#create-credential-config).

- 

Configure your third-party client to authenticate with
Artifact Registry.


- Container images: [Docker](/artifact-registry/docs/docker/authentication),
[Helm](/artifact-registry/docs/helm/authentication)







- OS packages: [Debian](/artifact-registry/docs/os-packages/debian/configure),
[RPM](/artifact-registry/docs/os-packages/rpm/configure)

**Use a service account**:

- [Create](/iam/docs/service-accounts-create#creating) a service
account to act on behalf of your application, or choose an existing service
account that use for your CI/CD automation.

- [Grant](#grant) the appropriate Artifact Registry role to the service
account to provide repository access.

- 

Configure your third-party client to authenticate with
Artifact Registry.


- Container images: [Docker](/artifact-registry/docs/docker/authentication),
[Helm](/artifact-registry/docs/helm/authentication)







- OS packages: [Debian](/artifact-registry/docs/os-packages/debian/configure),
[RPM](/artifact-registry/docs/os-packages/rpm/configure)

## Roles and permissions

Every Artifact Registry API method requires that the [principal](/iam/docs/overview#concepts_related_identity) making
the request has the required permissions to use the resource. Permissions are
given to principals by setting policies that grant the principal a predefined
role on the resource.

You can grant roles on the Google Cloud Dedicated in Germany project or the Artifact Registry
repository.

### Predefined Artifact Registry roles

IAM provides [predefined roles](/iam/docs/roles-permissions)
that grant access to specific Google Cloud Dedicated resources.

Use the following predefined roles for repositories:



| 
Role | 
Description | 
|




| 
Artifact Registry Reader

(`roles/artifactregistry.reader`) | 
View and get artifacts, view repository metadata.
| 
|

| 
Artifact Registry Writer

(`roles/artifactregistry.writer`) | 
Read and write artifacts.
| 
|

| 
Artifact Registry Repository Administrator

(`roles/artifactregistry.repoAdmin`) | 
Read, write, and delete artifacts.
| 
|

| 
Artifact Registry Administrator

(`roles/artifactregistry.admin`) | 
Create and manage repositories and artifacts.
| 
|



For a full list of the individual permissions in each role, refer to
[Artifact Registry roles](/iam/docs/roles-permissions/artifactregistry).
You can also use the
[`gcloud iam roles describe`](/sdk/gcloud/reference/iam/roles/describe)
command to view a list of permissions in each role.

### Basic IAM roles

Basic roles are highly permissive roles that existed prior to the introduction
of IAM. You shouldn't grant basic roles in a production
environment, but you can grant them in a development or test environment.

Use [predefined roles](#roles) for repository
access whenever possible so that users and service accounts only have the
permissions that are required.

For more information on basic roles, see
[IAM basic and predefined roles reference](/iam/docs/understanding-roles).

## Granting roles

Grant roles at the project level if the same roles apply to all
repositories in the project. If some accounts require different levels of
access, grant roles at the repository level.

If you're granting roles using the `gcloud` command, you can specify a single
role binding for a principal or you can make large-scale policy changes by
getting a resource's allow policy, modifying it, and then setting the modified
allow policy. For more information, see
[Grant or revoke multiple roles programmatically](/iam/docs/manage-access-other-resources#multiple-roles-programmatic).

### Granting project-wide roles

Grant a role at the project level if the same permissions apply to all
repositories in the project.

To add a user or service account to a project and grant them an
Artifact Registry role:


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

Open the IAM page in the Google Cloud Dedicated console.

[Open
the IAM page](https://console.cloud.berlin-build0.goog/iam-admin/iam) 

- 

Click **Select a project**, choose the project where
Artifact Registry is running, and click **Open**.

- 

Click **Add**.

- 

Enter an email address. You can add individuals, service accounts, or
Google Groups as principals.

- 

Select a role for the principal. In accordance with the security
principle of least privilege, consider granting the least amount of
privilege needed to access the required Artifact Registry resources. For information on
Artifact Registry predefined roles and permissions, see
[Predefined Artifact Registry roles](/artifact-registry/docs/access-control#roles).

- 

Click **Save**.




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

To grant a role to a single principal, run the following command:


```
gcloud projects add-iam-policy-binding PROJECT \ 
--member = PRINCIPAL \ 
--role = ROLE 
```


where

- PROJECT is the ID of the project where Artifact Registry
is running.

- 

PRINCIPAL is the principal to add the binding for. Use the form
`user|group|serviceAccount:email` or `domain:domain`.

Examples: `user:test-user@gmail.com`, `group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.

- 

ROLE is the [role](/artifact-registry/docs/access-control#roles) that you want to grant.

For more information, see the [add-iam-policy-binding](/sdk/gcloud/reference/projects/add-iam-policy-binding)
documentation.

To grant roles using a policy file, see
[Grant or revoke multiple roles programmatically](/iam/docs/manage-access-other-resources#multiple-roles-programmatic)




### Granting repository-specific roles

Grant repository-level roles when you want users or service accounts to
have different levels of access for each repository in your project.


[ Console ](#console) [ gcloud ](#gcloud) [ Terraform ](#terraform) 
More 




To grant access to a specific repository:

- 

Open the **Repositories** page in the Google Cloud Dedicated console.



[Open the Repositories page](https://console.cloud.berlin-build0.goog/artifacts)

- 

Select the appropriate repository.

- 

If the info panel is not displayed, click **Show Info Panel** in the menu
bar.

- 

On the Permissions tab, click **Add Principal**.

- 

Enter an email address. You can add individuals, service accounts, or Google
Groups as principals.

- 

Select a role for the principal. In accordance with the security
principle of least privilege, consider granting the least amount of
privilege needed to access the required Artifact Registry resources. For
information on Artifact Registry predefined roles and permissions,
see [Predefined Artifact Registry roles](/artifact-registry/docs/access-control#roles).

- 

Click **Save**.




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

You can set an IAM set of individual policy bindings or
use a policy file.

To grant a role to a single principal, run the following command:


```
gcloud artifacts repositories add-iam-policy-binding REPOSITORY \ 
--location = LOCATION \ 
--member = PRINCIPAL \ 
--role = ROLE 
```


where

- REPOSITORY is the ID of the repository.

- 

PRINCIPAL is the principal to add the binding for. Use the form
`user|group|serviceAccount:email` or `domain:domain`.

Examples: `user:test-user@gmail.com`, `group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.

- 

ROLE is the [role](#roles) that you want to grant.

- 

LOCATION is the regional
[location](/artifact-registry/docs/repo-locations) of the repository.

For example, to add an IAM policy binding for the role
`roles/artifactregistry.writer` for the user `write@gmail.com` with the
repository `my-repo` in the location `--u-germany-northeast1`, run:


```
gcloud artifacts repositories add-iam-policy-binding my-repo \ 
--location = u-germany-northeast1 --member = user:write@gmail.com --role = roles/artifactregistry.writer
```


To grant roles using a policy file, use the procedure described in
[Grant or revoke multiple roles programmatically](/iam/docs/manage-access-other-resources#multiple-roles-programmatic)
with the
[gcloud artifacts repositories get-iam-policy](/sdk/gcloud/reference/artifacts/repositories/get-iam-policy)
and
[gcloud artifacts repositories set-iam-policy](/sdk/gcloud/reference/artifacts/repositories/set-iam-policy)
commands.




Use the [google_artifact_registry_repository_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository_iam) resource to
configure an IAM policy. The following example defines a service
account with the resource name `repo-account` and grants it read access to a
repository with the resource name `my-repo`.

If you're new to using Terraform for Google Cloud Dedicated in Germany, see the
[Get Started - Google Cloud Dedicated in Germany](https://learn.hashicorp.com/collections/terraform/gcp-get-started) page on the
HashiCorp website.


```
provider "google" { 
project = " PROJECT-ID " 
} 

resource "google_artifact_registry_repository" "my-repo" { 
provider = google-beta 

location = " LOCATION " 
repository_id = " REPOSITORY " 
description = " DESCRIPTION " 
format = " FORMAT " 
} 

resource "google_service_account" "repo-account" { 
provider = google-beta 

account_id = " ACCOUNT-ID " 
display_name = "Repository Service Account" 
} 

resource "google_artifact_registry_repository_iam_member" "repo-iam" { 
provider = google-beta 

location = google_artifact_registry_repository.my-repo.location 
repository = google_artifact_registry_repository.my-repo.name 
role = "roles/artifactregistry.reader" 
member = "serviceAccount:${google_service_account.repo-account.email}" 
} 
```


ACCOUNT-ID is the ID of the service account. This is the
the part of the service account email field before the `@` symbol.

For additional examples, see the documentation for the
[google_artifact_registry_repository_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository_iam)
resource.



### Configuring public access to a repository

If you have artifacts that you want to make available to anyone on the internet
without authentication, store them in a repository that you make public.

To configure a repository for public read-only access, grant the
Artifact Registry Reader role to the principal `allUsers`. We also recommend
[capping user request quotas](/artifact-registry/quotas#user-quota) so that a single
user can't use up your project's overall quota.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

Open the **Repositories** page in the Google Cloud Dedicated console.



[Open the Repositories page](https://console.cloud.berlin-build0.goog/artifacts)

- 

Select the appropriate repository.

- 

If the info panel is not displayed, click **Show Info Panel** in the menu
bar.

- 

On the Permissions tab, click **Add Principal**.

- 

In **New principals** field, enter `allUsers`.

- 

Select the role **Artifact Registry Reader**.

- 

Set a per-user limit on Artifact Registry API requests to prevent
misuse by unauthenticated users. For instructions, see
[Capping usage](/docs/quotas/view-manage#capping_usage).




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

Run the following command:


```
gcloud artifacts repositories add-iam-policy-binding REPOSITORY \ 
--location = LOCATION --member = allUsers --role = ROLE 
```


where

- 

REPOSITORY is the ID of the repository.

- 

ROLE is the [role](#roles) that you want to grant.

+ LOCATION is the regional
[location](/artifact-registry/docs/repo-locations) of the repository.

For example, configure the repository `my-repo` in the location
`--u-germany-northeast1` as public, run:


```
gcloud artifacts repositories add-iam-policy-binding my-repo \ 
--location = u-germany-northeast1 --member = allUsers --role = roles/artifactregistry.reader
```


- 

Set a per-user limit on Artifact Registry API requests to prevent
misuse by unauthenticated users. For instructions, see
[Capping usage](/docs/quotas/view-manage#capping_usage).




### Revoking roles

To revoke access to a repository, remove the principal from the list of authorized
principals.

To remove public access from a repository, remove the `allUsers` principal.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




To revoke permissions:

- 

Open the **Repositories** page in the Google Cloud Dedicated console.



[Open the Repositories page](https://console.cloud.berlin-build0.goog/artifacts)

- 

Select the appropriate repository.

- 

If the info panel is not displayed, click **Show Info Panel** in the menu
bar.

- 

On the Permissions tab, expand the appropriate principal. If you
are making a public repository private, expand the `allUsers` principal.

- 

Click **Remove principal** to revoke access.




- 









In the Google Cloud Dedicated console, activate Cloud Shell.



[Activate Cloud Shell](https://console.cloud.berlin-build0.goog/?cloudshell=true)



At the bottom of the Google Cloud Dedicated console, a
[Cloud Shell](/shell/docs/how-cloud-shell-works)
session starts and displays a command-line prompt. Cloud Shell is a shell environment
with the Google Cloud CLI
already installed and with values already set for
your current project. It can take a few seconds for the session to initialize.







- 

To revoke a role at the project level, run the following command:


```
gcloud projects remove-iam-policy-binding PROJECT \ 
--member = PRINCIPAL \ 
--role = ROLE 
```


- PROJECT is the project ID.

- 

PRINCIPAL is the principal to remove the binding for. Use the form
`user|group|serviceAccount:email` or `domain:domain`.

Examples: `user:test-user@gmail.com`, `group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.

- 

ROLE is the [role](#roles) that you want to revoke.

To revoke a role for a repository, run the following command:


```
gcloud artifacts repositories remove-iam-policy-binding REPOSITORY 
--location = LOCATION \ 
--member = PRINCIPAL \ 
--role = ROLE 
```


where

- REPOSITORY is the ID of the repository.

- 

PRINCIPAL is the principal to remove the binding for. Use the form
`user|group|serviceAccount:email` or `domain:domain`.

Examples: `user:test-user@gmail.com`, `group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.

To revoke public access to the repository, specify the principal `allUsers`.

- 

ROLE is the [role](#roles) that you want to revoke.

For example, to remove a policy binding for the role
`roles/artifactregistry.writer` for the user `write@gmail.com` with the
repository `my-repo` in the location `--u-germany-northeast1`, run:


```
gcloud artifacts repositories remove-iam-policy-binding my-repo \ 
--location = u-germany-northeast1 \ 
--member = user:write@gmail.com \ 
--role = roles/artifactregistry.writer
```


To revoke public access to `my-repo` in the location `--u-germany-northeast1`, run:


```
gcloud artifacts repositories remove-iam-policy-binding my-repo \ 
--location = u-germany-northeast1 \ 
--member = allUsers \ 
--role = roles/artifactregistry.reader
```





## Granting conditional access with tags

Project administrators can create tags for resources across Google Cloud Dedicated
and manage them in [Resource Manager](/resource-manager/docs/tags/tags-overview). When you attach a tag to a
Artifact Registry repository, administrators can use the tag with
IAM conditions to grant conditional access to the repository.

You cannot attach tags to individual artifacts.

For more information see the following documentation:

- Administrators setting up tags and access control

- [Creating and managing tags](/resource-manager/docs/tags/tags-creating-and-managing)

- [Tags and access control](/iam/docs/tags-access-control).

- Developers attaching tags to repositories

- [Tagging repositories](/artifact-registry/docs/repositories/tag-repos)

## Integrating with Google Cloud Dedicated services

For most Google Cloud Dedicated service accounts, configuring access to a registry
only requires granting the appropriate IAM roles.

### Default service accounts for Google Cloud Dedicated in Germany services

Google Cloud Dedicated services such as Google Kubernetes Engine use a
[default service account](/iam/docs/service-account-types#default) or
[service agent](/iam/docs/service-account-types#default) to interact with
resources within the same project.

You must configure or modify permissions yourself if:

- The Google Cloud Dedicated in Germany service is in a different project than Artifact Registry.

- The default permissions don't meet your needs.

- You're using a user-provided service account to interact with
Artifact Registry instead of the default service account.

- Your organizational policy configuration prevents automatic role grants to
default service accounts.

The following service accounts typically access Artifact Registry. The
email address for the service account includes the Google Cloud Dedicated
[project ID or project number](/resource-manager/docs/creating-managing-projects#identifying_projects)
of the project where the service is running.




| 
Service | 
Service account | 
Email address | 
|

| 
Compute Engine | 
[
Compute Engine default service account](/compute/docs/access/service-accounts#default_service_account) | 
PROJECT-NUMBER -compute@developer.eu0-system.iam.gserviceaccount.com | 
|

| 
GKE | 
[
Compute Engine default service account](/compute/docs/access/service-accounts#default_service_account)

The default service account for nodes. | 
PROJECT-NUMBER -compute@developer.eu0-system.iam.gserviceaccount.com | 
|



Depending on your organization policy configuration, the default service account might
automatically be granted the [Editor role](/iam/docs/roles-overview#basic) on your
project. We strongly recommend that you disable the automatic role grant by [
enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy
constraint](/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this
constraint is enforced by default.

If you disable the automatic role grant, you must decide which roles to grant to the default
service accounts, and then [grant these
roles](/iam/docs/granting-changing-revoking-access) yourself.

If the default service account already has the Editor role, we recommend that you replace the
Editor role with less permissive roles.

### Granting access to Compute Engine instances

VM instances that access repositories must have both Artifact Registry
permissions and storage *access scope* configured.

While a service account's access level is determined by the
IAM roles granted to the service account, *access scopes* on
a VM instance determine the default OAuth scopes for requests made through the
gcloud CLI and client libraries on the instance. As a result, access scopes
potentially further limit access to API methods when authenticating with
[Application Default Credentials](/docs/authentication/application-default-credentials).

Compute Engine uses the following defaults:

- The [Compute Engine default service account](/compute/docs/access/service-accounts#default_service_account) is the identity for VM
instances. The service account email address has the suffix
**@developer.eu0-system.iam.gserviceaccount.com**.

- The default service account has the IAM basic
Editor role, if you have not [disabled this behavior](/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants).

- Instances you create with the default service account have the
Compute Engine [default access scopes](/compute/docs/access/service-accounts#default_scopes), including
read-only access to storage. While the Editor role generally grants write
access, the `read-only` storage access scope limits the instance service
account to downloading artifacts only from any repository in the same project.

You must configure the access scope of the service account if:

- The VM service account needs to access a repository in a different project.

- The VM service account needs to perform actions other than reading artifacts
from repositories. This typically applies third-party tools on a VM that need
to push images or run Artifact Registry `gcloud` commands.

To configure roles and set the access scope:

- 

In the project with your VM instance, get the name of the
[Compute Engine default service account](/compute/docs/access/service-accounts#default_service_account). The service account email address has the
suffix **@developer.eu0-system.iam.gserviceaccount.com**.

- 

In the project with the repository, [grant permissions](#grant) so that
the service account can access the repository.

- 

Set the access scope with the
[--scopes](/sdk/gcloud/reference/compute/instances/create#--scopes) option.

- 

Stop the VM instance. See
[Stopping an instance](/compute/docs/instances/stop-start-instance).

- 

Set the access scope with the following command:


```
gcloud compute instances set-service-account INSTANCE --scopes = SCOPE 
```


Replace SCOPE with the appropriate value.

- 

For Docker, the following options are supported:

- `storage-ro` - Grants read permission only for pulling images.

- `storage-rw` - Grants read and write permission for pushing or
pulling images.

- `cloud-platform` - View and manage data, including metadata, across
Google Cloud Dedicated service.

- 

For other formats, you must use the `cloud-platform` scope.

- 

Restart the VM instance. See
[Starting a stopped instance](/compute/docs/instances/stop-start-instance#starting_a_stopped_instance).

### Granting access to Google Kubernetes Engine clusters

GKE clusters and node pools can pull containers without any
additional configuration if all the following requirements are met:

- GKE is in the same project as Artifact Registry

- Nodes are using the default service account, the
[Compute Engine default service account](/compute/docs/access/service-accounts#default_service_account)

- Nodes were created with [read access to storage](#gke-scope) by:

- Using the Compute Engine [default access scopes](/compute/docs/access/service-accounts#default_scopes).

- Granting the `cloud-platform` access scope or another scope that includes
read access to storage.

- You're running a [supported version](/artifact-registry/docs/integrate-gke) of GKE

If your GKE environment does not meet these requirements the
instructions to grant access depend on whether you're using the
Compute Engine default service account or a user-provided service account as
the identity for your nodes.


Default service account 


The following configuration requirements apply to the
[Compute Engine default service account](/compute/docs/access/service-accounts#default_service_account):

- 

If GKE is in a different project than
Artifact Registry, [grant](#grant) the required permissions to the
service account.

- 

To push images, interact with repositories for formats other than
containers, or run `gcloud` commands from your cluster, you must set
[access scopes](#gke-scope) for the service account when you create the
cluster or node pool.

- 

If you're not using a [supported version](/artifact-registry/docs/integrate-gke) of
GKE, configure [imagePullSecrets](/artifact-registry/docs/access-control#pullsecrets).


User-provided service account 


If you want to use a user-provided [service account](/iam/docs/service-accounts)
as the identity for a cluster, you must:

- 

[Grant](#grant) the required permissions to the service account from the
Google Cloud Dedicated project where Artifact Registry is running.

- 

By default, creating a cluster or node pool with a user-provided service
account grants the `cloud-platform` access scope.

If you use the `--scopes` flag with the
[gcloud container clusters create](/sdk/gcloud/reference/container/clusters/create) or
[gcloud container node-pools create](/sdk/gcloud/reference/container/node-pools/create) command, you must include
the appropriate
[access scopes](#gke-scope) for use with Artifact Registry.




#### Setting access scopes

Access scopes are the legacy method of specifying authorization for
Compute Engine VMs. To pull images from Artifact Registry repositories,
GKE nodes must have the storage read-only access scope or
another storage access scope that includes storage read access.

You can only set access scopes when you create a cluster or node pool. You
cannot change access scopes on existing nodes.

- If you're using the [Compute Engine default service account](/compute/docs/access/service-accounts#default_service_account),
GKE creates nodes with the Compute Engine
[default access scopes](/compute/docs/access/service-accounts#default_scopes), which includes read-only access to
storage.

- If you're using a user-provided service account, GKE creates
nodes with the `cloud-platform` scope, the scope required for most
Google Cloud Dedicated services.

To specify access scopes when creating a cluster, run the following command:


```
gcloud container clusters create NAME --scopes = SCOPES 
```


To specify access scopes when creating a node pool, run the following command:


```
gcloud container node-pools create NAME --scopes = SCOPES 
```


Replace the following values:

- NAME is the name of the cluster or node pool.

- 

SCOPES is a comma-separated list of access scopes to grant.

- 

To access Docker repositories, use one of the following scopes:

- 

`storage-ro` - Grants read-only permission for pulling images.

- 

`storage-rw` - Grants read and write permission for pushing or
pulling images.

- 

`cloud-platform` - View and manage data, including metadata, across
Google Cloud Dedicated service.

- 

To access other repositories, you must use the `cloud-platform` scope.

For a full list of scopes, see the documentation for
[gcloud container clusters create](/sdk/gcloud/reference/container/clusters/create) or
[gcloud container node-pools create](/sdk/gcloud/reference/container/node-pools/create).

For more information about scopes you can set when creating a new cluster,
refer to the documentation for the command
[gcloud container clusters create](/sdk/gcloud/reference/container/clusters/create).

#### Configuring an `imagePullSecret`

To configure an `imagePullSecret`:

- 

In the project with GKE, find Compute Engine default
service account. The account email address has the suffix
**@developer.eu0-system.iam.gserviceaccount.com**.

- 

[Download the service account key](/iam/docs/creating-managing-service-account-keys#creating_service_account_keys)
for the service account.

- 

In the project with the repository, verify that you have
[granted permissions](#grant) to the repository.

- 

In the project with your cluster, create an `imagePullSecret` secret called
`artifact-registry` with the service account key.


```
kubectl create secret docker-registry artifact-registry \ 
--docker-server = https:// LOCATION -docker.pkg-berlin-build0.goog \ 
--docker-email = SERVICE-ACCOUNT-EMAIL \ 
--docker-username = _json_key \ 
--docker-password = " $( cat KEY-FILE ) " 
```


Replace the following:



- LOCATION is the regional
location of the repository.


- SERVICE-ACCOUNT-EMAIL is the email address of the
Compute Engine service account.

- KEY-FILE is the name of your service account key file. For
example `key.json`.

- 

Open your default service account:


```
kubectl edit serviceaccount default --namespace default
```


Every [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
in your Kubernetes cluster has a default service account called `default`.
This default service account is used to pull your container image.

- 

Add the newly created `imagePullSecret` secret to your default service
account:


```
imagePullSecrets: 
- name: artifact - registry 
```


Your service account should now look like this:


```
apiVersion: v1 
kind: ServiceAccount 
metadata: 
name: default 
namespace: default 
... 
secrets: 
- name: default - token - zd84v 
# The secret you created: 
imagePullSecrets: 
- name: artifact - registry 
```


Now, any new pods created in the current `default` namespace will have the
`imagePullSecret` secret defined.

## Artifact Registry service account

The Artifact Registry Service Agent is a Google-managed service account that
acts on behalf of Artifact Registry when interacting with Google Cloud Dedicated in Germany
services. For more information about the account and its permissions, see
[Artifact Registry service account](/artifact-registry/docs/ar-service-account).

## What's next

After you have set up permissions, learn more about working with your artifacts.


- Container images: [Docker](/artifact-registry/docs/docker),
[Helm](/artifact-registry/docs/helm)


- OS packages: [Debian](/artifact-registry/docs/os-packages/debian),
[RPM](/artifact-registry/docs/os-packages/rpm)