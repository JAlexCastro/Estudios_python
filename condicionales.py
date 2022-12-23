
#tipos de llaves 

Puerta_1 = ["naranja y cuadrada"]
Puerta_2 = ["amarila y redonda"]
Puerta_3 = ["roja y triangular"]

print(Puerta_1)
print(Puerta_2)
print(Puerta_3)

tienes_llave = input("Tienes llave? ")

if tienes_llave == "si":
    color = input("De que color es la llave? ")
    forma = input("De que forma es la llave? ")

    if tienes_llave == "si" and color == "naranja" and forma == "cuadrada":
        print("Puedes entras a la puerta #1 :)")

    elif tienes_llave == "si" and color == "amarilla" and forma == "redonda":
        print("Puedes entrar por la puerta 2 ;)")

    elif tienes_llave == "si" and color == "roja" and forma == "triangular":
         print("Puedes entrar por la puerta 3 ;)")

#De aquí hacia abajo, no me imprime

if tienes_llave == "no":
    print("Debes tener una llave para participar")

else:
    print("Debes tener 1 de los 3 tipos de llaves para entrar")

print("Fin")