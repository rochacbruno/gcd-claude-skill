# Quotas and limits

Source: https://documentation.s3ns.fr/service-usage/docs/quotas
Last updated: 2026-07-22

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/service-usage/docs/tpc-differences) for more details.














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

Access and resource management

](https://documentation.s3ns.fr/docs/access-resources)






- 








[

Service Usage

](https://documentation.s3ns.fr/service-usage/docs)






- 








[

Resources

](https://documentation.s3ns.fr/service-usage/docs/resources)

















- On this page 
- [ Rate limits ](#rate_limits)
- 









# Quotas and limits




This section describes the quota limits for Service Usage. Additional
quota can be requested from the
[Cloud de Confiance console APIs & Services page for Service Usage](https://console.cloud.s3nscloud.fr/apis/api/serviceusage.googleapis.com/quotas?project=_).

### Rate limits 




| 
API Call Type | 
Limit | 
|



| 
Read-only Calls | 
240 API calls per minute. | 
|

| 
Write Calls (`enable`, `disable`, and `batch Enable` methods) | 
60 API calls per minute. A `batch Enable` call counts as 5 write calls for quota purposes. | 
|