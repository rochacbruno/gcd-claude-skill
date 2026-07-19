# Best practices for testing

Source: https://berlin.devsitetest.how/docs/terraform/best-practices/testing
Last updated: 2026-07-17

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












# Best practices for testing 






- On this page 
- [ Use less expensive test methods first ](#test-methods)
- [ Start small ](#start-small)
- [ Randomize project IDs and resource names ](#randomize)
- [ Use a separate environment for testing ](#test-environment)
- [ Clean up all resources ](#clean-up)
- [ Optimize test runtime ](#runtime)
- [ What's next ](#whats-next)
- 










This document provides guidelines and recommendations for testing
Terraform for Google Cloud Dedicated modules and configurations.

Testing Terraform modules and configurations sometimes follows different
patterns and conventions from testing application code. While testing
application code primarily involves testing the business logic of applications
themselves, fully testing infrastructure code requires deploying real cloud
resources to minimize the risk of production failures. There are a few
considerations when running Terraform tests:

- Running a Terraform test creates, modifies, and destroys real
infrastructure, so your tests can potentially be time-consuming and expensive.

- *You cannot purely unit test an end-to-end architecture*. The best
approach is to break up your architecture into modules and test those
individually. The benefits of this approach include faster iterative
development due to faster test runtime, reduced costs for each test, and
reduced chances of test failures from factors beyond your control.

- *Avoid reusing state if possible*. There may be situations where you
are testing with configurations that share data with other configurations,
but ideally each test should be independent and should not reuse state
across tests.

## Use less expensive test methods first

There are multiple methods that you can use to test Terraform. In ascending
order of cost, run time, and depth, they include the following:

- **Static analysis:** Testing the syntax and structure of your configuration
without deploying any resources, using tools such as compilers, linters,
and dry runs. To do so, use
[`terraform validate`](https://www.terraform.io/cli/commands/validate)

- **Module integration testing**: To ensure that modules work correctly, test
individual modules in isolation. Integration testing for modules
involves deploying the module into a test environment and verifying that
expected resources are created. There are several testing frameworks that
make it easier to write tests, as follows:

- [Google's blueprint testing framework](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/infra/blueprint-test)

- [Terratest](https://terratest.gruntwork.io/)

- [Kitchen-Terraform](https://newcontext-oss.github.io/kitchen-terraform/)

- [InSpec](https://github.com/inspec/inspec-gcp)

- [tftest](https://pypi.org/project/tftest/)

- **End-to-end testing:** By extending the integration testing approach to
an entire environment, you can confirm that multiple modules work together.
In this approach, deploy all modules that make up the architecture in a
fresh test environment. Ideally, the test environment is as similar as
possible to your production environment. This is costly but provides the
greatest confidence that changes don't break your production environment.

## Start small

Make sure that your tests iteratively build on each other. Consider running
smaller tests first and then working up to more complex tests, using a
*fail fast* approach.

## Randomize project IDs and resource names

To avoid naming conflicts, make sure that your configurations have a globally
unique project ID and non-overlapping resource names within each project. To do
this, use namespaces for your resources. Terraform has a built-in
[random provider](https://registry.terraform.io/providers/hashicorp/random/latest/docs) 
for this.

## Use a separate environment for testing

During testing, many resources are created and deleted. Ensure that the
environment is isolated from development or production projects to avoid
accidental deletions during resource cleanup. The best approach is to have each
test create a fresh project or folder. To avoid misconfiguration, consider
creating service accounts specifically for each test execution.

## Clean up all resources

Testing infrastructure code means that you are deploying actual resources.
To avoid incurring charges, consider implementing a clean-up step.

To destroy all remote objects managed by a particular configuration, use the
`terraform destroy` command. Some testing frameworks have a built-in cleanup
step for you. For example, if you are using Terratest, add
`defer terraform.Destroy(t, terraformOptions)` to your test. If you're using
Kitchen-Terraform, delete your workspace using
`terraform kitchen delete WORKSPACE_NAME `.

After you run the `terraform destroy` command, also run additional clean-up
procedures to remove any resources that Terraform failed to destroy. Do this by
deleting any projects used for test execution or by using a tool like the
[`project_cleanup`](https://github.com/terraform-google-modules/terraform-google-scheduled-function/tree/master/modules/project_cleanup) module.

## Optimize test runtime

To optimize your test execution time, use the following approaches:

- **Run tests in parallel.** Some testing frameworks support running
multiple Terraform tests simultaneously.

- For example, with Terratest you can do this by adding
`t.Parallel()` after the test function definition.

- **Test in stages.** Separate your tests into independent configurations
that can be tested separately. This approach removes the need to go through
all stages when running a test, and accelerates the iterative development
cycle.

- For example, in Kitchen-Terraform, split tests into
separate suites. When iterating, execute each suite independently.

- Similarly, using Terratest, wrap each stage of your test with
`stage(t, STAGE_NAME , CORRESPONDING_TEST*FUNCTION* *)*`*.
Set environment variables that indicate which tests to run. For example,
`SKIP`*` STAGE_NAME ="true"`.

- The
[blueprint testing framework](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/infra/blueprint-test)
supports staged execution.

## What's next

- Learn about [general style and structure best practices for Terraform on Google Cloud Dedicated](/docs/terraform/best-practices/general-style-structure).

- Learn about [best practices when using Terraform root modules](/docs/terraform/best-practices/root-modules).