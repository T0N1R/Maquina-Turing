f = open("MT1.txt")

cinta_inicial = ""

cinta1 = ""
cinta2 = ""
cinta3 = ""
cinta4 = ""
cintaz = ""

for line in f:
    cinta_inicial = cinta_inicial + line

def leer_cinta_inicial(cinta):

    cont = cinta.find("111")
    cinta1 = "q"+cinta[:cont+3]
    cinta2 = "q01"+cinta[cont+3:]
    cinta3 = "q"
    cintaz = cinta[4:cont+3]

    return cinta1, cinta2, cinta3, cintaz

def quitar(cinta1, cinta2, cinta3):
    cinta3 = cinta3 + cinta1[cinta1.find("q")+1:cinta1.find("1")]
    cinta1 = cinta1[cinta1.find("q")]+cinta1[cinta1.find("1")+1:]
    return cinta1, cinta2, cinta3


def alo(cinta1,zonas_establecidas):
    ubc = str(cinta1.find("q"))
    #print("Q se encuentra en la seccion " + ubc)
    #print("Se buscara en la zona " + ubc)
    est = zonas_establecidas[int(ubc)].estado1
    let = zonas_establecidas[int(ubc)].letra1
    #print("el estado es: "+est)
    #print("la letra es: "+let)
    print("Busca la transicion con estado "+est+ " y letra "+let+ " en la cinta 1")
    cinta1 = cinta1.replace("q","")
    ss = len(est+"1"+let+"1")
    #print("**************************************")
    #print(ss)
    #print(cinta1)
    #print("**************************************")
    var = cinta1.find(est+"1"+let)+ss 
    cinta1 = cinta1[:var]+"q"+cinta1[var:]

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
    def __init__(self, estado1, letra1, estado2, letra2, movimiento):
        self.estado1 = estado1
        self.estado2 = estado2
        self.letra1 = letra1
        self.letra2 = letra2
        self.movimiento = movimiento

def crear_objetos(lista_de_zonas):
    #print("zonas")

    lista_objetos = []

    for i in range(0, len(lista_de_zonas)):
        separaciones = lista_de_zonas[i].split('1')
        #print(separaciones)

        objeto = Zona(separaciones[0], separaciones[1], separaciones[2], separaciones[3], separaciones[4])

        lista_objetos.append(objeto)

    return lista_objetos

print("-------------------------------------------------------------------")
print ("Cinta inicial")
print (cinta_inicial)
print("-------------------------------------------------------------------")
cinta1, cinta2, cinta3, cintaz = leer_cinta_inicial(cinta_inicial)
print ("PASO 1 Y 2")
print("-------------------------------------------------------------------")
print ("Cinta 1")
print(cinta1)
print ("Cinta 2")
print(cinta2)
print ("Cinta 3")
print(cinta3)
print("-------------------------------------------------------------------")
print ("PASO 3")

cinta1, cinta2, cinta3 = quitar(cinta1, cinta2, cinta3)

print("-------------------------------------------------------------------")
print ("Cinta 1")
print(cinta1)
print ("Cinta 2")
print(cinta2)
print ("Cinta 3")
print(cinta3)
#print("-------------------------------------------------------------------")
#print('CINTA Z')
#print(cintaz)
#print("-------------------------------------------------------------------")

zonas = separar_zonas(cintaz)

zonas_establecidas = crear_objetos(zonas)


#for x in zonas_establecidas:
#    print(x.estado1, x.letra1, x.estado2, x.letra2, x.movimiento)
print("-------------------------------------------------------------------")
#print(zonas_establecidas[2].movimiento)
print ("PASO 4")
print("-------------------------------------------------------------------")
cinta1 = alo(cinta1,zonas_establecidas)
print ("Cinta 1")
print(cinta1)
print ("Cinta 2")
print(cinta2)
print ("Cinta 3")
print(cinta3)
print("-------------------------------------------------------------------")
