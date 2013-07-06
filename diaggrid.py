size = 1001
m = size ** 2

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

start = int(size/2) 



grid = [[0 for i in range(size)] for j in range(size)]

pos = [start,start]
grid[pos[0]][pos[1]] = 1
pos[1] += 1
grid[pos[0]][pos[1]] = 2
d = DOWN
pos[0] += 1
l = 1
c = 0
for i in range (3,m+1):
	grid[pos[0]][pos[1]] = i
#	print (grid)
	c += 1
	if c >= l:
		c = 0
		d = (d + 1) % 4
#		print("Changing direction", d)
		if d == RIGHT or d == LEFT:
			l += 1
#			print("Extended")
#	else:
#		print ("Continue")

	if d == DOWN:
		pos[0] += 1
#		print("Down",pos)
	elif d == RIGHT:
		pos[1] += 1
#		print("Right",pos)
	elif d == UP:
		pos [0] -= 1
#		print("Up",pos)
	elif d == LEFT:
		pos [1] -= 1
#		print("Left",pos)

	
#print(grid)
s = 0
for i in range(size):
	for j in range(size):
		if i == j or size - j - 1 == i:
			s += grid[i][j]
#			print("Adding", grid[i][j], "from", i,j )
print(s) 



