# Set up ADC for a containerized development environment

Source: https://berlin.devsitetest.how/docs/authentication/set-up-adc-containerized-environment
Last updated: 2026-07-21

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/authentication/tpc-differences) for more details.














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

Google Cloud SDK

](https://berlin.devsitetest.how/sdk/docs)






- 








[

Authentication

](https://berlin.devsitetest.how/docs/authentication)






- 








[

Guides

](https://berlin.devsitetest.how/sdk/docs/overview)












# Set up ADC for a containerized development environment 






- On this page 
- [ Test containerized applications locally ](#local-testing)
- [ Run containerized applications on Google Cloud Dedicated ](#gcp-containerized)
- [ What's next ](#whats_next)
- 










Authentication for containerized applications running on Cloud Run
or Google Kubernetes Engine is handled differently between local testing environments
and Google Cloud Dedicated environments.

### Test containerized applications locally 

To test your containerized application on your local workstation, you can
configure your container to authenticate with your
[local ADC file](/docs/authentication/application-default-credentials#personal). For more information, see
[Configure ADC with your Google Account](/docs/authentication/set-up-adc-local-dev-environment#google-idp).

To test your implementation, use a local Kubernetes implementation such as
[`minikube` and the `gcp-auth` addon](https://minikube.sigs.k8s.io/docs/handbook/addons/gcp-auth/).

### Run containerized applications on Google Cloud Dedicated

See [
Access Google Cloud Dedicated APIs from GKE workloads](/kubernetes-engine/docs/how-to/workload-identity).



## What's next

- Learn more about [how ADC finds credentials](/docs/authentication/application-default-credentials).

- [Authenticate for using Cloud Client Libraries](/docs/authentication/client-libraries).

- [Authenticate for using REST](/docs/authentication/rest).

- Explore [authentication methods](/docs/authentication).