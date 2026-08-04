# Set up an identity provider

Source: https://documentation.s3ns.fr/docs/get-started-tpc/set-up-identity-provider
Last updated: 2026-07-29

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












# Set up an identity provider 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Procedure overview ](#procedure_overview)
- [ Sign in with your bootstrap ID ](#sign_in_with_your_bootstrap_id)
- [ Grant permissions to your bootstrap ID ](#grant_permissions_to_your_bootstrap_id)
- [ Configure Workforce Identity Federation ](#configure-workforce-identity-federation)
- [ Set an Organization Administrator ](#set_an_organization_administrator)
- [ Sign in with your administrator ID ](#sign_in_with_your_administrator_id)
- [ What's next ](#whats_next)
- 









An important first step in setting up Cloud de Confiance by S3NS is
setting up an identity provider (IdP), so that members of your organization can
sign in to Cloud de Confiance, and be authorized
to use services and resources with [IAM](/iam/docs/overview). In
Cloud de Confiance, you bring your own identity
provider using
[Workforce Identity Federation](/iam/docs/workforce-identity-federation), which lets
you continue to use existing
user IDs and groups if required. You can use Workforce Identity Federation
with any IdP that supports [OpenID Connect (OIDC)](https://openid.net/connect/)
or [SAML
2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html),
including Google Workspace, Microsoft Entra ID, Active Directory Federation Services (AD FS), and
Okta.

This page is for administrators who need to set up an identity provider for a
new organization in Cloud de Confiance, including
configuring an organization administrator role.

If your organization already has its identity provider set up (with you as
organization administrator) and you just need to set up new projects, networks, and
other resources for users, you can skip this guide and go straight to [Set up
your organization](/docs/get-started-tpc/set-up-organization). For other users who need to get started, including
developers and other technical practitioners, see [Get started with Cloud de Confiance](/docs/get-started-tpc).

Before you read this guide, you should:

- 

Understand the basic Cloud de Confiance
concepts described in the [Cloud de Confiance
overview](), including Cloud de Confiance
organizations and projects.

- 

Understand the
overall organization setup flow in [Get started with Cloud de Confiance](/docs/get-started-tpc).

## Before you begin

Before you configure a new Cloud de Confiance by S3NS
organization for the first time, you're provided with a temporary ID from a special Cloud de Confiance
IdP, known as your *bootstrap ID*, along with instructions for signing in. You
need this ID to complete the setup steps in this guide.

## Procedure overview

The following primary steps are involved in setting up your IdP:

- **Sign in with your bootstrap ID** to get initial administrator access to Cloud de Confiance by S3NS
and the Cloud de Confiance console. You'll do all the setup steps in this guide
by using the Cloud de Confiance console.

- **Grant your bootstrap ID permissions** so that you can configure
Workforce Identity Federation.

- **Configure Workforce Identity Federation** to get identity information from
your chosen IdP(s).

- **Create a new Organization Administrator** with an ID from your IdP (your
own or a group to which you belong), so that you can sign in and manage Cloud de Confiance by S3NS
without using your bootstrap ID.

- **Sign out and sign back in again** with your newly configured administrator ID.

## Sign in with your bootstrap ID

Sign in to Cloud de Confiance with your
bootstrap ID:

- Follow the instructions provided with your bootstrap ID to sign in to Cloud de Confiance.
You should now have access to the Cloud de Confiance console to complete the
remaining steps in this guide.

## Grant permissions to your bootstrap ID

Your bootstrap ID by default is the administrator of your organization, but has
no other permissions. To grant the necessary permissions to this ID to configure
Workforce Identity Federation, do the following:

- In the Cloud de Confiance console, navigate to the
**IAM & Admin** page:


[Go to IAM & admin](https://console.cloud.s3nscloud.fr/iam-admin)

The **IAM & Admin** page displays all the permissions for
your organization, and the identities (principals) to which they have been
granted. You should see only a single principal (your bootstrap ID) with the
Organization Administrator role.

- Click **Edit principal** edit next to
your ID.

- In the **Edit permissions** pane, select **Add another role**.

- In the **Select a role** drop-down, search for and select **IAM Workforce
Pool Admin**.

- Click **Save**.

You might need to wait a few minutes before the role is assigned to your
ID.

## Configure Workforce Identity Federation

Now that your bootstrap ID is authorized to configure
Workforce Identity Federation, you can add an identity provider (or providers)
to your organization. To do this you first need to create a workforce identity
*pool* that can be used across your organization, and then configure the pool to
use your provider(s). You can learn more about how
Workforce Identity Federation works in [the Workforce Identity Federation
documentation](/iam/docs/workforce-identity-federation).

- In the Cloud de Confiance console, navigate to **IAM** > **Workforce Identity Federation**:


[Go to Workforce Identity Federation](https://console.cloud.s3nscloud.fr/iam-admin/workforce-identity-pools)

You should be prompted to create a new workforce identity pool.

- Follow the **Console** instructions in [Configure
Workforce Identity Federation](/iam/docs/configuring-workforce-identity-federation#configure)
to add your workforce identity pool and IdP. Depending on your chosen IdP,
you might want to look at our provider-specific guides for common IdPs, for
example [Microsoft Entra ID](/iam/docs/workforce-sign-in-microsoft-entra-id)
and [Okta](/iam/docs/workforce-sign-in-okta).

You *must* set the optional [`google.posix_username` attribute
mapping](/iam/docs/workforce-identity-federation#attribute-mappings) while
setting up your provider, as in the following example. This is because this
attribute mapping is required for SSH to work.


```
google.subject = assertion.subject
google.posix_username = assertion.attributes [ 'username' ] 
google.groups = assertion.attributes [ 'groups' ] 
```


## Set an Organization Administrator

Next you need to specify a new Organization Administrator using an ID from your
configured IdP (for example, your existing user ID). You should also grant this ID
permission to manage Workforce Identity Federation. After you have done this, you no
longer need to use the bootstrap ID to sign into and manage Cloud de Confiance.

To set a new Organization Administrator:

- In the Cloud de Confiance console, navigate back to the main
**IAM & Admin** page:


[Go to IAM & admin](https://console.cloud.s3nscloud.fr/iam-admin)

- Click person_add **Grant access** to add
a new principal.

- 

In the **New principal** field, specify your user ID in the following
format:


```
principal://iam.googleapis.com/locations/global/workforcePools/ POOL_ID /subject/ USERNAME 
```


Replace the following:

- ` POOL_ID `: the unique identifier for your workforce identity
pool.

- ` USERNAME `: your user ID.

Alternatively, if you want to specify a group instead of a single user, use
the following format:


```
principalSet://iam.googleapis.com/locations/global/workforcePools/ POOL_ID /group/ GROUP_EMAIL 
```


- 

In the **Role** drop-down, search for and select **Organization
Administrator**.

- 

Click **Add another role**.

- 

In the **Role** drop-down, search for and select **IAM Workforce Pool
Admin**.

- 

Click **Save**.

You can learn more about the different types of entities and groups in your IdP
that can be represented as IAM principals in [Principal
identifiers](/iam/docs/principal-identifiers).

## Sign in with your administrator ID

Finally, sign out of Cloud de Confiance, then sign
back in using your newly-configured administrator ID from your IdP.

## What's next

- 

Set up the
Google Cloud CLI with your administrator ID: you'll use it to verify the other setup
steps in [Set up your organization](/docs/get-started-tpc/set-up-organization), as well as performing many other common tasks from the
command line. For instructions, see [Set up the Google Cloud CLI for Cloud de Confiance](/docs/get-started-tpc/setup-gcloud).

- 

If you want to explore services and tutorials before doing a full production setup, you can set up a [minimal configuration](/docs/get-started-tpc/set-up-organization/minimal-setup) with a single project.

- 

When you're ready to set up for your users and teams, learn how to [Set up your organization](/docs/get-started-tpc/set-up-organization).