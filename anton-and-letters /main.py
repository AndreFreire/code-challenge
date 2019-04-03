line = raw_input().replace(" ", "")
line = line[1:len(line)-1]
if len(line) == 0:
	print "0"
else:
	print str(len(set(line.split(","))))