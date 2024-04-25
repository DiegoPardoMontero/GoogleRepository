def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print("Hi, this is a simple program to help you calculate the n number of fibonacci series")
input("Press any key when you are ready")

number = input("\nGive me a number: ")
number = int(number)

print("The fibonnaci for the number " + str(number) + " = " + str(fibonacci(number)))
print("Thanks for using my program!")
