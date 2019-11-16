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
    


cinta1, cinta2 = leer_cinta_inicial(cinta_inicial)
print("-------------------------------------------------------------------")
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
#print ("PASO 4")
#alo(cinta1)

