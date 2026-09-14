rubles, coins, quantity = map(int, input().split())

print(rubles * quantity + coins * quantity // 100, 'руб.', coins * quantity % 100, 'коп.', sep=' ')
