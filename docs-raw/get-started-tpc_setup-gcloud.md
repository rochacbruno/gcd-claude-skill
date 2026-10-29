# Set up the Google Cloud CLI for Google Cloud Dedicated

Source: https://berlin.devsitetest.how/docs/get-started-tpc/setup-gcloud
Last updated: 2026-10-27

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

Get started

](https://berlin.devsitetest.how/docs/get-started)












# Set up the Google Cloud CLI for Google Cloud Dedicated 


















This guide provides instructions for setting up the Google Cloud CLI
(gcloud CLI) for use with
Google Cloud Dedicated. The gcloud CLI
helps you create and work with Google Cloud Dedicated
resources from the command line.

For more general information about configuring and using the
gcloud CLI, see the [Google Cloud CLI documentation](/sdk/gcloud).

## Differences from setup in Google Cloud

If you're already familiar with setting up and using the CLI with
Google Cloud, note the following:

- There is some additional initial setup required to use the
gcloud CLI with Google Cloud Dedicated,
as described in this guide.

- Cloud Shell is not available in Google Cloud Dedicated. The gcloud CLI must be installed on your local machine.

- Initializing the gcloud CLI in one step with `gcloud init` is not available.

- If a feature or product is unavailable in Google Cloud Dedicated,
the corresponding gcloud CLI commands and parameters are also unavailable.

## Before you begin

In addition to your own sign in details for Google Cloud Dedicated, you need the following to set up the gcloud CLI for the first
time. If you are not an administrator for your organization, your administrator
should provide you with this information.

- Your organization's **workload identity pool name**.

- Your organization's **identity provider** (IdP).

## Install the gcloud CLI

Install the gcloud CLI, following the instructions for your OS.






- Confirm that you have a supported version of Python. The Google Cloud CLI requires
Python 3.10 to 3.15. The x86_64 Linux package includes
a bundled Python interpreter that will be preferred by default. For
information on how to choose and configure your Python interpreter, see the 
[`gcloud topic startup` documentation](/sdk/gcloud/reference/topic/startup).


- Download one of the following:




| 
Platform | 
Package name | 
Size | 
SHA256 Checksum | 
|



| 
Linux 64-bit 

(x86_64) 
| 
[google-cloud-cli-linux-x86_64.tar.gz](https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-linux-x86_64.tar.gz) | 
94.4 MB | 
8b8c1be16284f7072359de05d31fe5ce52b6052fb295404a62a54b7d03ec4326 | 
|

| 
Linux 64-bit 

(Arm) 
| 
[google-cloud-cli-linux-arm.tar.gz](https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-linux-arm.tar.gz) | 
90.4 MB | 
c134c741f7232131e2556d77991bc8eaeb70054cfad426e06c533b3586ab69e6 | 
|

| 
Linux 32-bit 

(x86) 
| 
[google-cloud-cli-linux-x86.tar.gz](https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-linux-x86.tar.gz) | 
54.4 MB | 
de8c17292832482c411cbfa0fe203b89cb4679325530e24aedfcc77898160efe | 
|




To download the Linux archive file, run the following command:



```
curl -O https://storage.apis-berlin-build0.goog/cloud-sdk-release/ google-cloud-cli-linux-x86_64.tar.gz 
```



Refer to the table above and replace google-cloud-cli-linux-x86_64.tar.gz with the
`*.tar.gz` package name that applies to your configuration.




- To extract the contents of the file to your file system, run the following command:

```
tar -xf google-cloud-cli-linux-x86_64.tar.gz 
```

To replace an existing installation, delete the existing
`google-cloud-sdk` directory and then extract the archive to the
same location.


- Run the installation script from the root of the folder you
extracted:

```
./google-cloud-sdk/install.sh
```

The script prompts you to perform the following setup actions. To accept,
answer `Y` when prompted.



- Add the gcloud CLI to your `PATH`.

- Enable command completion.

- Opt in to send [anonymous usage statistics](/sdk/docs/usage-statistics)
to help improve the gcloud CLI.



You can also perform the installation non-interactively by providing flags.
To view available flags, run:

```
./google-cloud-sdk/install.sh --help
```



- Optional: If you updated your `PATH` in the previous step, open a new
terminal so that the changes take effect.