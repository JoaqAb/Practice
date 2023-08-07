# SETs

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Exercises: Level 1

# 1 Find the length of the set it_companies
print(len(it_companies))

# 2 Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Youtube', 'Linkedin', 'HP', 'Dell'])

# Remove one of the companies from the set it_companies
it_companies.remove('HP')

# What is the difference between remove and discard
print('With remove we delete specific item and with discard we delete random item.')
print(it_companies)

# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1 Join A and B
c = A.union(B)
print(c)

# 2 Find A intersection B
c = A.intersection(B)
print(c)

# 3 Is A subset of B
print(A.issubset(B))

# 4 Are A and B disjoint sets
print(A.isdisjoint(B))

# 5 Join A with B and B with A
c = A.union(B)
d = B.union(A)
print(c, d)

# 6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# 7 Delete the sets completely
del A, B

# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1 Convert the ages to a set and compare the length of the list and the set,
# which one is bigger?
st_ages = set(age)
if len(st_ages) > len(age):
    print('Set is bigger')
print('List is bigger')

# 2 Explain the difference between the following data types:
# string, list, tuple and set
print('String is a chain of characters.\nList is a list of items, with specific order it could have differnets elements\nand could be modified.\nTuple content items that coulnd''t be modified.\nSet is a collections of unique items unordered')

# 3 I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.

sentence = ('I am a teacher and I love to inspire and teach people'.split(' '))
sen_st = set(sentence)
print(len(sen_st))


