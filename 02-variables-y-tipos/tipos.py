# TIPOS DE VARIABLES

nada = None
cadena = "Hola soy Victor" # string
entero = 99 # int
flotante = 99.5 # decimal / float
booleano = True # bool | true or false
lista = [10, 20, 40, 80, 160] # Array
listaString = [44, 'treinta', 30]
tupla = ("Master", "en", "Python") # Lista de datos que no cambia
diccionario = {
    "nombre": "Victor",
    "apellido": "Arroyo",
    "curso": "Python"
} # Json
rango = range(9) # Rango
dato_byte = b"Probando" # Dato byte


print(dato_byte)

# Mostrar el tipo de dato
print(type(dato_byte))


print("------------------------------------------------------------------")

texto = "Hola soy un texto"
numerito = str(7776)
# Formatear int a string
print(type(numerito))
print(texto + " " + numerito)
# Formatear string a int
numerito = int(7776)
print(type(numerito))
# Formatear int a float
numerito = float(7776)
print(type(numerito))

print("------------------------------------------------------------------")

# CURIOSIDADES

mi_texto = "Master"
mi_texto2 = "en Phyton"
mi_texto2 = 'en "Phyton"'
mi_texto2 = "en \"Phyton\""

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)


texto_unido = mi_texto + " \n " + mi_texto2
print(texto_unido) # salto de linea

texto_unido = mi_texto + " \t " + mi_texto2
print(texto_unido) # tabulacion

texto_unido = mi_texto + " \r " + mi_texto2
print(texto_unido) # borrar todo lo que hay detrás


