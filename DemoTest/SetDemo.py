employee = {100, 100, 111, 112, 115}


print("employees IDs", employee)
employee.add(113)
print("employees new ID adding", employee)

abc = ['a', 'b', 'c']

employee.update(abc)
print("Update set ", employee)

remove = employee.discard('a')
print("remove", employee)

for se in employee:
    print(se)

a = {1, 3, 5}
b = {0, 2, 5, 4}

print(a | b)
print(a.union(b))

print(a & b)

print(a - b)
print(a ^ b)