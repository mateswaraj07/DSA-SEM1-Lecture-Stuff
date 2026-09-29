start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    flag = 0

    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            flag = 1
            break

    if flag == 0 and num > 1:
        print(num)