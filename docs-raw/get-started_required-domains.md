# Allow access to Google Cloud Dedicated console domains

Source: https://berlin.devsitetest.how/docs/get-started/required-domains
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/get-started/tpc-differences) for more details.














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

Get started

](https://berlin.devsitetest.how/docs/get-started)












# Allow access to Google Cloud Dedicated console domains 






- On this page 
- [ Required domains ](#required_domains)
- [ Monitoring domains ](#monitoring_domains)
- 











If you or your company uses a local networking configuration that denies access
to particular URLs, such as a firewall or proxy server, you might encounter
errors when accessing or using the Google Cloud Dedicated console. This document lists the
domains and domain patterns that must be allowed for
the Google Cloud Dedicated console to function properly.

## Required domains 

The following domains and domain patterns are required for
Google Cloud Dedicated console functionality. If any of these domains are blocked,
the console will not function as expected.

Make sure your networking configuration allows access to the following domains:




| 
Domain or domain pattern | 
Purpose | 
|



| 
console.cloud.google.com | 
The Google Cloud Dedicated console | 
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
reauth.cloud.google.com | 
Multi-factor authentication (MFA) conformance | 
|

| 
csp.withgoogle.com | 
Content Security Policy (CSP) violation reporting | 
|



## Monitoring domains

The following domains and URLs are used for health monitoring of
the Google Cloud Dedicated console. If any of these are blocked,
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