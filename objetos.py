#Funcion

def notas(estudiantes):
    return(sum(estudiantes) / len(estudiantes))

#Estudiantes

Alejandro = [90, 85, 80, 100]
Mirla = [94, 85, 88, 86]




promedio = notas(Alejandro)

print("El promedio es: ", promedio)