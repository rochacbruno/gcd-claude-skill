# Authorize requests

Source: https://berlin.devsitetest.how/resource-manager/docs/authorizing
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/resource-manager/docs/tpc-differences) for more details.














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

Resource Manager

](https://berlin.devsitetest.how/resource-manager/docs)






- 








[

Reference

](https://berlin.devsitetest.how/resource-manager/reference/mcp)












# Authorize requests 






- On this page ** 
- [ About authorization protocols ](#AboutAuthorization)
- [ Authorizing requests with OAuth 2.0 ](#OAuth2Authorizing)
- [ Acquiring and using an API key ](#APIKey)
- 









When your application requests private data, the request must be authorized by an authenticated user who has access to that data.

When your application requests public data, the request doesn't need to be authorized, but does need to be accompanied by an identifier, such as an API key.

Every request your application sends to the Cloud Resource Manager API needs to identify your application to Google. There are two ways to identify your application: using an [OAuth 2.0 token](#AboutAuthorization) (which also authorizes the request) and/or using the application's [API key](#APIKey). Here's how to determine which of those options to use:


- If the request requires authorization (such as a request for an individual's private data), then the application must provide an OAuth 2.0 token with the request. The application may also provide the API key, but it doesn't have to.

- If the request doesn't require authorization (such as a request for public data), then the application must provide either the API key or an OAuth 2.0 token, or both—whatever option is most convenient for you.

## About authorization protocols

Your application must use [OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2) to authorize requests. No other authorization protocols are supported. If your application uses [Sign In With Google](https://developers.google.com/identity/gsi/web), some aspects of authorization are handled for you.

## Authorizing requests with OAuth 2. 0

Requests to the Cloud Resource Manager API for non-public user data must be authorized by an authenticated user.

The details of the authorization process, or "flow," for OAuth 2.0 vary somewhat depending on what kind of application you're writing. The following general process applies to all application types:


- When you create your application, you register it using the [Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/). Google then provides information you'll need later, such as a client ID and a
client secret.

- Activate the Cloud Resource Manager API in the Google Cloud Dedicated console. (If the API isn't listed in the Google Cloud Dedicated console, then skip this step.)


- When your application needs access to user data, it asks Google for a particular **scope** of access.

- Google displays a **consent screen** to the user, asking them to authorize your application to request some of their data.

- If the user approves, then Google gives your application a short-lived **access token**.

- Your application requests user data, attaching the access token to the request.

- If Google determines that your request and the token are valid, it returns the requested data.

Some flows include additional steps, such as using **refresh tokens** to acquire new access tokens. For detailed information about flows for various types of applications, see Google's [OAuth 2.0 documentation](https://developers.google.com/identity/protocols/OAuth2).

Here's the OAuth 2.0 scope information for the Cloud Resource Manager API:



| 
Scope | 
Meaning | 
|

| 
`https://www.googleapis.com/auth/cloud-platform` | 
Read/write access. | 
|


To request access using OAuth 2.0, your application needs the scope information, as well as
information that Google supplies when you register your application (such as the client ID and the
client secret).

**Tip:** The Google APIs client libraries can handle some of the authorization process for you. They are available for a variety of programming languages; check the [page with libraries and samples](/resource-manager/docs/libraries) for more details.

## Acquiring and using an API key



Requests to the Cloud Resource Manager API for public data must be accompanied by an identifier, which can
be an [API key](https://developers.google.com/console/help/generating-dev-keys) or an
[access token](https://developers.google.com/accounts/docs/OAuth2).



To acquire an API key:








- Open the [Credentials page](https://console.cloud.berlin-build0.goog/apis/credentials) in the Google Cloud Dedicated console.

- 

This API supports two types of credentials.

Create whichever credentials are appropriate for your project:




- 


OAuth 2.0:** Whenever your application requests private user
data, it must send an OAuth 2.0 token along with the request. Your
application first sends a client ID and, possibly, a client secret to
obtain a token. You can generate OAuth 2.0 credentials for web
applications, service accounts, or installed applications.




For more information, see the [OAuth 2.0 documentation](https://developers.google.com/identity/protocols/OAuth2).



- 


**API keys:**

A request that does not provide an OAuth 2.0 token must send an API
key.

The key identifies your project and provides API access, quota, and
reports.




The API supports several types of restrictions on API keys. If the API key that you
need doesn't already exist, then create an API key in the Console by
clicking **[Create credentials
](https://console.cloud.berlin-build0.goog/apis/credentials) > API key**. You can restrict the key before using it
in production by clicking **Restrict key** and selecting one of the
**Restrictions**.






To keep your API keys secure, follow the [best practices for
securely using API keys](//cloud.google.com/docs/authentication/api-keys).

After you have an API key, your application can append the query parameter
`key= yourAPIKey ` to all request URLs.

The API key is safe for embedding in URLs; it doesn't need any encoding.