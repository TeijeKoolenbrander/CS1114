"""
Author: Teije Koolenbrander
Assignment / Part: HW5 - Q2
Date due: October 26, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
def get_decimal_time(hour, minute, second):
    initial_time = hour * 3600 + minute * 60 + second
    total_hours = initial_time // 10000
    total_minutes = initial_time % 10000 // 100
    total_seconds = initial_time % 10000 % 100
    return str(total_hours) + ":" + str(total_minutes) + ":" + str(total_seconds)

def get_decimal_date(month, day , year):
    import math
    french_year = year - 1792
    french_decade = math.ceil(day / 10)
    if month == 1:
        french_month = "Nivôse"
    elif month == 2:
        french_month = "Pluviôse"
    elif month == 3:
        french_month = "Ventôse"
    elif month == 4:
        french_month = "Germinal"
    elif month == 5:
        french_month = "Floréal"
    elif month == 6:
        french_month = "Prairial"
    elif month == 7:
        french_month = "Messidor"
    elif month == 8:
        french_month = "Thermidor"
    elif month == 9:
        french_month = "Fructidor"
    elif month == 10:
        french_month = "Vendémiaire"
    elif month == 11:
        french_month = "Brumaire"
    else:
        french_month = "Frimaire"
    return str(day) + " " + str(french_month) + " Year " + str(french_year) + " Décade " + str(french_decade)

def get_french_datetime(gregorian_datetime):
    hour_split = gregorian_datetime.find(":")
    minute_split = gregorian_datetime.find(":", hour_split + 1)
    second_split = gregorian_datetime.find(" ")
    month_split = gregorian_datetime.find("/")
    day_split = gregorian_datetime.find ("/", month_split + 1)
    hour = int(gregorian_datetime[:hour_split])
    minute = int(gregorian_datetime[hour_split+1:minute_split])
    second = int(gregorian_datetime[minute_split+1:second_split])
    month = int(gregorian_datetime[second_split+1:month_split])
    day = int(gregorian_datetime[month_split+1:day_split])
    year = int(gregorian_datetime[day_split+1:])
    return get_decimal_time(hour, minute, second) + "\n" + get_decimal_date(month, day, year)
