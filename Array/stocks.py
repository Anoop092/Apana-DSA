# stock buy and sell
prices = [7,1,5,3,6,4]

# let us assume every day is selling point
max_profit = 0
best_buy = prices[0]

for i in range(0,len(prices)):
    if prices[i] > best_buy:
        max_profit = max(max_profit,prices[i] - best_buy)
    best_buy = min(best_buy,prices[i])
print(max_profit)