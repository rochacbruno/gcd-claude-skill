# Authentication for Terraform

Source: https://berlin.devsitetest.how/docs/terraform/authentication
Last updated: 2026-07-07

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/terraform/tpc-differences) for more details.














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

Developer tools

](https://berlin.devsitetest.how/docs/costs-usage)






- 








[

Terraform on Google Cloud

](https://berlin.devsitetest.how/docs/terraform)






- 








[

Reference

](https://berlin.devsitetest.how/docs/terraform/api)












# Authentication for Terraform 






- On this page 
- [ Authenticate when using Terraform in a local development environment ](#local_dev_environment)

- [ Authenticate using a user account ](#auth_with_user_account)
- [ Authenticate using service account impersonation ](#auth_using_sa_impersonation)

- [ Authenticate when running Terraform on Google Cloud Dedicated ](#auth_on_cloud)
- [ Authenticate when running Terraform on-premises or on a different cloud provider ](#auth_on_cloud_provider)

- [ Authenticate using Workload Identity Federation ](#wlif)

- [ Authenticate using service account keys ](#auth_using_sa_keys_onprem)
- [ Authenticate to Cloud Storage backends ](#gcs_backends)
- [ What's next ](#whats_next)
- 










This document describes how to authenticate to Google Cloud Dedicated in Germany when using
Terraform.

Application Default Credentials (ADC) is the recommended way to authenticate to
Google Cloud Dedicated when using Terraform. ADC is a strategy used by the
authentication libraries to automatically find credentials based on the
application environment. When you use ADC, Terraform can run in either a
development or production environment without changing how it authenticates to
Google Cloud Dedicated in Germany services and APIs. For information about where ADC looks for
credentials and in what order, see [How Application Default Credentials
works](/docs/authentication/application-default-credentials).

## Authenticate when using Terraform in a local development environment 

When you're using Terraform in a local development environment, such as a
development workstation, you can authenticate using the credentials associated
with your [user account](/docs/authentication#user-accounts) or [service
account](/iam/docs/service-account-overview).

### Authenticate using a user account

To configure ADC with a user account, you use the Google Cloud CLI:











- 









[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).

After signing in,
[initialize](/sdk/docs/initializing) the Google Cloud CLI by running the following command:





```
gcloud init
```




















- 









Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








A sign-in screen appears. After you sign in, your credentials are stored in the
[
local credential file used by ADC](/docs/authentication/application-default-credentials#personal).













### Authenticate using service account impersonation

You can use service account impersonation to set up a local ADC file. Terraform
uses those credentials automatically.

- 

Make sure you must have the Service Account Token Creator
(`roles/iam.serviceAccountTokenCreator`) IAM role on the
service account you are impersonating. For more information, see [Required
roles](/docs/authentication/use-service-account-impersonation#required-roles).

- 

Use service account impersonation to create a local ADC file by running the
following command:


```
gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL 
```


If you want to allow users to use a shared primary authentication source
and a variable service account per environment, set the
[`impersonate_service_account`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#impersonate_service_account)
field in your Terraform configuration file:


```
provider "google" { 
impersonate_service_account = " SERVICE_ACCT_EMAIL " 
} 
```


## Authenticate when running Terraform on Google Cloud Dedicated

When running Terraform on a Google Cloud Dedicated cloud-based development
environment such as Cloud Shell, the tool uses the credentials you provided
when you signed in for authentication.

When using Terraform with Google Cloud Dedicated services such as Compute Engine,
App Engine, and Cloud Run functions, you can attach a [user-managed service
account](/iam/docs/service-account-types#user-created) to resources. Generally,
attaching a service account is supported when that service's resources can run
or include application code. When you attach a service account to a resource,
the code running on the resource can use that service account as its identity.

Attaching a user-managed service account is the preferred way to provide
credentials to ADC for production code running on Google Cloud Dedicated.

For help determining the roles that you need to provide to your service account,
see [Choose predefined roles](/iam/docs/choose-predefined-roles).

For information about which resources you can attach a service account to, and
help with attaching the service account to the resource, see the
[IAM documentation on attaching a service
account](/iam/docs/attach-service-accounts#attaching-new-resource).











Set up authentication:




- 
Ensure that you have the Create Service Accounts IAM role
(`roles/iam.serviceAccountCreator`) and the Project IAM Admin role
(`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](/iam/docs/granting-changing-revoking-access).


- 


Create the service account:



```
gcloud iam service-accounts create SERVICE_ACCOUNT_NAME 
```



Replace ` SERVICE_ACCOUNT_NAME ` with a name for the service account.





- 



To provide access to your project and your resources, grant a role to the service account:



```
gcloud projects add-iam-policy-binding PROJECT_ID --member = "serviceAccount: SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com" --role = ROLE 
```



Replace the following:





- ` SERVICE_ACCOUNT_NAME `: the name of the service account

- ` PROJECT_ID `: the project ID where you created the service account

- ` ROLE `: the role to grant










- 
To grant another role to the service account, run the command as you did in the previous step.




- 


Grant the required role to the principal that
will attach the service account to other resources.




```
gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com --member = "principal://iam.googleapis.com/locations/global/workforcePools/ POOL_ID /subject/ SUBJECT_ID " --role = roles/iam.serviceAccountUser
```



Replace the following:





- ` SERVICE_ACCOUNT_NAME `: the name of the service account.

- ` PROJECT_ID `: the project ID where you created the service account.

- ` POOL_ID `: a workforce identity pool ID.

- 
` SUBJECT_ID `: a subject ID; typically the identifier for a user
in a workforce identity pool. For details,
see [
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users).










## Authenticate when running Terraform on-premises or on a different cloud provider

If you are running your application outside of Google Cloud Dedicated, you need to
provide credentials that are recognized by Google Cloud Dedicated to use
Google Cloud Dedicated services.

### Authenticate using Workload Identity Federation

The preferred way to authenticate with Google Cloud Dedicated using credentials from
an external IdP is to use
[Workload Identity Federation](/iam/docs/workload-identity-federation). You can
create a credential configuration file and set the
`GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to it. This
approach is more secure than creating a service account key. For instructions
on setting up Workload Identity Federation for ADC, see
[Workload Identity Federation with other clouds](/iam/docs/workload-identity-federation-with-other-clouds).

## Authenticate using service account keys

When running Terraform in a local development environment, on premises, or
a different cloud provider, you can create a service account, grant it the
IAM roles that your application requires, and create a key for
the service account.

To create a service account key and make it available to ADC:

- 

Create a service account with the roles your application needs, and a key
for that service account, by following the instructions in [Creating a
service account key](/iam/docs/keys-create-delete#creating).

## Authenticate to Cloud Storage backends

Terraform lets you configure Cloud Storage as a backend to store Terraform
state files. To authenticate to a [Cloud Storage backend](/docs/terraform/resource-management/store-state),
use any of the methods described on this page. For information on
configuration variables related to authentication for Cloud Storage
backends, see the
[Terraform backends page for Cloud Storage](https://developer.hashicorp.com/terraform/language/settings/backends/gcs#configuration-variables).

## What's next

- Work through the [Terraform for Google Cloud Dedicated quickstart](/docs/terraform/create-vm-instance)

- Learn about the [basic Terraform commands](/docs/terraform/basic-commands).