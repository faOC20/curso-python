###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###


import os

from os import system
if system("clear") != 0: system("cls")


print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print('Convierte la cadena "12345" a un entero y luego a un float.')
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")


# ---------------------------- RESPUESTAS -------------------------


def clear_console():
    print("\n" * 100)


# ejercicio 1
clear_console()
print("Fabian Ortiz\nCumana")

# ejercicio 2
print(type(a))
print(type(b))
print(type(c))
print(type(e))

# ejercicio 3
number = "1234"

to_int_number = int(number)
print(f"{number} este numero es de tipo {type(number)}")

to_float_number = float(number)
print(f"{number} este numero es de tipo {type(number)}")

# ejercicio 4
name = "fabian"
age = 22
height = 1.68


def greetings():
    return f"hola! me llamo {name} y tengo {age} anios, mido {height} metros"


saludo = greetings()
print(saludo)


# ejercicio 5
pi = 3.141516
rounded_pi = round(pi)
final = rounded_pi / 2
print(int(final))
