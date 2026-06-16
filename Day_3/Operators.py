# Git is a memory card for code
# Version control - save your progress so you dont lose it as you go
# Enter commands to save your progress
# Save them so if they get deleted, you can go back to last saved
# Initialize your folder or project with git
# Have git downloaded and installed
# Type git init (your memory card is in your system)
# Git add is how we save our progress
# Save all changes since last time we saved
# Or you can save something specific
# Add a file after git add if you want to save something specific
# Git add . would save everything.
# Most people push changes on everything
# Git add. is the most used
# All files are in saving
# Git commit actually saves those changes to memory
# Git commit - m 'This is the commit message'
# Git commit - m 'Add HTML and CSS file'
# Git add.
# I have a feeling git add. saves all changes since last change to staging
# Git commit -m committs those changes to memory along with a message
# Add the files you wanna save, and then committ
# Git log gives us our saved files. Its a log of all saved changes
# Github is a website like bitbucket and gitlab
# All saved progress on my local machine can go to the site
# Others can see the code and do whatever they want with it

"""
Git is a memory card for code.
Version control lets you save your progress so you don't lose it as you go.

Enter commands to save your progress.
Save them so if they get deleted, you can go back to the last saved version.

Initialize your folder or project with Git:
git init

Have Git downloaded and installed first.

git add stages your changes.
It saves changes since the last commit to the staging area.

You can stage a specific file:
git add filename

Or stage everything:
git add .

Most people commonly use:
git add .

All selected files are now staged and ready to be committed.

git commit actually saves those staged changes to Git's history.

git commit -m "This is the commit message"
git commit -m "Add HTML and CSS file"

Workflow:
1. git add .
2. git commit -m "Your message"

git add . stages all changes since the last commit.
git commit -m saves those staged changes permanently in Git's history along with a message.

Add the files you want to save, then commit them.

git log shows the commit history.
It is a log of all saved changes.

GitHub is a website for hosting Git repositories, similar to Bitbucket and GitLab.

All saved progress on your local machine can be pushed to GitHub.
Others can view, clone, and collaborate on your code depending on the repository's permissions.
"""


"""
Git is a memory card for code.
Version control lets you save your progress.
Use git init to initialize a repository.
Use git add . to stage all changes.
Use git commit -m "message" to save those changes.
Use git log to see commit history.
GitHub lets you store and share repositories online.
"""

"""
GIT NOTES

git init
    Creates a new Git repository.

git add .
    Stages all changed files.

git commit -m "message"
    Saves staged changes to the repository.

git log
    Shows commit history.

GitHub
    Online service for hosting Git repositories.


Repository is a folder. 
Git push pushes changes to github or the website in question
Website will have those changes.

By default, all code is in a master branch. Master memory
Someone else could trail off, and work on it in another branch.
Someone could make changes to my code in another branch
Git checkout -b new-branch
Checking change
M means changes are being tracked
.git folder contains all configuration files. We dont mess with this.
"""
name = 'Usama  Rashid'
dob = '1/1/2000'

string = 'Hello world' 
string2 = 'Eureka!!!'

now_try = 'Trying now'

''' Make a single functionality
Then make a commit
To make sure things are clean and trackable
Git status tells us the changes done locally
What changes occured after the recent commit

Staging area is local. ;
We need to shift files to staging area through git add
Git add . shifts new files to staging area. 
We can commit changes in staging area
Only changes in staging area are committed.

I can also revert to an older commit
Some mechanism to go back in case something wrong occurs
If our commmit history is good, we should be able to go back cleanly

Commits are like linked lists
Head points to the latest commit
Changing head to an older committ would do the same thing
Technically, that would remove the previously latest commit
We need to be careful when handling heads
We might lose a lot of our commits
We might need to remove only a single commit that is in the middle somewhere
git revert
git reset
Git basics are complete now
study git revert and git reset


Git is important for consistent coding
Across various machines and teams
Github
Gitlab
Bitbucket
We have several publically available servers where we can push and pull commits
History can remain on the cloud
That public server is called Github
They make a UI layer for us
Task management as well
We can make a server on our own as well if need be
Gitlab and bitbucket are paid, so people dont use them
Its a slightly social media type platform
Git init make a local repository
We made a repo on github, our remote server
Code on local machine needs to be told to be in sync with github
git remote -v











'''

print (True)
print (False)

# Equals sign means assigning a value in a variable, rather than equality
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2


# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j)) #Woah did that just do the actual calculation?
''' So if i place numbers after the comma, i can then print them out
BUT
If i write a calculation, with an operator, i can then print the number out as well
Wonder if this works with varibles as well. I might be able to calculate them out too
'''

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print('total = ', total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)


print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density




print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)


print ('1 is 1', 1 is 1) # This should be true ideally
print ('2 is not 1', 2 is not 1) # Now this ought to be false
print ('U in Usama Rashid', 'U'in 'Usama Rashid') # Gotta be careful here. Its not is in, its just in.
print ('coding' in 'I am coding') # This should be true as well
print ('coding' in 'I am coding in python') # This should be true as well
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True, I can use expressions and calculations as well


print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


print (True)
print (False)

print('Addition:', 1+2) # This shuold give me 3
print('Subtraction:', 2-1) # This should give me 1
print('Multiplication:', 2*3) # This should give me 6
print('Division:', 4/2) # DIvision in python would give me a floating number
print('Division:', 6/2) # This should give me 3.0
print ('Modulus:', 3%2) # This should give me 1, gives the remainder
print('Exponentiation:', 2**3) # This should give me 8, it means 2 * 2 * 2


# Exercise
Age = 28
Height = 35.5
Complex_Var = 1+2j
base = float(input('Enter base of triangle: '))
height = float(input('Enter height of triangle: '))
Area = 0.5 * base * height
print('Area of triangle:', Area)


Side_a = float(input('Enter side a: '))
Side_b = float(input('Enter side b: '))
Side_c = float(input('Enter side c: '))
Perimeter = Side_a + Side_b + Side_c
print('The Perimeter of triangle is: ', Perimeter)


length = float(input('Enter length: '))
width = float(input('Enter width: '))
Area = length * width
Parameter = 2 * (length + width)
print('Area of rectangle is: ', Area)
print('Perimeter of rectangle is: ', Parameter)


radius = float(input('Enter radius of circle: '))
Area = 3.14 * radius ** 2
Circumference = 2 * 3.14 * radius
print('Area of circle is: ', Area)
print('Circumference of circle is: ', Circumference)


''' How to do this in code
Ive got an equation, y=2x-2
I need to calculate its slope and intercepts
I also need to do this in code
The equation is provided to me


'''


slope = 2

y_intercept = (0, -2)

x_intercept = (1, 0)

print("Slope:", slope)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)



(x1, y1) = (2, 2)  # Y-intercept
(x2, y2) = (6, 10) # X-intercept
m = (y2-y1)/(x2-x1)
print("Slope:", m)
Euclidean_distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("Euclidean distance between points:", Euclidean_distance)

print(slope == m)  # True, because the slope from the equation and the calculated slope are equal

x =float(input("Enter value for x: "))
y = x**2 + 6*x + 9
print("Value of y:", y)


print(len('python') > len('dragon'))   # False
print('on' in 'python' and 'on' in 'dragon') # True


print('on' in 'python' and 'on' in 'dragon')


print('in' in 'I hope this course is not full of jargon.')


len_python = len('python')
len_python = float (len_python)
len_python = str(len_python)

print(7//3 == int(2.7)) # True, because 7//3 is 2 and int(2.7) is also 2


print(type('10') == type(10)) # False, because the data type of '10' is str and the data type of 10 is int


print(type(int('9.8')) == type(10)) # False, because int('9.8') will raise a ValueError since '9.8' is not a valid integer string


hours = float(input('Enter hours: '))
input_rate = float(input('Enter rate per hour: '))  
print('Weekly earnings:', hours * input_rate)


Age = int(input('Enter the number of years you have lived: '))
Seconds =Age * 365 * 24 * 60 * 60
print('You have lived for', Seconds, 'seconds.')