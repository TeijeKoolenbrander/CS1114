"""
Author: Teije Koolenbrander
Assignment / Part: HW6 - Q1
Date due: November 02, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
def calculate_grade(assignment_score, midterm_score, final_score):
    total_assignment = assignment_score * 0.4
    total_midterm = midterm_score * 0.3
    total_final = final_score * 0.3
    return total_final + total_midterm + total_assignment

def get_valid_score(prompt):
    request_score = "Enter a score for " + prompt + ": "
    score = input(request_score)
    while not score.isdigit() or float(score) > 100 or float(score) < 0:
        print("Invalid, Enter a numeric value between 0 and 100.")
        score = input(request_score)
    return float(score)

def display_result(grade):
    if grade >= 90:
        print(f"Grade:{grade:.2f}. Outstanding performance")
    elif grade >= 80:
        print(f"Grade:{grade:.2f}. Good work")
    elif grade >= 70:
        print(f"Grade:{grade:.2f}. Can improve")
    elif grade >= 60:
        print(f"Grade:{grade:.2f}. Passed")
    else:
        print(f"Grade:{grade:.2f}. Failed")

def main():
    assignment_score = get_valid_score("Assignments")
    midterm_score = get_valid_score("Midterm")
    final_score = get_valid_score("Final")
    calculated_grade = calculate_grade(assignment_score, midterm_score, final_score)
    display_result(calculated_grade)
