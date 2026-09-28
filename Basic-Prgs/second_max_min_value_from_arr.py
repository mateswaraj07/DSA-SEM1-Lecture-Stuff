arr = [2,1,3,4,9,8,10,0]
min = arr[0]
max = arr[0]
smin = arr[0]
smax = arr[0]
for num in arr:
    if num < min:
        smin = min
        min = num
    if num > max:
        smax = max
        max = num
print("Maximum: ", max)
print("Minimum: ",min)
print("Second Maximum: ", smax)
print("Second Minimum: ",smin)