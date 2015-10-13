__author__ = 'Avantha'

stocks ={
    'Google': 530.34,
    'FBook':123.23,
    'AMZN':220.21,
    'YAHO':321.42,
    'Apple':412.11
}

print(min(zip(stocks.values(),stocks.keys())))
print(max(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.values(),stocks.keys())))
#print(min(zip(stocks.keys(),stocks.values())))

