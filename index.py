if 5 > 3:
    print("5 en mayor a 3")



mi_lista=["nombre", "Apellido"]



if mi_lista == "nombre":
    print("funciona")

else:
    print("no funciona")

mi_lista.append("Hola")
mi_lista.insert(0, "Buenos")
mi_lista.remove("Hola")

print(mi_lista[:])





diccionario = {
    "nombre" : "alex",
    "apellido" : "castro",
    "edad" : 21,
}




#print(diccionario.popitem())

#DICCIONARIOS ANIDADOS
mascotas = {
    
    "fluffy" : { 
        "nombre" : "fluffy",
        "edad" : 4
    },

    "manba" : {
        "nombre" : "black mamba",
        "edad" : 12
     } 
}


#DICCIONARIO SIMPLE
fluffy = { 
      "nombre" : "fluffy",
      "edad" : 4
}


manba = {


        "nombre" : "black mamba",
        "edad" : 12
     } 


#DICCIONARIO CON MÉTODO

diccinario_1 =dict({"nombre" : "Felipe", "Apellido" : "Lara"})

#print(diccinario_1)


