userinput = int(input("Please input a number: "))
result = True
while userinput > 0:
    lastDigitOfNumber = userinput % 10
    if (lastDigitOfNumber % 2) == 0:
        result = False
        break
    else:
        userinput = int(userinput / 10)

if result:
    print("All numbers are odd ones")
else:
    print("Not all numbers are odd ones")