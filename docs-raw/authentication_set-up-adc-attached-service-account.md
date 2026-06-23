# Set up ADC for a resource with an attached service account

Source: https://berlin.devsitetest.how/docs/authentication/set-up-adc-attached-service-account
Last updated: 2026-06-22

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












# Set up ADC for a resource with an attached service account 






- On this page 
- [ What's next ](#whats_next)
- 









Some Google Cloud Dedicated services—such as Compute Engine, App Engine, and
Cloud Run functions—support attaching a
[user-managed service account](/iam/docs/service-account-types#user-created) to some types of resources.
Generally, attaching a service account is supported when that service's
resources can run or include application code. When you attach a service account
to a resource, the code running on the resource can use that service account as
its identity.

Attaching a user-managed service account is the preferred way to provide
credentials to ADC for production code running on Google Cloud Dedicated.

For help determining the roles that you need to provide to
your service account, see [Choose predefined roles](/iam/docs/choose-predefined-roles).

For information about which resources you can attach a service account to, and
help with attaching the service account to the resource, see the
[IAM documentation on attaching a service account](/iam/docs/attach-service-accounts#attaching-new-resource).











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










## What's next

- Understand best practices for using [service accounts](/iam/docs/best-practices-service-accounts) and [service account keys](/iam/docs/best-practices-for-managing-service-account-keys).

- Learn more about [how ADC finds credentials](/docs/authentication/application-default-credentials).

- [Authenticate for using Cloud Client Libraries](/docs/authentication/client-libraries).

- Explore [authentication methods](/docs/authentication).