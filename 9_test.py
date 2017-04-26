a=['1','2']
print a
a.append('3')
print a
a.append(repr(4))
print a
a.append(5)
print a

for i in range(len(a)):
    print a[i]
