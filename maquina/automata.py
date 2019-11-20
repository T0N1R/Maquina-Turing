"""
    Logica matematica
    Proyecto Final - Maquina de Turing
    20/11/2019
    Gustavo de Leon #17085
    Antonio Reyes #17273
"""


f = open("MT1.txt")

cinta_inicial = ""

for line in f:
    cinta_inicial = cinta_inicial + line

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


def separar_segmentos(cinta):
    secuencia_inicial = ""
    secuencia_2 = ""
    secuencia_3 = ""

    nueva_secuencia_2 = ""

    for i in range(0, len(cinta)):
        if cinta[i] == "1":
            secuencia_inicial = cinta[ 0 : i ]
            secuencia_2 = cinta[ ( i + 1 ) : len(cinta) ]
            break

    for i in range(0, len(cinta)):
        if cinta[i] == "1":
            if cinta[ i + 1 ] == "1":
                if cinta[ i + 2 ] == "1":
                    secuencia_3 =  cinta[ (i + 3) : len(cinta)]


    for i in range(0, len(secuencia_2)):
        if cinta[i] == "1":
            if cinta[ i + 1 ] == "1":
                if cinta[ i + 2 ] == "1":
                    nueva_secuencia_2 = secuencia_2[ 0 : (i - 1) ]
    

    
    zonas = separar_zonas(nueva_secuencia_2)

    zonas_establecidas = crear_objetos(zonas)

    print("**************************************************")
    print(" --- ESTADO INICIAL ---  ")
    print(secuencia_inicial)
    print("**************************************************")
    print(" --- CINTA CON ZONAS --- ")
    print(nueva_secuencia_2)
    print(" --- CINTA SEPARADA EN ZONAS --- ")

    correcto_secuencia_2 = True

    for x in zonas_establecidas:
        print(x.estado1, x.letra1, x.estado2, x.letra2, x.movimiento)

    for x in zonas_establecidas:
        if "1" in x.estado1:
            correcto_secuencia_2 = False

        if "1" in x.letra1:
            correcto_secuencia_2 = False

        if "1" in x.estado2:
            correcto_secuencia_2 = False

        if "1" in x.letra2:
            correcto_secuencia_2 = False

        if len(x.movimiento) > 3:
            correcto_secuencia_2 = False

    print("")
    print("[[  Validez de esta cadena: ", correcto_secuencia_2, "  ]]")

    print("**************************************************")
    print(" --- CINTA CON LETRAS --- ")

    print(secuencia_3)

    correcto_secuencia_3 = True

    if "11" in secuencia_3:
        correcto_secuencia_3 = False

    print("[[  Validez de esta cadena: ", correcto_secuencia_3, "  ]]")


separar_segmentos(cinta_inicial)
