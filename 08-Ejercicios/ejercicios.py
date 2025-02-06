"""
EJERCICIO 1
    - Crea variables una "pais" y otra "continente"
    - Mostrar su valor por pantalla (imprimir)
    - Poner un comentario diciendo el tipo de dato
"""

pais = "Perú" # string
continente = "LAN" # string
year = 2025

print(f"{pais} - {continente} - {str(year)}")


"""
EJERCICIO 2
    - Escribri un script que nos muestre por pantalla
    todos los números pares del 1 al 120
"""

numero = 1
contador = 1



for numero in range(1, 121):
    if numero%2==0:
        print(numero)


print("-----------------------------------------------")

while contador <= 120:
    if contador%2==0:
        print(contador)
    contador += 1


"""
EJERCICIO 3
    Escribir un programa que muestre los cuadrados
    (un número multiplicado por si mismo) de los 60
    primeros números naturales. Usar "for" y "while"

"""

# Usando FOR

for cuadrado in range(61):
    print(cuadrado * cuadrado)


print("-----------------------------------------------")
# Usando WHLE

contador = 0

while contador <= 60:
    cuadrado = contador * contador
    print(cuadrado)
    contador += 1