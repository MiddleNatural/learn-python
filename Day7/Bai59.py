userinput = int(input("Please input a number: "))
result = True
list = []
while userinput > 0:
    lastDigitOfNumber = userinput % 10
    list.append(lastDigitOfNumber)
    userinput = int(userinput / 10)
len = len(list)
onepart = int(len // 2)
for index in range(onepart):
    if (list[index] == list[len - 1 - index]) == False:
        result = False
        break
if result:
    print("It is a Palindrome number")
else:
    print("It is NOT a Palindrome number")