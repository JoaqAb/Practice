# Level 1

# 1 Create an empty tuple
tpl_exercise = ()
tpl_with_tuple_constructor = tuple()

# 2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sis = ('Virginia', 'Agustina')
bros = ('Juan Panlo', 'Juan Jose')

# 3 Join brothers and sisters tuples and assign it to siblings
siblings = sis + bros

# 4 How many siblings do you have?
print(len(siblings))

# 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_member = list(siblings)
parents = ('Horacio', 'Carmen')
family_member = parents + siblings
print(family_member)

# Level 2

# 1 Unpack siblings and parents from family_members
parents_1 = family_member[0:2]
siblings_1 = family_member[2:]
print(parents_1, siblings_1)

# 2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('mango', 'banana', 'lemon', 'orange')
vegetables = ('brocoli', 'tomatoes', 'carrots', 'lettuce')
animals = ('dog', 'cat', 'horse', 'donkey')
food_stuff_tp = fruits + vegetables + animals

# 3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = food_stuff_tp[5:7]

# 5 Slice out the first three items and the last three items from food_staff_lt list
first_and_last_item = food_stuff_lt[0:3] + food_stuff_lt[-3:]

# 6 Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7 Check if an item exists in tuple:
"print(food_stuff_tp)"

# 8 Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

# 9 Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)