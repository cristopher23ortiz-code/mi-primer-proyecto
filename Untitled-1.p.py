carreras: tuple[str, ...] = (
    "Ingeniería de Software",
    "Contabilidad",
    "Derecho"
)

personas: list[tuple[str, str, int, int]] = [
    # nombre, apellido, edad, carrera
]

estudiantes: list[dict[str, str | int]] = [
    # Lista de diccionario con nombre, apellido, edad, carrera
]

for _ in range(5):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    carrera = int(input("Carrera (0: Ingeniería de Software, 1: Contabilidad, 2: Derecho): "))

    personas.append((nombre, apellido, edad, carrera))

    print("")

for nombre, apellido, edad, carrera in personas:
    estudiantes.append({
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carreras[carrera]
    })

for estudiante in estudiantes:
    print(
        f"{estudiante['nombre']} {estudiante['apellido']} "
        f"tiene {estudiante['edad']} años y estudia "
        f"{estudiante['carrera']}"
    )