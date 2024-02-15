"""
Author: Teije Koolenbrander
Assignment / Part: HW3 - Q2
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
days = int(input("Enter the number of days (1 to 100): "))
while days > 100 or days < 1:
    days = int(input("Enter a valid number of days (1 to 100): "))
total = 1
for steps in range(1, days):
    total += (steps * 2) + 1
print("The baby will have taken a total of", total, "steps after", days, "days.")
