import math
matches = {}

def hyp(a,b):
    return math.sqrt(a**2 + b**2)

for a in range(250,500):
    for b in range(20,a):
        c = hyp(a,b)
        if c == int(c):
            c = int(c)
            p = a + b + c
            if p <= 1000:
                if p in matches:
                    matches[p] += 1
                else:
                    matches[p] = 1
            else:
                break
ans = sorted(matches.items(), key=lambda x: x[1], reverse=True)[0]
print("Perimeter with most solutions is:", ans[0], "with",ans[1])
