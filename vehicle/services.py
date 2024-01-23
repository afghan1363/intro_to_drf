import requests
from rest_framework import status


def convert_currencies(rub_price):
    response = requests.get(
        url='https://api.currencyapi.com/v3/latest?apikey=cur_live_V8YF4KfG9OR6rxAAcNws41laUA7m4wnb20wpr92Y'
            '&currencies=RUB'
    )
    usd_price = 0
    if response.status_code == status.HTTP_200_OK:

        rate = response.json()['data']['RUB']['value']
        usd_price = float(rub_price) * round(rate, 2)
        print(usd_price)
    return usd_price
