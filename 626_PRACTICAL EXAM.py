#!/usr/bin/env python
# coding: utf-8

# In[1]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#DATE : 26/08/2021

#PROBLEM STATEMENT : CREATING A REGISTRATION/LOGIN INTERFACE FOR USERS AND STORING THE DATA IN A FILE.

#INPUT : 

print("******************************HELLO USER! WELCOME TO OUR PAGE.***********************************************")
print("1. REGISTRATION \n2. LOGIN")
choice =  int(input("PLEASE SELECT AN OPTION : "))

if choice == 1:
    print("*********************************************REGISTRATION********************************************************")
    print("\n\n********personal details*********")
    name = input("ENTER YOUR NAME : ")
    DOB = input("ENTER YOUR DATE OF BIRTH IN DDMM ORDER : ")
    YOB = input("ENTER YOUR YEAR OF BIRTH : ")
    AGE = input("ENTER YOUR AGE : ")
    GENDER = input("ENTER YOUR GENDER : ")
    NATIONALITY = input("WHICH COUNTRY DO YOU BELONG TO : ")
    print("\n\n**********************************************USERNAME*********************************************************")
    print("USERNAME SHOULD MATCH THE FOLLOWING CRITERIA : \n1. IT MUST BE MINIMUM 8 CHARACTERS LONG. \n2. IT MUST BE A MIXTURE OF LETTERS AND NUMBERS ONLY.\n3. IT MUST BE UNIQUE.")
    print("\n\nSOME USERNAME SUGGESTIONS FOR YOU ARE : ") 
    print("1. ", name+DOB ,"\n2. ", name+YOB)                       
    username = input("ENTER ANY USERNAME YOU LIKE : ")
    f = open("registered users.txt", "a")
    if len(username) >= 8:
        if username.isalnum():
            f = open("registered users.txt", "r")
            flag = 0
            index = 0
            for line in f:  
                index = index + 1 
                if username in line:
                    flag = 1
                    break 
            f.close()
            if flag == 0: 
                print("VALID USERNAME.") 
                f = open("registered users.txt", "a")
                f.write(username)
                f.write("\n")
                f.close() 
                
            else:
                print("USERNAME ALREADY TAKEN.")
                exit(1)
        else:
            print("USERNAME SHOULD NOT CONTAIN ANY SPECIAL CHARACTERS AND MUST BE STRICTLY ALPHANUMERIC.")
            exit(1)
    else:
        print("username should be minimum 8 characters long.")
        exit(1)
          
    def pass1():
        print("\n\n**********************************************PASSWORD*************************************************************")
        print("\n\nprepare a password which is\n1.minimum 8 letter long and contains atleast 1 Capital, 1 small alphabet and 1 number")
        password = input("ENTER A PASSWORD : ")
        length = len(password)                             
        if length >= 8:       
            if (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password)):
                print("\n\nYOUR USERNAME : ",username)  
                print("YOUR PASSWORD : ",password)
                print("ACCOUNT CREATION SUCCESSFUL.")
                f1 = open("password.txt", "a")
                f1.write(password)
                f1.write("\n")
                f1.close()
            else:
                print("THE PASSWORD DOES NOT MEET THE NECESSARY CRITERIA.")
                pass1()
        else:
            print("THE LENGTH OF THE PASSWORD SHOULD BE MINIMUM 8 LETTERS.")
            pass1()
        
    pass1()
    
else:
    print("\n\n************************************************login**************************************************************")

            
    print("\n\n\nlogin now to continue.")
    str1 = input("ENTER YOUR USERNAME : ")
    str2 = input("ENTER YOUR PASSWORD : ")
    print("ENTER THE FOLLOWING CAPTCHA IN THE BOX BELOW : Ql34Rw")
    captcha = input("ENTER THE CAPTCHA : ")

    file1 = open("registered users.txt", "r")
    flag1 = 0
    count = 0
    for line in file1:  
        count = count + 1 
        if str1 in line:
            flag1 = 1
            break 
    file1.close       
          
    if flag1 == 1:
        fpass = open('password.txt')
        content = fpass.readlines()
        if str2 == content[count-1]:
            if captcha == 'Ql34Rw':
                print("\nLOGIN SUCCESSFUL.")
            else:
                print("ENTER THE CORRECT CAPTCHA.TRY AGAIN.")
        else:
            print("PASSWORD ENTERED IS INCORRECT. TRY AGAIN.")
    else:
        print("ENTER THE CORRECT USERNAME. TRY AGAIN.")
    
print("\n\nTHANK YOU.")



#OUTPUT : 

******************************HELLO USER! WELCOME TO OUR PAGE.***********************************************
1. REGISTRATION 
2. LOGIN
PLEASE SELECT AN OPTION : 1
*********************************************REGISTRATION********************************************************


********personal details*********
ENTER YOUR NAME : nehaal
ENTER YOUR DATE OF BIRTH IN DDMM ORDER : 0312
ENTER YOUR YEAR OF BIRTH : 2002
ENTER YOUR AGE : 19
ENTER YOUR GENDER : male
WHICH COUNTRY DO YOU BELONG TO : india


**********************************************USERNAME*********************************************************
USERNAME SHOULD MATCH THE FOLLOWING CRITERIA : 
1. IT MUST BE MINIMUM 8 CHARACTERS LONG. 
2. IT MUST BE A MIXTURE OF LETTERS AND NUMBERS ONLY.
3. IT MUST BE UNIQUE.


SOME USERNAME SUGGESTIONS FOR YOU ARE : 
1.  nehaal0312 
2.  nehaal2002
ENTER ANY USERNAME YOU LIKE : iamboss123
VALID USERNAME.


**********************************************PASSWORD*************************************************************


prepare a password which is
1.minimum 8 letter long and contains atleast 1 Capital, 1 small alphabet and 1 number
ENTER A PASSWORD : prem2002
THE PASSWORD DOES NOT MEET THE NECESSARY CRITERIA.


**********************************************PASSWORD*************************************************************


prepare a password which is
1.minimum 8 letter long and contains atleast 1 Capital, 1 small alphabet and 1 number
ENTER A PASSWORD : nehaal
THE LENGTH OF THE PASSWORD SHOULD BE MINIMUM 8 LETTERS.


**********************************************PASSWORD*************************************************************


prepare a password which is
1.minimum 8 letter long and contains atleast 1 Capital, 1 small alphabet and 1 number
ENTER A PASSWORD : Prem@2002


YOUR USERNAME :  iamboss123
YOUR PASSWORD :  Prem@2002
ACCOUNT CREATION SUCCESSFUL.


THANK YOU.


# In[ ]:




