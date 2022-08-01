"""
n = int(input("Enter number of elements : "))

#ar = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]  # Read input
ar = list(map(int, input().strip().split()))[:n]
print(ar)

"""

d = {}
x = int(input("Input of X : "))
for i in range(x):
    key = int(input("Take position value & data : "))
    data = input()
    d[key] = data
print(d)

k = int(input("Input of K : "))
k1 = input("Take position value & data : ")
d[k] = k1
print(d)

k2 = int(input("Take position value & data : "))
d.pop(k2)
print(d)
d.popitem()
print(d)
