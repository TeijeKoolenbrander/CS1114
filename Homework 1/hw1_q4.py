"""
Author: Teije Koolenbrander
Assignment / Part: HW1 - Q4
Date due: September 21, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
dollars = int(input("Enter amount of dollars: "))
cents = int(input("Enter amount of cents: "))
total = dollars + 0.01 * cents
quarters = int(total // 0.25)
dimes = int(total % 0.25 //0.1)
nickels = int(total % 0.25 % 0.1 // 0.05)
pennies = int(total % 0.25 % 0.1 % 0.05 // 0.01)
print (dollars, "dollars and", cents, "cents are:", quarters, "quarters,", dimes, "dimes,", nickels, "nickels and", pennies, "pennies")