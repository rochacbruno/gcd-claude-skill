# Use custom organization policies

Source: https://berlin.devsitetest.how/docs/quotas/custom-constraints
Last updated: 2026-07-06

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/docs/quotas/tpc-differences) for more details.














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

Cloud Quotas

](https://berlin.devsitetest.how/docs/quotas)






- 








[

Guides

](https://berlin.devsitetest.how/docs/quotas/overview)












# Use custom organization policies 






- On this page ** 
- [ About organization policies and constraints ](#about_organization_policies_and_constraints)

- [ Policy inheritance ](#policy-inheritance)

- [ Limitations ](#limitations)
- [ Before you begin ](#before-you-begin)

- [ Required roles ](#required-roles)

- [ Cloud Quotas supported resources ](#supported_resources)
- [ Set up a custom constraint ](#set_up_custom_constraint)
- [ Enforce a custom organization policy ](#enforce_custom_constraint)
- [ Test the custom organization policy ](#test_constraint)

- [ Create an example constraint ](#example-create-constraint)
- [ Create the policy ](#example-create-policy)
- [ Test the policy ](#example-test-policy)
- [ Delete the example policy and constraint ](#delete-example)

- [ Example custom organization policies for common use cases ](#example_constraints)
- [ What's next ](#whats_next)
- [ What's next ](#whats_next_2)
- 












This page shows you how to use Organization Policy Service custom constraints to restrict
specific operations on the following Google Cloud Dedicated in Germany resources:


- `cloudquotas.googleapis.com/QuotaPreference`

To learn more about Organization Policy, see
[Custom organization policies][op-custom].

## About organization policies and constraints

The Google Cloud Dedicated Organization Policy Service gives you centralized, programmatic
control over your organization's resources. As the
[organization policy administrator][op-admin], you can define an organization
policy, which is a set of restrictions called *constraints* that apply to
Google Cloud Dedicated resources and descendants of those resources in the
[Google Cloud Dedicated in Germany resource hierarchy][op-hierarchy]. You can enforce organization
policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints][op-constraints]
for various Google Cloud Dedicated services. However, if you want more granular,
customizable control over the specific fields that are restricted in your
organization policies, you can also create *custom constraints* and use those
custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the
resources on which you enforce the policy. For example, if you enforce a policy
on a folder, Google Cloud Dedicated enforces the policy on all projects in the
folder. To learn more about this behavior and how to change it, refer to
[Hierarchy evaluation rules][op-hierarchy-eval].

## Limitations

Custom organization policy enforcement restricts operations that create or
update `QuotaPreference` resources. The following limitations apply because some
quota change scenarios don't create or update `QuotaPreference` resources:

- 

**When using the Service Usage API**: Quota value changes initiated
through the [Service Usage API](/service-usage/docs/overview) aren't
subject to custom organization policy enforcement because they don't change
`QuotaPreference` resources. To restrict quota value changes initiated
through the Service Usage API, implement an
[IAM deny policy](/iam/docs/deny-overview) on the
`serviceusage.quota.update` permission.

- 

**When initiating quota changes in the Google Cloud Dedicated console**: Quota value
changes initiated using the Google Cloud Dedicated console aren't subject to custom
organization policy enforcement because the Google Cloud Dedicated console does not
create `QuotaPreference` resources.

## Before you begin

















- 




In the Google Cloud Dedicated console, on the project selector page,
select or create a Google Cloud Dedicated project.




Roles required to select or create a project**





- 
**Select a project**: Selecting a project doesn't require a specific
IAM role—you can select any project that you've been
granted a role on.


- 
**Create a project**: To create a project, you need the Project Creator role
(`roles/resourcemanager.projectCreator`), which contains the
`resourcemanager.projects.create` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).












[Go to project selector](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)














- 



[Verify that billing is enabled for your Google Cloud Dedicated project](/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).






















- 


[Install](/sdk/docs/install) the Google Cloud CLI.












- 


Configure the gcloud CLI to use your federated identity.



For more information, see
[
Sign in to the gcloud CLI with your federated identity](/iam/docs/workforce-log-in-gcloud).







- 


To [initialize](/sdk/docs/initializing) the gcloud CLI, run the following command:



```
gcloud init
```





















- Ensure that you know your
[organization ID](/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

### Required roles


































To get the permissions that
you need to manage custom organization policies,

ask your administrator to grant you the
Organization Policy Administrator (`roles/orgpolicy.policyAdmin`)
IAM role on the organization resource.






For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access).









You might also be able to get
the required permissions through [custom
roles](/iam/docs/creating-custom-roles) or other [predefined
roles](/iam/docs/roles-overview#predefined).











## Cloud Quotas supported resources

The following table lists the Cloud Quotas resources that you can
reference in custom constraints:



























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































| 
Resource | 
Field | 
|


| 
cloudquotas.googleapis.com/QuotaPreference | 



`resource.dimensions`
| |
| 
`resource.name`
| |
| 
`resource.quotaConfig.preferredValue`
| |
| 
`resource.quotaId`
| |
| 
`resource.service`
| | 




## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods,
conditions, and actions that are supported by the service on which you are
enforcing the organization policy. Conditions for your custom constraints are
defined using
[Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build
conditions in custom constraints using CEL, see the CEL section of
[Creating and managing custom constraints][op-cel].





[Console](#console) [gcloud](#gcloud) 
**More 






To create a custom constraint, do the following:





- 
In the Google Cloud Dedicated console, go to the Organization policies** page.


[Go to Organization policies](https://console.cloud.berlin-build0.goog/iam-admin/orgpolicies) 



- 
From the project picker, select the project that you want to set the organization
policy for.


- 
Click add **Custom constraint**.


- 
In the **Display name** box, enter a human-readable name for the constraint. This name is
used in error messages and can be used for identification and debugging. Don't use
personally identifiable information (PII) or sensitive data in display names because this
name could be exposed in error messages. This field can contain up to 200 characters.


- 
In the **Constraint ID** box, enter the ID that you want for your new custom
constraint. A custom constraint can only contain letters (including upper and lowercase) or
numbers, for example `custom.restrictQuotaChangeCpusPerProjectPerRegion`. This field can contain up to
70 characters, not counting the prefix (`custom.`), for example,
`organizations/123456789/customConstraints/custom`. Don't include PII or
sensitive data in your constraint ID, because it could be exposed in error messages.


- 
In the **Description** box, enter a human-readable description of the constraint. This
description is used as an error message when the policy is violated. Include details about
why the policy violation occurred and how to resolve the policy violation. Don't include
PII or sensitive data in your description, because it could be exposed in error messages.
This field can contain up to 2000 characters.


- 
In the **Resource type** box, select the name of the Google Cloud Dedicated REST resource
containing the object and field that you want to restrict—for example,
`container.googleapis.com/NodePool`. Most resource types support up to 20 custom
constraints. If you attempt to create more custom constraints, the operation fails.


- 
Under **Enforcement method**, select whether to enforce the
constraint on a REST `CREATE` method or both `CREATE` and
`UPDATE` methods. If you enforce the constraint with the `UPDATE`
method on a resource that violates the constraint, changes to that resource are blocked by
the organization policy unless the change resolves the violation.



To see supported methods for each service, find the service in
[
Services that support custom constraints](/organization-policy/reference/custom-constraint-supported-services).



- 
To define a condition, click edit **Edit condition**.




- 
In the **Add condition** panel, create a CEL condition that refers to a supported
service resource, for example, `resource.management.autoUpgrade == false`. This
field can contain up to 1000 characters. For details about CEL usage, see
[
Common Expression Language](/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language).
For more information about the service resources you can use in your custom constraints,
see [
Custom constraint supported services](/resource-manager/docs/organization-policy/custom-constraint-supported-services).


- 
Click **Save**.




- 
Under **Action**, select whether to allow or deny the evaluated method if the condition
is met.



The deny action means that the operation to create or update the resource is blocked if the
condition evaluates to true.




The allow action means that the operation to create or update the resource is permitted only
if the condition evaluates to true. Every other case except those explicitly listed in the
condition is blocked.



- 
Click **Create constraint**.



When you have entered a value into each field, the equivalent YAML configuration for this
custom constraint appears on the right.










- 
To create a custom constraint, create a YAML file using the following format:


```
name : organizations/ ** ORGANIZATION_ID /customConstraints/ CONSTRAINT_NAME 
resourceTypes : RESOURCE_NAME 
methodTypes : 
- CREATE
- UPDATE 
condition : " CONDITION " 
actionType : ACTION 
displayName : DISPLAY_NAME 
description : DESCRIPTION 
```



Replace the following:





- 
` ORGANIZATION_ID `: your organization ID, such as
`123456789`.


- 
` CONSTRAINT_NAME `: the name that you want for your new custom
constraint. A custom constraint can only contain letters (including upper and lowercase)
or numbers, for example, `custom.restrictQuotaChangeCpusPerProjectPerRegion`. This field can contain up to 70
characters, not counting the prefix (`custom.`)— for example,
`organizations/123456789/customConstraints/custom`. Don't include PII or
sensitive data in your constraint ID, because it could be exposed in error messages.


- 
` RESOURCE_NAME `: the fully qualified name of the Google Cloud Dedicated
resource containing the object and field that you want to restrict. For example,
`cloudquotas.googleapis.com/QuotaPreference`. Most resource types support up to 20 custom
constraints. If you attempt to create more custom constraints, the operation fails.


- 
`methodTypes`: the REST methods that the constraint is enforced on.
Can be `CREATE` or both `CREATE` and
`UPDATE`. If you enforce the constraint with the `UPDATE` method on
a resource that violates the constraint, changes to that resource are blocked by the
organization policy unless the change resolves the violation.



To see the supported methods for each service, find the service in
[
Services that support custom constraints](/organization-policy/reference/custom-constraint-supported-services).



- 
` CONDITION `: a [
CEL condition](/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service
resource. This field can contain up to 1000 characters. For example,
`"resource.service == compute.googleapis.com && resource.quotaId == CPUS-per-project-region"`.




For more information about the resources available to write conditions against, see
[Supported resources](#supported_resources).




- 
` ACTION `: the action to take if the `condition` is met.
Possible values are `ALLOW` and
`DENY`.




The allow action means that if the condition evaluates to true, the operation to create or
update the resource is permitted. This also means that every other case except the one
explicitly listed in the condition is blocked.





The deny action means that if the condition evaluates to true, the operation to create or
update the resource is blocked.




- 
` DISPLAY_NAME `: a human-readable name for the constraint. This name
is used in error messages and can be used for identification and debugging. Don't use PII
or sensitive data in display names because this name could be exposed in error messages.
This field can contain up to 200 characters.


- 
` DESCRIPTION `: a human-friendly description of the constraint to
display as an error message when the policy is violated. This field can contain up to
2000 characters.




- 
After you have created the YAML file for a new custom constraint, you must set it up to make
it available for organization policies in your organization. To set up a custom constraint,
use the
[
`gcloud org-policies set-custom-constraint`](/sdk/gcloud/reference/org-policies/set-custom-constraint) command:


```
gcloud org-policies set-custom-constraint CONSTRAINT_PATH 
```



Replace ` CONSTRAINT_PATH ` with the full path to your custom constraint
file. For example, `/home/user/customconstraint.yaml`.




After this operation is complete, your custom constraints are available as organization
policies in your list of Google Cloud Dedicated in Germany organization policies.



- 
To verify that the custom constraint exists, use the
[
`gcloud org-policies list-custom-constraints`](/sdk/gcloud/reference/org-policies/list-custom-constraints) command:


```
gcloud org-policies list-custom-constraints --organization = ORGANIZATION_ID 
```



Replace ` ORGANIZATION_ID ` with the ID of your organization resource.




For more information, see
[
Viewing organization policies](/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies).







## Enforce a custom organization policy






You can enforce a constraint by creating an organization policy that references it, and then
applying that organization policy to a Google Cloud Dedicated in Germany resource.


[Console](#console) [gcloud](#gcloud) 
More 







- 
In the Google Cloud Dedicated console, go to the Organization policies** page.


[Go to Organization policies](https://console.cloud.berlin-build0.goog/iam-admin/orgpolicies) 



- 
From the project picker, select the project that you want to set the
organization policy for.


- 
From the list on the **Organization policies** page, select your constraint to view
the **Policy details** page for that constraint.


- 
To configure the organization policy for this resource, click **Manage policy**.


- 
On the **Edit policy** page, select **Override parent's policy**.


- 
Click **Add a rule**.


- 
In the **Enforcement** section, select whether this organization policy is enforced or
not.


- 
Optional: To make the organization policy conditional on a tag, click
**Add condition**. Note that if you add a conditional rule to an organization
policy, you must add at least one unconditional rule or the policy cannot be saved. For more
information, see
[
Scope organization policies with tags](/organization-policy/scope-policies).




- 
Click **Test changes** to simulate the effect of the organization policy. For more
information, see [
Test organization policy changes with Policy Simulator](/policy-intelligence/docs/test-organization-policies).



- 
To enforce the organization policy in dry-run mode, click **Set dry run policy**. For
more information, see [
Test organization policies](/organization-policy/test-policies).


- 
After you verify that the organization policy in dry-run mode works as intended, set the
live policy by clicking **Set policy**.










- 
To create an organization policy with boolean rules, create a policy YAML file that
references the constraint:


```
name : projects/ PROJECT_ID /policies/ CONSTRAINT_NAME 
spec : 
rules : 
- enforce : true 

dryRunSpec : 
rules : 
- enforce : true 
```



Replace the following:





- 
` PROJECT_ID `: the project that you want to enforce your constraint
on.


- 
` CONSTRAINT_NAME `: the name you defined for your custom constraint. For
example, `custom.restrictQuotaChangeCpusPerProjectPerRegion`.





- 
To enforce the organization policy in
[dry-run mode](/organization-policy/test-policies), run
the following command with the `dryRunSpec` flag:


```
gcloud org-policies set-policy POLICY_PATH --update-mask = dryRunSpec
```



Replace ` POLICY_PATH ` with the full path to your organization policy
YAML file. The policy requires up to 15 minutes to take effect.



- 
After you verify that the organization policy in dry-run mode works as intended, set the
live policy with the `org-policies set-policy` command and the `spec`
flag:


```
gcloud org-policies set-policy POLICY_PATH --update-mask = spec
```




Replace ` POLICY_PATH ` with the full path to your organization policy
YAML file. The policy requires up to 15 minutes to take effect.







## Test the custom organization policy

The following examples create a custom constraint and policy that deny all
`QuotaPreference` settings in a specific project for the
`compute.googleapis.com` service, which has a `CPUS-per-project-region`
quota ID.

Before you begin, you need to know the following:

- Your organization ID

- Your project ID

In the examples that follow, replace ` ORGANIZATION_ID ` and
` PROJECT_ID ` with the strings for your configuration.

### Create an example constraint

The following code snippet shows an example of creating a quota preference
constraint. When creating your own quota preference constraints, update these
fields as needed for your configuration.

- 

Save the following file as `quota-constraint.yaml`:


```
name : organizations/ ORGANIZATION_ID /customConstraints/custom.restrictCPUsPerProjectRegion 
resourceTypes : 
- cloudquotas.googleapis.com/QuotaPreference 
methodTypes : 
- CREATE 
- UPDATE 
condition : "resource.service == 'compute.googleapis.com' && resource.quotaId == 'CPUS-per-project-region'" 
actionType : DENY 
displayName : Restrict quota update for compute CPUS-per-project-region 
description : Deny quota change for the 'CPUS-per-project-region' quota ID of 'compute.googleapis.com' service. 
```


Replace the following:

- ` ORGANIZATION_ID `: your organization ID.
For help finding your organization ID, see
[Getting your organization resource ID][1].

This defines a constraint where quota cannot be changed for the
`CPUS-per-project-region` quota ID of `compute.googleapis.com` service.

- 

Apply the constraint:


```
gcloud org-policies set-custom-constraint quota-constraint.yaml
```


- 

Verify that the constraint exists:


```
gcloud org-policies list-custom-constraints --organization = ORGANIZATION_ID 
```


- 

The output is similar to the following:


```
CUSTOM_CONSTRAINT ACTION_TYPE METHOD_TYPES RESOURCE_TYPES DISPLAY_NAME
custom.restrictCPUsPerProjectRegion DENY CREATE,UPDATE cloudquotas.googleapis.com/QuotaPreference Restrict quota update for compute CPUS-per-project-region
```


### Create the policy

- 

Save the following file as `quota-policy.yaml`:


```
name : projects/ PROJECT_ID /policies/custom.restrictCPUsPerProjectRegion 
spec : 
rules : 
- enforce : true 
```


Replace ` PROJECT_ID ` with your project ID.

- 

Apply the policy:


```
gcloud org-policies set-policy quota-policy.yaml
```


- 

Verify that the policy exists:


```
gcloud org-policies list --project = PROJECT_ID 
```


The output is similar to the following:


```
CONSTRAINT LIST_POLICY BOOLEAN_POLICY ETAG
custom.restrictCPUsPerProjectRegion - SET CNXIq78GEODKiK4D-
```


After you apply the policy, wait for about two minutes for Google Cloud Dedicated to
start enforcing the policy.

### Test the policy

To test the policy, create a quota preference request:

- 

For example, run the following gcloud CLI command to create
a quota preference for Compute Engine:


```
gcloud beta quotas preferences create \ 
--service = compute.googleapis.com \ 
--quota-id = CPUS-per-project-region \ 
--preferred-value = 30 \ 
--project = PROJECT_ID 
```


- 

The output is similar to the following:


```
Operation denied by org policy on resource 'projects/ PROJECT_ID /locations/global': ["customConstraints/custom.restrictCPUsPerProjectRegion": "Deny quota change for the 'CPUS-per-project-region' quota ID of 'compute.googleapis.com' service."]
```


### Delete the example policy and constraint

After you have tested the policy, you can delete it:

- 

Delete the policy:


```
gcloud org-policies delete custom.restrictCPUsPerProjectRegion --project = PROJECT_ID 
```


- 

Delete the constraint:


```
gcloud org-policies delete-custom-constraint custom.restrictCPUsPerProjectRegion \ 
--organization = ORGANIZATION_ID 
```


## Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints.




| 
Description | 
Constraint syntax | 
|




| 
Don't allow changes for a specific service's quota ID | 


```
name : organizations/ ORGANIZATION_ID /customConstraints/custom.restrictCPUsPerProjectRegionQuota 
resourceTypes : 
- cloudquotas.googleapis.com/QuotaPreference 
methodTypes : 
- CREATE 
- UPDATE 
condition : |- 
resource.service == 'compute.googleapis.com' 
&& resource.quotaId == 'CPUS-per-project-region' 
actionType : DENY 
displayName : Deny quota update for compute CPUS-per-project-region 
description : Deny quota change for the 'CPUS-per-project-region' quota ID of 'compute.googleapis.com' service. 

```
| 
|

| 
Restrict quota value to be under a specified value | 


```
name : organizations/ ORGANIZATION_ID /customConstraints/custom.restrictCPUsPerProjectRegionQuotaLimit 
resourceTypes : 
- cloudquotas.googleapis.com/QuotaPreference 
methodTypes : 
- CREATE 
- UPDATE 
condition : |- 
resource.service == 'compute.googleapis.com' 
&& resource.quotaId == 'CPUS-per-project-region' 
&& resource.quotaConfig.preferredValue 
actionType : ALLOW 
displayName : Restrict quota update for compute CPUS-per-project-region 
description : Restrict quota change for the 'CPUS-per-project-region' quota ID of 'compute.googleapis.com' service. 

```
| 
|




## What's next



- Learn more about
[Organization Policy Service](/organization-policy/overview).

- Learn more about how to
[create and manage organization policies](/organization-policy/create-organization-policies).

- See the full list of managed
[organization policy constraints](/organization-policy/reference/org-policy-constraints).

[op-admin]: /iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin
[op-custom]: /organization-policy/overview#custom-organization-policies
[op-hierarchy]: /resource-manager/docs/cloud-platform-resource-hierarchy
[op-constraints]: /organization-policy/reference/org-policy-constraints
[op-hierarchy-eval]: /organization-policy/hierarchy-evaluation#disallow_inheritance
[op-cel]: /organization-policy/create-custom-constraints#common_expression_language

## What's next

- [Quota permissions](/docs/quotas/permissions)

- [Configure VPC Service Controls](/docs/quotas/configure-vpc-service-controls)

- [View and manage quotas](/docs/quotas/view-manage)