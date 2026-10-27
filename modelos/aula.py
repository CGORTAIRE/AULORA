class Aula:
    """Espacio físico donde se desarrollan las clases."""

    def __init__(self, id_aula, codigo, nombre, capacidad, tipo):
        self.__id_aula = id_aula
        self.__codigo = codigo
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__tipo = tipo  # por ejemplo: "Teoría" o "Laboratorio"
        self.__horarios_ocupados = []

    # ---------- Getters y setters (encapsulamiento) ----------
    @property
    def id_aula(self):
        return self.__id_aula

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre del aula no puede estar vacío")
        self.__nombre = valor

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if valor <= 0:
            raise ValueError("La capacidad debe ser mayor que 0")
        self.__capacidad = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def horarios_ocupados(self):
        return list(self.__horarios_ocupados)

    # ---------- Métodos del UML ----------
    def registrar(self):
        """Registra el aula en el sistema."""
        print(f"Aula registrada: {self.__codigo} - {self.__nombre} (cap. {self.__capacidad})")

    def actualizar(self, nombre=None, capacidad=None, tipo=None):
        """Actualiza los datos modificables del aula."""
        if nombre is not None:
            self.nombre = nombre
        if capacidad is not None:
            self.capacidad = capacidad
        if tipo is not None:
            self.tipo = tipo

    def esta_disponible(self, horario):
        """True si el aula NO está usada en otra clase que se cruce con 'horario'."""
        for ocupado in self.__horarios_ocupados:
            if ocupado is not horario and ocupado.se_solapa_con(horario):
                return False
        return True

    def tiene_capacidad_para(self, cantidad_estudiantes):
        """True si el aula alcanza para esa cantidad de estudiantes."""
        return self.__capacidad >= cantidad_estudiantes

    # ---------- Apoyo para la asignación ----------
    def ocupar(self, horario):
        if horario not in self.__horarios_ocupados:
            self.__horarios_ocupados.append(horario)

    def __str__(self):
        return f"Aula({self.__codigo}, cap. {self.__capacidad})"
