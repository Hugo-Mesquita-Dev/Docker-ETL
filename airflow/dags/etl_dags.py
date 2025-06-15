from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spark_etl',
    default_args=default_args,
    schedule_interval='@daily',
)

run_spark = DockerOperator(
    task_id='run_spark_job',
    image='spark-etl',
    api_version='auto',
    auto_remove=True,
    docker_url='unix://var/run/docker.sock',
    network_mode='docker-etl_default',  # Substitua pelo nome da sua rede
    dag=dag,
)