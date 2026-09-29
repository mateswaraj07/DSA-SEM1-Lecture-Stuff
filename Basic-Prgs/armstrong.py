num = int(input("Enter a number: "))
p = len(str(num))
sum = 0
n = num
while num>0:
    sum += (num%10)**p
    num //= 10
if n == sum:
    print("Number is Armstrong!")
else:
    print("Number is not Armstrong!")