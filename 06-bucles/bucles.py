"""
BUCLE FOR
es una estructura iterativa que se va a repetir x veces

for variable in elemento_interable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range(0, 5):
    print(f"voy por el {contador}")

    resultado += contador

print(f"el resultado es {resultado}")


# Ejemplo con tablas de multiplicar
print("\n########## EJEMPLO ##########")

# num_usuario = int(input("¿De que número quieres la tabla?: "))
num_usuario = 10

if num_usuario < 1:
    num_usuario = 1

print(f"\n#### Tabla de multiplicar del número {num_usuario} ####")


for num_tabla in range(0, 13):

    if num_usuario == 48:
        print("\nNo se pueden mostrar números prohibidos")
        break

    print(f"{num_usuario} x {num_tabla} = {num_usuario*num_tabla}")
else:
    print("\nTabla finalizada.")

"""
BUCLE WHILE
es una estructura de control que itera o repite la ejecución
de una serie de instrucciones tantas veces como sea necesario
hasta que deje de cumplirse la condición

while condición:
    BLOQUE DE INSTRUCCIONES
    ACTUALIZACIÓN DE CONTADOR
"""

contador = 1

while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador += 1
print("---------------------------------------------------------")

contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador = contador + 1
print(muestrame)


# Ejemplo
print("\n########## EJEMPLO ##########")

num_usuario = int(input("¿De que número quieres la tabla?: "))

if num_usuario < 1:
    num_usuario = 1

print(f"\n#### Tabla del {num_usuario} ####")

contador = 1

while contador <= 10:
    print(f"{num_usuario} x {contador} = {num_usuario*contador}")
    contador += 1
else:
    print("Tabla Terminada")