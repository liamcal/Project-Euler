checked = {1:set([1]), 89:set([89])}
count = 0
for i in range(1,597):
    if i % 100000 == 0:
        print("up to",i,count)
    n = i
    while n not in checked[1] and n not in checked[89]:
        n = sum(int(d)**2 for d in str(n))
        #print(n)
    if n in checked[89] or n ==89:
        count += 1
        checked[89].add(i)    
    elif n in checked[1] or n == 1:
        checked[1].add(i)
print(count)
print(len(checked[89]))