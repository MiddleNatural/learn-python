
Name = input("Tell me your name: ")
# Validate user input age
Age = input("Tell me your age: ")
if Age.isnumeric():
    print("Ok, you're eligible, keep moving")
else:
    print("Please write it in an integer form.")
    exit()
AgeInteger = int(Age)
# create an allow age list
AgeAllowlist = []
for index in range(1, 15):
    AgeAllowlist.append(index)
for index in AgeAllowlist:
    if (AgeInteger == index):
        print("Your age is: ", AgeInteger)
        break
    if (index == 15):
        print("Your age is allow in this class", AgeInteger)
# Validate user input phoneNumber
PhoneNumber = input("Tell me your phone number: ")
def new_func(ChangedName):
    ChangedName = Name.lower()
    if "m" in ChangedName:
     print("Good, the letter M is present in your name. Here's your data:", ChangedName, Age, PhoneNumber)
    else:
        print("Nope, the letter M isn't present in your name")
        return

print("Ok cool, let me check...")
new_func(ChangedName=True)
