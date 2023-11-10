#binh phuong cac so le tu 1 den 11

#khai bao 1 list empty
odd_square = []
for x in range(1,11):
    if x % 2 == 1:
        odd_square.append(x**2)

print(odd_square)

# newList = [ expression(element) for element in oldList if condition ]
odd_square_2 = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square_2)

# tao list cac so chan
even_square = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_square)

list_input = ["Tin", "Tuan", "Tai"]
list_output = [x + " Student" for x in list_input]
print(list_output)



