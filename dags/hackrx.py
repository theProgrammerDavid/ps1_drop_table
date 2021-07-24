from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from webscraper import MyCrawler

CRAWL_URL = "https://www.bajajfinserv.in/"

crawler = MyCrawler(CRAWL_URL)
def startCrawler():
    crawler.start_crawling(threshold=10)
    
def processData():
    crawler.output_result()



dag_args = {
    'owner': 'david velho',
    'depends_on_past': False,
    'start_date': datetime(2021, 7, 22),
    'email': ['davidvelho0603@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=3)}

dag = DAG(
    dag_id='ps1_website_search',
    start_date=datetime(2021, 7, 23),
    default_args=dag_args,
    end_date=None,
    schedule_interval='0 9 * * *')

with dag:
    start_crawler = PythonOperator(
        task_id='start_crawler',
        python_callable=startCrawler,
        op_args=[],
        dag=dag
    )
    process_data = PythonOperator(
        task_id='process_data',
        python_callable=processData,
        op_args=[],
        dag=dag
    )
    search_engine_cache = PythonOperator(
        task_id='search_engine_cache',
        python_callable=crawler.update_engine,
        op_args=[],
        dag=dag
    )
    start_crawler >> process_data >> search_engine_cache
