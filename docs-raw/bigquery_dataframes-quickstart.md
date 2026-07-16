# Try BigQuery DataFrames

Source: https://berlin.devsitetest.how/bigquery/docs/dataframes-quickstart
Last updated: 2026-07-15

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/bigquery/docs/tpc-differences) for more details.














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

Data analytics

](https://berlin.devsitetest.how/docs/data)






- 








[

BigQuery

](https://berlin.devsitetest.how/bigquery/docs)






- 








[

Guides

](https://berlin.devsitetest.how/bigquery/docs/introduction)

















- On this page ** 
- [ Before you begin ](#before_you_begin)

- [ Required permissions ](#required_permissions)

- [ Create a notebook ](#create_a_notebook)
- [ Try BigQuery DataFrames ](#try-dataframes)
- [ Clean up ](#clean_up)
- [ What's next ](#whats_next)
- 









# Try Big Query Data Frames 



Use this quickstart to perform the following analysis and machine learning (ML)
tasks by using the
[BigQuery DataFrames API](https://dataframes.bigquery.dev/reference/index.html) in a
[BigQuery notebook](/bigquery/docs/notebooks-introduction):

- Create a DataFrame over the `bigquery-public-data.ml_datasets.penguins`
public dataset.

- Calculate the average body mass of a penguin.

- Create a
[linear regression model](https://dataframes.bigquery.dev/reference/api/bigframes.ml.linear_model.LinearRegression.html).

- Create a DataFrame over a subset of the penguin data to use as training data.

- Clean up the training data.

- Set the model parameters.

- [Fit](https://dataframes.bigquery.dev/reference/api/bigframes.ml.linear_model.LinearRegression.fit.html) the model.

- [Score](https://dataframes.bigquery.dev/reference/api/bigframes.ml.linear_model.LinearRegression.score.html) the model.

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

Verify that the BigQuery API is enabled.



[
Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=bigquery)



If you created a new project, the BigQuery API is automatically
enabled.

### Required permissions

To create and run notebooks, you need the following Identity and Access Management (IAM)
roles:

- [BigQuery User (`roles/bigquery.user`)](/bigquery/docs/access-control#bigquery.user)

- [Notebook Runtime User (`roles/aiplatform.notebookRuntimeUser`)](/vertex-ai/docs/general/access-control#aiplatform.notebookRuntimeUser)

- [Code Creator (`roles/dataform.codeCreator`)](/dataform/docs/access-control#dataform.codeCreator)

## Create a notebook

Follow the instructions in [Create a notebook from the BigQuery editor](/bigquery/docs/create-notebooks#create-notebook-console) to create a new notebook.

## Try BigQuery DataFrames

Try BigQuery DataFrames by following these steps:

- Create a new code cell in the notebook.

- 

Add the following code to the code cell:


```
import bigframes.pandas as bpd 

# Set BigQuery DataFrames options 
# Note: The project option is not required in all environments. 
# On BigQuery Studio, the project ID is automatically detected. 
bpd . options . bigquery . project = your_gcp_project_id 

# Use "partial" ordering mode to generate more efficient queries, but the 
# order of the rows in DataFrames may not be deterministic if you have not 
# explictly sorted it. Some operations that depend on the order, such as 
# head() will not function until you explictly order the DataFrame. Set the 
# ordering mode to "strict" (default) for more pandas compatibility. 
bpd . options . bigquery . ordering_mode = "partial" 

# Create a DataFrame from a BigQuery table 
query_or_table = "bigquery-public-data.ml_datasets.penguins" 
df = bpd . read_gbq ( query_or_table ) 

# Efficiently preview the results using the .peek() method. 
df . peek () 
```


- 

Modify the `bpd.options.bigquery.project = your_gcp_project_id` line to
specify your Google Cloud Dedicated project ID. For example,
`bpd.options.bigquery.project = "myProjectID"`.

- 

Run the code cell.

The code returns a `DataFrame` object with data about penguins.

- 

Create a new code cell in the notebook and add the following code:


```
# Use the DataFrame just as you would a pandas DataFrame, but calculations 
# happen in the BigQuery query engine instead of the local system. 
average_body_mass = df [ "body_mass_g" ] . mean () 
print ( f "average_body_mass: { average_body_mass } " ) 
```


- 

Run the code cell.

The code calculates the average body mass of the penguins and prints it to the
Google Cloud Dedicated console.

- 

Create a new code cell in the notebook and add the following code:


```
# Create the Linear Regression model 
from bigframes.ml.linear_model import LinearRegression 

# Filter down to the data we want to analyze 
adelie_data = df [ df . species == "Adelie Penguin (Pygoscelis adeliae)" ] 

# Drop the columns we don't care about 
adelie_data = adelie_data . drop ( columns = [ "species" ]) 

# Drop rows with nulls to get our training data 
training_data = adelie_data . dropna () 

# Pick feature columns and label column 
X = training_data [ 
[ 
"island" , 
"culmen_length_mm" , 
"culmen_depth_mm" , 
"flipper_length_mm" , 
"sex" , 
] 
] 
y = training_data [[ "body_mass_g" ]] 

model = LinearRegression ( fit_intercept = False ) 
model . fit ( X , y ) 
model . score ( X , y ) 
```


- 

Run the code cell.

The code returns the model's evaluation metrics.

## Clean up

The easiest way to eliminate billing is to delete the project that you
created for the tutorial.

To delete the project:






- 
In the Google Cloud Dedicated console, go to the **Manage resources** page.


[Go to Manage resources](https://console.cloud.berlin-build0.goog/iam-admin/projects)




- 
In the project list, select the project that you
want to delete, and then click **Delete**.


- 
In the dialog, type the project ID, and then click
**Shut down** to delete the project.




## What's next

- Continue learning about
[BigQuery DataFrames](/bigquery/docs/bigquery-dataframes-introduction).

- Learn how to
[visualize graphs using BigQuery DataFrames](/bigquery/docs/dataframes-visualizations).

- Learn how to
[use a BigQuery DataFrames notebook](https://github.com/googleapis/python-bigquery-dataframes/tree/main/notebooks/getting_started/getting_started_bq_dataframes.ipynb).