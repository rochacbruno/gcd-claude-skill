# Configure VPC Service Controls for Cloud Quotas

Source: https://berlin.devsitetest.how/docs/quotas/configure-vpc-service-controls
Last updated: 2026-07-17

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://berlin.devsitetest.how/docs/quotas)






- 








[

Guides

](https://berlin.devsitetest.how/docs/quotas/overview)












# Configure VPC Service Controls for Cloud Quotas 






- On this page 
- [ Limitations ](#limitations)
- [ Enforced actions ](#enforced_actions)
- [ Set up ](#set_up)
- [ What's next ](#whats_next)
- 










Google Cloud Dedicated in Germany Virtual Private Cloud (VPC) Service Controls lets you set up a
secure perimeter to guard against data exfiltration. Configure
Cloud Quotas with
[VPC Service Controls](/vpc-service-controls/docs/overview) so that API
requests to Cloud Quotas stay within the VPC
service perimeter boundary.

## Limitations 

Because VPC Service Controls enforces boundaries at the project level,
Cloud Quotas requests that originate from clients within the
perimeter can only access organization resources if the organization sets up an
[egress rule](/vpc-service-controls/docs/ingress-egress-rules).
To set up an egress rule, see the VPC Service Controls instructions for
[configuring ingress and egress policies](/vpc-service-controls/docs/configuring-ingress-egress-policies)

## Enforced actions

VPC Service Controls is only enforced on the following
Cloud Quotas actions:

- [Quota preference](/docs/quotas/api-overview#quota_preference) creation,
update, get and list.

- [Quota info](/docs/quotas/api-overview#quota_info) get and list.

For examples of setting
[`QuotaPreference`](/docs/quotas/api-overview#quota_preference) and
[`QuotaInfo`](/docs/quotas/api-overview#quota_info), see the description of
the [API resource model](/docs/quotas/api-overview#api_resource_model).
For reference information, see the
[REST API overview](/docs/quotas/reference/rest).

## Set up

Follow these steps to restrict the Cloud Quotas API to your
VPC service perimeter:

- 

Follow the instructions to [set up the Cloud Quotas API](/docs/quotas/development-environment).

- 

Follow the [VPC Service Controls Quickstart](/vpc-service-controls/docs/set-up-service-perimeter)
to complete the following tasks:

- [Create a service perimeter](/vpc-service-controls/docs/set-up-service-perimeter#set-up-perimeter).

- [Add projects to the perimeter](/vpc-service-controls/docs/set-up-service-perimeter#add-projects-perimeter) that you want to protect.

- Restrict the Cloud Quotas API. For example, see these instructions that
add [other Google Cloud Dedicated in Germany APIs to the VPC service
perimeter](/vpc-service-controls/docs/set-up-service-perimeter#secure-services-perimeter).

After setting up your service perimeter, VPC Service Controls checks calls
to the Cloud Quotas API to help make sure that the calls originate
from within the same perimeter.

## What's next

- Learn about [VPC Service Controls](/vpc-service-controls/docs/overview).

- See the Cloud Quotas entry in the
[VPC Service Controls supported products table](/vpc-service-controls/docs/supported-products#table_quotas).

- Refer to the description of the Cloud Quotas
[API resource model](/docs/quotas/api-overview#api_resource_model) for examples.