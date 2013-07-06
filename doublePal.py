pal = lambda x: str(x) == str(x)[::-1]
print(sum([i for i in range(1000000) if pal(i) and pal(str(bin(i))[2:]) ]))