# Create an ML model in BigQuery ML by using SQL

Source: https://berlin.devsitetest.how/bigquery/docs/create-machine-learning-model
Last updated: 2026-07-07

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
- [ Objectives ](#objectives)
- [ Costs ](#costs)
- [ Required roles ](#required_roles)
- [ Before you begin ](#before-you-begin)
- [ Create a dataset ](#create_a_dataset)
- [ Create a logistic regression model ](#create_a_logistic_regression_model)
- [ View the model's loss statistics ](#view_the_models_loss_statistics)
- [ Evaluate the model ](#evaluate_the_model)
- [ Use the model to predict outcomes ](#use_the_model_to_predict_outcomes)
- [ Predict purchases per user ](#predict_purchases_per_user)
- [ Clean up ](#clean-up)

- [ Delete the dataset ](#delete_the_dataset)
- [ Delete the project ](#delete_the_project)

- [ What's next ](#whats-next)
- 










# Create a machine learning model in Big Query ML by using SQL 




This tutorial shows you how to create a logistic regression model by using
BigQuery ML SQL queries.

BigQuery ML lets you create and train machine learning models in
BigQuery by using SQL queries. This helps make machine learning more
approachable by letting you use familiar tools like the BigQuery
SQL editor, and also increases development speed by removing the need to move
data into a separate machine learning environment.

In this tutorial, you use the sample
[Google Analytics sample dataset for BigQuery](https://support.google.com/analytics/answer/7586738?ref_topic=3416089)
to create a model that predicts whether a website visitor will make a
transaction. For information on the schema of the Analytics dataset, see
[BigQuery export schema](https://support.google.com/analytics/answer/3437719)
in the Analytics Help Center.

To learn how to create models by using the Google Cloud Dedicated console user interface, see
[work with models by using a UI](/bigquery/docs/create-machine-learning-model-console).

## Objectives

This tutorial shows you how to perform the following tasks:

- Using the
[`CREATE MODEL` statement](/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create)
to create a binary logistic regression model.

- Using the
[`ML.EVALUATE` function](/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate)
to evaluate the model.

- Using the
[`ML.PREDICT` function](/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)
to make predictions by using the model.

## Costs

This tutorial uses billable components of Google Cloud Dedicated in Germany,
including the following:


- BigQuery

- BigQuery ML

For more information on BigQuery costs, see the
[BigQuery pricing](https://berlin.devsitetest.how/bigquery/pricing) page.

For more information on BigQuery ML costs, see
[BigQuery ML pricing](https://berlin.devsitetest.how/bigquery/pricing#bigquery-ml-pricing).

## Required roles

- 

To create a model and run inference, you must be granted the following roles:

- BigQuery Data Editor (`roles/bigquery.dataEditor`)

- BigQuery User (`roles/bigquery.user`)





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

BigQuery Data Editor, BigQuery Job User, Service Usage Admin



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




















- BigQuery is automatically enabled in new projects.
To activate BigQuery in a pre-existing project, go to








Enable the BigQuery API.






**Roles required to enable APIs**


To enable APIs, you need the Service Usage Admin IAM
role (`roles/serviceusage.serviceUsageAdmin`), which
contains the `serviceusage.services.enable` permission. [Learn how to grant
roles](/iam/docs/granting-changing-revoking-access).



[Enable the API](https://console.cloud.berlin-build0.goog/apis/enableflow?apiid=bigquery)






## Create a dataset

Create a BigQuery dataset to store your ML model.


[Console](#console) [bq](#bq) [ API ](#api) [ BigQuery DataFrames ](#bigquery-dataframes) 
**More 




- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to the BigQuery page](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the **Explorer** pane, click your project name.

- 

Click more_vert **View actions > Create dataset**

- 

On the **Create dataset** page, do the following:

- 

For **Dataset ID**, enter `bqml_tutorial`.

- 

For **Location type**, select **Multi-region**, and then select
**US**.

- 

Leave the remaining default settings as they are, and click
**Create dataset**.




To create a new dataset, use the
[`bq mk --dataset` command](/bigquery/docs/reference/bq-cli-reference#mk-dataset).

- 

Create a dataset named `bqml_tutorial` with the data location set to `US`.


```
bq mk --dataset \
--location=US \
--description "BigQuery ML tutorial dataset." \
bqml_tutorial
```


- 

Confirm that the dataset was created:


```
bq ls
```





Call the [`datasets.insert`](/bigquery/docs/reference/rest/v2/datasets/insert)
method with a defined [dataset resource](/bigquery/docs/reference/rest/v2/datasets).


```
{ 
"datasetReference" : { 
"datasetId" : "bqml_tutorial" 
} 
} 
```







Before trying this sample, follow the BigQuery DataFrames
setup instructions in the [BigQuery quickstart
using BigQuery DataFrames](/bigquery/docs/dataframes-quickstart).
For more information, see the
[BigQuery DataFrames reference documentation](/python/docs/reference/bigframes/latest).



To authenticate to BigQuery, set up Application Default Credentials.
For more information, see [Set
up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).
















































```
import google.cloud.bigquery 

bqclient = google . cloud . [ bigquery ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest) . [ Client ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html) () 
bqclient . [ create_dataset ](https://berlin.devsitetest.how/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_dataset) ( "bqml_tutorial" , exists_ok = True ) 
```





















## Create a logistic regression model

Create a logistic regression model using the Analytics sample
dataset for BigQuery.


[ SQL ](#sql) [ BigQuery DataFrames ](#bigquery-dataframes) 
More 




- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the query editor, run the following statement:


```
CREATE OR REPLACE MODEL `bqml_tutorial.sample_model` 
OPTIONS ( model_type = 'logistic_reg' ) AS 
SELECT 
IF ( totals . transactions IS NULL , 0 , 1 ) AS label , 
IFNULL ( device . operatingSystem , "" ) AS os , 
device . isMobile AS is_mobile , 
IFNULL ( geoNetwork . country , "" ) AS country , 
IFNULL ( totals . pageviews , 0 ) AS pageviews 
FROM 
`bigquery-public-data.google_analytics_sample.ga_sessions_*` 
WHERE 
_TABLE_SUFFIX BETWEEN '20160801' AND '20170630' 
```


The query takes several minutes to complete. After the first iteration is
complete, your model (`sample_model`) appears in the navigation panel.
Because the query uses a `CREATE MODEL` statement to create a model, you don't
see query results.

**Query details**

The `CREATE MODEL` statement creates the model and then trains the model
using the data retrieved by your query's `SELECT` statement.

The `OPTIONS(model_type='logistic_reg')` clause creates a [logistic
regression](https://en.wikipedia.org/wiki/Logistic_regression) model. A
logistic regression model splits input data into two classes, and then
estimates the probability that the data is in one of the classes. What you are
trying to detect, such as whether an email is spam, is represented by 1 and
other values are represented by 0. The likelihood of a given value belonging
to the class you are trying to detect is indicated by a value between 0 and 1.
For example, if an email receives a probability estimate of 0.9, then there is
a 90% probability that the email is spam.

This query's `SELECT` statement retrieves the following columns that are used
by the model to predict the probability that a customer will complete a
transaction:

- `totals.transactions`: the total number of ecommerce transactions
within the session. If the number of transactions is `NULL`, the value in the
`label` column is set to `0`. Otherwise, it is set to `1`. These values
represent the possible outcomes. Creating an alias named `label` is an
alternative to setting the `input_label_cols=` option in the `CREATE MODEL`
statement.

- `device.operatingSystem`: the operating system of the visitor's device.

- `device.isMobile` — Indicates whether the visitor's device is a mobile
device.

- `geoNetwork.country`: the country from which the sessions originated,
based on the IP address.

- `totals.pageviews`: the total number of page views within the session.

The `FROM` clause — causes the query to train the model by using the
`bigquery-public-data.google_analytics_sample.ga_sessions` sample tables.
These tables are sharded by date, so you aggregate them by using a wildcard in
the table name: `google_analytics_sample.ga_sessions_*`.

The `WHERE` clause — `_TABLE_SUFFIX BETWEEN '20160801' AND '20170630'`
— limits the number of tables scanned by the query. The date range
scanned is August 1, 2016 to June 30, 2017.



Before trying this sample, follow the BigQuery DataFrames
setup instructions in the [BigQuery quickstart
using BigQuery DataFrames](/bigquery/docs/dataframes-quickstart).
For more information, see the
[BigQuery DataFrames reference documentation](/python/docs/reference/bigframes/latest).



To authenticate to BigQuery, set up Application Default Credentials.
For more information, see [Set
up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).
















































```
from bigframes.ml.linear_model import LogisticRegression 
import bigframes.pandas as bpd 

# Start by selecting the data you'll use for training. `read_gbq` accepts 
# either a SQL query or a table ID. Since this example selects from multiple 
# tables via a wildcard, use SQL to define this data. Watch issue 
# https://github.com/googleapis/python-bigquery-dataframes/issues/169 
# for updates to `read_gbq` to support wildcard tables. 

df = bpd . read_gbq_table ( 
"bigquery-public-data.google_analytics_sample.ga_sessions_*" , 
filters = [ 
( "_table_suffix" , ">=" , "20160801" ), 
( "_table_suffix" , " , "20170630" ), 
], 
) 

# Extract the total number of transactions within 
# the Google Analytics session. 
# 
# Because the totals column is a STRUCT data type, call 
# Series.struct.field("transactions") to extract the transactions field. 
# See the reference documentation below: 
# https://cloud.google.com/python/docs/reference/bigframes/latest/bigframes.operations.structs.StructAccessor#bigframes_operations_structs_StructAccessor_field 
transactions = df [ "totals" ] . struct . field ( "transactions" ) 

# The "label" values represent the outcome of the model's 
# prediction. In this case, the model predicts if there are any 
# ecommerce transactions within the Google Analytics session. 
# If the number of transactions is NULL, the value in the label 
# column is set to 0. Otherwise, it is set to 1. 
label = transactions . notnull () . map ({ True : 1 , False : 0 }) . rename ( "label" ) 

# Extract the operating system of the visitor's device. 
operating_system = df [ "device" ] . struct . field ( "operatingSystem" ) 
operating_system = operating_system . fillna ( "" ) 

# Extract whether the visitor's device is a mobile device. 
is_mobile = df [ "device" ] . struct . field ( "isMobile" ) 

# Extract the country from which the sessions originated, based on the IP address. 
country = df [ "geoNetwork" ] . struct . field ( "country" ) . fillna ( "" ) 

# Extract the total number of page views within the session. 
pageviews = df [ "totals" ] . struct . field ( "pageviews" ) . fillna ( 0 ) 

# Combine all the feature columns into a single DataFrame 
# to use as training data. 
features = bpd . DataFrame ( 
{ 
"os" : operating_system , 
"is_mobile" : is_mobile , 
"country" : country , 
"pageviews" : pageviews , 
} 
) 

# Logistic Regression model splits data into two classes, giving the 
# a confidence score that the data is in one of the classes. 
model = LogisticRegression () 
model . fit ( features , label ) 

# The model.fit() call above created a temporary model. 
# Use the to_gbq() method to write to a permanent location. 
model . to_gbq ( 
your_model_id , # For example: "bqml_tutorial.sample_model", 
replace = True , 
) 
```




















## View the model's loss statistics

Machine learning is about creating a model that can use data to make a
prediction. The model is essentially a function that takes inputs and applies
calculations to the inputs to produce an output — a prediction.

Machine learning algorithms work by taking several examples where the
prediction is already known (such as the historical data of user purchases) and
iteratively adjusting various weights in the model so that the model's
predictions match the true values. It does this by minimizing how wrong the
model is using a metric called loss.

The expectation is that for each iteration, the loss should be decreasing,
ideally to zero. A loss of zero means the model is 100% accurate.

When training the model, BigQuery ML automatically splits the
input data into
[training and evaluation sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets),
in order to avoid [overfitting](https://en.wikipedia.org/wiki/Overfitting)
the model. This is necessary so that the training algorithm doesn't fit itself
so closely to the training data that it can't generalize to new examples.

Use the Google Cloud Dedicated console to see how the model's loss changes over the
model's training iterations:

- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the left pane, click explore **Explorer**:



If you don't see the left pane, click last_page **Expand left pane** to open the pane.

- 

In the **Explorer** pane, expand your project, click **Datasets**,
and then click the `bqml_tutorial` dataset.

- 

Click the **Models** tab, and then click the `sample_model` model.

- 

Click the **Training** tab and look at the **Loss** graph. The **Loss**
graph shows the change in the loss metric over the iterations on the
training dataset. If you hold your cursor over the graph, you can see that
there are lines for **Training loss** and **Evaluation loss**. Since you
performed a logistic regression, the training loss value is calculated as
[log loss](https://en.wikipedia.org/wiki/Cross-entropy#Cross-entropy_loss_function_and_logistic_regression), using
the training data. The evaluation loss is the log loss calculated on the
evaluation data. Both loss types represent average loss values, averaged
over all examples in the respective datasets for each iteration.

You can also see the results of the model training by using the
[`ML.TRAINING_INFO` function](/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train).

## Evaluate the model

Evaluate the performance of the model by using the `ML.EVALUATE` function. The
`ML.EVALUATE` function evaluates the predicted values generated by the model
against the actual data. To calculate logistic regression specific
metrics, you can use the
[`ML.ROC_CURVE` SQL function](/bigquery/docs/reference/standard-sql/bigqueryml-syntax-roc)
or the
[`bigframes.ml.metrics.roc_curve` BigQuery DataFrames function](https://dataframes.bigquery.dev/reference/api/bigframes.ml.metrics.roc_curve.html#bigframes.ml.metrics.roc_curve).

In this tutorial, you are using a binary classification model that
detects transactions. The values in the `label` column are the two classes
generated by the model: `0` (no transactions) and `1` (transaction made).


[ SQL ](#sql) [ BigQuery DataFrames ](#bigquery-dataframes) 
More 




- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the query editor, run the following statement:


```
SELECT 
* 
FROM 
ML . EVALUATE ( MODEL `bqml_tutorial.sample_model` , ( 
SELECT 
IF ( totals . transactions IS NULL , 0 , 1 ) AS label , 
IFNULL ( device . operatingSystem , "" ) AS os , 
device . isMobile AS is_mobile , 
IFNULL ( geoNetwork . country , "" ) AS country , 
IFNULL ( totals . pageviews , 0 ) AS pageviews 
FROM 
`bigquery-public-data.google_analytics_sample.ga_sessions_*` 
WHERE 
_TABLE_SUFFIX BETWEEN '20170701' AND '20170801' )) 
```


The results should look like the following:


```
+--------------------+---------------------+---------------------+---------------------+---------------------+--------------------+
| precision | recall | accuracy | f1_score | log_loss | roc_auc |
+--------------------+---------------------+---------------------+---------------------+---------------------+--------------------+
| 0.468503937007874 | 0.11080074487895716 | 0.98534315834767638 | 0.17921686746987953 | 0.04624221101176898 | 0.98174125874125873 |
+--------------------+---------------------+---------------------+---------------------+---------------------+--------------------+
```


Because you performed a logistic regression, the results include the following
columns:

- 

[`precision`](https://developers.google.com/machine-learning/glossary/#precision):
a metric for classification models. Precision identifies the frequency
with which a model was correct when predicting the positive class.

- 

[`recall`](https://developers.google.com/machine-learning/glossary/#recall):
a metric for classification models that answers the following
question: Out of all the possible positive labels, how many did the model
correctly identify?

- 

[`accuracy`](https://developers.google.com/machine-learning/glossary/#accuracy):
accuracy is the fraction of predictions that a classification model
got right.

- 

[`f1_score`](https://en.wikipedia.org/wiki/F1_score):
a measure of the accuracy of the model. The f1 score is the harmonic average of
the precision and recall. An f1 score's best value is 1. The worst value is 0.

- 

[`log_loss`](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression):
the loss function used in a logistic regression. This is the measure
of how far the model's predictions are from the correct labels.

- 

[`roc_auc`](https://developers.google.com/machine-learning/glossary/#AUC):
the area under the [ROC](https://developers.google.com/machine-learning/glossary/#ROC)
curve. This is the probability that a classifier is more confident that a
randomly chosen positive example is actually positive than that a randomly
chosen negative example is positive. For more information, see
[Classification](https://developers.google.com/machine-learning/crash-course/classification/video-lecture)
in the Machine Learning Crash Course.

**Query details**

The initial `SELECT` statement retrieves the columns from your model.

The `FROM` clause uses the `ML.EVALUATE` function against your model.

The nested `SELECT` statement and `FROM` clause are the same as those
in the `CREATE MODEL` query.

The `WHERE` clause — `_TABLE_SUFFIX BETWEEN '20170701' AND '20170801'`
— limits the number of tables scanned by the query. The date range
scanned is July 1, 2017 to August 1, 2017. This is the data you're using to
evaluate the predictive performance of the model. It was collected in the month
immediately following the time period spanned by the training data.



Before trying this sample, follow the BigQuery DataFrames
setup instructions in the [BigQuery quickstart
using BigQuery DataFrames](/bigquery/docs/dataframes-quickstart).
For more information, see the
[BigQuery DataFrames reference documentation](/python/docs/reference/bigframes/latest).



To authenticate to BigQuery, set up Application Default Credentials.
For more information, see [Set
up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).
















































```
import bigframes.pandas as bpd 

# Select model you'll use for evaluating. `read_gbq_model` loads model data from a 
# BigQuery, but you could also use the `model` object from the previous steps. 
model = bpd . read_gbq_model ( 
your_model_id , # For example: "bqml_tutorial.sample_model", 
) 

# The filters parameter limits the number of tables scanned by the query. 
# The date range scanned is July 1, 2017 to August 1, 2017. This is the 
# data you're using to evaluate the predictive performance of the model. 
# It was collected in the month immediately following the time period 
# spanned by the training data. 
df = bpd . read_gbq_table ( 
"bigquery-public-data.google_analytics_sample.ga_sessions_*" , 
filters = [ 
( "_table_suffix" , ">=" , "20170701" ), 
( "_table_suffix" , " , "20170801" ), 
], 
) 

transactions = df [ "totals" ] . struct . field ( "transactions" ) 
label = transactions . notnull () . map ({ True : 1 , False : 0 }) . rename ( "label" ) 
operating_system = df [ "device" ] . struct . field ( "operatingSystem" ) 
operating_system = operating_system . fillna ( "" ) 
is_mobile = df [ "device" ] . struct . field ( "isMobile" ) 
country = df [ "geoNetwork" ] . struct . field ( "country" ) . fillna ( "" ) 
pageviews = df [ "totals" ] . struct . field ( "pageviews" ) . fillna ( 0 ) 
features = bpd . DataFrame ( 
{ 
"os" : operating_system , 
"is_mobile" : is_mobile , 
"country" : country , 
"pageviews" : pageviews , 
} 
) 

# Some models include a convenient .score(X, y) method for evaluation with a preset accuracy metric: 

# Because you performed a logistic regression, the results include the following columns: 

# - precision — A metric for classification models. Precision identifies the frequency with 
# which a model was correct when predicting the positive class. 

# - recall — A metric for classification models that answers the following question: 
# Out of all the possible positive labels, how many did the model correctly identify? 

# - accuracy — Accuracy is the fraction of predictions that a classification model got right. 

# - f1_score — A measure of the accuracy of the model. The f1 score is the harmonic average of 
# the precision and recall. An f1 score's best value is 1. The worst value is 0. 

# - log_loss — The loss function used in a logistic regression. This is the measure of how far the 
# model's predictions are from the correct labels. 

# - roc_auc — The area under the ROC curve. This is the probability that a classifier is more confident that 
# a randomly chosen positive example 
# is actually positive than that a randomly chosen negative example is positive. For more information, 
# see ['Classification']('https://developers.google.com/machine-learning/crash-course/classification/video-lecture') 
# in the Machine Learning Crash Course. 

model . score ( features , label ) 
# precision recall accuracy f1_score log_loss roc_auc 
# 0 0.412621 0.079143 0.985074 0.132812 0.049764 0.974285 
# [1 rows x 6 columns] 
```




















## Use the model to predict outcomes

Use the model to predict the number of transactions made by website visitors
from each country.


[ SQL ](#sql) [ BigQuery DataFrames ](#bigquery-dataframes) 
More 




- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the query editor, run the following statement:


```
SELECT 
country , 
SUM ( predicted_label ) as total_predicted_purchases 
FROM 
ML . PREDICT ( MODEL `bqml_tutorial.sample_model` , ( 
SELECT 
IFNULL ( device . operatingSystem , "" ) AS os , 
device . isMobile AS is_mobile , 
IFNULL ( totals . pageviews , 0 ) AS pageviews , 
IFNULL ( geoNetwork . country , "" ) AS country 
FROM 
`bigquery-public-data.google_analytics_sample.ga_sessions_*` 
WHERE 
_TABLE_SUFFIX BETWEEN '20170701' AND '20170801' )) 
GROUP BY country 
ORDER BY total_predicted_purchases DESC 
LIMIT 10 
```


The results should look like the following:


```
+----------------+---------------------------+
| country | total_predicted_purchases |
+----------------+---------------------------+
| United States | 220 |
| Taiwan | 8 |
| Canada | 7 |
| India | 2 |
| Turkey | 2 |
| Japan | 2 |
| Italy | 1 |
| Brazil | 1 |
| Singapore | 1 |
| Australia | 1 |
+----------------+---------------------------+
```


**Query details**

The initial `SELECT` statement retrieves the `country` column and sums the
`predicted_label` column. The `predicted_label` column is generated by the
`ML.PREDICT` function. When you use the `ML.PREDICT` function, the output
column name for the model is `predicted_ `. For linear
regression models, `predicted_label` is the estimated value of `label`.
For logistic regression models, `predicted_label` is the label that best
describes the given input data value, either `0` or `1`.

The `ML.PREDICT` function is used to predict results using your model.

The nested `SELECT` statement and `FROM` clause are the same as those
in the `CREATE MODEL` query.

The `WHERE` clause — `_TABLE_SUFFIX BETWEEN '20170701' AND '20170801'`
— limits the number of tables scanned by the query. The date range
scanned is July 1, 2017 to August 1, 2017. This is the data for which you're
making predictions. It was collected in the month immediately following the time
period spanned by the training data.

The `GROUP BY` and `ORDER BY` clauses group the results by country and order
them by the sum of the predicted purchases in descending order.

The `LIMIT` clause is used here to display only the top 10 results.



Before trying this sample, follow the BigQuery DataFrames
setup instructions in the [BigQuery quickstart
using BigQuery DataFrames](/bigquery/docs/dataframes-quickstart).
For more information, see the
[BigQuery DataFrames reference documentation](/python/docs/reference/bigframes/latest).



To authenticate to BigQuery, set up Application Default Credentials.
For more information, see [Set
up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).
















































```
import bigframes.pandas as bpd 

# Select model you'll use for predicting. 
# `read_gbq_model` loads model data from 
# BigQuery, but you could also use the `model` 
# object from the previous steps. 
model = bpd . read_gbq_model ( 
your_model_id , # For example: "bqml_tutorial.sample_model", 
) 

# The filters parameter limits the number of tables scanned by the query. 
# The date range scanned is July 1, 2017 to August 1, 2017. This is the 
# data you're using to make the prediction. 
# It was collected in the month immediately following the time period 
# spanned by the training data. 
df = bpd . read_gbq_table ( 
"bigquery-public-data.google_analytics_sample.ga_sessions_*" , 
filters = [ 
( "_table_suffix" , ">=" , "20170701" ), 
( "_table_suffix" , " , "20170801" ), 
], 
) 

operating_system = df [ "device" ] . struct . field ( "operatingSystem" ) 
operating_system = operating_system . fillna ( "" ) 
is_mobile = df [ "device" ] . struct . field ( "isMobile" ) 
country = df [ "geoNetwork" ] . struct . field ( "country" ) . fillna ( "" ) 
pageviews = df [ "totals" ] . struct . field ( "pageviews" ) . fillna ( 0 ) 
features = bpd . DataFrame ( 
{ 
"os" : operating_system , 
"is_mobile" : is_mobile , 
"country" : country , 
"pageviews" : pageviews , 
} 
) 
# Use Logistic Regression predict method to predict results 
# using your model. 
# Find more information here in 
# [BigFrames](https://cloud.google.com/python/docs/reference/bigframes/latest/bigframes.ml.linear_model.LogisticRegression#bigframes_ml_linear_model_LogisticRegression_predict) 

predictions = model . predict ( features ) 

# Call groupby method to group predicted_label by country. 
# Call sum method to get the total_predicted_label by country. 
total_predicted_purchases = predictions . groupby ([ "country" ])[ 
[ "predicted_label" ] 
] . sum () 

# Call the sort_values method with the parameter 
# ascending = False to get the highest values. 
# Call head method to limit to the 10 highest values. 
total_predicted_purchases . sort_values ( ascending = False ) . head ( 10 ) 

# country 
# United States 220 
# Taiwan 8 
# Canada 7 
# India 2 
# Japan 2 
# Turkey 2 
# Australia 1 
# Brazil 1 
# Germany 1 
# Guyana 1 
# Name: predicted_label, dtype: Int64 
```




















## Predict purchases per user

Predict the number of transactions each website visitor will make.


[ SQL ](#sql) [ BigQuery DataFrames ](#bigquery-dataframes) 
More 




This query is identical to the query in the previous section except for the
`GROUP BY` clause. Here the `GROUP BY` clause — `GROUP BY fullVisitorId`
— is used to group the results by visitor ID.

- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the query editor, run the following statement:


```
SELECT 
fullVisitorId , 
SUM ( predicted_label ) as total_predicted_purchases 
FROM 
ML . PREDICT ( MODEL `bqml_tutorial.sample_model` , ( 
SELECT 
IFNULL ( device . operatingSystem , "" ) AS os , 
device . isMobile AS is_mobile , 
IFNULL ( totals . pageviews , 0 ) AS pageviews , 
IFNULL ( geoNetwork . country , "" ) AS country , 
fullVisitorId 
FROM 
`bigquery-public-data.google_analytics_sample.ga_sessions_*` 
WHERE 
_TABLE_SUFFIX BETWEEN '20170701' AND '20170801' )) 
GROUP BY fullVisitorId 
ORDER BY total_predicted_purchases DESC 
LIMIT 10 
```


The results should look like the following:


```
+---------------------+---------------------------+
| fullVisitorId | total_predicted_purchases |
+---------------------+---------------------------+
| 9417857471295131045 | 4 |
| 112288330928895942 | 2 |
| 2158257269735455737 | 2 |
| 489038402765684003 | 2 |
| 057693500927581077 | 2 |
| 2969418676126258798 | 2 |
| 5073919761051630191 | 2 |
| 7420300501523012460 | 2 |
| 0456807427403774085 | 2 |
| 2105122376016897629 | 2 |
+---------------------+---------------------------+
```





Before trying this sample, follow the BigQuery DataFrames
setup instructions in the [BigQuery quickstart
using BigQuery DataFrames](/bigquery/docs/dataframes-quickstart).
For more information, see the
[BigQuery DataFrames reference documentation](/python/docs/reference/bigframes/latest).



To authenticate to BigQuery, set up Application Default Credentials.
For more information, see [Set
up ADC for a local development environment](/docs/authentication/set-up-adc-local-dev-environment).
















































```
import bigframes.pandas as bpd 

# Select model you'll use for predicting. 
# `read_gbq_model` loads model data from 
# BigQuery, but you could also use the `model` 
# object from the previous steps. 
model = bpd . read_gbq_model ( 
your_model_id , # For example: "bqml_tutorial.sample_model", 
) 

# The filters parameter limits the number of tables scanned by the query. 
# The date range scanned is July 1, 2017 to August 1, 2017. This is the 
# data you're using to make the prediction. 
# It was collected in the month immediately following the time period 
# spanned by the training data. 
df = bpd . read_gbq_table ( 
"bigquery-public-data.google_analytics_sample.ga_sessions_*" , 
filters = [ 
( "_table_suffix" , ">=" , "20170701" ), 
( "_table_suffix" , " , "20170801" ), 
], 
) 

operating_system = df [ "device" ] . struct . field ( "operatingSystem" ) 
operating_system = operating_system . fillna ( "" ) 
is_mobile = df [ "device" ] . struct . field ( "isMobile" ) 
country = df [ "geoNetwork" ] . struct . field ( "country" ) . fillna ( "" ) 
pageviews = df [ "totals" ] . struct . field ( "pageviews" ) . fillna ( 0 ) 
full_visitor_id = df [ "fullVisitorId" ] 

features = bpd . DataFrame ( 
{ 
"os" : operating_system , 
"is_mobile" : is_mobile , 
"country" : country , 
"pageviews" : pageviews , 
"fullVisitorId" : full_visitor_id , 
} 
) 

predictions = model . predict ( features ) 

# Call groupby method to group predicted_label by visitor. 
# Call sum method to get the total_predicted_label by visitor. 
total_predicted_purchases = predictions . groupby ([ "fullVisitorId" ])[ 
[ "predicted_label" ] 
] . sum () 

# Call the sort_values method with the parameter 
# ascending = False to get the highest values. 
# Call head method to limit to the 10 highest values. 
total_predicted_purchases . sort_values ( ascending = False ) . head ( 10 ) 

# fullVisitorId 
# 9417857471295131045 4 
# 0376394056092189113 2 
# 0456807427403774085 2 
# 057693500927581077 2 
# 112288330928895942 2 
# 1280993661204347450 2 
# 2105122376016897629 2 
# 2158257269735455737 2 
# 2969418676126258798 2 
# 489038402765684003 2 
# Name: predicted_label, dtype: Int64 
```

























## Clean up





To avoid incurring charges to your Google Cloud Dedicated account for
the resources used on this page, follow these steps.






You can delete the project you created, or keep the project and delete the
dataset.

### Delete the dataset

Deleting your project removes all datasets and all tables in the project. If you
prefer to reuse the project, you can delete the dataset you created in this
tutorial:

- 

In the Google Cloud Dedicated console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.berlin-build0.goog/bigquery) 

- 

In the left pane, click explore **Explorer**:



- 

In the **Explorer** pane, expand your project, click **Datasets**,
and then click the `bqml_tutorial` dataset that you created.

- 

Click **Delete**.

- 

In the **Delete dataset** dialog, confirm the delete command by typing
`delete`.

- 

Click **Delete**.

### Delete the project

To delete the project:





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



- To learn more about machine learning, see the [Machine learning crash course](https://developers.google.com/machine-learning/crash-course/).

- For an overview of BigQuery ML, see [Introduction to BigQuery ML](/bigquery/docs/bqml-introduction).

- To learn more about the Google Cloud Dedicated console, see
[Using the Google Cloud Dedicated console](/bigquery/bigquery-web-ui).