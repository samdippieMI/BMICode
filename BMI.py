# New Features added, change to last print 
# Python code to crete BMI Calc funcationality 

import math as m 


def BMI (): 
    weight = int(input ("Please enter your weight (kgs): "))
    hight = int(input("Please enter your hight (cm): "))

    bmi = (weight / (pow(hight,2)))* 10000

    print ("Your BMI is:", bmi )
    # test 
    
BMI()

