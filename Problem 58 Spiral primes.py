import math

def is_prime(n):
    if n == 2 or n == 3: 
        return True
    elif n < 2 or n % 2 == 0: 
        return False
    elif n < 9:
        return True
    elif n % 3 == 0: 
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0: 
            return False
        else:
            f += 6
    return True


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
found = False
size = 4501
def create_spiral(size):
	m = size ** 2
	start = int(size/2)
#	grid = [[0 for i in range(size)] for j in range(size)]
	grid = [[1]]
#	pos = [start,start]
#	grid[pos[0]][pos[1]] = 1
#	pos[1] += 1
#	grid[pos[0]][pos[1]] = 2
	grid = add_layer(grid,size-1)
	# d = DOWN
	# pos[0] += 1
	# l = 1
	# c = 0
	# for i in range (3,m+1):
	# 	grid[pos[0]][pos[1]] = i
	# #	print (grid)
	# 	c += 1
	# 	if c >= l:
	# 		c = 0
	# 		d = (d + 1) % 4
	# #		print("Changing direction", d)
	# 		if d == RIGHT or d == LEFT:
	# 			l += 1
	# #			print("Extended")
	# #	else:
	# #		print ("Continue")

	# 	if d == DOWN:
	# 		pos[0] += 1
	# #		print("Down",pos)
	# 	elif d == RIGHT:
	# 		pos[1] += 1
	# #		print("Right",pos)
	# 	elif d == UP:
	# 		pos [0] -= 1
	# #		print("Up",pos)
	# 	elif d == LEFT:
	# 		pos [1] -= 1
	# #		print("Left",pos)
	return(grid)

def add_layer(grid,n):
	for l in range(n):
#		print ("Adding layer",l,n)
		for row in grid:
			row.insert(0,0)
			row.append(0)
		l = len(grid[0])
		grid.insert(0,[0 for i in range(l)])
		grid.append([0 for i in range(l)])
		start = (l - 2) ** 2 + 1
		stop = start + 2*l + 2*(l-2)
		pos = [1, l-1]
		d = DOWN
		c = 0
		for i in range(start,stop):
			grid[pos[0]][pos[1]] = i
#			for row in grid:
#				print(row)
			c += 1
			if c >= l-1:
				c = 0
				d = (d + 1) % 4
#				print("Changing direction", d)
#			else:
#				print ("Continue")
			if d == DOWN:
				pos[0] += 1
#				print("Down",pos)
			elif d == RIGHT:
				pos[1] += 1
#				print("Right",pos)
			elif d == UP:
				pos [0] -= 1
#				print("Up",pos)
			elif d == LEFT:
				pos [1] -= 1
#				print("Left",pos)
	return(grid)



def check_primes(grid,p,d):
	size = (len(grid)) -1
	dgs = d + 4
	prm = p
	if is_prime(grid[0][0]):
		prm += 1
#		print((grid[0][0], "is prime"),prm)
	if is_prime(grid[size][0]):
		prm += 1
#		print((grid[size][0], "is prime"),prm)
	if is_prime(grid[0][size]):
		prm += 1
#		print((grid[0][size], "is prime"),prm)
	if is_prime(grid[size][size]):
		prm += 1
#		print((grid[size][size], "is prime"),prm)
	ratio = prm/dgs
#	if size % 500 == 0:
	print(size,prm,'/',dgs,ratio)
	return([ratio,prm])

found = False
grid = create_spiral(8)
for row in grid:
	print(row)
# primes = 0
# diags = 0	
# i = 1
# ratio = 0
# #while not found:
# while i < 30:
# 	grid = add_layer(grid,1)
# #	print("added 20")
# #	for row in grid:
# #		print(row)
# 	i += 2
# 	result = check_primes(grid,primes,diags)
# 	if result[0] < 0.1:
# 		found = True
# 		ratio = result[0]
# 	else:
# 		primes = result[1]
# 		diags += 4
# #		print (result[1],diags)
# print("Found", ratio, i)


	
# #			print("Adding", grid[i][j], "from", i,j )
# print("Found,", size, ratio)



