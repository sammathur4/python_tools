a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(a)):
    a.remove(a[i])
    a.append(11)
print(a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iterator = iter(a)
next(iterator)

for i in iterator:
    a.remove(i)
    a.append(11)

print(a)

a.sort()