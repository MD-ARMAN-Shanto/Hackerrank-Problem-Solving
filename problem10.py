# exercise 5 repeat
import random

a = range(1, random.randint(1, 40))
b = range(1, random.randint(10, 100))

new_list = []

for i in a:
    for j in b:
        if i == j:
            new_list.append(i)
print(set(new_list))