userinput = int(input("Please input a number (must be a dividend): "))
number = 0
while number >= 0:
   number = number + 1
   if userinput % number == 0:
      print(number)
   else:
    continue