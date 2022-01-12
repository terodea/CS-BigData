from os import name
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.models import BaseOperator
from airflow.utils import apply_defaults, trigger_rule
from airflow.sensors.http_sensor import HttpSensor
from datetime import timedelta
dag = DAG(
    dag_id="helloworld_dag",
    schedule_interval='@daily',
    start_date=days_ago(1)
)
class MyOperator(BaseOperator):

    @apply_defaults
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def execute(self, context):
        message = "Hello {}".format(self.name)
        print(message)
        return message

task1 = BashOperator(task_id = 't1', bash_command='eacho hello', dag = dag)
task2 = BashOperator(task_id = 't2', bash_command='eacho t2', dag = dag)
task3 = BashOperator(task_id = 't3', bash_command='eacho t3', dag = dag, trigger_rule='all_failed')
task4 = MyOperator(name = 'Akshay', task_id = 't4', dag=dag, trigger_rule='one_success')

# Create connection id in UI.
sensor = HttpSensor(
    task_id = 'sensor', 
    endpoint='/', 
    http_conn_id='my_httpcon', 
    dag=dag, 
    retires=20, 
    retry_delay=timedelta(seconds=10)
    )

sensor >> task1 >> [task2, task3] >> task4