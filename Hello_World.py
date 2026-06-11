print('Hello World')

# Variables in Python
# So basically, i can use variables to get something stored in them
# things like first name, user id, country, location, age, approximations etc.
# These can be string, numeric, or even boolean
first_name = 'Usama'
last_name = 'Rashid'
country = 'Pakistan'
city = 'Rawalpindi'
age = 28
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python', "Project Management"] # Is this a list? Can't recall. Dont reckon i can change it tho
person_info = { # Ah, this is definitely a dictionary. Key value chain (or something)
   'firstname':'Usama',
   'lastname':'Rashid',
   'country':'Pakistan',
   'city':'Rawalpindi'
   } # I can plug the rest of the deets here too but im lazy ngl


print('Hello, World!') # The text Hello, World! is an argument. Argument is what resides inside the brackets.
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument since len is a single argument


# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Usama', 'Rashid', 'Pakistan', 28, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Different python data types
# Let's declare variables with various data types

first_name = 'Usama'     # str
last_name = 'Rashid'       # str
country = 'Pakistan'         # str
city= 'Rawalpindi'            # str
age = 28                  # int, It pains me how old im getting

# Printing out types
print(type('Usama'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Usama'}))    # dict - can plug in more here, but this is just to make a point about types
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip


# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Usama'
print(first_name)               # 'Usama'
first_name_to_list = list(first_name)
print(first_name_to_list)          