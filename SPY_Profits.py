import requests


key = 'YQ1RCVLLAF915U7R'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=SPY&outputsize=full' \
      '&apikey=YQ1RCVLLAF915U7R&datatype=json'
r = requests.get(url)
all_d = r.json()
useful_d = all_d['Time Series (Daily)']
# '1. open' , '2. high', '3. low', '4. close', '5. adjusted close', '6. volume', '7. dividend amount',
# '8. split coefficient'


def dailyprofit():
    # These are the daily profits for SPY since 1999-11-01 until 2023-06-21
    for n in useful_d:
        profit = float((useful_d[n]['1. open'])) - float((useful_d[n]['4. close']))
        print("Profit for " + str(n) + ": " + "%.4f" % profit)


def monthlyprofit():
    # These are the monthly profits for SPY in every month since 1999-11-xx until 2023-06-xx
    # My code works around the idea that the 6th character of the date will change when the month changes.
    # Example: When 1999-11 changes to 1999-12, the code knows a new month is starting.
    temp = "temporary"
    store = 0
    for m in useful_d:
        if temp[6] == m[6]:
            store = store + float(useful_d[m]['1. open']) - float(useful_d[m]['4. close'])
        else:
            if store != 0:
                print("Profit for month " + temp[5] + temp[6] + " of " + temp[0] + temp[1] + temp[2] + temp[3] + ": "
                      + "%.4f" % store)
                temp = m
                store = 0
                store = store + float(useful_d[m]['1. open']) - float(useful_d[m]['4. close'])

            else:
                store = store + float(useful_d[m]['1. open']) - float(useful_d[m]['4. close'])
                temp = m
    print("Profit for month " + temp[5] + temp[6] + " of " + temp[0] + temp[1] + temp[2] + temp[3] + ": "
          + "%.4f" % store)


def yearlyprofit():
    # These are the yearly profits for SPY. From 1999-2023
    temp = "temporary"
    store = 0
    for v in useful_d:
        if temp[3] == v[3]:
            store = store + float(useful_d[v]['1. open']) - float(useful_d[v]['4. close'])
        else:
            if store != 0:
                print("Profit for " + temp[0] + temp[1] + temp[2] + temp[3] + ": "
                      + "%.4f" % store)
                temp = v
                store = 0
                store = store + float(useful_d[v]['1. open']) - float(useful_d[v]['4. close'])
            else:
                store = store + float(useful_d[v]['1. open']) - float(useful_d[v]['4. close'])
                temp = v
    print("Profit for " + temp[0] + temp[1] + temp[2] + temp[3] + ": "
          + "%.4f" % store)

# Each function does as intended, yearlyprofit(), monthlyprofit() and dailyprofit()


yearlyprofit()
