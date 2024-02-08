# Python code to crete BMI Calc funcationality 

import math as m 


def BMI (): 
    weight = int(input ("Please enter your weight (kgs): "))
    hight = int(input("Please enter your hight (cm): "))

    bmi = (weight / (pow(hight,2)))* 10000

    print ("Your BMI is:", bmi )
    print ("Latest version: 9/02/2024")
    # test 
    #new feature 
    #Hello World

BMI()

