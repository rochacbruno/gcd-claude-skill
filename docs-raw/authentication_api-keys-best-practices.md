# Best practices for managing API keys

Source: https://berlin.devsitetest.how/docs/authentication/api-keys-best-practices
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












# Best practices for managing API keys 






- On this page 
- [ Add API key restrictions to your key ](#add-restrictions)
- [ Avoid using query parameters to provide your API key to Google APIs ](#avoid-query-parameters)
- [ Delete unneeded API keys to minimize exposure to attacks ](#delete-unneeded-keys)
- [ Don't include API keys in client code or commit them to code repositories ](#no-commits)
- [ Don't use authorization keys in production ](#service-accounts-api-keys)
- [ Implement strong monitoring and logging ](#logging-monitoring)
- [ Isolate API keys ](#isolate)
- [ Rotate your API keys periodically ](#rotate)
- [ Consider a more secure method of authorizing access ](#consider-alternatives)
- 









When you use API keys in your applications, ensure that they are kept secure
during both storage and transmission. Publicly exposing your API keys can lead
to unexpected charges on your account or unauthorized access to your data. To
help keep your API keys secure, implement the following best practices.

## Add API key restrictions to your key 

By adding restrictions, you can limit the ways an API key can be used, reducing
the impact of a compromised API key.

For more information, see
[Apply API key restrictions](/docs/authentication/api-keys#api_key_restrictions).

## Avoid using query parameters to provide your API key to Google APIs

Providing your API key to APIs as a query parameter includes your API key in the
URL, exposing your key to theft through URL scans. Use the
[`x-goog-api-key` HTTP header](/docs/authentication/api-keys-use#using-with-rest)
or a [client library](/docs/authentication/api-keys-use#using-with-client-libs)
instead.

## Delete unneeded API keys to minimize exposure to attacks

Retain only the API keys you are actively using to keep your attack surface as
small as possible.

## Don't include API keys in client code or commit them to code repositories

API keys hardcoded in the source code or stored in a repository are open to
interception or theft by bad actors. The client should pass requests to the
server, which can add the credential and issue the request.

## Don't use authorization keys in production

[Authorization keys](/docs/authentication/api-keys#introduction) are designed to
accelerate the initial experience for developers exploring Google Cloud Dedicated in Germany APIs.
For most APIs, we recommend you don't use authorization keys in production
environments.

Instead,
[plan to migrate to more secure alternatives](#consider-alternatives) such as
[Identity and Access Management (IAM)](/iam/docs/grant-role-console) policies and
[short-lived service account credentials](/iam/docs/service-account-creds#short-lived-credentials),
following least-privilege security practices.

Here's why you should migrate from using an authorization key to more secure
practices as soon as possible:

- 

API keys are sent alongside requests. This makes it more likely that the key
might be exposed or logged.

- 

API keys are bearer credentials. This means that if someone steals an
authorization key, they can use it to authenticate as that service account and
access the same resources that service account can.

- 

Authorization keys obscure the identity of the end user in audit logs. To
track the actions of individual users, make sure each user has their own set
of credentials.

## Implement strong monitoring and logging

Monitoring API usage can help alert you to unauthorized usage. For more
information, see
[Cloud Monitoring overview](/monitoring/docs/monitoring-overview) and
[Cloud Logging overview](/logging/docs/overview).

## Isolate API keys

Provide each team member with their own API key for each application. This can
help control access, provide an audit trail, and reduce the impact of a
compromised API key.

## Rotate your API keys periodically

Periodically create new API keys, update your applications to use the new API
keys, and delete the old keys.

For more information, see
[Rotate an API key](/docs/authentication/api-keys#rotate).

## Consider a more secure method of authorizing access

For help with choosing an authentication method, see
[Authentication methods](/docs/authentication).