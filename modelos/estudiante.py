class Estudiante:
    """Estudiante que cursa materias y consulta su horario."""

    def __init__(self, id_estudiante, cedula, nombre, apellido, nivel):
        self.__id_estudiante = id_estudiante
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nivel = nivel
        self.__materias = [] 

   
    @property
    def id_estudiante(self):
        return self.__id_estudiante

    @property
    def cedula(self):
        return self.__cedula

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = valor

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        if not valor:
            raise ValueError("El apellido no puede estar vacío")
        self.__apellido = valor

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, valor):
        self.__nivel = valor

    @property
    def materias(self):
        return list(self.__materias)
    def registrar(self):
        """Registra al estudiante en el sistema."""
        print(f"Estudiante registrado: {self.__nombre} {self.__apellido}")

    def actualizar(self, nombre=None, apellido=None, nivel=None):
        """Actualiza los datos modificables del estudiante."""
        if nombre is not None:
            self.nombre = nombre
        if apellido is not None:
            self.apellido = apellido
        if nivel is not None:
            self.nivel = nivel

    def asignar_materia(self, materia):
        """Matricula al estudiante en una materia, evitando cruces de horario.

        Devuelve True si se asignó, False si ya la tenía o hay cruce.
        """
        if materia in self.__materias:
            return False
        for h_nuevo in materia.horarios:
            for otra in self.__materias:
                for h_otro in otra.horarios:
                    if h_nuevo.se_solapa_con(h_otro):
                        print(f"Cruce: {materia.nombre} choca con {otra.nombre}")
                        return False
        self.__materias.append(materia)
        return True

    def consultar_horario(self):
        """Devuelve los horarios de todas las materias del estudiante.

        (El UML indica 'Horario'; como cursa varias materias, es una lista.)
        """
        horarios = []
        for materia in self.__materias:
            horarios.extend(materia.horarios)
        return horarios

    def __str__(self):
        return f"Estudiante({self.__nombre} {self.__apellido}, nivel {self.__nivel})"
