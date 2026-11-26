# Allow access to Cloud de Confiance by S3NS domains

Source: https://documentation.s3ns.fr/docs/get-started/required-domains
Last updated: 2026-11-25

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/get-started/tpc-differences) for more details.














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

Get started

](https://documentation.s3ns.fr/docs/get-started)












# Allow access to Cloud de Confiance by S3NS domains 






- On this page ** 
- [ Cloud de Confiance console domains ](#console-domains)
- [ Additional domains ](#additional_domains)
- [ Monitoring domains ](#monitoring_domains)
- 











If you or your company uses a local networking configuration that denies access
to particular URLs, such as a firewall or proxy server, you might encounter
errors when accessing or using Cloud de Confiance by S3NS. This document lists the domains and
domain patterns that you must allow for Cloud de Confiance by S3NS interfaces to function
properly.

## Cloud de Confiance console domains 

The following domains and domain patterns are required for
Cloud de Confiance console functionality. If any of these domains are blocked,
the console will not function as expected.

Make sure your networking configuration allows access to the following domains:




| 
Domain or domain pattern | 
Purpose | 
|



| 
console.cloud.google.com | 
The Cloud de Confiance console | 
|

| 
www.gstatic.com | 
Static content such as scripts, style sheets, and images | 
|

| 
ssl.gstatic.com | 
Images | 
|

| 
fonts.gstatic.com | 
Fonts | 
|

| 
*.clients6.google.com | 
Google APIs | 
|

| 
*.googleapis.com | 
Google APIs | 
|

| 
apis.google.com | 
Google API Client Libraries | 
|

| 
accounts.google.com | 
Google Account authentication and sign-in | 
|

| 
reauth.cloud.google.com | 
Multi-factor authentication (MFA) conformance | 
|

| 
csp.withgoogle.com | 
Content Security Policy (CSP) violation reporting | 
|



## Additional domains

The following domains are required for additional Cloud de Confiance by S3NS functionality in
interfaces outside of the Cloud de Confiance console.




| 
Domain or domain pattern | 
Purpose | 
|



| 
ogs.google.com | 
Google Account management | 
|

| 
explorer.apis.google.com | 
Google APIs Explorer and Try this method** panel in documentation | 
|



## Monitoring domains

The following domains and URLs are used for health monitoring of
the Cloud de Confiance console. If any of these are blocked,
the console might continue to function but Google will not be
aware of any errors or behavior issues you encounter while using
the console.




| 
Domain or URL | 
|



| 
cloud.google.com/log | 
|

| 
www.google-analytics.com | 
|

| 
www.googletagmanager.com | 
|