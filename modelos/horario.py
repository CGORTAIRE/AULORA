class Horario:
    """Día y hora asignados a una clase (materia + profesor + aula)."""

    def __init__(self, id_horario, dia_semana, hora_inicio, hora_fin, estado="Libre"):
        self.__id_horario = id_horario
        self.__dia_semana = dia_semana
        self.__hora_inicio = hora_inicio  # formato "HH:MM" (con cero a la izquierda)
        self.__hora_fin = hora_fin
        self.__estado = estado            # "Libre" o "Asignado"
        self.__materia = None
        self.__profesor = None
        self.__aula = None

    # ---------- Getters y setters (encapsulamiento) ----------
    @property
    def id_horario(self):
        return self.__id_horario

    @property
    def dia_semana(self):
        return self.__dia_semana

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @property
    def hora_fin(self):
        return self.__hora_fin

    @property
    def estado(self):
        return self.__estado

    @property
    def materia(self):
        return self.__materia

    @property
    def profesor(self):
        return self.__profesor

    @property
    def aula(self):
        return self.__aula

    # ---------- Métodos del UML ----------
    def registrar(self):
        """Registra el horario en el sistema."""
        print(f"Horario registrado: {self}")

    def actualizar(self, dia_semana=None, hora_inicio=None, hora_fin=None):
        """Actualiza día y horas (solo si el horario aún no está asignado)."""
        if self.__estado == "Asignado":
            raise ValueError("No se puede modificar un horario ya asignado")
        if dia_semana is not None:
            self.__dia_semana = dia_semana
        if hora_inicio is not None:
            self.__hora_inicio = hora_inicio
        if hora_fin is not None:
            self.__hora_fin = hora_fin

    def se_solapa_con(self, otro):
        """True si ambos horarios son el mismo día y sus horas se cruzan."""
        if self.__dia_semana != otro.dia_semana:
            return False
        return self.__hora_inicio < otro.hora_fin and otro.hora_inicio < self.__hora_fin

    def verificar_conflicto(self, profesor, aula):
        """True si asignar este horario a 'profesor' y 'aula' genera conflicto."""
        return not (profesor.consultar_disponibilidad(self)
                    and aula.esta_disponible(self))

    def generar_horario(self, materia, profesor, aula):
        """Asigna materia, profesor y aula a este horario si no hay conflicto.

        Devuelve True si se asignó, False si hubo conflicto.
        """
        if self.verificar_conflicto(profesor, aula):
            return False
        self.__materia = materia
        self.__profesor = profesor
        self.__aula = aula
        self.__estado = "Asignado"
        profesor.agregar_horario(self)
        aula.ocupar(self)
        materia.agregar_horario(self)
        return True

    def __str__(self):
        base = f"{self.__dia_semana} {self.__hora_inicio}-{self.__hora_fin}"
        if self.__materia is not None:
            return (f"{base} | {self.__materia.nombre} | "
                    f"{self.__profesor.nombre} {self.__profesor.apellido} | "
                    f"{self.__aula.nombre}")
        return f"{base} ({self.__estado})"
