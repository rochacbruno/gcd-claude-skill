# Cloud Load Balancing release notes

Source: https://documentation.s3ns.fr/load-balancing/docs/release-notes
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/load-balancing/docs/tpc-differences) for more details.














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

Networking

](https://documentation.s3ns.fr/docs/networking)






- 








[

Load Balancing

](https://documentation.s3ns.fr/load-balancing/docs)






- 








[

Resources

](https://documentation.s3ns.fr/load-balancing/docs/resources)












# Cloud Load Balancing release notes 


















This page contains release notes for features and updates to
Cloud Load Balancing.







You can see the latest product updates for all of Cloud de Confiance by S3NS on the
[
Cloud de Confiance](/release-notes) page, browse and filter all release notes in the
[Cloud de Confiance console](https://console.cloud.s3nscloud.fr/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.s3nscloud.fr/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://documentation.s3ns.fr/feeds/cloudloadbalancing-release-notes.xml) directly.









## May 22, 2026


Feature 


Application Load Balancers now support the configuration of a
[traffic duration](/load-balancing/docs/backend-service#applb-csm-traffic-duration)
setting when you add backends to backend services. You can configure this
setting as `SHORT` or `LONG` based on the response time needed by backends to
complete HTTP requests.

Application Load Balancers also support the use of the
[*in-flight* balancing mode](/load-balancing/docs/backend-service#bmtc-inflight)
that lets you configure the load balancer's traffic distribution to supported
backends when requests take more than a second to complete.

This feature is in **General availability**.



## May 21, 2026


Feature 


Zonal affinity, which was previously available in Preview,
is generally available (GA).

For more information, see [Zonal affinity for internal passthrough Network Load Balancers](/load-balancing/docs/internal/zonal-affinity). 


## January 23, 2026


Feature 


Application Load Balancers now support the configuration of a
[traffic duration](/load-balancing/docs/backend-service#applb-csm-traffic-duration)
setting when you add backends to the backend services. You can configure this
setting as `SHORT` or `LONG` based on the response time needed by backends to
complete HTTP requests.

Application Load Balancers also support the use of a new
[*in-flight* balancing mode](/load-balancing/docs/backend-service#bmtc-inflight)
that lets you configure the load balancer's traffic distribution to supported
backends when requests take more than a second to complete.

This feature is available in **Preview**.



## October 29, 2025


Feature 


You can specify a custom ephemeral `/96` IPv6 address range when creating a
regional IPv6 forwarding rule. For more information, see the following:

- [Internal passthrough Network Load Balancer overview](/load-balancing/docs/internal)

- [Backend service-based external passthrough Network Load Balancer overview](/load-balancing/docs/network/networklb-backend-service)

- [Protocol forwarding overview](/load-balancing/docs/protocol-forwarding)

This feature is in **General availability**. 


## February 20, 2025


Feature 


Cleartext HTTP/2 over TCP, also known as H2C, lets you use HTTP/2 without TLS. H2C is supported by internal and external Application Load Balancers for both of the following connections:

- 

Connections between clients and the load balancer. No special configuration is required. Support for this capability is in **General Availability**.

- 

Connections between the load balancer and its backends. Support for this capability is in **Preview**. 

To configure H2C for connections between the load balancer and its backends, you set the backend service protocol to `H2C`.




## February 19, 2025


Feature 


Internal and external passthrough Network Load Balancers now support connection draining for UDP and other non-TCP protocol traffic. For details, see [Enable connection draining](/load-balancing/docs/enabling-connection-draining).

This feature is now [generally available (GA)](https://documentation.s3ns.fr/products?e=48754805&hl=en#product-launch-stages).



## February 18, 2025


Feature 


TLS 1.3 early data is now supported on the target HTTPS proxy of global external Application Load Balancers and classic Application Load Balancers.

TLS 1.3 early data, also known as *zero-round-trip time (0-RTT) data*, can improve application performance for resumed connections by 30 to 50%.

For details, see [TLS 1.3 early data support](/load-balancing/docs/https#tls-early-data-support).

This feature is available in **General Availability**.



## January 24, 2025


Announcement 


**Changes to RSA certificate requirements coming April 28, 2025**

We're changing how Application Load Balancers establish TLS connections to backends. This change fixes a problem where the keyUsage extension of RSA certificates is not being validated consistently and might allow a certificate that should have been rejected based on the keyUsage configuration.

**What you need to do**

*Starting April 28, 2025*, RSA certificates that don't meet the keyUsage configuration requirements will no longer be considered valid for establishing TLS connections. We recommend that you check whether your backends' RSA certificates are invalid, and replace them with valid certificates if needed.

A valid RSA certificate is one that has the X509v3 Key Usage extension and includes both the Digital Signature and Key Encipherment parameters.

To identify an invalid RSA certificate, perform the following steps:

- 

First confirm that the certificate type is RSA by running the following command. 

`openssl x509 -text -in cert.crt | grep "Public Key Algorithm"`. 

For RSA certificates, this should output `rsaEncryption`. If it is a non-RSA certificate (for example, EC), you don't need to take any more action at this time.

- 

If it is an RSA certificate, examine the Key Usage configuration by running the following command:

`openssl x509 -text -in cert.crt | grep -A1 "X509v3 Key Usage"`

For a valid RSA certificate, the correct value is `Digital Signature, Key Encipherment`. If either of these values is not present, the RSA certificate is invalid.

For more information about the X.509 certificate format, see [RFC 5280 Key Usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3).



## November 20, 2024


Feature 


Regional external Application Load Balancers, cross-region internal Application Load Balancers, regional internal Application Load Balancers, regional internal proxy Network Load Balancers, cross-region internal proxy Network Load Balancers, and regional external proxy Network Load Balancers now support IPv4 and IPv6 (dual-stack) backends.

The following backends have dual-stack support:

- VM instance groups

- Zonal NEGs (`GCE_VM_IP_PORT` endpoints)

You can also convert your existing single-stack load balancers from IPv4-only to dual stack (IPv4 and IPv6) deployments. 

For details, see the following pages:

- [IPv6 overview](/load-balancing/docs/ipv6)

- [Convert your existing Application Load Balancer to IPv6](/load-balancing/docs/https/convert-applb-dualstack)

- [Convert your existing proxy Network Load Balancer to IPv6](/load-balancing/docs/tcp/convert-proxynetlb-dualstack)

This feature is available in **General Availability**.



## November 19, 2024


Feature 


Percentage-based request mirroring is now supported for the cross-region and regional internal Application Load Balancers. By default, the mirrored backend service receives all requests, even if the
original traffic is being split between multiple weighted backend services. You
can now configure the mirrored backend service to receive only a percentage of the
requests by using the `mirrorPercent` flag to specify the percentage of
requests to be mirrored expressed as a value between 0 and 100.0.

For an example, see [Set up traffic management for regional internal Application Load Balancers](/load-balancing/docs/l7-internal/setting-up-traffic-management#mirror_traffic).

This capability is available in **Preview**.



## November 12, 2024


Feature 


Cloud Load Balancing resources now let you use custom constraints to define your own restrictions on Google Cloud services. To learn about which load balancing resources support custom constraints, and some sample use cases, see [Manage Cloud Load Balancing resources using custom constraints](/load-balancing/docs/custom-constraints). 

For more information about custom constraints, see the following:

- [Custom organization policies](/resource-manager/docs/organization-policy/overview#custom-organization-policies)

- [Custom constraint supported services](/resource-manager/docs/organization-policy/custom-constraint-supported-services)

This feature is available in **General Availability**.



## November 04, 2024


Feature 


Percentage-based request mirroring is now supported for the global and regional external Application Load Balancers (classic is not supported). By default, the mirrored backend service receives all requests, even if the
original traffic is being split between multiple weighted backend services. You
can now configure the mirrored backend service to receive only a percentage of the
requests by using the `mirrorPercent` flag to specify the percentage of
requests to be mirrored expressed as a value between 0 and 100.0.

For an example, see [Set up traffic management for regional external Application Load Balancers](/load-balancing/docs/https/setting-up-reg-traffic-mgmt#mirror_traffic).

This capability is available in **Preview**.



## October 31, 2024


Feature 


Support for [IPv6 static routes](/vpc/docs/static-routes#static-route-next-hops) with a next hop internal passthrough Network Load Balancer (`next-hop-ilb`) is available in **Preview**.



## October 30, 2024


Feature 


Service Extensions plugins are available for Google Cloud Application Load Balancers, excluding Classic, in **Preview**.

Service Extensions plugins help you insert WebAssembly (Wasm) plugins in a fully managed serverless environment directly into the data path of Application Load Balancers. 

For details, see [Plugins for Cloud Load Balancing](/service-extensions/docs/overview#integration-lb-plugins).



## October 29, 2024


Feature 


All the Application Load Balancers, except the classic Application Load Balancer, now support stateful cookie-based session affinity. When you use stateful cookie-based affinity, the load balancer includes an HTTP cookie in the `Set-Cookie` header in response to the initial HTTP request. With stateful session affinity, customers can preserve stickiness to the selected backend.

For details, see [Stateful cookie-based session affinity](/load-balancing/docs/backend-service#stateful-session-affinity).

This capability is in **General Availability**.



## October 28, 2024


Feature 


To take advantage of the new features of the global external Application Load Balancer, you can now migrate your classic Application Load Balancer resources to the global external Application Load Balancer infrastructure.

To migrate to the global external Application Load Balancer, you change the load balancing scheme of your load balancing resources—specifically, the backend services and forwarding rules—from `EXTERNAL` to `EXTERNAL_MANAGED`. You can also rollback resources to the classic Application Load Balancer infrastructure, as long as you do so within 90 days of changing the load balancing scheme.

For more details on the migration process, see the following pages:

- [Migration overview](/load-balancing/docs/https/migrate-to-global)

- [Migrate resources from classic to global external Application Load Balancer](/load-balancing/docs/https/migrate-from-classic-global)

- [Roll back migrated resources to classic Application Load Balancer](/load-balancing/docs/https/roll-back-migrated-resources)

This capability is available in **Preview**.



## October 24, 2024


Feature 


Global external Application Load Balancers and global external proxy Network Load Balancers can now load balance IPv6 traffic. The following backends have dual-stack support:

- VM instance groups

- Zonal NEGs (`GCE_VM_IP_PORT` endpoints)

You can also convert your existing single-stack load balancers from IPv4-only to dual stack (IPv4 and IPv6) deployments. 

For details, see the following pages:

- [IPv6 overview](/load-balancing/docs/ipv6)

- [Convert your existing Application Load Balancer to IPv6](/load-balancing/docs/https/convert-applb-dualstack)

- [Convert your existing proxy Network Load Balancer to IPv6](/load-balancing/docs/tcp/convert-proxynetlb-dualstack)

This feature is available in **General Availability**.



## October 21, 2024


Feature 


Internal and external passthrough Network Load Balancers now support connection draining for UDP and other non-TCP protocol traffic.

For details, see [Enable connection draining](/load-balancing/docs/enabling-connection-draining).

This feature is available in **Preview**.



## October 18, 2024


Change 


Previously, the classic external Application Load Balancer had lenient HTTP/2 request parsing 
that did not reject requests containing certain invalid characters in the request path. The same requests would have been rejected if they had arrived over HTTP/1 or HTTP/3.

Now, all HTTP requests, including HTTP/2 requests, are rejected if the path contains a character that isn't one of the following:

- 

An allowed ASCII character specified in [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986), sections 3.3 and 3.4.

- 

One of the following special allowed characters: `[ ] { } | ^`

All other characters must be properly [URL encoded](https://www.w3schools.com/tags/ref_urlencode.ASP).

You can identify rejected requests in the proxy logs by looking for the following:

- `responseCode`: 400

- `response_code_details`: `invalid_http2_client_request_path`




Feature 


You can now use the Google Cloud Console to create the following load balancers in Premium Tier:

- Regional external Application Load Balancer

- Regional external proxy Network Load Balancer

Previously, only Standard Tier support was available in the Console.



## September 30, 2024


Feature 


The regional external Application Load Balancers, cross-region internal Application Load Balancers, regional internal Application Load Balancers, now support a configurable *client HTTP keepalive timeout*. The client HTTP keepalive timeout represents the maximum amount of time that a TCP connection can be idle between the (downstream) client and the target HTTP(S) proxy.

For details, see

- External Application Load Balancers: [Client HTTP keepalive timeout](/load-balancing/docs/https#http-keepalive-timeout)

- Internal Application Load Balancers: [Client HTTP keepalive timeout](/load-balancing/docs/l7-internal#http-keepalive-timeout)

This capability is available in **General Availability**.



## September 16, 2024


Feature 


Envoy-based Application Load Balancers now support authorization policies that let you establish access control checks for incoming traffic. For details, see [Authorization policy](/load-balancing/docs/auth-policy/auth-policy-overview).

This feature is available in **Preview**.



## August 28, 2024


Deprecated 


**The Global external Application Load Balancer and the Classic Application Load Balancer will no longer support TLS sessionID resumption. They continue to support modern forms of TLS resumption.**

The TLS protocol supports an optimization which allows a client reconnecting to a server with which it has communicated before to perform a cheaper *abbreviated handshake*. This optimization is available in several modes, which include the modern [PSK](https://datatracker.ietf.org/doc/html/rfc8446#section-2.2) and [ticket](https://datatracker.ietf.org/doc/html/rfc5077) mechanisms, as well as the long-obsolete [sessionID](https://datatracker.ietf.org/doc/html/rfc5246) mechanism.

The Global external Application Load Balancer and the Classic Application Load Balancer are the only Google Cloud products that currently support the obsolete sessionID mechanism.

This sessionID mechanism is going to be disabled over the next 4-5 weeks. Clients that currently make use of sessionID will transparently fall back to full TLS handshakes. To recover the performance optimization gains, we recommend that you upgrade clients to modern TLS libraries which support the PSK or ticket mechanisms.



## August 05, 2024


Feature 


Regional external Application Load Balancer, regional internal Application Load Balancer, and cross-region internal Application Load Balancer support mutual TLS (mTLS).

With mTLS, the load balancer requests that the client send a certificate to authenticate itself during the TLS handshake with the load balancer. You can configure a trust store to validate the client certificate's chain of trust.

For details, see the following:

- [Mutual TLS authentication](/load-balancing/docs/mtls)

- [Set up mutual TLS with user-provided certificates](/load-balancing/docs/https/setting-up-mtls-ccm)

- [Set up mutual TLS with a private CA](/load-balancing/docs/https/setting-up-mtls-ca-ccm)

This capability is in **General Availability**.

The global external Application Load Balancer and the classic Application Load Balancer already support frontend mTLS (General Availability).



## July 31, 2024


Feature 


Cloud Load Balancing now supports failover for global, classic, and regional external Application Load Balancers. Failover is handled by creating two or more regional external Application Load Balancers in the regions where you want the traffic to failover to. *Only regional external Application Load Balancers can be used as failover backup load balancers.*

For details, see [Failover for external Application Load Balancers](/load-balancing/docs/https/applb-failover-overview).

This feature is available in **Preview**.



## July 29, 2024


Feature 


All the Application Load Balancers, except the classic Application Load Balancer, now support *stateful cookie-based session affinity*. When you use stateful cookie-based affinity, the load balancer includes an HTTP cookie in the `Set-Cookie` response header of the initial HTTP request. 

For details, see [Stateful cookie-based session affinity](/load-balancing/docs/backend-service#stateful-session-affinity).

This capability is in **Preview**.



## July 19, 2024


Feature 


Regional external Application Load Balancers, cross-region internal Application Load Balancers, regional internal Application Load Balancers, regional internal proxy Network Load Balancers, cross-region internal proxy Network Load Balancers, and regional external proxy Network Load Balancers support IPv4 and IPv6 (dual-stack) backends.

Ingress IPv4 traffic can now be proxied over an IPv4 or IPv6 connection to the IPv4 and IPv6 (dual-stack) backends.

The following backends support dual stack:

- VM instance group

- Zonal NEGs (GCE_VM_IP_PORT)

You can now convert the load balancers from IPv4 based deployments to dual stack (IPv4 and IPv6) deployments. 

For details, see:

- 

[IPv6 overview](/load-balancing/docs/ipv6)

- 

[Convert Application Load Balancer to IPv6](/load-balancing/docs/https/convert-applb-dualstack)

- 

[Convert proxy Network Load Balancer to IPv6](/load-balancing/docs/tcp/convert-proxynetlb-dualstack)

This feature is available in **Preview**.



## July 15, 2024


Feature 


Cloud Load Balancing introduces advanced cost, latency, and resiliency optimizations for your global external Application Load Balancers. These include the following capabilities:

- You can use a *service load balancing policy* to customize the parameters that influence how traffic is distributed within the backends associated with a backend service (for example, load balancing algorithm and auto-capacity draining).

- You can designate specific backends as *preferred backends*.

For details, see [Advanced load balancing optimizations](/load-balancing/docs/service-lb-policy).

This feature is in **General Availability**.



## June 14, 2024


Feature 


You can now access backend services residing in different projects than the external or internal Application Load Balancers with cross-project service referencing.

For details, see:

- 

[Set up a global external Application Load Balancer with Shared VPC](/load-balancing/docs/https/set-up-global-ext-https-shared-vpc)

- 

[Set up regional external Application Load Balancers with Shared VPC](/load-balancing/docs/https/setting-up-reg-ext-shared-vpc)

- 

[Set up an internal Application Load Balancer with Shared VPC](/load-balancing/docs/l7-internal/l7-internal-shared-vpc)

This feature is available in **General Availability**.



## June 03, 2024


Feature 


Bring your own IP lets you [bring your own public IPv6 addresses](/vpc/docs/bring-your-own-ip#comparison) to Google Cloud. IPv6 BYOIP addresses can be used with [external passthrough Network Load Balancers](/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6). Bring your own IP for IPv6 addresses is available in **General Availability**.