nombre_archivo = 'tusmuertos.txt'
#archivo = open ('tusmuertos.txt', 'w')
try:
    with open('tusmuertos.txt', 'x') as archivo:
        archivo.write ('Hace un pete y besame el ojete\n')
        archivo.write ('No me gusta el pichon\n')
        archivo.write ('Pues cómete un mojón\n')
        archivo.write ('Y no me digas que no\n')
        archivo.close()
except FileExistsError as e:
    print(f'El archivo {nombre_archivo} ya existe. No se ha creado un nuevo archivo. Error tipo {e}')
print('El archivo se ha creado correctamente, ahora tira de WSL para leerlo si tienes pelotas')