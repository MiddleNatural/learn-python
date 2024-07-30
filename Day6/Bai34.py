import math
userinput = int(input("Input the amount of square roots: "))
answer = 0
for index in range(userinput):
    print(index)
    answer = math.sqrt((index + 1) + answer)
print(answer)