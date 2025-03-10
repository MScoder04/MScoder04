height = float(input("Enter height in centimeters: "))
weight = float(input("Enter weight in kilograms: "))
BMI = weight/(height/100)**2
if BMI<=18.4:
    print("You are underweight.")
elif BMI<=24.9:
    print("You are healthy")
elif BMI<=29.9:
    print("You are overweight.")
elif BMI<=34.9:
    print("You are severly overweight.")
elif BMI<=39.9:
    print("You are obese.")
else:
    print("You are severly obese.")