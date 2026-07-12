# 2-step verification requirement for Google Cloud Dedicated in Germany

Source: https://berlin.devsitetest.how/docs/authentication/mfa-requirement
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












# 2-step verification requirement for Google Cloud Dedicated in Germany 






- On this page 
- [ Timelines for 2SV enforcement ](#timelines)
- [ Scope of 2SV enforcement ](#scope)
- [ Enable 2SV for Google Accounts ](#enable-google)

- [ Additional factors for Google Accounts ](#additional-factors)

- [ Enable 2SV in Google Workspace ](#enable-workspace)
- [ Enable 2SV for third-party identity providers ](#enable-idp)
- [ Recover account access if a factor is lost or stolen ](#recover)
- 









Google Cloud Dedicated in Germany strives to provide its customers with the strongest security
possible. We prioritize protecting your identity, to help keep your account and
sensitive information safe. To help keep this commitment, Google is phasing in
the requirement that all Google Cloud Dedicated customers enable 2-step verification
(2SV) for their accounts.

Also known as *multifactor authentication* (MFA), 2SV is an important security
measure. In addition to your password, 2SV requires another proof of identity,
known as an *authentication factor*, to successfully sign in to an account.
Requiring an additional factor makes it much harder for your account to be
compromised by hackers. Even if your password is stolen, hackers still need an
additional factor to be able to access your account.

If you're using a Google Account and have already [enabled 2SV](#enable-google),
you don't need to take further action. You can check whether 2SV is enabled for
your account by opening the **Security** tab of your
[Google Account settings page](https://myaccount.google.com/security). The
**2-Step Verification** setting is displayed in the
**How you sign in to Google** section.

If you're using a third-party identity provider (IdP) to manage single sign-on
(SSO) in to Google Cloud Dedicated, you can use the 2SV provided by that IdP to
comply with Google Cloud Dedicated's 2SV requirement.

If you have questions that aren't answered in this document, contact
[Cloud Customer Care](https://berlin.devsitetest.how/support-hub).

## Timelines for 2SV enforcement

The timeline for 2SV enforcement for Google Cloud Dedicated depends on your account
type, as shown in the following table.



| 
Account type | 
Description | 
Enforcement start date | 
|

| 
Personal Google Accounts | 

User accounts you created for your own use, including Gmail
accounts, that are used as
[principals](/iam/docs/principals-overview) in Google Cloud Dedicated in Germany.
| 
On or after May 12, 2025 | 
|

| 
Enterprise Cloud Identity accounts (not using SSO) | 

User accounts with usernames and passwords created and managed by your
Google Workspace administrator in Cloud Identity.
| 
On or after September 15, 2026 | 
|

| 
Enterprise accounts using federated authentication | 

User accounts created and managed by your Google Workspace
administrator that use Google Workspace SSO,
[Cloud Identity](/identity/docs/overview) SSO, or
[
Workforce Identity Federation](/iam/docs/workforce-identity-federation).
| 
To be announced | 
|

| 
Reseller accounts | 

User accounts created and managed in a Google Cloud Dedicated in Germany reseller domain. End
users of the reseller are not affected.
| 
On or after April 28, 2025 | 
|


If you don't have 2SV enabled, an email reminder is sent at least 90 days before
2SV enforcement. The Google Cloud Dedicated console also begins displaying reminders 90
days before 2SV is enforced.

For resellers and their users, the Google Cloud Dedicated console displays reminders to
enable 2SV at least 60 days before, and leading up to 2SV enforcement.
Similarly, an email reminder is sent at least 60 days before 2SV enforcement.

When the requirement is enforced for your account, you must have 2SV enabled to
sign in to the Google Cloud Dedicated console or the Firebase console.

## Scope of 2SV enforcement

When the Google Cloud Dedicated 2SV requirement is enforced for your account, if you
don't have 2SV enabled, you won't be able to use the following Google Cloud Dedicated in Germany
interfaces:

- 

The [Google Cloud Dedicated console](/cloud-console)

- 

The [Firebase console](https://console.firebase.google.com/)

Google Cloud Dedicated 2SV enforcement doesn't directly affect service accounts.
However, Google Accounts [impersonating service accounts](/docs/authentication/use-service-account-impersonation),
*are* affected. If 2SV is enforced on your Google Account, you must enable 2SV
to successfully complete the impersonation flow.

Access to the following interfaces and services is **not** affected by the
Google Cloud Dedicated 2SV enforcement:

- 

Google Workspace, including Gmail, Google Drive, Google Sheets,
and Google Slides. However, Google Workspace has a separate 2SV
requirement. Contact
[your Google Workspace administrator](https://support.google.com/a/answer/6208960)
for more information.

- 

YouTube.

Your applications and workloads running on Google Cloud Dedicated, including
applications secured by Identity-Aware Proxy (IAP), aren't affected by 2SV
enforcement. However, your developers won't be able to use the
Google Cloud Dedicated console to manage those applications. In other words, your
control plane is affected by 2SV enforcement, but not your data plane.

## Enable 2SV for Google Accounts

You can enable 2SV on the **Security** tab of your
[Google Account settings page](https://myaccount.google.com/security). For
step-by-step instructions, see
[Turn on 2-Step Verification](https://support.google.com/accounts/answer/185839?sjid=8549799716107395240-NC).

If you don't see the **2-Step Verification** option for your account, your
administrator might have disabled it. Contact
[your administrator](https://support.google.com/a/answer/6208960) for
assistance.

### Additional factors for Google Accounts

Personal Google Accounts and enterprise accounts that use Google as their
identity provider (IdP) can use any of the following additional factors with
Google Cloud Dedicated:

- 

**Authenticator apps**: you can set up an authenticator application, such as
[Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2),
or [Authy](https://www.authy.com/), on your mobile or desktop device to act as
your second factor.

- 

**Backup codes**: you can create backup codes and use them as your second
factor. Backup codes must be stored securely, and can be used only once, so
this method should be used only when you have no other method available. For
more information, see
[Sign in with backup codes](https://support.google.com/accounts/answer/1187538).

- 

**Google Prompts**: if you are signed into your Google Account on another
device, you can receive a prompt on that device asking you whether it is you
signing in. You can confirm that it's you in a browser, on a tablet, or your
phone. For more information, see
[Sign in with Google prompts](https://support.google.com/accounts/answer/7026266).

- 

**Physical security key**: you can touch a physical security key to provide
your second factor. For more information, see
[Use a security key for 2-Step Verification](https://support.google.com/accounts/answer/6103523).

- 

**SMS codes**: you can use a code sent to your phone number as a second
factor. Before you can use SMS as a second factor, your phone number must be
associated with your Google Account.

## Enable 2SV in Google Workspace

Google Workspace administrators can
[deploy 2-step verification](https://knowledge.workspace.google.com/admin/security/deploy-2-step-verification)
for their users, which is recognized by Google Cloud Dedicated in Germany.

## Enable 2SV for third-party identity providers

Refer to your third-party IdP's documentation to learn how to enable 2SV.

## Recover account access if a factor is lost or stolen

See [Fix common issues with 2-Step verification](https://support.google.com/accounts/answer/185834)
for steps to recover your account.