# Write a Python program to create a person class. 
# Include attributes  like name, country and date of birth.
# Implement a method to  determine the person’s age. 

#This creates a Class called Person
class Person:
    name = ''
    country = ''
    year = 0
    def inputPersonInfo(self):
        #We create the attributes (Name, Country, birth year.)
        self.name = input("Name: ")
        self.country = input("Country: ")
        #we set the "ageCheck" variable to False to be able to execute the while loop
        ageCheck = False
        #this puts the user in a loop if their birth year is NOT an integer
        while ageCheck == False:
            birthYear  = input("Age: ")
            if birthYear.isnumeric() == False:
                birthYear  = input("Please input your year of birth in an integer form: ")
                continue
            #If the condition is true (birthYear.isnumeric() == True then we break out of the loop)
            else:
                self.year = int(birthYear)
                break
    #We now define a new method inside the class Person and we call it age_calculator    
    def age_calculator(self):
        currentAge = 2024 - self.year
        print("You are",currentAge,"years old")

person1 = Person()
person1.inputPersonInfo()
# we call the method inside of the Person for it to execute the code within the function
person1.age_calculator()




