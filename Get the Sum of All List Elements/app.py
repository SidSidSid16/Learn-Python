def get_sum_of_elements(list):
    return sum(list)

totalElements = int(input("how many numbers are in the list? "))

list = []

for n in range(totalElements):
    number = float(input('enter number: '))
    list.append(number)

print(get_sum_of_elements(list))
