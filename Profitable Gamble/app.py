def profitable_gamble(probability, prize, pay):
    if (probability * prize) > pay:
        return True
    else:
        return False

probability = float(input("enter the probability: "))
prize = float(input("enter the prize: "))
pay = float(input("enter the pay: "))

print(profitable_gamble(probability, prize, pay))
