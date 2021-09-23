import os
from os import system
system('clear')

array = (87, 10, 2, 46, 22, 19, 66)

print(type(array))
print(array)
for number in array:
    print(number)
#List
cars = ["BMW", "Audi", "VW", "Ford", "Honda", "Chevy"]
print(cars)
print(type(cars))
cars.sort()
for car in cars:
    print(car)

    numbers = [6, 3, 8, 1, 2, 8, 3]
print("Before sorting list")
for n in numbers:
    print(n)
print()
print("After sorting the list")
numbers.sort()
for n in numbers:
    print(n)