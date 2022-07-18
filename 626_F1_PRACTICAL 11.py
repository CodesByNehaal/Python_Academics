#!/usr/bin/env python
# coding: utf-8

# In[17]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#PRACTICAL 11 : Write a Python program to perform addition and multiplication of 2 matrices.


#input :  


#row = int(input("ENTER NO. OF ROWS IN MATRICES : "))           #taking matrix length by user.
#col = int(input("ENTER NO. OF COLUMNS IN MATRICES : "))

#initialise 'matrix1' as an empty list to store matrix values.
matrix1 = []
print("ENTER ELEMENTS OF FIRST 3x3 MATRIX : ")
  
#taking input from user using for loop.
for i in range(3):          #for loop for row entries
    list1 = []
    for j in range(3):      #for loop for column entries
         list1.append(int(input("ENTER THE ELEMENT : ")))
    matrix1.append(list1)
  
print("THE FIRST MATRIX IS : ")
# For printing the matrix
for i in range(3):
    for j in range(3):
        print(matrix1[i][j], end = " ")
    print()
    
    
#initialise 'matrix2' as an empty list to store matrix values.
matrix2 = []
print("ENTER ELEMENTS OF SECOND 3x3 MATRIX :")
  
#taking input from user using for loop.
for i in range(3):          #for loop for row entries
    list2 = []
    for j in range(3):      #for loop for column entries
         list2.append(int(input("ENTER THE ELEMENT : ")))
    matrix2.append(list2)
  
print("THE SECOND MATRIX IS : ")
# For printing the matrix
for i in range(3):
    for j in range(3):
        print(matrix2[i][j], end = " ")
    print()
    
#initialise sum as 2-d array and every element initialised to 0.
sum = [[0,0,0],[0,0,0],[0,0,0]]

# iterate through rows
for i in range(len(matrix1)):
   # iterate through columns
   for j in range(len(matrix1[0])):
       sum[i][j] = matrix1[i][j] + matrix2[i][j]       #adding the matrix elements and printing the result.
    
print("THE SUM OF THE MATRICES = \n")
for r in sum:
   print(r)


#initialise product as 2-d array and every element initialised to 0.
product = [[0,0,0],[0,0,0],[0,0,0]]

#iterate through rows of matrix1
for i in range(len(matrix1)):
#iterate through columns of matrix2
   for j in range(len(matrix2[0])):
#iterate through rows of matrix2
       for k in range(len(matrix2)):
           product[i][j] += matrix1[i][k] * matrix2[k][j]       #multplying the matrices and printing the values.

print("THE PRODUCT OF THE TWO MATRICES = \n")
for s in product:
   print(s)



#OUTPUT :
ENTER ELEMENTS OF FIRST 3x3 MATRIX : 
ENTER THE ELEMENT : 1
ENTER THE ELEMENT : 2
ENTER THE ELEMENT : 3
ENTER THE ELEMENT : 4
ENTER THE ELEMENT : 5
ENTER THE ELEMENT : 6
ENTER THE ELEMENT : 7
ENTER THE ELEMENT : 8
ENTER THE ELEMENT : 9
THE FIRST MATRIX IS : 
1 2 3 
4 5 6 
7 8 9 
ENTER ELEMENTS OF SECOND 3x3 MATRIX :
ENTER THE ELEMENT : 9
ENTER THE ELEMENT : 8
ENTER THE ELEMENT : 7
ENTER THE ELEMENT : 6
ENTER THE ELEMENT : 5
ENTER THE ELEMENT : 4
ENTER THE ELEMENT : 3
ENTER THE ELEMENT : 2
ENTER THE ELEMENT : 1
THE SECOND MATRIX IS : 
9 8 7 
6 5 4 
3 2 1 
THE SUM OF THE MATRICES = 

[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
THE PRODUCT OF THE TWO MATRICES = 

[30, 24, 18]
[84, 69, 54]
[138, 114, 90]


# In[ ]:




