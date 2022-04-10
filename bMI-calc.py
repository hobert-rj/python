from validInput import inputNum
height = inputNum("What is your height in cm? ", False, downLim=1)
mass = inputNum("What is your weight in kg? ", False, downLim=1)
age = inputNum("How old are you? ", downLim=1)
bmi = round(mass/(height/100)**2, 2)
if age > 18:
    if bmi < 16:
        result = "Underweight (Severe thinness)"
    elif bmi < 17:
        result = "Underweight (Moderate thinness)"
    elif bmi < 18.5:
        result = "Underweight (Mild thinness)"
    elif bmi < 25:
        result = "Normal"
    elif bmi < 30:
        result = "Overweight (Pre-obese)"
    elif bmi < 35:
        result = "Obese (Class I)"
    elif bmi < 40:
        result = "Obese (Class II)"
    else:
        result = "Obese (Class III)"
    print(f"The BMI is {bmi}, And based on that in range of {result}.")
else:
    print(f"The BMI is {bmi}\nBecause the age of subject is {age} years old, you should compare the bmi with typical values for other children of the same age and sex. Look for the charts!")
