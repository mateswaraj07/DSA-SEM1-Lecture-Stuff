arr = [2,1,3,4,9,8,10,0]
min = arr[0]
max = arr[0]
for num in arr:
    if num < min:
        min = num
    if num > max:
        max = num
print("Maximum: ", max)
print("Minimum: ",min)