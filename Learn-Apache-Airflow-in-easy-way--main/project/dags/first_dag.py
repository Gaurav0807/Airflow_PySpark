from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from datetime import time, timedelta
dag = DAG(
    dag_id="helloworld",
    schedule_interval='@daily',
    start_date=days_ago(1)
)
task1 = BashOperator(
    task_id = 't1',
    bash_command='{{var.value.keyVariable}}',
    ##bash_command = 'echo hello && exit 1', ##upstream
    dag = dag,  
    retries = 3
)
task2 = BashOperator(
    task_id = 't2',
    bash_command = 'echo t2',
    dag = dag
)
task3 = BashOperator(
    task_id = 't3',
    bash_command = 'echo t3',
    dag = dag,
    trigger_rule = 'all_failed'
)
task1 >> [task2, task3]  ##execute task in order precedence