# Set up the Google Cloud CLI for Google Cloud Dedicated

Source: https://berlin.devsitetest.how/docs/get-started-tpc/setup-gcloud
Last updated: 2026-07-10

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






- On this page ** 
- [ Differences from setup in Google Cloud ](#differences)
- [ Before you begin ](#before_you_begin)
- [ Install the gcloud CLI ](#install-gcloud)
- [ (Optional) Create a universe-specific configuration ](#optional_create_a_universe-specific_configuration)
- [ Create your login configuration file ](#create_your_login_configuration_file)
- [ Sign in to Google Cloud Dedicated with the gcloud CLI ](#sign-in)
- [ (Optional) Set up default properties ](#optional_set_up_default_properties)
- [ (Optional) Run commands ](#optional_run_commands)
- [ What's next ](#whats_next)
- 













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

[Linux](#linux) [macOS](#macos) [Windows](#windows) 
More 





- Confirm that you have a supported version of Python. The Google Cloud CLI requires
Python 3.10 to 3.14. The x86_64 Linux package includes
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
88.1 MB | 
3727f6aba95108cffa64448cef5db8b4981d4c48d821b4482dbffbdaef344ed1 | 
|

| 
Linux 64-bit 

(Arm) 
| 
[google-cloud-cli-linux-arm.tar.gz](https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-linux-arm.tar.gz) | 
61.0 MB | 
047768995ce95f525c8e5af805f3697238438b7f48f7b3c5e0a9c3bd0d661810 | 
|

| 
Linux 32-bit 

(x86) 
| 
[google-cloud-cli-linux-x86.tar.gz](https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-linux-x86.tar.gz) | 
61.1 MB | 
7130c90d3cdc635824c845cb6b65357890558abcfab2caab34272f13a32d24bb | 
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







- Confirm that you have a supported version of Python. The Google Cloud CLI requires
Python 3.10 to 3.14.


To check your Python version, run `python3 -V` or `python -V`.



The gcloud installer will install Python v3.14 and required extension modules by default.



For more information about configuring your Python interpreter, see the [`gcloud topic startup` documentation](/sdk/gcloud/reference/topic/startup).



- 
Download one of the following:




| 
Platform | 
Package | 
Size | 
SHA256 Checksum | 
|



| 

macOS 64-bit


(x86_64) 

| 


[google-cloud-cli-darwin-x86_64.tar.gz
](https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-darwin-x86_64.tar.gz)

| 
61.2 MB | 

123c47e410a9b274cd8a95f243277e19a32a8153972e425b16cc442d621b46ba 
| 
|

| 

macOS 64-bit


(ARM64, Apple silicon) 

| 


[google-cloud-cli-darwin-arm.tar.gz
](https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-darwin-arm.tar.gz)

| 
61.1 MB | 

502901c8d19c21b23803b33d5cedd417dcb16b12c918f162fb37e08c4be27d92 
| 
|

| 

macOS 32-bit


(x86) 

| 


[google-cloud-cli-darwin-x86.tar.gz
](https://storage.apis-berlin-build0.goog/cloud-sdk-release/google-cloud-cli-darwin-x86.tar.gz)

| 
59.5 MB | 

20c480e5a0c92128dd67a6304dc143545ab0558054de77fecd1b85d1fcbf66f3 
| 
|




Alternatively, you can download the archive from the command line.
Replace ` FILE_NAME ` with the package name for your
platform from the table above.



```
curl -O https://storage.apis-berlin-build0.goog/cloud-sdk-release/ FILE_NAME 
```



- Extract the contents of the file to your preferred location on your file
system. A common practice is to extract it to your home directory.


On macOS, you can do this by opening the downloaded
`.tar.gz` file in your preferred location. Alternatively, from the command line, run:



```
tar -xf FILE_NAME 
```



To replace an existing installation, delete the existing
`google-cloud-sdk` directory and then extract the archive to the same location.




- Run the installation script from the root of the folder you
extracted:

```
./google-cloud-sdk/install.sh
```

The script prompts you to perform the following setup actions. To accept,
answer `Y` when prompted.



- Install Python 3.13 and recommended modules if needed.

- Add the gcloud CLI to your `PATH` and enable command completion.

- Opt in to send [anonymous usage statistics](/sdk/docs/usage-statistics)
to help improve the gcloud CLI.



You can also perform the installation non-interactively by providing flags.
To view available flags, run:

```
./google-cloud-sdk/install.sh --help
```

To run the install script with screen reader mode enabled:

```
./google-cloud-sdk/install.sh --screen-reader = true 
```



- Optional: If you updated your `PATH` in the previous step, open a new
terminal so that the changes take effect.






The Google Cloud CLI on Windows requires Windows 8.1 and later, or Windows Server 2012 and later.


- 


Download the [Google Cloud CLI installer](https://storage.apis-berlin-build0.goog/cloud-sdk-release/GoogleCloudSDKInstaller.exe).




Alternatively, open a PowerShell terminal and run the following PowerShell commands:



```
( New-Object Net.WebClient ) .DownloadFile ( "https://storage.apis-berlin-build0.goog/cloud-sdk-release/GoogleCloudSDKInstaller.exe" , " $env :Temp\GoogleCloudSDKInstaller.exe" ) 

& $env :Temp \G oogleCloudSDKInstaller.exe

```



- 


Launch the installer and follow the prompts. The installer is signed by Google LLC.




- If you're using a screen reader, check the Turn on screen reader mode** checkbox. This
option configures `gcloud` to use status trackers instead of unicode spinners,
display progress as a percentage, and flatten tables. For more information, see the
[Accessibility features guide](/sdk/docs/enabling-accessibility-features).


- Google Cloud CLI requires Python; supported versions are Python 3.10 to 3.14. By
default, the Windows version of Google Cloud CLI comes bundled with Python 3. To use
Google Cloud CLI your operating system must be able to run a supported version of Python.


- The installer installs all necessary dependencies, including the needed Python version.
While Google Cloud CLI installs and manages Python 3 by default, you can use an existing
Python installation if necessary by **unchecking** the option to Install Bundled Python.
See [`gcloud topic startup`](/sdk/gcloud/reference/topic/startup) to
learn how to use an existing Python installation.







- After installation is complete, the installer gives you the option to create Start Menu
and Desktop shortcuts, start the Google Cloud CLI shell, and configure the
gcloud CLI. Leave the options to start the shell and configure
your installation selected. The installer starts a terminal window and runs the
[`gcloud init`](/sdk/gcloud/reference/init) command to initialize,
authorize, and configure the gcloud CLI.


- The default installation doesn't include the App Engine extensions required to deploy an
application using `gcloud` commands. These components can be installed using the
[gcloud CLI component manager](/sdk/docs/managing-components).



**Troubleshooting tips**


- If your installation is unsuccessful
due to the `find` command not being recognized, ensure your `PATH`
environment variable is set to include the folder containing `find`. Usually,
this is `C:\WINDOWS\system32;`.

- If you uninstalled the gcloud CLI, you must reboot your
system before installing the gcloud CLI again.

- If unzipping fails, run the installer as an administrator.



## (Optional) Create a universe-specific configuration

If you need to use your gcloud CLI installation with
multiple universes (for example, with Google Cloud and
Google Cloud Dedicated), you can create a specific
gcloud CLI
[configuration](/sdk/docs/configurations) for
Google Cloud Dedicated settings.

To create and switch to a new
configuration, run the following commands:


```
gcloud config configurations create CONFIG_NAME 
gcloud config configurations activate CONFIG_NAME 
```


Replace the following:

- ` CONFIG_NAME `: the unique name you have chosen for your configuration.

If you *don't* create a universe-specific configuration, the rest of these steps use the default
gcloud CLI (named `default`) configuration.

## Create your login configuration file

To set up access to your universe, you need to create a JSON configuration file
for the gcloud CLI, including domains used by Google Cloud Dedicated
and the IdP set up for your organization.

To create your login configuration file:

- 

Set the universe domain for gcloud CLI in your active configuration:


```
gcloud config set universe_domain apis-berlin-build0.goog
```


- 

Run the following commands:


```
AUDIENCE = locations/global/workforcePools/ POOL_ID /providers/ PROVIDER_ID 
UNIVERSE_WEB_DOMAIN = "cloud.berlin-build0.goog" 
UNIVERSE_API_DOMAIN = "apis-berlin-build0.goog" 

gcloud iam workforce-pools create-login-config \ 
$AUDIENCE \ 
--universe-cloud-web-domain = " $UNIVERSE_WEB_DOMAIN " \ 
--universe-domain = " $UNIVERSE_API_DOMAIN " \ 
--output-file = "wif-login-config.json" 
```


Replace the following:

- ` POOL_ID `: the unique identifier for your organization's
workload identity pool.

- ` PROVIDER_ID `: your organization's identity provider (IdP).

The output is similar to the following:


```
Created login configuration file [ wif-login-config.json ] .
```


After you have created your configuration file, you don't need to repeat this
step as long as you are signing in from the same machine.

## Sign in to Google Cloud Dedicated with the gcloud CLI

Now you can use the configuration file every time you need to sign in to Google Cloud Dedicated:

- 

To sign in from the command line, run the following command:


```
gcloud auth login --login-config = wif-login-config.json
```


- 

If you need to use [Application Default Credentials
(ADC)](/docs/authentication/application-default-credentials) (required for
running Terraform modules), run the following command:


```
gcloud auth application-default login --login-config = wif-login-config.json
```


A web page opens where you can sign in with your login details. After you've
logged in you can then go on to configure and use the gcloud CLI as
described in the rest of its documentation.

## (Optional) Set up default properties

When you set up the gcloud CLI, you are provided with a configuration
called `default` that you can use for [properties](/sdk/docs/properties) that
provide default flag values or govern the tool's behavior. Although it's optional,
we recommend configuring some default properties for gcloud CLI, such
as your default project, before using the tool. Default properties are useful if
you don't want to have to specify your project or preferred compute location
every time you run a command.

The following steps set the same properties that are configured by `gcloud init`
for Google Cloud users:

- 

To set your default project, run the following command, specifying your
chosen project ID:


```
gcloud config set project PROJECT_ID 
```


- 

If you use Compute Engine or GKE, some commands require you
to specify a compute [region or
zone](/docs/get-started-tpc/regions-and-zones). To set your default region
for commands, run the following command:


```
gcloud config set compute/region u-germany-northeast1
```


To set your default zone, run the following command:


```
gcloud config set compute/zone ZONE 
```


- 

To view your current configuration's properties, including the authenticated
user, run the following command:


```
gcloud config list
```


You can learn about how gcloud CLI configurations work and how to
create and use additional configurations in [Manage gcloud CLI
configurations](/sdk/docs/configurations). You can learn more about specifying
properties in [Manage gcloud CLI properties](/sdk/docs/properties).

## (Optional) Run commands

Run core commands to view information about your gcloud CLI installation:

- 

List accounts whose credentials are stored on the local system:


```
gcloud auth list 
```


The gcloud CLI displays a list of credentialed accounts:


```
Credentialed Accounts
ACTIVE ACCOUNT
* principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com
```


- 

List the properties in your active gcloud CLI configuration:


```
gcloud config list 
```


The gcloud CLI displays the list of properties:


```
[core]
account = principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com
disable_usage_reporting = False
project = my-project
```


- 

View information about `gcloud` commands and other topics:


```
gcloud help 
```


For example, to view the help for `gcloud compute instances create`:


```
gcloud help compute instances create 
```


The gcloud CLI displays a help topic that contains a
description of the command, a list of command flags and arguments, and
examples of how to use the command.

## What's next

- If you're an administrator setting up a Google Cloud Dedicated
organization for the first time, find out how to configure your organization
in [Set up your organization](/docs/get-started-tpc/set-up-organization).

- To find out more about what you can do with the Google Cloud CLI, see the [
Google Cloud CLI documentation](/sdk/gcloud)

- For more information about getting started with Google Cloud Dedicated, see [Get started with Google Cloud Dedicated](/docs/get-started-tpc).