# Manage API keys

Source: https://berlin.devsitetest.how/docs/authentication/api-keys
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












# Manage API keys 






- On this page 
- [ Introduction to API keys ](#introduction)

- [ Standard API keys ](#standard-api-keys)
- [ Authorization keys ](#api-keys-bound-sa)
- [ API key components ](#components)

- [ Before you begin ](#before_you_begin)

- [ Set up authentication ](#set_up_authentication)
- [ Required roles ](#required_roles)
- [ Enable authorization keys ](#enable-key-binding)

- [ Create an API key ](#create)
- [ Apply API key restrictions ](#api_key_restrictions)

- [ Add API restrictions ](#adding-api-restrictions)
- [ Add application restrictions ](#adding-application-restrictions)
- [ List API keys that don't have restrictions ](#list-no-restriction-keys)

- [ Get project information from a key string ](#get-info)
- [ Create a copy of an API key ](#copy)
- [ Rotate an API key ](#rotate)
- [ Undelete an API key ](#undelete)
- [ Determine the API key type ](#determine_the_api_key_type)
- [ Poll long-running operations ](#lro)
- [ Limits on API keys ](#limits)
- [ What's next ](#whats_next)
- 









This page describes how to create, edit, and restrict API keys. For information
about how to use API keys to access Google APIs, see
[Use API keys to access APIs](/docs/authentication/api-keys-use).

## Introduction to API keys 

There are two types of API keys: standard API keys, and authorization keys. Both
keys let you associate a request with a project for billing and quota purposes.
However, they differ in the following way:

- 

A standard API key doesn't authenticate a principal.

- 

An authorization key authenticates as a service account. It operates in a
similar fashion to a long-lived access token.

The [**Credentials** page](https://console.cloud.berlin-build0.goog/apis/credentials) in the
Google Cloud Dedicated console ensures that the correct type of API key is created for a
selected API.

### Standard API keys

Standard API keys provide a way to associate a request with a project for
billing and quota purposes. When you use a standard API key (an API key that has
not been bound to a service account) to access an API, the API key doesn't
identify a [principal](/docs/authentication#principal). Without a principal, the
request can't use Identity and Access Management (IAM) to check whether the caller is
authorized to perform the requested operation.

Standard API keys can be used with any API that accepts API keys, unless API
restrictions have been added to the key. Standard API keys can't be used with
services that don't accept API keys, including in
[express mode](https://berlin.devsitetest.how/resources/cloud-express-faqs).

### Authorization keys

Authorization keys are API keys that are bound to a service account. When you
use an authorization key to access an API, your request is processed as if you
used the bound service account to make the request.

APIs that support authorization keys include
[Vertex AI](/vertex-ai/generative-ai/docs/start/api-keys?usertype=standard)
(`aiplatform.googleapis.com`) and the
[Gemini API](https://ai.google.dev/api)
(`generativelanguage.googleapis.com`).

When using authorization keys, keep the following in mind:

- 

Requests authenticated by authorization keys aren't recorded in
[service account usage metrics](/iam/docs/service-account-monitoring).

- 

Binding keys to a service account is prevented by a default organization
policy constraint. To change this, see
[Enable authorization keys](#enable-key-binding).

### API key components

An API key has the following components, which let you manage and use the
key:


String 
The API key string is an encrypted string, for example,
`AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe`. When you use an API key to
access an API, you always use the key's string. API keys don't have an
associated JSON file. 
ID 
The API key ID is used by Google Cloud Dedicated administrative tools to uniquely
identify the key. The key ID can't be used to access APIs. The key ID can be
found in the URL of the key's edit page in the Google Cloud Dedicated console. You can also
get the key ID by using the Google Cloud CLI to list the keys in your project. 
Display name 
The display name is an optional, descriptive name for the key,
which you can set when you create or update the key. 
Bound service account 
Authorization keys include the service account's email address. 


## Before you begin

Complete the following tasks to use the samples on this page.

### Set up authentication













Select the tab for how you plan to use the samples on this page:











[Console](#console) [gcloud](#gcloud) [C++](#c++) [Java](#java) [Python](#python) [REST](#rest) 
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
you need to manage API keys,

ask your administrator to grant you the
following IAM roles on your project:













- [API Keys Admin ](/iam/docs/roles-permissions/serviceusage#serviceusage.apiKeysAdmin) (`roles/serviceusage.apiKeysAdmin`)




- 
Restrict an API key to specific APIs by using the Google Cloud Dedicated console:
[Service Usage Viewer ](/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer) (`roles/serviceusage.serviceUsageViewer`)










For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).









### Enable authorization keys

Before you can [create an authorization key](#api-keys-bound-sa), you must
do one of the following:

- 

Update the
`constraints/iam.managed.disableServiceAccountApiKeyCreation` organization
policy constraint to restrict the services that users can create
authorization keys for. When creating an authorization key, users must add
an [API restriction](#adding-api-restrictions) that matches a service
allowed by the constraint.

- 

Disable the `constraints/iam.managed.disableServiceAccountApiKeyCreation`
organization policy constraint.

Changing the organization policy requires an
[organization resource](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).
Projects without an organization aren't supported.

To change the policy constraint, complete the following instructions.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.berlin-build0.goog/iam-admin/orgpolicies/list)

- 

Switch to the organization, folder, or project you want to change the
policies for.

- 

In the **Filter** box, enter `Block service`, and then click the policy
name **Block service account API key bindings**.

- 

Click **Manage policy**.

- 

In the **Policy source** section, select **Override parent's policy**.

- 

Click **Add a rule**.

- 

To disable the constraint, set **Enforcement** to **Off**.

To add a service to the allowed list, set **Enforcement** to **On**.

- 

Click edit **Edit**.

- 

In the **Value type** section, select **User-defined**.

- 

Enter the service that you want to allow creating API keys for.

- 

Click **Done**.

- 

Optional: Click **Test changes** to give you insight on how the proposed
policy might cause compliance violations or disruptions.

- 

Click **Set policy**.




To add a service to the allowed list, do the following:

- 

Create a file named `spec.yaml` with the following content:


```
name : SCOPE / SCOPE_ID /policies/iam.managed.disableServiceAccountApiKeyCreation
spec : 
rules : 
- enforce : true 
parameters : 
allowedServices : 
- SERVICE_NAME 
```


Provide the following values:

- 

` SCOPE `: Either `organizations`, `folders`, or
`projects`.

- 

` SCOPE_ID `: Depending on SCOPE , the ID of
the organization, folder, or project to which the organization policy
applies.

- 

` SERVICE_NAME `: The name of the service you want to
allow—for example, `compute.googleapis.com`.

- 

Run the following `gcloud` command to allow binding of API keys to service
accounts for the specified service:


```
gcloud org-policies set-policy spec.yaml \ 
--update-mask spec
```


To disable the constraint, do the following:

- 

Create a file named `spec.yaml` with the following content:


```
name : SCOPE / SCOPE_ID /policies/iam.managed.disableServiceAccountApiKeyCreation
spec : 
rules : 
- enforce : false 
```


- 

Run the following `gcloud` command to disable the constraint:


```
gcloud org-policies set-policy spec.yaml \ 
--update-mask spec
```







## Create an API key

To create an API key, use one of the following options:


[ Console ](#console) [ gcloud ](#gcloud) [ C++ ](#c++) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 




- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click **Create credentials**, and then select **API key** from the menu.

- 

Add at least one API key restriction. For more information, see
[Apply API key restrictions](/docs/authentication/api-keys#api_key_restrictions).

- 

Optional: To bind the API key to a service account and create an
authorization key, select the
**Authenticate API calls through a service account** checkbox and then
click **Select a service account** to select the service account you want
to bind to the key.

For more information, see [Authorization keys](#api-keys-bound-sa).

- 

Click **Create**. The **API key created** dialog displays the string for
your newly created key.




You use the
[`gcloud services api-keys create` command](/sdk/gcloud/reference/services/api-keys/create)
to create an API key.


```
gcloud services api-keys create \ 
--display-name = DISPLAY_NAME \ 
--api-target = service = SERVICE_1 \ 
--api-target = service = SERVICE_2 
```


Replace the following values:

- 

` DISPLAY_NAME `: A descriptive name for your key.

- 

` SERVICE_1 `, ` SERVICE_2 `...:
The service names of the APIs that the key can be used to access.

You can find the service name by searching for the API on the
[API dashboard](https://console.cloud.berlin-build0.goog/apis/dashboard). Service names are strings
like `bigquery.googleapis.com`.

To bind the API key to a service account and create an authorization key
for services such as Vertex AI and the Gemini
API, use `gcloud beta` instead, with the `--service-account` flag:


```
gcloud beta services api-keys create \ 
--display-name = DISPLAY_NAME \ 
--api-target = service = SERVICE_1 \ 
--api-target = service = SERVICE_2 \ 
--service-account = SERVICE_ACCOUNT_EMAIL_ADDRESS 
```


For more information, see [Authorization keys](#api-keys-bound-sa).




To run this sample, you must install the
[API Keys client library](/cpp/docs/reference/apikeys/latest).






















```
#include "google/cloud/apikeys/v2/api_keys_client.h" 
#include "google/cloud/location.h" 

google :: api :: apikeys :: v2 :: Key CreateApiKey ( 
google :: cloud :: apikeys_v2 :: ApiKeysClient client , 
google :: cloud :: Location location , std :: string display_name ) { 
google :: api :: apikeys :: v2 :: CreateKeyRequest request ; 
request . set_parent ( location . FullName ()); 
request . mutable_key () - > set_display_name ( std :: move ( display_name )); 
// As an example, restrict the API key's scope to the Natural Language API. 
request . mutable_key () - > mutable_restrictions () - > add_api_targets () - > set_service ( 
"language.googleapis.com" ); 

// Create the key, blocking on the result. 
auto key = client . CreateKey ( request ). get (); 
if ( ! key ) throw std :: move ( key . status ()); 
std :: cout "Successfully created an API key: " key - > name () " \n " ; 

// For authenticating with the API key, use the value in `key->key_string()`. 

// The API key's resource name is the value in `key->name()`. Use this to 
// refer to the specific key in a `GetKey()` or `DeleteKey()` RPC. 
return * key ; 
} 
```






To run this sample, you must install the
[`google-cloud-apikeys` client library](/java/docs/reference/google-cloud-apikeys/latest/overview).






















```
import com.google.api.apikeys.v2.[ApiKeysClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) ; 
import com.google.api.apikeys.v2.[ApiTarget](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiTarget.html) ; 
import com.google.api.apikeys.v2.[CreateKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.CreateKeyRequest.html) ; 
import com.google.api.apikeys.v2.[Key](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) ; 
import com.google.api.apikeys.v2.[LocationName](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.LocationName.html) ; 
import com.google.api.apikeys.v2.[Restrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) ; 
import java.io.IOException ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.TimeUnit ; 
import java.util.concurrent.TimeoutException ; 

public class CreateApiKey { 

public static void main ( String [] args ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// TODO(Developer): Before running this sample, 
// 1. Replace the variable(s) below. 
// 2. Set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc 
// 3. Make sure you have the necessary permission to create API keys. 
String projectId = "GOOGLE_CLOUD_PROJECT_ID" ; 

createApiKey ( projectId ); 
} 

// Creates an API key. 
public static void createApiKey ( String projectId ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the `apiKeysClient.close()` method on the client to safely 
// clean up any remaining background resources. 
try ( [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) apiKeysClient = [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) . create ()) { 

[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) key = [ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) . newBuilder () 
. [ setDisplayName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.Builder.html#com_google_api_apikeys_v2_Key_Builder_setDisplayName_java_lang_String_) ( "My first API key" ) 
// Set the API key restriction. 
// You can also set browser/ server/ android/ ios based restrictions. 
// For more information on API key restriction, see: 
// https://cloud.google.com/docs/authentication/api-keys#api_key_restrictions 
. [ setRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.Builder.html#com_google_api_apikeys_v2_Key_Builder_setRestrictions_com_google_api_apikeys_v2_Restrictions_) ( [ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) . newBuilder () 
// Restrict the API key usage by specifying the target service and methods. 
// The API key can only be used to authenticate the specified methods in the service. 
. [ addApiTargets ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.Builder.html#com_google_api_apikeys_v2_Restrictions_Builder_addApiTargets_com_google_api_apikeys_v2_ApiTarget_) ( [ ApiTarget ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiTarget.html) . newBuilder () 
. [ setService ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiTarget.Builder.html#com_google_api_apikeys_v2_ApiTarget_Builder_setService_java_lang_String_) ( "translate.googleapis.com" ) 
. [ addMethods ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiTarget.Builder.html#com_google_api_apikeys_v2_ApiTarget_Builder_addMethods_java_lang_String_) ( "translate.googleapis.com.TranslateText" ) 
. build ()) 
. build ()) 
. build (); 

// Initialize request and set arguments. 
[ CreateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.CreateKeyRequest.html) createKeyRequest = [ CreateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.CreateKeyRequest.html) . newBuilder () 
// API keys can only be global. 
. setParent ( [ LocationName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.LocationName.html) . of ( projectId , "global" ). toString ()) 
. setKey ( key ) 
. build (); 

// Make the request and wait for the operation to complete. 
[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) result = apiKeysClient . [ createKeyAsync ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html#com_google_api_apikeys_v2_ApiKeysClient_createKeyAsync_com_google_api_apikeys_v2_CreateKeyRequest_) ( createKeyRequest ). get ( 3 , TimeUnit . MINUTES ); 

// For authenticating with the API key, use the value in "result.getKeyString()". 
// To restrict the usage of this API key, use the value in "result.getName()". 
System . out . printf ( "Successfully created an API key: %s" , result . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html#com_google_api_apikeys_v2_Key_getName__) ()); 
} 
} 
} 
```






To run this sample, you must install the
[API Keys client library](/python/docs/reference/apikeys/latest).






















```
from google.cloud import [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest)
from google.cloud.api_keys_v2 import [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html)

def create_api_key ( project_id : str , suffix : str ) - > Key : 
""" 
Creates and restrict an API key. Add the suffix for uniqueness. 

TODO(Developer): 
1. Before running this sample, 
set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc 
2. Make sure you have the necessary permission to create API keys. 

Args: 
project_id: Google Cloud project id. 

Returns: 
response: Returns the created API Key. 
""" 
# Create the API Keys client. 
client = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ApiKeysClient ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html) () 

key = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html) () 
key . display_name = f "My first API key - { suffix } " 

# Initialize request and set arguments. 
request = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ CreateKeyRequest ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.CreateKeyRequest.html) () 
request . parent = f "projects/ { project_id } /locations/global" 
request . key = key 

# Make the request and wait for the operation to complete. 
response = client . [ create_key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html#google_cloud_api_keys_v2_services_api_keys_ApiKeysClient_create_key) ( request = request ) . result () 

print ( f "Successfully created an API key: { response . name } " ) 
# For authenticating with the API key, use the value in "response.key_string". 
# To restrict the usage of this API key, use the value in "response.name". 
return response 
```






You use the
[`keys.create` method](/api-keys/docs/reference/rest/v2/projects.locations.keys/create)
to create an API key. This request returns a [long-running operation](#lro);
you must poll the operation to get the information for the new key.


```
curl -X POST \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"displayName" : " DISPLAY_NAME ", 
"restrictions" : { 
"apiTargets": [ 
{ 
"service": " SERVICE_1 " 
}, 
{ 
"service" : " SERVICE_2 " 
}, 
] 
} 
}' \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys" 
```


Replace the following values:

- 

` DISPLAY_NAME `: A descriptive name for your key.

- 

` PROJECT_ID `: Your Google Cloud Dedicated in Germany project ID or name.

- 

` SERVICE_1 `, ` SERVICE_2 `...:
The service names of the APIs that the key can be used to access.

You can find the service name by searching for the API on the
[API dashboard](https://console.cloud.berlin-build0.goog/apis/dashboard). Service names are strings
like `bigquery.googleapis.com`.

Optional: To bind the API key to a service account and create an authorization
key instead, use the following command:


```
curl -X POST \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json; charset=utf-8" \ 
-d '{ 
"displayName" : " DISPLAY_NAME ", 
"restrictions" : { 
"apiTargets": [ 
{ 
"service": " SERVICE_1 " 
}, 
{ 
"service" : " SERVICE_2 " 
}, 
] 
}, 
"serviceAccountEmail" : " SERVICE_ACCOUNT_EMAIL_ADDRESS " 
}' \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys" 
```


For more information, see [Authorization keys](#api-keys-bound-sa).

For more information about creating API keys using the REST API, see
[Creating an API key](/api-keys/docs/create-manage-api-keys#create) in the
API Keys API documentation.





## Apply API key restrictions

Unrestricted API keys are insecure. To reduce security risks, you can restrict
API keys in the following ways:

- 

**[API restrictions](#adding-api-restrictions)**: Limit an API key so it can
only be used with a specific set of APIs. API keys without API restrictions
can be used with all APIs that accept keys generated by Google Cloud Dedicated in Germany.

- 

**[Application restrictions](#adding-application-restrictions)**: Limit an API
key so it can only be used by specific websites, IP addresses, or
applications. API keys without application restrictions can be used from
anywhere.

We recommend setting both API restrictions and application restrictions.

In the Google Cloud Dedicated console, you must add at least one API restriction to be
able to create an API key. However, when you create API keys using the
gcloud CLI or REST API, the keys are unrestricted unless you specify
a restriction. To do so, add the following when you
[create an API key](#create):

- 

**The gcloud CLI**: The
[`--api-target`](/sdk/gcloud/reference/services/api-keys/create#--api-target)
flag, along with the API restrictions you want to add.

- 

**REST**: The
[`restrictions`](/api-keys/docs/reference/rest/v2/projects.locations.keys#restrictions)
object to your request body, containing an
[`apiTargets`](/api-keys/docs/reference/rest/v2/projects.locations.keys#restrictions)
array that specifies the restrictions you want to add.

### Add API restrictions

API restrictions specify which APIs can be called using the API key.

To add API restrictions, use one of the following options:


[ Console ](#console) [ gcloud ](#gcloud) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 




- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click the name of the API key that you want to restrict.

- 

In the **API restrictions** section, click **Restrict key**.

- 

Select all APIs that your API key will be used to access.

- 

Click **Save** to save your changes and return to the API key list.




- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[`gcloud services api-keys list` command](/sdk/gcloud/reference/services/api-keys/list)
to list the keys in your project.

- 

Use the
[`gcloud services api-keys update` command](/sdk/gcloud/reference/services/api-keys/update)
to specify which services an API key can be used to access.

Replace the following values:

- ` KEY_ID `: The ID of the key that you want to
restrict.

- 

` SERVICE_1 `, ` SERVICE_2 `...:
The service names of the APIs that the key can be used to access.

You must provide all service names with the update command; the service
names provided replace any existing services on the key.

You can find the service name by searching for the API on the
[API dashboard](https://console.cloud.berlin-build0.goog/apis/dashboard). Service
names are strings like `bigquery.googleapis.com`.


```
gcloud services api-keys update KEY_ID \ 
--api-target = service = SERVICE_1 --api-target = service = SERVICE_2 
```





To run this sample, you must install the
[`google-cloud-apikeys` client library](/java/docs/reference/google-cloud-apikeys/latest/overview).






















```
import com.google.api.apikeys.v2.[ApiKeysClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) ; 
import com.google.api.apikeys.v2.[ApiTarget](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiTarget.html) ; 
import com.google.api.apikeys.v2.[Key](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) ; 
import com.google.api.apikeys.v2.[Restrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) ; 
import com.google.api.apikeys.v2.[UpdateKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) ; 
import com.google.protobuf.[FieldMask](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.TimeUnit ; 
import java.util.concurrent.TimeoutException ; 

public class RestrictApiKeyApi { 

public static void main ( String [] args ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// TODO(Developer): Before running this sample, 
// 1. Replace the variable(s) below. 
String projectId = "GOOGLE_CLOUD_PROJECT_ID" ; 

// ID of the key to restrict. This ID is auto-created during key creation. 
// This is different from the key string. To obtain the key_id, 
// you can also use the lookup api: client.lookupKey() 
String keyId = "key_id" ; 

restrictApiKeyApi ( projectId , keyId ); 
} 

// Restricts an API key. Restrictions specify which APIs can be called using the API key. 
public static void restrictApiKeyApi ( String projectId , String keyId ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the `apiKeysClient.close()` method on the client to safely 
// clean up any remaining background resources. 
try ( [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) apiKeysClient = [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) . create ()) { 

// Restrict the API key usage by specifying the target service and methods. 
// The API key can only be used to authenticate the specified methods in the service. 
[ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) restrictions = [ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) . newBuilder () 
. [ addApiTargets ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.Builder.html#com_google_api_apikeys_v2_Restrictions_Builder_addApiTargets_com_google_api_apikeys_v2_ApiTarget_) ( [ ApiTarget ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiTarget.html) . newBuilder () 
. setService ( "translate.googleapis.com" ) 
. addMethods ( "translate.googleapis.com.TranslateText" ) 
. build ()) 
. build (); 

[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) key = [ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) . newBuilder () 
. setName ( String . format ( "projects/%s/locations/global/keys/%s" , projectId , keyId )) 
// Set the restriction(s). 
// For more information on API key restriction, see: 
// https://cloud.google.com/docs/authentication/api-keys 
. [ setRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.Builder.html#com_google_api_apikeys_v2_Key_Builder_setRestrictions_com_google_api_apikeys_v2_Restrictions_) ( restrictions ) 
. build (); 

// Initialize request and set arguments. 
[ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) updateKeyRequest = [ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) . newBuilder () 
. setKey ( key ) 
. [ setUpdateMask ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.Builder.html#com_google_api_apikeys_v2_UpdateKeyRequest_Builder_setUpdateMask_com_google_protobuf_FieldMask_) ( [ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_) ( "restrictions" ). build ()) 
. build (); 

// Make the request and wait for the operation to complete. 
[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) result = apiKeysClient . [ updateKeyAsync ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html#com_google_api_apikeys_v2_ApiKeysClient_updateKeyAsync_com_google_api_apikeys_v2_Key_com_google_protobuf_FieldMask_) ( updateKeyRequest ). get ( 3 , TimeUnit . MINUTES ); 

// For authenticating with the API key, use the value in "result.getKeyString()". 
System . out . printf ( "Successfully updated the API key: %s" , result . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html#com_google_api_apikeys_v2_Key_getName__) ()); 
} 
} 
} 
```






To run this sample, you must install the
[API Keys client library](/python/docs/reference/apikeys/latest).






















```
from google.cloud import [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest)
from google.cloud.api_keys_v2 import [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html)

def restrict_api_key_api ( project_id : str , key_id : str ) - > Key : 
""" 
Restricts an API key. Restrictions specify which APIs can be called using the API key. 

TODO(Developer): Replace the variables before running the sample. 

Args: 
project_id: Google Cloud project id. 
key_id: ID of the key to restrict. This ID is auto-created during key creation. 
This is different from the key string. To obtain the key_id, 
you can also use the lookup api: client.lookup_key() 

Returns: 
response: Returns the updated API Key. 
""" 

# Create the API Keys client. 
client = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ApiKeysClient ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html) () 

# Restrict the API key usage by specifying the target service and methods. 
# The API key can only be used to authenticate the specified methods in the service. 
api_target = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ApiTarget ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.ApiTarget.html) () 
api_target . service = "translate.googleapis.com" 
api_target . methods = [ "transate.googleapis.com.TranslateText" ] 

# Set the API restriction(s). 
# For more information on API key restriction, see: 
# https://cloud.google.com/docs/authentication/api-keys 
restrictions = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Restrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Restrictions.html) () 
restrictions . api_targets = [ api_target ] 

key = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html) () 
key . name = f "projects/ { project_id } /locations/global/keys/ { key_id } " 
key . restrictions = restrictions 

# Initialize request and set arguments. 
request = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ UpdateKeyRequest ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.UpdateKeyRequest.html) () 
request . key = key 
request . update_mask = "restrictions" 

# Make the request and wait for the operation to complete. 
response = client . [ update_key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html#google_cloud_api_keys_v2_services_api_keys_ApiKeysClient_update_key) ( request = request ) . result () 

print ( f "Successfully updated the API key: { response . name } " ) 
# Use response.key_string to authenticate. 
return response 
```






- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[keys.list](/api-keys/docs/reference/rest/v2/projects.locations.keys/list)
method. The ID is listed in the `uid` field of the response.

Replace ` PROJECT_ID ` with your Google Cloud Dedicated in Germany project
ID or name.


```
curl - X GET \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/" 
```


- 

Use the
[keys.patch](/api-keys/docs/reference/rest/v2/projects.locations.keys/patch)
method to specify which services an API key can be used to access.

This request returns a [long-running operation](#lro); you must poll the
operation to know when the operation completes and get the operation
status.

Replace the following values:

- 

` SERVICE_1 `, ` SERVICE_2 `...:
The service names of the APIs that the key can be used to access.

You must provide all service names with the request; the service
names provided replace any existing services on the key.

You can find the service name by searching for the API on the
[API dashboard](https://console.cloud.berlin-build0.goog/apis/dashboard). Service
names are strings like `bigquery.googleapis.com`.

- 

` PROJECT_ID `: Your Google Cloud Dedicated in Germany project ID or
name.

- 

` KEY_ID `: The ID of the key that you want to
restrict.


```
curl - X PATCH \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
- H "Content-Type: application/json; charset=utf-8" \ 
-- da ta ' { 
"restrictions" : { 
"apiTargets" : [ 
{ 
"service" : " SERVICE_1 " 
}, 
{ 
"service" : " SERVICE_2 " 
}, 
] 
} 
} ' \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/ KEY_ID ?updateMask=restrictions" 
```


For more information about adding API restrictions to a key using the REST
API, see
[Adding API restrictions](/api-keys/docs/add-restrictions-api-keys#add-api-restrictions)
in the API Keys API documentation.





### Add application restrictions

Application restrictions specify which websites, IP addresses, or apps can use
an API key.

You can apply only one application restriction type at a time. Choose the
restriction type based on your application type:



| 
Option | 
Application type | 
Notes | 
|




| 
[Websites](#websites) | 
Web applications | 
Specifies the websites that can use the key. | 
|

| 
[IP addresses](#ip) | 
Applications called by specific servers | 
Specifies the servers or cron jobs that can use the key. This is the only restriction available for authorization keys. | 
|

| 
[Android apps](#android) | 
Android applications | 
Specifies the Android application that can use the key. | 
|

| 
[iOS apps](#ios) | 
iOS applications | 
Specifies the iOS bundles that can use the key. | 
|





#### Websites

To control which websites can use your API keys, you can add one or more HTTP
referrers as website restrictions. For example, adding `https://example.com` to
an API key's website restrictions means that only calls from
`https://example.com` can use that API key.

The HTTP referrers used in website restrictions have limited wildcard support.
You can substitute a wildcard character (`*`) for a subdomain or path, but you
can't use a wildcard character in the middle of a URL. For example,
`*.example.com` is valid, and accepts all sites ending in `.example.com`.
However, `mysubdomain*.example.com` isn't a valid restriction.

Port numbers can be included in website restrictions. If you include a port
number, then only requests using that port are matched. If you don't specify a
port number, then requests from any port number are matched.

The following table shows some example scenarios and browser restrictions:



| 
**Scenario** | 
**Restrictions** | 
|



| 
Allow a specific URL | 
Add a URL with an exact path. For example:

`www.example.com/path`

`www.example.com/path/path`

Some browsers implement a
[
referrer policy](https://developer.chrome.com/blog/referrer-policy-new-chrome-default/) that sends only the origin URL for cross-origin requests.
Users of these browsers can't use keys with page-specific URL restrictions.

| 
|

| 
Allow any URL in your site | 
You must set two URLs in the `allowedReferers` list.

- 
URL for the domain, without a subdomain, and with a wildcard for
the path. For example:

`example.com/*`

- 
A second URL that includes a wildcard for the subdomain and a
wildcard for the path. For example:

`*.example.com/*`

| 
|

| 
Allow any URL in a single subdomain or naked domain | 



You must set two URLs in the `allowedReferers` list to allow an
entire domain:


- 
URL for the domain, without a trailing slash. For example:

`www.example.com`

`sub.example.com`

`example.com`

- 
A second URL for the domain that includes a wildcard for the path.
For example:

`www.example.com/*`

`sub.example.com/*`

`example.com/*`

| 
|



To restrict your API key to specific websites, use one of the following options:


[ Console ](#console) [ gcloud ](#gcloud) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 




- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click the name of the API key that you want to restrict.

- 

In the **Application restrictions** section, select **Websites**.

- 

For each restriction that you want to add, click **Add**, enter the
restriction, and then click **Done**.

- 

Click **Save** to save your changes and return to the API key list.




- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[`gcloud services api-keys list` command](/sdk/gcloud/reference/services/api-keys/list)
to list the keys in your project.

- 

Use the
[`gcloud services api-keys update` command](/sdk/gcloud/reference/services/api-keys/update)
to add website restrictions to an API key.

Replace the following values:

- ` KEY_ID `: The ID of the key that you want to
restrict.

- 

` ALLOWED_REFERRER_1 `: Your website restriction.

You can add as many restrictions as needed; use commas to separate
the restrictions. You must provide all referrer restrictions with the
update command; the referrer restrictions provided replace any existing
referrer restrictions on the key.


```
gcloud services api-keys update KEY_ID \ 
--allowed-referrers = " ALLOWED_REFERRER_1 " 
```





To run this sample, you must install the
[`google-cloud-apikeys` client library](/java/docs/reference/google-cloud-apikeys/latest/overview).






















```
import com.google.api.apikeys.v2.[ApiKeysClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) ; 
import com.google.api.apikeys.v2.[BrowserKeyRestrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.BrowserKeyRestrictions.html) ; 
import com.google.api.apikeys.v2.[Key](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) ; 
import com.google.api.apikeys.v2.[Restrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) ; 
import com.google.api.apikeys.v2.[UpdateKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) ; 
import com.google.protobuf.[FieldMask](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.TimeUnit ; 
import java.util.concurrent.TimeoutException ; 

public class RestrictApiKeyHttp { 

public static void main ( String [] args ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// TODO(Developer): Before running this sample, 
// 1. Replace the variable(s) below. 
String projectId = "GOOGLE_CLOUD_PROJECT_ID" ; 

// ID of the key to restrict. This ID is auto-created during key creation. 
// This is different from the key string. To obtain the key_id, 
// you can also use the lookup api: client.lookupKey() 
String keyId = "key_id" ; 

restrictApiKeyHttp ( projectId , keyId ); 
} 

// Restricts an API key. To restrict the websites that can use your API key, 
// you add one or more HTTP referrer restrictions. 
public static void restrictApiKeyHttp ( String projectId , String keyId ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the `apiKeysClient.close()` method on the client to safely 
// clean up any remaining background resources. 
try ( [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) apiKeysClient = [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) . create ()) { 

// Restrict the API key usage to specific websites by adding them 
// to the list of allowed_referrers. 
[ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) restrictions = [ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) . newBuilder () 
. [ setBrowserKeyRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.Builder.html#com_google_api_apikeys_v2_Restrictions_Builder_setBrowserKeyRestrictions_com_google_api_apikeys_v2_BrowserKeyRestrictions_) ( [ BrowserKeyRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.BrowserKeyRestrictions.html) . newBuilder () 
. [ addAllowedReferrers ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.BrowserKeyRestrictions.Builder.html#com_google_api_apikeys_v2_BrowserKeyRestrictions_Builder_addAllowedReferrers_java_lang_String_) ( "www.example.com/*" ) 
. build ()) 
. build (); 

[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) key = [ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) . newBuilder () 
. setName ( String . format ( "projects/%s/locations/global/keys/%s" , projectId , keyId )) 
// Set the restriction(s). 
// For more information on API key restriction, see: 
// https://cloud.google.com/docs/authentication/api-keys 
. [ setRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.Builder.html#com_google_api_apikeys_v2_Key_Builder_setRestrictions_com_google_api_apikeys_v2_Restrictions_) ( restrictions ) 
. build (); 

// Initialize request and set arguments. 
[ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) updateKeyRequest = [ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) . newBuilder () 
. setKey ( key ) 
. [ setUpdateMask ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.Builder.html#com_google_api_apikeys_v2_UpdateKeyRequest_Builder_setUpdateMask_com_google_protobuf_FieldMask_) ( [ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_) ( "restrictions" ). build ()) 
. build (); 

// Make the request and wait for the operation to complete. 
[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) result = apiKeysClient . [ updateKeyAsync ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html#com_google_api_apikeys_v2_ApiKeysClient_updateKeyAsync_com_google_api_apikeys_v2_Key_com_google_protobuf_FieldMask_) ( updateKeyRequest ). get ( 3 , TimeUnit . MINUTES ); 

// For authenticating with the API key, use the value in "result.getKeyString()". 
System . out . printf ( "Successfully updated the API key: %s" , result . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html#com_google_api_apikeys_v2_Key_getName__) ()); 
} 
} 
} 
```






To run this sample, you must install the
[API Keys client library](/python/docs/reference/apikeys/latest).






















```
from google.cloud import [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest)
from google.cloud.api_keys_v2 import [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html)

def restrict_api_key_http ( project_id : str , key_id : str ) - > Key : 
""" 
Restricts an API key. To restrict the websites that can use your API key, 
you add one or more HTTP referrer restrictions. 

TODO(Developer): Replace the variables before running this sample. 

Args: 
project_id: Google Cloud project id. 
key_id: ID of the key to restrict. This ID is auto-created during key creation. 
This is different from the key string. To obtain the key_id, 
you can also use the lookup api: client.lookup_key() 

Returns: 
response: Returns the updated API Key. 
""" 

# Create the API Keys client. 
client = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ApiKeysClient ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html) () 

# Restrict the API key usage to specific websites by adding them to the list of allowed_referrers. 
browser_key_restrictions = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ BrowserKeyRestrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.BrowserKeyRestrictions.html) () 
browser_key_restrictions . allowed_referrers = [ "www.example.com/*" ] 

# Set the API restriction. 
# For more information on API key restriction, see: 
# https://cloud.google.com/docs/authentication/api-keys 
restrictions = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Restrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Restrictions.html) () 
restrictions . browser_key_restrictions = browser_key_restrictions 

key = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html) () 
key . name = f "projects/ { project_id } /locations/global/keys/ { key_id } " 
key . restrictions = restrictions 

# Initialize request and set arguments. 
request = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ UpdateKeyRequest ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.UpdateKeyRequest.html) () 
request . key = key 
request . update_mask = "restrictions" 

# Make the request and wait for the operation to complete. 
response = client . [ update_key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html#google_cloud_api_keys_v2_services_api_keys_ApiKeysClient_update_key) ( request = request ) . result () 

print ( f "Successfully updated the API key: { response . name } " ) 
# Use response.key_string to authenticate. 
return response 
```






- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[keys.list](/api-keys/docs/reference/rest/v2/projects.locations.keys/list)
method. The ID is listed in the `uid` field of the response.

Replace ` PROJECT_ID ` with your Google Cloud Dedicated in Germany project
ID or name.


```
curl - X GET \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/" 
```


- 

Use the
[keys.patch](/api-keys/docs/reference/rest/v2/projects.locations.keys/patch)
method to add website restrictions to the API key.

This request
returns a [long-running operation](#lro); you must poll the operation to
know when the operation completes and get the operation status.

Replace the following values:

- 

` ALLOWED_REFERRER_1 `: Your website restriction.

You can add as many restrictions as needed; use commas to separate
the restrictions. You must provide all referrer restrictions with the
request; the referrer restrictions provided replace any existing
referrer restrictions on the key.

- 

` PROJECT_ID `: Your Google Cloud Dedicated in Germany project ID or
name.

- 

` KEY_ID `: The ID of the key that you want to
restrict.


```
curl - X PATCH \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
- H "Content-Type: application/json; charset=utf-8" \ 
-- da ta ' { 
"restrictions" : { 
"browserKeyRestrictions" : { 
"allowedReferrers" : [ " ALLOWED_REFERRER_1 " ] 
} 
} 
} ' \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/ KEY_ID ?updateMask=restrictions" 
```


For more information about adding website restrictions to a key using the REST
API, see
[Adding browser restrictions](/api-keys/docs/add-restrictions-api-keys#adding_browser_restrictions)
in the API Keys API documentation.



#### IP addresses

You can specify the external IP addresses of the callers (such as web servers or
cron jobs) that are allowed to use your API keys. You can specify IP addresses
in the following formats:

- 

IPv4 (`198.51.100.1`)

- 

IPv6 (`2001:db8::1`)

- 

A subnet using CIDR notation (`198.51.100.0/24`, `2001:db8::/64`)

Internal IP addresses and `localhost` aren't supported.

To restrict your API key to specific external IP addresses, use one of the
following options:


[ Console ](#console) [ gcloud ](#gcloud) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 




- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click the name of the API key that you want to restrict.

- 

In the **Application restrictions** section, select **IP addresses**.

- 

For each IP address that you want to add, click **Add**, enter the address,
and then click **Done**.

- 

Click **Save** to save your changes and return to the API key list.




- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[`gcloud services api-keys list` command](/sdk/gcloud/reference/services/api-keys/list)
to list the keys in your project.

- 

Use the
[`gcloud services api-keys update` command](/sdk/gcloud/reference/services/api-keys/update)
to add server (IP address) restrictions to an API key.

Replace the following values:

- ` KEY_ID `: The ID of the key that you want to
restrict.

- 

` ALLOWED_IP_ADDR_1 `: Your allowed IP address.

You can add as many IP addresses as needed; use commas to separate
the addresses.


```
gcloud services api-keys update KEY_ID \ 
--allowed-ips = " ALLOWED_IP_ADDR_1 " 
```





To run this sample, you must install the
[`google-cloud-apikeys` client library](/java/docs/reference/google-cloud-apikeys/latest/overview).






















```
import com.google.api.apikeys.v2.[ApiKeysClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) ; 
import com.google.api.apikeys.v2.[Key](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) ; 
import com.google.api.apikeys.v2.[Restrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) ; 
import com.google.api.apikeys.v2.[ServerKeyRestrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ServerKeyRestrictions.html) ; 
import com.google.api.apikeys.v2.[UpdateKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) ; 
import com.google.protobuf.[FieldMask](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 
import java.util.Arrays ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.TimeUnit ; 
import java.util.concurrent.TimeoutException ; 

public class RestrictApiKeyServer { 

public static void main ( String [] args ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// TODO(Developer): Before running this sample, 
// 1. Replace the variable(s) below. 
String projectId = "GOOGLE_CLOUD_PROJECT_ID" ; 

// ID of the key to restrict. This ID is auto-created during key creation. 
// This is different from the key string. To obtain the key_id, 
// you can also use the lookup api: client.lookupKey() 
String keyId = "key_id" ; 

restrictApiKeyServer ( projectId , keyId ); 
} 

// Restricts the API key based on IP addresses. You can specify one or more IP addresses 
// of the callers, for example web servers or cron jobs, that are allowed to use your API key. 
public static void restrictApiKeyServer ( String projectId , String keyId ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the `apiKeysClient.close()` method on the client to safely 
// clean up any remaining background resources. 
try ( [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) apiKeysClient = [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) . create ()) { 

// Restrict the API key usage by specifying the IP addresses. 
// You can specify the IP addresses in IPv4 or IPv6 or a subnet using CIDR notation. 
[ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) restrictions = [ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) . newBuilder () 
. [ setServerKeyRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.Builder.html#com_google_api_apikeys_v2_Restrictions_Builder_setServerKeyRestrictions_com_google_api_apikeys_v2_ServerKeyRestrictions_) ( [ ServerKeyRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ServerKeyRestrictions.html) . newBuilder () 
. [ addAllAllowedIps ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ServerKeyRestrictions.Builder.html#com_google_api_apikeys_v2_ServerKeyRestrictions_Builder_addAllAllowedIps_java_lang_Iterable_java_lang_String__) ( Arrays . asList ( "198.51.100.0/24" , "2000:db8::/64" )) 
. build ()) 
. build (); 

[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) key = [ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) . newBuilder () 
. setName ( String . format ( "projects/%s/locations/global/keys/%s" , projectId , keyId )) 
// Set the restriction(s). 
// For more information on API key restriction, see: 
// https://cloud.google.com/docs/authentication/api-keys 
. [ setRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.Builder.html#com_google_api_apikeys_v2_Key_Builder_setRestrictions_com_google_api_apikeys_v2_Restrictions_) ( restrictions ) 
. build (); 

// Initialize request and set arguments. 
[ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) updateKeyRequest = [ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) . newBuilder () 
. setKey ( key ) 
. [ setUpdateMask ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.Builder.html#com_google_api_apikeys_v2_UpdateKeyRequest_Builder_setUpdateMask_com_google_protobuf_FieldMask_) ( [ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_) ( "restrictions" ). build ()) 
. build (); 

// Make the request and wait for the operation to complete. 
[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) result = apiKeysClient . [ updateKeyAsync ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html#com_google_api_apikeys_v2_ApiKeysClient_updateKeyAsync_com_google_api_apikeys_v2_Key_com_google_protobuf_FieldMask_) ( updateKeyRequest ). get ( 3 , TimeUnit . MINUTES ); 

// For authenticating with the API key, use the value in "result.getKeyString()". 
System . out . printf ( "Successfully updated the API key: %s" , result . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html#com_google_api_apikeys_v2_Key_getName__) ()); 
} 
} 
} 
```






To run this sample, you must install the
[API Keys client library](/python/docs/reference/apikeys/latest).






















```
from google.cloud import [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest)
from google.cloud.api_keys_v2 import [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html)

def restrict_api_key_server ( project_id : str , key_id : str ) - > Key : 
""" 
Restricts the API key based on IP addresses. You can specify one or more IP addresses of the callers, 
for example web servers or cron jobs, that are allowed to use your API key. 

TODO(Developer): Replace the variables before running this sample. 

Args: 
project_id: Google Cloud project id. 
key_id: ID of the key to restrict. This ID is auto-created during key creation. 
This is different from the key string. To obtain the key_id, 
you can also use the lookup api: client.lookup_key() 

Returns: 
response: Returns the updated API Key. 
""" 

# Create the API Keys client. 
client = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ApiKeysClient ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html) () 

# Restrict the API key usage by specifying the IP addresses. 
# You can specify the IP addresses in IPv4 or IPv6 or a subnet using CIDR notation. 
server_key_restrictions = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ServerKeyRestrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.ServerKeyRestrictions.html) () 
server_key_restrictions . allowed_ips = [ "198.51.100.0/24" , "2000:db8::/64" ] 

# Set the API restriction. 
# For more information on API key restriction, see: 
# https://cloud.google.com/docs/authentication/api-keys 
restrictions = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Restrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Restrictions.html) () 
restrictions . server_key_restrictions = server_key_restrictions 

key = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html) () 
key . name = f "projects/ { project_id } /locations/global/keys/ { key_id } " 
key . restrictions = restrictions 

# Initialize request and set arguments. 
request = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ UpdateKeyRequest ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.UpdateKeyRequest.html) () 
request . key = key 
request . update_mask = "restrictions" 

# Make the request and wait for the operation to complete. 
response = client . [ update_key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html#google_cloud_api_keys_v2_services_api_keys_ApiKeysClient_update_key) ( request = request ) . result () 

print ( f "Successfully updated the API key: { response . name } " ) 
# Use response.key_string to authenticate. 
return response 
```






- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[keys.list](/api-keys/docs/reference/rest/v2/projects.locations.keys/list)
method. The ID is listed in the `uid` field of the response.

Replace ` PROJECT_ID ` with your Google Cloud Dedicated in Germany project ID
or name.


```
curl - X GET \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/" 
```


- 

Use the
[keys.patch](/api-keys/docs/reference/rest/v2/projects.locations.keys/patch)
method to add server (IP address) restrictions to an API key.

This request
returns a [long-running operation](#lro); you must poll the operation to
know when the operation completes and get the operation status.

Replace the following values:

- 

` ALLOWED_IP_ADDR_1 `: Your allowed IP address.

You can add as many IP addresses as needed; use commas to separate
the restrictions. You must provide all IP addresses with the
request; the referrer restrictions provided replace any existing
IP address restrictions on the key.

- 

` PROJECT_ID `: Your Google Cloud Dedicated in Germany project ID or
name.

- 

` KEY_ID `: The ID of the key that you want to
restrict.


```
curl - X PATCH \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
- H "Content-Type: application/json; charset=utf-8" \ 
-- da ta ' { 
"restrictions" : { 
"serverKeyRestrictions" : { 
"allowedIps" : [ " ALLOWED_IP_ADDR_1 " ] 
} 
} 
} ' \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/ KEY_ID ?updateMask=restrictions" 
```


For more information about adding IP address restrictions to a key using the
REST API, see
[Adding server restrictions](/api-keys/docs/add-restrictions-api-keys#adding_server_restrictions)
in the API Keys API documentation.



#### Android apps

You can restrict usage of an API key to specific Android apps. You must provide
the package name and the 20-byte SHA-1 certificate fingerprint for each app.

When you use the API key in a request, you must specify the package name
and certificate fingerprint by using the following HTTP headers:

- `X-Android-Package`

- `X-Android-Cert`

To restrict your API key to one or more Android apps, use one of the following
options:


[ Console ](#console) [ gcloud ](#gcloud) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 




- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click the name of the API key that you want to restrict.

- 

In the **Application restrictions** section, select **Android apps**.

- 

For each Android app that you want to add, click **Add**, enter the package
name and SHA-1 certificate fingerprint, and then click **Done**.

- 

Click **Save** to save your changes and return to the API key list.




- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[`gcloud services api-keys list` command](/sdk/gcloud/reference/services/api-keys/list)
to list the keys in your project.

- 

Use the
[`gcloud services api-keys update` command](/sdk/gcloud/reference/services/api-keys/update)
to specify the Android apps that can use an API key.

Replace the following values:

- ` KEY_ID `: The ID of the key that you want to
restrict.

- 

` SHA1_FINGERPRINT ` and
` PACKAGE_NAME `: The app
information for an Android app that can use the key.

You can add as many apps as needed; use additional
`--allowed-application` flags.


```
gcloud services api-keys update KEY_ID \ 
--allowed-application = sha1_fingerprint = SHA1_FINGERPRINT_1 ,package_name = PACKAGE_NAME_1 \ 
--allowed-application = sha1_fingerprint = SHA1_FINGERPRINT_2 ,package_name = PACKAGE_NAME_2 
```





To run this sample, you must install the
[`google-cloud-apikeys` client library](/java/docs/reference/google-cloud-apikeys/latest/overview).






















```
import com.google.api.apikeys.v2.[AndroidApplication](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.AndroidApplication.html) ; 
import com.google.api.apikeys.v2.[AndroidKeyRestrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.AndroidKeyRestrictions.html) ; 
import com.google.api.apikeys.v2.[ApiKeysClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) ; 
import com.google.api.apikeys.v2.[Key](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) ; 
import com.google.api.apikeys.v2.[Restrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) ; 
import com.google.api.apikeys.v2.[UpdateKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) ; 
import com.google.protobuf.[FieldMask](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.TimeUnit ; 
import java.util.concurrent.TimeoutException ; 

public class RestrictApiKeyAndroid { 

public static void main ( String [] args ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// TODO(Developer): Before running this sample, 
// 1. Replace the variable(s) below. 
String projectId = "GOOGLE_CLOUD_PROJECT_ID" ; 

// ID of the key to restrict. This ID is auto-created during key creation. 
// This is different from the key string. To obtain the key_id, 
// you can also use the lookup api: client.lookupKey() 
String keyId = "key_id" ; 

restrictApiKeyAndroid ( projectId , keyId ); 
} 

// Restricts an API key based on android applications. 
// Specifies the Android application that can use the key. 
public static void restrictApiKeyAndroid ( String projectId , String keyId ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the `apiKeysClient.close()` method on the client to safely 
// clean up any remaining background resources. 
try ( [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) apiKeysClient = [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) . create ()) { 

// Restrict the API key usage by specifying the allowed android applications. 
[ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) restrictions = [ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) . newBuilder () 
. [ setAndroidKeyRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.Builder.html#com_google_api_apikeys_v2_Restrictions_Builder_setAndroidKeyRestrictions_com_google_api_apikeys_v2_AndroidKeyRestrictions_) ( [ AndroidKeyRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.AndroidKeyRestrictions.html) . newBuilder () 
. [ addAllowedApplications ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.AndroidKeyRestrictions.Builder.html#com_google_api_apikeys_v2_AndroidKeyRestrictions_Builder_addAllowedApplications_com_google_api_apikeys_v2_AndroidApplication_) ( [ AndroidApplication ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.AndroidApplication.html) . newBuilder () 
// Specify the android application's package name and SHA1 fingerprint. 
. [ setPackageName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.AndroidApplication.Builder.html#com_google_api_apikeys_v2_AndroidApplication_Builder_setPackageName_java_lang_String_) ( "com.google.appname" ) 
. [ setSha1Fingerprint ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.AndroidApplication.Builder.html#com_google_api_apikeys_v2_AndroidApplication_Builder_setSha1Fingerprint_java_lang_String_) ( "0873D391E987982FBBD30873D391E987982FBBD3" ) 
. build ()) 
. build ()) 
. build (); 

[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) key = [ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) . newBuilder () 
. setName ( String . format ( "projects/%s/locations/global/keys/%s" , projectId , keyId )) 
// Set the restriction(s). 
// For more information on API key restriction, see: 
// https://cloud.google.com/docs/authentication/api-keys 
. [ setRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.Builder.html#com_google_api_apikeys_v2_Key_Builder_setRestrictions_com_google_api_apikeys_v2_Restrictions_) ( restrictions ) 
. build (); 

// Initialize request and set arguments. 
[ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) updateKeyRequest = [ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) . newBuilder () 
. setKey ( key ) 
. [ setUpdateMask ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.Builder.html#com_google_api_apikeys_v2_UpdateKeyRequest_Builder_setUpdateMask_com_google_protobuf_FieldMask_) ( [ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_) ( "restrictions" ). build ()) 
. build (); 

// Make the request and wait for the operation to complete. 
[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) result = apiKeysClient . [ updateKeyAsync ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html#com_google_api_apikeys_v2_ApiKeysClient_updateKeyAsync_com_google_api_apikeys_v2_Key_com_google_protobuf_FieldMask_) ( updateKeyRequest ). get ( 3 , TimeUnit . MINUTES ); 

// For authenticating with the API key, use the value in "result.getKeyString()". 
System . out . printf ( "Successfully updated the API key: %s" , result . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html#com_google_api_apikeys_v2_Key_getName__) ()); 
} 
} 
} 
```






To run this sample, you must install the
[API Keys client library](/python/docs/reference/apikeys/latest).






















```
from google.cloud import [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest)
from google.cloud.api_keys_v2 import [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html)

def restrict_api_key_android ( project_id : str , key_id : str ) - > Key : 
""" 
Restricts an API key based on android applications. 

Specifies the Android application that can use the key. 

TODO(Developer): Replace the variables before running this sample. 

Args: 
project_id: Google Cloud project id. 
key_id: ID of the key to restrict. This ID is auto-created during key creation. 
This is different from the key string. To obtain the key_id, 
you can also use the lookup api: client.lookup_key() 

Returns: 
response: Returns the updated API Key. 
""" 

# Create the API Keys client. 
client = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ApiKeysClient ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html) () 

# Specify the android application's package name and SHA1 fingerprint. 
allowed_application = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ AndroidApplication ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.AndroidApplication.html) () 
allowed_application . package_name = "com.google.appname" 
allowed_application . sha1_fingerprint = "0873D391E987982FBBD30873D391E987982FBBD3" 

# Restrict the API key usage by specifying the allowed applications. 
android_key_restriction = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ AndroidKeyRestrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.AndroidKeyRestrictions.html) () 
android_key_restriction . allowed_applications = [ allowed_application ] 

# Set the restriction(s). 
# For more information on API key restriction, see: 
# https://cloud.google.com/docs/authentication/api-keys 
restrictions = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Restrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Restrictions.html) () 
restrictions . android_key_restrictions = android_key_restriction 

key = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html) () 
key . name = f "projects/ { project_id } /locations/global/keys/ { key_id } " 
key . restrictions = restrictions 

# Initialize request and set arguments. 
request = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ UpdateKeyRequest ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.UpdateKeyRequest.html) () 
request . key = key 
request . update_mask = "restrictions" 

# Make the request and wait for the operation to complete. 
response = client . [ update_key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html#google_cloud_api_keys_v2_services_api_keys_ApiKeysClient_update_key) ( request = request ) . result () 

print ( f "Successfully updated the API key: { response . name } " ) 
# Use response.key_string to authenticate. 
return response 
```






- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[keys.list](/api-keys/docs/reference/rest/v2/projects.locations.keys/list)
method. The ID is listed in the `uid` field of the response.

Replace ` PROJECT_ID ` with your Google Cloud Dedicated in Germany project
ID or name.


```
curl - X GET \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/" 
```


- 

Use the
[keys.patch](/api-keys/docs/reference/rest/v2/projects.locations.keys/patch)
method to specify the Android apps that can use an API key.

This request
returns a [long-running operation](#lro); you must poll the operation to
know when the operation completes and get the operation status.

Replace the following values:

- 

` SHA1_FINGERPRINT_1 ` and
` PACKAGE_NAME_1 `: The app
information for an Android app that can use the key.

You can add the information for as many apps as needed; use commas to
separate the
[AndroidApplication](/api-keys/docs/reference/rest/v2/projects.locations.keys#AndroidApplication)
objects. You must provide all applications with the request; the
applications provided replace any existing allowed applications on the
key.

- 

` PROJECT_ID `: Your Google Cloud Dedicated in Germany project ID or
name.

- 

` KEY_ID `: The ID of the key that you want to
restrict.


```
curl - X PATCH \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
- H "Content-Type: application/json; charset=utf-8" \ 
-- da ta ' { 
"restrictions" : { 
"androidKeyRestrictions" : { 
"allowedApplications" : [ 
{ 
"sha1Fingerprint" : " SHA1_FINGERPRINT_1 " , 
"packageName" : " PACKAGE_NAME_1 " 
}, 
] 
} 
} 
} ' \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/ KEY_ID ?updateMask=restrictions" 
```


For more information about adding Android app restrictions to a key using the
REST API, see
[Adding Android restrictions](/api-keys/docs/add-restrictions-api-keys#adding_android_restrictions)
in the API Keys API documentation.



#### iOS apps

You can restrict usage of an API key to specific iOS apps by providing the
bundle ID of each app.

When you use the API key in a request, you must specify the bundle ID by using
the `X-Ios-Bundle-Identifier` HTTP header.

To restrict your API key to one or more iOS apps, use one of the following
options:


[ Console ](#console) [ gcloud ](#gcloud) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 




- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click the name of the API key that you want to restrict.

- 

In the **Application restrictions** section, select **iOS apps**.

- 

For each iOS app that you want to add, click **Add**, enter the bundle ID,
and then click **Done**.

- 

Click **Save** to save your changes and return to the API key list.




- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[`gcloud services api-keys list` command](/sdk/gcloud/reference/services/api-keys/list)
to list the keys in your project.

- 

Use the
[`gcloud services api-keys update`](/sdk/gcloud/reference/services/api-keys/update)
method to specify the iOS apps that can use the key.

Replace the following values:

- ` KEY_ID `: The ID of the key that you want to
restrict.

- 

` ALLOWED_BUNDLE_ID `: The bundle ID of an iOS app
that you want to be able to use this API key.

You can add as many bundle IDs as needed; use commas to separate the
IDs.


```
gcloud services api-keys update KEY_ID \ 
--allowed-bundle-ids = ALLOWED_BUNDLE_ID_1 , ALLOWED_BUNDLE_ID_2 
```





To run this sample, you must install the
[`google-cloud-apikeys` client library](/java/docs/reference/google-cloud-apikeys/latest/overview).






















```
import com.google.api.apikeys.v2.[ApiKeysClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) ; 
import com.google.api.apikeys.v2.[IosKeyRestrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.IosKeyRestrictions.html) ; 
import com.google.api.apikeys.v2.[Key](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) ; 
import com.google.api.apikeys.v2.[Restrictions](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) ; 
import com.google.api.apikeys.v2.[UpdateKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) ; 
import com.google.protobuf.[FieldMask](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) ; 
import java.io.IOException ; 
import java.util.Arrays ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.TimeUnit ; 
import java.util.concurrent.TimeoutException ; 

public class RestrictApiKeyIos { 

public static void main ( String [] args ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// TODO(Developer): Before running this sample, 
// 1. Replace the variable(s) below. 
String projectId = "GOOGLE_CLOUD_PROJECT_ID" ; 

// ID of the key to restrict. This ID is auto-created during key creation. 
// This is different from the key string. To obtain the key_id, 
// you can also use the lookup api: client.lookupKey() 
String keyId = "key_id" ; 

restrictApiKeyIos ( projectId , keyId ); 
} 

// Restricts an API key. You can restrict usage of an API key to specific iOS apps 
// by providing the bundle ID of each app. 
public static void restrictApiKeyIos ( String projectId , String keyId ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the `apiKeysClient.close()` method on the client to safely 
// clean up any remaining background resources. 
try ( [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) apiKeysClient = [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) . create ()) { 

// Restrict the API key usage by specifying the bundle ID(s) 
// of iOS app(s) that can use the key. 
[ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) restrictions = [ Restrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.html) . newBuilder () 
. [ setIosKeyRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Restrictions.Builder.html#com_google_api_apikeys_v2_Restrictions_Builder_setIosKeyRestrictions_com_google_api_apikeys_v2_IosKeyRestrictions_) ( [ IosKeyRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.IosKeyRestrictions.html) . newBuilder () 
. [ addAllAllowedBundleIds ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.IosKeyRestrictions.Builder.html#com_google_api_apikeys_v2_IosKeyRestrictions_Builder_addAllAllowedBundleIds_java_lang_Iterable_java_lang_String__) ( Arrays . asList ( "com.google.gmail" , "com.google.drive" )) 
. build ()) 
. build (); 

[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) key = [ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) . newBuilder () 
. setName ( String . format ( "projects/%s/locations/global/keys/%s" , projectId , keyId )) 
// Set the restriction(s). 
// For more information on API key restriction, see: 
// https://cloud.google.com/docs/authentication/api-keys 
. [ setRestrictions ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.Builder.html#com_google_api_apikeys_v2_Key_Builder_setRestrictions_com_google_api_apikeys_v2_Restrictions_) ( restrictions ) 
. build (); 

// Initialize request and set arguments. 
[ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) updateKeyRequest = [ UpdateKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.html) . newBuilder () 
. setKey ( key ) 
. [ setUpdateMask ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UpdateKeyRequest.Builder.html#com_google_api_apikeys_v2_UpdateKeyRequest_Builder_setUpdateMask_com_google_protobuf_FieldMask_) ( [ FieldMask ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) . newBuilder (). [ addPaths ](https://berlin.devsitetest.how/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_) ( "restrictions" ). build ()) 
. build (); 

// Make the request and wait for the operation to complete. 
[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) result = apiKeysClient . [ updateKeyAsync ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html#com_google_api_apikeys_v2_ApiKeysClient_updateKeyAsync_com_google_api_apikeys_v2_Key_com_google_protobuf_FieldMask_) ( updateKeyRequest ). get ( 3 , TimeUnit . MINUTES ); 

// For authenticating with the API key, use the value in "result.getKeyString()". 
System . out . printf ( "Successfully updated the API key: %s" , result . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html#com_google_api_apikeys_v2_Key_getName__) ()); 
} 
} 
} 
```






To run this sample, you must install the
[API Keys client library](/python/docs/reference/apikeys/latest).






















```
from google.cloud import [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest)
from google.cloud.api_keys_v2 import [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html)

def restrict_api_key_ios ( project_id : str , key_id : str ) - > Key : 
""" 
Restricts an API key. You can restrict usage of an API key to specific iOS apps 
by providing the bundle ID of each app. 

TODO(Developer): Replace the variables before running this sample. 

Args: 
project_id: Google Cloud project id. 
key_id: ID of the key to restrict. This ID is auto-created during key creation. 
This is different from the key string. To obtain the key_id, 
you can also use the lookup api: client.lookup_key() 

Returns: 
response: Returns the updated API Key. 
""" 

# Create the API Keys client. 
client = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ApiKeysClient ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html) () 

# Restrict the API key usage by specifying the bundle ID(s) of iOS app(s) that can use the key. 
ios_key_restrictions = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ IosKeyRestrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.IosKeyRestrictions.html) () 
ios_key_restrictions . allowed_bundle_ids = [ "com.google.gmail" , "com.google.drive" ] 

# Set the API restriction. 
# For more information on API key restriction, see: 
# https://cloud.google.com/docs/authentication/api-keys 
restrictions = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Restrictions ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Restrictions.html) () 
restrictions . ios_key_restrictions = ios_key_restrictions 

key = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ Key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.Key.html) () 
key . name = f "projects/ { project_id } /locations/global/keys/ { key_id } " 
key . restrictions = restrictions 

# Initialize request and set arguments. 
request = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ UpdateKeyRequest ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.UpdateKeyRequest.html) () 
request . key = key 
request . update_mask = "restrictions" 

# Make the request and wait for the operation to complete. 
response = client . [ update_key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html#google_cloud_api_keys_v2_services_api_keys_ApiKeysClient_update_key) ( request = request ) . result () 

print ( f "Successfully updated the API key: { response . name } " ) 
# Use response.key_string to authenticate. 
return response 
```






- 

Get the ID of the key that you want to restrict.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[keys.list](/api-keys/docs/reference/rest/v2/projects.locations.keys/list)
method. The ID is listed in the `uid` field of the response.

Replace ` PROJECT_ID ` with your Google Cloud Dedicated in Germany project
ID or name.


```
curl - X GET \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/" 
```


- 

Use the
[keys.patch](/api-keys/docs/reference/rest/v2/projects.locations.keys/patch)
method to specify the iOS apps that can use an API key.

This request
returns a [long-running operation](#lro); you must poll the operation to
know when the operation completes and get the operation status.

Replace the following values:

- 

` ALLOWED_BUNDLE_ID `: The bundle ID of an iOS app
that can use the key.

You can add the information for as many apps as needed; use commas to
separate the bundle IDs. You must provide all bundle IDs with the
request; the bundle IDs provided replace any existing allowed
applications on the key.

- 

` PROJECT_ID `: Your Google Cloud Dedicated in Germany project ID or
name.

- 

` KEY_ID `: The ID of the key that you want to
restrict.


```
curl - X PATCH \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
- H "Content-Type: application/json; charset=utf-8" \ 
-- da ta ' { 
"restrictions" : { 
"iosKeyRestrictions" : { 
"allowedBundleIds" : [ " ALLOWED_BUNDLE_ID_1 " , " ALLOWED_BUNDLE_ID_2 " ] 
} 
} 
} ' \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/ KEY_ID ?updateMask=restrictions" 
```


For more information about adding iOS app restrictions to a key using the REST
API, see
[Adding iOS restrictions](/api-keys/docs/add-restrictions-api-keys#adding_ios_restrictions)
in the API Keys API documentation.



### List API keys that don't have restrictions

You can list the API keys in an organization, folder, or project that don't
have restrictions using Cloud Asset Inventory. To do so, complete the following steps:

- 

Enable the Cloud Asset Inventory API in the project you're running Cloud Asset Inventory
commands from.

[Enable the Cloud Asset Inventory API](https://console.cloud.berlin-build0.goog/apis/library/cloudasset.googleapis.com)

- 

Make sure your account has the
[correct role to call the Cloud Asset Inventory API](/asset-inventory/docs/roles-permissions#roles).
For individual permissions for each call type, see
[Permissions](/asset-inventory/docs/roles-permissions#permissions).

- 

Run the following command to list API keys that don't have restrictions:


```
gcloud asset list \ 
-- SCOPE \ 
--asset-types = apikeys.googleapis.com/Key \ 
--content-type = resource \ 
--filter = " FILTER " 
```


Replace the following:

- 

` SCOPE `: The scope (project, folder, or organization) for
listing API keys. Use one of the following values:

- 

`project= PROJECT_ID `, where
` PROJECT_ID ` is the ID of the project.

- 

`folder= FOLDER_ID `, where ` FOLDER_ID `
is the ID of the folder.

- 

`organization= ORGANIZATION_ID `, where
` ORGANIZATION_ID ` is the ID of the organization.

- 

` FILTER `: Which API keys to list, based on the
restrictions they're missing:

- 

`-resource.data.restrictions:*`: Show API keys that are missing all
restrictions.

- 

`-resource.data.restrictions.apiTargets:*`: Show API keys that are
missing API restrictions.

- 

`-resource.data.restrictions.browserKeyRestrictions:*`: Show API keys
that are missing website restrictions.

- 

`-resource.data.restrictions.serverKeyRestrictions:*`: Show API keys
that are missing IP address restrictions.

- 

`-resource.data.restrictions.androidKeyRestrictions:*`: Show API keys
that are missing Android restrictions.

- 

`-resource.data.restrictions.iosKeyRestrictions:*`: Show API keys that
are missing iOS restrictions.

## Get project information from a key string

You can determine which Google Cloud Dedicated project an API key is associated with
from its string.

Replace ` KEY_STRING ` with the key string you need project
information for.


[ gcloud ](#gcloud) [ Java ](#java) [ Python ](#python) [ REST ](#rest) 
More 




You use the
[`gcloud services api-keys lookup` command](/sdk/gcloud/reference/services/api-keys/lookup)
to get the project ID from a key string.


```
gcloud services api-keys lookup KEY_STRING 

```





To run this sample, you must install the
[`google-cloud-apikeys` client library](/java/docs/reference/google-cloud-apikeys/latest/overview).






















```
import com.google.api.apikeys.v2.[ApiKeysClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) ; 
import com.google.api.apikeys.v2.[LookupKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.LookupKeyRequest.html) ; 
import com.google.api.apikeys.v2.[LookupKeyResponse](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.LookupKeyResponse.html) ; 
import java.io.IOException ; 

public class LookupApiKey { 

public static void main ( String [] args ) throws IOException { 
// TODO(Developer): Before running this sample, 
// 1. Replace the variable(s) below. 
// 2. Set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc 
// 3. Make sure you have the necessary permission to view API keys. 
// API key string to retrieve the API key name. 
String apiKeyString = "API_KEY_STRING" ; 

lookupApiKey ( apiKeyString ); 
} 

// Retrieves name (full path) of an API key using the API key string. 
public static void lookupApiKey ( String apiKeyString ) throws IOException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. After completing all of your requests, call 
// the `apiKeysClient.close()` method on the client to safely 
// clean up any remaining background resources. 
try ( [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) apiKeysClient = [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) . create ()) { 

// Initialize the lookup request and set the API key string. 
[ LookupKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.LookupKeyRequest.html) lookupKeyRequest = [ LookupKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.LookupKeyRequest.html) . newBuilder () 
. setKeyString ( apiKeyString ) 
. build (); 

// Make the request and obtain the response. 
[ LookupKeyResponse ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.LookupKeyResponse.html) response = apiKeysClient . lookupKey ( lookupKeyRequest ); 

System . out . printf ( "Successfully retrieved the API key name: %s" , response . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.LookupKeyResponse.html#com_google_api_apikeys_v2_LookupKeyResponse_getName__) ()); 
} 
} 
} 
```






To run this sample, you must install the
[API Keys client library](/python/docs/reference/apikeys/latest).






















```
from google.cloud import [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest)

def lookup_api_key ( api_key_string : str ) - > None : 
""" 
Retrieves name (full path) of an API key using the API key string. 

TODO(Developer): 
1. Before running this sample, 
set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc 
2. Make sure you have the necessary permission to view API keys. 

Args: 
api_key_string: API key string to retrieve the API key name. 
""" 

# Create the API Keys client. 
client = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ ApiKeysClient ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html) () 

# Initialize the lookup request and set the API key string. 
lookup_key_request = [ api_keys_v2 ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest) . [ LookupKeyRequest ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.types.LookupKeyRequest.html) ( 
key_string = api_key_string , 
# Optionally, you can also set the etag (version). 
# etag=etag, 
) 

# Make the request and obtain the response. 
lookup_key_response = client . [ lookup_key ](https://berlin.devsitetest.how/python/docs/reference/apikeys/latest/google.cloud.api_keys_v2.services.api_keys.ApiKeysClient.html#google_cloud_api_keys_v2_services_api_keys_ApiKeysClient_lookup_key) ( lookup_key_request ) 

print ( f "Successfully retrieved the API key name: { lookup_key_response . name } " ) 
```






You use the
[`lookupKey` method](/api-keys/docs/reference/rest/v2/keys/lookupKey)
to get the project ID from a key string.


```
curl - X GET \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
- H "Content-Type: application/json; charset=utf-8" \ 
"https://apikeys.apis-berlin-build0.goog/v2/keys:lookupKey?keyString= KEY_STRING " 
```



## Create a copy of an API key

If you need a new API key with the same restrictions as an existing API key, you
can create a copy of the existing API key. This operation creates a new API key
with a unique key string and ID, with the existing API key's restrictions.

The copy operation is available only in the Google Cloud Dedicated console. To use other
methods, follow the steps to [create an API key](#create), and then
[apply the same API key restrictions](#adding-api-restrictions) to the newly
generated API key.

- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click the name of the API key that you want to copy.

The API key's details page opens.

- 

Click **Create a copy**.

- 

Enter a name for the new API key and confirm that the restrictions are correct.

- 

Click **Create**.

## Rotate an API key

By periodically rotating your API keys, you can limit the impact of any
compromised API keys.

When you rotate an API key, you create a new key with the same restrictions as
the old key, and update your applications to use the new key. After all of your
applications are updated, you delete the old key.

The rotation operation is available only in the Google Cloud Dedicated console. To use other
methods, follow the steps to [create an API key](#create), and then
[apply the same API key restrictions](#adding-api-restrictions) to the newly
generated API key. After updating your applications to use the new key, you
delete the old key.

- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click the name of the API key that you want to rotate to open its details page.

- 

Click **Rotate key**.

- 

Enter a name for the new API key and confirm that the restrictions are correct.

- 

Click **Create**.

- 

Copy the key string and update your applications to use the new string.

- 

After you have updated all applications to use the new key, return to the
details page for the new key. In the **Previous key** section, click
**Delete the previous key** to delete the old key.

If you find that you deleted the old key prematurely, you can
[undelete it](#undelete).

## Undelete an API key

If you delete an API key by mistake, you can undelete (restore) that key within
30 days of deleting the key. After 30 days, you cannot undelete the API key.


[ Console ](#console) [ gcloud ](#gcloud) [ Java ](#java) [ REST ](#rest) 
More 




- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

- 

Click **Restore deleted credentials**.

- 

Find the deleted API key that you want to undelete, and click **Restore**.

Undeleting an API key may take a few minutes to propagate. After
propagation, the undeleted API key is displayed in the API keys list.




- 

Get the ID of the key that you want to undelete.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[`gcloud services api-keys list --show-deleted` command](/sdk/gcloud/reference/services/api-keys/list)
to list the deleted keys in your project.

- 

Use the
[`gcloud services api-keys undelete` command](/sdk/gcloud/reference/services/api-keys/undelete)
to undelete an API key.


```
gcloud services api-keys undelete KEY_ID 
```


Replace the following values:

- ` KEY_ID `: The ID of the key that you want to
undelete.




To run this sample, you must install the
[`google-cloud-apikeys` client library](/java/docs/reference/google-cloud-apikeys/latest/overview).






















```
import com.google.api.apikeys.v2.[ApiKeysClient](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) ; 
import com.google.api.apikeys.v2.[Key](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) ; 
import com.google.api.apikeys.v2.[UndeleteKeyRequest](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UndeleteKeyRequest.html) ; 
import java.io.IOException ; 
import java.util.concurrent.ExecutionException ; 
import java.util.concurrent.TimeUnit ; 
import java.util.concurrent.TimeoutException ; 

public class UndeleteApiKey { 

public static void main ( String [] args ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// TODO(developer): Replace these variables before running the sample. 
// Project ID or project number of the Google Cloud project. 
String projectId = "YOUR_PROJECT_ID" ; 
// The API key id to undelete. 
String keyId = "YOUR_KEY_ID" ; 

undeleteApiKey ( projectId , keyId ); 
} 

// Undeletes an API key. 
public static void undeleteApiKey ( String projectId , String keyId ) 
throws IOException , ExecutionException , InterruptedException , TimeoutException { 
// Initialize client that will be used to send requests. This client only needs to be created 
// once, and can be reused for multiple requests. 
try ( [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) apiKeysClient = [ ApiKeysClient ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html) . create ()) { 

// Initialize the undelete request and set the argument. 
[ UndeleteKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UndeleteKeyRequest.html) undeleteKeyRequest = [ UndeleteKeyRequest ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.UndeleteKeyRequest.html) . newBuilder () 
. setName ( String . format ( "projects/%s/locations/global/keys/%s" , projectId , keyId )) 
. build (); 

// Make the request and wait for the operation to complete. 
[ Key ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html) undeletedKey = apiKeysClient . [ undeleteKeyAsync ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.ApiKeysClient.html#com_google_api_apikeys_v2_ApiKeysClient_undeleteKeyAsync_com_google_api_apikeys_v2_UndeleteKeyRequest_) ( undeleteKeyRequest ) 
. get ( 3 , TimeUnit . MINUTES ); 

System . out . printf ( "Successfully undeleted the API key: %s" , undeletedKey . [ getName ](https://berlin.devsitetest.how/java/docs/reference/google-cloud-apikeys/latest/com.google.api.apikeys.v2.Key.html#com_google_api_apikeys_v2_Key_getName__) ()); 
} 
} 
} 
```






- 

Get the ID of the key that you want to undelete.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[keys.list](/api-keys/docs/reference/rest/v2/projects.locations.keys/list)
method, with the `showDeleted` query parameter set to `true`.
The key ID is listed in the `uid` field of the response.

Replace ` PROJECT_ID ` with your Google Cloud Dedicated in Germany project
ID or name.


```
curl - X GET \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys?showDeleted=true" 
```


- 

Use the
[undelete](/api-keys/docs/reference/rest/v2/projects.locations.keys/undelete)
method to undelete the API key.


```
curl - X POST \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
- H "Content-Type: application/json; charset=utf-8" \ 
"https://apikeys.apis-berlin-build0.goog/v2/projects/ PROJECT_ID /locations/global/keys/ KEY_ID :undelete" 
```


This request
returns a [long-running operation](#lro); you must poll the operation to
know when the operation completes and get the operation status.

Replace the following values:

- ` PROJECT_ID `: Your Google Cloud Dedicated in Germany project ID or
name.

- ` KEY_ID `: The ID of the key that you want to
restrict.




## Determine the API key type

You can determine whether the API key is a standard or authorization key by
inspecting the key.


[ Console ](#console) [ gcloud ](#gcloud) 
More 




- 

In the Google Cloud Dedicated console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.berlin-build0.goog/apis/credentials)

If a service account identifier is displayed, the API key is an
authorization key. If there is no service account identifier displayed,
the API key is a standard API key.




- 

Get the ID of the key.

The ID is not the same as the display name or the key string. You can get
the ID by using the
[`gcloud services api-keys list` command](/sdk/gcloud/reference/services/api-keys/list)
to list the keys in your project.

- 

Use the
[`gcloud services api-keys describe` command](/sdk/gcloud/reference/services/api-keys/describe)
to describe the API key.


```
gcloud services api-keys describe KEY_ID 
```


If a service account identifier is displayed, the API key is an
authorization key. If there is no service account identifier displayed,
the API key is a standard API key.




## Poll long-running operations

API Keys API methods use long-running operations. If you use the REST API to
create and manage API keys, an operation object is returned from the initial
method request. You use the operation name to poll the long-running operation.
When the long-running request completes, polling the operation returns the
data from the long-running request.

To poll a long-running API Keys API operation, you use the
[`operations.get`](/api-keys/docs/reference/rest/v2/operations/get) method.

Replace ` OPERATION_NAME ` with the operation name returned
by the long-running operation. For example,
`operations/akmf.p7-358517206116-cd10a88a-7740-4403-a8fd-979f3bd7fe1c`.


```
curl - X GET \ 
- H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
- H "Content-Type: application/json; charset=utf-8" \ 
"https://apikeys.apis-berlin-build0.goog/v2/ OPERATION_NAME " 
```


## Limits on API keys

You can create up to 300 API keys per project. This limit
is a system limit, and can't be changed using a quota increase request.
If more API keys are needed, you must use more than one project.

You can add up to 1200
[application restrictions](#adding-application-restrictions) to an API key.

## What's next

- Learn about [best practices for keeping your API keys secure](/docs/authentication/api-keys-best-practices).

- Learn more about the [API Keys API](/api-keys/docs/overview).