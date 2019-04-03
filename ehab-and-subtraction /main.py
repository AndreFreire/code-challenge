k = int(raw_input().split(" ")[1])	
numbers = map(int, raw_input().split(" "))

for i in range(k):
	if len(numbers) > 0:
		numbers = (i for i in numbers if i > 0)
	if len(numbers) == 0:
		minimum = 0
	else:
		minimum = min(numbers)

	print str(minimum)
	for j in range(len(numbers)):		
		numbers[j] -= minimum