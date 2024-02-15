"""
Author: Teije Koolenbrander
Assignment / Part: HW3 - Q5
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
integer = int(input("Please enter a positive integer: "))
variable = integer
for num in range(0, integer):
    print(" " * num, "*" * (2 * variable - 1), sep = "")
    variable -= 1
for num in range(1, integer):
    print(" " * (integer - 2), "*" * (2 * num + 1), sep = "")
    integer -= 1
