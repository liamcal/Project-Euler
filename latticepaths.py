gridSize = 20;
path =1;
 
for i in range(gridSize):

	path = path * (2*gridSize  -i);
	path = path / (i+1);

print (path)