# Open models overview

Source: https://documentation.s3ns.fr/gemini-enterprise-agent-platform/models/open-models/choose-serving-option
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/gemini-enterprise-agent-platform/tpc-differences) for more details.














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

AI and ML

](https://documentation.s3ns.fr/docs/ai-ml)






- 








[

Gemini Enterprise Agent Platform

](https://documentation.s3ns.fr/gemini-enterprise-agent-platform)






- 








[

Models

](https://documentation.s3ns.fr/gemini-enterprise-agent-platform/models)












# Open models overview 




















Gemini Enterprise Agent Platform offers multiple ways to serve open large language models,
including Llama, DeepSeek, Mistral, and Qwen, in Cloud de Confiance by S3NS. This document
provides an overview of Gemini Enterprise Agent Platform offerings for open model serving and
helps you choose the right option for your use case.

## Serving options

Gemini Enterprise Agent Platform offers the following options for serving open models. Each of
these options provides high availability and includes Cloud de Confiance by S3NS security
best practices by default:

- **[Model as a Service (MaaS)](/gemini-enterprise-agent-platform/models/open-models/use-maas)**: Serves open models by using
serverless managed APIs.

- **[Self-deployed models in Model Garden](/gemini-enterprise-agent-platform/models/open-models/deploy-model-garden)**:
Deploys open models from Model Garden by using one-click deployment
or with custom weights.

- **[Gemini Enterprise Agent Platform prebuilt container
images](/gemini-enterprise-agent-platform/models/open-models/use-prebuilt-containers)**: Serves open models by using prebuilt
containers for popular serving frameworks, for example, vLLM, Hex-LLM, and
TGI.

- **[Custom vLLM container](/gemini-enterprise-agent-platform/models/open-models/deploy-custom-vllm)**: Lets you build and deploy
your own custom vLLM container for greater flexibility.

### When to use MaaS

Consider using MaaS in these scenarios:

- **Rapid development and prototyping**: MaaS helps you quickly integrate LLM
capabilities into applications. This is especially useful for
initial exploration, rapid prototyping, and when fast time-to-market is a
key goal.

- **Minimizing operational overhead**: Choose MaaS when your team wants to
focus on application logic instead of infrastructure management. Google
handles all GPU/TPU provisioning, scaling, and maintenance, which benefits
teams focused on application development rather than MLOps or DevOps.

- **Variable traffic**: The pay-as-you-go model supports experimental
workloads or applications with unpredictable, bursty traffic patterns.

- **Out-of-the-box usage**: Use a managed API for applications that need
consistent performance but don't require deep customization of the
underlying model or serving stack.

- **Security and compliance**: MaaS lets enterprises use Cloud de Confiance by S3NS's
built-in, enterprise-grade security and compliance features.

- **Standard model usage**: Use MaaS when a standard, non-customized
foundation model meets your needs.

### When to use self-deployed models in Model Garden

Self-deployment options include deploying from Model Garden by using
prebuilt or custom containers. Consider self-deployment in these key scenarios:

- **Custom weights and fine-tuned models**: Self-deployment is the best choice
when your application requires using custom weights or a fine-tuned version
of a model, offering greater flexibility to deploy models tailored to your
specific needs. You can also build and deploy your own custom serving
containers. For example, use this option when a model requires unique
pre-processing or post-processing logic.

- **Predictable, high-volume workloads**: Self-deployment is a strategic and
cost-effective option for production applications with predictable and
high-volume traffic. While it requires a greater upfront engineering
investment, it can lead to a lower total cost of ownership (TCO) over the
application's lifetime due to optimized per-token costs at scale.

- **Granular control over infrastructure**: Use self-deployment when you need
to fine-tune performance and budget by choosing specific hardware
configurations. This includes selecting exact machine types, GPUs (for
example, NVIDIA L4 or H100) or TPUs, and optimized serving frameworks.

- **Stringent security and compliance**: This approach supports applications
that must adhere to specific data residency policies or stringent
regulations that prohibit using a multi-tenant managed service. It lets you
deploy models securely within your own Cloud de Confiance by S3NS project and Virtual Private Cloud
network, providing complete control over the data path.

- **Granular control over location**: Dedicated endpoints let you deploy on
any Compute Engine accelerator in Cloud de Confiance by S3NS across all regions.

### When to use prebuilt containers

Consider using Gemini Enterprise Agent Platform prebuilt containers in these scenarios:

- **Optimized performance**: Gemini Enterprise Agent Platform optimizes and customizes
prebuilt containers for frameworks like vLLM for enhanced performance,
reliability, and seamless integration within Cloud de Confiance by S3NS.

- **Ease of use**: Serve models by using popular serving
frameworks such as vLLM, Hex-LLM, SGLang, TGI, or TensorRT-LLM without
building and maintaining your own container images.

### When to use custom vLLM containers

Consider building and using your own custom container in these scenarios:

- **Maximum flexibility**: When existing serving options and prebuilt
containers are insufficient for your needs, and you require full control
over the container image, including dependencies and configurations.

- **Custom serving logic**: When your model requires unique pre-processing or
post-processing steps that are not supported by prebuilt containers.

## What's next

- [Use open models with Model as a Service (MaaS)](/gemini-enterprise-agent-platform/models/open-models/use-maas)

- [Deploy open models from Model Garden](/gemini-enterprise-agent-platform/models/open-models/deploy-model-garden)

- [Deploy open models with prebuilt containers](/gemini-enterprise-agent-platform/models/open-models/use-prebuilt-containers)

- [Deploy open models with a custom vLLM container](/gemini-enterprise-agent-platform/models/open-models/deploy-custom-vllm)