'''
# 1-2-3 Declarar variables
age = 38
weith = 89.9
comp_number = 5j

print((type(age)), age)
print((type(weith)), weith)
print((type(comp_number)), comp_number)

# 4- Area de un triangulo
base = int(input('Insert base: '))
height = int(input('Insert height: '))
area_of_triangle = (base * height)
print('Area of triangle:', area_of_triangle)

# 5- Perimetro de un triagunlo
side_a = int(input('Insert side "A": '))
side_b = int(input('Insert side "B": '))
side_c = int(input('Insert side "C": '))
# perimeter_of_triangle = (side_a + side_b + side_c)
print('Perimeter of triangle:', side_a + side_b + side_c)

# 6- Rectangle
length = int(input('Ingrese largo: '))
width = int(input('Ingrese ancho: '))
print('Area de rectangulo: ', length * width )
print('Perimetro de rectangulo: ', 2 * (length + width))

# 7- Circle
radio = int(input('Ingrese radio: '))
area_circle = 3.14 * radio ** 2
circum_circle = (2 * 3.14) * radio
print('Area of circle: ', area_circle)
print('Circumference of circle: ', circum_circle)

# 8- y = 2x - 2
punto_x1 = (1, 0)
punto_y1 = (0, -2)
slope_1 = ((-2 - 0) / (0 - 1))
print(slope_1)

# 9- Slope and distance
punto_x2 = (2, 2)
punto_y2 = (6, 10)

distancia_2 = ((((6 - 2)**2) + ((10 - 2)**2))**0.5)
print(distancia_2)
slope_2 = ((10 - 2) / (6 - 2))
print(slope_2)

# 10- Compare 8 and 9
if slope_1 > slope_2:
    print('La pendiente de recta 1 es mayor a la de recta 2')
elif slope_1 < slope_2:
    print('La pendiente de recta 1 es menor a la de recta 2') 
else:
    print('Las pendientes son iguales')

# 11- Ecuacion
x = int(input('Ingrese numero: '))
y = (x ** 2 + 6 * x + 9)
print(y) # Para que 'y' sea igual a '0' x debe ser '-3'

# 12- Length

print(len('python') is not len('dragon'))

# 13- on is in

print('on' in 'python' and 'on' in'dragon')

# 14- jargon in
jargon = 'I hope this course is not full of jargon'
print('jargon' in jargon)

# 15- 'on' dragon an python
print('on' not in 'python' and 'on' not in 'dragon')

# 16- convert

py = 'python'
py_float = float(len(py))
py_float_str = str(py_float)

print(py, (type(py)))
print(py_float, (type(py_float)))
print(py_float_str, (type(py_float_str)))

# 17- even or not even

even = int(input('Ingrese un numero: '))
if even % 2 == 0:
    print(even, ' is even')
else:
    print(even, ' is not even')

# 18- floor division

floor_1 = int(2.7)
floor_2 = 7 // 3
print(floor_1 == floor_2)

# 19- Check type
print((type('10')) == (type(10)))

# 20- check int
print((int(9.8)) == 10)

# 21- Script for hours
hours = int(input('Insert your hours: '))
rate_per_hour = int(input('Insert your rate: '))
print('Your weekly earning is: $', (hours * rate_per_hour))

# 22- second lived
years_lived = int(input('Insert your age: '))
print('You have lived; ',(years_lived * 365 * 24 * 60 * 60), 'seconds')
'''

# 23- Table script

fila_0 = 0
fila_1 = 1
while (fila_0 < 5):
    fila_0 += 1
    fila_2 = fila_1 * fila_0
    fila_3 = fila_2 * fila_0
    fila_4 = fila_3 * fila_0
    print(fila_0, fila_1, fila_2, fila_3, fila_4)




