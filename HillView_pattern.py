k = 10
for row in range(k):
    for col in range(row+1, k):
        print('  ', end=' ')

    for col in range(row):
        print('* ', end=' ')

    for col in range(row+1):
        print('* ', end=' ')

    print()
