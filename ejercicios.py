#dato = input("Ingrese datos aqui: ")

lista = ["hola", "buenas tardes", "alejandro", "castro"]

#if lista.count(dato) >  0:
    #print("el dato existe ")
#else:
    #print(" NO está registrado :( ", dato)

#print(input.dato("ingrese el dato"))
#print(input.dato())



primer = input("ingrese un número ")

try:
    primer = "hola"
except:
    primer = "primero no es hola"

if primer == "hola":
    print("Felicitaciones :)")
else:
    print("NO PASASTE :( ")