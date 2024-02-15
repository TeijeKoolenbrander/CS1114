"""
Author: Teije Koolenbrander
Assignment / Part: HW3 - Q4
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math
a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))
formula = b ** 2 - (4 * a * c)
if a == 0 and b == 0 and c == 0:
    print("This equation has infinite solution")
elif a == 0:
    print("This equation has no solution")
elif formula < 0:
    print("This equation has no real solution")
elif formula == 0:
    solution = (-1 * b)/(2 * a)
    print("This equation has 1 solution: x =", solution)
else:
    solution_one = ((-1 * b) + math.sqrt(formula))/(2 * a)
    solution_two = ((-1 * b) - math.sqrt(formula))/(2 * a)
    print("This equation has 2 solutions: x = ", solution_one, "and x =", solution_two)
