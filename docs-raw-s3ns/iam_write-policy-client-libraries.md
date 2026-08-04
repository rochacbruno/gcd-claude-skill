# Quickstart: Write an allow policy by using client libraries

Source: https://documentation.s3ns.fr/iam/docs/write-policy-client-libraries

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

IAM

](https://documentation.s3ns.fr/iam/docs)






- 








[

Guides

](https://documentation.s3ns.fr/iam/docs/overview)

















- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Create a Cloud de Confiance project ](#create-project)

- [ Install the client library ](#install_the_client_library)
- [ Read, modify, and write an allow policy ](#using_the_client_library)
- [ How did it go? ](#how-did-it-go)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Grant roles using client libraries 




Learn how to get started with the IAM methods from
the Resource Manager API in your favorite programming language.





## Before you begin 



### Create a Cloud de Confiance project 

For this quickstart, you need a new Cloud de Confiance project.

















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).







- 


To [initialize](/sdk/docs/initializing) the gcloud CLI, run the following command:



```
gcloud init
```
























- 




[Create or select a Cloud de Confiance project](https://documentation.s3ns.fr/resource-manager/docs/creating-managing-projects).




Roles required to select or create a project**





- 
**Select a project**: Selecting a project doesn't require a specific
IAM role—you can select any project that you've been
granted a role on.


- 
**Create a project**: To create a project, you need the Project Creator role
(`roles/resourcemanager.projectCreator`), which contains the
`resourcemanager.projects.create` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).













- 


Create a Cloud de Confiance project:


```
gcloud projects create ** PROJECT_ID 
```



Replace ` PROJECT_ID ` with a name for the Cloud de Confiance project you are creating.



- 


Select the Cloud de Confiance project that you created:


```
gcloud config set project PROJECT_ID 
```



Replace ` PROJECT_ID ` with your Cloud de Confiance project name.















- 



Enable the Resource Manager API:





Roles required to enable APIs**


To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).


```
gcloud services enable cloudresourcemanager.googleapis.com
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















- 



Grant roles to your user account. Run the following command once for each of the following
IAM roles:
`roles/resourcemanager.projectIamAdmin`




```
gcloud projects add-iam-policy-binding PROJECT_ID --member = "user: USER_IDENTIFIER " --role = ROLE 
```



Replace the following:




- ` PROJECT_ID `: Your project ID.


- ` USER_IDENTIFIER `: The identifier for your user

account. For examples, see
[
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users).



- ` ROLE `: The IAM role that you grant to your user account.




















## Install the client library

















[ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) 
More 










For more on setting up your C# development environment, refer to the [C# Development Environment Setup Guide](/dotnet/docs/setup).







```
install-package Google.Apis.Iam.v1
install-package Google.Apis.CloudResourceManager.v1
```








































```
go get golang.org/x/oauth2/google
go get google.golang.org/api/cloudresourcemanager/v1
```








































For more on setting up your Java development environment, refer to the [Java Development Environment Setup Guide](/java/docs/setup).






If you are using [Maven](https://maven.apache.org/), add this to your `pom.xml`
file.






















```
dependency >
groupId>com . google . apis / groupId >
artifactId>google - api - services - cloudresourcemanager / artifactId >
version>v3 - rev20240128 - 2.0.0 / version >
/ dependency >
dependency >
groupId>com . google . auth / groupId >
artifactId>google - auth - library - oauth2 - http / artifactId >
/ dependency >
dependency >
groupId>com . google . http - client / groupId >
artifactId>google - http - client - jackson2 / artifactId >
/ dependency >
dependency >
groupId>com . google . apis / groupId >
artifactId>google - api - services - iam / artifactId >
version>v1 - rev20240118 - 2.0.0 / version >
/ dependency >
```













































For more on setting up your Python development environment, refer to the [Python Development Environment Setup Guide](/python/docs/setup).







```
pip install --upgrade google-api-python-client google-auth google-auth-httplib2
```























## Read, modify, and write an allow policy

The code snippet in this quickstart does the following:

- Initializes the Resource Manager service, which manages Cloud de Confiance
projects.

- Reads the [allow policy](/iam/docs/overview#cloud-iam-policy) for your
project.

- Modifies the allow policy by granting the Log Writer role
(`roles/logging.logWriter`) to your Google Account.

- Writes the updated allow policy.

- Prints all the principals that have the Log Writer role
(`roles/logging.logWriter`) at the project level.

- Revokes the Log Writer role.

Replace the following values before running the code snippet:

- ` your-project `: The ID of your project.

- ` your-member `: The email address for your
user account. For example,
`principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com`.




















[ C# ](#c) [ Go ](#go) [ Java ](#java) [ Python ](#python) 
More 












To learn how to install and use the client library for Resource Manager, see
[Resource Manager client libraries](/iam/docs/reference/libraries).



For more information, see the
[Resource Manager C# API
reference documentation](https://googleapis.dev/dotnet/Google.Apis.CloudResourceManager.v1/latest/api/Google.Apis.CloudResourceManager.v1.html).





To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.



























```
using [ Google.Apis.Auth.OAuth2 ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html) ; 
using Google.Apis.CloudResourceManager.v1 ; 
using Google.Apis.CloudResourceManager.v1.Data ; 
using Google.Apis.Iam.v1 ; 
using System ; 
using System.Collections.Generic ; 
using System.Linq ; 

public class QuickStart 
{ 
public static void Main ( string [] args ) 
{ 
// TODO: Replace with your project ID 
var projectId = "your-project" ; 
// TODO: Replace with the ID of your principal. 
// For examples, see https://cloud.google.com/iam/docs/principal-identifiers 
var member = "your-principal" ; 
// Role to be granted 
var role = "roles/logging.logWriter" ; 

// Initialize service 
CloudResourceManagerService crmService = InitializeService (); 

// Grant your principal the "Log Writer" role for your project 
AddBinding ( crmService , projectId , member , role ); 

// Get the project's policy and print all principals with the the "Log Writer" role 
var policy = GetPolicy ( crmService , projectId ); 
var binding = policy . Bindings . FirstOrDefault ( x = > x . Role == role ); 
Console . WriteLine ( "Role: " + binding . Role ); 
Console . Write ( "Members: " ); 
foreach ( var m in binding . Members ) 
{ 
Console . Write ( "[" + m + "] " ); 
} 
Console . WriteLine (); 

// Remove principal from the "Log Writer" role 
RemoveMember ( crmService , projectId , member , role ); 
} 

public static CloudResourceManagerService InitializeService () 
{ 
// Get credentials 
var credential = [ GoogleCredential ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) . [ GetApplicationDefault ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault) () 
. [ CreateScoped ](https://documentation.s3ns.fr/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__) ( IamService . Scope . CloudPlatform ); 

// Create the Cloud Resource Manager service object 
CloudResourceManagerService crmService = new CloudResourceManagerService ( 
new CloudResourceManagerService . Initializer 
{ 
HttpClientInitializer = credential 
}); 

return crmService ; 
} 

public static Policy GetPolicy ( CloudResourceManagerService crmService , String projectId ) 
{ 
// Get the project's policy by calling the 
// Cloud Resource Manager Projects API 
var policy = crmService . Projects . GetIamPolicy ( 
new GetIamPolicyRequest (), 
projectId ). Execute (); 
return policy ; 
} 

public static void SetPolicy ( CloudResourceManagerService crmService , String projectId , Policy policy ) 
{ 
// Set the project's policy by calling the 
// Cloud Resource Manager Projects API 
crmService . Projects . SetIamPolicy ( 
new SetIamPolicyRequest 
{ 
Policy = policy 
}, projectId ). Execute (); 
} 

public static void AddBinding ( 
CloudResourceManagerService crmService , 
string projectId , 
string member , 
string role ) 
{ 
// Get the project's policy 
var policy = GetPolicy ( crmService , projectId ); 

// Find binding in policy 
var binding = policy . Bindings . FirstOrDefault ( x = > x . Role == role ); 

// If binding already exists, add principal to binding 
if ( binding != null ) 
{ 
binding . Members . Add ( member ); 
} 
// If binding does not exist, add binding to policy 
else 
{ 
binding = new Binding 
{ 
Role = role , 
Members = new List { member } 
}; 
policy . Bindings . Add ( binding ); 
} 

// Set the updated policy 
SetPolicy ( crmService , projectId , policy ); 
} 

public static void RemoveMember ( 
CloudResourceManagerService crmService , 
string projectId , 
string member , 
string role ) 
{ 
// Get the project's policy 
var policy = GetPolicy ( crmService , projectId ); 

// Remove the principal from the role 
var binding = policy . Bindings . FirstOrDefault ( x = > x . Role == role ); 
if ( binding == null ) 
{ 
Console . WriteLine ( "Role does not exist in policy." ); 
} 
else 
{ 
if ( binding . Members . Contains ( member )) 
{ 
binding . Members . Remove ( member ); 
} 
else 
{ 
Console . WriteLine ( "The member has not been granted this role." ); 
} 

if ( binding . Members . Count == 0 ) 
{ 
policy . Bindings . Remove ( binding ); 
} 
} 

// Set the updated policy 
SetPolicy ( crmService , projectId , policy ); 
} 
} 
```















































To learn how to install and use the client library for Resource Manager, see
[Resource Manager client libraries](/iam/docs/reference/libraries).



For more information, see the
[Resource Manager Go API
reference documentation](https://godoc.org/google.golang.org/api/cloudresourcemanager/v1).





To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.



























```
package main 

import ( 
"context" 
"flag" 
"fmt" 
"log" 
"strings" 
"time" 

"google.golang.org/api/cloudresourcemanager/v1" 
) 

func main () { 
// TODO: Add your project ID 
projectID := flag . String ( "project_id" , "" , "Cloud Project ID" ) 
// TODO: Add the ID of your principal. 
// For examples, see https://cloud.google.com/iam/docs/principal-identifiers 
member := flag . String ( "member_id" , "" , "Your principal ID" ) 
flag . Parse () 

// The role to be granted 
var role string = "roles/logging.logWriter" 

// Initializes the Cloud Resource Manager service 
ctx := context . Background () 
crmService , err := cloudresourcemanager . NewService ( ctx ) 
if err != nil { 
log . Fatalf ( "cloudresourcemanager.NewService: %v" , err ) 
} 

// Grants your principal the "Log writer" role for your project 
addBinding ( crmService , * projectID , * member , role ) 

// Gets the project's policy and prints all principals with the "Log Writer" role 
policy := getPolicy ( crmService , * projectID ) 
// Find the policy binding for role. Only one binding can have the role. 
var binding * cloudresourcemanager . Binding 
for _ , b := range policy . Bindings { 
if b . Role == role { 
binding = b 
break 
} 
} 
fmt . Println ( "Role: " , binding . Role ) 
fmt . Print ( "Members: " , strings . Join ( binding . Members , ", " )) 

// Removes member from the "Log writer" role 
removeMember ( crmService , * projectID , * member , role ) 

} 

// addBinding adds the principal to the project's IAM policy 
func addBinding ( crmService * cloudresourcemanager . Service , projectID , member , role string ) { 

policy := getPolicy ( crmService , projectID ) 

// Find the policy binding for role. Only one binding can have the role. 
var binding * cloudresourcemanager . Binding 
for _ , b := range policy . Bindings { 
if b . Role == role { 
binding = b 
break 
} 
} 

if binding != nil { 
// If the binding exists, adds the principal to the binding 
binding . Members = append ( binding . Members , member ) 
} else { 
// If the binding does not exist, adds a new binding to the policy 
binding = & cloudresourcemanager . Binding { 
Role : role , 
Members : [] string { member }, 
} 
policy . Bindings = append ( policy . Bindings , binding ) 
} 

setPolicy ( crmService , projectID , policy ) 

} 

// removeMember removes the principal from the project's IAM policy 
func removeMember ( crmService * cloudresourcemanager . Service , projectID , member , role string ) { 

policy := getPolicy ( crmService , projectID ) 

// Find the policy binding for role. Only one binding can have the role. 
var binding * cloudresourcemanager . Binding 
var bindingIndex int 
for i , b := range policy . Bindings { 
if b . Role == role { 
binding = b 
bindingIndex = i 
break 
} 
} 

// Order doesn't matter for bindings or members, so to remove, move the last item 
// into the removed spot and shrink the slice. 
if len ( binding . Members ) == 1 { 
// If the principal is the only member in the binding, removes the binding 
last := len ( policy . Bindings ) - 1 
policy . Bindings [ bindingIndex ] = policy . Bindings [ last ] 
policy . Bindings = policy . Bindings [: last ] 
} else { 
// If there is more than one member in the binding, removes the principal 
var memberIndex int 
for i , mm := range binding . Members { 
if mm == member { 
memberIndex = i 
} 
} 
last := len ( policy . Bindings [ bindingIndex ]. Members ) - 1 
binding . Members [ memberIndex ] = binding . Members [ last ] 
binding . Members = binding . Members [: last ] 
} 

setPolicy ( crmService , projectID , policy ) 

} 

// getPolicy gets the project's IAM policy 
func getPolicy ( crmService * cloudresourcemanager . Service , projectID string ) * cloudresourcemanager . Policy { 

ctx := context . Background () 

ctx , cancel := context . WithTimeout ( ctx , time . Second * 10 ) 
defer cancel () 
request := new ( cloudresourcemanager . GetIamPolicyRequest ) 
policy , err := crmService . Projects . GetIamPolicy ( projectID , request ). Do () 
if err != nil { 
log . Fatalf ( "Projects.GetIamPolicy: %v" , err ) 
} 

return policy 
} 

// setPolicy sets the project's IAM policy 
func setPolicy ( crmService * cloudresourcemanager . Service , projectID string , policy * cloudresourcemanager . Policy ) { 

ctx := context . Background () 

ctx , cancel := context . WithTimeout ( ctx , time . Second * 10 ) 
defer cancel () 
request := new ( cloudresourcemanager . SetIamPolicyRequest ) 
request . Policy = policy 
policy , err := crmService . Projects . SetIamPolicy ( projectID , request ). Do () 
if err != nil { 
log . Fatalf ( "Projects.SetIamPolicy: %v" , err ) 
} 
} 
```














































To learn how to install and use the client library for Resource Manager, see
[Resource Manager client libraries](/iam/docs/reference/libraries).



For more information, see the
[Resource Manager Java API
reference documentation](https://documentation.s3ns.fr/java/docs/reference/google-cloud-resourcemanager/latest/overview).





To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.



























```
import com.google.cloud.iam.admin.v1.[IAMClient](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) ; 
import com.google.iam.admin.v1.[ServiceAccountName](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html) ; 
import com.google.iam.v1.[Binding](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) ; 
import com.google.iam.v1.[GetIamPolicyRequest](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) ; 
import com.google.iam.v1.[Policy](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) ; 
import com.google.iam.v1.[SetIamPolicyRequest](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) ; 
import com.google.protobuf.[FieldMask](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 
import java.util.ArrayList ; 
import java.util.Arrays ; 
import java.util.List ; 

public class Quickstart { 

public static void main ( String [] args ) throws IOException { 
// TODO: Replace with your project ID. 
String projectId = "your-project" ; 
// TODO: Replace with your service account name. 
String serviceAccount = "your-service-account" ; 
// TODO: Replace with the ID of your principal. 
// For examples, see https://cloud.google.com/iam/docs/principal-identifiers 
String member = "your-principal" ; 
// The role to be granted. 
String role = "roles/logging.logWriter" ; 

quickstart ( projectId , serviceAccount , member , role ); 
} 

// Creates new policy and adds binding. 
// Checks if changes are present and removes policy. 
public static void quickstart ( String projectId , String serviceAccount , 
String member , String role ) throws IOException { 

// Construct the service account email. 
// You can modify the ".iam.gserviceaccount.com" to match the name of the service account 
// to use for authentication. 
serviceAccount = serviceAccount + "@" + projectId + ".iam.gserviceaccount.com" ; 

// Initialize client that will be used to send requests. 
// This client only needs to be created once, and can be reused for multiple requests. 
try ( [ IAMClient ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [ IAMClient ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) . create ()) { 

// Grants your principal the "Log writer" role for your project. 
addBinding ( iamClient , projectId , serviceAccount , member , role ); 

// Get the project's policy and print all principals with the "Log Writer" role 
[ Policy ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = getPolicy ( iamClient , projectId , serviceAccount ); 

[ Binding ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null ; 
List bindings = policy . [ getBindingsList ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__) (); 

for ( [ Binding ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : bindings ) { 
if ( b . getRole (). equals ( role )) { 
binding = b ; 
break ; 
} 
} 

System . out . println ( "Role: " + binding . [ getRole ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getRole__) ()); 
System . out . print ( "Principals: " ); 

for ( String m : binding . [ getMembersList ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__) ()) { 
System . out . print ( "[" + m + "] " ); 
} 
System . out . println (); 

// Removes principal from the "Log writer" role. 
removeMember ( iamClient , projectId , serviceAccount , member , role ); 
} 
} 

public static void addBinding ( [ IAMClient ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient , String projectId , String serviceAccount , 
String member , String role ) { 
// Gets the project's policy. 
[ Policy ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = getPolicy ( iamClient , projectId , serviceAccount ); 

// If policy is not retrieved, return early. 
if ( policy == null ) { 
return ; 
} 

[ Policy ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . Builder updatedPolicy = policy . [ toBuilder ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__) (); 

// Get the binding if present in the policy. 
[ Binding ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null ; 
for ( [ Binding ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : updatedPolicy . getBindingsList ()) { 
if ( b . getRole (). equals ( role )) { 
binding = b ; 
break ; 
} 
} 

if ( binding != null ) { 
// If binding already exists, adds principal to binding. 
binding . [ getMembersList ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__) (). add ( member ); 
} else { 
// If binding does not exist, adds binding to policy. 
binding = [ Binding ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) . newBuilder () 
. setRole ( role ) 
. [ addMembers ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_) ( member ) 
. build (); 
updatedPolicy . [ addBindings ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_) ( binding ); 
} 

// Sets the updated policy. 
setPolicy ( iamClient , projectId , serviceAccount , updatedPolicy . build ()); 
} 

public static void removeMember ( [ IAMClient ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient , String projectId , String serviceAccount , 
String member , String role ) { 
// Gets the project's policy. 
[ Policy ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) . Builder policy = getPolicy ( iamClient , projectId , serviceAccount ). toBuilder (); 

// Removes the principal from the role. 
[ Binding ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null ; 
for ( [ Binding ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : policy . [ getBindingsList ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__) ()) { 
if ( b . getRole (). equals ( role )) { 
binding = b ; 
break ; 
} 
} 

if ( binding != null && binding . [ getMembersList ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__) (). contains ( member )) { 
List newMemberList = new ArrayList <> ( binding . [ getMembersList ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__) ()); 
newMemberList . remove ( member ); 

[ Binding ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) newBinding = binding . [ toBuilder ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_toBuilder__) (). [ clearMembers ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_clearMembers__) () 
. [ addAllMembers ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addAllMembers_java_lang_Iterable_java_lang_String__) ( newMemberList ) 
. build (); 
List newBindingList = new ArrayList <> ( policy . [ getBindingsList ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__) ()); 
newBindingList . remove ( binding ); 

if ( ! newBinding . [ getMembersList ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__) (). isEmpty ()) { 
newBindingList . add ( newBinding ); 
} 

policy . [ clearBindings ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__) () 
. [ addAllBindings ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__) ( newBindingList ); 
} 

// Sets the updated policy. 
setPolicy ( iamClient , projectId , serviceAccount , policy . build ()); 
} 

public static [ Policy ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getPolicy ( [ IAMClient ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient , String projectId , String serviceAccount ) { 
// Gets the project's policy by calling the 
// IAMClient API. 
[ GetIamPolicyRequest ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [ GetIamPolicyRequest ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) . newBuilder () 
. setResource ( [ ServiceAccountName ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html) . of ( projectId , serviceAccount ). toString ()) 
. build (); 
return iamClient . [ getIamPolicy ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html#com_google_cloud_iam_admin_v1_IAMClient_getIamPolicy_com_google_api_resourcenames_ResourceName_) ( request ); 
} 

private static void setPolicy ( [ IAMClient ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient , String projectId , 
String serviceAccount , [ Policy ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy ) { 
List paths = Arrays . asList ( "bindings" , "etag" ); 
// Sets a project's policy. 
[ SetIamPolicyRequest ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request = [ SetIamPolicyRequest ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) . newBuilder () 
. setResource ( [ ServiceAccountName ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html) . of ( projectId , serviceAccount ). toString ()) 
. [ setPolicy ](https://documentation.s3ns.fr/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_) ( policy ) 
// A FieldMask specifying which fields of the policy to modify. Only 
// the fields in the mask will be modified. If no mask is provided, the 
// following default mask is used: 
// `paths: "bindings, etag"` 
. setUpdateMask ( [ FieldMask ](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addAllPaths ](https://documentation.s3ns.fr/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__) ( paths ). build ()) 
. build (); 
iamClient . [ setIamPolicy ](https://documentation.s3ns.fr/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html#com_google_cloud_iam_admin_v1_IAMClient_setIamPolicy_com_google_api_resourcenames_ResourceName_com_google_iam_v1_Policy_) ( request ); 
} 
} 
```


















































To learn how to install and use the client library for Resource Manager, see
[Resource Manager client libraries](/iam/docs/reference/libraries).



For more information, see the
[Resource Manager Python API
reference documentation](https://developers.google.com/resources/api-libraries/documentation/cloudresourcemanager/v1/python/latest/).





To authenticate to Resource Manager, set up Application Default Credentials.
For more information, see

[Set up authentication for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).





Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `s3nsapis.fr`.



























```
from google.cloud import [ resourcemanager_v3 ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest)
from google.iam.v1 import iam_policy_pb2 , policy_pb2 

def quickstart ( project_id : str , principal : str ) - > None : 
"""Demonstrates basic IAM operations. 

This quickstart shows how to get a project's IAM policy, 
add a principal to a role, list members of a role, 
and remove a principal from a role. 

Args: 
project_id: ID or number of the Google Cloud project you want to use. 
principal: The principal ID requesting the access. 
""" 

# Role to be granted. 
role = "roles/logging.logWriter" 
crm_service = [ resourcemanager_v3 ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest) . [ ProjectsClient ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html) () 

# Grants your principal the 'Log Writer' role for the project. 
modify_policy_add_role ( crm_service , project_id , role , principal ) 

# Gets the project's policy and prints all principals with the 'Log Writer' role. 
policy = get_policy ( crm_service , project_id ) 
binding = next ( b for b in policy . bindings if b . role == role ) 
print ( f "Role: { ( binding . role ) } " ) 
print ( "Members: " ) 
for m in binding . members : 
print ( f "[ { m } ]" ) 

# Removes the principal from the 'Log Writer' role. 
modify_policy_remove_principal ( crm_service , project_id , role , principal ) 

def get_policy ( 
crm_service : [ resourcemanager_v3 ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest) . [ ProjectsClient ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html) , project_id : str 
) - > policy_pb2 . Policy : 
"""Gets IAM policy for a project.""" 

request = iam_policy_pb2 . GetIamPolicyRequest () 
request . resource = f "projects/ { project_id } " 

policy = crm_service . [ get_iam_policy ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_get_iam_policy) ( request ) 
return policy 

def set_policy ( 
crm_service : [ resourcemanager_v3 ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest) . [ ProjectsClient ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html) , 
project_id : str , 
policy : policy_pb2 . Policy , 
) - > None : 
"""Adds a new role binding to a policy.""" 

request = iam_policy_pb2 . SetIamPolicyRequest () 
request . resource = f "projects/ { project_id } " 
request . policy . CopyFrom ( policy ) 

crm_service . [ set_iam_policy ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_set_iam_policy) ( request ) 

def modify_policy_add_role ( 
crm_service : [ resourcemanager_v3 ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest) . [ ProjectsClient ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html) , 
project_id : str , 
role : str , 
principal : str , 
) - > None : 
"""Adds a new role binding to a policy.""" 

policy = get_policy ( crm_service , project_id ) 

for bind in policy . bindings : 
if bind . role == role : 
bind . members . append ( principal ) 
break 
else : 
binding = policy_pb2 . Binding () 
binding . role = role 
binding . members . append ( principal ) 
policy . bindings . append ( binding ) 

set_policy ( crm_service , project_id , policy ) 

def modify_policy_remove_principal ( 
crm_service : [ resourcemanager_v3 ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest) . [ ProjectsClient ](https://documentation.s3ns.fr/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html) , 
project_id : str , 
role : str , 
principal : str , 
) - > None : 
"""Removes a principal from a role binding.""" 

policy = get_policy ( crm_service , project_id ) 

for bind in policy . bindings : 
if bind . role == role : 
if principal in bind . members : 
bind . members . remove ( principal ) 
break 

set_policy ( crm_service , project_id , policy ) 

if __name__ == "__main__" : 
# TODO: Replace with your project ID. 
project_id = "your-project-id" 
# TODO: Replace with the ID of your principal. 
# For examples, see https://cloud.google.com/iam/docs/principal-identifiers 
principal = "your-principal" 
quickstart ( project_id , principal ) 
```























Congratulations! You used the IAM methods in the Resource Manager API
to modify access for a project.

## How did it go?




It worked!





I got stuck.










## Clean up










- 



Optional: Revoke the authentication credentials that you created, and delete the local
credential file.



```
gcloud auth application-default revoke
```











- 



Optional: Revoke credentials from the gcloud CLI.



```
gcloud auth revoke
```










## What's next



- Read about [how IAM works](/iam/docs/concepts).

- Learn more about
[granting, changing, and revoking access](/iam/docs/granting-changing-revoking-access).

- Troubleshoot access issues with the [Policy Troubleshooter](/iam/docs/troubleshooting-access).