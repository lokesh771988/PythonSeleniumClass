# empty list
list = []

# assigning values
list1 = [1, 2, 3]

# multiple types values
list2 = [1, 'lokesh', 5.5, 5, 10, -1, 'a', 'b']


list2.append('Testing')

print(list2)

list3 = [1, 2, 3]
list4 = [4, 5, 6]
print(" List 3rd values ", list3)
print(" List 4th values ", list4)

list3.extend(list4)
print("after extend list", list3)

abc = ['a', 'b', 'c']
abc[1] = 'Testing'
print("before delete list values ", abc)

del abc[0]
print("after delete value from list", abc)
abc.remove('c')
print("after remove value from list", abc)

abc1 = [1, 2, 3, 4, 5]
abc1.reverse()
print("reverse list", abc1)

for ab in abc1:
    print(ab)

print(5 in abc1)

abc2 = [1, 2, 3, 4, 5, [1, 2, 3], [4, 5, 6]]

print(abc2[0:5])