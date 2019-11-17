f = open("MT1.txt")

cinta_inicial = ""

cinta1 = ""
cinta2 = ""
cinta3 = ""
cinta4 = ""

for line in f:
    cinta_inicial = cinta_inicial + line

def leer_cinta_inicial(cinta):

    cont = cinta.find("111")
    cinta1 = cinta[:cont+3]
    cinta2 = "01"+cinta[cont+3:]

    return cinta1, cinta2

def quitar(cinta1, cinta2, cinta3):
    cinta1 = cinta1[cinta1.find("1")+1:]
    cinta3 = cinta1[:3]

    return cinta1, cinta2, cinta3


def alo(cinta1):
    cinta1 = cinta1.replace("q","")
    print("Busca la transicion con estado "+cinta3+ " y letra "+cinta2[:1]+ " en la cinta 1")
    ss = len(cinta3+"1"+cinta2[:1])
    var = cinta1.find(cinta3+"1"+cinta2[:1])+ss
    #cinta1 = cinta1[:var+2] + "q" + cinta1[var+1:]
    #print("---------------------------hehe---------------")
    cinta1 = cinta1[:var+1]+"q"+cinta1[var+1:]
    
    #print(cinta1)
    return (cinta1)


def separar_zonas(cinta):

    global contador
    contador = 0

    global separacion
    separacion = ""

    global previa_zona
    previa_zona = 0
    zonas = []

    #print("la cinta que se ingresa es: ", len(cinta))

    for i in range(0, len(cinta)):

        if cinta[i] == "1":
            contador += 1

        if contador >= 6:
            separacion = cinta[previa_zona:(i+1)]
            #print(separacion)
            zonas.append(separacion)

            #evitamos que el siguiente sea 1
            previa_zona = i + 1
            contador = 0

    return zonas

class Zona:
    def __init__(self, estado1, estado2, letra1, letra2, movimiento):
        self.estado1 = estado1
        self.estado2 = estado2
        self.letra1 = letra1
        self.letra2 = letra2
        self.movimiento = movimiento

def crear_objetos(lista_de_zonas):
    print("zonas")

    lista_objetos = []

    for i in range(0, len(lista_de_zonas)):
        separaciones = lista_de_zonas[i].split('1')
        print(separaciones)

        objeto = Zona(separaciones[0], separaciones[1], separaciones[2], separaciones[3], separaciones[4])

        lista_objetos.append(objeto)

    return lista_objetos



cinta1, cinta2 = leer_cinta_inicial(cinta_inicial)


"""print("-------------------------------------------------------------------")
print ("Cinta inicial")
print (cinta_inicial)
print("-------------------------------------------------------------------")
print ("PASO 1 Y 2")
print("-------------------------------------------------------------------")
print ("Cinta 1")
print(cinta1)
print ("Cinta 2")
print(cinta2)
print ("Cinta 3")
print(cinta3)
print("-------------------------------------------------------------------")
print ("PASO 3")"""


cinta1, cinta2, cinta3 = quitar(cinta1, cinta2, cinta3)


"""print("-------------------------------------------------------------------")
print ("Cinta 1")
print(cinta1)
print ("Cinta 2")
print(cinta2)
print ("Cinta 3")
print(cinta3)
#print("-------------------------------------------------------------------")
#print ("PASO 4")
#alo(cinta1)

print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
"""
print('CINTA 1')
print(cinta1)

zonas = separar_zonas(cinta1)

zonas_establecidas = crear_objetos(zonas)

print("-------------------------------------------------------------------")

for x in zonas_establecidas:
    print(x.estado1, x.letra1, x.estado2, x.letra2, x.movimiento)