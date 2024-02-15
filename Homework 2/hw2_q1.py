"""
Author: [Teije Koolenbrander]
Assignment / Part: HW2 - Q1
Date due: September 28, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math
guests = int(input("Enter the number of guests: "))
slices = int(input("Enter the number of pizza slices each guest will eat: "))
total_slices = guests * slices
whole_pizzas = math.ceil(total_slices / 8)
left_over = whole_pizzas * 8 - total_slices
print("Minimum number of whole large pizzas required: ", whole_pizzas)
print("Total number of large pizza slices needed: ", total_slices)
print("Number of large pizza slices left over: ", left_over)