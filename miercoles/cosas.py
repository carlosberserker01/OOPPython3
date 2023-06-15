class Alumno:
    facultad = "FES Aragon"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

    def set_nombre(self, nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, ed):
        if ed >= 8 and ed < 120:
            self.__edad = ed
        else:
            print("La edad no es válida.")
            self.__edad = 0

    def get_edad(self):
        return self.__edad

    def set_carrera(self, carr):
        self.__carrera = carr

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "---------------\nNombre: " + self.__nombre
        cadena = cadena + "\nEdad: " + str(self.__edad)
        cadena = cadena + "\nCarrera: " + str(self.__carrera)
        cadena = cadena + "\n---------------"
        return cadena

    def estudiar(self, horas=1):
        print(f"El alumno {self.__nombre} está estudiando {horas} horas.")


class Perro:
    reino = "Canino"

    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    # Método de acceso get hecho con el decorador property
    @property
    def raza(self):
        return self.__raza

    # Método de acceso set
    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad < 20:
            self.__edad = edad
        else:
            print("La edad no es válida.")
            self.__edad = 0

    @property
    def estatura(self):
        return self.__estatura

    @estatura.setter
    def estatura(self, estatura):
        if estatura > 0.1 and estatura < 1.1:
            self.__estatura = estatura
        else:
            print("La estatura no es válida.")
            self.__estatura = 0

    def __str__(self):
        return f"""
        -------------------------------
        | Raza: {self.__raza}           |
        | Edad: {self.__edad}                     |
        | Estatura: {self.__estatura}              |
        -------------------------------
        """

    @staticmethod
    def es_cachorro(edad):
        return edad < 3

    @staticmethod
    def dormir(veces=5):
        for n in range(veces):
            print(f"Dando vuelta {n+1}.")
        print("Zzzzzzzzz")

    @classmethod
    def perro_grande(cls, est):
        if est > 0.79:
            return cls("", 0, est)
