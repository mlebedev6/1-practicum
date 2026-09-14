weight = float(input()) / 2.205
height = float(input()) * 2.54 / 100

imt = weight / (height ** 2)

print(f"{imt:.2f}")