# Reauthentication

Source: https://berlin.devsitetest.how/docs/authentication/reauthentication
Last updated: 2026-07-10

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/authentication/tpc-differences) for more details.














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

Google Cloud SDK

](https://berlin.devsitetest.how/sdk/docs)






- 








[

Authentication

](https://berlin.devsitetest.how/docs/authentication)






- 








[

Guides

](https://berlin.devsitetest.how/sdk/docs/overview)












# Reauthentication 






- On this page 
- [ Google Workspace session configuration ](#workspace-session)
- [ Identity-Aware Proxy reauthentication ](#iap)
- [ Refresh token expiration ](#refresh-token)
- [ Sensitive actions ](#sensitive-actions)

- [ When reauthentication is required ](#when_reauthentication_is_required)

- [ Disable reauthentication ](#disable)
- 









This page describes some scenarios when you might need to authenticate again,
even if you previously authenticated successfully.

## Google Workspace session configuration 

If you are accessing Google Cloud Dedicated in Germany by using a Google Workspace user
account, your Google Workspace administrator can configure the maximum
session length, and whether reauthentication is required when the session
expires. The credentials provided by local Application Default Credentials (ADC)
files also expire when the session expires. You must refresh them by running the
[`gcloud auth application-default login` command](/sdk/gcloud/reference/auth/application-default/login)
again.

If you have questions about your Google Workspace session configuration,
contact your Google Workspace administrator. For information about
setting the Google Workspace session length, see
[Set session length for Google Cloud Dedicated services](https://support.google.com/a/answer/9368756).

## Identity-Aware Proxy reauthentication

IAP can be configured to require reauthentication to protected
services and applications after a specific period of time. For more information,
see [IAP reauthentication](/iap/docs/configuring-reauth).

## Refresh token expiration

Refresh tokens can expire due to session length, or for other reasons. When they
expire, you must authenticate again. For more information, see
[Refresh token expiration](https://developers.google.com/identity/protocols/oauth2#expiration)
in the Google Identity documentation.

## Sensitive actions

The following Google Cloud Dedicated actions are considered sensitive actions:

- 

Billing assignment changes

- 

IAM allow policy changes at the organization, folder, or
project level

Users who can perform sensitive actions are known as *privileged users*. To help
protect against bad actors impersonating privileged users through cookie theft,
Google Cloud Dedicated requires reauthentication before sensitive actions can be
performed.

Reauthentication for sensitive actions is in the process of rolling out across
Google Cloud Dedicated in Germany accounts. The rollout is expected to be complete in 2026.

### When reauthentication is required

When you initiate a sensitive action, you are required to reenter your password
or complete multi-factor authentication (MFA) if all of the following conditions
are met:

- The action is initiated in the Google Cloud Dedicated console.

- You have not reauthenticated in the last 15 minutes.

- Your user account is managed by Google.

User accounts managed by an external identity provider (IdP) and federated by
using Workforce Identity Federation are not required to reauthenticate.

## Disable reauthentication

Reauthenticating for sensitive actions is enabled by default. To apply for an
exception, [contact support](https://console.cloud.berlin-build0.goog/support) with your reason for the
exception.