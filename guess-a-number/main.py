n = int(raw_input())
minimo = -10 ** 9
maximo = 10 ** 9
for i in range(n):
	line = raw_input().split(" ")
	if line[2] == "Y":
		if line[0] == ">=" and minimo < int(line[1]):
			minimo = int(line[1])
		elif line[0] == ">" and minimo < int(line[1]):
			minimo = int(line[1]) + 1
		elif line[0] == "<=" and maximo > int(line[1]):
			maximo = int(line[1])
		elif line[0] == "<" and maximo > int(line[1]):
			maximo = int(line[1]) -1
	else:
		if line[0] == ">=" and maximo > int(line[1]):
			maximo = int(line[1]) -1
		elif line[0] == ">" and maximo > int(line[1]):
			maximo = int(line[1])
		elif line[0] == "<=" and minimo < int(line[1]):
			minimo = int(line[1]) + 1
		elif line[0] == "<" and minimo < int(line[1]):
			minimo = int(line[1])
if minimo > maximo:
	print "Impossible"
elif minimo == maximo:
	print (str(minimo))
elif minimo == -10 ** 9:
	print str(maximo - 1)
else:
	print str(minimo)

