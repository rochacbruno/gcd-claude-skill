# Introduction to AI/ML workloads on GKE

Source: https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/machine-learning
Last updated: 2026-07-08

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/kubernetes-engine/docs/tpc-differences) for more details.














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

Google Kubernetes Engine (GKE)

](https://berlin.devsitetest.how/kubernetes-engine/docs)






- 








[

GKE AI/ML

](https://berlin.devsitetest.how/kubernetes-engine/docs)






- 








[

Guides

](https://berlin.devsitetest.how/kubernetes-engine/docs/concepts/machine-learning)












# Introduction to AI/ ML workloads on GKE 






- On this page ** 
- [ Get started with AI/ML workloads on GKE ](#get-started)
- [ Common use cases ](#common_use_cases)
- [ Choose the right platform for your AI/ML workload ](#choose_the_right_platform_for_your_aiml_workload)
- [ How GKE powers AI/ML workloads ](#how_powers_aiml_workloads)
- [ What's next ](#whats_next)
- 


















[

Autopilot


](/kubernetes-engine/docs/concepts/autopilot-overview)









[

Standard


](/kubernetes-engine/docs/concepts/choose-cluster-mode)








This page provides a conceptual overview of Google Kubernetes Engine (GKE) for
AI/ML workloads. GKE is a Google-managed implementation of the
[Kubernetes](https://kubernetes.io) open source container orchestration platform.





[Google Kubernetes Engine](/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
provides a scalable, flexible, and cost-effective platform for running all your
containerized workloads, including artificial intelligence and
machine learning (AI/ML) applications. Whether you're training large foundation
models, serving inference requests at scale, or building a comprehensive
AI platform, GKE offers the control and performance you
need.

This page is for Data and AI specialists, Cloud architects,
Operators, and Developers who are looking for a
scalable, automated, managed Kubernetes solution to run AI/ML workloads. To
learn more about common roles, see
[Common GKE user roles and tasks](/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Get started with AI/ ML workloads on GKE

You can start exploring GKE in minutes by using GKE's
[free tier](https://berlin.devsitetest.how/kubernetes-engine/pricing#cluster_management_fee_and_free_tier),
which lets you get started with Kubernetes without incurring costs for cluster
management.

- 

[Get started in Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/kubernetes/aiml/overview)

- Try these quickstarts:

- [Inference on GKE](/kubernetes-engine/docs/tutorials/serve-open-models-terraform): deploy an AI large language model (LLM) on GKE for inference using a pre-defined architecture.

- [Training on GKE](/kubernetes-engine/docs/quickstarts/train-model-gpus-standard): deploy an AI training model on GKE
and store the predictions in Cloud Storage.

- Read [About accelerator consumption options for AI/ML workloads](/kubernetes-engine/docs/concepts/consumption-option), which has guidance and resources for planning
and obtaining accelerators (GPUs and TPUs) for your platform.

## Common use cases

GKE provides a unified platform that can support all of your
AI workloads.

- **Building an AI platform**: for enterprise platform teams,
GKE provides the flexibility to build a standardized, multi-tenant
platform that serves diverse needs.

- **Low-latency online serving**: For developers building generative AI
applications, GKE with the Inference Gateway provides the
optimized routing and autoscaling needed to deliver a responsive user experience
while controlling costs.

## Choose the right platform for your AI/ML workload

Google Cloud Dedicated in Germany offers a spectrum of AI infrastructure products to support your
ML journey, from fully managed to fully configurable. Choosing the right
platform depends on your specific needs for control, flexibility, and level of
management.


Best practice**:

Choose GKE when you need deep control, portability, and the
ability to build a customized, high-performance AI platform.



- **Infrastructure control and flexibility**: you require a high degree of
control over your infrastructure, need to use custom pipelines, or require
kernel-level customizations.

- **Large-scale training and inference**: you want to train very large models
or serve models with minimal latency, by using GKE's
scaling and high performance.

- **Cost efficiency at scale**: you want to prioritize cost optimization by
using GKE's integration with Spot VMs and Flex-start VMs
to effectively manage costs.

- **Portability and open standards**: you want to avoid vendor
lock-in and run your workloads anywhere with Kubernetes, and you already have
existing Kubernetes expertise or a multi-cloud strategy.

You can also consider these alternatives:




| 
Google Cloud Dedicated in Germany service | 
Best for | 
|



| 
Vertex AI | 
A fully managed, end-to-end platform to accelerate development and offload infrastructure management. Works well for teams focused on MLOps and rapid time-to-value. For more information, watch [Choosing between self-hosted GKE and managed Vertex AI host AI models](https://www.youtube.com/watch?v=539_P8SnW4M). | 
|




## How GKE powers AI/ML workloads

GKE offers a suite of specialized components that simplify and
accelerate each stage of the AI/ML lifecycle, from large-scale training to
low-latency inference.



**Figure 1**: GKE as a scalable managed platform
for AI/ML workloads. 


The following table summarizes the GKE features that support
your AI/ML workloads or operational goals.



| 
AI/ML workload or operation | 
How GKE supports you | 
Key features | 
|



| 
**Inference and serving** | 
Optimized to serve AI models elastically, with low latency, high throughput,
and cost efficiency. | 

- [Accelerator flexibility](/kubernetes-engine/docs/concepts/consumption-option): GKE supports both [GPUs](/kubernetes-engine/docs/concepts/gpus)
for inference.

- [GKE Inference Gateway](/kubernetes-engine/docs/concepts/about-gke-inference-gateway): a model-aware gateway that provides intelligent routing and load balancing specifically for AI inference workloads.

- [GKE Inference Quickstart](/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart): a tool to simplify performance analysis and deployment by providing a set of benchmarked profiles for popular AI models.

- [GKE Autopilot](/kubernetes-engine/docs/concepts/autopilot-overview): a GKE operational mode that automates cluster operations and
capacity right-sizing, reducing overhead.

| 
|

| 
**Training and fine-tuning** | 
Provides the scale and orchestration capabilities necessary to efficiently train very large models while minimizing costs. | 

- [Faster startup nodes](/kubernetes-engine/docs/concepts/fast-starting-nodes#autopilot-gpu-workloads): an optimization designed specifically for GPU workloads that reduces node startup times by up to 80%.

- [Kueue](/kubernetes-engine/docs/tutorials/kueue-intro): a Kubernetes-native job queueing system that manages resource allocation, scheduling, quota management, and prioritization for batch workloads.

| 
|




## What's next

- 

[Learn about techniques to obtain computing accelerators, such as GPUs or TPUs, for your AI/ML workloads on GKE](/kubernetes-engine/docs/concepts/consumption-option).

- 

[Learn about AI/ML model inference on GKE](/kubernetes-engine/docs/concepts/machine-learning/inference).

- 

Explore experimental samples for leveraging GKE to accelerate your AI/ML initiatives in [GKE AI Labs](https://gke-ai-labs.dev/).

- 

[View details for your AI/ML workloads in Google Cloud Dedicated console](https://console.cloud.berlin-build0.goog/kubernetes/aiml), including resources such as JobSets, RayJobs, PyTorchJobs, and Deployments for inference serving.