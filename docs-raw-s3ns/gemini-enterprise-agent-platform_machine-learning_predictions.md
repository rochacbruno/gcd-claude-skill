# Overview of getting inferences on Agent Platform

Source: https://documentation.s3ns.fr/gemini-enterprise-agent-platform/machine-learning/predictions
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












# Overview of getting inferences on Agent Platform 















An inference is the output of a trained machine learning model. This page
provides an overview of the workflow for getting inferences from your models on
Gemini Enterprise Agent Platform.

Agent Platform supports online inferences:


- 
**Online inferences** are synchronous requests made to
a model that is deployed to an
[`Endpoint`](/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints).
Therefore, before sending a request, you must first deploy the
[`Model`](/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models)
resource to an endpoint. This associates
[compute resources](/gemini-enterprise-agent-platform/machine-learning/predictions/configure-compute) with
the model so that the model can serve online inferences with
low latency. Use online inferences when you are making requests in
response to application input or in situations that require timely
inference.


## Test your model locally

Before getting inferences, it's useful to deploy your model to a local
endpoint during the development and testing phase. This lets you both iterate
more quickly and test your model without deploying it to an online endpoint or
incurring inference costs. Local deployment is intended for local development
and testing, not for production deployments.

To deploy a model locally, use the Agent Platform SDK for Python and deploy a
[`LocalModel`](/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalModel)
to a
[`LocalEndpoint`](/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalEndpoint).

Even if your client is not written in Python, you can still use the
Agent Platform SDK for Python to launch the container and server so that you can test
requests from your client.

## Get inferences from custom trained models

To get inferences, you must first [import your
model](/gemini-enterprise-agent-platform/machine-learning/model-registry/import-model).
After it's imported, it becomes a
[`Model`](/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models) resource
that is visible in
[Model Registry](/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction).

Then, read the following documentation to learn how to get inferences:

[Deploy a model to an
endpoint](/gemini-enterprise-agent-platform/machine-learning/general/deployment)
and [get online
inferences](/gemini-enterprise-agent-platform/machine-learning/predictions/get-online-predictions).

## What's next

- Learn about [Compute resources for
inference](/gemini-enterprise-agent-platform/machine-learning/predictions/configure-compute).

- Learn about [Agent Platform differences in Cloud de Confiance versus Google Cloud](/gemini-enterprise-agent-platform/tpc-differences).