class AgeAndName:
    #new Superclass was created
    name = ""
    age = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Age(self):
         print("I'm", self.age, "years old.")
class Name(AgeAndName):
        #class Name inherited all of the attributes and properties from class Python
        def UserName(self):
           print("My name is", self.name)
class Person(AgeAndName):
    pass
class Student(AgeAndName):
    pass
class Employee(AgeAndName):
    room = ""
    def __init__(self, name, age, room):
        super().__init__(name, age)
        self.room = room

randomGuy2 = Person("Mike randomGuy2", 20)
randomGuy2.Age()

randomGuy = Student("Mike randomGuy", 20)
randomGuy.Age()

randomGuy3 = Name("Mike randomGuy3", 20)
# randomGuy3.UserName()
randomGuy3.Age()

employee = Employee("Tom", 6, "room1")
employee.Age()
employee.room = "room20"
print(employee.room)