"""
CONDICIONALES

# # Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones


if condición:
    instrucciones
else:
    otras condiciones

# # Operadores de comparación

== igual
!= diferente
<  menor que
>  mayor que
<= menor o igual que
>= mayor o igual que

# # Operadores lógicos
and ' y '
or  ' o '
!   ' negación '
not ' no '

"""

# Ejemplo 1
print("########## EJEMPLO 1 ##########")

color = "negro"
# color = input("Adivina cúal es el color en el que estoy pensando? -> ")

if color == "negro":
    print("Correcto!")
    print("Es el negro")
else:
    print("nheee")

# Ejemplo 2
print("\n########## EJEMPLO 2 ##########")

year = 2025
# year = int(input("¿En que año estamos? "))

if year >= 2024:
    print("Si es mayor")
else:
    print("Es menor")

# Ejemplo 3
print("\n########## EJEMPLO 3 ##########")

nombre = "Victor"
ciudad = "Lima"
continente = "America Sur"
edad = 25
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad.")

    if continente != "America Sur":
        print(f"{nombre} no es de america")
    else:
        print(f"{nombre} es de {continente} y de {ciudad}")

else:
    print(f"{nombre} no es mayor de edad.")

# Ejemplo 4
print("\n########## EJEMPLO 4 ##########")

# dia = int(input(f"Introduce el número del día de la semana: "))
dia = 1

"""
if dia == 1:
    print("Es Lunes")
else:
    if dia == 2:
      print("Es Martes")
    else:
        if dia == 3:
        print("Es Miércoles") 
"""

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miércoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")


# Ejemplo 5
print("\n########## EJEMPLO 5 ##########")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print(f"El usuario está en edad para trabajar")
else:
    print("El usuario no está en edad para trabajar")


# Ejemplo 6
print("\n########## EJEMPLO 6 ##########")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")


# Ejemplo 7
print("\n########## EJEMPLO 7 ##########")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} ES un país de habla hispana")
    

# Ejemplo 8
print("\n########## EJEMPLO 8 ##########")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} ES un país de habla hispana")