"""
Author: Teije Koolenbrander
Assignment / Part: HW8 - Q2, Q3.
Date due: November 16, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def is_haiku(input_string):
    split_string = input_string.split("/")
    syllable_count = 0
    line_count = 0
    for value in split_string:
        for i in range(len(value)):
            if value[i] == ",":
                syllable_count += 1
        if value == split_string[0]:
            if syllable_count != 4:
                print("WARNING: The first line is not 5 syllables long.")
                return False
            syllable_count = 0
        elif value == split_string[1]:
            if syllable_count != 6:
                print("WARNING: The second line is not 7 syllables long.")
                return False
            syllable_count = 0
        elif value == split_string[2]:
            if syllable_count != 4:
                print("WARNING: The third line is not 5 syllables long.")
                return False
        elif len(split_string) > 3:
            print("WARNING: The text contains more than three lines.")
            return False
    return True

def haiku_string_parser(input_string):
    if is_haiku(input_string):
        return_string = input_string.replace("/", "\n")
        return_string = return_string.replace(",", "")
        return return_string
    else:
        return ""

def main():
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)

main()

