from cosas import *

def main():
    per1 = Persona("Pedro", 32)
    print(per1)
    print(Persona.descripcion)

    print("-------------herencia alumno-------------")
    al1 = Alumno("José", 19, "2352435234", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("-------------herencia profe-------------")
    profe1 = Profesor("Jesus", 30+16, 324247, "Ingeniería de software")
    print(profe1)
    profe1.dormir()

    print("-------------herencia ayudante profe-------------")
    ayudante = AyudanteProfesor("Adrian", 20, "53453534", "ICO", 2354325, "Ing. de software",4)

    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("P.O.O.")

main()