import requests
from decimal import *
from datetime import datetime

def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in response:
        return None
    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    today = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, today)
    return f"{Decimal(rub.replace(',', '.'))}, {datetime(year=year, month=month, day=day)}"


print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('cny'))


# import utils
#
# print(utils.currency_rates('USD'))


# import utils
# import sys
#
# print(utils.currency_rates(sys.argv[1]))
