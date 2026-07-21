# Set up ADC for a local development environment

Source: https://berlin.devsitetest.how/docs/authentication/set-up-adc-local-dev-environment
Last updated: 2026-07-21

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












# Set up ADC for a local development environment 






- On this page 
- [ User credentials ](#local-user-cred)

- [ Tips for configuring ADC with your user credentials ](#tips_for_configuring_adc_with_your_user_credentials)

- [ Service account credentials ](#service-account)

- [ Service account impersonation ](#sa-impersonation)
- [ Service account keys ](#local-key)

- [ What's next ](#whats_next)
- 










You can provide either [your user credentials](#local-user-cred) or
[service account credentials](#service-account) to ADC in a local development
environment.

## User credentials 

When your code is running in a local development environment, such as a
development workstation, the best option is to use the credentials associated
with your [user account](/docs/authentication#user-accounts).

To configure ADC for a user account managed by an external IdP and federated
with [Workforce Identity Federation](/iam/docs/workforce-identity-federation):











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













### Tips for configuring ADC with your user credentials

When you configure ADC with your user account, you should be aware of the
following facts:

- 

ADC configured with a user account might not work for some APIs without extra
configuration steps. If you see an error message about the API not being
enabled in the project, or that there is no quota project available, see
[User credentials not working](/docs/authentication/troubleshoot-adc#user-creds-client-based).

- 

The local ADC file contains your refresh token. Any user with access to your
file system can use it to get a valid access token. If you no longer need
these local credentials, you can revoke them by using the
[`gcloud auth application-default revoke` command](/sdk/gcloud/reference/auth/application-default/revoke).

- 

Your local ADC file is associated with your user account, not your
gcloud CLI configuration. Changing to a different
gcloud CLI configuration might change the identity used by the
gcloud CLI, but it does not affect your local ADC file or the ADC
configuration.

## Service account credentials

You can configure ADC with credentials from a
[service account](/docs/authentication#service-accounts) by using service account impersonation or by
using a service account key.

### Service account impersonation

You can use service account impersonation to set up a local Application Default Credentials (ADC) file. Client
libraries that support impersonation can use those credentials automatically. Local ADC files
created by using impersonation are supported in the following languages:


- C#

- C++

- Go

- Java

- Node.js

- PHP

- Python

- Ruby

- Rust



You must have the Service Account Token Creator
(`roles/iam.serviceAccountTokenCreator`) IAM role on the service account you are
impersonating. For more information, see
[Required roles](/docs/authentication/use-service-account-impersonation#required-roles).


Use service account impersonation to create a local ADC file:


```
gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL 
```


You can now use client libraries using the supported languages the same way you would after
setting up a local ADC file with user credentials. Credentials are automatically found by the
authentication libraries. For more information, see
[Authenticate for using client libraries](/docs/authentication/client-libraries).

Credentials from a local ADC file generated by using service account impersonation are not
supported by all of the authentication libraries. For more information, see
[
Error returned for local credentials from service account impersonation](/docs/authentication/troubleshoot-adc#local-impersonated).

### Service account keys

If you cannot use a user account or service account impersonation for local
development, you can use a service account key.

To create a service account key and make it available to ADC:


- 
Create a service account with the roles your application needs, and a key
for that service account, by following the instructions in
[Creating a service account key](/iam/docs/keys-create-delete#creating).


- 






Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS`
to the path of the JSON file that contains your credentials.
This variable applies only to your current shell session, so if you open
a new session, set the variable again.




**Example:** Linux or macOS



```
export GOOGLE_APPLICATION_CREDENTIALS = "` KEY_PATH `" 
```



Replace ` KEY_PATH ` with the path of the JSON file that contains your credentials.



For example:


```
export GOOGLE_APPLICATION_CREDENTIALS = "/home/user/Downloads/service-account-file.json" 
```





**Example:** Windows




For PowerShell:


```
$env :GOOGLE_APPLICATION_CREDENTIALS = "` KEY_PATH `" 
```



Replace ` KEY_PATH ` with the path of the JSON file that contains your credentials.



For example:


```
$env :GOOGLE_APPLICATION_CREDENTIALS = "C:\Users\username\Downloads\service-account-file.json" 
```




For command prompt:


```
set GOOGLE_APPLICATION_CREDENTIALS = ` KEY_PATH `
```



Replace ` KEY_PATH ` with the path of the JSON file that contains your credentials.






## What's next

- 

Understand best practices for using [service account keys](/iam/docs/best-practices-for-managing-service-account-keys).

- 

Learn more about [how ADC finds credentials](/docs/authentication/application-default-credentials).

- 

[Authenticate for using Cloud Client Libraries](/docs/authentication/client-libraries).

- 

[Authenticate for using REST](/docs/authentication/rest).

- 

Explore [authentication methods](/docs/authentication).