#nesting conditionals example

#ask user for a number
num = int(input("Enter a number: "))
#check if number is positive
if num > 0:
    print("Number is positive")
    #check if number is greater than 50
    if num > 50:
        print("Number is greater than 50")
    #check if number is less than 50
    elif num < 50:
        print("Number is less than 50")
    #number is 50
    else:
        print("Number is 50")
#check if number is negative
elif num < 0:
    print("Number is negative")
#number is 0
else:
    print("Number is 0")

#BMI calculator
#ask user for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
#calculate BMI
bmi = round(weight / (height ** 2))
#check if BMI is less than 18.5
if bmi < 18.5:
    print("You are underweight")
#check if BMI is between 18.5 and 24.9
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are normal weight")
#check if BMI is between 25 and 29.9
elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight")
#check if BMI is greater than 30
elif bmi > 30:
    print("You are obese")
#display BMI
print("Your BMI is", bmi)
