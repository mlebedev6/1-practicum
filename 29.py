from math import *

a, b, c = float(input()), float(input()), float(input())

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

ugol1 = degrees(asin(2 * s / (b * c)))
if b**2 + c**2 < a**2:
    ugol1 = 180 - ugol1

ugol2 = degrees(asin(2 * s / (a * c)))
if a**2 + c**2 < b**2:
    ugol2 = 180 - ugol2

ugol3 = 180 - ugol1 - ugol2

print(ugol1, ugol2, ugol3, sep='\n')
