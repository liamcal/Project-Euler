

target = 100000
coins = range(1,target)
ways = [1]+[0]*target
for coin in coins:
    for i in range(coin,target+1):
        ways[i]+=ways[i-coin]
for j in range(1,target):
    if j % 50 == 0:
        print("Upto", j, ways[j] + 1)
    if (ways[j] + 1) % 1000000 == 0:
        print("found" , target, ways[target])
        break
