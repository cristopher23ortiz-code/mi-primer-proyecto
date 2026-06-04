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

    print("Carreras disponibles:")
    for i, carrera in enumerate(carreras, start=1):
        print(f"{i}. {carrera}")

    opcion = int(input("Seleccione una carrera (0-2): "))

    personas.append((nombre, apellido, edad, opcion))

    estudiantes.append({
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carreras[opcion - 1]
    })

    print("")

        