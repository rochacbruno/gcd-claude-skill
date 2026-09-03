# VPC Flow Logs

Source: https://berlin.devsitetest.how/vpc/docs/flow-logs
Last updated: 2026-09-02

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/vpc/docs/tpc-differences) for more details.














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

Virtual Private Cloud

](https://berlin.devsitetest.how/vpc/docs)






- 








[

Guides

](https://berlin.devsitetest.how/vpc/docs/overview)

















- On this page 
- [ Use cases ](#use_cases)

- [ Network monitoring ](#network_monitoring)
- [ Understanding network usage and optimizing network traffic expenses ](#understanding_network_usage_and_optimizing_network_traffic_expenses)
- [ Network forensics ](#network_forensics)

- [ Supported configurations ](#configurations)
- [ Logs collection ](#logs_collection)

- [ Log sampling and processing ](#log-sampling)

- [ Specifications ](#key_properties)
- [ What's next ](#whats_next)
- 









# VPC Flow Logs 



VPC Flow Logs samples packets in your Virtual Private Cloud (VPC)
network to generate flow logs. Flow logs are aggregated by IP connection
(5-tuple). VPC Flow Logs samples the following packets:

- Packets that are sent from and received by
[virtual machine (VM) instances](/compute/docs/instances), including
instances used as [Google Kubernetes Engine nodes](/kubernetes-engine/docs)

- Packets that are sent from and received by Cloud Run resources
configured with [Direct VPC egress](/run/docs/configuring/vpc-direct-vpc)

- Packets that are sent through VLAN attachments for
[Cloud Interconnect](/network-connectivity/docs/interconnect/concepts/overview)
and [Cloud VPN](/network-connectivity/docs/vpn/concepts/overview) tunnels

You can view flow logs in [Cloud Logging](/logging), and you
can export logs to any destination that Cloud Logging export supports.
These logs can be used for network monitoring, forensics, security analysis,
and expense optimization. For more information, see
[Supported configurations](#configurations).





## Use cases

The following are use cases for VPC Flow Logs.

### Network monitoring

VPC Flow Logs provides you with visibility into network
throughput and performance. You can:

- Monitor the VPC network

- Perform network diagnosis

- Filter the flow logs by VMs, serverless endpoints, VLAN attachments, and
Cloud VPN tunnels to understand traffic changes

- Understand traffic growth for capacity forecasting

### Understanding network usage and optimizing network traffic expenses

You can analyze network usage with VPC Flow Logs to
optimize network traffic expenses. For example, you can
analyze the network flows for the following:

- Traffic between regions and zones

- Traffic to specific countries on the internet

- Traffic to on-premises and other cloud networks

- Top talkers in the network, including VMs, serverless endpoints,
VLAN attachments, and Cloud VPN tunnels

### Network forensics

You can use VPC Flow Logs for network forensics. For example,
if an incident occurs, you can examine the following:

- Which IP addresses have communicated with each other and when

- Which IPs are compromised by analyzing all the incoming and outgoing network flows

[Learn how Google Cloud Dedicated in Germany users strengthen their cyber
defense with VPC Flow Logs](https://www.youtube.com/watch?v=v3lx-rKkM-g).

## Supported configurations

You can enable VPC Flow Logs at the organization and project
levels. An organization-level VPC Flow Logs configuration enables
flow logs for all subnets, VLAN attachments, and Cloud VPN tunnels in
all VPC networks in the organization.

At the project level, you can enable VPC Flow Logs for specific
VPC networks, subnets, VLAN attachments, and Cloud VPN
tunnels.



| 
Configuration scope | 
Generates flow logs for these resources | 
Steps to enable | 
|



| 
Organization | 




- All VM instances and Cloud Run resources in all subnets
in the organization

- All VLAN attachments in the organization

- All Cloud VPN tunnels in the organization


| 
[Enable VPC Flow Logs for an organization](/vpc/docs/using-flow-logs#enable-organization) | 
|

| 
VPC network | 




- All VM instances and Cloud Run resources in all subnets
in the VPC network

- All VLAN attachments in the VPC network

- All Cloud VPN tunnels in the VPC network


| 
[Enable VPC Flow Logs for a VPC network](/vpc/docs/using-flow-logs#enable-network) | 
|

| 
Subnet | 
All VM instances and Cloud Run resources in a specific
subnet | 

Enable VPC Flow Logs for a subnet:




- Recommended: [Enable VPC Flow Logs for a subnet (Network Management API)](/vpc/docs/using-flow-logs#network-management)

- [Enable VPC Flow Logs for a subnet (Compute Engine API)](/vpc/docs/using-flow-logs#compute-engine)


| 
|

| 
VLAN attachment | 
A specific VLAN attachment | 
[Enable VPC Flow Logs for a VLAN attachment](/vpc/docs/using-flow-logs#enable-vlan-attachment) | 
|

| 
Cloud VPN tunnel | 
A specific Cloud VPN tunnel | 
[Enable VPC Flow Logs for a Cloud VPN tunnel](/vpc/docs/using-flow-logs#enable-vpn-tunnel) | 
|



You can use filtering to customize these configuration scopes. For more
information, see [Log sampling and processing](#log-sampling).

## Logs collection

Packets are sampled within an aggregation interval. All packets collected for
a given IP connection within the aggregation interval are aggregated into a
single flow log entry. This data is then sent to
[Logging](/logging/docs) in the Google Cloud Dedicated project of the
VPC network that reported the flow.

Logs are stored in Logging for 30 days by default. If
you want to keep logs longer than that, you can either [set a custom
retention period](/logging/docs/storage#logs-retention) or
[export them](/logging/docs/export/configure_export_v2) to a supported
destination.

### Log sampling and processing

To generate flow logs, VPC Flow Logs samples packets in your
VPC network, including packets that are sent from and received by
VMs and serverless endpoints and packets that pass through gateways such as
VLAN attachments or Cloud VPN tunnels. After the flow logs are
generated, VPC Flow Logs processes them by following the procedure
described in this section.

VPC Flow Logs samples packets using a *primary sampling rate*.
The primary sampling rate is dynamic and varies depending on the load of the
physical host running the reporting resource at the time of sampling. The
probability of sampling any single IP connection increases with the volume of
packets. You can't control the primary flow log sampling process or adjust the
primary sampling rate.

After the flow logs are generated, VPC Flow Logs processes them
according to the following procedure:

- **Filtering**. You can specify that only logs that match specified criteria
are generated. For example, you can filter so that only logs
for a particular VM or only logs with a particular metadata value
are generated and the rest are discarded. For more information, see
[Log filtering](/vpc/docs/about-flow-logs-records#filtering).

- **Aggregation**. Information for sampled packets is aggregated over
a configurable *aggregation interval* to produce a *flow log entry*.

- **Secondary flow log sampling**. This is a second sampling process. Flow log entries
are further sampled according to a configurable *secondary sampling rate* parameter.
The secondary sampling is performed on the flow logs generated by the
primary flow log sampling process. For example, if the secondary sampling
rate is set to 1.0, or 100%, VPC Flow Logs samples 100% of
the flow logs generated by the primary flow log sampling.

- **Metadata**. If disabled, all metadata annotations are discarded. If you
want to keep metadata, you can retain all fields or a specific set of
fields. For more information, see [Metadata
annotations](/vpc/docs/about-flow-logs-records#metadata).

- **Write to Logging**. The final log entries are written to
Cloud Logging.

VPC Flow Logs doesn't capture every packet. Instead, it estimates
total traffic based on the sampled packets, accounting for missed packets.
For more information, see
[VPC Flow Logs: Understanding byte and packet counts](https://services.google.com/fh/files/misc/vpc_flow_logs_understanding_byte_and_packet_counts.pdf).

Even though Google Cloud Dedicated doesn't capture every packet, log record captures
can be quite large. You can balance your traffic visibility and storage cost
needs by adjusting the following aspects of logs collection:

- **Aggregation interval**. Sampled packets for a time interval are aggregated
into a single log entry. This time interval can be 5 seconds
(default), 30 seconds, 1 minute, 5 minutes, 10 minutes, or 15 minutes.

- **Secondary sampling rate**.

- For configurations created with the Compute Engine API, 50% of log
entries are kept by default. You can set this
parameter from `1.0` (100%, all log entries are kept)
to `0.0` (0%, no logs are kept).

- For configurations created with the Network Management API, 100% of
log entries are kept by default. You can set this
parameter from `1.0` to greater than `0.0`.

- **Metadata annotations**. By default, flow log entries are annotated with
metadata information, such as the names of the source and
destination within Google Cloud Dedicated or the geographic region of external
sources and destinations. Metadata annotations can be turned off, or you
can specify only certain annotations, to save storage space.

- **Filtering**. By default, logs are generated for every sampled flow.
You can set [filters](/vpc/docs/about-flow-logs-records#filtering) to
generate logs that only match certain criteria.

## Specifications

- VPC Flow Logs introduces no delay
or performance penalty when enabled.

- VPC Flow Logs works with VPC networks, not legacy
networks.

- VPC Flow Logs [samples](#log-sampling) TCP, UDP, ICMP, ESP, GRE,
and RDMA flows:

- Both inbound and outbound flows are sampled. For RDMA over Converged
Ethernet (RoCE), only outbound flows are sampled.

- Flows can be within Google Cloud Dedicated or between Google Cloud Dedicated and
other networks.

- If a flow is captured by sampling,
VPC Flow Logs generates a log for the flow. Each flow record
includes the information described in the
[Record format](/vpc/docs/about-flow-logs-records#record_format) section.

- Flow logs don't indicate which endpoint initiated the flow; they identify
packet direction.

- VPC Flow Logs interacts with firewall rules in the following
ways:

- Egress packets are sampled *before* *egress* firewall rules. Even if an
egress firewall rule denies outbound packets, those packets can be
sampled by VPC Flow Logs.

- Ingress packets are sampled *after* *ingress* firewall rules. If an
ingress firewall rule denies inbound packets, those packets aren't
sampled by VPC Flow Logs.

- You can use [filters](/vpc/docs/about-flow-logs-records#filtering) in
VPC Flow Logs to generate only certain logs.

- VPC Flow Logs supports VMs that have multiple network interfaces.
In each VPC, you need to enable VPC Flow Logs
for each subnet that contains a network interface.

- To log flows between Pods on the same Google Kubernetes Engine (GKE) node, you
must enable
[intranode visibility](/kubernetes-engine/docs/how-to/intranode-visibility)
for the cluster.

- VPC Flow Logs isn't supported for subnets with purpose
`INTERNAL_HTTPS_LOAD_BALANCER` because these subnets are used as proxy-only
subnets and have no VM instances or serverless endpoints.

- VPC Flow Logs writes logs to the project of the reporting
VPC network. For resources in Shared VPC networks,
logs are reported in the host project.

## What's next

- To learn more about the VPC Flow Logs record format and which
metadata annotations are available, see
[About VPC Flow Logs records](/vpc/docs/about-flow-logs-records).

- To see examples of VPC Flow Logs that are collected for various
use cases, see [About traffic flows](/vpc/docs/about-traffic-flows).

- To start reporting flows for a subnet, see
[Configure VPC Flow Logs](/vpc/docs/using-flow-logs).