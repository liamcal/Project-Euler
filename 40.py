s= ""
i = 1
p = 1
while len(s) < 1000000:
	s+=str(i)
	i+=1
for j in range (7):
	p = p * int(s[10**j-1])
print(p)
