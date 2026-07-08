# About SSH connections

Source: https://berlin.devsitetest.how/compute/docs/instances/ssh
Last updated: 2026-07-07

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/compute/docs/tpc-differences) for more details.














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

Compute

](https://berlin.devsitetest.how/docs/compute-area)






- 








[

Compute Engine

](https://berlin.devsitetest.how/compute/docs)






- 








[

Guides

](https://berlin.devsitetest.how/compute/docs/overview)












# About SSH connections 






- On this page 
- [ Metadata-managed SSH connections ](#metadata)
- [ What's next? ](#whats_next)
- 






















Compute Engine uses key-based SSH authentication to establish connections to
Linux virtual machine (VM) instances and additionally supports
[certificate-based authentication for OS Login VMs](/compute/docs/oslogin/certificates).
You can optionally enable SSH for Windows VMs. By default, passwords aren't
configured for local users on Linux VMs.

Before you can connect to a VM, several configurations must be performed. If you
use the Google Cloud Dedicated console or the Google Cloud CLI to connect to your VMs,
Compute Engine performs these configurations on your behalf.





## Metadata-managed SSH connections

Compute Engine uses custom project and/or instance metadata to
configure SSH keys and to manage SSH access.

Click each tab to learn more about the configurations Compute Engine performs
before it grants SSH connections when you use the Google Cloud Dedicated console, the
gcloud CLI, or third-party tools to connect to VMs. If you connect to
VMs without using the Google Cloud Dedicated console or the gcloud CLI, you must
perform some configurations yourself.


[ Console ](#console) [ gcloud ](#gcloud) [ Third-party tools ](#third-party-tools) 
More 




- You use the [SSH button in the
Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/compute/instances) to [connect
to your VM](/compute/docs/instances/connecting-to-instance#console).

- Compute Engine sets a username and creates an ephemeral SSH key pair with the
following configuration:




- Your username is set as the username in your Google Account. For example, if the email
address associated with your Google Account is `cloudysanfrancisco@gmail.com`, then
your username is `cloudysanfrancisco`.


- Your public and private SSH keys are stored in your browser session.

- Your SSH key has an expiry of three minutes. Three minutes after Compute Engine creates the
key, you can't use the SSH key to connect to the VM anymore.



- Compute Engine authenticates your SSH key and grants your connection.

- Compute Engine uploads the public SSH key and username to metadata.

- Compute Engine retrieves the SSH key and username from metadata, creates a
user account with the username, and on Linux VMs, stores the public key in your
user's `~/.ssh/authorized_keys` file on the VM. On Windows VMs, Compute Engine
doesn't store the public key on the VM.

- Compute Engine grants your connection.




- You use the `gcloud compute ssh` command to
[connect to your VM](/compute/docs/instances/connecting-to-instance#gcetools).

- Compute Engine sets a username and creates a persistent SSH key pair with the
following configurations:




- Your username is set as the username in your local machine.


- Your public SSH key is stored in project metadata. If Compute Engine can't store the SSH
key in project metadata, for example, because `block-project-ssh-keys` is set to
`TRUE`, Compute Engine stores the SSH key in instance metadata.

- Your private SSH key is stored on your local machine.

- Your SSH key doesn't have an expiry. It is used for all future SSH connections you make,
unless you configure a new key.



- Compute Engine authenticates your SSH key and grants your connection.

- Compute Engine uploads the public SSH key and username to metadata.

- Compute Engine retrieves the SSH key and username from metadata, creates a
user account with the username, and on Linux VMs, stores the public key in your
user's `~/.ssh/authorized_keys` file on the VM. On Windows VMs, Compute Engine
doesn't store the public key on the VM.

- Compute Engine grants your connection.




- You create an SSH key pair and username. See
[
Create SSH keys](/compute/docs/connect/create-ssh-keys) for details.

- You upload the public key and username to metadata.
See [
Add SSH keys to VMs that use metadata-based SSH keys](/compute/docs/connect/add-ssh-keys#metadata) for details.

- You connect to the VM.

- Compute Engine retrieves the SSH key and username from metadata, creates a
user account with the username, and on Linux VMs, stores the public key in your
user's `~/.ssh/authorized_keys` file on the VM. On Windows VMs, Compute Engine
doesn't store the public key on the VM.

- Compute Engine grants your connection.




## What's next?

- Learn how to [Manage SSH keys in metadata](/compute/docs/instances/adding-removing-ssh-keys).

- Learn how to [Connect to VMs](/compute/docs/instances/connecting-to-instance).

- To find methods and tools for diagnosing and resolving failed SSH connections,
see [Troubleshooting SSH](/compute/docs/troubleshooting/troubleshooting-ssh).