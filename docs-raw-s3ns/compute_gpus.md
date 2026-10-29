# GPU machine types

Source: https://documentation.s3ns.fr/compute/docs/gpus
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/compute/docs/tpc-differences) for more details.














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

Compute

](https://documentation.s3ns.fr/docs/compute-area)






- 








[

Compute Engine

](https://documentation.s3ns.fr/compute/docs)






- 








[

Guides

](https://documentation.s3ns.fr/compute/docs/overview)












# GPU machine types 



























This document outlines the NVIDIA GPU models that you can use to
accelerate machine learning (ML), data processing, and graphics-intensive
workloads on your Compute Engine instances. This
document also details which GPUs come pre-attached to accelerator-optimized
machine series such as A4X Max, A4X, A4, A3, A2, G4, and G2, and which GPUs you
can attach to N1 general-purpose instances.

Use this document to compare the performance, memory, and features of different
GPU models. For a more detailed overview of the accelerator-optimized machine
family, including information on CPU platforms, storage options, and networking
capabilities, and to find the specific machine type that matches your workload,
see [Accelerator-optimized machine family](/compute/docs/accelerator-optimized-machines).

For more information about GPUs on Compute Engine, see
[About GPUs](/compute/docs/gpus/about-gpus).

To view available regions and zones for GPUs on Compute Engine, see
[GPUs regions and zone availability](/compute/docs/gpus/gpu-regions-zones).





## Overview



Compute Engine offers different machine types to support your various
workloads.

Some machine types support
[NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/).
When you create an instance that uses NVIDIA RTX Virtual Workstation,
Compute Engine automatically adds a vWS license. For information about pricing
for virtual workstations, see the
[GPU pricing page](https://documentation.s3ns.fr/compute/gpus-pricing).




| 
**GPU machine types** | 
|

| 
AI and ML workloads | 
Graphics and visualization | 
Other GPU workloads | 
|

| 

**Accelerator-optimized A series machine types** are designed for high
performance computing (HPC), artificial intelligence (AI), and machine
learning (ML) workloads.


The later generation A series are ideal for pre-training and fine-tuning
foundation models that involves large clusters of accelerators, while the A2
series can be used for training smaller models and single host inference.



For these machine types, the GPU model is automatically attached to the instance.

| 

**Accelerator-optimized G series machine types** are designed for workloads
such as NVIDIA Omniverse simulation workloads, graphics-intensive applications,
video transcoding, and virtual desktops. These machine types support
[NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/).


The G series can also be used for training smaller models and for
single-host inference.



For these machine types, the GPU model is automatically attached to the instance.

| 



For N1 general-purpose machine types, except for the N1 shared-core
(`f1-micro` and `g1-small`), you can attach a select
set of GPU models. Some of these GPU models also support NVIDIA RTX Virtual
Workstations (vWS).

| 
|

| 




- [A4X Max](/compute/docs/accelerator-optimized-machines#a4x-vms)
(NVIDIA GB300 Ultra Superchips) 
(`nvidia-gb300`)

- [A4X](/compute/docs/accelerator-optimized-machines#a4x-vms)
(NVIDIA GB200 Superchips) 
(`nvidia-gb200`)

- [A4](/compute/docs/accelerator-optimized-machines#a4-vms)
(NVIDIA B200) 
(`nvidia-b200`)

- [A3 Ultra](/compute/docs/accelerator-optimized-machines#a3-ultra-vms)
(NVIDIA H200) 
(`nvidia-h200-141gb`)

- [A3 Mega](/compute/docs/accelerator-optimized-machines#a3-mega-vms)
(NVIDIA H100) 
(`nvidia-h100-mega-80gb`)

- [A3 High](/compute/docs/accelerator-optimized-machines#a3-high-vms)
(NVIDIA H100) 
(`nvidia-h100-80gb`)

- [A3 Edge](/compute/docs/accelerator-optimized-machines#a3-edge-vms)
(NVIDIA H100) 
(`nvidia-h100-80gb`)

- [A2 Ultra](/compute/docs/accelerator-optimized-machines#a2-ultra-vms)
(NVIDIA A100 80GB) 
(`nvidia-a100-80gb`)

- [A2 Standard](/compute/docs/accelerator-optimized-machines#a2-standard-vms)
(NVIDIA A100 4OGB) 
(`nvidia-tesla-a100`)


| 




- [G4](/compute/docs/accelerator-optimized-machines#g4-series) (NVIDIA RTX PRO 6000) 
(`nvidia-rtx-pro-6000`) 
(`nvidia-rtx-pro-6000-vws`)

- [G2](/compute/docs/accelerator-optimized-machines#g2-vms) (NVIDIA L4) 

(`nvidia-l4`) 
(`nvidia-l4-vws`)


| 
The following GPU models can be attached to N1 general-purpose machine
types:



- NVIDIA T4 
(`nvidia-tesla-t4`) 
(`nvidia-tesla-t4-vws`). NVIDIA T4 is approaching end
of support, see
[NVIDIA T4 end of support](/compute/docs/eol/t4-eos).

- NVIDIA P4 
(`nvidia-tesla-p4`) 
(`nvidia-tesla-p4-vws`). NVIDIA P4 is approaching end
of support, see
[NVIDIA P4 end of support](/compute/docs/eol/p4-eos).

- NVIDIA V100 
(`nvidia-tesla-v100`)


| 
|



You can also use some GPU machine types on
[AI Hypercomputer](/ai-hypercomputer/docs/overview). AI Hypercomputer is a
supercomputing system that is optimized to support your artificial intelligence
(AI) and machine learning (ML) workloads. This option is recommended for creating a
densely allocated, performance-optimized infrastructure that has integrations
for Google Kubernetes Engine (GKE) and Slurm schedulers.

## A4X Max and A4X machine series

The [A4X Max and A4X machine series](/compute/docs/accelerator-optimized-machines#a4x-vms)
runs on an exascale platform based on
[NVIDIA's rack-scale architecture](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)
and is optimized for compute and memory-intensive, network-bound ML training and
HPC workloads. A4X Max and A4X differ primarily in their GPU and networking
components. A4X Max is available only as bare metal instances, which provide
direct access to the host server's CPU and memory, without the Compute Engine
hypervisor layer.

### A4X Max machine types (NVIDIA GB300)


[A4X Max accelerator-optimized](/compute/docs/accelerator-optimized-machines#a4x-vms)

machine types use NVIDIA GB300 Grace Blackwell Ultra Superchips (`nvidia-gb300`) and
are ideal for foundation model training and serving. A4X Max machine types are available
as [bare metal instances](/compute/docs/instances/bare-metal-instances).




A4X Max is an exascale platform based on
[NVIDIA GB300
NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/). Each machine has two sockets with NVIDIA Grace CPUs with Arm
Neoverse V2 cores. These CPUs are connected to four NVIDIA B300 Blackwell GPUs with fast
chip-to-chip ([NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/))
communication. For information about machine type limitations, see
[A4X Max and A4X limitations](/compute/docs/accelerator-optimized-machines#a4x-limitations).





| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Attached Local SSD (GiB) | 
Physical NIC count | 
Maximum network bandwidth (Gbps) | 
NVIDIA GB300 GPU count | 
GPU memory (GB HBM3e) | 
|



| 
`a4x-maxgpu-4g-metal` | 
144 | 
960 | 
12,000 | 
6 | 
3,600 | 
4 | 
1,116 | 
|



#### A4X Max machine type notes

The following notes apply to the preceding table:


- **vCPU count**: a vCPU is implemented as a single hardware hyper-thread on one of
the available [CPU platforms](/compute/docs/cpu-platforms).

- **Maximum network bandwidth**: maximum egress bandwidth can't exceed the number given. Actual
egress bandwidth depends on the destination IP address and other factors.
For more information about network bandwidth,
see [Network bandwidth](/compute/docs/network-bandwidth).

- **GPU memory**: GPU memory is the memory on a GPU device that can be used for
temporary storage of data. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

### A4X machine type (NVIDIA GB200)


[A4X accelerator-optimized](/compute/docs/accelerator-optimized-machines#a4x-vms)

machine types use NVIDIA GB200 Grace Blackwell Superchips (`nvidia-gb200`) and
are ideal for foundation model training and serving.




A4X is an exascale platform based on
[NVIDIA GB200
NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/). Each machine has two sockets with NVIDIA Grace CPUs with Arm
Neoverse V2 cores. These CPUs are connected to four NVIDIA B200 Blackwell GPUs with fast
chip-to-chip ([NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/))
communication. For information about machine type limitations, see
[A4X Max and A4X limitations](/compute/docs/accelerator-optimized-machines#a4x-limitations).





| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Attached Local SSD (GiB) | 
Physical NIC count | 
Maximum network bandwidth (Gbps) | 
NVIDIA GB200 GPU count | 
GPU memory (GB HBM3e) | 
|



| 
`a4x-highgpu-4g` | 
140 | 
884 | 
12,000 | 
6 | 
2,000 | 
4 | 
744 | 
|



#### A4X machine type notes

The following notes apply to the preceding table:


- **vCPU count**: a vCPU is implemented as a single hardware hyper-thread on one of
the available [CPU platforms](/compute/docs/cpu-platforms).

- **Maximum network bandwidth**: maximum egress bandwidth can't exceed the number given. Actual
egress bandwidth depends on the destination IP address and other factors.
For more information about network bandwidth,
see [Network bandwidth](/compute/docs/network-bandwidth).

- **GPU memory**: GPU memory is the memory on a GPU device that can be used for
temporary storage of data. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

## A4 machine series (NVIDIA B200)

[A4 accelerator-optimized](/compute/docs/accelerator-optimized-machines#a4-vms)

machine types have
[NVIDIA B200 Blackwell GPUs](https://www.nvidia.com/en-us/data-center/b200/)
(`nvidia-b200`) attached and are ideal for foundation model
training and serving. For information about machine type limitations, see
[A4 limitations](/compute/docs/accelerator-optimized-machines#a4-limitations).




| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Attached Local SSD (GiB) | 
Physical NIC count | 
Maximum network bandwidth (Gbps) | 
NVIDIA B200 Blackwell GPU count | 
GPU memory (GB HBM3e) | 
|



| 
`a4-highgpu-8g` | 
224 | 
3,968 | 
12,000 | 
10 | 
3,600 | 
8 | 
1,440 | 
|



### A4 machine type notes

The following notes apply to the preceding table:


- **vCPU count**: a vCPU is implemented as a single hardware hyper-thread on one of
the available [CPU platforms](/compute/docs/cpu-platforms).

- **Maximum network bandwidth**: maximum egress bandwidth can't exceed the number given. Actual
egress bandwidth depends on the destination IP address and other factors.
For more information about network bandwidth, see
[Network bandwidth](/compute/docs/network-bandwidth).

- **GPU memory**: GPU memory is the memory on a GPU device that can be used for
temporary storage of data. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

## A3 machine series

[A3 accelerator-optimized](/compute/docs/accelerator-optimized-machines#a3-vms)
machine types have NVIDIA H100 SXM or NVIDIA H200 SXM GPUs attached.

### A3 Ultra machine type (NVIDIA H200)

[A3 Ultra](/compute/docs/accelerator-optimized-machines#a3-ultra-vms)
machine types have [NVIDIA H200 SXM GPUs](https://www.nvidia.com/en-us/data-center/h200/)
(`nvidia-h200-141gb`) attached and provide the highest network
performance in the A3 series. A3 Ultra machine types are ideal for foundation model training and
serving. For information about machine type limitations, see
[A3 Ultra limitations](/compute/docs/accelerator-optimized-machines#a3-ultra-limitations).




| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Attached Local SSD (GiB) | 
Physical NIC count | 
Maximum network bandwidth (Gbps) | 
NVIDIA H200 GPU count | 
GPU memory (GB HBM3e) | 
|



| 
`a3-ultragpu-8g` | 
224 | 
2,952 | 
12,000 | 
10 | 
3,600 | 
8 | 
1128 | 
|



#### A3 Ultra machine type notes

The following notes apply to the preceding table:


- **vCPU count**: a vCPU is implemented as a single hardware hyper-thread on one of
the available [CPU platforms](/compute/docs/cpu-platforms).

- **Maximum network bandwidth**: maximum egress bandwidth can't exceed the number given. Actual
egress bandwidth depends on the destination IP address and other factors.
For more information about network bandwidth,
see [Network bandwidth](/compute/docs/network-bandwidth).

- **GPU memory**: GPU memory is the memory on a GPU device that can be used for
temporary storage of data. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

### A3 Mega, High, and Edge machine types (NVIDIA H100)

To use [NVIDIA H100 SXM GPUs](https://www.nvidia.com/en-us/data-center/h100/), you have the following options:

- [A3 Mega](/compute/docs/accelerator-optimized-machines#a3-mega-vms): these machine types have H100 SXM GPUs (`nvidia-h100-mega-80gb`) and are ideal for large-scale training and serving workloads.

- [A3 High](/compute/docs/accelerator-optimized-machines#a3-high-vms): these machine types have H100 SXM GPUs (`nvidia-h100-80gb`) and are well-suited for both training and serving tasks.

- [A3 Edge](/compute/docs/accelerator-optimized-machines#a3-edge-vms): these machine types have H100 SXM GPUs (`nvidia-h100-80gb`), are designed specifically for serving, and are available in a [limited set of regions](/compute/docs/regions-zones/gpu-regions-zones).





### A3 Mega







| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Attached Local SSD (GiB) | 
Physical NIC count | 
Maximum network bandwidth (Gbps) | 
NVIDIA H100 GPU count | 
GPU memory (GB HBM3) | 
|



| 
`a3-megagpu-8g` | 
208 | 
1,872 | 
6,000 | 
9 | 
1,800 | 
8 | 
640 | 
|







### A3 High







| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Attached Local SSD (GiB) | 
Physical NIC count | 
Maximum network bandwidth (Gbps) | 
NVIDIA H100 GPU count | 
GPU memory (GB HBM3) | 
|



| 
`a3-highgpu-1g` | 
26 | 
234 | 
750 | 
1 | 
25 | 
1 | 
80 | 
|

| 
`a3-highgpu-2g` | 
52 | 
468 | 
1,500 | 
1 | 
50 | 
2 | 
160 | 
|

| 
`a3-highgpu-4g` | 
104 | 
936 | 
3,000 | 
1 | 
100 | 
4 | 
320 | 
|

| 
`a3-highgpu-8g` | 
208 | 
1,872 | 
6,000 | 
5 | 
1,000 | 
8 | 
640 | 
|







### A3 Edge







| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Attached Local SSD (GiB) | 
Physical NIC count | 
Maximum network bandwidth (Gbps) | 
NVIDIA H100 GPU count | 
GPU memory (GB HBM3) | 
|



| 
`a3-edgegpu-8g` | 
208 | 
1,872 | 
6,000 | 
5 | 
600 (`asia-south1` and `northamerica-northeast2`) or 400 (all other [A3 Edge regions](/compute/docs/gpus/gpu-regions-zones#view-using-table)) | 
8 | 
640 | 
|








#### A3 Mega, High, and Edge machine type notes

The following notes apply to the preceding table:


- **vCPU count**: a vCPU is implemented as a single hardware hyper-thread on one of
the available [CPU platforms](/compute/docs/cpu-platforms).

- **Maximum network bandwidth**: maximum egress bandwidth can't exceed the number given. Actual
egress bandwidth depends on the destination IP address and other factors.
For more information about network bandwidth,
see [Network bandwidth](/compute/docs/network-bandwidth).

- **GPU memory**: GPU memory is the memory on a GPU device that can be used for
temporary storage of data. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

## A2 machine series (NVIDIA A100)

[A2 accelerator-optimized](/compute/docs/accelerator-optimized-machines#a2_vms)
machine types have [NVIDIA A100 GPUs](https://www.nvidia.com/en-us/data-center/a100/)
attached and are ideal for model fine tuning, large model
and cost optimized inference.

The A2 machine series offers two types:

- *A2 Ultra*: these machine types have A100 80GB GPUs
(`nvidia-a100-80gb`) and Local SSD disks attached.

- *A2 Standard*: these machine types have A100 40GB GPUs
(`nvidia-tesla-a100`) attached. You can also add Local
SSD disks when creating an A2 Standard instance. For the number of disks
you can attach, see
[Machine types that require you to choose a number of Local SSD disks](/compute/docs/disks/local-ssd#lssd_disk_options).





### A2 Ultra






| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Attached Local SSD (GiB) | 
Maximum network bandwidth (Gbps) | 
NVIDIA A100 80GB GPU count | 
GPU memory (GB HBM2e) | 
|



| 
`a2-ultragpu-1g` | 
12 | 
170 | 
375 | 
24 | 
1 | 
80 | 
|

| 
`a2-ultragpu-2g` | 
24 | 
340 | 
750 | 
32 | 
2 | 
160 | 
|

| 
`a2-ultragpu-4g` | 
48 | 
680 | 
1,500 | 
50 | 
4 | 
320 | 
|

| 
`a2-ultragpu-8g` | 
96 | 
1,360 | 
3,000 | 
100 | 
8 | 
640 | 
|







### A2 Standard






| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Local SSD supported | 
Maximum network bandwidth (Gbps) | 
NVIDIA A100 40GB GPU count | 
GPU memory (GB HBM2) | 
|



| 
`a2-highgpu-1g` | 
12 | 
85 | 
Yes | 
24 | 
1 | 
40 | 
|

| 
`a2-highgpu-2g` | 
24 | 
170 | 
Yes | 
32 | 
2 | 
80 | 
|

| 
`a2-highgpu-4g` | 
48 | 
340 | 
Yes | 
50 | 
4 | 
160 | 
|

| 
`a2-highgpu-8g` | 
96 | 
680 | 
Yes | 
100 | 
8 | 
320 | 
|

| 
`a2-megagpu-16g` | 
96 | 
1,360 | 
Yes | 
100 | 
16 | 
640 | 
|








### A2 machine type notes

The following notes apply to the preceding table:


- **vCPU count**: a vCPU is implemented as a single hardware hyper-thread on one of
the available [CPU platforms](/compute/docs/cpu-platforms).

- **Maximum network bandwidth**: maximum egress bandwidth can't exceed the number given. Actual
egress bandwidth depends on the destination IP address and other factors.
For more information about network bandwidth,
see [Network bandwidth](/compute/docs/network-bandwidth).

- **GPU memory**: GPU memory is the memory on a GPU device that can be used for
temporary storage of data. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

## G4 machine series (NVIDIA RTX PRO 6000)




[G4 accelerator-optimized](/compute/docs/accelerator-optimized-machines#g4-series)

machine types use [
NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/) (`nvidia-rtx-pro-6000`)
and are
suitable for NVIDIA Omniverse simulation workloads, graphics-intensive applications, video
transcoding, and virtual desktops. G4 machine types also provide a low-cost solution for
performing single host inference and model tuning compared with A series machine types.




You can also add Titanium SSD disks when you create a G4 instance. For the number of disks
you can attach, see
[Machine types that require you to choose a number of Local SSD disks](/compute/docs/disks/local-ssd#lssd_disk_options).
For information about machine type limitations, see
[G4 limitations](/compute/docs/accelerator-optimized-machines#g4-limitations).


A key feature of the G4 series is support for direct GPU peer-to-peer (P2P) communication
on multi-GPU machine types (`g4-standard-96`, `g4-standard-192`,
`g4-standard-384`). This allows GPUs within the same instance to
exchange data directly over the PCIe bus, without involving the CPU host. For more information about
G4 GPU peer-to-peer communication, see
[G4 GPU peer-to-peer communication](/compute/docs/accelerator-optimized-machines#g4-gpu-p2p).




| 
Machine type | 
vCPU count | 
Instance memory (GB) | 
Maximum Titanium SSD supported (GiB) | 
Physical NIC count | 
Maximum network bandwidth (Gbps) | 
NVIDIA RTX PRO 6000 GPU count | 
GPU memory (GB GDDR7) | 
|



| 
`g4-standard-6` | 
6 | 
22 | 
0 | 
1 | 
20 | 
1/8 | 
12 | 
|

| 
`g4-standard-12` | 
12 | 
45 | 
375 | 
1 | 
20 | 
1/4 | 
24 | 
|

| 
`g4-standard-24` | 
24 | 
90 | 
750 | 
1 | 
20 | 
1/2 | 
48 | 
|

| 
`g4-standard-48` | 
48 | 
180 | 
1,500 | 
1 | 
50 | 
1 | 
96 | 
|

| 
`g4-standard-96` | 
96 | 
360 | 
3,000 | 
1 | 
100 | 
2 | 
192 | 
|

| 
`g4-standard-192` | 
192 | 
720 | 
6,000 | 
1 | 
200 | 
4 | 
384 | 
|

| 
`g4-standard-384` | 
384 | 
1,440 | 
12,000 | 
2 | 
400 | 
8 | 
768 | 
|



### G4 machine type notes

The following notes apply to the preceding table:


- **vCPU count**: a vCPU is implemented as a single hardware hyper-thread on one of
the available [CPU platforms](/compute/docs/cpu-platforms).

- **Maximum network bandwidth**: maximum egress bandwidth can't exceed the number given. Actual
egress bandwidth depends on the destination IP address and other factors.
For more information about network bandwidth, see [Network bandwidth](/compute/docs/network-bandwidth).

- **GPU memory**: GPU memory is the memory on a GPU device that can be used for
temporary storage of data. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

## G2 machine series (NVIDIA L4)

[G2 accelerator-optimized](/compute/docs/accelerator-optimized-machines#g2-vms)
machine types have [NVIDIA L4 GPUs](https://www.nvidia.com/en-us/data-center/l4/)
attached and are ideal for cost-optimized inference, graphics-intensive and
high performance computing workloads.

Each G2 machine type also has a default memory and a custom
memory range. The custom memory range defines the amount of memory that
you can allocate to your instance for each machine type. You can also add Local
SSD disks when creating a G2 instance. For the number of disks
you can attach, see
[Machine types that require you to choose a number of Local SSD disks](/compute/docs/disks/local-ssd#lssd_disk_options).

For information about machine type limitations, see
[G2 limitations](/compute/docs/accelerator-optimized-machines#g2-limitations).




| 
Machine type | 
vCPU count | 
Default instance memory (GB) | 
Custom instance memory range (GB) | 
Max Local SSD supported (GiB) | 
Maximum network bandwidth (Gbps) | 
NVIDIA L4 GPU count | 
GPU memory (GB GDDR6) | 
|



| 
`g2-standard-4` | 
4 | 
16 | 
16 to 32 | 
375 | 
10 | 
1 | 
24 | 
|

| 
`g2-standard-8` | 
8 | 
32 | 
32 to 54 | 
375 | 
16 | 
1 | 
24 | 
|

| 
`g2-standard-12` | 
12 | 
48 | 
48 to 54 | 
375 | 
16 | 
1 | 
24 | 
|

| 
`g2-standard-16` | 
16 | 
64 | 
54 to 64 | 
375 | 
32 | 
1 | 
24 | 
|

| 
`g2-standard-24` | 
24 | 
96 | 
96 to 108 | 
750 | 
32 | 
2 | 
48 | 
|

| 
`g2-standard-32` | 
32 | 
128 | 
96 to 128 | 
375 | 
32 | 
1 | 
24 | 
|

| 
`g2-standard-48` | 
48 | 
192 | 
192 to 216 | 
1,500 | 
50 | 
4 | 
96 | 
|

| 
`g2-standard-96` | 
96 | 
384 | 
384 to 432 | 
3,000 | 
100 | 
8 | 
192 | 
|



### G2 machine type notes

The following notes apply to the preceding table:


- **vCPU count**: a vCPU is implemented as a single hardware hyper-thread on one of
the available [CPU platforms](/compute/docs/cpu-platforms).

- **Maximum network bandwidth**: maximum egress bandwidth can't exceed the number given. Actual
egress bandwidth depends on the destination IP address and other factors.
For more information about network bandwidth,
see [Network bandwidth](/compute/docs/network-bandwidth).

- **GPU memory**: GPU memory is the memory on a GPU device that can be used for
temporary storage of data. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

## N1 machine series

You can attach the following GPU models to an
[N1 machine type](/compute/docs/general-purpose-machines#n1_machines)
with the exception of the [N1 shared-core machine types](/compute/docs/machine-resource#shared-core-types).

Unlike the machine types in the accelerator-optimized machine series, N1 machine
types don't come with a set number of attached GPUs. Instead, you specify the
number of GPUs to attach when creating the instance.

N1 instances with fewer GPUs limit the maximum number of vCPUs. In general, a
higher number of GPUs lets you create instances with a higher number of vCPUs
and memory.

### N1+T4 GPUs

You can attach [NVIDIA T4](https://www.nvidia.com/en-us/data-center/tesla-t4/)
GPUs to N1 general-purpose instances with the following instance configurations.




| 
Accelerator type | 
NVIDIA T4 GPU count | 
GPU memory (GB GDDR6) | 
vCPU count | 
Instance memory (GB) | 
Local SSD supported | 
|



| 
`nvidia-tesla-t4` or `nvidia-tesla-t4-vws` | 
1 | 
16 | 
1 to 48 | 
1 to 312 | 
Yes | 
|

| 
`nvidia-tesla-t4` or `nvidia-tesla-t4-vws` | 
2 | 
32 | 
1 to 48 | 
1 to 312 | 
Yes | 
|

| 
`nvidia-tesla-t4` or `nvidia-tesla-t4-vws` | 
4 | 
64 | 
1 to 96 | 
1 to 624 | 
Yes | 
|



#### N1+T4 machine type notes

The following note applies to the preceding table:


- **GPU memory**: GPU memory is the memory available on a GPU device that you can use
for temporary data storage. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

### N1+P4 GPUs

You can attach
[NVIDIA P4](https://images.nvidia.com/content/pdf/tesla/184457-Tesla-P4-Datasheet-NV-Final-Letter-Web.pdf)
GPUs to N1 general-purpose instances with the following instance configurations.
For instances with attached NVIDIA P4 GPUs, Local SSD disks are only supported
in the `us-central1-c` and `northamerica-northeast1-b` zones.




| 
Accelerator type | 
NVIDIA P4 GPU count | 
GPU memory (GB GDDR5) | 
vCPU count | 
Instance memory (GB) | 
Local SSD supported | 
|



| 
`nvidia-tesla-p4` or `nvidia-tesla-p4-vws` | 
1 | 
8 | 
1 to 24 | 
1 to 156 | 
Yes (`us-central1-c` and `northamerica-northeast1-b` only) | 
|

| 
`nvidia-tesla-p4` or `nvidia-tesla-p4-vws` | 
2 | 
16 | 
1 to 48 | 
1 to 312 | 
Yes (`us-central1-c` and `northamerica-northeast1-b` only) | 
|

| 
`nvidia-tesla-p4` or `nvidia-tesla-p4-vws` | 
4 | 
32 | 
1 to 96 | 
1 to 624 | 
Yes (`us-central1-c` and `northamerica-northeast1-b` only) | 
|



#### N1+P4 machine type notes

The following note applies to the preceding table:


- **GPU memory**: GPU memory is the memory available on a GPU device that you can use
for temporary data storage. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

### N1+V100 GPUs

You can attach [NVIDIA V100](https://www.nvidia.com/en-us/data-center/v100/)
GPUs to N1 general-purpose instances with the following instance configurations.
For instances with attached NVIDIA V100 GPUs, Local SSD disks aren't supported
in the `us-east1-c` zone.




| 
Accelerator type | 
NVIDIA V100 GPU count | 
GPU memory (GB HBM2) | 
vCPU count | 
Instance memory (GB) | 
Local SSD supported | 
|



| 
`nvidia-tesla-v100` | 
1 | 
16 | 
1 to 12 | 
1 to 78 | 
Yes (except `us-east1-c`) | 
|

| 
`nvidia-tesla-v100` | 
2 | 
32 | 
1 to 24 | 
1 to 156 | 
Yes (except `us-east1-c`) | 
|

| 
`nvidia-tesla-v100` | 
4 | 
64 | 
1 to 48 | 
1 to 312 | 
Yes (except `us-east1-c`) | 
|

| 
`nvidia-tesla-v100` | 
8 | 
128 | 
1 to 96 | 
1 to 624 | 
Yes (except `us-east1-c`) | 
|



#### N1+V100 machine type notes

The following note applies to the preceding table:


- **GPU memory**: GPU memory is the memory available on a GPU device that you can use
for temporary data storage. It is separate from the instance's memory and is
specifically designed to handle the higher bandwidth demands of your
graphics-intensive workloads.

### Maintenance experience for N1 instances with GPUs

During the [lifecycle of a
Compute Engine instance](/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple
*host events*.

A host event can include the regular maintenance of
Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also
applies some non-disruptive lightweight upgrades for the hypervisor and network
in the background.

The following table describes the host maintenance features for
N1 with attached GPU

machine types:




| 
Machine type | 
Number of GPUs | 
Typical scheduled maintenance event frequency | 
Maintenance behavior | 
Advanced notification for scheduled maintenance | 

On-demand maintenance | 
Simulate maintenance | 
|











| 
N1+T4 | 
1 or 2 | 
Minimum of 15 days | 
Terminate and restart | 
7 days | 
No | 
Yes | 
|

| 
N1+T4 | 
4 | 
Minimum of 30 days | 
Terminate and restart | 
7 days | 
Yes | 
Yes | 
|

| 
N1+P4 | 
1 or 2 | 
Minimum of 15 days | 
Terminate and restart | 
7 days | 
No | 
Yes | 
|

| 
N1+P4 | 
4 | 
Minimum of 30 days | 
Terminate and restart | 
7 days | 
Yes | 
Yes | 
|

| 
N1+V100 | 
1, 2, or 4 | 
Minimum of 15 days | 
Terminate and restart | 
7 days | 
No | 
Yes | 
|

| 
N1+V100 | 
8 | 
Minimum of 30 days | 
Terminate and restart | 
7 days | 
Yes | 
Yes | 
|





The following notes apply to the preceding table:


- **Typical scheduled maintenance event frequency**: 

The maintenance frequencies shown in the previous table are approximations, not guarantees.
Compute Engine might occasionally perform maintenance more frequently.



## General comparison chart

The following table describes the GPU memory size, feature availability, and
ideal workload types of different GPU models on
Compute Engine.

In the following table, `N/A` indicates that the metric is not applicable or not available for this GPU model.



| 
Machine type (GPU model) | 
GPU memory and bandwidth | 
Interconnect | 
NVIDIA RTX Virtual Workstation (vWS) support | 
Best used for | 
|



| 
A4X Max (GB300) | 
279 GB HBM3e (8 TBps) | 
NVLink Full Mesh (1,800 GBps) | 
No | 
Large-scale distributed training and inference of MoE LLMs, Recommenders, HPC | 
|

| 
A4X (GB200) | 
186 GB HBM3e (8 TBps) | 
NVLink Full Mesh (1,800 GBps) | 
No | 
Large-scale distributed training and inference of LLMs, Recommenders, HPC | 
|

| 
A4 (B200) | 
180 GB HBM3e (8 TBps) | 
NVLink Full Mesh (1,800 GBps) | 
No | 
Large-scale distributed training and inference of LLMs, Recommenders, HPC | 
|

| 
A3 Ultra (H200) | 
141 GB HBM3e (4.8 TBps) | 
NVLink Full Mesh (900 GBps) | 
No | 
Large models with large data tables for ML Training, Inference, HPC,
BERT, DLRM | 
|

| 
A3 Mega, A3 High, A3 Edge (H100) | 
80 GB HBM3 (3.35 TBps) | 
NVLink Full Mesh (900 GBps) | 
No | 
Large models with large data tables for ML Training, Inference, HPC,
BERT, DLRM | 
|

| 
A2 Ultra (A100 80GB) | 
80 GB HBM2e (1.9 TBps) | 
NVLink Full Mesh (600 GBps) | 
No | 
Large models with large data tables for ML Training, Inference, HPC,
BERT, DLRM | 
|

| 
A2 Standard (A100 40GB) | 
40 GB HBM2 (1.6 TBps) | 
NVLink Full Mesh (600 GBps) | 
No | 
ML Training, Inference, HPC | 
|

| 
G4 (RTX PRO 6000) | 
96 GB GDDR7 (1.597 TBps) | 
N/A | 
Yes | 
ML Inference, Training, Remote Visualization Workstations,
Video Transcoding, HPC | 
|

| 
G2 (L4) | 
24 GB GDDR6 (300 GBps) | 
N/A | 
Yes | 
ML Inference, Training, Remote Visualization Workstations,
Video Transcoding, HPC | 
|

| 
N1 (T4) | 
16 GB GDDR6 (320 GBps) | 
N/A | 
Yes | 
ML Inference, Training, Remote Visualization Workstations, Video Transcoding | 
|

| 
N1 (P4) | 
8 GB GDDR5 (192 GBps) | 
N/A | 
Yes | 
Remote Visualization Workstations, ML Inference, and Video Transcoding | 
|

| 
N1 (V100) | 
16 GB HBM2 (900 GBps) | 
NVLink Ring (300 GBps) | 
No | 
ML Training, Inference, HPC | 
|



To compare GPU pricing for the different GPU models and regions available on
Compute Engine, see [GPU pricing](https://documentation.s3ns.fr/compute/gpus-pricing).

## Tensor Core and standard CUDA core performance

The following sections provide performance metrics for each GPU architecture,
separated into vector or standard CUDA cores and Tensor Core performance.

- 

**Tensor Cores**: Tensor performance refers to the throughput specialized
Tensor Cores achieve. These are dedicated hardware units (often called
*matrix units*) designed specifically to accelerate the large
matrix multiply-accumulate operations that form the backbone of deep
learning, training, and inference.

This type of performance is best for deep learning, large language models
(LLMs), and any workload that can be expressed as dense matrix operations.
Tensor Cores provide significantly higher throughput than CUDA cores for the
same data type.

- 

**Vector or standard CUDA cores**: Vector performance refers to the
throughput standard CUDA cores achieve. These are general-purpose units
that operate using a single instruction, multiple threads (SIMT) model,
typically performing operations on individual data elements or vectors.

This type of performance is best for general compute, graphics rendering,
and workloads that don't involve dense matrix math.

### Blackwell architecture

The A4X Max, A4X, A4, and G4 machine types run on NVIDIA's
[Blackwell architecture](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/).





### Tensor Core

NVIDIA's Blackwell architecture, used by these machine types,
introduces Tensor Core support for FP4 precision and expanded INT4
capabilities for high performance in large-model inference.

In the following table, `N/A` indicates that the metric is not
applicable or not available for this GPU model. The following notes also apply:


- **TF32, Mixed FP16/32, INT8, FP8, and FP4**: the Blackwell architecture supports [structural sparsity](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/) for these precision metrics, which can double computational throughput. The performance values in this table assume dense matrix multiplication. If you use structural sparsity, performance is doubled.

- **Mixed FP16/32**: for mixed-precision training, GPUs that run on the Blackwell architecture also support the `bfloat16` data type.



| 
Machine type (GPU model) | 
FP64 (TFLOPS) | 
TF32 (TFLOPS) | 
Mixed FP16/32 (TFLOPS) | 
INT8 (TFLOPS) | 
FP8 (TFLOPS) | 
FP4 (TFLOPS) | 
|



| 
A4X Max (GB300) | 
1.3 | 
1,250 | 
2,500 | 
5,000 | 
5,000 | 
15,000 | 
|

| 
A4X (GB200) | 
45 | 
1,250 | 
2,500 | 
5,000 | 
5,000 | 
10,000 | 
|

| 
A4 (B200) | 
40 | 
1,100 | 
2,250 | 
4,500 | 
4,500 | 
9,000 | 
|

| 
G4 (RTX PRO 6000) | 
N/A | 
233.9 | 
467.8 | 
935.6 | 
935.6 | 
1871.2 | 
|





### Standard CUDA cores

The machine types that use the Blackwell architecture
provide high-performance FP64 and FP32 operations for demanding HPC and AI workloads.

For A4X Max, A4X, and A4, FP16 operations are accelerated by Tensor Cores.
For G4, FP16 performance on standard CUDA cores is
included because graphics workloads, such as rendering and visualization, can
benefit from the reduced memory usage and bandwidth requirements of FP16
precision, even when not using Tensor Cores.

In the following table, `N/A` indicates that the metric is not applicable or
not available for this GPU model. The following note also applies:


- **A4X Max (GB300) FP64**: FP64 performance on GB300 is reduced to prioritize FP4 performance.



| 
Machine type (GPU model) | 
FP64 (TFLOPS) | 
FP32 (TFLOPS) | 
FP16 (TFLOPS) | 
|



| 
A4X Max (GB300) | 
1.39 | 
45 | 
N/A | 
|

| 
A4X (GB200) | 
45 | 
45 | 
N/A | 
|

| 
A4 (B200) | 
40 | 
80 | 
N/A | 
|

| 
G4 (RTX PRO 6000) | 
1.8 | 
117 | 
117 | 
|






### Hopper, Ada Lovelace, and Ampere architectures

The A3 series uses the
[Hopper architecture](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/),
which introduced specialized engines for transformer models. The A2 series uses
the [Ampere architecture](https://www.nvidia.com/en-us/data-center/ampere-architecture/),
providing a balanced foundation for high-performance training and inference.
The G2 series uses the [Ada Lovelace architecture](https://www.nvidia.com/en-us/technologies/ada-architecture/),
which provides versatile and energy-efficient acceleration for AI inference,
video transcoding, and graphics workloads.





### Tensor Core

The Hopper, Ada Lovelace, and Ampere architectures, feature advanced Tensor
Cores that accelerate TF32, FP16, FP8, and INT8 data types, providing high
throughput for mixed-precision training and inference.

In the following table, `N/A` indicates that the metric is not applicable or
not available for this GPU model. The following notes also apply:


- **TF32, Mixed FP16/32, INT8, and FP8**: the Hopper, Ada Lovelace, and Ampere architectures support [structural sparsity](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/) for these precision metrics (and INT4), which can double computational throughput. The performance values in this table assume dense matrix multiplication. If you use structural sparsity, performance is doubled.

- **Mixed FP16/32**: for mixed-precision training, NVIDIA H200, H100, A100, and L4 GPUs also support the `bfloat16` data type.



| 
Machine type (GPU model) | 
FP64 (TFLOPS) | 
TF32 (TFLOPS) | 
Mixed FP16/32 (TFLOPS) | 
INT8 (TOPS) | 
FP8 (TFLOPS) | 
|



| 
A3 Ultra (H200) | 
67 | 
494.5 | 
989.5 | 
1,979 | 
1,979 | 
|

| 
A3 Mega/High/Edge (H100) | 
67 | 
494.5 | 
989.5 | 
1,979 | 
1,979 | 
|

| 
A2 Ultra (A100 80GB) | 
19.5 | 
156 | 
312 | 
624 | 
N/A | 
|

| 
A2 Standard (A100 40GB) | 
19.5 | 
156 | 
312 | 
624 | 
N/A | 
|

| 
G2 (L4) | 
N/A | 
60 | 
121 | 
242.5 | 
121 | 
|





### Standard CUDA cores

The machine types that use the Hopper, Ada Lovelace, and Ampere architectures
provide high-performance FP64 and FP32 operations for demanding HPC and AI workloads.

In the following table, `N/A` indicates that the metric is not
applicable or not available for this GPU model.



| 
Machine type (GPU model) | 
FP64 (TFLOPS) | 
FP32 (TFLOPS) | 
|



| 
A3 Ultra (H200) | 
34 | 
67 | 
|

| 
A3 Mega, High, Edge (H100) | 
34 | 
67 | 
|

| 
A2 Ultra (A100 80GB) | 
9.7 | 
N/A | 
|

| 
A2 Standard (A100 40GB) | 
9.7 | 
N/A | 
|

| 
G2 (L4) | 
N/A | 
30.3 | 
|






### Volta, Pascal, and Turing architectures

The N1 machine types use the following GPU architectures:

- [Volta](https://www.nvidia.com/en-us/data-center/volta-gpu-architecture/) (V100)

- [Pascal](https://www.nvidia.com/en-us/data-center/pascal-gpu-architecture/) (P4)

- [Turing](https://developer.nvidia.com/blog/nvidia-turing-architecture-in-depth/) (T4)





### Tensor Core

NVIDIA's Turing and Volta architectures, available on N1 instances, provide
Tensor Core support for mixed-precision, INT8, and INT4 operations, offering
foundational acceleration for deep learning inference.

These GPUs introduced the first generations of Tensor Cores, used primarily
for FP16 training and INT8 and INT4 quantization in inference. This
table doesn't include the N1 (P4) machine type because
it doesn't have Tensor cores.

In the following table, `N/A` indicates that the metric is not applicable or
not available for this GPU model.



| 
Machine type (GPU model) | 
Mixed FP16/32 (TFLOPS) | 
INT8 (TOPS) | 
INT4 (TOPS) | 
|



| 
N1 (V100) | 
125 | 
N/A | 
N/A | 
|

| 
N1 (T4) | 
65 | 
130 | 
260 | 
|





### Standard CUDA cores

The machine types that use the Volta, Pascal, and Turing architectures are
equipped with FP64 and FP32 CUDA cores to accelerate a range of HPC and AI
workloads.

In the following table, `N/A` indicates that the metric is not applicable or
not available for this GPU model.



| 
Machine type (GPU model) | 
FP64 (TFLOPS) | 
FP32 (TFLOPS) | 
|



| 
N1 (V100) | 
7.8 | 
15.6 | 
|

| 
N1 (T4) | 
N/A | 
8.1 | 
|

| 
N1 (P4) | 
0.2 | 
5.5 | 
|






## What's next?

- Learn more about [Compute Engine GPUs](/compute/docs/gpus/about-gpus).

- Check [GPU regions and zones availability](/compute/docs/gpus/gpu-regions-zones).

- Review [Network bandwidths and GPUs](/compute/docs/gpus/gpu-network-bandwidth).

- View [GPU pricing details](https://documentation.s3ns.fr/compute/gpus-pricing).