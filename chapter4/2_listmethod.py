l = [3,4,-6,746,90,-4563,4654,90,8.34,1,4]

print(l)

l.append("afaque")
print(l)

l.pop()
print(l)

l.insert(0,"nishu")
print(l)

l.remove("nishu")
print(l)

l.sort()
print(l)

l.reverse()
print(l)

print(l.count(90))


l1 = [1,2,3,4,9]
l2 = [78,92,90,26]

l1.extend(l2)
print(l1)