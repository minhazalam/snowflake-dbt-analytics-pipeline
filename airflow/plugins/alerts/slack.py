import os
import requests


def notify_slack(context):
    """
    Generic Slack failure notification for Airflow tasks.
    Can be reused across DAGs via on_failure_callback.
    """

    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        # Fail silently if webhook is not configured
        return

    ti = context.get("task_instance")
    dag = context.get("dag")

    dag_id = dag.dag_id if dag else "unknown_dag"
    task_id = ti.task_id if ti else "unknown_task"
    execution_date = context.get("execution_date")
    log_url = ti.log_url if ti else "no_log_url"

    message = {
        "text": (
            ":x: *Airflow Task Failed*\n"
            f"*DAG:* `{dag_id}`\n"
            f"*Task:* `{task_id}`\n"
            f"*Execution:* {execution_date}\n"
            f"*Logs:* {log_url}"
        )
    }

    try:
        requests.post(webhook_url, json=message, timeout=10)
    except Exception as e:
        # Never fail the task because Slack failed
        print(f"Slack notification failed: {e}")
