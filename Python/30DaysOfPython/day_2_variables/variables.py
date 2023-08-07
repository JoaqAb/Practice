# Day 2: 30 days of python programming

first_name = 'Joaquin'
last_name = 'Abuin'
full_name = first_name + last_name
country = 'Argentina'
city = 'Tucuman'
age = 38
year = 1984
is_married = True
is_light_on = False
partner_name, partner_last_name, partner_age = 'Sol', 'Leiva', 40

print(type(first_name))
print(type(last_name))
print(type( full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_light_on))
print(type(partner_name), (type(partner_last_name)), (type(partner_age)))

print(len(first_name))
print(len(last_name))

if len(first_name) > len(last_name):
    print('First_name mayor a last_name length')
else:
    print('Last_name mayor a first_name length')

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(num_one)
print(num_two)
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30
print(area_of_circle)
print(circum_of_circle)

radio = input('Ingrese radio: ')
print(type(radio))
user_area = 3.14 * (int(radio) ** 2) 
user_circum = 2 * 3.14 * int(radio)
print(user_area)
print(user_circum)

# User input

user_name = input('Ingrese su nombre: ')
user_last_name = input('Ingrese su apellido: ')
user_country = input('Ingrese su pais: ')
user_age = input('Ingrese su edad: ')

print(user_name)
print(user_last_name)
print(user_country)
print(user_age)










