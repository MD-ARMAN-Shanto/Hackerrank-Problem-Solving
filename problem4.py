# find out divisors of any number
number = int(input("Enter any number\n"))

new_list = []
x = list(range(1, number+1))  # make a range list of divisors

for i in x:
    if number % i == 0:
        new_list.append(i)

print(new_list)