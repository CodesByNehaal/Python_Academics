#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#DATE : 03/06/2021.

#PRACTICAL 6 : Write a Python program to print different patterns.

#INPUT
ROW = int(input("Enter the number of rows : "))            #taking no. of rows from user.            
#outer loop to handle number of rows
for i in range(0, ROW):                                    #values is changing according to outer loop 
     for j in range(0, ROW + 1):                           #inner loop to handle number of columns
             print("* ", end="")                           #printing stars
     print("\n")                                           #printing new lines.
                  
        
#OUTPUT
Enter the number of rows : 5
* 

* * 

* * * 

* * * * 

* * * * * 



#INPUT 
ROW = int(input("Enter the number of rows : "))            #taking no. of rows from user.            
#outer loop to handle number of rows
for i in range(0, ROW):                                    #values is changing according to outer loop 
     for j in range(0, ROW - i):                           #inner loop to handle number of columns
             print("* ", end="")                           #printing stars
     print("\n")                                           #printing new lines.
                 
    
#OUTPUT
Enter the number of rows : 5
* * * * * 

* * * * 

* * * 

* * 

* 



#INPUT
ROW = int(input("Enter the number of rows : "))            #taking no. of rows from user. 
temp = 2*ROW-2                                             #temp variable to store no. of spaces.
for i in range(0,ROW):                                     #outer loop to handle number of rows(new line)
    for j in range(0,temp):                                #inner loop to handle number of columns(spaces)
        print(end=(" "))                                   #printing spaces
    temp = temp - 2
    for k in range (0,i+1):                                #inner loop to handle number of columns(stars)
        print("* ", end=(""))                              #printing stars
    print("\n")                                            #printing new line.
    

#OUTPUT
Enter the number of rows : 8
              * 

            * * 

          * * * 

        * * * * 

      * * * * * 

    * * * * * * 

  * * * * * * * 

* * * * * * * * 



#INPUT
rows = int(input("Enter the number of rows : "))            #taking no. of rows from user 
temp = (2 * rows) - 2                                       
for i in range(0, rows):                                    #outer loop to handle number of rows
    for j in range(0, temp):                                #inner loop for spaces.
        print(end=" ")                                      #printing spaces.
    temp = temp - 1                                         #decrementing temp after each loop  
    for j in range(0, i + 1):                               #inner loop for stars
        print("*", end=' ')                                 #printing full Triangle pyramid using stars
    print(" ")                                              
    
    
 #OUTPUT
Enter the number of rows : 10
                  *  
                 * *  
                * * *  
               * * * *  
              * * * * *  
             * * * * * *  
            * * * * * * *  
           * * * * * * * *  
          * * * * * * * * *  
         * * * * * * * * * *  
        
        
        
#INPUT
rows = int(input("Enter the number of rows : "))            #taking no. of rows from user 
k = 2 * rows - 2                                            #It is used to print space 
for i in range(rows, -1, -1):                               #outer loop in reverse order    
    for j in range(k, 0, -1):                               #Inner loop will print the number of space.
        print(end= " ")                                                        
    k = k + 1  
    
    for j in range(0, i + 1):                              #This inner loop will print the number o stars                              
        print("*", end=" ")                                #printing stars
    print("")  
    
    
#output
Enter the number of rows : 10
                  * * * * * * * * * * * 
                   * * * * * * * * * * 
                    * * * * * * * * * 
                     * * * * * * * * 
                      * * * * * * * 
                       * * * * * * 
                        * * * * * 
                         * * * * 
                          * * * 
                           * * 
                            * 

