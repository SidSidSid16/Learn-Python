def km_to_miles(kilometers):
    return kilometers * 0.621371

kilometers = float(input("enter a value in kilometers: "))

print(round(km_to_miles(kilometers), 5))
