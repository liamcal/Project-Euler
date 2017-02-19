import math
with open('p099_base_exp.txt') as f:
    largest = 0
    ans = -1
    for i, line in enumerate(f):
        base, exponent = map(int,line.strip().split(','))
        new = exponent * math.log(base)
        if new > largest:
            largest = new
            ans = i + 1
    print(ans)
