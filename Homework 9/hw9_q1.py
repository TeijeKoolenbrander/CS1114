"""
Author: Teije Koolenbrander
Assignment / Part: HW9 - Q1
Date due: November 23, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def group_students(clubs, students):
    return_list = []
    for item in clubs:
        student_list = []
        for names in students:
            if item[0] == names[1] and len(student_list) < item[1]:
                student_list.append(names[0])
        return_list.append(student_list)
    return return_list
