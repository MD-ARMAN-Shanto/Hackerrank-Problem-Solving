# list overlapping

a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []

for i in a:
    for j in b:
        if i == j:
            new_list.append(i)


print(set(new_list))  # removing the duplicate number from the list

