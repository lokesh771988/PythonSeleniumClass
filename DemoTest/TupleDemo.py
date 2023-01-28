tup1 = ()
tup = (1, 2, 3)

print("empty tuple", tup1)
print("tuple values ", tup)
print("accessing tuple ", tup[1])

tup2 = ("test")
tup3 = ("test",)
print(type(tup2))
print(type(tup1))
print(type(tup3))
tup4 = (1, 2, 3, 4, 5, 6, 1, 1, 2, 3)
print(tup4[-1])
print(tup4[1:])
print(tup4[1:3])
print(tup4[:3])
print(tup4.count(1))
print(tup4.index(3))

for a in tup4:
    print(a)