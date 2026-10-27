class Carrera:

    def __init__(self, id_carrera, codigo, nombre, facultad):
        self.__id_carrera = id_carrera
        self.__codigo = codigo
        self.__nombre = nombre
        self.__facultad = facultad
        self.__materias = [] 


    @property
    def id_carrera(self):
        return self.__id_carrera

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre de la carrera no puede estar vacío")
        self.__nombre = valor

    @property
    def facultad(self):
        return self.__facultad

    @facultad.setter
    def facultad(self, valor):
        self.__facultad = valor

    def registrar(self):
        """Registra la carrera en el sistema."""
        print(f"Carrera registrada: {self.__codigo} - {self.__nombre}")

    def actualizar(self, nombre=None, facultad=None):
        """Actualiza los datos modificables de la carrera."""
        if nombre is not None:
            self.nombre = nombre
        if facultad is not None:
            self.facultad = facultad

    def consultar_materias(self):
        """Devuelve la lista de materias de la carrera."""
        return list(self.__materias)

  
    def agregar_materia(self, materia):
        if materia not in self.__materias:
            self.__materias.append(materia)

    def __str__(self):
        return f"Carrera({self.__codigo}, {self.__nombre})"
