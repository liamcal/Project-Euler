triangles= []

def genTri(n):
	triangles.append( int((n/2) * (n + 1)))
def wordScore(name):
	return sum([ord(c) - 64 for c in name ])
words = str(open('words.txt', 'r').read()).replace('"','').split(',')
scores = [wordScore(w) for w in words]
i = 1
genTri(i)
while max(triangles) < max(scores):
	i += 1
	genTri(i)
count = 0
for s in scores:
	if s in triangles:
		count += 1
print(count)
print (triangles)