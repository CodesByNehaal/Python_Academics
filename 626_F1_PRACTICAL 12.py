#!/usr/bin/env python
# coding: utf-8

# In[3]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#PRACTICAL 12.1 :  Write Python class for bank customer with withdraw and deposit operations 
#                  (use inheritance (Introduce class, object concepts).

#input :

import random                                     #importing random library to generate a random 4 digit number.

class SBI_bank:                                   #Creating a class called SBI_bank

    def __init__(self):                           #initializing the object
        self.balance = random.randint(1111,9999)  #let a random 4 digit number generated be the available balance of the acc. holder
        print("CURRENT BALANCE :",self.balance)   #displaying current balance.
    
    def Customer(self):                           #Method to Enter Details of customer(name, account type, account number)
        name = input("ENTER THE NAME OF THE ACCOUNT HOLDER : ")           
        acc_type = input("ENTER THE TYPE OF ACCOUNT YOU HAVE (savings,current,other) : ")
        acc_num = int(input("Enter Account number (16-Digits) : "))

    def deposit(self):                                                            #Method to deposit amount
        depo_value = int(input("\nENTER THE AMOUNT TO BE DEPOSITED (in Rs.) : ")) #Asking user to enter the amount to be diposited
        self.balance = self.balance + depo_value                                  #Adding the amount to balance
        print("Rs.",depo_value," HAS BEEN DEPOSITED IN YOUR ACCOUNT.")            #Displaying the deposit amount.
        print("CURRENT BALANCE :",self.balance)                                   #displaying current balance.
    
    def withdraw(self):                                                                    #Method to withdraw amount
        withdraw_value = int(input("\nENTER THE AMOUNT YOU WISH TO WITHDRAW (in Rs.) : ")) #asking user to enter the amount to be withdrawn.
        if withdraw_value > self.balance:                                                  #if withdrawal amount is greater than available balance, print the following.
            print("INSUFFICIENT BALANCE. THANK YOU!!!") 
        else:                                                                              #else, execute the withdrawal process.                              
            self.balance = self.balance - withdraw_value
            print("Rs.",withdraw_value," HAS BEEN WITHDRAWN FROM YOUR ACCOUNT.")           #displaying the withdrawal amount. 
        print("CURRENT BALANCE :",self.balance)                                            #displaying current balance.
    
    
    def display(self):                                                            #Method to Display the available balance
        print("Rs.",self.balance,"IS AVAILABLE IN YOUR ACCOUNT.")


sbi = SBI_bank()      #creating an object of class

sbi.Customer()        #Calling methods
sbi.deposit()     
sbi.withdraw()
sbi.display()
  
        
#OUTPUT : 
CURRENT BALANCE : 7102
ENTER THE NAME OF THE ACCOUNT HOLDER : NEHAAL PANDEY
ENTER THE TYPE OF ACCOUNT YOU HAVE (savings,current,other) : savings
Enter Account number (16-Digits) : 0000123456789000

ENTER THE AMOUNT TO BE DEPOSITED (in Rs.) : 4000
Rs. 4000  HAS BEEN DEPOSITED IN YOUR ACCOUNT.
CURRENT BALANCE : 11102

ENTER THE AMOUNT YOU WISH TO WITHDRAW (in Rs.) : 10000
Rs. 10000  HAS BEEN WITHDRAWN FROM YOUR ACCOUNT.
CURRENT BALANCE : 1102
Rs. 1102 IS AVAILABLE IN YOUR ACCOUNT.


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#PRACTICAL 12.2: Using concepts of polymorphism write Python application program.

#input

class family:   #introducing base class
    def __init__(self,name,age):  
        self.name = name
        self.age = age
        
    def member1(self):
        print(f"{self.name} is the head of the family. He is {self.age} years old.")
        
    def member2(self):
        print(f"{self.name} is the wife of the head of the family. she is {self.age} years old.")
        
class child: #introducing dervived class
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def member1(self):
        print(f"{self.name} is his son. he is {self.age} years old.")
    
    def member2(self):
        print(f"{self.name} is their daughter. she is {self.age} years old.")
        
parent1 = family("ANIL PANDEY", 48)
parent2 = family("PRAMILA PANDEY", 46)
child1 = child("NEHAAL PANDEY", 18)
child2 = child("NISHA PANDEY", 28)

for nuclear_family in (parent1,child1):
    nuclear_family.member1()
    

for nuclear_family in (parent2,child2):
    nuclear_family.member2()
    
    
#OUTPUT : 
ANIL PANDEY is the head of the family. He is 48 years old.
NEHAAL PANDEY is his son. he is 18 years old.
PRAMILA PANDEY is the wife of the head of the family. she is 46 years old.
NISHA PANDEY is their daughter. she is 28 years old.
    



