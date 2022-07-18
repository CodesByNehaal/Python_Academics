#!/usr/bin/env python
# coding: utf-8

# In[4]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#DATE : 17/06/2021.
'''Practical 8 : Write a Python program to perform following string operations. 
    a) String concatenation b) String Reverse 
    c) String compare d) String length 
    e) Palindrome f) Case change.'''
    
    
#INPUT

#TAKING PERSONAL DETAILS AS INPUT FROM USER.
print("***********************WELCOME TO OUR PAGE. TO CONTINUE, SIGNUP BY ENTERING OUR DETAILS.*******************************")
print("\n\n********personal details*********")
name = input("ENTER YOUR NAME : ")
DOB = input("ENTER YOUR DATE OF BIRTH IN DDMM ORDER : ")
YOB = input("ENTER YOUR YEAR OF BIRTH : ")
AGE = input("ENTER YOUR AGE : ")

print("\n\n**********************************************USERNAME*************************************************************")

print("\n\nUSERNAME SUGGESTIONS FOR YOU ARE : ") 
print("1. ", name+DOB ,"\n2. ", name+YOB,"\n3. ", "@" +name+"#"+AGE) #creating username suggestions using string concatenation.
username = input("ENTER THE USERNAME YOU LIKE : ")

print("\n\n**********************************************PASSWORD*************************************************************")

print("\n\nprepare a password which is\n1.minimum 8 letter long. \n2.a palindrome. \n3.LOWERCASE ONLY")
password = input("ENTER A PASSWORD : ")
length = len(password)                              #len() function returns the length of string
rev_pass = password[::-1]                           #storing the reverse of the string in the given variable. 
if length >= 8:       
    if password == rev_pass:                        #checking for palindrome condition.                                      
        if password.islower():                      #isLower() method evaluates whether all alphabets in a string are lowercase.
            print("\n\nYOUR USERNAME : ",username)  
            print("YOUR PASSWORD : ",password)
            print("ACCOUNT CREATION SUCCESSFUL.")
        else:
            password = password.lower()             #lower() changes case of all characters to lower.
            print("\n\nYOUR USERNAME : ",username)
            print("YOUR PASSWORD : ",password)
            print("ACCOUNT CREATION SUCCESSFUL.")
    else:
        print("THE PASSWORD IS NOT A PALINDROME.")
else:
    print("THE LENGTH OF THE PASSWORD SHOULD BE MINIMUM 8 LETTERS.")
        
        
print("\n\n************************************************login**************************************************************")

            
print("\n\n\nlogin now to continue.")
str1 = input("ENTER YOUR USERNAME : ")
str2 = input("ENTER YOUR PASSWORD : ")
print("ENTER THE FOLLOWING CAPTCHA IN THE BOX BELOW : Ql34Rw")
captcha = input("ENTER THE CAPTCHA : ")

#comparing strings.(entered texts with the username and password and captcha.)

if str1 == username:
    if str2 == password:
        if captcha == 'Ql34Rw':
            print("\nLOGIN SUCCESSFUL.")
        else:
            print("ENTER THE CORRECT CAPTCHA.TRY AGAIN.")
    else:
        print("PASSWORD ENTERED IS INCORRECT. TRY AGAIN.")
else:
    print("ENTER THE CORRECT USERNAME. TRY AGAIN.")
    
print("\n\nTHANK YOU.")

'''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#OUTPUT

***********************WELCOME TO OUR PAGE. TO CONTINUE, SIGNUP BY ENTERING OUR DETAILS.*******************************


********personal details*********
ENTER YOUR NAME : NEHAAL
ENTER YOUR DATE OF BIRTH IN DDMM ORDER : 0312
ENTER YOUR YEAR OF BIRTH : 2002
ENTER YOUR AGE : 19


**********************************************USERNAME*************************************************************


USERNAME SUGGESTIONS FOR YOU ARE : 
1.  NEHAAL0312 
2.  NEHAAL2002 
3.  @NEHAAL#19
ENTER THE USERNAME YOU LIKE : NEHAAL0312


**********************************************PASSWORD*************************************************************


prepare a password which is
1.minimum 8 letter long. 
2.a palindrome. 
3.LOWERCASE ONLY
ENTER A PASSWORD : ABC55CBA


YOUR USERNAME :  NEHAAL0312
YOUR PASSWORD :  abc55cba
ACCOUNT CREATION SUCCESSFUL.


************************************************login**************************************************************



login now to continue.
ENTER YOUR USERNAME : NEHAAL0312
ENTER YOUR PASSWORD : abc55cba
ENTER THE FOLLOWING CAPTCHA IN THE BOX BELOW : Ql34Rw
ENTER THE CAPTCHA : Ql34Rw

LOGIN SUCCESSFUL.


THANK YOU.

'''



