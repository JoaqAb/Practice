'''
empty_tuple = ()
tp1 = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits.index('orange'))
print(len(tp1))

first_item = tp1[0]
second_item = tp1[1]
print(first_item, second_item)

last_index = len(fruits) - 1
last_fruit = fruits[-1]
print(last_index, last_fruit)

# Syntax
# Positive
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
print(middle_two_items, orange_mango, orange_to_the_rest)

# Negative
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

fruits = ('banana', 'orange', 'mango', 'lemon')
lst = list(fruits)
print(fruits, type(fruits), lst, type(lst))

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)

# checking item in tuples 

tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
'''

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_vegetables = fruits + vegetables
print(fruits_vegetables)

del fruits
print(fruits)

