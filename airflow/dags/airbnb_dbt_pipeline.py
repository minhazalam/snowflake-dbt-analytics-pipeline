from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

from alerts.slack import notify_slack

with DAG(
    dag_id="airbnb_dbt_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    on_failure_callback=notify_slack,
) as dag:

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="""
        cd /opt/airflow/project &&
        dbt run
        """
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
        cd /opt/airflow/project &&
        dbt test
        """
    )

    dbt_run >> dbt_test
