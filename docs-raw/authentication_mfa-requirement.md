# 2-step verification requirement for Google Cloud Dedicated in Germany

Source: https://berlin.devsitetest.how/docs/authentication/mfa-requirement
Last updated: 2026-07-22

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

Developer tools

](https://berlin.devsitetest.how/docs/costs-usage)






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
- [ Interfaces that require 2SV ](#scope)
- [ Timelines for 2SV requirement ](#timelines)
- [ Enable 2SV for Google Accounts ](#enable-google)

- [ Additional factors for Google Accounts ](#additional-factors)

- [ Enable 2SV in Google Workspace ](#enable-workspace)
- [ Enable 2SV for third-party identity providers ](#enable-idp)
- [ Recover account access if a factor is lost or stolen ](#recover)
- [ Monitor 2SV conformance ](#monitor_2sv_conformance)

- [ Understand conformance log entries ](#understand-conformance-log)

- [ Cloud Identity: extend the deadline for the 2SV requirement ](#extend)
- [ Cloud Identity: opt out of the 2SV requirement ](#opt-out)

- [ Opt back in to 2SV ](#opt-in)

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
(SSO) into Google Cloud Dedicated, you can use the 2SV provided by that IdP to
comply with Google Cloud Dedicated's 2SV requirement.

If you have questions that aren't answered in this document, contact
[Cloud Customer Care](https://berlin.devsitetest.how/support-hub).

## Interfaces that require 2SV

When 2SV is required for specific account types in your organization, those
accounts must have 2SV enabled to access the following Google Cloud Dedicated in Germany interfaces:

- 

The [Google Cloud Dedicated console](/cloud-console)

- 

The [Firebase console](https://console.firebase.google.com/)

User accounts that don't have 2SV enabled are prompted to set it up before they
can proceed to these interfaces.

Access to the following interfaces and services is **not** affected by the
Google Cloud Dedicated 2SV requirement:

- 

Google Workspace, including Gmail, Google Drive, Google Sheets,
and Google Slides. However, Google Workspace has a separate 2SV
requirement. Contact
[your Google Workspace administrator](https://support.google.com/a/answer/6208960)
for more information.

- 

YouTube.

Your applications and workloads running on Google Cloud Dedicated, including
applications secured by Identity-Aware Proxy (IAP), aren't affected by the 2SV
requirement. However, your developers won't be able to use the
Google Cloud Dedicated console to manage those applications. In other words, your
control plane is affected by the 2SV requirement, but not your data plane.

Other Google Cloud Dedicated in Germany interfaces like the gcloud CLI don't have a 2SV
requirement. However, after a user account enables 2SV, 2SV becomes part of the
account's regular sign-in flow. For example, if you enable 2SV for your account
and then
[authenticate for the gcloud CLI](/sdk/docs/authenticate#user-accounts),
you are prompted for your second factor as part of the sign-in process.

## Timelines for 2SV requirement

When you need to enable 2SV for your user account in Google Cloud Dedicated in Germany depends on
your account type, as shown in the following table.



| 
Account type | 
Description | 
Requirement start date | 
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
On or after October 20, 2026 | 
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
the 2SV requirement starts. The Google Cloud Dedicated console also begins displaying
reminders 90 days before the 2SV requirement starts.

For resellers and their users, the Google Cloud Dedicated console displays reminders to
enable 2SV at least 60 days before, and leading up to the 2SV requirement.
Similarly, an email reminder is sent at least 60 days before the 2SV requirement
starts.

User accounts added after the 2SV requirement is enabled for an organization
don't receive reminders, and are prompted to enable 2SV to access the
Google Cloud Dedicated console or the Firebase console.

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

## Monitor 2SV conformance

Administrators can monitor user account 2SV conformance when they interact with
the Google Cloud Dedicated console in Logs Explorer:

- 

In the Google Cloud Dedicated console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.berlin-build0.goog/projectselector2/logs/query?supportedpurview=organizationId)

- 

Select your organization.

- 

Pick a time range for the logs you want to query.

- 

Add the following query:


```
jsonPayload.@type="type.googleapis.com/google.identity.mfaforall.LogEntry"
```


- 

Click **Run query**.

You can filter the log results using the **Fields** pane. Alternatively, you
can expand your query to require other fields, such as in the following example:


```
jsonPayload.@type="type.googleapis.com/google.identity.mfaforall.LogEntry"
jsonPayload.enforcementState="ENFORCEMENT_STATE_UPCOMING_ENFORCEMENT"
jsonPayload.userEmail: " PRINCIPAL_IDENTIFIER "
jsonPayload.mfaEligibility: "MFA_ELIGIBILITY_ELIGIBLE"
```


For the fields you can filter by and their definitions, see
[Understand conformance log entries](#understand-conformance-log).

### Understand conformance log entries

Conformance log entries look similar to the following:


```
{ 
i nsert Id : "00000000" 
jso n Payload : { 
@ t ype : "type.googleapis.com/google.identity.mfaforall.LogEntry" 
e nf orceme nt S tate : "ENFORCEMENT_STATE_UPCOMING_ENFORCEMENT" 
m fa Eligibili t y : "MFA_ELIGIBILITY_ELIGIBLE" 
userEmail : " PRINCIPAL_IDENTIFIER " 
} 
logName : "organizations/ ORGANIZATION_ID /logs/mfaforall.googleapis.com%2Fmfa_conformance_check" 
receiveTimes ta mp : "2026-06-02T21:52:21.150677295Z" 
resource : { 
labels : { 
loca t io n : "global" 
resource_co nta i ner : "organizations/ ORGANIZATION_ID " 
} 
t ype : "mfaforall.googleapis.com/Location" 
} 
severi t y : "INFO" 
t imes ta mp : "2026-06-02T21:52:20.838Z" 
} 
```


The following fields can help you to monitor 2SV conformance for user accounts:

- 

`userEmail`: This key's value is the principal identifier for the monitored
user account, which is an email address.

- 

`mfaEligibility`: This key's value is one of following:

- 

`MFA_ELIGIBILITY_ELIGIBLE`: The user account is eligible for the 2SV
requirement.

- 

`MFA_ELIGIBILITY_INELIGIBLE`: The user account is blocked from enrolling in
2SV due to their organization's policy settings in Google Workspace.

- 

`MFA_ELIGIBILITY_UNSPECIFIED`: The user account's eligibility for the 2SV
requirement is unknown. This value is returned when the user is
authenticated through a third-party IdP using single sign-on.

- 

`enforcementState`: This key's value is one of the following:

- 

`ENFORCEMENT_STATE_UPCOMING_ENFORCEMENT`: The user account is in the
[reminder window](#timelines) for the 2SV requirement.

- 

`ENFORCEMENT_STATE_ENFORCED`: 2SV is required for this user account. Users
attempting to access the Google Cloud Dedicated console or the
Firebase console are prompted to enable 2SV to continue.

- 

`ENFORCEMENT_STATE_MFA_COMPLIANT`: The user is compliant with the 2SV
requirement.

- 

`ENFORCEMENT_STATE_NO_ENFORCEMENT_ORG_OPTED_OUT`: The organization is opted
out of the 2SV requirement. The user account doesn't require 2SV.

- 

`ENFORCEMENT_STATE_NO_ENFORCEMENT_SSO_USER`: The user authenticated through
a third-party IdP using single sign-on, and 2SV must be managed there.

## Cloud Identity: extend the deadline for the 2SV requirement

Organizations that use Enterprise [Cloud Identity](/identity) (non-SSO) and
were created before the 2SV requirement can enable a one-time, 90-day extension
to the 2SV requirement at the organization level in the Google Cloud Dedicated console.

To do so, principals with the
[Organization Administrator](/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin)
(`roles/resourcemanager.organizationAdmin`) role must complete the following
steps:

- 

In the Google Cloud Dedicated console, go to the **Organizations** page.

[Go to Organizations](https://console.cloud.berlin-build0.goog/projectselector2/organizations/details?supportedpurview=organizationId)

- 

Select your organization.

- 

In the 2SV notification, click **Extend by 90 days**, and then confirm the
extension. It might take a few minutes for the change to take effect.

After the extension expires, the 2SV requirement is reenabled.

## Cloud Identity: opt out of the 2SV requirement

We don't recommend opting out of the 2SV requirement. However, organizations
that use Enterprise [Cloud Identity](/identity) (non-SSO) can choose to opt
out of the requirement at the organization level in the Google Cloud Dedicated console.
Opting out only bypasses the 2SV requirement; it doesn't disable 2SV for users
who already have it enabled, and users can still enable 2SV for themselves.

Principals with the
[Organization Administrator](/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin)
(`roles/resourcemanager.organizationAdmin`) role at the organization level can
opt out of the 2SV requirement by completing the following steps:

- 

In the Google Cloud Dedicated console, go to the **Organizations** page.

[Go to Organizations](https://console.cloud.berlin-build0.goog/projectselector2/organizations/details?supportedpurview=organizationId)

- 

Select your organization.

- 

Disable **Enforce 2SV**. It might take a few minutes for the settings change
to take effect.

After an organization has opted out of the 2SV requirement, users with 2SV
disabled are no longer required to enable it to use the Google Cloud Dedicated console
or the Firebase console.

### Opt back in to 2SV

If you choose to opt in to 2SV again, a minimum 30-day grace period takes place
before 2SV is required.