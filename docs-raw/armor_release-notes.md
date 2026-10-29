# Cloud Armor release notes

Source: https://berlin.devsitetest.how/armor/docs/release-notes
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/armor/docs/tpc-differences) for more details.














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

Networking

](https://berlin.devsitetest.how/docs/networking)






- 








[

Google Cloud Armor

](https://berlin.devsitetest.how/armor/docs)






- 








[

Resources

](https://berlin.devsitetest.how/armor/docs/resources)












# Cloud Armor release notes 


















This page contains release notes for features and updates to Google Cloud Armor.







You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/armor-release-notes.xml) directly.









## October 19, 2026


Security 


Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-stable`
rulesets. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning).

The following rulesets have been updated:

- `sqli-v33-stable`

- `xss-v33-stable`

- `lfi-v33-stable`

- `rfi-v33-stable`

- `rce-v33-stable`

- `methodenforcement-v33-stable`

- `scannerdetection-v33-stable`

- `protocolattack-v33-stable`

- `php-v33-stable`

- `sessionfixation-v33-stable`

- `java-v33-stable`

- `nodejs-v33-stable`




Security 


Security fixes and enhancements to Cloud Armor preconfigured WAF `stable`
rulesets for v3.0. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning).

The following rulesets have been updated:

- `sqli-stable`

- `xss-stable`

- `lfi-stable`

- `rfi-stable`

- `rce-stable`

- `methodenforcement-stable`

- `scannerdetection-stable`

- `protocolattack-stable`

- `php-stable`

- `sessionfixation-stable`




## August 27, 2026


Feature 


Cloud Armor supports advanced match conditions to include attributes for
inspecting request body content and parameters in Preview. This lets you write
custom CEL rules to filter traffic based on raw body content, structured data
(JSON, Form Data, GraphQL), and query parameters. For more information, see
[Configure custom rules language
attributes](/armor/docs/rules-language-reference).



## August 19, 2026


Feature 


[Global Front
End](/docs/networking/cross-cloud-network/global-front-end/gfee-overview) is a
unified offering that simplifies billing by consolidating pricing across
networking products. Cloud Armor is included in the Global Front End Enterprise
billing tier. Enabling Global Front End Enterprise in a project enables specific
Cloud Armor Enterprise features for your global external Application Load
Balancers. For more information, see [Global Front
End](/armor/docs/armor-enterprise-overview#global-front-end).This feature is
available in Preview.



## July 08, 2026


Feature 


Cloud Armor preconfigured rules support [ModSecurity Core Rule Set (CRS)
4.22](https://github.com/coreruleset/coreruleset/releases/tag/v4.22.0) 
as a rule source. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning). This feature is Generally Available.



## April 06, 2026


Feature 


Cloud Armor preconfigured rules support [ModSecurity Core Rule Set (CRS)
4.22](https://github.com/coreruleset/coreruleset/releases/tag/v4.22.0) 
as a rule source. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning). This feature is available in Preview.



## March 31, 2026


Feature 


Cloud Armor supports a visual **Match Condition Builder** that allows you to
create complex expressions in Common Expression Language (CEL) without writing raw
code. For more information, see [Use the Match Condition Builder](/armor/docs/manage-security-policies#mcb).



## March 06, 2026


Security 


Security fixes and enhancements to Cloud Armor preconfigured WAF `canary`
rulesets for v3.0. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning).

The following rulesets have been updated:

- `sqli-canary`

- `xss-canary`

- `lfi-canary`

- `rfi-canary`

- `rce-canary`

- `methodenforcement-canary`

- `scannerdetection-canary`

- `protocolattack-canary`

- `php-canary`

- `sessionfixation-canary`




## February 18, 2026


Change 


Cloud Armor [preconfigured WAF rules](/armor/docs/waf-rules) support for
inspection up to the first 64 kB (either 8 kB, 16 kB, 32 kB,
48 kB, or 64 kB) of the [request body
content](/armor/docs/security-policy-overview#request-body) is Generally
Available.



## February 13, 2026


Security 


Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-canary`
rulesets. For more information, see [Tuning Google Cloud Armor WAF
rules](/armor/docs/rule-tuning).

The following rulesets have been updated:

- `sqli-v33-canary`

- `xss-v33-canary`

- `lfi-v33-canary`

- `rfi-v33-canary`

- `rce-v33-canary`

- `methodenforcement-v33-canary`

- `scannerdetection-v33-canary`

- `protocolattack-v33-canary`

- `php-v33-canary`

- `sessionfixation-v33-canary`

- `java-v33-canary`

- `nodejs-v33-canary`




## December 06, 2025


Security 


The Cloud Armor `cve-canary` rules include the
[`google-mrs-v202512-id000002-rce`
signature](/armor/docs/waf-rules#cves_and_other_vulnerabilities) to help detect
and mitigate [CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182).
For more information, see
[Cloud Armor preconfigured WAF rules overview](/armor/docs/waf-rules).



## December 03, 2025


Security 


The Cloud Armor `cve-canary` rules include the
[`google-mrs-v202512-id000001-rce`
signature](/armor/docs/waf-rules#cves_and_other_vulnerabilities) to help detect
and mitigate [CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182).
For more information, see
[Cloud Armor preconfigured WAF rules overview](/armor/docs/waf-rules).



## July 08, 2025


Change 


Cloud Armor [preconfigured WAF rules](/armor/docs/waf-rules) can now inspect up to the first 64 kB (either 8 kB, 16 kB, 32 kB, 48 kB, or 64 kB) of the [request body content](/armor/docs/security-policy-overview#request-body) in Preview.



## October 09, 2024


Feature 


Cloud Armor support for [IP address groups](/armor/docs/address-groups-overview) is Generally Available.



Feature 


Cloud Armor support for regional internal Application Load Balancers is Generally Available. You can use the regional backend security policy type with this load balancer. For more information, see [types of security policies](/armor/docs/security-policy-overview#policy-types).



## July 17, 2024


Feature 


Granular models for Cloud Armor Adaptive Protection are now Generally Available. For more information, see the [Adaptive Protection overview](/armor/docs/adaptive-protection-overview#granular-models).



## June 27, 2024


Feature 


Cloud Armor supports [IP address groups](/armor/docs/address-groups-overview) in Preview.



## June 25, 2024


Feature 


Cloud Armor support for Layer 7 filtering in [globally scoped edge security policies](/armor/docs/security-policy-overview#expandable-1) for Media CDN is now Generally Available.