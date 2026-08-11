# Organization Policy overview

Source: https://documentation.s3ns.fr/organization-policy/overview
Last updated: 2026-07-29

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/organization-policy/tpc-differences) for more details.














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

Organization Policy

](https://documentation.s3ns.fr/organization-policy)






- 








[

Guides

](https://documentation.s3ns.fr/organization-policy/overview)












# Organization Policy overview 






- On this page 
- [ Benefits ](#benefits)
- [ Common use cases ](#common_use_cases)
- [ Differences from Identity and Access Management ](#differences_from_iam)
- [ How organization policy works ](#how_organization_policy_works)
- [ Constraints ](#constraints)

- [ Managed constraints ](#managed-constraints)
- [ Custom constraints ](#custom-constraints)
- [ Managed constraints (legacy) ](#legacy-constraints)

- [ Conditional organization policies ](#conditional_organization_policies)
- [ Inheritance ](#inheritance)
- [ Violations ](#violations)
- [ Next steps ](#next_steps)
- 










The Organization Policy Service gives you centralized and programmatic control over your
organization's Cloud de Confiance resources. As the
[organization policy administrator](/organization-policy/create-organization-policies#delegate-admin),
you can configure constraints across your entire
[resource hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy).

## Benefits 

- Centralize control to configure restrictions on how your organization's
resources can be used.

- Define and establish guardrails for your development teams to stay within
compliance boundaries.

- Help project owners and their teams move quickly without fear of breaking
compliance.

## Common use cases

Organization policies allow you to do the following:

- [Limit resource sharing based on domain](/organization-policy/restrict-domains).

- [Limit the usage of Identity and Access Management (IAM) service accounts](/organization-policy/restrict-service-accounts).

There are many more constraints that give you fine-grained control of your
organization's resources. For more information, see the
[list of all Organization Policy constraints](/organization-policy/reference/org-policy-constraints).

## Differences from Identity and Access Management

[Identity and Access Management](/iam) focuses on *who*, and lets the administrator
[authorize](/resource-manager/docs/access-control-org) who can take action on
specific resources based on permissions.

Organization Policy focuses on *what*, and lets the administrator set
restrictions on specific resources to determine how they can be configured.

## How organization policy works

An organization policy configures a single [constraint](#constraints) that
restricts one or more Cloud de Confiance services. The organization policy is
set on an organization, folder, or project resource to enforce the constraint on
that resource and any child resources.

An organization policy contains one or more *rules* that specify how, and
whether, to enforce the constraint. For example, an organization policy could
contain one rule that enforces the constraint only on resources tagged
`environment=development`, and another rule that prevents the constraint from
being enforced on other resources.

Descendants of the resource to which the organization policy is attached
[inherit](#inheritance) the organization policy. By applying an organization
policy to the organization resource, the organization policy administrator can
control enforcement of that organization policy and configuration of
restrictions across your organization.



## Constraints

A constraint is a particular type of restriction against a
[Cloud de Confiance service](/docs/overview/cloud-platform-services) or a list
of Cloud de Confiance services. Think of the constraint as a blueprint that
defines what behaviors are controlled. For example, you can restrict project
resources from accessing Compute Engine storage resources using the
`compute.storageResourceUseRestrictions` constraint.

This blueprint is then set on a resource in your
[resource hierarchy](/resource-manager/docs/cloud-platform-resource-hierarchy)
as an organization policy, which applies the rules defined in the constraint.
The Cloud de Confiance service mapped to that constraint and associated with
that resource enforces the restrictions configured within the organization
policy.

An organization policy is defined in a YAML or JSON file by the constraint it
enforces and optionally by the conditions under which the constraint is
enforced. Each organization policy enforces exactly one constraint in active
mode, dry-run mode, or both.

Managed constraints have list or boolean parameters that are determined by
the enforcing Cloud de Confiance service.

Custom constraints are functionally similar to managed constraints with boolean
parameters, and are either enforced or not enforced.

Legacy managed constraints have one or more list rules or boolean rules based on
the constraint type. List rules are a collection of allowed or denied values.
Boolean rules can allow all values, deny all values, or determine if a
constraint is enforced or not enforced.

### Managed constraints

Managed constraints are designed to replace equivalent legacy managed
constraints, but with additional flexibility and greater insight from
[Policy Intelligence tools](#policy-intelligence). These constraints
have similar structure to custom organization policy constraints, but are
managed by Google.

If the equivalent legacy managed constraint has a constraint type of boolean,
the managed constraint can either be enforced or not in the same way. For
example, the following organization policy enforces
`iam.managed.disableServiceAccountCreation`, which is the equivalent constraint
to `iam.disableServiceAccountCreation`:


```
name : organizations/1234567890123/policies/iam.managed.disableServiceAccountCreation 
spec : 
rules : 
- enforce : true 
```


If the equivalent legacy managed constraint has a constraint type of list, the
managed constraint supports defining parameters that define the resources and
behaviors that are restricted by the constraint. For example, the following
organization policy enforces a managed constraint that only allows the
`example.com` and `altostrat.com` domains to be added to
Essential Contacts for `organizations/1234567890123`:


```
name : organizations/1234567890123/policies/essentialcontacts.managed.allowedContactDomains 
spec : 
rules : 
- enforce : true 
parameters : 
allowedDomains : 
- @ example.com 
- @ altostrat.com 
```


By default, managed constraints support simulation in [Policy Simulator
for Organization Policy](/policy-intelligence/docs/test-organization-policies).
If a managed constraint doesn't support simulation, it's noted in the
[table of constraints](/organization-policy/reference/org-policy-constraints), and
by the `simulation_disabled` field being set to `true` in the
constraint definition.

### Custom constraints

Like managed constraints, custom constraints allow or restrict resource creation
and updates. However, custom constraints are managed by your organization
instead of by Google. You can use
[Policy Intelligence tools](#policy-intelligence) to test and analyze
your custom organization policies.

For a list of service resources that support custom constraints, see
[Custom constraint supported services](/organization-policy/reference/custom-constraint-supported-services).

To learn more about using custom organization policies, see
[Create custom constraints](/organization-policy/create-custom-constraints).

For a list of sample custom constraints, see the
[custom organization policy library](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/custom-organization-policy-library) on GitHub.

### Managed constraints (legacy)

Legacy managed constraints have a *constraint type* of list or boolean, which
determines the values that can be used for checking enforcement. The enforcing
Cloud de Confiance service will evaluate the constraint type and value to
determine the restriction that is enforced.

These legacy constraints were previously known as *predefined constraints*.

#### List rules

Legacy managed constraints with list rules allow or disallow a list of values
that are defined in an organization policy. These legacy constraints were
previously known as *list constraints*. The list of allowed or denied values is
expressed as a hierarchy subtree string. The subtree string specifies the type
of resource it applies to. For example, the legacy managed constraint
`constraints/compute.trustedImageProjects` takes a list of project IDs in the
form of `projects/ PROJECT_ID `.

You can specify that all values are allowed, all values are denied, or that a
specific list of values are either allowed or denied. When you specify a list
of allowed or denied values, Organization Policy implicitly evaluates that only
those values are allowed or denied. For example, if you have a constraint that
allows only `projects/ PROJECT_ID `, then all other values are
implicitly denied.

Values can be given a prefix in the form `prefix:value` for constraints that
support them, which gives the value additional meaning:

- 

`is:` - applies a comparison against the exact value. This is the same
behavior as not having a prefix, and is required when the value includes a
colon.

- 

`under:` - applies a comparison to the value and all of its child values. If
a resource is allowed or denied with this prefix, its child resources are also
allowed or denied. The value provided must be the ID of an organization,
folder, or project resource.

- 

`in:` - applies a comparison to all resources that include this value. For
example, you can add `in:us-locations` to the denied list of the
`constraints/gcp.resourceLocations` constraint to block all locations that are
included in the `us` region.

If no list of values is provided, or the organization policy is set to the
Google-managed default, then the default behavior of the constraint takes
effect, which either allows all values or denies all values.

The following organization policy enforces a legacy managed constraint that
allows the Compute Engine VM instances `vm-1` and `vm-2` in
`organizations/1234567890123` to access external IP addresses:


```
name : organizations/1234567890123/policies/compute.vmExternalIpAccess 
spec : 
rules : 
- values : 
allowedValues : 
- is:projects/project_a/zones/us-central1-a/instances/vm-1 
- is:projects/project_b/zones/us-central1-a/instances/vm-2 
```


#### Boolean rules

A legacy managed constraint with a boolean rule is either enforced or not
enforced. For example, `constraints/compute.disableSerialPortAccess` has two
possible states:

- Enforced - the constraint is enforced, and serial port access is not
allowed.

- Not enforced - the `disableSerialPortAccess` constraint is not enforced or
checked, so serial port access is allowed.

If the organization policy is set to the Google-managed default, then the
default behavior for the constraint takes effect.

These legacy constraints were previously known as *boolean constraints*.

The following organization policy enforces a legacy managed constraint that
disables the creation of external service accounts in
`organizations/1234567890123`:


```
name : organizations/1234567890123/policies/iam.disableServiceAccountCreation 
spec : 
rules : 
- enforce : true 
```


## Conditional organization policies

Tags provide a way to conditionally enforce constraints based on whether a
resource has a specific tag. You can use tags and conditional enforcement of
constraints to provide centralized control of the resources in your hierarchy.

For more information about tags, see
[Tags overview](/resource-manager/docs/tags/tags-overview). To learn how to set
a conditional organization policy using tags, see
[Scope organization policies with tags](/organization-policy/scope-policies).

## Inheritance

When an organization policy is set on a resource, all descendants of that
resource inherit the organization policy by default. If you set an
organization policy on the organization resource, then the configuration of
restrictions defined by that policy will be passed down through all descendant
folders, projects, and service resources.

You can set an organization policy on a descendant resource that either
overwrites the inheritance or inherits the organization policy of the parent
resource. Organization policies that enforce legacy managed constraints are
merged based on the rules of hierarchy evaluation. This system provides precise
control for how your organization policies apply throughout your organization
and where you want exceptions made.

To learn more, see
[Hierarchy evaluation](/organization-policy/hierarchy-evaluation).

## Violations

A violation is when a Cloud de Confiance service acts or is in a state that is
counter to the organization policy restriction configuration within the scope of
its resource hierarchy. Cloud de Confiance services will enforce constraints to
prevent violations, but the application of new organization policies is usually
not retroactive. If an organization policy constraint is retroactively
enforced, it will be labeled as such on the
[organization policy constraints](/organization-policy/reference/org-policy-constraints)
page.

If a new organization policy sets a restriction on an action or state that a
service is already in, the policy is considered to be in violation, but the
service won't stop its original behavior. You will need to address this
violation manually. This prevents the risk of a new organization policy
completely shutting down your business continuity.

## Next steps

- Learn about the [Organization Policy differences in Cloud de Confiance versus Google Cloud](/organization-policy/tpc-differences).

- 

Learn [how to define organization policies](/organization-policy/create-organization-policies).

- 

Explore the [solutions you can accomplish](/organization-policy/reference/org-policy-constraints)
with organization policy constraints.