from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

dag = DAG(
    dag_id="helloworld_dag",
    schedule_interval='@daily',
    start_date=days_ago(1)
)

task1 = BashOperator(task_id = 't1', bash_command='eacho hello', dag = dag)