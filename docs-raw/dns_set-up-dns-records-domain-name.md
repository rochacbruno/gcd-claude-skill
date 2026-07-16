# Quickstart: Set up DNS records for a domain name with Cloud DNS

Source: https://berlin.devsitetest.how/dns/docs/set-up-dns-records-domain-name
Last updated: 2026-07-15

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/dns/docs/tpc-differences) for more details.














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

Cloud DNS

](https://berlin.devsitetest.how/dns/docs)






- 








[

Guides

](https://berlin.devsitetest.how/dns/docs/set-up-dns-records-domain-name)

















- On this page ** 
- [ Requirements ](#requirements)
- [ Before you begin ](#before-you-begin)
- [ Create a managed public zone in Cloud DNS ](#create-managed-public-zone)
- [ Create a record to point the domain to an external IP address ](#create_a_record_to_point_the_domain_to_an_external_ip_address)
- [ Create a CNAME record for the www subdomain ](#create-cname-subdomain)
- [ Update your domain name servers to publish your domain ](#update-domain-name-servers)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Quickstart: Set up DNS records for a domain name with Cloud DNS 




This page explains how to set up a Cloud DNS managed zone and a resource
record for your domain name. It guides you through an example of creating a
managed zone and then setting up Address (`A`) and Canonical Name (`CNAME`)
records for the domain.

For more information, see the following resources:

- For Cloud DNS concepts, see the
[Cloud DNS overview](/dns/docs/overview).

- For terminology related to Cloud DNS, see
[Key terms](/dns/docs/key-terms).

- For Virtual Private Cloud (VPC) network configuration information, see the
[VPC overview](/vpc/docs/overview).

- For configuration how-tos and API information, see [What's next](#whats-next).

## Requirements

This quickstart assumes that you have the following:

- A domain name through a domain name registrar. You can register a domain name
by using [Cloud Domains](/domains/docs/register-domain) or another
domain registrar of your choice. Cloud Domains lets you manage
domains by using the Cloud Domains API.

- A [Windows Server virtual machine (VM)
instance](/compute/docs/create-windows-server-vm-instance) or a [Linux VM
instance](/compute/docs/create-linux-vm-instance).

- An IP address to point the `A` record of your zone to. A valid IP
address can be a server that you already have running with an IP address that
you can point to. For example, you can go through the
[Running a basic Apache Web server](/compute/docs/tutorials/basic-webserver-apache)
tutorial to start up a web server on a Compute Engine VM.





## Before you begin



















- 




In the Google Cloud Dedicated console, on the project selector page,
select or create a Google Cloud Dedicated project.




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












[Go to project selector](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)














- 



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).


















- 




Make sure that you have the following role or roles on the project:

Service Usage Admin, DNS Administrator



#### Check for the roles





- 


In the Google Cloud Dedicated console, go to the **IAM** page.


[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project)


- 

Select the project.



- 


In the **Principal** column, find all rows that identify you or a group that
you're included in. To learn which groups you're included in, contact your
administrator.




- 
For all rows that specify or include you, check the **Role** column to see whether
the list of roles includes the required roles.





#### Grant the roles





- 


In the Google Cloud Dedicated console, go to the **IAM** page.





[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project)


- 

Select the project.



- 
Click person_add **Grant access**.


- 


In the **New principals** field, enter your user identifier.

This is typically the identifier for a user in a workforce identity pool. For details,
see [
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users), or contact your administrator.





- 
Click **Select a role**, then search for the role.

- 
To grant additional roles, click add **Add
another role** and add each additional role.


- 
Click **Save**.



















- 




Enable the DNS API.






**Roles required to enable APIs**


To enable APIs, you need the `serviceusage.services.enable` permission. If you
created the project, then you likely already have this permission through the
Owner role (`roles/owner`). Otherwise, you can get this permission through the
Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
[Learn how to grant roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=dns)






## Create a managed public zone in Cloud DNS

- 

In the Google Cloud Dedicated console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.berlin-build0.goog/net-services/dns/zones/new/create)

- 

To create a public DNS zone, click
**Create
zone** .

- 

For **Zone type**, choose **Public**.

- 

In the
**Zone name** field, enter `my-new-zone`.

- 

In the **DNS
name** field, enter the name of the domain
that you purchased. Enter the domain name only. For example:


```
example.com
```


- 

In the
**DNSSEC** drop-down list,
select **Off**.

- 

Click
**Create** .

The **Zone details** page is displayed. Default NS and SOA records
have been created for you.

To edit a record, on the **Zone details** page, at the end of the row for the
record that you want to edit, click
*edit***Edit**.

## Create a record to point the domain to an external IP address

If your IP address is in the format `#.#.#.#`, you have an IPv4 address and need
to create an `A` record.

If your IP address is in the format `#:#:#:#:#:#:#:#`, you have an IPv6
address and need to create an `AAAA` record.

- 

In the Google Cloud Dedicated console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.berlin-build0.goog/net-services/dns/zones)

- 

Click the zone where you want to add a record set.

- 

Click **Add standard**.

- 

For **Resource Record Type**, to create an `A` record, select `A`.
To create an `AAAA` record, select `AAAA`.

- 

For **IPv4 Address** or **IPv6 Address**, enter the IP address that you
want to use with this domain.

- 

Click **Create**.

## Create a CNAME record for the `www` subdomain

- 

In the Google Cloud Dedicated console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.berlin-build0.goog/net-services/dns/zones)

- 

Click the zone where you want to add a record set.

- 

Click **Add standard**.

- 

For **DNS Name**, enter `www`.

- 

For **Resource Record Type**, select `CNAME`.

- 

For **Canonical name**, enter the domain name, followed by a period (for
example, `example.com.`).

- 

Click **Create**.

The record update takes some time to propagate depending on the
time to live (TTL) values of the records. You can verify that the DNS records
are working by visiting the domain name and confirming that the domain resolves
to your IP address.

## Update your domain name servers to publish your domain

Finally, you must
[update your domain's name servers to use Cloud DNS](/dns/docs/update-name-servers)
to publish your new records to the internet.

You have successfully used Cloud DNS to set up your DNS records.






## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






- 

In the Google Cloud Dedicated console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/net-services/dns/zones)

- 

Click the zone name (`my-new-zone`) to get to the **Zone details** page.

- 

Select the A and CNAME records that you created.

- 

Click **Delete record sets**.

- 

Go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.berlin-build0.goog/net-services/dns/zones)

- 

To delete the zone, select the `my-new-zone` checkbox, and then at the end
of the row, click
*delete***Delete zone**.






## What's next



- To add, delete, or update records, see
[Manage records](/dns/docs/records).

- To work with managed zones, see
[Create, modify, and delete zones](/dns/docs/zones).

- To find solutions for common issues that you might encounter when using
Cloud DNS, see [Troubleshooting](/dns/docs/troubleshooting).

- To reference the API, see
[Cloud DNS REST API](/dns/docs/reference/v1).

- To determine costs, see [Cloud DNS Pricing](https://berlin.devsitetest.how/dns/pricing).