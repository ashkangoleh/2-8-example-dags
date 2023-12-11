"""

"""

from airflow import Dataset
from airflow.decorators import dag, task
from airflow.io.path import ObjectStoragePath
from pendulum import datetime
import requests


URI = "file://include/bears"
MY_DATASET = Dataset(URI)
base_local = ObjectStoragePath(URI)


@dag(
    start_date=datetime(2023, 12, 1),
    schedule=None,
    catchup=False,
    tags=["Listeners"],
)
def producer_dag():
    @task(
        outlets=[MY_DATASET],
    )
    def get_bear(base):
        r = requests.get("https://placebear.com/200/300")
        file_path = base / "bear.jpg"

        if r.status_code == 200:
            base.mkdir(parents=True, exist_ok=True)
            file_path.write_bytes(r.content)
            file_path.replace("bear.jpg")
        else:
            print(f"Failed to retrieve image. Status code: {r.status_code}")

    get_bear(base=base_local)


producer_dag()
