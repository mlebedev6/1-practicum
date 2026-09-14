from math import pi

r_first = int(input())
r_second = int(input())
if r_first > r_second:
    print(pi * (r_first ** 2 - r_second ** 2))
else:
    print(pi * (r_second ** 2 - r_first ** 2))
