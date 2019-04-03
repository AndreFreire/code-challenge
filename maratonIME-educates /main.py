raw_input()
numbers = map(int, raw_input().split(" "))
if sum(numbers)%5==0:
	print str(sum(numbers)/5)
else:
	print str((sum(numbers)/5)+1)