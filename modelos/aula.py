class Persona:
    def __init__(self, cedula: str, nombre: str, apellido: str):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar(self):
        return f"{self.nombre} {self.apellido} - {self.cedula}"

class RecursoAcademico:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre

class Carrera:
    def __init__(self, idCarrera: int, codigo: str, nombre: str, facultad: str):
        self.idCarrera = idCarrera
        self.codigo = codigo
        self.nombre = nombre
        self.facultad = facultad

    def registrar(self): print(f"Carrera {self.nombre} registrada")
    def actualizar(self): print(f"Carrera {self.nombre} actualizada")
    def consultarMaterias(self): return []

class Materia(RecursoAcademico):
    def __init__(self, idMateria: int, codigo: str, nombre: str, creditos: int, nivel: int):
        super().__init__(codigo, nombre) # 1.4 super()
        self.idMateria = idMateria
        self.creditos = creditos
        self.nivel = nivel

    def registrar(self): print(f"Materia {self.nombre} registrada")
    def actualizar(self): print(f"Materia {self.nombre} actualizada")
    def asignarProfesor(self, profesor: 'Profesor'): print(f"Profesor {profesor.nombre} asignado a {self.nombre}")


class Profesor(Persona):
    def __init__(self, idProfesor: int, cedula: str, nombre: str, apellido: str):
        super().__init__(cedula, nombre, apellido)
        self.idProfesor = idProfesor

    def registrar(self): print(f"Profesor {self.nombre} registrado")
    def actualizar(self): print(f"Profesor actualizado")
    def consultarDisponibilidad(self): return True


class Estudiante(Persona):
    def __init__(self, idEstudiante: int, cedula: str, nombre: str, apellido: str, nivel: int):
        super().__init__(cedula, nombre, apellido)
        self.idEstudiante = idEstudiante
        self.nivel = nivel

    def registrar(self): print(f"Estudiante {self.nombre} registrado")
    def actualizar(self): print(f"Estudiante actualizado")
    def asignarMateria(self, materia: Materia): print(f"Materia {materia.nombre} asignada")
    def consultarHorario(self): return None

class Aula(RecursoAcademico):
    def __init__(self, idAula: int, codigo: str, nombre: str, capacidad: int, tipo: str):
        super().__init__(codigo, nombre)
        self.idAula = idAula
        self.capacidad = capacidad
        self.tipo = tipo

    def registrar(self): print(f"Aula {self.nombre} registrada")
    def actualizar(self): print(f"Aula actualizada")
    def estaDisponible(self): return True

class Horario:
    def __init__(self, idHorario: int, diaSemana: str, horaInicio: str, horaFin: str, estado: str):
        self.idHorario = idHorario
        self.diaSemana = diaSemana
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.estado = estado

    def registrar(self): print(f"Horario {self.diaSemana} registrado")
    def actualizar(self): print(f"Horario actualizado")
    def verificarConflicto(self): return False
    def generarHorario(self): print("Generando horario...")

class ProfesorTitular(Profesor):
    def __init__(self, idProfesor: int, cedula: str, nombre: str, apellido: str, categoria: str):
        super().__init__(idProfesor, cedula, nombre, apellido)
        self.categoria = categoria

# Persona -> Estudiante -> EstudianteBecado
class EstudianteBecado(Estudiante):
    def __init__(self, idEstudiante: int, cedula: str, nombre: str, apellido: str, nivel: int, tipo_beca: str):
        super().__init__(idEstudiante, cedula, nombre, apellido, nivel)
        self.tipo_beca = tipo_beca


class HorarioPresencial(Horario, Aula):
    def __init__(self, idHorario, diaSemana, horaInicio, horaFin, estado, idAula, codigoAula, nombreAula, capacidad, tipoAula, materia: Materia, profesor: Profesor):
        Horario.__init__(self, idHorario, diaSemana, horaInicio, horaFin, estado)
        Aula.__init__(self, idAula, codigoAula, nombreAula, capacidad, tipoAula)
        self.materia = materia
        self.profesor = profesor

    def detalle_completo(self):
        return f"{self.diaSemana} {self.horaInicio}-{self.horaFin} | {self.materia.nombre} con {self.profesor.nombre} en {self.nombre} ({self.tipo})"


class AyudanteCatedra(Estudiante, Profesor):
    def __init__(self, idEstudiante, idProfesor, cedula, nombre, apellido, nivel, materia_asistida):
        # En herencia múltiple debemos llamar ambos init
        Estudiante.__init__(self, idEstudiante, cedula, nombre, apellido, nivel)
        self.idProfesor = idProfesor
        self.materia_asistida = materia_asistida

