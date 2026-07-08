# Create and manage custom roles

Source: https://berlin.devsitetest.how/iam/docs/creating-custom-roles
Last updated: 2026-07-08

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












# Create and manage custom roles 






- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Required roles ](#required-roles)

- [ View available permissions for projects, folders, and organizations ](#viewing-resource-permissions)
- [ Get the role metadata ](#get-metadata)
- [ Create a custom role ](#creating)
- [ Edit an existing custom role ](#edit-role)
- [ Disable a custom role ](#disabling-custom-role)
- [ List roles ](#roles-list)
- [ Delete a custom role ](#deleting-custom-role)
- [ Undelete a custom role ](#undelete-role)
- [ What's next ](#whats-next)
- 










This page describes how to create and manage Identity and Access Management (IAM)
custom roles. Managing roles includes modifying, disabling, listing, deleting,
and undeleting roles.

## Before you begin 

- 




Enable the IAM API.






Roles required to enable APIs**


To enable APIs, you need the Service Usage Admin IAM
role (`roles/serviceusage.serviceUsageAdmin`), which
contains the `serviceusage.services.enable` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).



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

Understand the Google Cloud Dedicated in Germany [resource hierarchy](/iam/docs/overview#resource-hierarchy).

- 

Read [Understanding IAM custom roles](/iam/docs/understanding-custom-roles).

### Required roles

























































To get the permissions that
you need to create and manage custom roles,

ask your administrator to grant you the
following IAM roles:












- 
To manage roles for a project:
[Role Administrator ](/iam/docs/roles-permissions/iam#iam.roleAdmin) (`roles/iam.roleAdmin`)
on the project that you want to manage roles for





- 
To manage roles for an organization:
[Organization Role Administrator ](/iam/docs/roles-permissions/iam#iam.organizationRoleAdmin) (`roles/iam.organizationRoleAdmin`)
on the organization that you want to manage roles for










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).











## View available permissions for projects, folders, and organizations

You can create custom roles for an entire organization, or for a specific
project in that organization. The permissions that are available for custom
roles depend on where you create the role. For example, if a permission can only
be used at the organization level, then you can't include that permission in a
project-level custom role.

To check which permissions are available for organization-level and
project-level custom roles, you can use the gcloud CLI or the
Identity and Access Management API to list the permissions that are available in a specific
organization or project. For example, you can get all permissions that are
available for custom roles that are created in your project.

Some permissions might not be visible to you or usable in a custom role, even if they are supported
in custom roles. For example, a permission might not be available for use in custom roles if you
have not [enabled the API](/apis/docs/getting-started#enabling_apis) for the service.

To learn more about the permissions that you can add to custom roles, see
[Supported permissions](/iam/docs/roles-overview#custom-role-supported-permissions).















[ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 













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


Use the `[gcloud iam list-testable-permissions](/sdk/gcloud/reference/iam/list-testable-permissions)` command to get a list of permissions that are available for custom roles in a
specific project or organization. The response lists the permissions that you
can use in custom roles for that project or organization.



To list permissions that are available in custom roles for a project or
organization, run this command:


```
gcloud iam list-testable-permissions FULL_RESOURCE_NAME \
--filter="customRolesSupportLevel!=NOT_SUPPORTED"
```



Replace ` FULL_RESOURCE_NAME ` with one of the following
values:




- 


Project: `//cloudresourcemanager.googleapis.com/projects/ PROJECT_ID `
(for example, `//cloudresourcemanager.googleapis.com/projects/my-project`)



- 


Organization: `//cloudresourcemanager.googleapis.com/organizations/ NUMERIC_ID `
(for example, `//cloudresourcemanager.googleapis.com/organizations/123456789012`)






The results indicate whether each permission is supported in custom roles.
Permissions that do not have a `customRolesSupportLevel` field are fully
supported.



The `list-testable-permissions` command might return hundreds of results. This
partial example shows the format of each result:


```
---
name: appengine.applications.create
stage: GA
---
customRolesSupportLevel: TESTING
name: appengine.applications.disable
stage: GA
---
name: appengine.applications.get
stage: GA
---
name: appengine.applications.update
stage: GA
---
name: appengine.instances.delete
stage: GA
---
name: appengine.instances.get
stage: GA
---
```























































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
[]( std :: string const & resource ) { 
iam :: IAMClient client ( iam :: MakeIAMConnection ()); 
google :: iam :: admin :: v1 :: QueryTestablePermissionsRequest request ; 
request . set_full_resource_name ( resource ); 
int count = 0 ; 
for ( auto & permission : client . QueryTestablePermissions ( request )) { 
if ( ! permission ) throw std :: move ( permission ). status (); 
std :: cout "Permission successfully retrieved: " permission - > name () 
" \n " ; 
++ count ; 
} 
if ( count == 0 ) { 
std :: cout "No testable permissions found in resource: " resource 
" \n " ; 
} 
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
using System.Collections.Generic ; 
using [ Google.Apis.Auth.OAuth2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.Iam.v1 ; 
using Google.Apis.Iam.v1.Data ; 

public partial class CustomRoles 
{ 
public static IList QueryTestablePermissions ( 
string fullResourceName ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 
var service = new IamService ( new IamService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

var request = new QueryTestablePermissionsRequest 
{ 
FullResourceName = fullResourceName 
}; 
var response = service . Permissions . QueryTestablePermissions ( request ) 
. Execute (); 
foreach ( var p in response . Permissions ) 
{ 
Console . WriteLine ( p . Name ); 
} 
return response . Permissions ; 
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

// queryTestablePermissions lists testable permissions on a resource. 
func queryTestablePermissions ( w io . Writer , fullResourceName string ) ([] * iam . Permission , error ) { 
ctx := context . Background () 
service , err := iam . NewService ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "iam.NewService: %w" , err ) 
} 

request := & iam . QueryTestablePermissionsRequest { 
FullResourceName : fullResourceName , 
} 
response , err := service . Permissions . QueryTestablePermissions ( request ). Do () 
if err != nil { 
return nil , fmt . Errorf ( "Permissions.QueryTestablePermissions: %w" , err ) 
} 
for _ , p := range response . Permissions { 
fmt . Fprintf ( w , "Found permissions: %v" , p . Name ) 
} 
return response . Permissions , nil 
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
import com.google.cloud.iam.admin.v1.[IAMClient](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).[QueryTestablePermissionsPagedResponse](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.QueryTestablePermissionsPagedResponse.html) ; 
import com.google.iam.admin.v1.[QueryTestablePermissionsRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.QueryTestablePermissionsRequest.html) ; 
import java.io.IOException ; 

/** View available permissions in a project. */ 
public class QueryTestablePermissions { 
public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variable before running the sample. 
// Full resource names can take one of the following forms: 
// cloudresourcemanager.googleapis.com/projects/PROJECT_ID 
// cloudresourcemanager.googleapis.com/organizations/NUMERIC_ID 
String fullResourceName = "your-full-resource-name" ; 

queryTestablePermissions ( fullResourceName ); 
} 

public static void queryTestablePermissions ( String fullResourceName ) throws IOException { 
[ QueryTestablePermissionsRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.QueryTestablePermissionsRequest.html) queryTestablePermissionsRequest = 
[ QueryTestablePermissionsRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.QueryTestablePermissionsRequest.html) . newBuilder (). setFullResourceName ( fullResourceName ). build (); 

try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
[ QueryTestablePermissionsPagedResponse ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.QueryTestablePermissionsPagedResponse.html) queryTestablePermissionsPagedResponse = 
iamClient . queryTestablePermissions ( queryTestablePermissionsRequest ); 
queryTestablePermissionsPagedResponse 
. iterateAll () 
. forEach ( permission - > System . out . println ( permission . getName ())); 
} 
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
import os 
from typing import List 

from google.cloud import [ resourcemanager_v3 ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest)
from google.iam.v1 import iam_policy_pb2 , policy_pb2 

def query_testable_permissions ( 
project_id : str , permissions : List [ str ] 
) - > policy_pb2 . Policy : 
"""Tests IAM permissions of the caller. 

project_id: ID or number of the Google Cloud project you want to use. 
permissions: List of permissions to get. 
""" 

client = [ resourcemanager_v3 ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest) . [ ProjectsClient ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html) () 
request = iam_policy_pb2 . TestIamPermissionsRequest () 
request . resource = f "projects/ { project_id } " 
request . permissions . extend ( permissions ) 

permissions_reponse = client . [ test_iam_permissions ](https://berlin.devsitetest.how/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_test_iam_permissions) ( request ) 
print ( permissions_reponse ) 
return permissions_reponse . permissions 
```










































The 
`[permissions.queryTestablePermissions](/iam/docs/reference/rest/v1/permissions/queryTestablePermissions)`

method lists permissions available in an organization or project.












Before using any of the request data,
make the following replacements:


- ` FULL_RESOURCE_NAME `: A URI consisting of
the service name and the path to the resource. For examples, see
[Full resource names](/iam/docs/full-resource-names).

- ` PAGE_SIZE `: Optional. The number of permissions to include in the
response. The default value is 100, and the maximum value is 1,000. If the number of permissions
is greater than the page size, the response contains a pagination token that you can use to
retrieve the next page of results.

- ` NEXT_PAGE_TOKEN `: Optional. The pagination token returned in an earlier
response from this method. If specified, the list of testable permissions
will start where the previous response ended.

HTTP method and URL:



```
POST https://iam.googleapis.com/v1/permissions:queryTestablePermissions
```



Request JSON body:



```
{
"fullResourceName": " FULL_RESOURCE_NAME "
"pageSize": PAGE_SIZE ,
"pageToken": " NEXT_PAGE_TOKEN "
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
"https://iam.googleapis.com/v1/permissions:queryTestablePermissions"
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
-Uri "https://iam.googleapis.com/v1/permissions:queryTestablePermissions" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/iam/docs/reference/rest/v1/permissions/queryTestablePermissions).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.





The response contains the list of permissions.




```
{
"permissions": [
{
"name": "iam.serviceAccountKeys.create",
"stage": "GA"
},
{
"name": "iam.serviceAccountKeys.delete",
"stage": "GA"
},
{
"name": "iam.serviceAccountKeys.get",
"stage": "GA"
}
],
"nextPageToken": "CgoHBajEfjUDQyABEPaIv5vIiMDTVhgDIhtpYW0uc2VydmljZUFjY291bnRLZXlzLmxpc3Q"
}
```

























## Get the role metadata

Before you create a custom role, you might want to get the metadata for both
predefined and custom roles. Role metadata includes the role ID and permissions
contained in the role. You can view the metadata using the
Google Cloud Dedicated console or the IAM API.

To view the role metadata, use one of the methods below:















[Console](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
**More 










- 

In the Google Cloud Dedicated console go to the **Roles** page.

[
Go to the Roles page](https://console.cloud.berlin-build0.goog/iam-admin/roles)

- 

Select your organization or project from the drop-down list at the top of
the page.

- 

Click the tab for the type of role that you want to view metadata for:

- To view metadata for predefined roles, stay on the **Predefined** tab.

- To view metadata for custom roles, click the **Custom** tab.

- 

To view the role permissions, select the checkbox for the roles whose
permissions you want to view, then click **Details**. The panel displays the
permissions contained in the roles.

If you want to find all the roles that include a specific permission, type the
permission name in the **Filter** box at the top of the list of roles.









































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


Use the `[gcloud iam roles describe](/sdk/gcloud/reference/iam/roles/describe)`
command to view metadata for predefined roles and custom roles.



To view the metadata for a predefined role, execute the following command:


```
gcloud iam roles describe ROLE_ID 
```



` ROLE_ID ` is the ID of the role. Predefined roles include
the `role` prefix in their IDs, for example, `roles/iam.roleViewer`.



The following example demonstrates the output of the `describe` command
when executed on the predefined role `roles/iam.roleViewer`:



`gcloud iam roles describe roles/iam.roleViewer`


```
description : Read access to all custom roles in the project. 
etag : AA== 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
- resourcemanager.projects.get 
- resourcemanager.projects.getIamPolicy 
name : roles/iam.roleViewer 
stage : GA 
title : Role Viewer 
```



To view the metadata for a custom role, execute one of the following commands:




- 


To view the metadata for a custom role created at the organization level,
execute the following command:


```
gcloud iam roles describe --organization= ORGANIZATION_ID ROLE_ID 
```



- 


To view the metadata for a custom role created at the project level,
execute the following command:


```
gcloud iam roles describe --project= PROJECT_ID ROLE_ID 
```






Each placeholder value is described below:




- 


` ORGANIZATION_ID ` is the numeric ID of the organization,
such as `123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as
`my-project`.



- 


` ROLE_ID ` is the ID of the role, excluding any prefixes
like `projects/`, `organizations/`, or `roles/`. For example,
`myCompanyAdmin`.






For more information, see the reference documentation for `[gcloud iam roles describe](/sdk/gcloud/reference/iam/roles/describe)`.























































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
[]( std :: string const & name ) { 
iam :: IAMClient client ( iam :: MakeIAMConnection ()); 
google :: iam :: admin :: v1 :: GetRoleRequest request ; 
request . set_name ( name ); 
auto response = client . GetRole ( request ); 
if ( ! response ) throw std :: move ( response ). status (); 
std :: cout "Role successfully retrieved: " response - > DebugString () 
" \n " ; 
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

public partial class CustomRoles 
{ 
public static Role GetRole ( string name ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 
var service = new IamService ( new IamService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

var role = service . Roles . Get ( name ). Execute (); 
Console . WriteLine ( role . Name ); 
Console . WriteLine ( String . Join ( ", " , role . IncludedPermissions )); 
return role ; 
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

// getRole gets role metadata. 
func getRole ( w io . Writer , name string ) ( * iam . Role , error ) { 
ctx := context . Background () 
service , err := iam . NewService ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "iam.NewService: %w" , err ) 
} 

role , err := service . Roles . Get ( name ). Do () 
if err != nil { 
return nil , fmt . Errorf ( "Roles.Get: %w" , err ) 
} 
fmt . Fprintf ( w , "Got role: %v\n" , role . Name ) 
for _ , permission := range role . IncludedPermissions { 
fmt . Fprintf ( w , "Got permission: %v\n" , permission ) 
} 
return role , nil 
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
import com.google.iam.admin.v1.[GetRoleRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetRoleRequest.html) ; 
import com.google.iam.admin.v1.[Role](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) ; 
import java.io.IOException ; 

/** Get role metadata. Specifically, printing out role permissions. */ 
public class GetRole { 

public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variable before running the sample. 
String roleId = "a unique identifier (e.g. testViewer)" ; 

getRole ( roleId ); 
} 

public static void getRole ( String roleId ) throws IOException { 
[ GetRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetRoleRequest.html) getRoleRequest = [ GetRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetRoleRequest.html) . newBuilder (). setName ( roleId ). build (); 

// Initialize client for sending requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) role = iamClient . getRole ( getRoleRequest ); 
role . [ getIncludedPermissionsList ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html#com_google_iam_admin_v1_Role_getIncludedPermissionsList__) (). forEach ( permission - > System . out . println ( permission )); 
} 
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
from google.api_core.exceptions import NotFound 
from google.cloud.iam_admin_v1 import [ GetRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetRoleRequest.html) , [ IAMClient ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html) , [ Role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html)

def get_role ( project_id : str , role_id : str ) - > Role : 
client = IAMClient () 
name = f "projects/ { project_id } /roles/ { role_id } " 
request = GetRoleRequest ( name = name ) 
try : 
role = client . [ get_role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_get_role) ( request ) 
print ( f "Retrieved role: { role_id } : { role } " ) 
return role 
except NotFound as exc : 
raise NotFound ( f "Role with id [ { role_id } ] not found, take some actions" ) from exc 
```










































The 
`[roles.get](/iam/docs/reference/rest/v1/projects.roles/get)`

method gets the definition of a role.










Before using any of the request data,
make the following replacements:


- ` ROLE_NAME `: The full role name, including any
`organizations/`, `projects/`, or `roles/` prefixes. For example,
`organizations/123456789012/roles/myCompanyAdmin`.

HTTP method and URL:



```
GET https://iam.googleapis.com/v1/ ROLE_NAME 
```



To send your request, expand one of these options:


#### curl (Linux, macOS, or Cloud Shell)













Execute the following command:


































```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://iam.googleapis.com/v1/ ROLE_NAME "
```




#### PowerShell (Windows)













Execute the following command:




















































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method GET `
-Headers $headers `
-Uri "https://iam.googleapis.com/v1/ ROLE_NAME " | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Open the

[method reference page](/iam/docs/reference/rest/v1/projects.roles/get).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Complete any required fields and click Execute**.





The response contains the role definition.




```
{
"name": "projects/my-project/roles/customRole",
"title": "My Custom Role",
"description": "My custom role description.",
"includedPermissions": [
"storage.buckets.get",
"storage.buckets.list"
],
"etag": "BwWiPg2fmDE="
}
```























## Create a custom role

You can create a custom role at the project or organization level.

An organization-level custom role can include any of the IAM
[permissions that are supported in custom
roles](/iam/docs/custom-roles-permissions-support). A project-level custom role can
contain any supported permission *except for* permissions that can only be used
at the organization or folder level, such as
`resourcemanager.organizations.get`. If you try to add these permissions to a
project-level custom role, you see an error message:


[Console](#console) [gcloud](#gcloud) [REST API](#rest-api) 
**More 




The following warning message is displayed:
"Not applicable for project-level custom roles". The
permission will be automatically unselected from the list of included
permissions, and you can proceed with creating the role.



The following error message
is returned: `INVALID_ARGUMENT: Permission PERMISSION is not
valid`. The custom role will not be created until you first remove the
permission from the role definition and try
the operation again.



The following error message is returned:
`Permission PERMISSION is not valid`, along with an
HTTP 400 error code and a status of `INVALID_ARGUMENT`. The custom role will
not be created until you first remove the permission from the role
definition and try the operation again.



Each custom role can contain up to 3,000
permissions. Also, the maximum total size of the title, description, and
permission names for a custom role is 64 KB. If you
need to create a larger custom role, you can split the permissions across
multiple custom roles. Choose role titles that show the relationship between the
custom roles, such as `Custom Admin (1 of 2)` and `Custom Admin (2 of 2)`.

Each custom role can have a launch stage. Most launch stages are informational,
and help you keep track of whether each role is ready for widespread use.
Additionally, the `DISABLED` launch stage lets you [disable a custom
role](#disabling-custom-role). For more information about launch stages, see
[Testing and deploying](/iam/docs/roles-overview#custom-role-testing-deploying).















[Console](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 










Some predefined roles contain deprecated permissions or permissions that are
otherwise not permitted in custom roles. If you try to create a custom role
based on one of these predefined roles, the custom role will omit the deprecated
and restricted permissions.

To create a new custom role from scratch, do the following:

- 

In the Google Cloud Dedicated console, go to the **Roles** page.

[
Go to the Roles page](https://console.cloud.berlin-build0.goog/iam-admin/roles)

- 

Using the drop-down list at the top of the page, select the organization or
project in which you want to create a role.

- 

Click **Create custom role**.

- 

Enter a **Title**, **Description**, **ID**, and **Role launch stage**
for the role. The role ID cannot be changed after the role is created.

- 

Click **Add Permissions**.

- 

Select the permissions you want to include in the role and click **Add
Permissions**. Use the **All Services** and **All Types** drop-down lists to
filter and select permissions by services and types.

To create a custom role based on an existing predefined role, do the following:

- 

In the Google Cloud Dedicated console, go to the **Roles** page.

[
Go to the Roles page](https://console.cloud.berlin-build0.goog/iam-admin/roles) 

- 

Select the organization or project in which you want to create a role.

- 

Select the checkbox for the roles that you want to base the new custom
role on.

- 

Click **Create custom role from selection**.

- 

Enter a **Title**, **Description**, **ID**, and **Role launch stage**
for the role. The role ID cannot be changed after the role is created.

- 

Uncheck the permissions you want to exclude from the role.

- 

Click **Add Permissions** to include any permissions.

- 

Click **Create**.









































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


Use the `[gcloud iam roles create](/sdk/gcloud/reference/iam/roles/create)`
command to create new custom roles. You can use this command in two ways:




- 


By providing a YAML file that contains the role definition



- 


By using flags to specify the role definition






When creating a custom role, you must specify whether it applies to the
organization level or project level by using the
`--organization= ORGANIZATION_ID ` or
`--project= PROJECT_ID ` flags. Each example below creates a
custom role at the project level.



A custom role can contain only
[permissions that are supported in custom roles](/iam/docs/custom-roles-permissions-support).
If the custom role contains other permissions, the command fails.



To create a custom role using a YAML file:**



Create a YAML file that contains the definition for your custom role. The
file must be structured in the following way:


```
title : ** ROLE_TITLE 
description : ROLE_DESCRIPTION 
stage : LAUNCH_STAGE 
includedPermissions : 
- PERMISSION_1 
- PERMISSION_2 
```



Each placeholder value is described below:




- 


` ROLE_TITLE ` is a friendly title for the role, such as
`"My Company Admin"`.



- 


` ROLE_DESCRIPTION ` is a short description of the
role, such as `"My custom role description"`.



- 


` LAUNCH_STAGE ` indicates the stage of a role in the
launch lifecycle, such as `ALPHA`, `BETA`, or `GA`.



- 


` PERMISSION_1 ` and ` PERMISSION_2 `
are permissions to include in the custom role, such as `iam.roles.get`. You
can't use wildcard characters (`*`) in permission names.






Save the YAML file, and then execute one of the following commands:




- 


To create a custom role at the organization level, execute the following
command:


```
gcloud iam roles create ROLE_ID --organization= ORGANIZATION_ID \
--file= YAML_FILE_PATH 
```



- 


To create a custom role at the project level, execute the following command:


```
gcloud iam roles create ROLE_ID --project= PROJECT_ID \
--file= YAML_FILE_PATH 
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role, such as `myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization, such as
`123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as `my-project`.



- 


` YAML_FILE_PATH ` is the path to the location of your YAML file that
contains the custom role definition.






Examples**



The following example YAML file demonstrates how to create a role definition:


```
title : "My Company Admin" 
description : "My custom role description." 
stage : "ALPHA" 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
```



The following example demonstrates how to create a role at the organization
level using the YAML file:


```
gcloud iam roles create myCompanyAdmin --organization=123456789012 \
--file=my-role-definition.yaml
```



If the role was created successfully, the command's output is similar to the
following:


```
Created role [myCompanyAdmin]. 
description : My custom role description. 
etag : BwVkBX0sQD0= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
name : organizations/123456789012/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```



The following example demonstrates how to create a role at the project level
using the YAML file:


```
gcloud iam roles create myCompanyAdmin --project=my-project \
--file=my-role-definition.yaml
```



If the role was created successfully, the command's output is similar to the
following:


```
Created role [myCompanyAdmin]. 
description : My custom role description. 
etag : BwVkBX0sQD0= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
name : projects/my-project/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```



**To create a custom role using flags:**



Execute one of the following commands:




- 


To create a custom role at the organization level, execute the following
command:


```
gcloud iam roles create ** ROLE_ID --organization= ORGANIZATION_ID \
--title= ROLE_TITLE --description= ROLE_DESCRIPTION \
--permissions=" PERMISSIONS_LIST " --stage= LAUNCH_STAGE 
```



- 


To create a custom role at the project level, execute the following command:


```
gcloud iam roles create ROLE_ID --project= PROJECT_ID \
--title= ROLE_TITLE --description= ROLE_DESCRIPTION \
--permissions=" PERMISSIONS_LIST " --stage= LAUNCH_STAGE 
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role, such as
`myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization,
such as `123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as
`my-project`.



- 


` ROLE_TITLE ` is a friendly title for the role, such as
`"My Company Admin"`.



- 


` ROLE_DESCRIPTION ` is a short description of the role,
such as `"My custom role description."`.



- 


` PERMISSIONS_LIST ` contains a comma-separated list of
permissions you want to include in the custom role. For example:
`iam.roles.get,iam.roles.list`. You can't use wildcard characters (`*`) in
permission names.



- 


` LAUNCH_STAGE ` indicates the stage of a role in the
launch lifecycle, such as `ALPHA`, `BETA`, or `GA`.






Examples**



The following example demonstrates how to create a role at the organization
level using flags:


```
gcloud iam roles create myCompanyAdmin --organization=123456789012 \
--title="My Company Admin" --description="My custom role description." \
--permissions="iam.roles.get,iam.roles.list" --stage=ALPHA
```



If the role was created successfully, the command's output is similar to the
following:


```
Created role [myCompanyAdmin]. 
description : My custom role description. 
etag : BwVkBX0sQD0= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
name : organizations/123456789012/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```



The following example demonstrates how to create a role at the project
level using flags:


```
gcloud iam roles create myCompanyAdmin --project=my-project \
--title="My Company Admin" --description="My custom role description." \
--permissions="iam.roles.get,iam.roles.list" --stage=ALPHA
```



If the role was created successfully, the command's output is similar to the
following:


```
Created role [myCompanyAdmin]. 
description : My custom role description. 
etag : BwVkBX0sQD0= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
name : projects/my-project/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```























































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
[]( std :: string const & parent , std :: string const & role_id , 
std :: vector :: string > const & included_permissions ) { 
iam :: IAMClient client ( iam :: MakeIAMConnection ()); 
google :: iam :: admin :: v1 :: CreateRoleRequest request ; 
request . set_parent ( "projects/" + parent ); 
request . set_role_id ( role_id ); 
google :: iam :: admin :: v1 :: Role role ; 
role . set_stage ( google :: iam :: admin :: v1 :: Role :: GA ); 
for ( auto const & permission : included_permissions ) { 
* role . add_included_permissions () = permission ; 
} 
* request . mutable_role () = role ; 
auto response = client . CreateRole ( request ); 
if ( ! response ) throw std :: move ( response ). status (); 
std :: cout "Role successfully created: " response - > DebugString () 
" \n " ; 
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
using System.Collections.Generic ; 
using [ Google.Apis.Auth.OAuth2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.Iam.v1 ; 
using Google.Apis.Iam.v1.Data ; 

public partial class CustomRoles 
{ 
public static Role CreateRole ( string name , string projectId , string title , 
string description , IList permissions , string stage ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 
var service = new IamService ( new IamService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

var role = new Role 
{ 
Title = title , 
Description = description , 
IncludedPermissions = permissions , 
Stage = stage 
}; 
var request = new CreateRoleRequest 
{ 
Role = role , 
RoleId = name 
}; 
role = service . Projects . Roles . Create ( request , 
"projects/" + projectId ). Execute (); 
Console . WriteLine ( "Created role: " + role . Name ); 
return role ; 
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

// createRole creates a custom role. 
func createRole ( w io . Writer , projectID , name , title , description , stage string , permissions [] string ) ( * iam . Role , error ) { 
ctx := context . Background () 
service , err := iam . NewService ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "iam.NewService: %w" , err ) 
} 

request := & iam . CreateRoleRequest { 
Role : & iam . Role { 
Title : title , 
Description : description , 
IncludedPermissions : permissions , 
Stage : stage , 
}, 
RoleId : name , 
} 
role , err := service . Projects . Roles . Create ( "projects/" + projectID , request ). Do () 
if err != nil { 
return nil , fmt . Errorf ( "Projects.Roles.Create: %w" , err ) 
} 
fmt . Fprintf ( w , "Created role: %v" , role . Name ) 
return role , nil 
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
import com.google.iam.admin.v1.[CreateRoleRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateRoleRequest.html) ; 
import com.google.iam.admin.v1.[Role](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) ; 
import com.google.iam.admin.v1.[Role](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).[RoleLaunchStage](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.RoleLaunchStage.html) ; 
import java.io.IOException ; 
import java.util.Arrays ; 

/** Create role. */ 
public class CreateRole { 
public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
String projectId = "your-project-id" ; 
String roleId = "a unique identifier (e.g. testViewer)" ; 
String title = "a title for your role (e.g. IAM Role Viewer)" ; 
String description = "a description of the role" ; 
Iterable includedPermissions = 
Arrays . asList ( "roles/iam.roleViewer" , "roles/logging.viewer" ); 

createRole ( projectId , title , description , includedPermissions , roleId ); 
} 

public static void createRole ( 
String projectId , 
String title , 
String description , 
Iterable includedPermissions , 
String roleId ) 
throws IOException { 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) . Builder roleBuilder = 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) . newBuilder () 
. setTitle ( title ) 
. setDescription ( description ) 
. [ addAllIncludedPermissions ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.Builder.html#com_google_iam_admin_v1_Role_Builder_addAllIncludedPermissions_java_lang_Iterable_java_lang_String__) ( includedPermissions ) 
// See launch stage enums at 
// https://cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#rolelaunchstage 
. setStage ( [ RoleLaunchStage ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.RoleLaunchStage.html) . BETA ); 
[ CreateRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateRoleRequest.html) createRoleRequest = 
[ CreateRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateRoleRequest.html) . newBuilder () 
. setParent ( "projects/" + projectId ) 
. [ setRoleId ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateRoleRequest.Builder.html#com_google_iam_admin_v1_CreateRoleRequest_Builder_setRoleId_java_lang_String_) ( roleId ) 
. setRole ( roleBuilder ) 
. build (); 

// Initialize client for sending requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) result = iamClient . createRole ( createRoleRequest ); 
System . out . println ( "Created role: " + result . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html#com_google_iam_admin_v1_Role_getName__) ()); 
} 
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
from typing import List , Optional 

from google.api_core.exceptions import AlreadyExists , FailedPrecondition 
from google.cloud.iam_admin_v1 import [ CreateRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateRoleRequest.html) , [ IAMClient ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html) , [ Role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html)

def create_role ( 
project_id : str , role_id : str , permissions : List [ str ], title : Optional [ str ] = None 
) - > Role : 
"""Creates iam role with given parameters. 

Args: 
project_id: GCP project id 
role_id: id of GCP iam role 
permissions: list of iam permissions to assign to role. f.e ["iam.roles.get", "iam.roles.list"] 
title: title for iam role. role_id will be used in case of None 

Returns: google.cloud.iam_admin_v1.Role object 
""" 
client = IAMClient () 

parent = f "projects/ { project_id } " 

request = CreateRoleRequest ( 
parent = parent , 
role_id = role_id , 
role = Role ( title = title , included_permissions = permissions ), 
) 
try : 
role = client . [ create_role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_create_role) ( request ) 
print ( f "Created iam role: { role_id } : { role } " ) 
return role 
except AlreadyExists : 
print ( f "Role with id [ { role_id } ] already exists, take some actions" ) 
except FailedPrecondition : 
print ( 
f "Role with id [ { role_id } ] already exists and in deleted state, take some actions" 
) 
```










































The 
`[roles.create](/iam/docs/reference/rest/v1/projects.roles/create)`

method creates a custom role in a project or organization.












Before using any of the request data,
make the following replacements:


- ` RESOURCE_TYPE `: The resource type whose
custom roles you want to manage. Use the value `projects` or `organizations`.


- ` RESOURCE_ID `: The project ID or
organization ID whose custom roles you want to manage. Project IDs are alphanumeric strings, like
`my-project`. Organization IDs are numeric, like `123456789012`.

- ` ROLE_ID `: The name of the role, such as
`myCompanyAdmin`.

- ` ROLE_TITLE `: The human-readable title for the
role. For example, `My Company Admin`.

- ` ROLE_DESCRIPTION `: A description for the
role. For example, `"The company admin role allows company admins to access important
resources"`.

- 


` PERMISSION_1 ` and
` PERMISSION_2 `: The permissions that you want to include in the role. For
example, `storage.objects.update`. You can't use wildcard characters (`*`) in
permission names.



A custom role can contain only
[permissions that are supported in custom
roles](/iam/docs/custom-roles-permissions-support). If the custom role contains other permissions, the request fails.




- ` LAUNCH_STAGE `: The current launch stage of the
role. This field can contain one of the following values: `EAP`, `ALPHA`,
`BETA`, `GA`, `DEPRECATED`, or `DISABLED`.

HTTP method and URL:



```
POST https://iam.googleapis.com/v1/ ** RESOURCE_TYPE / RESOURCE_ID /roles
```



Request JSON body:



```
{
"roleId": " ROLE_ID ",
"role": {
"title": " ROLE_TITLE ",
"description": " ROLE_DESCRIPTION ",
"includedPermissions": [
" PERMISSION_1 ",
" PERMISSION_2 "
],
"stage": " LAUNCH_STAGE "
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
"https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles"
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
-Uri "https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/iam/docs/reference/rest/v1/projects.roles/create).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.





The response contains the role you created.




```
{
"name": "projects/myProject/roles/myCompanyAdmin",
"title": "My Company Admin",
"description": "My custom role description.",
"includedPermissions": [
"iam.roles.get",
"iam.roles.list"
],
"etag": "BwWox/JbaZw="
}
```

























## Edit an existing custom role

A common pattern for updating a resource's metadata, such as a custom role, is
the *read-modify-write* pattern. With this pattern, you read the role's current
state, update the data locally, and then send the modified data for writing.

The read-modify-write pattern can cause a conflict if two or more independent
processes attempt the sequence simultaneously. For example, if two owners for a
project try to make conflicting changes to a role at the same time, some changes
could fail. IAM solves this problem using an `etag` property in
custom roles. This property is used to verify if the custom role has changed
since the last request. When you make a request to IAM with an
etag value, IAM compares the etag value in the request with the
existing etag value associated with the custom role. It writes the change only
if the etag values match.

When you update a role, first get the role using `roles.get()`, update the role,
and then write the updated role using `roles.patch()`. Use the etag value when
setting the role only if the corresponding role in `roles.get()` contains an
etag value.















[Console](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
**More 










- 

In the Google Cloud Dedicated console, go to the **Custom** tab of the **Roles**
page.

[
Go to the Roles page](https://console.cloud.berlin-build0.goog/iam-admin/roles/custom)

- 

Using the drop-down list at the top of the page, select the project or
organization that contains the role that you want to edit.

- 

Click the name of a custom role to open the details page for that role.

- 

Click **Edit role**.

- 

To update the role's metadata, edit the role's **Title**, **Description**,
or **Role launch stage**.

- 

To update the role's permissions, do the following:

- Click **Add Permissions** to add new permissions to the role.

- Uncheck permissions to remove permissions from the role.

- 

Click **Update** to save the edited role.









































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


Use the `[gcloud iam roles update](/sdk/gcloud/reference/iam/roles/update)`
command to update custom roles. You can use this command in two ways:




- 


By providing a YAML file that contains the updated role definition



- 


By using flags to specify the updated role definition






When updating a custom role, you must specify whether it applies to the
organization level or project level by using the `--organization= ORGANIZATION_ID `
or `--project= PROJECT_ID ` flags. Each example below creates a
custom role at the project level.



To update a custom role using a YAML file:**



Get the current definition for the role by executing one of the following commands:




- 


To get the role definition of an organization-level custom role, execute the
following command:


```
gcloud iam roles describe ** ROLE_ID --organization= ORGANIZATION_ID 
```



- 


To get the role definition of a project-level custom role, execute the following command:


```
gcloud iam roles describe ROLE_ID --project= PROJECT_ID 
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role to update, such as
`myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization, such as
`123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as `my-project`.






The `describe` command returns the role's definition and includes
an `etag` value that uniquely identifies the current version
of the role. The `etag` value should be provided in the updated
role definition to ensure that any concurrent role changes are not overwritten.



The `describe` command returns the following output:


```
description : ROLE_DESCRIPTION 
etag : ETAG 
includedPermissions : 
- PERMISSION_1 
- PERMISSION_2 
name : ROLE_NAME 
stage : LAUNCH_STAGE 
title : ROLE_TITLE 
```



Each placeholder value is described below:




- 


` ROLE_DESCRIPTION ` is a short description of the role,
such as `"My custom role description"`.



- 


` ETAG ` is the unique identifier for the current
version of the role, such as `BwVkBkbfr70=`.



- 


` PERMISSION_1 ` and ` PERMISSION_2 `
are permissions to include in the custom role, such as `iam.roles.get`.
You can't use wildcard characters (`*`) in permission names.



- 


` ROLE_NAME ` is the full role name, including any
`organizations/`, `projects/`, or `roles/`
prefixes. For example, `organizations/123456789012/roles/myCompanyAdmin.`



- 


` LAUNCH_STAGE ` indicates the stage of a role in the
launch lifecycle, such as `ALPHA`, `BETA`, or `GA`.



- 


` ROLE_TITLE ` is a friendly title for the role, such as
`"My Company Admin"`.






To update the role, either include the outputted role definition to a YAML
file or update the original YAML file with the outputted `etag` value.



Consider the following example YAML file, which contains the output from
the `describe` command for a project-level role and adds two
Cloud Storage permissions:


```
description : My custom role description. 
etag : BwVkBkbfr70= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
- storage.buckets.get 
- storage.buckets.list 
name : projects/my-project/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```



Save the YAML file, and then execute one of the following commands:




- 


To update an organization-level role, execute the following command:


```
gcloud iam roles update ROLE_ID --organization= ORGANIZATION_ID \
--file= YAML_FILE_PATH 
```



- 


To update a project-level role, execute the following command:


```
gcloud iam roles update ROLE_ID --project= PROJECT_ID \
--file= YAML_FILE_PATH 
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role to update, such as
`myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization,
such as `123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as
`my-project-id`.



- 


` YAML_FILE_PATH ` is the path to the location of your YAML
file that contains the updated custom role definition.






Examples**



The following example demonstrates how to update an organization-level role using a YAML file:


```
gcloud iam roles update ** ROLE_ID --organization= ORGANIZATION_ID \
--file= YAML_FILE_PATH 
```




- 


To update a project-level role, execute the following command:


```
gcloud iam roles update ROLE_ID --project= PROJECT_ID \
--file= YAML_FILE_PATH 
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role to update, such as
`myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization, such as
`123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as `my-project`.



- 


` YAML_FILE_PATH ` is the path to the location of your YAML file that
contains the updated custom role definition.






Examples**



The following example demonstrates how to update an organization-level role
using a YAML file:


```
gcloud iam roles update myCompanyAdmin --organization=123456789012 \
--file=my-role-definition.yaml
```



If the role was updated successfully, the command's output is similar to the
following:


```
description : My custom role description. 
etag : BwVkBwDN0lg= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
- storage.buckets.get 
- storage.buckets.list 
name : organizations/123456789012/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```



The following example demonstrates how to update a project-level role using a YAML file:


```
gcloud iam roles update myCompanyAdmin --project=my-project \
--file=my-role-definition.yaml
```



If the role was updated successfully, the command's output is similar to the following:


```
description : My custom role description. 
etag : BwVkBwDN0lg= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
- storage.buckets.get 
- storage.buckets.list 
name : projects/my-project/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```



**To update a custom role using flags:**



Each part of a role definition can be updated using a corresponding flag.
See the `[gcloud iam roles update](/sdk/gcloud/reference/iam/roles/update)`
topic for a list of all possible flags.



You can use the following flags to add or remove permissions:




- 


`--add-permissions= PERMISSIONS `: Adds one or more
comma-separated permissions to the role. You can't use wildcard characters
(`*`) in permission names.



- 


`--remove-permissions= PERMISSIONS `: Removes one or more
comma-separated permissions from the role. You can't use wildcard characters
(`*`) in permission names.






Alternatively, you can simply specify the new permissions using the
`--permissions= PERMISSIONS ` flag and providing a
comma-separated list of permissions to replace the existing permissions list.



To update other parts of the role definition, execute one of the following
commands:




- 


To update an organization-level role, execute the following command:


```
gcloud iam roles update ** ROLE_ID --organization= ORGANIZATION_ID \
--title= ROLE_TITLE --description= ROLE_DESCRIPTION \
--stage= LAUNCH_STAGE 
```



- 


To update a project-level role, execute the following command:


```
gcloud iam roles update ROLE_ID --project= PROJECT_ID \
--title= ROLE_TITLE --description= ROLE_DESCRIPTION \
--stage= LAUNCH_STAGE 
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role, such as `myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization,
such as `123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as
`my-project`.



- 


` ROLE_TITLE ` is a friendly title for the role, such as
`"My Company Admin"`.



- 


` ROLE_DESCRIPTION ` is a short description of the role,
such as `"My custom role description."`.



- 


` LAUNCH_STAGE ` indicates the stage of a role in the
launch lifecycle, such as `ALPHA`, `BETA`, or `GA`.






Examples**



The following example demonstrates how to add permissions to an
organization-level role using flags:


```
gcloud iam roles update myCompanyAdmin --organization=123456789012 \
--add-permissions="storage.buckets.get,storage.buckets.list"
```



If the role was updated successfully, the command's output is similar to the following:


```
description : My custom role description. 
etag : BwVkBwDN0lg= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
- storage.buckets.get 
- storage.buckets.list 
name : organizations/123456789012/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```



The following example demonstrates how to add permissions to a project-level role using flags:


```
gcloud iam roles update myCompanyAdmin --project=my-project \
--add-permissions="storage.buckets.get,storage.buckets.list"
```



If the role was updated successfully, the command's output is similar to the following:


```
description : My custom role description. 
etag : BwVkBwDN0lg= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
- storage.buckets.get 
- storage.buckets.list 
name : projects/my-project/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```























































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
[]( std :: string const & name , std :: string const & title ) { 
iam :: IAMClient client ( iam :: MakeIAMConnection ()); 
google :: iam :: admin :: v1 :: UpdateRoleRequest request ; 
request . set_name ( name ); 
google :: iam :: admin :: v1 :: Role role ; 
role . set_title ( title ); 
google :: protobuf :: FieldMask update_mask ; 
* update_mask . add_paths () = "title" ; 
* request . mutable_role () = role ; 
* request . mutable_update_mask () = update_mask ; 
auto response = client . UpdateRole ( request ); 
if ( ! response ) throw std :: move ( response ). status (); 
std :: cout "Role successfully updated: " response - > DebugString () 
" \n " ; 
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
using System.Collections.Generic ; 
using [ Google.Apis.Auth.OAuth2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.Iam.v1 ; 
using Google.Apis.Iam.v1.Data ; 

public partial class CustomRoles 
{ 
public static Role EditRole ( string name , string projectId , string newTitle , 
string newDescription , IList newPermissions , string newStage ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 
var service = new IamService ( new IamService . Initializer 
{ 
HttpClientInitializer = credential 
}); 
// First, get a Role using List() or Get(). 
string resource = $"projects/{projectId}/roles/{name}" ; 
var role = service . Projects . Roles . Get ( resource ). Execute (); 
// Then you can update its fields. 
role . Title = newTitle ; 
role . Description = newDescription ; 
role . IncludedPermissions = newPermissions ; 
role . Stage = newStage ; 
role = service . Projects . Roles . Patch ( role , resource ). Execute (); 
Console . WriteLine ( "Updated role: " + role . Name ); 
return role ; 
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

// editRole modifies a custom role. 
func editRole ( w io . Writer , projectID , name , newTitle , newDescription , newStage string , newPermissions [] string ) ( * iam . Role , error ) { 
ctx := context . Background () 
service , err := iam . NewService ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "iam.NewService: %w" , err ) 
} 

resource := "projects/" + projectID + "/roles/" + name 
role , err := service . Projects . Roles . Get ( resource ). Do () 
if err != nil { 
return nil , fmt . Errorf ( "Projects.Roles.Get: %w" , err ) 
} 
role . Title = newTitle 
role . Description = newDescription 
role . IncludedPermissions = newPermissions 
role . Stage = newStage 
role , err = service . Projects . Roles . Patch ( resource , role ). Do () 
if err != nil { 
return nil , fmt . Errorf ( "Projects.Roles.Patch: %w" , err ) 
} 
fmt . Fprintf ( w , "Updated role: %v" , role . Name ) 
return role , nil 
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
import com.google.iam.admin.v1.[Role](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) ; 
import com.google.iam.admin.v1.[Role](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).[RoleLaunchStage](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.RoleLaunchStage.html) ; 
import com.google.iam.admin.v1.[UpdateRoleRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html) ; 
import com.google.protobuf.[FieldMask](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 

/** Edit role metadata. Specifically, update description and launch stage. */ 
public class EditRole { 

public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
// Role ID must point to an existing role. 
String projectId = "your-project-id" ; 
String roleId = "a unique identifier (e.g. testViewer)" ; 
String description = "a new description of the role" ; 

editRole ( projectId , roleId , description ); 
} 

public static void editRole ( String projectId , String roleId , String description ) 
throws IOException { 
String roleName = "projects/" + projectId + "/roles/" + roleId ; 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) . Builder roleBuilder = 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) . newBuilder () 
. setName ( roleName ) 
. setDescription ( description ) 
// See launch stage enums at 
// https://cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#rolelaunchstage 
. setStage ( [ RoleLaunchStage ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.RoleLaunchStage.html) . GA ); 
[ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_) ( "description" ). [ addPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_) ( "stage" ). build (); 
[ UpdateRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html) updateRoleRequest = 
[ UpdateRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html) . newBuilder () 
. setName ( roleName ) 
. setRole ( roleBuilder ) 
. setUpdateMask ( fieldMask ) 
. build (); 

// Initialize client for sending requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) result = iamClient . updateRole ( updateRoleRequest ); 
System . out . println ( "Edited role:\n" + result ); 
} 
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
from google.api_core.exceptions import NotFound 
from google.cloud.iam_admin_v1 import [ IAMClient ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html) , [ Role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html) , [ UpdateRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UpdateRoleRequest.html)

from snippets.get_role import get_role 

def edit_role ( role : Role ) - > Role : 
"""Edits an existing IAM role in a GCP project. 

Args: 
role: google.cloud.iam_admin_v1.Role object to be updated 

Returns: Updated google.cloud.iam_admin_v1.Role object 
""" 
client = IAMClient () 
request = UpdateRoleRequest ( name = role . name , role = role ) 
try : 
role = client . [ update_role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_update_role) ( request ) 
print ( f "Edited role: { role . name } : { role } " ) 
return role 
except NotFound : 
print ( f "Role [ { role . name } ] not found, take some actions" ) 
```










































The 
`[roles.patch](/iam/docs/reference/rest/v1/projects.roles/patch)`

method updates a custom role in a project or organization.












Before using any of the request data,
make the following replacements:

**Required:**


- ` RESOURCE_TYPE `: The resource type whose
custom roles you want to manage. Use the value `projects` or `organizations`.


- ` RESOURCE_ID `: The project ID or
organization ID whose custom roles you want to manage. Project IDs are alphanumeric strings, like
`my-project`. Organization IDs are numeric, like `123456789012`.

- ` ROLE_NAME `: The full role name, including any
`organizations/`, `projects/`, or `roles/` prefixes. For example,
`organizations/123456789012/roles/myCompanyAdmin`.

**Recommended:**


- ` ETAG `: An identifier for a version of the role.
Include this field to prevent overwriting other role changes.

**Optional (define one or more of the following values):**


- ` ROLE_TITLE `: The human-readable title for the
role. For example, `My Company Admin`.

- ` ROLE_DESCRIPTION `: A description for the
role. For example, `"The company admin role allows company admins to access important
resources"`.

- ` PERMISSION_1 ` and
` PERMISSION_2 `: The permissions that you want to include in the role. For
example, `storage.objects.update`. You can't use wildcard characters (`*`) in
permission names.

- ` LAUNCH_STAGE `: The current launch stage of the
role. This field can contain one of the following values: `EAP`, `ALPHA`,
`BETA`, `GA`, `DEPRECATED`, or `DISABLED`.

HTTP method and URL:



```
PATCH https://iam.googleapis.com/v1/ ** RESOURCE_TYPE / RESOURCE_ID /roles
```



Request JSON body:



```
{
"roleId": " ROLE_NAME ",
"title": " ROLE_TITLE ",
"description": " ROLE_DESCRIPTION ",
"includedPermissions": [
" PERMISSION_1 ",
" PERMISSION_2 "
],
"stage": " LAUNCH-STAGE ",
"etag": " ETAG "
}
```



To send your request, expand one of these options:


#### curl (Linux, macOS, or Cloud Shell)













Save the request body in a file named `request.json`,
and execute the following command:






































```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
"https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles"
```




#### PowerShell (Windows)













Save the request body in a file named `request.json`,
and execute the following command:
























































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method PATCH `
-Headers $headers `
-ContentType: "application/json; charset=utf-8" `
-InFile request.json `
-Uri "https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/iam/docs/reference/rest/v1/projects.roles/patch).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.





The response contains an abbreviated role definition that includes the role name, the fields that
you updated, and an etag that identifies the current version of the role.




```
{
"name": "projects/test-project-1000092/roles/myCompanyAdmin",
"title": "My Updated Company Admin",
"includedPermissions": [
"storage.buckets.get",
"storage.buckets.list"
],
"stage": "BETA",
"etag": "BwWoyDpAxBc="
}
```

























## Disable a custom role

You can disable a custom role by changing its launch stage to `DISABLED`. When a
role is disabled, any role bindings related to the role are inactivated,
meaning that granting the role to a user has no effect.















[Console](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
**More 










- 

In the Google Cloud Dedicated console, go to the **Custom** tab of the **Roles**
page.

[
Go to the Roles page](https://console.cloud.berlin-build0.goog/iam-admin/roles/custom)

- 

Using the drop-down list at the top of the page, select the project or
organization that contains the role that you want to disable.

- 

Select the checkbox for the roles that you want to disable and click
**Disable**.









































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


Use the `[gcloud iam roles update](/sdk/gcloud/reference/iam/roles/update)`
command to disable a custom role by setting its launch stage to `DISABLED`.



As described in the gcloud** tab of the
[Editing an existing custom role](#editing_an_existing_custom_role)
section, you can update an existing custom role in the following two ways:




- 


By providing a YAML file that contains the updated role definition



- 


By using flags to specify the updated role definition






The easiest way to disable an existing custom role is to use the `--stage`
flag and set it to `DISABLED`. Execute one of the following commands:




- 


To disable an organization-level role, execute the following command:


```
gcloud iam roles update ** ROLE_ID --organization= ORGANIZATION_ID \
--stage=DISABLED
```



- 


To disable a project-level role, execute the following command:


```
gcloud iam roles update ROLE_ID --project= PROJECT_ID \
--stage=DISABLED
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role, such as `myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization, such as
`123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as `my-project`.






Examples**



The following example demonstrates how to disable an organization-level role:


```
gcloud iam roles update myCompanyAdmin --organization=123456789012 \
--stage=DISABLED
```



If the role was updated successfully, the command's output is similar to the following:


```
description : My custom role description. 
etag : BwVkB5NLIQw= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
name : organizations/123456789012/roles/myCompanyAdmin 
stage : DISABLED 
title : My Company Admin 
```



The following example demonstrates how to disable a project-level role:


```
gcloud iam roles update myCompanyAdmin --project=my-project \
--stage=DISABLED
```



If the role was updated successfully, the command's output is similar to the following:


```
description : My custom role description. 
etag : BwVkB5NLIQw= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
name : projects/my-project/roles/myCompanyAdmin 
stage : DISABLED 
title : My Company Admin 
```










































[Update](/iam/docs/creating-custom-roles#editing_an_existing_custom_role)
the `stage` field of the role to `DISABLED`.









































[Update](/iam/docs/creating-custom-roles#editing_an_existing_custom_role)
the `stage` field of the role to `DISABLED`.








































[Update](/iam/docs/creating-custom-roles#editing_an_existing_custom_role)
the `stage` field of the role to `DISABLED`.






















































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
import com.google.iam.admin.v1.[Role](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) ; 
import com.google.iam.admin.v1.[UpdateRoleRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html) ; 
import com.google.protobuf.[FieldMask](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 

public class DisableRole { 

public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
// Role ID must point to an existing role. 
String projectId = "your-project-id" ; 
String roleId = "testRole" ; 

[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) role = disableRole ( projectId , roleId ); 
System . out . println ( "Role name: " + role . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html#com_google_iam_admin_v1_Role_getName__) ()); 
System . out . println ( "Role stage: " + role . [ getStage ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html#com_google_iam_admin_v1_Role_getStage__) ()); 
} 

public static [ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) disableRole ( String projectId , String roleId ) 
throws IOException { 
String roleName = "projects/" + projectId + "/roles/" + roleId ; 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) role = [ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) . newBuilder () 
. setName ( roleName ) 
. setStage ( [ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) . RoleLaunchStage . DISABLED ) 
. build (); 

[ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_) ( "stage" ). build (); 
[ UpdateRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html) updateRoleRequest = 
[ UpdateRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html) . newBuilder () 
. setName ( roleName ) 
. setRole ( role ) 
. setUpdateMask ( fieldMask ) 
. build (); 

// Initialize client for sending requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
return iamClient . updateRole ( updateRoleRequest ); 
} 
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
from google.api_core.exceptions import NotFound 
from google.cloud.iam_admin_v1 import [ GetRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetRoleRequest.html) , [ IAMClient ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html) , [ Role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html) , [ UpdateRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UpdateRoleRequest.html)

def disable_role ( project_id : str , role_id : str ) - > Role : 
"""Disables an IAM role in a GCP project. 

Args: 
project_id: GCP project ID 
role_id: ID of GCP IAM role 

Returns: Updated google.cloud.iam_admin_v1.Role object with disabled stage 
""" 
client = IAMClient () 
name = f "projects/ { project_id } /roles/ { role_id } " 
get_request = GetRoleRequest ( name = name ) 
try : 
role = client . [ get_role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_get_role) ( get_request ) 
role . stage = [ Role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html) . [ RoleLaunchStage ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.RoleLaunchStage.html) . DISABLED 
update_request = UpdateRoleRequest ( name = role . name , role = role ) 
client . [ update_role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_update_role) ( update_request ) 
print ( f "Disabled role: { role_id } : { role } " ) 
return role 
except NotFound as exc : 
raise NotFound ( f 'Role with id [ { role_id } ] not found, take some actions' ) from exc 
```










































The 
`[roles.patch](/iam/docs/reference/rest/v1/projects.roles/patch)`

method lets you change a custom role's launch stage to `DISABLED`,
which disables the role.
















Before using any of the request data,
make the following replacements:


- ` RESOURCE_TYPE `: The resource type whose
custom roles you want to manage. Use the value `projects` or `organizations`.


- ` RESOURCE_ID `: The project ID or
organization ID whose custom roles you want to manage. Project IDs are alphanumeric strings, like
`my-project`. Organization IDs are numeric, like `123456789012`.

- ` ROLE_NAME `: The full role name, including any
`organizations/`, `projects/`, or `roles/` prefixes. For example,
`organizations/123456789012/roles/myCompanyAdmin`.


- ` ETAG `: An identifier for a version of the role.
Include this field to prevent overwriting other role changes.

HTTP method and URL:



```
PATCH https://iam.googleapis.com/v1/ ** RESOURCE_TYPE / RESOURCE_ID /roles
```



Request JSON body:



```
{
"roleId": " ROLE_NAME ",
"stage": DISABLED,
"etag": " ETAG "
}
```



To send your request, expand one of these options:


#### curl (Linux, macOS, or Cloud Shell)













Save the request body in a file named `request.json`,
and execute the following command:






































```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
"https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles"
```




#### PowerShell (Windows)













Save the request body in a file named `request.json`,
and execute the following command:
























































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method PATCH `
-Headers $headers `
-ContentType: "application/json; charset=utf-8" `
-InFile request.json `
-Uri "https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/iam/docs/reference/rest/v1/projects.roles/patch).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.







You should receive a JSON response similar to the following:






```
{
"name": "projects/test-project-1000092/roles/myCompanyAdmin",
**"stage": "DISABLED",**
"etag": "BwWoyDpAxBc="
}
```

























## List roles

You can list all custom roles created in your project or organization.















[Console](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
**More 










In the Google Cloud Dedicated console, go to the **Custom** tab of the **Roles** page.

[
Go to the Roles page](https://console.cloud.berlin-build0.goog/iam-admin/roles/custom)

All the custom roles for the organization or project that you have selected are
listed on the page.









































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


Use the `[gcloud iam roles list](/sdk/gcloud/reference/iam/roles/list)`
command to list custom roles and predefined roles for a project or organization:




- 


To list organization-level custom roles, execute the following command:


```
gcloud iam roles list --organization= ORGANIZATION_ID 
```



- 


To list project-level custom roles, execute the following command:


```
gcloud iam roles list --project= PROJECT_ID 
```






Each placeholder value is described below:




- 


` ORGANIZATION_ID ` is the numeric ID of the organization, such as
`123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as `my-project`.






To list deleted roles, you can also specify the `--show-deleted` flag.



Execute the following command to list predefined roles:


```
gcloud iam roles list
```























































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
[]( std :: string const & project ) { 
iam :: IAMClient client ( iam :: MakeIAMConnection ()); 
int count = 0 ; 
google :: iam :: admin :: v1 :: ListRolesRequest request ; 
request . set_parent ( project ); 
for ( auto & role : client . ListRoles ( request )) { 
if ( ! role ) throw std :: move ( role ). status (); 
std :: cout "Roles successfully retrieved: " role - > name () " \n " ; 
++ count ; 
} 
if ( count == 0 ) { 
std :: cout "No roles found in project: " project " \n " ; 
} 
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
using System.Collections.Generic ; 
using [ Google.Apis.Auth.OAuth2 ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.Iam.v1 ; 
using Google.Apis.Iam.v1.Data ; 

public partial class CustomRoles 
{ 
public static IList ListRoles ( string projectId ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 
var service = new IamService ( new IamService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

var response = service . Projects . Roles . List ( "projects/" + projectId ) 
. Execute (); 
foreach ( var role in response . Roles ) 
{ 
Console . WriteLine ( role . Name ); 
} 
return response . Roles ; 
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

// listRoles lists a project's roles. 
func listRoles ( w io . Writer , projectID string ) ([] * iam . Role , error ) { 
ctx := context . Background () 
service , err := iam . NewService ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "iam.NewService: %w" , err ) 
} 

response , err := service . Projects . Roles . List ( "projects/" + projectID ). Do () 
if err != nil { 
return nil , fmt . Errorf ( "Projects.Roles.List: %w" , err ) 
} 
for _ , role := range response . Roles { 
fmt . Fprintf ( w , "Listing role: %v\n" , role . Name ) 
} 
return response . Roles , nil 
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
import com.google.cloud.iam.admin.v1.[IAMClient](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).[ListRolesPagedResponse](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.ListRolesPagedResponse.html) ; 
import com.google.iam.admin.v1.[ListRolesRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListRolesRequest.html) ; 
import java.io.IOException ; 

/** List roles in a project. */ 
public class ListRoles { 

public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variable before running the sample. 
String projectId = "your-project-id" ; 

listRoles ( projectId ); 
} 

public static void listRoles ( String projectId ) throws IOException { 
[ ListRolesRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListRolesRequest.html) listRolesRequest = 
[ ListRolesRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListRolesRequest.html) . newBuilder (). setParent ( "projects/" + projectId ). build (); 

// Initialize client for sending requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
[ ListRolesPagedResponse ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.ListRolesPagedResponse.html) listRolesResponse = iamClient . listRoles ( listRolesRequest ); 
listRolesResponse . iterateAll (). forEach ( role - > System . out . println ( role )); 
} 
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
from google.cloud.iam_admin_v1 import [ IAMClient ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html) , [ ListRolesRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesRequest.html) , [ RoleView ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.RoleView.html)
from google.cloud.iam_admin_v1.services.iam.pagers import [ ListRolesPager ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListRolesPager.html)

def list_roles ( 
project_id : str , show_deleted : bool = True , role_view : RoleView = [ RoleView ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.RoleView.html) . BASIC 
) - > ListRolesPager : 
"""Lists IAM roles in a GCP project. 

Args: 
project_id: GCP project ID 
show_deleted: Whether to include deleted roles in the results 
role_view: Level of detail for the returned roles (e.g., BASIC or FULL) 

Returns: A pager for traversing through the roles 
""" 

client = IAMClient () 
parent = f "projects/ { project_id } " 
request = ListRolesRequest ( parent = parent , show_deleted = show_deleted , view = role_view ) 
roles = client . [ list_roles ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_list_roles) ( request ) 
for page in roles . pages : 
for role in page . roles : 
print ( role ) 
print ( "Listed all iam roles" ) 
return roles 
```










































The 
`[roles.list](/iam/docs/reference/rest/v1/projects.roles/list)`

method lists all of the custom roles in a project or organization.














Before using any of the request data,
make the following replacements:


- ` RESOURCE_TYPE `: The resource type whose
custom roles you want to manage. Use the value `projects` or `organizations`.


- ` RESOURCE_ID `: The project ID or
organization ID whose custom roles you want to manage. Project IDs are alphanumeric strings, like
`my-project`. Organization IDs are numeric, like `123456789012`.

- ` ROLE_VIEW `: Optional. The information to include for the returned
roles. To include the roles' permissions, set this field to `FULL`. To exclude the
roles' permissions, set this field to `BASIC`. The default value is `BASIC`.


- ` PAGE_SIZE `: Optional. The number of roles to include in the
response. The default value is 300, and the maximum value is 1,000. If the number of roles
is greater than the page size, the response contains a pagination token that you can use to
retrieve the next page of results.

- ` NEXT_PAGE_TOKEN `: Optional. The pagination token returned in an earlier
response from this method. If specified, the list of roles will start where the previous
request ended.

HTTP method and URL:



```
GET https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles?view= ROLE_VIEW &pageSize= PAGE_SIZE &pageToken= NEXT_PAGE_TOKEN 
```



To send your request, expand one of these options:


#### curl (Linux, macOS, or Cloud Shell)













Execute the following command:


































```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles?view= ROLE_VIEW &pageSize= PAGE_SIZE &pageToken= NEXT_PAGE_TOKEN "
```




#### PowerShell (Windows)













Execute the following command:




















































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method GET `
-Headers $headers `
-Uri "https://iam.googleapis.com/v1/ RESOURCE_TYPE / RESOURCE_ID /roles?view= ROLE_VIEW &pageSize= PAGE_SIZE &pageToken= NEXT_PAGE_TOKEN " | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Open the

[method reference page](/iam/docs/reference/rest/v1/projects.roles/list).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Complete any required fields and click Execute**.







You should receive a JSON response similar to the following:






```
{
"roles": [
{
"name": "projects/my-project/roles/customRole1",
"title": "First Custom Role",
"description": "Created on: 2020-06-01",
"etag": "BwWiPg2fmDE="
},
{
"name": "projects/my-project/roles/customRole2",
"title": "Second Custom Role",
"description": "Created on: 2020-06-07",
"etag": "BwWiuX53Wi0="
}
]
}
```

























## Delete a custom role

You can delete any custom role in your project or organization.















[Console](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
**More 










- 

In the Google Cloud Dedicated console, go to the **Custom** tab of the **Roles**
page.

[
Go to the Roles page](https://console.cloud.berlin-build0.goog/iam-admin/roles/custom)

- 

Using the drop-down list at the top of the page, select the project or
organization that contains the role that you want to delete.

- 

Select the checkbox for the roles you want to delete and click
*delete* **Delete**.









































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


Use the `[gcloud iam roles delete](/sdk/gcloud/reference/iam/roles/delete)`
command to delete a custom role:




- 


To delete an organization-level custom role, execute the following command:


```
gcloud iam roles delete ROLE_ID --organization= ORGANIZATION_ID 
```



- 


To delete a project-level custom role, execute the following command:


```
gcloud iam roles delete ROLE_ID --project= PROJECT_ID 
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role, such as `myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization, such as
`123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as `my-project`.






The role will not be included in `gcloud iam roles list`, unless the
`--show-deleted` flag is included. Deleted roles are indicated by the
`deleted: true` block in a `list` response, such as:


```
---
deleted: true
description: My custom role description.
etag: BwVkB5NLIQw=
name: projects/my-project/roles/myCompanyAdmin
title: My Company Admin
---
```























































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
[]( std :: string const & name ) { 
iam :: IAMClient client ( iam :: MakeIAMConnection ()); 
google :: iam :: admin :: v1 :: DeleteRoleRequest request ; 
request . set_name ( name ); 
auto response = client . DeleteRole ( request ); 
if ( ! response ) throw std :: move ( response ). status (); 
std :: cout "Role successfully deleted: " response - > DebugString () 
" \n " ; 
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

public partial class CustomRoles 
{ 
public static void DeleteRole ( string name , string projectId ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 
var service = new IamService ( new IamService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

service . Projects . Roles . Delete ( 
$"projects/{projectId}/roles/{name}" ). Execute (); 
Console . WriteLine ( "Deleted role: " + name ); 
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

// deleteRole deletes a custom role. 
func deleteRole ( w io . Writer , projectID , name string ) error { 
ctx := context . Background () 
service , err := iam . NewService ( ctx ) 
if err != nil { 
return fmt . Errorf ( "iam.NewService: %w" , err ) 
} 

_ , err = service . Projects . Roles . Delete ( "projects/" + projectID + "/roles/" + name ). Do () 
if err != nil { 
return fmt . Errorf ( "Projects.Roles.Delete: %w" , err ) 
} 
fmt . Fprintf ( w , "Deleted role: %v" , name ) 
return nil 
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
import com.google.iam.admin.v1.[DeleteRoleRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.DeleteRoleRequest.html) ; 
import java.io.IOException ; 

/** Delete role. */ 
public class DeleteRole { 

public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
// Role ID must point to an existing role. 
String projectId = "your-project-id" ; 
String roleId = "a unique identifier (e.g. testViewer)" ; 

deleteRole ( projectId , roleId ); 
} 

public static void deleteRole ( String projectId , String roleId ) throws IOException { 
String roleName = "projects/" + projectId + "/roles/" + roleId ; 
[ DeleteRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.DeleteRoleRequest.html) deleteRoleRequest = [ DeleteRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.DeleteRoleRequest.html) . newBuilder (). setName ( roleName ). build (); 

// Initialize client for sending requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
iamClient . deleteRole ( deleteRoleRequest ); 
System . out . println ( "Role deleted." ); 
} 
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
from google.api_core.exceptions import FailedPrecondition , NotFound 
from google.cloud.iam_admin_v1 import ( 
[ DeleteRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteRoleRequest.html) , 
[ IAMClient ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html) , 
[ Role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html) , 
[ UndeleteRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteRoleRequest.html) , 
) 
def delete_role ( project_id : str , role_id : str ) - > Role : 
"""Deletes iam role in GCP project. Can be undeleted later. 
Args: 
project_id: GCP project id 
role_id: id of GCP iam role 

Returns: google.cloud.iam_admin_v1.Role object 
""" 
client = IAMClient () 
name = f "projects/ { project_id } /roles/ { role_id } " 
request = DeleteRoleRequest ( name = name ) 
try : 
role = client . [ delete_role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_delete_role) ( request ) 
print ( f "Deleted role: { role_id } : { role } " ) 
return role 
except NotFound : 
print ( f "Role with id [ { role_id } ] not found, take some actions" ) 
except FailedPrecondition as err : 
print ( f "Role with id [ { role_id } ] already deleted, take some actions)" , err ) 
```










































The 
`[roles.delete](/iam/docs/reference/rest/v1/projects.roles/delete)`

method deletes a custom role in a project or organization.










Before using any of the request data,
make the following replacements:


- ` ROLE_NAME `: The full role name, including any
`organizations/`, `projects/`, or `roles/` prefixes. For example,
`organizations/123456789012/roles/myCompanyAdmin`.

HTTP method and URL:



```
DELETE https://iam.googleapis.com/v1/ ROLE_NAME 
```



To send your request, expand one of these options:


#### curl (Linux, macOS, or Cloud Shell)













Execute the following command:


































```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://iam.googleapis.com/v1/ ROLE_NAME "
```




#### PowerShell (Windows)













Execute the following command:




















































```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
-Method DELETE `
-Headers $headers `
-Uri "https://iam.googleapis.com/v1/ ROLE_NAME " | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Open the

[method reference page](/iam/docs/reference/rest/v1/projects.roles/delete).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Complete any required fields and click Execute**.





The response contains the definition of the role that was deleted.




```
{
"name": "projects/my-project/roles/myCompanyAdmin",
"title": "My Company Admin",
"description": "My custom role description.",
"includedPermissions": [
"iam.roles.get",
"iam.roles.list"
],
"etag": "BwWiPg2fmDE=",
**"deleted": true**
}
```























When a role is deleted, any role bindings that refer to the role remain in your
allow policies, but they have no effect. You can undelete a role within
7 days. During this 7-day
period, the Google Cloud Dedicated console shows that the role was deleted. You can also
list deleted roles programmatically, but they are omitted by default.

The role is scheduled for permanent deletion 7 to
14 days after the initial request to delete the role.
At this point, the role no longer counts towards the limit of
300 custom roles per organization or
300 custom roles per project.

After the role is scheduled for permanent deletion, Google Cloud Dedicated initiates
the process to permanently delete the role. This process takes
30 days. During this 30-day
window, the role and all associated bindings are permanently removed, and you
cannot create a new role with the same role ID.

After the role has been permanently deleted, up to 44
days after the initial deletion request, you can create a new role using the
same role ID.



## Undelete a custom role

Undeleting a role returns it to its previous state.

Roles can only be undeleted within 7 days. After
7 days, Google Cloud Dedicated initiates the process to
permanently delete the role. This permanent deletion process can take up to
30 days. After a role is permanently deleted, all role
bindings that refer to the role are removed, and you can create a new role using
the same role ID.















[Console](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
**More 










- 

In the Google Cloud Dedicated console, go to the **Custom** tab of the **Roles**
page.

[
Go to the Roles page](https://console.cloud.berlin-build0.goog/iam-admin/roles/custom)

- 

Using the drop-down list at the top of the page, select the project or
organization that contains the role that you want to undelete.

- 

Select the checkbox for the roles that you want to undelete, then click
**Undelete**.









































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


Use the `[gcloud iam roles undelete](/sdk/gcloud/reference/iam/roles/delete)`
command to undelete a custom role:




- 


To undelete an organization-level custom role, execute the following command:


```
gcloud iam roles undelete ROLE_ID --organization= ORGANIZATION_ID 
```



- 


To undelete a project-level custom role, execute the following command:


```
gcloud iam roles undelete ROLE_ID --project= PROJECT_ID 
```






Each placeholder value is described below:




- 


` ROLE_ID ` is the name of the role, such as `myCompanyAdmin`.



- 


` ORGANIZATION_ID ` is the numeric ID of the organization, such as
`123456789012`.



- 


` PROJECT_ID ` is the name of the project, such as `my-project`.






Examples**



The following example demonstrates how to undelete an organization-level custom role:


```
gcloud iam roles undelete myCompanyAdmin --organization=123456789012
```



If the role was undeleted successfully, the command's output is similar to the following:


```
description : My custom role description. 
etag : BwVkCAx9W6w= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
name : organizations/123456789012/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```



The following example demonstrates how to undelete a project-level custom role:


```
gcloud iam roles undelete myCompanyAdmin --project=my-project
```



If the role was undeleted successfully, the command's output is similar to the following:


```
description : My custom role description. 
etag : BwVkCAx9W6w= 
includedPermissions : 
- iam.roles.get 
- iam.roles.list 
name : projects/my-project/roles/myCompanyAdmin 
stage : ALPHA 
title : My Company Admin 
```























































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
[]( std :: string const & name ) { 
iam :: IAMClient client ( iam :: MakeIAMConnection ()); 
google :: iam :: admin :: v1 :: UndeleteRoleRequest request ; 
request . set_name ( name ); 
auto response = client . UndeleteRole ( request ); 
if ( ! response ) throw std :: move ( response ). status (); 
std :: cout "Role successfully undeleted: " response - > DebugString () 
" \n " ; 
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

public partial class CustomRoles 
{ 
public static Role UndeleteRole ( string name , string projectId ) 
{ 
var credential = [ GoogleCredential ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://berlin.devsitetest.how/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 
var service = new IamService ( new IamService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

string resource = $"projects/{projectId}/roles/{name}" ; 
var role = service . Projects . Roles . Undelete ( 
new UndeleteRoleRequest (), resource ). Execute (); 
Console . WriteLine ( "Undeleted role: " + role . Name ); 
return role ; 
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

// undeleteRole restores a deleted custom role. 
func undeleteRole ( w io . Writer , projectID , name string ) ( * iam . Role , error ) { 
ctx := context . Background () 
service , err := iam . NewService ( ctx ) 
if err != nil { 
return nil , fmt . Errorf ( "iam.NewService: %w" , err ) 
} 

resource := "projects/" + projectID + "/roles/" + name 
request := & iam . UndeleteRoleRequest {} 
role , err := service . Projects . Roles . Undelete ( resource , request ). Do () 
if err != nil { 
return nil , fmt . Errorf ( "Projects.Roles.Undelete: %w" , err ) 
} 
fmt . Fprintf ( w , "Undeleted role: %v" , role . Name ) 
return role , nil 
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
import com.google.iam.admin.v1.[Role](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) ; 
import com.google.iam.admin.v1.[UndeleteRoleRequest](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UndeleteRoleRequest.html) ; 
import java.io.IOException ; 

/** 
* Undelete a role to return it to its previous state. Undeleting only works on roles that were 
* deleted in the past 7 days. 
*/ 
public class UndeleteRole { 

public static void main ( String [] args ) throws IOException { 
// TODO(developer): Replace the variables before running the sample. 
// Role ID must point to a role that was deleted in the past 7 days. 
String projectId = "your-project-id" ; 
String roleId = "a unique identifier (e.g. testViewer)" ; 

undeleteRole ( projectId , roleId ); 
} 

public static void undeleteRole ( String projectId , String roleId ) throws IOException { 
String roleName = "projects/" + projectId + "/roles/" + roleId ; 
[ UndeleteRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UndeleteRoleRequest.html) undeleteRoleRequest = 
[ UndeleteRoleRequest ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UndeleteRoleRequest.html) . newBuilder (). setName ( roleName ). build (); 

// Initialize client for sending requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 
[ Role ](https://berlin.devsitetest.how/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) result = iamClient . undeleteRole ( undeleteRoleRequest ); 
System . out . println ( "Undeleted role:\n" + result ); 
} 
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
from google.api_core.exceptions import FailedPrecondition , NotFound 
from google.cloud.iam_admin_v1 import ( 
[ DeleteRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteRoleRequest.html) , 
[ IAMClient ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html) , 
[ Role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html) , 
[ UndeleteRoleRequest ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteRoleRequest.html) , 
) 
def undelete_role ( project_id : str , role_id : str ) - > Role : 
"""Undeleted deleted iam role in GCP project. 

Args: 
project_id: GCP project id 
role_id: id of GCP iam role 
""" 
client = IAMClient () 
name = f "projects/ { project_id } /roles/ { role_id } " 
request = UndeleteRoleRequest ( name = name ) 
try : 
role = client . [ undelete_role ](https://berlin.devsitetest.how/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_undelete_role) ( request ) 
print ( f "Undeleted role: { role_id } : { role } " ) 
return role 
except NotFound : 
print ( f "Role with id [ { role_id } ] not found, take some actions" ) 
except FailedPrecondition as err : 
print ( f "Role with id [ { role_id } ] is not deleted, take some actions)" , err ) 
```










































The 
`[roles.undelete](/iam/docs/reference/rest/v1/projects.roles/undelete)`

method undeletes a custom role in a project or organization.












Before using any of the request data,
make the following replacements:


- ` ROLE_NAME `: The full role name, including any
`organizations/`, `projects/`, or `roles/` prefixes. For example,
`organizations/123456789012/roles/myCompanyAdmin`.


- ` ETAG `: An identifier for a version of the role.
Include this field to prevent overwriting other role changes.

HTTP method and URL:



```
POST https://iam.googleapis.com/v1/ ** ROLE_NAME :undelete
```



Request JSON body:



```
{
"etag": " ETAG "
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
"https://iam.googleapis.com/v1/ ROLE_NAME :undelete"
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
-Uri "https://iam.googleapis.com/v1/ ROLE_NAME :undelete" | Select-Object -Expand Content
```




#### APIs Explorer (browser)






Copy the request body and open the

[method reference page](/iam/docs/reference/rest/v1/projects.roles/undelete).
The APIs Explorer panel opens on the right side of the page.
You can interact with this tool to send requests.

Paste the request body in this tool, complete any other required fields, and click Execute**.





The response contains the definition of the role that was undeleted.




```
{
"name": "projects/my-project/roles/myCompanyAdmin",
"title": "My Company Admin",
"description": "My custom role description.",
"includedPermissions": [
"iam.roles.get",
"iam.roles.list"
],
"etag": "BwWiPg2fmDE="
}
```























## What's next

- Find out how to [grant roles to principals](/iam/docs/granting-changing-revoking-access).

- Learn about [conditional role bindings](/iam/docs/conditions-overview), which grant a role only if
specific conditions are met.