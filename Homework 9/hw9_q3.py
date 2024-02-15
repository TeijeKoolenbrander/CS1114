"""
Author: Teije Koolenbrander
Assignment / Part: HW9 - Q3
Date due: November 23, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
def word_frequency_counter_from_file(path):
    try:
        with open(path, "r") as file:
            dict = {}
            file_lines = [line.strip().split() for line in file]
            word_list = [word for line in file_lines for word in line]
            for line in file_lines:
                for word in range(len(line)):
                    if line[word] not in dict:
                        dict[line[word]] = (word_list.count(line[word]), [word])
                    else:
                        dict[line[word]][1].append(word)
            return dict
    except:
        print("Error: Unable to read the file. Please check the file path.")
        return None
