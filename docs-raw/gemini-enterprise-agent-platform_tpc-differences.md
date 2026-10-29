# Agent Platform in Google Cloud Dedicated versus Google Cloud

Source: https://berlin.devsitetest.how/gemini-enterprise-agent-platform/tpc-differences
Last updated: 2026-10-26

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












# Agent Platform in Google Cloud Dedicated versus Google Cloud 















Gemini Enterprise Agent Platform is a platform for building, deploying, and managing generative AI applications.
This page describes the differences between the
Google Cloud Dedicated and Google Cloud versions of Agent Platform.



For more detailed information about Agent Platform, see the
[Agent Platform overview](/gemini-enterprise-agent-platform/overview) and the rest of the
Agent Platform documentation.




## Key differences



There are some differences between the Google Cloud Dedicated version of Agent Platform and
the Google Cloud version.
Some notable differences include the following:






- Only [Model Garden](/gemini-enterprise-agent-platform/models/model-garden/explore-models),
[Model Registry on Gemini Enterprise Agent Platform](/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction),
and [Online inference (predictions)](/gemini-enterprise-agent-platform/machine-learning/predictions)
are available in Google Cloud Dedicated. Other components and features of Agent Platform are unavailable.

- The Agent Platform SDK (Vertex AI SDK) and Google Gen AI SDK are unavailable. Supported interfaces are the Google Cloud Dedicated console, the Google Cloud CLI (`gcloud` CLI), and the REST API.

- Open first-party and third-party models (such as Gemma and Mistral) are available. Gemini and other proprietary models are unavailable.

- Only self-deploy options are available in Google Cloud Dedicated.




A more detailed list of differences is provided in the rest of this section.
If you are already familiar with Google Cloud, we recommend that you review these
differences carefully, particularly before designing an application to run on
Google Cloud Dedicated. We also recommend reviewing the [
general differences between Google Cloud Dedicated and Google Cloud](/docs/overview/tpc-key-differences).




If you would like to use a particular Agent Platform feature that isn't currently
available in Google Cloud Dedicated, contact
[Google Cloud Dedicated support](/docs/overview/gcd-support).
To be notified when new features roll out in Google Cloud Dedicated, subscribe to the
[release notes](/release-notes). Unless otherwise specified, features that are in preview are not available in
Google Cloud Dedicated.




### Workflows and tools




| 
Feature support differences | 
|



| 
**SDK and client interfaces** | 

The Agent Platform SDK (Vertex AI SDK) and Google Gen AI SDK are unavailable in Google Cloud Dedicated. Supported interfaces are the Google Cloud Dedicated console, the gcloud CLI (`gcloud` CLI), and the REST API.
| 
|

| 
**Unavailable components** | 

The following components of Agent Platform are unavailable in Google Cloud Dedicated: all components other than Model Garden, Model Registry, and Online inference.
| 
|



#### Model Garden




| 
Functionality and options differences | 
|



| 
**Features not available in the console interface** | 

The following areas are not available in the main console interface:



- Explore Generative AI

- Fast Deployment

- Deployment with custom weights

- Foundational Models section (including Gemini models)

- Fine-tunable Models section


| 
|

| 
**Model availability** | 

Gemini models and third-party proprietary models are unavailable. Gemma and select third-party open-source models are available.
| 
|

| 
**Model deployment and actions** | 

The following actions are unavailable:



- Model fine-tuning

- Opening a model notebook

- Model evaluation

- "Try it Out" (Agent Studio feature)

- One-click deployment of external models directly from Hugging Face Hub


| 
|

| 
**Model deployment options** | 

Only self-deploy options are available. Model-as-a-Service is unavailable.
| 
|

| 
**Deployment targets** | 

Deploying models from Model Garden to Google Kubernetes Engine (GKE) is unavailable (only deployment to an Agent Platform endpoint is supported).
| 
|



#### Model Registry




| 
Functionality differences | 
|



| 
**Unavailable registry actions** | 

The following actions are unavailable in Model Registry in Google Cloud Dedicated:



- Create a new model

- Train a new model version

- Register BigQuery ML models in Model Registry

- Batch inference

- Evaluate

- Data lineage

- Deploy a model for batch inference

- Export model versions (`ExportModel`) to Cloud Storage


| 
|

| 
**Model details page and actions** | 

Testing models is unavailable on the model details page.
| 
|



#### Online inference (Predictions)




| 
Functionality differences | 
|



| 
**Inference features** | 

Only synchronous `Predict` and `RawPredict` prediction methods are available. The following inference features and prediction methods are unavailable in Google Cloud Dedicated:



- Streaming prediction methods (`StreamRawPredict`, `ServerStreamingPredict`, `StreamingPredict`, and `StreamGenerateContent`)

- Specialized prediction methods (`ChatCompletions`, `DirectPredict`, `CountTokens`, and `EmbedContent`)

- Explanation requests (`Explain`)

- Invoke requests

- Batch prediction (batch prediction API endpoints are omitted or disabled)


| 
|

| 
**Endpoint access** | 

Only standard-access regional endpoints are available (Private Service Connect and private peering endpoints are unavailable).
| 
|



### Integrations




| 
Integration differences | 
|



| 
**BigQuery ML integration** | 

You can't register BigQuery ML models in Model Registry in Google Cloud Dedicated.
| 
|



### API surface




| 
API surface differences | 
|



| 
**API endpoint restrictions** | 

Only allowed control plane methods (for endpoints, models, and deployments) and data plane methods (for serving predictions) are available.
Specifically, only synchronous `Predict` and `RawPredict` prediction methods are available. Streaming prediction methods (`StreamRawPredict`, `ServerStreamingPredict`, `StreamingPredict`, and `StreamGenerateContent`), specialized prediction methods (`ChatCompletions`, `DirectPredict`, `CountTokens`, and `EmbedContent`), and other methods (such as `Explain`, `GenerateContent`, and `ExportModel`) are unavailable.
| 
|






## Related guides



The following information might also affect how you use and design for Agent Platform
in Google Cloud Dedicated in Germany. These guides include general information about working in Google Cloud Dedicated,
including documentation, security and access control, billing, tooling, and service usage.



For details about other services and features in Google Cloud Dedicated and their differences from
their Google Cloud counterparts, see the [product list.](https://berlin.devsitetest.how/products)





- 


[Google Cloud Dedicated in Germany overview](/docs/overview/tpc-overview)




- 


[Key differences between Google Cloud Dedicated in Germany and Google Cloud](/docs/overview/tpc-key-differences)