#This opens the text file that will be used later
class CustomerInfo:
    email = ""
    phone = 0
    balance = 0
    customerid = ""
    #Creates a method that asks the user to input their email, phone number and balance
def CustomerInputInfo(self):
        self.email = input("Email account: ")
        self.phone = input("Phone number: ")
        self.balance = input("Balance: ")
        self.customerid = print(self.email, "|", self.phone, "|", self.balance)
        print(self.customerid)
#Action 1
def Get_All_Customer():
    fuga = open("Day4/customerdata.txt", "rt")
    print(fuga.read())
    fuga.close()
#Action 2
def Get_Customer_Based_On_Email(email):
    fuga = open("Day4/customerdata.txt", "rt")
    for line in fuga:
        if email in line:
            print(line)
    fuga.close()
#Action 3
def Create_CustomerInfo(fuga):
    fuga = open("Day4/customerdata.txt", "at")
    fuga.write(CustomerInputInfo)

while True:
    nextstep = input("input a number to choose your transaction:\n(1)View all customer info\n(2)Get one customer info based on Email\n(3)Create one customer info (change in data file)\n(4)Update customer balance based on Email (change in data file)\n(5)Delete one customer info based on Email (change in data file)\n(6)Finish\n ")
    if int(nextstep) == 1:
        Get_All_Customer()
    if int(nextstep) == 2:
        email = input("Please input your email: ")
        Get_Customer_Based_On_Email(email)
    if int(nextstep) == 3:
        fuga = open("Day4/customerdata.txt", "at")
        Create_CustomerInfo(fuga)
    if int(nextstep) == 6:
        break
        

        


    
    
