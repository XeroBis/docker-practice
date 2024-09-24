from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import psycopg2

def extract_data():
    conn = psycopg2.connect(
        host="db",
        database="mydatabase",
        user="user",
        password="password"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales;")
    rows = cursor.fetchall()
    conn.close()
    serializable_rows = []
    for row in rows:
        serializable_row = [str(item) for item in row]
        serializable_rows.append(serializable_row)
    
    return serializable_rows

def print_data(ti):
    data = ti.xcom_pull(task_ids='extract_data')
    for row in data:
        print(row)

default_args = {
    'start_date': datetime(2024, 9, 20),
    'schedule_interval': '@daily',
}

with DAG('etl_dag', default_args=default_args, catchup=False) as dag:
    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    print_task = PythonOperator(
        task_id='print_data',
        python_callable=print_data
    )

    extract >> print_task
