def penta(max):
	nums = []
	for i in range(1,max):
		nums.append(int(i*(3*i-1)/2))
	return(nums)


a = penta(2500)
p = set(a)
m = 999999999
print("done")
for i in range(len(a)):
	for j in (range(len(a))):
		if ( len (p.intersection([a[i]+a[j],a[j]-a[i]]) ) > 1 and a[i] !=a[j] ):
			#print(len (p.intersection([a[i]+a[j],a[j]-a[i]]) ))
			if abs(a[i]-a[j]) < m:
				m = abs(a[i]-a[j])
				print("new min:", m)
print("finished")
print(m)


#and [n for n in p if i == p[i] + p[j]]