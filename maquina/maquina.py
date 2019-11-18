f = open("MT1.txt")

cinta_inicial = ""
cinta1 = ""
cinta2 = ""
cinta3 = ""
cinta4 = ""
cintaz = ""

for line in f:
    cinta_inicial = cinta_inicial + line

def paso_inicial(cinta):
    cont = cinta.find("111")
    cinta1 = "q"+cinta[:cont+3]
    cinta2 = "q01"+cinta[cont+3:]
    cinta3 = "q"
    cintaz = cinta[4:cont+3]
    print ("PASO 1 Y 2")
    print("-------------------------------------------------------------------")
    print ("Cinta 1")
    print(cinta1)
    print ("Cinta 2")
    print(cinta2)
    print ("Cinta 3")
    print(cinta3)

    return cinta1, cinta2, cinta3, cintaz

def paso3(cinta1, cinta2, cinta3):
    cinta3 = cinta3 + cinta1[cinta1.find("q")+1:cinta1.find("1")]
    cinta1 = cinta1[cinta1.find("q")]+cinta1[cinta1.find("1")+1:]
    print("-------------------------------------------------------------------")
    print ("PASO 3")
    print("-------------------------------------------------------------------")
    print ("Cinta 1")
    print(cinta1)
    print ("Cinta 2")
    print(cinta2)
    print ("Cinta 3")
    print(cinta3)
    
    return cinta1, cinta2, cinta3


def maquina(cinta1,cinta2,cinta3,zonas_establecidas):
    cont = 0
    #CICLO MOMENTANEO MIENTRAS SE CREA LA CONDICION PARA SALIR DEL LOOP
    while(cont < 4):
        #INICIO DE PASOS REPETITIVOS

        #PRIMERA PARTE DE LOS PASOS REPETITIVOS
        print("-------------------------------------------------------------------")
        print ("PASO "+str(cont+4))
        print("-------------------------------------------------------------------")
        #OBTIENE EL ESTADO CORRESPONDIENTE
        estadoC = cinta3[1:]
        #OBTIENE LA LETRA CORRESPONDIENTE
        q1 = cinta2.find("q")+1
        enc = cinta2[q1:].find("1")
        letraC1 = cinta2[q1:][:enc]+"1"
        letraC = cinta2[q1:][:enc]
        print("Busca la transicion con estado "+estadoC+ " y letra "+letraC+ " en la cinta 1")
        #MUEVE LA LETRA Q A SU POSICION NUEVA
        cinta1 = cinta1.replace("q","")
        ss = len(estadoC+"1"+letraC1)
        var = cinta1.find(estadoC+"1"+letraC1)+ss
        #print("******************************************")
        #print(cinta1[:var])
        #print(cinta1[var:])
        #print("******************************************")
        #IMPRIME NUEVOS VALORES DE LAS CINTAS
        cinta1 = cinta1[:var]+"q"+cinta1[var:]
        print ("Cinta 1")
        print(cinta1)
        print ("Cinta 2")
        print(cinta2)
        print ("Cinta 3")
        print(cinta3)
        print("")
        
        #SEGUNDA PARTE DE LOS PASOS REPETITIVOS
        print("Despues de la busqueda de la transicion con estado "+estadoC+ " y letra "+letraC+ " en la cinta 1")

        """
        SI LA TRANSICION = 0 STAY
        SI LA TRANSICION = 00 LEFT
        SI LA TRANSICION = 000 RIGHT"""
        
        #NUEVO ESTADO DE CINTA 3
        encq = cinta1.find("q")
        cinta1N = cinta1[encq:]
        encq1 =cinta1N.find("1")
        estadoN = cinta1N[:encq1]
        cinta3 = estadoN

        #REINICIO DE CINTA 1 
        cinta1 = cinta1.replace("q","")
        cinta1 = "q"+cinta1
        
        #MOVIMIENTO DE Q EN CINTA 2 (POR EL MOMENTO SOLO A LA DERECHA)
        encq2 = cinta2.find("q")
        encq3 = cinta2.find("1")
        aaaa = cinta2[encq2:].find("1")
        bbb = aaaa+encq2
        cinta2 = cinta2.replace("q","")
        cinta2 = cinta2[:bbb]+"q"+cinta2[bbb:]

        
        #IMPRIME NUEVOS VALORES DE LAS CINTAS
        print ("Cinta 1")
        print(cinta1)
        print ("Cinta 2")
        print(cinta2)
        print ("Cinta 3")
        print(cinta3)
        print("")
        #CONTADOR MOMENTANEO MIENTRAS SE CREA CONDICION DE FINALIZACION
        cont +=1
    
    return cinta1,cinta2,cinta3
    
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
        objeto = Zona(separaciones[0], separaciones[1], separaciones[2], separaciones[3], separaciones[4])
        lista_objetos.append(objeto)

    return lista_objetos

print("-------------------------------------------------------------------")
print ("Cinta inicial")
print (cinta_inicial)
print("-------------------------------------------------------------------")
cinta1, cinta2, cinta3, cintaz = paso_inicial(cinta_inicial)
cinta1, cinta2, cinta3 = paso3(cinta1, cinta2, cinta3)
zonas = separar_zonas(cintaz)
zonas_establecidas = crear_objetos(zonas)
inta1,cinta2,cinta3 = maquina(cinta1,cinta2,cinta3,zonas_establecidas)

