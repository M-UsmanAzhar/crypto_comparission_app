import requests as r
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


def compare_price(symbol, comparison_symbol, all_data=True, aggregate=1, exchange=''):

    inp = int(input('1 for Minute\n2 for Hourly\n3 for Daily '))
    if inp == 1:
        limit = 9999
        history = 'histominute'
    elif inp == 2:
        limit = 9999
        history = 'histohour'
    elif inp == 3:
        limit = 1
        history = 'histoday'

    url = 'https://min-api.cryptocompare.com/data/'+history+'?fsym={}&tsym={}&limit={}&aggregate={}'.format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)

    df = pd.DataFrame(r.get(url).json()['Data'])
    df['timestamp'] = [dt.datetime.fromtimestamp(d) for d in df.time]
    plt.plot(df.timestamp, df.close)
    plt.xticks(rotation = 30)
    return plt.show()


print(compare_price('BTC', 'USD'))



