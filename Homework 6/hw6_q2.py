"""
Author: Teije Koolenbrander
Assignment / Part: HW6 - Q2
Date due: November 02, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
def create_word_pyramid(string, int):
        pyramid_string = ""
        for i in range(1, int + 1):
                pyramid_string += ((chr(ord(string)+i-1) * i))
                pyramid_string += "\n"
        return pyramid_string
def add_pyramid_level(string):
        char = string[-2]
        new_level = chr(ord(char) + 1) * (string.count("\n") + 1)
        return string + new_level + "\n"
def count_pyramid_levels(string):
        return string.count("\n")
def main():
        char = 'B'
        levels = 5

        word_pyramid = create_word_pyramid(char, levels)
        print("Word Pyramid:")
        print(word_pyramid)

        updated_pyramid = add_pyramid_level(word_pyramid)
        print("Updated Word Pyramid:")
        print(updated_pyramid)
        print("Number of Levels in Pyramid:", count_pyramid_levels(updated_pyramid))
