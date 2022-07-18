#!/usr/bin/env python
# coding: utf-8

# In[7]:


def rollno(batch):                                             #DEFINING A FUNCTION TO COLLECT ROLL NOs of student in batch.
    roll_no = []                                               #initialising an empty list to store roll no.
    for i in range (batch):
        item = input("ENTER THE ROLL NO. OF STUDENT = ")
        roll_no.append(item)                                   #appending the elements to the list and returning it.
    return roll_no

def name(batch):                                               #DEFINING A FUNCTION TO COLLECT NAMES of student in batch.
    name = []                                                  #initialising an empty list to store names.
    for i in range (batch):
        items = input("ENTER THE NAME OF STUDENT = ")
        name.append(items)                                     #appending the elements to the list and returning it.
    return name

def SGPA(batch):                                               #DEFINING A FUNCTION TO COLLECT sgpa of student in batch.
    sgpa = []                                                  #initialising an empty list to store sgpa
    for i in range (batch):
        element = input("ENTER THE SGPA OF STUDENT IN SEM 1 = ")
        sgpa.append(element)                                   #appending the elements to the list and returning it.
    return sgpa

def tempo(roll_no,batch,search,temp=0):  #defining a function with parameters mentioned in the ()
    for i in range(0,batch-1):           #using for loop, creating a linear search from oth element to 2nd last element
        if roll_no[i] == search:         #if we get the element we are looking,
            temp=2                       #temp stores 2.
            return i                     #function returns i.
            break                        #interpretor breaks out of the loop.
        else:                            #else, temp stores 1 and coninues the loop.
            temp=1
            continue
    while (temp==1):                     #while, temp is 1, we perform search on the last element.
        if roll_no[batch-1] == search:   #if we get the search element at last element,
            temp=2                       #temp becomes 2.
            i = batch-1                  #i stores the last element number and function returns it.
            return i

        else:                            #else, temp stores 0.5 and function returns it.
            temp = 0.5
            return temp 
            
#values of temp notify different thing.            
#2 specifies search successful. 1 specifies not found yet but operation in process and 0.5 defines that search unsuccesssful.
            
            

batch = int(input("HOW MANY STUDENTS ARE PRESENT IN YOUR BATCH : "))
roll_no = rollno(batch)                        #the variable stores what the function returns. i.e. a list.
name = name(batch)
sgpa = SGPA(batch)
print("\n\n\nSTUDENT INFO STORED SUCCESSFULLY.")

search = input("\n\nENTER THE ROLL NO. OF THE STUDENT WHOSE DETAILS YOU WANT : ") #taking search element from user.

i = tempo(roll_no,batch,search) #i stores value which the function returns.


        
        
if i == 0.5: #if i = 0.5, means element not found.
    print("\nno details found.")
else:        #else, we print the student details.
    print("\nSTUDENT NAME : ", name[i])
    print("STUDENT roll no. : ", roll_no[i])
    print("STUDENT SGPA : ", sgpa[i])
    
    
print("\nthank you!")
    
    
#OUTPUT

HOW MANY STUDENTS ARE PRESENT IN YOUR BATCH : 5
ENTER THE ROLL NO. OF STUDENT = 601
ENTER THE ROLL NO. OF STUDENT = 602
ENTER THE ROLL NO. OF STUDENT = 603
ENTER THE ROLL NO. OF STUDENT = 604
ENTER THE ROLL NO. OF STUDENT = 605
ENTER THE NAME OF STUDENT = JAY YAMSANWAR
ENTER THE NAME OF STUDENT = SAURABH MULIK
ENTER THE NAME OF STUDENT = VEERAJ GAUDAR
ENTER THE NAME OF STUDENT = ADITYA GAUTAM
ENTER THE NAME OF STUDENT = NEHAAL PANDEY
ENTER THE SGPA OF STUDENT IN SEM 1 = 9
ENTER THE SGPA OF STUDENT IN SEM 1 = 8.9
ENTER THE SGPA OF STUDENT IN SEM 1 = 9.8
ENTER THE SGPA OF STUDENT IN SEM 1 = 9.5
ENTER THE SGPA OF STUDENT IN SEM 1 = 7



STUDENT INFO STORED SUCCESSFULLY.


ENTER THE ROLL NO. OF THE STUDENT WHOSE DETAILS YOU WANT : 605

STUDENT NAME :  NEHAAL PANDEY
STUDENT roll no. :  605
STUDENT SGPA :  7

thank you!


# In[ ]:




