# Create service accounts

Source: https://berlin.devsitetest.how/iam/docs/service-accounts-create
Last updated: 2026-07-21

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

IAM

](https://berlin.devsitetest.how/iam/docs)






- 








[

Guides

](https://berlin.devsitetest.how/iam/docs/overview)












# Create service accounts 






- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Required roles ](#permissions)

- [ Create a service account ](#creating)
- [ What's next ](#whats-next)
- 










This page explains how to create service accounts using the
Identity and Access Management (IAM) API, the Google Cloud Dedicated console, and the `gcloud` command-
line tool.

## Before you begin 

- 




Enable the IAM API.






Roles required to enable APIs**


To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=iam.googleapis.com&redirect=https%3A//console.cloud.google.com)

- 

Set up authentication.













Select the tab for how you plan to use the samples on this page:











[Console](#console) [gcloud](#gcloud) [C#](#c) [C++](#c++) [Go](#go) [Java](#java) [Python](#python) [REST](#rest) 
**More 







When you use the Google Cloud Dedicated console to access Google Cloud Dedicated in Germany services and
APIs, you don't need to set up authentication.

































[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).

After signing in,
[initialize](/sdk/docs/initializing) the Google Cloud CLI by running the following command:





```
gcloud init
```








































To use the .NET samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Google Cloud Dedicated authentication documentation.





















To use the C++ samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Google Cloud Dedicated authentication documentation.






















To use the Go samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Google Cloud Dedicated authentication documentation.





















To use the Java samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Google Cloud Dedicated authentication documentation.



























To use the Python samples on this page in a local development environment, install and
initialize the gcloud CLI, and then set up Application Default Credentials with
your user credentials.















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


























- 




Create local authentication credentials for your user account:




```
gcloud auth application-default login
```






If an authentication error is returned, and you are using an external identity provider
(IdP), confirm that you have
[
signed in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).








For more information, see
[
Set up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment)
in the Google Cloud Dedicated authentication documentation.



























To use the REST API samples on this page in a local development environment, you use the
credentials you provide to the gcloud CLI.












[Install](/sdk/docs/install) the Google Cloud CLI, and then
[
sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).


















For more information, see
[Authenticate for using REST](/docs/authentication/rest)
in the Google Cloud Dedicated authentication documentation.

















- 

Understand [IAM service accounts](/iam/docs/service-account-overview)

### Required roles


































To get the permissions that
you need to create service accounts,

ask your administrator to grant you the
[Create Service Accounts ](/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`) IAM role on the project.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).











If you want to grant newly created service accounts access to your project, you
also need the Project IAM admin (`roles/resourcemanager.projectIamAdmin`) role.

## Create a service account

When you create a service account, you must provide an alphanumeric ID
(` SERVICE_ACCOUNT_NAME ` in the samples below), such as
`my-service-account`. The ID must be between 6 and 30 characters, and can
contain lowercase alphanumeric characters and dashes. After you create a service
account, you cannot change its name.

The service account's name appears in the email address that is provisioned
during creation, in the format
` SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com`.

Each service account also has a permanent, unique numeric ID, which is generated
automatically.

You also provide the following information when you create a service account:

- ` DESCRIPTION ` is an optional description for the
service account.

- ` DISPLAY_NAME ` is a friendly name for the service
account.

- ` PROJECT_ID ` is the ID of your Google Cloud Dedicated in Germany project.

After you create a service account, you might need to wait for
60 seconds or more before you use the service account. This behavior
occurs because read operations are eventually consistent; it can take time for
the new service account to become visible. If you try to read or use a service
account immediately after you create it, and you receive an error, you can
[retry the request with exponential backoff](/iam/docs/retry-strategy).

The number of service accounts that you can have in each project depends on your
project. To view the quota for a project, [view your project's quotas in the
Google Cloud Dedicated console](/docs/quotas/view-manage#viewing_your_quota_console) and search for **Service Account Count**.















[Console](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 










- In the Google Cloud Dedicated console, go to the Create service account** page.









- Select a Google Cloud Dedicated project.

- Enter a service account name to display in the Google Cloud Dedicated console.



The Google Cloud Dedicated console generates a service account ID based on this
name. Edit the ID if necessary. You cannot change the ID later.

- Optional: Enter a description of the service account.

- If you don't want to set access controls now, click **Done** to finish
creating the service account.

To set access controls now, click **Create and continue** and continue to
the next step.

- Optional: Choose one or more [IAM roles](/iam/docs/understanding-roles) to grant to the service account on the project.

- When you are done adding roles, click **Continue**.

- Optional: In the **Service account users role** field, add members that need to [attach the service account to other resources](/iam/docs/attach-service-accounts).

- Optional: In the **Service account admins role** field, add members that need to manage the service account.

- Click **Done** to finish creating the service account.








































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


To create the service account, run the
`[gcloud iam service-accounts create](/sdk/gcloud/reference/iam/service-accounts/create)` command:


```
gcloud iam service-accounts create ** SERVICE_ACCOUNT_NAME \ 
--description = " DESCRIPTION " \ 
--display-name = " DISPLAY_NAME " 
```



Replace the following values:




- 


`SERVICE_ACCOUNT_NAME` : the name of the service account



- 


`DESCRIPTION` : an optional description of the
service account



- 


`DISPLAY_NAME` : a service account name to display in
the Google Cloud Dedicated console






- 


Optional: To grant your service account an
[IAM role](/iam/docs/understanding-roles) on your project, run the
`[gcloud projects add-iam-policy-binding](/sdk/gcloud/reference/projects/add-iam-policy-binding)`
command:


```
gcloud projects add-iam-policy-binding PROJECT_ID \ 
--member = "serviceAccount: SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com" \ 
--role = " ROLE_NAME " 
```



Replace the following values:




- 


`PROJECT_ID` : the project ID



- 


`SERVICE_ACCOUNT_NAME` : the name of the service account



- 


`ROLE_NAME` : a role name, such as
`roles/compute.osLogin`






- 


Optional: To allow users to [attach the service account to
other resources](/iam/docs/attach-service-accounts), run the `[gcloud
iam service-accounts add-iam-policy-binding](/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding)` command to grant a
user the Service Account User role
(`roles/iam.serviceAccountUser`) on the service account:



```
gcloud iam service-accounts add-iam-policy-binding \ 
SERVICE_ACCOUNT_NAME @ PROJECT_ID .eu0.iam.gserviceaccount.com \ 
--member = "user: USER_EMAIL " \ 
--role = "roles/iam.serviceAccountUser" 
```



Replace the following values:




- 

`PROJECT_ID` : the project ID


- 

`SERVICE_ACCOUNT_NAME` : the name of the
service account


- 

`USER_EMAIL` : the email address for the
user

























































To learn how to install and use the client library for IAM, see
[IAM client libraries](/iam/docs/reference/libraries).



For more information, see the
[IAM C++ API
reference documentation](/cpp/docs/reference/iam/latest).





To authenticate to IAM, set up Application Default Credentials.
For more information, see

[Before you begin](#before-you-begin).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
namespace iam = :: google :: cloud :: iam_admin_v1 ; 
[]( std :: string const & project_id , std :: string const & account_id , 
std :: string const & display_name , std :: string const & description ) { 
iam :: IAMClient client ( iam :: MakeIAMConnection ()); 
google :: iam :: admin :: v1 :: ServiceAccount service_account ; 
service_account . set_display_name ( display_name ); 
service_account . set_description ( description ); 
auto response = client . CreateServiceAccount ( "projects/" + project_id , 
account_id , service_account ); 
if ( ! response ) throw std :: move ( response ). status (); 
std :: cout "ServiceAccount successfully created: " 
response - > DebugString () " \n " ; 
} 
```

























































To learn how to install and use the client library for IAM, see
[IAM client libraries](/iam/docs/reference/libraries).



For more information, see the
[IAM C# API
reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1).





To authenticate to IAM, set up Application Default Credentials.
For more information, see

[Before you begin](#before-you-begin).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
using System ; 
using [ Google.Apis.Auth.OAuth2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.Iam.v1 ; 
using Google.Apis.Iam.v1.Data ; 

public partial class ServiceAccounts 
{ 
public static ServiceAccount CreateServiceAccount ( string projectId , 
string name , string displayName ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 
var service = new IamService ( new IamService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

var request = new CreateServiceAccountRequest 
{ 
AccountId = name , 
ServiceAccount = new ServiceAccount 
{ 
DisplayName = displayName 
} 
}; 
var serviceAccount = service . Projects . ServiceAccounts . Create ( 
request , "projects/" + projectId ). Execute (); 
Console . WriteLine ( "Created service account: " + serviceAccount . Email ); 
return serviceAccount ; 
} 
} 
```
























































To learn how to install and use the client library for IAM, see
[IAM client libraries](/iam/docs/reference/libraries).



For more information, see the
[IAM Go API
reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1).





To authenticate to IAM, set up Application Default Credentials.
For more information, see

[Before you begin](#before-you-begin).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import ( 
"context" 
"fmt" 
"io" 

iam "google.golang.org/api/iam/v1" 
) 

// createServiceAccount creates a service account. 
func createServiceAccount ( w io . Writer , projectID , name , displayName string ) ( * iam . ServiceAccount , error ) { 
ctx := context . Background () 
service , err := iam . NewService ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "iam.NewService: %w" , err ) 
} 

request := & iam . CreateServiceAccountRequest { 
AccountId : name , 
ServiceAccount : & iam . ServiceAccount { 
DisplayName : displayName , 
}, 
} 
account , err := service . Projects . ServiceAccounts . Create ( "projects/" + projectID , request ). Do () 
if err != nil { 
return nil , fmt . Errorf ( "Projects.ServiceAccounts.Create: %w" , err ) 
} 
fmt . Fprintf ( w , "Created service account: %v" , account ) 
return account , nil 
} 
```

























































To learn how to install and use the client library for IAM, see
[IAM client libraries](/iam/docs/reference/libraries).



For more information, see the
[IAM Java API
reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1).





To authenticate to IAM, set up Application Default Credentials.
For more information, see

[Before you begin](#before-you-begin).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
import com.google.cloud.iam.admin.v1.[IAMClient](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) ; 
import com.google.iam.admin.v1.[CreateServiceAccountRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountRequest.html) ; 
import com.google.iam.admin.v1.[ProjectName](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ProjectName.html) ; 
import com.google.iam.admin.v1.[ServiceAccount](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html) ; 
import java.io.IOException ; 

public class CreateServiceAccount { 
public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
String projectId = "your-project-id" ; 
String serviceAccountName = "my-service-account-name" ; 

createServiceAccount ( projectId , serviceAccountName ); 
} 

// Creates a service account. 
public static [ ServiceAccount ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html) createServiceAccount ( String projectId , String serviceAccountName ) 
throws IOException { 
[ ServiceAccount ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html) serviceAccount = [ ServiceAccount ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html)
. newBuilder () 
. [ setDisplayName ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.Builder.html#com_google_iam_admin_v1_ServiceAccount_Builder_setDisplayName_java_lang_String_) ( "your-display-name" ) 
. build (); 
[ CreateServiceAccountRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountRequest.html) request = [ CreateServiceAccountRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountRequest.html) . newBuilder () 
. setName ( [ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ProjectName.html) . of ( projectId ). toString ()) 
. [ setAccountId ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountRequest.Builder.html#com_google_iam_admin_v1_CreateServiceAccountRequest_Builder_setAccountId_java_lang_String_) ( serviceAccountName ) 
. setServiceAccount ( serviceAccount ) 
. build (); 
// Initialize client that will be used to send requests. 
// This client only needs to be created once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
serviceAccount = iamClient . createServiceAccount ( request ); 
System . out . println ( "Created service account: " + serviceAccount . [ getEmail ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html#com_google_iam_admin_v1_ServiceAccount_getEmail__) ()); 
} 
return serviceAccount ; 
} 
} 
```

























































To learn how to install and use the client library for IAM, see
[IAM client libraries](/iam/docs/reference/libraries).



For more information, see the
[IAM Python API
reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1).





To authenticate to IAM, set up Application Default Credentials.
For more information, see

[Before you begin](#before-you-begin).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.




























```
from typing import Optional 

from google.cloud import iam_admin_v1 
from google.cloud.iam_admin_v1 import [ types ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html)

def create_service_account ( 
project_id : str , account_id : str , display_name : Optional [ str ] = None 
) - > types . ServiceAccount : 
"""Creates a service account. 

project_id: ID or number of the Google Cloud project you want to use. 
account_id: ID which will be unique identifier of the service account 
display_name (optional): human-readable name, which will be assigned 
to the service account 

return: ServiceAccount 
""" 

iam_admin_client = iam_admin_v1 . [ IAMClient ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html) () 
request = [ types ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html) . [ CreateServiceAccountRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateServiceAccountRequest.html) () 

request . account_id = account_id 
request . name = f "projects/ { project_id } " 

service_account = [ types ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html) . [ ServiceAccount ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount.html) () 
service_account . display_name = display_name 
request . service_account = service_account 

account = iam_admin_client . [ create_service_account ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_create_service_account) ( request = request ) 

print ( f "Created a service account: { account . email } " ) 
return account 
```










































The 
`[serviceAccounts.create](/iam/docs/reference/rest/v1/projects.serviceAccounts/create)`

method creates a service account.
















Before using any of the request data,
make the following replacements:


- ` PROJECT_ID `: Your Google Cloud Dedicated project
ID. Project IDs are alphanumeric strings, like `my-project`.

- ` SA_NAME `: The alphanumeric ID of your
service account. This name must be between 6 and 30 characters, and can contain lowercase
alphanumeric characters and dashes.

- ` SA_DESCRIPTION `: Optional. A description for
the service account.

- ` SA_DISPLAY_NAME `: A human-readable
name for the service account.

HTTP method and URL:



```
POST https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts
```



Request JSON body:



```
{
"accountId": " SA_NAME ",
"serviceAccount": {
"description": " SA_DESCRIPTION ",
"displayName": " SA_DISPLAY_NAME "
}
}
```



To send your request, expand one of these options:


#### curl (Linux, macOS, or Cloud Shell)













Save the request body in a file named `request.json`,
and execute the following command:






































```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
"https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts"
```




#### PowerShell (Windows)













Save the request body in a file named `request.json`,
and execute the following command:
























































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method POST `
-Headers $headers `
-ContentType: "application/json; charset=utf-8" `
-InFile request.json `
-Uri "https://iam.googleapis.com/v1/projects/ PROJECT_ID /serviceAccounts" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/iam/docs/reference/rest/v1/projects.serviceAccounts/create).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.







You should receive a JSON response similar to the following:






```
{
"name": "projects/my-project/serviceAccounts/my-service-account@my-project.eu0.iam.gserviceaccount.com",
"projectId": "my-project",
"uniqueId": "123456789012345678901",
"email": "my-service-account@my-project.eu0.iam.gserviceaccount.com",
"displayName": "My service account",
"etag": "BwUp3rVlzes=",
"description": "A service account for running jobs in my project",
"oauth2ClientId": "987654321098765432109"
}
```























After you create a service account,
[grant one or more roles to the service account](/iam/docs/granting-changing-revoking-access)
so that it can act on your behalf.

Also, if the service account needs to access resources in other projects, you
usually must [enable the APIs](/apis/docs/getting-started#enabling_apis) for those resources in the project
where you created the service account.

## What's next

- Learn how to [list and edit service accounts](/iam/docs/service-accounts-list-edit).

- Review the process for [granting IAM roles to all types of principals](/iam/docs/granting-changing-revoking-access),
including service accounts.

- Understand how to [attach service accounts to resources](/iam/docs/attach-service-accounts).

- Get [best practices for working with service accounts](/iam/docs/best-practices-service-accounts).