def difference_min_max(list):
    return max(list) - min(list)

numberOfElements = int(input("enter total elements in the list: "))

list = []

for i in range(numberOfElements):
    list.append(float(input("enter a number to add in list: ")))

print(difference_min_max(list))
