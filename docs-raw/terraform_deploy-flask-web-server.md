# Deploy a basic Flask web server by using Terraform

Source: https://berlin.devsitetest.how/docs/terraform/deploy-flask-web-server
Last updated: 2026-07-07

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/terraform/tpc-differences) for more details.














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

Developer tools

](https://berlin.devsitetest.how/docs/costs-usage)






- 








[

Terraform on Google Cloud

](https://berlin.devsitetest.how/docs/terraform)






- 








[

Guides

](https://berlin.devsitetest.how/docs/terraform/terraform-overview)












# Deploy a basic Flask web server by using Terraform 






- On this page ** 
- [ Costs ](#costs)
- [ Before you begin ](#before-you-begin)

- [ Select or create a project ](#select_or_create_a_project)
- [ Set up permissions ](#permissions)
- [ Enable the API ](#enable-api)
- [ Install gcloud CLI ](#install-cli)

- [ Create the Compute Engine VM ](#create-vm)

- [ Create the directory ](#prep)
- [ Create the Virtual Private Cloud network and subnet ](#vpc)
- [ Create the Compute Engine VM resource ](#vm)
- [ Initialize Terraform ](#init)
- [ Validate the Terraform configuration ](#plan)
- [ Apply the configuration ](#apply)

- [ Run a web server on Google Cloud Dedicated ](#run-web-server)

- [ Add a custom SSH firewall rule ](#ssh-firewall-rule)
- [ Connect to the VM with SSH ](#ssh)
- [ Build the Flask app ](#flask)
- [ Open port 5000 on the VM ](#open-port)
- [ Add an output variable for the web server URL ](#output)

- [ Troubleshooting ](#troubleshooting)
- [ Clean up ](#clean-up)
- 










In this tutorial, you learn how to get started with Terraform by using Terraform
to create a basic web server on Compute Engine.

In this tutorial, you do the following:

- Use Terraform to create a VM in Google Cloud Dedicated.

- Start a basic Python Flask server.

## Costs 






In this document, you use the following billable components of Google Cloud Dedicated in Germany:








[
Compute Engine](https://berlin.devsitetest.how/compute/all-pricing)














When you finish the tasks that are described in this document, you can avoid
continued billing by deleting the resources that you created. For more information, see
[Clean up](#clean-up).

## Before you begin

Prepare to start the tutorial.

### Select or create a project





- 


In the Google Cloud Dedicated console, go to the project selector page.



[Go to project selector](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)




- 


Select or create a Google Cloud Dedicated project.




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














### Set up permissions

Make sure that you have the necessary [
Compute Engine permissions](/compute/docs/access/iam) on your user account:

- `compute.instances.*`

- `compute.firewalls.*`

[
Go to the IAM page](https://console.cloud.berlin-build0.goog/iam-admin/iam)

[Learn more](/iam/docs) about roles and permissions.

### Enable the API




Enable the Compute Engine API.






**Roles required to enable APIs**


To enable APIs, you need the Service Usage Admin IAM
role (`roles/serviceusage.serviceUsageAdmin`), which
contains the `serviceusage.services.enable` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=compute.googleapis.com)

### Install gcloud CLI

To use the Terraform from a local development environment, install and
initialize the Google Cloud CLI, and then set up Application Default
Credentials with your user credentials:


- 
[Install](/sdk/docs/install) the gcloud CLI.


- 
[Initialize](/sdk/docs/initialize) gcloud CLI:

```
gcloud init
```



- Create local authentication credentials for your account:

```
gcloud auth application-default login
```



## Create the Compute Engine VM

First, you define the VM's settings in a Terraform configuration file. Then, you
run Terraform commands to create the VM in your project.

### Create the directory

Create a new directory. In your new directory, create a
`main.tf` file for the Terraform configuration. The contents of this file
describe all of the Google Cloud Dedicated resources to be created in the project.


```
mkdir tf-tutorial && cd tf-tutorial
```



```
nano main.tf
```


### Create the Virtual Private Cloud network and subnet

In this section, you create a Virtual Private Cloud (VPC) network and subnet for the VM's
network interface.

Add the following Terraform resources to the `main.tf` file that you created:

- [`google_compute_network`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network) 

- [`google_compute_subnetwork`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork) 




















```
resource "google_compute_network" "vpc_network" {
name = "my-custom-mode-network"
auto_create_subnetworks = false
mtu = 1460
}

resource "google_compute_subnetwork" "default" {
name = "my-custom-subnet"
ip_cidr_range = "10.0.1.0/24"
region = "us-west1"
network = google_compute_network.vpc_network.id
}
```



### Create the Compute Engine VM resource

In this section, you create a single Compute Engine instance running
Debian. In this tutorial, you use the smallest
[machine type](/compute/docs/machine-types) that's available. Later, you can
upgrade to a larger machine type.

Add the following [`google_compute_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) Terraform resource to the `main.tf` file that you created.




















```
# Create a single Compute Engine instance
resource "google_compute_instance" "default" {
name = "flask-vm"
machine_type = "f1-micro"
zone = "us-west1-a"
tags = ["ssh"]

boot_disk {
initialize_params {
image = "debian-cloud/debian-11"
}
}

# Install Flask
metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python3-pip rsync; pip install flask"

network_interface {
subnetwork = google_compute_subnetwork.default.id

access_config {
# Include this section to give the VM an external IP address
}
}
}
```



The sample code sets the Google Cloud Dedicated zone to `us-west1-a`. You can change
this to a different [zone](/compute/docs/regions-zones#available).

### Initialize Terraform

At this point, you can run `terraform init` to add the necessary plugins and
build the `.terraform` directory.


```
terraform init
```


Output:


```
Initializing the backend...

Initializing provider plugins...
...

Terraform has been successfully initialized!
```


### Validate the Terraform configuration

Optionally, you can validate the Terraform code that you've built so far. Run
`terraform plan`, which does the following:

- Verifies that the syntax of `main.tf` is correct

- Shows a preview of the resources that will be created


```
terraform plan
```


Output:


```
...

Plan: 1 to add, 0 to change, 0 to destroy.

Note: You didn't use the -out option to save this plan, so Terraform can't
guarantee to take exactly these actions if you run "terraform apply" now.
```


### Apply the configuration

To create the VM, run `terraform apply`.


```
terraform apply
```


When prompted, enter `yes`.

Terraform calls Google Cloud Dedicated APIs to set up the new VM. Check the
[VM instances page](https://console.cloud.berlin-build0.goog/compute/instances) to
see the new VM.

## Run a web server on Google Cloud Dedicated

Your next steps are getting a web application created, deploying it to the
VM, and creating a firewall rule to allow client requests to the web
application.

### Add a custom SSH firewall rule

The `default-allow-ssh` firewall rule in the `default` network lets you use
SSH to connect to the VM. If you'd rather use your own custom firewall
rule, you can add the following resource at the end of your `main.tf` file:




















```
resource "google_compute_firewall" "ssh" {
name = "allow-ssh"
allow {
ports = ["22"]
protocol = "tcp"
}
direction = "INGRESS"
network = google_compute_network.vpc_network.id
priority = 1000
source_ranges = ["0.0.0.0/0"]
target_tags = ["ssh"]
}
```



Run `terraform apply` to create the firewall rule.

### Connect to the VM with SSH

Validate that everything is set up correctly at this point by connecting to the
VM with SSH.

- 

Go to the [VM Instances page](https://console.cloud.berlin-build0.goog/compute/instances).

- 

Find the VM with the name `flask-vm`.

- 

In **Connect** column, click **SSH**.

An SSH-in-browser terminal window opens for the running VM.

For more information, see [Connecting to
VMs](/compute/docs/instances/connecting-to-instance).

### Build the Flask app

You build a [Python Flask app](http://flask.pocoo.org/) for this tutorial so
that you can have a single file describing your web server and test endpoints.

- 

In the SSH-in-browser terminal, create a file called `app.py`.


```
nano app.py
```


- 

Add the following to the `app.py` file:


```
from flask import Flask 
app = Flask ( __name__ ) 

@app . route ( '/' ) 
def hello_cloud (): 
return 'Hello Cloud!' 

app . run ( host = '0.0.0.0' ) 
```


- 

Run `app.py`:


```
python3 app.py
```


Flask serves traffic on `localhost:5000` by default.

- 

Open a second SSH connection:

- Go to the [VM Instances page](https://console.cloud.berlin-build0.goog/compute/instances).

- Find the VM named `flask-vm` and click **SSH**.

- 

In the second SSH connection, run `curl` to confirm that the greeting that
you configured in `app.py` is returned.


```
curl http://0.0.0.0:5000
```


The output from this command is `Hello Cloud`.

### Open port 5000 on the VM

To connect to the web server from your local computer, the VM must have
port 5000 open. Google Cloud Dedicated lets you open ports to traffic by using
firewall rules.

Add the following [`google_compute_firewall`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall) Terraform resource at the end of your `main.tf` file.




















```
resource "google_compute_firewall" "flask" {
name = "flask-app-firewall"
network = google_compute_network.vpc_network.id

allow {
protocol = "tcp"
ports = ["5000"]
}
source_ranges = ["0.0.0.0/0"]
}
```



Run `terraform apply` to create the firewall rule.

### Add an output variable for the web server URL

- 

At the end of `main.tf`, add [a Terraform output
variable](https://www.terraform.io/language/values/outputs) 
to output the web server URL:


```
// A variable for extracting the external IP address of the VM
output "Web-server-URL" {
value = join("",["http://",google_compute_instance.default.network_interface.0.access_config.0.nat_ip,":5000"])
}
```


- 

Run `terraform apply`.


```
terraform apply
```


When prompted, enter `yes`. Terraform prints the VM's external IP
address and port 5000 to the screen, as follows:


```
Web-server-URL = "http:// IP_ADDRESS :5000"
```


At any time, you can run `terraform output` to return this
output:


```
terraform output
```


- 

Click the URL from the previous step, and see the "Hello Cloud!" message.

This means that your server is running.

## Troubleshooting

- 

If a required API isn't enabled, Terraform returns an error. The error message
includes a link to enable the API. After enabling the API, you can rerun
`terraform apply`.

- 

If you can't connect to your VM through SSH:

- Make sure to add the [SSH firewall rule](#ssh-firewall-rule).

- Make sure that your VM includes the `tags = ["ssh"]` argument.

## Clean up

After completing the tutorial, you can delete everything that you
created so that you don't incur any further costs.

Terraform lets you remove all the resources defined in the configuration file by
running the `terraform destroy` command:


```
terraform destroy
```


Enter `yes` to allow Terraform to delete your resources.