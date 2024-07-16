class Student:
  def __init__(self, name, age, phoneNumber):
    self.name = name
    self.age = age
    self.phoneNumber = phoneNumber

  def __str__(self):
    return f"{self.name}({self.age})"

# student1 = Student(Name, AgeInteger, PhoneNumber)
student1 = Student("John", 36, "123")

# create student student1
# append each student to student list
# for loop through student list
# check student name contain m