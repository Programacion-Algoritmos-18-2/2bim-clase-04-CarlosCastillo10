import codecs
import sys

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion2.csv", "a")

    def agregar_informacion(self, e):

        # Accedemos a cada uno de los atributos del objeto recibido
        self.archivo.write("%s|%s|%s|%s" % (e.obtener_nombre(),e.obtener_ciudad(),e.obtener_campeonatos(),e.obtener_num_jugadores()))

    def cerrar_archivo(self):
        self.archivo.close()
