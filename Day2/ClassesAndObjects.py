# class     | object
# blueprint | instance

#this creates a class (blueprint, data structure)
class Room():
    furniture = ""
    width = 0
    length = 0
    def __init__(self, furniture, width, length):
        self.furniture = furniture
        self.width = width
        self.length = length
    def myfunc(self):
        if self.width > 30:
            print(self.furniture + "BIG ROOM!!!")
        else:
            print("Room info: ", self.furniture, self.width, self.length)
    def __str__(self):
        return f"String Object info furniture:{self.furniture}, width:{self.width}, length:{self.length}"

#New object called Room1 with all assigned properties (instance 1) 
# lua definition: each object is an instance of a specific class
room1 = Room("Table", 10, 20)
room1.myfunc()

#New object called Room2 with all assigned properties (instance 2)
room2 = Room("Chair", 50, 20)
del room2.furniture
room2.myfunc()

room3 = Room("TV", 100, 24)
room3.furniture = "Table"
room3.myfunc()