class Materia:
    """Asignatura que forma parte de una carrera y de un nivel académico."""

    def __init__(self, id_materia, codigo, nombre, creditos, nivel):
        self.__id_materia = id_materia
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__nivel = nivel
        self.__profesor = None   # relación "es impartida por"
        self.__horarios = []     # relación "se programa en"

    # ---------- Getters y setters (encapsulamiento) ----------
    @property
    def id_materia(self):
        return self.__id_materia

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre de la materia no puede estar vacío")
        self.__nombre = valor

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, valor):
        if valor <= 0:
            raise ValueError("Los créditos deben ser mayores que 0")
        self.__creditos = valor

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, valor):
        self.__nivel = valor

    @property
    def profesor(self):
        return self.__profesor

    @property
    def horarios(self):
        return list(self.__horarios)

    # ---------- Métodos del UML ----------
    def registrar(self):
        """Registra la materia en el sistema."""
        print(f"Materia registrada: {self.__codigo} - {self.__nombre}")

    def actualizar(self, nombre=None, creditos=None, nivel=None):
        """Actualiza los datos modificables de la materia."""
        if nombre is not None:
            self.nombre = nombre
        if creditos is not None:
            self.creditos = creditos
        if nivel is not None:
            self.nivel = nivel

    def asignar_profesor(self, profesor):
        """Define qué profesor imparte esta materia."""
        self.__profesor = profesor

    # ---------- Apoyo a la relación "se programa en" ----------
    def agregar_horario(self, horario):
        if horario not in self.__horarios:
            self.__horarios.append(horario)

    def __str__(self):
        return f"Materia({self.__codigo}, {self.__nombre}, nivel {self.__nivel})"
