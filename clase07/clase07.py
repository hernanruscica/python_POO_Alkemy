from enum import Enum

class TipoInstrumento(Enum):
    CAT1 = "Viento"
    CAT2 = "Cuerdas"
    CAT3 = "Percusion"

class Instrumento:
    def __init__(self, id, precio, tipo, nombre ):
        self.id = id
        self.precio = precio
        self.tipo = tipo
        self.nombre = nombre

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
        print("Muestro lista de todos los instrumentos de todas las sucursales:\n")
        for sucursal in self.lista_sucursales:            
            longitud_texto = len("Sucursal: %s" % sucursal.nombre)            
            cadena_guiones = "  " + "-" * longitud_texto
            print("%s\n| Sucursal: %s |\n%s" % (cadena_guiones, sucursal.nombre, cadena_guiones))
            for instrumento in sucursal.lista_instrumentos:
                print("Id: %s\nPrecio: $%.2f\n" % (instrumento.id, instrumento.precio))
            
    def instrumentosPorTipos(self, tipoInstrumento):
        print("muestro los intrumentos por tipo %s" %tipoInstrumento.value)
        longitud_texto = len("Instrumentos de  de todas las sucursales :: %s" % tipoInstrumento.name)            
        cadena_guiones = "  " + "-" * longitud_texto   
        print(cadena_guiones)
        print("| Instrumentos de %s de todas las sucursales : |" % tipoInstrumento.value)
        print(cadena_guiones)
        for sucursal in self.lista_sucursales:    
            for instrumento in sucursal.lista_instrumentos:       
                if instrumento.tipo.name == tipoInstrumento.name:                            
                    print("\nNombre: %s\nId: %s\nPrecio: $%.2f\nSucursal: %s" % (instrumento.nombre, instrumento.id, instrumento.precio, sucursal.nombre ))                
                    

    def borrarInstrumento(self, id):
        print("borro el instrumento con id %s" % id)
        for sucursal in self.lista_sucursales:                
            for instrumento in sucursal.lista_instrumentos: 
                if instrumento.id == id:
                    sucursal.lista_instrumentos.remove(instrumento)
                    print("Instrumento eliminado")
                    break                 

    def PorcInstrumentosPorTipo(self, nombreSucursal):
        #print("Muestro los porcentajes de tipos de instrumentos en la sucursal %s" % nombreSucursal)
        contadorTipoViento = 0                    
        contadorTipoCuerdas = 0
        contadorTipoPercusion = 0    
        InstrumentosXsucursal = 0
        for sucursal in self.lista_sucursales:
            for instrumento in sucursal.lista_instrumentos:
                if sucursal.nombre == nombreSucursal:                                    
                    #print("Nombre: %s - Tipo: %s" % (instrumento.nombre, instrumento.tipo.value))
                    if instrumento.tipo.value == "Viento":
                        contadorTipoViento += 1
                    elif instrumento.tipo.value == "Cuerdas":
                        contadorTipoCuerdas += 1
                    elif instrumento.tipo.value == "Percusion":
                        contadorTipoPercusion += 1
                    else:
                        pass  
                    InstrumentosXsucursal += 1      
        #print("Tipo Viento= %d\nTipo Cuerdas= %d\nTipo Percusion= %d\nTotal: %d" % (contadorTipoViento, contadorTipoCuerdas, contadorTipoPercusion, InstrumentosXsucursal))    
        promedioViento = round((contadorTipoViento / InstrumentosXsucursal) * 100)
        promedioCuerdas = round((contadorTipoCuerdas / InstrumentosXsucursal) * 100)
        promedioPercusion = round((contadorTipoPercusion / InstrumentosXsucursal) * 100)
        return [ 
            {"nombre": "Viento", "prom": promedioViento }, 
            {"nombre": "Percusion", "prom": promedioPercusion},
            {"nombre": "Cuerdas", "prom": promedioCuerdas}]
                
                        

#pruebas
flauta = Instrumento(1, 100, TipoInstrumento.CAT1, "flauta")
guitarra = Instrumento(2, 250, TipoInstrumento.CAT2, "guitarra")
bateria = Instrumento(3, 1000, TipoInstrumento.CAT3, "batería") 
saxofon = Instrumento(4, 250, TipoInstrumento.CAT1, "saxofón")
violin = Instrumento(5, 300, TipoInstrumento.CAT2, "violín")
tambor = Instrumento(6, 350, TipoInstrumento.CAT3, "tambor")
clarinete = Instrumento(7, 400, TipoInstrumento.CAT1, "clarinete")
contrabajo = Instrumento(8, 450, TipoInstrumento.CAT2, "contrabajo")
timbal = Instrumento(9, 500, TipoInstrumento.CAT3, "timbal")
trompeta = Instrumento(10, 550, TipoInstrumento.CAT1, "trompeta")
arpa = Instrumento(11, 600, TipoInstrumento.CAT2, "arpa")
bongos = Instrumento(12, 650, TipoInstrumento.CAT3, "bongos")
oboe = Instrumento(13, 700, TipoInstrumento.CAT1, "oboe")
cello = Instrumento(14, 750, TipoInstrumento.CAT2, "cello")
conga = Instrumento(15, 800, TipoInstrumento.CAT3, "conga")

sucursalItuzaingo = Sucursal("Kairon Music")
sucursalItuzaingo.agregarInstrumento(guitarra)
sucursalItuzaingo.agregarInstrumento(flauta)

sucursalCastelar = Sucursal("KEMUEL")
sucursalCastelar.agregarInstrumento(bateria)
sucursalCastelar.agregarInstrumento(saxofon)
sucursalCastelar.agregarInstrumento(violin)
sucursalCastelar.agregarInstrumento(tambor)

sucursalMoron = Sucursal("Best Music")
sucursalMoron.agregarInstrumento(clarinete)
sucursalMoron.agregarInstrumento(contrabajo)
sucursalMoron.agregarInstrumento(timbal)
sucursalMoron.agregarInstrumento(trompeta)
sucursalMoron.agregarInstrumento(arpa)

sucursalHaedo = Sucursal("Haedo tienda musical")
sucursalHaedo.agregarInstrumento(bongos)
sucursalHaedo.agregarInstrumento(oboe)
sucursalHaedo.agregarInstrumento(cello)
sucursalHaedo.agregarInstrumento(conga)


fabricaInstrumentosArgentinos = fabrica()
fabricaInstrumentosArgentinos.agregarSucursal(sucursalItuzaingo)
fabricaInstrumentosArgentinos.agregarSucursal(sucursalCastelar)
fabricaInstrumentosArgentinos.agregarSucursal(sucursalMoron)
fabricaInstrumentosArgentinos.agregarSucursal(sucursalHaedo)

#fabricaInstrumentosArgentinos.listarInstrumentos()
fabricaInstrumentosArgentinos.instrumentosPorTipos(TipoInstrumento.CAT1)
fabricaInstrumentosArgentinos.borrarInstrumento(8)
fabricaInstrumentosArgentinos.listarInstrumentos()

porcentajesTiposInstrumentosEnKemuel = fabricaInstrumentosArgentinos.PorcInstrumentosPorTipo("KEMUEL")

print("Datos de la sucursal 'KEMUEL': ")
for porcentajes in porcentajesTiposInstrumentosEnKemuel:
    print("\nPorcentaje de instrumentos de %s: %.0f%%" % (porcentajes['nombre'], porcentajes['prom']))
print("\n-------------------------")
    
    

print("Datos de la sucursal 'Best Music': ")
porcentajesTiposInstrumentosEnKemuel = fabricaInstrumentosArgentinos.PorcInstrumentosPorTipo("Best Music")
for porcentajes in porcentajesTiposInstrumentosEnKemuel:
    print("\nPorcentaje de instrumentos de %s: %.0f%%" % (porcentajes['nombre'], porcentajes['prom']))
print("\n-------------------------")