# Day 2: 30 Days of python programming
# Trying this out
import math

first_name = 'Usama'
last_name = 'Rashid'
full_name = "Muhammad Usama Rashid"
country = 'Pakistan'
city = 'Rawalpindi'
age = 28
year = 2026
is_married = True
is_true = True
is_light_on = True
first_name_player_2, last_name_player_2 = 'Mah', 'Noor'



# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(first_name_player_2))
print(type(last_name_player_2))


length_first_name = len(first_name)
print(length_first_name)

print('Length of the first name is:', len(first_name))
print('Length of the last name is:', len(last_name))
# Trying to compare them by using a comparison operator
print(len(first_name) > len(last_name))

num_one = 5
num_two = 4
print('num_one = ',num_one)
print('num_two = ',num_two)

total = num_one + num_two
print('total =', total)

diff = num_one - num_two
print('diff = ',diff)

product = num_one * num_two
print('Product = ',product)

division = num_one/num_two
print('Division = ', division)

# What even was floor division again???
# Rounds off answer to the lower whole number
floor_division = num_one // num_two
print('Floor Division = ', floor_division)

exp = num_two ** num_one
print('Exp = ',exp)

# The radius if 30 meters
# We need the area of the circle
Area_Circle = 3.14159 * (30 ** 2)
print('Area of Circle = ', Area_Circle)

Circumference = 2 * math.pi * 30
print(f'Circumference is = {Circumference:.3f}')

radius = float(input('What is the radius of circle?'))

Circumference = 2 * math.pi * radius
Area_Circle = math.pi * (radius ** 2)

print('The Circumference of your circle is = ', Circumference)
print('The Area of the circle of radius ',radius, 'is', Area_Circle)

first_name = input('Input your first name ')
last_name = input('Input your last name ')
country = input('Input your country ')
age = input('Input your age ')


print("Your name is", first_name ,last_name, 'And your age is ',age, 'and you are from ', country)