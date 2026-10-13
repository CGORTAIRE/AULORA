# AULORA
AULORA: Plan de organización del equipo
13 oct 2026 · @calros
Responsables
Cada integrante es dueño de una clase y de su archivo; el coordinador cuida que main no se rompa.
Integrante
Clase (archivo)
Relación que debe conectar
Revisa el Pull Request de
Carlos Gortaire (coordinador)
Carrera (carrera.py)
Lista de materias
Daniel Vélez
Luis Arauz
Materia (materia.py)
Su profesor y sus horarios
Carlos Gortaire
Uriel Zambrano
Profesor (profesor.py)
Sus horarios asignados
Luis Arauz
Diana López
Aula (aula.py)
Sus horarios ocupados
Uriel Zambrano
Juan Ávila
Estudiante (estudiante.py)
Su lista de materias
Diana López
Daniel Vélez
Horario (horario.py)
Une materia, profesor y aula
Juan Ávila
El coordinador crea el repositorio en GitHub, invita a los otros cinco y activa la protección de main. Pueden intercambiar clases, pero cada una debe tener un solo dueño.
Acuerdos de grupo
Estos seis acuerdos hacen que las clases encajen entre sí; se firman antes de escribir código.
1. Atributos privados con doble guion bajo (self.__nombre) y acceso con @property.
2. Nombres de métodos en snake_case, tal como están en el UML (consultar_disponibilidad, esta_disponible).
3. Horas como texto "HH:MM" con cero a la izquierda ("08:00") y el día como texto ("Lunes").
4. Un archivo por clase, dentro de la carpeta modelos/.
5. Un archivo __init__.py en modelos/ para poder importar las clases.
6. Cada clase se prueba por separado antes de pedir revisión.
Checklist por clase
Cada dueño marca estos puntos antes de abrir su Pull Request.
[ ] Atributos privados del UML, con sus tipos
[ ] Método __init__
[ ] @property para leer cada atributo, y setter solo donde tenga sentido modificarlo
[ ] Todos los métodos del UML (pueden empezar con pass)
[ ] Método __str__ para poder imprimir el objeto
[ ] Una prueba pequeña que demuestre que funciona
Orden de trabajo
El trabajo va en seis pasos; la columna de fecha la completa el grupo según la entrega del profesor.
Paso
Qué se hace
Quién
Fecha límite
1
Crear el repo, clonarlo y subir un commit de prueba (el nombre en el README)
Todos

2
Escribir cada clase en su rama y abrir el Pull Request
Cada dueño

3
Revisión cruzada de los Pull Requests
Revisor asignado

4
Reunión corta para acordar cómo se conectan las clases
Todos

5
Integrar horario.py, que depende de las demás clases
Daniel Vélez

6
Armar main.py de prueba con objetos de ejemplo
Todos

Flujo de Git
Cada integrante repite estos pasos en su propia rama; ejemplo con la clase Aula.
git checkout main
git pull
git checkout -b feature/clase-aula
# ...trabajar en su archivo...
git add modelos/aula.py
git commit -m "Agrega clase Aula con atributos y metodos"
git push -u origin feature/clase-aula
Después se abre el Pull Request en GitHub hacia main; el revisor asignado lo aprueba y recién ahí se hace el merge.
Reglas del grupo
• Nadie hace push directo a main (se bloquea en Settings → Branches).
• Commits pequeños con mensaje claro, no "cambios" ni "arreglos".
• Si necesitan algo del archivo de otro, se lo piden por el grupo de WhatsApp y no lo editan.
• Antes de cada sesión de trabajo: git pull en main.
• Un conflicto de merge lo resuelven las dos personas afectadas, sin borrar código a ciegas.
