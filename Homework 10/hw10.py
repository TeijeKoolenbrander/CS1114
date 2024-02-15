"""
Author: Teije Koolenbrander
Assignment / Part: HW10 - Q1, Q2, Q3.
Date due: December 09, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import random

class Instrument:
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength

    def does_break(self):
        break_strength = self.strength / 2
        random_float = random.uniform(0,1)
        return break_strength > random_float

    def __str__(self):
        return f"{self.brand} {self.model} ({self.strength * 100} / 100 strength)"

class Musician:
    def __init__(self, stage_name, instruments):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(instruments)

    def pick_instrument(self, instrument_index = None):
        if self.number_of_instruments == 0:
            return None
        elif instrument_index == None:
            return self.instruments[random.randrange(0, self.number_of_instruments)]
        elif instrument_index > self.number_of_instruments - 1:
            return self.instruments[-1]
        else:
            return self.instruments[instrument_index]

    def __str__(self):
        if self.number_of_instruments == 0:
            return f"Musician object '{self.stage_name}', owning no instruments"
        elif self.number_of_instruments == 1:
            return f"Musician object '{self.stage_name}', owning a {self.instruments[0]}"
        else:
            instrument_list = ", ".join([str(instrument) for instrument in self.instruments[:-1]])
            return f"Musician object '{self.stage_name}', owning a {instrument_list}, and a {self.instruments[-1]}"

def get_name_of_battle_winner(one, two):
    weapon_one = one.pick_instrument()
    print(f"{one.stage_name} picked a {weapon_one}")
    weapon_two = two.pick_instrument()
    print(f"{two.stage_name} picked a {weapon_two}")
    if weapon_one == None and weapon_two == None:
        return "NO CONTEST"
    elif weapon_one == None:
        return two.stage_name
    elif weapon_two == None:
        return one.stage_name

    if weapon_one.strength > weapon_two.strength:
        if weapon_one.does_break():
            print(f"{one.stage_name}'s {weapon_one.model} broke!")
            return two.stage_name
        else:
            return one.stage_name
    elif weapon_two.strength > weapon_one.strength:
        if weapon_two.does_break():
            print(f"{two.stage_name}'s {weapon_two.model} broke!")
            return one.stage_name
        else:
            return two.stage_name
    else:
        print("Both musician's instruments are the same strength. The winner will be decided by the whim of chance.")
        if random.randrange(0, 2) == 1:
            return one.stage_name
        else:
            return two.stage_name

def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]
    # Let's say both musicians have access to the same gear
    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)
    # Testing the get_name_of_battle_winner method a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!", end="\n\n")

main()
