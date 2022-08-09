"""
x = []
p = int(input())
for i in range(p):
    z = int(input())
    x.append(z)
print("Array list : ", x)
x.pop()
print("After pop : ", x)
x.append()

q = int(input())
x.append(q)
print("After Append:", q)
"""
"""
s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
"""

l = [1]
print("push:", l)
l.append(2)  # append 2
print("push:", l)
l.append(3)  # append 3
print("push:", l)
l.pop()  # pop 3
print("pop:", l)
print("peek:", l[-1])  # get top most element
l.pop()  # pop 2
print("pop:", l)
print("peek:", l[-1])  # get top most element
