# prime number check

number = int(input("Enter a number\n"))
x = list(range(1,number+1))

for i in x:
    if number%i == 0:
        print("Its not a prime")
        break
    else:
        print("its a prime")
        break
