# Step1: Define register function 
def registerStudent():
    name = input("Tell me your name: ")
    # Validate user input age
    checkAge = False
    while checkAge == False:
        age = input("Please tell me your age integer form: ")
        if age.isnumeric() == False:
            continue
        else:
            AgeInteger = int(age)
            if AgeInteger>0 and AgeInteger<15:
                break
            else:
                print("Your age must less than 15")
    phoneNumber = input("Tell me your phone number: ")
    newStudent = {
        "name": name,
        "age": int(age),
        "phoneNumber": phoneNumber
    }
    return newStudent

# Step2: Input student info
totalStudent = 2
studentListDictionary = []
for x in range(totalStudent):
    print("Please input student", x)
    newStudent = registerStudent()
    studentListDictionary.append(newStudent)

# Step3: Check student has 'm' in their name
for student in studentListDictionary:
    if "m" in student.get("name"):
        print("Found student has 'm' in their name: ", student)