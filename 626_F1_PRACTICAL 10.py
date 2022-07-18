#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#DATE : 10/07/2021.

#PRACTICAL 10: Choose cricket team of eleven players find the captain of the team (consider tallest person as a captain) using dictionary.

#INPUT
n=int(input("enter the no. of players:\t"))           #taking the count of players
cricketer={}                                          #creating a dictionary.
for i in range(1,n+1):                                #using for loop, taking names and height of players and storing them in the dictionary.
    print("\ncricketer no: ",i)
    name=input("enter the name of the cricketer:")
    ht=input("enter their height:")
    cricketer[name]=ht                               #assigning height of player name in the dictionary.
print("\n",cricketer)                                #printing the dictionary.
max_hgt = max(cricketer, key=cricketers.get)         #max function returns the maximum value from the dictionary. i.e. a player with the max. height.
print("the captain is:",max_hgt)                     #printing the cricketer name the max function returns.

#OUTPUT
'''
enter the no. of players:	11


cricketer no:  1
enter the name of the cricketer:Mayank Agarwal
enter their height:170




cricketer no:  2
enter the name of the cricketer:Rohit Sharma
enter their height:169




cricketer no:  3
enter the name of the cricketer:Hardik Pandya
enter their height:174




cricketer no:  4
enter the name of the cricketer:Virat Kohli 
enter their height:171




cricketer no:  5
enter the name of the cricketer:Jasprit Bumrah
enter their height:168




cricketer no:  6
enter the name of the cricketer:Kuldeep Yadav
enter their height:165




cricketer no:  7
enter the name of the cricketer:Shikhar Dhawan
enter their height:175




cricketer no:  8
enter the name of the cricketer:Ravindra Jadeja
enter their height:170




cricketer no:  9
enter the name of the cricketer:Mohammed Shami
enter their height:168




cricketer no:  10
enter the name of the cricketer:Dinesh Karthik
enter their height:167




cricketer no:  11
enter the name of the cricketer:MS Dhoni
enter their height:176


{'Mayank Agarwal': '170', 'Rohit Sharma': '169', 'Hardik Pandya': '174', 'Virat Kohli ': '171', 'Jasprit Bumrah': '168', 'Kuldeep Yadav': '165', 'Shikhar Dhawan': '175', 'Ravindra Jadeja': '170', 'Mohammed Shami': '168', 'Dinesh Karthik': '167', 'MS Dhoni': '176'}
the captain is: MS Dhoni
'''

