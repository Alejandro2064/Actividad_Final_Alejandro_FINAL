import string
import os

print( "\033[H\033[J")

def alum_alfab(lista):   # Mostrar la lista (alfabética) de alumnos.
    nom_alfab = curso
    nom_alfab.sort()
    for i in nom_alfab:
        print(i[0])
    return i

def alum_notas_alfab(lista):  # Mostrar la lista (alfabética) de alumnos con sus notas.
    nom_alfab = curso
    nom_alfab.sort()
    for i in nom_alfab:
        print(i)
    return i 

def alum_prom_alfab(lista): # Mostrar la lista (alfabética) de alumnos con su promedios
    f = curso
    f.sort()
    for i in curso:
        print(" El Alumno/a", i[0], "\t", end=" ")
        suma = 0
        f = 1
        while f < len(i):
            suma = suma + i[f]
            f = f + 1
        promedio = suma / (len(i)-1)
        print ("promedio de: ", round(promedio, 1))

def nota_media_alum(lista):  # Mostrar la nota media de todos los alumnos.
    suma1 = 0
    for i in curso: 
        suma = 0
        f = 1
        while f < len(i):
            suma = suma + i[f]
            f = f + 1
        promedio = suma / (len(i)-1)
        suma1 = suma1 + promedio
        promedio1 = suma1/20
    print ("La nota media de todos los alumnos es:", round(promedio1,1))

def nota_media_alum_aprob(lista):  # Mostrar la nota media de los alumnos aprobados
    suma1 = 0
    j = 0
    for i in curso: 
        suma = 0
        f = 1
        while f < len(i):
            suma = suma + i[f]
            f = f + 1
        promedio = suma / (len(i)-1)
        if promedio >= 7:
            j = j + 1
            suma1 = suma1 + promedio
            promedio1 = suma1/j
    print ("La nota media de todos los alumnos aprobados con 7 o mas es de:", round(promedio1,1)) 

def nota_media_alum_desaprob(lista):  # Mostrar la nota media de los alumnos desaprobados
    suma1 = 0
    j = 0
    for i in curso: 
        suma = 0
        f = 1
        while f < len(i):
            suma = suma + i[f]
            f = f + 1
        promedio = suma / (len(i)-1)
        if promedio < 7:
            j = j + 1
            suma1 = suma1 + promedio
            promedio2 = suma1/j
    print ("La nota media de todos los alumnos desaprobados con menos de 7 es de:", round(promedio2,1))    

curso = [
        ["Ocana, Juan", 8, 6, 9, 5],
        ["Pérez, Ana", 4, 6, 8, 5],
        ["Albornoz, María", 9, 9, 8, 10, 7],
        ["Sosa, Jorge", 7, 6, 5, 4, 6, 8],
        ["Amarilla, Eduardo", 6, 5, 3, 4],
        ["Blanco, Fernanda", 7, 8, 6, 5],
        ["Ercilla, Nahuel", 8, 9, 10, 7, 8, 8],
        ["Polanca, Zoe", 7, 4, 3, 9],
        ["Castro, Yamila", 6, 5, 8, 8, 7],
        ["Brito, Susana", 9, 10, 8, 9, 10],
        ["Paredes, Facundo", 6, 5, 9, 4, 8],
        ["Caputo, Silvia", 8, 5, 9, 4],
        ["Rojas, Viviana", 7, 8, 9, 6, 6],
        ["Cillo, Valeria", 4, 3, 5, 7],
        ["Nieva, Cristina", 5, 7, 6, 6, 8],
        ["Echeverri, Silvia",7, 6, 5],
        ["Salas, Silvia", 8, 7, 5, 4],
        ["Bustos, Facundo", 5, 4, 3, 6, 4],
        ["Mansilla, Romina", 8, 9, 10, 7, 9, 8],
        ["Paredes, Gustavo", 5, 4, 3, 7, 6],
        ]


print(" - Ingrese una opcion:")
print("a) Para mostrar la lista (alfabética) de alumnos.")
print("b) Para mostrar la lista (alfabética) de alumnos con sus notas.")
print("c) Para mostrar la lista (alfabética) de alumnos con su promedios.")
print("d) Para mostrar la nota media de todos los alumnos.")
print("e) Para mostrar la nota media de los alumnos aprobados.")
print("f) Para mostrar la nota media de los alumnos suspendidos.")
print("g) Para Salir del programa")

op = "a"
while op != "g":
    print(" ")
    print("******************************")
    print(" ")
    op = str (input("Ingrese la opcion // v) para volver al menú // : "))

    cls = lambda:os.system('cls')
    cls()

    if op == "a":   
        alum_alfab(curso)
    elif op == "b":
        alum_notas_alfab(curso)
    elif op == "c":
        alum_prom_alfab(curso)
    elif op == "d":
        nota_media_alum(curso)
    elif op == "e":
        nota_media_alum_aprob(curso)
    elif op == "f":
        nota_media_alum_desaprob(curso)
    elif op == "g":
        print("Fin del programa")
    elif op == "v":
        print(" - Ingrese una opcion:")
        print("a) Para mostrar la lista (alfabética) de alumnos.")
        print("b) Para mostrar la lista (alfabética) de alumnos con sus notas.")
        print("c) Para mostrar la lista (alfabética) de alumnos con su promedios.")
        print("d) Para mostrar la nota media de todos los alumnos.")
        print("e) Para mostrar la nota media de los alumnos aprobados.")
        print("f) Para mostrar la nota media de los alumnos suspendidos.")
        print("g) Para Salir del programa")
    else:
        print ("*** Opcion incorrecta ***")
        print (" ")
        print(" - Ingrese una opcion:")
        print("a) Para mostrar la lista (alfabética) de alumnos.")
        print("b) Para mostrar la lista (alfabética) de alumnos con sus notas.")
        print("c) Para mostrar la lista (alfabética) de alumnos con su promedios.")
        print("d) Para mostrar la nota media de todos los alumnos.")
        print("e) Para mostrar la nota media de los alumnos aprobados.")
        print("f) Para mostrar la nota media de los alumnos suspendidos.")
        print("g) Para Salir del programa")