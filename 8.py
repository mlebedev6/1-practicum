pl = []

print("Введите плей-лист папы:")
while True:
    a = input()
    if not a:
        break
    pl.append(a)

print("Плей-лист мамы:")
for i in pl[::-1]:
    print(i)
