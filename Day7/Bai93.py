userinput = int(input("Please input a number: "))
result = True
if userinput % 2 == 0 or userinput % 3 == 0 or userinput % 5 == 0 or userinput % 7 == 0:
    result = False
if result:
    print("bru")
else:
    print("gah")