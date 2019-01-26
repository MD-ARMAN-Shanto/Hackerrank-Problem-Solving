stocks = {

    'GOOG' : 520.76,
    'FB' : 76.75,
    'YHOO' : 39.28,
    'AMZN' : 306.21,
    'APPLE' : 99.25
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))