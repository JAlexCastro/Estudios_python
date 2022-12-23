#def notas(notas_alumnos):
    #return (sum(notas_alumnos) / len(notas_alumnos))

#notas_alumnos =[6, 5, 7]

#promedio = notas(notas_alumnos)

#print("Es es el promedio de el alumno: ", promedio)


#Lista De Estudiantes

Alejandro = [85, 95, 80]
Mirla = [80, 100, 85]

def notas(Estudiante):
    return(sum(Estudiante) / len(Estudiante))

   
promedio_a = notas(Alejandro)
promedio_m = notas(Mirla)


print("El promedio de Alejandro es: ", notas(Alejandro),
"El promedio de Milra es: ", notas(Mirla) )
