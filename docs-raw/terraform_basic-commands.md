# Basic Terraform commands

Source: https://berlin.devsitetest.how/docs/terraform/basic-commands
Last updated: 2026-06-29

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/terraform/tpc-differences) for more details.














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

Terraform on Google Cloud

](https://berlin.devsitetest.how/docs/terraform)






- 








[

Guides

](https://berlin.devsitetest.how/docs/terraform/terraform-overview)












# Basic Terraform commands 






- On this page 
- [ Prepare Cloud Shell ](#prepare-cloud-shell)
- [ Prepare the directory ](#prepare-the-directory)
- [ Apply the changes ](#apply-the-changes)
- [ Reformat ](#format)
- [ Validate ](#validate)
- [ Delete changes ](#destroy)
- [ Specify the project ID ](#google_project)
- [ What's next ](#whats_next)
- 










To apply your Terraform configuration in a Google Cloud Dedicated project, complete the steps in the
following sections.

## Prepare Cloud Shell 


- Launch [Cloud Shell](https://shell.cloud.google.com/).

- 


Set the default Google Cloud Dedicated project
where you want to apply your Terraform configurations.




You only need to run this command once per project, and you can run it in any directory.


```
export GOOGLE_CLOUD_PROJECT= PROJECT_ID 
```



Environment variables are overridden if you set explicit values in the Terraform
configuration file.



## Prepare the directory

Each Terraform configuration file must have its own directory (also
called a *root module*).


- 
In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new
file within that directory. The filename must have the
`.tf` extension—for example `main.tf`. In this
tutorial, the file is referred to as `main.tf`.

```
mkdir DIRECTORY && cd DIRECTORY && touch main.tf
```



- 


If you are following a tutorial, you can copy the sample code in each section or step.



Copy the sample code into the newly created `main.tf`.



Optionally, copy the code from GitHub. This is recommended
when the Terraform snippet is part of an end-to-end solution.




- Review and modify the sample parameters to apply to your environment.

- Save your changes.

- 
Initialize Terraform. You only need to do this once per directory.

```
terraform init
```



Optionally, to use the latest Google provider version, include the `-upgrade`
option:



```
terraform init -upgrade
```



## Apply the changes


- 
Review the configuration and verify that the resources that Terraform is going to create or
update match your expectations:

```
terraform plan
```



Make corrections to the configuration as necessary.



- 
Apply the Terraform configuration by running the following command and entering `yes`
at the prompt:

```
terraform apply
```



Wait until Terraform displays the "Apply complete!" message.



- [Open your Google Cloud Dedicated project](https://console.cloud.berlin-build0.goog/) to view
the results. In the Google Cloud Dedicated console, navigate to your resources in the UI to make sure
that Terraform has created or updated them.


## Reformat

To reformat your Terraform configuration in the standard style, enter the
following command:


```
terraform fmt
```


## Validate

To check whether your configuration is valid, enter the following command:


```
terraform validate
```


## Delete changes

Remove resources previously applied with your Terraform configuration by running the following
command and entering `yes` at the prompt:


```
terraform destroy
```


## Specify the project ID

If you run the `export GOOGLE_CLOUD_PROJECT` command, most resources can infer
the `project_id`.

Some resources, such as `project_iam_*`, cannot infer the project ID. As a
workaround, some samples use the [`data "google_project"`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/project)
data source. You can replace this data source with the project ID string or a
variable.

For a sample that uses this workaround, see
[sql_instance_iam_condition](https://github.com/terraform-google-modules/terraform-docs-samples/blob/main/cloud_sql/instance_iam_condition/main.tf).

## What's next

- [Learn more about Terraform's CLI features](https://www.terraform.io/cli/commands).