k = 10
for row in range(k):
    for col in range(row):
        print('  ', end=' ')
    for col in range(row, k):
        print('* ', end=' ')
    print()
