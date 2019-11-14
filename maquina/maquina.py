f = open("MT1.txt")

cinta_inicial = ""

cinta1 = ""
cinta2 = ""
cinta3 = ""

for line in f:
    cinta_inicial = cinta_inicial + line

def leer_cinta_inicial(cinta):
    contador = 0
    for x in cinta:
        if (x == "1"):
            if (cinta[contador + 1] == "1"):
                if (cinta[contador + 2] == "1"):
                    cinta1 = cinta[:contador+3]
                    cinta2 = cinta[contador+2:]

        contador+=1

    return cinta1, cinta2

cinta1, cinta2 = leer_cinta_inicial(cinta_inicial)

print(cinta1)
print("------------------------------------------")
print(cinta2)