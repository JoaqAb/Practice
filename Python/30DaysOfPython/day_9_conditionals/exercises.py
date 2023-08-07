# Exercises: Level 1

# 1 Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 
# Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
'''age = int(input('Enter you age:' ))
if age >= 18:
    print('You are old enough to drive.')
else:
    print('You need ' + (str(18 - age)) + ' more years to learn to drive.')

age = int(input('Enter you age:' ))
under_age = (18 - age)
if age >= 18:
    print('You are old enough to drive.')
else:
    print(('You need {} more years to learn to drive.').format(under_age))'''

# 2 Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age
# as input. You can use a nested condition to print 'year' for 1 year 
# difference in age, 'years' for bigger differences, and a custom text if 
# my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
'''my_age = 20
your_age = int(input('Enter your age: '))
older = str(your_age - my_age)
younger = str(my_age - your_age)

if your_age > my_age:
    if your_age == my_age + 1:
        print('You are 1 year older than me')
    else:
        your_age > my_age + 1
        print('You are ' + (older) + ' years older than me')
elif your_age < my_age:
    if your_age == my_age - 1:
        print('You are 1 year younger than me')
    else:
        your_age < my_age + 1
        print('You are ' + (younger) + ' years younger than me')
else:
    print('We are the same age')'''

#  3Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. 
# Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
'''a = int(input('Insert number a: '))
b = int(input('Insert number b: '))
if a > b:
    print('a is greater than b')
elif a < b:
    print('a is smaller than b')
else:
    print('a is equal to b')'''
    
### Exercises: Level 2

# 1 Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
'''note = int(input('Insert your score: '))
if note >= 80 and note <= 100:
    print('Your grade is: "A"')
elif note >= 70 and note <= 89:
    print('Your grade is: "B"')
elif note >= 60 and note <= 69:
    print('Your grade is: "C"')
elif note >= 50 and note <= 59:
    print('Your grade is: "D"')
elif note >= 0 and note <= 59:
    print('Your grade is: "F"')
else:
    print('Wrong input')'''


# 2 Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring 
# June, July or August, the season is Summer

'''month = input('Insert a month: ')
month = month.lower()
if  month == 'september' or month == 'october' or month == 'november':
    print('The season is Autumn')
elif  month == 'december' or month == 'january' or month == 'february':
    print('The season is Winter')
elif  month == 'march' or month == 'april' or month == 'may':
    print('The season is Spring')
elif  month == 'june' or month == 'july' or month == 'august':
    print('The season is Summer')
else:
    print('Wrong input')'''    

#  3 The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list
# and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

'''new_fruit = input('Insert a fruit: ')
fruits = ['banana', 'orange', 'mango', 'lemon']
if new_fruit in fruits:
    print('That fruit already exist in the list')
else: 
    fruits.append(new_fruit)
print(fruits)'''

### Exercises: Level 3

# Check if the person dictionary has skills key, if so print out the middle
# skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person
# has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end
# developer'), if the person skills has Node, Python, MongoDB, print
# ('He is a backend developer'), if the person skills has React, 
# Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions 
# can be nested!
# If the person is married and if he lives in Finland, print the information
# in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
}
}

'''if ('skills' in person):
    print(person['skills'][2])
    
if ('skills' in person):
    if ('Python' in person['skills']):
        print(True)
    else:
        print(False)

if ('JavaScript' in person['skills'] 
    and 'React' in person['skills']) and (len(person['skills']) == 2):
    print('He is a front end developer')
elif ('Node' in person['skills'] 
      and 'Python' in person['skills'] 
      and 'MongoDB' in person['skills']) and (len(person['skills']) == 3):
    print('He is a back end developer')
elif ('Node' in person['skills'] 
      and 'React' in person['skills'] 
      and 'MongoDB' in person['skills']) and (len(person['skills']) == 3):
    print('He is a fullstack developer')
else:
    print('unknown title')'''  

if (person['is_marred']) == True and (person['country']) == 'Finland':
    print(person['first_name'] + ' ' + person['last_name'] + ' lives in ' + person['country'] + '. He is married')
    