#!/usr/bin/env python
# coding: utf-8

# In[3]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#DATE : 03/06/2021.

#PRACTICAL 4 : Write a program in Python to enter two unequal nos. 
               #if first no. is greater than display square of the smaller no. and cube of the greater no. otherwise vice-versa. 
               #If no. are equal display the message both no. are equal find square, square root and cube root of a number.

#INPUT
num1 = int(input("enter the first number :\t"))   #Taking two numbers from the user.
num2 = int(input("enter the second number :\t"))
if num1 != num2:                                  #using nested if else conditional statements to execute.
    print("BOTH THE NUMBERS ARE UNEQUAL\n\n")     #if the numbers are unequal, print the following statement.
    if num1 > num2:                               #if num1 is greater than num2, execute the following.
        print("HERE",num1,"IS GREATER THAN",num2)
        print("CUBE OF",num1,"IS",num1**3)
        print("SQUARE OF",num2,"IS",num2**2)
    else:                                         #else, the following statements are executed.
        print("HERE",num2,"IS GREATER THAN",num1)
        print("CUBE OF",num2,"IS",num2**3)
        print("SQUARE OF",num1,"IS",num1**2)
else:                                             #and if the numbers were equal, the following statements would be executed.
    print("BOTH THE NUMBERS ARE EQUAL\n\n")
    print("THE SQUARE OF ",num1,"= ", num1**2)
    print("THE SQUARE ROOT OF ",num1,"= ", num1**(1/2))
    print("THE CUBE ROOT OF ",num1,"= ", num1**(1/3))
    
#OUTPUT
enter the first number :	50
enter the second number :	50
BOTH THE NUMBERS ARE EQUAL


THE SQUARE OF  50 =  2500
THE SQUARE ROOT OF  50 =  7.0710678118654755
THE CUBE ROOT OF  50 =  3.6840314986403864


# In[ ]:




