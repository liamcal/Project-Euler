print([i for i in range(123456,166666) if all(set(str(a*i)) == set(str(i)) for a in range(1,7)) ][0])

