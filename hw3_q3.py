"""
Author: Teije Koolenbrander
Assignment / Part: HW3 - Q3
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import random
start = input("Would you like to play 'Twenty-One'? [y/n] ")
while start != "y" and start != "n":
    start = input("Would you like to play 'Twenty-One'? [y/n]")
if start == "y":
    card_one = random.randrange(1, 12)
    card_two = random.randrange(1, 12)
    print("Your cards are worth ", card_one, " and ", card_two, ".", sep="")
    draw_card = input("Would you like another card? [y/n] ")
    while draw_card != "y" and draw_card != "n":
        draw_card = input("Would you like another card? [y/n] ")
    if draw_card == "y":
        card_three = random.randrange(1, 12)
        total_score = card_one + card_two + card_three
    else:
        total_score = card_one + card_two
    print("Your score is ", total_score, "!", sep="")
    opponent_score = random.randrange(0, 101)
    while opponent_score > 33 or opponent_score < 3:
        opponent_score = random.randrange(0, 101)
    print("Your opponent's score is ", opponent_score, "!", sep="")
    if opponent_score == total_score or opponent_score > 21 and total_score > 21:
        print("It's a draw!")
    elif opponent_score > total_score and opponent_score <= 21 or total_score > 21:
        print("Your opponent wins! Their score was ", opponent_score, ".", sep="")
    else:
        print("You win! Your score was ", total_score, ".", sep="")
else:
    print("Thank you for playing!")
