#!/usr/bin/env python
# coding: utf-8

# In[9]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#DATE : 03/06/2021.

#PRACTICAL 3 : To accept students five courses marks and compute his/her result. 
               #Student is passing if he/she scores marks equal to and above 40 in each course. 
               #If student scores aggregate greater than 75%, then the grade is distinction. 
               #If aggregate is 60>= and <75 then the grade is first division. 
               #If aggregate is 50>= and <60, then the grade is second division. 
               #If aggregate is 40>= and <50, then the grade is third division.
            
            
#INPUT
sub1 = int(input("ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 1 = ")) #TAKING MARKS OBTAINED OUT OF 100  BY USER.
sub2 = int(input("ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 2 = "))
sub3 = int(input("ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 3 = "))
sub4 = int(input("ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 4 = "))
sub5 = int(input("ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 5 = "))

#CHECKING WHETHER THE STUDENT SCORED ABOVE 40 IN EVERY UBJECT. IF YES, HE PASSES THE EXAMINATION. ELSE, HE FAILS...

if sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40 and sub5>=40:
    print("STUDENT HAS PASSED THE EXAMINATION.")
    sum = sub1 + sub2 + sub3 + sub4 + sub5    #CALC. THE SUM OF ALL THE MARKS AND PRINT. 
    print("total marks out of 500 = ",sum)
    per= (sum/500)*100                        #CALC. PERCENTAGE AND PRINTING.
    print("percentage = ",per,"%")
    if per>=75:                               #If student scores aggregate greater than 75%, then the grade is distinction.
        print("GRADE : distinction")
    elif per<75 and per>=60:                  #If aggregate is 60>= and <75 then the grade is first division.
        print("GRADE : first division")
    elif per<60 and per>=50:                  #If aggregate is 50>= and <60, then the grade is second division. 
        print("GRADE : second division")
    else:                                     #else, the grade is third division.
        print("GRADE : third division")
else:                                         #if student fails to score 40 in atleast one subject, he fails.
    sum = sub1 + sub2 + sub3 + sub4 + sub5
    print("total marks out of 500 = ",sum)
    print("student has failed the examination.")
                    
    
#OUTPUT
#ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 1 = 98
#ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 2 = 91
#ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 3 = 80
#ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 4 = 86
#ENTER THE MARKS OBTAINED OUT OF 100 IN SUBJECT 5 = 92
#STUDENT HAS PASSED THE EXAMINATION.
#total marks out of 500 =  447
#percentage =  89.4 %
#GRADE : distinction


# In[ ]:





# In[ ]:




