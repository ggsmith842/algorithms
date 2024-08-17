from concurrent.futures import ThreadPoolExecutor, as_completed

import time

import requests # used to make api call for example


# Example to process
def long_api_call(currencyId: str):

    url = f"https://api.exchange.coinbase.com/currencies/{currencyId}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    # add sleep to simulate a long response
    time.sleep(5)

    return currencyId, response['status']


if __name__ == '__main__':

    # list of currencies to make calls for
    currency_list = ['ADA', 'XTZ', 'ETH', 'BTC']

    # iterative example
    start = time.time()
    
    print(f'Id\tStatus')
    for currencyId in currency_list:
        id, status = long_api_call(currencyId)
        print(f'{id}\t{status}')
    
    endtime = time.time() - start
    print(f'Iterative process completed {len(currency_list)} calls in {endtime} seconds')

    # with ThreadPoolExecutor() as executor:



