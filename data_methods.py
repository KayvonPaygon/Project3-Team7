import requests
import json
# retrieve data, graph data, display data methods

# retrieve data from AlphaVantage's open API
def print_pretty(data: dict):
  print(json.dumps(data, indent=4))

api_key = 'M5U4GAA5AW5TD1I1'

def retrieve_data(function: str, symbol: str, api_key: str) -> dict:
  # query from API
  url = f'https://www.alphavantage.co/query?function=(function)&symbol=(symbol)&apikey=(api_key)'
  response = requests.get(url)
  # read output
  data = response.text
  # parse output
  parsed = json.loads(data)

return parsed
# print_pretty(retrieve_data('INCOME_STATEMENT', 'AAPL', api_key))

# graph data


