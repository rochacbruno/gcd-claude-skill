# Set up ADC for on-premises or another cloud provider

Source: https://berlin.devsitetest.how/docs/authentication/set-up-adc-on-premises
Last updated: 2026-06-29

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












# Set up ADC for on-premises or another cloud provider 






- On this page 
- [ Workload Identity Federation ](#wlif)
- [ Service account key ](#wlif-key)
- [ What's next ](#whats_next)
- 









If you are running your application outside of Google Cloud Dedicated, you need to
provide credentials that are recognized by Google Cloud Dedicated to
use Google Cloud Dedicated services.

### Workload Identity Federation 

The preferred way to authenticate with Google Cloud Dedicated using credentials from
an external IdP is to use [Workload Identity Federation](/iam/docs/workload-identity-federation);
you create a credential configuration file and set the
`GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to it. This
approach is more secure than creating a service account key.

For help with setting up Workload Identity Federation for ADC, see
[Workload Identity Federation with other clouds](/iam/docs/workload-identity-federation-with-other-clouds).

### Service account key

If you are not able to configure Workload Identity Federation, then you must
create a service account, grant it the IAM roles that
your application requires, and create a key for the service account.

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

- Learn about [Workload Identity Federation](/iam/docs/workload-identity-federation).

- Understand best practices for using [service account keys](/iam/docs/best-practices-for-managing-service-account-keys).

- Learn more about [how ADC finds credentials](/docs/authentication/application-default-credentials).

- Explore [authentication methods](/docs/authentication).