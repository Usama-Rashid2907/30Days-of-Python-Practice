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