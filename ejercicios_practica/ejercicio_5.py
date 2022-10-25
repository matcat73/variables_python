# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
palabra_1 = str(input('Ingrese palabra 1:'))

palabra_2 = str(input('Ingrese palabra 2:'))

# Objetivo:
# De la primera palabra tome las primeras tres letras,
# utilice el operador dos puntos :
# De la segunda palabra tome las primeras dos letras
# utilice el operador dos puntos 

p1 = palabra_1[:3]

p2 = palabra_2[:2]

# Alumno:
# Crear una variable llamada palabra_combinada
# con los recortes solicitados de las variables
# palabra_1 y palabra_2 en el orden correspondiente

palabra_combinada = p1 + p2


# Imprima en pantalla la variable palabra_combinada

print('La combinación de letras es:', palabra_combinada)
