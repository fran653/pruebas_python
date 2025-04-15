nombre_archivo= 'tusmuertos.txt'
with open(nombre_archivo, 'r') as archivo:
    #print(archivo.readlines())   
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

print('**otro método**')
with open (nombre_archivo, 'r') as archivo:
    print(archivo.read().strip())