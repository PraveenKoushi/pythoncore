some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
print(some_list)

dup_list = []

for value in some_list:
    if some_list.count(value) > 1 and value not in dup_list:
        dup_list.append(value)

print(dup_list)
