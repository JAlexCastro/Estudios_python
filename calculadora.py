
primero = input("ingrese el primer número ")

try:
    primero = int(primero)
except:
    primero = "solo ingrese números"

if primero == "solo ingrese números":
    print("Solo puedes ingresar números")
    exit()



segundo = input("ingrese un número ")

try:
    segundo = int(segundo)
except:
    segundo = "solo ingrese números"

if segundo == "solo ingrese números":
    print("Solo puedes ingresar números")
    exit()


#if primero == "solo ingrese números" or segundo == "solo ingrese números":
    #print("Solo puede ingresar números")

simbolo = input("ingrese tipo de operacion ")

if simbolo == "+":
    print("suma ", primero + segundo)
elif simbolo == "-":
        print("resta ", primero - segundo)
elif simbolo == "x":
    print("multiplicación ", primero * segundo)
elif simbolo == "/":
    print("division ", primero / segundo)
else:
    print("HA INGRESADO MAL EL TIPO DE OPERACIÓN ")
