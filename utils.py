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

if __name__ == '__main__':
    import sys
    print(sys.argv)



