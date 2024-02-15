"""
Author: Teije Koolenbrander
Assignment / Part: HW9 - Q4
Date due: November 23, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def merge_intervals(intervals):
    intervals.sort()
    return_list = [intervals[0]]
    for values in intervals[1:]:
        if values[0] <= return_list[-1][1]:
            if values[1] <= return_list[-1][1]:
                return_list[-1] = (return_list[-1][0], return_list[-1][1])
            else:
                return_list[-1] = (return_list[-1][0], values[1])
        else:
            return_list.append(values)
    return return_list
