def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print("Hi, this is a simple program to help you calculate the factorial of a number n")
input("Press any key when you are ready")

number = input("\nGive me a number: ")
number = int(number)

print("The factorial for the number " + str(number) + " = " + str(factorial(number)))
