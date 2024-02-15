"""
Author: Teije Koolenbrander
Assignment / Part: HW9 - Q2
Date due: November 23, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def group_anagrams(path):
    try:
        with open(path, "r") as file:
            word_list = [line.strip() for line in file]
            return_list = []
            for word in word_list:
                letters = [char for char in word]
                letters.sort()
                count = 0
                for group in return_list:
                    if group[0] == letters:
                        group.append(word)
                        count += 1
                if count == 0:
                    return_list.append([letters, word])
            for item in return_list:
                item.pop(0)
            return return_list

    except:
        print("Error: Unable to read the file. Please check the file path.")
        return None
