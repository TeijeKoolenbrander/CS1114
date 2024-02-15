"""
Author: [Teije Koolenbrander]
Assignment / Part: HW2 - Q2
Date due: September 28, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math
frequency = float(input("Enter the value for the frequency, w: "))
duration = float(input("Enter a value for the duration of the sound wave, T: "))
amplitude_spectrum = round((2 * math.sin(frequency * duration))/frequency, 3)
print("The amplitude spectrum of this Fourier transform is: ", amplitude_spectrum)
