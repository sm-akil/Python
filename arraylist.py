n = int(input())
arr = input()  # takes the whole line of n numbers
l = list(map(int, arr.split(' ')))
# split those numbers with space( becomes ['2','3','6','6','5']) and then map every element into int (becomes [2,3,6,6,5])
