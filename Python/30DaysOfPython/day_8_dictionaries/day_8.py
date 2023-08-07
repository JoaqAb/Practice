### DICTIONARIES ###
'''
empty_dict = {}
print(type(empty_dict))

person = {
    'first_name':'Joaquin',
    'last_name':'Abuin',
    'age':38,
    'country':'Argentina',
    'is_married':True,
    'skills':['Poker', 'Python', 'Javascript', 'React'],
    'adress':{
        'street':'Monteagudo 1175',
        'zip_code':'4000'
    }
    }

#access dictionary
print(len(person))
print(person['skills'])
print(person['adress'])
print(person['adress']['street'])

# Accessing an item by key name raises an error if the key does not exist.
# To avoid this error first we have to check if a key exist or we can use 
# the get method. The get method returns None, which is a NoneType object
# data type, if the key does not exist.

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

# add items

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
dct['key4'] = 'value4'
print(dct)
print(dct['key3'])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}

person['job'] = 'Instructor'
person['skills'].insert(2, 'HTML')
print(person)
'''
# modifyind
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct)
dct['key1'] = 'value-one'
print(dct)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person['first_name'] = 'Eyob'
person['age'] = 252

print('key2' in dct)
print('key8' in dct)

'''pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name
'''
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

person.pop('first_name')
person.popitem()
del person['country']
print(person)

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(type(dct))
print(dct.items())
print(type(dct))

print(dct.clear())

del dct

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct, dct_copy)

print(dct.values())