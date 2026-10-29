# Execute jobs on a schedule

Source: https://berlin.devsitetest.how/run/docs/execute/jobs-on-schedule
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/run/docs/tpc-differences) for more details.














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

Application hosting

](https://berlin.devsitetest.how/docs/application-hosting)






- 








[

Cloud Run

](https://berlin.devsitetest.how/run/docs)






- 








[

Guides

](https://berlin.devsitetest.how/run/docs/overview/what-is-cloud-run)












# Execute jobs on a schedule 















This page describes how to execute Cloud Run jobs on a schedule using
crontab.

## Required roles

To get the permissions that you need for the operations described on this page,
ask your administrator to grant you one of the following IAM
roles on your Cloud Run job:

- To execute jobs using the Google Cloud CLI: [Cloud Run Invoker](/iam/docs/roles-permissions/run#run.invoker) (`roles/run.invoker`) on the Cloud Run job.

- To execute jobs using the Google Cloud Dedicated console, to override job configurations, or to cancel job executions: [Cloud Run Developer](/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job.

For a list of IAM roles and permissions that are associated with
Cloud Run, see
[Cloud Run IAM roles](/run/docs/reference/iam/roles)
and [Cloud Run IAM permissions](/run/docs/reference/iam/permissions).
If your Cloud Run job interfaces with
Google Cloud Dedicated APIs, such as Cloud Client Libraries, see the
[service identity configuration guide](/run/docs/configuring/jobs/service-identity).
For more information about granting roles, see
[deployment permissions](/run/docs/reference/iam/roles#additional-configuration)
and [manage access](/iam/docs/granting-changing-revoking-access).

## Grant the service account access to your project

If you haven't created a service account for your Cloud Run job,
create a service account. For example:


```
gcloud iam service-accounts create SERVICE_ACCOUNT_NAME 
```


Replace SERVICE_ACCOUNT_NAME with the name of your service account,
for example, `job-scheduler`.

To get the permissions that your service account needs to execute jobs, ask your
administrator to grant your service account the
[Jobs Executor](/iam/docs/roles-permissions/run#run.jobsExecutor)
(`roles/run.jobsExecutor`) role on your project. For example:


```
gcloud projects add-iam-policy-binding PROJECT_ID \ 
--member = serviceAccount:job-scheduler@ PROJECT_ID .eu0.iam.gserviceaccount.com \ 
--role roles/run.jobsExecutor
```


Replace PROJECT_ID with the name of your project ID.

## Before you begin

- [Create a Cloud Run job](/run/docs/create-jobs) if you have not created
one yet.

- 

Enable the Cloud Scheduler API for your project:


```
gcloud services enable cloudscheduler.googleapis.com
```


## Configure a Cloud Run job to execute on a schedule

To execute a Cloud Run job on a schedule, follow these steps:

- 

Create a new directory named `cloud-run-jobs-sched` and change directory into
it:


```
mkdir cloud-run-jobs-sched
cd cloud-run-jobs-sched
```


- 

Create a `Dockerfile` file and paste the following lines into it:


```
FROM gcr . io / google . com / cloudsdktool / google - cloud - cli : 536.0.1 

RUN apt - get update - y && \
apt - get install - y python3 - dev python3 - pip python3 - venv && \
apt - get install - y cron 

ENV APP_HOME / app 
WORKDIR $ APP_HOME 
COPY . ./ 

ENV VIRTUAL_ENV =/ opt / venv 
RUN python3 - m venv $ VIRTUAL_ENV 
ENV PATH = "$VIRTUAL_ENV/bin:$PATH" 

RUN pip install -- no - cache - dir - r requirements . txt 

# Set up the cron schedule. 
RUN crontab / app / cron 

CMD / app / entrypoint . sh 
```


- 

Create an `entrypoint.sh` file and paste the following lines into it:


```
gcloud config set project $ PROJECT 
gcloud config set run / region $ REGION 

cron 

gunicorn -- bind : $ PORT -- workers 1 -- threads 8 -- timeout 0 main : app 
```


- 

Create a `main.py` file and paste the following Python code into it:


```
import os 

from flask import Flask 

app = Flask ( __name__ ) 

@app . route ( "/" ) 
def hello_world (): 
return "Hello World!" 

if __name__ == "__main__" : 
app . run ( debug = True , host = "0.0.0.0" , port = int ( os . environ . get ( "PORT" , 8080 ))) 
```


- 

Create a `requirements.txt` file and paste the following dependencies into
it:


```
Flask == 3.0.3 
gunicorn == 23.0.0 
Werkzeug == 3.0.3 
```


- 

Create a `cron` file in your directory and add a cron schedule to execute the
job. For example:


```
0 2 * * * gcloud run jobs execute -- async test - job > / proc / 1 / fd / 1 2 >& 1 
```


This command executes a job called `test-job` every day at 2am. Any errors
starting the job execution will be shown in the service's logs.

To create multiple schedules for multiple jobs, update the `cron` file with
any jobs that you'd like to execute, along with their associated schedule.
For example:


```
$ { cron_schedule } gcloud run jobs execute -- async $ { job_1 } > / proc / 1 / fd / 1 2 >& 1 
$ { cron_schedule } gcloud run jobs execute -- async $ { job_2 } > / proc / 1 / fd / 1 2 >& 1 
... 
```


- 

Deploy the job scheduler service:


```
gcloud run deploy JOB \ 
--source . \ 
--region REGION \ 
--set-env-vars PROJECT = PROJECT_ID ,REGION = REGION \ 
--service-account SERVICE_ACCOUNT \ 
--no-allow-unauthenticated \ 
--min-instances = 1 \ 
--no-cpu-throttling
```


Replace the following:

- ` JOB `: the name of your Cloud Run job.

- ` REGION `: the region for your Cloud Run
job, for example, `europe-west1`.

- ` PROJECT_ID `: your project ID.

- ` SERVICE_ACCOUNT `: your service account.

## What's next

After you use this feature, you can do the following:

- [View job logs](/run/docs/logging)

- [Monitor job performance](/run/docs/monitoring)

- [Create a job](/run/docs/create-jobs)

- [Execute a job](/run/docs/execute/jobs)

- [Manage jobs](/run/docs/managing/jobs)

- 

[Manage job executions](/run/docs/managing/job-executions)

- 

[Set memory limits](/run/docs/configuring/jobs/memory-limits)

- 

[Set environment variables](/run/docs/configuring/jobs/environment-variables)