import random

a = range(1, random.randint(1, 30))

b = range(1, random.randint(10, 40))

new_list = []

for num in a:
    if num in b:
        new_list.append(num)

print(new_list)


