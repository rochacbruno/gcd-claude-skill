# Quickstart: Grant roles in the Google Cloud Dedicated console

Source: https://berlin.devsitetest.how/iam/docs/grant-role-console
Last updated: 2026-06-25

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/iam/docs/tpc-differences) for more details.














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

Security

](https://berlin.devsitetest.how/docs/security)






- 








[

IAM

](https://berlin.devsitetest.how/iam/docs)






- 








[

Guides

](https://berlin.devsitetest.how/iam/docs/overview)

















- On this page ** 
- [ Before you begin ](#before-you-begin)

- [ Create a Google Cloud Dedicated project ](#create-project)
- [ Ensure that you have the required roles ](#required-roles)
- [ Enable the APIs ](#enable-apis)

- [ Grant an IAM role ](#grant_an_iam_role)
- [ Observe the effects of IAM roles ](#observe_the_effects_of_iam_roles)
- [ Grant additional roles to the same principal ](#grant-other-roles)
- [ Revoke IAM roles ](#revoke-roles)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Grant an IAM role by using the Google Cloud Dedicated console 




Learn how to use the Google Cloud Dedicated console to grant
IAM roles to principals at the project level.

See the following video for a quick walkthrough:

[ ](https://www.youtube.com/watch?v=Sdt-i-Q7tyA)





## Before you begin



### Create a Google Cloud Dedicated project

For this quickstart, you need a new Google Cloud Dedicated project.








- 
Ensure that you have the Project Creator IAM role
(`roles/resourcemanager.projectCreator`). [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).



- 


In the Google Cloud Dedicated console, go to the project selector page.



[Go to project selector](https://console.cloud.berlin-build0.goog/projectselector2/home/dashboard)




- 


Click Create project**.



- 


Name your project. Make a note of your generated project ID.



- 


Edit the other fields as needed.



- 


Click **Create**.





### Ensure that you have the required roles










Make sure that you have the following role or roles on the project:

Project IAM Admin



#### Check for the roles





- 


In the Google Cloud Dedicated console, go to the **IAM** page.


[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project)


- 

Select the project.



- 


In the **Principal** column, find all rows that identify you or a group that
you're included in. To learn which groups you're included in, contact your
administrator.




- 
For all rows that specify or include you, check the **Role** column to see whether
the list of roles includes the required roles.





#### Grant the roles





- 


In the Google Cloud Dedicated console, go to the **IAM** page.





[Go to IAM](https://console.cloud.berlin-build0.goog/projectselector/iam-admin/iam?supportedpurview=project)


- 

Select the project.



- 
Click person_add **Grant access**.


- 


In the **New principals** field, enter your user identifier.

This is typically the identifier for a user in a workforce identity pool. For details,
see [
Represent workforce pool users in IAM policies](/iam/docs/workforce-identity-federation#representing-workforce-users), or contact your administrator.





- 
Click **Select a role**, then search for the role.

- 
To grant additional roles, click add **Add
another role** and add each additional role.


- 
Click **Save**.







### Enable the APIs




Enable the IAM and Resource Manager APIs.






**Roles required to enable APIs**


To enable APIs, you need the Service Usage Admin IAM
role (`roles/serviceusage.serviceUsageAdmin`), which
contains the `serviceusage.services.enable` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).



[Enable the APIs](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)






## Grant an IAM role

Grant a principal the Logs Viewer role on the project.

- 

In the Google Cloud Dedicated console, go to the **IAM** page.

[Go to IAM](https://console.cloud.berlin-build0.goog/iam-admin/iam?supportedpurview=project) 

- 

Select your new project.

- 

Click person_add **Grant access**.

- 

Enter an identifier for the principal. For example,
`//iam.googleapis.com/locations/global/workforcePools/my-pool/subject/my-user@example.com`.

- 

From the **Select a role** drop-down menu, search for **Logs Viewer**,
then click **Logs Viewer**.

- 

Click **Save**.

- 

Verify that the principal and the corresponding role are listed in the
IAM page.

You have successfully granted an IAM role to a principal.

## Observe the effects of IAM roles

Verify that the principal you granted a role to can access the expected
Google Cloud Dedicated console pages by doing the following:

- 

Send the following URL to the principal to whom you granted the role in the
preceding step:


```
https://console.cloud.berlin-build0.goog/logs?project= ** PROJECT_ID 
```


This URL takes the principal to the **Logs Explorer** page for your project.

- 

Verify that the principal is able to access and view the URL.

If the principal tries to access a different Google Cloud Dedicated console page that
they don't have access to, they see an error message.



## Grant additional roles to the same principal

Grant the principal the Compute Viewer role in addition to their Logs Viewer
role.

- 

In the Google Cloud Dedicated console, go to the **IAM** page.

[Go to IAM](https://console.cloud.berlin-build0.goog/iam-admin/iam) 

- 

Locate the row that contains the principal to whom you want to grant another
role, and click **Edit principal** edit 
in that row.

- 

In the **Edit permissions** pane, click **Add another role**.

- 

From the **Select a role** drop-down menu, search for **Compute Viewer**,
then click **Compute Viewer**. Click **Save**.

- 

Click **Save**.

The principal now has a second IAM role.



## Revoke IAM roles

Revoke the roles you granted to the principal in the preceding steps by doing
the following:

- 

Locate the row that contains the principal that you granted roles to and
click **Edit principal** edit 
in that row.

- 

In the **Edit permissions** pane, click the delete icon next to the Logs
Viewer and Compute Viewer roles.

- 

Click **Save**.

You have now removed the principal from both of the roles. If they try to view
the **Logs Explorer** page, they see the following error message:

`You don't have permissions to view logs.`






## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






Clean up by deleting the project that you created for this quickstart.





- 
In the Google Cloud Dedicated console, go to the Manage resources** page.


[Go to Manage resources](https://console.cloud.berlin-build0.goog/iam-admin/projects)




- 
In the project list, select the project that you
want to delete, and then click **Delete**.


- 
In the dialog, type the project ID, and then click
**Shut down** to delete the project.







## What's next



- [Learn the basics](/iam/docs/overview) of IAM.

- Review the [list of all IAM roles](/iam/docs/understanding-roles).

- Find out how to [manage access with IAM](/iam/docs/granting-changing-revoking-access).