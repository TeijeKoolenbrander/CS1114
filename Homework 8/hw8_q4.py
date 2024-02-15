"""
Author: Teije Koolenbrander
Assignment / Part: HW8 - Q4
Date due: November 16, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import statistics

def get_list_of_grades(grades_filepath):
    try:
        with open(grades_filepath, "r") as file:
            whole_list = []
            return_list = []
            for line in file:
                new_line = line.strip()
                whole_list.append(new_line.split(","))
            for column in range(5, len(whole_list[0])):
                grades_list = []
                for row in range(1, len(whole_list)):
                    if whole_list[row][column].isnumeric():
                        grades_list.append(float(whole_list[row][column]))
                return_list.append(grades_list)
            return return_list
    except:
        return

def generate_statistics_report(grades_filepath, stats_filepath = "score_stats.csv"):
    grades_list = get_list_of_grades(grades_filepath)
    try:
        with open(stats_filepath, "w") as file:
            file.write("Mean,Standard Deviation,Median\n")
            for value in grades_list:
                file.write(f"{statistics.mean(value)},{statistics.stdev(value)},{statistics.median(value)}\n")
    except:
        return

def main():
    grades = get_list_of_grades("Midterm1_scores.csv")
    print(grades)
    generate_statistics_report("Midterm1_scores.csv", "stats.csv")

main()
