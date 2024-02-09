# Python code to crete BMI Calc funcationality 
""""
import math as m 

a = 2
b = 3 

print(a+b)



def BMI (): 
    weight = int(input ("Please enter your weight (kgs): "))
    hight = int(input("Please enter your hight (cm): "))

    bmi = (weight / (pow(hight,2)))* 10000

    print ("Your BMI is:", bmi )
    print ("Latest version: 9/02/2024")
    # test 
    #new feature 
    #Hello World
    #new update


BMI()
"""

from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

@app.route('/')
def index():
    return render_template('BMI.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = calculate_bmi(weight, height)
    return f'Your BMI is: {bmi:.2f}'

if __name__ == '__main__':
    app.run(debug=True)


