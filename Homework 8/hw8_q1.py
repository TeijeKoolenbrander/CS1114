"""
Author: Teije Koolenbrander
Assignment / Part: HW8 - Q1
Date due: November 16, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def update_frequencies(frequency, sequence):
   frequency_list = []
   added_list = []
   for i in range(len(frequency)):
       count = 0
       for letter in sequence:
            if frequency[i][0] == letter:
                count += 1
       added_list.append(count)
       count += frequency[i][1]
       frequency_list.append(tuple([frequency[i][0],count]))
   print(f"Number of nucleotides added: A -> {added_list[0]} | C -> {added_list[1]} | T -> {added_list[2]} | G -> {added_list[3]}")
   return frequency_list

def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)
    print(new_frequencies)

main()
