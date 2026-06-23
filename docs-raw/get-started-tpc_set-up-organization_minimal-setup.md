# Minimal setup

Source: https://berlin.devsitetest.how/docs/get-started-tpc/set-up-organization/minimal-setup
Last updated: 2026-06-18

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












# Minimal setup 






- On this page 
- [ Before you begin ](#before_you_begin)
- [ Set up with minimal configuration ](#minimal)
- [ No default network ](#no_default_network)
- [ What's next? ](#whats_next)
- 









When you first onboard to Google Cloud Dedicated, you
are provided with a new empty
[organization](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

If you just want to try out a new organization before setting it up fully,
you can add a single project and Virtual Private Cloud (VPC) network. This basic deployment is
enough to explore available services and run our quickstart tutorials.

For options for a full enterprise setup, see [Set up your organization](/docs/get-started-tpc/set-up-organization).

## Before you begin 

Ensure the following:

- You have [an identity provider (IdP) configured for your organization](/docs/get-started-tpc/set-up-identity-provider) and
that you are able to sign in with your ID.

- You have [set up the Google Cloud CLI](/docs/get-started-tpc/setup-gcloud) for use with Google Cloud Dedicated.

## Set up with minimal configuration

To add your project and network, do the following:

- [Create a project](/resource-manager/docs/creating-managing-projects) in
your organization.

- 

Create and configure a VPC network called `default` in your
project with the following commands:


```
gcloud compute networks create default
gcloud compute firewall-rules create default-allow-internal --allow = tcp:1-65535,udp:1-65535,icmp --source-ranges 10 .128.0.0/9
gcloud compute firewall-rules create default-allow-ssh --allow = tcp:22
gcloud compute firewall-rules create default-allow-rdp --allow = tcp:3389
gcloud compute firewall-rules create default-allow-icmp --allow = icmp
```


You can now go on to try out our services.

## No default network

If you're familiar with Google Cloud, you might not expect
to have to create a network: in Google Cloud, a [default
VPC network](/vpc/docs/vpc#default-network) (with pre-populated
IPV4 firewall rules) is created automatically for each project. A Google Cloud Dedicated
project, however, does *not* have a default network, so you need to create one
yourself for you and your team members to get started.

## What's next?

- When you're ready to set up an enterprise organization for your users and teams, learn how to [Set up your organization](/docs/get-started-tpc/set-up-organization).