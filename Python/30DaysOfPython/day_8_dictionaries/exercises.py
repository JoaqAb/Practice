# 1 Create an empty dictionary called dog
dog = {}

# 2 Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Vega'
dog['color'] = 'orange'
dog['breed'] = 'akita inu'
dog['legs'] = 4
dog['age'] = 1
print(dog)

# 3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Joaquin',
    'last_name':'Abuin',
    'gender':'male',
    'age':38,
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Argentina',
    'city':'Tucuman',
    'address':{'street':'Monteagudo', 'zip_code':4000}
    }
print(student)

# 4 Get the length of the student dictionary
print(len(student))

# 5 Get the value of skills and check the data type, it should be a list
print((student.get('skills')),(type(student.get('skills'))))

# 6 Modify the skills values by adding one or two skills
student['skills'].insert(1,'HTML')
student['skills'].append('Java')
print(student.get('skills'))

# 7 Get the dictionary keys as a list
keys_student = student.keys()
print(keys_student)

# 8 Get the dictionary values as a list
values_student = student.values()
print(values_student)

# 9 Change the dictionary to a list of tuples using items() method
items_student = student.items()
print(items_student)

# 10 Delete one of the items in the dictionary
student.pop('gender')
print(student)

# 11 Delete one of the dictionaries
del dog