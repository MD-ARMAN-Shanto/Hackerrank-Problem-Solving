# taking a list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int(input("Enter a Num\n"))  # taking the number which user want

# taking a new list to save the less number thn input
new_list = []

for element in a:
    if element < number:
        new_list.append(element)  # output as a list

print(new_list)


