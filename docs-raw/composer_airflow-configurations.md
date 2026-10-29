# Blocked and limited Airflow configuration options

Source: https://berlin.devsitetest.how/composer/docs/airflow-configurations
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Google Cloud Dedicated. See [Differences from Google Cloud](/composer/docs/tpc-differences) for more details.














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

Managed Service for Apache Airflow

](https://berlin.devsitetest.how/composer/docs)






- 








[

Reference

](https://berlin.devsitetest.how/composer/docs/apis)












# Blocked and limited Airflow configuration options 


















This page lists Airflow
[configuration options](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) that are blocked or limited in
Managed Airflow.

## Limited configuration options in Managed Airflow (Gen 3)

Managed Airflow (Gen 3) introduces limited Airflow configuration options. Values of
these options can have values only in specific ranges. The limits help to make
sure that certain Airflow configurations does not impact the environment's
operation or performance in negative ways.




| 
Section | 
Configuration option | 
Minimum | 
Maximum | 
|




| 
`core` | 
`min_file_process_interval` | 
`30` | 
`any` | 
|


| 
`core` | 
`dag_file_processor_timeout` | 
`any` | 
`600` | 
|


| 
`core` | 
`dagbag_import_timeout` | 
`dag_file_processor_timeout` | 
`600` | 
|


| 
`core` | 
`dagbag_import_timeout` | 
`dag_file_processor_timeout` | 
`600` | 
|


| 
`celery` | 
`worker_concurrency` | 
`1` | 
`24` | 
|


| 
`kubernetes_executor` | 
`worker_pods_queued_check_interval` | 
`30` | 
`60` | 
|


| 
`scheduler` | 
`scheduler_heartbeat_sec` | 
`15` | 
`any` | 
|


| 
`scheduler` | 
`scheduler_health_check_threshold` | 
`2 * scheduler_heartbeat_sec` | 
`any` | 
|


| 
`triggerer` | 
`triggerer_health_check_threshold` | 
`30, or 2 * job_heartbeat_sec` | 
`any` | 
|


| 
`triggerer` | 
`job_heartbeat_sec` | 
`30` | 
`any` | 
|




## Blocked configuration options

If a configuration option is blocked, you cannot [override](/composer/docs/composer-2/override-airflow-configurations)
its value.

### Blocked configurations in Airflow 3.3.1



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
3.3.1 | 
`cli` | 
All configuration options | 
| 
|

| 
3.3.1 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
3.3.1 | 
`api_auth` | 
`jwt_algorithm` | 
| 
|

| 
3.3.1 | 
`api_auth` | 
`jwt_audience` | 
| 
|

| 
3.3.1 | 
`api_auth` | 
`jwt_issuer` | 
| 
|

| 
3.3.1 | 
`api_auth` | 
`jwt_kid` | 
| 
|

| 
3.3.1 | 
`api_auth` | 
`jwt_private_key_path` | 
| 
|

| 
3.3.1 | 
`api_auth` | 
`jwt_secret` | 
| 
|

| 
3.3.1 | 
`api_auth` | 
`trusted_jwks_url` | 
| 
|

| 
3.3.1 | 
`dag_processor` | 
`dag_bundle_config_list` | 
| 
|

| 
3.3.1 | 
`dag_processor` | 
`dag_bundle_storage_path` | 
| 
|

| 
3.3.1 | 
`execution_api` | 
`jwt_audience` | 
| 
|

| 
3.3.1 | 
`execution_api` | 
`jwt_expiration_time` | 
| 
|

| 
3.3.1 | 
`metrics` | 
`statsd_ipv6` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`api_client_retry_configuration` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`cluster_context` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`config_file` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`delete_option_kwargs` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`delete_worker_pods` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`in_cluster` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`kube_client_request_args` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`logs_task_metadata` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`multi_namespace_mode` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`ssl_ca_cert` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`tcp_keep_cnt` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`tcp_keep_idle` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`tcp_keep_intvl` | 
| 
|

| 
3.3.1 | 
`kubernetes` | 
`verify_ssl` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`cluster_context` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`config_file` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`in_cluster` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
| 
|

| 
3.3.1 | 
`kubernetes_executor` | 
`verify_ssl` | 
| 
|

| 
3.3.1 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
3.3.1 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
3.3.1 | 
`celery` | 
`broker_url` | 
| 
|

| 
3.3.1 | 
`celery` | 
`result_backend` | 
| 
|

| 
3.3.1 | 
`celery` | 
`pool` | 
| 
|

| 
3.3.1 | 
`celery` | 
`worker_autoscale` | 
| 
|

| 
3.3.1 | 
`celery` | 
`default_queue` | 
| 
|

| 
3.3.1 | 
`celery` | 
`celery_config_options` | 
| 
|

| 
3.3.1 | 
`celery` | 
`flower_basic_auth` | 
| 
|

| 
3.3.1 | 
`celery` | 
`flower_host` | 
| 
|

| 
3.3.1 | 
`celery` | 
`flower_port` | 
| 
|

| 
3.3.1 | 
`celery` | 
`flower_url_prefix` | 
| 
|

| 
3.3.1 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
| 
|

| 
3.3.1 | 
`celery` | 
`ssl_active` | 
| 
|

| 
3.3.1 | 
`celery` | 
`ssl_cacert` | 
| 
|

| 
3.3.1 | 
`celery` | 
`ssl_cert` | 
| 
|

| 
3.3.1 | 
`celery` | 
`ssl_key` | 
| 
|

| 
3.3.1 | 
`celery` | 
`worker_enable_remote_control` | 
| 
|

| 
3.3.1 | 
`celery` | 
`worker_precheck` | 
| 
|

| 
3.3.1 | 
`celery` | 
`worker_prefetch_multiplier` | 
| 
|

| 
3.3.1 | 
`operators` | 
`default_queue` | 
| 
|

| 
3.3.1 | 
`core` | 
`dags_folder` | 
| 
|

| 
3.3.1 | 
`core` | 
`database_access_isolation` | 
| 
|

| 
3.3.1 | 
`core` | 
`execution_api_server_url` | 
| 
|

| 
3.3.1 | 
`core` | 
`fernet_key` | 
| 
|

| 
3.3.1 | 
`core` | 
`multi_team` | 
| 
|

| 
3.3.1 | 
`core` | 
`plugins_folder` | 
| 
|

| 
3.3.1 | 
`core` | 
`security` | 
| 
|

| 
3.3.1 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
3.3.1 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.3.1 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.3.1 | 
`core` | 
`load_examples` | 
| 
|

| 
3.3.1 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
3.3.1 | 
`core` | 
`store_dag_code` | 
| 
|

| 
3.3.1 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
3.3.1 | 
`core` | 
`base_log_folder` | 
| 
|

| 
3.3.1 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
3.3.1 | 
`core` | 
`logging_config_class` | 
| 
|

| 
3.3.1 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
3.3.1 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
3.3.1 | 
`core` | 
`remote_logging` | 
| 
|

| 
3.3.1 | 
`core` | 
`task_log_reader` | 
| 
|

| 
3.3.1 | 
`core` | 
`log_format` | 
| 
|

| 
3.3.1 | 
`core` | 
`daemon_umask` | 
| 
|

| 
3.3.1 | 
`core` | 
`default_impersonation` | 
| 
|

| 
3.3.1 | 
`core` | 
`donot_pickle` | 
| 
|

| 
3.3.1 | 
`core` | 
`executor` | 
| 
|

| 
3.3.1 | 
`core` | 
`hostname_callable` | 
| 
|

| 
3.3.1 | 
`core` | 
`unit_test_mode` | 
| 
|

| 
3.3.1 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
3.3.1 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.3.1 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.3.1 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
3.3.1 | 
`database` | 
`external_db_managers` | 
| 
|

| 
3.3.1 | 
`database` | 
`migration_batch_size` | 
| 
|

| 
3.3.1 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
3.3.1 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
3.3.1 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
3.3.1 | 
`scheduler` | 
`enable_tracemalloc` | 
| 
|

| 
3.3.1 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
3.3.1 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
3.3.1 | 
`scheduler` | 
`parsing_processes` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`base_url` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`secret_key` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
3.3.1 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
3.3.1 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
3.3.1 | 
`logging` | 
`callsite_parameters` | 
| 
|

| 
3.3.1 | 
`logging` | 
`colored_console_log` | 
| 
|

| 
3.3.1 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
3.3.1 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
3.3.1 | 
`logging` | 
`log_format` | 
| 
|

| 
3.3.1 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
3.3.1 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
3.3.1 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
3.3.1 | 
`logging` | 
`remote_logging` | 
| 
|

| 
3.3.1 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
3.3.1 | 
`api` | 
`google_oauth2_audience` | 
| 
|

| 
3.3.1 | 
`api` | 
`rbac_bindings` | 
| 
|

| 
3.3.1 | 
`usage_data_collection` | 
`enabled` | 
| 
|



### Blocked configurations in Airflow 3.2.2



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
3.2.2 | 
`cli` | 
All configuration options | 
| 
|

| 
3.2.2 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
3.2.2 | 
`api_auth` | 
`jwt_algorithm` | 
| 
|

| 
3.2.2 | 
`api_auth` | 
`jwt_audience` | 
| 
|

| 
3.2.2 | 
`api_auth` | 
`jwt_issuer` | 
| 
|

| 
3.2.2 | 
`api_auth` | 
`jwt_kid` | 
| 
|

| 
3.2.2 | 
`api_auth` | 
`jwt_private_key_path` | 
| 
|

| 
3.2.2 | 
`api_auth` | 
`jwt_secret` | 
| 
|

| 
3.2.2 | 
`api_auth` | 
`trusted_jwks_url` | 
| 
|

| 
3.2.2 | 
`dag_processor` | 
`dag_bundle_config_list` | 
| 
|

| 
3.2.2 | 
`dag_processor` | 
`dag_bundle_storage_path` | 
| 
|

| 
3.2.2 | 
`execution_api` | 
`jwt_audience` | 
| 
|

| 
3.2.2 | 
`execution_api` | 
`jwt_expiration_time` | 
| 
|

| 
3.2.2 | 
`metrics` | 
`statsd_ipv6` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`api_client_retry_configuration` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`cluster_context` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`config_file` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`delete_option_kwargs` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`delete_worker_pods` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`in_cluster` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`kube_client_request_args` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`logs_task_metadata` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`multi_namespace_mode` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`ssl_ca_cert` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`tcp_keep_cnt` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`tcp_keep_idle` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`tcp_keep_intvl` | 
| 
|

| 
3.2.2 | 
`kubernetes` | 
`verify_ssl` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`cluster_context` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`config_file` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`in_cluster` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
| 
|

| 
3.2.2 | 
`kubernetes_executor` | 
`verify_ssl` | 
| 
|

| 
3.2.2 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
3.2.2 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
3.2.2 | 
`celery` | 
`broker_url` | 
| 
|

| 
3.2.2 | 
`celery` | 
`result_backend` | 
| 
|

| 
3.2.2 | 
`celery` | 
`pool` | 
| 
|

| 
3.2.2 | 
`celery` | 
`worker_autoscale` | 
| 
|

| 
3.2.2 | 
`celery` | 
`default_queue` | 
| 
|

| 
3.2.2 | 
`celery` | 
`celery_config_options` | 
| 
|

| 
3.2.2 | 
`celery` | 
`flower_basic_auth` | 
| 
|

| 
3.2.2 | 
`celery` | 
`flower_host` | 
| 
|

| 
3.2.2 | 
`celery` | 
`flower_port` | 
| 
|

| 
3.2.2 | 
`celery` | 
`flower_url_prefix` | 
| 
|

| 
3.2.2 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
| 
|

| 
3.2.2 | 
`celery` | 
`ssl_active` | 
| 
|

| 
3.2.2 | 
`celery` | 
`ssl_cacert` | 
| 
|

| 
3.2.2 | 
`celery` | 
`ssl_cert` | 
| 
|

| 
3.2.2 | 
`celery` | 
`ssl_key` | 
| 
|

| 
3.2.2 | 
`celery` | 
`worker_enable_remote_control` | 
| 
|

| 
3.2.2 | 
`celery` | 
`worker_precheck` | 
| 
|

| 
3.2.2 | 
`celery` | 
`worker_prefetch_multiplier` | 
| 
|

| 
3.2.2 | 
`operators` | 
`default_queue` | 
| 
|

| 
3.2.2 | 
`core` | 
`dags_folder` | 
| 
|

| 
3.2.2 | 
`core` | 
`database_access_isolation` | 
| 
|

| 
3.2.2 | 
`core` | 
`execution_api_server_url` | 
| 
|

| 
3.2.2 | 
`core` | 
`fernet_key` | 
| 
|

| 
3.2.2 | 
`core` | 
`multi_team` | 
| 
|

| 
3.2.2 | 
`core` | 
`plugins_folder` | 
| 
|

| 
3.2.2 | 
`core` | 
`security` | 
| 
|

| 
3.2.2 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
3.2.2 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.2.2 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.2.2 | 
`core` | 
`load_examples` | 
| 
|

| 
3.2.2 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
3.2.2 | 
`core` | 
`store_dag_code` | 
| 
|

| 
3.2.2 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
3.2.2 | 
`core` | 
`base_log_folder` | 
| 
|

| 
3.2.2 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
3.2.2 | 
`core` | 
`logging_config_class` | 
| 
|

| 
3.2.2 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
3.2.2 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
3.2.2 | 
`core` | 
`remote_logging` | 
| 
|

| 
3.2.2 | 
`core` | 
`task_log_reader` | 
| 
|

| 
3.2.2 | 
`core` | 
`log_format` | 
| 
|

| 
3.2.2 | 
`core` | 
`daemon_umask` | 
| 
|

| 
3.2.2 | 
`core` | 
`default_impersonation` | 
| 
|

| 
3.2.2 | 
`core` | 
`donot_pickle` | 
| 
|

| 
3.2.2 | 
`core` | 
`executor` | 
| 
|

| 
3.2.2 | 
`core` | 
`hostname_callable` | 
| 
|

| 
3.2.2 | 
`core` | 
`unit_test_mode` | 
| 
|

| 
3.2.2 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
3.2.2 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.2.2 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.2.2 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
3.2.2 | 
`database` | 
`external_db_managers` | 
| 
|

| 
3.2.2 | 
`database` | 
`migration_batch_size` | 
| 
|

| 
3.2.2 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
3.2.2 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
3.2.2 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
3.2.2 | 
`scheduler` | 
`enable_tracemalloc` | 
| 
|

| 
3.2.2 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
3.2.2 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
3.2.2 | 
`scheduler` | 
`parsing_processes` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`base_url` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`secret_key` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
3.2.2 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
3.2.2 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
3.2.2 | 
`logging` | 
`callsite_parameters` | 
| 
|

| 
3.2.2 | 
`logging` | 
`colored_console_log` | 
| 
|

| 
3.2.2 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
3.2.2 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
3.2.2 | 
`logging` | 
`log_format` | 
| 
|

| 
3.2.2 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
3.2.2 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
3.2.2 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
3.2.2 | 
`logging` | 
`remote_logging` | 
| 
|

| 
3.2.2 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
3.2.2 | 
`api` | 
`google_oauth2_audience` | 
| 
|

| 
3.2.2 | 
`api` | 
`rbac_bindings` | 
| 
|

| 
3.2.2 | 
`usage_data_collection` | 
`enabled` | 
| 
|



### Blocked configurations in Airflow 3.1.8



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
3.1.8 | 
`cli` | 
All configuration options | 
| 
|

| 
3.1.8 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
3.1.8 | 
`api_auth` | 
`jwt_algorithm` | 
| 
|

| 
3.1.8 | 
`api_auth` | 
`jwt_audience` | 
| 
|

| 
3.1.8 | 
`api_auth` | 
`jwt_issuer` | 
| 
|

| 
3.1.8 | 
`api_auth` | 
`jwt_kid` | 
| 
|

| 
3.1.8 | 
`api_auth` | 
`jwt_private_key_path` | 
| 
|

| 
3.1.8 | 
`api_auth` | 
`jwt_secret` | 
| 
|

| 
3.1.8 | 
`api_auth` | 
`trusted_jwks_url` | 
| 
|

| 
3.1.8 | 
`dag_processor` | 
`dag_bundle_config_list` | 
| 
|

| 
3.1.8 | 
`dag_processor` | 
`dag_bundle_storage_path` | 
| 
|

| 
3.1.8 | 
`execution_api` | 
`jwt_audience` | 
| 
|

| 
3.1.8 | 
`execution_api` | 
`jwt_expiration_time` | 
| 
|

| 
3.1.8 | 
`metrics` | 
`statsd_ipv6` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`api_client_retry_configuration` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`cluster_context` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`config_file` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`delete_option_kwargs` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`delete_worker_pods` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`in_cluster` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`kube_client_request_args` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`logs_task_metadata` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`multi_namespace_mode` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`ssl_ca_cert` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`tcp_keep_cnt` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`tcp_keep_idle` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`tcp_keep_intvl` | 
| 
|

| 
3.1.8 | 
`kubernetes` | 
`verify_ssl` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`cluster_context` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`config_file` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`in_cluster` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
| 
|

| 
3.1.8 | 
`kubernetes_executor` | 
`verify_ssl` | 
| 
|

| 
3.1.8 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
3.1.8 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
3.1.8 | 
`celery` | 
`broker_url` | 
| 
|

| 
3.1.8 | 
`celery` | 
`result_backend` | 
| 
|

| 
3.1.8 | 
`celery` | 
`pool` | 
| 
|

| 
3.1.8 | 
`celery` | 
`worker_autoscale` | 
| 
|

| 
3.1.8 | 
`celery` | 
`default_queue` | 
| 
|

| 
3.1.8 | 
`celery` | 
`celery_config_options` | 
| 
|

| 
3.1.8 | 
`celery` | 
`flower_basic_auth` | 
| 
|

| 
3.1.8 | 
`celery` | 
`flower_host` | 
| 
|

| 
3.1.8 | 
`celery` | 
`flower_port` | 
| 
|

| 
3.1.8 | 
`celery` | 
`flower_url_prefix` | 
| 
|

| 
3.1.8 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
| 
|

| 
3.1.8 | 
`celery` | 
`ssl_active` | 
| 
|

| 
3.1.8 | 
`celery` | 
`ssl_cacert` | 
| 
|

| 
3.1.8 | 
`celery` | 
`ssl_cert` | 
| 
|

| 
3.1.8 | 
`celery` | 
`ssl_key` | 
| 
|

| 
3.1.8 | 
`celery` | 
`worker_enable_remote_control` | 
| 
|

| 
3.1.8 | 
`celery` | 
`worker_precheck` | 
| 
|

| 
3.1.8 | 
`celery` | 
`worker_prefetch_multiplier` | 
| 
|

| 
3.1.8 | 
`operators` | 
`default_queue` | 
| 
|

| 
3.1.8 | 
`core` | 
`dags_folder` | 
| 
|

| 
3.1.8 | 
`core` | 
`database_access_isolation` | 
| 
|

| 
3.1.8 | 
`core` | 
`execution_api_server_url` | 
| 
|

| 
3.1.8 | 
`core` | 
`fernet_key` | 
| 
|

| 
3.1.8 | 
`core` | 
`plugins_folder` | 
| 
|

| 
3.1.8 | 
`core` | 
`security` | 
| 
|

| 
3.1.8 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
3.1.8 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.1.8 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.1.8 | 
`core` | 
`load_examples` | 
| 
|

| 
3.1.8 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
3.1.8 | 
`core` | 
`store_dag_code` | 
| 
|

| 
3.1.8 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
3.1.8 | 
`core` | 
`base_log_folder` | 
| 
|

| 
3.1.8 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
3.1.8 | 
`core` | 
`logging_config_class` | 
| 
|

| 
3.1.8 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
3.1.8 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
3.1.8 | 
`core` | 
`remote_logging` | 
| 
|

| 
3.1.8 | 
`core` | 
`task_log_reader` | 
| 
|

| 
3.1.8 | 
`core` | 
`log_format` | 
| 
|

| 
3.1.8 | 
`core` | 
`daemon_umask` | 
| 
|

| 
3.1.8 | 
`core` | 
`default_impersonation` | 
| 
|

| 
3.1.8 | 
`core` | 
`donot_pickle` | 
| 
|

| 
3.1.8 | 
`core` | 
`executor` | 
| 
|

| 
3.1.8 | 
`core` | 
`hostname_callable` | 
| 
|

| 
3.1.8 | 
`core` | 
`unit_test_mode` | 
| 
|

| 
3.1.8 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
3.1.8 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.1.8 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.1.8 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
3.1.8 | 
`database` | 
`external_db_managers` | 
| 
|

| 
3.1.8 | 
`database` | 
`migration_batch_size` | 
| 
|

| 
3.1.8 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
3.1.8 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
3.1.8 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
3.1.8 | 
`scheduler` | 
`enable_tracemalloc` | 
| 
|

| 
3.1.8 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
3.1.8 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
3.1.8 | 
`scheduler` | 
`parsing_processes` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`base_url` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`secret_key` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
3.1.8 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
3.1.8 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
3.1.8 | 
`logging` | 
`callsite_parameters` | 
| 
|

| 
3.1.8 | 
`logging` | 
`colored_console_log` | 
| 
|

| 
3.1.8 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
3.1.8 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
3.1.8 | 
`logging` | 
`log_format` | 
| 
|

| 
3.1.8 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
3.1.8 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
3.1.8 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
3.1.8 | 
`logging` | 
`remote_logging` | 
| 
|

| 
3.1.8 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
3.1.8 | 
`api` | 
`google_oauth2_audience` | 
| 
|

| 
3.1.8 | 
`usage_data_collection` | 
`enabled` | 
| 
|



### Blocked configurations in Airflow 3.1.7



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
3.1.7 | 
`cli` | 
All configuration options | 
| 
|

| 
3.1.7 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
3.1.7 | 
`api_auth` | 
`jwt_algorithm` | 
| 
|

| 
3.1.7 | 
`api_auth` | 
`jwt_audience` | 
| 
|

| 
3.1.7 | 
`api_auth` | 
`jwt_issuer` | 
| 
|

| 
3.1.7 | 
`api_auth` | 
`jwt_kid` | 
| 
|

| 
3.1.7 | 
`api_auth` | 
`jwt_private_key_path` | 
| 
|

| 
3.1.7 | 
`api_auth` | 
`jwt_secret` | 
| 
|

| 
3.1.7 | 
`api_auth` | 
`trusted_jwks_url` | 
| 
|

| 
3.1.7 | 
`dag_processor` | 
`dag_bundle_storage_path` | 
| 
|

| 
3.1.7 | 
`dag_processor` | 
`dag_bundle_config_list` | 
| 
|

| 
3.1.7 | 
`execution_api` | 
`jwt_audience` | 
| 
|

| 
3.1.7 | 
`execution_api` | 
`jwt_expiration_time` | 
| 
|

| 
3.1.7 | 
`metrics` | 
`statsd_ipv6` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`api_client_retry_configuration` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`cluster_context` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`config_file` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`delete_option_kwargs` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`delete_worker_pods` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`in_cluster` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`kube_client_request_args` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`logs_task_metadata` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`multi_namespace_mode` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`ssl_ca_cert` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`tcp_keep_cnt` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`tcp_keep_idle` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`tcp_keep_intvl` | 
| 
|

| 
3.1.7 | 
`kubernetes` | 
`verify_ssl` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`cluster_context` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`config_file` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`in_cluster` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
| 
|

| 
3.1.7 | 
`kubernetes_executor` | 
`verify_ssl` | 
| 
|

| 
3.1.7 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
3.1.7 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
3.1.7 | 
`celery` | 
`broker_url` | 
| 
|

| 
3.1.7 | 
`celery` | 
`result_backend` | 
| 
|

| 
3.1.7 | 
`celery` | 
`pool` | 
| 
|

| 
3.1.7 | 
`celery` | 
`worker_autoscale` | 
| 
|

| 
3.1.7 | 
`celery` | 
`default_queue` | 
| 
|

| 
3.1.7 | 
`celery` | 
`celery_config_options` | 
| 
|

| 
3.1.7 | 
`celery` | 
`flower_basic_auth` | 
| 
|

| 
3.1.7 | 
`celery` | 
`flower_host` | 
| 
|

| 
3.1.7 | 
`celery` | 
`flower_port` | 
| 
|

| 
3.1.7 | 
`celery` | 
`flower_url_prefix` | 
| 
|

| 
3.1.7 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
| 
|

| 
3.1.7 | 
`celery` | 
`ssl_active` | 
| 
|

| 
3.1.7 | 
`celery` | 
`ssl_cacert` | 
| 
|

| 
3.1.7 | 
`celery` | 
`ssl_cert` | 
| 
|

| 
3.1.7 | 
`celery` | 
`ssl_key` | 
| 
|

| 
3.1.7 | 
`celery` | 
`worker_enable_remote_control` | 
| 
|

| 
3.1.7 | 
`celery` | 
`worker_precheck` | 
| 
|

| 
3.1.7 | 
`celery` | 
`worker_prefetch_multiplier` | 
| 
|

| 
3.1.7 | 
`operators` | 
`default_queue` | 
| 
|

| 
3.1.7 | 
`core` | 
`dags_folder` | 
| 
|

| 
3.1.7 | 
`core` | 
`database_access_isolation` | 
| 
|

| 
3.1.7 | 
`core` | 
`execution_api_server_url` | 
| 
|

| 
3.1.7 | 
`core` | 
`fernet_key` | 
| 
|

| 
3.1.7 | 
`core` | 
`plugins_folder` | 
| 
|

| 
3.1.7 | 
`core` | 
`security` | 
| 
|

| 
3.1.7 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
3.1.7 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.1.7 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.1.7 | 
`core` | 
`load_examples` | 
| 
|

| 
3.1.7 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
3.1.7 | 
`core` | 
`store_dag_code` | 
| 
|

| 
3.1.7 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
3.1.7 | 
`core` | 
`base_log_folder` | 
| 
|

| 
3.1.7 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
3.1.7 | 
`core` | 
`logging_config_class` | 
| 
|

| 
3.1.7 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
3.1.7 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
3.1.7 | 
`core` | 
`remote_logging` | 
| 
|

| 
3.1.7 | 
`core` | 
`task_log_reader` | 
| 
|

| 
3.1.7 | 
`core` | 
`log_format` | 
| 
|

| 
3.1.7 | 
`core` | 
`daemon_umask` | 
| 
|

| 
3.1.7 | 
`core` | 
`default_impersonation` | 
| 
|

| 
3.1.7 | 
`core` | 
`donot_pickle` | 
| 
|

| 
3.1.7 | 
`core` | 
`executor` | 
| 
|

| 
3.1.7 | 
`core` | 
`hostname_callable` | 
| 
|

| 
3.1.7 | 
`core` | 
`unit_test_mode` | 
| 
|

| 
3.1.7 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
3.1.7 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.1.7 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.1.7 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
3.1.7 | 
`database` | 
`external_db_managers` | 
| 
|

| 
3.1.7 | 
`database` | 
`migration_batch_size` | 
| 
|

| 
3.1.7 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
3.1.7 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
3.1.7 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
3.1.7 | 
`scheduler` | 
`enable_tracemalloc` | 
| 
|

| 
3.1.7 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
3.1.7 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
3.1.7 | 
`scheduler` | 
`parsing_processes` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`base_url` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`secret_key` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
3.1.7 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
3.1.7 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
3.1.7 | 
`logging` | 
`callsite_parameters` | 
| 
|

| 
3.1.7 | 
`logging` | 
`colored_console_log` | 
| 
|

| 
3.1.7 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
3.1.7 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
3.1.7 | 
`logging` | 
`log_format` | 
| 
|

| 
3.1.7 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
3.1.7 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
3.1.7 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
3.1.7 | 
`logging` | 
`remote_logging` | 
| 
|

| 
3.1.7 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
3.1.7 | 
`api` | 
`google_oauth2_audience` | 
| 
|

| 
3.1.7 | 
`usage_data_collection` | 
`enabled` | 
| 
|



### Blocked configurations in Airflow 3.1.0



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
3.1.0 | 
`cli` | 
All configuration options | 
| 
|

| 
3.1.0 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
3.1.0 | 
`api_auth` | 
`jwt_algorithm` | 
| 
|

| 
3.1.0 | 
`api_auth` | 
`jwt_audience` | 
| 
|

| 
3.1.0 | 
`api_auth` | 
`jwt_issuer` | 
| 
|

| 
3.1.0 | 
`api_auth` | 
`jwt_kid` | 
| 
|

| 
3.1.0 | 
`api_auth` | 
`jwt_private_key_path` | 
| 
|

| 
3.1.0 | 
`api_auth` | 
`jwt_secret` | 
| 
|

| 
3.1.0 | 
`api_auth` | 
`trusted_jwks_url` | 
| 
|

| 
3.1.0 | 
`dag_processor` | 
`dag_bundle_storage_path` | 
| 
|

| 
3.1.0 | 
`execution_api` | 
`jwt_audience` | 
| 
|

| 
3.1.0 | 
`execution_api` | 
`jwt_expiration_time` | 
| 
|

| 
3.1.0 | 
`metrics` | 
`statsd_ipv6` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`api_client_retry_configuration` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`cluster_context` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`config_file` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`delete_option_kwargs` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`delete_worker_pods` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`in_cluster` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`kube_client_request_args` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`logs_task_metadata` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`multi_namespace_mode` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`ssl_ca_cert` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`tcp_keep_cnt` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`tcp_keep_idle` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`tcp_keep_intvl` | 
| 
|

| 
3.1.0 | 
`kubernetes` | 
`verify_ssl` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`cluster_context` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`config_file` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`in_cluster` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
| 
|

| 
3.1.0 | 
`kubernetes_executor` | 
`verify_ssl` | 
| 
|

| 
3.1.0 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
3.1.0 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
3.1.0 | 
`celery` | 
`broker_url` | 
| 
|

| 
3.1.0 | 
`celery` | 
`result_backend` | 
| 
|

| 
3.1.0 | 
`celery` | 
`pool` | 
| 
|

| 
3.1.0 | 
`celery` | 
`worker_autoscale` | 
| 
|

| 
3.1.0 | 
`celery` | 
`default_queue` | 
| 
|

| 
3.1.0 | 
`celery` | 
`celery_config_options` | 
| 
|

| 
3.1.0 | 
`celery` | 
`flower_basic_auth` | 
| 
|

| 
3.1.0 | 
`celery` | 
`flower_host` | 
| 
|

| 
3.1.0 | 
`celery` | 
`flower_port` | 
| 
|

| 
3.1.0 | 
`celery` | 
`flower_url_prefix` | 
| 
|

| 
3.1.0 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
| 
|

| 
3.1.0 | 
`celery` | 
`ssl_active` | 
| 
|

| 
3.1.0 | 
`celery` | 
`ssl_cacert` | 
| 
|

| 
3.1.0 | 
`celery` | 
`ssl_cert` | 
| 
|

| 
3.1.0 | 
`celery` | 
`ssl_key` | 
| 
|

| 
3.1.0 | 
`celery` | 
`worker_enable_remote_control` | 
| 
|

| 
3.1.0 | 
`celery` | 
`worker_precheck` | 
| 
|

| 
3.1.0 | 
`celery` | 
`worker_prefetch_multiplier` | 
| 
|

| 
3.1.0 | 
`operators` | 
`default_queue` | 
| 
|

| 
3.1.0 | 
`core` | 
`dags_folder` | 
| 
|

| 
3.1.0 | 
`core` | 
`database_access_isolation` | 
| 
|

| 
3.1.0 | 
`core` | 
`execution_api_server_url` | 
| 
|

| 
3.1.0 | 
`core` | 
`fernet_key` | 
| 
|

| 
3.1.0 | 
`core` | 
`plugins_folder` | 
| 
|

| 
3.1.0 | 
`core` | 
`security` | 
| 
|

| 
3.1.0 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
3.1.0 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.1.0 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.1.0 | 
`core` | 
`load_examples` | 
| 
|

| 
3.1.0 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
3.1.0 | 
`core` | 
`store_dag_code` | 
| 
|

| 
3.1.0 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
3.1.0 | 
`core` | 
`base_log_folder` | 
| 
|

| 
3.1.0 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
3.1.0 | 
`core` | 
`logging_config_class` | 
| 
|

| 
3.1.0 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
3.1.0 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
3.1.0 | 
`core` | 
`remote_logging` | 
| 
|

| 
3.1.0 | 
`core` | 
`task_log_reader` | 
| 
|

| 
3.1.0 | 
`core` | 
`log_format` | 
| 
|

| 
3.1.0 | 
`core` | 
`daemon_umask` | 
| 
|

| 
3.1.0 | 
`core` | 
`default_impersonation` | 
| 
|

| 
3.1.0 | 
`core` | 
`donot_pickle` | 
| 
|

| 
3.1.0 | 
`core` | 
`executor` | 
| 
|

| 
3.1.0 | 
`core` | 
`hostname_callable` | 
| 
|

| 
3.1.0 | 
`core` | 
`unit_test_mode` | 
| 
|

| 
3.1.0 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
3.1.0 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
3.1.0 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
3.1.0 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
3.1.0 | 
`database` | 
`external_db_managers` | 
| 
|

| 
3.1.0 | 
`database` | 
`migration_batch_size` | 
| 
|

| 
3.1.0 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
3.1.0 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
3.1.0 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
3.1.0 | 
`scheduler` | 
`enable_tracemalloc` | 
| 
|

| 
3.1.0 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
3.1.0 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
3.1.0 | 
`scheduler` | 
`parsing_processes` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`base_url` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`secret_key` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
3.1.0 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
3.1.0 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
3.1.0 | 
`logging` | 
`colored_console_log` | 
| 
|

| 
3.1.0 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
3.1.0 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
3.1.0 | 
`logging` | 
`log_format` | 
| 
|

| 
3.1.0 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
3.1.0 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
3.1.0 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
3.1.0 | 
`logging` | 
`remote_logging` | 
| 
|

| 
3.1.0 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
3.1.0 | 
`api` | 
`google_oauth2_audience` | 
| 
|

| 
3.1.0 | 
`usage_data_collection` | 
`enabled` | 
| 
|



### Blocked configurations in Airflow 2.11.1



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
2.11.1 | 
`cli` | 
All configuration options | 
| 
|

| 
2.11.1 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
2.11.1 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
2.11.1 | 
`kubernetes` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`kubernetes_executor` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
2.11.1 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
2.11.1 | 
`celery` | 
`broker_url` | 
| 
|

| 
2.11.1 | 
`celery` | 
`result_backend` | 
| 
|

| 
2.11.1 | 
`celery` | 
`pool` | 
| 
|

| 
2.11.1 | 
`celery` | 
`worker_autoscale` | 
| 
|

| 
2.11.1 | 
`celery` | 
`default_queue` | 
| 
|

| 
2.11.1 | 
`celery` | 
`celery_config_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`flower_basic_auth` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`flower_host` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`flower_port` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`flower_url_prefix` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`ssl_active` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`ssl_cacert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`ssl_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`ssl_key` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`worker_enable_remote_control` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`worker_precheck` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`celery` | 
`worker_prefetch_multiplier` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`operators` | 
`default_queue` | 
| 
|

| 
2.11.1 | 
`core` | 
`dags_folder` | 
| 
|

| 
2.11.1 | 
`core` | 
`database_access_isolation` | 
| 
|

| 
2.11.1 | 
`core` | 
`fernet_key` | 
| 
|

| 
2.11.1 | 
`core` | 
`plugins_folder` | 
| 
|

| 
2.11.1 | 
`core` | 
`security` | 
| 
|

| 
2.11.1 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
2.11.1 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.11.1 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.11.1 | 
`core` | 
`load_examples` | 
| 
|

| 
2.11.1 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
2.11.1 | 
`core` | 
`store_dag_code` | 
| 
|

| 
2.11.1 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
2.11.1 | 
`core` | 
`base_log_folder` | 
| 
|

| 
2.11.1 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
2.11.1 | 
`core` | 
`logging_config_class` | 
| 
|

| 
2.11.1 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
2.11.1 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
2.11.1 | 
`core` | 
`remote_logging` | 
| 
|

| 
2.11.1 | 
`core` | 
`task_log_reader` | 
| 
|

| 
2.11.1 | 
`core` | 
`log_format` | 
| 
|

| 
2.11.1 | 
`core` | 
`daemon_umask` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`core` | 
`default_impersonation` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`core` | 
`donot_pickle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`core` | 
`executor` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`core` | 
`hostname_callable` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`core` | 
`unit_test_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
2.11.1 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.11.1 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.11.1 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
2.11.1 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
2.11.1 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
2.11.1 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
2.11.1 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
2.11.1 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
2.11.1 | 
`scheduler` | 
`parsing_processes` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.11.1 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`base_url` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`secret_key` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
2.11.1 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
2.11.1 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
2.11.1 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
2.11.1 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
2.11.1 | 
`logging` | 
`log_format` | 
| 
|

| 
2.11.1 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
2.11.1 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
2.11.1 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
2.11.1 | 
`logging` | 
`remote_logging` | 
| 
|

| 
2.11.1 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
2.11.1 | 
`api` | 
`google_oauth2_audience` | 
| 
|

| 
2.11.1 | 
`api` | 
`rbac_bindings` | 
| 
|

| 
2.11.1 | 
`usage_data_collection` | 
`enabled` | 
| 
|



### Blocked configurations in Airflow 2.10.5



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
2.10.5 | 
`cli` | 
All configuration options | 
| 
|

| 
2.10.5 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
2.10.5 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
2.10.5 | 
`kubernetes` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`kubernetes_executor` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
2.10.5 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
2.10.5 | 
`celery` | 
`broker_url` | 
| 
|

| 
2.10.5 | 
`celery` | 
`result_backend` | 
| 
|

| 
2.10.5 | 
`celery` | 
`pool` | 
| 
|

| 
2.10.5 | 
`celery` | 
`worker_autoscale` | 
| 
|

| 
2.10.5 | 
`celery` | 
`default_queue` | 
| 
|

| 
2.10.5 | 
`celery` | 
`celery_config_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`flower_basic_auth` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`flower_host` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`flower_port` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`flower_url_prefix` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`ssl_active` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`ssl_cacert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`ssl_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`ssl_key` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`worker_enable_remote_control` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`worker_precheck` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`celery` | 
`worker_prefetch_multiplier` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`operators` | 
`default_queue` | 
| 
|

| 
2.10.5 | 
`core` | 
`dags_folder` | 
| 
|

| 
2.10.5 | 
`core` | 
`database_access_isolation` | 
| 
|

| 
2.10.5 | 
`core` | 
`fernet_key` | 
| 
|

| 
2.10.5 | 
`core` | 
`plugins_folder` | 
| 
|

| 
2.10.5 | 
`core` | 
`security` | 
| 
|

| 
2.10.5 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
2.10.5 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.10.5 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.10.5 | 
`core` | 
`load_examples` | 
| 
|

| 
2.10.5 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
2.10.5 | 
`core` | 
`store_dag_code` | 
| 
|

| 
2.10.5 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
2.10.5 | 
`core` | 
`base_log_folder` | 
| 
|

| 
2.10.5 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
2.10.5 | 
`core` | 
`logging_config_class` | 
| 
|

| 
2.10.5 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
2.10.5 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
2.10.5 | 
`core` | 
`remote_logging` | 
| 
|

| 
2.10.5 | 
`core` | 
`task_log_reader` | 
| 
|

| 
2.10.5 | 
`core` | 
`log_format` | 
| 
|

| 
2.10.5 | 
`core` | 
`daemon_umask` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`core` | 
`default_impersonation` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`core` | 
`donot_pickle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`core` | 
`executor` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`core` | 
`hostname_callable` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`core` | 
`unit_test_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
2.10.5 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.10.5 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.10.5 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
2.10.5 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
2.10.5 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
2.10.5 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
2.10.5 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
2.10.5 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
2.10.5 | 
`scheduler` | 
`parsing_processes` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.5 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`base_url` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`secret_key` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
2.10.5 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
2.10.5 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
2.10.5 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
2.10.5 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
2.10.5 | 
`logging` | 
`log_format` | 
| 
|

| 
2.10.5 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
2.10.5 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
2.10.5 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
2.10.5 | 
`logging` | 
`remote_logging` | 
| 
|

| 
2.10.5 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
2.10.5 | 
`api` | 
`google_oauth2_audience` | 
| 
|

| 
2.10.5 | 
`usage_data_collection` | 
`enabled` | 
| 
|



### Blocked configurations in Airflow 2.10.2



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
2.10.2 | 
`cli` | 
All configuration options | 
| 
|

| 
2.10.2 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
2.10.2 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
2.10.2 | 
`kubernetes` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`kubernetes_executor` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
2.10.2 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
2.10.2 | 
`celery` | 
`broker_url` | 
| 
|

| 
2.10.2 | 
`celery` | 
`result_backend` | 
| 
|

| 
2.10.2 | 
`celery` | 
`pool` | 
| 
|

| 
2.10.2 | 
`celery` | 
`default_queue` | 
| 
|

| 
2.10.2 | 
`celery` | 
`worker_autoscale` | 
| 
|

| 
2.10.2 | 
`celery` | 
`celery_config_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`flower_basic_auth` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`flower_host` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`flower_port` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`flower_url_prefix` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`ssl_active` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`ssl_cacert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`ssl_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`ssl_key` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`worker_enable_remote_control` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`worker_precheck` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`celery` | 
`worker_prefetch_multiplier` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`operators` | 
`default_queue` | 
| 
|

| 
2.10.2 | 
`core` | 
`dags_folder` | 
| 
|

| 
2.10.2 | 
`core` | 
`database_access_isolation` | 
| 
|

| 
2.10.2 | 
`core` | 
`fernet_key` | 
| 
|

| 
2.10.2 | 
`core` | 
`plugins_folder` | 
| 
|

| 
2.10.2 | 
`core` | 
`security` | 
| 
|

| 
2.10.2 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
2.10.2 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.10.2 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.10.2 | 
`core` | 
`load_examples` | 
| 
|

| 
2.10.2 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
2.10.2 | 
`core` | 
`store_dag_code` | 
| 
|

| 
2.10.2 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
2.10.2 | 
`core` | 
`base_log_folder` | 
| 
|

| 
2.10.2 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
2.10.2 | 
`core` | 
`logging_config_class` | 
| 
|

| 
2.10.2 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
2.10.2 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
2.10.2 | 
`core` | 
`remote_logging` | 
| 
|

| 
2.10.2 | 
`core` | 
`task_log_reader` | 
| 
|

| 
2.10.2 | 
`core` | 
`log_format` | 
| 
|

| 
2.10.2 | 
`core` | 
`daemon_umask` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`core` | 
`default_impersonation` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`core` | 
`donot_pickle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`core` | 
`executor` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`core` | 
`hostname_callable` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`core` | 
`unit_test_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
2.10.2 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.10.2 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.10.2 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
2.10.2 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
2.10.2 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
2.10.2 | 
`scheduler` | 
`print_stats_interval` | 
| 
|

| 
2.10.2 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
2.10.2 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
2.10.2 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
2.10.2 | 
`scheduler` | 
`parsing_processes` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.10.2 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`base_url` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`secret_key` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
2.10.2 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
2.10.2 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
2.10.2 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
2.10.2 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
2.10.2 | 
`logging` | 
`log_format` | 
| 
|

| 
2.10.2 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
2.10.2 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
2.10.2 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
2.10.2 | 
`logging` | 
`remote_logging` | 
| 
|

| 
2.10.2 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
2.10.2 | 
`api` | 
`google_oauth2_audience` | 
| 
|

| 
2.10.2 | 
`usage_data_collection` | 
`enabled` | 
| 
|



### Blocked configurations in Airflow 2.9.3



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
2.9.3 | 
`cli` | 
All configuration options | 
| 
|

| 
2.9.3 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
2.9.3 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
2.9.3 | 
`kubernetes` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`kubernetes_executor` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
2.9.3 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
2.9.3 | 
`celery` | 
`broker_url` | 
| 
|

| 
2.9.3 | 
`celery` | 
`result_backend` | 
| 
|

| 
2.9.3 | 
`celery` | 
`pool` | 
| 
|

| 
2.9.3 | 
`celery` | 
`default_queue` | 
| 
|

| 
2.9.3 | 
`celery` | 
`worker_autoscale` | 
In Managed Airflow (Gen 3), and in Managed Airflow (Gen 2) starting from version 2.10.2. | 
|

| 
2.9.3 | 
`celery` | 
`celery_config_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`flower_basic_auth` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`flower_host` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`flower_port` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`flower_url_prefix` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`ssl_active` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`ssl_cacert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`ssl_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`ssl_key` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`worker_enable_remote_control` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`worker_precheck` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`celery` | 
`worker_prefetch_multiplier` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`operators` | 
`default_queue` | 
| 
|

| 
2.9.3 | 
`core` | 
`dags_folder` | 
| 
|

| 
2.9.3 | 
`core` | 
`fernet_key` | 
| 
|

| 
2.9.3 | 
`core` | 
`plugins_folder` | 
| 
|

| 
2.9.3 | 
`core` | 
`security` | 
| 
|

| 
2.9.3 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
2.9.3 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.9.3 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.9.3 | 
`core` | 
`load_examples` | 
| 
|

| 
2.9.3 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
2.9.3 | 
`core` | 
`store_dag_code` | 
| 
|

| 
2.9.3 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
2.9.3 | 
`core` | 
`base_log_folder` | 
| 
|

| 
2.9.3 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
2.9.3 | 
`core` | 
`logging_config_class` | 
| 
|

| 
2.9.3 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
2.9.3 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
2.9.3 | 
`core` | 
`remote_logging` | 
| 
|

| 
2.9.3 | 
`core` | 
`task_log_reader` | 
| 
|

| 
2.9.3 | 
`core` | 
`log_format` | 
| 
|

| 
2.9.3 | 
`core` | 
`daemon_umask` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`core` | 
`default_impersonation` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`core` | 
`donot_pickle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`core` | 
`executor` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`core` | 
`hostname_callable` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`core` | 
`unit_test_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
2.9.3 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.9.3 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.9.3 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
2.9.3 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
2.9.3 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
2.9.3 | 
`scheduler` | 
`print_stats_interval` | 
| 
|

| 
2.9.3 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
2.9.3 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
2.9.3 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
2.9.3 | 
`scheduler` | 
`parsing_processes` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.3 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`base_url` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`secret_key` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
2.9.3 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
2.9.3 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
2.9.3 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
2.9.3 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
2.9.3 | 
`logging` | 
`log_format` | 
| 
|

| 
2.9.3 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
2.9.3 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
2.9.3 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
2.9.3 | 
`logging` | 
`remote_logging` | 
| 
|

| 
2.9.3 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
2.9.3 | 
`api` | 
`google_oauth2_audience` | 
| 
|



### Blocked configurations in Airflow 2.9.1



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
2.9.1 | 
`cli` | 
All configuration options | 
| 
|

| 
2.9.1 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
2.9.1 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
2.9.1 | 
`kubernetes` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`kubernetes_executor` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
2.9.1 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
2.9.1 | 
`celery` | 
`broker_url` | 
| 
|

| 
2.9.1 | 
`celery` | 
`result_backend` | 
| 
|

| 
2.9.1 | 
`celery` | 
`pool` | 
| 
|

| 
2.9.1 | 
`celery` | 
`default_queue` | 
| 
|

| 
2.9.1 | 
`celery` | 
`celery_config_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`flower_basic_auth` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`flower_host` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`flower_port` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`flower_url_prefix` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`worker_autoscale` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`ssl_active` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`ssl_cacert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`ssl_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`ssl_key` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`worker_enable_remote_control` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`worker_precheck` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`celery` | 
`worker_prefetch_multiplier` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`operators` | 
`default_queue` | 
| 
|

| 
2.9.1 | 
`core` | 
`dags_folder` | 
| 
|

| 
2.9.1 | 
`core` | 
`fernet_key` | 
| 
|

| 
2.9.1 | 
`core` | 
`plugins_folder` | 
| 
|

| 
2.9.1 | 
`core` | 
`security` | 
| 
|

| 
2.9.1 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
2.9.1 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.9.1 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.9.1 | 
`core` | 
`load_examples` | 
| 
|

| 
2.9.1 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
2.9.1 | 
`core` | 
`store_dag_code` | 
| 
|

| 
2.9.1 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
2.9.1 | 
`core` | 
`base_log_folder` | 
| 
|

| 
2.9.1 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
2.9.1 | 
`core` | 
`logging_config_class` | 
| 
|

| 
2.9.1 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
2.9.1 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
2.9.1 | 
`core` | 
`remote_logging` | 
| 
|

| 
2.9.1 | 
`core` | 
`task_log_reader` | 
| 
|

| 
2.9.1 | 
`core` | 
`log_format` | 
| 
|

| 
2.9.1 | 
`core` | 
`daemon_umask` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`core` | 
`default_impersonation` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`core` | 
`donot_pickle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`core` | 
`executor` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`core` | 
`hostname_callable` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`core` | 
`unit_test_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
2.9.1 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.9.1 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.9.1 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
2.9.1 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
2.9.1 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
2.9.1 | 
`scheduler` | 
`print_stats_interval` | 
| 
|

| 
2.9.1 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
2.9.1 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
2.9.1 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
2.9.1 | 
`scheduler` | 
`parsing_processes` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.9.1 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`base_url` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`secret_key` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
2.9.1 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
2.9.1 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
2.9.1 | 
`logging` | 
`dag_processor_manager_log_stdout` | 
| 
|

| 
2.9.1 | 
`logging` | 
`enable_task_context_logger` | 
| 
|

| 
2.9.1 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
2.9.1 | 
`logging` | 
`log_format` | 
| 
|

| 
2.9.1 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
2.9.1 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
2.9.1 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
2.9.1 | 
`logging` | 
`remote_logging` | 
| 
|

| 
2.9.1 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
2.9.1 | 
`api` | 
`google_oauth2_audience` | 
| 
|



### Blocked configurations in Airflow 2.7.3



| 
Airflow version | 
Section | 
Configuration option | 
Notes | 
|




| 
2.7.3 | 
`cli` | 
All configuration options | 
| 
|

| 
2.7.3 | 
`metrics` | 
All configuration options | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`pod_template_file` | 
| 
|

| 
2.7.3 | 
`kubernetes` | 
`namespace` | 
| 
|

| 
2.7.3 | 
`kubernetes` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`pod_template_file` | 
| 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`namespace` | 
| 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`api_client_retry_configuration` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`cluster_context` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`config_file` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`delete_option_kwargs` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`delete_worker_pods` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`delete_worker_pods_on_failure` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`enable_tcp_keepalive` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`in_cluster` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`kube_client_request_args` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`logs_task_metadata` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`multi_namespace_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`multi_namespace_mode_namespace_list` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`ssl_ca_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`tcp_keep_cnt` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`tcp_keep_idle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`tcp_keep_intvl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`kubernetes_executor` | 
`verify_ssl` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`celery_app_name` | 
| 
|

| 
2.7.3 | 
`celery` | 
`worker_log_server_port` | 
| 
|

| 
2.7.3 | 
`celery` | 
`broker_url` | 
| 
|

| 
2.7.3 | 
`celery` | 
`result_backend` | 
| 
|

| 
2.7.3 | 
`celery` | 
`pool` | 
| 
|

| 
2.7.3 | 
`celery` | 
`default_queue` | 
| 
|

| 
2.7.3 | 
`celery` | 
`celery_config_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`flower_basic_auth` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`flower_host` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`flower_port` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`flower_url_prefix` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`result_backend_sqlalchemy_engine_options` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`worker_autoscale` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`ssl_active` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`ssl_cacert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`ssl_cert` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`ssl_key` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`worker_enable_remote_control` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`worker_precheck` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`celery` | 
`worker_prefetch_multiplier` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`operators` | 
`default_queue` | 
| 
|

| 
2.7.3 | 
`core` | 
`dags_folder` | 
| 
|

| 
2.7.3 | 
`core` | 
`fernet_key` | 
| 
|

| 
2.7.3 | 
`core` | 
`plugins_folder` | 
| 
|

| 
2.7.3 | 
`core` | 
`security` | 
| 
|

| 
2.7.3 | 
`core` | 
`sql_alchemy_conn` | 
| 
|

| 
2.7.3 | 
`core` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.7.3 | 
`core` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.7.3 | 
`core` | 
`load_examples` | 
| 
|

| 
2.7.3 | 
`core` | 
`store_serialized_dags` | 
| 
|

| 
2.7.3 | 
`core` | 
`store_dag_code` | 
| 
|

| 
2.7.3 | 
`core` | 
`wait_dag_not_found_timeout` | 
| 
|

| 
2.7.3 | 
`core` | 
`base_log_folder` | 
| 
|

| 
2.7.3 | 
`core` | 
`encrypt_s3_logs` | 
| 
|

| 
2.7.3 | 
`core` | 
`logging_config_class` | 
| 
|

| 
2.7.3 | 
`core` | 
`remote_base_log_folder` | 
| 
|

| 
2.7.3 | 
`core` | 
`remote_log_conn_id` | 
| 
|

| 
2.7.3 | 
`core` | 
`remote_logging` | 
| 
|

| 
2.7.3 | 
`core` | 
`task_log_reader` | 
| 
|

| 
2.7.3 | 
`core` | 
`log_format` | 
| 
|

| 
2.7.3 | 
`core` | 
`daemon_umask` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`core` | 
`default_impersonation` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`core` | 
`donot_pickle` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`core` | 
`executor` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`core` | 
`hostname_callable` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`core` | 
`unit_test_mode` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`database` | 
`sql_alchemy_conn` | 
| 
|

| 
2.7.3 | 
`database` | 
`sql_alchemy_pool_recycle` | 
| 
|

| 
2.7.3 | 
`database` | 
`sql_alchemy_pool_size` | 
| 
|

| 
2.7.3 | 
`database` | 
`alembic_ini_file_path` | 
| 
|

| 
2.7.3 | 
`smtp` | 
`smtp_password` | 
| 
|

| 
2.7.3 | 
`scheduler` | 
`child_process_log_directory` | 
| 
|

| 
2.7.3 | 
`scheduler` | 
`print_stats_interval` | 
| 
|

| 
2.7.3 | 
`scheduler` | 
`enable_health_check` | 
| 
|

| 
2.7.3 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
| 
|

| 
2.7.3 | 
`scheduler` | 
`standalone_dag_processor` | 
| 
|

| 
2.7.3 | 
`scheduler` | 
`parsing_processes` | 
Only in Managed Airflow (Gen 3) | 
|

| 
2.7.3 | 
`webserver` | 
`access_logfile` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`base_url` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`error_logfile` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`log_fetch_timeout_sec` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`secret_key` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`web_server_host` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`web_server_port` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`web_server_ssl_cert` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`web_server_ssl_key` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`web_server_worker_timeout` | 
| 
|

| 
2.7.3 | 
`webserver` | 
`worker_refresh_batch_size` | 
| 
|

| 
2.7.3 | 
`logging` | 
`base_log_folder` | 
| 
|

| 
2.7.3 | 
`logging` | 
`encrypt_s3_logs` | 
| 
|

| 
2.7.3 | 
`logging` | 
`logging_config_class` | 
| 
|

| 
2.7.3 | 
`logging` | 
`remote_base_log_folder` | 
| 
|

| 
2.7.3 | 
`logging` | 
`remote_log_conn_id` | 
| 
|

| 
2.7.3 | 
`logging` | 
`remote_logging` | 
| 
|

| 
2.7.3 | 
`logging` | 
`task_log_reader` | 
| 
|

| 
2.7.3 | 
`logging` | 
`log_format` | 
| 
|

| 
2.7.3 | 
`api` | 
`google_oauth2_audience` | 
| 
|



### Blocked configurations in Airflow 2.6.3



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.6.3 | 
`cli` | 
All configuration options | 
|

| 
2.6.3 | 
`kubernetes` | 
`pod_template_file` | 
|

| 
2.6.3 | 
`kubernetes` | 
`namespace` | 
|

| 
2.6.3 | 
`kubernetes_executor` | 
`pod_template_file` | 
|

| 
2.6.3 | 
`kubernetes_executor` | 
`namespace` | 
|

| 
2.6.3 | 
`celery` | 
`celery_app_name` | 
|

| 
2.6.3 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.6.3 | 
`celery` | 
`broker_url` | 
|

| 
2.6.3 | 
`celery` | 
`result_backend` | 
|

| 
2.6.3 | 
`celery` | 
`pool` | 
|

| 
2.6.3 | 
`celery` | 
`default_queue` | 
|

| 
2.6.3 | 
`operators` | 
`default_queue` | 
|

| 
2.6.3 | 
`core` | 
`dags_folder` | 
|

| 
2.6.3 | 
`core` | 
`fernet_key` | 
|

| 
2.6.3 | 
`core` | 
`plugins_folder` | 
|

| 
2.6.3 | 
`core` | 
`security` | 
|

| 
2.6.3 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.6.3 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.6.3 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.6.3 | 
`core` | 
`load_examples` | 
|

| 
2.6.3 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.6.3 | 
`core` | 
`store_dag_code` | 
|

| 
2.6.3 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.6.3 | 
`core` | 
`base_log_folder` | 
|

| 
2.6.3 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.6.3 | 
`core` | 
`logging_config_class` | 
|

| 
2.6.3 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.6.3 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.6.3 | 
`core` | 
`remote_logging` | 
|

| 
2.6.3 | 
`core` | 
`task_log_reader` | 
|

| 
2.6.3 | 
`core` | 
`log_format` | 
|

| 
2.6.3 | 
`database` | 
`sql_alchemy_conn` | 
|

| 
2.6.3 | 
`database` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.6.3 | 
`database` | 
`sql_alchemy_pool_size` | 
|

| 
2.6.3 | 
`smtp` | 
`smtp_password` | 
|

| 
2.6.3 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.6.3 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.6.3 | 
`scheduler` | 
`enable_health_check` | 
|

| 
2.6.3 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
|

| 
2.6.3 | 
`scheduler` | 
`standalone_dag_processor` | 
|

| 
2.6.3 | 
`webserver` | 
`access_logfile` | 
|

| 
2.6.3 | 
`webserver` | 
`base_url` | 
|

| 
2.6.3 | 
`webserver` | 
`error_logfile` | 
|

| 
2.6.3 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.6.3 | 
`webserver` | 
`secret_key` | 
|

| 
2.6.3 | 
`webserver` | 
`web_server_host` | 
|

| 
2.6.3 | 
`webserver` | 
`web_server_port` | 
|

| 
2.6.3 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.6.3 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.6.3 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.6.3 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.6.3 | 
`logging` | 
`base_log_folder` | 
|

| 
2.6.3 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.6.3 | 
`logging` | 
`logging_config_class` | 
|

| 
2.6.3 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.6.3 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.6.3 | 
`logging` | 
`remote_logging` | 
|

| 
2.6.3 | 
`logging` | 
`task_log_reader` | 
|

| 
2.6.3 | 
`logging` | 
`log_format` | 
|

| 
2.6.3 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.5.3



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.5.3 | 
`cli` | 
All configuration options | 
|

| 
2.5.3 | 
`kubernetes` | 
`pod_template_file` | 
|

| 
2.5.3 | 
`kubernetes` | 
`namespace` | 
|

| 
2.5.3 | 
`kubernetes_executor` | 
`pod_template_file` | 
|

| 
2.5.3 | 
`kubernetes_executor` | 
`namespace` | 
|

| 
2.5.3 | 
`celery` | 
`celery_app_name` | 
|

| 
2.5.3 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.5.3 | 
`celery` | 
`broker_url` | 
|

| 
2.5.3 | 
`celery` | 
`result_backend` | 
|

| 
2.5.3 | 
`celery` | 
`pool` | 
|

| 
2.5.3 | 
`celery` | 
`default_queue` | 
|

| 
2.5.3 | 
`operators` | 
`default_queue` | 
|

| 
2.5.3 | 
`core` | 
`dags_folder` | 
|

| 
2.5.3 | 
`core` | 
`fernet_key` | 
|

| 
2.5.3 | 
`core` | 
`plugins_folder` | 
|

| 
2.5.3 | 
`core` | 
`security` | 
|

| 
2.5.3 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.5.3 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.5.3 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.5.3 | 
`core` | 
`load_examples` | 
|

| 
2.5.3 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.5.3 | 
`core` | 
`store_dag_code` | 
|

| 
2.5.3 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.5.3 | 
`core` | 
`base_log_folder` | 
|

| 
2.5.3 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.5.3 | 
`core` | 
`logging_config_class` | 
|

| 
2.5.3 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.5.3 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.5.3 | 
`core` | 
`remote_logging` | 
|

| 
2.5.3 | 
`core` | 
`task_log_reader` | 
|

| 
2.5.3 | 
`core` | 
`log_format` | 
|

| 
2.5.3 | 
`database` | 
`sql_alchemy_conn` | 
|

| 
2.5.3 | 
`database` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.5.3 | 
`database` | 
`sql_alchemy_pool_size` | 
|

| 
2.5.3 | 
`smtp` | 
`smtp_password` | 
|

| 
2.5.3 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.5.3 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.5.3 | 
`scheduler` | 
`enable_health_check` | 
|

| 
2.5.3 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
|

| 
2.5.3 | 
`scheduler` | 
`standalone_dag_processor` | 
|

| 
2.5.3 | 
`webserver` | 
`access_logfile` | 
|

| 
2.5.3 | 
`webserver` | 
`base_url` | 
|

| 
2.5.3 | 
`webserver` | 
`error_logfile` | 
|

| 
2.5.3 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.5.3 | 
`webserver` | 
`secret_key` | 
|

| 
2.5.3 | 
`webserver` | 
`web_server_host` | 
|

| 
2.5.3 | 
`webserver` | 
`web_server_port` | 
|

| 
2.5.3 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.5.3 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.5.3 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.5.3 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.5.3 | 
`logging` | 
`base_log_folder` | 
|

| 
2.5.3 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.5.3 | 
`logging` | 
`logging_config_class` | 
|

| 
2.5.3 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.5.3 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.5.3 | 
`logging` | 
`remote_logging` | 
|

| 
2.5.3 | 
`logging` | 
`task_log_reader` | 
|

| 
2.5.3 | 
`logging` | 
`log_format` | 
|

| 
2.5.3 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.5.1



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.5.1 | 
`cli` | 
All configuration options | 
|

| 
2.5.1 | 
`kubernetes` | 
`pod_template_file` | 
|

| 
2.5.1 | 
`kubernetes` | 
`namespace` | 
|

| 
2.5.1 | 
`celery` | 
`celery_app_name` | 
|

| 
2.5.1 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.5.1 | 
`celery` | 
`broker_url` | 
|

| 
2.5.1 | 
`celery` | 
`result_backend` | 
|

| 
2.5.1 | 
`celery` | 
`pool` | 
|

| 
2.5.1 | 
`celery` | 
`default_queue` | 
|

| 
2.5.1 | 
`operators` | 
`default_queue` | 
|

| 
2.5.1 | 
`core` | 
`dags_folder` | 
|

| 
2.5.1 | 
`core` | 
`fernet_key` | 
|

| 
2.5.1 | 
`core` | 
`plugins_folder` | 
|

| 
2.5.1 | 
`core` | 
`security` | 
|

| 
2.5.1 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.5.1 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.5.1 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.5.1 | 
`core` | 
`load_examples` | 
|

| 
2.5.1 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.5.1 | 
`core` | 
`store_dag_code` | 
|

| 
2.5.1 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.5.1 | 
`core` | 
`base_log_folder` | 
|

| 
2.5.1 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.5.1 | 
`core` | 
`logging_config_class` | 
|

| 
2.5.1 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.5.1 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.5.1 | 
`core` | 
`remote_logging` | 
|

| 
2.5.1 | 
`core` | 
`task_log_reader` | 
|

| 
2.5.1 | 
`core` | 
`log_format` | 
|

| 
2.5.1 | 
`database` | 
`sql_alchemy_conn` | 
|

| 
2.5.1 | 
`database` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.5.1 | 
`database` | 
`sql_alchemy_pool_size` | 
|

| 
2.5.1 | 
`smtp` | 
`smtp_password` | 
|

| 
2.5.1 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.5.1 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.5.1 | 
`scheduler` | 
`enable_health_check` | 
|

| 
2.5.1 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
|

| 
2.5.1 | 
`scheduler` | 
`standalone_dag_processor` | 
|

| 
2.5.1 | 
`webserver` | 
`access_logfile` | 
|

| 
2.5.1 | 
`webserver` | 
`base_url` | 
|

| 
2.5.1 | 
`webserver` | 
`error_logfile` | 
|

| 
2.5.1 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.5.1 | 
`webserver` | 
`secret_key` | 
|

| 
2.5.1 | 
`webserver` | 
`web_server_host` | 
|

| 
2.5.1 | 
`webserver` | 
`web_server_port` | 
|

| 
2.5.1 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.5.1 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.5.1 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.5.1 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.5.1 | 
`logging` | 
`base_log_folder` | 
|

| 
2.5.1 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.5.1 | 
`logging` | 
`logging_config_class` | 
|

| 
2.5.1 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.5.1 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.5.1 | 
`logging` | 
`remote_logging` | 
|

| 
2.5.1 | 
`logging` | 
`task_log_reader` | 
|

| 
2.5.1 | 
`logging` | 
`log_format` | 
|

| 
2.5.1 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.4.3



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.4.3 | 
`cli` | 
All configuration options | 
|

| 
2.4.3 | 
`kubernetes` | 
`pod_template_file` | 
|

| 
2.4.3 | 
`kubernetes` | 
`namespace` | 
|

| 
2.4.3 | 
`celery` | 
`celery_app_name` | 
|

| 
2.4.3 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.4.3 | 
`celery` | 
`broker_url` | 
|

| 
2.4.3 | 
`celery` | 
`result_backend` | 
|

| 
2.4.3 | 
`celery` | 
`pool` | 
|

| 
2.4.3 | 
`celery` | 
`default_queue` | 
|

| 
2.4.3 | 
`operators` | 
`default_queue` | 
|

| 
2.4.3 | 
`core` | 
`dags_folder` | 
|

| 
2.4.3 | 
`core` | 
`fernet_key` | 
|

| 
2.4.3 | 
`core` | 
`plugins_folder` | 
|

| 
2.4.3 | 
`core` | 
`security` | 
|

| 
2.4.3 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.4.3 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.4.3 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.4.3 | 
`core` | 
`load_examples` | 
|

| 
2.4.3 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.4.3 | 
`core` | 
`store_dag_code` | 
|

| 
2.4.3 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.4.3 | 
`core` | 
`base_log_folder` | 
|

| 
2.4.3 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.4.3 | 
`core` | 
`logging_config_class` | 
|

| 
2.4.3 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.4.3 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.4.3 | 
`core` | 
`remote_logging` | 
|

| 
2.4.3 | 
`core` | 
`task_log_reader` | 
|

| 
2.4.3 | 
`core` | 
`log_format` | 
|

| 
2.4.3 | 
`database` | 
`sql_alchemy_conn` | 
|

| 
2.4.3 | 
`database` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.4.3 | 
`database` | 
`sql_alchemy_pool_size` | 
|

| 
2.4.3 | 
`smtp` | 
`smtp_password` | 
|

| 
2.4.3 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.4.3 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.4.3 | 
`scheduler` | 
`enable_health_check` | 
|

| 
2.4.3 | 
`scheduler` | 
`scheduler_health_check_server_port` | 
|

| 
2.4.3 | 
`scheduler` | 
`standalone_dag_processor` | 
|

| 
2.4.3 | 
`webserver` | 
`access_logfile` | 
|

| 
2.4.3 | 
`webserver` | 
`base_url` | 
|

| 
2.4.3 | 
`webserver` | 
`error_logfile` | 
|

| 
2.4.3 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.4.3 | 
`webserver` | 
`secret_key` | 
|

| 
2.4.3 | 
`webserver` | 
`web_server_host` | 
|

| 
2.4.3 | 
`webserver` | 
`web_server_port` | 
|

| 
2.4.3 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.4.3 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.4.3 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.4.3 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.4.3 | 
`logging` | 
`base_log_folder` | 
|

| 
2.4.3 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.4.3 | 
`logging` | 
`logging_config_class` | 
|

| 
2.4.3 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.4.3 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.4.3 | 
`logging` | 
`remote_logging` | 
|

| 
2.4.3 | 
`logging` | 
`task_log_reader` | 
|

| 
2.4.3 | 
`logging` | 
`log_format` | 
|

| 
2.4.3 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.3.4



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.3.4 | 
`cli` | 
All configuration options | 
|

| 
2.3.4 | 
`kubernetes` | 
`pod_template_file` | 
|

| 
2.3.4 | 
`kubernetes` | 
`namespace` | 
|

| 
2.3.4 | 
`celery` | 
`celery_app_name` | 
|

| 
2.3.4 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.3.4 | 
`celery` | 
`broker_url` | 
|

| 
2.3.4 | 
`celery` | 
`result_backend` | 
|

| 
2.3.4 | 
`celery` | 
`pool` | 
|

| 
2.3.4 | 
`celery` | 
`default_queue` | 
|

| 
2.3.4 | 
`operators` | 
`default_queue` | 
|

| 
2.3.4 | 
`core` | 
`dags_folder` | 
|

| 
2.3.4 | 
`core` | 
`fernet_key` | 
|

| 
2.3.4 | 
`core` | 
`plugins_folder` | 
|

| 
2.3.4 | 
`core` | 
`security` | 
|

| 
2.3.4 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.3.4 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.3.4 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.3.4 | 
`core` | 
`load_examples` | 
|

| 
2.3.4 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.3.4 | 
`core` | 
`store_dag_code` | 
|

| 
2.3.4 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.3.4 | 
`core` | 
`base_log_folder` | 
|

| 
2.3.4 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.3.4 | 
`core` | 
`logging_config_class` | 
|

| 
2.3.4 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.3.4 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.3.4 | 
`core` | 
`remote_logging` | 
|

| 
2.3.4 | 
`core` | 
`task_log_reader` | 
|

| 
2.3.4 | 
`core` | 
`log_format` | 
|

| 
2.3.4 | 
`database` | 
`sql_alchemy_conn` | 
|

| 
2.3.4 | 
`database` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.3.4 | 
`database` | 
`sql_alchemy_pool_size` | 
|

| 
2.3.4 | 
`smtp` | 
`smtp_password` | 
|

| 
2.3.4 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.3.4 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.3.4 | 
`scheduler` | 
`standalone_dag_processor` | 
|

| 
2.3.4 | 
`webserver` | 
`access_logfile` | 
|

| 
2.3.4 | 
`webserver` | 
`base_url` | 
|

| 
2.3.4 | 
`webserver` | 
`error_logfile` | 
|

| 
2.3.4 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.3.4 | 
`webserver` | 
`secret_key` | 
|

| 
2.3.4 | 
`webserver` | 
`web_server_host` | 
|

| 
2.3.4 | 
`webserver` | 
`web_server_port` | 
|

| 
2.3.4 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.3.4 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.3.4 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.3.4 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.3.4 | 
`logging` | 
`base_log_folder` | 
|

| 
2.3.4 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.3.4 | 
`logging` | 
`logging_config_class` | 
|

| 
2.3.4 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.3.4 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.3.4 | 
`logging` | 
`remote_logging` | 
|

| 
2.3.4 | 
`logging` | 
`task_log_reader` | 
|

| 
2.3.4 | 
`logging` | 
`log_format` | 
|

| 
2.3.4 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.3.3



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.3.3 | 
`cli` | 
All configuration options | 
|

| 
2.3.3 | 
`kubernetes` | 
`pod_template_file` | 
|

| 
2.3.3 | 
`kubernetes` | 
`namespace` | 
|

| 
2.3.3 | 
`celery` | 
`celery_app_name` | 
|

| 
2.3.3 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.3.3 | 
`celery` | 
`broker_url` | 
|

| 
2.3.3 | 
`celery` | 
`result_backend` | 
|

| 
2.3.3 | 
`celery` | 
`pool` | 
|

| 
2.3.3 | 
`celery` | 
`default_queue` | 
|

| 
2.3.3 | 
`operators` | 
`default_queue` | 
|

| 
2.3.3 | 
`core` | 
`dags_folder` | 
|

| 
2.3.3 | 
`core` | 
`fernet_key` | 
|

| 
2.3.3 | 
`core` | 
`plugins_folder` | 
|

| 
2.3.3 | 
`core` | 
`security` | 
|

| 
2.3.3 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.3.3 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.3.3 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.3.3 | 
`core` | 
`load_examples` | 
|

| 
2.3.3 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.3.3 | 
`core` | 
`store_dag_code` | 
|

| 
2.3.3 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.3.3 | 
`core` | 
`base_log_folder` | 
|

| 
2.3.3 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.3.3 | 
`core` | 
`logging_config_class` | 
|

| 
2.3.3 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.3.3 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.3.3 | 
`core` | 
`remote_logging` | 
|

| 
2.3.3 | 
`core` | 
`task_log_reader` | 
|

| 
2.3.3 | 
`core` | 
`log_format` | 
|

| 
2.3.3 | 
`database` | 
`sql_alchemy_conn` | 
|

| 
2.3.3 | 
`database` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.3.3 | 
`database` | 
`sql_alchemy_pool_size` | 
|

| 
2.3.3 | 
`smtp` | 
`smtp_password` | 
|

| 
2.3.3 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.3.3 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.3.3 | 
`webserver` | 
`access_logfile` | 
|

| 
2.3.3 | 
`webserver` | 
`base_url` | 
|

| 
2.3.3 | 
`webserver` | 
`error_logfile` | 
|

| 
2.3.3 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.3.3 | 
`webserver` | 
`secret_key` | 
|

| 
2.3.3 | 
`webserver` | 
`web_server_host` | 
|

| 
2.3.3 | 
`webserver` | 
`web_server_port` | 
|

| 
2.3.3 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.3.3 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.3.3 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.3.3 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.3.3 | 
`logging` | 
`base_log_folder` | 
|

| 
2.3.3 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.3.3 | 
`logging` | 
`logging_config_class` | 
|

| 
2.3.3 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.3.3 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.3.3 | 
`logging` | 
`remote_logging` | 
|

| 
2.3.3 | 
`logging` | 
`task_log_reader` | 
|

| 
2.3.3 | 
`logging` | 
`log_format` | 
|

| 
2.3.3 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.2.5



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.2.5 | 
`cli` | 
All configuration options | 
|

| 
2.2.5 | 
`kubernetes` | 
`pod_template_file` | 
|

| 
2.2.5 | 
`kubernetes` | 
`namespace` | 
|

| 
2.2.5 | 
`celery` | 
`celery_app_name` | 
|

| 
2.2.5 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.2.5 | 
`celery` | 
`broker_url` | 
|

| 
2.2.5 | 
`celery` | 
`result_backend` | 
|

| 
2.2.5 | 
`celery` | 
`pool` | 
|

| 
2.2.5 | 
`celery` | 
`default_queue` | 
|

| 
2.2.5 | 
`operators` | 
`default_queue` | 
|

| 
2.2.5 | 
`core` | 
`dags_folder` | 
|

| 
2.2.5 | 
`core` | 
`fernet_key` | 
|

| 
2.2.5 | 
`core` | 
`plugins_folder` | 
|

| 
2.2.5 | 
`core` | 
`security` | 
|

| 
2.2.5 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.2.5 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.2.5 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.2.5 | 
`core` | 
`load_examples` | 
|

| 
2.2.5 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.2.5 | 
`core` | 
`store_dag_code` | 
|

| 
2.2.5 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.2.5 | 
`core` | 
`base_log_folder` | 
|

| 
2.2.5 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.2.5 | 
`core` | 
`logging_config_class` | 
|

| 
2.2.5 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.2.5 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.2.5 | 
`core` | 
`remote_logging` | 
|

| 
2.2.5 | 
`core` | 
`task_log_reader` | 
|

| 
2.2.5 | 
`core` | 
`log_format` | 
|

| 
2.2.5 | 
`smtp` | 
`smtp_password` | 
|

| 
2.2.5 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.2.5 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.2.5 | 
`webserver` | 
`access_logfile` | 
|

| 
2.2.5 | 
`webserver` | 
`base_url` | 
|

| 
2.2.5 | 
`webserver` | 
`error_logfile` | 
|

| 
2.2.5 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.2.5 | 
`webserver` | 
`secret_key` | 
|

| 
2.2.5 | 
`webserver` | 
`web_server_host` | 
|

| 
2.2.5 | 
`webserver` | 
`web_server_port` | 
|

| 
2.2.5 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.2.5 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.2.5 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.2.5 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.2.5 | 
`logging` | 
`base_log_folder` | 
|

| 
2.2.5 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.2.5 | 
`logging` | 
`logging_config_class` | 
|

| 
2.2.5 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.2.5 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.2.5 | 
`logging` | 
`remote_logging` | 
|

| 
2.2.5 | 
`logging` | 
`task_log_reader` | 
|

| 
2.2.5 | 
`logging` | 
`log_format` | 
|

| 
2.2.5 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.2.3



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.2.3 | 
`cli` | 
All configuration options | 
|

| 
2.2.3 | 
`kubernetes` | 
`pod_template_file` | 
|

| 
2.2.3 | 
`kubernetes` | 
`namespace` | 
|

| 
2.2.3 | 
`celery` | 
`celery_app_name` | 
|

| 
2.2.3 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.2.3 | 
`celery` | 
`broker_url` | 
|

| 
2.2.3 | 
`celery` | 
`result_backend` | 
|

| 
2.2.3 | 
`celery` | 
`pool` | 
|

| 
2.2.3 | 
`celery` | 
`default_queue` | 
|

| 
2.2.3 | 
`operators` | 
`default_queue` | 
|

| 
2.2.3 | 
`core` | 
`dags_folder` | 
|

| 
2.2.3 | 
`core` | 
`fernet_key` | 
|

| 
2.2.3 | 
`core` | 
`plugins_folder` | 
|

| 
2.2.3 | 
`core` | 
`security` | 
|

| 
2.2.3 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.2.3 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.2.3 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.2.3 | 
`core` | 
`load_examples` | 
|

| 
2.2.3 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.2.3 | 
`core` | 
`store_dag_code` | 
|

| 
2.2.3 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.2.3 | 
`core` | 
`base_log_folder` | 
|

| 
2.2.3 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.2.3 | 
`core` | 
`logging_config_class` | 
|

| 
2.2.3 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.2.3 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.2.3 | 
`core` | 
`remote_logging` | 
|

| 
2.2.3 | 
`core` | 
`task_log_reader` | 
|

| 
2.2.3 | 
`core` | 
`log_format` | 
|

| 
2.2.3 | 
`smtp` | 
`smtp_password` | 
|

| 
2.2.3 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.2.3 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.2.3 | 
`webserver` | 
`access_logfile` | 
|

| 
2.2.3 | 
`webserver` | 
`base_url` | 
|

| 
2.2.3 | 
`webserver` | 
`error_logfile` | 
|

| 
2.2.3 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.2.3 | 
`webserver` | 
`secret_key` | 
|

| 
2.2.3 | 
`webserver` | 
`web_server_host` | 
|

| 
2.2.3 | 
`webserver` | 
`web_server_port` | 
|

| 
2.2.3 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.2.3 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.2.3 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.2.3 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.2.3 | 
`logging` | 
`base_log_folder` | 
|

| 
2.2.3 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.2.3 | 
`logging` | 
`logging_config_class` | 
|

| 
2.2.3 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.2.3 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.2.3 | 
`logging` | 
`remote_logging` | 
|

| 
2.2.3 | 
`logging` | 
`task_log_reader` | 
|

| 
2.2.3 | 
`logging` | 
`log_format` | 
|

| 
2.2.3 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.1.4



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.1.4 | 
`cli` | 
All configuration options | 
|

| 
2.1.4 | 
`celery` | 
`celery_app_name` | 
|

| 
2.1.4 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.1.4 | 
`celery` | 
`broker_url` | 
|

| 
2.1.4 | 
`celery` | 
`result_backend` | 
|

| 
2.1.4 | 
`celery` | 
`pool` | 
|

| 
2.1.4 | 
`celery` | 
`default_queue` | 
|

| 
2.1.4 | 
`operators` | 
`default_queue` | 
|

| 
2.1.4 | 
`core` | 
`dags_folder` | 
|

| 
2.1.4 | 
`core` | 
`fernet_key` | 
|

| 
2.1.4 | 
`core` | 
`plugins_folder` | 
|

| 
2.1.4 | 
`core` | 
`security` | 
|

| 
2.1.4 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.1.4 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.1.4 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.1.4 | 
`core` | 
`load_examples` | 
|

| 
2.1.4 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.1.4 | 
`core` | 
`store_dag_code` | 
|

| 
2.1.4 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.1.4 | 
`core` | 
`base_log_folder` | 
|

| 
2.1.4 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.1.4 | 
`core` | 
`logging_config_class` | 
|

| 
2.1.4 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.1.4 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.1.4 | 
`core` | 
`remote_logging` | 
|

| 
2.1.4 | 
`core` | 
`task_log_reader` | 
|

| 
2.1.4 | 
`core` | 
`log_format` | 
|

| 
2.1.4 | 
`smtp` | 
`smtp_password` | 
|

| 
2.1.4 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.1.4 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.1.4 | 
`webserver` | 
`access_logfile` | 
|

| 
2.1.4 | 
`webserver` | 
`base_url` | 
|

| 
2.1.4 | 
`webserver` | 
`error_logfile` | 
|

| 
2.1.4 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.1.4 | 
`webserver` | 
`secret_key` | 
|

| 
2.1.4 | 
`webserver` | 
`web_server_host` | 
|

| 
2.1.4 | 
`webserver` | 
`web_server_port` | 
|

| 
2.1.4 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.1.4 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.1.4 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.1.4 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.1.4 | 
`logging` | 
`base_log_folder` | 
|

| 
2.1.4 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.1.4 | 
`logging` | 
`logging_config_class` | 
|

| 
2.1.4 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.1.4 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.1.4 | 
`logging` | 
`remote_logging` | 
|

| 
2.1.4 | 
`logging` | 
`task_log_reader` | 
|

| 
2.1.4 | 
`logging` | 
`log_format` | 
|

| 
2.1.4 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.1.2



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.1.2 | 
`cli` | 
All configuration options | 
|

| 
2.1.2 | 
`celery` | 
`celery_app_name` | 
|

| 
2.1.2 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.1.2 | 
`celery` | 
`broker_url` | 
|

| 
2.1.2 | 
`celery` | 
`result_backend` | 
|

| 
2.1.2 | 
`celery` | 
`pool` | 
|

| 
2.1.2 | 
`celery` | 
`default_queue` | 
|

| 
2.1.2 | 
`operators` | 
`default_queue` | 
|

| 
2.1.2 | 
`core` | 
`dags_folder` | 
|

| 
2.1.2 | 
`core` | 
`executor` | 
|

| 
2.1.2 | 
`core` | 
`fernet_key` | 
|

| 
2.1.2 | 
`core` | 
`plugins_folder` | 
|

| 
2.1.2 | 
`core` | 
`security` | 
|

| 
2.1.2 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.1.2 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.1.2 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.1.2 | 
`core` | 
`load_examples` | 
|

| 
2.1.2 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.1.2 | 
`core` | 
`store_dag_code` | 
|

| 
2.1.2 | 
`core` | 
`base_log_folder` | 
|

| 
2.1.2 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.1.2 | 
`core` | 
`logging_config_class` | 
|

| 
2.1.2 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.1.2 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.1.2 | 
`core` | 
`remote_logging` | 
|

| 
2.1.2 | 
`core` | 
`task_log_reader` | 
|

| 
2.1.2 | 
`smtp` | 
`smtp_password` | 
|

| 
2.1.2 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.1.2 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.1.2 | 
`webserver` | 
`access_logfile` | 
|

| 
2.1.2 | 
`webserver` | 
`base_url` | 
|

| 
2.1.2 | 
`webserver` | 
`error_logfile` | 
|

| 
2.1.2 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.1.2 | 
`webserver` | 
`secret_key` | 
|

| 
2.1.2 | 
`webserver` | 
`web_server_host` | 
|

| 
2.1.2 | 
`webserver` | 
`web_server_port` | 
|

| 
2.1.2 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.1.2 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.1.2 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.1.2 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.1.2 | 
`webserver` | 
`rbac_autoregister_per_folder_roles` | 
|

| 
2.1.2 | 
`logging` | 
`base_log_folder` | 
|

| 
2.1.2 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.1.2 | 
`logging` | 
`logging_config_class` | 
|

| 
2.1.2 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.1.2 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.1.2 | 
`logging` | 
`remote_logging` | 
|

| 
2.1.2 | 
`logging` | 
`task_log_reader` | 
|

| 
2.1.2 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.1.1



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.1.1 | 
`cli` | 
All configuration options | 
|

| 
2.1.1 | 
`celery` | 
`celery_app_name` | 
|

| 
2.1.1 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.1.1 | 
`celery` | 
`broker_url` | 
|

| 
2.1.1 | 
`celery` | 
`result_backend` | 
|

| 
2.1.1 | 
`celery` | 
`pool` | 
|

| 
2.1.1 | 
`celery` | 
`default_queue` | 
|

| 
2.1.1 | 
`operators` | 
`default_queue` | 
|

| 
2.1.1 | 
`core` | 
`dags_folder` | 
|

| 
2.1.1 | 
`core` | 
`executor` | 
|

| 
2.1.1 | 
`core` | 
`fernet_key` | 
|

| 
2.1.1 | 
`core` | 
`plugins_folder` | 
|

| 
2.1.1 | 
`core` | 
`security` | 
|

| 
2.1.1 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.1.1 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.1.1 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.1.1 | 
`core` | 
`load_examples` | 
|

| 
2.1.1 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.1.1 | 
`core` | 
`store_dag_code` | 
|

| 
2.1.1 | 
`core` | 
`base_log_folder` | 
|

| 
2.1.1 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
2.1.1 | 
`core` | 
`logging_config_class` | 
|

| 
2.1.1 | 
`core` | 
`remote_base_log_folder` | 
|

| 
2.1.1 | 
`core` | 
`remote_log_conn_id` | 
|

| 
2.1.1 | 
`core` | 
`remote_logging` | 
|

| 
2.1.1 | 
`core` | 
`task_log_reader` | 
|

| 
2.1.1 | 
`smtp` | 
`smtp_password` | 
|

| 
2.1.1 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.1.1 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.1.1 | 
`webserver` | 
`access_logfile` | 
|

| 
2.1.1 | 
`webserver` | 
`base_url` | 
|

| 
2.1.1 | 
`webserver` | 
`error_logfile` | 
|

| 
2.1.1 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.1.1 | 
`webserver` | 
`secret_key` | 
|

| 
2.1.1 | 
`webserver` | 
`web_server_host` | 
|

| 
2.1.1 | 
`webserver` | 
`web_server_port` | 
|

| 
2.1.1 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.1.1 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.1.1 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.1.1 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.1.1 | 
`webserver` | 
`rbac_autoregister_per_folder_roles` | 
|

| 
2.1.1 | 
`logging` | 
`base_log_folder` | 
|

| 
2.1.1 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.1.1 | 
`logging` | 
`logging_config_class` | 
|

| 
2.1.1 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.1.1 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.1.1 | 
`logging` | 
`remote_logging` | 
|

| 
2.1.1 | 
`logging` | 
`task_log_reader` | 
|

| 
2.1.1 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 2.0.2, 2.0.1, 2.0.0



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
2.0.2, 2.0.1, 2.0.0 | 
`cli` | 
All configuration options | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`celery` | 
`celery_app_name` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`celery` | 
`worker_log_server_port` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`celery` | 
`broker_url` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`celery` | 
`result_backend` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`celery` | 
`default_queue` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`celery` | 
`pool` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`dags_folder` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`executor` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`fernet_key` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`plugins_folder` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`security` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`load_examples` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`store_serialized_dags` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`core` | 
`store_dag_code` | 
|

| 
2.0.2 | 
`core` | 
`wait_dag_not_found_timeout` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`smtp` | 
`smtp_password` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`access_logfile` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`base_url` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`error_logfile` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`secret_key` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`web_server_host` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`web_server_port` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`worker_refresh_batch_size` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`webserver` | 
`rbac_autoregister_per_folder_roles` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`logging` | 
`base_log_folder` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`logging` | 
`encrypt_s3_logs` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`logging` | 
`logging_config_class` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`logging` | 
`remote_base_log_folder` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`logging` | 
`remote_log_conn_id` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`logging` | 
`remote_logging` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`logging` | 
`task_log_reader` | 
|

| 
2.0.2 | 
`logging` | 
`log_format` | 
|

| 
2.0.2, 2.0.1, 2.0.0 | 
`api` | 
`google_oauth2_audience` | 
|



### Blocked configurations in Airflow 1.10.15, 1.10.14, 1.10.12



| 
Airflow version | 
Section | 
Configuration option | 
|




| 
1.10.15, 1.10.14, 1.10.12 | 
`cli` | 
All configuration options | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`celery` | 
`celery_app_name` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`celery` | 
`worker_log_server_port` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`celery` | 
`broker_url` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`celery` | 
`celery_result_backend` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`celery` | 
`result_backend` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`celery` | 
`default_queue` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`celery` | 
`pool` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`airflow_home` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`base_log_folder` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`dags_folder` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`encrypt_s3_logs` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`executor` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`fernet_key` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`logging_config_class` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`plugins_folder` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`remote_base_log_folder` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`remote_log_conn_id` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`remote_logging` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`security` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`sql_alchemy_conn` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`sql_alchemy_pool_recycle` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`sql_alchemy_pool_size` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`task_log_reader` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`core` | 
`load_examples` | 
|

| 
1.10.15 | 
`core` | 
`log_format` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`smtp` | 
`smtp_password` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`scheduler` | 
`authenticate` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`scheduler` | 
`auth_backend` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`scheduler` | 
`child_process_log_directory` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`scheduler` | 
`print_stats_interval` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`access_logfile` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`authenticate` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`auth_backend` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`base_url` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`error_logfile` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`filter_by_owner` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`google_oauth2_audience` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`log_fetch_timeout_sec` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`owner_mode` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`secret_key` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`web_server_host` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`web_server_port` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`web_server_ssl_cert` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`web_server_ssl_key` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`web_server_worker_timeout` | 
|

| 
1.10.15, 1.10.14, 1.10.12 | 
`webserver` | 
`worker_refresh_batch_size` | 
|



## What's next

- [Managed Airflow versions](/composer/docs/composer-versions)

- [Overriding Airflow configurations](/composer/docs/composer-2/override-airflow-configurations)