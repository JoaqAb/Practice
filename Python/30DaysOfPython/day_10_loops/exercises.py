# Exercises: Level 1

# 1 Iterate 0 to 10 using for loop, do the same using while loop.
a = 0
while a < 11:
    print(a)
    a += 1

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for b in num:
    print(b)

# 2 Iterate 10 to 0 using for loop, do the same using while loop.
x = 10
while x > -1:
    print(x)
    x -= 1
    
num.reverse()
for y in num:
    print(y)
    
# 3 Write a loop that makes seven calls to print(), 
# so we get on the output the following triangle:
var1 = 0
var2 = '#'
while var1 < 8:
    print(var2)
    var1 += 1
    var2 = var2 + '#'

columns = [1, 2, 3, 4, 5, 6, 7, 8]
y = '#'
for i in columns:
    y = y + '#'
    print(y)
    
# 4 Use nested loops to create the following:
columns = [1, 2, 3, 4, 5, 6, 7, 8]
y = '# '
for i in columns:
    print(y * 8)
    
col = 0
while col < 9:
    print(y * 8)
    col += 1
    
# 5 Print the following pattern:    
a = 0
b = 0
while a < 11:
    c = a * b
    result = ('{} x {} = {} ').format(a, b, c)
    print(result)
    a += 1
    b += 1

# 6 Iterate through the list using a for loop and print out the items.
my_lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in my_lst:
    print(item)

# 7 Use for loop to iterate from 0 to 100 and print only even numbers
for number in range(0, 101, 2):
    print(number)

# 8 Use for loop to iterate from 0 to 100 and print only odd numbers
for odd in range(0, 100, 1):
    if odd % 2 != 0:
        print(odd)

# Exercises: Level 2

#  1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
numbers = list(range(0, 101)) 
total = 0 
for n in numbers:
    total = total + n
print(total)
    
# 2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
odd_evens = list(range(0, 101)) 
total_evens = 0
total_odds = 0
for n in odd_evens:
    if n % 2 == 0:
        total_evens = total_evens + n
    elif n % 2 != 0:
        total_odds = total_odds + n
print('The evens sum is:',total_evens)
print('The odds sum is:',total_odds)

# Exercises: Level 3

# 1 Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing
# the word land.
from countries import countries
for n in countries:
    if 'land' in n:
        print(n)
        
# 2 This is a fruit list, reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon'] 
re_fruits = []
for f in fruits:
    re_fruits = [f] + re_fruits
print(re_fruits)
    
# 3 Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world
from data_countries import data




    

    
    
    
    



    
