# Manage access to projects, folders, and organizations

Source: https://berlin.devsitetest.how/iam/docs/granting-changing-revoking-access
Last updated: 2026-06-29

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












# Manage access to projects, folders, and organizations 






- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Required roles ](#required-permissions)

- [ View current access ](#view-access)
- [ Grant or revoke a single IAM role ](#single-role)

- [ Grant a single IAM role ](#grant-single-role)
- [ Revoke a single IAM role ](#revoke-single-role)

- [ Grant or revoke multiple IAM roles using the Google Cloud Dedicated console ](#multiple-roles-console)
- [ Grant or revoke multiple IAM roles programmatically ](#multiple-roles-programmatic)

- [ Get the current allow policy ](#getting-policy)
- [ Modify the allow policy ](#modifying-policy)
- [ Set the allow policy ](#setting-policy)

- [ What's next ](#whats_next)
- 










This page describes how to grant, change, and revoke access to projects,
folders, and organizations. When you grant access to projects, folders, and
organizations, you also grant access to the resources inside them.

To learn how to manage access to other resources, see the following guides:

- [Manage access to service accounts](/iam/docs/manage-access-service-accounts)

- [Manage access to other resources](/iam/docs/manage-access-other-resources)

In Identity and Access Management (IAM), access is granted through *allow policies*, also
known as IAM policies. An allow policy is attached to a
Google Cloud Dedicated in Germany resource. Each allow policy contains a collection of *role
bindings* that associate one or more principals, such as users or service
accounts, with an IAM role. These role bindings grant the
specified roles to the principals, both on the resource that the allow policy is
attached to and on all of that resource's [descendants](/resource-manager/docs/cloud-platform-resource-hierarchy). For
more information about allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).

You can manage access to projects, folders, and organizations with the
Google Cloud Dedicated console, the Google Cloud CLI, the REST API, or the [Resource Manager
client libraries](/resource-manager/docs/libraries).

## Before you begin

- 

Ensure that you have the IAM roles required to manage access.

When you create a project, folder, or organization, you are automatically
granted a role that lets you manage access for that resource. For more
information, see [Default policies](/iam/docs/allow-policies#default).

If you didn't create your project, folder, or organization, then ask your
administrator to grant you the [required roles](#required-permissions).

- 

Set up authentication.













Select the tab for how you plan to use the samples on this page:











[Console](#console) [gcloud](#gcloud) [C#](#c) [Java](#java) [Python](#python) [REST](#rest) 
More 







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

















### Required roles

















































































































































































































To get the permissions that
you need to manage access to a project, folder, or organization,

ask your administrator to grant you the
following IAM roles on the resource that you want to manage access for (project,
folder, or organization):












- 
To manage access to a project:
[Project IAM Admin ](/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)





- 
To manage access to a folder:
[Folder Admin ](/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`)





- 
To manage access to projects, folders, and organizations:
[Organization Admin ](/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)





- 
To manage access to almost all Google Cloud Dedicated resources:
[Security Admin ](/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)

















These predefined roles contain

the permissions required to manage access to a project, folder, or organization. To see the exact permissions that are
required, expand the **Required permissions** section:





#### Required permissions




The following permissions are required to manage access to a project, folder, or organization:





- 
To manage access to projects:




- 
`resourcemanager.projects.getIamPolicy`


- 
`resourcemanager.projects.setIamPolicy`







- 
To manage access to folders:




- 
`resourcemanager.folders.getIamPolicy`


- 
`resourcemanager.folders.setIamPolicy`







- 
To manage access to organizations:




- 
`resourcemanager.organizations.getIamPolicy`


- 
`resourcemanager.organizations.setIamPolicy`




















You might also be able to get these permissions with [custom
roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles).



## View current access

You can view who has access to your project, folder, or organization using
the Google Cloud Dedicated console, the gcloud CLI, the REST API, or the
Resource Manager client libraries.















[Console](#console) [ gcloud ](#gcloud) [ C# ](#c) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 










- 

In the Google Cloud Dedicated console, go to the **IAM** page.

[Go
to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

- 

Select a project, folder, or organization.

The Google Cloud Dedicated console lists all the principals who have been granted
roles on your project, folder, or organization. This list includes
principals who have inherited roles on the resource from parent resources.
For more information about policy inheritance, see [Policy inheritance and
the resource hierarchy](/iam/docs/allow-policies#inheritance).

- 

Optional: To view role grants for [service agents](/iam/docs/service-account-types#service-agents), select
the **Include -provided role grants** checkbox.








































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


To see who has access to your project, folder, or organization, get the allow
policy for the resource. To learn how to interpret allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).





To get the allow policy for the resource, run the `get-iam-policy` command for
the resource:


```
gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format = FORMAT > PATH 
```



Provide the following values:




- 


` RESOURCE_TYPE `: The type of the resource that you want to
view access to. Use one of these values:
`projects`, `resource-manager folders`, or
`organizations`.



- 


` RESOURCE_ID `: Your Google Cloud Dedicated project, folder,
or organization ID. Project IDs are alphanumeric, like
`my-project`. Folder and organization IDs are numeric, like
`123456789012`.



- 


` FORMAT `: The desired format for the policy. Use `json`
or `yaml`.



- 


` PATH `: The path to a new output file for the policy.






For example, the following command gets the policy for the project `my-project`
and saves it to your home directory in JSON format:


```
gcloud projects get-iam-policy my-project --format = json > ~/policy.json
```


















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).

To see who has access to your project, folder, or organization, get the allow
policy for the resource. To learn how to interpret allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).

The following example shows how to get the allow policy for a project. To
learn how to get the allow policy for a folder or organization, review the
[Resource Manager client library
documentation](/resource-manager/docs/libraries) for your programming language.



























```
using [ Google.Apis.Auth.OAuth2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.CloudResourceManager.v1 ; 
using Google.Apis.CloudResourceManager.v1.Data ; 

public partial class AccessManager 
{ 
public static Policy GetPolicy ( string projectId ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( CloudResourceManagerService . Scope . CloudPlatform ); 
var service = new CloudResourceManagerService ( 
new CloudResourceManagerService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

var policy = service . Projects . GetIamPolicy ( new GetIamPolicyRequest (), 
projectId ). Execute (); 
return policy ; 
} 
} 
```



















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).

To see who has access to your project, folder, or organization, get the allow
policy for the resource. To learn how to interpret allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).

The following example shows how to get the allow policy for a project. To
learn how to get the allow policy for a folder or organization, review the
[Resource Manager client library
documentation](/resource-manager/docs/libraries) for your programming language.



























```
import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) ; 
import com.google.iam.admin.v1.[ProjectName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) ; 
import com.google.iam.v1.[GetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import java.io.IOException ; 

public class GetProjectPolicy { 
public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
// TODO: Replace with your project ID. 
String projectId = "your-project-id" ; 

getProjectPolicy ( projectId ); 
} 

// Gets a project's policy. 
public static [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getProjectPolicy ( String projectId ) throws IOException { 
// Initialize client that will be used to send requests. 
// This client only needs to be created once, and can be reused for multiple requests. 
try ( [ ProjectsClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ ProjectsClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) . create ()) { 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) . newBuilder () 
. setResource ( [ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) . of ( projectId ). toString ()) 
. build (); 
return projectsClient . getIamPolicy ( request ); 
} 
} 
} 
```



















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).

To see who has access to your project, folder, or organization, get the allow
policy for the resource. To learn how to interpret allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).

The following example shows how to get the allow policy for a project. To
learn how to get the allow policy for a folder or organization, review the
[Resource Manager client library
documentation](/resource-manager/docs/libraries) for your programming language.



























```
from google.cloud import resourcemanager_v3 
from google.iam.v1 import iam_policy_pb2 , policy_pb2 

def get_project_policy ( project_id : str ) - > policy_pb2 . Policy : 
"""Get policy for project. 

project_id: ID or number of the Google Cloud project you want to use. 
""" 

client = resourcemanager_v3 . ProjectsClient () 
request = iam_policy_pb2 . GetIamPolicyRequest () 
request . resource = f "projects/ { project_id } " 

policy = client . get_iam_policy ( request ) 
print ( f "Policy retrieved: { policy } " ) 

return policy 
```










































To see who has access to your project, folder, or organization, get the allow
policy for the resource. To learn how to interpret allow policies, see
[Understanding allow policies](/iam/docs/allow-policies).

The Resource Manager API's
`[get-iam-policy](/resource-manager/reference/rest/v1/projects/getIamPolicy)`

method gets a project's, folder's, or organization's allow policy.












Before using any of the request data,
make the following replacements:


- ` API_VERSION `: The API version to use. For
projects and organizations, use `v1`. For folders, use `v2`.

- ` RESOURCE_TYPE `: The resource type whose
policy you want to manage. Use the value `projects`, `folders`, or
`organizations`.

- ` RESOURCE_ID `: Your Google Cloud Dedicated
project, organization, or folder ID. Project IDs are alphanumeric strings, like
`my-project`. Folder and organization IDs are numeric, like `123456789012`.


- ` POLICY_VERSION `: The policy version to be
returned. Requests should specify the most recent policy version, which is policy version
3. See [Specifying
a policy version when getting a policy](/iam/docs/allow-policies#specifying-version-get) for details.

HTTP method and URL:



```
POST https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :getIamPolicy
```



Request JSON body:



```
{
"options": {
"requestedPolicyVersion": POLICY_VERSION 
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
"https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :getIamPolicy"
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
-Uri "https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :getIamPolicy" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/resource-manager/reference/rest/v1/projects/getIamPolicy).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.





The response contains the resource's allow policy. For example:




```
{
"version": 1,
"etag": "BwWKmjvelug=",
"bindings": [
{
"role": "roles/owner",
"members": [
"principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com"
]
}
]
}
```































## Grant or revoke a single IAM role

You can use the Google Cloud Dedicated console and the gcloud CLI to quickly
grant or revoke a single role for a single principal, without editing the
resource's allow policy directly.

Common types of principals include service accounts, identities in workforce
identity pools, and identities in workload identity pools.

For a list of all
principal types, see [Principal types](/iam/docs/principals-overview#principal-types).

In general, policy changes take effect within 2 minutes. However, in some cases, it
can take 7 minutes or more for changes to propagate across the system.

If you need help identifying the most appropriate predefined role, see
[Find the right predefined roles](/iam/docs/choose-predefined-roles).





### Grant a single IAM role

To grant a single role to a principal, do the following:















[Console](#console) [ gcloud ](#gcloud) 
**More 










- 

In the Google Cloud Dedicated console, go to the **IAM** page.

[Go
to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

- 

Select a project, folder, or organization.

- 

Select a principal to grant a role to:

- 

To grant a role to a principal who already has other roles on the resource,
find a row containing the principal, click
edit **Edit principal** in that row,
and click add **Add another role**.

To grant a role to a [service agent](/iam/docs/service-account-types#service-agents), select the **Include
-provided role grants** checkbox to see its email address.

- 

To grant a role to a principal who doesn't have any existing roles on the
resource, click person_add **Grant
Access**, then enter a
[principal identifier](/iam/docs/principal-identifiers)—for
example,
`//iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

- 

Click Select a role**, then enter the name of a role or permission to filter for a role to grant.
To follow the principle of least privilege, choose a role that includes only the permissions that
your principal needs.

- 

Optional: Add a [condition](/iam/docs/conditions-overview) to the role.

- 

Click **Save**. The principal is granted the role on the resource.

To grant a role to a principal for more than one project, folder, or
organization, do the following:

- 

In the Google Cloud Dedicated console, go to the **Manage resources** page.

[Go to
Manage resources](https://console.cloud.berlin-build0.goog/cloud-resource-manager)

- 

Select all the resources for which you want to grant permissions.

- 

If the info panel is not visible, click **Show info panel**. Then, click
**Permissions**.

- 

Select a principal to grant a role to:

- To grant a role to a principal who already has other roles, find a row
containing the principal, click
edit **Edit principal** in that row,
and click add **Add another role**.

- To grant a role to a principal who does not already have other roles,
click person_add **Grant access**,
then enter a [principal
identifier](/iam/docs/principal-identifiers)—for example,
`//iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

- 

Click **Select a role**, then enter the name of a role or permission to filter for a role to grant.
To follow the principle of least privilege, choose a role that includes only the permissions that
your principal needs.

- 

Optional: Add a [condition](/iam/docs/conditions-overview) to the role.

- 

Click **Save**. The principal is granted the selected role on each of the
selected resources.









































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




The

`[add-iam-policy-binding](/sdk/gcloud/reference/projects/add-iam-policy-binding)`

command lets you quickly grant a role to a principal.



Before using any of the command data below,
make the following replacements:


- 


` RESOURCE_TYPE `: The resource type that you want to
manage access to. Use `projects`, `resource-manager folders`, or
`organizations`.



- 


` RESOURCE_ID `: Your Google Cloud Dedicated project, folder,
or organization ID. Project IDs are alphanumeric, like `my-project`.
Folder and organization IDs are numeric, like `123456789012`.



- 


` PRINCIPAL `: An identifier for the principal, or member,
which usually has the following form:
` PRINCIPAL_TYPE : ID `.
For example, `principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.
For a full list of the values that ` PRINCIPAL ` can have, see [Principal identifiers](/iam/docs/principal-identifiers).




- 


` ROLE_NAME `: The name of the role that you want
to grant. Use one of the following formats:





- Predefined roles: `roles/ SERVICE . IDENTIFIER `

- Project-level custom roles: `projects/ PROJECT_ID /roles/ IDENTIFIER `

- Organization-level custom roles: `organizations/ ORG_ID /roles/ IDENTIFIER `




For a list of predefined roles, see [Understanding roles](/iam/docs/understanding-roles).




- 


` CONDITION `: The condition to add to the role
binding. If you don't want to add a condition, use the value `None`. For
more information about conditions, see the [conditions overview](/iam/docs/conditions-overview).



Execute the

following

command:


#### Linux, macOS, or Cloud Shell




```
gcloud ** RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \ 
--member = PRINCIPAL --role = ROLE_NAME \ 
--condition = CONDITION 
```




#### Windows (PowerShell)




```
gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID ` 
--member = PRINCIPAL --role = ROLE_NAME ` 
--condition = CONDITION 
```




#### Windows (cmd.exe)





```
gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID ^
--member = PRINCIPAL --role = ROLE_NAME ^
--condition = CONDITION 
```





The response contains the updated IAM allow policy.



























### Revoke a single IAM role

To revoke a single role from a principal, do the following:















[Console](#console) [ gcloud ](#gcloud) 
More 










- 

In the Google Cloud Dedicated console, go to the **IAM** page.

[
Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

- 

Select a project, folder, or organization.

- 

Find the row containing the principal whose access you want to revoke. Then,
click edit **Edit principal** in that
row.

- 

Click the **Delete** delete button for
the role that you want to revoke, and then click **Save**.








































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


To quickly revoke a role from a user, run the `remove-iam-policy-binding`
command:


```
gcloud RESOURCE_TYPE remove-iam-policy-binding RESOURCE_ID 

--member = PRINCIPAL --role = ROLE_NAME 
```



Provide the following values:




- 


` RESOURCE_TYPE `: The resource type that you want to
manage access to. Use `projects`, `resource-manager folders`, or
`organizations`.



- 


` RESOURCE_ID `: Your Google Cloud Dedicated project, folder,
or organization ID. Project IDs are alphanumeric, like `my-project`.
Folder and organization IDs are numeric, like `123456789012`.



- 


` PRINCIPAL `: An identifier for the principal, or
member, which usually has the following form:
` PRINCIPAL_TYPE : ID `.
For example, `principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.




- 


` ROLE_NAME `: The name of the role that you want
to revoke. Use one of the following formats:





- Predefined roles: `roles/ SERVICE . IDENTIFIER `

- Project-level custom roles: `projects/ PROJECT_ID /roles/ IDENTIFIER `

- Organization-level custom roles: `organizations/ ORG_ID /roles/ IDENTIFIER `




For a list of predefined roles, see [Understanding roles](/iam/docs/understanding-roles).







For example, to revoke the Project Creator role from the service account
`example-service-account@example-project.eu0.iam.gserviceaccount.com` for the project `example-project`:


```
gcloud projects remove-iam-policy-binding example-project 

--member = serviceAccount:example-service-account@example-project.eu0.iam.gserviceaccount.com 

--role = roles/resourcemanager.projectCreator
```























To help ensure that you don't revoke any necessary roles, you can enable [change
risk recommendations](/recommender/docs/change-risk-recommendations). Change risk recommendations
generate warnings when you try to revoke project-level roles that
Google Cloud Dedicated has identified as important.

## Grant or revoke multiple IAM roles using the Google Cloud Dedicated console

You can use the Google Cloud Dedicated console to grant and revoke multiple roles for
a single principal:

- 

In the Google Cloud Dedicated console, go to the **IAM** page.

[
Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

- 

Select a project, folder, or organization.

- 

Select the principal whose roles you want to modify:

- 

To modify roles for a principal who already has roles on the
resource, find a row containing the principal, click edit **Edit principal** in that row, and
click add **Add another role**.

To modify roles for a [service agent](/iam/docs/service-account-types#service-agents), select the
**Include -provided role grants** checkbox to see its
email address.

- 

To grant roles to a principal who doesn't have any roles on the resource,
click person_add **Grant Access**, then
enter a [principal
identifier](/iam/docs/principal-identifiers)—for example, `//iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

- 

Modify the principal's roles:

- To grant a role to a principal who doesn't have any existing roles on the resource, click
Select a role**, then filter for a role to grant.

- To grant an additional role to the principal, click **Add another role**, then
filter for a role to grant.

- To replace one of the principal's roles
with a different role, click the existing role, then filter for a different role to grant.

- To revoke one of the principal's roles, click the **Delete** delete button for each role that you want to
revoke.

You can also [add a condition](/iam/docs/managing-conditional-role-bindings#add) to a role, [modify a role's
condition](/iam/docs/managing-conditional-role-bindings#modify), or [remove a role's
condition](/iam/docs/managing-conditional-role-bindings#removing).

- 

Click **Save**.






## Grant or revoke multiple IAM roles programmatically

To make large-scale access changes that involve granting and revoking multiple
roles for multiple principals, use the *read-modify-write* pattern to update the
resource's allow policy:

- Read the current allow policy by calling `getIamPolicy()`.

- Edit the allow policy, either by using a text editor or programmatically, to
add or remove any principals or role bindings.

- Write the updated allow policy by calling `setIamPolicy()`.

You can use the gcloud CLI, the REST API, or the Resource Manager
client libraries to update the allow policy.

In general, policy changes take effect within 2 minutes. However, in some cases, it
can take 7 minutes or more for changes to propagate across the system.



### Get the current allow policy















[ gcloud ](#gcloud) [ C# ](#c) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
**More 










The

`[gcloud get-iam-policy](/sdk/gcloud/reference/projects/add-iam-policy-binding)`

command gets a project's, folder's, or organization's allow policy.

Before using any of the command data below,
make the following replacements:


- 


` RESOURCE_TYPE `: The type of the resource that you want
to get the allow policy for. Valid values are
`projects`, `resource-manager folders`, or
`organizations`.



- 


` RESOURCE_ID `: Your Google Cloud Dedicated project, folder,
or organization ID. Project IDs are alphanumeric, like
`my-project`. Folder and organization IDs are numeric, like
`123456789012`.



- 


` FORMAT `: The desired format for the allow policy. Use
`json` or `yaml`.



- 


` PATH `: The path to a new output file for the allow
policy.



Execute the

following

command:


#### Linux, macOS, or Cloud Shell




```
gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format = FORMAT > PATH 
```




#### Windows (PowerShell)




```
gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format = FORMAT > PATH 
```




#### Windows (cmd.exe)





```
gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format = FORMAT > PATH 
```






For example, the following command gets the allow policy for the project
`my-project` and saves it to your home directory in JSON format:


```
gcloud projects get-iam-policy my-project --format json > ~/policy.json
```

















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).

The following example shows how to get the allow policy for a project. To
learn how to get the allow policy of a folder or organization, review the
[Resource Managerclient library
documentation](/resource-manager/docs/libraries) for your programming language.



























```
using [ Google.Apis.Auth.OAuth2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.CloudResourceManager.v1 ; 
using Google.Apis.CloudResourceManager.v1.Data ; 

public partial class AccessManager 
{ 
public static Policy GetPolicy ( string projectId ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( CloudResourceManagerService . Scope . CloudPlatform ); 
var service = new CloudResourceManagerService ( 
new CloudResourceManagerService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

var policy = service . Projects . GetIamPolicy ( new GetIamPolicyRequest (), 
projectId ). Execute (); 
return policy ; 
} 
} 
```



















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).

The following example shows how to get the allow policy for a project. To
learn how to get the allow policy of a folder or organization, review the
[Resource Managerclient library
documentation](/resource-manager/docs/libraries) for your programming language.



























```
import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) ; 
import com.google.iam.admin.v1.[ProjectName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) ; 
import com.google.iam.v1.[GetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import java.io.IOException ; 

public class GetProjectPolicy { 
public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
// TODO: Replace with your project ID. 
String projectId = "your-project-id" ; 

getProjectPolicy ( projectId ); 
} 

// Gets a project's policy. 
public static [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getProjectPolicy ( String projectId ) throws IOException { 
// Initialize client that will be used to send requests. 
// This client only needs to be created once, and can be reused for multiple requests. 
try ( [ ProjectsClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ ProjectsClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) . create ()) { 
[ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [ GetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) . newBuilder () 
. setResource ( [ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) . of ( projectId ). toString ()) 
. build (); 
return projectsClient . getIamPolicy ( request ); 
} 
} 
} 
```



















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).

The following example shows how to get the allow policy for a project. To
learn how to get the allow policy of a folder or organization, review the
[Resource Managerclient library
documentation](/resource-manager/docs/libraries) for your programming language.



























```
from google.cloud import resourcemanager_v3 
from google.iam.v1 import iam_policy_pb2 , policy_pb2 

def get_project_policy ( project_id : str ) - > policy_pb2 . Policy : 
"""Get policy for project. 

project_id: ID or number of the Google Cloud project you want to use. 
""" 

client = resourcemanager_v3 . ProjectsClient () 
request = iam_policy_pb2 . GetIamPolicyRequest () 
request . resource = f "projects/ { project_id } " 

policy = client . get_iam_policy ( request ) 
print ( f "Policy retrieved: { policy } " ) 

return policy 
```










































The Resource Manager API's
`[get-iam-policy](/resource-manager/reference/rest/v1/projects/getIamPolicy)`

method gets a project's, folder's, or organization's allow policy.












Before using any of the request data,
make the following replacements:


- ` API_VERSION `: The API version to use. For
projects and organizations, use `v1`. For folders, use `v2`.

- ` RESOURCE_TYPE `: The resource type whose
policy you want to manage. Use the value `projects`, `folders`, or
`organizations`.

- ` RESOURCE_ID `: Your Google Cloud Dedicated
project, organization, or folder ID. Project IDs are alphanumeric strings, like
`my-project`. Folder and organization IDs are numeric, like `123456789012`.


- ` POLICY_VERSION `: The policy version to be
returned. Requests should specify the most recent policy version, which is policy version
3. See [Specifying
a policy version when getting a policy](/iam/docs/allow-policies#specifying-version-get) for details.

HTTP method and URL:



```
POST https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :getIamPolicy
```



Request JSON body:



```
{
"options": {
"requestedPolicyVersion": POLICY_VERSION 
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
"https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :getIamPolicy"
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
-Uri "https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :getIamPolicy" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/resource-manager/reference/rest/v1/projects/getIamPolicy).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.





The response contains the resource's allow policy. For example:




```
{
"version": 1,
"etag": "BwWKmjvelug=",
"bindings": [
{
"role": "roles/owner",
"members": [
"principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com"
]
}
]
}
```



Save the response in a file of the appropriate type (`json` or `yaml`).























### Modify the allow policy

Programmatically or using a text editor, modify the local copy of your
resource's allow policy to reflect the roles that you want to grant or revoke.

To help prevent you from overwriting other changes, don't edit or remove the
allow policy's `etag` field. The `etag` field identifies the current state of
the allow policy. When you [set the updated allow policy](#setting-policy),
IAM compares the `etag` value in the request with the
existing `etag`, and only writes the allow policy if the values match.

To edit the roles that an allow policy grants, you need to edit the role
bindings in the allow policy. Role bindings have the following format:


```
{ 
"role" : " ** ROLE_NAME " , 
"members" : [ 
" PRINCIPAL_1 " , 
" PRINCIPAL_2 " , 
... 
" PRINCIPAL_N " 
], 
"conditions:" { 
CONDITIONS 
} 
} 
```


Replace the following:

- 

` ROLE_NAME `: The name of the role that you want to
grant. Use one of the following formats:

- Predefined roles: `roles/ SERVICE . IDENTIFIER `

- Project-level custom roles: `projects/ PROJECT_ID /roles/ IDENTIFIER `

- Organization-level custom roles: `organizations/ ORG_ID /roles/ IDENTIFIER `

For a list of predefined roles, see [Understanding
roles](/iam/docs/understanding-roles).

- 

` PRINCIPAL_1 `, ` PRINCIPAL_2 `,
`... PRINCIPAL_N `: Identifiers for the principals that
you want to grant the role to.

Principal identifiers usually have the following form:
` PRINCIPAL-TYPE : ID `.
For example, `principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com` or
`principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.
For a full list of the values that ` PRINCIPAL ` can have,
see [Principal identifiers](/iam/docs/principal-identifiers).

- 

` CONDITIONS `: Optional. Any [conditions](/iam/docs/conditions-overview)
that specify when access will be granted.

#### Grant an IAM role

To grant roles to your principals, modify the role bindings in the allow policy.
To learn what roles you can grant, see
[Understanding roles](/iam/docs/understanding-roles), or
[view grantable roles](/iam/docs/viewing-grantable-roles) for the resource. If you need help to
identify the most appropriate predefined roles, see
[Find the right predefined roles](/iam/docs/choose-predefined-roles).

Optionally, you can use [conditions](/iam/docs/conditions-overview) to grant roles only when
certain requirements are met.

To grant a role that is already included in the allow policy, add the principal
to an existing role binding:















[ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 










Edit the returned allow policy by adding the principal to an existing role
binding. This change won't take effect until you
[set the updated allow policy](#setting-policy).

For example, imagine the allow policy contains the following role binding, which
grants the Security Reviewer role (`roles/iam.securityReviewer`) to
Kai:


```
{ 
"role" : "roles/iam.securityReviewer" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/kai@example.com" 
] 
} 
```


To grant that same role to Raha, add Raha's principal identifier to the
existing role binding:


```
{ 
"role" : "roles/iam.securityReviewer" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/kai@example.com" , 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/raha@example.com" **
] 
} 
```


















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).



























```
using System.Linq ; 
using Google.Apis.CloudResourceManager.v1.Data ; 

public partial class AccessManager 
{ 
public static Policy AddMember ( Policy policy , string role , string member ) 
{ 
var binding = policy . Bindings . First ( x = > x . Role == role ); 
binding . Members . Add ( member ); 
return policy ; 
} 
} 
```


















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).



























```
import ( 
"fmt" 
"io" 

"google.golang.org/api/iam/v1" 
) 

// addMember adds a member to a role binding. 
func addMember ( w io . Writer , policy * iam . Policy , role , member string ) { 
for _ , binding := range policy . Bindings { 
if binding . Role != role { 
continue 
} 
for _ , m := range binding . Members { 
if m != member { 
continue 
} 
fmt . Fprintf ( w , "Role %q found. Member already exists.\n" , role ) 
return 
} 
binding . Members = append ( binding . Members , member ) 
fmt . Fprintf ( w , "Role %q found. Member added.\n" , role ) 
return 
} 
fmt . Fprintf ( w , "Role %q not found. Member not added.\n" , role ) 
} 
```



















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).



























```
import com.google.iam.v1.[Binding](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import java.util.ArrayList ; 
import java.util.List ; 

public class AddMember { 
public static void main ( String [] args ) { 
// TODO(developer): Replace the variables before running the sample. 
// TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount). 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . newBuilder (). build (); 
// TODO: Replace with your role. 
String role = "roles/existing-role" ; 
// TODO: Replace with your principal. 
// For examples, see https://cloud.google.com/iam/docs/principal-identifiers 
String member = "principal-id" ; 

addMember ( policy , role , member ); 
} 

// Adds a principal to a pre-existing role. 
public static [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) addMember ( [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy , String role , String member ) { 
List newBindingsList = new ArrayList <> (); 

for ( [ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : policy . [ getBindingsList ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__) ()) { 
if ( b . getRole (). equals ( role )) { 
newBindingsList . add ( b . toBuilder (). [ addMembers ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_) ( member ). build ()); 
} else { 
newBindingsList . add ( b ); 
} 
} 

// Update the policy to add the principal. 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policy . [ toBuilder ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__) () 
. [ clearBindings ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__) () 
. [ addAllBindings ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__) ( newBindingsList ) 
. build (); 

System . out . println ( "Added principal: " + updatedPolicy . [ getBindingsList ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__) ()); 

return updatedPolicy ; 
} 
} 
```



















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).



























```
from google.iam.v1 import policy_pb2 
from snippets.get_policy import get_project_policy 
from snippets.set_policy import set_project_policy 

def modify_policy_add_principal ( 
project_id : str , role : str , principal : str 
) - > policy_pb2 . Policy : 
"""Add a principal to certain role in project policy. 

project_id: ID or number of the Google Cloud project you want to use. 
role: role to which principal need to be added. 
principal: The principal requesting access. 

For principal ID formats, see https://cloud.google.com/iam/docs/principal-identifiers 
""" 
policy = get_project_policy ( project_id ) 

for bind in policy . bindings : 
if bind . role == role : 
bind . members . append ( principal ) 
break 

return set_project_policy ( project_id , policy ) 
```










































Edit the returned allow policy by adding the principal to an existing role
binding. This change won't take effect until you
[set the updated allow policy](#setting-policy).

For example, imagine the allow policy contains the following role binding, which
grants the Security Reviewer role (`roles/iam.securityReviewer`) to
Kai:


```
{ 
"role" : "roles/iam.securityReviewer" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/kai@example.com" 
] 
} 
```


To grant that same role to Raha, add Raha's principal identifier to the
existing role binding:


```
{ 
"role" : "roles/iam.securityReviewer" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/kai@example.com" , 
** "principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/raha@example.com" **
] 
} 
```






















To grant a role that is not yet included in the allow policy, add a new role
binding:















[ gcloud ](#gcloud) [ C# ](#c) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
**More 










Edit the allow policy by adding a new role binding that grants the role to the
principal. This change won't take effect until you
[set the updated allow policy](#setting-policy).

For example, to grant the Compute Storage Admin role
(`roles/compute.storageAdmin`) to Raha, add the following role binding to the
`bindings` array for the allow policy:


```
{ 
"role" : "roles/compute.storageAdmin" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/raha@example.com" 
] 
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






To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).


























```
using System.Collections.Generic ; 
using Google.Apis.CloudResourceManager.v1.Data ; 

public partial class AccessManager 
{ 
public static Policy AddBinding ( Policy policy , string role , string member ) 
{ 
var binding = new Binding 
{ 
Role = role , 
Members = new List { member } 
}; 
policy . Bindings . Add ( binding ); 
return policy ; 
} 
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






To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).


























```
import com.google.iam.v1.[Binding](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import java.util.Collections ; 
import java.util.List ; 

public class AddBinding { 
public static void main ( String [] args ) { 
// TODO(developer): Replace the variables before running the sample. 
// TODO: Replace with your policy: GetPolicy.getPolicy(projectId, serviceAccount). 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . newBuilder (). build (); 
// TODO: Replace with your role. 
String role = "roles/role-to-add" ; 
// TODO: Replace with your principals. 
// For examples, see https://cloud.google.com/iam/docs/principal-identifiers 
List members = Collections . singletonList ( "principal-id" ); 

addBinding ( policy , role , members ); 
} 

// Adds a principals to a role. 
public static [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) addBinding ( [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy , String role , List members ) { 
[ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = [ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) . newBuilder () 
. setRole ( role ) 
. [ addAllMembers ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addAllMembers_java_lang_Iterable_java_lang_String__) ( members ) 
. build (); 

// Update bindings for the policy. 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policy . [ toBuilder ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__) (). [ addBindings ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_) ( binding ). build (); 

System . out . println ( "Added binding: " + updatedPolicy . [ getBindingsList ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__) ()); 

return updatedPolicy ; 
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






To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).


























```
def modify_policy_add_role ( policy : dict , role : str , principal : str ) - > dict : 
"""Adds a new role binding to a policy.""" 

binding = { "role" : role , "members" : [ principal ]} 
policy [ "bindings" ] . append ( binding ) 
print ( policy ) 
return policy 
```










































Edit the allow policy by adding a new role binding that grants the role to the
principal. This change won't take effect until you
[set the updated allow policy](#setting-policy).

For example, to grant the Compute Storage Admin role
(`roles/compute.storageAdmin`) to Raha, add the following role binding to the
`bindings` array for the allow policy:


```
{ 
"role" : "roles/compute.storageAdmin" , 
"members" : [ 
"principal://iam.googleapis.com/locations/global/workforcePools/example-pool/subject/raha@example.com" 
] 
} 
```






















You can only grant roles related to activated API services. If a service, such
as Compute Engine, is not active, you cannot grant roles exclusively related to
Compute Engine. For more information, see
[Enable and disable APIs](https://support.google.com/cloud/answer/6158841).

There are some unique constraints when granting permissions on projects,
especially when granting the Owner (`roles/owner`) role. See the
[`projects.setIamPolicy()`reference documentation](/resource-manager/reference/rest/v1/projects/setIamPolicy)
for more information.

#### Revoke an IAM role

To revoke a role, remove the principal from the role binding. If there are no
other principals in the role binding, remove the entire role binding.















[ gcloud ](#gcloud) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 










Revoke a role by editing the JSON or YAML allow policy returned by the
`get-iam-policy` command. This change won't take effect until you
[set the updated allow policy](#setting-policy).

To revoke a role from a principal, delete the principal or binding from the
`bindings` array for the allow policy.























































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






To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).


























```
using System.Linq ; 
using Google.Apis.CloudResourceManager.v1.Data ; 

public partial class AccessManager 
{ 
public static Policy RemoveMember ( Policy policy , string role , string member ) 
{ 
try 
{ 
var binding = policy . Bindings . First ( x = > x . Role == role ); 
if ( binding . Members . Count != 0 && binding . Members . Contains ( member )) 
{ 
binding . Members . Remove ( member ); 
} 
if ( binding . Members . Count == 0 ) 
{ 
policy . Bindings . Remove ( binding ); 
} 
return policy ; 
} 
catch ( System . InvalidOperationException e ) 
{ 
System . Diagnostics . Debug . WriteLine ( "Role does not exist in policy: \n" + e . ToString ()); 
return policy ; 
} 
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






To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).


























```
import ( 
"fmt" 
"io" 

"google.golang.org/api/iam/v1" 
) 

// removeMember removes a member from a role binding. 
func removeMember ( w io . Writer , policy * iam . Policy , role , member string ) { 
bindings := policy . Bindings 
bindingIndex , memberIndex := - 1 , - 1 
for bIdx := range bindings { 
if bindings [ bIdx ]. Role != role { 
continue 
} 
bindingIndex = bIdx 
for mIdx := range bindings [ bindingIndex ]. Members { 
if bindings [ bindingIndex ]. Members [ mIdx ] != member { 
continue 
} 
memberIndex = mIdx 
break 
} 
} 
if bindingIndex == - 1 { 
fmt . Fprintf ( w , "Role %q not found. Member not removed.\n" , role ) 
return 
} 
if memberIndex == - 1 { 
fmt . Fprintf ( w , "Role %q found. Member not found.\n" , role ) 
return 
} 

members := removeIdx ( bindings [ bindingIndex ]. Members , memberIndex ) 
bindings [ bindingIndex ]. Members = members 
if len ( members ) == 0 { 
bindings = removeIdx ( bindings , bindingIndex ) 
policy . Bindings = bindings 
} 
fmt . Fprintf ( w , "Role %q found. Member removed.\n" , role ) 
} 

// removeIdx removes arr[idx] from arr. 
func removeIdx [ T any ]( arr [] T , idx int ) [] T { 
return append ( arr [: idx ], arr [ idx + 1 :] ... ) 
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






To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).


























```
import com.google.iam.v1.[Binding](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import java.io.IOException ; 
import java.util.ArrayList ; 
import java.util.List ; 

public class RemoveMember { 
public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
// TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount). 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . newBuilder (). build (); 
// TODO: Replace with your role. 
String role = "roles/existing-role" ; 
// TODO: Replace with your principal. 
// For examples, see https://cloud.google.com/iam/docs/principal-identifiers 
String member = "principal-id" ; 

removeMember ( policy , role , member ); 
} 

// Removes principal from a role; removes binding if binding contains no members. 
public static [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) removeMember ( [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy , String role , String member ) { 
// Creating new builder with all values copied from origin policy 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . Builder policyBuilder = policy . [ toBuilder ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__) (); 

// Getting binding with suitable role. 
[ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null ; 
for ( [ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : policy . [ getBindingsList ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__) ()) { 
if ( b . getRole (). equals ( role )) { 
binding = b ; 
break ; 
} 
} 

if ( binding != null && binding . [ getMembersList ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__) (). contains ( member )) { 
List newMemberList = new ArrayList <> ( binding . [ getMembersList ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__) ()); 
// Removing principal from the role 
newMemberList . remove ( member ); 

System . out . println ( "Member " + member + " removed from " + role ); 

// Adding all remaining principals to create new binding 
[ Binding ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) newBinding = binding . [ toBuilder ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_toBuilder__) () 
. [ clearMembers ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_clearMembers__) () 
. [ addAllMembers ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addAllMembers_java_lang_Iterable_java_lang_String__) ( newMemberList ) 
. build (); 

List newBindingList = new ArrayList <> ( policyBuilder . getBindingsList ()); 

// Removing old binding to replace with new one 
newBindingList . remove ( binding ); 

// If binding has no more members, binding will not be added 
if ( ! newBinding . [ getMembersList ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__) (). isEmpty ()) { 
newBindingList . add ( newBinding ); 
} 

// Update the policy to remove the principal. 
policyBuilder . [ clearBindings ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__) () 
. [ addAllBindings ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__) ( newBindingList ); 
} 

[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policyBuilder . build (); 

System . out . println ( "Exising principals: " + updatedPolicy . [ getBindingsList ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__) ()); 

return updatedPolicy ; 
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






To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).


























```
from google.iam.v1 import policy_pb2 
from snippets.get_policy import get_project_policy 
from snippets.set_policy import set_project_policy 

def modify_policy_remove_principal ( 
project_id : str , role : str , principal : str 
) - > policy_pb2 . Policy : 
"""Remove a principal from certain role in project policy. 

project_id: ID or number of the Google Cloud project you want to use. 
role: role to revoke. 
principal: The principal to revoke access from. 

For principal ID formats, see https://cloud.google.com/iam/docs/principal-identifiers 
""" 
policy = get_project_policy ( project_id ) 

for bind in policy . bindings : 
if bind . role == role : 
if principal in bind . members : 
bind . members . remove ( principal ) 
break 

return set_project_policy ( project_id , policy , False ) 
```










































Revoke a role by editing the JSON or YAML allow policy returned by the
`get-iam-policy` command. This change won't take effect until you
[set the updated allow policy](#setting-policy).

To revoke a role from a principal, delete the principal or binding from the
`bindings` array for the allow policy.























### Set the allow policy

After you modify the allow policy to grant and revoke roles, call
`setIamPolicy()` to update the policy.















[ gcloud ](#gcloud) [ C# ](#c) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 










The

`[gcloud set-iam-policy](/sdk/gcloud/reference/projects/add-iam-policy-binding)`

command sets the policy in the request as the new allow policy for the project, folder, or organization.

Before using any of the command data below,
make the following replacements:


- 


` RESOURCE_TYPE `: The type of the resource that you want to set the
allow policy for. Valid values are `projects`, `resource-manager folders`,
or `organizations`.



- 


` RESOURCE_ID `: Your Google Cloud Dedicated project, folder,
or organization ID. Project IDs are alphanumeric, like
`my-project`. Folder and organization IDs are numeric, like
`123456789012`.



- 


` PATH `: The path to a file that contains the new
allow policy.



Execute the

following

command:


#### Linux, macOS, or Cloud Shell




```
gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH 
```




#### Windows (PowerShell)




```
gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH 
```




#### Windows (cmd.exe)





```
gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH 
```





The response contains the updated allow policy.

For example, the following command sets the allow policy stored in `policy.json`
as the allow policy for the project `my-project`:


```
gcloud projects set-iam-policy my-project ~/policy.json
```








































































```
using [ Google.Apis.Auth.OAuth2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.CloudResourceManager.v1 ; 
using Google.Apis.CloudResourceManager.v1.Data ; 

public partial class AccessManager 
{ 
public static Policy SetPolicy ( string projectId , Policy policy ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( CloudResourceManagerService . Scope . CloudPlatform ); 
var service = new CloudResourceManagerService ( 
new CloudResourceManagerService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

return service . Projects . SetIamPolicy ( new SetIamPolicyRequest 
{ 
Policy = policy 
}, projectId ). Execute (); 
} 
} 
```



















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).

The following example shows how to set the allow policy for a project. To
learn how to set the allow policy of a folder or organization, review the
[Resource Manager client library
documentation](/resource-manager/docs/libraries) for your programming language.



























```
import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) ; 
import com.google.iam.admin.v1.[ProjectName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) ; 
import com.google.iam.v1.[Policy](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import com.google.iam.v1.[SetIamPolicyRequest](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) ; 
import com.google.protobuf.[FieldMask](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 
import java.util.Arrays ; 
import java.util.List ; 

public class SetProjectPolicy { 
public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
// TODO: Replace with your project ID. 
String projectId = "your-project-id" ; 
// TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount). 
[ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . newBuilder (). build (); 

setProjectPolicy ( policy , projectId ); 
} 

// Sets a project's policy. 
public static [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) setProjectPolicy ( [ Policy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy , String projectId ) 
throws IOException { 

// Initialize client that will be used to send requests. 
// This client only needs to be created once, and can be reused for multiple requests. 
try ( [ ProjectsClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ ProjectsClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) . create ()) { 
List paths = Arrays . asList ( "bindings" , "etag" ); 
[ SetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request = [ SetIamPolicyRequest ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) . newBuilder () 
. setResource ( [ ProjectName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) . of ( projectId ). toString ()) 
. [ setPolicy ](https://berlin.devsitetest.how/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_) ( policy ) 
// A FieldMask specifying which fields of the policy to modify. Only 
// the fields in the mask will be modified. If no mask is provided, the 
// following default mask is used: 
// `paths: "bindings, etag"` 
. setUpdateMask ( [ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addAllPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__) ( paths ). build ()) 
. build (); 

return projectsClient . setIamPolicy ( request ); 
} 
} 
} 
```



















































To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see [Before you begin](#before-you-begin).

To learn how to install and use the client library for Resource Manager, see
[Resource Manager client
libraries](/resource-manager/docs/libraries).

The following example shows how to set the allow policy for a project. To
learn how to set the allow policy of a folder or organization, review the
[Resource Manager client library
documentation](/resource-manager/docs/libraries) for your programming language.



























```
from google.cloud import [ resourcemanager_v3 ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest)
from google.iam.v1 import iam_policy_pb2 , policy_pb2 

def set_project_policy ( 
project_id : str , policy : policy_pb2 . Policy , merge : bool = True 
) - > policy_pb2 . Policy : 
""" 
Set policy for project. Pay attention that previous state will be completely rewritten. 
If you want to update only part of the policy follow the approach read->modify->write. 
For more details about policies check out https://cloud.google.com/iam/docs/policies 

project_id: ID or number of the Google Cloud project you want to use. 
policy: Policy which has to be set. 
merge: The strategy to be used forming the request. CopyFrom is clearing both mutable and immutable fields, 
when MergeFrom is replacing only immutable fields and extending mutable. 
https://googleapis.dev/python/protobuf/latest/google/protobuf/message.html#google.protobuf.message.Message.CopyFrom 
""" 
client = [ resourcemanager_v3 ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest) . [ ProjectsClient ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html) () 

request = iam_policy_pb2 . GetIamPolicyRequest () 
request . resource = f "projects/ { project_id } " 
current_policy = client . [ get_iam_policy ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_get_iam_policy) ( request ) 

# Etag should as fresh as possible to lower chance of collisions 
policy . ClearField ( "etag" ) 
if merge : 
current_policy . MergeFrom ( policy ) 
else : 
current_policy . CopyFrom ( policy ) 

request = iam_policy_pb2 . SetIamPolicyRequest () 
request . resource = f "projects/ { project_id } " 

# request.etag field also will be merged which means you are secured from collision, 
# but it means that request may fail and you need to leverage exponential retries approach 
# to be sure policy has been updated. 
request . policy . CopyFrom ( current_policy ) 

policy = client . [ set_iam_policy ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_set_iam_policy) ( request ) 
return policy 
```










































The Resource Manager API's
`[set-iam-policy](/resource-manager/reference/rest/v1/projects/setIamPolicy)`

method sets the policy in the request as the new allow policy for the project, folder, or organization.












Before using any of the request data,
make the following replacements:


- ` API_VERSION `: The API version to use. For
projects and organizations, use `v1`. For folders, use `v2`.

- ` RESOURCE_TYPE `: The resource type whose
policy you want to manage. Use the value `projects`, `folders`, or
`organizations`.

- ` RESOURCE_ID `: Your Google Cloud Dedicated
project, organization, or folder ID. Project IDs are alphanumeric strings, like
`my-project`. Folder and organization IDs are numeric, like `123456789012`.


- 


` POLICY `: A JSON representation of the policy that you
want to set. For more information about the format of a policy, see the
[Policy reference](/iam/docs/reference/rest/v1/Policy).



HTTP method and URL:



```
POST https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :setIamPolicy
```



Request JSON body:



```
{
"policy": POLICY 
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
"https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :setIamPolicy"
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
-Uri "https://cloudresourcemanager.googleapis.com/ API_VERSION / RESOURCE_TYPE / RESOURCE_ID :setIamPolicy" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/resource-manager/reference/rest/v1/projects/setIamPolicy).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.





The response contains the updated allow policy.





















## What's next

- Learn how to [manage access to service accounts](/iam/docs/manage-access-service-accounts).

- Learn the general steps for
[managing access to other resources](/iam/docs/manage-access-other-resources).

- Find out how to
[choose the most appropriate predefined roles](/iam/docs/choose-predefined-roles).

- Discover how to
[view the roles that you can grant on a particular resource](/iam/docs/viewing-grantable-roles).

- Learn how to make a principal's access conditional with
[conditional role bindings](/iam/docs/conditions-overview).