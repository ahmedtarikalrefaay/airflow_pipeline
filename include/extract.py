import pandas as pd
import requests 
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

csv_path = "/usr/local/airflow/include/data/retail_sales.csv"
api_url = "https://dummyjson.com/products"

def extract_csv_data():
    df = pd.read_csv(csv_path)
    return df

def extract_api():
    session = requests.Session()
    retry =Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504]

    )

    session.mount("https://", HTTPAdapter(max_retries=retry))


    headers ={

        "User-Agent": "Mozilla/5.0"
    }

    responce = session.get(api_url, headers=headers,timeout=20)
    responce.raise_for_status()

    data = responce.json()
    return pd.DataFrame(data["products"])






