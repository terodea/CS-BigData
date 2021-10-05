from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

dag = DAG(
    dag_id="helloworld_dag",
    schedule_interval='@daily',
    start_date=days_ago(1)
)

task1 = BashOperator(task_id = 't1', bash_command='eacho hello', dag = dag, retry=3)
task2 = BashOperator(task_id = 't2', bash_command='eacho t2', dag = dag)
task3 = BashOperator(task_id = 't3', bash_command='eacho t3', dag = dag)

task1 >> [task2, task3]