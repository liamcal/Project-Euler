names = sorted(str(open('names.txt', 'r').read()).replace('"','').split(',')) #Build the list of names
print(sum([sum([ord(c) -64 for c in list(name)])*(names.index(name)+1) for name in names ])) #Sum the scores

