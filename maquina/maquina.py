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
    print(cinta3+"1"+cinta2[:1])
    print(cinta1.find(cinta3+"1"+cinta2[:1]))


def separar_zonas(cinta):

    global contador
    contador = 0

    global separacion
    separacion = ""

    global previa_zona
    previa_zona = 0
    zonas = []

    print("la cinta que se ingresa es: ", len(cinta))

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

    return zonas


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
print("las zonas son:")
print(zonas)

