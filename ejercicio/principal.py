
"""
	Importamos las clases que necesitamos de los modulos.
"""
from paquete_modelo.mimodelo import Equipo,Operaciones
from paquete_archivos.miarchivo import MiArchivo,MiArchivoEscribir


m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion() # Guardamos lo que retorna el metodo
lista = [l.split("|") for l in lista] # Separamos por '|'' el csv

lista_equipos = []

for d in lista:
    e = Equipo(d[0], d[1], d[2], d[3])
    lista_equipos.append(e) # Agregamos a la lista los objetos

operacion = Operaciones(lista_equipos) # Creamos el objeto de tipo Operaciones

# Guardamos la opcion que ingresa el usuario
opcion = int(input("\n%20s\n\n\t1. Por nombre\n\t2. Por numero de campeonatos\nEscoja una opcion: "%("OPCIONES DE ORDENAMIENTO")))

lista_ordenada = operacion.ordenar(opcion) # Guardamos lo que retorna el metodo


for x in lista_ordenada:
	m2.agregar_informacion(x) # Enviamos el objeto al metodo 'agregar_informacion'
 
# Cerramos los archivos
m.cerrar_archivo()
m2.cerrar_archivo()




