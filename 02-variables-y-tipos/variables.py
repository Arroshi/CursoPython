# VARIABLES
"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada tenga un dato distinto.
"""

texto = "Máster en Python"
numero = 45
decimal = 6.7

# Mostrar el valor de las variables
print(texto)
print(numero)
print(decimal)

print("-----------------------------------")

# Sustituir el valor de algunas variables / reasignando valores
numero = 90
decimal = 12.4

print(numero)
print(decimal)

print("-----------------------------------")

# CONCATENAR
# Concatenación, te permite unir 2 variables 
nombre = "Victor"
apellidos = "Arroyo"
web = "mak.com"
# web = f"mak.com {nombre}" 

print(nombre + ' ' + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print(nombre, apellidos, web)

