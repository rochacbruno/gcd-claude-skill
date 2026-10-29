# Overview of Model Garden

Source: https://berlin.devsitetest.how/gemini-enterprise-agent-platform/models/model-garden/explore-models
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/gemini-enterprise-agent-platform/tpc-differences) for more details.














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

AI and ML

](https://berlin.devsitetest.how/docs/ai-ml)






- 








[

Gemini Enterprise Agent Platform

](https://berlin.devsitetest.how/gemini-enterprise-agent-platform)






- 








[

Models

](https://berlin.devsitetest.how/gemini-enterprise-agent-platform/models)












# Overview of Model Garden 















Model Garden is an AI/ML model library that helps you discover, test,
customize, and deploy models and assets from Google and Google partners.

## Advantages of Model Garden

When you're working with AI models, Model Garden provides the following
advantages:

- Available models are all grouped in a single location

- Model Garden provides a consistent deployment pattern for different
types of models

- Model Garden provides built-in integration with other parts of
Gemini Enterprise Agent Platform such as model tuning, evaluation, and serving

- Serving generative AI models can be difficult—Gemini Enterprise Agent Platform handles
model deployment and serving for you

## Explore models

To view the list of available Gemini Enterprise Agent Platform and open source foundation,
tunable, and task-specific models, go to the Model Garden page in the
Google Cloud Dedicated console.

[Go to Model Garden](https://console.cloud.berlin-build0.goog/agent-platform/model-garden) 

The model categories available in Model Garden are:




| 
Category | 
Description | 
|




| 
Task-specific solutions | Most of these prebuilt models are
ready to use. Many can be customized using your own data. | 
|



To filter models in the filter pane, specify the following:

- **Tasks**: Click the task that you want the model to perform.

- **Model collections**: Click to choose models that are managed by Google,
partners, or you.

- **Providers**: Click the provider of the model.

- **Features**: Click the features that you want in the model.

To learn more about each model, click its model card.

## Model security scanning

Google does thorough testing and benchmarking on the serving and tuning
containers that we provide. Active vulnerability scanning is also applied to
container artifacts.

Third-party models from featured partners undergo model checkpoint scans to
ensure authenticity. Third-party models from HuggingFace Hub are scanned
directly by HuggingFace and their
[third-party scanner](https://huggingface.co/docs/hub/en/security-protectai)
for malware, pickle files, Keras Lambda layers, and secrets. Models deemed
unsafe from these scans are flagged by HuggingFace and blocked from deployment
in Model Garden. Models deemed suspicious or those that have the
ability to potentially execute remote code are indicated in
Model Garden but can still be deployed. We recommend you perform a
thorough review of any suspicious model before deploying it
within Model Garden.

## Control access to specific models

You can set a [Model Garden organization
policy](/gemini-enterprise-agent-platform/models/control-model-access) at the organization, folder, or
project level to control access to specific models in Model Garden. For
example, you can allow access to specific models that you've vetted and deny
access to all others.

## Learn more about Model Garden

For more information about the deployment options and customizations that you
can do with models in Model Garden, view the resources in the
following sections.

### Deploy and serve

Learn more about customizing deployments and advance serving features.

- [Deploy and serve open source model using Python SDK, CLI, REST API, or console](/gemini-enterprise-agent-platform/models/model-garden/use-models#deploy_a_model)

- [Deploying Gemma and making predictions](/gemini-enterprise-agent-platform/models/model-garden/deploy-and-inference-tutorial)

- [Serve open models with a Hex-LLM container on Cloud
TPUs](/gemini-enterprise-agent-platform/models/open-models/use-hex-llm)

- [Serving Gemma 2 with multiple LoRA adapters with HuggingFace DLC for PyTorch inference tutorial on Medium](https://medium.com/google-cloud/open-models-on-vertex-ai-with-hugging-face-serving-multiple-lora-adapters-on-vertex-ai-e3ceae7b717c) 

- [Use custom handles to serve PaliGemma for image captioning with HuggingFace DLC for PyTorch inference tutorial on LinkedIn](https://www.linkedin.com/posts/ivan-nardini_vertexai-huggingface-deeplearning-activity-7269824291238526976-oxuM?utm_source=li_share&utm_content=feedcontent&utm_medium=g_dt_web&utm_campaign=copy)

- [Deploy and serve a HuggingFace model](/gemini-enterprise-agent-platform/models/open-models/use-hugging-face-models)

- [Use xDiT GPU serving container for image and video generation](/gemini-enterprise-agent-platform/models/open-models/xdit)

- [Use vLLM to serve text-only and multimodel language models on Cloud GPUs](/gemini-enterprise-agent-platform/models/open-models/vllm/use-vllm)