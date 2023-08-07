# SETs
'''
Set is a collection of items. 
Let me take you back to your elementary or high school Mathematics lesson. 
The Mathematics definition of a set can be applied also in Python. 
Set is a collection of unordered and un-indexed distinct elements. 
In Python set is used to store unique items, and it is possible to find the union, 
intersection, difference, symmetric difference, subset, super set
 and disjoint set among sets.
'''
# Create a Set 
st = {}
st = set()

st = {'item1', 'item2', 'item3'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

print(len(fruits))

# Check if a item is in set
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits )

# Adding items to a set

# add single item
fruits.add('apple')
print(fruits)

# add multiple items
st.update(['item5', 'item6', 'item7'])
print(st)

vegetables = ('tomato', 'potato', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# remove items
fruits.remove('potato')
print(fruits)

# pop remove random item from a set
fruits.pop()
removed_item = fruits.pop()
print(fruits)
print(removed_item)

# clear method to a empty a set
st.clear()
print(st)

# del method to delete a set
del st

# converting list to a set.Converting list to set removes duplicates
# and only unique items will be reserved.
lst = ['banana', 'orange', 'mango', 'lemon', 'banana', 'orange']
st = set(lst)
print(lst, st)

# joining sets. using union() or update()

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
st1.update(st2)
print(st3)
print(st1)

# intersection
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))     # {'o', 'n'}

# subset and superset
# Subset: issubset()
# Super set: issuperset()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)
st1.issuperset(st2)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))     # False

# difference between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1.difference(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon)) 
print(dragon.difference(python))

# symmetric.
# It returns the the symmetric difference between two sets.
# It means that it returns a set that contains all items from both sets, 
# except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
print(st2.symmetric_difference(st1)) # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(dragon.symmetric_difference(python))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# Joining sets. 
# If two sets do not have a common item or items we call them disjoint sets.
# We can check if two sets are joint or disjoint using isdisjoint() method.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}





