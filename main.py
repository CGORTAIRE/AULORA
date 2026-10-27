from modelos import Carrera, Materia, Profesor, Aula, Estudiante, Horario


def main():
    # --- Datos maestros ---
    carrera = Carrera(1, "TI", "Tecnologías de la Información", "Ciencias de la Vida y Tecnologías")
    poo = Materia(1, "POO", "Programación Orientada a Objetos", 4, 3)
    bd = Materia(2, "BD", "Base de Datos", 4, 3)
    carrera.agregar_materia(poo)
    carrera.agregar_materia(bd)

    ormaza = Profesor(1, "1300000001", "Jharol", "Ormaza")
    poo.asignar_profesor(ormaza)
    bd.asignar_profesor(ormaza)

    aula1 = Aula(1, "A-101", "Aula 101", 35, "Teoría")
    aula2 = Aula(2, "A-102", "Aula 102", 35, "Teoría")

    estudiante = Estudiante(1, "1300000002", "Carlos", "Gortaire", 3)

    for objeto in (carrera, poo, bd, ormaza, aula1, estudiante):
        objeto.registrar()

    # --- Generación de horarios ---
    h1 = Horario(1, "Lunes", "08:00", "10:00")
    h2 = Horario(2, "Lunes", "09:00", "11:00")  # se cruza con h1
    h3 = Horario(3, "Martes", "08:00", "10:00")

    print("\n--- Asignación de horarios ---")
    print("h1 (POO, Ormaza, Aula 101):", h1.generar_horario(poo, ormaza, aula1))
    print("h2 (BD, Ormaza, Aula 102): ", h2.generar_horario(bd, ormaza, aula2),
          "<- False: el profesor ya tiene clase")
    print("h3 (BD, Ormaza, Aula 101): ", h3.generar_horario(bd, ormaza, aula1))

    # --- Estudiante ---
    print("\n--- Matrícula del estudiante ---")
    print("Asignar POO:", estudiante.asignar_materia(poo))
    print("Asignar BD: ", estudiante.asignar_materia(bd))

    print("\n--- Horario del estudiante ---")
    for horario in estudiante.consultar_horario():
        print(horario)

    # --- Encapsulamiento: el atributo privado no es accesible directamente ---
    print("\nCapacidad (por property):", aula1.capacidad)
    try:
        print(aula1.__capacidad)
    except AttributeError:
        print("aula1.__capacidad -> AttributeError (atributo privado)")


if __name__ == "__main__":
    main()
