maxPerm = lambda x: ''.join(sorted(list(str(x)), reverse= True))
cubePerms = {}
for i in range(1,10000):
    mp = maxPerm(i**3)
    if mp in cubePerms:
        cubePerms[mp].append(i)
        if len(cubePerms[mp]) == 5:
            print(sorted(cubePerms[mp])[0]**3)
            break
    else:
        cubePerms[mp] = [i]