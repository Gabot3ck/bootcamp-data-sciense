numero1 = 70 #declaración de variable. Tipos de Datos - Primitivos, Numerales.
numero2 = 3.14 #declaración de variable. Tipos de Datos - Primitivos, Numerales.
booleano = False #declaración de variable. Tipos de Datos - Primitivos, Boolean.
cadena = 'Hola Mundo' #declaración de variable. Tipos de Datos - Primitivos, Strings.
#declaración de una lista, tipo de dato compuesto.
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] 
#declaración de un diccionario, tipo de dato compuesto.
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False}
#declaración de una tupla, tipo de dato compuesto.
frutas = ('guayaba', 'fresa', 'papaya')
print(type(frutas)) #revisión de tipo de dato

#acceder al valor de la lista ingredientes_pastel - imprime 'Huevos'.
print(ingredientes_pastel[2]) 

#agrega un nuevo elemento a la lista ingredientes_pastel
ingredientes_pastel.append('Mantequilla')

#accede al valor de de la clave 'nombre' del diccionario persona
print(persona['nombre'])

#cambia el valor de la clave 'nombre' del diccionario persona
persona['nombre'] = 'Kevin'

#agrega un nuevo elemento al diccionario persona
persona['color_ojos'] = 'cafe'

print(frutas[2])

if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor")

if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8):
    print(x)
for x in range(2,8):
    print(x)
for x in range(2,8,2):
    print(x)
x = 0
while(x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop()
ingredientes_pastel.pop(1)

print(persona)
persona.pop('color_ojos')
print(persona)

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)