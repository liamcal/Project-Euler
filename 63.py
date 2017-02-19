print (len([[base,exponent] for base in range(1,100) for exponent in range(1,100) if len(str(base**exponent)) == exponent]))
