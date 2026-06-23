# Quickstart: Discover object storage with the Google Cloud Dedicated console

Source: https://berlin.devsitetest.how/storage/docs/discover-object-storage-console
Last updated: 2026-06-18

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/storage/docs/tpc-differences) for more details.














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

Storage

](https://berlin.devsitetest.how/docs/storage)






- 








[

Cloud Storage

](https://berlin.devsitetest.how/storage/docs)






- 








[

Guides

](https://berlin.devsitetest.how/storage/docs/discover-object-storage-console)

















- On this page ** 
- [ Before you begin ](#before-you-begin)
- [ Create a bucket ](#create_a_bucket)
- [ Upload an object into the bucket ](#upload_an_object_into_the_bucket)
- [ Download the object ](#download_the_object)
- [ Share the object ](#share_the_object)
- [ Create a simulated folder ](#create_folders)
- [ Delete the objects ](#delete_the_objects)
- [ Clean up ](#clean-up)
- [ What's next ](#whats-next)
- 










# Discover object storage with the Google Cloud Dedicated console 




Learn how to get started with Cloud Storage using
the Google Cloud Dedicated console.

Costs that you incur in Cloud Storage are based on the resources you
use. This quickstart typically uses less than $0.01 USD worth of
Cloud Storage resources.





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




Make sure that you have the following role or roles on the project:

Storage Admin



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
























## Create a bucket

*Buckets* are the basic containers that hold your data in Cloud Storage.

To create a bucket:

- In the Google Cloud Dedicated console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.berlin-build0.goog/storage/browser)

- 

Click add_box **Create**.

- 

In the **Get started** section, enter a globally unique name for your bucket.

See bucket naming requirements. 



- Bucket names can only contain lowercase letters, numeric characters, dashes (`-`),
and underscores (`_`). Spaces are not allowed.


- Bucket names must start and end with a number or letter.

- Bucket names must contain 3-63 characters. Names containing dots can contain up to
222 characters, but each dot-separated component can be no longer than 63 characters.

- Bucket names cannot be represented as an IP address in dotted-decimal notation
(for example, 192.168.5.4).

- Bucket names cannot begin with the "goog" prefix.

- Bucket names cannot contain "google" or close misspellings, such as "g00gle".



- 

In the **Choose where to store your data** section, for
**Location type**, select **Region**. Use the default value in this field.

- 

In the **Choose how to store your data** section, use the default values.

- 

In the **Choose how to control access to objects** section, clear the
**Enforce public access prevention on this bucket** checkbox. This lets you
share the object later.

- 

In the **Choose how to protect object data** section, use the default values.

- 

Click **Create**.

That's it — you've just created a Cloud Storage bucket!

## Upload an object into the bucket

- 

Save the following image to your device.



- 

On the **Bucket details** page, on the **Objects** tab, click **Upload**.
Then, select **Upload files**.

- 

On your device, locate and select the image that you previously saved.

After the upload completes, you should see the filename and information about
the file, such as its size and type.

## Download the object

To download the image from your bucket, click
download **Download**.

## Share the object

To allow public access to the bucket and create a publicly accessible URL for
the image:

- 

Click the **Permissions** tab.

- 

Click **Grant Access**.

- 

In the **New principals** field, enter `allUsers`.

- 

In the **Select a role** list, select **Cloud Storage**. Then, select
**Storage Object Viewer**.

- 

Click **Save**.

- 

In the **Are you sure you want to make this resource public?** dialog, click
**Allow public access**.

To verify, click the **Objects** tab to return to the list of objects. The
object's **Public access** column should read **Public to internet**.
The **Copy URL** button provides a shareable URL similar to the following:
`https://storage.apis-berlin-build0.goog/ YOUR_BUCKET_NAME /kitten.png`

To remove public access from the bucket and stop sharing the image publicly:

- 

Click the **Permissions** tab.

- 

In the **Principal** column, locate the **allUsers** principal, and then
select the checkbox associated with it.

- 

Click the **Remove Access** button, and then confirm when prompted.

On the **Objects** tab, you should see that the image no longer has a
**Copy URL** button.

## Create a simulated folder

- 

On the **Objects** tab, click **Create folder**.

- 

In the **Name** field, enter `quickstart-folder`.

- 

Click **Create**.

The simulated folder appears in the bucket, with a folder icon that
distinguishes it from objects.

- 

To upload a file to the simulated folder, do the following:

- 

Click **quickstart-folder**.

- 

Click **Upload**, and then select **Upload files**.

- 

On your device, locate and select the image that you previously saved.

After the upload completes, you should see the filename and information
about the file, such as its size and type.

## Delete the objects

- 

In the **Folder browser** panel, click the name of your bucket.

- 

Select the checkbox next to **quickstart-folder**.

- 

Click **Delete**, and then confirm when prompted.

The simulated folder and all objects in it are deleted.






## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






- In the Google Cloud Dedicated console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.berlin-build0.goog/storage/browser)

- 

Select the checkbox next to the bucket that you created.

- 

Click **Delete**, and then confirm when prompted.






## What's next



- [Work through the Cloud Storage quickstart using the Google Cloud CLI](/storage/docs/discover-object-storage-gcloud).

- Read the [Cloud Storage product overview](/storage/docs/introduction).

- Learn about [storage classes](/storage/docs/storage-classes).

- Get started with the [Cloud Storage client libraries](/storage/docs/reference/libraries).