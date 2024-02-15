"""
Author: Teije Koolenbrander
Assignment / Part: HW3 - Q1
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
print("Welcome to the Lemonade Stand Profit Calculator!")
season = input("Enter the current season (summer/other): ")
small_cups = int(input("Enter the number of small cups of lemonade sold: "))
medium_cups = int(input("Enter the number of medium cups of lemonade sold: "))
large_cups = int(input("Enter the number of large cups of lemonade sold: "))
if season == "summer":
    small_profit = small_cups * (2-1)
    medium_profit = medium_cups * (2.5-1.25)
    large_profit = large_cups * (3-1.5)
    time = "summer : $"
else:
    small_profit = small_cups * (1.5-0.75)
    medium_profit = medium_cups * (2-1)
    large_profit = large_cups * (2.5-1.25)
    time = "rest of the year : $"
total_profit = small_profit + medium_profit + large_profit
print("Total profit for the day in the ", time, total_profit, sep="")
