raw_input()
arr = map(int, raw_input().split(" "))
prev = arr.pop(0)
n = len(arr)
count = 0
for i in range(n):
    if prev > arr[i]:
        count += prev - arr[i]
    else:    
        prev = arr[i]
print count