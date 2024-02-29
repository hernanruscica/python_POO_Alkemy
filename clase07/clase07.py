from enum import Enum

class TipoInstrumento(Enum):
    CAT1 = "Viento"
    CAT2 = "Cuerdas"
    CAT3 = "Percusion"

class Instrumento:
    def __init__(self, id, precio, tipo ):
        self.id = id
        self.precio = precio
        self.tipo = tipo

class Sucursal:
    def __init__(self, nombre): 
        self.nombre = nombre
        self.lista_instrumentos = []
    def agregarInstrumento(self, instrumento):
        self.lista_instrumentos.append(instrumento)

class fabrica:
    def __init__(self):
        self.lista_sucursales = []
    def agregarSucursal(self, sucursal):
        self.lista_sucursales.append(sucursal)
    def listarInstrumentos(self):
        print("Muestro lista de todos los instrumentos de todas las sucursales:\n----------------------------------------------------")
        for sucursal in self.lista_sucursales:
            print(sucursal.nombre)
            for instrumento in sucursal.lista_instrumentos:
                print("Id: ", instrumento.id)
            
    def instrumentosPorTipos(self):
        print("muestro los intrumentos por tipo")
    def borrarInstrumento(self, id):
        print("borro el instrumento con id id")
    def PorcInstrumentosPorTipo(self, tipo):
        print("mustro los instrumentos del tipo tipo")

#pruebas
flauta = Instrumento(1, 100, TipoInstrumento.CAT1)
guitarra = Instrumento(2, 250, TipoInstrumento.CAT2)
bateria = Instrumento(3, 1000, TipoInstrumento.CAT3) 

sucursalItuzaingo = Sucursal("Kairon Music")
sucursalItuzaingo.agregarInstrumento(guitarra)
sucursalItuzaingo.agregarInstrumento(flauta)

fabricaInstrumentosArgentinos = fabrica()
fabricaInstrumentosArgentinos.agregarSucursal(sucursalItuzaingo)
fabricaInstrumentosArgentinos.listarInstrumentos()
