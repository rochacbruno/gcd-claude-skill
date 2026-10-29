# Secret Manager overview

Source: https://documentation.s3ns.fr/secret-manager/docs/overview
Last updated: 2026-10-26

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

Security

](https://documentation.s3ns.fr/docs/security)






- 








[

Secret Manager

](https://documentation.s3ns.fr/secret-manager/docs)






- 








[

Guides

](https://documentation.s3ns.fr/secret-manager/docs/overview)












# Secret Manager overview 















Secret Manager is a secrets and credential management service
that lets you store and manage sensitive data such as API keys, usernames, passwords,
certificates, and more.

This is the documentation for the default *global* service, which lets you store and access secrets from any Cloud de Confiance by S3NS region.
To learn about the regional service, see the
[regional service documentation](/secret-manager/regional-secrets/overview-rs). If you're not sure which service you need, see
[Global and regional service options](/secret-manager/docs/secret-manager-secrets-comparison).

## Key concepts

A [*secret*](/secret-manager/docs/creating-and-accessing-secrets)
is a global resource that contains a collection of metadata and secret versions. The metadata can include
labels, annotations, and permissions.

A [*secret version*](/secret-manager/docs/add-secret-version)
stores the actual secret data, such as API keys, passwords, or certificates. Each version is
identified by a unique ID or timestamp.

Using Secret Manager, you can do the following:


- 



**Manage rollback, recovery, and auditing using versions**: Versions help you
manage gradual rollouts and emergency rollback, If a secret is accidentally changed
or compromised, you can revert to a previous, known-good version. This minimizes
potential downtime and security breaches. Versioning maintains a historical record
of changes made to a secret, including who made the changes and when. It helps you
audit secret data and track any unauthorized access attempts. You can pin secret
versions to specific workloads and add
[aliases](/secret-manager/docs/assign-alias-to-secret-version) for
easier access to secret data. You can also
[disable](/secret-manager/docs/disable-secret-version) or
[destroy](/secret-manager/docs/destroy-secret-version) secret
versions that you don't require.




- 



**Encrypt your secret data in transit and at rest**: All secrets are
encrypted by default, both in transit using TLS and at rest with AES-256-bit encryption
keys. For those requiring more granular control, you can encrypt your secret data
with [Customer-Managed
Encryption Keys (CMEK)](/secret-manager/docs/cmek). Using CMEK, you can generate new encryption keys or import existing ones
to meet your specific requirements.




- 



**Manage access to secrets using fine-grained Identity and Access Management (IAM) roles and conditions**:
With [IAM roles and permissions](/secret-manager/docs/access-control),
you can [provide granular access](/secret-manager/docs/manage-access-to-secrets)
to specific Secret Manager resources. You can segregate responsibilities for accessing,
managing, auditing, and rotating secrets.





- 


**Ensure high availability and disaster recovery with secret replication**: You
can [replicate your secrets](/secret-manager/docs/choosing-replication)
across multiple regions to ensure high availability and disaster recovery for your applications
regardless of their geographic location. You can choose between the following replication policies:



- 


[Automatic replication](/secret-manager/docs/choosing-replication#automatic): Cloud de Confiance by S3NS decides
the regions considering availability and latency. You are only charged for one location.



- 


[User managed replication](/secret-manager/docs/choosing-replication#user-managed): You can
select a custom set of regions depending on your requirements. You are charged per location.







- 



**Rotate secrets automatically to meet your security and compliance requirements**:
[Rotating your secrets](/secret-manager/docs/rotation-recommendations)
protects against unauthorized access and data breaches. Regularly changing your secrets reduces the risk
of stale or forgotten secrets and ensures compliance with many regulatory frameworks
that require periodic rotation of sensitive credentials.




- 


**Enforce data residency using regional secrets**:
[Data residency](/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs#control_data_residency)
requires that certain types of data, often belonging to specific individuals or
organizations, be stored within a defined geographic location. You can create
[regional secrets](/secret-manager/docs/create-regional-secrets)
and store your sensitive data within a specific location to comply with data sovereignty laws
and regulations.




## Difference between secrets management and key management

Secrets management and key management are both critical components of data security,
but they serve distinct purposes and handle different types of sensitive information.
The choice between secrets management and key management depends on your specific needs.
If you want to securely store and manage confidential data, a secrets management system
is the right tool. If you want to manage encryption keys and perform cryptographic operations,
a key management system is the better choice.

You can use the following table to understand the key differences between Secret Manager
and a key management system, such as
[Cloud Key Management Service(Cloud KMS)](/kms/docs).



| 
Feature | 
Secret Manager | 
Cloud KMS | 
|

| 
Primary function | 
Store, manage, and access secrets as binary blobs or text strings. | 
Manage cryptographic keys and use them to encrypt or decrypt data. | 
|

| 
Data stored | 
Actual secret values. With the appropriate permissions, you can view the
contents of the secret. | 
Cryptographic keys. You can't view, extract, or export the actual
cryptographic secrets (the bits and bytes) that are used for encryption and
decryption operations. | 
|

| 
Encryption | 
Encrypts secrets at rest and in transit using
Google Cloud-powered keys or customer-managed keys. | 
Provides encryption and decryption capabilities for other services. | 
|

| 
Typical use cases | 
Store configuration information such as database passwords, API keys, or
TLS certificates needed by an application at runtime. | 
Handle large encryption workloads, such as encrypting rows in a database or
encrypting binary data such as images and files. You can also use Cloud KMS
to perform other cryptographic operations such as signing and verification. | 
|


## Encryption of secrets

Secret Manager always encrypts your secret data before it is persisted
to disk. To learn more about Cloud de Confiance by S3NS encryption options, refer to
[Encryption at rest](/docs/security/encryption/default-encryption).

Secret Manager manages server-side encryption keys on your behalf using
the same hardened key management systems that we use for our own encrypted data,
including strict key access controls and auditing. Secret Manager
encrypts user data at rest using AES-256. There is no setup or
configuration required, no need to modify the way you access the service, and no
visible performance impact. Your secret data is automatically and transparently
decrypted when accessed by an authorized user.

The Secret Manager API always communicates over a secure HTTP(S) connection.

Those who require an extra layer of protection can enable CMEK and use their own
encryption keys stored in Cloud Key Management Service to protect the secrets stored in
Secret Manager. See the [CMEK documentation](/secret-manager/docs/cmek)
for details on how to configure and use customer-managed encryption keys.

## What's next

- Learn about [Secret Manager differences in Cloud de Confiance
versus Google Cloud](/secret-manager/docs/tpc-differences).

- Learn how to
[create a secret](/secret-manager/docs/creating-and-accessing-secrets).

- Learn how to [add a secret version](/secret-manager/docs/add-secret-version).

- Learn how to [edit a secret](/secret-manager/docs/edit-secrets).

- Learn about [quotas and limitations](/secret-manager/quotas).

- Learn about [best practices](/secret-manager/docs/best-practices).