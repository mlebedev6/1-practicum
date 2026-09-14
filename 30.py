att = int(input())
comp = int(input())
yds = int(input())
td = int(input())
inttt = int(input())

a = (comp / att - 0.3) * 5
b = (yds / att - 3) * 0.25
c = (td / att) * 20
d = 2.375 - ((inttt / att) * 25)

print((a + b + c + d) / 6 * 100)
