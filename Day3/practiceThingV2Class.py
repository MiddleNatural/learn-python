# Step1: Define a class student
class Student:
  def __init__(self, name, age, phoneNumber):
    self.name = name
    self.age = age
    self.phoneNumber = phoneNumber

  def __str__(self):
    return f"Name: {self.name}, age: {self.age}, phoneNumber: {self.phoneNumber}"

# Step2: Define register function 
def registerStudent():
    Name = input("Tell me your name: ")
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
    AgeInteger = int(age)
    PhoneNumber = input("Tell me your phone number: ")
    newStudent = Student(Name, AgeInteger, PhoneNumber)
    return newStudent

# Step3: Input student info
totalStudent = 2
studentList = []
for x in range(totalStudent):
    print("Please input student", x)
    newStudent = registerStudent()
    studentList.append(newStudent)

# Step4: Check student has 'm' in their name
for student in studentList:
    if "m" in student.name:
        print("Found student has 'm' in their name: ", student)