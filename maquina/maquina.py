
"""
    Logica matematica
    Proyecto Final - Maquina de Turing
    20/11/2019
    Gustavo de Leon #17085
    Antonio Reyes #17273
"""

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
    inicio = cinta.find("1")
    cont = cinta.find("111")
    cinta1 = "q"+cinta[:cont+3]
    cinta2 = "q01"+cinta[cont+3:]
    cinta3 = "q"
    cintaz = cinta[inicio+1:cont+3]
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


def maquina(cinta1,cinta2,cinta3):
    anterior = ""
    cont = 0
    seguirB = True
    cinta3BOOLEAN = True
    #CICLO MOMENTANEO MIENTRAS SE CREA LA CONDICION PARA SALIR DEL LOOP
    while(cinta3 != "q0"):
        seguirB = True
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
        cochinada = cinta1.find(estadoC+"1"+letraC1) #da la posicion de lo que se busca
        valor_anterior = cinta1[cochinada-2:cochinada] #Para saber si es estado1 siendo = a 11
        valor_despues = cinta1[cochinada:cochinada+2]
        
        


        if(cochinada != 0):
            busquedaG =cinta1.find("11"+estadoC+"1"+letraC+"1")
            busquedaGG = len(estadoC+"1"+letraC+"1")
            ponerQ = busquedaG+busquedaGG+2
            cinta1 = cinta1[:ponerQ]+"q"+cinta1[ponerQ:]
            if(busquedaG == -1):
                print("***********************")
                print("NO ENCONTRÓ EL ESTADO")
                print("***********************")
                cinta3BOOLEAN = False
                
                
            
        else:            
            cinta1 = cinta1[:var]+"q"+cinta1[var:]
            
        #IMPRIME NUEVOS VALORES DE LAS CINTAS
        
        salvacion = cinta1.find("q")
        salva = cinta1[salvacion:]
        num = salva.find("11")
        vida = num+salvacion
        busca = cinta1[salvacion+1:vida]
        busca1 = busca.find("1")
        busca2 = busca[busca1+1:]
        busca3 = busca2.find("1")
        busca4 = busca2[busca3+1:]
        movimiento = busca4

        busca5 = cinta1[salvacion:]
        busca6 = busca5.find("1")
        busca7 = salvacion+busca6+1
        busca8 = cinta1[busca7:]
        busca9 = busca8.find("1")
        
        letra2 = busca8[:busca9]

        cint2Q = cinta2.find("q")
        busca10 = cinta2[cint2Q:]
        busca11 = busca10.find("1")
        
        cambio = busca10[1:busca11]
        posC = cinta2.find(cambio)
        largo = len(cambio)
        cinta2Ch = cinta2[cint2Q+1:]
        largodeuno = cinta2Ch.find("1")
        cambiar = cinta2Ch[:largodeuno]
        cinta2A = cinta2[:cint2Q+1]
        cinta2D = cinta2Ch[len(cambiar):]
        cinta2 = cinta2A+letra2+cinta2D

        
        
        
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
        if(cinta3BOOLEAN == False):
            cinta3 = "q0"

        #REINICIO DE CINTA 1 
        cinta1 = cinta1.replace("q","")
        cinta1 = "q"+cinta1
        
        #MOVIMIENTO DE Q EN CINTA 2
        if(movimiento == "000"):
            encq2 = cinta2.find("q")
            encq3 = cinta2.find("1")
            aaaa = cinta2[encq2:].find("1")
            bbb = aaaa+encq2
            cinta2 = cinta2.replace("q","")
            cinta2 = cinta2[:bbb]+"q"+cinta2[bbb:]
            
        elif(movimiento == "00"):
            numq = cinta2.find("q")
            if(numq == 2):
                cinta2 = cinta2.replace("q","")
                cinta2 = "q"+cinta2
            else:
                conter = 0
                conti = 0
                contai = 0
                contaG = 0
                for x in cinta2:
                    if(x == "1"):
                        conter+=1
                        if(cinta2[conti+1] =="q"):
                            break
                    conti +=1
                cinta2 = cinta2.replace("q","")
                
                
                for z in cinta2:
                    contaG+=1
                    if(z == "1"):
                        contai+=1
                    if(contai == (conter-1)):
                        break
                cinta2 = cinta2[:contaG]+"q"+cinta2[contaG:] 
        else:
            prueba = 1

        
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

def final(cinta1,cinta2,cinta3):
    print("-------------------------------------------------------------------")
    print("Borra la cinta 1 y copia la cinta 2 a la cinta 1")
    cinta1 = cinta2
    print ("Cinta 1")
    print(cinta1)
    print ("Cinta 2")
    print(cinta2)
    print ("Cinta 3")
    print(cinta3)
    print("")
    
    
    
def separar_zonas(cinta):

    global contador
    contador = 0

    global separacion
    separacion = ""

    global previa_zona
    previa_zona = 0
    zonas = []

    #print("la cinta que se ingresa es: ", len(cinta))
    print("****************************************************")
    for i in range(0, len(cinta)):

        if cinta[i] == "1":
            contador += 1
        
        if contador >= 6:
            separacion = cinta[previa_zona:(i+1)]
            
            print(separacion)
            
            zonas.append(separacion)

            #evitamos que el siguiente sea 1
            previa_zona = i + 1
            contador = 0
    print("****************************************************")
    return zonas

class Zona:
    def __init__(self, estado1, letra1, estado2, letra2, movimiento):
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

print("-------------------------------------------------------------------")
print ("Cinta inicial")
print (cinta_inicial)
print("-------------------------------------------------------------------")
cinta1, cinta2, cinta3, cintaz = paso_inicial(cinta_inicial)
cinta1, cinta2, cinta3 = paso3(cinta1, cinta2, cinta3)
cinta1,cinta2,cinta3 = maquina(cinta1,cinta2,cinta3)
final(cinta1,cinta2,cinta3)
#zonas = separar_zonas(cintaz)
#zonas_establecidas = crear_objetos(zonas)
#print("*****************************************************************")
#for x in zonas_establecidas:
#    print(x.estado1, x.letra1, x.estado2, x.letra2, x.movimiento)

