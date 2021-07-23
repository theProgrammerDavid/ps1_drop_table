from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from webscraper import MyCrawler

CRAWL_URL = "https://www.bajajfinserv.in/"

def startCrawler():
    crawler = MyCrawler(CRAWL_URL)
    crawler.start_crawling(threshold=10)
    

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
	process_data = BashOperator(task_id='process_data', bash_command='sleep 5')
	dump_csv = BashOperator(task_id='dump_csv', bash_command='echo "Hello David"')
	db_insert = BashOperator(task_id='db_insert', bash_command='echo "Hello David"')
	search_engine_recache = BashOperator(task_id='search_engine_recache', bash_command='echo "Engine Recache"')

	start_crawler >> process_data >> dump_csv >> db_insert >> search_engine_recache



