print(sum([i for i in range(10,400000) if sum([int(c)**5 for c in str(i)]) == i]))

