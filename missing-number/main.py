raw_input()
numbers = map(int, raw_input().split(" "))
numbers.sort()
for i in range(0, len(numbers)):
	if(numbers[i] != i+1):
		print str(i+1)
		break