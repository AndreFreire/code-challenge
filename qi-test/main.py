raw_input()
numbers = map(int, raw_input().split(" "))
even = []
odd = []
for i in range(len(numbers)):
	if numbers[i] %2 == 0:
		even.append(i+1)
	else:
		odd.append(i+1)
	if i >= 2 and len(even)>0 and len(odd)>0:
		break 
if len(odd) == 1:
	print str(odd[0])
else:
	print str(even[0])