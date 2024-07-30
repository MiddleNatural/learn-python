#Action 1
def Get_All_Customer():
    fuga = open("Day5/customerdata.txt", "rt")
    print("| Email | Name | Balance |")
    for line in fuga:
        customerline = line.split(",")
        row = customerline[0] + "|" + customerline[1] + "|" + customerline[2].replace("\n", "") + "|"
        print(row)
    fuga.close()
#Action 2
def Get_Customer_Based_On_Email():
    fuga = open("Day5/customerdata.txt", "rt")
    email = input("Please input your email: ")
    for line in fuga:
        if email in line:
            print(line)
    fuga.close()
#Action 3
def Create_CustomerInfo():
    fuga = open("Day5/customerdata.txt", "at")
    email = input("email: ")
    name = input("name: ")
    customerdata = email + "," + name + "," + "0"
    print("The information of your email has been created: " + email)
    fuga.write("\n")
    fuga.write(customerdata)
    fuga.close()
#Action 4
def Update_CustomerBalance():
    #Loading data from file to customer list
    fuga = open("Day5/customerdata.txt", "rt")
    customerlist = []
    for line in fuga:
        customerlist.append(line)
    fuga.close
    #Find customer via email and update customer's balance
    email = input("Please input your email: ")
    balance = int(input("Please input your balance: "))
    updatedCustomerData = ""
    for customer in customerlist:
        if email in customer:
            customerline = customer.split(",")
            updatedCustomerData = customerline[0] + "," + customerline[1] + "," + str(balance)
    #Write all customer's info file
    fuga = open("Day5/customerdata.txt", "wt")
    for customer in customerlist:
        if email in customer:
            print("The information of your email has been updated." + email)
            fuga.write(updatedCustomerData)
            fuga.write("\n")
        else:
            fuga.write(customer)
    fuga.close()
def Delete_Customer():
    #Loading data from file to customer list
    fuga = open("Day5/customerdata.txt", "rt")
    customerlist = []
    for line in fuga:
        customerlist.append(line)
    fuga.close
    #Find customer via email to delete the customer from the database
    email = input("Please input your email: ")
    #Write all customer's info file
    fuga = open("Day5/customerdata.txt", "wt")
    for customer in customerlist:
        if email in customer:
            print("The information of your email has been deleted." + email)
            pass
        else:
            fuga.write(customer)
    fuga.close()
while True:
    nextstep = input("input a number to choose your transaction:\n(1)View all customer info\n(2)Get one customer info based on Email\n(3)Create one customer info (change in data file)\n(4)Update customer balance based on Email (change in data file)\n(5)Delete one customer info based on Email (change in data file)\n(6)Finish\n ")
    if int(nextstep) == 1:
        Get_All_Customer()
    if int(nextstep) == 2:
        Get_Customer_Based_On_Email()
    if int(nextstep) == 3:
        Create_CustomerInfo()
    if int(nextstep) == 4:
        Update_CustomerBalance()
    if int(nextstep) == 5:
        Delete_Customer()
    if int(nextstep) == 6:
        break