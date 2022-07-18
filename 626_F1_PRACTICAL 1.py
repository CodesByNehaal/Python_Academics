#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#DATE : 27/05/2021.
#PRACTICAL 1.1 : To accept an object mass in kilograms and velocity in meters per second and display its momentum and energy. Momentum=mc, Energy=mc2 where m is the mass of the object and c is its velocity

#INPUT
print("WELCOME TO PRACTICAL 1.1")                                    #print function helps to print our statements.
mass = int(input("enter the mass of the object in kg : "))           #mass stores the value of mass of the object which user enters.
velocity = int(input("enter the velocity of the object in m/s : "))  #velocity stores the value of velocity of the object which user enters. 
momentum = mass*velocity                                             #momentum = mc = mass * velocity
energy= mass*velocity**2                                             #energy = mass * velocity^2 ==> e=mc^2
print("\nThe energy of the object = ",energy,"Joules")               #value of energy will be displayed to user.
print("The momentum of the object = ", momentum, "kg-m/s")           #value of momentum will be displayed to user.


#OUTPUT:
WELCOME TO PRACTICAL 1.1
enter the mass of the object in kg : 80
enter the velocity of the object in m/s : 25

The energy of the object =  50000 Joules
The momentum of the object =  2000 kg-m/s



#PRACTICAL 1.2 : Find the area volume of any given shape like cube ,sphere or cuboid.

#INPUT
print("WELCOME TO PRACTICAL 1.2")                                        
print("***********************CUBE***************************")
side = int(input("ENTER THE LENGTH OF SIDE OF THE CUBE : "))         #taking the length of a side of cube from user.
print("\nAREA OF THE CUBE = ", 6*side**2, "unit sqr.")               #area(cube) = 6(side)^2 and displaying the result. 
print("VOLUME OF THE CUBE = ", side**3, "unit cube")                 #volume(cube) = side^3 and displaying the result.

print("\n\n******************CUBOID**************************")
len = int(input("ENTER THE LENGTH OF THE CUBOID : "))                #taking the dimensions of the cuboid from the user. (length,bredth,height)
wid = int(input("ENTER THE WIDTH OF THE CUBOID : "))
hgt = int(input("ENTER THE HEIGHT OF THE CUBOID : "))
area = 2*(len*wid + wid*hgt + hgt*len)                               #area(cuboid) = 2(lb + bh + lh)
vol = len*wid*hgt                                                    #volume(cuboid) = l*b*h
print("\nAREA OF THE CUBOID = ", area, "unit sqr.")                  #displaying the results to the user.
print("VOLUME OF THE CUBOID = ", vol, "unit cube")

print("\n\n******************SPHERE**************************")
rad = int(input("ENTER THE RADIUS OF THE SPHERE : "))                #taking the radius of the sphere.
AREA = 4*3.14*rad**2                                                 #area = 4*pi*radius^2
volume = 4/3*3.14*rad**3                                             #volume = $/3*pi*radius^3
print("\nAREA OF THE CUBOID = ", AREA, "unit sqr.")                  #displaying the result to the user.
print("VOLUME OF THE CUBOID = ", volume, "unit cube")


#OUTPUT
WELCOME TO PRACTICAL 1.2
***********************CUBE***************************
ENTER THE LENGTH OF SIDE OF THE CUBE : 5

AREA OF THE CUBE =  150 unit sqr.
VOLUME OF THE CUBE =  125 unit cube


******************CUBOID**************************
ENTER THE LENGTH OF THE CUBOID : 1
ENTER THE WIDTH OF THE CUBOID : 2
ENTER THE HEIGHT OF THE CUBOID : 3

AREA OF THE CUBOID =  22 unit sqr.
VOLUME OF THE CUBOID =  6 unit cube


******************SPHERE**************************
ENTER THE RADIUS OF THE SPHERE : 5 
    
AREA OF THE CUBOID =  314.0 unit sqr.
VOLUME OF THE CUBOID =  523.3333333333334 unit cube



#PRACTICAL 1.3 : Calculate the percentage loss or the percentage profit by taking the cost price & selling price from the user

print("WELCOME TO PRACTICAL 1.3") 
CP = int(input("ENTER THE COST PRICE OF THE PRODUCT : "))          #taking cost price(CP) 0f the product from user.
SP = int(input("ENTER THE SELLING PRICE OF THE PRODUCT : "))       #taking selling price(SP) of the product from user.
gains = SP-CP                                                      #the difference in selling price and cost price tells us about the profits made or loss incurred. (p/l)
percent = gains/CP*100                                             #p/l percentage = "p/l"/CP * 100
print("P/L of the seller = ", gains)                               #displaying the results.
print("P/L PERCENTAGE = ", percent, "%")


#OUTPUT
WELCOME TO PRACTICAL 1.3
ENTER THE COST PRICE OF THE PRODUCT : 100
ENTER THE SELLING PRICE OF THE PRODUCT : 80
P/L of the seller =  -20
P/L PERCENTAGE =  -20.0 %



#PRACTICAL 1.4 : To calculate the mileage of a bike or car in KMPL. Input: Distance traveled in Meters and Amount of fuel used in Millilitres.

#INPUT : 
print("WELCOME TO PRACTICAL 1.4")
metre = int(input("ENTER THE DISTANCE TRAVELLED BY VEHICLE IN m : "))    #taking the distance travelled in meters from user.
mililitre = int(input("ENTER THE AMOUNT OF FUEL USED IN ml : "))         #taking fuel burnt to travel that distance in mililitres from user.
mileage = metre/mililitre                                                #mileage = metre/mililitre. hence here mileage is in mpml.
print("\nMILEAGE OF THE VEHICLE = ", mileage, "KMPL")                    #since kmpl = mpml, we dont convert and write the unit as kmpl.


#OUTPUT :
WELCOME TO PRACTICAL 1.4
ENTER THE DISTANCE TRAVELLED BY VEHICLE IN m : 1500
ENTER THE AMOUNT OF FUEL USED IN ml : 200

MILEAGE OF THE VEHICLE =  7.5 KMPL





