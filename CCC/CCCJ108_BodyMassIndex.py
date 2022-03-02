"""

The Body Mass Index (BMI) is one of the calculations used by doctors to assess an adult's health. The doctor measures
the patient's height (in metres) and weight (in kilograms), then calculates the BMI using the formula:

bmi = weight / height * height

Write a program which takes the patient's weight and height as input, calculates the BMI, and displays the corresponding
message from the table below.

BMI Category	Message
More than 25 Overweight
Between 18.5 and 25 (inclusive)	Normal weight
Less than 18.5 Underweight


"""

w = float(input())
h = float(input())

BMI = w / (h * h)

print(BMI)
if BMI > 25:
    print("Overweight")
elif 18.5 < BMI <= 25.0:
    print("Normal weight")
else:
    print("Underweight")
