# Strings

# letter = 'P'                # A string could be a single character or a bunch of texts
# print(letter)               # P
# print(len(letter))          # 1
# greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
# print(greeting)             # Hello, World!
# print(len(greeting))        # 13
# sentence = "I hope you are enjoying 30 days of Python Challenge"
# print(sentence)

# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)

# # Another way of doing the same thing
# multiline_string_1 = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string_1)
'''
first_name = 'Joaquin'
last_name = 'Abuin'
space = ' '
full_name = first_name + space + last_name
print(full_name)

print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

print('Ihope everyone is enjoying Pithon Challenge. \nAre you?')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash symbol (\\)')
print('In every programming language it start with \"Hello, World!\"')
# Strings only
first_name = 'Joaquin'
last_name = 'Abuin'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
# Strings and numbres
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string)
# New Format
first_name = 'Joaquin'
last_name = 'Abuin'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

a, b = 4, 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings and numbers
radius, pi = 10, 3.14
area = pi * radius
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formated_string)
a, b = 4, 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
# Unpacking characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
language = 'Python'
firs_letter = language[0]
print(firs_letter)
last_index = len(language) -1
print(last_index)
last_letter = language[-1]
print(last_letter)
language = 'Python'
first_three = language[0:3]
last_three = language[3:6]
print(first_three)
print(last_three)
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)
greeting = 'Hello, World!'
print(greeting[::-1])
language = 'Python'
pto = language[0:6:2]
print(pto)
challenge = 'thirty days of python'
print(challenge.capitalize())
print(challenge.count('y'))
print(challenge.count('t', 4, -1))
print(len(challenge))

print(challenge.endswith('on'))
challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs())
print(challenge.expandtabs(20))
challenge = 'thirty days of python'
print(challenge.find('x'))
first_name = 'Joaquin'
last_name = 'Abuin'
age = 38
job = 'poker player'
country = 'Argentina'
sentence = 'I am {} {}. I am {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence)

radius = 10
pi = 3.14
area = int(pi * radius ** 2)
result = 'The area of a circle with radius {} is {}.'.format(str(radius), str(area))
print(result)

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error
challenge = 'ThirtyDaysOfPython'
print(challenge.isalnum())

challenge = '30DaysOfPython'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum())
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00A2'
print(challenge.isdigit())   # True

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

web_tech = ['HTML', 'CSS', 'JacaScript', 'React']
result = ' - '.join(web_tech)
print(result)
'''
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON