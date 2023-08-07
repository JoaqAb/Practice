# Variables
"""
first_name = 'Joaquin'
last_name = 'Abuin'
country = 'Argentina'
city = 'Tucuman'
age = 38
is_married = True
skills = ['Pyhon', 'Poker', '3d']
person_info = {
    'firstname':'Joaquin',
    'lastname':'Abuin',
    'country':'Argentina',
    'city':'Tucuman'
}

#Funciones del sistema "len()" : longitud del dato de la variable  
print('First name: ', first_name)
print('First name length: ', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Person skills: ', skills)
print('Person information: ', person_info)

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))

my_bool_variables = False
print(my_bool_variables)

print('Hello, World!')
print('Hello',',','World!')
print(len('Hello, Wolrd!'))

# Concatenacion de variables en print
print(my_string_variable, my_int_to_str_variable, my_bool_variables)

# Variables en una sola linea

name, surname, nacimiento = 'Joaquin', 'Abuin', 1984
print(name, surname, nacimiento)

# Input() la variablew se declara con los datos que ingresa el usuario
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
"""
# Convertir valores en otro tipo de datos
# Float to int
num_int = 10
print('num_int', num_int)

# Int to float
num_float = float(num_int)
print('num_float', num_float)

gravity = 9.81
print('gravity:', gravity, 'float_to_int gravity', int(gravity))

# Int to str
print(num_int)
num_str = str(num_int)
print(num_str, (type(num_str)))

# Str to int or float
# Primero pasar a float y despues a int
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))
num_int = int(num_float)
print('num_int', num_int)    