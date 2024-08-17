from concurrent.futures import ThreadPoolExecutor

from time import sleep # used to simulate waiting on a task

import requests
# Example to process

def long_api_call(currencyId: str):

    url = f"https://api.exchange.coinbase.com/currencies/{currencyId}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    return currencyId, response['status']

if __name__ == '__main__':

    x, y = long_api_call("ADA")

    print(x, y)

