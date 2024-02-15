"""
Author: [Teije Koolenbrander]
Assignment / Part: HW2 - Q3
Date due: September 28, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
gender = input("Enter your gender (F for female, M for male): ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: "))
if gender == "M":
    bee = 66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)
else:
    bee = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
print("Your BEE is: ", bee)
