"""
Author: Teije Koolenbrander
Assignment / Part: HW5 - Q1
Date due: October 26, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
initials = input("Enter the initials of the suspects:")
wrappers = input("Enter the candy wrappers: ")
suspects = ""
for i in initials:
    for j in wrappers:
        if i == j:
            suspects += j
if suspects != "":
    for letter in suspects:
        print(letter, "is a candy thief suspect")
else:
    print("No candy thief found")
