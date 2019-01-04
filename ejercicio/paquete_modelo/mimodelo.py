
class Equipo(object):

	# Constructor
	def __init__(self,n,c,camp,jugadores):

		self.agregar_nombre(n)
		self.agregar_ciudad(c)
		self.agregar_campeonatos(camp)
		self.agregar_num_jugadores(jugadores)

	
	# Metodos de agregar
	def agregar_nombre(self, n):
		self.nombre = n

	def agregar_ciudad(self, c):
		self.ciudad = c

	def agregar_campeonatos(self, camp):
		self.campeonatos = camp

	def agregar_num_jugadores(self, jugadores):
		self.num_jugadores = jugadores

	# Metodos de obtener
	def obtener_nombre(self):
		return self.nombre

	def obtener_ciudad(self):
		return self.ciudad

	def obtener_campeonatos(self):
		return self.campeonatos

	def obtener_num_jugadores(self):
		return self.num_jugadores

	def __str__(self):

		return "\nNombre: %s\nCiudad: %s\nNumero de Campeonatos: %s\nNumero de Jugadores: %s"%(self.obtener_nombre(),self.obtener_ciudad(),
			self.obtener_campeonatos(),self.obtener_num_jugadores())

	def __repr__(self):

		return "\nNombre: %s\nCiudad: %s\nNumero de Campeonatos: %s\nNumero de Jugadores: %s"%(self.obtener_nombre(),self.obtener_ciudad(),
			self.obtener_campeonatos(),self.obtener_num_jugadores())

class Operaciones(object):

	# Constructor
	def __init__(self, listado):

		self.listado_equipos = listado

	# Metodo que recibe la opcion de ordenamiento
	def ordenar(self,respuesta):

		# Dependiendo de la opcion retorna una  lista ordenada
		if (respuesta == 1):
			return sorted(self.listado_equipos, key=lambda equipo: equipo.obtener_nombre())
		else:
			return sorted(self.listado_equipos, key=lambda equipo: equipo.obtener_campeonatos())