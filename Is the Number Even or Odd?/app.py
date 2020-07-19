def isEvenOrOdd(number):
    if (number % 2) == 0:
        return "even"
    else:
        return "odd"

number = int(input("enter a number: "))

print(isEvenOrOdd(number))
