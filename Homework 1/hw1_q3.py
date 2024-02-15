"""
Author: Teije Koolenbrander
Assignment / Part: HW1 - Q3
Date due: September 21, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
print("Enter number of coins: ")
quarters = int(input("Number of quarters: "))
dimes = int(input("Number of dimes: "))
nickels = int(input("Number of nickels: "))
pennies = int(input("Number of pennies: "))
total = quarters / 4 + dimes / 10 + nickels / 20 + pennies / 100
print("The total is", int(total // 1), "dollar(s) and", int(total % 1 * 100), "cent(s)")