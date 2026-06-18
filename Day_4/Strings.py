# Length of a string using len() method
letter = 'p'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = 'Hope youre loving this python journey!'
print(sentence)
print(len(sentence))

# Strings can also be multi quotes
Multi_line_string = '''This is a multi-line string.
It can span multiple lines. I am a teacher
who enjoys teaching python programming.
I didnt find anything as emppowering as educating people.
This is why the 30 days of python exists'''
print(Multi_line_string)
print(len(Multi_line_string))

# Another way of doing the same thing
multi_line_string2 = """This is a multi-line string.
It can span multiple lines. I am a teacher
who enjoys teaching python programming. 
I didnt find anything as emppowering as educating people.
This is why the 30 days of python exists"""
print(multi_line_string2)
print(len(multi_line_string2))


# String Concatenation
# It is possible to string multiple string together  
first_name = 'Usama'
last_name = 'Rashid'
space = ' '
full_name = first_name + space + last_name
print('Full name = ' + full_name)

print(len(first_name))  
print(len(last_name))   
print(len(first_name) > len(last_name)) 
print(len(full_name)) 


#Escape sequences in strings
# Escape sequences allow us to use characters that are otherwise difficult to include in a 
# string. For example, if we want to include a single quote in a string that is enclosed in
# single quotes, we can use the backslash (\) as an escape character.

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# So there's \n to go to a new line
# There's \t to tab
# There's \\ to do a backlash
# And finally there \" " to write a "" within a string  
