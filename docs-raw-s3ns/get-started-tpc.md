# Get started with Cloud de Confiance

Source: https://documentation.s3ns.fr/docs/get-started-tpc
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












# Get started with Cloud de Confiance 






- On this page 
- [ Set up a new organization ](#set_up_a_new_organization)
- [ Set up tools and workflows ](#set_up_tools_and_workflows)
- 









Before you or your organization's users can start working with
Cloud de Confiance, you must complete some key
setup tasks.

The tasks you need to perform depend on whether you're setting up a whole new
organization, or if you need to start working with an existing organization.
These tasks include:

- 

Tasks that are typically completed by *platform admins and IT
administrators* to get your organization ready for
Cloud de Confiance.

These are tasks that are only completed once for the whole organization.

- 

Tasks that are typically completed by *app operators*, *platform admins*,
and other *technical practitioners* to configure tools and workflows for use
with
Cloud de Confiance.

These are tasks that are completed as-needed for users to access and use
Cloud de Confiance.

## Set up a new organization 

One-time core tasks that are typically completed platform admins or IT
administrators before others can access and use
Cloud de Confiance include:

- 

[Set up an identity provider](/docs/get-started-tpc/set-up-identity-provider)

You must configure an identity provider (IdP) so that members of your
organization can sign in to Cloud de Confiance,
and be authorized to use services and resources with Identity and Access Management. You use
your own identity provider using Workforce Identity Federation, which lets you
continue to use existing user IDs and groups if required.

- 

[Set up your organization](/docs/get-started-tpc/set-up-organization)

When you first onboard to Cloud de Confiance,
you are provided with a new empty organization. You must configure this
organization with projects, a network, and other resources before users can
start to deploy and run applications. We also recommend that you configure the
Google Cloud CLI as part of setting up your organization.

## Set up tools and workflows

After an organization has been set up, the following tasks are typically
performed by developers, app operators, and other technical practitioners who
need to interact with Cloud de Confiance:

- 

[Set up API access](/docs/get-started/access-apis)

Cloud de Confiance APIs help you
programmatically access services from the command line, through automated
scripts, or in your own applications.

- 

[Set up the Google Cloud CLI](/docs/get-started-tpc/setup-gcloud)

The gcloud CLI is
Cloud de Confiance's command line tool for
interacting with services and resources. Using the gcloud CLI with
Cloud de Confiance requires some one-time
configuration to work with Cloud de Confiance
services and your organization's identity provider.

- 

[Use client libraries](/docs/get-started-tpc/use-client-libraries)

Cloud de Confiance provides client libraries for
interacting with services programmatically. As with the gcloud CLI,
you must specify your target universe when using client libraries. If you're
already familiar with using client libraries in Google Cloud,
this guide also explains some key differences when using these libraries in
Cloud de Confiance.