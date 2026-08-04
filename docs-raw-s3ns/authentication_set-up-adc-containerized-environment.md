# Set up ADC for a containerized development environment

Source: https://documentation.s3ns.fr/docs/authentication/set-up-adc-containerized-environment
Last updated: 2026-07-21

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/docs/authentication/tpc-differences) for more details.














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

Developer tools

](https://documentation.s3ns.fr/docs/costs-usage)






- 








[

Google Cloud SDK

](https://documentation.s3ns.fr/sdk/docs)






- 








[

Authentication

](https://documentation.s3ns.fr/docs/authentication)






- 








[

Guides

](https://documentation.s3ns.fr/sdk/docs/overview)












# Set up ADC for a containerized development environment 






- On this page 
- [ Test containerized applications locally ](#local-testing)
- [ Run containerized applications on Cloud de Confiance ](#gcp-containerized)
- [ What's next ](#whats_next)
- 










Authentication for containerized applications running on Cloud Run
or Google Kubernetes Engine is handled differently between local testing environments
and Cloud de Confiance environments.

### Test containerized applications locally 

To test your containerized application on your local workstation, you can
configure your container to authenticate with your
[local ADC file](/docs/authentication/application-default-credentials#personal). For more information, see
[Configure ADC with your Google Account](/docs/authentication/set-up-adc-local-dev-environment#google-idp).

To test your implementation, use a local Kubernetes implementation such as
[`minikube` and the `gcp-auth` addon](https://minikube.sigs.k8s.io/docs/handbook/addons/gcp-auth/).

### Run containerized applications on Cloud de Confiance

See [
Access Cloud de Confiance APIs from GKE workloads](/kubernetes-engine/docs/how-to/workload-identity).



## What's next

- Learn more about [how ADC finds credentials](/docs/authentication/application-default-credentials).

- [Authenticate for using Cloud Client Libraries](/docs/authentication/client-libraries).

- [Authenticate for using REST](/docs/authentication/rest).

- Explore [authentication methods](/docs/authentication).