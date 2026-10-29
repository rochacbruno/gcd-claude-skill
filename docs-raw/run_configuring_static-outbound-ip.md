# Static outbound IP address

Source: https://berlin.devsitetest.how/run/docs/configuring/static-outbound-ip
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/run/docs/tpc-differences) for more details.














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

Application hosting

](https://berlin.devsitetest.how/docs/application-hosting)






- 








[

Cloud Run

](https://berlin.devsitetest.how/run/docs)






- 








[

Guides

](https://berlin.devsitetest.how/run/docs/overview/what-is-cloud-run)












# Static outbound IP address 















By default, Cloud Run workloads connect to external endpoints on the
internet using a regional pool of dynamic IP addresses shared across all
serverless workloads. Because other workloads share this pool, you shouldn't
rely on it when you need a predictable origin IP address or isolated IP
reputation.

Configure your Cloud Run workloads to route outbound requests
using a dedicated static IP address in the following situations:

- You connect to an external database or API that uses an IP address allowlist
or firewall.

- You connect to reputation-sensitive external endpoints, such as payment
gateways, hosted databases, or partner APIs protected by third-party web
application firewalls (WAFs). Noisy traffic from another tenant on the
default shared IP pool can degrade IP reputation and cause external WAFs to
block or throttle your requests.

- You run authorized network scanning, port enumeration, host fingerprinting,
vulnerability probing, web scraping, or load testing workloads.

To send outbound requests from a dedicated static IP address, configure your
Cloud Run service to use [Direct VPC egress](/run/docs/configuring/vpc-direct-vpc).

## Task overview

To route requests using a static IP address, configure the service's
[VPC egress](/run/docs/configuring/connecting-vpc) to send all outbound traffic
(`--vpc-egress=all-traffic`) through a [VPC network](/vpc/docs).
Attach a [Cloud NAT](/nat/docs) gateway to that network with your reserved static
IP address.

In this tutorial, you configure Cloud NAT in manual mode and assign a
single static IP address to it. If your workloads scale to many container
instances or open many concurrent connections, such as during authorized network
scanning, assign multiple static IP addresses to Cloud NAT. You can
also increase the minimum ports per container instance or enable dynamic port
allocation to prevent port exhaustion. Learn more about how Cloud NAT
gateways use [IP addresses and ports](/nat/docs/ports-and-addresses).

Routing your traffic through [Cloud NAT](/nat/docs) doesn't add an extra hop
in your networking stack because the Cloud NAT gateway and the
Cloud Router provide only a control plane, and packets don't pass through
the NAT gateway or the Cloud Router.

## Configure network address translation (NAT)

If you use Direct VPC egress, requests
from your Cloud Run service arrive at your VPC network.
If you want to route outbound requests to external endpoints using a static IP,
configure a [Cloud NAT](/nat/docs) gateway.



### gcloud

- 

Create a new Cloud Router to program a Cloud NAT gateway:


```
gcloud compute routers create ROUTER_NAME \ 
--network = NETWORK_NAME \ 
--region = REGION 
```


Replace the following:

- ` ROUTER_NAME `: a name for the
Cloud Router resource that you want to create.

- ` NETWORK_NAME `: the name of the
VPC network that you found earlier.

- ` REGION `: the region that you want to
create a Cloud NAT gateway in.

- 

Reserve a static IP address. A reserved IP address resource retains
the underlying IP address when the resource it is associated with is
deleted and re-created:


```
gcloud compute addresses create ORIGIN_IP_NAME --region = REGION 
```


Replace the following:

- ` ORIGIN_IP_NAME `: the name that you want to
assign to the IP address resource.

- ` REGION `: the [region](/run/docs/locations)
that will run the Cloud NAT router. Use the same region as your
Cloud Run service to minimize latency and network costs.

- 

Create a Cloud NAT gateway configuration on this router to
route the traffic originating from the VPC network using
the static IP address that you created:


```
gcloud compute routers nats create NAT_NAME \ 
--router = ROUTER_NAME \ 
--region = REGION \ 
--nat-custom-subnet-ip-ranges = SUBNET_NAME \ 
--nat-external-ip-pool = ORIGIN_IP_NAME 
```


Replace the following:

- ` NAT_NAME `: a name for the Cloud NAT
gateway resource that you want to create.

- ` ROUTER_NAME `: the name of your
Cloud Router.

- ` REGION `: the region that you want to
create a Cloud NAT gateway in.

- ` SUBNET_NAME `: the name of your subnet.

- ` ORIGIN_IP_NAME `: the name of the reserved IP
address resource that you created in the previous step.



### Terraform

To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).

- 

Create a new Cloud Router to program a Cloud NAT gateway:






















```
resource "google_compute_router" "default" { 
name = "cr-static-ip-router" 
network = google_compute_network.default.name 
region = google_compute_subnetwork.default.region 
} 
```



Replace `cr-static-ip-router` with your subnet name.

- 

Reserve a static IP address. A reserved IP address resource retains
the underlying IP address when the resource it is associated with is
deleted and recreated:






















```
resource "google_compute_address" "default" { 
name = "cr-static-ip-addr" 
region = google_compute_subnetwork.default.region 
} 
```



Replace `cr-static-ip-addr` with your subnet name.

- 

Create a Cloud NAT gateway configuration on this router to
route the traffic originating from the VPC network using
the static IP address that you created:






















```
resource "google_compute_router_nat" "default" { 
name = "cr-static-nat" 
router = google_compute_router.default.name 
region = google_compute_subnetwork.default.region 

nat_ip_allocate_option = "MANUAL_ONLY" 
nat_ips = [ google_compute_address.default.self_link ] 

source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS" 
subnetwork { 
name = google_compute_subnetwork.default.id 
source_ip_ranges_to_nat = [ "ALL_IP_RANGES" ] 
} 
} 
```



Replace `cr-static-nat` with your Cloud NAT gateway name.




## Route Cloud Run traffic through the VPC network

After Cloud NAT is configured, deploy or update your Cloud Run
service with [Direct VPC egress](/run/docs/configuring/vpc-direct-vpc), and set the VPC egress to
[route all traffic through the VPC network](/run/docs/configuring/connecting-vpc):



### gcloud

**Direct VPC egress**

To deploy or update your Cloud Run service to use Direct VPC
egress and route all egress traffic through it, run the following command:


```
gcloud run deploy SERVICE_NAME \ 
--image = IMAGE_URL \ 
--network = NETWORK \ 
--subnet = SUBNET \ 
--region = REGION \ 
--vpc-egress = all-traffic
```


Replace the following:

- SERVICE_NAME : the name of the
Cloud Run service that you want to deploy.

- ` IMAGE_URL `: a reference to the container image, for
example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry,
the [repository](/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must
already be created. The URL follows the format of ` LOCATION -docker.pkg.dev/ PROJECT_ID / REPO_NAME / PATH : TAG `
.

- NETWORK : the name of your VPC network.

- SUBNET : the name of your subnet.

- REGION : a region for your service.



### YAML

**Direct VPC egress**

- 

If you are creating a new service, skip this step.
If you are updating an existing service, download its [YAML configuration](/run/docs/reference/yaml/v1):


```
gcloud run services describe SERVICE --format export > service.yaml
```


- 

Update as needed.

```
apiVersion : serving.knative.dev/v1 
kind : Service 
metadata : 
name : SERVICE 
spec : 
template : 
metadata : 
annotations : 
run.googleapis.com/network-interfaces : '[{"network":" NETWORK ","subnetwork":" SUBNET "}]' 
run.googleapis.com/vpc-access-egress : all-traffic 
spec : 
containers : 
- image : IMAGE_URL 
```


Replace the following:

- SERVICE : the name of the Cloud Run
service.

- NETWORK : the name of your VPC network.

- SUBNET : the name of your subnet.

- IMAGE_URL : the URL of your service container image.

- 

Create or update the service using the following command:


```
gcloud run services replace service.yaml
```


The `gcloud run services replace` command defaults to using `service.yaml` file if present.



### Terraform

To learn how to apply or remove a Terraform configuration, see
[Basic Terraform commands](/docs/terraform/basic-commands).

**Direct VPC egress**

This Cloud Run service uses Direct VPC egress and
routes all egress traffic through it:






















```
resource "google_cloud_run_v2_service" "default" { 
name = "cloudrun-service" 
location = "us-central1" 

deletion_protection = false # set to "true" in production 

template { 
containers { 
image = "us-docker.pkg.dev/cloudrun/container/hello" 
} 
vpc_access { 
network_interfaces { 
network = "default" 
subnetwork = "default" 
tags = [ "tag1", "tag2", "tag3" ] 
} 
} 
} 
} 
```



Replace `us-docker.pkg.dev/cloudrun/container/hello` with a reference to
your container image.



## Verify the static external IP address

After completing the previous steps, you have set up Cloud NAT on your
VPC network with a predefined static IP address, and you have
routed all of your Cloud Run service's outbound traffic into your
VPC network. Requests from your Cloud Run service travel
through your VPC network and reach external endpoints using
the static IP address.

To verify this behavior and confirm the origin IP address that your service
uses, you can make a request to an API or a website such as [curlmyip.org](https://curlmyip.org)
that shows the originating IP address.

## Deleting the static external IP address

If you no longer need a static external IP address, see [Release a static external IP address](/vpc/docs/reserve-static-external-ip-address#release_ip).