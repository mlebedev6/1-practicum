rows = int(input())
colomns = int(input())
number = int(input())

print((number - 1) // (rows * colomns) + 1, 'страница', ((number - 1) % (rows * colomns) // rows + 1), 'столбец', ((number - 1) % (rows * colomns) % rows + 1), 'строка', sep=' ')