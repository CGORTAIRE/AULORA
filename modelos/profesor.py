class Profesor:
    """Docente encargado de impartir las materias."""

    def __init__(self, id_profesor, cedula, nombre, apellido):
        self.__id_profesor = id_profesor
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__horarios_asignados = []  # horarios en los que ya da clase

    
    @property
    def id_profesor(self):
        return self.__id_profesor

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
    def horarios_asignados(self):
        return list(self.__horarios_asignados)

    
    def registrar(self):
        """Registra al profesor en el sistema."""
        print(f"Profesor registrado: {self.__nombre} {self.__apellido}")

    def actualizar(self, nombre=None, apellido=None):
        """Actualiza los datos modificables del profesor."""
        if nombre is not None:
            self.nombre = nombre
        if apellido is not None:
            self.apellido = apellido

    def consultar_disponibilidad(self, horario):
        """True si el profesor NO tiene otra clase que se cruce con 'horario'."""
        for asignado in self.__horarios_asignados:
            if asignado is not horario and asignado.se_solapa_con(horario):
                return False
        return True

    
    def agregar_horario(self, horario):
        if horario not in self.__horarios_asignados:
            self.__horarios_asignados.append(horario)

    def __str__(self):
        return f"Profesor({self.__nombre} {self.__apellido})"

