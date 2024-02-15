"""
Author: [Teije Koolenbrander]
Assignment / Part: HW2 - Q4
Date due: September 28, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
days_neha = int(input("Enter the number of days Neha has worked: "))
hours_neha = int(input("Enter the number of hours Neha has worked: "))
minutes_neha = int(input("Enter the number of minutes Neha has worked: "))
days_oleg = int(input("Enter the number of days Oleg has worked: "))
hours_oleg = int(input("Enter the number of hours Oleg has worked: "))
minutes_oleg = int(input("Enter the number of minutes Oleg has worked: "))
neha_time = (days_neha * 1440) + (hours_neha * 60) + minutes_neha
oleg_time = (days_oleg * 1440) + (hours_oleg * 60) + minutes_oleg
total_minutes = neha_time + oleg_time
final_days = total_minutes // 1440
final_hours = total_minutes % 1440 // 60
final_minutes = total_minutes % 1440 % 60
print("The total time both CAs worked together is", final_days, "days,", final_hours, "hours and", final_minutes, "minutes")



