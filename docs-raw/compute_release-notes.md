# Compute Engine release notes

Source: https://berlin.devsitetest.how/compute/docs/release-notes
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

Resources

](https://berlin.devsitetest.how/compute/docs/resources)












# Compute Engine release notes 






- On this page 
- [ June 26, 2026 ](#June_26_2026)
- [ June 22, 2026 ](#June_22_2026)
- [ May 01, 2026 ](#May_01_2026)
- [ April 16, 2026 ](#April_16_2026)
- [ April 15, 2026 ](#April_15_2026)
- [ April 02, 2026 ](#April_02_2026)
- [ March 23, 2026 ](#March_23_2026)
- [ March 19, 2026 ](#March_19_2026)
- [ March 11, 2026 ](#March_11_2026)
- [ March 04, 2026 ](#March_04_2026)
- [ February 12, 2026 ](#February_12_2026)
- [ February 09, 2026 ](#February_09_2026)
- [ December 22, 2025 ](#December_22_2025)
- [ December 14, 2025 ](#December_14_2025)
- [ December 10, 2025 ](#December_10_2025)
- [ November 24, 2025 ](#November_24_2025)
- [ November 18, 2025 ](#November_18_2025)
- [ November 10, 2025 ](#November_10_2025)
- [ November 04, 2025 ](#November_04_2025)
- [ November 02, 2025 ](#November_02_2025)
- [ October 30, 2025 ](#October_30_2025)
- [ October 21, 2025 ](#October_21_2025)
- [ October 20, 2025 ](#October_20_2025)
- [ October 18, 2025 ](#October_18_2025)
- [ October 17, 2025 ](#October_17_2025)
- [ October 16, 2025 ](#October_16_2025)
- [ October 06, 2025 ](#October_06_2025)
- [ June 30, 2025 ](#June_30_2025)
- [ June 27, 2025 ](#June_27_2025)
- [ March 26, 2025 ](#March_26_2025)
- [ March 10, 2025 ](#March_10_2025)
- [ March 04, 2025 ](#March_04_2025)
- [ January 29, 2025 ](#January_29_2025)
- [ January 20, 2025 ](#January_20_2025)
- [ January 17, 2025 ](#January_17_2025)
- [ December 10, 2024 ](#December_10_2024)
- [ November 26, 2024 ](#November_26_2024)
- [ November 05, 2024 ](#November_05_2024)
- [ October 30, 2024 ](#October_30_2024)
- [ October 16, 2024 ](#October_16_2024)
- [ October 15, 2024 ](#October_15_2024)
- [ October 09, 2024 ](#October_09_2024)
- [ September 26, 2024 ](#September_26_2024)
- [ June 18, 2024 ](#June_18_2024)
- [ June 17, 2024 ](#June_17_2024)
- [ June 14, 2024 ](#June_14_2024)
- [ June 13, 2024 ](#June_13_2024)
- [ June 12, 2024 ](#June_12_2024)
- [ June 11, 2024 ](#June_11_2024)
- [ June 05, 2024 ](#June_05_2024)
- [ June 04, 2024 ](#June_04_2024)
- [ May 31, 2024 ](#May_31_2024)
- 














This page contains the latest release notes for features and updates to the
Compute Engine service.

The following release notes are also available for Compute Engine:

- [Guest environment release notes](/compute/docs/images/guest-environment/release-notes):
contains feature rollouts and updates for the guest agent and other
essential software required for your instances to function correctly on
Compute Engine.

- [The archive](/compute/docs/release-notes-archive): contains older release
notes.

**Latest API version: v1**







You can see the latest product updates for all of Google Cloud Dedicated in Germany on the
[
Google Cloud Dedicated](/release-notes) page, browse and filter all release notes in the
[Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/release-notes),
or programmatically access release notes in
[BigQuery](https://console.cloud.berlin-build0.goog/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table).













To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the
[feed URL](https://berlin.devsitetest.how/feeds/compute-release-notes.xml) directly.









## June 26, 2026


Feature 


**Generally available**: In a managed instance group (MIG), you can use a health
check to monitor your application health without triggering repairs for an
unhealthy VM, if the application fails the health check. You can prevent the MIG
from repairing an unhealthy VM by turning off autohealing. For more information,
see [Turn off repairs in a MIG](/compute/docs/instance-groups/turn-off-vm-repairs-in-mig).



## June 22, 2026


Feature 


**Generally available**: You can create instances all at once in a regional
managed instance group (MIG) by using resize requests. For more information, see
[About resize requests in a MIG](/compute/docs/instance-groups/about-resize-requests-mig).



## May 01, 2026


Feature 


**Generally available**:
Compute Engine has enabled support of Spot VMs in Google Cloud
Dedicated universes. Spot VMs are available for C3, M3, and A3
machine series. Use Spot VMs for workloads that can withstand
preemption to receive a discount of up to 60% off the on-demand price.
For the latest pricing information, see the
[pricing page](https://berlin.devsitetest.how/spot-vms/pricing).

For information about how Spot VMs work, see
[Spot VMs](/compute/docs/instances/spot) and
[Create and use Spot VMs](/compute/docs/instances/create-use-spot).



## April 16, 2026


Feature 


**Generally available**: You can rotate the customer-managed encryption key
(CMEK) used to encrypt a disk, standard snapshot, or archive snapshot to a new key version without
downtime.

**Generally available**: You can change the CMEK used to encrypt a disk, standard
snapshot, or archive snapshot to a different key without downtime.

For more information, see
[Rotate the CMEK for a disk or standard snapshot](/compute/docs/disks/customer-managed-encryption#rotate_encryption)
and
[Change the CMEK for a disk or standard snapshot](/compute/docs/disks/customer-managed-encryption#change-key).



## April 15, 2026


Announcement 


You can view the physical location of your Compute Engine instances in a zone
to understand your cluster topology. This information helps you reduce network
latency between your compute instances. For more information, see
[View Compute Engine instance topology](/compute/docs/instances/view-instance-topology).



Feature 


**Generally available**: You can control the physical location of the
Compute Engine instances in a MIG by using workload policies. Workload
policies help you to, for example, place your compute instances close together
to minimize network latency when running AI or ML workloads. For more
information, see
[About workload policies in MIGs](/compute/docs/instance-groups/about-workload-policies).



## April 02, 2026


Feature 


**Preview**: To control the use of the deprecated container startup agent, an option for
deploying containers on Compute Engine instances, you can enforce the
`constraints/compute.managed.disableVmsWithContainerStartupAgent` organization
policy constraint. This constraint prevents the creation of
Compute Engine instances that use the container startup
agent and the `gce-container-declaration` metadata.

You can also enforce this organization policy in dry-run mode to identify
projects that use the deprecated metadata, without blocking resource creation.

For more information, see [Prevent the creation of VMs that use the container
metadata](/compute/docs/containers/prevent-konlet-vms) and [Migrate containers
deployed on VMs during VM creation](/compute/docs/containers/migrate-containers).



## March 23, 2026


Feature 


**Preview**: The instance flexibility policy of a managed instance group (MIG)
lets you override the minimum CPU platform and disk definition that is specified
in the MIG's instance template. With these overrides, you can select machine
types that run on different CPU platforms and that have different architectures.

For more information, see [About instance flexibility in MIGs](/compute/docs/instance-groups/about-instance-flexibility#overrides-for-instance-properties).



## March 19, 2026


Breaking 


**Changed**: The following operations on the boot disk of a Compute Engine instance
that has a service account attached require the `iam.serviceAccounts.actAs` permission
on the service account. In the following list, the boot disk of such an instance is
referred to as the *source disk*.

- Creating a standard or archive snapshot of the source disk, including application
consistent snapshots

- Cloning the source disk

- Creating a machine image of the instance

- Creating a custom image of the source disk

- Starting asynchronous replication of the source disk to another region

- Creating a new disk when you create an instance, if the new disk is
created from an instant snapshot of the source disk

If you already have the Compute Instance Admin (v1)
(`roles/compute.instanceAdmin.v1`) role and the Service Account User (v1)
(`roles/iam.serviceAccountUser`) role on the project, no action is required.

Otherwise, ask your administrator to grant you the `iam.serviceAccounts.actAs`
permission on the service account. For instructions, see
[Manage access to other resources](/iam/docs/manage-access-other-resources).



## March 11, 2026


Issue 


To address high-severity kernel vulnerabilities (including [CVE-2025-21756](https://nvd.nist.gov/vuln/detail/CVE-2025-21756) and [CVE-2025-38052](https://nvd.nist.gov/vuln/detail/CVE-2025-38052)) in Rocky Linux 8 and 9, updates are available for the Compute Engine images maintained by [CIQ](https://ciq.com/products/rocky-linux/). If your VM instances use images dated before September 2025 (version `v20250912`), you must take action to ensure you continue to receive security patches.

**How to determine if your Compute Engine VMs are affected**

You are affected if your VM instance uses a Rocky Linux image from an `-optimized-gcp` or `-optimized-gcp-nvidia` family with a version date older than `v20250912` (for example, `rocky-linux-9-optimized-gcp-v20250807`). To check your VM's source image, see View [VM instance image details](/compute/docs/instances/view-vm-image). You can view details for these image families in [Rocky Linux OS details](/compute/docs/images/os-details#rocky_linux).

**Action required**

- 

**If your image version is** `v20250912` **or later:** Your VM is already configured to use the newer [SIG/Cloud Next (SCN)](https://docs.ciq.com/scn/) repositories and is receiving security updates. **No action is required.**

- 

**If your image version is older than** `v20250912`: Your VM is configured to use legacy [SIG/Cloud](https://sig-cloud.rocky.page/) repositories that no longer receive regular kernel updates and won't receive future security patches. While running `sudo dnf update` applies a one-time patch for the vulnerabilities listed, you **must** manually migrate the VM to the SCN repositories to receive ongoing updates by following the [CIQ migration guide](https://docs.ciq.com/scn/#migration-from-sigcloud).




## March 04, 2026


Feature 


**Generally available**: You can use managed constraints with Organization Policy Service
for centralized, programmatic control of your Compute Engine resources.
Managed constraints replace legacy `compute.*` constraints and are identifiable
by the `compute.managed.*` prefix. They also include built-in support for safe
rollout tools like Policy Simulator and dry run mode.

For more information, see
[Organization policies for Compute Engine](/compute/docs/access/organization-policies)
and
[Managed constraints](/compute/docs/access/managed-constraints).



## February 12, 2026


Feature 


**Generally available**: You can use instance flexibility to improve resource
availability when creating VMs in bulk in a region. With instance flexibility,
you specify one or more suitable machine types for your workload.
Compute Engine then provisions VMs from the list of machine types based
on capacity and quota availability.

For more information, see
[About instance flexibility for VMs created in bulk](/compute/docs/instances/multiple/about-instance-flexibility-for-bulk-vms)
and
[Create VMs in bulk with instance flexibility](/compute/docs/instances/multiple/create-in-bulk-with-instance-flexibility).



## February 09, 2026


Feature 


You can autoscale a managed instance group (MIG) that
has instance flexibility configured. Autoscaling lets the MIG create or
delete virtual machine instances based on an increase or decrease in load. For
more information, see
[About instance flexibility](/compute/docs/instance-groups/about-instance-flexibility#instance_flexibility_and_autoscaling).



## December 22, 2025


Feature 


When you autoscale a regional managed instance group (MIG), you can view the
reasons why the autoscaler adds or removes VMs in your MIG. Autoscaling
reasons were previously available only for zonal MIGs. For more information, see
[Viewing autoscaler logs](/compute/docs/autoscaler/viewing-autoscaler-logs).



## December 14, 2025


Feature 


Instance flexibility in regional managed instance
groups (MIGs) support the `ANY` target distribution shape. Selecting this shape
lets you maximize resource obtainability and the utilization of unused zonal
reservations. For more information, see
[About instance flexibility in MIGs](/compute/docs/instance-groups/about-instance-flexibility).



## December 10, 2025


Fixed 


If you clone a source disk that's encrypted with a customer-supplied encryption
key or customer-managed encryption key, you must use the same key to encrypt the
clone.

For more information, see [Create a clone of an encrypted source disk](/compute/docs/disks/clone-duplicate-disks#encrypted-source).



## November 24, 2025


Feature 


**Public Preview**: You can now access the VM metadata server using IPv6 connectivity
from single-stack IPv6 VM instances. For more information, see
[About VM metadata](/compute/docs/metadata/overview).



## November 18, 2025


Feature 


You can autoscale a regional managed instance group
(MIG) that has the target distribution shape set to `ANY` or `ANY_SINGLE_ZONE`.
These shapes are particularly beneficial for batch workloads.
For more information about target distribution shapes, see
[Regional MIG target distribution shape](/compute/docs/instance-groups/regional-mig-distribution-shape).



## November 10, 2025


Issue 


The Windows guest agent identifies administrator accounts and groups using
string matching. Therefore, credential management features only function
correctly when you use English language names for user accounts and groups,
for example, `Administrators`. If you use non-English language names, credential
management features such as generating or resetting passwords might not function
as expected. For more information about managing Windows user accounts, see
[Manage accounts and credentials on Windows VMs](/compute/docs/instances/windows/generating-credentials) and
[Known issues for Windows VM instances](/compute/docs/troubleshooting/known-issues#windows-non-english-credentials).



## November 04, 2025


Feature 


**Generally available**: You can verify which reservation a VM consumes and
view a list of VMs that consume a reservation. For more information,
see [View reservation consumption](/compute/docs/instances/reservations-view#view_reservation_consumption).



## November 02, 2025


Feature 


If you need to synchronize time with high accuracy and monitor its accuracy for
your Compute Engine instances, you can sync your VM clock with its host
server clock using `chrony` and `ptp_kvm`. This configuration provides accuracy
within 1 ms for supported setups. For more information, see
[Configure accurate time for Compute Engine VMs](/compute/docs/instances/time-synchronization).



## October 30, 2025


Feature 


**Generally available**: Dynamic NICs let you add or remove network interfaces
to or from an instance without restarting or recreating the instance.

You can also use Dynamic NICs when you need more network interfaces. The
maximum number of vNICs for most machine types in Google Cloud is 10; however,
you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

- [Multiple network interfaces overview](/vpc/docs/multiple-interfaces-concepts)

- [Create VM instances with multiple network interfaces](/vpc/docs/create-use-multiple-interfaces)

- [Add Dynamic NICs to an instance](/vpc/docs/add-dynamic-nics)



## October 21, 2025


Feature 


**Generally available**: Future reservations let you reserve capacity for a
specific date up to one year in advance. For more information, see
[About future reservation requests](/ai-hypercomputer/docs/reserve-capacity).



Change 


As part of the consolidation of CIQ's kernel trees, the kernel `dist-tag` that supports the Rocky Linux Optimized and Accelerator images on Compute Engine is changing from `elX_ycld_next` to `elX_y_ciq`. There are no changes to Secure Boot or GPG signing keys.

For example, `6.12.0-55.32.1.el10_0cld_next.2.1` changes to `6.12.0-55.39.1.el10_0_ciq.2.1`, where `ciq` replaces the `cld_next` tag.

This change affects the Rocky Linux 8, 9, and 10 optimized and accelerator images in an upcoming kernel update over the next month. The major version 8 and 9 kernels now include FIPS 140-3 patches as part of CIQ's ongoing FIPS 140-3 validation efforts for Rocky Linux. These patches have no effect if FIPS mode is not enabled. There are no code changes to the major version 10 kernel.

You can find the kernel source tree in the CIQ [kernel-src-tree](https://github.com/ctrliq/kernel-src-tree) GitHub repository.



## October 20, 2025


Feature 


**Generally Available**: The G4
[accelerator-optimized machine series](/compute/docs/accelerator-optimized-machines#g4-series)
is designed for graphics-intensive workloads such as NVIDIA Omniverse simulations,
video transcoding, and virtual desktops. The G4 machine series also provides a
cost-effective solution for single-host inference and model tuning.
The G4 machine series is now available in the following regions and zones:

- APAC

- Jurong West, Singapore: `asia-southeast1-b`

- Europe

- Eemshaven, Netherlands: `europe-west4-a`

- North America

- Council Bluffs, Iowa: `us-central1-b`

- Ashburn, Virginia: `us-east4-c`

- Columbus, Ohio: `us-east5-c`

To get started with G4 machine types, see
[Create a G2 or G4 instance](/compute/docs/gpus/create-gpu-vm-g-series).



## October 18, 2025


Feature 


**Generally Available**: You can use the Compute Engine alpha API at the
project level through a self-service process. By enabling the alpha API, you can
use the Google Cloud Dedicated console, Google Cloud CLI, API, and Terraform to view and manage
preview features. For more information, see [Use the Compute Engine alpha API](/compute/docs/reference/rest/alpha).



## October 17, 2025


Feature 


**Generally Available**: You can use the Compute Engine alpha API at the
project level through a self-service process. By enabling the alpha API, you can
use the Google Cloud Dedicated console, Google Cloud CLI, API, and Terraform to view and manage
preview features. For more information, see [Use the Compute Engine alpha API](/compute/docs/reference/rest/alpha).



## October 16, 2025


Change 


Starting with SUSE Linux Enterprise Server (SLES) 16, including variants for SAP, the default file system for the root partition (`/`) is [Btrfs](https://en.wikipedia.org/wiki/Btrfs), which replaces the previous default of XFS. For more information, see [File systems in SLES](https://documentation.suse.com/sles/15-SP7/html/SLES-all/cha-filesystems.html#sec-filesystems-major-btrfs-suse) in the SUSE documentation.



## October 06, 2025


Change 


The Google Cloud optimized (`-optimized-gcp`) and accelerated
(`optimized-gcp-nvidia-*`) versions of the Rocky Linux images include the
[CIQ SIG/Cloud Next repository](https://docs.ciq.com/rlc/ciq-sig-cloud-next/),
which provides a cloud-optimized kernel. The accelerated
images also include the [CIQ SIG/Cloud Next Nonfree
repository](https://gitlab.com/ctrl-iq-public/sig-cloud-next/next-nonfree),
which provides proprietary GPU drivers for the cloud-optimized kernel.

This update applies to images created on or after September 12, 2025.

For more information about Rocky Linux OS images, see [Rocky
Linux](/compute/docs/images/os-details#rocky_linux) on
the operating system details page.



## June 30, 2025


Feature 


**Generally available**: You can now modify licenses attached to your disks. Previously, licenses on disk resources were immutable. You had to delete and recreate disks, or engage our support team to change licenses.

This feature provides greater flexibility for managing your disk licenses. You can now:

- Append, remove, replace, and view the history of license updates.

- Perform in-place license upgrades, such as [Ubuntu to Ubuntu Pro](/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu), using the `gcloud` CLI and REST.

- [Switch from PAYG to BYOS billing](/compute/docs/licenses/switch-between-payg-and-byos) models.

- Review [license changes and restrictions](/compute/docs/licenses/license-changes-and-restrictions) and [append a RHEL ELS](/compute/docs/images/premium/rhel/append-els-licenses) license to a newer version.

For more information on how to manage licenses, see [Manage licenses](/compute/docs/licenses/manage).



## June 27, 2025


Feature 


**Generally available**: You can specify a custom ephemeral external IPv6 address when creating an instance. For more information, see [Create instances that use IPv6 addresses](/compute/docs/instances/create-ipv6-instance).



## March 26, 2025


Feature 


**Generally available**: You can specify a custom ephemeral internal IPv6 address when creating an instance. For more information, see [Create instances that use IPv6 addresses](/compute/docs/instances/create-ipv6-instance).



## March 10, 2025


Feature 


**Generally available**: Configure the host error detection time, which is the maximum amount of time Compute Engine waits to restart or terminate an instance after detecting that the instance is unresponsive. For more information, see [Set VM host maintenance policy](/compute/docs/instances/setting-vm-host-options).



## March 04, 2025


Feature 


**Generally available:** Stockholm, Sweden, Europe `(europe-north2-a,b,c)` has launched with [N4, C3D highmem, C4 highmem, and E2](/compute/docs/general-purpose-machines) machine types available in all three zones. For more information, see [Cloud locations](https://berlin.devsitetest.how/about/locations) and [VM instance pricing](https://berlin.devsitetest.how/compute/vm-instance-pricing).



## January 29, 2025


Feature 


**Preview:** You can now modify which machine types are recommended, so that the generated recommendations only include your preferred machine series. You can also change the metrics used to generate memory recommendations to improve the accuracy of the recommendations. For more information, see [Configure machine type recommendations](/compute/docs/instances/configure-machine-type-recommendations).



## January 20, 2025


Feature 


**Generally available**: Managed instance groups (MIGs) let you create pools of suspended and stopped virtual machine (VM) instances. You can manually suspend and stop VMs in a MIG to save on costs, or use suspended and stopped pools to speed up scale out operations of your MIG. For more information, see [About suspending and stopping VMs in a MIG](/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig).



## January 17, 2025


Feature 


Compute Engine is enabled for use with Cloud KMS Autokey.

Using keys generated by Autokey can help you consistently align with industry
standards and recommended practices for data security, including the HSM
protection level, separation of duties, key rotation, location, and key
specificity. Keys requested using Autokey function identically to other
Cloud HSM keys with the same settings.

For more information, see [About disk encryption](/compute/docs/disks/disk-encryption). To learn more
about Cloud KMS Autokey, see
[Autokey overview](/kms/docs/autokey-overview).



## December 10, 2024


Feature 


**Generally available**: Instance flexibility in a managed instance group (MIG) lets you configure multiple machine types in the group. This can improve resource availability for applications that require large-scale capacity and high-demand hardware. Support for Terraform has also been added. For more information, see [About instance flexibility in MIGs](/compute/docs/instance-groups/about-instance-flexibility).



## November 26, 2024


Feature 


**Preview:** Use the disk performance status metric to monitor the health of your Hyperdisk or Persistent Disk volumes. This metric indicates whether your disks might be affected by adverse events within Compute Engine.

To learn more, see [Monitor disk health](/compute/docs/disks/disk-health).



## November 05, 2024


Feature 


**Generally available**: An updated version of the gVNIC driver for Windows offers improved network performance and support for Jumbo frames. For more information, see [Update to the latest gVNIC driver for Windows](/compute/docs/networking/using-gvnic#windows-os-upgrade).



## October 30, 2024


Feature 


**Generally available**: You can autoscale a regional MIG with a BALANCED target distribution shape. With the BALANCED shape, the autoscaler is aware of the capacity in each zone and creates VMs in zones that have resource availability. For more information, see [Autoscaling a regional MIG](/compute/docs/instance-groups/regional-migs#autoscaling_a_regional_mig).



## October 16, 2024


Deprecated 


**End of life:** On October 31, 2024, SLES 12 SP5 and SLES 12 SP5 for SAP are reaching end of life and the images will be deprecated on Google Cloud. If you use SLES 12 SP5 or SLES 12 SP5 for SAP images in your project, review [Long Term Service Support Pack (LTSS) options](/compute/docs/images/premium/sles-faq#ltss).



## October 15, 2024


Feature 


**Generally available**: In addition to the A3 High machine type that has 8 NVIDIA H100 GPUs attached, we now have smaller machine types available that have 1, 2, or 4 NVIDIA H100 GPUs attached. These smaller machine types are ideal for workloads such as inference, simulations, and small-scale training.

To get started, review [A3 High machine types](/compute/docs/accelerator-optimized-machines#a3-standard-vms).



## October 09, 2024


Feature 


**Public preview**: Instance flexibility in a managed instance group (MIG) lets you configure multiple machine types in the group. This can improve resource availability for applications that require large-scale capacity and high-demand hardware. For more information, see
[About instance flexibility in MIGs](/compute/docs/instance-groups/about-instance-flexibility).



## September 26, 2024


Deprecated 


OS Login POSIX groups support is deprecated. For more information, see [OS Login POSIX groups support deprecation](/compute/docs/deprecations/oslogin-groups).



## June 18, 2024


Change 


Preemptible allocation quotas also apply to some temporary GPU VMs. This behavior can help you improve quota obtainability for temporary GPU VMs while maintaining the benefits of uninterrupted run time of the standard provisioning model. For more information, see [GPU VMs and preemptible allocation quotas](/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas).



Fixed 


The issue related to creating C2 sole tenant nodes with more than 60 CPUs.



## June 17, 2024


Feature 


**Generally available**: You can now use the **Require OS Config** organization policy constraint to automatically enable VM Manager for all new VMs in your organization, folder, or project. For more information, see [Enable VM Manager using an organization policy](/compute/docs/manage-os#enable-vmm-org-policy).



## June 14, 2024


Change 


[Spot VMs](/compute/docs/instances/spot) are now available for the [H3 machine series](/compute/docs/compute-optimized-machines#h3_series).



## June 13, 2024


Feature 


**Preview**: C3 bare metal machine types are available in Preview in the C3 machine series. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. With bare metal instances, you can access all the raw compute resources of the server. For more information, see the [C3 machine series](/compute/docs/general-purpose-machines#c3_series).



## June 12, 2024


Feature 


**Preview**: [General Purpose C4 VM](/compute/docs/general-purpose-machines) instances are now available in Public Preview on the [Intel Emerald Rapids CPU](/compute/docs/cpu-platforms). The C4 machine series offers consistently high performance with up to 192 vCPUs and 1.5 TB of DDR5 memory, and support for [Hyperdisk](/compute/docs/disks/hyperdisks) storage.



Change 


**Expanded Hyperdisk Balanced support for M3 and C3 machine types**: The maximum number of Hyperdisk Balanced volumes that you can use with C3 and M3 virtual machines has been increased, as follows:

- C3 VMs with 4 or 8 vCPUs now support attaching up to 16 Hyperdisk Balanced volumes.

- C3 VMs with 16 or more vCPUs support 32 Hyperdisk Balanced volumes.

- M3 virtual machines support up to 32 Hyperdisk Balanced volumes, up from 2. 

For more information, see the documentation for [M3](/compute/docs/memory-optimized-machines?#m3_disks) and [C3](/compute/docs/general-purpose-machines#c3_disks) VMs.



## June 11, 2024


Change 


**Generally available**: The [A3 Mega accelerator-optimized machine type](/compute/docs/accelerator-optimized-machines#a3-mega-vms) is now available. The A3 Mega machine type has NVIDIA® H100 80GB GPUs attached and provides twice the network bandwidth speed when compared to A3 Standard. A3 Mega VMs can be used to support your large artificial intelligence (AI) models, machine learning (ML), and high performance computing (HPC) workloads. The A3 machine type is available in the following regions and zones:

- APAC

- Singapore: `asia-southeast1-b`

- Europe

- Netherlands: `europe-west4-b,c`

- North America

- Iowa: `us-central1-a,c`

- Virginia: `us-east4-a,b`

- Ohio:`us-east5-a`

- Oregon: `us-west1-a,b`

- Nevada: `us-west4-a`

To get started with A3 Mega VMs, see [Run large-scale model training and fine-tuning](/compute/docs/gpus/overview#large-scale-ai).



Feature 


C3 and C3D VMs are available in the following [regions and zones](/compute/docs/regions-zones#available):

C3:

- `asia-northeast1-b` Tokyo, Japan

- `europe-west3-b,c` Frankfurt, Germany

- `us-west1-a,b` The Dalles, OR

- `us-west2-a` Los Angeles, CA

- `us-south1-a` Dallas, TX

C3D:

- `australia-southeast1-c` Sydney, Australia

- `europe-west3-c` Frankfurt, Germany

- `us-west4-a` Las Vegas, NV




## June 05, 2024


Issue 


You can't provision C2 sole tenant nodes with 60 vCPUs. For details, see [Known issues](/compute/docs/troubleshooting/known-issues).



## June 04, 2024


Feature 


You can now order and request quota for X4 bare metal instances. You create bare metal instances using a new predefined machine type for the X4 memory-optimized machine series. X4 instances can be used to host the largest production SAP HANA databases. For more information, see the [X4 machine series](/compute/docs/memory-optimized-machines#x4_series).



## May 31, 2024


Issue 


Creating a larger (>90 vCPUs) C3D `standard-lssd` or `highmem-lssd` VM results in an error message. See [Known issues](/compute/docs/troubleshooting/known-issues) for the workaround. Larger C3D VMs that don't require `-lssd` are not impacted.