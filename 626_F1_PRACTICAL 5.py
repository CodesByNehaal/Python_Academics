#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#DATE : 03/06/2021.

#PRACTICAL 5 : To check whether input number is Armstrong number or not. An Armstrong number is an integer with three digits such that the sum of the cubes of its digits is equal to the number itself. Ex. 371.

#INPUT
num = int(input("ENTER A NUMBER TO VERIFY IF ITS AN ARMSTRONG NUMBER OR NOT : ")) #taking a number from the user.
sum = 0                                                  #initialising sum to 0
temp = num                                               #initialising num value in temp(temporary variable)

while temp > 0:                                          #using while loop with condition of temp being positive.
    digit = temp % 10     #dividing the temp(given number) with 10 and storing it. at first we get the units place digit followed by tens and etc.
    sum = sum + digit**3  #cubing the digit and adding its value to variable sum.
    temp = temp//10       #floor division on temp by 10. and then it goes back to the condition and interpret accordingly.
print("THE GIVEN NUMBER = ", num)                            #printing the given number.
print("THE SUM OF CUBE OF DIGITS OF GIVEN NUMBER = ",sum)    #printing the sum of cubes of the digits.
    
if num == sum:                                               #using if else conditional statement, check whether they are equal or not. act accordingly.
    print("BOTH ARE EQUAL.")
    print("HENCE, NUMBER IS AN ARMSTRONG NUMBER")
else:
    print("BOTH ARE UNEQUAL.")
    print("HENCE, NUMBER IS NOT AN ARMSTRONG NUMBER")

    
#OUTPUT
ENTER A NUMBER TO VERIFY IF ITS AN ARMSTRONG NUMBER OR NOT : 681
THE GIVEN NUMBER =  681
THE SUM OF CUBE OF DIGITS OF GIVEN NUMBER =  729
BOTH ARE UNEQUAL.
HENCE, NUMBER IS NOT AN ARMSTRONG NUMBER


# In[ ]:




