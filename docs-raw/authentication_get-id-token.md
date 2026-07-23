# Get an ID token

Source: https://berlin.devsitetest.how/docs/authentication/get-id-token
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












# Get an ID token 






- On this page 
- [ Methods for getting an ID token ](#methods)

- [ Get an ID token from the metadata server ](#metadata-server)
- [ Use a connecting service to generate an ID token ](#connecting-service)
- [ Generate an ID token by impersonating a service account ](#impersonation)

- [ What's next ](#whats-next)
- 










This page describes some ways to acquire a Google-signed OpenID Connect (OIDC)
ID token.



For information about ID token contents and lifetimes, see
[ID tokens](/docs/authentication/token-types#identity-tokens).

ID tokens have a specific service or application that they can be used for,
specified by the value of their `aud` claim. This document uses the term
*target service* to refer to the service or application that the ID token can be
used to authenticate to.

When you get the ID token, you can include it in an
`Authorization` header in the request to the target service.

## Methods for getting an ID token 

There are various ways to get an ID token. This page describes the following
methods:


- 
[Get an ID token from the metadata server](#metadata-server)


- 
[Use a connecting service to generate an
ID token](#connecting-service)


- 
[Generate an ID token by impersonating a service
account](#impersonation)


If you need an ID token to be accepted by an application not hosted on
Google Cloud Dedicated, you can probably use these methods. However, you should
determine what ID token claims the application requires.

### Get an ID token from the metadata server

When your code is running on a resource that can have a
[service account attached to it](/iam/docs/attach-service-accounts#attaching-to-resources),
the metadata server for the associated service can usually provide an ID token.
The metadata server generates ID tokens for the attached service account. You
cannot get an ID token based on user credentials from the metadata server.

You can get an ID token from the metadata server when your code is running
on the following Google Cloud Dedicated services:


- 
[
Compute Engine](/compute/docs/instances/verifying-instance-identity#request_signature)



- 
[
Google Kubernetes Engine](/kubernetes-engine/docs/concepts/workload-identity#instance_metadata)


To retrieve an ID token from the metadata server, you query the identity
endpoint for the service account, as shown in this example.


[ curl ](#curl) [ PowerShell ](#powershell) [ Java ](#java) [ Go ](#go) [ Node.js ](#node.js) [ Python ](#python) [ Ruby ](#ruby) 
More 




Replace ` AUDIENCE ` with the URI for the target service,
for example `http://www.example.com`.


```
curl -H "Metadata-Flavor: Google" \
'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience= AUDIENCE '
```



Replace ` AUDIENCE ` with the URI for the target service,
for example `http://www.example.com`.


```
$value = (Invoke-RestMethod `
-Headers @{'Metadata-Flavor' = 'Google'} `
-Uri "http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience= AUDIENCE ")
$value
```



To run this code sample, you must first complete the following steps:

- 
Install the [
Auth Client Library for Java](https://github.com/googleapis/google-auth-library-java)

- 
Set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable to
`apis-berlin-build0.goog`.






















```
import com.google.auth.oauth2.[GoogleCredentials](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) ; 
import com.google.auth.oauth2.[IdTokenCredentials](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html) ; 
import com.google.auth.oauth2.[IdTokenProvider](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html) ; 
import com.google.auth.oauth2.[IdTokenProvider](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html).[Option](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.Option.html) ; 
import java.io.IOException ; 
import java.security.GeneralSecurityException ; 
import java.util.Arrays ; 

public class IdTokenFromMetadataServer { 

public static void main ( String [] args ) throws IOException , GeneralSecurityException { 
// TODO(Developer): Replace the below variables before running the code. 

// The url or target audience to obtain the ID token for. 
String url = "https://example.com" ; 

getIdTokenFromMetadataServer ( url ); 
} 

// Use the Google Cloud metadata server to create an identity token and add it to the 
// HTTP request as part of an Authorization header. 
public static void getIdTokenFromMetadataServer ( String url ) throws IOException { 
// Construct the GoogleCredentials object which obtains the default configuration from your 
// working environment. 
[ GoogleCredentials ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) googleCredentials = [ GoogleCredentials ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) . [ getApplicationDefault ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__) (); 

[ IdTokenCredentials ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html) idTokenCredentials = 
[ IdTokenCredentials ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html) . newBuilder () 
. [ setIdTokenProvider ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setIdTokenProvider_com_google_auth_oauth2_IdTokenProvider_) (( [ IdTokenProvider ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html) ) googleCredentials ) 
. [ setTargetAudience ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setTargetAudience_java_lang_String_) ( url ) 
// Setting the ID token options. 
. [ setOptions ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setOptions_java_util_List_com_google_auth_oauth2_IdTokenProvider_Option__) ( Arrays . asList ( [ Option ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.Option.html) . FORMAT_FULL , [ Option ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.Option.html) . LICENSES_TRUE )) 
. build (); 

// Get the ID token. 
// Once you've obtained the ID token, you can use it to make an authenticated call to the 
// target audience. 
String idToken = idTokenCredentials . [ refreshAccessToken ](https://berlin.devsitetest.how/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html#com_google_auth_oauth2_IdTokenCredentials_refreshAccessToken__) (). getTokenValue (); 
System . out . println ( "Generated ID token." ); 
} 
} 
```






Before running code samples, set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment
variable to `apis-berlin-build0.goog`.






















```
import ( 
"context" 
"fmt" 
"io" 

"golang.org/x/oauth2/google" 
"google.golang.org/api/idtoken" 
"google.golang.org/api/option" 
) 

// getIdTokenFromMetadataServer uses the Google Cloud metadata server environment 
// to create an identity token and add it to the HTTP request as part of an Authorization header. 
func getIdTokenFromMetadataServer ( w io . Writer , url string ) error { 
// url := "http://www.example.com" 

ctx := context . Background () 

// Construct the GoogleCredentials object which obtains the default configuration from your 
// working environment. 
credentials , err := google . FindDefaultCredentials ( ctx ) 
if err != nil { 
return fmt . Errorf ( "failed to generate default credentials: %w" , err ) 
} 

ts , err := idtoken . NewTokenSource ( ctx , url , option . WithCredentials ( credentials )) 
if err != nil { 
return fmt . Errorf ( "failed to create NewTokenSource: %w" , err ) 
} 

// Get the ID token. 
// Once you've obtained the ID token, you can use it to make an authenticated call 
// to the target audience. 
_ , err = ts . Token () 
if err != nil { 
return fmt . Errorf ( "failed to receive token: %w" , err ) 
} 
fmt . Fprintf ( w , "Generated ID token.\n" ) 

return nil 
} 
```






To run this code sample, you must first complete the following steps:

- 
Install the [
Google Auth Library for Node.js](https://github.com/googleapis/google-auth-library-nodejs).

- 
Set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable to
`apis-berlin-build0.goog`.






















```
/** 
* TODO(developer): 
* 1. Uncomment and replace these variables before running the sample. 
*/ 
// const targetAudience = 'http://www.example.com'; 

const { GoogleAuth } = require ( '[google-auth-library](https://berlin.devsitetest.how/nodejs/docs/reference/google-auth-library/latest/overview.html)' ); 

async function getIdTokenFromMetadataServer () { 
const googleAuth = new [ GoogleAuth ](https://berlin.devsitetest.how/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html) (); 

const client = await googleAuth . [ getIdTokenClient ](https://berlin.devsitetest.how/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html) ( targetAudience ); 

// Get the ID token. 
// Once you've obtained the ID token, you can use it to make an authenticated call 
// to the target audience. 
await client . [ idTokenProvider ](https://berlin.devsitetest.how/nodejs/docs/reference/google-auth-library/latest/google-auth-library/idtokenclient.html) . fetchIdToken ( targetAudience ); 
console . log ( 'Generated ID token.' ); 
} 

getIdTokenFromMetadataServer (); 
```






To run this code sample, you must first complete the following steps:

- 
Install the [
Google Auth Python Library](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth).

- 
Set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable to
`apis-berlin-build0.goog`.






















```
import [ google ](https://berlin.devsitetest.how/python/docs/reference/googleapis-common-protos/latest)
from google.auth import compute_engine 
import google.auth.transport.requests 
import google.oauth2.credentials 

def idtoken_from_metadata_server ( url : str ) - > None : 
""" 
Use the Google Cloud metadata server in the Cloud Run (or AppEngine or Kubernetes etc.,) 
environment to create an identity token and add it to the HTTP request as part of an 
Authorization header. 

Args: 
url: The url or target audience to obtain the ID token for. 
Examples: http://www.example.com 
""" 

request = [ google ](https://berlin.devsitetest.how/python/docs/reference/googleapis-common-protos/latest) . auth . transport . [ requests ](https://berlin.devsitetest.how/python/docs/reference/google-resumable-media/latest/google.resumable_media.requests.html) . [ Request ](https://berlin.devsitetest.how/python/docs/reference/policytroubleshooter-iam/latest/google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.Request.html) () 
# Set the target audience. 
# Setting "use_metadata_identity_endpoint" to "True" will make the request use the default application 
# credentials. Optionally, you can also specify a specific service account to use by mentioning 
# the service_account_email. 
credentials = compute_engine . IDTokenCredentials ( 
request = request , target_audience = url , use_metadata_identity_endpoint = True 
) 

# Get the ID token. 
# Once you've obtained the ID token, use it to make an authenticated call 
# to the target audience. 
credentials . refresh ( request ) 
# print(credentials.token) 
print ( "Generated ID token." ) 
```






To run this code sample, you must first complete the following steps:

- 
Install the [
Google Auth Library for Ruby](https://github.com/googleapis/google-auth-library-ruby).

- 
Set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable to
`apis-berlin-build0.goog`.






















```
require "googleauth" 

## 
# Uses the Google Cloud metadata server environment to create an identity token 
# and add it to the HTTP request as part of an Authorization header. 
# 
# @param url [String] The url or target audience to obtain the ID token for 
# (e.g. "http://www.example.com") 
# 
def auth_cloud_idtoken_metadata_server url : 
# Create the GCECredentials client. 
id_client = Google :: Auth :: [ GCECredentials ](https://berlin.devsitetest.how/ruby/docs/reference/googleauth/latest/Google-Auth-GCECredentials.html) . new target_audience : url 

# Get the ID token. 
# Once you've obtained the ID token, you can use it to make an authenticated call 
# to the target audience. 
id_client . [ fetch_access_token ](https://berlin.devsitetest.how/ruby/docs/reference/googleauth/latest/Google-Auth-GCECredentials.html)
puts "Generated ID token." 

id_client . refresh! 
end 
```






### Use a connecting service to generate an ID token

Some Google Cloud Dedicated services help you call other services. These connecting
services might help determine when the call gets made, or manage a workflow that
includes calling the service. The following services can automatically include
an ID token, with the appropriate value for the `aud` claim, when they initiate
a call to a service that requires an ID token:



Pub/Sub 

Pub/Sub enables asynchronous communication between services.
You can configure Pub/Sub to include an ID token with a
message. For more information, see
[
Authentication for push subscription](/pubsub/docs/push#authentication).




### Generate an ID token by impersonating a service account

Service account impersonation allows a principal to generate short-lived
credentials for a trusted service account. The principal can then use these
credentials to authenticate as the service account.

Before a principal can impersonate a service account, it must have an
IAM role on that service account that enables impersonation.
If the principal is itself another service account, it might seem easier to
simply provide the required permissions directly to that service account, and
enable it to impersonate itself. This configuration, known as
self-impersonation, creates a security vulnerability, because it lets the
service account create an access token that can be refreshed in perpetuity.

Service account impersonation should always involve two
principals: a principal that represents the caller, and the service account that
is being impersonated, called the privilege-bearing service account.

To generate an ID token by impersonating a service account, you use the
following general process.

For step-by-step instructions, see
[Create an ID token](/iam/docs/create-short-lived-credentials-direct#sa-credentials-oidc).

- 

Identify or [create a service account](/iam/docs/service-accounts-create#creating) to be the privilege-bearing
service account.



- 
Consult the product documentation to identify the required roles to invoke
the target service. Grant these roles to the service account on the target
service.


- 

Identify the principal that will perform the impersonation, and set up
[Application Default Credentials (ADC)](/docs/authentication/provide-credentials-adc) to use the credentials for
this principal.

For development environments, the principal is usually the user account you
provided to ADC by using the gcloud CLI. However, if you're
running on a resource with a service account attached, the attached service
account is the principal.

- 

Grant the principal the Service Account OpenID Connect Identity
Token Creator role (`roles/iam.serviceAccountOpenIdTokenCreator`).

- 

Use the [IAM Credentials API](/iam/docs/reference/credentials/rest) to generate
the ID token for the authorized service account.

Replace the following:

- AUDIENCE : The URI for the target service&mdashfor example,
`http://www.example.com`.

- SERVICE_ACCOUNT_EMAIL : The email address of the
privilege-bearing service account.


```
curl -X POST \ 
-H "Authorization: Bearer $( gcloud auth print-access-token ) " \ 
-H "Content-Type: application/json" \ 
-d '{"audience": " AUDIENCE ", "includeEmail": "true"}' \ 
https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/ SERVICE_ACCOUNT_EMAIL :generateIdToken
```


## What's next

- Understand [ID tokens](/docs/authentication/token-types#identity-tokens).

- Use shell commands to
[query the Compute Engine metadata server](/compute/docs/metadata/querying-metadata).

- Learn more about [authentication methods](/docs/authentication).