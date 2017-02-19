n = 100
target = n
coins = list(range(1,n))
ways = [1]+[0]*target
for coin in coins:
    for i in range(coin,target+1):
        ways[i]+=ways[i-coin]
print(ways[target])
