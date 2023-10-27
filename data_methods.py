import requests
import json


def print_pretty(data: dict):
    print(json.dumps(data, indent=4))


def retrieve_data(function: str, symbol: str, api_key: str) -> dict:
    # query from API
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    # read output
    data = response.text
    # parse output
    parsed = json.loads(data)

    return parsed
